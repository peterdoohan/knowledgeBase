https://doi.org/10.1038/s41593-022-01211-5 

## **nature neuroscience** 

## **Article** 

## **Arithmetic value representation for hierarchical behavior composition** 

Received: 8 December 2021 **Hiroshi Makino** Accepted: 21 October 2022 Published online: xx xx xxxx The ability to compose new skills from a preacquired behavior repertoire is a hallmark of biological intelligence. Although artificial agents extract Check for updates reusable skills from past experience and recombine them in a hierarchical manner, whether the brain similarly composes a novel behavior is largely unknown. In the present study, I show that deep reinforcement learning agents learn to solve a novel composite task by additively combining representations of prelearned action values of constituent subtasks. Learning efficacy in the composite task was further augmented by the introduction of stochasticity in behavior during pretraining. These theoretical predictions were empirically tested in mice, where subtask pretraining enhanced learning of the composite task. Cortex-wide, two-photon calcium imaging revealed analogous neural representations of combined action values, with improved learning when the behavior variability was amplified. Together, these results suggest that the brain composes a novel behavior with a simple arithmetic operation of preacquired action-value representations with stochastic policies. 

Humans and other animals can repurpose their preacquired behavior skills to new, unseen tasks. Such an aptitude can grow their behavior repertoire through combinatorial expansion[1][–][4] . Research in the artificial intelligence (AI) field of deep reinforcement learning (deep RL) posits that reuse of past experience can dramatically improve learning of tasks that can be broken down into simpler subproblems[5][–][9] . The linear arithmetic operation on prelearned action values ( _Q_ ) derived from each subproblem leads to composition of a new nearly optimal policy, which can be transferred and further fine-tuned for a novel task[10][,][11] . However, it remains largely unknown whether the brain similarly creates a novel behavior. 

In deep RL, policy entropy can be harnessed for agents to express a stochastic policy and learn multiple modes of nearly optimal behavior[12] . Maximum entropy policies endow agents with flexibility and robustness to perturbation. Furthermore, pretraining agents with maximum entropy policies enhance composability of a new behavior by providing better initialization to maintain the ability to explore in new settings[10][,][13] . In neuroscience, initially high behavior variability is similarly shown to be important for motor learning in humans and other animals[14][,][15] . Such a correspondence between artificial and biological systems prompts the question of whether there is algorithmic convergence to promote exploration for future learning. 

As deep supervised and unsupervised learning have been pivotal to model neural activity in the visual system[16][–][19] , deep RL invites direct comparisons in representational learning underlying reward-based learning between the brain and the machine[20][–][22] . Inspired by the theoretical frameworks established in deep RL, in the present study I used cortex-wide, two-photon calcium imaging to empirically test whether these algorithmic features are leveraged in the mouse cortex while mice hierarchically solve a novel composite task. The results suggest that building blocks of stochastic policies acquired during pretraining can be combined to compose a nearly optimal policy for a downstream task with a minimum degree of fine-tuning. 

## **Results** 

## **Hierarchical composition of a novel behavior in mice** 

I developed an object manipulation task in which head-restrained mice hierarchically combined two previously learned subtasks. In the first subtask (‘Task 1’), mice were trained to use a joystick to remotely move a light-emitting diode (LED)-attached object in an arena of 10 × 10 cm[2] from a random location toward a reward zone in the center (4 × 4 cm[2] )[22] (Fig. 1a and Extended Data Fig. 1a,b). Each trial was completed when the object successfully reached the reward zone (hit) or when 5 min 

Lee Kong Chian School of Medicine, Nanyang Technological University, Singapore, Singapore. e-mail: hmakino@ntu.edu.sg 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [439 x 381] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Task 1 Task 2 b ***<br>0.8 Task 1<br>Task 2<br>LED<br>Object Object 0.4<br>Arena Arena 0<br>Object trajectory in Task 1  Joystick Lick in Task 2 *<br>0.8<br>Composite task<br>0.4<br>Object LED 10 s<br>Early Late Response period 0<br>Arena<br>Joystick<br>c Task 1 d Composite task e Object trajectory State value and policy 1.0<br>60 Task 2 100<br>80 *** 1<br>40 60<br>40<br>20 Pretraining<br>20 Scratch 5<br>0 0<br>1 2 3 4 5 Session 1 Session 5 0.0<br>Session Early Late<br>f SAC g<br>Actor Critic Task 1 Task 2 Composite task<br>Agent<br>State<br>State πθ Qф<br>Action<br>Q Task1 Q Task2 ( Q Task1+ Q Task2)/2<br>h Task 1 Task 2 i Composite task j Agent trajectory State value and policy 1.0<br>1.0 1.0 ***<br>NS<br>*** Early<br>0.5 *** 0.5 Average<br>Scratch<br>Max. Late<br>0 0<br>100 200 100 200 Early Late 0.3<br>Early Late<br>Epoch Epoch<br>Task1<br>Q<br>Mean<br>Task2<br>Q<br> Mean<br>Naive Expert<br>to expert Session<br>Session no. Correct (%) State value<br>Subtask<br>Q<br>Return<br>State value<br>Mean<br>**----- End of picture text -----**<br>


**Fig. 1 | Hierarchical composition of a novel behavior in mice and deep RL** 

**agents. a** , Schematic of the behavior paradigm for mice. Mice learned the two subtasks before the composite task. **b** , Increases in action values ( _Q_ ) averaged over states and actions during subtask learning in mice (Task 1:[***] _P_ < 0.001, _n_ = 6 and 7 mice for naive and expert, respectively; Task 2:[*] _P_ = 0.01, _n_ = 7 mice for naive and expert, one-tailed bootstrap, mean ± s.e.m.). **c** , Number of sessions required to reach the expert stage for each subtask in mice ( _n_ = 7 mice for Tasks 1 and 2, mean ± s.e.m.). **d** , Learning curve for the composite task with and without pretraining in subtasks in mice ([***] _P_ < 0.001 compared with the first session, _n_ = 7 and 6 mice for pretraining and scratch, respectively, one-tailed bootstrap, mean ± s.e.m.). **e** , Example object trajectories (trial duration: session 1: 96.1 ± 27.5 s; session 5: 17.2 ± 9.3 s, mean ± s.e.m., 7 mice), state-value functions 

(color) and policies (vector field) in sessions 1 and 5 of the composite task in mice. **f** , Neural network architecture of deep RL agents trained with the SAC algorithm. _πθ_ is a policy, defined as an action probability given a state and parameterized by _θ. Qφ_ is an action value for a given state–action pair and parametrized by _φ_ . **g** , Schematic of the behavior paradigm for deep RL agents. **h** , Increases in mean action values ( _Q_ ) during subtask learning in deep RL agents ([***] _P_ < 0.001 for Tasks 1 and 2, _n_ = 6 agents, one-tailed bootstrap between naive and expert, mean ± s.e.m.). **i** , Learning curve for the composite task with average _Q_ , maximum _Q_ and without pretraining in subtasks in deep RL agents (average:[***] _P_ < 0.001 compared with scratch; maximum: NS, _P_ = 0.89 compared with scratch, _n_ = 6 agents, one-tailed bootstrap at the early stage with Bonferroni’s correction, mean ± s.e.m.). **j** , Same as **e** for deep RL agents. Early session: 20th epoch; late session: 200th epoch. 

had elapsed (miss). In the second subtask (‘Task 2’), mice were trained to lick a water spout placed on the stationary LED-attached object located in front of them (Fig. 1a and Extended Data Fig. 1a,c). Each trial ended when mice licked the water spout during a response period, which started 2 s after the LED onset (hit) or when 5 min had passed (miss). During Task 1, mice learned to manipulate the joystick to move (or not to move) the object (action) in each position of the arena (state). During Task 2, mice learned to associate the state of the LED-attached object (LED on/off status and its location) with licking (or no licking) action; over learning, their lick rate during the LED-on period became relatively higher than during the LED-off period ( _P_ = 0.008, _n_ = 7 mice, one-tailed bootstrap). Subtask learning was evident from an increase in the correct rate or a decrease in the trial duration (Extended Data Fig. 1a). In each subtask, I measured the action-value function ( _Q_ function), an RL variable defined as the 

expected sum of future rewards when mice take a particular action _a_ given a state _s_ according to: 

**==> picture [179 x 13] intentionally omitted <==**

where 𝔼 _π_ is an expectation under a policy _π_ , _Rt_ +1 a reward at time _t_ + 1 sampled every 10 ms, _γ_ a discount factor (0.99) and _V_ ( _st_ +1) a state-value function defined as: 

**==> picture [208 x 14] intentionally omitted <==**

where _T_ is a trial end. As the reward was obtained only at the terminal state, _V_ ( _s_ ) can be simplified as[22] : 

**==> picture [155 x 13] intentionally omitted <==**

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

Thus, _Q_ is a monotonic function of how fast either the object reaches the reward zone from each location (Task 1) or mice lick the water spout (Task 2) during the response period when the LED is on. Mean _Q_ over states and actions increased during learning of these subtasks, with improvements in _V_ ( _s_ ) and _π_ (Task 1: _P_ < 0.001, _n_ = 6 and 7 mice for naive and expert, respectively; Task 2: _P_ = 0.01, _n_ = 7 mice for naive and expert, one-tailed bootstrap; Fig. 1b and Extended Data Fig. 1b,c). These results demonstrate that mice learned to solve these subtasks more optimally. 

After mice became proficient at these subtasks, they were introduced to a new composite task where the water spout was attached to the object but was movable. In the composite task, mice combined preacquired knowledge in the two subtasks by moving the water spout (action) to a reachable location in the arena (state) while the LED was on (state) and lick the spout (action) to obtain a reward (Fig. 1a). I hypo thesized that successful hierarchical composition of a new behavior was reflected by few-shot learning where only a few trials were necessary to achieve good performance. Although behavior training for the two subtasks took approximately 2–3 months (Fig. 1c), mice generally learned the composite task within one session ( _P_ < 0.001 compared with no pretraining, _n_ = 6 and 7 mice for naive and expert, respectively, one-tailed bootstrap; Fig. 1d). Trajectory analysis revealed nearly optimal _V_ ( _s_ ) and _π_ even in the first session (Fig. 1e). Notably, mice did not simply complete the two subtasks serially because the object was directed toward the bottom center of the arena during the early stage of the composite task (Fig. 1e and Extended Data Fig. 2a). These results demonstrate few-shot learning in mice through hierarchical combination of subtask policies. 

## **Hierarchical policy composition in deep RL agents** 

To build theoretical models to understand how the brain composes a novel behavior, artificial deep RL agents were trained in the same tasks with Soft Actor-Critic (SAC), a model-free actor-critic algorithm based on the maximum entropy RL framework[23][,][24] (Fig. 1f,g). SAC is an off-policy algorithm that reuses past experiences to improve sample efficiency. SAC was selected because accumulating evidence suggests that animal learning may involve actor-critic-like mechanisms[21] and its relevance to policy composition[10] . Although traditional actor-critic algorithms aim to maximize only the expected cumulative sum of future rewards, SAC additionally maximizes policy entropy according to the objective _J_ ( _π_ ): 

**==> picture [204 x 24] intentionally omitted <==**

where _ρπ_ is a state–action marginal of the trajectory distribution determined by _π, r_ ( _st_ , _at_ ) a reward given a state _st_ and action _at_ at time _t_ , _α_ a temperature parameter to determine the relative contribution of the policy entropy term against the reward and ℋ an entropy of _π_ . _π_ (·| _st_ ) describes a probability of any action given a state _st_ . Intuitively, maximum entropy policies in SAC encourage exploration and capture multimodal solutions to the same problem by assigning a nonzero probability to all actions while sampling more promising avenues with a higher probability[13] . This property endows the agent with robustness to perturbation and flexibility. Importantly, theoretical analysis has demonstrated that (1) independently trained maximum entropy policies can be composed offline by adding their _Q_ functions and (2) composability of a new policy depends on the entropy of the constituent subpolicies[10] . With a deep artificial neural network (ANN), the actor computes _π_ , whereas the critic estimates the _Q_ function. Following a previous study[23] , I constructed deep RL agents composed of actor and critic ANNs, each of which contained 3 hidden layers with 256 units (Fig. 1f). I confirmed that the agents trained for the subtasks improved task performance with gradual increases in their mean _Q_ and _V_ ( _s_ ) and _π_ being optimized 

( _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap; Fig. 1h and Extended Data Fig. 1d–f). 

Research in deep RL established that individual _Q_ functions obtained from each subtask can be averaged to derive a new composite _Q_ ( _Q_ Composite) function to extract a new approximately optimal policy according to: 

**==> picture [205 x 22] intentionally omitted <==**

where _Q_[∗] Composite[ is the true optimal ] _[Q]_[ function of the composite task, ] _Q_ Σ represents a newly derived composite _Q_ function via averaging, _C_ is defined as _C_ ⊆ {1, …, _K_ } of _K_ tasks, | _C_ | is the number of subtasks and _Q_[∗] _i_[ the optimal ] _[Q]_[ function of the ] _[i]_[th subtask][10][,][11][. This approximation ] has proven to be true when the constituent subpolicies agree on an action or are indifferent to each other’s actions[10] . The _Q_ Composite function acquired during pretraining can be transferred and further fine-tuned to be closer to the _Q_[∗] Composite[ function to solve a downstream task.] 

I tested whether such a simple arithmetic operation on subtask-derived _Q_ functions ( _Q_ Subtask) enabled agents to solve the new composite task more efficiently (Fig. 1g). When introduced to the composite task, agents initialized with the combined _Q_ function showed rapid learning compared with those learning from scratch ( _P_ < 0.001 compared with scratch, _n_ = 6 agents, one-tailed bootstrap with Bonferroni’s correction; Fig. 1i). Agent’s trajectories and resulting _V_ ( _s_ ) and _π_ were nearly optimal even at the early stage of training; the agents moved to the bottom center of the arena instead of serially completing the two subtasks (Fig. 1j and Extended Data Fig. 2a). By contrast, when the composite function was constructed by another method via computing the maximum of the two _Q_ Subtask functions, composite task learning remained slow ( _P_ = 0.89 compared with scratch, _n_ = 6 agents, one-tailed bootstrap; Fig. 1i). Moreover, agents with control initialization by modifying Task 2 contained the same overall _Q_ but failed to rapidly learn the composite task ( _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap; Extended Data Fig. 2b). Notably, agents trained with the model-based policy optimization (MBPO) algorithm, which iteratively builds an ensemble of forward dynamic models and uses model-free SAC as a policy optimization algorithm under the learned model[25] , learned the composite task faster than those without the model ( _P_ = 0.006, _n_ = 10 agents, one-tailed bootstrap; Extended Data Fig. 2c). This suggests that model construction can further augment the sample efficiency even without pretraining. These results reveal that averaging _QS_ ubtask functions facilitated effective learning in the artificial agents. 

## **Emergence of neural representations of** _**Q**_ **Subtask functions** 

To investigate neural mechanisms underlying the rapid composition of a novel behavior, I examined neural activity in hidden layers of the _Q_ networks of the deep RL agents trained in each subtask (Fig. 2a and Extended Data Fig. 3a). In Task 1, I observed one type of neuron displaying high activity in the middle of the arena corresponding to high _V_ Task1 (mean _Q_ Task1 over actions), and the other type of neuron characterized by conjunctive space (state) and direction (action) tuning of the agent, where neuron’s directional tuning corresponded to the distribution of _Q_ Task1 over actions in the state with high activity (Fig. 2b and Extended Data Fig. 3b). Intuitively, as the _Q_ Task1 function is determined for each binned state and action pair, distributions over actions were compared between the unit activity and _Q_ for the same states. Both classes of neurons were abundant (Extended Data Fig. 3c). In Task 2, a neuron was considered to be encoding the _Q_ Task2 function when its lick tuning (activity during licking versus no licking) and _Q_ Task2 ( _Q_ for licking versus no licking) were comodulated more than what would be expected by chance (Fig. 2b). Fractions of these _Q_ Subtask function-encoding neurons increased over learning in both subtasks (Task 1: _P_ < 0.001; Task 2: _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap; Fig. 2c). 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [521 x 408] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Task 1 Q Task1 Q Task2 d 2p-RAM Q Task1 Q Task2<br>State Task 1 Task 2<br>Q Task1<br>Action<br>Task 2 Object<br>State<br>Q Task2 Arena<br>Action<br>Low High Joystick Low High<br>b Agent e<br>State Action Q Task1 State Action Q Task1 Action Q Task2 Two-photon<br>0.89 0.97 0.1 M1<br>M2<br>S1<br>RSC<br>0.91 0.64 0.1<br>PPC<br>5 mm<br>90 Preferred<br>(normalized activity)Tuning 180 270 0 Low High direction 1 mm 500 µm<br>Mouse f Generalized linear model Pseudo-EV<br>State Action Q Task1 State Action Q Task1 Action Q Task2<br>0.88 0.20 0.1 Cell 1 0.53<br>Cell 2 0.52<br>0.75 0.68 0.1<br>Cell 3 0.46<br>Low High Actual Predicted 10 s<br>c Agent g Mouse Cortical distribution<br>Task 1 Task 2 Task 1 Task 2 Naive Expert<br>100 *** 100 *** 8 ** 30 *<br>Naive Expert<br>80 80 6<br>20<br>60 60<br>4<br>40 40<br>10<br>20 20 2<br>0 0 0 0<br>... ... ... Mean Mean<br>Lick Lick<br>None None<br>... ... ...<br>Cell 1 Cell 3 Cell 5<br>Tuning<br>Cell 2 Cell 4 Cell 6<br>(normalized activity)<br>None Lick None Lick<br>Cell 1 Cell 3 Cell 5<br>Tuning<br>Cell 2 Cell 4 Cell 6<br>(normalized activity)<br>None Lick None Lick<br>Task1<br>Q<br> cells (%)  cells (%)  cells (%)  cells (%)<br>Q Task1 Q Task2 Q Task1 QTask2 Q Task2<br>Naive Expert Naive Expert Naive Expert M1 M2 S1 RSC PPC Naive Expert M1 M2 S1 RSC PPC<br>**----- End of picture text -----**<br>


**Fig. 2 | Emergence of** _**Q**_ **Subtask function representation during learning. a** , Left, schematic of the ANNs in the deep RL agent. State and action scalar values are fed into the ANNs to output scalar values ( _Q_ Task1 and _Q_ Task2). Right, _Q_ Subtask functions derived by computing _Q_ in each state–action pair. The _Q_ Subtask functions were averaged across expert deep RL agents. The middle box in _Q_ Task1 and the top box in _Q_ Task2 indicate action-averaged _Q_ functions in state spaces. For visualization, the spatial activation map for each action (movement in eight directions, lick and none) was obtained by subtracting the action-averaged _Q_ function. The gray box denotes the reward zone. **b** , Space, direction and lick tuning of example neurons representing _Q_ functions of Tasks 1 and 2 in expert deep RL agents (top) or mice (bottom). ‘State’ and ‘Action’ denote maximum-normalized activity. The number for each _Q_ function describes the maximum _Q_ value across directions. Two classes of _Q_ Task1-representing neurons are displayed. **c** , Emergence of 

_Q_ Subtask function-encoding neurons during learning of Tasks 1 and 2 in deep RL agents (Task 1:[***] _P_ < 0.001; Task 2:[***] _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap, mean ± s.e.m.). **d** , Left, schematic of the imaging experiment in the subtasks. Right, same as **a** for expert mice. **e** , Left, imaged cortical regions (M1, M2, S1, RSC and PPC). Right, example of two-photon calcium imaging. The right image is the boxed region in the left image. **f** , GLM for example neurons. Pseudo-EV denotes pseudo-explained variance. **g** , Left, same as **c** for mice (Task 1:[**] _P_ = 0.004, _n_ = 6 and 7 mice for naive and expert, respectively; Task 2:[*] _P_ = 0.04, _n_ = 7 mice for naive and expert, one-tailed bootstrap, mean ± s.e.m.). Neurons were further categorized based on cortical regions (fraction ± s.d. over 1,000 samples with replacement). Right, relative cortical distribution of _Q_ Task1- and _Q_ Task2-representing neurons across learning. Circle size and transparency indicate the relative fractions of neurons in the five cortical regions across the two learning stages. 

To determine whether neural substrates of the _Q_ Subtask functions existed in the mouse brain, the activity of cortical excitatory neurons was imaged in transgenic mice (CaMKII-tTA × TRE-GCaMP6s) using a two-photon, random-access mesoscope (2p-RAM)[26] (Fig. 2d,e). Calcium imaging with 2p-RAM records activity from thousands of neurons across distant cortical regions with cellular resolution. The imaging window included five cortical regions: primary motor cortex (M1), secondary motor cortex (M2), primary somatosensory cortex (S1), retrosplenial cortex (RSC) and posterior parietal cortex (PPC). Generalized linear models (GLMs) were built for individual neurons to extract their encoding properties for each task variable 

and their space and direction tuning was obtained (Task 1: 12,232 and 15,324 neurons; Task 2: 3,619 and 2,563 neurons for naive and expert, respectively; Fig. 2f and Extended Data Fig. 4a–c). Tuning properties analogous to those observed in the ANN emerged, such that the fractions of neurons encoding respective _Q_ Subtask functions increased over learning with distinct functional parcellation across cortical areas (Task 1: _P_ = 0.004; _n_ = 6 and 7 mice for naive and expert, respectively; Task 2: _P_ = 0.04, _n_ = 7 mice for naive and expert, one-tailed bootstrap; Fig. 2b,g). The observed fraction of neurons encoding the _Q_ Task1 function at the expert stage (naive: 1.27%; expert: 5.11%) was above a chance level (naive: 0.60%; expert: 2.97%, _P_ < 0.001 for both naive and expert, 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

one-tailed permutation), computed by shuffling the indices of cells. Among neurons conjunctively tuned to space and direction, 29.2% of neurons were deemed to be representing the _Q_ Task1 function (M1: 22.7%; M2: 34.5%; S1: 23.9%; RSC: 43.0%; PPC: 32.0%). The observed increase in the fractions of neurons encoding _Q_ Task1 functions could not be explained by changes in the fractions of movement-related neurons (Extended Data Fig. 4d). Moreover, manipulation of the reward function confirmed that these neurons encoded the _Q_ Task1 function but not the object movement itself (Extended Data Fig. 5a–d). In Task 2, the observed fraction of neurons encoding the _Q_ Task2 function (naive: 11.8%; expert: 18.8%) was above a chance level (naive: 6.5%; expert: 9.2%, _P_ < 0.001 for both naive and expert, one-tailed permutation), computed by shuffling of lick events. Furthermore, the fractions of neurons encoding the lick onset and _Q_ Task2 function were not correlated with lick-event frequency (Extended Data Figs. 4e and 5e). At the expert stage, cortical distribution of _Q_ Subtask function-representing neurons for each subtask was distinct, where _Q_ Task1-encoding neurons were more enriched in the PPC whereas _Q_ Task2-encoding neurons were more abundant in M2 (Task 1 naive: M1 and M2: _P_ < 0.01; M1 and PPC: _P_ < 0.001; M2 and S1: _P_ < 0.001; M2 and PPC: _P_ < 0.01; S1 and RSC: _P_ < 0.01; S1 and PPC: _P_ < 0.001; RSC and PPC: _P_ < 0.001; Task 1 expert: M1 and M2: _P_ < 0.001; M1 and RSC: _P_ < 0.01; M1 and PPC: _P_ < 0.001; M2 and S1: _P_ < 0.05; S1 and PPC: _P_ < 0.001; Task 2 naive: M1 and M2: _P_ < 0.001; M1 and S1: _P_ < 0.001; M1 and RSC: _P_ < 0.001; M1 and PPC: _P_ < 0.01; M2 and S1: _P_ < 0.001; M2 and RSC: _P_ < 0.001; Task 2 expert: M1 and M2: _P_ < 0.001; M1 and S1: _P_ < 0.001; M1 and RSC: _P_ < 0.001; M1 and PPC: _P_ < 0.001; M2 and S1: _P_ < 0.001; M2 and RSC: _P_ < 0.001; M2 and PPC: _P_ < 0.001; S1 and PPC: _P_ < 0.001; RSC and PPC: _P_ < 0.001; all the other comparisons: _P_ > 0.05, two-tailed bootstrap with false discovery rate (FDR); Fig. 2g). These results are corroborated by our previous study demonstrating that the PPC is critical for the object manipulation task[22] , with others demonstrating the importance of anterior lateral motor cortex (a subregion of M2) for licking behavior[27] . Thus, the mouse cortex learned to represent the _Q_ Subtask functions in functionally segregated networks. 

## **Transfer of learned representations of** _**Q**_ **Subtask functions** 

In the deep RL agents, few-shot learning in the composite task was attained by constructing the _Q_ Composite function via averaging the two _Q_ Subtask functions (Fig. 3a). I examined the consequence of such an arithmetic operation on neural representations of the _Q_ function in the ANN of the deep RL agents at the early learning stage of the composite task (Supplementary Video 1). During training of the ANN, backpropagation of the error signal derived from the new _Q_ Composite function modulates neural activity across the whole network (Fig. 3a). Two predictions were made in the present study: first, as the action spaces in Task 1 (movement) and Task 2 (lick) were independent, averaging of _Q_ Task1( _s_ , _a_ ) and _Q_ Task2( _s_ , _a_ ) yields representations similar to those of individual _Q_ Subtask( _s_ , _a_ ), albeit the values are halved (Extended Data Fig. 6). The _Q_ functions related to the object movement and licking were referred to as _Q_ Move and _Q_ Lick, respectively, regardless of whether the task was a subtask or composite task, whereas _Q_ Subtask denoted the _Q_ function for the object movement in Task 1 or licking for Task 2. Second, as the state spaces were shared between Tasks 1 and 2 (position of the agent), state representations derived via averaging reveal a mixed _Q_ Subtask function (Extended Data Fig. 6). Overall, response profiles in individual neurons were more similar during the transition from the subtasks to the composite task than during learning of the individual subtasks (Extended Data Fig. 7a). Consistent with the first prediction, representations of the _Q_ Subtask functions were retained in the composite task (Fig. 3b). The importance of these representations was evident as ablation of _Q_ Subtask-encoding neurons in the ANN decelerated learning of the composite task in the deep RL agents (full ablation: _P_ < 0.001; 50% ablation: _P_ = 0.006, _n_ = 6 agents, one-tailed bootstrap with Bonferroni’s correction), whereas control ablation retained few-shot learning ( _P_ = 0.83 compared with no ablation, _n_ = 6 agents, one-tailed bootstrap, Fig. 3c). These results 

establish that representations of _Q_ Subtask functions in the ANN were reused in the composite task at the level of single neurons. 

I reasoned that, if the few-shot learning of the composite task in mice was mediated by a similar mechanism, representations in cortical neurons should resemble those detected in the deep RL agents. Indeed, tuning properties of single neurons remained comparable between the subtasks and composite task (3,364 and 4,873 neurons analyzed in the composite task for the early and late sessions, respectively; Fig. 3b and Extended Data Fig. 7b). The observed fraction of neurons encoding the _Q_ Task1 function at the early stage of the composite task (8.3%) was above a chance level (5.3%, _P_ < 0.001, one-tailed permutation). Among neurons conjunctively tuned to space and direction, 39.9% of neurons were deemed to represent the _Q_ Task1 function in the composite task (M1: 30.1%; M2: 46.5%; S1: 25.8%; RSC: 52.0%; PPC: 60.0%). Moreover, cortical distribution of the _Q_ Subtask-function representations was stable such that functionally specialized circuits persisted across the subtasks and composite task (Fig. 3d). 

Why was learning of the composite task more sample efficient in the deep RL agents and mice? It has been proposed that learning is constrained by the intrinsic covariance structure of neural population activity[28] : learning becomes harder when the covariance needs large restructuring. I hypothesized that the rapid acquisition of a new behavior was possible due to reuse of the preacquired patterns of population neural activity. Population activity can be described as a point in high-dimensional space where each axis corresponds to the activity of a single neuron. Comodulation of activity of a population of neurons comprises a low-dimensional subspace, known as the intrinsic manifold[28] . With Kullback-Leibler (KL) divergence estimation[29] , divergence of the intrinsic manifolds was measured between the expert stage of the subtasks and the early stage of the composite task. This analysis revealed that similar intrinsic manifolds were shared across tasks in both the deep RL agents and the mice (Fig. 3e and Extended Data Fig. 7c–e). By contrast, subtask learning in the deep RL agents considerably changed intrinsic manifolds, indicating that there was large reorganization of weights in the ANN (Extended Data Fig. 7c–e). This observation also provides a potential explanation of why learning of the subtasks was slow in mice (Fig. 1c). Together, these results demonstrate that the deep RL agents and mice transferred geometric representations of learned task variables to efficiently solve the novel task. In the case of the deep RL agents, as representation learning acts as a bottleneck[30] , reuse of learned representations of the _Q_ Subtask functions improves sample efficiency in the downstream task. 

## **Hierarchical composition of** _**Q**_ **Composite representations** 

It has been demonstrated so far that reuse/transfer of _Q_ Subtask representations in the deep RL agents facilitates composite task learning. In mice, similar _Q_ representations were observed between the subtasks and composite task. However, construction of the new _Q_ Composite function and its fine-tuning were critical because mere coexistence of independent _Q_ representations of the two subtasks was not sufficient to fully solve the composite task (first training epoch in ‘average’ on Fig. 1i). Existence of the individual _Q_ Subtask representations in mice supports, but does not prove, a new _Q_ Composite function being constructed through the averaging operation. To address this, I tested the second prediction that the state representation derived from averaging results in a mixture of _Q_ Subtask functions in single neurons (Extended Data Fig. 6). Based on Pearson’s correlation coefficients between the state representation of the _Q_ Composite function and space tuning of individual units, I confirmed the second prediction to be true even at the early stage of learning in the composite task; spatial activation of neurons was confined to two locations corresponding to the states with high expected values of the _Q_ in the two subtasks (Fig. 4a and Extended Data Fig. 8a). The resulting neural representations were due to moment-by-moment activation of each neuron at the corresponding states (Extended Data Fig. 8b). The observed fraction (22.2%) was higher than what would be expected by 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [521 x 284] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Space: Action State Composite task Space: Action State<br>ActionState Q Task1 Q Comp.: Q Move Q Lick Q Comp. 2p-RAM Q Comp.: Q Move Q Lick Q Comp.<br>Q Comp.<br>Lick Lick<br>State Object<br>Action Q Task2<br>No lick Arena No lick<br>Backpropagation Joystick<br>b Agent composite task early c Agent d Mouse<br>State Action Q Move State Action Q Lick Ablation of  Q Subtask cells Q Task1 Q Move Q Task2 Q Lick<br>0.48 0.1 1.0 ***** 20 *** 8 *** M1<br>NS 16 M2<br>0.55 0.1 0.5 FullHalf 12 4 S1RSC<br>Control 8 PPC<br>90 0 100 200 4 4 6 8 0 0 10 20 30<br>(normalized activity)Tuning 180 270 0 Low High Epoch Q Task1 cells (%) Q Task2 cells (%)<br>Mouse composite task early e Subtask expert<br>State Action Q Move State Action Q Lick Q manifold Comp. task early Agent Mouse<br>0.51 0.1 Within 40 20 Data<br>Outside Shuffle<br>20 10 Task 1<br>0.53 0.1 Task 2<br>0 0<br>Preferred 1 10 1 10<br>direction Low High Dimension Dimension<br>Cell 2 Cell 3<br>... ... ...<br>... ... ...<br>Cell 1 Cell 3  cells in  cells in<br>Tuning Return<br>Cell 2 Cell 4 Q Subtaskcomp. task (%) Q Subtaskcomp. task (%)<br>(normalized activity)<br>None Lick None Lick<br>Cell 1 Cell 3<br>Tuning Cell 1<br>Cell 2 Cell 4 KL divergence KL divergence<br>(normalized activity)<br>None Lick None Lick<br>**----- End of picture text -----**<br>


**Fig. 3 | Transfer of** _**Q**_ **Subtask representation to the composite task. a** , Left, schematic of the composite ANN architecture and the _Q_ Composite function in action and state spaces in deep RL agents in the early learning phase of the composite task. Output scalar values ( _Q_ Task1 and _Q_ Task2) are averaged to derive a scalar value ( _Q_ Composite ( _Q_ Comp.)). Right, same as left for mice with schematic of the imaging experiment. It is the same visualization as Fig. 2a,d. **b** , _Q_ Subtask representations in the early phase of the composite task in deep RL agents (top) and mice (bottom). It is the same visualization as Fig. 2b. **c** , Learning curve in the composite task with ablation of _Q_ Task1- and _Q_ Task2-representing neurons in deep RL agents. Full ablation: 11.3 ± 0.3% (mean ± s.e.m.) for movement and 14.0 ± 0.3% for lick of all neurons ablated,[***] _P_ < 0.001 compared with control ablation; 50% ablation: 5.8 ± 0.1% for movement and 7.1 ± 0.2% for lick of all neurons ablated, ** _P_ = 0.006 compared with control ablation; control ablation: same number as the full ablation ablated, _P_ = 0.83 compared with no ablation, _n_ = 6 agents, one-tailed bootstrap with 

Bonferroni’s correction (mean ± s.e.m.). **d** , Persistent cortical distribution of _Q_ Subtask-related movement (left) and lick (right) representations across the subtasks and composite (comp.) task in mice (Task 1: _R_[2] = 0.98,[***] _P_ < 0.001; Task 2: _R_[2] = 0.76,[***] _P_ < 0.001, one-tailed bootstrap for positive correlations, fraction ± s.d. >1,000 samples with replacement). Direct comparisons in the absolute fractions of _Q_ Subtask-related neurons across tasks are complicated due to different task predictors used in GLMs. **e** , Left, schematic of the _Q_ manifold of population neural activity representing a _Q_ function. Middle, _Q_ manifold in an example of a deep RL agent embedded in the same principal component space. The dots correspond to activity at randomly sampled timepoints. Right, manifold overlaps. The dots indicate the mean KL divergence. The edges of the whiskers are maximum and minimum and the edges of the boxes are 75% and 25% of 1,000 shuffled mean KL divergence ( _P_ < 0.001 for all comparisons, _n_ = 7 mice and _n_ = 6 agents, one-tailed permutation). 

chance assuming that space tuning was uniformly distributed (11.1%, _P_ < 0.001, one-tailed bootstrap). These activation patterns were rarely observed in the subtasks (Fig. 2b and Extended Data Fig. 8c). In addition, when the _Q_ Composite function was derived from computing the maximum of the two _Q_ Subtask functions, differences in representations from the averaging operation were subtle, except that these mixed _Q_ Subtask representations were absent (Extended Data Fig. 8d). As such a small difference led to distinct learning efficiency in the composite task (Fig. 1i), the mixed representations were likely to be critical in the deep RL agents. 

In mice, more direct evidence for the additive _Q_ Composite construction is, therefore, to reveal similar multiplexed representations of _Q_ Task1 and _Q_ Task2 in single cortical neurons. Neurons in the mouse cortex were indeed spatially tuned to the two high value states derived from the two subtasks (Fig. 4a and Extended Data Figs. 6 and 8a). The observed fraction (20.7%) was higher than what would be expected by chance assuming that space tuning was uniformly distributed (16.1%, _P_ = 0.006, one-tailed bootstrap). As in the case of the ANN, the mixed representations were due to moment-by-moment activation of each neuron, do not reflect co-occurrence of the object movement and licking actions, and were not observed in the subtasks (Extended Data 

Fig. 8b,c). Importantly, these tuning properties did not reflect a reward as such because there was no reward associated with the center of the arena in the composite task. Furthermore, the observed representations suggest that the brain’s efficient learning in the composite task was not simply attained by construction of dynamic models (Extended Data Fig. 2c), but the combination of prelearned _Q_ functions is important to derive a new policy. 

The rapid learning in the composite task in the deep RL agents and mice was followed by gradual refinement of the policy during the fine-tuning phase (Fig. 1e,j). To seek additional evidence for the composition of the new _Q_ Composite function in mice, I next studied how neural representations were shaped during this phase of learning. As the deep RL agents learned the composite task (Supplementary Video 2), there was a transition in ANN activity from dedicated to distributed representations: neural representations of _Q_ for movement and lick in the two subnetworks, which were computed in the same manner as _Q_ Subtask representations, were initially segregated but gradually became mixed on training (Fig. 4b and Extended Data Fig. 9a–c). I reasoned that if the mouse cortex computed the _Q_ Composite function by averaging the two _Q_ Subtask functions, there should be similar redistribution of neural representations of the _Q_ function across the cortical regions. In support 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [471 x 468] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Space tuning in composite task early b Composite task early Composite task late<br>Agent Dedicated Distributed<br>Q Comp.<br>0.6<br>Task 1 Q Task1 Q Task1<br>0.2 Q Comp.<br>Task 2 Q Task2 Q Task2<br>40 * **<br>Backpropagation<br>Agent<br>20<br>Q Move Q Lick Q Move Q Lick<br>80 *** *** 30 100 NS NS 80<br>0<br>60 60<br>20<br>–0.9 0.9<br>40 50 40<br>Correlation 10<br>20 20<br>Mouse 0 0 0 0<br>Q Comp.<br>0.6 Network: Network:<br>0.2<br>c Mouse Distribution of Q-function<br>Composite task representation<br>Early Late<br>40 ** *** Comp. early<br>Comp. early<br>Comp. late<br>20<br>Q Task1:Move Q Comp:Move<br>Move<br>0 Lick<br>–0.6 0.6 Task 1-like<br>Correlation Q Task2:Lick Q Comp:Lick Agent Task 2-like<br>Q Subtask representation in the composite task. representation in the composite task. for the object movement and licking, respectively, derived from the subtask or<br>, Space tuning of 300 randomly selected neurons in the tSNE coordinate for  the composite task.  c , Left, cortical distribution of movement- and lick-related<br>deep RL agents and mice. The color indicates Pearson’s correlation coefficient  Q Subtask- and  Q Composite-representing neurons. The circle size and transparency<br>Q Composite function. Note the  function. Note the  indicate the relative fractions of neurons in the five cortical regions across<br>the two learning stages. Right, distribution of  Q  representations in deep RL<br>[[***]] P  < 0.001,  n  = 6 agents, mouse:  agents constructed by arithmetic operation of the  Q Subtask functions predicts<br> = 7 mice, one-tailed bootstrap compared with a chance level,  the cortical distribution of  Q  representations in mice ( R [2]  = 1.0,  [***] P  < 0.001,<br>b , Top, schematic of the composite ANN architecture of the deep  one-tailed bootstrap for positive correlations, error bars: s.d. of 1,000 samples<br>with replacement). The two axes denote how dedicated  Q  representations are in<br>Q  in both subnetworks  each subnetwork for deep RL agents and in cortical distributions for mice. For<br>become more distributed due to backpropagation of the common error signal.  example, the green open circle indicates dedicated QMove representations at the<br>Q Subtask- and - and  Q Composite-- early phase of the composite task in the Task 1 subnetwork for deep RL agents,<br>whereas cortical distributions of  Q Move representations were similar between the<br>P  = 0.66 and 0.40 from the left to right,  n  = 6  early phase of the composite task and the expert stage of Task 1 for mice.<br>Cells (%)<br> cells  cells<br>Subtask Comp.<br>Q Q<br>in comp. task (%) in comp. task (%)<br>Task 1 Task 2 Task 1 Task 2 Task 1 Task 2 Task 1 Task 2<br>Cells (%) Mouse<br>**----- End of picture text -----**<br>


**Fig. 4 | Arithmetic operation on** _**Q**_ **Subtask representation in the composite task. representation in the composite task. a** , Space tuning of 300 randomly selected neurons in the tSNE coordinate for deep RL agents and mice. The color indicates Pearson’s correlation coefficient between space tuning and the spatial map of the _Q_ Composite function. Note the  function. Note the two locations (center and bottom middle) corresponding to the high value states derived from the two subtasks (agent:[[***]] _P_ < 0.001, _n_ = 6 agents, mouse: ** _P_ = 0.006, _n_ = 7 mice, one-tailed bootstrap compared with a chance level, mean ± s.e.m.). **b** , Top, schematic of the composite ANN architecture of the deep RL agent and changes in representation during the composite task learning. Representations of movement-related and lick-related _Q_ in both subnetworks become more distributed due to backpropagation of the common error signal. Bottom, distribution of movement- and lick-related _Q_ Subtask- and - and _Q_ Composite-representing neurons in each subnetwork in deep RL agents across learning ([***] _P_ < 0.001, nonsignificant (NS): _P_ = 0.66 and 0.40 from the left to right, _n_ = 6 agents, one-tailed bootstrap, mean ± s.e.m.). _QM_ ove and _Q_ Lick are action values 

of this, although _Q_ Subtask representations were initially segregated in dedicated circuits, _Q_ Composite representations became widely distributed across different cortical regions after the composite task learning (Figs. 2g and 4c and Extended Data Fig. 9d–g). Remarkably, redistribution of the agent’s _Q_ representations in the subnetworks predicted that observed in the mouse cortex ( _R_[2] = 1.0, _P_ < 0.001, one-tailed bootstrap for positive correlations; Fig. 4c). These similarities lend further support to the notion that mice used a simple arithmetic operation to derive a new _Q_ Composite function to solve the composite task. 

## **Maximum entropy policy for efficient behavior composition** 

Finally, I examined whether a stochastic policy was critical for the rapid composition of the new behavior, a question related to the second term of the objective in the SAC algorithm. In the deep RL agents, behavior performance in the composite task depended on the policy entropy, such that learning was accelerated when the agent’s policy in Task 1 became stochastic: when the entropy maximization term was 

removed from the RL objective of the SAC algorithm ( _α_ = 0 in equation (4)), pretraining with the subtasks failed to improve learning ( _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap; Fig. 5a). Additional analysis demonstrated that, even though there was a conflict in the optimal policies between Task 1 and the composite task, entropy in subpolicies promoted exploration such that it enhanced the probability of visiting the reward zone in the composite task; the visitation of the reward zone predicted whether the agents were successful in solving the composite task (Extended Data Fig. 10a–c). Notably, the maximum entropy policy can be detrimental under the condition that the reward zone between Task 1 and the composite task was identical ( _P_ = 0.01, _n_ = 6 agents, one-tailed bootstrap; Extended Data Fig. 10d). Furthermore, successful composition of a new policy entailed a substantial overlap in high _Q_ states between the subtasks and composite task (Extended Data Fig. 2b). 

I hypothesized that the deep RL agents’ few-shot learning of the composite task was due to representations of broadly distributed _Q_ 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [440 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>Agent Direction tuning<br>Agent trajectory in Task 1 Composite task Task 1 Comp. task in Task 1<br>1.0 *** 100 ***<br>Trial Offset Cell 1 6080<br>10 0.5 + Entropy Cell 2 40 + Entropy<br>1 0 – Entropy Broad = Fast 200 – Entropy<br>+ Entropy – Entropy 100 200 Cell 3 0 0.5 1.0<br>maximization maximization Epoch Narrow = Slow Broad SI Narrow<br>d Mouse e Direction tuning<br>Object trajectory in Task 1 Composite task in Task 1<br>100 *** 100 *** 100 ***<br>80 80 Cell 1 80<br>Trial 60 60 60<br>10 40 40 Stochastic Cell 2 40 Stochastic<br>1 200 200 Deterministic 200 Deterministic<br>Stochastic Deterministic 1 2 3 4 5 0.4 0.8 Cell 3 0 0.1 0.2<br>Initial state Session Task 1 policy entropy Broad SI Narrow<br>Return<br>Cumulative (%)<br>Correct (%) Correct (%)<br>Cumulative (%)<br>**----- End of picture text -----**<br>


**Fig. 5 | Maximum entropy policies improve learning of the composite task. a** , Left, example trajectories of deep RL agents in Task 1 with and without policy entropy maximization. Note that the trajectories overlap in the right panel. Right, learning curve in the composite task with and without policy entropy maximization ([***] _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap at the early stage, mean ± s.e.m.). **b** , Schematic showing that broader direction tuning confers rapid learning in the composite task because minimal fine-tuning is required. **c** , Example direction tuning of the same neurons in deep RL agents in Task 1 with and without policy entropy maximization, measured by the SI defined as 1 − Circular variance ([***] _P_ < 0.001, _n_ = 2,340 and 2,313 cells with and without policy entropy maximization, respectively, one-tailed KS test). **d** , Left, 

example trajectories of the object moved by mice in Task 1 with stochastic and deterministic policies. Middle, learning curve in the composite task with stochastic and deterministic policies ([***] _P_ < 0.001 compared with the first session, _n_ = 7 and 8 mice for stochastic and deterministic policy, respectively, one-tailed bootstrap, mean ± s.e.m.). Right, correlation between Task 1 policy entropy and the session-averaged correct rate in the composite task ( _R_[2] = 0.57,[***] _P_ < 0.001 computed with Student’s _t_ cumulative distribution function, one tailed, _n_ = 15 mice). **e** , Example of direction tuning of neurons in the mouse cortex in Task 1 with stochastic and deterministic policies ([***] _P_ < 0.001, _n_ = 3,251 and 2,972 cells for stochastic and deterministic policy, respectively, one-tailed KS test). 

functions over different actions, which enable multimodal solutions[12] . Depending on the state, the optimal action of the agent could be slightly different between Task 1 and the composite task, and the agents were required to fine-tune their policy accordingly. Broad representations of _Q_ functions can flexibly adapt to such a slight offset in the optimal policy (Fig. 5b). However, if representations of _Q_ are specific to certain directions, the agents need to unlearn old _Q_ functions and relearn new ones. When the agents were trained with the entropy maximization term, the direction tuning of individual neurons was broader ( _P_ < 0.001, _n_ = 2,340 and 2,313 cells with and without entropy maximization, respectively, one-tailed Kolmogorov–Smirnov (KS) test, Fig. 5c). 

I next tested whether policy stochasticity was similarly important in mice by modifying Task 1 to encourage mice to employ a more deterministic policy (Fig. 5d). As observed in the deep RL agents, learning in the composite task was slower when the trajectories in Task 1 were not highly variable ( _P_ < 0.001, _n_ = 7 and 8 mice for stochastic and deterministic policy, respectively, one-tailed bootstrap; Fig. 5d). Individually, the variability in the Task 1 policy entropy predicted the variability of task performance in the composite task ( _R_[2] = 0.57, _P_ < 0.001, _n_ = 15 mice, one-tailed for correlation; Fig. 5d). Neural representations of the object movement direction were broader when the policy was more stochastic ( _P_ < 0.001, _n_ = 3,251 and 2,972 cells for stochastic and deterministic policy, respectively, one-tailed KS test; Fig. 5e). Thus, policy entropy conferred flexible composition of a new behavior policy by broadly representing _Q_ functions over different actions. 

## **Discussion** 

Although research in AI aims to express unique properties of biological intelligence in machines[3] , various algorithms have been developed to provide explanatory views of their biologically plausible mechanisms. This has, in turn, created new opportunities for neuroscience to empirically validate theoretical models of how biological intelligence is implemented[31][–][33] . It has been postulated that new ideas and behavior skills are rapidly developed through a combination of their primitives, the notion related to compositionality[9][,][34] . Such properties, however, 

have rarely been scrutinized in rodent system neuroscience, in which - recordings of single neurons across multiple brain areas are common place. Deep RL, on the other hand, reveals neural representations of RL variables in single neurons in the ANN. Exploiting advantages of both systems, I generated deep RL-derived models on how concerted actions of individual neurons in the brain lead to new policy composition. A simple linear operation of averaging, but not computing the maximum of, the _Q_ Subtask functions in the deep RL agents was critical to increase sample efficiency in the composite task. A striking resemblance between the deep RL agents and mice in their behavior and _Q_ representations implies that animals employ a similar arithmetic code to expand their behavior repertoire. 

Brain regions such as the basal ganglia, in particular dorsal and ventral subdivisions of the striatum, are often associated with the actor-critic model[35][,][36] . The present results indicate additional involvement of cortical neurons in representing values of relevant actions according to the functional parcellation, which is consistent with the proposed role of corticostriatal pathways[35][,][37] . This view is corroborated by a recent human study demonstrating that activity in the PPC resembles activation patterns in the deep _Q_ network[38] . The current finding, however, does not exclude the possibility that other forms - of learning not involving a reward, or other brain regions not exam ined in the present study, contribute to the composition of a novel behavior. For instance, the brain may construct predictive models of the environment to further improve learning via simulations. In the present study, I demonstrate that construction of dynamic models and model-free policy optimization together augments sample efficiency in the deep RL agents (Extended Data Fig. 2c). Whether the brain constructs dynamic models, in addition to the transfer of the combined _Q_ function described in the present study, warrants further investigation. 

Variability in the sensorimotor system can be harnessed to augment learning in humans and other animals[14][,][15] . In deep RL, the SAC algorithm maximizes the policy entropy to attain multiple solutions to the same problem, which has been theoretically shown to improve composability of a new policy: stochastic and deterministic subpolicies 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

are associated with high and low composability, respectively[10] . In the context of the present study, deterministic policies in the subtasks during pretraining lead to loss of exploration when they are transferred to the composite task, leading to very slow adaptation of the agents. Such a common mechanism between the biological and artificial systems uncovers an essential role of variability in behavior composition. In particular, the comparative analysis provides a formal account of why variability facilitates learning in the biological system. High variability in a policy allows exploration of relevant _Q_ spaces, which was evident in broadly tuned, action-related neural activity in both systems. I acknowledge that the manipulation to encourage mice to employ a deterministic policy might have deprived them of additional statistical features of the environment critical for the behavior composition. None the less, the current results support the hypothesis that policy stochasticity facilitates hierarchical composition of a new behavior in both the brain and the machine. 

The present study naturally translates into several important questions: how does the brain know which policies to combine under different contexts? Does the brain build dynamic models to further improve learning[25][,][39][,][40] ? The selection of appropriate policies among many may require cognitive control by the prefrontal cortex, the function of which has been implicated in metalearning[20] . Model construction in deep RL provides theoretical predictions for neural representations in the brain. The comparative analysis between the two intelligent systems is imperative to explore such interesting subjects. 

## **Online content** 

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41593-022-01211-5. 

## **References** 

1. Epstein, R., Kirshnit, C. E., Lanza, R. P. & Rubin, L. C. ‘Insight’ in the pigeon: antecedents and determinants of an intelligent performance. _Nature_ **308** , 61–62 (1984). 

2. Saxe, A. M., Earle, A. C. & Rosman, B. Hierarchy through composition with multitask LMDPs. _Proceedings of Machine Learning Research_ **70** , 3017–3026 (2017). 

3. Lake, B. M., Ullman, T. D., Tenenbaum, J. B. & Gershman, S. J. Building machines that learn and think like people. _Behav. Brain Sci._ **40** , e253 (2017). 

4. Geddes, C. E., Li, H. & Jin, X. Optogenetic editing reveals the hierarchical organization of learned action sequences. _Cell_ **174** , 32–43.e15 (2018). 

5. Parr, R. & Russell, S. in _Advances in Neural Information Processing Systems 10: Proceedings of the 1997 Conference_ (eds Jordan, M. I., Kearns, M. J. & Solla, S. A.) 1043–1049 (1998). 

6. Dietterich, T. G. Hierarchical reinforcement learning with the MAXQ value function decomposition. cs/9905014 (1999). https://ui.adsabs.harvard.edu/abs/1999cs……..5014D 

7. Sutton, R. S., Precup, D. & Singh, S. Between MDPs and semi-MDPs: a framework for temporal abstraction in reinforcement learning. _Artif. Intell._ **112** , 181–211 (1999). 

8. Barto, A. G. & Mahadevan, S. Recent advances in hierarchical reinforcement learning. _Discret. Event Dyn. Syst._ **13** , 341–379 (2003). 

9. Botvinick, M. M., Niv, Y. & Barto, A. G. Hierarchically organized behavior and its neural foundations: a reinforcement learning perspective. _Cognition_ **113** , 262–280 (2009). 

10. Haarnoja, T. et al. Composable deep reinforcement learning for robotic manipulation. Preprint at _arXiv_ https://ui.adsabs.harvard. edu/abs/2018arXiv180306773H (2018). 

11. Niekerk, B. V., James, S., Earle, A. & Rosman, B. in _Proceedings of the 36th International Conference on Machine Learning_ Vol. 97 (eds C. Kamalika & S. Ruslan) 6401–6409 (Proceedings of Machine Learning Research, 2019). 

12. Ziebart, B. D., Maas, A., Bagnell, J. A. & Dey, A. K. in _Proceedings of the 23rd National Conference on Artificial Intelligence,_ Vol. 3 1433–1438 (AAAI Press, 2008). 

13. Haarnoja, T., Tang, H., Abbeel, P. & Levine, S. Reinforcement learning with deep energy-based policies. Preprint at _arXiv_ https://ui.adsabs.harvard.edu/abs/2017arXiv170208165H (2017). 

14. Wu, H. G., Miyamoto, Y. R., Gonzalez Castro, L. N., Olveczky, B. P. & Smith, M. A. Temporal structure of motor variability is dynamically regulated and predicts motor learning ability. _Nat. Neurosci._ **17** , 312–321 (2014). 

15. Dhawale, A. K., Smith, M. A. & Olveczky, B. P. The role of variability in motor learning. _Annu. Rev. Neurosci._ **40** , 479–498 (2017). 

16. Yamins, D. L. et al. Performance-optimized hierarchical models predict neural responses in higher visual cortex. _Proc. Natl Acad. Sci. USA_ **111** , 8619–8624 (2014). 

17. Zhuang, C. et al. Unsupervised neural network models of the ventral visual stream. _Proc. Natl Acad. Sci. USA_ https://doi.org/ 10.1073/pnas.2014196118 (2021). 

18. Cadieu, C. F. et al. Deep neural networks rival the representation of primate IT cortex for core visual object recognition. _PLoS Comput. Biol._ **10** , e1003963 (2014). 

19. Khaligh-Razavi, S. M. & Kriegeskorte, N. Deep supervised, but not unsupervised, models may explain IT cortical representation. _PLoS Comput. Biol._ **10** , e1003915 (2014). 

20. Wang, J. X. et al. Prefrontal cortex as a meta-reinforcement learning system. _Nat. Neurosci._ **21** , 860–868 (2018). 

21. Song, H. F., Yang, G. R. & Wang, X. J. Reward-based training of recurrent neural networks for cognitive and value-based tasks. _eLife_ https://doi.org/10.7554/eLife.21492 (2017). 

22. Suhaimi, A., Lim, A. W. H., Chia, X. W., Li, C. & Makino, H. Representation learning in the artificial and biological neural networks underlying sensorimotor integration. _Sci. Adv._ **8** , eabn0984 (2022). 

23. Haarnoja, T., Zhou, A., Abbeel, P. & Levine, S. Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor. Preprint at _arXiv_ https://ui.adsabs.harvard.edu/ abs/2018arXiv180101290H (2018). 

24. Haarnoja, T. et al. Soft actor-critic algorithms and applica tions. Preprint at _arXiv_ https://ui.adsabs.harvard.edu/abs/ 2018arXiv181205905H (2018). 

25. Janner, M., Fu, J., Zhang, M. & Levine, S. in _Proceedings of the 33rd International Conference on Neural Information Processing Systems_ Article 1122 (Curran Associates Inc., 2019). 

26. Sofroniew, N. J., Flickinger, D., King, J. & Svoboda, K. A large field of view two-photon mesoscope with subcellular resolution for in vivo imaging. _eLife_ https://doi.org/10.7554/eLife.14472 (2016) 

27. Komiyama, T. et al. Learning-related fine-scale specificity imaged in motor cortex circuits of behaving mice. _Nature_ **464** , 1182–1186 (2010). 

28. Sadtler, P. T. et al. Neural constraints on learning. _Nature_ **512** , 423–426 (2014). 

29. Perez-Cruz, F. in _2008 IEEE International Symposium on Information Theory_ 1666–1670 (2008). 

30. Shelhamer, E., Mahmoudieh, P., Argus, M. & Darrell, T. Loss is its own reward: self-supervision for reinforcement learning. Preprint at _arXiv_ https://ui.adsabs.harvard.edu/abs/2016arXiv161207307S (2016). 

31. Hassabis, D., Kumaran, D., Summerfield, C. & Botvinick, M. Neuroscience-inspired artificial intelligence. _Neuron_ **95** , 245–258 (2017). 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

32. Kriegeskorte, N. & Douglas, P. K. Cognitive computational neuroscience. _Nat. Neurosci._ **21** , 1148–1160 (2018). 

33. Macpherson, T. et al. Natural and artificial intelligence: a brief introduction to the interplay between AI and neuroscience research. _Neural Netw._ **144** , 603–613 (2021). 

34. Ribas-Fernandes, J. J. et al. A neural signature of hierarchical reinforcement learning. _Neuron_ **71** , 370–379 (2011). 

35. O’Doherty, J. et al. Dissociable roles of ventral and dorsal striatum in instrumental conditioning. _Science_ **304** , 452–454 (2004). 

36. Takahashi, Y., Schoenbaum, G. & Niv, Y. Silencing the critics: understanding the effects of cocaine sensitization on dorsolateral and ventral striatum in the context of an actor/critic model. _Front. Neurosci._ **2** , 86–99 (2008). 

37. Lau, B. & Glimcher, P. W. Value representations in the primate striatum during matching behavior. _Neuron_ **58** , 451–463 (2008). 

38. Cross, L., Cockburn, J., Yue, Y. & O’Doherty, J. P. Using deep reinforcement learning to reveal how the brain encodes abstract state-space representations in high-dimensional environments. _Neuron_ **109** , 724–738 e727 (2021). 

39. Miller, K. J., Botvinick, M. M. & Brody, C. D. Dorsal hippocampus contributes to model-based planning. _Nat. Neurosci._ **20** , 1269–1276 (2017). 

40. Sutton, R. S. & Barto, A. G. _Reinforcement Learning: An introduction_ , 2nd edn (The MIT Press, 2018). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons. org/licenses/by/4.0/. 

- © The Author(s) 2022 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

## **Methods Animals** 

All procedures were in accordance with the Institutional Animal Care and Use Committee at Nanyang Technological University. Transgenic mice were acquired from the Jackson Laboratory (CaMKII-tTA: catalog no. 007004; TRE-GCaMP6s: catalog no. 024742). Mice were housed in a reversed light cycle (12 h:12 h) in standard cages and experiments were performed typically during the dark period. Male and female hemizygous mice were used. 

## **Surgery** 

The surgical procedure has been described previously[22] . Briefly, adult mice (aged between 7 weeks and 4 months) were anesthetized with 1–2% isoflurane and a craniotomy (~7 mm in diameter) was carried out around the bregma with a dental drill. An imaging window, constructed from a small (~6 mm in diameter) glass plug (no. 2 thickness, Thermo Fisher Scientific, catalog no. 12-540-B) attached to a larger (~8 mm in diameter) glass base (no. 1 thickness, Thermo Fisher Scientific, catalog no. 12-545-D), was placed in the craniotomy. A custom-built titanium head-plate was implanted on the window with cyanoacrylate glue and black dental acrylic (Lang Dental, catalog no. 1520BLK or 1530BLK). Buprenorphine (0.05-0.1 mg per kg of body weight), Baytril (10 mg per kg of body weight) and dexamethasone (2 mg per kg of body weight) were subcutaneously injected. 

## **Behavior** 

Mice were water restricted for ~2 weeks starting at least 3 d after the surgery. After a few days of habituation to the task apparatus, they were trained to perform two subtasks—the object manipulation task (‘Task 1’) and the licking task (‘Task 2’)—followed by the composite task. The trial structure in each task was controlled by Bpod (Sanworks) using customized codes written in MATLAB and task variables were measured by Wavesurfer (Janelia Research Campus) at the sampling rate of 2,000 Hz. 

**Task 1.** Task 1 has been described previously[22] . Briefly, mice manipulated, with their right forepaws, a joystick to remotely move an object to a reward zone (4 × 4 cm[2] ) located in the center of the arena (10 × 10 cm[2] ). The object in the arena was a three-dimensional-printed cube attached to a 525-nm LED (Thorlabs, catalog no. LED525E) and the reward zone was indicated by another 525-nm LED. The object was moved by the joystick controlled with Arduino Leonardo (Arduino) and a motor shield (Adafruit, catalog no. 1438). 

In each trial, the LEDs on the object and target were turned on. When the object reached the reward zone, it became stationary, a water (8 μl) reward was provided and the LEDs were turned off. This was followed by 4 s of a reward consumption period and 2 s of an intertrial interval. The object was reinitialized to a random position outside the reward zone after each successful trial. Each trial lasted up to 5 min and in each session mice performed up to 60 trials over ~1 h. Naive sessions were the first few sessions when another group of mice was directly introduced to the environment with the reward zone of 4 × 4 cm[2] . Expert sessions were those following completion of 60 trials for at least 2 consecutive sessions within 30 min. 

In the experiment with the altered-reward function (two rewards), the reward size was changed on the left (or top) and right (or bottom) side of the reward zone (10 μl and 1 μl of water for the high- and low-reward side, respectively), but otherwise followed the same task structure as Task 1, as described previously[22] . An independent group of four and two mice was used in the environment where the reward was high on the right and bottom side of the reward zone, respectively. 

To force mice to employ a more deterministic policy, a separate set of mice was trained in a modified version of the task, where the initial position was fixed (7 cm from the bottom of the arena on the left edge) in every trial. 

**Task 2.** Once mice became expert at Task 1, Tasks 1 and 2 were interleaved for two sessions each to ensure that mice were able to switch between these subtasks. This was then followed by three consecutive sessions of Task 2. In Task 2, mice were trained to lick a water spout on the LED-attached, nonmovable object located in front of them. The trial started with onset of the LED, whereas the target LED used in Task 1 remained off throughout the session. Mice received a water (8 μl) reward when they successfully licked the water spout during the response period, which started 2 s after the trial onset. The trial structure was otherwise the same as Task 1. Lick events were detected with a customized touch sensor. Naive and expert sessions were defined as the first and fifth sessions, respectively. 

**Composite task.** Once mice became expert at Tasks 1 and 2, they were introduced to the composite task, in which they had to combine knowledge acquired from the subtasks. In the composite task, the water spout was attached to the object that could be moved with the joystick. The trial started with onset of the object LED and the other LED used in Task 1 remained off. When the object reached the target region (5 × 0.16 mm[2] in _x_ and _y_ at the bottom middle region of the arena), it became stationary and mice had to lick the water spout to trigger water dispensation (8 μl). As in the case of Task 1, after each trial the object was reinitialized to a random position outside the target region. The trial structure was the same as Task 1 and mice were trained over a total of five sessions. As a control, mice without any prior experience in Tasks 1 and 2 were trained in the composite task over the same number of sessions. In the composite task, the first session that contained more than 20 correct trials out of 60 total trials was considered as the early session for each mouse (first session for 4 mice and second session for 3 mice), whereas the fifth session was considered as the late session. 

## **Two-photon calcium imaging** 

Images were acquired using a 2p-RAM (Thorlabs) controlled with ScanImage (Vidrio Technologies) and a laser (InSight X3, Spectra-Physics), as described previously[22] . The excitation wavelength of the laser was tuned to 940 nm with a power of ~40 mW at the objective lens. The frame rate was ~5.67 Hz and the imaging resolution was 1 × 0.4 pixel per μm with 2 fields of view of 0.5 × 5 mm[2] at the depth of ~200–300 μm (layer 2/3). 

## **Behavior analysis of mice** 

**State-value function.** As described previously[22] , the state-value function _V_ ( _s_ ) was defined as the value of each state _s_ , which corresponded to the mean discounted time steps for each spatial bin and calculated according to equation (3). Mice received a reward of 1 in successful trials. The state value of the reward zone was set to be 1. 

**Action-value function.** The action-value function _Q_ ( _s_ , _a_ ) was defined as the value of each action _a_ in a given state _s_ , and described according to equation (1). _a_ corresponded to one of eight discretized directions (0°, 45°, 90°, 135°, 180°, 225°, 270° and 315°) or no movement in Task 1, and lick or no lick action in Task 2. In the composite task, both types of action were considered. _V_ ( _st_ +1) was the value of a neighboring state in the 10 × 10 binned arena in the case of eight direction movements or the value of the same state if the movement hit the edges of the arena or in the case of no movement. 

**Policy.** In Task 1 and the composite task, policy _π_ was considered as a probability distribution of the object movement direction. For simplicity, _π_ was displayed as a vector field with unit vectors showing the preferred action in each state and calculated by the vectorial sum of all velocity vectors in each spatial bin, obtained based on the angle and speed of the object movement over 100 ms. 

Policies across the tasks and learning stages were compared with cosine similarity, where, in each spatial bin, two vectors obtained 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

from the vectorial sum of all velocity vectors in two given conditions were multiplied and normalized by the product of their lengths. The resulting vectors were averaged across spatial bins and across sessions per animal. 

**Policy entropy.** Policy entropy was computed in Task 1 in each spatial bin ( _i,j_ ) of the 10 × 10 arena as: 

**==> picture [194 x 22] intentionally omitted <==**

where _π_ is the action probability distribution computed as the normalized sum of speed of individual object movements in each direction so that the values across directions summed to 1. The mean of the policy entropy across spatial bins was then computed to determine a total policy entropy in each session. 

**State occupancy.** State occupancy was determined in each session as the probability of the object residing in each of the 10 × 10 spatial bins. In the altered-reward function (two-reward) experiment, ratios of state occupancy between a high-reward side and a low-reward side were computed and averaged across sessions and across mice. The value was then compared with ratios of state occupancy obtained by randomly sampling mice with replacement 1,000× from the experiment with the original reward function. 

## **Imaging data analysis** 

Suite2p (https://github.com/cortex-lab/Suite2P) was used to perform image registration, semiautomated cell detection and neuropil correction to obtain deconvoluted calcium traces from individual cells[41] . Only those neurons with activity that passed a threshold of 20 at least once during each session were further analyzed (Task 1: 12,232, 15,324, 15,792 and 51,845 neurons for naive, expert, expert deterministic and expert altered reward function, respectively; Task 2: 3,619 and 2,563 neurons for naive and expert, respectively; composite task: 3,364 and 4,873 neurons for early and late, respectively). 

Parcellation of the cortical areas was performed with the Allen Mouse Common Coordinate Framework. Each neuron was categorized to one of the five cortical regions based on the distance from the bregma. Neurons that were located at the border of the cortical areas were not classified (Task 1: M1: 938 and 3970; M2: 2,270 and 2,520; S1: 618 and 992; RSC: 1,480 and 4,481; PPC: 218 and 410 neurons for naive and expert, respectively; Task 2: M1: 815 and 862; M2: 616 and 545; S1: 374 and 250; RSC: 1,160 and 604; PPC: 51 and 19 neurons for naive and expert, respectively; composite task: M1: 904 and 1,157; M2: 659 and 912; S1: 467 and 472; RSC: 765 and 1,555; PPC: 78 and 299 neurons for early and late, respectively). 

The same neurons from different sessions were identified and registered using ROIMatchPub (https://github.com/ransona/ROIMatchPub). This package performs translational shift and rotation of images to match with a reference image after manually identifying landmarks. An overlap threshold was set as 0.01 and the results were manually validated. 

**GLM.** As described previously[22] , an encoding model of experimentally designed task variables was built for each neuron independently with the GLM[42][–][44] . The task variables included: Task 1: trial-onset and -offset times, object velocity, object position, joystick velocity and reward-onset times; Task 2: trial-onset and -offset times, joystick velocity, lick-onset times and reward-onset times; composite task: trial-onset and -offset times, object velocity, object position, joystick velocity, lick-onset times and reward-onset times. As the task variables were measured at a higher temporal sampling rate (2,000 Hz) than the imaging (5.67 Hz), they were downsampled by averaging during each imaging frame to match the imaging sampling rate. 

A design matrix for GLM was constructed by representing the trial-onset and -offset times, lick-onset times and reward-onset times as boxcar functions where a value of 1 was assigned to these times and 0 elsewhere. The angle of the object velocity and joystick velocity was discretized to eight equally spaced bins (0°, 45°, 90°, 135°, 180°, 225°, 270° and 315°) to generate eight time-series data with amplitude of movement. The object position was calculated by binning the arena into 10 × 10 spatial bins. Each of the task variables was convoluted with a set of behaviorally appropriate spatial or temporal basis functions to produce task predictors (trial-onset and -offset times and lick-onset times: six evenly spaced raised cosine functions extended 2 s forward and backward in time; object and joystick velocity: six evenly spaced raised cosine functions extended 2 s forward and backward in time for each direction; object position: 100 (10 × 10) evenly spaced raised cosine functions along the two axes of the arena; reward-onset times: nine evenly spaced raised cosine functions extended 4 s forward and 2 s backward in time). GLM fitting and extraction of GLM-derived response profiles for each task variable were then performed as described previously[22] . 

To examine relationships between actions (object movement for Task 1 and lick frequency for Task 2) and their neural representations, session-by-session correlations were computed across the learning stages between the traveled distance of the object and the fraction of object velocity neurons for Task 1 and between the lick frequency and the fraction of lick-onset neurons for Task 2. To further determine whether the increased fraction of the object velocity neurons was due to the increase in the object movement or learning, each session was split in half to reduce the object movement by approximately half and the fraction of the object velocity neurons was determined. 

**Analysis of** _**Q**_ **representation in the mouse cortex.** To determine neural representations of the _Q_ Task1 function, _Q_ Task1( _s_ , _a_ ), conjunctive cells encoding the object’s spatial position and direction, which respectively corresponded to _s_ and _a_ , were considered. Two types of neural representations of the _Q_ Task1 function were identified. The first class represented a high expected value of _Q_ Task1( _s_ , _a_ ) over actions, which was considered equivalent to _V_ Task1( _s_ ). Space tuning of each conjunctive neuron was compared with _VTask_ 1( _s_ ) using Pearson’s correlation coefficient. _P_ values were obtained by shuffling the object position 1,000×, computing shuffled space tuning in each neuron and calculating Pearson’s correlation coefficient between the shuffled space tuning and _V_ Task1( _s_ ). The other class of neurons represented the _Q_ Task1 function, in which the direction tuning of each neuron correlated with the _Q_ Task1 function over eight directions with no movement in spatial bins corresponding to the top 5% of activity in the space-tuning map of the same neuron. The _QTask_ 1 function was obtained by averaging _Q_ Task1 over the spatial bins after weighting _Q_ Task1 by the normalized activity in the same bins. To consider both direction and magnitude, Pearson’s correlation coefficient and dot product were then calculated between the direction tuning of each neuron and the _Q_ Task1 function. _P_ values were obtained by shuffling the object movement direction 1,000×, computing shuffled direction tuning in each neuron and obtaining the same metric between the shuffled direction tuning and the _Q_ Task1 function. 

To obtain a chance level of the fraction of neurons encoding _Q_ Task1, given the same fractions of state (space)- and action (direction)-encoding neurons, state-representing neurons and action-representing neurons were randomly sampled and it was examined whether they showed conjunctive coding and whether they represented the _Q_ Task1. 

Enrichment of _Q_ Task1-representing neurons in the original and altered-reward function (two-reward) experiments was determined by investigating the peak location of space tuning in each neuron. The fraction of neuron enriched on the high-reward side was then determined for the altered-reward function experiment in each mouse and the value was averaged across mice. For a statistical analysis, the same 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

metric was computed by randomly sampling mice with replacement 1,000× from the experiment with the original reward function and the probability distribution was obtained. 

To identify neural representations of the _Q_ Task2 function, _Q_ Task2( _s_ , _a_ ), cells encoding the licking action were considered. As there was only one state in Task 2, the space tuning of neurons was not determined. A neuron was deemed to represent the _Q_ Task2 function when the lick tuning of the neuron correlated with the _Q_ Task2 function using Pearson’s correlation coefficient and dot product. _P_ values were obtained by shuffling the lick-onset events 1,000×, computing shuffled lick tuning in each neuron and calculating the same metric between the shuffled lick tuning and the _Q_ Task2 function. The fraction of _Q_ Task2-encoding neurons that can be obtained by chance was determined by shuffling time-series of lick events. To examine a relationship between lick frequency and representations of _Q_ Task2, session-by-session correlations over learning between the lick frequency and the fraction of _Q_ Task2 function-encoding neurons were determined. 

Neural representations of the _Q_ Composite function, _Q_ Composite( _s_ , _a_ ), were determined for object movement and licking in the same way as above, except that conjunctive cells encoding space and lick events for lick-related _Q_ function ( _Q_ Lick function) were considered. The _Q_ Lick function was obtained by averaging _Q_ Lick over spatial bins corresponding to the top 5% of activity in the space-tuning map of the same neuron. _Q_ Lick was weighted by the normalized activity in each spatial bin. A chance level of the fraction of neurons encoding _Q_ Task1 at the early stage of the composite task was computed in the same way as Task 1. For all tasks, neurons with _P_ value <0.05 with the FDR in at least one metric were considered to be _Q_ Task1-, _Q_ Task2- or _Q_ Composite-representing cells. 

To estimate the variability of neural representations of the _Q_ functions in a given cortical area, neurons were sampled with replacement and fractions of _Q_ -function-related neurons among those that are task related were computed. This procedure was repeated 1,000×. 

Relationships in the fractions of _Q_ Subtask neurons across cortical regions between the subtasks and composite task were determined by sampling neurons with replacement 1,000× in each task independently and _P_ values were computed to test whether they were positively correlated. 

Neural representations of the mean _Q_ Composite function over actions were identified by comparing the space tuning of individual neurons and spatial map of the function with Pearson’s correlation coefficient. _P_ values were then obtained by shuffling the object position 1,000× as described above. The _t_ -distributed stochastic neighbor embedding (tSNE) was performed on space-tuned neurons for visualization. To test whether the mixed representations of the _Q_ Composite functions in the space domain of the mouse cortex were not observed by chance, the fraction of neurons correlated with the _Q_ Composite function averaged over actions was computed under the assumption that ‘place fields’ were uniformly distributed in the arena with the spatial basis function used in GLM[22] . 

Moment-by-moment activity of _Q_ Composite function-encoding neurons in the mouse cortex was derived from the GLM by marginalizing out task predictors other than the object position. The activity was then thresholded at the _z_ -score of 3 of the activity time-series for each neuron and sampled every 20 imaging frames for display. 

**Manifolds.** Intrinsic manifolds for population neural activity were obtained by principal component analysis (PCA) to reduce dimensionality of activity of the same set of neurons between the subtasks and composite task. Activity during each trial and preceding 2 s was concatenated within each session. The coefficient obtained by PCA from the composite task was applied to population activity from the subtask to embed it in the same PC space. The resulting manifolds derived from the subtasks and composite task were compared using the KL divergence estimation[29] , which detects whether two sets of data samples were drawn from the same distribution. The KL divergence 

between the two manifolds was therefore inversely related to their overlaps in the PC space. The KL divergence was computed using the scipy.spatial.cKDTree module in the SciPy library in Python. Briefly, the Euclidean distance was calculated between a given sample of the subtask manifold data in the PC space and its nearest neighbor within the same data (randomly sampled _n_ points). Similarly, the Euclidean distance was also determined between the same sample of the subtask manifold data and its nearest neighbor in the sampled manifold data of the composite task. The KL divergence was then estimated between the two resulting vectors ( **r** and **s** ) containing _n_ elements according to: 

**==> picture [257 x 67] intentionally omitted <==**

To compute _P_ values, the neuron index for the composite task was randomly shuffled before computing PCA and population neural activity obtained from the subtasks was embedded in this PC space. KL divergence was then computed between the resulting distributions. 

**Object movement direction selectivity.** To determine the broadness of object direction tuning of each neuron, the selectivity index (SI) was determined according to: 

**==> picture [194 x 8] intentionally omitted <==**

The circular variance was calculated according to: 

**==> picture [188 x 22] intentionally omitted <==**

where _k_ is the direction index, _rk_ the neural activity in response to the _k_ th direction and _θ_ an angle expressed in radians[45] . 

## **Deep reinforcement learning** 

**Environment.** A customized OpenAI’s gym environment was created with continuous state and action spaces to simulate the behavior paradigm designed for mice. The arena was 2.0 × 2.0 arbitrary units (a.u.) in size. The states were agent’s position in _x_ and _y_ coordinates and velocity. The movement variable ranged from −0.1 to 0.1 in _x_ and _y_ directions and the lick variable ranged from 0 to 0.1. If the lick variable exceeded 0.08, this was considered as a lick event. In Task 1, a reward of 1 was given when agents reached the reward zone (0.8 × 0.8 a.u.) located in the center of the arena from a random position outside the reward zone and no reward was given elsewhere. In Task 2, a reward of 1 was given only when the agent’s lick event was detected. In the composite task, a reward of 1 was given when the agents reached a target area located at the bottom center of the arena (0.1 × 0.0031 a.u.) and took a lick action. Agents became nonmovable once they reached the target area. No reward was given elsewhere. As was the case for Task 1, agents were reinitialized to a random position outside the target region at the start of each trial. 

**SAC algorithm.** The SAC algorithm[23][,][24] is an off-policy actor-critic algorithm used in continuous state and action spaces for a Markov decision process. The SAC algorithm considers the following objective: 

**==> picture [197 x 22] intentionally omitted <==**

where _π_ is a policy, _T_ the end of an episode, 𝔼𝔼 expectation, _ρπ_ a state-action marginal of the trajectory distribution determined by _π_ , _r_ ( _st_ , _at_ ) a reward in a state _st_ and action _at_ at time _t_ , _α_ a temperature 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

parameter to determine the relative contribution of the entropy term against the reward and ℋ an entropy of _π_ , defined as: 

**==> picture [182 x 19] intentionally omitted <==**

The conventional objective of RL can be recovered when _α_ becomes 0. 

The SAC algorithm used in the present study was based on the OpenAI Spinning Up packages (https://spinningup.openai.com/en/ latest/#). The agent was composed of ANNs with multilayered perceptrons for the actor computing _π_ and critic computing the _Q_ function (3 hidden layers and 256 neurons in each layer with ReLU as an activation function). Two parameterized _Q_ networks were independently trained and the minimum of the two was used to mitigate positive bias in the policy improvement step. Adam was used as an optimizer for the actor and critic networks. Hyperparameters of the algorithms were: steps per epoch: 300, epoch number: 200, replay size: 1,000,000, gamma: 0.95, polyak averaging parameter: 0.995, learning rate: 0.0001, _α_ : 0.02 for the stochastic policy in Tasks 1 and 2; 0 for the deterministic policy in Task 1; 0.005 for the composite task; maximum episode length: 300. A total of six agents were trained with different seeds. 

In the composite task, the initial _Q_ Composite function was obtained either by averaging the _Q_ Subtask functions or by taking the maximum of the _Q_ Subtask functions using learned parameters of the _Q_ Subtask networks. As a control, the agent with a randomly initialized _Q_ Composite function was also trained. The early and late learning stages of the composite task were defined as the 20th and 200th out of 200 epochs, respectively. 

For control initialization in the composite task learning, Task 2 was modified so that the state of the agent was located at the top middle region of the arena. This ensured that the value of the mean _Q_ Composite function over states and actions remained comparable with the original value before the deep RL agents were introduced to the composite task. 

**MBPO.** The MBPO algorithm[25] was based on the model-based reinforcement learning library (MBRL-Lib)[46] . MBPO constructs an ensemble of forward dynamic models using probabilistic neural networks and uses model-free SAC as a policy optimization algorithm under the learned model. MBPO uses an iterative process of data collection under the updated policy and training of new dynamic models with these data. For the model construction, the ensemble of 10 forward dynamic models was used, each of which was composed of a multilayer perceptron with 4 hidden layers and 256 units with the Sigmoid Linear Unit function as an activation function. Hyperparameters of the algorithm were selected as: model learning rate: 0.0001; model weight decay: 2 × 10[−6] ; model batch size: 256; validation ratio: 0.2; frequency of model training: 200; effective model rollouts per step: 5; rollout schedule: [1,15,1,1]; number of SAC updates per step: 20; SAC updates every step: 1; and number of epochs to retain in SAC buffer: 50. The model learning rate was set to 0 when the dynamic models were not constructed. SAC hyperparameters were the same as above. A total of ten agents was trained with different seeds for each group (model and no-model groups). 

## **Behavior analysis of deep RL agents** 

The behavior of deep RL agents was obtained from the initial state by iteratively inputting new states based on previous actions defined by the actor whereas parameters for the _π_ and _Q_ neural networks were fixed. In each trial, this procedure was repeated until agents obtained a reward (hit) or 300 time steps elapsed (miss). A total of 3,000 episodes was performed. The state-value function, _V_ ( _s_ ), action-value function, _Q_ ( _s_ , _a_ ), policy, _π_ and policy entropy were computed similarly to those in mice with _γ_ set to be 0.95. As in the case of mice, cosine similarity was computed to compare policies across tasks and learning stages. 

**Maximum entropy policies and composability of a new policy.** To study whether maximum entropy policies were critical for behavior composition, visitation of the reward zone of the composite task was measured in Task 1 while the initial position was fixed ( _x_ : −0.2; _y_ : −0.98). A relationship between the visitation and the return obtained during the composite task was then determined. Furthermore, to investigate the condition under which maximum entropy policies may become detrimental, deep RL agents were trained in the environment where the target regions were made identical between Task 1 and the composite task. 

## **Activity analysis of the ANN of deep RL agents** 

Space tuning of neurons in the hidden layers of the _Q_ networks was determined by feeding 100,000 uniformly distributed random state and action inputs and measuring outputs of each layer after the activation function. The arena was divided into 40 × 40 spatial bins and the activity corresponding to each bin was averaged. This analysis ensured that activity was captured in the states that agents might not visit due to the limited number of trials, so that space tuning across different learning stages could be compared. Direction tuning of neurons in the hidden layers of the _Q_ networks was determined by averaging neural activity corresponding to each binned direction of agent’s movement. 

**Analysis of** _**Q**_ **representation in deep RL agents.** Neural representations of the _Q_ functions in the hidden layers of the _Q_ networks and their chance-level fractions were determined in the same manner as those in mice. _Q_ manifolds were also identified similarly to mice for the middle layer and additional comparisons between the naive and expert stages of the subtasks were performed. 

Moment-by-moment activity of neurons encoding the _Q_ Composite function in deep RL agents was obtained by concatenating activity across epochs for each neuron, which was then _z_ -scored and sampled every 100 steps for display. 

**Ablation in the ANN of deep RL agents.** To investigate how inactivation of _Q_ Subtask-representing neurons affects an agent’s learning in the composite task, activity of either 50% or 100% (full) _Q_ Subtask-representing neurons in the hidden layers of the _Q_ networks were set as 0. As a control, the same number of non- _Q_ Subtask-representing neurons as the full ablation were also inactivated. 

**Distribution of** _**Q**_ **representation in deep RL agents and mice.** It was determined whether the _Q_ Move and _Q_ Lick functions were represented in a dedicated or distributed manner. For the ANN of deep RL agents, relative fractions of _Q_ Move and _Q_ Lick representations were obtained in the Task 1 and Task 2 subnetworks according to: 

Fraction in Task 1 (or Task 2) network − Fraction in Task 2(or Task 1)network Fraction in Task 1 (or Task 2) network + Fraction in Task 2(or Task 1)network (12) 

For mice, Pearson’s correlation coefficients in the cortical distribution of _Q_ Move and _Q_ Lick representations were computed between the subtask expert and composite task early or composite task late stages. 

## **Statistics** 

For statistically significant results, _P_ values were adjusted after respective correction methods for multiple comparisons, which are described in each figure legend. 

## **Reporting summary** 

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

## **Data availability** 

Data are available at https://doi.org/10.5281/zenodo.7283276 on Zenodo. 

## **Code availability** 

Code for data analysis is available at https://github.com/HiroshiMakinoLaboratory/Makino2022NatureNeuroscience on GitHub. 

manuscript. This work was funded by the NARSAD Young Investigator Grant from the Brain & Behavior Research Foundation, Nanyang Assistant Professorship from Nanyang Technological University, Singapore Ministry of Education Academic Research Fund Tier 1 (grant nos. 2018-T1-001-032 and RT11/19), Ministry of Education Academic Research Fund Tier 2 (grant no. MOE2018-T2-1-021) and Ministry of Education Academic Research Fund Tier 3 (grant no. MOE2017-T3-1-002). 

## **References** 

41. Pachitariu, M. et al. Suite2p: beyond 10,000 neurons with standard two-photon microscopy. Preprint at _bioRxiv_ https://doi. org/10.1101/061507 (2016). 

42. Park, I. M., Meister, M. L., Huk, A. C. & Pillow, J. W. Encoding and decoding in parietal cortex during sensorimotor decision-making. _Nat. Neurosci._ **17** , 1395–1403 (2014). 

43. Driscoll, L. N., Pettit, N. L., Minderer, M., Chettih, S. N. & Harvey, C. D. Dynamic reorganization of neuronal activity patterns in parietal cortex. _Cell_ **170** , 986–999.e916 (2017). 

44. Minderer, M., Brown, K. D. & Harvey, C. D. The spatial structure of neural encoding in mouse posterior cortex during navigation. _Neuron_ **102** , 232–248.e211 (2019). 

45. Ringach, D. L., Shapley, R. M. & Hawken, M. J. Orientation selectivity in macaque V1: diversity and laminar dependence. _J. Neurosci._ **22** , 5639–5651 (2002). 

46. Pineda, L., Amos, B., Zhang, A., Lambert, N. O. & Calandra, R. MBRL-Lib: a modular library for model-based reinforcement learning. Preprint at _arXiv_ https://ui.adsabs.harvard.edu/ abs/2021arXiv210410159P (2021). 

## **Acknowledgements** 

I thank A. Suhaimi and A. Lim for their assistance with the experiments, K. Tay for animal husbandry, A. Y. Tan and S. -C. Yen for discussions and members of the Makino laboratory for comments on the 

## **Author contributions** 

H.M. conceived the study, performed the experiments, conducted deep RL training, analyzed the data and wrote the manuscript. 

## **Competing interests** 

The author declares no competing interests. 

## **Additional information** 

**Extended data** is available for this paper at https://doi.org/10.1038/ s41593-022-01211-5. 

**Supplementary information** The online version contains supplementary material available at https://doi.org/10.1038/s41593-022-01211-5. 

**Correspondence and requests for materials** should be addressed to Hiroshi Makino. 

**Peer review information** _Nature Neuroscience_ thanks Kiah Hardcastle and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [441 x 324] intentionally omitted <==**

**Extended Data Fig. 1 | Behavior analysis of subtasks over learning in mice and deep RL agents. a** , Left, schematic of subtasks. Right, subtask behavior analysis in mice (Task 1: *** _P_ < 0.001, _n_ = 7 and 6 mice for naive and expert respectively; Task 2: n.s., _P_ = 0.33, *** _P_ < 0.001, _n_ = 7 mice for naive and expert, one-tailed bootstrap with Bonferroni correction, mean ± s.e.m.). Naive sessions in Task 1 were defined as the first few sessions when mice were directly introduced to the environment with the 4 × 4 cm[2] reward zone and expert sessions were defined as those following completion of at least two consecutive sessions within 30 minutes. In Task 2, naive and expert sessions were defined as the first and fifth sessions, respectively. **b** , Example Task 1 trajectories, state-value functions, _V_ ( _s_ ), and policies, _π_ , at different learning stages in mice (trial duration: naive: 204.7 

± 21.8 s; expert: 4.8 ± 0.6 s, mean ± s.e.m., _n_ = 7 and 6 mice for naive and expert respectively). Note that the object movement was biased in top left and bottom right directions due to relative position of the joystick to the right forelimb. **c** , Example Task 2 lick events and state-value functions, _V_ ( _s_ ), at different learning stages in mice. Lick events required to dispense water but not related to water consumption became more restricted during the LED-on period over the course of learning ( _P_ = 0.006, _n_ = 7 mice for naive and expert, one-tailed bootstrap). **d** , Subtask behavior analysis in deep RL agents (Task 1 and Task 2: *** _P_ < 0.001, n.s., _P_ = 1.0, _n_ = 6 agents, one-tailed bootstrap between naive vs. expert with Bonferroni correction, mean ± s.e.m.). **e** , Same as **b** for deep RL agents. **f** , Same as **c** for deep RL agents. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [337 x 248] intentionally omitted <==**

**Extended Data Fig. 2 | Further analysis of the composite task. a** , Left, policies described as vector fields during each phase of the tasks in deep RL agents. Right, cosine similarities of the policies relative to the policy at the early phase of the composite task in deep RL agents and mice (*** _P_ < 0.001, _n_ = 6 agents and _n_ = 7 mice, one-tailed bootstrap, mean ± s.e.m.). **b** , Learning curve of deep RL agents with control initialization in the composite task (*** _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap, mean ± s.e.m.). In the control initialization, Task 2 

was modified so that the state of the agent was located at the top middle region of the arena. **c** , Learning curve of deep RL agents trained with and without model training in the model-based policy optimization (MBPO) algorithm in the composite task (** _P_ = 0.006, _n_ = 10 agents, one-tailed bootstrap, mean ± s.e.m.). MBPO constructs forward dynamics models and uses model-free SAC as a policy optimization algorithm under the learned model. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [431 x 412] intentionally omitted <==**

**Extended Data Fig. 3 | Neural representation in** _**Q**_ **networks. a** , Tuning properties for space, direction and lick in example units in each layer of _Q_ networks for each task. **b** , Schematic of how _QTask_ 1 representations in individual neurons were determined. After tuning properties of a given neuron were identified (i), relevant states, _s_ , were determined based on space-related activity 

(ii). _QTask_ 1 distribution over movement directions was then computed in these states (iii) and the resulting _QTask_ 1 function was compared with the direction tuning of the neuron (iv). **c** , Fractions of each type of _QTask_ 1-representing neurons in deep RL agents and mice. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [499 x 358] intentionally omitted <==**

**Extended Data Fig. 4 | Generalized linear model (GLM) and representation of task variables. a** , Schematic of GLM. Task predictors included trial onset and offset, object velocity, object position, joystick velocity, lick onset and reward onset. **b** , Pseudo-explained variance (EV) for each cortical region at the naive and expert stages of Task 1, Task 2 and the composite task. **c** , Fractions of task-variable-related cells in each cortical area. ‘Task’ indicates any of the task variables. **d** , Left, relationship between fractions of object velocity neurons and object movement (cm) in Task 1 ( _R_[2] = 0.50, *** _P_ < 0.001 computed with Student’s _t_ cumulative distribution function, two-tailed, _n_ = 48 sessions, considering both 

the naive and expert stages). Right, fractions of object velocity neurons at the expert stage of Task 1 when all or the second half of the session was used (n.s., _P_ = 0.41, _n_ = 7 mice, one-tailed bootstrap, mean ± s.e.m.). These results indicate that the amount of the object movement _per se_ was not related to the fractions of object velocity neurons; their co-modulation is a consequence of learning. **e** , Relationship between fractions of lick onset neurons and lick frequency ( _R_[2] = 0.01, n.s., _P_ = 0.53 computed with Student’s _t_ cumulative distribution function, two-tailed, _n_ = 35 sessions, considering all learning stages). 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [471 x 174] intentionally omitted <==**

**Extended Data Fig. 5 | Neural representation of** _**QSubtask**_ **functions is not due to actions** _**per se**_ **. a** , Environments with altered reward functions and resulting _QTask_ 1 functions. The reward zone in Task 1 was split into two and a high or low reward was assigned. Same visualization as Fig. 2d. **b** , Tuning properties of example neurons showing shifts in space representations of _QTask_ 1-representing neurons to the high reward side. **c** , The policy (top) and state occupancy (bottom) did not change between the original (control) and altered (two reward) reward functions (policy: n.s., _P_ > 0.05 for all pair-wise comparisons, _n_ = 21, 42, 15 animal-by-animal comparisons from the left to right, one-tailed bootstrap 

with Bonferroni correction, mean ± s.e.m.; state occupancy: n.s., _P_ = 0.80, _n_ = 7 and 6 mice for control and two reward, respectively, one-tailed bootstrap). For the policy, cosine similarities were computed either within or across the two environments. **d** , Quantification of the enrichment of _QTask_ 1-representing neurons on the high reward side (** _P_ = 0.006, _n_ = 7 and 6 mice for control and two reward, respectively, one-tailed bootstrap, mean ± s.e.m.). **e** , Lick frequency was not predictive of the fractions of _QTask_ 2-representing neurons ( _R_[2] = 0.00, n.s., _P_ = 0.94 computed with Student’s _t_ cumulative distribution function, two-tailed, _n_ = 35 sessions, considering all learning stages). 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [295 x 197] intentionally omitted <==**

**Extended Data Fig. 6 | Representation models for the hierarchical composition of a new** _**QComposite**_ **function.** Left, since the action spaces between Task 1 and Task 2 are independent, averaging the two _QSubtask_ functions yields a similar _Q_ function ( _QComp_ .). Right, by contrast, since the state spaces are 

shared between Task 1 and Task 2, the averaging results in a mixed value function with two hot spots located in the center and bottom middle regions. Same visualization as Fig. 2a,d. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [393 x 363] intentionally omitted <==**

**Extended Data Fig. 7 | Reuse of learned neural representation in the composite task. a** , Neural representations in deep RL agents. Left, space, direction and lick tuning of example neurons at the subtask naive, subtask expert and composite task early stages. Right, quantification of representation similarity. Space tuning: *** _P_ < 0.001; direction tuning: ** _P_ = 0.005, _n_ = 478 and 403 neurons for Task 1 naive and composite task early compared to Task 1 expert, respectively; lick tuning: * _P_ = 0.02, _n_ = 427 and 413 neurons for Task 2 naive and composite task early compared to Task 2 expert, respectively, two-tailed KS test with Bonferroni correction). **b** , Same as **a** for mice. Note that the same neurons were imaged across the subtask expert and composite task early stages only (no subtask naive stage). Space tuning: * _P_ = 0.03, _n_ = 422 neurons; direction tuning: *** _P_ < 0.001, _n_ = 634 neurons; lick tuning: *** _P_ < 0.001, _n_ = 213 neurons, one-tailed permutation with Bonferroni correction). **c** , Left, explained variance (EV) derived 

from principal component analysis (PCA) as a function of dimensions across different learning stages of deep RL agents ( _n_ = 6 agents for Task 1 and Task 2, mean ± s.e.m.). Right, number of dimensions required for EV of >90% across different learning stages in deep RL agents ( _n_ = 6 agents for Task 1 and Task 2, mean ± s.e.m.). **d** , Schematic of the _Q_ manifold and example population activity of deep RL agents in the PC space. Note that the overlap between the subtask naive versus subtask expert stages is smaller than the subtask expert versus composite task early stages. **e** , Manifold overlaps measured by KL divergence of the population activity in the PC space in deep RL agents (Task 1 and Task 2: *** _P_ < 0.001, _n_ = 6 agents, one-tailed bootstrap). Number of dimensions considered: 3 for Task 1 and 1 for Task 2 based on **c** . The edges of the whiskers are maximum and minimum and the edges of the boxes are 75% and 25% of 1000 randomly sampled mean KL divergence. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [469 x 292] intentionally omitted <==**

**Extended Data Fig. 8 | Further analysis of the hierarchical composition a new** _**QComposite**_ **function. a** , Space tuning of individual neurons shown in Fig. 4a for deep RL agents and mice. **b** , Moment-by-moment activity of example neurons encoding the _QComposite_ function. The activity of the mouse neurons was derived from GLM after marginalizing out other task predictors than the object position. **c** , Spatial representations of randomly selected 300 neurons (150 from Task 1 and 150 from the composite task) in the same tSNE coordinate are distinct between Task 1 and the composite task in deep RL agents and mice. The arrows indicate regions containing the mixed _Q_ representations shown on the right. **d** , Spatial representations of randomly selected 300 neurons in the same tSNE coordinate 

in deep RL agents trained with the _QComposite_ function derived from the average and maximum of the _QSubtask_ functions at the early stage of the composite task (150 from average and 150 from maximum). The magenta and gray arrows indicate clusters of neurons whose space tuning was unique to the _QComposite_ function derived from the averaging operation. Note that such a subtle difference led to distinct learning efficiency in the composite task (Fig. 1i), indicating that these mixed _Q_ representations of the subtasks (high activation in the center and bottom middle regions of the arena) were important for the hierarchical composition of a new policy. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [427 x 361] intentionally omitted <==**

**Extended Data Fig. 9 | Neural representation of the** _**QComposite**_ **function at the late learning stage of the composite task. a** , _QComposite_ function in deep RL agents at the late learning stage of the composite task. Same visualization as Fig. 2a. **b** , Example neural representations of the _QComposite_ function in deep RL agents. Same visualization as Fig. 2b. **c** , Space tuning of randomly selected 300 neurons in the tSNE coordinate in deep RL agents. Correlation denotes Pearson 

correlation coefficient between space tuning of individual neurons and the mean _QComposite_ function over actions. **d** , Same as **a** for mice. **e** , Same as **b** for mice. **f** , Fractions of movement- and lick-related _QComposite_ -representing neurons at the late stage of the composite task in mice ( _n_ = 7 mice, mean ± s.e.m.). Corresponding plots for deep RL agents are shown in Fig. 4b. **g** , Same as **c** for mice. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01211-5 

**==> picture [425 x 185] intentionally omitted <==**

**Extended Data Fig. 10 | Maximum entropy policies improve composability of a new policy. a** , Left, schematic illustrating the conflict in policies between Task 1 and the composite task. Right, _V_ ( _s_ ) in the composite task averaged across deep RL agents. The arrow indicates location of the conflict. **b** , Maximum entropy policies for Task 1 increase the probability of deep RL agents to visit the reward zone in the composite task. The higher visitation of the reward zone of the composite task in Task 1 increases the state occupancy in its vicinity during the early phase of the composite task. **c** , Relationship between the visitation of the reward zone 

of the composite task in Task 1 and return during the early stage of the composite task ( _R_[2] = 0.59 for ‘+ entropy maximization’ fit with a single-term power series model, _n_ = 6 agents for ‘+ entropy maximization’ and ‘– entropy maximization’). **d** , Maximum entropy policies may become detrimental when the target regions are identical between Task 1 and the composite task. In this case, deterministic policies in Task 1 lead to more rapid learning, albeit at the cost of flexibility (* _P_ = 0.01, _n_ = 6 agents, one-tailed bootstrap, mean ± s.e.m.). 

Nature Neuroscience 

**==> picture [228 x 36] intentionally omitted <==**

**==> picture [365 x 47] intentionally omitted <==**

**==> picture [519 x 403] intentionally omitted <==**

**==> picture [76 x 60] intentionally omitted <==**

**==> picture [523 x 103] intentionally omitted <==**

**==> picture [359 x 92] intentionally omitted <==**

**==> picture [186 x 53] intentionally omitted <==**

**==> picture [238 x 143] intentionally omitted <==**

**==> picture [433 x 39] intentionally omitted <==**

**==> picture [152 x 110] intentionally omitted <==**

**==> picture [113 x 67] intentionally omitted <==**

**==> picture [520 x 179] intentionally omitted <==**

