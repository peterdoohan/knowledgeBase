# **Successor Features for Transfer in Reinforcement Learning** 

**André Barreto, Will Dabney, Rémi Munos, Jonathan J. Hunt, Tom Schaul** , **Hado van Hasselt** , **David Silver** 

```
{andrebarreto,wdabney,munos,jjhunt,schaul,hado,davidsilver}@google.com
```

DeepMind 

## **Abstract** 

Transfer in reinforcement learning refers to the notion that generalization should occur not only within a task but also across tasks. We propose a transfer framework for the scenario where the reward function changes between tasks but the environment’s dynamics remain the same. Our approach rests on two key ideas: _successor features_ , a value function representation that decouples the dynamics of the environment from the rewards, and _generalized policy improvement_ , a generalization of dynamic programming’s policy improvement operation that considers a set of policies rather than a single one. Put together, the two ideas lead to an approach that integrates seamlessly within the reinforcement learning framework and allows the free exchange of information across tasks. The proposed method also provides performance guarantees for the transferred policy even before any learning has taken place. We derive two theorems that set our approach in firm theoretical ground and present experiments that show that it successfully promotes transfer in practice, significantly outperforming alternative methods in a sequence of navigation tasks and in the control of a simulated robotic arm. 

## **1 Introduction** 

Reinforcement learning (RL) provides a framework for the development of situated agents that learn how to behave while interacting with the environment [21]. The basic RL loop is defined in an abstract way so as to capture only the essential aspects of this interaction: an agent receives observations and selects actions to maximize a reward signal. This setup is generic enough to describe tasks of different levels of complexity that may unroll at distinct time scales. For example, in the task of driving a car, an action can be to turn the wheel, make a right turn, or drive to a given location. 

Clearly, from the point of view of the designer, it is desirable to describe a task at the highest level of abstraction possible. However, by doing so one may overlook behavioral patterns and inadvertently make the task more difficult than it really is. The task of driving to a location clearly encompasses the subtask of making a right turn, which in turn encompasses the action of turning the wheel. In learning how to drive an agent should be able to identify and exploit such interdependencies. More generally, the agent should be able to break a task into smaller subtasks and use knowledge accumulated in any subset of those to speed up learning in related tasks. This process of leveraging knowledge acquired in one task to improve performance on other tasks is called _transfer_ [25, 11]. 

In this paper we look at one specific type of transfer, namely, when subtasks correspond to different reward functions defined in the same environment. This setup is flexible enough to allow transfer to happen at different levels. In particular, by appropriately defining the rewards one can induce different task decompositions. For instance, the type of hierarchical decomposition involved in the driving example above can be induced by changing the frequency at which rewards are delivered: 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA. 

a positive reinforcement can be given after each maneuver that is well executed or only at the final destination. Obviously, one can also decompose a task into subtasks that are independent of each other or whose dependency is strictly temporal (that is, when tasks must be executed in a certain order but no single task is clearly “contained” within another). 

The types of task decomposition discussed above potentially allow the agent to tackle more complex problems than would be possible were the tasks modeled as a single monolithic challenge. However, in order to apply this divide-and-conquer strategy to its full extent the agent should have an explicit mechanism to promote transfer between tasks. Ideally, we want a transfer approach to have two important properties. First, the flow of information between tasks should not be dictated by a rigid diagram that reflects the relationship between the tasks themselves, such as hierarchical or temporal dependencies. On the contrary, information should be exchanged across tasks whenever useful. Second, rather than being posed as a separate problem, transfer should be integrated into the RL framework as much as possible, preferably in a way that is almost transparent to the agent. 

In this paper we propose an approach for transfer that has the two properties above. Our method builds on two conceptual pillars that complement each other. The first is a generalization of Dayan’s [7] _successor representation_ . As the name suggests, in this representation scheme each state is described by a prediction about the future occurrence of all states under a fixed policy. We present a generalization of Dayan’s idea which extends the original scheme to continuous spaces and also facilitates the use of approximation. We call the resulting scheme _successor features_ . As will be shown, successor features lead to a representation of the value function that naturally decouples the dynamics of the environment from the rewards, which makes them particularly suitable for transfer. 

The second pillar of our framework is a generalization of Bellman’s [3] classic policy improvement theorem that extends the original result from one to multiple decision policies. This novel result shows how knowledge about a set of tasks can be transferred to a new task in a way that is completely integrated within RL. It also provides performance guarantees on the new task _before_ any learning has taken place, which opens up the possibility of constructing a library of “skills” that can be reused to solve previously unseen tasks. In addition, we present a theorem that formalizes the notion that an agent should be able to perform well on a task if it has seen a similar task before—something clearly desirable in the context of transfer. Combined, the two results above not only set our approach in firm ground but also outline the mechanics of how to actually implement transfer. We build on this knowledge to propose a concrete method and evaluate it in two environments, one encompassing a sequence of navigation tasks and the other involving the control of a simulated two-joint robotic arm. 

## **2 Background and problem formulation** 

As usual, we assume that the interaction between agent and environment can be modeled as a _Markov decision process_ (MDP, Puterman, [19]). An MDP is defined as a tuple _M ≡_ ( _S, A, p, R, γ_ ). The sets _S_ and _A_ are the state and action spaces, respectively; here we assume that _S_ and _A_ are finite whenever such an assumption facilitates the presentation, but most of the ideas readily extend to continuous spaces. For each _s ∈S_ and _a ∈A_ the function _p_ ( _·|s, a_ ) gives the next-state distribution upon taking action _a_ in state _s_ . We will often refer to _p_ ( _·|s, a_ ) as the _dynamics_ of the MDP. The reward received at transition _s −→a s′_ is given by the random variable _R_ ( _s, a, s′_ ); usually one is interested in the expected value of this variable, which we will denote by _r_ ( _s, a, s[′]_ ) or by _r_ ( _s, a_ ) = E _S′∼p_ ( _·|s,a_ )[ _r_ ( _s, a, S[′]_ )]. The discount factor _γ ∈_ [0 _,_ 1) gives smaller weights to future rewards. 

The objective of the agent in RL is to find a policy _π_ —a mapping from states to actions—that maximizes the expected discounted sum of rewards, also called the _return Gt_ =[�] _[∞] i_ =0 _[γ][i][R][t]_[+] _[i]_[+1] _[,]_ where _Rt_ = _R_ ( _St, At, St_ +1). One way to address this problem is to use methods derived from _dynamic programming_ (DP), which heavily rely on the concept of a _value function_ [19]. The _action-value function_ of a policy _π_ is defined as 

_Q[π]_ ( _s, a_ ) _≡_ E _[π]_ [ _Gt | St_ = _s, At_ = _a_ ] _,_ (1) 

where E _[π]_ [ _·_ ] denotes expected value when following policy _π_ . Once the action-value function of a particular policy _π_ is known, we can derive a new policy _π[′]_ which is _greedy_ with respect to _Q[π]_ ( _s, a_ ), that is, _π[′]_ ( _s_ ) _∈_ argmax _aQ[π]_ ( _s, a_ ). Policy _π[′]_ is guaranteed to be at least as good as (if not better than) policy _π_ . The computation of _Q[π]_ ( _s, a_ ) and _π[′]_ , called _policy evaluation_ and _policy improvement_ , define the basic mechanics of RL algorithms based on DP; under certain conditions their successive application leads to an optimal policy _π[∗]_ that maximizes the expected return from every _s ∈S_ [21]. 

2 

In this paper we are interested in the problem of _transfer_ , which we define as follows. Let _T , T[′]_ be two sets of tasks such that _T[′] ⊂T_ , and let _t_ be any task. Then there is _transfer_ if, after training on _T_ , the agent always performs as well or better on task _t_ than if only trained on _T[′]_ . Note that _T[′]_ can be the empty set. In this paper a task will be defined as a specific instantiation of the reward function _R_ ( _s, a, s[′]_ ) for a given MDP. In Section 4 we will revisit this definition and make it more formal. 

## **3 Successor features** 

In this section we present the concept that will serve as a cornerstone for the rest of the paper. We start by presenting a simple reward model and then show how it naturally leads to a generalization of Dayan’s [7] successor representation (SR). 

Suppose that the expected one-step reward associated with transition ( _s, a, s[′]_ ) can be computed as 

**==> picture [255 x 12] intentionally omitted <==**

where _**φ**_ ( _s, a, s[′]_ ) _∈_ R _[d]_ are features of ( _s, a, s[′]_ ) and **w** _∈_ R _[d]_ are weights. Expression (2) is not restrictive because we are not making any assumptions about _**φ**_ ( _s, a, s[′]_ ): if we have _φi_ ( _s, a, s[′]_ ) = _r_ ( _s, a, s[′]_ ) for some _i_ , for example, we can clearly recover any reward function exactly. To simplify the notation, let _**φ** t_ = _**φ**_ ( _st, at, st_ +1). Then, by simply rewriting the definition of the action-value function in (1) we have 

**==> picture [341 x 52] intentionally omitted <==**

The decomposition (3) has appeared before in the literature under different names and interpretations, as discussed in Section 6. Since here we propose to look at (3) as an extension of Dayan’s [7] SR, we call _**ψ**[π]_ ( _s, a_ ) the _successor features_ (SFs) of ( _s, a_ ) under policy _π_ . 

The i[th] component of _**ψ**[π]_ ( _s, a_ ) gives the expected discounted sum of _φi_ when following policy _π_ starting from ( _s, a_ ). In the particular case where _S_ and _A_ are finite and _**φ**_ is a tabular representation of _S × A × S_ —that is, _**φ**_ ( _s, a, s[′]_ ) is a one-hot vector in R _[|S|]_[2] _[|A|]_ — _**ψ**[π]_ ( _s, a_ ) is the discounted sum of occurrences, under _π_ , of each possible transition. This is essentially the concept of SR extended from the space _S_ to the set _S × A × S_ [7]. 

One of the contributions of this paper is precisely to generalize SR to be used with function approximation, but the exercise of deriving the concept as above provides insights already in the tabular case. To see this, note that in the tabular case the entries of **w** _∈_ R _[|S|]_[2] _[|A|]_ are the function _r_ ( _s, a, s[′]_ ) and suppose that _r_ ( _s, a, s[′]_ ) = 0 in only a small subset _W ⊂S × A × S_ . From (2) and (3), it is clear that the cardinality of _W_ , and not of _S × A × S_ , is what effectively defines the dimension of the representation _**ψ**[π]_ , since there is no point in having _d > |W|_ . Although this fact is hinted at by Dayan [7], it becomes more apparent when we look at SR as a particular case of SFs. 

SFs extend SR in two other ways. First, the concept readily applies to continuous state and action spaces without any modification. Second, by explicitly casting (2) and (3) as inner products involving feature vectors, SFs make it evident how to incorporate function approximation: as will be shown, these vectors can be learned from data. 

The representation in (3) requires two components to be learned, **w** and _**ψ**[π]_ . Since the latter is thethatexpectedapproximatingdiscounted _r_ ( _s, a, s_ sum _[′]_ ) of _≈_ _**φφ**_ (under _s, a, sπ[′]_ ), _[⊤]_ we **w** ˜ ismusta supervisedeither be givenlearning _**φ**_ orproblem,learn it soas wewell.canNoteuse well-understood techniques from the field to learn **w** ˜ (and potentially _**φ**_[˜] , too) [9]. As for _**ψ**[π]_ , we note that 

**==> picture [327 x 12] intentionally omitted <==**

that is, SFs satisfy a Bellman equation in which _φi_ play the role of rewards—something also noted by Dayan [7] regarding SR. Therefore, in principle _any_ RL method can be used to compute _**ψ**[π]_ [24]. 

The SFs _**ψ**[π]_ summarize the dynamics induced by _π_ in a given environment. As shown in (3), this allows for a modular representation of _Q[π]_ in which the MDP’s dynamics are decoupled from its 

3 

rewards, which are captured by the weights **w** . One potential benefit of having such a decoupled representation is that only the relevant module must be relearned when either the dynamics or the reward changes, which may serve as an argument in favor of adopting SFs as a general approximation scheme for RL. However, in this paper we focus on a scenario where the decoupled value-function approximation provided by SFs is exploited to its full extent, as we discuss next. 

## **4 Transfer via successor features** 

We now return to the discussion about transfer in RL. As described, we are interested in the scenario where all components of an MDP are fixed, except for the reward function. One way to formalize this model is through (2): if we suppose that _**φ** ∈_ R _[d]_ is fixed, any **w** _∈_ R _[d]_ gives rise to a new MDP. Based on this observation, we define 

**==> picture [333 x 13] intentionally omitted <==**

that is, _M[φ]_ is the set of MDPs induced by _**φ**_ through all possible instantiations of **w** . Since what differentiates the MDPs in _M[φ]_ is essentially the agent’s goal, we will refer to _Mi ∈M[φ]_ as a _task_ . The assumption is that we are interested in solving (a subset of) the tasks in the environment _M[φ]_ . 

Definition (5) is a natural way of modeling some scenarios of interest. Think, for example, how the desirability of water or food changes depending on whether an animal is thirsty or hungry. One way to model this type of preference shifting is to suppose that the vector **w** appearing in (2) reflects the taste of the agent at any given point in time [17]. Further in the paper we will present experiments that reflect this scenario. For another illustrative example, imagine that the agent’s goal is to produce and sell a combination of goods whose production line is relatively stable but whose prices vary considerably over time. In this case updating the price of the products corresponds to picking a new **w** . A slightly different way of motivating (5) is to suppose that the environment itself is changing, that is, the element **w** _i_ indicates not only desirability, but also availability, of feature _φi_ . 

In the examples above it is desirable for the agent to build on previous experience to improve its performance on a new setup. More concretely, if the agent knows good policies for the set of tasks _M ≡{M_ 1 _, M_ 2 _, ..., Mn}_ , with _Mi ∈M[φ]_ , it should be able to leverage this knowledge to improve its behavior on a new task _Mn_ +1—that is, it should perform better than it would had it been exposed to only a subset of the original tasks, _M[′] ⊂M_ . We can assess the performance of an agent on task _Mn_ +1 based on the value function of the policy followed after **w** _n_ +1 has become available but _before_ any policy improvement has taken place in _Mn_ +1.[1] More precisely, suppose that an agent has been exposed to each one of the tasks _Mi ∈M[′]_ . Based on this experience, and on the new **w** _n_ +1, the agent computes a policy _π[′]_ that will define its initial behavior in _Mn_ +1. Now, if we repeat the experience replacing _M[′]_ with _M_ , the resulting policy _π_ should be such that _Q[π]_ ( _s, a_ ) _≥ Q[π][′]_ ( _s, a_ ) for all ( _s, a_ ) _∈S × A_ . 

Now that our setup is clear we can start to describe our solution for the transfer problem discussed above. We do so in two stages. First, we present a generalization of DP’s notion of policy improvement whose interest may go beyond the current work. We then show how SFs can be used to implement this generalized form of policy improvement in an efficient and elegant way. 

## **4.1 Generalized policy improvement** 

One of the fundamental results in RL is Bellman’s [3] _policy improvement theorem_ . In essence, the theorem states that acting greedily with respect to a policy’s value function gives rise to another policy whose performance is no worse than the former’s. This is the driving force behind DP, and most RL algorithms that compute a value function are exploiting Bellman’s result in one way or another. 

In this section we extend the policy improvement theorem to the scenario where the new policy is to be computed based on the value functions of a _set_ of policies. We show that this extension can be done in a natural way, by acting greedily with respect to the maximum over the value functions available. Our result is summarized in the theorem below. 

1 Of course **w** _n_ +1 can, and will be, learned, as discussed in Section 4.2 and illustrated in Section 5. Here we assume that **w** _n_ +1 is given to make our performance criterion clear. 

4 

**Theorem 1.** ˜ ˜ **(Generalized Policy Improvement)** ˜ _Let π_ 1 _, π_ 2 _, ..., πn be n decision policies and let_ 1 2 _n Q[π] , Q[π] , ..., Q[π] be approximations of their respective action-value functions such that_ 

**==> picture [398 x 92] intentionally omitted <==**

The proofs of our theoretical results are in the supplementary material. As one can see, our theorem covers the case where the policies’ value functions are not computed exactly, either because function approximation is used or because some exact algorithm has not be run to completion. This error is captured by _ϵ_ in (6), which re-appears as a penalty term in the lower bound (8). Such a penalty is inherent to the presence of approximation in RL, and in fact it is identical to the penalty incurred in the single-policy case (see _e.g._ Bertsekas and Tsitsiklis’s Proposition 6.1 [5]). 

In order to contextualize generalized policy improvement (GPI) within the broader scenario of DP, suppose for a moment that _ϵ_ = 0. In this case Theorem 1 states that _π_ will perform no worse than _all_ of the policies _π_ 1, _π_ 2 _, ..., πn_ . This is interesting because in general max _i Q[π][i]_ —the function used to induce _π_ —is not the value function of any particular policy. It is not difficult to see that _π_ will be strictly better than all previous policies if no single policy dominates all other policies, that is, if argmax _i_ max _a Q_[˜] _[π][i]_ ( _s, a_ ) _∩_ argmax _i_ max _a Q_[˜] _[π][i]_ ( _s[′] , a_ ) = _∅_ for some _s, s[′] ∈S_ . If one policy does dominate all others, GPI reduces to the original policy improvement theorem. 

If we consider the usual DP loop, in which policies of increasing performance are computed in sequence, our result is not of much use because the most recent policy will always dominate all others. Another way of putting it is to say that after Theorem 1 is applied once adding the resulting _π_ to the set _{π_ 1, _π_ 2 _, ..., πn}_ will reduce the next improvement step to standard policy improvement, and thus the policies _π_ 1, _π_ 2 _, ..., πn_ can be simply discarded. There are however two situations in which our result may be of interest. One is when we have many policies _πi_ being evaluated in parallel. In this case GPI provides a principled strategy for combining these policies. The other situation in which our result may be useful is when the underlying MDP changes, as we discuss next. 

## **4.2 Generalized policy improvement with successor features** 

We start this section by extending our notation slightly to make it easier to refer to the quantities involved in transfer learning. Let _Mi_ be a task in _M[φ]_ defined by **w** _i ∈_ R _[d]_ . We will use _πi[∗]_[to refer] to an optimal policy of MDP _Mi_ and use _Qiπi[∗]_ to refer to its value function. The value function of _πi[∗]_ when executed in _Mj ∈M[φ]_ will be denoted by _Qπj i[∗]_[.] 

Suppose now that an agent has computed optimal policies for the tasks _M_ 1 _, M_ 2 _, ..., Mn ∈M[φ]_ . Suppose further that when presented with a new task _Mn_ +1 the agent computes _{Q[π] n_ 1 _[∗]_ +1 _[, Q] n[π]_ 2 _[∗]_ +1 _[, ..., Q] n[π] n[∗]_ +1 _[}]_[,] the evaluation of each _πi[∗]_[under the new reward function induced by] **[ w]** _[n]_[+1][.][In this case, applying the] GPI theorem to the newly-computed set of value functions will give rise to a policy that performs at least as well as a policy based on any subset of these, including the empty set. Thus, this strategy 

There is a caveat, though. Why would one waste time computing the value functions of _π_ 1 _[∗][, π]_ 2 _[∗]_[, ...,] _πn[∗]_[, whose performance in] _[ M][n]_[+1][may be mediocre, if the same amount of resources can be allocated] to compute a sequence of _n_ policies with increasing performance? This is where SFs come into play. Suppose that we have learned the functions _Qπi i[∗]_ using the representation scheme shown in (3). Now, if the reward changes to _rn_ +1( _s, a, s[′]_ ) = _**φ**_ ( _s, a, s[′]_ ) _[⊤]_ **w** _n_ +1, as long as we have **w** _n_ +1 we can compute the new value function of _πi[∗]_[by simply making] _[ Q] πni[∗]_ +1[(] _[s, a]_[) =] _**[ ψ]**[π] i[∗]_ ( _s, a_ ) _[⊤]_ **w** _n_ +1. This reduces the computation of all _Qπni[∗]_ +1[to the much simpler supervised problem of approximating] **[ w]** _[n]_[+1][.] 

Once the functions _Qπni[∗]_ +1[have][been][computed,][we][can][apply][GPI][to][derive][a][policy] _[π]_[whose] performance on _Mn_ +1 is no worse than the performance of _π_ 1 _[∗][, π]_ 2 _[∗][, ..., π] n[∗]_[on][the][same][task.][A] 

5 

question that arises in this case is whether we can provide stronger guarantees on the performance of _π_ by exploiting the structure shared by the tasks in _M[φ]_ . The following theorem answers this question in the affirmative. 

_π[∗]_ **Theorem 2.** _Let Mi ∈M[φ] and let Qi j be the action-value function of an optimal policy of Mj ∈M[φ] when executed in Mi. Given approximations {Q_[˜] _[π] i_ 1 _[∗][,][Q]_[˜] _[π] i_ 2 _[∗][, ...,][Q]_[˜] _[π] i n[∗][}][ such that]_ 

**==> picture [257 x 19] intentionally omitted <==**

_π[∗] for all s ∈S, a ∈A, and j ∈{_ 1 _,_ 2 _, ..., n}, let π_ ( _s_ ) _∈_ argmax _a_ max _j Q_[˜] _i j_[(] _[s, a]_[)] _[.][Finally,][let]_ _**φ**_ max = max _s,a ||_ _**φ**_ ( _s, a_ ) _||, where || · || is the norm induced by the inner product adopted. Then,_ 

**==> picture [323 x 24] intentionally omitted <==**

Note that we used _Mi_ rather than _Mn_ +1 in the theorem’s statement to remove any suggestion of order among the tasks. Theorem 2 is a specialization of Theorem 1 for the case where the set of value functions used to compute _π_ are associated with tasks in the form of (5). As such, it provides stronger guarantees: instead of comparing the performance of _π_ with that of the previously-computed policies _πj_ , Theorem 2 quantifies the loss incurred by following _π_ as opposed to one of _Mi_ ’s optimal policies. 

As shown in (10), the loss _Qπi i[∗]_[(] _[s, a]_[)] _[−][Q][π] i_[(] _[s, a]_[)][is][upper-bounded][by][two][terms.] The term 2 _**φ**_ maxmin _j||_ **w** _i −_ **w** _j||/_ (1 _− γ_ ) is of more interest here because it reflects the structure of _M[φ]_ . This term is a multiple of the distance between **w** _i_ , the vector describing the task we are currently interested in, and the closest **w** _j_ for which we have computed a policy. This formalizes the intuition that the agent should perform well in task **w** _i_ if it has solved a similar task before. More generally, the term in question relates the concept of distance in R _[d]_ with difference in performance in _M[φ]_ . Note that this correspondence depends on the specific set of features _**φ**_ used, which raises the interesting question of how to define _**φ**_ such that tasks that are close in R _[d]_ induce policies that are also similar in some sense. Regardless of how exactly _**φ**_ is defined, the bound (10) allows for powerful extrapolations. For example, by covering the relevant subspace of R _[d]_ with balls of appropriate radii centered at **w** _j_ we can provide performance guarantees for _any_ task **w** [14]. This corresponds to building a library of _options_ (or “skills”) that can be used to solve any task in a (possibly infinite) set [22]. In Section 5 we illustrate this concept with experiments. 

Although Theorem 2 is inexorably related to the characterization of _M[φ]_ in (5), it does not depend on the definition of SFs in any way. Here SFs are the _mechanism_ used to efficiently apply the protocol suggested by Theorem 2. When SFs are used the value function approximations are given by _Q_ ˜ _πi j[∗]_[(] _[s, a]_[) =] _**[ψ]**_[˜] _πj[∗]_ ( _s, a_ ) _[⊤]_ **w** ˜ _i_ . The modules _**ψ**_ ˜ _πj[∗]_ are computed and stored when the agent is learning the tasks _Mj_ ; when faced with a new task _Mi_ the agent computes an approximation of **w** _i_ , which is a supervised learning problem, and then uses the GPI policyNote that we do not assume that eitherand **w** ˜ _i_ are accounted for by the term _ϵ_ appearing in (9). _**ψ** πj[∗]_ or **w** _i_ is computed exactly:As shown in (10), if _π_ defined in Theorem 2 to learnthe effect of errors in _ϵ_ is small and the agent _**ψψ**_[˜] ˜ _ππi[∗] j[∗]_ . has seen enough tasks the performance of _π_ on _Mi_ should already be good, which suggests it may also speed up the process of learning _**ψ**_[˜] _πi[∗]_ . 

Interestingly, Theorem 2 also provides guidance for some practical algorithmic choices. Since in an _π[∗]_ actual implementation one wants to limit the number of SFs _**ψ**_[˜] _j_ stored in memory, the corresponding whenvectors min **w** ˜ _jj||_ can be used to decide which ones to keep. **w** ˜ _i −_ **w** ˜ _j||_ is above a given threshold; alternatively, once the maximum number of SFsFor example, one can create a new _**ψ**_[˜] _πi[∗]_ only has been reached, one can replace _**ψ**_[˜] _πk[∗]_ , where _k_ = argmin _j||_ **w** ˜ _i −_ **w** ˜ _j||_ (here **w** _i_ is the current task). 

## **5 Experiments** 

In this section we present our main experimental results. Additional details, along with further results and analysis, can be found in Appendix B of the supplementary material. 

The first environment we consider involves navigation tasks defined over a two-dimensional continuous space composed of four rooms (Figure 1). The agent starts in one of the rooms and must reach a 

6 

goal region located in the farthest room. The environment has objects that can be picked up by the agent by passing over them. Each object belongs to one of three classes determining the associated reward. The objective of the agent is to pick up the “good” objects and navigate to the goal while avoiding “bad” objects. The rewards associated with object classes change at every 20 000 transitions, giving rise to very different tasks (Figure 1). The goal is to maximize the sum of rewards accumulated over a sequence of 250 tasks, with each task’s rewards sampled uniformly from [ _−_ 1 _,_ 1][3] . 

We defined a straightforward instantia-tion of our approach in which both **w** ˜ and _**ψ**_[˜] _π_ are computed incrementally in order to minimize losses induced by (2) and (4).current _**ψ**_[˜] Every time the task changes the _πi_ is stored and a new _**ψ**_ ˜ _πi_ +1 is created. We call this method SFQL as a reference to the fact that SFs are learned through an algorithm analogous to _Q_ -learning (QL)—which is used as a baseline in our comparisons [27]. As a Figure 1: Environment layout and some examples of optimore challenging reference point we remal trajectories associated with specific tasks. The shapes port results for a transfer method called of the objects represent their classes; ‘S’ is the start state _probabilistic policy reuse_ [8]. We adopt and ‘G’ is the goal. a version of the algorithm that builds on QL and reuses all policies learned. The resulting method, PRQL, is thus directly comparable to SFQL. The details of QL, PRQL, and SFQL, including their pseudo-codes, are given in Appendix B. 

We compared two versions of SFQL. In the first one, called SFQL- _**φ**_ , we assume the agent has access to features _**φ**_ that perfectly predict the rewards, as in (2). The second version of our agent had to learn an approximation _**φ**_[˜] _∈_ R _[h]_ directly from data collected by QL in the first 20 tasks. Note that _h_ may not coincide with the true dimension of _**φ**_ , which in this case is 4; we refer to the different instances of our algorithm as SFQL- _h_ . The process of learning _**φ**_[˜] followed the multi-task learning protocol proposed by Caruana [6] and Baxter [2], and described in detail in Appendix B. 

The results of our experiments can be seen in Figure 2. As shown, all versions of SFQL significantly outperform the other two methods, with an improvement on the average return of more than 100% when compared to PRQL, which itself improves on QL by around 100%. Interestingly, SFQL- _h_ seems to achieve good overall performance _faster_ than SFQL- _φ_ , even though the latter uses features that allow for an exact representation of the rewards. One possible explanation is that, unlike their counterparts _φi_ , the features _φ_[˜] _i_ are activated over most of the space _S × A × S_ , which results in a dense pseudo-reward signal that facilitates learning. 

The second environment we consider is a set of control tasks defined in the MuJoCo physics engine [26]. Each task consists in moving a two-joint torque-controlled simulated robotic arm to a 

**==> picture [396 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
SFQL-8<br>SFQL-휙 / SFQL-4<br>PRQL<br>Q-Learning<br>**----- End of picture text -----**<br>


Figure 2: Average and cumulative return per task in the four-room domain. SFQL- _h_ receives no reward during the first 20 tasks while learning _**φ**_[˜] . Error-bands show one standard error over 30 runs. 

7 

**==> picture [375 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
SFDQN<br>DQN<br>Tasks Trained<br>(b) Average performance on test tasks.<br>Task 1<br>Task 2<br>Task 3<br>Task 4<br>Tasks Trained<br>(a) Performance on training tasks (faded dotted lines in the (c) Colored and gray circles depict<br>background are DQN’s results). training and test targets, respectively.<br>Normalized Return<br>Normalized Return<br>**----- End of picture text -----**<br>


Figure 3: Normalized return on the reacher domain: ‘1’ corresponds to the average result achieved by DQN after learning each task separately and ‘0’ corresponds to the average performance of a randomly-initialized agent (see Appendix B for details). SFDQN’s results were obtained using the GPI policies _πi_ ( _s_ ) defined in the text. Shading shows one standard error over 30 runs. 

specific target location; thus, we refer to this environment as “the reacher domain.” We defined 12 tasks, but only allowed the agents to train in 4 of them (Figure 3c). This means that the agent must be able to perform well on tasks that it has never experienced during training. 

In order to solve this problem, we adopted essentially the same algorithm as above, but we replaced QL with Mnih et al.’s DQN—both as a baseline and as the basic engine underlying the SF agent [15]. The resulting method, which we call SFDQN, is an illustration of how our method can be naturally combined with complex nonlinear approximators such as neural networks. The features _φi_ used by SFDQN are the negation of the distances to the center of the 12 target regions. As usual in experiments of this type, we give the agents a description of the current task: for DQN the target coordinates are given as inputs, while for SFDQN this is provided as an one-hot vector **w** _t ∈_ R[12] [12]. Unlike in the previous experiment, in the current setup each transition was used to train all four _**ψ**_[˜] _πi_ through losses derived from (4). Here _πi_ is the GPI policy on the i[th] task: _πi_ ( _s_ ) _∈_ argmax _a_ max _j_ _**ψ**_[˜] _j_ ( _s, a_ ) _[⊤]_ **w** _i_ . 

Results are shown in Figures 3a and 3b. Looking at the training curves, we see that whenever a task is selected for training SFDQN’s return on that task quickly improves and saturates at nearoptimal performance. The interesting point to be noted is that, when learning a given task, SFDQN’s performance also improves in all other tasks, including the test ones, for which it does not have specialized policies. This illustrates how the combination of SFs and GPI can give rise to flexible agents able to perform well in _any_ task of a set of tasks with shared dynamics—which in turn can be seen as both a form of temporal abstraction and a step towards more general hierarchical RL [22, 1]. 

## **6 Related work** 

Mehta et al.’s [14] approach for transfer learning is probably the closest work to ours in the literature. There are important differences, though. First, Mehta et al. [14] assume that both _**φ**_ and **w** are always observable quantities provided by the environment. They also focus on average reward RL, in which the quality of a decision policy can be characterized by a single scalar. This reduces the process of selecting a policy for a task to one decision made at the outset, which is in clear contrast with GPI. 

8 

The literature on transfer learning has other methods that relate to ours [25, 11]. Among the algorithms designed for the scenario considered here, two approaches are particularly relevant because they also reuse old policies. One is Fernández et al.’s [8] probabilistic policy reuse, adopted in our experiments and described in Appendix B. The other approach, by Bernstein [4], corresponds to using our method but relearning all _**ψ**_[˜] _πi_ from scratch at each new task. 

When we look at SFs strictly as a representation scheme, there are clear similarities with Littman et al.’s [13] predictive state representation (PSR). Unlike SFs, though, PSR tries to summarize the dynamics of the entire environment rather than of a single policy _π_ . A scheme that is perhaps closer to SFs is the value function representation sometimes adopted in inverse RL [18]. 

SFs are also related to Sutton et al.’s [23] _general value functions_ (GVFs), which extend the notion of value function to also include “pseudo-rewards.” If we see _φi_ as a pseudo-reward, _ψi[π]_[(] _[s, a]_[)][ becomes] a particular case of GVF. Beyond the technical similarities, the connection between SFs and GVFs uncovers some principles underlying both lines of work that, when contrasted, may benefit both. On one hand, Sutton et al.’s [23] and Modayil et al.’s [16] hypothesis that relevant knowledge about the world can be expressed in the form of many predictions naturally translates to SFs: if _**φ**_ is expressive enough, the agent should be able to represent _any_ relevant reward function. Conversely, SFs not only provide a concrete way of using this knowledge, they also suggest a possible criterion to select the pseudo-rewards _**φ**_ ( _s, a, s[′]_ ) _[⊤]_ **w** ˜ _≈ φri_ , since ultimately we are only interested in features that help in the approximation( _s, a, s[′]_ ). 

Another generalization of value functions that is related to SFs is Schaul et al.’s [20] _universal value function approximators_ (UVFAs). UVFAs extend the notion of value function to also include as an argument an abstract representation of a “goal,” which makes them particularly suitable for transfer. _π[∗]_ ˜ ˜ The function max _j_ _**ψ**_[˜] _j_ ( _s, a_ ) _[⊤]_ **w** used in our framework can be seen as a function of _s_ , _a_ , and **w** —the The connection between SFs and UVFAs raises an interesting point:latter a generic way of representing a goal—, and thus in some sense this representationsince under this interpretation _is_ a UVFA. **w** ˜ is simply the description of a task, it can in principle be a direct function of the observations, whichopens up the possibility of the agent determining **w** ˜ even _before_ seeing any rewards. 

As discussed, our approach is also related to temporal abstraction and hierarchical RL: if we look at _**ψ**[π]_ as instances of Sutton et al.’s [22] _options_ , acting greedily with respect to the maximum over their value functions corresponds in some sense to planning at a higher level of temporal abstraction (that is, each _**ψ**[π]_ ( _s, a_ ) is associated with an option that terminates after a single step). This is the view adopted by Yao et al. [28], whose _universal option model_ closely resembles our approach in some aspects (the main difference being that they do not do GPI). 

Finally,[10] and Zhang et al.there have been [29] propose similar architectures to jointly learnprevious attempts to combine SR and neural _**ψ**_[˜] networks. _π_ ( _s, a_ ), _**φ**_ ˜ ( _s, a, s_ Kulkarni _′_ ) andet **w** al.˜ . Although neither work exploits SFs for GPI, they both discuss other uses of SFs for transfer. In principle the proposed (or similar) architectures can also be used within our framework. 

## **7 Conclusion** 

This paper builds on two concepts, both of which are generalizations of previous ideas. The first one is SFs, a generalization of Dayan’s [7] SR that extends the original definition from discrete to continuous spaces and also facilitates the use of function approximation. The second concept is GPI, formalized in Theorem 1. As the name suggests, this result extends Bellman’s [3] classic policy improvement theorem from a single to multiple policies. 

Although SFs and GPI are of interest on their own, in this paper we focus on their combination to induce transfer. The resulting framework is an elegant extension of DP’s basic setting that provides a solid foundation for transfer in RL. As a complement to the proposed transfer approach, we derived a theoretical result, Theorem 2, that formalizes the intuition that an agent should perform well on a novel task if it has seen a similar task before. We also illustrated with a comprehensive set of experiments how the combination of SFs and GPI promotes transfer in practice. 

We believe the proposed ideas lay out a general framework for transfer in RL. By specializing the basic components presented one can build on our results to derive agents able to perform well across a wide variety of tasks, and thus extend the range of environments that can be successfully tackled. 

9 

## **Acknowledgments** 

The authors would like to thank Joseph Modayil for the invaluable discussions during the development of the ideas described in this paper. We also thank Peter Dayan, Matt Botvinick, Marc Bellemare, and Guy Lever for the excellent comments, and Dan Horgan and Alexander Pritzel for their help with the experiments. Finally, we thank the anonymous reviewers for their comments and suggestions to improve the paper. 

## **References** 

- [1] Andrew G. Barto and Sridhar Mahadevan. Recent advances in hierarchical reinforcement learning. _Discrete Event Dynamic Systems_ , 13(4):341–379, 2003. 

- [2] Jonathan Baxter. A model of inductive bias learning. _Journal of Artificial Intelligence Research_ , 12:149–198, 2000. 

- [3] Richard E. Bellman. _Dynamic Programming_ . Princeton University Press, 1957. 

- [4] Daniel S. Bernstein. Reusing old policies to accelerate learning on new MDPs. Technical report, Amherst, MA, USA, 1999. 

- [5] Dimitri P. Bertsekas and John N. Tsitsiklis. _Neuro-Dynamic Programming_ . Athena Scientific, 1996. 

- [6] Rich Caruana. Multitask learning. _Machine Learning_ , 28(1):41–75, 1997. 

- [7] Peter Dayan. Improving generalization for temporal difference learning: The successor representation. _Neural Computation_ , 5(4):613–624, 1993. 

- [8] Fernando Fernández, Javier García, and Manuela Veloso. Probabilistic policy reuse for inter-task transfer learning. _Robotics and Autonomous Systems_ , 58(7):866–871, 2010. 

- [9] Trevor Hastie, Robert Tibshirani, and Jerome Friedman. _The Elements of Statistical Learning: Data Mining, Inference, and Prediction_ . Springer, 2002. 

- [10] Tejas D. Kulkarni, Ardavan Saeedi, Simanta Gautam, and Samuel J Gershman. Deep successor reinforcement learning. _arXiv preprint arXiv:1606.02396_ , 2016. 

- [11] Alessandro Lazaric. _Transfer in Reinforcement Learning: A Framework and a Survey_ . Reinforcement Learning: State-of-the-Art, pages 143–173, 2012. 

- [12] Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement learning. _arXiv preprint arXiv:1509.02971_ , 2015. 

- [13] Michael L. Littman, Richard S. Sutton, and Satinder Singh. Predictive representations of state. In _Advances in Neural Information Processing Systems (NIPS)_ , pages 1555–1561, 2001. 

- [14] Neville Mehta, Sriraam Natarajan, Prasad Tadepalli, and Alan Fern. Transfer in variable-reward hierarchical reinforcement learning. _Machine Learning_ , 73(3), 2008. 

- [15] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level control through deep reinforcement learning. _Nature_ , 518(7540):529–533, 2015. 

- [16] Joseph Modayil, Adam White, and Richard S. Sutton. Multi-timescale nexting in a reinforcement learning robot. _Adaptive Behavior_ , 22(2):146–160, 2014. 

- [17] Sriraam Natarajan and Prasad Tadepalli. Dynamic preferences in multi-criteria reinforcement learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 601–608, 2005. 

10 

- [18] Andrew Ng and Stuart Russell. Algorithms for inverse reinforcement learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 663–670, 2000. 

- [19] Martin L. Puterman. _Markov Decision Processes—Discrete Stochastic Dynamic Programming_ . John Wiley & Sons, Inc., 1994. 

- [20] Tom Schaul, Daniel Horgan, Karol Gregor, and David Silver. Universal Value Function Approximators. In _International Conference on Machine Learning (ICML)_ , pages 1312–1320, 2015. 

- [21] Richard S. Sutton and Andrew G. Barto. _Reinforcement Learning: An Introduction_ . MIT Press, 1998. 

- [22] Richard S. Sutton, Doina Precup, and Satinder Singh. Between MDPs and semi-MDPs: a framework for temporal abstraction in reinforcement learning. _Artificial Intelligence_ , 112: 181–211, 1999. 

- [23] Richard S. Sutton, Joseph Modayil, Michael Delp, Thomas Degris, Patrick M. Pilarski, Adam White, and Doina Precup. Horde: A scalable real-time architecture for learning knowledge from unsupervised sensorimotor interaction. In _International Conference on Autonomous Agents and Multiagent Systems_ , pages 761–768, 2011. 

- [24] Csaba Szepesvári. _Algorithms for Reinforcement Learning_ . Synthesis Lectures on Artificial Intelligence and Machine Learning. Morgan & Claypool Publishers, 2010. 

- [25] Matthew E. Taylor and Peter Stone. Transfer learning for reinforcement learning domains: A survey. _Journal of Machine Learning Research_ , 10(1):1633–1685, 2009. 

- [26] Emanuel Todorov, Tom Erez, and Yuval Tassa. MuJoCo: A physics engine for model-based control. In _IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)_ , pages 5026–5033, 2012. 

- [27] Christopher Watkins and Peter Dayan. Q-learning. _Machine Learning_ , 8:279–292, 1992. 

- [28] Hengshuai Yao, Csaba Szepesvári, Richard S Sutton, Joseph Modayil, and Shalabh Bhatnagar. Universal option models. In _Advances in Neural Information Processing Systems (NIPS)_ , pages 990–998. 2014. 

- [29] Jingwei Zhang, Jost Tobias Springenberg, Joschka Boedecker, and Wolfram Burgard. Deep reinforcement learning with successor features for navigation across similar environments. _CoRR_ , abs/1612.05533, 2016. 

11 

# **Successor Features for Transfer in Reinforcement Learning Supplementary Material** 

**André Barreto** , **Will Dabney** , **Rémi Munos** , **Jonathan J. Hunt** , **Tom Schaul** , **Hado van Hasselt** , **David Silver** 

```
{andrebarreto,wdabney,munos,jjhunt,schaul,hado,davidsilver}@google.com
```

DeepMind 

## **Abstract** 

In this supplement we give details of the theory and experiments that had to be left out of the main paper due to the space limit. For the convenience of the reader the statements of the theoretical results are reproduced before the respective proofs. We also provide a thorough description of the protocol used to carry out our experiments, present details of the algorithms, including their pseudo-code, and report additional empirical analysis that could not be included in the paper. The numbering of sections, equations, and figures resume that used in the main paper, so we refer to these elements as if paper and supplement were a single document. We also cite references listed in the main paper. 

## **A Proofs of theoretical results** 

**Theorem 1.** ˜ ˜ **(Generalized Policy Improvement)** ˜ _Let π_ 1 _, π_ 2 _, ..., πn be n decision policies and let_ 1 2 _n Q[π] , Q[π] , ..., Q[π] be approximations of their respective action-value functions such that_ 

**==> picture [286 x 12] intentionally omitted <==**

_Define_ 

**==> picture [126 x 18] intentionally omitted <==**

_Then,_ 

**==> picture [150 x 23] intentionally omitted <==**

_for any s ∈ S and any a ∈ A, where Q[π] is the action-value function of π._ 

_Proof._ To simplify the notation, let 

**==> picture [284 x 12] intentionally omitted <==**

We start by noting that for any _s ∈ S_ and any _a ∈ A_ the following holds: 

**==> picture [406 x 17] intentionally omitted <==**

12 

For all _s ∈ S_ , _a ∈ A_ , and _i ∈{_ 1 _,_ 2 _, ..., n}_ we have 

**==> picture [262 x 161] intentionally omitted <==**

Since _T[π] Q_[˜] max( _s, a_ ) _≥ Q[π][i]_ ( _s, a_ ) _− γϵ_ for any _i_ , it must be the case that 

**==> picture [158 x 48] intentionally omitted <==**

Let _e_ ( _s, a_ ) = 1 for all _s, a ∈ S × A_ . It is well known that _T[π]_ ( _Q_[˜] max( _s, a_ ) + _ce_ ( _s, a_ )) = _T[π] Q_[˜] max( _s, a_ ) + _γc_ for any _c ∈_ R. Using this fact together with the monotonicity and contraction properties of the Bellman operator _T[π]_ , we have 

**==> picture [156 x 70] intentionally omitted <==**

**Lemma 1.** _Let δij_ = max _s,a |ri_ ( _s, a_ ) _− rj_ ( _s, a_ ) _|. Then,_ 

**==> picture [134 x 23] intentionally omitted <==**

**==> picture [259 x 16] intentionally omitted <==**

**==> picture [338 x 32] intentionally omitted <==**

Our strategy will be to bound _|Q[i] i_[(] _[s, a]_[)] _[ −][Q][j] j_[(] _[s, a]_[)] _[|]_[ and] _[ |][Q][j] j_[(] _[s, a]_[)] _[ −][Q] i[j]_[(] _[s, a]_[)] _[|]_[.][Note that] _[ |][Q][i] i_[(] _[s, a]_[)] _[ −] Q[j] j_[(] _[s, a]_[)] _[|]_[ is the difference between the value functions of two MDPs with the same transition function] 

13 

but potentially different rewards. Let ∆ _ij_ = max _s,a |Q[i] i_[(] _[s, a]_[)] _[ −][Q][j] j_[(] _[s, a]_[)] _[|]_[.][Then,][2] 

**==> picture [408 x 126] intentionally omitted <==**

Since (12) is valid for any _s, a ∈ S × A_ , we have shown that ∆ _ij ≤ δij_ + _γ_ ∆ _ij_ . Solving for ∆ _ij_ we get 

**==> picture [233 x 24] intentionally omitted <==**

We now turn our attention to _|Q[j] j_[(] _[s, a]_[)] _[ −][Q] i[j]_[(] _[s, a]_[)] _[|]_[.][Following][the][previous][steps,][define][∆] _[′] ij_[=] max _s,a |Q[i] i_[(] _[s, a]_[)] _[ −][Q][j] i_[(] _[s, a]_[)] _[|]_[.][Then,] 

**==> picture [440 x 110] intentionally omitted <==**

Solving for ∆ _[′] ij_[, as above, we get] 

**==> picture [233 x 23] intentionally omitted <==**

Plugging (13) and (14) back in (11) we get the desired result. 

**Theorem 2.** _Let Mi ∈M[φ] and let Qπi j[∗] be the value function of an optimal policy of Mj ∈M[φ] when executed in Mi. Given the set {Q_[˜] _[π] i_ 1 _[∗][,][Q]_[˜] _[π] i_ 2 _[∗][, ...,][Q]_[˜] _[π] i n[∗][}][ such that]_ 

**==> picture [292 x 20] intentionally omitted <==**

_let_ 

**==> picture [128 x 21] intentionally omitted <==**

_Finally, let_ _**φ**_ max = max _s,a ||_ _**φ**_ ( _s, a_ ) _||, where || · || is the norm induced by the inner product adopted. Then,_ 

**==> picture [244 x 24] intentionally omitted <==**

> 2We follow the steps of Strehl and Littman [31]. 

14 

_Proof._ The result is a direct application of Theorem 1 and Lemma 1. For any _j ∈{_ 1 _,_ 2 _, ..., n}_ , we have 

**==> picture [454 x 134] intentionally omitted <==**

## **B Details of the experiments** 

In this section we provide additional information about our experiments. We start with the four-room environment and then we discuss the reacher domain. In both cases the structure of the discussion is the same: we start by giving a more in depth description of the environment itself, both at a conceptual level and at a practical level, then we provide a thorough description of the algorithms used, and, finally, we explain the protocol used to carry out the experiments. 

## **B.1 Four-room environment** 

## **B.1.1 Environment** 

In Section 5 of the paper we gave an intuitive description of the four-room domain used in our experiments. In this section we provide a more formal definition of the environment _M_ as a family of Markov decision processes (MDPs) _M_ , each one associated with a task. 

The environment has objects that can be picked up by the agent by passing over them. There is a total of _no_ objects, each belonging to one of _nc ≤ no_ classes. The class of an object determines the reward _rc_ associated with it. An episode ends when the agent reaches the goal, upon which all the objects re-appear. We assume that _rg_ is always 1 but _rc_ may vary: a specific instantiation of the rewards _rc_ defines a _task_ . Every time a new task starts the rewards _rc_ are sampled from a uniform distribution over [ _−_ 1 _,_ 1]. Figure 1 shows the specific environment layout used, in which _no_ = 12 and _nc_ = 3. 

We now focus on a single task _M ∈M_ . We start by describing the state and action spaces, and the transition dynamics. The agent’s position at any instant in time is a point _{sx, sy} ∈_ [0 _,_ 1][2] . There are four actions available, _A ≡{_ up _,_ down _,_ left _,_ right _}_ . The execution of one of the actions moves the agent 0 _._ 05 units in the desired direction, and normal random noise with zero mean and standard deviation 0 _._ 005 is added to the position of the agent (that is, a move along the _x_ axis would be _s[′] x_[=] _[ s][x][± N]_[(0] _[.]_[05] _[,]_[ 0] _[.]_[005)][, where] _[ N]_[(0] _[.]_[05] _[,]_[ 0] _[.]_[005)][ is a normal variable with mean][ 0] _[.]_[05][ and standard] deviation 0 _._ 005). If after a move the agent ends up outside of the four rooms or on top of a wall the move is undone. Otherwise, if the agent lands on top of an object it picks it up, and if it lands on the goal region the episode is terminated (and all objects re-appear). In the specific instance of the environment shown in Figure 1 objects were implemented as circles of radius 0 _._ 04, the goal is a circle of radius 0 _._ 1 centered at one of the extreme points of the map, and the walls are rectangles of width 0 _._ 04 traversing the environment’s range. 

As described in the paper, within an episode each of the _no_ objects can be present or absent, and since they define the reward function a well defined Markov state must distinguish between all possible 2 _[n][o]_ object configurations. Therefore, the state space of our MDP is _S ≡{_ 0 _,_ 1 _}[n][o] ×_ R[2] . An intuitive way of visualizing _S_ is to note that each of the 2 _[n][o]_ object configurations is potentially associated with a different value function over the continuous space [0 _,_ 1][2] . 

Having already described _S_ , _A_ , and _p_ ( _·|s, a_ ), we only need to define the reward function _R_ ( _s, a, s[′]_ ) and the discount factor _γ_ in order to conclude the formulation of the MDP _M_ . As discussed in 

15 

Section 5, the reward _R_ ( _s, a, s[′]_ ) is a deterministic function of _s[′]_ : if the agent is over an object of class _c_ in _s[′]_ it gets a reward of _rc_ , and if it is in the goal region it gets a reward of _rg_ = 1; in all other cases the reward is zero. In our experiments we fixed _γ_ = 0 _._ 95. 

By mapping each object onto its class, it is possible to construct features _**φ**_ ( _s, a, s[′]_ ) that perfectly predicts the reward for all tasks _M_ in the environment _M[φ]_ , as in (2) and (5). Let _**φ** c_ ( _s, a, s[′]_ ) _≡ δ{_ is the agent over an object of class _c_ in _s[′]_ ? _}_ , where _δ{_ false _}_ = 0 and _δ{_ true _}_ = 1. Similarly, let _**φ** g_ ( _s, a, s[′]_ ) _≡ δ{_ is the agent over the goal region in _s[′]_ ? _}_ . By concatenating the _nc_ functions _**φ** c_ and _**φ** g_ we get the vector _**φ**_ ( _s, a, s[′]_ ) _∈{_ 0 _,_ 1 _}[n][c]_[+1] ; now, if we make **w** _c_ = _rc_ for all _c_ and **w** _nc_ +1 = _rg_ , it should be clear that _r_ ( _s, a, s[′]_ ) = _**φ**_ ( _s, a, s[′]_ ) _[⊤]_ **w** , as desired. 

Since _r_ ( _s, a, s[′]_ ) can be written in the form of (2), the definition of _M_ can be naturally extended to _M_ , as in (5). In our experiments we assume that the agents receive a signal from _M_ whenever the task changes (see Algorithms 1, 2, and 3 and discussion below). 

## **B.1.2 Algorithms** 

We assume that the agents know their position _{sx, sy} ∈_ [0 _,_ 1][2] and also have an “object detector” **o** _∈{_ 0 _,_ 1 _}[n][o]_ whose i[th] component is 1 if and only if the agent is over object _i_ . Using this information the agents build two vectors of features. The vector _**ϕ** p_ ( _s_ ) _∈_ R[100] is composed of the activations of a regular 10 _×_ 10 grid of radial basis functions at the point _{sx, sy}_ . Specifically, in our experiments we used Gaussian functions, that is: 

**==> picture [294 x 25] intentionally omitted <==**

where **c** _i ∈_ R[2] is the center of the i[th] Gaussian. As explained in Section B.1.3, the value of _σ_ was determined in preliminary experiments with QL; all algorithms used _σ_ = 0 _._ 1. In addition to _**ϕ** p_ ( _s_ ), using **o** the agents build an “inventory” _**ϕ** i_ ( _s_ ) _∈{_ 0 _,_ 1 _}[n][o]_ whose i[th] component indicates whether the i[th] object has been picked up or not. The concatenation of _**ϕ** i_ ( _s_ ) and _**ϕ** p_ ( _s_ ) plus a constant term gives rise to the feature vector˜ _**ϕ**_ ( _s_ ) _∈_ R _[D]_ used by all the agents to represent the value function: _Q[π]_ ( _s, a_ ) = _**ϕ**_ ( _s_ ) _[⊤]_ **z** _[π] a_[, where] **[ z]** _[π] a[∈]_[R] _[D]_[are learned weights.] 

It is instructive to take a closer look at how exactly SFQL represents the value function. Note that, even though our algorithm also represents _Q_[˜] _[π]_ as a linear combination of the features _**ϕ**_ ( _s_ ), it never explicitly computes **z** _[π] a_[.][Specifically,][SFQL represent SFs as] _**[ψ]**_[˜] _π_ ( _s, a_ ) = _**ϕ**_ ( _s_ ) _⊤_ **Z** _πa_[,][where] **Z** _[π] a[∈]_[R] _[D][×][d]_[,][and][the][value][function][as] _[Q]_[˜] _[π]_[(] _[s, a]_[)][=] _**[ψ]**_[˜] _π_ ( _s, a_ ) _⊤_ **w** ˜ = _**ϕ**_ ( _s_ ) _⊤_ **Z** _πa_ **[w]**[˜][.][By][making] **z** _[π] a_[=] **[ Z]** _[π] a_ **[w]**[˜][, it becomes clear that SFQL unfolds the problem of learning] **[ z]** _[π] a_[into the sub-problems of] learning **Z** _[π] a_[and] **[w]**[˜][.][These parameters are learned via gradient descent in order to minimize losses] induced by (4) and (2), respectively (see below). 

The pseudo-codes of QL, PRQL, and SFQL are given in Algorithms 1, 2, and 3, respectively. As one can see, all algorithms used an _ϵ_ -greedy policy to explore the environment, with _ϵ_ = 0 _._ 15 [21]. Two design choices deserve to be discussed here. First, as mentioned in Section B.1.1, the agents “know” when the task changes. This makes it possible for the algorithms to take measures like reinitializing the weights **z** _[π] a_[or adding a new representative to the set of decision policies.][Another] design choice, this one specific to PRQL and SFQL, was not to limit the number of decision policies (orsignal and an ever-growing set of policies. _**ψ**_[˜] _πi_ ) stored. It is not difficult to come up with strategies to avoid both an explicit end-of-taskFor example, in Section 4.2 we discuss how **w** ˜ can be used to select which _**ψ**_[˜] _πi_ to keep in the case of limited memory. Also, by monitoring the error in the approximation _**φ**_[˜] ( _s, a, s[′]_ ) _[⊤]_ **w** ˜ one can detect when the task has changed in a significant way. Although these are interesting extensions, given the introductory character of this paper we refrained from overspecializing the algorithms in order to illustrate the properties of the proposed approach in the clearest way possible. 

## **SFQL** 

We now discuss some characteristics of the specific SFQL algorithm used in the experiments. First, note that errors in the value-function approximation can potentially have a negative effect on GPI, since an overestimated _Q_[˜] _[π][i]_ ( _s, a_ ) may be the function determining the action selected by _π_ in (7). One 

16 

**Algorithm 1** QL 

_ϵ_ exploration parameter for _ϵ_ -greedy strategy **Require:** _α_ learning rate 1: **for** _t ←_ 1 _,_ 2 _, ...,_ num_tasks **do** 2: **z** _a ←_ small random initial values **for** all _a ∈A_ 3: new_episode _←_ true 4: **for** _i ←_ 1 _,_ 2 _, ...,_ num_steps **do** 5: **if** new_episode **then** 6: new_episode _←_ false 7: _s ←_ initial state 8: **end if** 9: sel_rand_a _∼_ Bernoulli( _ϵ_ ) // Sample from a Bernoulli distribution with parameter _ϵ_ 10: **if** sel_rand_a **then** _a ∼_ Uniform ( _{_ 1 _,_ 2 _, ..., |A|}_ ) // _ϵ_ -greedy exploration strategy 11: **else** _a ←_ argmax _bQ_ ( _s, b_ ) 12: Take action _a_ and observe reward _r_ and next state _s[′]_ 13: **if** _s[′]_ is a terminal state **then** 14: _γ ←_ 0 15: new_episode _←_ true 16: **end if** 17: **z** _a ←_ **z** _a_ + _α_ ( _r_ + _γ_ max _a′ Q_ ( _s[′] , a[′]_ ) _− Q_ ( _s, a_ )) _∇_ **z** _Q_ ( _s, a_ ) // For _Q_ ( _s, a_ ) = _**ϕ**_ ( _s_ ) _[⊤]_ **z** _a_ , _∇_ **z** _Q_ ( _s, a_ ) = _**ϕ**_ ( _s_ 18: _s ← s[′]_ 19: **end for** 20: **end for** 

**==> picture [172 x 11] intentionally omitted <==**

way of keeping this phenomenon from occurring indefinitely is to continue to update the functions˜ _Q[π] i_ ( _s, a_ ) that are relevant for action selection. In the context of SFs this corresponds to constantly refining _**ψ**_[˜] _πi_ , which can be done as long as we have access to _πi_ . In the scenario considered here we can recover _πi_ by keeping the weights **w** ˜ _i_ used to learn the SFs _**ψ**_[˜] _πi_ (line 2 of Algorithm 3). Note that with this information one can easily update any _**ψ**_[˜] _πi_ off-policy; as shown in lines 25–30 of Algorithm 3, in the version of SFQL used in the experiments we always update the _**ψ**_[˜] _πi_ that achieves the maximum in (7) (line 10 of the pseudo-code). 

> Next we discuss the details of howto compute **w** ˜ : **w** ˜ and _**ψ**_[˜] _π_ are learned. We start by showing the loss function used 

**==> picture [312 x 25] intentionally omitted <==**

where _D_ is a distribution over _S ×A×S_ which in RL is usually the result of executing a policy under the environment’s dynamics _p_ ( _·|s, a_ ). The minimization of (16) is done in line 21 of Algorithm 3. As discussed, SFQL keeps a set of _**ψ**_[˜] _πi_ , each one associated with a policy _πi_ . The loss function used to compute each _**ψ**_[˜] _πi_ is 

**==> picture [378 x 49] intentionally omitted <==**

where _a[′]_ = argmax _bQ_[˜] _[π][i]_ ( _s[′] , b_ ) = argmax _b_ _**ψ**_[˜] _πi_ ( _s′, b_ ) _⊤_ **w** ˜ . Note that the policy that induces _D_ is not necessarily _πi_ —that is, _**ψ**_[˜] _πi_ ( _s, a_ ) can be learned off-policy, as discussed above. As usual in RL, the target _**φ**_[˜] ( _s, a, s[′]_ ) + _γ_ _**ϕ**_ ( _s[′]_ ) _[⊤]_ **Z** _[π] a[′][i]_[is considered fixed,] _[ i.e.]_[, the loss][ L] _[Z]_[is minimized with respect to] **Z** _[π] a[i]_[only.][The minimization of (17) is done in lines 23 and 28 of Algorithm 3.] 

As discussed in Section 5, we used two versions of SFQL in our experiments. In the first one, SFQL- _**φ**_ , we assume that the agent knows how to construct a vector of features _**φ**_ that perfectly predicts the reward for all tasks _M_ in the environment _M[φ]_ . The other version of our algorithm, SFQL- _h_ , uses an approximate _**φ**_[˜] learned from data. We now give details of how _**φ**_[˜] was computed 

17 

**Algorithm 2** PRQL 

_ϵ_ exploration parameter for _ϵ_ -greedy strategy _α_ learning rate **Require:** _η_ parameter to control probability to reuse old policy _τ_ parameter to control bias in favor of stronger policies 1: **for** _t ←_ 1 _,_ 2 _, ...,_ num_tasks **do** 2: **for** _k ←_ 1 _,_ 2 _, ..., t_ **do** 3: score _k ←_ 0 // score _k_ is the score associated with policy _πk_ 4: used _k ←_ 0 // used _k_ is the number of times policy _πk_ was used 5: **end for** 6: c _← t_ // c is the index of the policy currently being used 7: **z** _[t] a[←]_[small random initial values] 8: curr_score _←_ 0 9: new_episode _←_ true 10: **for** _i ←_ 1 _,_ 2 _, ...,_ num_steps **do** 11: **if** new_episode **then** 12: scorec _←_[score][c] _[ ×]_[ used][c][ + curr][_][score] // Update score for policy currently being used usedc + 1 13: **for** _k ←_ 1 _,_ 2 _, ..., t_ **do** _pk ← e[τ][×]_[score] _[k] /_[�] _[t] j_ =1 _[e][τ][×]_[score] _[j]_ // Turn scores into probabilities 14: _c ∼_ Multinomial( _p_ 1 _, p_ 2 _, ..., pt_ ) // Select policy _c_ with probability _pc_ 15: usedc _←_ usedc + 1 // Update number of times policy _πc_ has been used 16: curr_score _←_ 0 17: new_episode _←_ false 18: _s ←_ initial state 19: **end if** 20: **if** _t ̸_ = _c_ **then** use_prev_policy _∼_ Bernoulli( _η_ ) **else** use_prev_policy _←_ false 21: **if** use_prev_policy **then** // Action will be selected by _πc_ , the policy being reused 22: _a ←_ argmax _a′Q_ c( _s, a[′]_ ) 23: **else** // Action will be selected by _πc_ , the most recent policy 24: sel_rand_a _∼_ Bernoulli( _ϵ_ ) 25: **if** sel_rand_a **then** _a ∼_ Uniform ( _{_ 1 _,_ 2 _, ..., |A|}_ ) **else** _a ←_ argmax _a′Qt_ ( _s, a[′]_ ) // _ϵ_ -greedy exploration strategy 26: **end if** 27: Take action _a_ and observe reward _r_ and next state _s[′]_ 28: **if** _s[′]_ is a terminal state **then** 29: _γ ←_ 0 30: new_episode _←_ true 31: **end if** 32: **z** _[t] a[←]_ **[z]** _[t] a_[+] _[ α]_[(] _[r]_[ +] _[ γ]_[ max] _[a][′][ Q][t]_[(] _[s][′][, a][′]_[)] _[ −][Q][t]_[(] _[s, a]_[))] _[∇]_ **[z]** _[Q][t]_[(] _[s, a]_[)] // For _Qt_ ( _s, a_ ) = _**ϕ**_ ( _s_ ) _[⊤]_ **z** _[t] a_[,] _[ ∇]_ **z** _[Q] t_[(] _[s, a]_[) =] _**[ ϕ]**_[(] _[s]_[)] 33: curr_score _←_ curr_score + _r_ 34: _s ← s[′]_ 35: **end for** 36: **end for** 

in this case. In order to learn _**φ**_[˜] , we used the samples ( _si, ai, ri, s[′] i_[)] _[t]_[collected][by][QL][in][the][first] _t_ = 1 _,_ 2 _, ...,_ 20 tasks. Since this results in an unbalanced dataset in which most of the transitions have _ri_ = 0, we kept all the samples with _ri_ = 0 and discarded 75% of the remaining samples. We then used the resulting dataset to minimize the following loss: 

**==> picture [383 x 18] intentionally omitted <==**

where _Dt[′]_[reflects the down-sampling of zero rewards.][The vector of features] _**[ ϕ]**_[(] _[s, s][′]_[)][ is the con-] catenation of _**ϕ**_ ( _s_ ) and _**ϕ**_ ( _s[′]_ ), and _ς_ ( _·_ ) is a sigmoid function applied element-wise. We note that **o** ( _s[′]_ ) = _**ϕ** i_ ( _s[′]_ ) _−_ _**ϕ** i_ ( _s_ ), from which it is possible to compute an “exact” _**φ**_[˜] = _**φ**_ . In order to minimize (18) we used the multi-task framework proposed by Caruana [6]. Simply put, Caruana’s [6] approach consists in looking at _ς_ ( _**ϕ**_ ( _s, s[′]_ ) _[⊤]_ **H** ) _[⊤]_ **w** _t_ as a neural network with one hidden layer and 20 

18 

**Algorithm 3** SFQL 

_ϵ_ exploration parameter for _ϵ_ -greedy strategy _α_ learning rate for _**ψ**_ ’s parameters **Require:** _αw_ learning rate for **w** _**φ**_ features to be predicted by SFs 1: **for** _t ←_ 1 _,_ 2 _, ...,_ num_tasks **do** 2: **w** _t ←_ small random initial values 3: **Z** _[t] a[←]_[small random initial values in][ R] _[D][×][h]_ **[ if]** _[ t]_[ = 1] **[ else][ Z]** _[t] a[−]_[1] // The k[th] column of **Z** _[t] a_[,] **[ z]** _[tk] a_[, are the parameters of the k][th][component of] _**[ψ]**_[˜] _t_[,][ ( ˜] _**[ψ]** t_[)] _k[≡]_ _**[ψ]**_[˜] _tk_ 4: new_episode _←_ true 5: **for** _i ←_ 1 _,_ 2 _, ...,_ num_steps **do** 6: **if** new_episode **then** 7: new_episode _←_ false 8: _s ←_ initial state 9: **end if** 10: _c ←_ argmax _k∈{_ 1 _,_ 2 _,...,t}_ max _b_ _**ψ**_[˜] _k_ ( _s, b_ ) _[⊤]_ **w** _t_ // _c_ is the index of the _**ψ**_[˜] associated with the largest value in _s_ 11: sel_rand_a _∼_ Bernoulli( _ϵ_ ) // Sample from a Bernoulli distribution with parameter _ϵ_ 12: **if** sel_rand_a **then** _a ∼_ Uniform ( _{_ 1 _,_ 2 _, ..., |A|}_ ) // _ϵ_ -greedy exploration strategy 13: **else** _a ←_ argmax _b_ _**ψ**_[˜] _c_ ( _s, b_ ) _[⊤]_ **w** _t_ 14: Take action _a_ and observe reward _r_ and next state _s[′]_ 15: **if** _s[′]_ is a terminal state **then** 16: _γ ←_ 0 17: new_episode _←_ true 18: **else** 19: _a[′] ←_ argmax _b_ max _k∈{_ 1 _,_ 2 _,...,t}_ _**ψ**_[˜] _k_ ( _s[′] , b_ ) _[⊤]_ **w** _t_ // _a[′]_ is the action with the highest value in _s[′]_ 20: **end if** 21: **w** _t ←_ **w** _t_ + _αw_ � _r −_ _**φ**_ ( _s, a, s[′]_ ) _[⊤]_ **w** � _**φ**_ ( _s, a, s[′]_ ) // Update **w** 22: **for** _k ←_ 1 _,_ 2 _, ..., d_ **do** 23: **z** _[tk] a[←]_ **[z]** _[tk] a_[+] _[ α]_ _**φ** k_ ( _s, a, s[′]_ ) + _γ_ _**ψ**_[˜] _tk_ ( _s[′] , a[′]_ ) _−_ _**ψ**_[˜] _tk_ ( _s, a_ ) _∇_ **z** _**ψ**_[˜] _tk_ ( _s, a_ ) � � // For _**ψ**_[˜] _t_ ( _s, a_ ) = _**ϕ**_ ( _s_ ) _[⊤]_ **Z** _[t] a_[,] _[ ∇]_ **z** _**[ψ]**_[˜] _tk_[(] _[s, a]_[) =] _**[ ϕ]**_[(] _[s]_[)] 24: **end for** 25: **if** _c ̸_ = _t_ **then** 26: _a[′] ←_ argmax _b_ _**ψ**_[˜] _c_ ( _s[′] , b_ ) _[⊤]_ **w** _c_ // _a[′]_ is selected according to reward function induced by **w** _c_ 27: **for** _k ←_ 1 _,_ 2 _, ..., d_ **do** 28: **z** _[ck] a[←]_ **[z]** _[ck] a_[+] _[ α]_ _**φ** k_ ( _s, a, s[′]_ ) + _γ_ _**ψ**_[˜] _ck_ ( _s[′] , a[′]_ ) _−_ _**ψ**_[˜] _ck_ ( _s, a_ ) _∇_ **z** _**ψ**_[˜] _ck_ ( _s, a_ ) // Update _**ψ**_[˜] _c_ � � 29: **end for** 30: **end if** 31: _s ← s[′]_ 32: **end for** 33: **end for** 

outputs, that is, **w** ˜ is replaced with **W**[˜] _∈_ R _[h][×]_[20] and a reward _r_ received in the t[th] task is extended into a 20-dimensional vector in which the t[th] component is _r_ and all other components are zero. One can then minimize (18) with respect to the parameters **H** and **w** _t_ through gradient descent. Although this strategy of using the _k_ first tasks to learn _**φ**_[˜] is feasible, in practice one may want to replace this arbitrary decision with a more adaptive approach, such as updating _**φ**_[˜] online until a certain stop criterion is satisfied. Note though that a significant change in _**φ**_[˜] renders the SFs _**ψ**_[˜] _πi_ outdated, and thus the benefits of refining the former should be weighed against the overhead of constantly updating the latter, potentially off-policy. 

As one can see in this section, we tried to keep the methods as simple as possible in order to not obfuscate the main message of the paper, which is not to propose any particular algorithm but rather to present a general framework for transfer based on the combination of SFs and GPI. 

19 

## **B.1.3 Experimental setup** 

In this section we describe the precise protocol adopted to carry out our experiments. Our initial step was to use QL, the basic algorithm behind all three algorithms, to make some decisions that apply to all of them. First, in order to define the features _**ϕ**_ ( _s_ ) used by the algorithms, we checked the performance of QL when using different configurations of the vector _**ϕ** p_ ( _s_ ) giving the position of the agent. Specifically, we tried two-dimensional grids of Gaussians with 5, 10, 15, and 20 functions per dimension. Since the improvement in QL’s performance when using a number of functions larger than 10 was not very significant, we adopted a 10 _×_ 10 grid of Gaussians in our experiments. We also varied the value of the parameter _σ_ appearing in (15) in the set _{_ 0 _._ 01 _,_ 0 _._ 1 _,_ 0 _._ 3 _}_ . Here the best performance of QL was obtained with _σ_ = 0 _._ 1, which was then the value adopted throughout the experiments. The parameter _ϵ_ used for _ϵ_ -greedy exploration was also set based on QL’s performance. Specifically, we varied _ϵ_ in the set _{_ 0 _._ 15 _,_ 0 _._ 2 _,_ 0 _._ 3 _}_ and verified that the best results were obtained with _ϵ_ = 0 _._ 15 (we tried relatively large values for _ϵ_ because of the non-stationarity of the underlying environment). Finally, we tested two variants of QL: one that resets the weights **z** _[π] a_[every time a new] task starts, as in line 2 of Algorithm 1, and one that keeps the old values. Since the performance of the former was significantly better, we adopted this strategy for all algorithms. 

QL, PRQL, and SFQL depend on different sets of parameters, as shown in Algorithms 1, 2, and 3. In order to properly configure the algorithms we tried three different values for each parameter and checked the performance of the corresponding agents under each resulting configuration. Specifically, we tried the following sets of values for each parameter: 

|sets of values|for each parameter:||
|---|---|---|
|**Parameter**|**Algorithms**|**Values**|
|_α_<br>_αw_<br>_η_<br>_τ_|QL, PRQL, SFQL<br>SFQL<br>PRQL<br>PRQL|_{_0_._01_,_0_._05_,_0_._1_}_<br>_{_0_._01_,_0_._05_,_0_._1_}_<br>_{_0_._1_,_0_._3_,_0_._5_}_<br>_{_1_,_10_,_100_}_|



The cross-product of the values above resulted in 3 configurations of QL, 27 configurations of PRQL, and 9 configurations of SFQL. The results reported correspond to the best performance of each algorithm, that is, for each algorithm we picked the configuration that lead to the highest average return over all tasks. 

## **B.2 Reacher environment** 

## **B.2.1 Environment** 

The reacher environment is a two-joint torque-controlled robotic arm simulated using the MuJoCo physics engine [26]. It is based on one of the domains used by Lillicrap et al. [12]. This is a particularly appropriate domain to illustrate our ideas because it is straightforward to define multiple tasks (goal locations) sharing the same dynamics. 

The problem’s state space _S ⊂_ R[4] is composed of the angle and angular velocities of the two joints. The two-dimensional continuous action space _A_ was discretized using 3 values per dimension (maximum positive, maximum negative or zero torque for each actuator), resulting in a total of 9 discrete actions. We adopted a discount factor of _γ_ = 0 _._ 9. 

The reward received at each time step was _−δ_ , where _δ_ is the Euclidean distance between the target position and the tip of the arm. The start state at each episode was defined as follows during training: the inner joint angle was sampled from an uniform distribution over [0 _,_ 2 _π_ ], the outer joint was sampled from an uniform distribution over _{−π/_ 2 _, π/_ 2 _}_ , and both angular velocities were set to 0 (during the evaluation phase two fixed start states were used—see below). We used a time step of 0 _._ 02s and episodes lasted for 10s (500 time steps). We defined 12 target locations, 4 of which we used for training and 8 were reserved for testing (see Figure 3). 

## **B.2.2 Algorithms** 

The baseline method used for comparisons in the reacher domain was the DQN algorithm by Mnih et al. [15]. In order to make it possible for DQN to generalize across tasks we provided the target locations as part of the state description. The action-value function _Q_[˜] was represented by a multi-layer perceptron (MLP) with two hidden layers of 256 linear units followed by tanh non-linearities. The 

20 

output of the network was a vector in R[9] with the estimated value associated with each action. The replay buffer adopted was large enough to retain all the transitions seen by the agent—that is, we never removed transitions from the buffer (this helps prevent DQN from “forgetting” previously seen tasks when learning new ones). Each value-function update used a mini-batch of 32 transitions sampled uniformly from the replay buffer, and the associated minimization (line 17 of Algorithm 1) was carried out using the Adam optimizer with a learning rate of 10 _[−]_[3] [30]. 

SFDQN is similar to SFQL, whose pseudo-code is shown in Algorithm 3, with a few modifications to make learning with nonlinear function approximators more stable. The vector of features _**φ** ∈_ R[12] used by SFDQN was composed of the negation of the distances to all target locations.[3] We used a separate MLP to represent each of the four _**ψ**_[˜] _i_ . The MLP architecture was the same as the one adopted with DQN, except that in this case the output of the network was a matrix **Ψ**[˜] _i ∈_ R[9] _[×]_[12] representing _**ψ**_[˜] _i_ ( _s, a_ ) _∈_ R[12] for each _a ∈A_ . This means that the parameters **Z** _i_ in Algorithm 3 should now be interpreted as weights of a nonlinear neural network. The final output of the network was computed as _**ψ**_[˜] _⊤i_ **[w]** _[t]_[, where] **[ w]** _[t][∈]_[R][12][ is an one-hot vector indicating the task] _[ t]_[ currently active.] Analogously to the the target locations given as inputs to DQN, here we assume that **w** _t_ is provided by the environment. Again making the connection with Algorithm 3, this means that line 21 would be skipped. 

> Following Mnih et al. _**ψ**_ ˜ using a target network. [15], in order to make the training of the neural network more stable we updatedThis corresponds to replacing (17) with the following loss: 

**==> picture [332 x 24] intentionally omitted <==**

_πi_ where _**ψ**_[˜] _−_ is a target network that remained fixed during updates and was periodically replaced by _**ψ**_[˜] _πi_ at every 1000 steps (the same configuration used for DQN). For each transition we updated all four MLPs _**ψ**_[˜] _i_ in order to minimize losses derived from (4). As explained in Section 5, the policies _πi_ ( _s_ ) used in (4) were the GPI policies associated with each training task, _πi_ ( _s_ ) _∈_ argmax _a_ max _j_ _**ψ**_[˜] _j_ ( _s, a_ ) _[⊤]_ **w** _i_ . An easy way to modify Algorithm 3) to reflect this update strategy would be to select the action _a[′]_ in line 26 using _πi_ ( _s_ ) and then repeat the block in lines 25–30 for all **w** _i_ , with _i ∈{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ and _i ̸_ = _t_ , where _t_ is the current task. 

## **B.2.3 Experimental setup** 

The agents were trained for 200 000 transitions on each of the 4 training tasks. Data was collected using an _ϵ_ -greedy policy with _ϵ_ = 0 _._ 1 (for SFDQN, this corresponds to lines 12 and 13 of Algorithm 3). As is common in fixed episode-length control tasks, we excluded the terminal transitions during training to make the value of states independent of time, which corresponds to learning continuing policies [12]. 

During the entire learning process we monitored the performance of the agents on all 12 tasks when using an _ϵ_ -greedy policy with _ϵ_ = 0 _._ 03. The results shown in Figure 3 reflect the performance of this policy. Specifically, the return shown in the figure is the sum of rewards received by the 0 _._ 03-greedy policy over two episodes starting from fixed states. Since the maximum possible return varies across tasks, we normalized the returns per task based on the performance of standard DQN on separate experiments (this is true for both training and test tasks). Specifically, we carried out the normalization as follows. First, we ran DQN 30 times on each task and recorded the algorithm’s performance before and after training. Let _G_[¯] _b_ and _G_[¯] _a_ be the average performance of DQN over the 30 runs before and after training, respectively. Then, if during our actual experiments DQN or SFDQN got a return of _G_ , the normalized version of this metric was obtained as _Gn_ = ( _G − G_[¯] _b_ ) _/_ ( _G_[¯] _a − G_[¯] _b_ ). These are the values shown in Figure 3. Visual inspection of videos extracted from the experiments with DQN alone suggests that the returns used for normalization were obtained by near-optimal policies that reach the targets almost directly. 

> 3 In fact, instead of the negation of the distances _−δ_ we used 1 _− δ_ in the definition of both the rewards and the features _**φ** i_ . Since in our domain _δ <_ 1, this change made the rewards always positive. This helps preventing randomly-initialized value function approximations from dominating the ‘max’ operation in (7). 

21 

**==> picture [258 x 131] intentionally omitted <==**

Figure 4: Understanding how much each type of transfer promoted by SFs helps in performance. Results averaged over 30 runs; standard errors are shown as shadowed regions but are almost imperceptible at this scale. PRQL’s results are shown for reference. 

## **C Additional empirical analysis** 

In this section we report empirical results that had to be left out of the main paper due to the space limit. Specifically, the objective of the experiments described here is to provide a deeper understanding of SFQL, in particular, and of SFs, more generally. We use the four-room environment to carry out our empirical investigation. 

## **C.1 Understanding the types of transfer promoted by SFs** 

We start by asking why exactly SFQL performed so much better than QL and PRQL in our experiments (see Figure 2). Note that there are several possible reasons for that to be the case. As shown in (3), SFQL uses a decoupled representation of the value function in which the environment’s dynamics are dissociated from the rewards. If the reward function of a given environment can be non-trivially decomposed in the form (2) assumed by SFQL, the algorithm can potentially build on this knowledge to quickly learn the value function and to adapt to changes in the environment, as discussed in Section 3. In our experiments not only did we know that such a non-trivial decomposition exists, we actually provided such an information to SFQL— either directly, through a handcrafted _**φ**_ , or indirectly, by providing features that allow for _**φ**_ to be recovered exactly. Although this fact should help explain the good results of SFQL, it does not seem to be the main reason for the difference in performance. Observe in Figure 2 how the advantage of SFQL over the other methods only starts to show up in the second task, and it only becomes apparent from the third task on. This suggests that the the algorithm’s good performance is indeed due to some form of transfer. 

But what kind of transfer, exactly? We note that SFQL naturally promotes two forms of transfer. The first one is of course a consequence of GPI. As discussed in the paper, SFQL applies GPI by storing a set of SFs˜ _π_ _**ψ**_[˜] _πi_ . Note though that SFs promote a weaker form of transfer even when only a˜ _π single_ _**ψ**_ exists. To see why this is so, observe that if _**ψ**_ persists from task _t_ to _t_ + 1, instead of arbitrary approximations _Q_[˜] _[π]_ one will have reasonable estimates of _π_ ’s value function under the current **w** ˜ . In other words, _**ψ**_[˜] _π_ will transfer knowledge about _π_ from one task to the other. 

In order to have a better understanding of the two types of transfer promoted by SFs, we carried out experiments in which we tried to isolate as much as possible each one of them. Specifically, we repeated the experiments shown in Figure 2 but now running SFQL with and without GPI (we can turn off GPI by replacing _c_ with _t_ in line 10 of Algorithm 3). 

The results of our experiments are shown in Figure 4. It is interesting to note that even without GPI SFQL initially outperforms PRQL. This is probably the combined effect of the two factors discussed above: the decoupled representation of the value function plus the weak transfer promoted by _**ψ**_[˜] _π_ . Note though that, although these factors do give SFQL a head-start, eventually both algorithms reach the same performance level, as clear by the slope of the respective curves. In contrast, SFQL with GPI consistently outperforms the other two methods, which is evidence in favor of the hypothesis that GPI is indeed a crucial component of the proposed approach. Another evidence in this direction 

22 

**==> picture [63 x 63] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

**==> picture [64 x 64] intentionally omitted <==**

**==> picture [64 x 63] intentionally omitted <==**

**==> picture [64 x 63] intentionally omitted <==**

**==> picture [63 x 64] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

**==> picture [231 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
φ ˜ ( s, a, s [′] ) [⊤] w ˜ t max ψ ˜ i ( s, a ) [⊤] w ˜ t max ψ ˜ i ( s, a ) [⊤] w ˜ t<br>a,i<t a,i≤t<br>**----- End of picture text -----**<br>


Figure 5: Functions computed by SFQL after 200 transitions into three randomly selected tasks (all objects present). 

is given in Figure 5, which shows all the functions computed by the SFQL agent. Note how after only 200 transitions into a new task SFQL already has a good approximation of the reward function, which, combined with the set of previously computed _**ψ**_[˜] _πi_ , with _i < t_ , provide a very informative value function even without the current _**ψ**_[˜] _πt_ . 

## **C.2 Analyzing the robustness of SFs** 

As discussed in the previous section, part of the benefits provided by SFs come from the decoupled representation of the value function shown in (3), which depends crucially on a decomposition of the reward function _**φ**_[˜] ( _s, a, s[′]_ ) _[⊤]_ **w** _≈ r_ ( _s, a, s[′]_ ). In Section 5 we illustrated two ways in which such a decomposition can be obtained: by handcrafting _**φ**_[˜] based on prior knowledge about the environment or by learning it from data. When _**φ**_[˜] is learned it is obviously not reasonable to expect an exact decomposition of the reward function, but even when it is handcrafted the resulting reward model can be only an approximation (for example, the “object detector” used by the agents in the experiments with the four-room environment could be noisy). Regardless of the source of the imprecision, we do not want SFQL in particular, and more generally any method using SFs, to completely break with the addition of noise to _**φ**_[˜] . In Section 5 we saw how an approximate _**φ**_[˜] can in fact lead to very good performance. In this section we provide a more systematic investigation of this matter by analyzing the performance of SFQL with _**φ**_[˜] corrupted in different ways. 

Our first experiment consisted in adding spurious features to _**φ**_ that do not help in any way in the approximation of the reward function. This reflects the scenario where the agent’s set of predictions is a superset of the features needed to compute the reward (see in Section 6 the connection with Sutton et al.’s GVFs, 2011). In order to implement this, we added objects to our environment that always lead to zero reward—that is, even though the SFs _**ψ**_[˜] _π_ learned by SFQL would predict the occurrence of these objects, such predictions would not help in the approximation of the reward function. Specifically, we added to our basic layout 15 objects belonging to 6 classes, as shown in Figure 6, which means that in this case SFQL used a _**φ**_[˜] _∈_ R[10] . In addition to adding spurious features, we also corrupted _**φ**_[˜] by adding to each of its components, in each step, a sample from a normal distribution with mean zero and different standard deviations _σ_ . 

The outcome of our experiment is shown in Figure 7. Overall, the results are as expected, with both spurious features and noise hurting the performance of SFQL. Interestingly, the two types of perturbations do not seem to interact very strongly, since their effects seem to combine in an 

23 

**==> picture [130 x 130] intentionally omitted <==**

Figure 6: Environment layout with additional objects. Spurious objects are represented as diamonds; numbers indicate the classes of the objects. 

**==> picture [318 x 155] intentionally omitted <==**

Figure 7: Analyzing SFQL’s robustness to distortions in _**φ**_[˜] . PRQL’s and QL’s results are shown for reference. Results averaged over 30 runs; standard errors are shown on top of each bar. 

additive way. More important, SFQL’s performance seems to degrade gracefully as a result of either intervention, which corroborate our previous experiments showing that the proposed approach is robust to approximation errors in _**φ**_[˜] . 

## **References** 

- [30] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

- [31] Alexander L. Strehl and Michael L. Littman. A theoretical analysis of model-based interval estimation. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 857–864, 2005. 

24 

