# **Learning Options via Compression** 

**Yiding Jiang** _[∗]_ Carnegie Mellon University `yidingji@cs.cmu.edu` 

**Evan Zheran Liu** _[∗]_ Stanford University `evanliu@cs.stanford.edu` 

**Benjamin Eysenbach J. Zico Kolter Chelsea Finn** Carnegie Mellon University Carnegie Mellon University Stanford University `beysenba@cs.cmu.edu zkolter@cs.cmu.edu cbfinn@cs.stanford.edu` 

## **Abstract** 

Identifying statistical regularities in solutions to some tasks in multi-task reinforcement learning can accelerate the learning of new tasks. Skill learning offers one way of identifying these regularities by decomposing pre-collected experiences into a sequence of skills. A popular approach to skill learning is maximizing the likelihood of the pre-collected experience with latent variable models, where the latent variables represent the skills. However, there are often many solutions that maximize the likelihood equally well, including degenerate solutions. To address this underspecification, we propose a new objective that combines the maximum likelihood objective with a penalty on the description length of the skills. This penalty incentivizes the skills to maximally extract common structures from the experiences. Empirically, our objective learns skills that solve downstream tasks in fewer samples compared to skills learned from only maximizing likelihood. Further, while most prior works in the offline multi-task setting focus on tasks with low-dimensional observations, our objective can scale to challenging tasks with high-dimensional image observations. 

## **1 Introduction** 

While learning tasks from scratch with reinforcement learning (RL) is often sample inefficient [31, 8], leveraging datasets of pre-collected experience from various tasks can accelerate the learning of new tasks. This experience can be used in numerous ways, including to learn a dynamics model [18, 39], to learn compact representations of observations [88], to learn behavioral priors [78], or to extract meaningful skills or options [80, 43, 2, 60] for hierarchical reinforcement learning (HRL) [6]. Our work studies this last approach. The central idea is to extract commonly occurring behaviors from the pre-collected experience as skills, which can then be used in place of primitive low-level actions to accelerate learning new tasks via planning [71, 52] or RL [56, 48, 53]. For example, in a navigation domain, learned skills may correspond to navigating to different rooms or objects. 

Prior methods learn skills by maximizing the likelihood of the pre-collected experience [44, 43, 2, 91]. However, this maximum likelihood objective (or the lower bounds on it) is _underspecified_ : it often admits many solutions, only some of which would help learning new tasks (see Figure 1). For example, one degenerate solution is to learn a single skill for each entire trajectory; another degenerate solution is to learn skills that operate for a single timestep, equivalent to the original action space. Both of these decompositions can perfectly reconstruct the pre-collected experiences (and, hence, maximize likelihood), but they are of limited use for learning to solve new tasks. Overall, the maximum likelihood objective cannot distinguish between such decompositions and potentially more useful 

> _∗_ Equal contribution 

36th Conference on Neural Information Processing Systems (NeurIPS 2022). 

**==> picture [396 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Skills that  arbitrarily segment the trajectories Skills that  navigate to objects<br>**----- End of picture text -----**<br>


Figure 1: Skill learning via maximizing likelihood is _underspecified_ : the skills (represented by the different colored segments) on both the left and the right maximize the likelihood (i.e., encode the data), but the skills on the right are more likely to be useful for a new task. Our approach factors out common temporal structures, yielding the skills on the right. The visualized tasks are from Kipf et al. [43]. 

decompositions, and we find that this underspecification problem can empirically occur even on simple tasks in our experiments. 

To address this underspecification problem, we propose to introduce an additional objective which biases skill learning to acquire skills that can accelerate the learning of new tasks. To construct such an objective, we make two key observations: 

- Skills must extract reusable temporally-extended structure from the pre-collected experiences to accelerate learning of new tasks. 

- _Compressing_ data also requires identifying and extracting common structure. 

Hence, we hypothesize that compression is a good objective for skill learning. We formalize this notion of compression with the principle of _minimum description length_ (MDL) [70]. Concretely, we combine the maximum likelihood objective (used in prior works) with a new term to minimize the number of bits required to represent the pre-collected experience with skills, which incentivizes the skills to find common structure. Additionally, while prior compression-based methods typically involve discrete optimization and hence are not differentiable, we also provide a method to minimize our compression objective via gradient descent (Section 4), which enables optimizing our objective with neural networks. 

Overall, our main contribution is an objective for extracting skills from offline experience, which addresses the underspecification problem with the maximum likelihood objective. We call the resulting approach LOVE ( **L** earning **O** ptions **V** ia compr **E** ssion). Using multi-task benchmarks from prior work [43], we find that LOVE can learn skills that enable faster RL and are more semantically meaningful compared to skills learned with prior methods. We also find that LOVE can scale to tasks with high-dimensional image observations, whereas most prior works focus on tasks with low-dimensional observations. 

## **2 Related Works** 

We study the problem of using offline experience from one set of tasks to quickly learn new tasks. While we use the experience to learn skills, prior works also consider other approaches of leveraging the offline experience, including to learn a dynamics model [39], to learn a compact representation of observations [88], and to learn behavioral priors for exploring new tasks [78]. 

We build on a rich literature on extracting skills [80] from _offline_ experience [63, 21, 44, 75, 43, 7, 67, 93, 92, 47, 2, 73, 72, 60, 91, 54, 94, 69, 81, 89]. These works predominantly learn skills using a latent variable model, where the latent variables partition the experience into skills, and the overall model is learned by maximizing (a lower bound on) the likelihood of the experiences. This approach is structurally similar to a long line of work in hierarchical Bayesian modeling [24, 9, 20, 50, 38, 13, 49, 40, 29, 15]. We also follow this approach and build off of VTA [40] for the latent variable model, but differ by introducing a new compression term to address the underspecification problem with maximizing likelihood. Several prior approaches [91, 92, 23] also use compression, but yield open-loop skills, whereas we aim to learn closed-loop skills that can react to the state. Additionally, Zhang et al. [91] show that maximizing likelihood with variational inference can itself be seen as a form of compression, but this work compresses the latent variables at each time step, which does not in general yield optimal compression as our objective does. Other works learn skills by limiting the information used from the state [25], whereas we learn skills by compressing entire trajectories. 

2 

Beyond learning skills from offline experience, prior works also consider learning skills with additional supervision [3, 64, 76, 36, 79], from online interaction without reward labels [26, 19, 17, 74, 5], and from online interaction with reward labels [82, 45, 4, 85, 30, 59]. Additionally, a large body of work on meta-reinforcement learning [16, 86, 68, 95, 51] also leverages prior experience to quickly learn new tasks, though not necessarily through skill learning. 

## **3 Preliminaries** 

**Problem setting.** We consider the problem of using an offline dataset of experience to quickly solve new RL tasks, where each task is identified by a reward function. The offline dataset is a set of trajectories _D_ = _{τi}[N] i_ =1[, where each trajectory is a sequence of states] _**[ x]**[∈X]_[and actions] _**[ a]**[∈A]_[:] _τi_ = _{_ ( _**x**_ 1 _,_ _**a**_ 1) _,_ ( _**x**_ 2 _,_ _**a**_ 2) _, . . .}_ . Each trajectory is collected by some unknown policy interacting with a Markov decision process (MDP) with dynamics _P_ ( _**x** t_ +1 _|_ _**x** t,_ _**a** t_ ). Following prior work [18, 1, 14], we do not assume access to the rewards (i.e., the task) of the offline trajectories. 

Using this dataset, our aim is to quickly solve a new task. The new task involves interacting with the same MDP as the data collection policy in the offline dataset, except with a new reward function _R_ ( _**x** ,_ _**a**_ ). The objective is to learn a policy that maximizes the expected returns in as few numbers of environment interactions as possible. 

**Variational Temporal Abstraction.** Our method builds upon the graphical model from variational temporal abstraction (VTA) [40], which is a method for decomposing non-control sequential data (i.e., data without actions) into subsequences. We overview VTA below and extend it to handle actions it Section 4.1. 

VTA assumes that each observation _**x** t_ is associated with an abstract representation _**s** t_ and a subsequence descriptor _**z** t_ . An additional, binary random variable _**m** t_ indicates whether a new subsequence begins at the current observation. VTA uses the following generative model: 

1. Determine whether to begin a new subsequence: _**m** t ∼ p_ ( _**m** t |_ _**s** t−_ 1). A new subsequence always begins on the first time step, i.e., _**m**_ 1 = 1. 

2. Sample the descriptor: _**z** t ∼ p_ ( _**z** t |_ _**z** <t,_ _**m** t_ ). If _**m** t_ = 0, the previous descriptor is copied, i.e., _**z** t_ = _**z** t−_ 1. 

3. Sample the next state abstract representation: _**s** t ∼ p_ ( _**s** t |_ _**s** <t,_ _**z** t,_ _**m** t_ ). 

4. Sample the observation: _**x** t ∼ p_ ( _**x** t |_ _**s** t_ ). 

We visualize this sampling procedure in Figure 2. Formally, we can write this generative model as: 

**==> picture [151 x 99] intentionally omitted <==**

- Figure 2: The VTA graphical model (adapted from Kim et al. [40]). The model decomposes the data _x_ 1: _T_ into subsequences demarcated by when the boundary variables _mt_ = 1 (highlighted in yellow). Each subsequence is assigned a descriptor _**z**_ , where all _**z** t_ within a subsequence are the same (outlined in dashed lines). 

**==> picture [374 x 30] intentionally omitted <==**

VTA maximizes the likelihood of the observed data under this latent variable model using the standard evidence lower bound (ELBO): 

**==> picture [331 x 25] intentionally omitted <==**

This lower bound holds for any choice of _q_ _**θ**_ . VTA chooses to factor this distribution as: 

**==> picture [356 x 27] intentionally omitted <==**

As discussed above and as we observe in Section 6, the maximum likelihood objective is underspecified and may yield degenerate or unhelpful solutions, which we address in the next section. Specifically, we use the graphical model from VTA, but introduce a new objective that compresses the latent variables _**z**_ , while also maximizing the ELBO. 

3 

## **4 LOVE: Learning Options via Compression** 

In this section, we describe our method for learning skills from pre-collected experience. We first extend the VTA graphical model to handle experience labeled with actions, and then introduce a compression objective that encourages extracting common structure from the experience. 

## **4.1 A Graphical Model for Interaction Data** 

We now extend the VTA graphical model [40] to handle sequential data labeled with actions, where descriptors _**z**_ now represent skills. From a high level, the model partitions a trajectory into subsequences with the boundary variables _**m**_ and labels each subsequence as a skill _**z**_ . 

We wish to learn a state-conditional policy rather than the joint distribution of the whole trajectory. To do this, we write a new generative model for the actions _**a**_ 1: _T_ conditional on the state _**x**_ 1: _T_ : 

**==> picture [407 x 30] intentionally omitted <==**

This differs from the original VTA generative model in two ways: (1) we introduce a _p_ ( _**a** t |_ _**s** t_ ) term that indicates how actions are sampled; and (2) the distributions over _**z** t_ and _**s** t_ do not depend on all previous _**z**_ 1: _t_ and _**s**_ 1: _t_ to encode the Markov property. We then augment the variational distribution such that the posterior over skills _**z**_ also depends on actions: 

**==> picture [386 x 36] intentionally omitted <==**

Overall, this yields a model with 3 learned components: 

- A _state abstraction posterior q_ _**θ**_ ( _**s** t |_ _**z** t,_ _**x** t_ ) and _decoder p_ _**θ**_ ( _**a** t |_ _**s** t_ ), which together form a distribution over actions conditioned on the skill _**z** t_ and current state _**x** t_ . We refer to these jointly as the _skill policy π_ _**θ**_ ( _**a** t |_ _**z** t,_ _**x** t_ ) = E _**s** t∼q_ _**θ**_ ( _**s** t|_ _**z** t,_ _**x** t_ ) [ _p_ _**θ**_ ( _**a** t |_ _**s** t_ )]. 

- A _termination policy q_ _**θ**_ ( _**m** t |_ _**x**_ 1: _t_ ), which determines whether the previous skill terminates. 

- A _skill posterior q_ _**θ**_ ( _**z** t |_ _**z** t−_ 1 _,_ _**m** t,_ _**x**_ 1: _T ,_ _**a**_ 1: _T_ ), which outputs the current skill _**z** t_ conditioned on all states _**x**_ 1: _T_ and actions _**a**_ 1: _T_ . This depends on _**m** t_ and _**z** t−_ 1, since the boundary variables determine whether the previous skill _**z** t−_ 1 terminates: when _**m** t_ = 0, the previous skill does not terminate and _**z** t_ = _**z** t−_ 1. 

Once this model is learned, the skill policy and termination policy represent the skills, without a need for the skill posterior: Given a skill variable _**z**_ , the skill policy encodes what actions the skill takes, and the termination policy determines when the skill stops. In the next section, we describe our objective for learning this model. Then, in Section 5, we describe how we use the skill policy and termination policy to learn new tasks. 

## **4.2 Discovering Structure via Compression** 

As previously discussed, the maximum likelihood objective is underspecified for skill learning, because many skills can maximize likelihood, independent of whether they are useful for learning new tasks. In this section, we address this with a new objective that attempts to measure how useful skills will be for learning new tasks in terms of compression. Our objective is based on the intuition that effectively compressing a sequence of data requires factoring out common structure, and factoring out common structure is critical for learning useful skills. 

We measure the complexity of a skill decomposition as the amount of information required to communicate the sequence of skills that encode the pre-collected experience. The latent variable model introduced in the previous section encodes each trajectory as a sequence of skills _**z**_ 1: _T_ and boundaries _**m**_ 1: _T_ . However, using the skill and termination policies, it is possible to recover each trajectory from only the skill variables at the boundary points: i.e., at the time steps _{t ∈_ [ _T_ ] _|_ _**m** t_ = 1 _}_ . For a prior on skills _p_ _**z**_ , an optimal code requires _−_ log _p_ _**z**_ ( _**z** t_ ) bits to send a skill _**z** t_ [12, Chapter 5.2]. Hence, 

4 

the expected code length of communicating a trajectory _**τ**_ 1: _T_ = _{_ ( _**x**_ 1 _,_ _**a**_ 1) _, . . . ,_ ( _**x** T ,_ _**a** T_ ) _}_ is: 

**==> picture [213 x 30] intentionally omitted <==**

where the expectation is under trajectories _**τ**_ 1: _T_ from the pre-collected experience and sampling _**z**_ 1: _T_ from the skill posterior and _**m**_ 1: _T_ from the termination policy. The choice of prior that minimizes the average code length is one that equals the empirical distribution of skills under the pre-collected experience [12, Chapter 5.3]: 

**==> picture [340 x 31] intentionally omitted <==**

and _n_ s ≜ E _**τ**_ 1: _T ,_ _**m**_ 1: _T Tt_ =1 _**[m]**[t]_ . In Appendix A.1, we show that this marginal _p[⋆]_ _**z**_[is][a][proper] �� � density for both continuous and discrete _**z**_ . Substituting in this optimal choice of prior, we can show that the code length can be expressed as the marginal entropy _Hp⋆_ _**z**_ [ _**z**_ ] times the number of skills per trajectory _n_ s (see Appendix A.2 for proof): 

**==> picture [356 x 28] intentionally omitted <==**

Intuitively, this is equal to the average code length of a skill multiplied by the the average number of skills per trajectory. Note that compression is only beneficial if the model also achieves high likelihood of the data. We capture this by solving the following constrained optimization problem: 

min _L_ CL( _**θ**_ ) s.t. _L_ ELBO( _**θ**_ ) _≤ C,_ (2) _**θ**_ 

where _L_ ELBO( _**θ**_ ) a negated evidence lower bound on the log-likelihood (detailed in Appendix B). 

**Remarks.** We discuss a connection between this objective and variational inference in Appendix A.3. Additionally, while this work focuses on the RL setting, our objective generally applies to sequential modeling problems. We believe that it could be useful for many applications beyond option learning. 

## **4.3 Connections to Minimal Description Length** 

Our approach closely relates to the minimum description length (MDL) principle [70]. This principle equates _learning_ with _finding regularity_ in data, which can be used to _compress_ the data. Informally, the best model is the one that encodes the data with the lowest description length. Given a model _**θ**_ that encodes the data _D_ into some message, one way to formalize the description length of the data _L_ ( _D_ ) is with a crude two-part code [27]. This decomposes the description length of the data as the length of the message plus the length of the model: 

**==> picture [265 x 25] intentionally omitted <==**

In our case, the message is the latent variables _**z** t_ at the boundary points _{t ∈_ [ _T_ ] _|_ _**m** t_ = 1 _}_ , which can be decoded into the data _D_ with the skill and termination policies (representing the model). Hence, our approach can be seen as an instance of minimizing the description length _L_ ( _D_ ). Optimizing our objective in Equation 1 is equivalent to minimizing the message length _L_ ( _D |_ _**θ**_ ). While we do not directly attempt to minimize the model length term _L_ ( _**θ**_ ), many works [61, 83] indicate that deep learning has _implicit regularization_ , which biases optimization toward low complexity solutions without an explicit regularizer. In general, computing the true description length or appropriate notion of complexity for neural networks is a tall order [62, 90, 37]; however, there is a rich space of methods to be explored here and we therefore leave the extension of our approach to directly minimizing the model length term for future work. 

## **4.4 A Practical Implementation** 

**Model.** We instantiate our model by defining discrete skills _**z** ∈_ [ _K_ ], state abstractions _**s** ∈_ R _[d]_ , and binary boundary variables _**m** ∈{_ 0 _,_ 1 _}_ . We parameterize all components of our model as neural networks. See Appendix D for architecture details. 

5 

**Optimization.** We apply Gumbel-softmax [35, 55] to optimize over the discrete random variables _**z**_ to improve the stability of optimization. and _**m**_ . We rewrite the compression objectiveThis rewriting allows computing a gradient in terms of a _L_ CL as a product of _n_ s and _Hp⋆_ _**z**_ [ _**z** t_ ] in Equation 1 distribution over the skill variables _p[⋆]_ _**z**_[, rather than samples] _**[ z]**[t]_[, which yields a more accurate finite] sample gradient. Empirically, this leads to stabler optimization and convergence to better solutions. We approximate the optimal skill prior _p[⋆]_ _**z**_[using our skill posterior as:] 

**==> picture [312 x 33] intentionally omitted <==**

where E[�] denotes the empirical expectation over minibatches of _**x**_ 1: _T ,_ _**a**_ 1: _T_ from _D_ and sampling _**m**_ 1: _T_ from the termination policy. We solve the constrained optimization problem (Equation 2) with dual gradient descent on the Lagrangian. In Appendix G, we summarize the overall training procedure in Algorithm 1 and report details about the Lagrangian. 

**Enforcing a minimum skill length.** Though degenerate solutions such as skills that only take a single action score poorly in our compression objective, empirically, such solutions create local optima that are difficult to escape. To avoid this, we mask the boundary variables during training to ensure that each skill _zt_ operates for at least _T_ min = 3 time steps. We find that when the skills are at least minimally temporally extended, optimization of the compression objective appears to be stabler and achieves better values. We remove these masks at test time, when we learn a task with our skills. 

## **5 Using the Learned Skills for Hierarchical RL** 

We now describe how we quickly learn new tasks, given the skills learned from the pre-collected experience. Overall, we simply augment the agent’s action space with the learned skills and learn a new policy that can take either low-level actions or learned skills, similar to Kipf et al. [43]. However, our compression objective may result in unused skills, since this decreases the encoding cost of the used skills. Therefore, we first filter down to only the skills that are used to compress the pre-collected experience by selecting the skills where the marginal is over some threshold _α_ : 

**==> picture [128 x 13] intentionally omitted <==**

Then, on a new task with action space _A_ , we train an agent using the augmented action space _A_[+] = _A ∪Z_ . When the agent selects a skill _z ∈Z_ , we follow the procedure in Algorithm 2 in the Appendix. We take actions following the skill policy _π_ _**θ**_ ( _**a** t |_ _**z** ,_ _**x** t_ ) (lines 2–3), until the termination policy _q_ _**θ**_ ( _**m** t |_ _**x**_ 1: _t_ ) outputs a termination _**m** t_ = 1 (line 5). At that point, the agent observes the next state _**x** t_ +1 and selects the next action or skill. 

## **6 A Didactic Experiment: Frame Prediction** 

Before studying the RL setting, we first illustrate the effect of LOVE in the simpler setting of sequential data without actions. In this setting, we use the original VTA model, which partitions a sequence _**x**_ 1: _T_ into contiguous subsequences with the boundary variables _**m**_ and labels each subsequence with a descriptor _**z**_ , as described in Section 3. Here, VTA’s objective is to maximize the likelihood of the sequence _**x**_ 1: _T_ , and our compression objective applies to this setting completely unmodified. We compare LOVE and only maximizing likelihood, i.e., VTA [40], by measuring how well the learned subsequences correspond to underlying patterns in the data. To isolate the effect of the compression objective, we do not enforce a minimum skill length. 

**Dataset.** We consider two simple datasets _Simple Colors_ and _Conditional Colors_ , which consist of sequences of 32 _×_ 32 monochromatic frames, with repeating underlying patterns. _Simple Colors_ consists of 3 patterns: 3 consecutive yellow frames, 3 consecutive blue frames and 3 consecutive green frames. The dataset is generated by sampling these patterns with probability 0.4, 0.4, and 0.2 respectively and concatenating the results. Each pattern is sampled independent of history. The dataset is then divided into sequences of 6 patterns, equal to 6 _×_ 3 = 18 frames. 

In contrast to _Simple Colors_ , _Conditional Colors_ tests learning patterns that depend on history. It consists of 4 patterns: the 3 patterns from _Simple Colors_ with an additional pattern of 3 consecutive 

6 

**==> picture [171 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
LOVE<br>VTA<br>**----- End of picture text -----**<br>


Figure 3: Learned boundaries and descriptors on _Simple Colors_ . LOVE recovers the patterns, while VTA learns boundaries that break up patterns or span multiple patterns (outlined in red). 

Table 1: Effect of LOVE on the _Simple Colors_ and _Conditional Colors_ datasets (5 seeds). All approaches achieve similar values for the likelihood objective, but LOVE better recovers the correct boundaries. 

|_L_ELBO|_Simple_<br>**VTA**<br>2868_±_43|_Colors_<br>**LOVE**<br>2838_±_19|_Conditional Colors_<br>**VTA**<br>**LOVE**<br>2832_±_7_._7<br>2827_±_1_._9|_Conditional Colors_<br>**VTA**<br>**LOVE**<br>2832_±_7_._7<br>2827_±_1_._9|
|---|---|---|---|---|
||||2832_±_7_._7|2827_±_1_._9|
|Precision<br>Recall<br>F1<br>Code Length|0_._87_±_0_._19<br>0_._79_±_0_._13<br>0_._82_±_0_._13<br>7_._58_±_1_._3|**0****_._99**_±_0_._01<br>**0****_._85**_±_0_._03<br>**0****_._91**_±_0_._02<br>**6****_._34**_±_0_._75|0_._84_±_0_._22<br>**0****_._82**_±_0_._16<br>0_._83_±_0_._19<br>9_._17_±_1_._76|**0****_._99**_±_0_._01<br>**0****_._83**_±_0_._06<br>**0****_._90**_±_0_._03<br>**6****_._83**_±_0_._51|



purple frames. The dataset is generated by uniformly sampling the patterns from _Simple Colors_ . To make the current timestep pattern dependent on the previous timestep, the yellow frames are re-colored to purple, if the previous pattern was blue or yellow. As in _Simple Colors_ , the dataset is divided into sequences of 6 patterns. 

In both datasets, the optimal encoding strategy is to learn 3 subsequence descriptors (i.e., skills), one for each pattern in _Simple Colors_ . In _Conditional Colors_ , the descriptor corresponding to yellow in _Simple Colors_ either outputs yellow or purple, depending on the history. This encoding strategy achieves an expected code length of 6 _._ 32 nats in _Simple Colors_ and 6 _._ 59 nats in _Conditional Colors_ . 

**Results.** We visualize the learned descriptors and boundaries in Figure 3. LOVE successfully segments the sequences into the patterns and assigns a consistent descriptor _**z**_ to each pattern. In contrast, despite the simple structure of this problem, VTA learns subsequences that span over multiple patterns or last for fewer timesteps than a single pattern. 

Quantitatively, we measure the (1) precision, recall, and F1 scores of the boundary prediction, (2) the ELBO of the maximum likelihood objective and (3) the average code length _L_ CL in Table 1. While both VTA and LOVE achieve approximately the same negated ELBO (lower is better), LOVE recovers the correct boundaries with much higher precision, recall, and F1 scores. This illustrates that the underspecification problem can occur even in simple sequential data. Additionally, we find that LOVE achieves an encoding cost close to the optimal value. One interesting, though rare, failure mode is that LOVE sometimes even achieves a lower encoding cost than the optimal value by over-weighting the compression term and imperfectly reconstructing the data. In Appendix C, we conduct a ablation study on the weights of _L_ CL in optimization. 

## **7 Experiments** 

We aim to answer three questions: (1) Does LOVE learn semantically meaningful skills? (2) Do skills learned with LOVE accelerate learning for new tasks? (3) Can LOVE scale to high-dim pixel observations? To answer these questions, we learn skills from demonstrations and use these skills to learn new tasks, first on a 2D multi-task domain, and later on a 3D variant. 

**==> picture [53 x 84] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [8 x 9] intentionally omitted <==**

**==> picture [24 x 50] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.<br>2.<br>3.<br>4.<br>5.<br>**----- End of picture text -----**<br>


**==> picture [9 x 10] intentionally omitted <==**

**==> picture [9 x 10] intentionally omitted <==**

**==> picture [9 x 10] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**Multi-task domain.** We consider the multi-task 10 _×_ 10 grid world introduced by Kipf et al. [43], a representative skill learning approach (Figure 4). This domain features a challenging control problem that requires the agent to collect Figure 4: Multi-task grid world instance up to 5 objects, and we later add a perception challenge to it from Kipf et al. [43].43].].. The agent must with the 3D variant. We use our own custom implementation, pick up a sequence of objects in a specisince the code from Kipf et al. [43] is not publicly available. fied order. In each task, 6 objects are randomly sampled from a set of _N_ obj = 10 different objects and placed at random positions in the grid. Additionally, impassable walls are randomly added to the grid, and the agent is also placed at a random initial grid cell. Each task also includes an instruction list of _N_ pick = 3 or 5 objects that the agent must pick up in order. 

Figure 4: Multi-task grid world instance from Kipf et al. [43].43].].. The agent must pick up a sequence of objects in a speci- 

Within each task, the agent’s actions are to move up, down, left, right, or to pick up an item at the agent’s grid cell. The state consists of two parts: (1) a 10 _×_ 10 _×_ ( _N_ obj + 2) grid observation, 

7 

indicating if the agent, a wall, or any of the _N_ obj different object types is present at each of the 10 _×_ 10 grid cells; (2) the instruction corresponding to the next object to pick up, encoded as a one-hot integer. Following Kipf et al. [43], we consider two reward variants: In the _sparse reward_ variant, the agent only receives +1 reward after picking up _all N_ pick objects in the correct order. In the _dense reward_ variant, the agent receives +1 reward after picking up each specified object in the correct order. Our dense reward variant is slightly harder than the variant in Kipf et al. [43], which gives the agent +1 reward for picking up objects in _any_ order. The agent receives 0 reward in all other time steps. The episode ends when the agent has picked up all the objects in the correct order, or after 50 timesteps. 

**Pre-collected experience.** We follow the setting in Kipf et al. [43]. We set the pre-collected experience to be 2000 demonstrations generated via breadth-first search on randomly generated tasks with only _N_ pick = 3 and test if the agent can generalize to _N_ pick = 5 when learning a new task. These demonstrations are not labeled with rewards and also _do not_ contain the instruction list observations. 

**Points of comparison.** To study our compression objective, we compare with two representatives of learning skills via the maximum likelihood objective: 

- VTA [40], modified to handle interaction data as in Section 4.1. 

- Discovery of deep options (DDO) [21]. We implement DDO’s maximum likelihood objective and graphical model on top of VTA’s variational inference optimization procedure, instead of expectation-gradients used in the original paper. 

For fairness, we also compare with variants of these that implement the minimum skill length constraint from Section 4.4. CompILE [43] is another approach that learns skill by maximizing likelihood and was introduced in the same paper as this grid world. Because the implementation is unavailable, we do not compare with it. However, we note that CompILE requires additional supervision that LOVE, VTA, and DDO do not: namely, it requires knowing how many skills each demonstration is composed of. This supervision can be challenging to obtain without already knowing what the skills should be. 

Since latent variable models are prone to local optima [46], it is common to learn such models with multiple restarts [58]. We therefore run each method with 3 random initializations and pick the best model according to the compression objective _L_ CL for LOVE and according to the ELBO of the maximum likelihood objective _L_ ELBO for the others. Notably, this does not require any additional demonstrations or experience. 

We begin by analyzing the skills learned from the pre-collected experience before analyzing the utility of these skills for learning downstream tasks in the next sections. 

## **7.1 Analyzing the Learned Skills** 

We analyze the learned skills by comparing them to a natural decomposition that partitions the demonstration in _N_ pick sequences of moving to and picking up an object. Specifically, we measure the precision and recall of each method in outputting the correct boundaries of these _N_ pick sequences. 

We find that only LOVE recovers the correct boundaries with both high precision and recall (Table 2). Visually examining the 

Table 2: Precision and recall of outputting the boundaries between picking up different objects. Only LOVE learns skills that move to and pick up an object. 

|||Precision|Recall|F1|
|---|---|---|---|---|
||DDO [21]|0.19|**1**|0.32|
||DDO + min. skill length<br>VTA [40]|0.26<br>0.19|0.53<br>**0.99**|0.35<br>0.32|
||VTA + min. skill length|0.27|0.53|0.36|
||LOVE(ours)|**0.90**|0.94|**0.92**|



skills learned with LOVE shows that each skill moves to an object and picks it up. We visualize LOVE’s skills in Appendix H. In contrast, maximizing likelihood with either DDO or VTA learns degenerate skills that output only a single action, leading to high recall, but low precision. Adding the minimum skill length constraint to these approaches prevents such degenerate solutions, but still does not lead to the correct boundaries. Skills learned by VTA with the minimum skill length constraint exhibit no apparent structure, but skills learned by DDO with the minimum skill length constraint appear to move toward objects, though they terminate at seemingly random places. These results further illustrate the underspecification problem. All approaches successfully learn to reconstruct the 

8 

**==> picture [397 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
N pick = 3 (Dense) N pick = 3 (Sparse) N pick = 5 (Dense) N pick = 5 (Sparse)<br>1 . 2<br>3 . 0 1 . 0 5 1 . 0<br>2 . 5 4<br>0 . 8 0 . 8<br>2 . 0<br>0 . 6 3 0 . 6<br>1 . 5<br>0 . 4 2 0 . 4<br>1 . 0<br>0 . 5 0 . 2 1 0 . 2<br>0 . 0 0 . 0 0 0 . 0<br>0 500 1000 1500 2000 0 1000 2000 3000 4000 0 1000 2000 3000 0 1000 2000 3000 4000 5000<br>Timesteps (1e3) Timesteps (1e3) Timesteps (1e3) Timesteps (1e3)<br>Love VTA No skills DDO<br>Optimal VTA (min. skill length) No skills (behavior cloning) DDO (min. skill length)<br>Returns<br>Average<br>**----- End of picture text -----**<br>


Figure 5: **Sample efficient learning.** We plot returns vs. timesteps of environment interactions for 4 settings in the grid world with 1-stddev error bars (5 seeds). Only LOVE achieves high returns across all 4 settings. 

demonstrations and achieve high likelihood, but only LOVE and DDO with the minimum skill length constraint learn skills that appear to be semantically meaningful. 

## **7.2 Learning New Tasks** 

Next, we evaluate the utility of the skills for learning new tasks. To evaluate the skills, we sample a new task in each of 4 settings: with sparse or dense rewards and with _N_ pick = 3 or _N_ pick = 5. Then we learn the new tasks following the procedure in Section 5: we augment the action space with the skills and train an agent over the augmented action space. To understand the impact of skills, we also compare with a low-level policy that learns these tasks using only the original action space, and the same low-level policy that incorporates the demonstrations by pre-training with behavioral cloning. We parametrize the policy for all approaches with dueling double deep Q-networks [57, 87, 84] with _ϵ_ -greedy exploration. We report the returns of evaluation episodes with _ϵ_ = 0, which are run every 10 episodes. We report returns averaged over 5 seeds. See Appendix F.4 for full details. 

**Results.** Overall, LOVE learns new tasks across all 4 settings comparably to or faster than both skill methods based on maximizing likelihood and incorporating demonstrations via behavior cloning (Figure 5). More specifically, when _N_ pick = 3, DDO with the min. skill length constraint performs comparably to LOVE, despite not segmenting the demonstrations into sequences of moving to and picking up objects. We observe that while a single DDO skill does not move to and pick up an object, the skills consistently move toward objects, which likely helps with exploration. Imitating the demonstrations with behavior cloning also accelerates learning when _N_ pick = 3 with dense rewards, though not as much as LOVE or DDO, and yields insignificant benefit in all other settings. Skill learning with VTA yields no benefit over no skill learning at all. 

Recall that _N_ pick = 3 in all of the demonstrations. LOVE learns new tasks in the generalization setting of _N_ pick = 5 much faster than the other methods. With dense rewards, DDO (min. skill length) also eventually solves the task, but requires over 8 _×_ more timesteps. The other approaches learn to pick up some objects, but never achieve optimal returns of 5. With sparse rewards, LOVE is the only approach that achieves high returns, while all other approaches achieve 0 returns. This likely occurs because this setting creates a challenging exploration problem, so exploring with low-level actions or skills learned with VTA or DDO rarely achieves reward. By contrast, exploring with skills learned with LOVE achieves rewards much more frequently, which enables LOVE to ultimately solve the task. 

## **7.3 Scaling to High-dimensional Observations** 

Prior works in the offline multi-task setting have learned skills from low-dimensional states and then transferred them to high-dim pixel observations [69], or have learned hierarchical models from pixel observations [40, 21]. However, to the best of our knowledge, prior works in this setting have not directly learned skills from high-dim pixel observations, only from low-dimensional states. Hence, in this section, we test if LOVE can scale up to high-dim pixel observations by considering a challenging 3D image-based variant of the multi-task domain above, illustrated in Figure 6. The goal is still to pick up _N_ pick objects in the correct order, where objects are blocks of different colors. Each task includes 3 objects randomly sampled from a set of _N_ obj = 6 different colors. The observations are 400 _×_ 60 _×_ 3 egocentric panoramic RGB arrays. The actions are to move forward / backward, turn left / right, and pick up. 

9 

**==> picture [133 x 88] intentionally omitted <==**

Figure 6: 3D visual multi-task domain. 

**==> picture [189 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 . 0<br>0 . 5<br>0 . 0<br>0 250 500 750 1000 1250 1500<br>Timesteps (1e3)<br>Optimal VTA (min. skill length) No skills<br>Love DDO (min. skill length) No skills (BC)<br>Returns<br>**----- End of picture text -----**<br>


Figure 7: Returns on the 3D visual multi-task domain with 1-stddev error bars (5 seeds). Only LOVE achieves near-optimal returns. 

We consider only the harder _sparse reward_ and generalization setting, where the agent must pick up _N_ pick = 4 objects in the correct order, after receiving 2,000 pre-collected demonstrations of the approximate shortest path of picking up _N_ pick = 2 objects in the correct order. We use the same hyperparameters as in multi-task domain and only change the observation encoder and action decoder (full details in Appendix D.3). Figure 7 shows the results. Again, LOVE learns skills that each navigate to and pick up an object, which quickly achieves optimal returns, indicating its ability to scale to high-dim observations. In contrast, the other approaches perform much worse on pixel observations than the previous low-dim observations. DDO also makes progress on the task, but requires far more samples, as it again learns skills that only operate for a few timesteps, though they move toward the objects. All other approaches fail to learn at all, including the variants of VTA and DDO without the min. skill length, which are not plotted. 

## **8 Conclusion** 

We started by highlighting the underspecification problem: maximizing likelihood does not necessarily yield skills that are useful for learning new tasks. To overcome this problem, we drew a connection between skill learning and compression and proposed a new objective for skill learning via compression and a differentiable model for optimizing our objective. Empirically, we found that the underspecification problem occurs even on simple tasks and learning skills with our objective allows learning new tasks much faster than learning skills by maximizing likelihood. 

Still, important future work remains. LOVE applies when there are useful and consistent structures that can be extracted from multiple trajectories. This is often present in multi-task demonstrations, which solve related tasks in similar ways. However, an open challenge for adapting to general offline data like D4RL [22], is to ensure that the learned skills do not overfit to potentially noisy or unhelpful behaviors often present in offline data. In addition, we showed a connection between skill learning and compression by minimizing the description length of a crude two-part code. However, we only proposed a way to optimize the message length term and not the model length. Completing this connection by accounting for model length may therefore be an promising direction for future work. 

**Reproducibility.** Our code is publicly available at `https://github.com/yidingjiang/love` . 

**Acknowledgements.** We would like to thank Karol Hausman, Abhishek Gupta, Archit Sharma, Sergey Levine, Annie Xie, Zhe Dong, Samuel Sokota for valuable discussions during the course of this work, and Victor Akinwande, Christina Baek, Swaminathan Gurumurthy for comments on the draft. We would also like to thank the anonymous reviewers for their valuable feedback. Last, but certainly not least, YJ and EZL thank the beautiful beach of Kona for initiating this project. 

YJ is supported by funding from the Bosch Center for Artificial Intelligence. EZL is supported by a National Science Foundation Graduate Research Fellowship under Grant No. DGE-1656518. CF is a Fellow in the CIFAR Learning in Machines and Brains Program. This work was also supported in part by the ONR grant N00014-21-1-2685, Google, and Intel. Icons in this work were made by ThoseIcons, FreePik, VectorsMarket, from FlatIcon. 

- LOVE _is a many-splendored thing._ LOVE _lifts us up where we belong. All you need is_ LOVE _._ — Moulin Rouge (Elephant Love Song Medley) 

10 

## **References** 

- [1] Pulkit Agrawal, Ashvin Nair, Pieter Abbeel, Jitendra Malik, and Sergey Levine. Learning to poke by poking: Experiential learning of intuitive physics. _arXiv preprint arXiv:1606.07419_ , 2016. 

- [2] Anurag Ajay, Aviral Kumar, Pulkit Agrawal, Sergey Levine, and Ofir Nachum. Opal: Offline primitive discovery for accelerating offline reinforcement learning. _arXiv preprint arXiv:2010.13611_ , 2020. 

- [3] Jacob Andreas, Dan Klein, and Sergey Levine. Modular multitask reinforcement learning with policy sketches. In _International Conference on Machine Learning_ , pages 166–175. PMLR, 2017. 

- [4] Pierre-Luc Bacon, Jean Harb, and Doina Precup. The option-critic architecture. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 31, 2017. 

- [5] Akhil Bagaria, Jason K Senthil, and George Konidaris. Skill discovery for exploration and planning using deep skill graphs. In _International Conference on Machine Learning_ , pages 521–531. PMLR, 2021. 

- [6] Andrew G Barto and Sridhar Mahadevan. Recent advances in hierarchical reinforcement learning. _Discrete event dynamic systems_ , 13(1):41–77, 2003. 

- [7] Ritwik Bera, Vinicius G Goecks, Gregory M Gremillion, John Valasek, and Nicholas R Waytowich. Podnet: A neural network for discovery of plannable options. _arXiv preprint arXiv:1911.00171_ , 2019. 

- [8] Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław Debiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, et al. Dota 2 with large scale deep reinforcement learning. _arXiv preprint arXiv:1912.06680_ , 2019. 

- [9] David M Blei and Pedro J Moreno. Topic segmentation with an aspect hidden markov model. In _Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval_ , pages 343–348, 2001. 

- [10] Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. Empirical evaluation of gated recurrent neural networks on sequence modeling. _arXiv preprint arXiv:1412.3555_ , 2014. 

- [11] Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochreiter. Fast and accurate deep network learning by exponential linear units (elus). _arXiv preprint arXiv:1511.07289_ , 2015. 

- [12] Thomas M Cover. _Elements of information theory_ . John Wiley & Sons, 1999. 

- [13] Hanjun Dai, Bo Dai, Yan-Ming Zhang, Shuang Li, and Le Song. Recurrent hidden semi-markov model. 2016. 

- [14] Sudeep Dasari, Frederik Ebert, Stephen Tian, Suraj Nair, Bernadette Bucher, Karl Schmeckpeper, Siddharth Singh, Sergey Levine, and Chelsea Finn. Robonet: Large-scale multi-robot learning. _arXiv preprint arXiv:1910.11215_ , 2019. 

- [15] Zhe Dong, Bryan Seybold, Kevin Murphy, and Hung Bui. Collapsed amortized variational inference for switching nonlinear dynamical systems. In _International Conference on Machine Learning_ , pages 2638–2647. PMLR, 2020. 

- [16] Yan Duan, John Schulman, Xi Chen, Peter L Bartlett, Ilya Sutskever, and Pieter Abbeel. Rl[2] : Fast reinforcement learning via slow reinforcement learning. _arXiv preprint arXiv:1611.02779_ , 2016. 

- [17] Benjamin Eysenbach, Abhishek Gupta, Julian Ibarz, and Sergey Levine. Diversity is all you need: Learning skills without a reward function. In _International Conference on Learning Representations_ , 2019. URL `https://openreview.net/forum?id=SJx63jRqFm` . 

11 

- [18] Chelsea Finn, Ian Goodfellow, and Sergey Levine. Unsupervised learning for physical interaction through video prediction. _Advances in neural information processing systems_ , 29:64–72, 2016. 

- [19] Carlos Florensa, Yan Duan, and Pieter Abbeel. Stochastic neural networks for hierarchical reinforcement learning. _arXiv preprint arXiv:1704.03012_ , 2017. 

- [20] Emily B Fox, Erik B Sudderth, Michael I Jordan, and Alan S Willsky. A sticky hdp-hmm with application to speaker diarization. _The Annals of Applied Statistics_ , pages 1020–1056, 2011. 

- [21] Roy Fox, Sanjay Krishnan, Ion Stoica, and Ken Goldberg. Multi-level discovery of deep options. _arXiv preprint arXiv:1703.08294_ , 2017. 

- [22] Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine. D4rl: Datasets for deep data-driven reinforcement learning. _arXiv preprint arXiv:2004.07219_ , 2020. 

- [23] Francisco M Garcia, Bruno C da Silva, and Philip S Thomas. A compression-inspired framework for macro discovery. _arXiv preprint arXiv:1711.09048_ , 2017. 

- [24] Zoubin Ghahramani and Geoffrey E Hinton. Variational learning for switching state-space models. _Neural computation_ , 12(4):831–864, 2000. 

- [25] Anirudh Goyal, Shagun Sodhani, Jonathan Binas, Xue Bin Peng, Sergey Levine, and Yoshua Bengio. Reinforcement learning with competitive ensembles of information-constrained primitives. _arXiv preprint arXiv:1906.10667_ , 2019. 

- [26] Karol Gregor, Danilo Jimenez Rezende, and Daan Wierstra. Variational intrinsic control. _arXiv preprint arXiv:1611.07507_ , 2016. 

- [27] Peter Grunwald. A tutorial introduction to the minimum description length principle. _arXiv preprint math/0406077_ , 2004. 

- [28] Jean Harb, Pierre-Luc Bacon, Martin Klissarov, and Doina Precup. When waiting is not an option: Learning options with a deliberation cost. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 32, 2018. 

- [29] James Harrison, Apoorva Sharma, Chelsea Finn, and Marco Pavone. Continuous meta-learning without tasks. _arXiv preprint arXiv:1912.08866_ , 2019. 

- [30] Karol Hausman, Jost Tobias Springenberg, Ziyu Wang, Nicolas Heess, and Martin Riedmiller. Learning an embedding space for transferable robot skills. In _International Conference on Learning Representations_ , 2018. URL `https://openreview.net/forum?id=rk07ZXZRb` . 

- [31] Nicolas Heess, Dhruva TB, Srinivasan Sriram, Jay Lemmon, Josh Merel, Greg Wayne, Yuval Tassa, Tom Erez, Ziyu Wang, SM Eslami, et al. Emergence of locomotion behaviours in rich environments. _arXiv preprint arXiv:1707.02286_ , 2017. 

- [32] Geoffrey E Hinton and Richard S Zemel. Autoencoders, minimum description length, and helmholtz free energy. _Advances in neural information processing systems_ , 6:3–10, 1994. 

- [33] Antti Honkela and Harri Valpola. Variational learning and bits-back coding: an informationtheoretic view to bayesian learning. _IEEE transactions on Neural Networks_ , 15(4):800–810, 2004. 

- [34] Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In _International conference on machine learning_ , pages 448–456. PMLR, 2015. 

- [35] Eric Jang, Shixiang Gu, and Ben Poole. Categorical reparameterization with gumbel-softmax. _arXiv preprint arXiv:1611.01144_ , 2016. 

- [36] Yiding Jiang, Shixiang Gu, Kevin Murphy, and Chelsea Finn. Language as an abstraction for hierarchical deep reinforcement learning. _arXiv preprint arXiv:1906.07343_ , 2019. 

12 

- [37] Yiding Jiang*, Behnam Neyshabur*, Hossein Mobahi, Dilip Krishnan, and Samy Bengio. Fantastic generalization measures and where to find them. In _International Conference on Learning Representations_ , 2020. URL `https://openreview.net/forum?id=SJgIPJBFvH` . 

- [38] Matthew J Johnson, David K Duvenaud, Alex Wiltschko, Ryan P Adams, and Sandeep R Datta. Composing graphical models with neural networks for structured representations and fast inference. _Advances in neural information processing systems_ , 29:2946–2954, 2016. 

- [39] Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, and Thorsten Joachims. Morel: Model-based offline reinforcement learning. _arXiv preprint arXiv:2005.05951_ , 2020. 

- [40] Taesup Kim, Sungjin Ahn, and Yoshua Bengio. Variational temporal abstraction. _Advances in Neural Information Processing Systems_ , 32:11570–11579, 2019. 

- [41] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

- [42] Diederik P Kingma and Max Welling. Auto-encoding variational bayes. _arXiv preprint arXiv:1312.6114_ , 2013. 

- [43] Thomas Kipf, Yujia Li, Hanjun Dai, Vinicius Zambaldi, Alvaro Sanchez-Gonzalez, Edward Grefenstette, Pushmeet Kohli, and Peter Battaglia. Compile: Compositional imitation learning and execution. In _International Conference on Machine Learning_ , pages 3418–3428. PMLR, 2019. 

- [44] Sanjay Krishnan, Roy Fox, Ion Stoica, and Ken Goldberg. Ddco: Discovery of deep continuous options for robot learning from demonstrations. In _Conference on robot learning_ , pages 418–437. PMLR, 2017. 

- [45] Tejas D Kulkarni, Karthik Narasimhan, Ardavan Saeedi, and Josh Tenenbaum. Hierarchical deep reinforcement learning: Integrating temporal abstraction and intrinsic motivation. _Advances in neural information processing systems_ , 29:3675–3683, 2016. 

- [46] M Pawan Kumar, Benjamin Packer, and Daphne Koller. Self-paced learning for latent variable models. In _NIPS_ , volume 1, page 2, 2010. 

- [47] Sang-Hyun Lee and Seung-Woo Seo. Learning compound tasks without task-specific knowledge via imitation and self-supervised learning. In _International Conference on Machine Learning_ , pages 5747–5756. PMLR, 2020. 

- [48] Youngwoon Lee, Shao-Hua Sun, Sriram Somasundaram, Edward S Hu, and Joseph J Lim. Composing complex skills by learning transition policies. In _International Conference on Learning Representations_ , 2018. 

- [49] Scott Linderman, Matthew Johnson, Andrew Miller, Ryan Adams, David Blei, and Liam Paninski. Bayesian learning and inference in recurrent switching linear dynamical systems. In _Artificial Intelligence and Statistics_ , pages 914–922. PMLR, 2017. 

- [50] Scott W Linderman, Andrew C Miller, Ryan P Adams, David M Blei, Liam Paninski, and Matthew J Johnson. Recurrent switching linear dynamical systems. _arXiv preprint arXiv:1610.08466_ , 2016. 

- [51] Evan Z Liu, Aditi Raghunathan, Percy Liang, and Chelsea Finn. Decoupling exploration and exploitation for meta-reinforcement learning without sacrifices. In _International conference on machine learning_ , pages 6925–6935. PMLR, 2021. 

- [52] Evan Zheran Liu, Ramtin Keramati, Sudarshan Seshadri, Kelvin Guu, Panupong Pasupat, Emma Brunskill, and Percy Liang. Learning abstract models for strategic exploration and fast reward transfer. _arXiv preprint arXiv:2007.05896_ , 2020. 

- [53] Siqi Liu, Guy Lever, Zhe Wang, Josh Merel, SM Eslami, Daniel Hennes, Wojciech M Czarnecki, Yuval Tassa, Shayegan Omidshafiei, Abbas Abdolmaleki, et al. From motor control to team play in simulated humanoid football. _arXiv preprint arXiv:2105.12196_ , 2021. 

13 

- [54] Yuchen Lu, Yikang Shen, Siyuan Zhou, Aaron Courville, Joshua B Tenenbaum, and Chuang Gan. Learning task decomposition with ordered memory policy network. _arXiv preprint arXiv:2103.10972_ , 2021. 

- [55] Chris J Maddison, Andriy Mnih, and Yee Whye Teh. The concrete distribution: A continuous relaxation of discrete random variables. _arXiv preprint arXiv:1611.00712_ , 2016. 

- [56] Amy McGovern and Richard S Sutton. Macro-actions in reinforcement learning: An empirical analysis. _Computer Science Department Faculty Publication Series_ , page 15, 1998. 

- [57] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. _nature_ , 518(7540):529–533, 2015. 

- [58] Kevin P Murphy. _Machine learning: a probabilistic perspective_ . MIT press, 2012. 

- [59] Ofir Nachum, Shixiang Gu, Honglak Lee, and Sergey Levine. Data-efficient hierarchical reinforcement learning. _arXiv preprint arXiv:1805.08296_ , 2018. 

- [60] Taewook Nam, Shao-Hua Sun, Karl Pertsch, Sung Ju Hwang, and Joseph J Lim. Skill-based meta-reinforcement learning. In _Fifth Workshop on Meta-Learning at the Conference on Neural Information Processing Systems_ , 2021. URL `https://openreview.net/forum?id= jsV1-AQVEFY` . 

- [61] Behnam Neyshabur, Ryota Tomioka, and Nathan Srebro. In search of the real inductive bias: On the role of implicit regularization in deep learning. _arXiv preprint arXiv:1412.6614_ , 2014. 

- [62] Behnam Neyshabur, Srinadh Bhojanapalli, David McAllester, and Nathan Srebro. Exploring generalization in deep learning. _arXiv preprint arXiv:1706.08947_ , 2017. 

- [63] Scott Niekum, Sachin Chitta, Andrew G Barto, Bhaskara Marthi, and Sarah Osentoski. Incremental semantically grounded learning from demonstration. In _Robotics: Science and Systems_ , volume 9, pages 10–15607. Berlin, Germany, 2013. 

- [64] Junhyuk Oh, Satinder Singh, Honglak Lee, and Pushmeet Kohli. Zero-shot task generalization with multi-task deep reinforcement learning. In _International Conference on Machine Learning_ , pages 2661–2670. PMLR, 2017. 

- [65] Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet: A generative model for raw audio. _arXiv preprint arXiv:1609.03499_ , 2016. 

- [66] Aaron van den Oord, Oriol Vinyals, and Koray Kavukcuoglu. Neural discrete representation learning. _arXiv preprint arXiv:1711.00937_ , 2017. 

- [67] Karl Pertsch, Youngwoon Lee, and Joseph J Lim. Accelerating reinforcement learning with learned skill priors. _arXiv preprint arXiv:2010.11944_ , 2020. 

- [68] Kate Rakelly, Aurick Zhou, Chelsea Finn, Sergey Levine, and Deirdre Quillen. Efficient off-policy meta-reinforcement learning via probabilistic context variables. In _International conference on machine learning_ , pages 5331–5340. PMLR, 2019. 

- [69] Dushyant Rao, Fereshteh Sadeghi, Leonard Hasenclever, Markus Wulfmeier, Martina Zambelli, Giulia Vezzani, Dhruva Tirumala, Yusuf Aytar, Josh Merel, Nicolas Heess, et al. Learning transferable motor skills with hierarchical latent mixture policies. _arXiv preprint arXiv:2112.05062_ , 2021. 

- [70] Jorma Rissanen. Modeling by shortest data description. _Automatica_ , 14(5):465–471, 1978. 

- [71] Melrose Roderick, Christopher Grimm, and Stefanie Tellex. Deep abstract q-networks. _arXiv preprint arXiv:1710.00459_ , 2017. 

- [72] Tanmay Shankar and Abhinav Gupta. Learning robot skills with temporal variational inference. In _International Conference on Machine Learning_ , pages 8624–8633. PMLR, 2020. 

14 

- [73] Tanmay Shankar, Shubham Tulsiani, Lerrel Pinto, and Abhinav Gupta. Discovering motor programs by recomposing demonstrations. In _International Conference on Learning Representations_ , 2020. URL `https://openreview.net/forum?id=rkgHY0NYwr` . 

- [74] Archit Sharma, Shixiang Gu, Sergey Levine, Vikash Kumar, and Karol Hausman. Dynamicsaware unsupervised discovery of skills. In _International Conference on Learning Representations_ , 2020. URL `https://openreview.net/forum?id=HJgLZR4KvH` . 

- [75] Arjun Sharma, Mohit Sharma, Nicholas Rhinehart, and Kris M Kitani. Directed-info gail: Learning hierarchical policies from unsegmented demonstrations using directed information. _arXiv preprint arXiv:1810.01266_ , 2018. 

- [76] Kyriacos Shiarlis, Markus Wulfmeier, Sasha Salter, Shimon Whiteson, and Ingmar Posner. Taco: Learning task decomposition via temporal alignment for control. In _International Conference on Machine Learning_ , pages 4654–4663. PMLR, 2018. 

- [77] Yuri M Shtarkov. Univresal sequential coding of single messages. _Prob. Pered. Inf._ , 23:175–186, 1987. 

- [78] Avi Singh, Huihan Liu, Gaoyue Zhou, Albert Yu, Nicholas Rhinehart, and Sergey Levine. Parrot: Data-driven behavioral priors for reinforcement learning. In _International Conference on Learning Representations_ , 2021. URL `https://openreview.net/forum?id=Ysuv-WOFeKR` . 

- [79] Sumedh A Sontakke, Sumegh Roychowdhury, Mausoom Sarkar, Nikaash Puri, Balaji Krishnamurthy, and Laurent Itti. Video2skill: Adapting events in demonstration videos to skills in an environment using cyclic mdp homomorphisms. _arXiv preprint arXiv:2109.03813_ , 2021. 

- [80] Richard S Sutton, Doina Precup, and Satinder Singh. Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. _Artificial intelligence_ , 112(1-2): 181–211, 1999. 

- [81] Daniel Tanneberg, Kai Ploeger, Elmar Rueckert, and Jan Peters. Skid raw: Skill discovery from raw trajectories. _IEEE Robotics and Automation Letters_ , 6(3):4696–4703, 2021. 

- [82] Sebastian Thrun and Anton Schwartz. Finding structure in reinforcement learning. _Advances in neural information processing systems_ , 7, 1994. 

- [83] Guillermo Valle-Perez, Chico Q Camargo, and Ard A Louis. Deep learning generalizes because the parameter-function map is biased towards simple functions. _arXiv preprint arXiv:1805.08522_ , 2018. 

- [84] Hado Van Hasselt, Arthur Guez, and David Silver. Deep reinforcement learning with double q-learning. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 30, 2016. 

- [85] Alexander Sasha Vezhnevets, Simon Osindero, Tom Schaul, Nicolas Heess, Max Jaderberg, David Silver, and Koray Kavukcuoglu. Feudal networks for hierarchical reinforcement learning. In _International Conference on Machine Learning_ , pages 3540–3549. PMLR, 2017. 

- [86] Jane X Wang, Zeb Kurth-Nelson, Dhruva Tirumala, Hubert Soyer, Joel Z Leibo, Remi Munos, Charles Blundell, Dharshan Kumaran, and Matt Botvinick. Learning to reinforcement learn. _arXiv preprint arXiv:1611.05763_ , 2016. 

- [87] Ziyu Wang, Tom Schaul, Matteo Hessel, Hado Hasselt, Marc Lanctot, and Nando Freitas. Dueling network architectures for deep reinforcement learning. In _International conference on machine learning_ , pages 1995–2003. PMLR, 2016. 

- [88] Mengjiao Yang and Ofir Nachum. Representation matters: Offline pretraining for sequential decision making. _arXiv preprint arXiv:2102.05815_ , 2021. 

- [89] Mengjiao Yang, Sergey Levine, and Ofir Nachum. Trail: Near-optimal imitation learning with suboptimal data. _arXiv preprint arXiv:2110.14770_ , 2021. 

- [90] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. Understanding deep learning (still) requires rethinking generalization. _Communications of the ACM_ , 64(3): 107–115, 2021. 

15 

- [91] Jesse Zhang, Karl Pertsch, Jiefan Yang, and Joseph J Lim. Minimum description length skills for accelerated reinforcement learning. In _Self-Supervision for Reinforcement Learning Workshop - ICLR 2021_ , 2021. URL `https://openreview.net/forum?id=r4XxtrIo1m9` . 

- [92] Zelin Zhao, Chuang Gan, Jiajun Wu, Xiaoxiao Guo, and Joshua B Tenenbaum. Augmenting policy learning with routines discovered from a demonstration. _arXiv preprint arXiv:2012.12469_ , 2020. 

- [93] Wenxuan Zhou, Sujay Bajracharya, and David Held. Plas: Latent action space for offline reinforcement learning. _arXiv preprint arXiv:2011.07213_ , 2020. 

- [94] Yifeng Zhu, Peter Stone, and Yuke Zhu. Bottom-up skill discovery from unsegmented demonstrations for long-horizon robot manipulation. _arXiv preprint arXiv:2109.13841_ , 2021. 

- [95] Luisa Zintgraf, Kyriacos Shiarlis, Maximilian Igl, Sebastian Schulze, Yarin Gal, Katja Hofmann, and Shimon Whiteson. Varibad: A very good method for bayes-adaptive deep rl via metalearning. _arXiv preprint arXiv:1910.08348_ , 2019. 

16 

## **A Derivations** 

**A.1** _p[⋆]_ _**z**_ **[is a valid density]** 

**Proposition A.1.** _p[⋆]_ _**z**_[(] _[ξ]_[)] _[ is a proper probability density function.]_ 

_Proof._ Recall that 

**==> picture [180 x 40] intentionally omitted <==**

A function is a probability density function if it is non-negative, continuous, and integrates to 1. By construction, _p[⋆]_ _**z**_[(] _[ξ]_[)][is][non-negative][since] _**[m]**[t][≥]_[0][and] _[δ]_[(] _**[z]**[t]_[=] _[ξ]_[)] _[≥]_[0][.][Further,] _[δ]_[(] _**[z]**[t]_[=] _[ξ]_[)] _T_ is continuous in _ξ_ so the numerator E _**τ**_ 1: _T_ _**z** ,_ 1: _**m** T_ 1: _T ,_ �� _t_ =1 _[δ]_[(] _**[z]**[t]_[=] _[ ξ]_[)] _**[m]**[t]_ �, an expectation containing _δ_ ( _**z** t_ = _ξ_ ), is also continuous in _ξ_ . Finally, 

**==> picture [426 x 125] intentionally omitted <==**

Therefore, _p[⋆]_ _**z**_[(] _[ξ]_[)][ satisfies all 3 properties of a probability density function.] 

**Remarks.** This result generalizes to the case for discrete _**z**_ by replacing the delta with an indicator function and integration with summation. 

## **A.2 Two expressions of** _L_ **CL** 

**Proposition A.2.** _The expected coding length of a trajectory is equal to the expected number skills multiplied by the marginal entropy:_ 

**==> picture [438 x 237] intentionally omitted <==**

_Proof._ 

17 

**==> picture [214 x 62] intentionally omitted <==**

**----- Start of picture text -----**<br>
T<br>= E τ  1: T , m 1: T , z 1: T � m t −p [⋆] z [(] [ξ] [) log] [ p][⋆] z [(] [ξ] [)] [dξ]<br>� �� � t =1 �� �� ξ �� �<br>n s Hp⋆ z  [ z ]<br>=  n s Hp⋆ z [ z ]<br>**----- End of picture text -----**<br>


**Remarks.** This result generalizes to the case for discrete _**z**_ by replacing the delta with an indicator function and integration with summation. Further, this rewriting not only offers an insightful interpretation of the objective but also has _different_ finite-sample gradient compared to the original form. We discuss its implication further in Section 4.4. 

## **A.3 Connection between LOVE and Variational Inference** 

Is the compression objective a prior in the framework of variational inference (VI)? The answer to this question is surprisingly nuanced. A bridge that connects VI and source coding is the bits-back coding argument [32, 33]. Under this scheme, the additional cost of communicating a message is equal to the KL divergence between the approximate posterior and the chosen prior distribution. This is because the posterior often does not match the prior and the sender must use more bits to send the message compared to using the prior exactly. In modern deep latent variable models such as VAE [42], the prior is in general chosen to be an isotropic Gaussian distribution or a sequence of isotropic Gaussian distributions that decomposes over the time steps. The bit-back coding argument shows that VI as a coding scheme is asymptotically optimal (in the limit of sending large numbers of messages), but it does not immediately guarantee good _representation learning_ . As a thought experiment, imagine we choose the dimension of the latent variable in a VAE to be equal to the dimension of the data itself. It is clear that the model is not incentivized to perform good representation learning, but the bit-backing coding scheme still guarantees asymptotic optimality. Instead, good representation can only emerge _if_ the prior is chosen properly. 

Contrary to this prevailing design choice, our latent variables _**z**_ 1: _T_ and _**m**_ 1: _T_ are not independent from each other and the timesteps are not independent from each other. In fact, the interaction between the latent variables is crucial for compressing the trajectory optimally in our framework. Therefore, our objective takes into account the _global_ structure of the latent variables. Note that _L_ CL also has the natural interpretation of measuring the average number of bits that is required to send a trajectory under the coding scheme of this work. As both quantities measure the cost of the communication, the philosophical parallel between KL divergence and _L_ CL is likely not a coincidence. In practice, we observe that _L_ CL also has comparable regularization effect on the latent code, and in some cases it is possible to learn a good model _without_ any KL divergence if _L_ CL is present. From this perspective, our compression objective is indeed a “prior” insofar as it specifies the desired properties of the posterior. Another interpretation of LOVE is that it is optimizing the prior _directly_ . 

Nonetheless, it is an open question whether _L_ CL has a precise counterpart in Bayesian inference, that is, it is not immediately obvious if it can be written as the KL divergence between the posterior _q_ ( _**z**_ 1: _T ,_ _**m**_ 1: _T |_ _**x**_ 1: _T_ ) and some prior distribution _p_ ( _**z**_ 1: _T ,_ _**m**_ 1: _T_ ). One complication, for example, is the fact that the log density of _**m**_ 1: _T_ does not participate in the computation of _L_ CL. It may be possible to construct some form of hierarchical priors that enables a fully Bayesian interpretation of _L_ CL, but it is also well-known that the MDL framework can accommodate codes that are not Bayesian (e.g., the Shtarkov normalized maximum likelihood code [77]). We do not offer a definitive answer to this question in this work, but the connection between Bayesian inference and _L_ CL is certainly an interesting direction for future works. 

## **B Evidence Lower Bound** 

## **B.1 VTA** 

We reproduce the data generating process of Kim et al. [40] here: 

**==> picture [380 x 30] intentionally omitted <==**

18 

VTA [40] shows that the ELBO can be written as: 

**==> picture [330 x 59] intentionally omitted <==**

Like most ELBO, this ELBO can be deconstructed into a reconstruction term: 

**==> picture [134 x 30] intentionally omitted <==**

and the remaining KL term _L_ KL( _**θ** ,_ _**φ**_ ). 

## **B.2 LOVE** 

We reproduce the data generating process of LOVE here. Instead of using _**φ**_ for the parameters of priors and decoder, we will merge all parameters into _**θ**_ : 

**==> picture [416 x 30] intentionally omitted <==**

For LOVE, the ELBO is re-written as: 

**==> picture [387 x 59] intentionally omitted <==**

Since _zt_ is a categorical distribution, we chose the uniform prior _p_ ( _zt_ ) similar to Oord et al. [66]. Similar to VTA, the loss is also decomposed into a reconstruction term and a KL term. 

## **C Sensitivity to Compression Objective Weighting** 

Here we study how sensitive LOVE is to the choice of _λ_ , the coefficient of _L_ CL. We tested 5 values of _λ ∈_ [0 _._ 01 _,_ 1] on _Simple_ and _Cond. Colors_ and applied dual gradient descent to automatically tune _λ_ . Stopping point is selected based on the shortest code length achieved. 

Table 3: The effect of different values of _λ_ and dual GD on F1 scores of _Simple Colors_ and _Conditional Colors_ over 5 seeds. 

|er 5 seeds.||||||||
|---|---|---|---|---|---|---|---|
|Simple (F1)<br>Cond. (F1)|_λ_=0_._01<br>_._67_± ._27<br>_._84_± ._06|_λ_=0_._03<br>_._80_± ._21<br>_._92_± ._02|_λ_=0_._1<br>_._91_± ._02<br>_._90_± ._03|_λ_=0_._3<br>_._95_± ._06<br>_._82_± ._08|_λ_=1_._0<br>_._74_± ._08<br>_._87_± ._08|_λ_(dual GD)<br>_._99_± ._00<br>_._99_± ._00|VTA|
||||||||_._82_± ._13<br>_._83_± ._19|



We see that while _λ_ can change the quality of solutions found, the performance is stable within a _±_ 3 _×_ regions around _λ_ = 0 _._ 1. Further, using dual GD _consistently_ outperforms handpicked _λ_ with an ELBO threshold _C_ slightly (e.g., 5%) higher than the _L_ ELBO achieved without compression, which can be obtained with minimal prior knowledge about the task. Hence _λ_ likely can be tuned without strong prior knowledge. This contrasts with the other methods such as Kipf et al. [43] which require knowing the number of skills in each demonstration to perform well while achieving the similar or better performance. 

19 

## **D Architecture** 

## **D.1 Frame Prediction** 

Our base architecture is similar to Kim et al. [40][2] and we highlight the difference blue. The parameters of the posteriors are implemented with neural networks. First, the observation _**x**_ 1: _T_ are encoded into a lower dimension embedding _**x**_ ˆ 1: _T_ with a `observation encoder` . The embedding is then passed through a `boundary posterior decoder` that outputs the parameters of _**m**_ 1: _T_ . The embedding is further passed through a GRU [10], _f_ s-rnn-fwd which runs on _**x**_ ˆ 1: _T_ and give the cell state `h` 1: _T_ . For _**z**_ 1: _T_ , we have two GRU’s with cell, _f_ z-rnn-bwd and _f_ z-rnn-bwd, which run on _**x**_ ˆ 1: _T_ in different temporal direction (i.e., _f_ z-rnn-bwd sees the future) to generate cell states `c`[fwd] 1: _T_[and] `[c]`[bwd] 1: _T_[.][For][each] time step _t_ , a candidate _**z**[′] t_[is sampled from a] _[ n][z]_[-dimensional categorical distribution][3][whose log] probability is a linear projection of `c`[fwd] _t ∥_ `c`[bwd] _t_ . The sampled _**z**[′] t_[are embedded linearly into a vector] of size 128. If _**m**_ 1 = 1, the _**z** t_ = _**z**[′] t_[; otherwise,] _**[ z]**[t]_[=] _**[z]**[t][−]_[1][4][.][Then we concatenate] `[ h]` _[t][−]_[1] _[∥]_ _**[z]**[t]_[and] linearly project the vector into the mean and standard deviation of a isotropic Gaussian in R[8] . A ˆ _**s** t_ is sampled from this Gaussian. 

Th model also keeps two “belief” vectors that keep track of the history of the computation. These vectors are modulated by two RNN, _f_ h-rnn and _f_ c-rnn. The abstraction belief _**c** t_ = _**m** t·f_ c-rnn( _**z** t,_ _**c** t−_ 1)+ (1 _−_ _**m** t_ ) _·_ _**c** t−_ 1. The observation belief _**h** t_ = _**m** t_ _**c** t−_ 1 + (1 _−_ _**m** t_ ) _· f_ h-rnnˆ(ˆ _**s** t∥_ _**c** t∥_ _**z** t,_ _**h** t−_ 1). Finally the state abstraction is computed as the linear projection of _**s** t_ = proj( _**h** t∥_ _**s** t_ ). The projection layer is 256 _×_ 128. Finally, _**s** t_ is passed through a `observation decoder` and decode into the reconstruction of _**x** t_ . Refer to Kim et al. [40] for more details and an illustration of the computation graph. 

For each convolutional layer or transposed convolution layer, the tuple’s values correspond to input channel, output channel, kernel size, stride, padding. With that notation in mind, the specific hyperparameters for each components are: 

- `observation encoder` : 4-layer convolutional neural network with {(3, 128, 4, 2, 1), (128, 128, 4, 2, 1), (128, 128, 4, 2, 1), (128, 128, 4, 1, 0)} with ELU activation [11] and batch normalization [34]. The output is flattened linearly projected to vector of size 128. 

- `boundary posterior decoder` is a 5-layer 1-D causal temporal convolution [65] with {(128, 128, 5, 1, 2) _×_ 5, (128, 2, 5, 1, 2)} with ELU activation and batch normalization. The output is the logits for the _**m**_ 1: _T_ . 

- _f_ z-rnn-bwd _, f_ z-rnn-fwd _, f_ s-rnn-fwd _, f_ c-rnn _, f_ h-rnn: GRU with cell size 128 

- `observation decoder` : 4-layer transposed convolutional layers {(128, 128, 4, 1, 0), (128, 128, 4, 2, 1), (128, 128, 4, 2, 1), (128, 3, 4, 2, 1)} with ELU activation and batch normalization on all but the last layer. The last layer has no normalization and has `tanh` activation. 

**Removing Boundary Regularization.** An important difference from Kim et al. [40] is that we do not enforce maximum number of subsequence _N_ max and the maximum length of subsequence _l_ max through the boundary prior (This effectively amounts to setting both to a value larger than the sequence length). These two hyperparameters’ effect are similar to that of picking the number of segments in CompILE [43] and provide strong training signal. This assumption is in general problematic since we cannot expect to know a priori what the good values are for these hyperparameters. Kipf et al. [43] demonstrates that the performance can suffer if this kind of supervision is wrong. On the other hand, we do not assume anything about the the duration of the subsequence or how many subsequences there are in each demonstration. 

We do, however, enforce a minimum length on the skill. While it is largely an optimization choice, we believe this prior is significantly weaker since useful options are almost always temporally extended. Indeed, with only the minimum length constraint, VTA is unable to learn good skills conducive for downstream tasks. 

> 2 `https://github.com/taesupkim/vta` 

> 3Kim et al. [40] uses a isotropic Gaussian. 

> 4This is the COPY action in Kim et al. [40]. 

20 

## **D.2 Multi-task Grid World Environment** 

For trajectories, we make some larger changes to the architecture to encode properties we want in a model for learning options, e.g., Markov property. Though similar in spirit, a large portion of the architecture is different from the base VTA model, so the difference will not be highlighted. 

For the posterior, we have an `observation encoder` and an `action encoder` that embeds both the state observation _**x**_ 1: _T_ and actions _**a**_ 1: _T_ to get embedding `a` 1: _T_ and `x` 1: _T_ each of size 128. The concatenation `a` _t∥_ `x` _t_ linear projected down to a vector of size 128. The embedding is then passed through a `boundary posterior decoder` that outputs the parameters of _**m**_ 1: _T_ . The embedding is further passed through a GRU [10], _f_ s-rnn-fwd which runs on _**x**_ ˆ 1: _T_ and give the cell state `h` 1: _T_ . For _**z**_ 1: _T_ , we have two GRU’s with cell, _f_ z-rnn-bwd and _f_ z-rnn-bwd, which run on _**x**_ ˆ 1: _T_ in different temporal direction (i.e., _f_ z-rnn-bwd sees the future) to generate cell states `c`[fwd] 1: _T_[and] `[ c]`[bwd] 1: _T_[.] 

For sampling _**z**_ is done differently for interaction data for better gradient and representation learning. Instead of doing straight-through estimator for the categorical random variable, we opt to use vector-quantization [66] with straight-through estimators. First, `c`[fwd] _t ∥_ `c`[bwd] _t_ is linearly projected into dimension 128. Then a ReLU is applied and another 128 by 128 linear layer is applied. The VQ codebook is of size _n_ _**z** ×_ 128. Instead of taking argmax of the codebook, we approximate the distribution to be proportional to the softmax over the distance over a temperature _tV Q_ . We can sample from this distribution and apply the straight-through gradient on the sampled code candidate _**z**[′]_ 1: _T_[.][If] _**[ m]**_[1][= 1][, the] _**[ z]**[t]_[=] _**[ z]**[′] t_[; otherwise,] _**[ z]**[t]_[=] _**[ z]**[t][−]_[1][.] 

We construct directly _**s** t_ = _**z** t∥_ `x` _t_ . and linearly project the vector into the mean and standard deviation of a isotropic Gaussian R[8] . _**s** t_ is sampled from this Gaussian and then decoded with the `action decoder` into the reconstructed action in _A_ . 

For each convolutional layer or transposed convolution layer, the tuple’s values correspond to input channel, output channel, kernel size, stride, padding. With that notation in mind, the specific hyperparameters for each components are: 

- `observation encoder` : This takes as input the 10 _×_ 10 _× N_ obj + 2 and is implemented as a two 2D convolutional layers with ReLU activations, followed by a linear layer with a ReLU activation and a linear layer with no activation. The convolutional layers have hyperparameters (12 _,_ 64 _,_ 3 _,_ 1 _,_ 0) and (64 _,_ 64 _,_ 3 _,_ 1 _,_ 0) respectively. The first linear has input dimension 6 _×_ 6 _×_ 64 and output dimension 128. The second linear layer has input and output dimensions 128. 

- `action encoder` : The actions are embedded with an embedding matrix with embedding dimension 128. 

- `boundary posterior decoder` is a 5-layer 1-D causal temporal convolution [65] with {(128, 128, 5, 1, 2) _×_ 5, (128, 2, 5, 1, 2)} with ELU activation and batch normalization. The output is the logits for the _**m**_ 1: _T_ . 

- _f_ z-rnn-bwd _, f_ z-rnn-fwd _, f_ s-rnn-fwd: GRU with cell size 128 

- `action decoder` : The decoder is implemented as three linear layers with ReLU activations, followed by a linear layer with no activation. The (input, output) dimensions of these layers are as follows: (128 _,_ 128) _,_ (128 _,_ 128) _,_ (128 _,_ 128) _,_ (128 _,_ 5), where the last layer outputs logits over the actions. 

## **D.3 3D Navigation Environment** 

The architecture used in the 3D navigation environment is identical to that of the multi-task environment detailed above, with the exception that the `observation encoder` is changed to handle visual inputs. Specifically, the `observation encoder` is a a 3-layer convolutional neural network parameters (3 _,_ 32 _,_ 5 _,_ 2 _,_ 0) _,_ (32 _,_ 32 _,_ 5 _,_ 2 _,_ 0) _,_ (32 _,_ 32 _,_ 4 _,_ 2 _,_ 0), followed two linear layers (7520 _,_ 128) _,_ (128 _,_ 128) with a ReLU activation in between. 

## **D.4 Hierarchical Reinforcement Learning** 

For all approaches, we parametrize the policy as a double dueling deep Q-network [57, 87, 84]. The parametrization of the Q-function consists of a state embedding followed by two linear layer heads for 

21 

the state-value _Vθ_ ( _s_ ) function and the advantage _Aθ_ ( _s, a_ ) function. Then the Q-function is computed as _Qθ_ ( _s, a_ ) = _Vθ_ ( _s_ ) + _Aθ_ ( _s, a_ ) _− |A|_ 1 � _a[′] ∈A[A][θ]_[(] _[s, a]_[)][.] 

The value function _Vθ_ ( _s_ ) and advantage function _Aθ_ ( _s, a_ ) are computed as linear layers with output dimension 1 and _|A|_ respectively on top of the embedding _e_ ( _s_ ) of the state _s_ . Recall that the state _s_ consists of two portions: the observation _o_ of the grid or 3D environment, and the instruction _i_ corresponding to the next object to pick up, where the instruction is not present in the demonstrations. The embedding _e_ ( _s_ ) of the state _s_ is computed by embedding the observation _e_ ( _o_ ) with the `observation encoder` defined in the previous sections, and embedding the instruction _e_ ( _i_ ) with a 16-dimensional embedding matrix. Then, the embedding _e_ ( _s_ ) is a final linear layer with output dimension 128 applied to a ReLU of the concatenation of _e_ ( _o_ ) and _e_ ( _i_ ). 

## **E Hardware** 

All our experiments are conducted on a GeForce RTX 2080 Ti or a GeForce RTX A6000. 

## **F Hyperparameters** 

## **F.1 Frame Prediction** 

For these set of experiments, we use the same architecture and hyperparameters as Kim et al. [40]. The hyperparameters used for both _Simple Colors_ and _Conditional Colors_ are: 

- KL divergence weight _β_ : 1 _._ 0 

- MDL objective weight _λ_ (fixed) : 0 _._ 1 

- Mini-batch size: 512 

- Training iteration: 30000 

- Number of skills _nz_ = 10 

## **F.2 Multi-task Grid World Segmentation** 

We use the following hyperparameters for skill learning from demonstrations on the multi-task grid world environment experiments. 

- KL divergence weight _β_ = 0: 

   - We found that the compression objective readily provides strong and sufficient regularization for the latent code. Adding additional KL divergence often results in the model not being able to reconstruct the actions properly. 

- MDL objective weight _λ_ : 

   - We use a adaptive scheduling that approximate dual gradient descent. _λ_ is initialized to 0. After every gradient step, _λ_ is increased by 2 _._ 0 _×_ 10 _[−]_[5] if _L_ ELBO _≤_ 0 _._ 05 (Since _β_ = 0, this is effectively _L_ rec); otherwise, _λ_ is decreased by 2 _._ 0 _×_ 10 _[−]_[5] . After each update, the value of _λ_ is clipped to [0 _,_ 0 _._ 05]. We find this setting provides the most stable training. 

- Mini-batch size: 64 

- Training iteration: 20000 

- Number of skills _nz_ = 10 

- _t_ VQ = 0 _._ 1 

- Learning rate: 0 _._ 0005 with Adam Optimizer 

## **F.3 3D Visual Navigation Segmentation** 

We use the same hyperparameter as Multi-task grid world experiments except that the maximum _L_ ELBO is capped at 0 _._ 001, _i.e._ , _L_ ELBO _≤_ 0 _._ 001. 

22 

## **F.4 Hierarchical Reinforcement Learning** 

We use the same hyperparameters for training the policy for all approaches. Specifically, these hyperparameter values are as follows: 

- _ϵ_ -greedy schedule: We linearly decay _ϵ_ from 1 to 0 _._ 01 over 500 _K_ timesteps for dense reward settings and over 5 _M_ timesteps for sparse reward settings in the multi-task grid world environment. In the 3D visual navigation environment, we decay over 250 _K_ timesteps. 

- Discount factor _γ_ : We use _γ_ = 0 _._ 99 in all of the DQN updates. 

- Maximum replay buffer size: 50K 

- Minimum replay buffer size before updating: 500 

- Learning rate: 0.0001 with the Adam optimizer [41] 

- Batch size: 32 

- Update frequency: every 4 timesteps 

- Target syncing frequency: every 50K updates for multi-task grid world environment, every 30K updates for 3D navigation 

- Gradient _ℓ_ 2-norm clipping: 10 

- Marginal threshold _α_ = 0 _._ 001 

Since the demonstrations do not contain the instruction list observations, we set those to 0 in the demonstrations for the behavior cloning approach. Though we use _α_ = 0 _._ 001 in all of the experiments for consistency, we also found that slightly higher values of _α_ yielded greater sample efficiency for LOVE. 

## **G Algorithm** 

The Lagrangian for the unconstrained optimization problem is: 

min _**θ**_[max] _λ≥_ 0 _[λ][L]_[CL][(] _**[θ]**_[) + (] _[L]_[ELBO][(] _**[θ]**_[)] _[ −][C]_[)] _[ .]_ 

In standard KKT condition, the dual variable is introduced on the ELBO, but the two problems are equivalent by inverting the dual variable. Since the only constraint on _λ_ is that it is non-negative, this transformation does not change the optimal solution. Further note that we find that in many cases, choosing a fixed constant value for _λ_ is sufficient for solving the problem. 

**Algorithm 1 Learning Options via Compression** (LOVE): We highlight differences between our method and prior work (VTA) in blue. 

1: Initialize model parameters _**θ**_ 2: **while** not converged **do** 3: Sample a trajectory ( _**x**_ 0 _,_ _**a**_ 0 _, . . . ,_ _**x** T_ ) from the pre-collected experience _D_ 4: **for** _t_ = 1 _,_ 2 _, . . . , T_ **do** 5: Sample boundary conditioned on entire trajectory _mt ∼ q_ _**θ**_ ( _mt |_ _**x**_ 1: _t_ ) 6: Sample skill from skill posterior _zt ∼ q_ _**θ**_ ( _zt | mt,_ _**x**_ 1: _t,_ _**a**_ 1: _t_ ) 7: Sample abstraction from abstraction posterior _**s** t ∼ q_ _**θ**_ ( _**s** t | zt,_ _**x** t_ ) 8: Compute probability of the correct action from the decoder _p_ _**θ**_ ( _**a** t |_ _**s** t_ ) 9: **end for** 10: Compute lower bound on maximum likelihood objective _L_ ELBO according to Equation 4 11: Compute compression objective _L_ CL according to Equation 1 12: Update _**θ** ←_ _**θ** − η∇_ ( _L_ ELBO + _λL_ CL) and _λ_ 13: **end while** 

23 

**Algorithm 2** Executing skill _**z**_ 

- 1: **while** skill has not terminated **do** 

- 2: Compute state abstraction _µ_ _**s** t_ = E _s∼q_ _**θ**_ ( _**s** t|_ _**z** ,_ _**x** t_ ) [ _s_ ] 3: Take action _**a** t_ = arg max _**a** p_ _**θ**_ ( _**a** | µ_ _**s** t_ ) 4: Observe next state _**x** t_ +1 5: Terminate if E _**m** t_ +1 _∼q_ _**θ**_ ( _**m** t_ +1 _|_ _**x**_ 1: _t_ +1) [ _**m** t_ +1] _>_ 0 _._ 5 6: **end while** 

24 

## **H Visualization of Learned Skills** 

**==> picture [342 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
Skill 1 Skill 2 Skill 3 Skill 4 Skill 5<br>Skill 6 Skill 7 Skill 8 Skill 9 Skill 10<br>**----- End of picture text -----**<br>


**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [45 x 63] intentionally omitted <==**

**==> picture [36 x 63] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 6] intentionally omitted <==**

**==> picture [5 x 6] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

Figure 8: Skill visualization for all 10 skills of LOVE. 

**==> picture [397 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Skill 1 Skill 2 Skill 3 Skill 4 Skill 5<br>-7<br>-5<br>-3<br>-1<br>1<br>3<br>5<br>7<br>-7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7<br>Skill 6 Skill 7 Skill 8 Skill 9 Skill 10<br>-7<br>-5<br>-3<br>-1<br>1<br>3<br>5<br>7<br>-7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7 -7 -5 -3 -1 1 3 5 7<br>Horizontal change<br>Vertical change<br>Vertical change<br>**----- End of picture text -----**<br>


Figure 9: Heat map the agent’s end position minus the agent’s start position after applying each skill. In other words, this shows what direction the agent moves in after following each skill. 

In Figure 8, we visualize the behavior of following each of LOVE’s 10 skills on an example task. Each skill moves to and picks up an object, and the total set of skills covers 3 of the 4 object types in the task. These skills pick up both nearby objects, such as the tree in skill 2, as well as more distant objects, such as the diamond in skill 1. This contrasts DDO and VTA, which do not learn skills that move to and pick up objects. 

To further understand what each of LOVE’s skills does, we analyze whether there is a correlation between each skill and either the type of object it picks up, or the location of the object it picks up. We find that there appears to be little correlation between each skill and the type of object it picks up. Plotting the frequency of picking up each object type by skill shows that each skill picks up each object type with roughly the same frequency. Instead, there appears to be a correlation between each skill and the location of the object it picks up, illustrated in Figure 9. For example, skill 1 appears to specialize in moving to and picking up objects that are above the agent, while skill 7 tends to pick up objects that are up and to the right of the agent. It is also interesting to note that some skills are much more biased to move in certain direction (e.g., skill 1, 6, 7) while some appear to be more general (e.g., 4, 5, 8, 9) and move in any direction. Note in Figure 8, it may seem LOVE’s skills seem short / redundant. This is due to the fact that LOVE’s skills each pick up an object, so they 

25 

naturally appear short when the agent is close to the objects, as in Figure 8. However, when the agent is far away from the objects, the skills still pick up the objects and are much longer. From Figure 9, we can see from the heatmap that even the skills that appear to do same thing in Figure 8 have very distinct behaviors depending on the state they are in. Also, recall LOVE imposes a sparse distribution over skills (Section 5). After filtering, skill 3, 7 and 10 in Figure 8 are dropped since they have low marginal probability and are not used to describe a significant part of the trajectories. Figure 8 includes redundant skills LOVE does not use; the used skills in the sparse distribution have little redundancy. 

## **I Option Critic Results** 

**==> picture [334 x 123] intentionally omitted <==**

**----- Start of picture text -----**<br>
Npick = 3 (Dense) Npick = 5 (Sparse)<br>2.00<br>1.75 0.04<br>1.50<br>0.02<br>1.25<br>1.00 0.00<br>0.75<br>0.50 0.02<br>0.25 0.04<br>0.00<br>0 50000 100000 150000 200000 0 100000 200000 300000 400000<br>step step<br>Figure 10: Results of running option critic [4] on 2 of the settings we considered in Figure 5.<br>reward reward<br>**----- End of picture text -----**<br>


Option critic [4] is a classical online HRL algorithm. We show the results of running option critic[5] on two of the four RL tasks we considered in Figure 10. The best return achieved over the training is shown in Table 4. We set the number of option to 8 following Bacon et al. [4] and leave other hyperparameters untouched. _N_ pick = 3 with dense reward is the easily setting and _N_ pick = 5 with sparse reward is the hardest setting. We see that in _N_ pick = 3, option critic is able to reach reward of 2 (maximum possible is 3) at around 1M environment steps but the performance deterioates afterwards. In _N_ pick = 5, the algorithm fails to make any meaningful progress. These observations may suggest online HRL algorithms like option critic may be insufficient for solving these tasks. 

|tion-Critic<br>VE(Ours)|_N_pick = 3(Dense)<br>2_._0<br>**3****_._0**|_N_pick = 5(Sparse)|
|---|---|---|
|||0_._0<br>**0****_._7**|



Table 4: Comparison between LOVE and Bacon et al. [4] on the two RL tasks we consider in this work. Each entry is the maximum average return achieved during the course of training for both algorithms. For _N_ pick = 3 (Dense), 3 _._ 0 is the maximum possible return. For _N_ pick = 5 (Sparse), 1 _._ 0 is the maximum possible return. 

## **J Comparison to Zhang et al. [91]** 

|Precision<br>Recall<br>F1|_Simple Colors_<br>**MDL**<br>**LOVE**<br>0_._87<br>**0****_._99**<br>0_._78<br>**0****_._85**<br>0_._82<br>**0****_._91**|_Conditional Colors_<br>**MDL**<br>**LOVE**<br>0_._84<br>**0****_._99**<br>0_._82<br>**0****_._83**<br>0_._83<br>**0****_._90**|_Navigation_<br>**MDL**<br>**LOVE**<br>0_._79<br>**0****_._90**<br>0_._34<br>**0****_._94**<br>0_._48<br>**0****_._92**|_Navigation_<br>**MDL**<br>**LOVE**<br>0_._79<br>**0****_._90**<br>0_._34<br>**0****_._94**<br>0_._48<br>**0****_._92**|
|---|---|---|---|---|
||||0_._79<br>0_._34<br>0_._48|**0****_._90**<br>**0****_._94**<br>**0****_._92**|



Table 5: Comparison between LOVE and Zhang et al. [91] on the three segmentation tasks we consider in this work. We refer to Zhang et al. [91] as **MDL** in the table. 

> 5 `https://github.com/lweitkamp/option-critic-pytorch` 

26 

Zhang et al. [91] learn open-loop skills, which do not condition on the state and therefore cannot adapt to different states. Further, the MDL used in Zhang et al. [91] is equivalent to the variational inference used by VTA (on a different graphical model), which can be seen as greedily compressing each skill independently, rather than compressing a whole trajectory as LOVE does. Table 5 reports segmentation results on the Color domain and grid world, akin to Tables 2 and 3. Zhang et al. [91] performs the same as VTA on the Color domains – as they both use variational inference and there is no state – which achieves lower precision / recall than LOVE. On the grid world navigation, Zhang et al. [91] fails to recover the boundaries, unlike LOVE, because skills that navigate to objects require observing the state. This problem is shared by all open-loop approaches. 

## **K Number of Initial Skills Ablation** 

|Precision<br>Recall<br>F1|_K_ = 2<br>0_._27<br>0_._53<br>0_._35|_K_ = 5<br>0_._80<br>0_._91<br>0_._86|_K_ = 10<br>0_._90<br>0_._94<br>0_._92|_K_ = 15<br>0_._96<br>0_._96<br>0_._96|_K_ = 20<br>0_._96<br>0_._95<br>0_._95|_K_ = 30|_K_ = 50|
|---|---|---|---|---|---|---|---|
|||||||0_._95<br>0_._96<br>0_._95|0_._95<br>0_._93<br>0_._94|



Table 6: Performance of LOVE on the grid navigation task with varying number of initial skills (K). 

The number of skills to extract from demonstrations is often not known a priori, so choosing an appropriate value of the number of initial skills before filtering _K_ is important. Intuitively, we hypothesize that _K_ can be set conservatively: LOVE requires at least a minimum number of skills in order to fit the behaviors in the demonstrations, but may be able to gracefully prune out skills if _K_ is set too high via the filtering described in Section 5. We test this intuition by varying _K ∈{_ 2 _,_ 5 _,_ 10 _,_ 15 _,_ 20 _,_ 30 _,_ 50 _}_ and measuring the segmentation performance on the grid world multitask domain, and find that it appears to hold true in Table 6. For smaller values of _K_ , such as _K_ = 2 and _K_ = 5, LOVE’s F1 scores significantly degrade. However, performance remains high for all values where _K_ is sufficiently large. Hence, we conservatively sizing _K_ to be a large number. 

## **L Comparison to Different Regularizers** 

|Precision<br>Recall<br>F1|`entropy`<br>0_._26<br>0_._53<br>0_._35|`num switch`<br>0_._80<br>0_._93<br>0_._86|`VTA(3,5)`<br>0_._34<br>0_._46<br>0_._39|`VTA(3,10)`<br>0_._40<br>0_._60<br>0_._48|`VTA(5,5)`<br>0_._34<br>0_._50<br>0_._40|`VTA(5,10)`|LOVE|
|---|---|---|---|---|---|---|---|
|||||||**0.95**<br>0_._43<br>0_._37|0.90<br>**0.94**<br>**0.92**|



Table 7: Comparison of different kinds of regularizers that have been used in the literature for skill segmentation. LOVE outperforms all significantly. 

Several prior methods encourage skills to act for more timesteps or prevent skills from switching too frequently, which can similarly help avoid degenerate solutions like LOVE. We note that such prior methods do not necessarily yield skills that help learn new tasks, while the maximum of LOVE’s objective achieves the information-theoretic limit of compressing the trajectories (under a fixed function class), which is not done in other works. We empirically compare LOVE with several such methods on the segmentation of the multi-task grid world domain, including: 

1. _Entropy_ : This approach regularizes the entropy of skill marginal akin to Shankar et al. [73], which they refer to this as _parsimony_ . Specifically, this approach adds a regularization term _Hp⋆_ _**z**_ [ _**z**_ ] to the objective _L_ ELBO. 

2. _Num switches_ : This approach penalizes switching between skills, similar to Harb et al. [28], a variant of the Option-Critic framework [4]. Specifically, this approach adds a penalty _n_ s to the objective _L_ ELBO equal to the number of switches (i.e., the number of times _mt_ = 1) in a demonstration. 

27 

3. VTA( _N_ max _, l_ max): VTA includes a prior on its boundary variables, which effectively sets the maximum number of skills per episode to be _N_ max and sets the maximum number of actions a skill can take to _l_ max. We experiment with several settings of _N_ max and _l_ max, including those that use prior knowledge about the domain not used by LOVE. 

The results are summarized in Table 7. We find that regularizing the number of switches performs fairly well, but LOVE achieves higher F1 than other approaches that regularize the skills. 

28 

