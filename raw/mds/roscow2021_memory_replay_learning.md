Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

## Review 

## Learning offline: memory replay in biological and artificial reinforcement learning 

## Emma L. Roscow,[1,] * Raymond Chua,[2] Rui Ponte Costa,[3] Matt W. Jones,[4,6] and Nathan Lepora[5,6] 

Learning to act in an environment to maximise rewards is among the brain’s key functions. This process has often been conceptualised within the framework of reinforcement learning, which has also gained prominence in machine learning and artificial intelligence (AI) as a way to optimise decision making. A common aspect of both biological and machine reinforcement learning is the reactivation of previously experienced episodes, referred to as replay. Replay is important for memory consolidation in biological neural networks and is key to stabilising learning in deep neural networks. Here, we review recent developments concerning the functional roles of replay in the fields of neuroscience and AI. Complementary progress suggests how replay might support learning processes, including generalisation and continual learning, affording opportunities to transfer knowledge across the two fields to advance the understanding of biological and artificial learning and memory. 

## Replay in biological and artificial reinforcement learning 

Research into reinforcement learning (see Glossary) in biology, psychology, and AI has a long and symbiotic history [1]. In recent years, deep reinforcement learning has shown remarkable success in problems previously thought intractable. Key to the success of these algorithms is the practice of interleaving new trials with old ones, a technique known as experience replay [2], and an example of convergence between biological and artificial neural networks. Replay has proved important for cognitive theories of memory [3] and the importance of replay in deep reinforcement learning supports the theory that ‘offline’ activity can aid learning and memory, raising general computational principles through which this can be achieved by any intelligent system. The relative ease of manipulating replay in artificial systems compared with biological brains means that advances in deep reinforcement learning can offer useful test cases for neuroscientists. Meanwhile, the continuing search for ever-better learning algorithms in AI could be informed by recent neurobiological insights into how self-organised activity can lead to selective strengthening or weakening of specific memories [4–8], generalisation from individual experiences to abstract knowledge [9], and, more generally, flexible adaptation to a changing world [10–13]. 

Here, we review recent developments in both fields. We discuss the successes of uniform experience replay and prioritised experience replay in AI, reviewing analogous neurobiological phenomena evident in rodent and human experiments. Our review converges on the proposal that methods which avoid explicit storage of past trials and generate their own replay samples may better reflect biological processes and hold the key to flexible reinforcement learning. 

## Highlights 

Reinforcement learning in deep neural networks often relies on the interleaving of new and old episodes, a technique which mimics the replay of neuronal activity in the brain. 

Biological replay is important for memory consolidation and has wider roles in other cognitive processes such as planning and generalisation. Deep neural networks offer a framework for understanding the role of replay in learning and memory. 

We suggest how recent developments could be leveraged to support more robust, efficient, and flexible reinforcement learning agents by avoiding explicit storage of past trials. 

Theoretical advances and more sophisticated experimental task designs will help uncover how biological replay supports complex cognition over time and throughout the brain. 

- 1Centre de Recerca Matemàtica, Bellaterra, Spain 

- 2McGill University and Mila, Montréal, Canada 

3Bristol Computational Neuroscience Unit, Intelligent Systems Lab, Department of Computer Science, University of Bristol, Bristol, UK 4School of Physiology, Pharmacology and Neuroscience, University of Bristol, Bristol, UK 

5Department of Engineering Mathematics and Bristol Robotics Laboratory, University of Bristol, Bristol, UK 

- 6These authors contributed equally to this work 

## Uniform experience replay and its origins in neuroscience 

Reinforcement learning in AI was developed in the mid-20th century, taking inspiration from earlier animal behaviour research [1]. In training reinforcement learning algorithms, an artificial 

*Correspondence: 

eroscow@crm.cat (E.L. Roscow). 

808 Trends in Neurosciences, October 2021, Vol. 44, No. 10 https://doi.org/10.1016/j.tins.2021.07.007 © 2021 Elsevier Ltd. All rights reserved. 

## Trends in Neurosciences 

agent collects data samples through continuous interaction with a real or simulated world, learning policies for selecting actions given the state of the environment in a way that maximises a reward function. Given limited online experience, learning can be accelerated by storing past experiences and subsequently sampling from them repeatedly, in effect to increase the training set. 

Experience replay first appeared in the AI literature in the early 1990s as a means to achieve such an increase [2] (Box 1) and grew in popularity with the advent of deep reinforcement learning and its applications to Atari games and Go in the early 2010s [14,15]. Independently, a series of neurophysiology studies beginning in the 1980s and 1990s found a similar phenomenon of reusing past experience in the mammalian brain (see Figure 1 and Box 2, and recent reviews for more detail [3,16–19]). These neuroscientific replay studies unveiled, among other insights, potential mechanisms of sleep-dependent memory consolidation, with replay providing a cellular basis for the long-standing observation that sleep supports memory [20]. 

How does replay improve memory? One of the leading hypotheses is that replay induces Hebbian plasticity between the cells being replayed [21–25], thereby strengthening their synaptic connections. Replay events, particularly during non-rapid eye movement (non-REM) sleep, typically reiterate neural patterns on a faster timescale than during the original experience [26–28], which might further encourage spike-timing-dependent plasticity [21]; one could call this the ‘offloading plasticity until later’ theory of how replay supports memory consolidation. However, while the importance of replay for spatial (hippocampus-dependent) memory has been established, questions remain about which aspects of the experience are represented in replayed activity, how replay patterns propagate through the brain, and the roles of replay in wider cognitive processes. 

Computational studies have suggested functions for replay that extend beyond memory consolidation (Box 3). The complementary learning systems theory has used the so-called ‘penguin problem’ to illustrate the necessity of maintaining a network that is stable enough for acquired 

## Box 1. Experience replay in artificial intelligence 

In discrete time sequences, incoming data samples are usually represented in the form of an experience tuple, consisting of a state s at time step t, action a performed at time step t, reward r obtained at time step t, and the next state st+1 at next time step t + 1. This experience tuple is first stored in a buffer and, during the learning phase, samples are randomly drawn in mini-batch from this buffer uniformly. 

In deep Q networks, these mini-batch samples are then used to learn the agent’s Q-value function, the expected future reward associated with each pair of states and actions, using off-policy Q-learning. The Q-value function is policydependent as it relies on data collected resulting from the agent’s actions derived from its policy (behaviour). In the tabular setting, this Q-value function can be represented by a table of size ∣S ∣ × ∣ A∣, where ∣S∣ is the number of states and ∣A∣ is the number of actions in the environment. It is defined as: 

Q[π] ðs; aÞ ¼ E π �r1 þ γ r2 þ γ[2] r3 þ … js0 ¼ s; a0 ¼ a� 

½I� 

where γ is the discount factor that controls how much the agent prioritises immediate rewards against long-term rewards. The off-policy update rule for the Q-value function is: 

Qðs; aÞ ← Qðs; aÞ þ α½rtþ1 þ γ maxa0 Qðs[0] ; a[0] Þ − Qðs; aÞ� ½II� where α is the learning rate. The Q-value function is said to have been completely learnt when its values have converged. 

As the agent continuously explores the environment and collects data samples, sooner or later the buffer will become full and the oldest samples will be replaced by newer samples. This strikes a balance between learning the most recent samples and allowing older samples to ‘live’ longer than they usually would, such as in the classical online learning setting. Experience replay has shown to improve the learning efficiency of artificial agents [105]. 

## Glossary 

Action policy: behaviour learned by a reinforcement learning agent that determines the actions to be taken given observations about the current state. Backpropagation: learning algorithm for updating the weights in a deep neural network, in which the gradients of the error function are calculated for each layer sequentially, starting with the last layer. 

Catastrophic interference(: or forgetting); when new learning in a network causes dramatic changes that result in the loss of previously acquired, stable associations. 

Deep Q network (DQN): deep neural network that performs Q-learning. Deep reinforcement learning: reinforcement learning algorithms implemented in deep neural networks, characterised by an input later, an output layer, and at least one intermediate hidden layer. Dopamine: neuromodulator released by (among other brain regions) the basal forebrain. Dopamine has been proposed to function as a reward-prediction error signal throughout the brain. 

Experience replay: technique of sampling from past experiences stored in a memory buffer and replaying them to the network. 

Experience tuple: the data from a single episode that is stored in a memory buffer to be replayed later; typically, the state of the environment, the action taken by the agent, the resulting reward, and the subsequent state of the environment. 

Hippocampal replay: reinstatement of neural activity that encodes a previous experience in the hippocampus during rest and sleep. 

Memory buffer: storage of experience tuples during the learning of a task, which can later be sampled from and replayed. 

Memory consolidation: stabilisation of a recent memory into the neural circuit so that it is retained long-term, through chemical and structural plasticity processes. 

Neuromodulation: chemical transmission between neurons that diffuses over a broad area, to regulate the activity of a large number of neurons. Non-REM sleep: light and deep sleep stages, excluding rapid eye movement (REM) sleep, characterised by synchronous patterns of neural activity. Most replay has been observed in non- 

**==> picture [44 x 36] intentionally omitted <==**

Trends in Neurosciences, October 2021, Vol. 44, No. 10 809 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

**==> picture [356 x 121] intentionally omitted <==**

## **Trends in Neurosciences** 

Figure 1. Replay of hippocampal place cells. Replay of hippocampal place cells during a single lap of a linear track. (A) Spiking of place cells during a sharp-wave ripple, representing a forward replay. (B) Sequential spiking of place cells that encode successive locations on the track; colours represent the location on the track to which the cell is tuned. Black trace at the top shows concurrent local field potential. Red and blue boxes outline bursts of spiking, which are magnified in A and C, respectively. (C) Spiking of place cells during a sharp-wave ripple, representing a reverse replay. (D) Animal’s running velocity, including periods of immobility before and after the run. Figure adapted from [119]. 

knowledge to persist, but plastic enough to incorporate new knowledge [29]. In this illustration, a network was trained to classify living things from their characteristics, before being presented with an anomalous semi-aquatic bird (the penguin) that has feathers and wings like a bird, but does 

## Box 2. Hippocampal replay 

Pyramidal neurons in the hippocampus exhibit spatial receptive fields: their firing rate increases by as much as tenfold when the animal is in a particular location [106]. Taken together, such ‘place cells’ have been proposed to form a cognitive map of an environment from which an animal may be able to plan routes, find shortcuts, and make other inference. As the animal traverses a room or a habitat, the sequence of increased firing rates of one place cell after another can provide a read-out of the animal’s trajectory through the environment [29]. Following earlier predictions [107,108], a series of studies in the 1990s showed that pairs of place cells that were coactive during behaviour (i.e., encoding overlapping or adjacent locations on a maze) became coactive again when the animal was taken away from the maze and left to rest or sleep in one place [31–34]. This reactivation of place cell pairs was above both the level of chance and the level of their coactivation during rest before exploring the environment; that is to say that the hippocampal trace of previous behaviour was being replayed during rest, when the animal was not running or exploring and the hippocampus was otherwise unengaged with the task of navigation (Figure 1). 

REM sleep and it is unclear to what extent the quantity, attributes, and computational roles of replay differ between REM and non-REM sleep. Place cell: neuron found in the hippocampus that fires preferentially when the animal is in a particular place. Plasticity: changes in neural circuits, particularly the strengthening and weakening of synaptic connections. Q-learning: a model-free reinforcement learning algorithm and extension of temporal-difference learning, for optimising the policy of selecting actions in any given state. 

Reinforcement learning: learning to act to maximise expected rewards, an area of study in both psychology and machine learning. 

State transitions: the possibility or probability of one state leading to another state in a single step; in spatial navigation tasks this depends on the topology of the environment, including physical distance between states and barriers between them. 

Temporal-difference error: reinforcement learning algorithm that learns the values of states by minimising the difference in predicted value between temporally successive states. 

Further research has shown that such replay extends outside the hippocampus to cortical [35–37] and limbic [38–40] brain areas, which are involved in processing nonspatial information, suggesting a brain-wide phenomenon in which many facets of an experience, including sensory and reward-related properties, can be reactivated together. 

In humans, the noninvasive, nonsurgical experimental methods usually required for recording neural activity offer lower spatial and temporal resolution, making replay detection more difficult. Nevertheless, classifiers trained on human neural activity during a task show hippocampal reactivation of task representations during subsequent rest, with a bias towards replaying items that are highly rewarded and subsequently better remembered [109,110]. Replay has also been shown to selectively strengthen weaker memories [111] and re-evaluate state-action values for reinforcement learning [13] and with tentative evidence of hippocampal-to-cortical transfer of task-relevant information [112]. 

Evidence for the causal role of replay in memory consolidation has come from studies in which sharp-wave ripples in the hippocampus are either disrupted or prolonged. Hippocampal replay relies on synchronous excitation of large neuronal populations, which occurs during sharp-wave ripples [31]: distinctive, transient bursts of high-frequency oscillatory activity [113] that promotes the firing of a subset of pyramidal cells, resulting in replay sequences [26,27]. Disrupting the ripples, which also disrupts coincident replay events, results in slower spatial learning on timescales of minutes [4,5,10], and days [41,42]. Disrupting the replay event but not the ripple itself (technically a much harder feat) has also been shown to slow down learning [43]. Extending the duration of ripples, conversely, appears to increase replay and improve spatial memory [5]. Finally, studies that invoke or bias replay of some experiences over others can selectively improve the memory of those items [6–8,44]. The definitive evidence for a link between replay and memory consolidation would be performance improvement following the induction of a replay event from scratch. Such a test, however, is technically challenging and to our knowledge has not been achieved experimentally so far. 

810 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

## Box 3. Proposed computational functions of replay 

Replay has been proposed to serve a variety of cognitive and network functions for learning, some of which depend biologically on brain area and sleep–wake state (during behaviour, extended rest, rapid eye movement (REM) sleep, or non-REM sleep). The theories and perspectives outlined briefly in the following bullet points are not mutually exclusive and some of them are not unique to reinforcement learning, but they suggest how replay can support learning from individual rewarded episodes. 

- Consolidation of new memories rapidly encoded by a fast learner (the hippocampus) into long-term storage in a slow learner (the cortex) [57]. Memory encoding can form rapidly in the hippocampus but takes longer to be integrated into cortical representations (but see [114,115]). Replay serves as additional training to supplement online learning, in order to strengthen cortical representations [116]. 

- Generalising across episodes. Representations formed quickly and sparsely, for example, in the hippocampus enable pattern separation, which is beneficial for one-shot learning or retention of individual episodes of experience, but poorly suited to generalising across episodes. By contrast, a slower-learning cortex can integrate multiple episodes and encode statistical regularities between them, but takes many examples to achieve this (but see [117]). Replay serves as additional training for the cortex from individual episodes initiated by the hippocampus. 

- Preventing catastrophic interference. Gradual interleaving of online and offline information regularises synaptic changes or weight changes to ensure that network representations of older information are not supplanted by those of newer information [30,57]. 

- Stabilising learning. Experiences close in time tend to be correlated, which can result in large, fluctuating weight changes. Interleaving uncorrelated samples constrains weight changes for more stable learning [57,118]. 

not fly and swims like a fish. Updating the connection weights to incorporate this new information disrupted and worsened performance for other birds [29]. The proposed solution was replay, interleaving training of the new item (penguin) with older, similar items (other birds); this proved sufficient to maintain both representations without interference. One could call this the ‘preventing catastrophic interference’ theory of how replay improves memory consolidation, an idea that dates back to connectionist models early in the history of artificial neural networks [30]. 

Models of replay are often concerned with its role in reinforcement learning. Although biological replay is discussed commonly in terms of episodic memory consolidation and the integration of new memory traces into long-term storage [3,16–19,29,31–37], evidence from animal studies usually comes from spatial navigation tasks in which food rewards or electrical brain stimulation are used to reinforce exploration and navigation of an environment [4,5,8,10–12,26,27,29,31–48]. The additional plasticity that replay incurs may itself reinforce habitual behaviours that are driven by the replayed activity patterns [39]. Replay of activity in the hippocampus alone is necessary for stabilising newly formed representations of the environment, ensuring that learned state transitions are maintained for subsequent visits [49,50]. In addition, the recruitment of other brain areas that are involved in evaluating likely outcomes and rewards during replay may promote further updating of stored action values or state values in neural reinforcement learning circuits [13,40,48,51]. 

These two functional roles of replay (preventing catastrophic interference and facilitating reinforcement learning) are particularly relevant for deep reinforcement learning. The fact that the use of experience replay was crucial to the first notable success of reinforcement learning with deep neural networks showed that these proposed functions of replay have application beyond the mammalian brain and extend to artificially intelligent systems [14]. In this work, an artificial neural network composed of several convolutional and fully connected layers received visual input (images from Atari 2600 computer games) while producing joystick movements to play the game. Its learning algorithm builds on classical Q-learning, which maps states (visual input) to actions (joystick output). The error generated by the Q-learning loss function is then used to train the deep neural network using the backpropagation algorithm. This process gradually 

Trends in Neurosciences, October 2021, Vol. 44, No. 10 811 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

**==> picture [350 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 DQN<br>Optimise<br>Replay buffer<br>4<br>Sample<br>3<br>1 Store (st, rt, at, st+1)<br>Action,  at 2 Reward,  rt<br>Observation,  ot+1<br>Visual inputs,  st , st+1<br>Trends in Neurosciences<br>**----- End of picture text -----**<br>


Figure 2. Deep Q network (DQN) with memory buffer. DQN with memory buffer. Top: a DQN trained to play the Atari game Boxing. At every time-step t, the DQN outputs an action corresponding to a joystick movement (1), which causes the game to produce a new reward (game score) and a new observation (pixel values; 2). The observation is transformed into a series of four visual frames that make up the state, and the tuple of state, reward, action, and subsequent state are stored in the replay buffer (3). These tuples are then sampled from the buffer and replayed to the DQN so that it optimises a function mapping state inputs to action outputs in order to maximise reward (4). Bottom: at each update, Q-values for a given pair of state s and action a from the sample are updated according to the difference between the observed value and expected value, where the observed value is the reward r from the sample added to expected future reward maxQ(s′, a′) discounted by a factor ɣ and expected value is the previous Q-value of the state-action pair. Over repeated updates, the Q-values converge on an approximation of how a state-action pair (top node) maps onto possible subsequent states (white nodes) and actions (bottom nodes). 

optimises the neuron parameters (e.g., synaptic weights) towards an optimal mapping between the state space (Atari images) and the possible actions (Figure 2). 

A necessary element of the deep Q network (DQN) is that past trials are stored in a memory buffer and regularly played back to the network. Because the incoming training data depends on the agent’s previous actions, the distribution of the training data is prone to shift as the agent’s action policy for how it behaves also shifts, leading to nonstationary data distributions. Such temporal correlations between successive online learning trials can cause a phenomenon known as catastrophic forgetting, where weight parameters undergo changes that optimise for the most recent gameplay at the cost of older gameplay; this results in behaviour learned from the previous task being rapidly overwritten by the agent’s new behaviour. Experience replay proved a crucial intervention to break temporal correlations between successive online learning trials, which stabilises learning and ultimately leads to much improved performance. 

Experience replay itself was proposed in machine learning long before the deep reinforcement breakthrough, but it was only when experience replay and deep reinforcement learning were combined that closer parallels with replay in the brain emerged [14]. It can be argued that DQNs exemplify how artificial neural networks can be used as models of biological learning to test theories of how replay can support learning. Manipulating biological replay has largely been limited to broad disruption of replay patterns [4,5,10,41,42], typically during a relatively brief period immediately following learning, which is found to diminish learning. Whereas in DQNs the consequences of manipulations such as including, excluding, or tweaking replay have been examined more comprehensively [14,52], the effects of such manipulations in biological settings have been relatively less studied. 

However, the differences between how experience replay is implemented algorithmically and how biological replay occurs physiologically merit further consideration. In the early experience replay method [14], the memory buffer consisted of past samples taken at random from the replay 

812 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

buffer. The memory buffer was set with an arbitrary capacity of the most recent one million trials; when full, the older samples in memory were replaced with new ones to maintain relatively recent training data. Several of these features of artificial experience replay (specifically the storage of exact copies of previous trials [53,54], the prioritisation of recent experience [55], uniform sampling from the memory buffer [56], and its fixed capacity [53]) have been developed further in recent years and all of them can be said to be unrepresentative of biological replay to varying degrees. In the following sections, we highlight how advances in experience replay algorithms have come closer to replicating biological replay and the implications for replay as a cognitive mechanism. 

## Prioritised experience replay 

In principle, replaying activity corresponding to past trials effectively increases the training set, by supplementing ‘live’, online experiences with additional samples. Further, manipulating the set of replayed experiences (the replay buffer) can alter the statistics of this training set to promote more efficient learning. For example, given limited time or resources, prioritising more ‘important’ samples for replay can produce faster and more efficient learning of the encoded information. Depending on what is considered important for the animal or agent, this can be achieved by biasing replay towards rarer events to overcome the under-representation of such information online, towards information that is likely to be needed in the near future [4,11,37,38,57,58], or towards the most surprising or unexpected information [46,48]. 

One approach is to select samples stored in the replay buffer by prioritising them according to the magnitude of the temporal-difference error [56]: a measure of how unexpected a transition between temporally successive states has been. This prioritised replay has also been applied to computational models in neuroscience research, showing that considering rewards while accessing memory can lead to better planning and decision making [58]. Replaying surprising information is particularly beneficial, because examples where observed outcomes diverge from predictions indicate that the predictions need improving, so there is more to be gained from updating the weights that produced the erroneous prediction. Predictive coding, based on a mental model of the environment, is a feature of neural activity in the hippocampus and elsewhere [59] and offers an efficient way of learning by correcting for errors in predictions. Dopaminergic signals, which influence plasticity in the hippocampus and other brain areas that exhibit replay, have been argued to encode reward-prediction errors during reinforcement learning [60]. This means that there is a normative case to be made for the brain to prioritise neural activity associated with errors and there are plausible neuromodulatory mechanisms by which this might be instantiated. Relatedly, it has been shown that using DQNs with replay biased by prediction errors can speed up learning [56]. 

In the biological context, prioritised experience is exemplified by the finding in rats that there is greater replay immediately following reward in a reinforcement learning task than following the absence of reward [46] or following reward that does not depend on reinforcement learning [61], suggesting a bias towards (positive) reward-prediction error. Biological prioritised experience replay is believed to rely on neuromodulatory influences in networks of neurons [62]. The association between reward and replay had been observed not only immediately after a trial during wakefulness but also during subsequent sleep; however, these findings are consistent with several possible computational roles for reward in replay [63]. More generally, replay has been found to be biased by aversive as well as rewarding outcomes [40,64], suggesting that the brain does engage in methods of prioritising some replay events over others. In addition to carefully designed experiments to tease out how replay contributes to reinforcement learning in animals [63], directly examining the effects of prioritised replay on a deep neural network can be an important proof of principle for how different replay regimes affect learning. 

Trends in Neurosciences, October 2021, Vol. 44, No. 10 813 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

Overall, this is a research area where AI, we would argue, could be a good model for biological learning, because the prediction-error theory of the midbrain dopaminergic circuit has been successful historically in explaining a wide range of experimental findings and several parts of that circuit have been implicated in replay [13,36–39]: hippocampus and prefrontal cortex for encoding states [65,66], striatum for action values [67,68], and ventral tegmental area for reward-prediction errors [69,70]. Therefore, it provides a suitable framework for integrating hypotheses about replay, reinforcement learning, dopaminergic signalling, and temporaldifference errors. 

Other reviews have covered in greater depth the suitability of deep neural networks as models of neuronal function [71–74]. There are fundamental differences between biological and artificial networks, but, in various domains, deep neural networks can be useful as abstract neural models especially for manipulations that are not easy to test biologically; for example, to model how different neural architectures and cost functions can support learning and performance. This is exemplified by convolutional neural networks and long short-term memory architectures, which have been successfully used as models for visual processing and short-term memory, respectively [75]. For replay, manipulating the rules for prioritising replay in deep neural networks can offer insight into how it supports cognitive functions. Where deep neural networks diverge from biological networks, there is an opportunity to identify the necessary elements for recreating desired features. In-depth investigation of how such differences affect information processing in both biological and artificial neural networks has the potential to reveal the key computational principles underlying learning in these systems. 

For example, it may be important to establish some quantification of phenomena such as interleaving of online and offline episodes. Quantifying replay over the course of learning in animal studies is difficult for several reasons, among which is a lack of consistency in how replay is defined, measured, and reported. However, the majority of decodable replay events immediately following an episode or trial are repetitions of the same hippocampal activity rather than replays of a different episode [45], a proportion that decreases with learning [76]. Specifically, 0.4–2 hippocampal replays of a familiar, low-reward and low-prediction-error episode per online trial have been reported [77–79], rising to 1–4 replays per online trial for higher-reward episodes [45,76,77,79] and as many as 9 replays per online trial for episodes with high reward-prediction error [77]. This compares to, for example, a mini-batch of 32 samples from the replay buffer for each online trial in a DQN [14]. Similarly, before initiating an action, the majority of decodable replay events reflect the upcoming trajectory [12,45] (but see [79]), a proportion that increases with learning [76]. 

Does this mean replays during learning are mostly massed repetitions and not interleaved? This remains to be seen. Some place cells are selective not just for spatial location but also temporal or behavioural context [45,77,78,80]; whether they differentially participate in replay events to interleave different contexts for the same spatial trajectory is not clear. In addition, what is replayed in prefrontal cortex appears to be mostly independent of what is replayed in hippocampus [81], which suggests that interleaving may happen at a higher cortical, rather than hippocampal, level. Finally, decodable replay events typically coincide with half or less of sharp-wave ripple events, which means the remaining ripples may contain undetected replays of hippocampal activity encoding other environments or tasks [47] (but see [79]). 

Biological replay continues for hours after training at a slowly decaying rate [82], so sleep or extended rest may offer an opportunity for increasingly interleaved replay of these new episodes with older ones [47]. However, what is replayed, apart from the novel experience, is largely 

814 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

unknown, because studies typically record a single task in one environment to which replayed activity can be decoded. Ambitious experiments with several environments or reinforcement learning tasks, varying in their similarity to each other and recorded over long timescales, would be beneficial for testing predictions about how replay is interleaved. 

## Memory buffer as a limitation of replay 

Uniform and prioritised experience replay have proved useful for learning individual, relatively deterministic tasks such as video games. But as the AI field becomes more ambitious in its application domains, the tasks to which models are applied become more complex and less constrained, necessitating more sophisticated solutions. One example is hindsight experience replay [83], in which the learning agent breaks down complicated goals into simpler ones by redefining its goal (target state) retrospectively when replaying past experience. This flexibility makes it easier to learn from sparse rewards and allows learning of many policies in parallel, supporting efficient learning for robotics where there are many more degrees of freedom in how an agent can interact with the physical world than a joystick-controlled video game with limited screen resolution. Even this has limitations when the tasks to be learned are too distinct from each other. 

A further limitation is that memory buffers in deep reinforcement learning are often designed to contain one million transitions, an arbitrary hyperparameter that is commonly untuned. With more complex tasks, a limited memory buffer cannot contain a representative set of samples from a very large state-space: some will fail to be stored in the memory buffer, so the network is at risk of converging on solutions that are not appropriate for these forgotten experiences. This storage issue is particularly problematic for continual learning when many tasks must be learned in sequence, which is becoming an important problem as AI progresses towards ever more complex challenges. 

One response to this challenge is to innovate ways to prioritise the samples that are stored in the memory buffer, contrasting with the simpler approach of just making the buffer bigger. Techniques have been developed to penalise, limit, or freeze weight changes in the network that were important for one task when learning a new additional task. For example, with elastic weight consolidation, the learnt connections that are important for one task but not another can be restricted to limit weight changes, ensuring that new learning is encoded by a different set of connections in the same network [84]. To some degree this resembles the largely nonoverlapping cortical neuronal representations that are enforced when successive tasks are learnt in quick succession, which has been shown to prevent interference [85], although this is not characteristic of hippocampus [86], and over longer timescales and larger spatial scales ‘representational drift’ achieves a similar effect by different mechanisms [80]. Variations of this approach mean that the replay buffer can either be abolished altogether, or used only to store a limited selection of recent samples (such as from the current task) [87–91]. 

Although these approaches prevent catastrophic forgetting, often without needing a replay buffer, they often assume a series of discrete, well-defined tasks with parameters that do not need to be updated once learned [92]. This may not be suitable for autonomous agents that face continuous, unsupervised learning in the real world. In addition, reducing the overlap between representations of different tasks in the network disregards the potential benefits of transfer learning, in which shared representations can speed up learning on new, similar tasks. 

How can replay be used to support continual learning? To some extent, maintaining the memory buffer as a representative sample of tasks past and present can mitigate catastrophic forgetting [55], but eventually the trade-off remains between a large computationally costly memory buffer and remembering insufficient samples. Another ethical consideration is that explicitly storing training 

Trends in Neurosciences, October 2021, Vol. 44, No. 10 815 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

data may also violate privacy for some applications. Given that the mammalian brain achieves both continual learning and transfer learning with ease despite limits on resources, again neuroscience has major potential to offer inspiration for solving this problem: converging new evidence suggests that the hippocampus is capable of generating its own samples to train from. 

## Generative replay 

Brains are not structured in a way that separates the processing network away from the learning network that stores exact copies of past trials. Moreover, neuronal firing in brains is inherently stochastic. The result is that no two patterns of activity, either the original online activity encoding the novel experience, or any subsequent replay, are exactly the same. In the context of spatial navigation, sequences of activity during replay events can reflect random walks through the cognitive map [93], encoding paths through the environment that have never been observed directly by an animal, including reverse trajectories in a one-way system, shortcuts, and blocked-off paths that were seen but not taken [94,95] (Figure 3). One can interpret this as if the hippocampus generates its own samples (its own training data) from a minimal stored model. 

**==> picture [359 x 282] intentionally omitted <==**

**Trends in Neurosciences** 

Figure 3. Biological and artificial generative replay. (A) Hippocampal replay sequences have been found to reflect paths through the environment never taken by the animal, as demonstrated by decoding of locations during a replay event along the top of the maze when the animal had only explored it in a figure-of-eight pattern. Bottom: spiking of hippocampal cells that have place fields on the left and right loops of the maze, respectively, during a replay event. Top: decoded position during replay event. Colour indicates temporal order in the replay sequence. (B) Images generated by a generative adversarial network trained to reproduce handwritten MNIST digits and Street View House Numbers, instead of explicitly storing copies of such images in a memory buffer as in standard experience replay. Sample examples from early (top) and later in training (bottom) are shown; as training progresses, the samples produced by the generator increasingly resemble real images and are increasingly recognisable as numbers. Panels (A) and (B) adapted from [53,94], respectively. 

816 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

Deep neural networks can generate their own samples too, although so far this has been achieved primarily in supervised classification tasks with relatively simple datasets and with minimal applications for reinforcement learning. Typically, a generative adversarial network, autoencoder, or restricted Boltzmann machine is trained to generate data with the same parameter distributions as incoming data. The generated data is then replayed to the (main) solver model, so that even as new tasks are learned, the cumulative input distribution of all previous tasks continue to be replayed with minimal storage burden. 

This approach has been shown to work well for classifying the MNIST database of handwritten digits learnt in sequence without succumbing to catastrophic forgetting [53] (Figure 3). So far, implementations of generative replay usually train a separate network for each task, assuming well-isolated tasks. The challenge for efficient deep generative replay is training a generator that is flexible enough to be scalable to many tasks and complex inputs. 

Future research on this topic could, in principle, apply generative replay to a broader range of reinforcement learning tasks and extend it as a model of biological replay. Hippocampal replay is influenced by neuromodulation both at the time of encoding and during replay [96], which could serve to bias the generative mechanism towards goal states or high-error transitions, or otherwise alter the parameters of the generated samples in a way that enhances reinforcement learning. There is also evidence of a bidirectional process whereby cortical activity can prompt or select replay patterns in hippocampus [8,44,97], in addition to the hippocampus replaying information to the cortex and other brain areas. These are underexplored in modelling hippocampal replay and may also serve to improve the performance of deep generative replay for more complex tasks. There are many ways in which replayed information need not reflect online updates: lowdimensional representations, top-down influences, biasing towards salient information, and different update or plasticity rules could all be used to improve replay algorithms. For example, work on deep generative replay suggests that freezing weights in initial layers of the network and replaying low-dimensional information may reduce the computational burden [54]. An improved understanding of how replay patterns propagate through cortical and subcortical networks may inspire further refinements to this approach. 

Finally, the additional flexibility that comes with generative replay may offer other benefits: one example of nonstereotyped replay is that hidden structures can be inferred from information presented in a disjointed way. This pertains not only to finding shortcuts in spatial environments [94], but, more abstractly, to replaying sequences of images in the appropriate order [9]. Inferring hidden structures from segmented experience may not be possible with an explicit memory buffer, but such forms of biologically inspired replay might allow deep neural networks to gain more insight from their training than current methods can support. A possible role for replay in transfer learning, in which knowledge of past tasks is leveraged to improve learning on new tasks, is yet to be investigated in either neuroscience or machine learning, but may offer both improved algorithms and better insight into cognitive processes. 

## Future directions 

Recent experimental innovations allow recording of broader areas of the brain over longer timescales to capture more neural data [9,80,97]. This richer data offers possibilities for exploring how replay spreads throughout the brain [8,81] and over time [47,53,82], but will need strong theory to guide the boundless possibilities for analysis. Meanwhile, reinforcement learning in AI is increasingly taking advantage of more complex and brain-inspired representations of the world to meet the challenges of complex, noisy, and nonstationary applications, including hierarchies of learners [98] and distributions of values [99]. Increasingly sophisticated task designs in 

Trends in Neurosciences, October 2021, Vol. 44, No. 10 817 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

experimental neuroscience may advance current understanding of replay of inferred structure [9], generalisations [81], interleaved episodes [47], and other ways of organising information to support complex cognition. In turn, these biological insights could help improve the use of past samples in machine learning to support transfer, continual and hierarchical reinforcement learning. While this recent focus on increasing the quantity of data is valuable, understanding the role of replay in complex cognitive processes will require more sophisticated and carefully designed behavioural tasks than are now available. 

Other developments include encoding states of the world as successor representations [100], a computational structure that represents states in terms of where they might lead to (i.e., expected occupancies of future states). Successor representations make learning more efficient, generalise better in multitask settings [101], and can be used as a model of hippocampal place cells [59]. Replaying the successor representations themselves, rather than pixel observations as is typical in experience replay [14], could further support learning in complex settings, not only improving machine learning algorithms but also shedding light on the function of hippocampal replay. 

Beyond gaining insights into optimisation of cognitive processes, closer integration of research on replay for reinforcement learning in AI and neuroscience could lead to new avenues for understanding disease aetiology and symptoms. Reinforcement learning is altered, for instance, in patients with Parkinson’s disease and schizophrenia (conditions that are characterised by altered dopamine levels), both during learning itself and in the consolidation period of hours or days afterwards [102,103]. Future models of replay for reinforcement learning that explicitly relate to the various neural circuits affected by such conditions may help to explain how they give rise to the associated cognitive changes. 

## Concluding remarks 

Deep neural networks and brains are examples of artificial and natural intelligent systems that solve computationally related problems involving reinforcement learning in complex environments. Despite significant fundamental differences between biological and artificial networks, replay appears to reflect convergence on comparable mechanisms: both biologically and artificially intelligent systems harness replay of past experience to stabilise, consolidate, generalise from, and accelerate learning. In neuroscience, questions remain about how replay is initiated and propagated through cortical and subcortical networks and what influence this has on learning. By addressing these problems in simulated and real-world settings, computational models can play important roles in making testable predictions of how the brain solves these problems (see Outstanding questions). Deep neural networks are an example of such a computational model that underlie complex applications of AI in computer vision and other domains while also being biologically plausible in some aspects, making them invaluable for manipulating aspects of replay that are difficult to control experimentally to reveal how it supports learning and memory processes. In particular, experimental studies are restricted to learning and memory processes that take place over timescales of seconds to weeks; therefore, hypotheses about lifelong learning may be more easily developed and tested in deep neural networks. Conversely, as research on replay throughout the brain develops, it may hold keys to solving some of the biggest challenges in AI today, including continual learning where algorithms fall short of what brains can do with ease [104]. A more ambitious long-term goal for AI, with prospects of its feasibility being debated, is the design of an artificial general intelligence that can tackle virtually any task in the grasp of humans. 

## Outstanding questions 

To what extent does replay reflect individual episodes versus aggregated statistics in the brain and how does the replay of individual versus generalised information support learning and consolidation in both biology and AI? 

Replay in deep reinforcement learning often starts at the input layer and propagates to higher layers; in the mammalian brain it is unclear how different brain areas interact during replay events. Can replay originate in lower layers (corresponding to sensory cortices, in brains), higher layers (hippocampus, prefrontal cortex), and output layers (striatum)? How does it propagate through the network and what influence does this have on learning? 

How does replay of newer versus older information, and overlapping versus distinct representations, support learning and consolidation? 

How can replay of similar information benefit transfer learning? 

Are the update rules different for online experience versus replay? Are the update rules different for replay during wake versus sleep and replay during rapid eye movement (REM) versus non-REM sleep? 

How can generative replay be used to support continual learning of complex tasks? 

## Acknowledgements 

This research was funded in part by a Wellcome Senior Research Fellowship in Basic Biomedical Science (grant number 202810/Z/16/Z to M.W.J.), a Wellcome PhD studentship (grant number 109070/Z/15/A to E.R.), a Leverhulme Trust 

818 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

Research Leadership Award (grant number RL-2016-39 to N.L.). R.C. was supported by Unifying Neuroscience and Artificial Intelligence - Québec (UNIQUE), Fonds de recherche du Québec (FRQNT), and Natural Sciences and Engineering Research Council of Canada (NSERC). For the purpose of Open Access, the authors have applied a CC BY public copyright licence to any Author Accepted Manuscript version arising from this submission. 

## Declaration of interests 

The authors declare no competing interests in relation to this work. 

## References 

|1.|Sutton, R.S. and Barto, A.G. (1998) Introduction to Reinforcement|25.|Colgin, L.L. et al. (2004) Long-term potentiation is impaired in|
|---|---|---|---|
||Learning The MIT Press||rat hippocampal slices that produce spontaneous sharp|
|2.|Lin, L.-J. (1992) Self-improving reactive agents based on rein-||waves.J. Physiol.558, 953–961|
||forcement learning, planning and teaching. Mach. Learn. 8,|26.|Nádasdy, Z.et al. (1999) Replay and time compression of re-|
||293–4, pp. 293–321||curring spike sequences in the hippocampus. J. Neurosci.|
|3.|Ólafsdóttir, H.F.et al.(2018) The role of hippocampal replay in||19, 9497–9507|
||memory and planning.Curr. Biol.28, R37–R50|27.|Lee, A.K. and Wilson, M.A. (2002) Memory of sequential expe-|
|4.|Michon, F. et al. (2019) Post-learning hippocampal replay se-||rience in the hippocampus during slow wave sleep.Neuron36,|
||lectively reinforces spatial memory for highly rewarded loca-||1183–1194|
||tions.Curr. Biol.29, 1436–1444|28.|Yoshida, M. et al. (2012) Cholinergic modulation of the CAN|
|5.|Fernández-Ruiz, A. et al. (2019) Long-duration hippocampal||current may adjust neural dynamics for active memory mainte-|
||sharp wave ripples improve memory.Science364, 1082–1086||nance, spatial navigation and time-compressed replay. Front.|
|6.|Rasch, B. et al. (2007) Odor cues during slow-wave sleep||Neural Circuits6, 10|
||prompt declarative memory consolidation. Science 315,|29.|Wilson, M.A. and McNaughton, B.L. (1993) Dynamics of the|
||1426–1429||hippocampal ensemble code for space. Science 261,|
|7.|Barnes, D.C. and Wilson, D.A. (2014) Slow-wave sleep-im-||1055–1058|
||posed replay modulates both strength and precision of mem-|30.|McCloskey, M. and Cohen, N.J. (1989) Catastrophic interfer-|
||ory.J. Neurosci.34, 5134–5142||ence in connectionist networks: the sequential learning prob-|
|8.|Rothschild, G. et al. (2017) A cortical-hippocampal-cortical||lem.Psychol. Learn. Motiv. Adv. Res. Theory 24, 109–165|
||loop of information processing during memory consolidation.|31.|Wilson, M.A. and McNaughton, B.L. (1994) Reactivation of hip-|
||Nat. Neurosci.20, 251–259||pocampal ensemble memories during sleep. Science 265,|
|9.|Liu, Y. et al. (2019) Human replay spontaneously reorganizes||676–679|
||experience.Cell178, 640–652|32.|Skaggs, W.E. and McNaughton, B.L. (1996) Replay of neuro-|
|10.|Jadhav, S.P.et al.(2012) Awake hippocampal sharp-wave rip-||nalfring sequences in rat hippocampus during sleep following|
||ples support spatial memory.Science336, 1454–1458||spatial experience.Science271, 1870–1873|
|11.|Carey, A.A.et al.(2019) Reward revaluation biases hippocam-|33.|Kudrimoti, H.S. et al. (1999) Reactivation of hippocampal cell|
||pal replay content away from the preferred outcome. Nat.||assemblies: effects of behavioral state, experience, and EEG|
||Neurosci.22, 1450–1459||dynamics.J. Neurosci.19, 4090–4101|
|12.|Ólafsdóttir, H.F.et al.(2017) Task demands predict a dynamic|34.|Qin, Y.-L.et al. (1997) Memory reprocessing in corticocortical|
||switch in the content of awake hippocampal replay.Neuron96,||and hippocampocortical neuronal ensembles. Philos. Trans.|
||925–935||R. Soc. B Biol. Sci.352, 1525–1533|
|13.|Momennejad, I.et al.(2018) Offine replay supports planning in|35.|Ji, D. and Wilson, M.A. (2007) Coordinated memory replay in|
||human reinforcement learning.Elife7, e32548||the visual cortex and hippocampus during sleep. Nat.|
|14.|Mnih, V. et al. (2015) Human-level control through deep rein-||Neurosci.10, 100–107|
||forcement learning.Nature518, 529–533|36.|Euston, D.R. et al. (2007) Fast-forward playback of recent|
|15.|Silver, D. et al. (2016) Mastering the game of Go with||memory sequences in prefrontal cortex during sleep.Science|
||deep neural networks and tree search. Nature 529,||318, 1147–1150|
||484–489|37.|Peyrache, A.et al.(2009) Replay of rule-learning related neural|
|16.|Joo, H.R. and Frank, L.M. (2018) The hippocampal sharp||patterns in the prefrontal cortex during sleep. Nat. Neurosci.|
||wave–ripple in memory retrieval for immediate use and con-||12, 919–926|
||solidation.Nat. Rev. Neurosci.19, 744–757|38.|Pennartz, C.M.A. et al. (2004) The ventral striatum in off-|
|17.|Foster, D.J. (2017) Replay comes of age.Annu. Rev. Neurosci.||line processing: ensemble reactivation during sleep and|
||40, 581–602||modulation by hippocampal ripples. J. Neurosci. 24,|
|18.|Rothschild, G. (2019) The transformation of multi-sensory ex-||6446–6456|
||periences into memories during sleep. Neurobiol. Learn.|39.|Gomperts, S.N.et al.(2015) VTA neurons coordinate with the|
||Mem.160, 58–66||hippocampal reactivation of spatial experience. Elife 4,|
|19.|Pfeiffer, B.E. (2020) The content of hippocampal ‘replay.||321–352|
||Hippocampus30, 6–18|40.|Girardeau, G. et al.(2017) Reactivations of emotional memory|
|20.|Stickgold, R. (2005) Sleep-dependent memory consolidation.||in the hippocampus–amygdala system during sleep. Nat.|
||Nature437, 1272–1278||Neurosci.20, 1634–1642|
|21.|Sadowski, J.H.L.P. et al. (2016) Sharp-wave ripples orches-|41.|Girardeau, G. et al. (2009) Selective suppression of hippo-|
||trate the induction of synaptic plasticity during reactivation of||campal ripples impairs spatial memory. Nat. Neurosci. 12,|
||place cell fring patterns in the hippocampus. Cell Rep. 14,||1222–1223|
||1916–1929|42.|Ego-Stengel, V. and Wilson, M.A. (2010) Disruption of ripple-|
|22.|Behrens, C.J.et al.(2005) Induction of sharp wave–ripple com-||associated hippocampal activity during rest impairs spatial|
||plexes in vitro and reorganization of hippocampal networks.||learning in the rat.Hippocampus20, 1–10|
||Nat. Neurosci.8, 1560–1567|43.|Gridchyn, I.et al.(2020) Assembly-specifc disruption of hippo-|
|23.|Norimoto, H.et al.(2018) Hippocampal ripples down-regulate||campal replay leads to selective memory defcit. Neuron 106,|
||synapses.Science359, 1524–1527||291–300|
|24.|Lubenov, E.V. and Siapas, A.G. (2008) Decoupling through|44.|Bendor, D. and Wilson, M.A. (2012) Biasing the content of|
||synchrony in neuronal circuits with propagation delays.Neuron||hippocampal replay during sleep. Nat. Neurosci. 15,|
||58, 118–131||1439–1444|



Trends in Neurosciences, October 2021, Vol. 44, No. 10 819 

Trends in Neurosciences 

**==> picture [121 x 36] intentionally omitted <==**

|45.|Xu, H. et al. (2019) Assembly responses of hippocampal CA1|72.|Richards, B.A.et al.(2019) A deep learning framework for neu-|
|---|---|---|---|
||place cells predict learned behavior in goal-directed spatial||roscience. Nat. Neurosci.22, 1761–1770|
||tasks on the radial eight-arm maze.Neuron 101, 119–132|73.|Saxe, A.et al.(2021) If deep learning is the answer, what is the|
|46.|Singer, A.C. and Frank, L.M. (2009) Rewarded outcomes en-||question?Nat. Rev. Neurosci.22, 55–67|
||hance reactivation of experience in the hippocampus. Neuron|74.|Cichy, R.M. and Kaiser, D. (2019) Deep neural networks as sci-|
||64, 910–921||entifc models.Trends Cogn. Sci.23, 305–317|
|47.|Karlsson, M.P. and Frank, L.M. (2009) Awake replay of remote|75.|Hassabis, D.et al.(2017) Neuroscience-inspired artifcial intelli-|
||experiences in the hippocampus.Nat. Neurosci.12, 913–918||gence.Neuron 95, 245–258|
|48.|Lansink, C.S. et al. (2008) Preferential reactivation of motiva-|76.|Shin, J.D. et al. (2019) Dynamics of awake hippocampal-pre-|
||tionally<br>relevant<br>information<br>in<br>the<br>ventral<br>striatum.||frontal replay for spatial learning and memory-guided decision|
||J. Neurosci.28, 6372–6382||making.Neuron104, 1110–1125|
|49.|van de Ven, G.M.et al.(2016) Hippocampal offine reactivation|77.|Igata, H.et al.(2021) Prioritized experience replays on a hippo-|
||consolidates recently formed cell assembly patterns during||campal predictive map for learning.Proc. Natl. Acad. Sci. U. S.|
||sharp wave-ripples.Neuron92, 968–974||A.118, 1|
|50.|Roux, L.et al.(2017) Sharp wave ripples during learning sta-|78.|Bhattarai, B.et al.(2020) Distinct effects of reward and naviga-|
||bilize the hippocampal spatial map. Nat. Neurosci. 20,||tion history on hippocampal forward and reverse replays.Proc.|
||845–853||Natl. Acad. Sci. U. S. A.117, 689–697|
|51.|Gershman, S.J. et al. (2014) Retrospective revaluation in se-|79.|Gillespie, A.K.et al.(2021) Hippocampal replay refects specifc|
||quential decision making: a tale of two systems. J. Exp.||past experiences rather than a plan for subsequent choice.|
||Psychol. Gen.143, 182–194||bioRxiv Published online March 24, 2021. https://doi.org/|
|52.|Fedus, W. et al. (2020) Revisiting fundamentals of experience||10.1101/2021.03.09.434621|
||replay. In Proc. 37th Int. Conf. Mach. Learn. Proc. Mach.|80.|Ziv, Y. et al.(2013) Long-term dynamics of CA1 hippocampal|
||Learn. Res(119), pp. 3061–3071||place codes.Nat. Neurosci.16, 264–266|
|53.|Lee, J.K.et al.(2017) Continual learning with deep generative|81.|Kaefer, K. et al. (2020) Replay of behavioral sequences in the|
||replay. In 31st Conference on Neural Information Processing||medial prefrontal cortex during rule switching. Neuron 106,|
||Systems (NIPS 2017), pp. 2990–2999||154–165|
|54.|van de Ven, G.M.et al.(2020) Brain-inspired replay for contin-|82.|Giri, B.et al.(2019) Hippocampal reactivation extends for sev-|
||ual learning with artifcial neural networks. Nat. Commun. 11,||eral hours following novel experience. J. Neurosci. 39,|
||4069||866–875|
|55.|Isele, D. and Cosgun, A. (2018) Selective experience replay for|83.|Andrychowicz, M.et al.(2017) Hindsight experience replay. In|
||lifelong learning. In32nd AAAI Conference on Artifcial Intelligence||31st Conference on Neural Information Processing Systems|
||AAAI 2018, pp. 3302–3309|84.|Kirkpatrick, J.et al.(2017) Overcoming catastrophic forgetting|
|56.|Schaul, T. et al. (2016) Prioritized experience replay. In 4th||in neural networks. Proc. Natl. Acad. Sci. U. S. A. 114,|
||International Conference on Learning Representations||3521–3526|
||ICLR 2016|85.|Cichon, J. and Gan, W.B. (2015) Branch-specifc dendritic Ca2|
|57.|McClelland, J.L. et al. (1995) Why there are complementary||+ spikes cause persistent synaptic plasticity. Nature 520,|
||learning systems in the hippocampus and neocortex: insights||180–185|
||from the successes and failures of connectionist models of|86.|Gava, G.P. et al. (2021) Integrating new memories into the|
||learning and memory.Psychol. Rev.102, 419–457||hippocampal network activity space. Nat. Neurosci. 24,|
|58.|Mattar, M.G. and Daw, N.D. (2018) Prioritized memory access||326–330|
||explains planning and hippocampal replay.Nat. Neurosci.21,|87.|Li, Z. and Hoiem, D. (2018) Learning without forgetting. IEEE|
||1609–1617||Trans. Pattern Anal. Mach. Intell.40, 2935–2947|
|59.|Stachenfeld, K.L. et al. (2017) The hippocampus as a predic-|88.|Zenke, F.et al.(2017) Continual learning through synaptic intel-|
||tive map.Nat. Neurosci.20, 1643–1653||ligence. In34th International Conference on Machine Learning,|
|60.|Watabe-Uchida, M.et al.(2017) Neural circuitry of reward pre-||ICML 2017(Vol. 8), pp. 6072–6082|
||diction error.Annu. Rev. Neurosci.40, 373–394|89.|Masse, N.Y. et al. (2018) Alleviating catastrophic forgetting|
|61.|Dupret, D. et al. (2010) The reorganization and reactivation of||using context dependent gating and synaptic stabilization.|
||hippocampal maps predict spatial memory performance. Nat.||Proc. Natl. Acad. Sci. U. S. A.115, E104657–E104675|
||Neurosci.13, 995–1002|90.|Rusu, A.A. et al. (2016) Progressive neural networks. arXiv|
|62.|de Lavilléon, G. et al. (2015) Explicit memory creation during||1606.04671|
||sleep demonstrates a causal role of place cells in navigation.|91.|Schwarz, J. et al. (2018) Progress & compress: a scalable|
||Nat. Neurosci.18, 493–495||framework for continual learning. In35th International Confer-|
|63.|Roscow, E.et al.(2019) Behavioural and computational evidence||ence on Machine Learning ICML 2018(Vol. 10), pp. 7199–7208|
||for memory consolidation biased by reward-prediction errors.|92.|Parisi, G.I. et al. (2019) Continual lifelong learning with neural|
||bioRxiv Published online July 26, 2019. https://doi.org/||networks: a review.Neural Netw.113, 54–71|
||10.1101/716290|93.|Stella, F.et al.(2019) Hippocampal reactivation of random tra-|
|64.|Wu, C.-T.et al.(2017) Hippocampal awake replay in fear mem-||jectories resembling Brownian diffusion.Neuron102, 450–461|
||ory retrieval.Nat. Neurosci.20, 571–580|94.|Gupta, A.S. et al. (2010) Hippocampal replay is not a simple|
|65.|Wilson, R.C. et al. (2014) Orbitofrontal cortex as a cognitive||function of experience.Neuron65, 695–705|
||map of task space.Neuron81, 267–279|95.|Ólafsdóttir, H.F. et al. (2015) Hippocampal place cells con-|
|66.|Wikenheiser, A.M. and Schoenbaum, G. (2016) Over the river,||struct reward related sequences through unexplored space.|
||through the woods: cognitive maps in the hippocampus and||Elife4, e06063|
||orbitofrontal cortex.Nat. Rev. Neurosci.17, 513–523|96.|Atherton, L.A.et al.(2015) Memory trace replay: the shaping of|
|67.|Samejima, K.et al.(2005) Representation of action-specifc re-||memory consolidation by neuromodulation. Trends Neurosci.|
||ward values in the striatum.Science310, 1337–1340||38, 560–570|
|68.|Lau, B. and Glimcher, P.W. (2008) Value representations in the|97.|Abadchi, J.K.et al.(2020) Spatiotemporal patterns of neocor-|
||primate striatum during matching behavior. Neuron 58,||tical activity around hippocampal sharp-wave ripples. Elife 9,|
||451–463||e51972|
|69.|Schultz, W. (1998) Predictive reward signal of dopamine neu-|98.|Wang, J.X.et al.(2018) Prefrontal cortex as a meta-reinforce-|
||rons.J. Neurophysiol.80, 1–27||ment learning system.Nat. Neurosci.21, 860–868|
|70.|O’Doherty, J.P. et al. (2003) Temporal difference models and|99.|Dabney, W.et al.(2020) A distributional code for value in dopa-|
||reward-related learning in the human brain. Neuron 38,||mine-based reinforcement learning.Nature577, 671–675|
||329–337|100.|Dayan, P. (1993) Improving generalization for temporal differ-|
|71.|Marblestone, A.H. et al.(2016) Toward an integration of deep||ence learning: the successor representation. Neural Comput.|
||learning and neuroscience.Front. Comput. Neurosci.10, 94||5, 613–624|



820 Trends in Neurosciences, October 2021, Vol. 44, No. 10 

## Trends in Neurosciences 

**==> picture [44 x 36] intentionally omitted <==**

101. Barreto, A. et al. (2020) Fast reinforcement learning with gener111. Schapiro, A.C. et al. (2018) Human hippocampal replay during alized policy updates. Proc. Natl. Acad. Sci. U. S. A. 117, rest prioritizes weakly learned information and predicts memory 30079–30087 performance. Nat. Commun. 9, 3920 

102. Grogan, J.P. et al. (2017) Effects of dopamine on reinforcement 112. Schuck, N.W. and Niv, Y. (2019) Sequential replay of nonlearning and consolidation in Parkinson’s disease. Elife 6, spatial task states in the human hippocampus. Science e26801 364, 6447 

103. Culbreth, A.J. et al. (2021) Retention of value representations across 113. Buzsáki, G. et al. (1992) High-frequency network oscillation in time in people with schizophrenia and healthy control subjects. Biol. the hippocampus. Science 256, 1025–1027 Psychiatry Cogn. Neurosci. Neuroimaging 6, 420–428 114. Tse, D. et al. (2007) Schemas and memory consolidation. 

104. Hadsell, R. et al. (2020) Embracing change: continual learning Science 316, 76–82 in deep neural networks. Trends Cogn. Sci. 24, 1028–1040 115. Cook, Z. et al. (2013) Exploration versus exploitation in 

105. Lin, L.-J. (1991) Programming robots using reinforcement polydomous ant colonies. J. Theor. Biol. 323, 49–56 learning and teaching. In Proceedings of the Ninth National 116. Antony, J.W. and Paller, K.A. (2017) Hippocampal contribuConference on Artificial Intelligence, pp. 781–786 tions to declarative memory consolidation during sleep. In 

106. O’Keefe, J. and Dostrovsky, J. (1971) The hippocampus as a The Hippocampus from Cells to Systems: Structure, Connecspatial map. Preliminary evidence from unit activity in the tivity, and Functional Contributions to Memory and Flexible freely-moving rat. Brain Res. 34, 171–175 Cognition (Hannula, D.E. and Duff, M.C., eds), pp. 245–280, 

107. Marr, D. (1971) Simple memory: a theory for archicortex. Springer International Publishing Philos. Trans. R. Soc. Lond. B 262, 23–81 117. Schapiro, A.C. et al. (2017) Complementary learning systems 

108. Pavlides, C. and Winson, J. (1989) Influences of hippocamwithin the hippocampus: a neural network modelling approach pal place cell firing in the awake state on the activity of to reconciling episodic memory with statistical learning. Philos. these cells during subsequent sleep episodes. J. Neurosci. Trans. R. Soc. B Biol. Sci. 372, 20160049 9, 2907–2918 118. McClelland, J.L. et al. (2020) Integration of new information 

109. Gruber, M.J. et al. (2016) Post-learning hippocampal dynamics in memory: new insights from a complementary learning promote preferential retention of rewarding events. Neuron 89, systems perspective. Philos. Trans. R. Soc. B Biol. Sci. 1110–1120 375, 1799 

110. Murty, V.P. et al. (2017) Selectivity in postencoding connectivity 119. Carr, M.F. et al. (2011) Hippocampal replay in the awake state: with high-level visual cortex is associated with reward-motia potential substrate for memory consolidation and retrieval. vated memory. J. Neurosci. 37, 537–545 Nat. Neurosci. 14, 147–153 

Trends in Neurosciences, October 2021, Vol. 44, No. 10 821 

