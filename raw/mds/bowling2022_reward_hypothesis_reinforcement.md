_2022-12-21_ 

**==> picture [100 x 26] intentionally omitted <==**

## **Settling the Reward Hypothesis** 

**Michael Bowling**[*,1,2] **, John D. Martin**[*,2,3] **, David Abel**[1] **and Will Dabney**[1] 

*Equal contributions, 1DeepMind, 2Amii, University of Alberta, 3Intel Labs 

**The** _**reward hypothesis**_ **posits that, “all of what we mean by goals and purposes can be well thought of as maximization of the expected value of the cumulative sum of a received scalar signal (reward).” We aim to fully settle this hypothesis. This will not conclude with a simple affirmation or refutation, but rather specify completely the implicit requirements on goals and purposes under which the hypothesis holds.** 

_Keywords: Reinforcement Learning, Utility Theory, Reward Hypothesis, Goals_ 

## **Introduction** 

The _reward hypothesis_ posited by Sutton states that, “all of what we mean by goals and purposes can be well thought of as maximization of the expected value of the cumulative sum of a received scalar signal (reward).” (Littman, 2017; Sutton, 2004; Sutton and Barto, 2018) This statement takes on considerable import if one also accepts McCarthy’s claim that “Intelligence is the computational part of the ability to achieve goals in the world.” (McCarthy, 1998). Together these two statements offer a sort of _sufficiency_ to the study of reinforcement learning (RL), whose agents learn to achieve goals through the maximization of expected future rewards. They imply that to succeed at building AI, it is sufficient to succeed at solving RL.[1] 

Silver et al. (2021) propose the related, _rewardis-enough_ hypothesis, which posits that “intelligence, and all of its associated abilities, can be understood as subserving the maximization of reward.” While the two hypotheses are of course deeply connected, we emphasize that our focus is on Sutton’s earlier _reward hypothesis_ . 

Sutton’s original hypothesis provides an informal starting point from which to question the expressivity of reward. In this vein, Abel et al. (2021) grounded the notion of “goals and purposes” as 

> 1Furthermore, it is possible these two claims show that RL is necessary as well as sufficient. If some artificial system were to be able to achieve all that we mean by goals and purposes, then such a system would have to—at least implicitly—maximize expected cumulative reward. In other words, there must be a reduction between the RL problem and the problem the system solves. 

an ordering over policies and explored whether a Markov reward[2] function could express these orderings. They provided examples showing that a Markov reward is unable to express every such ordering. Their analysis also reveals how using a behavioral defintion of goals can sometimes lead to unsatisfying conclusions. In one example (“steady-state type” failures), an agent needs to experience unrealizable outcomes to achieve their goal. When viewed through the lens of McCarthy’s definition of intelligence, it seems that a behavioral conception of goals deflates the role that computation performs—to one of simply executing a goal’s defining policy, or re-expressing the policy in a different form. Surely intelligence involves more meaningful computation than this? 

Shakerinava and Ravanbakhsh (2022) take a different approach. They ground goals and purposes in preference relations over (distributions of) state-trajectories in a controlled Markov process. In the same spirit of von Neumann-Morgenstern (vNM) utility axioms (von Neumann and Morgenstern, 1953), they propose axioms on the preference relation (including the vNM rationality axioms) which are necessary and sufficient for the preference to be expressed with a Markov reward. Indeed, Shakerinava and Ravanbakhsh (2022) build on work by Pitis (2019) that first analyzed standard objectives of RL from the perspective of decision theory. The work of Pitis can be viewed from two complementary perspectives. First, Pitis provides a normative account for why we should embrace a state-action dependent dis- 

> 2They take a Markov reward function to be one that only depends on the most recent experience of the agent. 

_Corresponding author(s): bowlingm@deepmind.com_ © 2022 DeepMind. All rights reserved 

Settling the Reward Hypothesis 

count factor, as developed by White (2017): A fixed discount cannot capture all preferences we might consider rational. Second, Pitis presents three axioms on top of the vNM axioms that characterize the conditions under which a state-action dependent discount factor can be viewed as rational. 

Our work builds off this pair of insightful approaches by starting with preferences over histories. We abandon strictly Markov processes to consider general stochastic environments and policies in line with recent work by Dong et al. (2021), Lu et al. (2021), and early work on general RL (Lattimore, 2014; Lattimore et al., 2013; Leike, 2016; Majeed, 2021). We introduce a new axiom that generalizes previous axioms from Shakerinava and Ravanbakhsh (2022) and accommodates the discounted reward, average reward (Mahadevan, 1996), and episodic settings. Our approach posits “goals and purposes” as preceding environment dynamics, giving space for the agent’s computational role of learning representations and behavior necessary to accomplish a goal. Using our new axiom along with the standard vNM rationality axioms, we provide a treatment of the reward hypothesis in both the setting that goals are the subjective desires of the agent and in the setting where goals are the objective desires of an agent designer. Altogether, our account does not give a simple affirmation or refutation of the reward hypothesis, but rather aims to completely specify the implicit requirements on goals and purposes under which the hypothesis holds. 

## **The Reward Hypothesis** 

As we aim to settle the reward hypothesis, the first step in doing so is to formalize what it claims, and to do so in as much generality as possible. We do this by stating a series of assumptions for each of the phrases in the claim. 

## **Goals as Preferences** 

We ground “all of what we mean by goals and purposes” with a binary preference relation expressing preference for one outcome over another. 

The core of agent interaction is the cycle of repeat- 

edly observing the environment and then taking action to affect the environment. Let O be a finite set of observations, and A a finite set of actions.[3] A history is then a sequence _𝑜_ 1 _, 𝑎_ 1 _, 𝑜_ 2 _, 𝑎_ 2 _, . . ._ with _𝜀_ as the empty history of zero length. We define the set of histories of length _𝑛_ ∈ ℕ≥0 as def H _𝑛_ = (O × A) _[𝑛]_ , and all finite length histories def as H =[�][∞][For] _[ℎ]_[∈H][and][transition] _𝑛_ =1[H] _[𝑛]_[.] _𝑡_ ∈O × A, let _𝑡_ · _ℎ_ ∈H be the history with _𝑡_ prepended to _ℎ_ . 

In deterministic settings, preferences are expressed over histories. However, when the environment and agent behavior are stochastic, we will want to consider distributions over histories, Δ(H ).[4] Given _𝐴, 𝐵_ ∈ Δ(H ) and _𝑝_ ∈ [0 _,_ 1], let _𝑝𝐴_ + (1 − _𝑝_ ) _𝐵_ ∈ Δ(H ) be the distribution that samples a history from _𝐴_ with probability _𝑝_ and _𝐵_ with (1 − _𝑝_ ). For _𝐴_ ∈ Δ(H ) and _𝑡_ ∈O × A, let _𝑡_ · _𝐴_ ∈ Δ(H ), be the distribution where _𝑡_ is prepended to a history sampled from _𝐴_ . 

The reward hypothesis posits a “received scalar signal”. This could mean that the posited scalar reward signal is present in the agent’s received observation, or can be computed by the agent from it. Alternatively, it could mean that there is an additional scalar signal provided to the agent by an external observer. We call the first setting _subjective goals_ , as the posited reward signal can be constructed from the agent’s subjective observation, and the latter case correspondingly _objective goals_ . We first develop our main result with the subjective goals setting, but will later broaden the result to objective goals. 

**Assumption 1** (Subjective Goals) **.** _“All of what we mean by goals and purposes” can be expressed as a binary preference relation on distributions over finite histories. For 𝐴, 𝐵_ ∈ Δ(H ) _, we write 𝐴_ ≿ _𝐵 if 𝐴 is weakly preferred to 𝐵, meaning that either 𝐴 is strictly preferred 𝐵, or the two are indifferently preferred._ 

Notice that our notion of “goals and purposes” make no reference to the environment. Goals 

> 3We assume O and A are finite, but suspect the results generalize to the case where they are simply countable sets. 

> 4We will use Δ(S) to refer to the set of all probability distributions with finite support over a countable set S. 

2 

Settling the Reward Hypothesis 

are stated as desirable histories, whereas the environment will act to constrain what histories and distributions over histories are possible. An agent’s behavior, along with the environment, then induces a distribution over histories. Formally, given an environment _𝑒_ : H → Δ(O) and policy _𝜋_ : H × O → Δ(A), let _𝐷𝑛[𝜋]_[be the distribu-] tion over H _𝑛_ induced by _𝑒_ and _𝜋_ . 

**==> picture [209 x 49] intentionally omitted <==**

While _𝐷𝑛[𝜋]_[depends on the environment] _[𝑒]_[, we do] not parameterize it as such since _𝑒_ typically is fixed throughout. We assume preferences over agent policies are then consistent with the distributions over histories that they induce. When comparing policies, we write _𝜋_ 1 ≿ _𝑔 𝜋_ 2 to mean _𝜋_ 1 is weakly preferred to _𝜋_ 2 under the goal _𝑔_ . 

**Assumption 2** (Policy Preferences) **.** _We weakly prefer 𝜋_ 1 ≿ _𝑔 𝜋_ 2 _in 𝑒 if and only if there exists 𝑁 such that 𝐷𝑛[𝜋]_[1][≿] _[𝐷] 𝑛[𝜋]_[2] _[for all][𝑛]_[≥] _[𝑁][.]_ 

This notion of eventually preferring one policy’s history distribution to another allows us the generality of goals and purposes that can be achieved in a defined time frame as well as those of a continuing nature. This assumption is just one simple way of handling infinite sequences, but it is not the only one. For instance, Sobel (1975) and Pitis (2019) propose alternative resolutions (horizon continuity and countable transitivity—see details in cited resources). 

## **Maximizing Cumulative Sums** 

We now consider what the reward hypothesis says about these goals and purposes. First, let us examine what is entailed by the “maximization of the cumulative sum” of a scalar reward. This is clearly the domain of reinforcement learning, of which this problem takes a number of forms, including episodic total reward with absorbing states, infinite sum of discounted rewards, and average reward. We want to unify all of these formalisms in what could be meant by maximizing cumulative sums of rewards, and do so employing White’s 

generalization of transition-dependent discounting (White, 2017). When comparing policies under a reward _𝑟_ , we write _𝜋_ 1 ≿ _𝑟 𝜋_ 2. 

**Assumption 3** (Cumulative Sum of Rewards) **.** _The “maximization of the expected value of the cumulative sum of a received scalar signal (reward)” means that there is a reward function 𝑟_ : O × A → ℝ _and transition-dependent discount function 𝛾_ : O × A → [0 _,_ 1] _, such that we weakly prefer 𝜋_ 1 ≿ _𝑟 𝜋_ 2 _under our reward if and only if there exists 𝑁 such that 𝑉𝑛[𝜋]_[1] ≥ _𝑉𝑛[𝜋]_[2] _for all 𝑛_ ≥ _𝑁, where_ 

**==> picture [219 x 33] intentionally omitted <==**

Notice how (1) simultaneously captures objectives for the average reward, discounted reward, and episodic settings. If _𝛾_ ( _𝑡_ ) = 1 for some _𝑜, 𝑎_ pair _𝑡_ , the objective corresponds to a typical total reward or average reward setting (even if the sum of the reward is not bounded). If _𝛾_ ( _𝑡_ ) = _𝛾<_ 1 is constant for all _𝑡_ , then the objective corresponds to a discounted reward objective. If _𝛾_ ( _𝑡_ ) = 0 infinitely often then the objective can correspond to an episodic setting. In the Appendix, we expand on the average reward case and show how the notion of the expected cumulative sum eventually being larger allows us to capture multiple kinds of optimality. 

We can now state what we take the reward hypothesis to mean under all of these assumptions. 

**Assumption 4** (Reward Hypothesis) **.** _What the reward hypothesis means by “well thought of” is that for any preference relation on distributions of histories there exists 𝑟 and 𝛾 such that 𝜋_ 1 ≿ _𝑔 𝜋_ 2 _if and only if 𝜋_ 1 ≿ _𝑟 𝜋_ 2 _._ 

In what follows, we explore if this is true or false, or more precisely, what might be required of possible goals and purposes, i.e., our preference relation, for the reward hypothesis to hold. 

## **Rationality Axioms** 

The vNM axioms provide necessary and sufficient conditions for a preference relation to be express- 

3 

Settling the Reward Hypothesis 

ible as the expectation of some scalar-valued function of outcomes. The “expected value of the cumulative sum” of rewards is central to the reward hypothesis, so we present these axioms here along with the corresponding vNM utility theorem. In the statement of these and additional axioms, H is any set of finite length sequences of some countable set of transitions _𝑇_ (e.g., _𝑇_ may be O × A as in the subjective goals case of Assumption 1). 

We next state each of the four vNM axioms alongside some brief intuition. 

**Axiom 1** (Completeness) **.** _For all 𝐴, 𝐵_ ∈ Δ(H ) _, 𝐴_ ≿ _𝐵 or 𝐵_ ≿ _𝐴 (or both, if 𝐴_ ∼ _𝐵)._ 

Completeness requires that the preference ordering make _some_ judgment about any pair of distributions. Note that the preference _could_ simply convey indifference: we might be equally satisfied with an apple and a banana. This is distinct from having no preference at all (Chang (2015) discusses the incomparability of virtues like “justice” and “mercy”). Note that there are alternative sets of axioms that simply remove completeness, as developed by Aumann (1962). 

**Axiom 2** (Transitivity) **.** _For all 𝐴, 𝐵, 𝐶_ ∈ Δ(H ) _, if 𝐴_ ≿ _𝐵_ ≿ _𝐶, then 𝐴_ ≿ _𝐶._ 

Transitivity is relatively straightforward: no coherent goal can involve cyclical preferences. 

**Axiom 3** (Independence) **.** _For all 𝐴, 𝐵, 𝐶_ ∈ Δ(H ) _and 𝑝_ ∈ (0 _,_ 1) _, 𝐴_ ≿ _𝐵 if and only if_ 

**==> picture [145 x 11] intentionally omitted <==**

Independence was historically viewed as an unlikely axiom, and one that led to skepticism about vNM’s initial results (Machina, 1990). However, it does convey a relatively powerful intuition, once it is unpacked. Consider the following example. Suppose we must choose between an Apple, a Banana, or Chocolate. We are asked: (1) Do you prefer one Apple to one Banana? and (2) Consider two coins of the same weight which, when flipped can yield {H: Apple, T: Chocolate}, and {H: Banana, T: Chocolate}—which coin do you prefer to flip? Independence requires that for _all_ coin weights, your answer to (1) and (2) must be 

the same. In other words, if you truly prefer an Apple to a Banana, then the _chance_ of procuring the Apple and Banana should not change this preference (when the other alternatives are the same). Independence is deeply connected to many alternative objectives in RL such as risk-aversion and multi-objective RL, which we discuss in more detail shortly. 

**Axiom 4** (Continuity) **.** _For all 𝐴, 𝐵, 𝐶_ ∈ Δ(H ) _if 𝐴_ ≿ _𝐵_ ≿ _𝐶, then there exists 𝑝_ ∈ [0 _,_ 1] _such that,_ 

**==> picture [86 x 11] intentionally omitted <==**

Continuity demands the existence of a break-even point when one becomes indifferent to a mixture of outcomes that are individually more or less preferred. At what precise coin weight does one become indifferent between a Banana and a distribution of Apple and Chocolate? 

These four axioms comprise the typical account of rational preferences under vNM’s theory. We next state the classical vNM result. 

**Theorem 1** (von Neumann-Morgenstern Utility Theorem) **.** _A binary preference relation on_ Δ(H ) _satisfies axioms 1-4 if and only if there exists a utility function 𝑢_ : Δ(H ) → ℝ _such that,_ 

**==> picture [219 x 25] intentionally omitted <==**

_and 𝑢 is unique up to positive affine transformations._ 

In other words, there exists a utility function whose expectation for any distribution over histories is consistent with the preference relation. 

These rationality axioms are sufficient for our interpretation of the reward hypothesis (Assumption 4) to trivially hold with no further assumptions. Simply define the “received” reward for experiencing transition _𝑡_ following history _ℎ_ as the change in utility from appending transition _𝑡_ to _ℎ_ , written as _𝑟_ ( _𝑡_ ; _ℎ_ ) = _𝑢_ ( _ℎ_ · _𝑡_ ) − _𝑢_ ( _ℎ_ ). However, this reward function is not, in general, computable from the agent’s received observation as it depends on the entire history. This definition of reward function may not even be computable by 

4 

Settling the Reward Hypothesis 

a bounded agent or a bounded external observer as, in general, it requires complete memory of the history. We will need to add an additional axiom for the reward hypothesis to hold for a Markov reward; that is, a reward that is received or computable from the agent’s most immediate experience. 

## **A New Axiom: Temporal** _𝛾_ **-** 

Here we derive a new axiom that ensures the existence of Markov rewards and implicitly specifies the type of objective faced by an agent. We start from an observation about how preferences can still encode statements about magnitude, even without reducing them to a scalar value. 

Let _𝐴, 𝐵, 𝐶, 𝐷_ ∈ Δ(H ) with _𝐴_ ≿ _𝐵_ and _𝐶_ ≿ _𝐷_ . Suppose we wanted to state that _𝐴_ is preferred over _𝐵 by the same amount_ as _𝐶_ is preferred over _𝐷_ . If we could encode preferences as utilities, then we could write 

**==> picture [128 x 11] intentionally omitted <==**

We could rewrite this as 

**==> picture [132 x 10] intentionally omitted <==**

**==> picture [171 x 27] intentionally omitted <==**

Notice that now we are just comparing utilities of two distributions. We could equivalently state this entirely through the preference relation: 

**==> picture [111 x 9] intentionally omitted <==**

Furthermore, suppose we wanted to state that _𝐴_ is preferred to _𝐵_ by a multiplicative factor _𝛼>_ 0 of how much _𝐶_ is preferred to _𝐷_ . Again, if we had an equivalent utility function we could write 

**==> picture [152 x 27] intentionally omitted <==**

**==> picture [203 x 56] intentionally omitted <==**

So we can write the same concept entirely within the preference relation. 

Now if we consider a transition _𝑡_ ∈ _𝑇_ and two distributions over histories _𝐴, 𝐵_ ∈ Δ(H ), we can use the above to state that _𝑡_ · _𝐴_ is preferred to _𝑡_ · _𝐵_ by a multiplicative factor _𝛾_ ( _𝑡_ ) of the amount _𝐴_ is preferred to _𝐵_ : 

**==> picture [219 x 18] intentionally omitted <==**

This brings us to what we call the Temporal _𝛾_ - Indifference axiom. 

**Axiom 5** (Temporal _𝛾_ -Indifference) **.** _For all 𝐴, 𝐵_ ∈ Δ(H ) _and transitions 𝑡_ ∈ _𝑇,_ 

**==> picture [208 x 38] intentionally omitted <==**

Notice this axiom is parameterized by a discount function _𝛾_ : _𝑇_ → [0 _,_ 1] defined on transitions _𝑇_ . 

The axiom essentially requires that _𝑡_ · _𝐴_ is preferred to _𝑡_ · _𝐵_ by a multiplicative factor _𝛾_ ( _𝑡_ ) of how much _𝐴_ is preferred to _𝐵_ . This fact is illustrated in the following example. 

**Example 1.** _Suppose 𝛾_ ( _𝑡_ ) = 1 _for all transitions 𝑡_ ∈ _𝑇. Then, the temporal indifference axiom states that for all ℎ_ 1 _, ℎ_ 2 ∈H _and transitions 𝑡_ ∈ _𝑇,_ 

**==> picture [168 x 10] intentionally omitted <==**

_In other words, given any two histories to be experienced with equal probability, the agent is indifferent to which history gets prepended with a transition, regardless of the transition. No matter which history is prepended with 𝑡, the transition 𝑡 must be experienced. So the indifference is requiring the agent has no preference over which history is delayed, even if one history is highly preferred to the other._ 

We now state our main result. All proofs are included in the Appendix. 

**Theorem 2** (Markov Reward Theorem) **.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 if and only if there exists a utility function 𝑢_ : Δ(H ) → 

5 

Settling the Reward Hypothesis 

ℝ _, a reward function 𝑟_ : _𝑇_ → ℝ _, and transitiondependent discount function 𝛾_ : _𝑇_ → [0 _,_ 1] _, such_ def _that 𝑢_ ( _𝜀_ ) = 0 _, and_ 

**==> picture [122 x 16] intentionally omitted <==**

_under the following conditions._ 

**==> picture [184 x 11] intentionally omitted <==**

**==> picture [212 x 11] intentionally omitted <==**

_where 𝑟 is unique up to a positive scale factor, and 𝛾 is the function for which Axiom 5 is satisfied._ 

In other words, there exist a Markov reward function such that the expected sum of rewards under a particular transition-dependent discount factor is consistent with the preference relation. Furthermore, we can show there exists an efficient algorithm that constructs the reward function and discount factor from a preference relation that satisfies Axioms 1–5 (See Algorithm 1 in the Appendix for additional details.). 

Additionally, notice the form the objective takes (e.g. discounted reward, episodic total reward, average reward) is determined by the preference relation and how it satisfies the Temporal _𝛾_ -Indifference axiom. This is what ultimately dictates _𝛾_ ( _𝑡_ ). 

## **Objective Goals** 

The results thus far assume that the preferences and rewards of interest originate from the same perspective—that is, the agent doing the maximizing is the same as the agent holding the preferences. In practice, we often find ourselves in a different setting in which the relevant preferences originate from an _agent designer_ that has a desired goal or purpose in mind for a separate _learning agent_ to pursue (Alice and Bob in work by Abel et al. (2021), or the “designer” and “agent” in work by Singh et al. (2009)). In this section we adapt our previous assumptions to show how the results of Theorem 2 apply more broadly—to arbitrary sequences that contain the designer’s experiences. This is what we refer to as the _objective goals_ case. Indeed, this setup includes common 

cases from the literature where preferences are expressed in numerous ways: as demonstrations of desired behaviors (Ng et al., 2000), partial orders over a set of trajectories (Wirth et al., 2017), or through a generic interaction process with the designer (Leike et al., 2018). 

In the objective goals setting, the designer experiences a stream of observations ¯ _𝑜_ ∈ O[¯] . These form a distinct process which is potentially related the observation stream of the agent. For instance, the designer may observe more than the agent: O ⊂ O[¯] . In other cases, O[¯] may include the agent’s actions. The designer provides the agent with a learning signal that reflects its preferences on distributions over histories _ℎ_[¯] _𝑡_ = ¯ _𝑜_ 1 _,_ ¯ _𝑜_ 2 _, . . . ,_ ¯ _𝑜𝑡_ , where each ¯ _𝑜𝑖_ ∈ O[¯] . We let H[¯] _𝑛_ be all histories of length def _𝑛_ and H[¯] =[�][∞] _𝑛_ =0 H[¯] _𝑛_ be all finite length histories over designer observations.[5] In what follows, we suppose the designer maintains a preference relation over distributions from Δ(H[¯] ), then we adapt our assumptions so the results of Theorem 2 apply to this setting. 

**Assumption 5** (Objective Goals) **.** _“All of what we mean by goals and purposes” can be expressed as a binary preference relation on distributions over finite histories of designer observations_ Δ(H[¯] ) _._ 

We have two choices here for defining the agent’s interface to the environment. First, the designer can provide the rewards _𝑟_ and the discounts _𝛾_ as separate inputs to the agent. Second, the designer can provide rewards that are already discounted, 

**==> picture [165 x 34] intentionally omitted <==**

We adopt the second view to maintain the standard agent-environment interface, but note that the former view might yield an alternative plausible account. 

**Assumption 6** (Cumulative Sum of Objective Rewards) **.** _The “maximization of the expected value of the cumulative sum of a received scalar signal (reward)” means that there is a reward function 𝑟_ : O[¯] → ℝ _and transition-dependent discount function 𝛾_ : O[¯] → [0 _,_ 1] _, such that a designer prefers_ 

5Note that we could choose to augment these histories with actions, but leave them out for brevity. 

6 

Settling the Reward Hypothesis 

_𝜋_ 1 ≿ _𝑟 𝜋_ 2 _under the reward 𝑟 if and only if there exists 𝑁 such that 𝑉𝑛[𝜋]_[1] _> 𝑉𝑛[𝜋]_[2] _for all 𝑛_ ≥ _𝑁, where 𝑉𝑛[𝜋]_[=] _[𝐸]_ �� _𝑛𝑖_ =1 _[𝑟][𝑖]_ � _._ 

With this we can now restate our interpretation of the reward hypothesis for the objective goals case. What the reward hypothesis means by “well thought of” is that for any binary preference relation on distributions of a designer’s histories, there exists an already discounted _𝑟_ , as defined in (2), such that _𝜋_ 1 ≿ _𝑔 𝜋_ 2 if and only if _𝜋_ 1 ≿ _𝑟 𝜋_ 2. 

## **History and Related Work** 

We next discuss relevant literature from across RL and economics. 

## **Economics** 

Economics has been studying the nature of rational behavior for centuries. In the 1700s, Gabriel Cramer and Daniel Bernoulli independently formulated what is now called the Expected Utility Hypothesis (Machina, 1990) in response to the “St. Petersburg Paradox” (Martin, 2011) articulated by Daniel’s cousin Nicholas Bernoulli (1738). The Expected Utility Hypothesis says, roughly, that individuals “might maximize the expectation of ‘utility’ rather than of monetary value.” (Machina, 1990). Centuries later, Ramsey (1926) provided the first formal axiomatic treatment of expected utility, which would later be refined by von Neumann and Morgenstern (1953) to form the now widely adopted foundations of decision theory. Following this development, an expansive body of research has explored how to account for other aspects of rationality, including uncertainty (Kreps and Porteus, 1978), time (Koopmans, 1960; Koopmans et al., 1964), and computation (Lewis, 1985; Richter and Wong, 1999; Rustem and Velupillai, 1990). 

with a focus on the discount factor, _𝛾_ . As discussed in the introduction, Pitis provides a normative account for why we should embrace a state-action dependent discount factor, as developed by White (2017): A fixed discount cannot capture all preferences we might consider rational. Second, Pitis presents three axioms on top of the vNM axioms that characterize the conditions under which a state-action dependent discount factor can be viewed as rational. These axioms bear some resemblance to aspects of our formalism: For instance, Pitis’ countable transitivity axiom also addresses the issue of infinite experiences, like our Assumption 2. 

Shakerinava and Ravanbakhsh (2022) focus on utility theory for a variety of controlled MDPs. They formalize the notion of “goals and purposes” using rational preference relations. And using expected utility theory, they explicate the preconditions (i.e. axioms) under which a reward function is guaranteed to exist in each type of MDP. Our work takes inspiration from this approach to formalize “goals and purposes” in a general sequential decision making setting. Furthermore, we can prove that our new Temporal _𝛾_ -Indifference axiom generalizes two of their axioms. Here we state their axioms using our notation. 

**Axiom 6** (Memoryless (Shakerinava and Ravanbakhsh, 2022)) **.** _For all 𝑡_ ∈ _𝑇 and 𝐴, 𝐵_ ∈ Δ(H ) 

**==> picture [112 x 9] intentionally omitted <==**

**Theorem 3.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 with 𝛾_ ( _𝑡_ ) ∈ [0 _,_ 1] _if and only if Axioms 1-4 and the Memoryless axiom are satisfied._ 

**Axiom 7** (Additivity (Shakerinava and Ravanbakhsh, 2022)) **.** _For all ℎ_ 1 _, ℎ_ 2 ∈H _, 𝐴, 𝐵, 𝐶, 𝐷_ ∈ Δ(H ) _and 𝑝_ ∈ [0 _,_ 1] _,_ 

**==> picture [216 x 28] intentionally omitted <==**

## **Utility Theory for Sequential Decision Making** 

More recently, Pitis (2019) and Shakerinava and Ravanbakhsh (2022) examine the connection between RL and classical utility theory. 

Pitis (2019) explored the relationship between the vNM axioms and the typical objectives of RL, 

**Theorem 4.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 with 𝛾_ ( _𝑡_ ) = 1 _if and only if Axioms 1-4 are satisfied as well as Additivity._ 

In contrast to our work, Shakerinava and Ravanbakhsh (2022) are not predominately concerned 

7 

Settling the Reward Hypothesis 

with “settling” the reward hypothesis. Rather, they use the hypothesis as a template to frame existential questions about reward functions for various flavors of controlled MDPs. In their work, goals and purposes are fundamentally connected to the environment; they suppose outcomes over which preferences are held are the product of a fully-observable process given for reward construction. As previously mentioned, our work decouples these concepts by treating goals and purposes in isolation of the environment dynamics. Even in this more general setting, we show there exists an efficient algorithm to construct rewards using a preference relation that satisfies Axioms 1–5 (See Algorithm 1 in the Appendix). 

Separately, Sunehag and Hutter (2011, 2015) study what constitutes a _rational reinforcement learning agent_ . More concretely, in both works, Sunehag and Hutter suppose the environment and reward function are defined, and set out to characterize what kinds of agents might we consider rational. In their first work (Sunehag and Hutter, 2011), they provide a series of properties that characterize what it means for an RL agent to be rational. These properties bear some similarity to the vNM axioms, but are agent-side properties rather than implicit requirements on the structure of goals or rewards themselves. In follow up work Sunehag and Hutter (2015) focus specifically on the rationality of optimistic agents. That is, given a reward function and environment, they contrast agents that are strictly expected utility maximizers with those that act optimistically. They give a full characterization of rational agency that justifies the use of optimism for exploration, showing that expected utility maximization on its own can be strictly worse than optimistic behavior. 

## **The Limited Expressivity of Markov Reward** 

Abel et al. (2021) study the expressivity of reward in Markovian environments. In particular, they suppose the environment is characterized by a finite state space and transition function, and assume that preferences over objects defined with respect to the environment are given. These preferences come in three forms: (1) A set of acceptable policies, (2) A partial ordering on policies, or (3) A partial ordering on fixed-length state-action 

trajectories. Each of these preference types are defined with respect to the environment’s _state space_ , S, that is known to be sufficient to support a Markovian transition function (and thus, _𝑒_ : S × A → Δ(S)). For example, in the case of (1), the policy space is defined as all deterministic mappings of the form _𝜋_ : S →A. Then, a choice of the first preference type is just a selection of acceptable policies. Under these three types, Abel et al. show that there are restrictions on what kinds of preferences can be codified in terms of a reward function that is Markov with respect to the same state space. Specifically, they point out two styles of counterexample: (1) the _steady state type_ , in which preferences have bearing on impossible outcomes, and (2) the _entailment type_ , in which the desirability of an action choice depends on behavior elsewhere in the environment. 

We next show how the two styles of counterexample from Abel et al. play out in the context of our results. We find that the steady state type violates one of our assumptions, and the entailment type violates an axiom. In this sense, we provide an _explanatory_ account about why these counterexamples contained preferences that could not be translated into a Markov reward function. 

**Steady State.** First, recall the steady state counterexample, pictured in Figure 1a. The environment in question contains two states and two actions, with transitions between the states as pictured. The given preference over policies asserts that the only acceptable policy chooses _𝑎_ 2 in the left state, but _𝑎_ 1 in the right. This is a counterexample in the sense that there is no Markov reward function that ensures the policy _𝜋_ 12 : { _𝑠_ 0 ↦→ _𝑎_ 1 | _𝑠_ 1 ↦→ _𝑎_ 2}, has higher value than _𝜋_ 11 : { _𝑠_ 0 ↦→ _𝑎_ 1 | _𝑠_ 1 ↦→ _𝑎_ 1}, since both policies never reach state _𝑠_ 1. 

Under our formalism, these policies would induce equivalent outcome distributions and thus be interchangeably preferred. We begin with preferences over outcomes of the kind suggested by Assumption 1. That is, in the two-state environment described, our preferences are over sequences of state-action pairs. Recall that under Assumption 2, we understand a preference over policies _𝜋_ 1 ≿ _𝑔 𝜋_ 2 to mean that there exists a time after 

8 

Settling the Reward Hypothesis 

**==> picture [395 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
a1<br>a2 a1 a2<br>a2<br>s0 s1 s0 s1<br>a1 a2<br>a1<br>(a) Steady State Case (b) Entailment Case<br>**----- End of picture text -----**<br>


Figure 1 | The two counterexamples from Abel et al. (2021). In the steady state case, the set of acceptable policies contains only the policy that executes _𝑎_ 2 in the left, and _𝑎_ 1 in the right. In the entailment case, the two acceptable policies are those that choose a _different_ action across the two states. 

which we always prefer the distribution over outcomes produced by _𝜋_ 1 to _𝜋_ 2. Thus, when we consider the steady state counter example, we can see that Assumption 2 is violated: We prefer _𝜋_ 1 to _𝜋_ 2 even though they induce _identical_ distributions _𝐷𝑛[𝜋]_[1][and] _[𝐷] 𝑛[𝜋]_[2][.][It is in this sense that this] counterexample to the expressivity of reward is an instance of a broader principle we have codified in this pair of assumptions. 

**Entailment.** The second kind of counterexample deals with cases in which the value of one policy necessarily entails something about the value of another policy. For instance, in the example pictured in Figure 1b, the two acceptable policies are those that take a different action in each of the two states. So, _𝜋_ 12 : { _𝑠_ 0 ↦→ _𝑎_ 1 | _𝑠_ 1 ↦→ _𝑎_ 2} and _𝜋_ 21 : { _𝑠_ 0 ↦→ _𝑎_ 2 | _𝑠_ 1 ↦→ _𝑎_ 1} are both desirable because they each take opposing actions across the two states. In follow up work, Abel et al. (2022) demonstrate that a simple state-construction procedure can resolve the counterexample. In our framing, where precisely do the preferences of this entailment type go wrong? Such preferences directly violate Axiom 5, the new axiom. To see why, consider the two (Dirac) distributions: _𝐴_ = _𝑠_ 2 _, 𝑎_ 2 and _𝐵_ = _𝑠_ 2 _, 𝑎_ 1. Let _𝑡_ = _𝑠_ 1 _, 𝑎_ 1. That is, the composite distributions formed are _𝑡_ · _𝐴_ = _𝑠_ 1 _, 𝑎_ 1 _, 𝑠_ 2 _, 𝑎_ 2 and _𝑡_ · _𝐵_ = _𝑠_ 1 _, 𝑎_ 1 _, 𝑠_ 2 _, 𝑎_ 1. However, there is no choice of _𝛾_ ( _𝑡_ ) for which the indifference expressed by the Axiom holds, as the preference requires that _𝐴_ ≿ _𝐵_ . 

## **Challenges to the Reward Hypothesis** 

We next summarize common challenges to the reward hypothesis. Additionally, we consider whether our formalization of the hypothesis can provide any further insight into these arguments. 

## **Human Irrationality** 

To say that an agent is rational is to say that it acts according to reason. In other words, an agent makes decisions that are in its best interest, according to a clear and precise set of preferences. Decades ago it was common to view humans as rational agents.[6] Though it wasn’t until the work of Johnson-Laird (1983), and Kahneman and Tversky that scientists began to understand the extent to which human beings deviate from this model (Kahneman and Tversky, 1982, 1984; Kahneman et al., 1982; Tversky and Kahneman, 1983). For instance, Johnson-Laird demonstrated that people do not employ mental logic when solving problems. Kahneman and Tversky showed in a series of dramatic experiments how humans tend to prefer outcomes that avoid risk, even when such outcomes are suboptimal according to vNM expected utility theory. Indeed, Hayden and Niv (2021) argue against the presence of so called “economic values” in the brain. Many take these observations as direct evidence of how vNM utility theory is fundamentally flawed at providing a complete account of human behavior. 

Expected utility theory may not provide a full or even an accurate theory of human behavior, 

> 6Bertrand Russel speculated that this perspective may have originated from Aristotle. 

9 

Settling the Reward Hypothesis 

but fortunately this is not needed to settle the reward hypothesis. Settling the reward hypothesis is about the expression of goals, not the behaviors that emerge in their pursuit. Our results prove the existence of a Markov reward signal under the presumption that all goals and purposes can be rationally expressed. 

## **Multiple Objectives** 

Another natural reaction to the reward hypothesis is to suspect that collapsing all of the nuance that might go into “purpose” down to a single scalar seems difficult, if not impossible.[7] Suppose we are interested in designing an autonomous taxi to take passengers between the airport and the university. We would like the taxi to balance between safety, timeliness, and energy use. But how precisely do we make these trade-offs, and can we really reduce the nuances of their tradeoffs down to a single scalar? 

This challenge often yields a variant called multiobjective or multi-criteria decision making that has been studied extensively in the literature. Hausner (1953) drops continuity (Axiom 4) in order to generalize the vNM results to the multidimensional setting. Gábor et al. (1998) propose multi-criteria RL in MDPs and establish initial conditions for importing classical results from scalar valued rewards such as the existence of stationary policies and the Bellman equation. More recently, Miura (2022) explicitly focus on the expressivity of multi-dimensional reward, enriching the result’s of Abel et al. (2021). In particular, Miura shows that multi-dimensional Markov reward functions are strictly more expressive than scalar Markov reward functions in MDPs. However, we note that this expressivity comes with the cost of violating at least one of the axioms— we describe this in more detail shortly. Pitis et al. (2022) make a similar argument, and prove that some multi-objective problems cannot be collapsed to a scalar objective. 

> 7Indeed, this challenge is closely related to the puzzle of the incomparability (or incommeasurability) of value (Chang, 2015) often discussed in ethics. 

**Constrained MDPs.** In a Constrained MDP, an agent’s goal is to maximize the expected sum of a base scalar reward function, subject to additional constraints on the expected sums of other independent reward functions. It has been shown that Constrained MDPs are more expressive than single-reward MDPs (Szepesvári, 2020). Szepesvári shows that it is generally not possible to reduce a Constrained MDP through “scalarization” and solve it with typical MDP techniques. This is viewed as a challenge to the reward hypothesis. 

Despite the additional expressivity, one can find Constrained MDPs that violate both independence (Axiom 3) and continuity (Axiom 4). Consider the example pictured in Figure 2. The environment contains two actions, _𝐿_ and _𝑅_ , whose combinations produce four different histories, which we denote _𝐿𝐿, 𝐿𝑅, 𝑅𝐿, 𝑅𝑅_ . The accumulated payoffs under the base reward _𝑟_ 1 and secondary reward _𝑟_ 2 are also shown. 

Suppose the constrained objective involves maximizing expected utility under _𝑟_ 1 while demanding expected utility under _𝑟_ 2 be non-negative. Under this objective, distributions of feasible histories are preferred to those which are infeasible. Consider two such distributions _𝐴_ =[1][1] 2 _[𝑅𝐿]_[+] 2 _[𝑅𝑅]_[and] _𝐵_ = _𝐿𝐿_ . We have _𝐴_ ≿ _𝐵_ , since the first distribution is feasible and the second is not. 

Independence asserts that the preference remains unchanged when _𝐴_ and _𝐵_ are equally-mixed with any other distribution. However, in this example, the preference reverses when mixed with _𝐶_ = _𝑅𝑅_ . That is[1][1][1][In][this][case,][both] 2 _[𝐴]_[+] 2 _[𝐶]_[≾][1] 2 _[𝐵]_[+] 2 _[𝐶]_[.] distributions are feasible, but the first achieves less expected utility under the base reward _𝑟_ 1. 

A similar example can be used for continuity. This time consider the distributions _𝐴_ =[1][1] 2 _[𝑅𝐿]_[+] 2 _[𝑅𝑅]_[,] _𝐵_ = 1[1][and] _[𝐶]_[=] _[𝑅𝑅]_[.][We][have] _[𝐴]_[≿] 2 _[𝐿𝑅]_[+] 2 _[𝑅𝑅]_[,] _𝐵_ ≿ _𝐶_ , because _𝐴_ is feasible with the highest expected base utility, _𝐵_ is feasible but achieves less utility than _𝐴_ , and _𝐶_ is infeasible. For this selection, there is no break even point _𝑝_ ∈ (0 _,_ 1) that would make an agent indifferent between _𝐴_ and the mixture _𝑝𝐵_ + (1 − _𝑝_ ) _𝐶_ . The latter is always infeasible. 

Beyond violating our particular definition of goals 

10 

Settling the Reward Hypothesis 

**==> picture [279 x 77] intentionally omitted <==**

**----- Start of picture text -----**<br>
History Total r 1 Total r 2<br>LL 1 -1<br>LR 0 -1<br>RL 1 -1<br>RR 0 1<br>LL LR RL RR<br>**----- End of picture text -----**<br>


Figure 2 | An environment used to illustrate how constrained MDPs can violate independence and continuity. Two actions, _𝐿_ and _𝑅_ , produce four histories shown in the table above. Also shown are the cumulative rewards of each history. In our example, the objective is to maximize expected utility under _𝑟_ 1 such that zero expected utility occurs under _𝑟_ 2. 

and purposes, Constrained MDPs allow for goals that violate independence in a way that is inconsistent with an agent’s lived experience. We expand on this observation in the Appendix. 

**Risk.** Risk-sensitive objectives applied to the returns generated by a policy can, in general, cause the optimal policy to be non-Markovian (Bellemare et al., 2023). This can be readily seen in the case of maximizing a variance-penalized mean return, where the agent first experiences some uncontrolled randomness that produces two different rewards (e.g. 0 or 1) and then faces the choice of two actions with different rewards (again, 0 or 1) allowing it to choose between maximizing value or reducing variance. For sufficiently large variance penalties the optimal policy will be to choose the action leading to the opposite reward of what it had previously experienced. However, this is not possible for Markov policies. 

Observe that when all optimal policies are nonMarkov, such as in this example, there does not exist any Markov reward function with the same optimal policy under a risk-neutral objective. This is because the optimal policy will necessarily be Markovian. As a result, we can conclude that at least one of our assumptions or axioms must have been violated. In the above example, the issue is a violation of Axiom 5 and can be overcome by augmenting the state using the objective goals formulation. 

## **Conclusion** 

We have here provided a conclusive account summarizing the implicit conditions required for the reward hypothesis. We separate such conditions into _assumptions_ , that center around interpretations of the hypothesis, and _axioms_ , that express specific formal properties about rational preference relations of all that one could mean by goals and purposes. Our main result (Theorem 2) states that, under Assumptions 1-4, the reward hypothesis for Markov reward functions holds if and only if Axioms 1-5 are satisfied. This result completely specifics the requirements on preferences under which the hypothesis holds. We further explore consequences of our new framing and results, including a variant from the viewpoint of the designer, an efficient constructive algorithm that translates rational preferences into a reward function, and discussion of how this axiomatic perspective can sharpen our understanding of alternative RL objectives such as constrained MDPs and risk. 

## **Acknowledgements** 

The authors gratefully acknowledge how the interactions and feedback of their colleagues have shaped this paper. In particular, we would like to thank Andrè Barreto and Doina Precup for their thoughtful comments on an early draft of the paper, and Bernardo Ávila Pires for helpful conversations. 

11 

Settling the Reward Hypothesis 

## **References** 

- D. Abel, W. Dabney, A. Harutyunyan, M. K. Ho, M. L. Littman, D. Precup, and S. Singh. On the expressivity of Markov reward. In _Advances in Neural Information Processing Systems_ , 2021. 

- D. Abel, A. Barreto, M. Bowling, W. Dabney, S. Hansen, A. Harutyunyan, M. K. Ho, R. Kumar, M. L. Littman, D. Precup, and S. Satinder. Expressing non-Markov reward to a Markov agent. _Multidisciplinary Conference on Reinforcement Learning and Decision Making_ , 2022. 

- R. J. Aumann. Utility theory without the completeness axiom. _Econometrica: Journal of the Econometric Society_ , pages 445–462, 1962. 

- M. G. Bellemare, W. Dabney, and M. Rowland. _Distributional Reinforcement Learning_ . MIT Press, 2023. `http://www` _._ `distributionalrl` _._ `org` . 

- D. Bernoulli. Specimen theoriae novae de mensura sortis (trans. in 1954 as exposition of a new theory on the measurement of risk). _Econometrica_ , 22(1):23–36, 1738. 

- A. R. Cassandra, L. P. Kaelbling, and M. L. Littman. Acting optimally in partially observable stochastic domains. In _Proceedings of the AAAI Conference on Artificiall Intelligence_ , 1994. 

- R. Chang. Value incomparability and incommensurability. _The Oxford handbook of value theory_ , pages 205–224, 2015. 

- S. Dong, B. Van Roy, and Z. Zhou. Simple agent, complex environment: Efficient reinforcement learning with agent states. _arXiv preprint arXiv:2102.05261_ , 2021. 

- Z. Gábor, Z. Kalmár, and C. Szepesvári. Multicriteria reinforcement learning. In _Proceedings of the International Conference on Machine Learning_ , volume 98, 1998. 

- M. Hausner. Multidimensional utilities (rev). Technical report, RAND CORP SANTA MONICA CA, 1953. 

- B. Y. Hayden and Y. Niv. The case against economic values in the orbitofrontal cortex (or 

anywhere else in the brain). _Behavioral Neuroscience_ , 135(2):192, 2021. 

- P. N. Johnson-Laird. _Mental models: Towards a cognitive science of language, inference, and consciousness_ . Number 6. Harvard University Press, 1983. 

- D. Kahneman and A. Tversky. The psychology of preferences. _Scientific American_ , 246(1):160– 173, 1982. 

- D. Kahneman and A. Tversky. Choices, values, and frames. _American psychologist_ , 39(4):341, 1984. 

- D. Kahneman, S. P. Slovic, P. Slovic, and A. Tversky. _Judgment under uncertainty: Heuristics and biases_ . Cambridge university press, 1982. 

- R. L. Keeney, H. Raiffa, and R. F. Meyer. _Decisions with multiple objectives: preferences and value trade-offs_ . Cambridge university press, 1993. 

- T. C. Koopmans. Stationary ordinal utility and impatience. _Econometrica: Journal of the Econometric Society_ , pages 287–309, 1960. 

- T. C. Koopmans, P. A. Diamond, and R. E. Williamson. Stationary utility and time perspective. _Econometrica: Journal of the Econometric Society_ , pages 82–100, 1964. 

- D. M. Kreps and E. L. Porteus. Temporal resolution of uncertainty and dynamic choice theory. _Econometrica: journal of the Econometric Society_ , pages 185–200, 1978. 

- T. Lattimore. _Theory of General Reinforcement Learning_ . PhD thesis, The Australian National University, 2014. 

- T. Lattimore, M. Hutter, and P. Sunehag. The sample-complexity of general reinforcement learning. In _Proceedings of the International Conference on Machine Learning_ , 2013. 

- J. Leike. _Nonparametric general reinforcement learning_ . PhD thesis, The Australian National University, 2016. 

- J. Leike, D. Krueger, T. Everitt, M. Martic, V. Maini, and S. Legg. Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_ , 2018. 

12 

Settling the Reward Hypothesis 

- A. A. Lewis. On effectively computable realizations of choice functions: Dedicated to professors kenneth j. arrow and anil nerode. _Mathematical Social Sciences_ , 10(1):43–80, 1985. 

- M. Littman. The reward hypothesis. `https://www` _._ `coursera` _._ `org/lecture/ fundamentals-of-reinforcementlearning/michael-littman-thereward-hypothesis-q6x0e` , 2017. 

- X. Lu, B. Van Roy, V. Dwaracherla, M. Ibrahimi, I. Osband, and Z. Wen. Reinforcement learning, bit by bit. _arXiv preprint arXiv:2103.04047_ , 2021. 

- M. J. Machina. Expected utility hypothesis. In _Utility and probability_ , pages 79–95. Springer, 1990. 

- S. Mahadevan. Average reward reinforcement learning: Foundations, algorithms, and empirical results. _Machine learning_ , 22(1):159–195, 1996. 

- S. J. Majeed. _Abstractions of General Reinforcement Learning_ . PhD thesis, The Australian National University, 2021. 

- R. Martin. The st. petersburg paradox. _Stanford Encyclopedia of Philosophy_ , 2011. 

- J. McCarthy. What is artificial intelligence. _URL: http://www-formal. stanford. edu/jmc/whatisai. html_ , 1998. 

- S. Miura. On the expressivity of multidimensional Markov reward. In _In RLDM Workshop on Reinforcement Learning as a Model of Agency_ , 2022. 

- A. Y. Ng, S. Russell, et al. Algorithms for inverse reinforcement learning. In _Proceedings of the International Conference on Machine Learning_ , pages 663–670, 2000. 

- S. Pitis. Rethinking the discount factor in reinforcement learning: A decision theoretic approach. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , 2019. 

- S. Pitis, D. Bailey, and J. Ba. Rational multiobjective agents must admit non-markov reward representations. 2022. 

- F. P. Ramsey. Truth and probability. In _Readings in formal epistemology_ , pages 21–45. Springer, 1926. 

- M. K. Richter and K.-C. Wong. Computable preference and utility. _Journal of Mathematical Economics_ , 32(3):339–354, 1999. 

- B. Rustem and K. Velupillai. Rationality, computability, and complexity. _Journal of Economic Dynamics and Control_ , 14(2):419–432, 1990. 

- M. Shakerinava and S. Ravanbakhsh. Utility theory for sequential decision making. In _Proceedings of the International Conference on Machine Learning_ , 2022. 

- D. Silver, S. Singh, D. Precup, and R. S. Sutton. Reward is enough. _Artificial Intelligence_ , 299: 103535, 2021. 

- S. Singh, R. L. Lewis, and A. G. Barto. Where do rewards come from? In _Proceedings of the Annual Conference of the Cognitive Science Society_ , 2009. 

- M. J. Sobel. Ordinal dynamic programming. _Management science_ , 21(9):967–975, 1975. 

- P. Sunehag and M. Hutter. Axioms for rational reinforcement learning. In _International Conference on Algorithmic Learning Theory_ , pages 338–352. Springer, 2011. 

- P. Sunehag and M. Hutter. Rationality, optimism and guarantees in general reinforcement learning. _The Journal of Machine Learning Research_ , 16(1):1345–1390, 2015. 

- R. S. Sutton. The reward hypothesis. `http://incompleteideas` _._ `net/ rlai` _._ `cs` _._ `ualberta` _._ `ca/RLAI/ rewardhypothesis` _._ `html` , 2004. 

- R. S. Sutton and A. G. Barto. _Reinforcement learning: An introduction_ . MIT press, 2018. 

- C. Szepesvári. Constrained MDPs and the reward hypothesis. `https: //readingsml` _._ `blogspot` _._ `com/2020/ 03/constrained-mdps-and-rewardhypothesis` _._ `html` , 2020. 

13 

Settling the Reward Hypothesis 

- A. Tversky and D. Kahneman. Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. _Psychological review_ , 90 (4):293, 1983. 

- J. von Neumann and O. Morgenstern. _Theory of Games and Economic Behavior_ . Princeton University Press, third edition, 1953. 

- M. White. Unifying task specification in reinforcement learning. In _Proceedings of the Thirty-fourth International Conference on Machine Learning_ , 2017. 

- C. Wirth, R. Akrour, G. Neumann, J. Fürnkranz, et al. A survey of preference-based reinforcement learning methods. _Journal of Machine Learning Research_ , 18(136):1–46, 2017. 

14 

Settling the Reward Hypothesis 

## **Proof of Main Theorem** 

**Theorem 2** (Markov Reward Theorem) **.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 if and only if there exists a utility function 𝑢_ : Δ(H ) → ℝ _, a reward function 𝑟_ : _𝑇_ → ℝ _, and transition-dependent_ def _discount function 𝛾_ : _𝑇_ → [0 _,_ 1] _, such that 𝑢_ ( _𝜀_ ) = 0 _, and_ 

**==> picture [123 x 16] intentionally omitted <==**

_under the following conditions._ 

_1._ ∀ _𝐴, 𝐵_ ∈ Δ(H ) _𝐴_ ≿ _𝐵_ ⇔ _𝑢_ ( _𝐴_ ) ≥ _𝑢_ ( _𝐵_ ) _,_ 

_2._ ∀([�] _𝑖[𝑝] 𝑖[ℎ] 𝑖_[)][ ∈][Δ(][H][)] _[ 𝑢]_[(][�] _𝑖[𝑝] 𝑖[ℎ] 𝑖_[) =][ �] _𝑖[𝑝] 𝑖[𝑢]_[(] _[ℎ] 𝑖_[)] _[,]_ 

_where 𝑟 is unique up to a positive scale factor, and 𝛾 is the function for which Axiom 5 is satisfied._ 

_Proof._ We first show the axioms imply the existence of a Markov reward. By Theorem 1 and axioms 1-4, we can select _𝑢_ : Δ(H ) → ℝ, such that _𝑢_ ( _𝜀_ ) = 0, leaving _𝑢_ unique up to a positive scale factor. def Define _𝑟_ ( _𝑡_ ) = _𝑢_ ( _𝑡_ ). From Axiom 5 and choosing _ℎ_ 1 = _ℎ_ and _ℎ_ 2 = _𝜀_ , 

**==> picture [266 x 25] intentionally omitted <==**

Applying Theorem 1 (first consequence 1 then consequence 2) we get, 

**==> picture [296 x 26] intentionally omitted <==**

Multiplying by _𝛾_ ( _𝑡_ ) + 1, we get, 

**==> picture [173 x 28] intentionally omitted <==**

We now show that any Markov reward satisfies the axioms. Due to Theorem 1 we know Axioms 1-4 are satisfied. We also know, for all _ℎ_ ∈H , 

**==> picture [117 x 11] intentionally omitted <==**

so, 

**==> picture [119 x 11] intentionally omitted <==**

Hence for all _ℎ_ 1 _, ℎ_ 2 ∈H 

**==> picture [235 x 11] intentionally omitted <==**

Rearranging we get, 

**==> picture [207 x 11] intentionally omitted <==**

Dividing all terms by _𝛾_ ( _𝑡_ ) + 1, 

**==> picture [332 x 26] intentionally omitted <==**

Applying Theorem 1 (first consequence 2 then consequence 1), 

**==> picture [379 x 42] intentionally omitted <==**

thus Axiom 5 is satisfied. 

15 

Settling the Reward Hypothesis 

## **Proofs of Relationship to Shakerinava and Ravanbakhsh (2022)** 

**Theorem 3.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 with 𝛾_ ( _𝑡_ ) ∈ [0 _,_ 1] _if and only if Axioms 1-4 and the Memoryless axiom are satisfied._ 

_Proof._ Starting from the Temporal _𝛾_ -Indifference Axiom, we use the vNM theorem under a specific choice of history to reduce the utility function to a positive affine form. The converse is proved with a similar argument to Mike’s proof of the Markov Reward Theorem. 

=⇒ Take some _𝑡_ from O×A, and let _𝛾_ ( _𝑡_ ) _>_ 0. Temporal _𝛾_ -Indifference states that for any distributions _𝐴_ and _𝐵_ from Δ(H ) 

**==> picture [288 x 26] intentionally omitted <==**

The vNM utility theorem guarantees this indifference has a utility representation: 

**==> picture [317 x 42] intentionally omitted <==**

Let _𝐵_ = _𝜖_ , and define _𝑢_ ( _𝜖_ ) ≜ 0, _𝑟_ ( _𝑡_ ) ≜ _𝑢_ ( _𝑡_ · _𝜖_ ) so we obtain 

**==> picture [123 x 11] intentionally omitted <==**

By Lemma 2 we know _𝑢_ ( _𝑡_ · _𝐴_ ) is strategically equivalent to. _𝑢_ ( _𝐴_ ), meaning _𝐴_ ∼ ( _𝑡_ · _𝐴_ ). Therefore, for all distributions _𝐴, 𝐵_ ∈ Δ(H ) 

**==> picture [132 x 10] intentionally omitted <==**

⇐= The Memoryless Axiom states that for all _𝑡_ ∈ _𝑇_ and _𝐴, 𝐵_ ∈ Δ(H ) 

**==> picture [132 x 10] intentionally omitted <==**

This means that _𝐴_ and _𝐵_ are strategically equivalent to ( _𝑡_ · _𝐴_ ) and ( _𝑡_ · _𝐵_ ) respectively. By Lemma 2, their utility representations are affine functions of the same rewards _𝑟_ ( _𝑡_ ) and discounts _𝛾_ ( _𝑡_ ): 

**==> picture [320 x 11] intentionally omitted <==**

Simple algebra shows that 

**==> picture [393 x 105] intentionally omitted <==**

The last line follows from the vNM utility theorem. 

**Definition 1** (Strategic Equivalence) **.** _Two utility functions 𝑢_ 1 _and 𝑢_ 2 _are strategically equivalent, denoted 𝑢_ 1 ∼ _𝑢_ 2 _, if and only if they imply the same preference ranking for any two distributions._ 

16 

Settling the Reward Hypothesis 

**Lemma 1** (Keeney et al. (1993)) **.** _If 𝑢_ 1 ∼ _𝑢_ 2 _, there exists two constants 𝑎 and 𝑏>_ 0 _st._ 

**==> picture [133 x 12] intentionally omitted <==**

_Proof._ Let _𝑥_ be any value in [ _𝑥_ 0 _, 𝑥_[∗] ], and let _𝑥_ ∼ ( _𝑥_[∗] _, 𝑐, 𝑥_ 0) so that 

**==> picture [201 x 10] intentionally omitted <==**

Letting _𝑖_ = 2 and solving for _𝑐_ we get 

**==> picture [284 x 45] intentionally omitted <==**

Substituting this value of _𝑐_ in when _𝑖_ = 1 gives the desired result. 

**Lemma 2** (Positive Affine Equivalence) **.** _For any 𝑡 and 𝑡_[′] _from_ O × A _,_ 

**==> picture [250 x 11] intentionally omitted <==**

_for all 𝐴_ ∈ Δ(H ) _._ 

_Proof._ The first implication follows from repeated application of Lemma 1. The converse follows from algebra. 

=⇒ : To apply Lemma 1, fix _𝑡_[′] and denote the utility function conditioned on it _𝑢_ ( _𝑡_[′] · _𝐴_ ). Similarly, denote the utility function at every _𝑡_ ∈{ _𝑡_ 1 _, 𝑡_ 2 _,_ · · ·} = O × A to be _𝑢_ ( _𝑡𝑖, 𝐴_ ). Then for each _𝑡𝑖_ , Lemma 1 guarantees there are constants _𝑎𝑖_ and _𝑏𝑖 >_ 0 relating _𝑢_ ( _𝑡𝑖, 𝐴_ ) and _𝑢_ ( _𝑡_[′] · _𝐴_ ). Define the functions 

**==> picture [133 x 28] intentionally omitted <==**

It follows that for any _𝑡_ ∈O × A, _𝑢_ ( _𝑡_ · _𝐴_ ) = _𝑟_ ( _𝑡_ ) + _𝛾_ ( _𝑡_ ) _𝑢_ ( _𝑡_[′] · _𝐴_ ) for all _𝐴_ ∈ Δ(H ). 

⇐= : For some _𝑡_ and _𝑡_[′] , consider the ordering of utilities over all _𝐴_ ∈{ _𝐴 𝑗_ } _𝑗_ ≥1 = Δ(H ): 

**==> picture [203 x 12] intentionally omitted <==**

Scaling by a positive constant _𝛾_ ( _𝑡_ ) preserves the ordering, and so does shifting by _𝑟_ ( _𝑡_ ): 

**==> picture [227 x 44] intentionally omitted <==**

Therefore _𝑢_ ( _𝑡_ · _𝐴_ ) ∼ _𝑢_ ( _𝑡_[′] · _𝐴_ ) for all _𝐴_ . □ 

**Theorem 4.** _A binary preference relation on_ Δ(H ) _satisfies Axioms 1-5 with 𝛾_ ( _𝑡_ ) = 1 _if and only if Axioms 1-4 are satisfied as well as Additivity._ 

_Proof._ The first direction follows from Independence and Lemma 3. The converse is reduced to the Memoryless Axiom, then the remainder of the argument follows from Theorem 3. 

=⇒ Take any _𝑡_ ∈O × A, and _𝐴, 𝐵, 𝐶, 𝐷_ ∈ Δ(H ) for which 

**==> picture [192 x 11] intentionally omitted <==**

17 

Settling the Reward Hypothesis 

By the Independence Axiom, the preference remains unchanged after mixing distributions with ( _𝑡_[′] · _𝑋_ ) by an amount _𝑞_ ∈ [0 _,_ 1]: 

**==> picture [231 x 28] intentionally omitted <==**

If we take _𝑞𝑝_ = (1 − _𝑞_ ), then we can form uniform compound distributions of ( _𝑡,_ ·) and ( _𝑡_[′] · _𝑋_ ): 

**==> picture [373 x 74] intentionally omitted <==**

The last line follows from Lemma 3, which takes Temporal Indifference as its precondition. Finally, we invoke the Independence axiom to remove ( _𝑡_ · _𝑋_ ) mixture: 

**==> picture [194 x 12] intentionally omitted <==**

⇐= For any _𝑡, 𝑡_[′] ∈ _𝑇_ , and _𝐴, 𝐵, 𝐶, 𝐷_ ∈ Δ(H ), the Additivity Axiom states 

**==> picture [410 x 12] intentionally omitted <==**

This reduces to the Memoryless Axiom if we restrict _𝑡_ to O × A, and take _𝑡_[′] = _𝜖_ and _𝐶_ = _𝐷_ : 

**==> picture [406 x 44] intentionally omitted <==**

The last line follows from independence on _𝐷_ . 

Finally, Theorem 3 established that the Memoryless Axiom holds if and only if the Temporal _𝛾_ - Indifference Axiom holds. Therefore, the remainder of the proof follows from that. □ 

**Lemma 3.** _If Temporal 𝛾-Indifference holds when 𝛾_ = 1 _, then for any 𝑡, 𝑡_[′] ∈O × A _, and 𝐴, 𝑋_ ∈ Δ(H ) _,_ 

**==> picture [194 x 24] intentionally omitted <==**

_Proof._ Take some _𝑡_ from O × A, and let _𝛾_ ( _𝑡_ ) = 1. Temporal _𝛾_ -Indifference states that for any distributions _𝐴_ and _𝑋_ 

**==> picture [148 x 23] intentionally omitted <==**

This applies to any _𝑡_ , so it must apply to any other _𝑡_[′] from O × A with _𝛾_ ( _𝑡_[′] ) = 1: 

**==> picture [330 x 23] intentionally omitted <==**

The vNM utility theorem guarantees these preferences have a utility representation, meaning: 

**==> picture [414 x 23] intentionally omitted <==**

18 

Settling the Reward Hypothesis 

Regardless of whether a distribution involves _𝑡_ or _𝑡_[′] , the difference between utilities will be equal: 

**==> picture [395 x 117] intentionally omitted <==**

## **Preferences in the Average Reward Setting** 

The notion of the cumulative sum eventually being larger allows us to capture settings where the series is convergent (i.e., lim _𝑛_ →∞ _𝑉𝑛[𝜋]_[exists) as well as cases where it is not, such as average reward; if] one policy has higher average reward, then its finite sum must eventually be larger. For this analysis we will assume without loss of generality that the transition-dependent discount _𝛾_ ( _𝑡_ ) = 1 ∀ _𝑡_ ∈ _𝑇_ . 

This last point is made formal in the following proposition, where the average reward for policy _𝜋_ is _𝜇𝜋_ ≜ lim _𝑛_ →∞[1] _𝑛[𝑉] 𝑛[𝜋]_[.] 

**Proposition 1.** _For any policies 𝜋𝐴, 𝜋𝐵 whose average rewards 𝜇 𝐴, 𝜇 𝐵 exist, if 𝜇 𝐴 > 𝜇 𝐵, then there exists an 𝑁 such that 𝑉𝑛[𝐴][> 𝑉] 𝑛[𝐵][for all][𝑛]_[≥] _[𝑁][.]_ 

_Proof._ Assume _𝜇 𝐴 > 𝜇 𝐵_ exist. According to the definition of a limit, for any _𝜀𝐴, 𝜀𝐵 >_ 0, there exists some _𝑁𝐴_ and _𝑁𝐵_ such that 

**==> picture [248 x 23] intentionally omitted <==**

for all _𝑘_ ≥ _𝑁𝐴_ and _𝑚_ ≥ _𝑁𝐵_ . 

Choose _𝜀𝐴_ = _𝜀𝐵_ =[1] 2[(] _[𝜇][𝐴]_[−] _[𝜇][𝐵]_[)] _[>]_[0 and let] _[𝑁]_[=][max][{] _[𝑁][𝐴][, 𝑁][𝐵]_[}][,][so the above inequalities hold for all] _𝑛_ ≥ _𝑁_ . If you negate the second inequality and add them together, then for all _𝑛> 𝑁_ , 

**==> picture [166 x 102] intentionally omitted <==**

Thus, _𝑉𝑛[𝐴][> 𝑉] 𝑛[𝐵]_[.] 

**==> picture [8 x 7] intentionally omitted <==**

We can show a similar result for the specialized bias-optimal case of average reward. **Definition 2** (Bias Value) **.** _The relative difference in total reward gathered is_ 

**==> picture [131 x 34] intentionally omitted <==**

19 

Settling the Reward Hypothesis 

**Proposition 2.** _For any policies 𝜋𝐴, 𝜋𝐵 whose average rewards 𝜇 𝐴, 𝜇 𝐵 exist, if 𝜇 𝐴_ = _𝜇 𝐵 and the bias values exist with 𝑉[𝐴] > 𝑉[𝐵] , then there exists an 𝑁 such that 𝑉𝑛[𝐴][> 𝑉] 𝑛[𝐵][for all][𝑛]_[≥] _[𝑁][.]_ 

_Proof._ Assume _𝜇 𝐴_ = _𝜇 𝐵_ exist as well as the bias optimal values _𝑉[𝐴] > 𝑉[𝐵]_ . 

**==> picture [331 x 34] intentionally omitted <==**

Distributing the expectation, breaking the summation, and recognizing the expected _𝑛_ -step sums as _𝑉𝑛[𝐴]_[=] **[ E]**[[][�] _[𝑛] 𝑖_ =1 _[𝑅] 𝑖[𝐴]_[] and] _[ 𝑉] 𝑛[𝐵]_[=] **[ E]**[[][�] _[𝑛] 𝑖_ =1 _[𝑅] 𝑖[𝐵]_[], we have] 

**==> picture [290 x 17] intentionally omitted <==**

According to the definition of a limit, for any _𝜀𝐴, 𝜀𝐵 >_ 0, there exists some _𝑁𝐴_ and _𝑁𝐵_ such that 

**==> picture [277 x 14] intentionally omitted <==**

for all _𝑘_ ≥ _𝑁𝐴_ and _𝑚_ ≥ _𝑁𝐵_ . 

Choose _𝜀𝐴_ = _𝜀𝐵_ =[1] 2[(] _[𝑉][𝐴]_[−] _[𝑉][𝐵]_[)] _[>]_[0][and][let] _[𝑁]_[=][max][{] _[𝑁][𝐴][, 𝑁][𝐵]_[}][,][so][that][for][all] _[𝑛]_[≥] _[𝑁]_[,][the][above] inequalities hold. If you negate the second inequality and add them together, then for all _𝑛> 𝑁_ , 

**==> picture [224 x 23] intentionally omitted <==**

Since _𝜇 𝐴_ = _𝜇 𝐵_ , 

**==> picture [165 x 103] intentionally omitted <==**

Thus, _𝑉𝑛[𝐴][> 𝑉] 𝑛[𝐵]_[.] 

**==> picture [8 x 6] intentionally omitted <==**

## **A Constructive Algorithm** 

We now develop an algorithm that can construct the realizing reward function given a preference relation that is known to satisfy Axioms 1-5. Algorithm 1 uses the preference relation to sort outcomes, then computes rewards and two-step utilities by scaling their rankings relative to their break-even point with the best and worst outcomes. With this information, the discount factor can be computed in closed-form. Below we summarize the procedures for using a preference relation to sort and scale outcomes. 

PrefSort (Algorithm 2) is a procedure for sorting a set of outcomes according to their preference. Our implementation takes in a preference relation and set of outcomes T . The procedure returns a tuple of outcomes which are sorted in ascending order, according to R, with MergeSort. 

20 

Settling the Reward Hypothesis 

**Algorithm 1** Reward and Discount Design 

Input: R = {≺ _,_ ≾ _,_ ≻ _,_ ≿ _,_ ∼}. Output: _𝑟_ : A × O → ℝ, _𝛾_ : A × O → [0 _,_ 1]. 1: T =PrefSort(R _,_ A × O ∪{ _𝜀_ }) 2: P =PrefScale(R _,_ T _, 𝜖_ ) 3: Let _𝑖𝜀_ be the index of _𝜀_ in T . 4: **for** _𝑖_ ∈{1 _,_ · · · _,_ |T |} **do** 5: **if** _𝑖_ = _𝑖𝜀_ **then** 6: _𝑟_ ( _𝑡𝑖_ ) = 0 7: **else** 8: _𝑟_ ( _𝑡𝑖_ ) = _𝑝𝑖_ (1 − _𝑖𝜀_ ) + (1 − _𝑝𝑖_ )(1 − _𝑖𝜀/_ |T |) 9: U =PrefSort(R _,_ T × T ) 10: Q =PrefScale(R _,_ T × T _, 𝜖_ ) 11: Let _𝑘𝜀_ be the index of _𝜀_ in U. 12: **for** _𝑘_ ∈{1 _,_ · · · _,_ |U|} **do** 13: **if** _𝑘_ = _𝑘𝜀_ **then** 14: _𝑢_ ( _𝜏𝑘_ ) = 0 15: **else** 16: _𝑢_ ( _𝜏𝑘_ ) = _𝑞𝑘_ (1 − _𝑘𝜀_ ) + (1 − _𝑞𝑘_ )(1 − _𝑘𝜀/_ |U|) 17: **for** _𝑖_ ∈{1 _,_ · · · _,_ |T |} **do** 18: _𝜏_ ← ( _𝑡𝑖, 𝑡_ |T |) 19: _𝛾_ ( _𝑡𝑖_ ) ← ( _𝑢_ ( _𝜏_ ) − _𝑟_ ( _𝑡𝑖_ )) _/𝑟_ |T | 20: **return** _𝑟_ , _𝛾_ 

PrefScale (Algorithm 3) is a procedure to determine the relative degree of preference between outcomes. In our implementation, it takes a preference relation, a tuple of preference-sorted outcomes T , and a tolerance parameter _𝜀_ ∈ (0 _,_ 1]. The procedure returns a set of numerical scale factors that reflect the degree to which each outcome is preferred relative to best and worst outcomes. Our implementation assigns scale factors using a binary line search informed by the continuity axiom Axiom 4. The inner loop of the line search terminates when the difference between subsequent factors differ less than a pre-specified _𝜀_ . 

The complexity of Algorithm 1 only depends on |A| and |O|: we make two calls to PrefSort, each requiring _𝑂_ ( _𝑛_ log _𝑛_ ) operations, where _𝑛_ = |A|×|O| in the first case, and _𝑛_ = (|A|×|O|)[2] in the second case. The two calls to PrefScale require _𝑂_ ( _𝑛_ ) operations. In the same way as before, _𝑛_ = |A|×|O| in the first case, and _𝑛_ = (|A|×|O|)[2] in the second case. We then run three for loops, the largest of which iterating through |U|= (|A|×|O|)[2] elements. Thus, the total run-time is _𝑂_[�] (|A|×|O|)[2][�] . 

## **Additional Comments on Objective Goals** 

As a special case, consider when the environment can be modeled as a Partially Observable MDP (POMDP, Cassandra et al. (1994)), and suppose that the designer observes the environment states and the agent’s actions, O[¯] = S × A, so that histories are _ℎ_[¯] = _𝑎_ 1 _, 𝑠_ 1 _, 𝑎_ 2 _, 𝑠_ 2 _, . . ._ . If Axioms 1-5 apply to the designer’s preference relation on this distributions over histories, where the reference to transition (O × A) in Axiom 5 now refers to (S × A), then Theorem 2 extends to reward functions _𝑟_ : (S × A) → ℝ and discount functions _𝛾_ : (S × A) → [0 _,_ 1]. 

Note that the in the objective goals setting, the designer’s states may encode more than necessary 

21 

Settling the Reward Hypothesis 

**Algorithm 2** PrefSort 

Input: R _,_ T = ( _𝑡_ 1 _,_ · · · _, 𝑡𝑛_ ). Output: Sorted T . 1: **if** _𝑛_ ≤ 1 **then** 2: **output** T 3: L _,_ K ← () 4: **for** _𝑖_ = 1 _,_ · · · _, 𝑛_ **do** 5: **if** _𝑡𝑖_ ≿ _𝑡_ ⌊ _𝑛/_ 2⌋ **then** 6: K ← concat(K _, 𝑡𝑖_ ) 7: **else** 8: L ← concat(L _, 𝑡𝑖_ ) 9: L ←PrefSort(L) 10: K ←PrefSort(K) 11: T ← concat(L _,_ K) 12: **output** T 

**Algorithm 3** PrefScale 

Input: R _,_ T = ( _𝑡_ 1 ≾ _𝑡_ 2 ≾ · · ·) _, 𝜖_ ∈ (0 _,_ 1]. Output: P = { _𝑝_ 1 _,_ · · · _, 𝑝_ |T |}. 1: **for** _𝑖_ ∈{1 _,_ · · · _,_ |T |} **do** 2: _𝑝𝑖[𝑘]_[−][1] ← 1 3: Δ ← 2 _𝜖_ 4: **while** Δ ≥ _𝜖_ **do** 5: **if** _𝑡𝑖_ ≻ _𝑝𝑖[𝑘]_[−][1] _𝑡_ 1 + (1 − _𝑝𝑖[𝑘]_[−][1] ) _𝑡_ |T | **then** 6: _𝑝𝑖[𝑘]_[←][3] _[𝑝] 𝑖[𝑘]_[−][1] _/_ 2 7: **else if** _𝑡𝑖_ ≺ _𝑝𝑖[𝑘]_[−][1] _𝑡_ 1 + (1 − _𝑝𝑖[𝑘]_[−][1] ) _𝑡_ |T | **then** 8: _𝑝𝑖[𝑘]_[←] _[𝑝] 𝑖[𝑘]_[−][1] _/_ 2 9: **else** 10: **break** 11: Δ ←| _𝑝𝑖[𝑘]_[−] _[𝑝] 𝑖[𝑘]_[−][1] | 12: _𝑝𝑖[𝑘]_[−][1] ← _𝑝𝑖[𝑘]_ 13: _𝑝𝑖_ = _𝑝𝑖[𝑘]_[−][1] 14: **output** P. 

to produce Markov state transitions. For example, they could encode a reward bundle (Abel et al., 2022), a finite state machine defining an otherwise non-Markov reward. This should allow us to define a variant of Axiom 5 that only needs to be satisfied when state transitions consist of POMDP states produced with any other finite state machine that transitions on POMDP transitions. In other words, preferences that can be expressed as reward bundles are captured by this extended axiom. 

## **Additional Comments on Multiple Objectives** 

Here we examine the temporal nature of handling multiple objectives in view of an agent’s lived experience. We present an additional axiom with which we may want to constrain goals and purposes. Let _𝐴_ [ _ℎ_ → _𝐵_ ] refer to the distribution over histories where all histories with non-zero support in _𝐴_ that share the prefix _ℎ_ are removed, and their support shifted to _ℎ_ · _𝐵_ . 

22 

Settling the Reward Hypothesis 

**Axiom 8** (Sequential Consistency) **.** _For all 𝐴, 𝐵, 𝐶_ ∈ Δ(H ) _and ℎ_ ∈H _, ℎ_ · _𝐴_ ≻ _ℎ_ · _𝐵 if and only if 𝐶_ [ _ℎ_ → _𝐴_ ] ≻ _𝐶_ [ _ℎ_ → _𝐵_ ] _._ 

In other words, extensions to a hypothetical history that are more aligned with some goal or purpose do not change if that hypothetical history becomes certain. In behavioral terms, goal-aligning behavior following a possible future is the same as goal-aligning behavior following that future occurring. Alternatively, goal-aligning behavior after some history should not depend on hypothetical alternative pasts that did not come about. 

This is related to notions of _dynamic inconsistency_ in behavioural economics[8] : one may prefer to receive $110 in 101 days to $100 in 100 days, and yet when 100 days passes the same person may now prefer $100 to waiting one day for $110 (i.e., human preferences are often not dynamically consistent). It is straightforward to see that Independence (Axiom 3) implies Sequential Consistency (Axiom 8). However, while one may reject Independence, it seems much more difficult to reject Sequential Consistency, i.e., the goal-alignment of extensions of histories change if the history becomes certain. Notice, however, that Constrained MDP formulations for capturing multiple objectives, in fact, violate this more specific axiom. 

> 8It is best to think of “time passing” in our formalization as “the past” at some time _𝑡_ becoming certain — fixing _ℎ𝑡_ ∈H _𝑡_ — and so the policy and environment specify distributions over histories whose support has _ℎ𝑡_ as a prefix. 

23 

