## **Disentangling the component processes in complex planning impairments following ventromedial prefrontal lesions** 

Eleanor Holton[1*] , Bas van Opheusden[2] , Jan Grohn[1] , Harry Ward[3] , John Grogan[4] , Patricia L Lockwood[5] , Ili Ma[6,7] , Wei Ji Ma[8] , Sanjay G Manohar[1 ] 

*For correspondence: eleanor.holton@psy.ox.ac.uk 

1University of Oxford, Oxford, UK; 2Imbue, Inc., San Francisco, CA, USA; 3Queen Mary University London, London, UK;[4] Trinity College, Dublin, Ireland;[5] University of Birmingham, Birmingham, UK;[6] Leiden University, Leiden, the Netherlands;[7] Leiden Institute for Brain and Cognition, Leiden, The Netherlands;[8] New York University, New York, NY, USA 

## **Abstract** 

Damage to ventromedial prefrontal cortex (vmPFC) in humans disrupts planning abilities in naturalistic settings. However, it is unknown which components of planning are affected in these patients, including selecting the relevant information, simulating future states, or evaluating between these states. To address this question, patients with damage to vmPFC, control lesion patients, and healthy age-matched controls played Four-in-a-Row, a board game of medium planning complexity. Damage to vmPFC disrupted performance in this task compared to both control groups. We then leveraged a computational framework to assess different component processes of planning. Impairments following vmPFC damage included shallower planning depth, and a tendency to overlook game-relevant features. In a simpler planning setting involving binary choices across a short future horizon (‘Two-Step Task’), we found little evidence of planning in all groups, and no behavioural differences between groups. Taken together, these results suggest that planning impairments following vmPFC lesions are apparent in more complex state spaces, and associated with a tendency to overlook relevant information and plan less deeply into the future. 

## **Introduction** 

Damage to the ventromedial prefrontal cortex (vmPFC) has life-altering effects for patients, often leading to devastating consequences for employment, relationships, and general lifestyle (Harlow, 1868; Burgess 2000; Schneider & Koenigs, 2017). Despite this, pinpointing the precise cognitive deficits causing these real-world problems has proved a challenging research question (Eslinger and Damasio 1985; Shallice and Burgess 1991; Tranel et al. 2007). A resounding message from decades of frontal lesion research is the need for planning tasks that deliver the complexity necessary to reveal subtle behavioural alterations, while still allowing researchers to discriminate between specific cognitive functions supporting task performance (Burgess 2000, Schneider & Koenigs, 2017, Yu et al. 2020). 

VmPFC damage disrupts tasks that broadly test future planning or sequential decisionmaking. These include the Multiple Errands task, where vmPFC patients struggle to structure decisions across a sequence of real-world errands in a shopping mall (Shallice & Burgess, 1991, Tranel et al. 2007), and the Tower of London task (Owen et al. 1990). In other simple 

1 

laboratory tasks, neural correlates of stepwise planning have been observed in orbitofrontal cortex (Rowe et al. 2001, Jones et al. 2012, Wilson et al. 2014, Kaplan et al. 2015, Schuck et al. 2016, Chan et al. 2016, Basu et al. 2021, Wimmer & Büchel 2019, Costa et al. 2022). However, real-world planning is a composite ability relying on separable cognitive components, which these tasks are not designed to tease apart. 

Some studies have proposed that vmPFC damage causes specific impairments in imagining or simulating the future. For example, patients struggle to imagine events in the distant future (Fellows and Farah, 2005), and produce less detail about imagined future events (Bertossi et al., 2015, Bertossi et al., 2016, Bertossi et al., 2017). On the other hand, other studies have emphasised the role of vmPFC in evaluation, particularly when choices require integrating multiple attributes of value or involve multiple options (Bartra et al. 2013; Levy and Glimcher 2011; Pelletier and Fellows 2021; Vaidya et al. 2018; Bowren et al. 2018; Noonan et al. 2017). New task paradigms are required to determine whether vmPFC is necessary for all computations involved in planning or whether specific aspects of planning are impaired, such as imagining the future, evaluating between states, or selecting the relevant information. 

In computational terms, planning involves using a model of the world to guide choices through simulation of possible future states of the world. This process of imagining future trajectories can be operationalised as a decision tree, where each decision is a branching point leading to alternative futures (Newell et al. 1959, Mattar & Lengyel, 2022, Botvinick et al. 2009, Keramati et al. 2011, Otto et al. 2013, Huys et al. 2015, Sezener et al. 2019, Callaway et al. 2022). In the real world, the branching of decision trees leads to rapid growth of options and makes full simulation of all possible future states intractable. To solve this problem, work in artificial intelligence utilizes heuristics for search that combine simulation of selected branches with simplified value estimations of future states or actions (Shannon, 1950, Pearl, 1984, Russell & Norvig, 2016, Mnih et al. 2013, Geffner, 2013, Silver et al. 2016, 2017). 

The ‘Four-in-a-Row’ task was developed to disentangle these distinct computational components of human planning in a complex state space (van Opheusden et al. 2023, Ma et al. 2022). Human behaviour in the task can be reasonably well modelled by a planning algorithm that separates exploration of future states using a tree search algorithm, and evaluation of the states using feature-based heuristics. By separating these distinct elements of planning, the task can quantify how far people search into the future (‘depth’), their knowledge of good heuristics for evaluating states (‘heuristic quality’), and their tendency to overlook relevant features (‘feature drop’). Our first aim was to determine whether vmPFC lesion patients show impairments in this complex planning task, and if so, to identify the components contributing to the deficit. 

Our second aim was to determine whether vmPFC planning deficits depend on the complexity of the task or reflect a more general impairment in using an internal model of the world to guide choice. To investigate this ability in patients with vmPFC damage, we examined behaviour in a simpler task which measures peoples’ capacity to make decisions using a model of the environment, namely the Two-Step Task (Daw et al. 2011). 

We conducted both tasks in vmPFC lesion patients, lesion control patients, and an agematched control sample. We first asked whether vmPFC patients performed worse than controls at Four-in-a-Row, the more complex planning task. We then used computational modelling to assess differences between the groups in the underlying component processes of 

2 

complex planning. Finally, we asked whether the groups differed in performance and modelbased decision making in the simpler Two-Step Task setting. 

## **Materials and Methods** 

## **Participants** 

We studied planning behaviour in three populations: lesion patients with damage to vmPFC (vmPFC), control lesion patients with damage outside vmPFC (lesion controls; LCs), and healthy age-matched control participants (healthy controls; HCs). In Study 1, a total of 18 lesion patients (mean age=59) and 30 HC participants (mean age=58) completed the Four-ina-Row Task. In Study 2, a total of 50 lesion patients (mean age=58) and 20 HC participants (mean age=68) completed the Two-Step Task; 1 patient was excluded because they dropped out of Study 2, leaving a total of 49 lesion patients. Data collection for Study 2 was collected prior to data collection for Study 1. In both studies, we recruited lesion patients from a database of individuals who had previously visited the John Radcliffe Hospital and consented to be contacted for research studies. Ethical approval was obtained by the London Fullham Research Ethics Committee (IRAS project number: 242551; REC Reference number: 18/LO/2152). All participants gave informed consent before the experiment. Participants were compensated for their time at a rate of £10/hour. 

A neurologist (SGM) manually registered brain lesions prior to study recruitment. The Harvard-Oxford Cortical Structural Atlas (RRID:SCR_001476) (Kennedy et al., 1998; Makris et al., 1999) as distributed with FSL (FMRIB Software Library) (Jenkinson et al., 2012) was used to allocate participants to the vmPFC group or LC group, using the binarized mask of frontal medial cortex for vmPFC classification (threshold > 0, **Fig.1a** ). Individuals who had damage within the mask were assigned to the vmPFC group (Study 1 vmPFC group: _N_ =10; **Fig.1b** , _left;_ Study 2 vmPFC group: _N_ =30; **Fig.1c** , _left_ ), while those for whom the vmPFC was spared were assigned to the LC group (Study 1 LC group: _N_ =8; **Fig.1b** , _right;_ Study 2 LC group: _N_ =19, **Fig.1c** , _right_ ). The vmPFC lesions were highly focal (median volume: 8.5 cm[3] in Study 1; 14.5 cm[3 ] in Study 2). In Study 1 (where vmPFC damage was found to affect behaviour), 3 vmPFC patients also had damage in ventral striatum or dorsomedial PFC (individual maps displayed in **Fig. S1** ). 

**==> picture [509 x 182] intentionally omitted <==**

3 

**Figure 1** . **Lesion Maps. (a)** Anatomical vmPFC mask from the Harvard-Oxford Cortical Structural Atlas (RRID:SCR_001476) (Kennedy et al., 1998; Makris et al., 1999) as distributed with FSL (FMRIB Software Library) (Jenkinson et al., 2012). Patients were categorised into vmPFC and LC groups on the basis of whether they had neural damage inside the mask. **(b)** Overlap of brain lesion masks for the vmPFC group (left, pink) and LC group (right, blue) who participated in Study 1 (Fourin-a-Row Task). Colour bar shows number of patients with damage in each voxel. **(c)** Same as (b) for Study 2 (Two-Step Task). 

## **Study 1 (Four-in-a-Row Task)** 

## **Experimental Methods** 

All participants played a computer-based version of ‘Four-in-a-Row’. In this game, two players take turns to place a single piece of their colour (Black or White) on an empty space in a four-by-nine grid ( **Fig.2a** ). A board of this size has approximately 1.2 x 10[16] nonterminal states (van Opheusden et al. 2023). Each player’s goal is to place four pieces of their colour in a line (vertical, horizontal or diagonal) before their opponent. Our participants played against computer opponents. Each game could end in a win for the participant (the participant obtains four pieces in a row), a loss (the computer opponent obtains four pieces in a row), or a draw (the grid fills up without either player obtaining four in a row). Across games, each participant alternated between playing Black and White, where Black always plays first. 

The task was programmed in JavaScript and participants completed the game in a web browser hosted on Amazon Web Services. For the patients, the researcher remained on the telephone throughout the session to help with any technical difficulties with the task. However, all participants received identical standardised training on the web browser, which consisted of instructions, two practice games, and five comprehension questions. After training, participants completed forty games total. The HCs were recruited from Prolific.co.uk, and received the same training and study procedure with the only difference that the researcher was not present on the telephone during testing. 

The set of AI opponents comprised 200 difficulty levels published previously (van Opheusden et al. 2023). The 200 difficulty levels were divided into five categories of playing strength (with 40 agents per category). For the two practice games, we set the initial difficulty level to 1, which is the easiest possible. After training, participants began the study by playing an opponent randomly drawn from an easy level (category 2 i.e. levels 40-79). Participants advanced to more challenging opponents depending on performance, as implemented using a staircase procedure. Specifically, after each game, the next opponent was chosen based on the outcome of the game: after a loss, a new opponent was drawn from the category below; after 1 win or a draw, a new opponent was drawn from the same category, and after 2 wins a new opponent was drawn from the category above. 

## **Statistical Analysis** 

## _Task performance_ 

We operationalised task performance as playing strength, estimated using the Elo System (Elo, 1978). In Elo rating systems, players are ranked based on their history of wins, losses and draws against the same pool of opponents. In this case, we followed van Opheusden and colleagues in treating each category of computer level (5 categories total) as an individual 

4 

‘opponent’ faced by participants (van Opheusden et al. 2023). This measure of playing strength is purely based on the history of game outcomes and not on the quality of individual moves nor on cognitive modelling of participant behaviour. 

## _Planning Model_ 

To disentangle the cognitive components of planning in Four-in-a-Row, we used the model developed and validated by van Opheusden and colleagues (van Opheusden et al. 2023). Given the size of the state space, it is impossible to plan across all possible futures in this task. For this reason, agents must search the space efficiently. To do this, the model rests on two assumptions, namely that simple features are used to estimate the value of different moves (‘heuristic value function’), and that the most promising moves are explored first during planning (‘best-first search’). 

The heuristic value function determines the value of each board state _V(s)_ according to a combination of heuristic ‘features’ ( **Fig.2c** ). The algorithm posits 5 evaluative features: connected 2-in-a-row (i.e. two consecutive pieces surrounded by empty squares such that a 4- in-a-row could be formed in principle), un-connected 2-in-a-row (i.e. two non-consecutive pieces that, when combined, could form a 4-in-a-row), 3-in-a-row, 4-in-a-row, and proximity to the board centre. The model approximates the value of different moves through a weighted sum of the counts of these features across the board, regardless of location or orientation. Separate weights are fit for each feature. In addition, features are scaled differently (with a scaling constant _C_ ) depending on whether their colour belongs to the current ‘active’ player, or the other ‘passive’ player during the simulated move, capturing the fact that features are more valuable if they belong to the player who is currently about to move. The final value function is as follows. 

**==> picture [400 x 31] intentionally omitted <==**

Where 𝐹 comprises the set of evaluative features listed earlier (connected 2-in-a-row, unconnected 2-in-a-row, 3-in-a-row, 4-in-a-row), 𝑐black= _C_ and 𝑐white=1 whenever black is to move in state _s_ , and 𝑐black=1 and 𝑐white= _C_ whenever white is to move in state _s_ . The last term  adds Gaussian noise with mean zero and unit variance. 

Guided by the value function, the tree search algorithm constructs a partial decision-tree using best-first search ( **Fig.2d** ; Dechter & Pearl, 1985). On each iteration, the value function determines which position to explore, resulting from the sequence if both players choose their highest-value moves in the current tree. All legal moves from the selected position are evaluated, and values are backpropagated to predecessor nodes up to the root of the tree using minimax rule. Moves that are lower than the best move minus a ‘threshold’ (θ) are pruned. This reflects the fact that people cannot do an exhaustive search over the state space, and aligns with empirical evidence that people ‘prune’ branches with initial low values (Huys et al. 2012). Finally, at the end of each iteration, there is a probability of the search being terminated with a stopping probability parameter. 

In addition to the parameters related to the value function and tree search, there are two additional parameters related to sources of noise. The ‘feature drop’ parameter accounts for limitations of selective attention. Specifically, it is the probability of missing a feature on a 

5 

particular trial (a particular feature is ‘dropped’ from _V_ ( _s_ ) at all points in the tree). Finally, the lapse rate is the probability of choosing a random move. 

The model produces three final summary parameters: depth, heuristic quality, and feature drop rate. These summary parameters have better reliability and test-retest stability than the basic parameters. Following the original methods of van Opheusden and colleagues (2023) to calculate these summary parameters, we used each individual’s set of sub-parameters to simulate moves across 5482 unique states. We repeated this simulation 10 times, to minimise variability in noise. The final parameters are described below: 

1. _Planning Depth_ . The average length of the decision tree across simulated searches (i.e. how far a participant plans into the future on average). To derive depth, each participant’s fitted sub-parameters are used to simulate their moves by building a decision tree. Planning depth is formally quantified as the length of the forwardly simulated sequence (depth of decision tree), averaged across simulations. 

2. _Heuristic Quality._ The difference between the participant’s subjective weights for the five heuristic ‘features’, and the optimal weights. The subjective value is calculated across the 5482 states using each participant’s weighted combination of features. The optimal state values were calculated by running the model with no noise and no pruning until convergence on the state value. Heuristic quality is the correlation between the subjective state value (the participant’s weighted combination of features), and the objective optimal value. 

3. _Feature Drop Rate._ This parameter directly corresponds to an estimated parameter in the model, capturing the probability that a participant overlooks a feature instance on the board. When a feature is ‘dropped’, its weight is temporarily set to zero during a particular move. This captures oversights of relevant features during a move. 

Model fitting was performed on the NYU high-performance cluster (Intel Xeon E5-2690v2 CPUs 3.0 GHz) with a parallel implementation of inverse binomial sampling, which uses 20 cores. 

## _Group Comparisons_ 

Across all group comparisons, we used non-parametric tests because all variables violated assumptions of normality. First, we established whether the three groups differed in performance. For this initial test, we used Kruskal-Wallis to determine if Elo rating differed as a function of group (vmPFC, LC, or HC). We followed this test with two-sided MannWhitney U tests. The critical test was whether individuals with vmPFC lesions performed worse than other individuals with lesion damage (vmPFC patients versus LC). Following this, we verified that vmPFC patients were also worse than healthy age-matched controls (vmPFC patients versus HC). 

As an additional control, we verified that performance was truly related to the _location_ of damage rather than the size of the lesion. To do this, we predicted Elo ratings using the volume of brain damage within the vmPFC, while controlling for the total volume of brain damage: 

Elo ~  +  0𝑉vmPFC +  1𝑉total +  

6 

where 𝑉vmPFC refers to the volume of brain damage within the vmPFC, while 𝑉total refers to the total volume of brain damage (where volume was quantified in voxels). Once we established that vmPFC lesion patients had a performance deficit, we used one-sided MannWhitney tests to test three hypotheses, namely that vmPFC lesion patients planned less deeply into the future (depth), were more likely to miss valuable features (feature drop rate), or demonstrated worse heuristic value estimates (heuristic quality). Again, we started with the critical test to determine whether there was an effect of vmPFC lesion within the lesion population (vmPFC patients versus LC), following up with a comparison against healthy agematched controls (vmPFC patients versus HC). 

## **Study 2 (Two-Step Task)** 

## **Experimental Methods** 

All participants completed a variant of the Two-Step Task (Daw et al. 2011), designed to measure habitual versus goal-directed decision-making. Data collection took place in person, at the John Radcliffe Hospital in Oxford. The task involved making repeated two-stage decisions in order to earn rewards ( **Fig.3a** ). On each trial, participants first chose between two colours and then between two shapes. Of crucial significance to the task, each colour in Step 1 led to a specific pair of shapes in Step 2 with a 75% probability (“common transition”), but led to the opposite pair of shapes in 25% of trials (“rare transition”). Of the four possible shapes that could be offered in Step 2, only one shape had a high probability of reward at any point in time. This required participants to think strategically about which choice in Step 1 was most likely to lead them to the set of offers that included the high reward option. 

A learner who uses a “model-free” strategy will be more likely to repeat their Step 1 choice on the next trial after being rewarded at Step 2, regardless of whether the previous transition between steps was common or rare. However, a decision-maker who uses a model of the task structure will be sensitive to the relationship between the steps. For example, they should repeat their Step 1 choice after being rewarded on a ‘common’ transition, but switch choices when rewarded on a ‘rare’ transition, which informs them that the opposite Step 1 choice is rewarding. 

To facilitate learning in the patient population, the reward probabilities for the Step 2 choices were stationary for long periods with abrupt shifts in reward (as in Castro-Rodrigues et al. 2022, Blanco-Pozo et al. 2024, Doody et al. 2022), rather than drifting continuously. Specifically, at any point in time, one arm would be associated with a high reward probability (80% chance of payout) while each of the other three arms would be associated with low reward probabilities (8.3% chance of payout). The high-reward option was associated with the same arm for a period of 32 trials, before switching to a different arm (unannounced to the participant). The entire study consisted of 288 trials (9 blocks of 32 trials). Participants received standardised instructions from the experimenter in person ( **Fig. S5** ). The task was coded in MATLAB. 

## **Statistical Analysis** 

7 

## _Performance and simple behavioural analyses_ 

We operationalised performance as the proportion of correct choices for Step 1 i.e. choices that, if the common transition occurred, would lead to the rewarding shape at Step 2. Given the probabilistic reward structure of the task, this metric of performance is less noisy than overall reward. We examined Step 1 choices rather than Step 2 choices because only Step 1 choices can capture planning across the two steps. We used non-parametric Kruskal-Wallis tests to determine whether there was a difference between groups. 

Next, we quantified the extent to which participants were sensitive to the transition structure of the environment through response times. Participants using a model of the environment may slow down more when making their Step 2 choice after surprising ‘rare’ transitions compared to predicted ‘common’ transitions (Nussenbaum et al. 2020). For each participant, the average Step 2 response times following a rare transition and following a common transition were computed. Paired t-tests were used to determine whether response times differed as a function of transition. 

Second, we analysed stay probability to assess model-free versus model-based behavioural strategies (Daw, 2011, Otto et al. 2013, Friedel et al. 2014, Worbe et al. 2016, Otto et al. 2013, Eppinger et al. 2013, Lockwood et al. 2020, Castro-Rodrigues et al. 2022). We examined the probability that people would repeat their Step 1 choice as a function of the previous outcome (reward versus no reward) and previous transition (common versus rare) experienced. When deciding whether to repeat their choice, model-based agents will not only take into account whether they were rewarded, but will modulate this by whether the reward outcome followed a common versus rare transition sequence. We quantified this in a logistic regression model, where the previous outcome, transition, and transition–outcome interaction were all used as predictors of staying on the subsequent Step 1 choice. In addition, we included a binary control regressor capturing the tendency to repeat ‘correct’ Step 1 choices (i.e. whether the Step 1 choice on the previous trial commonly leads to the high-rewarded state). This ‘correct’ predictor was included following Akam and colleagues (2015), who showed that analyses of stay probabilities in the Two-Step Task can give rise to inflated metrics of model-based strategies unless this control regressor is included (Akam et al. 2015). Following previous studies, we used the weights corresponding to the transition-outcome interaction as a marker of ‘model-based’ reasoning (Daw, 2011; Akam et al. 2015). 

## _Reinforcement learning model_ 

We modelled choices using a reinforcement learning model with separate components capturing model-based and model-free learning (Daw et al. 2011). The task involves three states, with only one Step 1 state, and two possible Step 2 states. In the following notation, 𝑠1,𝑡 corresponds to the Step 1 state taken at trial _t_ (which is always the same), while 𝑠2,𝑡 corresponds to the Step 2 state (dependent on the first choice and transition). In each state, there are two available actions (𝑎A or 𝑎B). 

_Model-free algorithm_ 

8 

The model-free algorithm updates the value of state-action pairs according to a SARSA (λ) temporal-difference reinforcement learner (Daw et al. 2011, Rummery and Niranjan, 1994). At each step _i_ of the two-step trial _t_ , the value for the chosen action (𝑎𝑖,𝑡) is updated: 

**==> picture [187 x 15] intentionally omitted <==**

Where 𝛼 is a learning rate parameter, and the reward prediction error (RPE; 𝛿𝑖,𝑡) corresponds to the following: 

**==> picture [238 x 16] intentionally omitted <==**

The reward following the Step 1 choice (𝑟1,𝑡) is always 0, while the reward following the Step 2 choice (𝑟2,𝑡) can be 1 or 0. Note that the prediction error is driven by different sources of information after the first versus second stage choices. At the Step 1 choice, reward is never received, so the update is driven by the Step 2 value, 𝑄mf(𝑠2,𝑡,𝑎2,𝑡). At the Step 2 choice, the update is driven entirely by the reward received, 𝑟2,𝑡 (while the value of the subsequent state is set to zero because the trial ends after two steps). Finally, at the end of the trial, the value of the Step 1 choice is also updated with an eligibility trace. In other words, the RPE from the final choice is used to update the Step 1 choice, multiplied by an eligibility parameter (λ) (Sutton and Barto 1998): 

**==> picture [200 x 15] intentionally omitted <==**

## _Model-based algorithm_ 

The model-based algorithm updates its values for Step 1 using a model of the task structure – that is, the probabilities associated with transitioning between steps. For example, if the state in Step 2 was unlikely to occur after the Step 1 choice (rare transition of 25%), the algorithm correspondingly updates the value of the action in Step 1 that most commonly reaches the rewarded state. Below, 𝑠A and 𝑠B denote the two possible second states. The values of the Step 1 actions (𝑎𝑗) are computed according to the Bellman equation: 

**==> picture [388 x 21] intentionally omitted <==**

This is re-computed at every trial from the current estimates of value. At Step 2, model-based learning is equivalent to model-free learning, since the second step value purely reflects an estimate of the immediate reward (Daw et al. 2011). 

## _Choice algorithm_ 

The influence of model-based versus model-free strategies can be quantified in the choices at Step 1. The probability of choosing each Step 1 action is determined by a combination of model-based value, model-free value, and a ‘repetition bias’. We fit an adapted version of Daw’s original model that has previously been used to investigate individual differences in the Two-Step Task (Decker et al. 2016; Potter, Bryce et al. 2017; Nussenbaum et al. 2020). Specifically, this model contains separate softmax temperature parameters associated with the 

9 

influence of the model-based value (𝛽mb) and the model-free value (𝛽mf), alongside a parameter capturing a bias to repeat the Step 1 choice from the previous trial (𝑝). The probability of choosing each possible action 𝑎𝑖 at Step 1 is the following: 

**==> picture [387 x 32] intentionally omitted <==**

At Step 2, the model-free value is used to predict choice with a separate softmax temperature: 

**==> picture [217 x 31] intentionally omitted <==**

The final model had six free parameters, namely a Step 1 weight for model-free value (𝛽mf), a Step 1 weight for model-based value (𝛽mb), a Step 1 weight for persistence (repeating the previous choice; 𝑝), a Step 2 softmax temperature for model-free value (𝛽step−2), learning rate (𝛼) and eligibility parameter (𝜆). 

## _Model Validation and Fitting_ 

While the behavioural model described above has been used extensively in the literature (Decker et al., 2016; Potter et al. 2017, Nussenbaum et al. 2020), we collected this dataset using an adapted version of the Two-Step Task that would be easier for patients with brain damage to learn. In this version, reward probabilities were stationary with abrupt shifts, rather than continuously drifting. Since previous studies have shown that model-free behaviour can be mistaken for model-based behaviour in environments with stationary probabilities (Akam et al. 2015), it was important to validate the model to determine that model-based behaviour could still be recovered in the exact task variant used in this study. Full details of model validation are included in the supplementary materials, showing that model-based behaviour is recoverable in this version of the task ( **Fig. S3** ). 

We used a Bayesian hierarchical modelling framework to fit the reinforcement learning models to behaviour, allowing us to pool data across participants to improve individual parameter estimates. Full details of model priors and fitting procedure are included in the supplementary materials. We coded the models in the Stan modelling language (Carpenter et al. 2017), fitting each dataset using the Cmdstanpy interface. Following previous studies (Decker et al. 2016; Potter et al. 2017), we did not include the first 9 choice trials in the analysis. 

## _Group Comparisons_ 

Following the same analysis procedure as Study 1, we began by investigating differences in performance between the three groups (vmPFC, LC and HC), defined for this task as accuracy for the Step 1 choice. ANOVA was used since this metric did not violate assumptions of normality. 

10 

We then investigated group differences in model-based planning. Three metrics were used to probe model-based planning. First, we used analysis of stay probabilities to quantify whether participants took into account the transition structure of the task. Specifically, this is the interaction between whether a choice was rewarded, and whether the outcome followed a common or rare transition (transition-outcome interaction on the probability of staying). Second, we quantified sensitivity to the transition structure by analysing response time differences for making a Step 2 decision following a rare versus common transition after Step 1. This was computed as an individual’s difference in their average Step 2 response time following a rare versus common transition, where a smaller difference could indicate lower sensitivity to the task model. Finally, we formally quantified model-based planning weights using the reinforcement learning model described above. To test for a difference between lesion and control groups, we used ANOVA unless assumptions of normality were violated, in which case non-parametric Kruskal-Wallis tests. Additional behavioural metrics, including the other reinforcement learning model parameters, are reported in the Supplementary materials. 

## **Results** 

## **VmPFC damage impairs complex planning in Four-in-a-Row** 

VmPFC lesion patients were worse at playing Four-in-a-Row compared to both control lesion patients, and age-matched healthy controls ( **Fig.2b** ). To quantify playing strength, we used the Bayeselo algorithm (https://www.remi-coulom.fr/Bayesian-Elo/), originally developed for rating chess players, which has previously been used to rate performance in Four-in-a-Row (van Opheusden et al. 2023). A Kruskal-Wallis test indicated that there was a difference in Elo ratings between the three groups ( _H_ (2)=7.20, _p_ =0.027). Lesion patients with vmPFC damage had lower Elo ratings compared to LCs (median vmPFC Elo rating=–66.0, median LC Elo rating=33.5; two-sided Mann-Whitney: _n_ 1=10, _n_ 2=8, _U_ =14, _p_ =0.021), and also compared to HCs (median HC Elo rating=27.5; two-sided Mann-Whitney: _n_ 1=10, _n_ 2=30, _U_ =71, _p_ =0.014). 

To eliminate the possibility that our results were driven by differences in lesion size rather than location, we controlled for total lesion volume in a regression analysis. Within the patient population, we found that lower Elo ratings were predicted by larger vmPFC lesions (β=-0.08, _p_ =0.033) but not significantly by larger lesions in general (β=0.00, _p_ =0.664). These findings suggest that damage to the vmPFC impairs performance in this complex planning task. 

11 

**==> picture [379 x 452] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>*<br>*<br>c d<br>e f g<br>** n.s. n.s.<br>** ** n.s.<br>**----- End of picture text -----**<br>


**Figure 2** . **Study 1 (Four-in-a-Row Task). (a)** Depiction of the task, where participants aimed to place four pieces of their colour in a row. The arrow depicts a winning move for the Black player. **(b)** Elo ratings, which provide a metric of performance, or ‘playing strength’, as a function of group. Error bars show s.e.m., dots show individual participant ratings. Stars show statistical significance ( _n.s._ : _p_ >0.05; *: _p_ <0.05; **: _p_ <0.01) from the results of non-parametric tests comparing vmPFC group to control groups, after establishing there was a difference across populations. VmPFC lesion patients performed worse than both lesion controls and age-matched controls. **(c)** The computational model consists of a heuristic value function (for evaluating states) and a tree search algorithm (for simulating future moves). The value function corresponds to a linear combination of heuristic ‘features’ critical for playing the game. Coloured lines depict example features, where purple shows connected two-in-a-row, blue shows un-connected two-in-a-row, and orange shows three-in-a-row. Within the model, ‘heuristic quality’ refers to how closely an individual’s weights for each feature match the optimal weights. ‘Feature drop rate’ refers to the probability of overlooking a feature on the map, on any trial. **(d)** The tree search algorithm constructs a partial decision-tree using best-first search (Dechter & Pearl, 1985; see Materials and Methods for full description). ‘Depth’ refers to the average length of forward search, illustrated in the example with the red trajectory. **(e, f, g).** Summary parameters from the planning model, plotted by group. Error bars show s.e.m., dots depict individual participant parameter estimates. Stars depict result of non-parametric one-sided tests of the three 

12 

hypotheses, namely that vmPFC lesions are associated with lower depth, higher feature drop rate, and lower heuristic quality than the two control groups. 

## **Planning deficits following vmPFC lesions are linked to attentional oversights and lower depth of search** 

How could vmPFC lesions affect planning? We fit behaviour in the Four-in-a-Row Task using a computational process model, allowing us to investigate three separate cognitive components of complex planning. VmPFC patients could be worse at Four-in-a-Row because they plan less far into the future (lower ‘depth’), struggle to evaluate moves using heuristics (lower ‘heuristic quality’), or overlook relevant features during planning (higher ‘feature drop rate’). 

The ‘feature drop’ parameter captures the probability of overlooking relevant information on the board when planning a move. We found the vmPFC group were more likely to miss important features on the board compared to both LCs ( **Fig.2e** ; one-sided Mann-Whitney; _n_ 1=10, _n_ 2=8, _U_ =72.0, _p_ =0.002), and HCs (one-sided Mann-Whitney; _n_ 1=10, _n_ 2=30, _U_ =246.0, _p_ =0.001). 

The ‘depth’ parameter captures how far into the future participants were planning. We found the vmPFC group planned to a lower depth than LCs ( **Fig.2f** ; one-sided Mann-Whitney; _n_ 1=10, _n_ 2=8, _U_ =15.0, _p_ =0.013). This result did not survive comparison with HCs (one-sided Mann-Whitney U; _n_ 1=10, _n_ 2=30, _U_ =103.0, _p_ =0.073), although depth was lower for vmPFC patients when compared to both control groups pooled (one-sided Mann-Whitney U; _n_ 1=10, _n_ 2=38, _U_ =118.0, _p_ =0.035). 

The ‘heuristic quality’ parameter captures the difference between a participant’s use of appropriate heuristics to evaluate moves, and how an optimal player would use these heuristics (for example, assigning a high value to a three-in-a-row feature of ones’ own colour). Damage to vmPFC did not significantly impair the quality of the heuristics used to evaluate moves compared to either LCs or HCs ( **Fig.2g** ; LCs: _n_ 1=10, _n_ 2=8, _U_ =23.0, _p_ =0.072; HCs: _n_ 1=10, _n_ 2=30, _U_ =104.0, _p_ =0.078). 

## **Simple Two-Step task showed no evidence of model-based planning in patients or controls** 

We found vmPFC patients were impaired at planning in the complex Four-in-a-Row task, and had a tendency to overlook relevant information and to search less deeply into the future. Next, we asked whether behavioural differences following vmPFC lesions could be detected in a simpler task which also probes the use of an internal model to make choices – a prerequisite for more complex planning. We adopted the ‘Two-Step’ task (Daw et al. 2011), originally developed to measure decisions reflecting the use of a model of the environment (‘model-based’) from more basic decision strategies (‘model-free’). In this simpler planning setting, decisions affect outcomes at most two steps into the future, and involve choices between binary options with only a single attribute. 

All three groups performed above chance in the task, but showed no difference as a function of lesion location. In each group, participants picked the correct colour at Step 1 more 

13 

frequently than chance ( **Fig.3b** ; one-sample two-sided t-test comparing the mean proportion of ‘correct’ Step 1 choices against 0.5; vmPFC: _t_ (29)=4.44, _p_ =0.0001; LCs: _t_ (18)=3.23, _p_ =0.005; HCs: _t_ (19)=3.70, _p_ =0.002; see **Fig. S2a-b** for other performance metrics), showing a basic understanding of the reward structure. However, unlike in the Four-in-a-Row task, lesion damage did not significantly affect performance (ANOVA for effect of lesion group on Step 1 choice accuracy; _F_ (2,66) = 0.71, _p_ = 0.495). 

While we found no evidence that vmPFC damage affected performance, lesions may affect the type of strategy used in the Two-Step task. On each trial, receiving reward depends on making two sequential choices. The ability to plan across the two choices using structural knowledge of the task (‘model-based’) can be dissociated from simple repetition of actions which lead to reward (‘model-free’). This is because the task exploits a probabilistic structure where the majority of trials consist of predictable chains of events (‘common’ trials), but in a subset of trials, the two chains of events are swapped over (‘rare’ trials). A decision-maker who uses a model-free strategy will be more likely to repeat an initial choice leading to reward, regardless of whether the previous trial followed a common or rare sequence of events (main effect of outcome on stay probability). However, a decision-maker who uses a model of the task structure will be more likely to repeat their first step choice after being rewarded on a common trial, but switch to the opposite choice when rewarded on a rare trial (outcome x transition interaction on stay probability). 

Notably, across our population of older subjects, use of model-based strategies was attenuated. While participants (pooled across groups) were more likely to stay after being rewarded (main effect of reward; two-sided one sample Wilcoxon: 𝛽=0.57, n=69, _Z=_ 4.68, _p_ =2.88 x 10[-6] ), they did not modulate their behaviour significantly depending on the rarity of the transition experienced (see **Fig. S2d-f** ; outcome x transition interaction; two-sided one sample Wilcoxon: 𝛽=0.14, _n_ =69, _Z=_ 0.62, _p_ =0.536). This is consistent with previous studies finding reduced model-based reasoning in older populations (Eppinger et al. 2013). Importantly, we also did not find any difference between groups in either model-free or model-based strategies as a function of brain damage ( **Fig. S2g** ; Kruskal-Wallis test for effect of lesion group on main effect of reward: _H_ (2)=0.59, _p_ =0.744; Kruskal-Wallis test for effect of lesion group on outcome x transition interaction: _H_ (2)=2.34, _p_ =0.310). 

Despite this, all groups were sensitive to the transition structure linking Step 1 and Step 2 as indicated by slower response times following the more surprising ‘rare’ transition compared to the ‘common’ transition ( **Fig. S2c** ; Wilcoxon signed-rank of mean response times after rare versus common transitions; vmPFC: _Z_ =4.68, _n_ =30, _p_ =2.88 x 10[-6] ; LCs: _Z_ =3.22, _n_ =19, _p_ =0.001; HCs: _Z_ =3.47, _n_ =20, _p_ =0.0005). Again, we did not find that lesion damage significantly affected sensitivity to the task structure as reflected in response times (KruskalWallis for effect of lesion group on response time difference following common versus rare transitions: _H_ (2)=2.35, _p_ =0.309). 

Finally, we fit reinforcement learning models to the data to formally quantify the contribution of model-based and model-free reasoning, while also controlling for other behavioural factors such as persistence (the tendency to repeat the previous action), and learning rate (how quickly people update their beliefs in the value). We found no significant group differences in model-based behaviour when formally modelled ( **Fig.3c** ; Kruskal-Wallis for effect of lesion group on model-based beta weight in RL model: _H_ (2)=5.19, _p_ =0.075; see **Fig. S4** for other RL parameters). Our findings show that across a range of behavioural metrics, vmPFC 

14 

patients neither demonstrated significantly worse performance nor showed significant differences in model-based metrics in the Two-Step Task. 

**==> picture [489 x 188] intentionally omitted <==**

**Figure 3** . **Study 2 (Two-Step Task). (a)** Depiction of the task, where participants made two sequential decisions between colours (Step 1) followed by shapes (Step 2), with the aim of maximising wins. The arrows between Step 1 and Step 2 illustrate the common transitions (bold arrow, 75% probability) and the rare transitions (narrow arrow, 25% probability). Arrows between Step 2 and the reward outcome illustrate the probability of winning after selection of each shape. At any point in time, a particular shape (in this example, the star) was associated with a high probability of winning reward. The high-reward option shifted to a different shape every 32 trials. **(b)** Performance plotted by group. Annotations show the result of ANOVA tests for difference between populations ( _n.s._ corresponds to _p_ >0.05). Performance is quantified as the proportion of correct choices at Step 1 which corresponds to choosing the first-step option that commonly led to the rewarded shape. Error bars depict s.e.m., dots show individual data points, line depicts chance performance. **(c)** Model-based weights from the reinforcement learning model capturing the contribution of model-based strategy. Annotations show the result of non-parametric tests for difference between populations. Model-based weights are plotted by group, where error bars depict s.e.m. and dots show individual data points. 

## **Discussion** 

Damage to vmPFC has long been associated with differences in planning in complex environments, but how this relates to the underlying cognitive processes supporting planning is unclear. We investigated how vmPFC damage affects complex planning using a recently developed task and computational framework called ‘Four-in-a-Row’, which enables the dissociation of multiple components of planning (van Opheusden et al. 2023). Consistent with findings from more naturalistic settings, vmPFC damage was associated with worse performance in this rich multi-step planning game compared to lesion control patients and age-matched healthy controls. We investigated how planning deficits related to the cognitive processes identified by a planning model, through three possibilities: that vmPFC damage leads to more feature oversights, to reductions in planning depth, or to systematic deviations in how options are heuristically evaluated. We found the first two of these hypotheses to be true. Patients with vmPFC damage were more likely to overlook game-relevant features on the board, leading to missed opportunities for winning or blocking opponents. VmPFC 

15 

damage was also associated with planning less far into the future compared to patients with damage to other brain areas. 

We investigated whether planning differences revealed using Four-in-a-Row could be detected in another planning paradigm with a substantially smaller set of options and a shorter planning horizon. Four-in-a-Row characterizes planning over multiple steps and a vast number of candidate options, making it more similar to real-world planning than many previous laboratory planning tasks (van Opheusden et al. 2023, Ma et al. 2020). We employed the ‘Two-Step’ task to investigate planning with a maximum horizon of only two steps into the future, with only two options available at each step. The Two-Step findings in our study are limited by the fact that no group demonstrated significant model-based planning. This is likely to be related to the age of the population, where older cohorts generally show reduced metrics of model-based behaviour (Eppinger et al. 2013). Notably, it it unlikely to be explained by a lack of power, as our sample size for the Two-Step Task was substantially larger than for most lesion patient studies (Yu et al. 2020), including studies detecting location-based differences using the Two-Step paradigm (Vikbladh et al. 2019). 

While the Two-Step Task failed to reveal evidence of planning in this older population, the Four-in-a-Row task was able to detect strong signatures of planning as well as behavioural differences between groups, even with a smaller sample size. This difference may be explained by the substantially larger state space involved in Four-in-a-Row, which allows for characterisation of more complex planning behaviours. This suggests that the Four-in-a-Row task provides a more sensitive computational framework for studying planning that can be used even in older populations, where the Two-Step Task loses sensitivity for detecting planning behaviour. 

When choices in the Four-in-a-Row task were investigated using a computational planning model, we found that vmPFC patients were more likely to overlook game-relevant information on any given trial (‘feature drop’). This metric captures the tendency to miss critical features on the game board, for example opportunities for winning or blocking opponents. One possible cause for this behaviour is that vmPFC damage affects the ability to integrate all relevant information for making decisions. This is consistent with previous work showing that patients with vmPFC damage fail to make decisions which require integrating multiple value-relevant attributes (Fellows, 2006; Pelletier & Fellows, 2019). Another possibility is that patients failed to orient attention to value-relevant features of the environment. This idea is also consistent with previous studies showing vmPFC damage alters the allocation of attention to valuable features of the environment (Vaidya and Fellows 2015), while activity in vmPFC predicts goal-oriented attention in healthy individuals (Günseli and Aly 2020; Holton et al. 2024). Future work could disentangle these different mechanisms leading to more feature oversights, for example by using eye-tracking. 

As well as overlooking game-relevant features, we found that vmPFC patients planned to lower depth than control patients. However, in contrast to the previous finding relating vmPFC damage to feature oversights, this finding did not survive comparison with a healthy age-matched population. Planning involves mental simulation of possible futures that one could encounter. Problems simulating the future will lead to suboptimal planning and has been one of the proposed explanations for planning deficits in vmPFC patients (Bertossi et al. 2015). As far as we know, this finding that vmPFC patients planned to lower depth than control lesion patients is the first evidence from a computational paradigm to support a wealth of qualitative evidence suggesting vmPFC patients have difficulties producing detail 

16 

about the future (Fellows and Farah, 2005, Bertossi et al., 2016a, 2016b, Bertossi et al., 2017). Difficulty in planning deeply may arise due to damage of an internal ‘map’ of the causal task structure, which has been localised to vmPFC in neuroimaging (Wilson et al. 2014, Schuck et al. 2016). Alternatively, future planning may be attenuated if the temporal discount factor is very steep (i.e. decisions are dominated by proximal rewards), as is sometimes observed after vmPFC lesions (Peters and D'Esposito, 2016, Sellitto et al., 2010; although note that results have been conflicting, see Fellows and Farah, 2005). 

While we found that vmPFC damage reduces planning depth, the simulation of future states is likely to rest on distributed neural mechanisms. One possibility is that vmPFC is critical for coordinating task-dependent computations performed in other areas such as hippocampus or striatum (Blanco-Pozo et al., 2024). Consistent with this idea, damage to hippocampus has been shown to impair model-based planning in rodents (Miller et al. 2017) and most recently in humans performing the Two-Step Task (Vikbladh et al. 2019). Greater functional coupling between hippocampus and vmPFC has also been shown to predict better inferences over unseen structured relationships in healthy individuals (Zeithamova et al. 2012), and many tasks involving model-based inferences find activity in both vmPFC and hippocampus (Redish 2016, Wang et al. 2020, Barron et al. 2013; Barron et al. 2020; Park et al. 2021), supporting the possibility that prefrontal areas may coordinate model-based simulation played out in hippocampal areas. 

There is growing evidence that people use heuristic strategies to plan when the environment is too complex to simulate all possible future (Huys et al. 2012, 2015, Solway et al. 2014, Solway & Botvinick, 2015, Keramati et al. 2016, Snider et al. 2015, van Opheusden et al. 2023). We did not find evidence that vmPFC patients were significantly worse at identifying what constituted a good heuristic for evaluating moves compared to controls (‘heuristic quality’). This alternative metric captured the difference between how participants weighed up different heuristic features for evaluating candidate moves compared to an optimal player. 

In conclusion, we leveraged recent computational methods for studying planning in patients with frontal brain lesions. The rich framework of the Four-in-a-Row task revealed that deficits in complex planning following vmPFC damage are related to tendencies to overlook relevant information, and to plan less deeply into the future. This contrasted with a simpler paradigm for studying planning, namely the Two-Step Task, which failed to reveal behavioural differences between groups. Novel computational methods for capturing behaviour in rich task settings offer exciting new opportunities for meeting the age-old challenge of balancing complexity and interpretability in lesion patient studies. 

17 

## **References** 

- Akam, T., Costa, R., & Dayan, P. (2015). Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task. _PLOS Computational Biology_ , _11_ (12), e1004648. https://doi.org/10.1371/journal.pcbi.1004648 

- Barron, H. C., Dolan, R. J., & Behrens, T. E. J. (2013). Online evaluation of novel choices by simultaneous representation of multiple memories. _Nature Neuroscience_ , _16_ (10), 1492–1498. https://doi.org/10.1038/nn.3515 

- Barron, H. C., Reeve, H. M., Koolschijn, R. S., Perestenko, P. V., Shpektor, A., Nili, H., Rothaermel, R., Campo-Urriza, N., O’Reilly, J. X., Bannerman, D. M., Behrens, T. E. J., & Dupret, D. (2020). Neuronal Computation Underlying Inferential Reasoning in Humans and Mice. _Cell_ , _183_ (1), 228-243.e21. https://doi.org/10.1016/j.cell.2020.08.035 

- Bartra, O., McGuire, J. T., & Kable, J. W. (2013). The valuation system: A coordinate-based meta-analysis of BOLD fMRI experiments examining neural correlates of subjective value. _NeuroImage_ , _76_ , 412–427. https://doi.org/10.1016/j.neuroimage.2013.02.063 

- Basu, R., Gebauer, R., Herfurth, T., Kolb, S., Golipour, Z., Tchumatchenko, T., & Ito, H. T. (2021). The orbitofrontal cortex maps future navigational goals. _Nature_ , _599_ (7885), 449–452. https://doi.org/10.1038/s41586-021-04042-9 

- Bertossi, E., Aleo, F., Braghittoni, D., & Ciaramelli, E. (2016). Stuck in the here and now: Construction of fictitious and future experiences following ventromedial prefrontal damage. _Neuropsychologia_ , _81_ , 107–116. https://doi.org/10.1016/j.neuropsychologia.2015.12.015 

- Bertossi, E., Candela, V., De Luca, F., & Ciaramelli, E. (2017). Episodic future thinking following vmPFC damage: Impaired event construction, maintenance, or narration? _Neuropsychology_ , _31_ (3), 337–348. https://doi.org/10.1037/neu0000345 

- Bertossi, E., Tesini, C., Cappelli, A., & Ciaramelli, E. (2016). Ventromedial prefrontal damage causes a pervasive impairment of episodic memory and future thinking. _Neuropsychologia_ , _90_ , 12–24. https://doi.org/10.1016/j.neuropsychologia.2016.01.034 

- Blanco-Pozo, M., Akam, T., & Walton, M. E. (2024). Dopamine-independent effect of rewards on choices through hidden-state inference. _Nature Neuroscience_ , _27_ (2), 286–297. https://doi.org/10.1038/s41593-023-01542-x 

- Botvinick, M. M., Niv, Y., & Barto, A. G. (2009). Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective. _Cognition_ , _113_ (3), 262–280. https://doi.org/10.1016/j.cognition.2008.08.011 

- Bowren, M. D., Croft, K. E., Reber, J., & Tranel, D. (2018). Choosing spouses and houses: Impaired congruence between preference and choice following damage to the ventromedial prefrontal cortex. _Neuropsychology_ , _32_ (3), 280–303. https://doi.org/10.1037/neu0000421 

- Burgess, P. W., Veitch, E., de Lacy Costello, A., & Shallice, T. (2000). The cognitive and neuroanatomical correlates of multitasking. _Neuropsychologia_ , _38_ (6), 848–863. https://doi.org/10.1016/s0028-3932(99)00134-7 

- Callaway, F., van Opheusden, B., Gul, S., Das, P., Krueger, P. M., Griffiths, T. L., & Lieder, F. (2022). Rational use of cognitive resources in human planning. _Nature Human Behaviour_ , _6_ (8), 1112–1125. https://doi.org/10.1038/s41562-022-01332-8 

- Camille, N., Griffiths, C. A., Vo, K., Fellows, L. K., & Kable, J. W. (2011). Ventromedial Frontal Lobe Damage Disrupts Value Maximization in Humans. _Journal of Neuroscience_ , _31_ (20), 7527–7532. https://doi.org/10.1523/JNEUROSCI.6527-10.2011 

- Carpenter, B., Gelman, A., Hoffman, M. D., Lee, D., Goodrich, B., Betancourt, M., Brubaker, M. A., Guo, J., Li, P., & Riddell, A. (2017). Stan: A Probabilistic Programming Language. _Journal of Statistical Software_ , _76_ , 1. https://doi.org/10.18637/jss.v076.i01 

- Castro-Rodrigues, P., Akam, T., Snorasson, I., Camacho, M., Paixão, V., Maia, A., BarahonaCorrêa, J. B., Dayan, P., Simpson, H. B., Costa, R. M., & Oliveira-Maia, A. J. (2022). 

18 

Explicit knowledge of task structure is a primary determinant of human model-based action. _Nature Human Behaviour_ , _6_ (8), 1126–1141. https://doi.org/10.1038/s41562-022-01346-2 

Chan, S. C. Y., Niv, Y., & Norman, K. A. (2016). A Probability Distribution over Latent Causes, in the Orbitofrontal Cortex. _Journal of Neuroscience_ , _36_ (30), 7817–7828. https://doi.org/10.1523/JNEUROSCI.0659-16.2016 

- Costa, K. M., Scholz, R., Lloyd, K., Moreno-Castilla, P., Gardner, M. P. H., Dayan, P., & Schoenbaum, G. (2023). The role of the lateral orbitofrontal cortex in creating cognitive maps. _Nature Neuroscience_ , _26_ (1), 107–115. https://doi.org/10.1038/s41593-022-01216-0 

- Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans’ choices and striatal prediction errors. _Neuron_ , _69_ (6), 1204–1215. https://doi.org/10.1016/j.neuron.2011.02.027 

- Dechter, R., & Pearl, J. (1985). Generalized best-first search strategies and the optimality of A*. _Journal of the ACM_ , _32_ (3), 505–536. https://doi.org/10.1145/3828.3830 

- Decker, J. H., Otto, A. R., Daw, N. D., & Hartley, C. A. (2016). From Creatures of Habit to GoalDirected Learners: Tracking the Developmental Emergence of Model-Based Reinforcement Learning. _Psychological Science_ , _27_ (6), 848–858. https://doi.org/10.1177/0956797616639301 

Doody, M., Van Swieten, M. M. H., & Manohar, S. G. (2022). Model-based learning retrospectively updates model-free values. _Scientific Reports_ , _12_ (1), 2358. https://doi.org/10.1038/s41598-022-05567-3 

- Elliott Wimmer, G., & Büchel, C. (2019). Learning of distant state predictions by the orbitofrontal cortex in humans. _Nature Communications_ , _10_ (1), 2554. https://doi.org/10.1038/s41467-01910597-z 

- Elo, A. E. (1978). _The Rating of Chessplayers, Past and Present_ . Arco Pub. 

- Eppinger, B., Walter, M., & Heekeren, H. R. (2013). Of goals and habits: Age-related and individual differences in goal-directed decision-making. _Frontiers in Neuroscience_ , _7_ . https://doi.org/10.3389/fnins.2013.00253 

- Eslinger, P. J., & Damasio, A. R. (1985). Severe disturbance of higher cognition after bilateral frontal lobe ablation: Patient EVR. _Neurology_ , _35_ (12), 1731–1741. https://doi.org/10.1212/wnl.35.12.1731 

- Fellows, L. K., & Farah, M. J. (2005). Dissociable elements of human foresight: A role for the ventromedial frontal lobes in framing the future, but not in discounting future rewards. _Neuropsychologia_ , _43_ (8), 1214–1221. https://doi.org/10.1016/j.neuropsychologia.2004.07.018 

- Fellows, L. K., & Farah, M. J. (2007). The Role of Ventromedial Prefrontal Cortex in Decision Making: Judgment under Uncertainty or Judgment Per Se? _Cerebral Cortex_ , _17_ (11), 2669– 2674. https://doi.org/10.1093/cercor/bhl176 

- Friedel, E., Koch, S. P., Wendt, J., Heinz, A., Deserno, L., & Schlagenhauf, F. (2014). Devaluation and sequential decisions: Linking goal-directed and model-based behavior. _Frontiers in Human Neuroscience_ , _8_ . https://doi.org/10.3389/fnhum.2014.00587 

- Geffner, H. (2013). Computational models of planning. _Wiley Interdisciplinary Reviews. Cognitive Science_ , _4_ (4), 341–356. https://doi.org/10.1002/wcs.1233 

- Gigerenzer, G., & Gaissmaier, W. (2011). Heuristic Decision Making. _Annual Review of Psychology_ , _62_ (Volume 62, 2011), 451–482. https://doi.org/10.1146/annurev-psych-120709145346 

- Günseli, E., & Aly, M. (2020). Preparation for upcoming attentional states in the hippocampus and medial prefrontal cortex. _eLife_ , _9_ , e53191. https://doi.org/10.7554/eLife.53191 

- Harlow, J. M. (1868). _Recovery from the passage of an iron bar through the head—Digital Collections—National Library of Medicine_ (20th ed., Vol. 39). Publications of the 

19 

- Massachusetts Medical Society. https://collections.nlm.nih.gov/catalog/nlm:nlmuid 66210360R-bk 

- Holton, E., Grohn, J., Ward, H., Manohar, S. G., O’Reilly, J. X., & Kolling, N. (2024). Goal commitment is supported by vmPFC through selective attention. _Nature Human Behaviour_ , 1–15. https://doi.org/10.1038/s41562-024-01844-5 

- Huys, Q. J. M., Eshel, N., O’Nions, E., Sheridan, L., Dayan, P., & Roiser, J. P. (2012). Bonsai Trees in Your Head: How the Pavlovian System Sculpts Goal-Directed Choices by Pruning Decision Trees. _PLOS Computational Biology_ , _8_ (3), e1002410. https://doi.org/10.1371/journal.pcbi.1002410 

- Huys, Q. J. M., Lally, N., Faulkner, P., Eshel, N., Seifritz, E., Gershman, S. J., Dayan, P., & Roiser, J. P. (2015). Interplay of approximate planning strategies. _Proceedings of the National Academy of Sciences_ , _112_ (10), 3098–3103. https://doi.org/10.1073/pnas.1414219112 

- Jones, J., Esber, G., McDannald, M., Gruber, A., Hernandez, A., Mirenzi, A., & Schoenbaum, G. (2012). Orbitofrontal Cortex Supports Behavior and Learning Using Inferred But Not Cached Values. _Science_ , _338_ (6109), 953–956. https://doi.org/10.1126/science.1227489 

- Kaplan, R., King, J., Koster, R., Penny, W. D., Burgess, N., & Friston, K. J. (2017). The Neural Representation of Prospective Choice during Spatial Planning and Decisions. _PLOS Biology_ , _15_ (1), e1002588. https://doi.org/10.1371/journal.pbio.1002588 

- Kennedy, D. N., Lange, N., Makris, N., Bates, J., Meyer, J., & Caviness, V. S. (1998). Gyri of the human neocortex: An MRI-based analysis of volume and variance. _Cerebral Cortex (New York, N.Y.: 1991)_ , _8_ (4), 372–384. https://doi.org/10.1093/cercor/8.4.372 

- Keramati, M., Dezfouli, A., & Piray, P. (2011). Speed/accuracy trade-off between the habitual and the goal-directed processes. _PLoS Computational Biology_ , _7_ (5), e1002055. 

- Leong, Y. C., Radulescu, A., Daniel, R., DeWoskin, V., & Niv, Y. (2017). Dynamic Interaction between Reinforcement Learning and Attention in Multidimensional Environments. _Neuron_ , _93_ (2), 451–463. https://doi.org/10.1016/j.neuron.2016.12.040 

- Levy, D. J., & Glimcher, P. W. (2012). The root of all value: A neural common currency for choice. _Current Opinion in Neurobiology_ , _22_ (6), 1027–1038. https://doi.org/10.1016/j.conb.2012.06.001 

- Lockwood, P. L., Klein-Flügge, M. C., Abdurahman, A., & Crockett, M. J. (2020). Model-free decision making is prioritized when learning to avoid harming others. _Proceedings of the National Academy of Sciences_ , _117_ (44), 27719–27730. https://doi.org/10.1073/pnas.2010890117 

- Ma, I., Phaneuf, C., van Opheusden, B., Ma, W. J., & Hartley, C. (2022). _The component processes of complex planning follow distinct developmental trajectories_ . https://osf.io/preprints/psyarxiv/d62rw/ 

- Makris, N., Meyer, J. W., Bates, J. F., Yeterian, E. H., Kennedy, D. N., & Caviness, V. S. (1999). MRI-Based topographic parcellation of human cerebral white matter and nuclei II. Rationale and applications with systematics of cerebral connectivity. _NeuroImage_ , _9_ (1), 18–45. https://doi.org/10.1006/nimg.1998.0384 

- Mattar, M. G., & Lengyel, M. (2022). Planning in the brain. _Neuron_ , _110_ (6), 914–934. https://doi.org/10.1016/j.neuron.2021.12.018 

- Miller, K. J., Botvinick, M. M., & Brody, C. D. (2017). Dorsal hippocampus contributes to modelbased planning. _Nature Neuroscience_ , _20_ (9), 1269–1276. https://doi.org/10.1038/nn.4613 

- Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., & Riedmiller, M. (2013). _Playing Atari with Deep Reinforcement Learning_ (arXiv:1312.5602). arXiv. https://doi.org/10.48550/arXiv.1312.5602 

20 

- Newell, A., Shaw, J., & Simon, H. (1959). _Report on a general problem-solving program_ . IFIP Congress. https://www.semanticscholar.org/paper/Report-on-a-general-problem-solvingprogram-Newell-Shaw/97876c2195ad9c7a4be010d5cb4ba6af3547421c 

- Niv, Y. (2019). Learning task-state representations. _Nature Neuroscience_ , _22_ (10), 1544–1553. https://doi.org/10.1038/s41593-019-0470-8 

- Noonan, M. P., Chau, B. K. H., Rushworth, M. F. S., & Fellows, L. K. (2017). Contrasting Effects of Medial and Lateral Orbitofrontal Cortex Lesions on Credit Assignment and DecisionMaking in Humans. _Journal of Neuroscience_ , _37_ (29), 7023–7035. https://doi.org/10.1523/JNEUROSCI.0692-17.2017 

- Nussenbaum, K., Scheuplein, M., Phaneuf, C. V., Evans, M. D., & Hartley, C. A. (2020). Moving Developmental Research Online: Comparing In-Lab and Web-Based Studies of Model-Based Reinforcement Learning. _Collabra: Psychology_ , _6_ (1), 17213. https://doi.org/10.1525/collabra.17213 

- Otto, A. R., Gershman, S. J., Markman, A. B., & Daw, N. D. (2013). The Curse of Planning: Dissecting Multiple Reinforcement-Learning Systems by Taxing the Central Executive. _Psychological Science_ , _24_ (5), 751–761. https://doi.org/10.1177/0956797612463080 

- Owen, A. M., Downes, J. J., Sahakian, B. J., Polkey, C. E., & Robbins, T. W. (1990). Planning and spatial working memory following frontal lobe lesions in man. _Neuropsychologia_ , _28_ (10), 1021–1034. https://doi.org/10.1016/0028-3932(90)90137-d 

- Park, S. A., Miller, D. S., & Boorman, E. D. (2021). Inferences on a multidimensional social hierarchy use a grid-like code. _Nature Neuroscience_ , _24_ (9), Article 9. https://doi.org/10.1038/s41593-021-00916-3 

- Pearl, J. (1984). _Heuristics: Intelligent Search Strategies for Computer Problem Solving_ . AddisonWesley Publishing Company. 

- Pelletier, G., Aridan, N., Fellows, L. K., & Schonberg, T. (2021). A Preferential Role for Ventromedial Prefrontal Cortex in Assessing “the Value of the Whole” in Multiattribute Object Evaluation. _Journal of Neuroscience_ , _41_ (23), 5056–5068. https://doi.org/10.1523/JNEUROSCI.0241-21.2021 

- Peters, J., & D’Esposito, M. (2016). Effects of Medial Orbitofrontal Cortex Lesions on SelfControl in Intertemporal Choice. _Current Biology: CB_ , _26_ (19), 2625–2628. https://doi.org/10.1016/j.cub.2016.07.035 

- Potter, T. C. S., Bryce, N. V., & Hartley, C. A. (2017). Cognitive components underpinning the development of model-based learning. _Developmental Cognitive Neuroscience_ , _25_ , 272–280. https://doi.org/10.1016/j.dcn.2016.10.005 

- Redish, A. D. (2016). Vicarious trial and error. _Nature Reviews Neuroscience_ , _17_ (3), 147–159. https://doi.org/10.1038/nrn.2015.30 

- Rowe, J. B., Owen, A. M., Johnsrude, I. S., & Passingham, R. E. (2001). Imaging the mental components of a planning task. _Neuropsychologia_ , _39_ (3), 315–327. https://doi.org/10.1016/S0028-3932(00)00109-3 

- Russell, S. J., & Norvig, P. (2016). _Artificial intelligence: A modern approach_ . Pearson. https://thuvienso.hoasen.edu.vn/handle/123456789/8967 

- Schneider, B., & Koenigs, M. (2017). Human lesion studies of ventromedial prefrontal cortex. _Neuropsychologia_ , _107_ , 84–93. https://doi.org/10.1016/j.neuropsychologia.2017.09.035 

- Schuck, N. W., Cai, M. B., Wilson, R. C., & Niv, Y. (2016). Human orbitofrontal cortex represents a cognitive map of state space. _Neuron_ , _91_ (6), 1402–1412. 

- Sellitto, M., Ciaramelli, E., & di Pellegrino, G. (2010). Myopic discounting of future rewards after medial orbitofrontal damage in humans. _The Journal of Neuroscience: The Official Journal of the Society for Neuroscience_ , _30_ (49), 16429–16436. https://doi.org/10.1523/JNEUROSCI.2516-10.2010 

21 

Sezener, C. E., Dezfouli, A., & Keramati, M. (2019). Optimizing the depth and the direction of prospective planning using information values. _PLOS Computational Biology_ , _15_ (3), e1006827. https://doi.org/10.1371/journal.pcbi.1006827 

Shallice, T., & Burgess, P. (1991). Deficits in strategy application following frontal lobe damage in man. _Brain_ , _114_ (2), 727–741. https://doi.org/10.1093/brain/114.2.727 Shannon, C. E. (1950). XXII. Programming a computer for playing chess. _The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science_ . https://doi.org/10.1080/14786445008521796 

Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J., Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., & Hassabis, D. (2016). Mastering the game of Go with deep neural networks and tree search. _Nature_ , _529_ (7587), 484–489. https://doi.org/10.1038/nature16961 

- Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M., Bolton, A., Chen, Y., Lillicrap, T., Hui, F., Sifre, L., van den Driessche, G., Graepel, T., & Hassabis, D. (2017). Mastering the game of Go without human knowledge. _Nature_ , _550_ (7676), 354–359. https://doi.org/10.1038/nature24270 

- Snider, J., Lee, D., Poizner, H., & Gepshtein, S. (2015). Prospective Optimization with Limited Resources. _PLOS Computational Biology_ , _11_ (9), e1004501. https://doi.org/10.1371/journal.pcbi.1004501 

- Solway, A., & Botvinick, M. M. (2015). Evidence integration in model-based tree search. _Proceedings of the National Academy of Sciences_ , _112_ (37), 11708–11713. https://doi.org/10.1073/pnas.1505483112 

- Solway, A., Diuk, C., Córdova, N., Yee, D., Barto, A. G., Niv, Y., & Botvinick, M. M. (2014). Optimal Behavioral Hierarchy. _PLOS Computational Biology_ , _10_ (8), e1003779. https://doi.org/10.1371/journal.pcbi.1003779 

- Tranel, D., Hathaway-Nepple, J., & Anderson, S. W. (2007). Impaired behavior on real-world tasks following damage to the ventromedial prefrontal cortex. _Journal of Clinical and Experimental Neuropsychology_ , _29_ (3), 319–332. https://doi.org/10.1080/13803390600701376 

- Vaidya, A. R., & Fellows, L. K. (2015). Ventromedial Frontal Cortex Is Critical for Guiding Attention to Reward-Predictive Visual Features in Humans. _Journal of Neuroscience_ , _35_ (37), 12813–12823. https://doi.org/10.1523/JNEUROSCI.1607-15.2015 

- Vaidya, A. R., Sefranek, M., & Fellows, L. K. (2018). Ventromedial Frontal Lobe Damage Alters how Specific Attributes are Weighed in Subjective Valuation. _Cerebral Cortex (New York, N.Y.: 1991)_ , _28_ (11), 3857–3867. https://doi.org/10.1093/cercor/bhx246 

- van Opheusden, B., Kuperwajs, I., Galbiati, G., Bnaya, Z., Li, Y., & Ma, W. J. (2023). Expertise increases planning depth in human gameplay. _Nature_ , _618_ (7967), 1000–1005. 

- Vikbladh, O. M., Meager, M. R., King, J., Blackmon, K., Devinsky, O., Shohamy, D., Burgess, N., & Daw, N. D. (2019). Hippocampal Contributions to Model-Based Planning and Spatial Memory. _Neuron_ , _102_ (3), 683-693.e4. https://doi.org/10.1016/j.neuron.2019.02.014 

- Wang, F., Schoenbaum, G., & Kahnt, T. (2020). Interactions between human orbitofrontal cortex and hippocampus support model-based inference. _PLoS Biology_ , _18_ (1), e3000578. 

- Wilson, R. C., Takahashi, Y. K., Schoenbaum, G., & Niv, Y. (2014). Orbitofrontal Cortex as a Cognitive Map of Task Space. _Neuron_ , _81_ (2), 267–279. https://doi.org/10.1016/j.neuron.2013.11.005 

- Worbe, Y., Palminteri, S., Savulich, G., Daw, N. D., Fernandez-Egea, E., Robbins, T. W., & Voon, V. (2016). Valence-dependent influence of serotonin depletion on model-based choice strategy. _Molecular Psychiatry_ , _21_ (5), 624–629. https://doi.org/10.1038/mp.2015.46 

22 

Yu, L. Q., Kan, I. P., & Kable, J. W. (2020). Beyond a rod through the skull: A systematic review of lesion studies of the human ventromedial frontal lobe. _Cognitive Neuropsychology_ , _37_ (1– 2), 97–141. https://doi.org/10.1080/02643294.2019.1690981 

Zeithamova, D., Dominick, A. L., & Preston, A. R. (2012). Hippocampal and Ventral Medial Prefrontal Activation during Retrieval-Mediated Learning Supports Novel Inference. _Neuron_ , _75_ (1), 168–179. https://doi.org/10.1016/j.neuron.2012.05.010 

## **Author Contributions** 

E.H., B.v.O., W.J.M. and S.M contributed to conceptualization of the research. E.H., H.W., and P.L. collected data. E.H., B.v.O., J.Grohn, W.J.M and S.M. developed methodology. E.H., B.v.O., I.M. and J.Grogan contributed software. E.H. and B.v.O. carried out formal analyses. E.H. wrote the paper. All authors contributed to editing the paper. 

## **Acknowledgements** 

This research was funded an Oxford NIHR BRC, the McDonnell foundation and an MRC clinician scientist fellowship (MR/P00878X to S.G.M). Research was also funded in part by the Wellcome Trust (Grant number 222347/Z/21/Z to E.H.). For the purpose of Open Access, we have applied a CC BY public copyright licence to any author-accepted manuscript version arising from this submission. The funders had no role in study design, data collection and analysis, or preparation of the paper. We thank Jill O’Reilly and Matthias Raemaekers for helpful discussions of this work, Dan Drew and Ayat Abdurahman for help with the TwoStep task data collection, and Daisy Lin, Tylier Seip and Ionatan Kuperwajs for help with the Four-in-a-Row modelling. 

## **Competing Interests** 

The authors declare no competing interests. 

23 

## **Supplementary Information** 

**==> picture [477 x 283] intentionally omitted <==**

**Supplementary Figure 1. Individual lesion maps in Study 1 (Four-in-a-Row).** 

24 

## _Illustration of MF and MB behaviour_ 

**==> picture [451 x 299] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b n.s. c<br>n.s.<br>d model-free agent e model-based agent f all participants g n.s.<br>n.s.<br>**----- End of picture text -----**<br>


**Supplementary Figure 2. Study 2 Behaviour (Two-Step Task). (a)** Average proportion of rewarded trials plotted by the trial number following a shift in reward contingency. The rewarded shape changed every 32 trials. Colour depicts group, confidence intervals depict s.e.m. **(b)** Proportion of trials where the participant received reward across the experiment for each group. Error bars depict s.e.m, dots show individual data points. **(c)** Step 2 choice response times plotted for the three groups (colour), split by whether the transition experienced was common or rare (circle shows common, star shows rare). Error bars depict s.e.m, and pale lines show response times for individual participants. Stars depict significance, corresponding to the fact that in each group participants slow down after experiencing a rare transition. Within all groups, participants slow down following a rare versus common transition, showing sensitivity to the general transition probabilities in the task. **(d)** Analysis of stay probabilities from a simulated model-free agent (who ignores the transition structure between Step 1 and Step 2). Probability of repeating the same choice is plotted as a function of the previous outcome (reward or no reward), and the previous transition experienced (common or rare). **(e)** Same as (d) for a simulated model-based agent, who takes into account the transition probabilities between steps when updating choice values. **(f)** Same as (d) across all participants from the empirical data-set. **(g)** Modulation of stay behaviour as a function of previous outcome and transition. The outcometransition interaction beta weights are plotted by lesion group, where higher beta values indicate more ‘model-based’ modulation of behaviour. Error bars depict s.e.m, dots show individual data points. 

## _RL Model Validation_ 

While the reinforcement learning model in this paper has been widely used in the literature (Decker et al., 2016;  Potter, Bryce et al. 2017, Nussenbaum et al. 2020), this dataset was collected using an adapted version of the Two-Step Task with stationary rather than drifting 

25 

reward probabilities. For this reason, it was important to check that critical parameter values could still be recovered in the new task variant, where reward probabilities were stationary with abrupt shifts. 

Behaviour was simulated for 70 participants using the actual transitions (rare/common) and reward probability structure experienced by the 70 participants in our dataset. For each simulated participant, the six parameters were sampled from a normal distribution based on the range reported in Decker et al. 2016 (mean and standard deviation from this range). The participant data was then fit using the same procedure described in ‘Model Fitting’. The parameters were recoverable in the adapted version of the task ( **Fig. S3** ). 

**==> picture [399 x 290] intentionally omitted <==**

**Supplementary Figure 3. Parameter recoverability for Two-Step Task.** The six reinforcement learning parameters were simulated using the range reported in Decker et al. 2016. Dots show individual simulated data sets for the 70 empirical schedules. Titles refer to the Pearson’s R between simulated and recovered parameters in each case. 

## _RL Model Fitting_ 

A Bayesian hierarchical modelling framework was used to fit the reinforcement learning models to behaviour, allowing us to pool data across participants to improve individual parameter estimates. To aid model fitting in stan, we used reparameterization to sample parameters as centred standard normal distributions (which facilitate gradient calculations in stan), which were then transformed into the appropriate prior distributions. Group-level parameters for means and variances were sampled from the following distributions: 

26 

**==> picture [197 x 22] intentionally omitted <==**

**==> picture [68 x 15] intentionally omitted <==**

**==> picture [263 x 20] intentionally omitted <==**

Group-level variance was defined as a lognormal distribution to ensure only positive values. 

For all parameters with the exception of _p_ (for which the appropriate prior distribution is a centred normal distribution) parameter transformations were used to enforce constraints and impose uniform prior distributions across the appropriate ranges. Parameters were transformed using an approximation of the phi function (i.e. normal cumulative density function), which leads to a uniform prior over the constrained range when applying the cumulative density function to a normal distribution: 

**==> picture [59 x 15] intentionally omitted <==**

**==> picture [55 x 14] intentionally omitted <==**

**==> picture [110 x 22] intentionally omitted <==**

**==> picture [106 x 15] intentionally omitted <==**

**==> picture [156 x 17] intentionally omitted <==**

This constrains 𝛼 and  𝜆 to have a uniform prior on (0,1), and constrains 𝛽𝑚𝑏, 𝛽𝑚𝑓, and 𝛽𝑠𝑡𝑒𝑝−𝑡𝑤𝑜 to have a uniform prior on (0,10). 

_i i i_ The individual-level parameters for the _i_ th participant ( _p[i]_ , 𝛼 _[ i]_ , 𝜆 _[ i]_ , 𝛽𝑚𝑏 , 𝛽𝑚𝑓 and 𝛽𝑠𝑡𝑒𝑝−𝑡𝑤𝑜 ) were given a normal distribution with the mean as the prior on group mean, and variance as the prior on group variance. The individual-level parameters were then also transformed using the phi function to enforce constraints. For example, in the case of 𝛼[𝑖] : 

**==> picture [95 x 16] intentionally omitted <==**

Models were coded in the Stan modelling language (Carpenter et al. 2017), and fitted to each dataset using the Cmdstanpy interface. Datasets were fit with 4 chains, using 1000 samples per chains (warmup 500). R-hat values ≤ 1.1 indicated convergence across all parameters. Following previous studies (Decker et al. 2016; Bryce et al. 2017), we did not include the first 9 choice trials in the analysis. 

_RL parameters across groups_ 

27 

In the main results, we reported tests for the a priori hypothesis that model-based planning would be lower in vmPFC patients, which we found was not the case. We had no other a priori hypotheses about parameters from the reinforcement learning model. We therefore performed exploratory analyses to determine if there was an effect of any group using Kruskal-Wallis non-parametric tests since assumptions of normality were violated in each case. None of the five remaining parameters from the RL model showed any significant differences as a result of group (Kruskal-Wallis tests; model-based weight: _H_ (2)=5.19, _p_ =0.075; model-free weight: _H_ (2)=0.60, _p_ =0.741; Step 2 beta: _H_ (2)=0.640, _p_ =0.726; persistence bias: _H_ (2)=5.49, _p_ =0.065; alpha: _H_ (2)=1.03, _p_ =0.597; lambda: _H_ (2)=0.08, _p_ =0.959). 

**==> picture [410 x 327] intentionally omitted <==**

**Supplementary Figure 4. Reinforcement learning model parameters for Two-Step Task.** 

28 

**==> picture [451 x 283] intentionally omitted <==**

**Supplementary Figure 5. Two-Step Task instructions.** Participants were told about contingencies between the two steps (“Your choice of colour influences which two shapes are displayed”), and about the basic reward structure (“There are four possible shapes, but one shape is rewarded more often than not. The rewarded shape may change throughout the task”). However, unlike in some studies e.g. Castro-Rodrigues et al. (2022), they were not explicitly informed of the transition probabilities. 

29 

