## **Schemas, reinforcement learning,** 

## **and the medial prefrontal cortex.** 

_Oded Bein[1*] & Yael Niv[1,2 ]_ 

## _Affiliations_ 

1Princeton Neuroscience Institute and 2Psychology Department, 

Princeton University, Princeton, NJ, 08540, USA. 

*Correspondence: oded.bein@princeton.edu 

Key words: 

Schema, reinforcement learning, orbitofrontal cortex, medial prefrontal cortex, learning, 

memory 

1 

## **Abstract** 

Schemas are rich and complex knowledge structures about the typical unfolding of events in a context. For example, a schema of a lovely dinner at a restaurant. Schemas are central in psychology and neuroscience. Here, we suggest that reinforcement learning (RL), a computational theory of learning the structure of the world and relevant goal-oriented behavior, underlies schema learning. We synthesize literature about schemas and RL to offer that three RL principles might govern the learning of schemas: learning via prediction errors, constructing hierarchical knowledge using hierarchical RL, and dimensionality reduction through learning a simplified and abstract representation of the world. We then offer that the orbito-medial prefrontal cortex is involved in both schemas and RL due to its involvement in dimensionality reduction and in guiding memory reactivation through interactions with posterior brain regions. Finally, we hypothesize that the amount of dimensionality reduction might underlie gradients of involvement along the ventral-dorsal and posterior-anterior axes of the orbito-medial prefrontal cortex. More specific and detailed representations might engage the ventral and posterior parts, while abstraction might shift representations toward the dorsal and anterior parts of the medial prefrontal cortex. 

2 

## **Introduction** 

Imagine entering a restaurant. An influx of knowledge informs you about the likely sequence of occurrences and the relevant set of behaviors. You know you will be seated at a table and given a menu. You will then read the menu and choose your food. After placing your order, you will receive a delicious meal, and maybe a glass of fine wine to go along. This delightful dinner will be followed by paying the bill and leaving the restaurant. The general knowledge of what typically occurs in an event and in what order, as well as the appropriate behavior, is referred to as the “schema” of the event (Alba & Hasher, 1983; Bartlett, 1932; Ghosh & Gilboa, 2014; Schank & Abelson, 1977). While schemas are widely used in psychology and, more recently, in neuroscience, they also remain notoriously elusive and ill-defined (Ghosh & Gilboa, 2014; Gilboa & Marlatte, 2017). Importantly, we still lack a satisfying computational account of how schemas are learned, how they guide behavior, and how they influence perception, attention, learning, and memory. 

Reinforcement learning (RL) offers a computational theory of how we learn the structure of our environment and the relevant behaviors through experience (Sutton & Barto, 2018). RL algorithms have been powerful in accounting for behavioral and neural findings in simplified environments (Dayan & Niv, 2008; Schultz et al., 1997). However, these algorithms suffer from a “curse of dimensionality:” they scale poorly to rich high-dimensional everyday life events (Niv, 2019; Sutton & Barto, 2018). Thus, RL and schemas can be thought of as two ends of a spectrum: at the one end, highly rich and ecological knowledge structures that lack a satisfying computational account. At the other end, a detailed account that is dissatisfying in the complexity of the phenomena it explains. Can we bring these seemingly disparate fields of research together, and are they indeed so different? 

The goal of this opinion paper is to answer this question. We are motivated by recent neuroscientific research that has emphasized the importance of the medial prefrontal cortex (mPFC) and orbitofrontal cortex (OFC) for both schemas and RL. Within the RL framework, the medial orbitofrontal cortex and ventral part of the medial prefrontal cortex (mOFC/vmPFC) are 

3 

thought to represent a “cognitive map” of the current task[1] (Chan et al., 2016; Klein-Flügge et al., 2022; Schuck et al., 2016; Wilson et al., 2014; Zhou et al., 2020). In RL, this map partitions the task into specific contexts or time points termed “states,” each state including information relevant to guiding behavior in that context. In parallel, memory research on schemas suggests that the mPFC (which includes the mOFC/vmPFC) represents schemas and mediates the influence of schemas on memory (e.g., Baldassano et al., 2018; Bonasia et al., 2018; Gilboa & Marlatte, 2017; Giuliano et al., 2021; van Kesteren et al., 2012; Varga et al., 2022). This colocalization prompted us to explore common mechanisms that might underly RL and schemas. 

Below, we synthesize selected research on schemas and RL to propose that RL and complementary algorithms may provide a computational framework for learning schemas. We focus on three core computational principles that could underly learning schemas: (1) learning a summary of the environment through prediction errors, (2) grouping of states through hierarchical RL, and (3) dimensionality reduction through learning of abstract state representations. We begin with a brief description of schemas and the above three aspects of RL and show how schemas and RL mechanisms are related. We then postulate that the mPFC is involved in both RL and schemas as it mediates dimensionality reduction and guides memory retrieval through communicating with more posterior brain regions. We conclude by postulating that graded recruitment along the ventral-dorsal and anterior-posterior axes of the mPFC might reflect the amount of dimensionality reduction required in a current situation. 

## **A (very) brief introduction to schemas** 

Schemas are associative knowledge structures that organize knowledge of what typically occurs in a context (Bartlett, 1932; Ghosh & Gilboa, 2014; Piaget, 1952; Preston & Eichenbaum, 2013; Rumelhart & Ortony, 1977). Schemas are associative in that they include knowledge of relationships and co-occurrences between units (e.g., menu and food in a restaurant). Here, we predominantly discuss schemas that are extended in time, similar to the notion of ‘scripts’ (Schank & Abelson, 1977) or ‘event schemas’ (Zacks, 2020). Thus, the schemas we discuss 

> 1 Another prominent view within the RL literature proposes that the mOFC/vmPFC represents economic value that guides decisions (Levy & Glimcher, 2012; Padoa-Schioppa & Conen, 2017; for additional theories about these brain areas, see e.g., Delgado et al., 2016). 

4 

include knowledge of the _temporal structure_ of an event. 

Critically, schemas entail knowledge of commonalities extracted over multiple experiences (Ghosh & Gilboa, 2014). Our schema of a restaurant includes the knowledge that typically, we order, wait, and then receive our food. This knowledge was extracted from multiple visits to restaurants in which this sequence occurred. The flip side of including knowledge of the repeated structure of the world is that schemas are, by definition, devoid of details of specific episodes. That we ordered salmon on one specific visit is not likely to become a part of our schema of a restaurant, because it does not occur typically enough (though if we usually order pasta, that may be part of our schema of eating out). 

Schemas can guide behavior as they include knowledge of context-appropriate actions. For example, the knowledge that upon receiving a menu, one should read it and place an order. Finally, schemas can be described as hierarchically organized “modules” that can be shared across schemas: both the restaurant schema and that of having dinner at home can include a module of sitting at the table and eating. Additionally, the schema of an airport can include a restaurant as a module because restaurants are found in airports. Thus, schemas can be a part of other schemas, as well as include other schemas. 

Despite decades of research on the influence of schemas on cognition (Alba & Hasher, 1983; Bartlett, 1932; Gilboa & Marlatte, 2017; Piaget, 1952), it is not completely clear how schemas are learned and how they influence perception, action, learning, and memory (Elman & McRae, 2019; Franklin et al., 2020; Varga et al., 2022). Computational models of semantic networks, as well as models of concepts and category learning (A. M. Collins & Loftus, 1975; A. M. Collins & Quillian, 1969; Kenett et al., 2017; Kumar, 2021; Love et al., 2004; McClelland, McNaughton, & Oreilly, 1995; Murphy, 2004; Rumelhart & Ortony, 1977), characterize some aspects of extracting general knowledge about entities and their co-occurrence, as well as the hierarchical structure of conceptual knowledge, but do not seem to capture fully the scope and richness of schemas. For example, the fact that schemas are characteristically learned through experience that involves having goals, taking actions toward these goals, and learning from the outcomes of said actions. Experience is also dynamic in time and involves temporal information. To incorporate these aspects into a theory of schemas, we turn to the framework 

5 

of RL. 

## **A brief introduction to reinforcement learning** 

Reinforcement learning (RL) provides a set of algorithms for goal-oriented learning and behavior. The goal is typically conceptualized as maximizing reward while minimizing costs or punishments (Sutton & Barto, 2018). Through trial and error over multiple instances, an RL agent learns the sequence of actions most suitable for achieving maximal reward in an environment. 

In RL theory, tasks are divided into a series of discrete time points or contexts, termed “states _”_ . For instance, a visit to a restaurant can be divided into the states of standing at the entrance, sitting down, having a menu in hand, etc. Each of these states can have an associated action policy: standing at the entrance of a restaurant requires us to look for the host and follow their lead; upon obtaining the menu, reading the menu and selecting our desired dish is useful towards our goal of having dinner. States (or state-action pairs) can also have associated values, which denote the (possibly discounted) sum of future rewards expected when in that state (and, for state-action pairs, taking that action). 

As is clear from the example, tasks can be divided into states at different levels of coarseness, and similarly, policies can be defined as single actions or high-level action groupings (see more below). For RL algorithms to learn correct reward-maximizing policies, states only need be “Markovian,” that is, they must include all the information that determines the probability of immediate reward and of subsequently transitioning to each of the states, regardless of the sequence of previous states. For instance, with a menu in hand, if we order food, with high probability we will transfer to the state of having food on our plate, regardless of whether we arrived at the restaurant in a car or used public transportation. 

In addition to learning what actions lead to long-term reward in each state, in a sequential task that extends over time, the agent can learn the probability of transitioning between different states contingent on different actions, that is, the probabilities of different sequences of states (Daw et al., 2005, 2011; Doya et al., 2002). In RL, learning occurs when one encounters a prediction error: a situation in which the actual outcome is different from the 

6 

predicted one (Niv & Schoenbaum, 2008; Rescorla, 1988; Rescorla & Wagner, 1972). Prediction errors include both reward prediction errors, which refer to obtaining more or less reward than expected, and state prediction errors, which refer to transitioning to a different state than expected (with expectations – in the form of values or transition probabilities – obtained from past learning). When encountering a prediction error, the agent adaptively updates their expectations so that these expectations align better with the observed outcome. In this way, through experience, the agent can learn a world model, which includes the representation of states, transitions between them, and the distribution of rewards in each state (this is termed “model-based RL”; Daw et al., 2005). The agent can then mentally simulate actions within the learned world model to determine which action is best in what situation. Alternatively, in “model-free RL,” the agent can learn the optimal policy directly from trial and error using reward prediction errors, without learning a world model. 

From this description, it is already clear how schemas might be mapped to a representation of a task in model-based RL, including the world model and the policy. In what follows, we unpack that mapping, focusing on three aspects: learning through prediction errors, hierarchical organization of task representations, and the development of an efficient state representation through dimensionality reduction (Figure 1). 

7 

**==> picture [381 x 535] intentionally omitted <==**

_Figure 1._ Three reinforcement learning principles contribute to schema learning. Circles represent states/time points in the schema or the episode, with different shades and colors representing different features of states. Top: Prediction errors, namely, the difference between the schema-based predictions (top) and the evidence from a specific episode (bottom), drive schema update (middle). This eventually converges to the typical unfolding of events. The episode and schemas to be updated are selected through latent cause inference, illustrated by the green circles ‘selected’ from the grey ones in the stream of experience. Middle: dimensionality reduction, implemented via schema-guided attention, mediates the elimination of episodic details that differ in each episode (symbols dimension), and the inclusion of goal-relevant information as well as repeating, but not necessarily goal-relevant information (purple dimension). Bottom:  schemas’ hierarchical structures are learned via identifying subgoals (yellow) that chunk sub-schemas. 

8 

## **Are schemas learned through prediction errors?** 

Since RL algorithms use prediction-error driven learning, the first question we ask is whether schemas are also learned and updated via prediction errors (Fig. 1, top). Before diving into studies supporting this view and outlining outstanding questions, it is useful to mention briefly an additional hypothesis: that a summary of the typical and repeating structure of the world is learned by tracking the frequency of occurrences (termed “unsupervised learning”; e.g., Kumar, 2021). In the frequency hypothesis, learning does not require a prediction and an update following an error – each experience leads to an update of associations between contiguous events. 

In animal learning, the discovery of the phenomenon of “blocking” (Kamin, 1968, 1969) led theorists to shift from assuming that contiguity is sufficient for associative learning to considering prediction errors as the main force driving learning. In blocking, a stimulus previously associated with a motivationally relevant outcome (e.g., an electric shock or food) prevents a co-occurring neutral stimulus from also becoming associated with the same outcome. The idea is that because the first stimulus fully predicts the outcome, there is no prediction error when the outcome occurs, and thus learning about the association with the newly added stimulus is “blocked” (Rescorla, 1988; Rescorla & Wagner, 1972). In humans, a wealth of research shows that reward prediction errors drive learning (d’Acremont et al., 2013; Niv & Langdon, 2016; Niv & Schoenbaum, 2008) and facilitate long-term memory (Ergo et al., 2020; Greve et al., 2019; Rouhani et al., 2018; Rouhani & Niv, 2021). 

To establish that prediction errors drive schema learning, one can modify transition probabilities between states and test whether the resulting state prediction errors lead to updating of that model of the world (the schema) and to changes in behavior. Recent work hints at this process. In rodents, Sharpe and colleagues demonstrated blocking of learning of simple stimulus-stimulus associations (without rewards or otherwise motivationally relevant stimuli), showing that learning such “neutral” associations is also driven by prediction errors (Sharpe et al., 2017, 2020). Computational models that learn via state prediction errors have been shown to explain choice data in studies that involved frequent changes (reversals) of either transition probabilities or the state structure in humans (Momennejad et al., 2017; Sharp 

9 

et al., 2021, 2022) and animals (Akam et al., 2021; Bartolo & Averbeck, 2020). Other studies involved extensive training of participants on state transitions, and found enhanced memory of items that violated these transitions (Bein et al., 2021; Greve et al., 2017; Kafkas & Montaldi, 2018; for reviews, see Henson & Gagnepain, 2010; Quent et al., 2021). Additionally, memory was reduced for items that cued a future state that was (surprisingly) not transitioned to (G. Kim et al., 2014; H. Kim et al., 2020). Enhanced memory for violations together with reduced memory for items that elicited predictions that were violated is consistent with updating a model of the world. These studies, which focused on learning over a few trials or sessions, provide evidence that initial learning of schemas might be driven by state prediction errors. 

An interesting question is whether updating of established and consolidated schemas uses the same mechanism. Compared to newly learned knowledge, consolidated and welllearned knowledge is thought to be (1) stable and less amenable to change, (2) largely supported by cortical structures (whereas newly-acquired knowledge is supported by the hippocampus, see Box 1), and (3) more abstract and including fewer specific episodic details (Antony & Schapiro, 2019; Frankland & Bontempi, 2005; Gilboa & Moscovitch, 2021; Moscovitch et al., 2016; Squire & Alvarez, 1995). We are not aware of studies that directly tested whether changes to established models of the world are learned and updated via state prediction errors. 

Another aspect of the prediction-error account of schema learning is that it requires having predictions. Otherwise, there is no error. In contrast, the frequency account does not require prediction prior to the update. Behavioral studies have linked prediction strength to memory for violations, providing evidence that memory enhancement is indeed related to forming predictions (Bein et al., 2021; Greve et al., 2017). Further, explicitly generating a prediction before being provided with a piece of violating information boosted memory for that information (Brod et al., 2018, 2020). fMRI studies additionally showed that better predictions, defined as higher accuracy of decoding a predicted category from multivoxel BOLD activity patterns, correlated with better memory for violations of those predictions (H. Kim et al., 2020; see also Long et al., 2016 for related findings). 

By showing that prediction errors facilitate learning and memory of the structure of the 

10 

environment, the studies surveyed here lay the ground for our proposal that prediction errors facilitate learning and updating of schemas. However, these studies were mostly done in simplified environments that trained participants only on one or few associations. It is not clear that their findings generalize to updating of complex and well-learned associative structures that are characteristic of schemas, as work in humans shows that complex semantic knowledge can both impair and enhance learning and memory of new associations (Anderson & Reder, 1999; Bein et al., 2019; Bellana et al., 2021; Gasser & Davachi, 2022; Reder et al., 2007; Tompary & Thompson-Schill, 2021). 

One example of this complexity is that in everyday life, cues and outcomes are not as clearly defined as in many of the studies mentioned here, but rather dynamically evolve in time, and span multiple temporal scales (Brunec & Momennejad, 2022; Gravina & Sederberg, 2017; Lee et al., 2021). In one study that extends ideas about the effects of prediction errors on memory updating to such a scenario, Sinclair and colleagues (2018) used rich movie-clip stimuli to elicit predictions of action outcomes that had been learned over a lifetime of experience, for example, a baseball batter hitting a home run. They then violated these predictions by stopping the movie before the expected outcome, essentially omitting the outcome. Participants were then presented with another, semantically related movie clip. In a subsequent memory test of the original clips, the researchers found that participants recalled details from the related clips as if they were in the original clip, and this happened more frequently if the original clip was stopped as compared to when it was played fully, suggesting that stopping the clips leads to more memory intrusions from related clips (Sinclair et al., 2021; Sinclair & Barense, 2018). These intrusions might reflect memory update of the original movie clips, that was enhanced by violations of everyday life expectations (see also Antony et al., 2020). Of course, in everyday life, experience never stops. Rather, surprise occurs when events unfold in an unexpected way. In sum, while many questions remain open, emerging literature suggests that schemas might indeed be learned and updated via prediction errors, similar to ideas about learning in RL. 

11 

## **Schema hierarchies might be learned, and instantiated, via hierarchical RL and latent cause inference mechanisms** 

As mentioned, schemas are hierarchically organized: each schema can be composed of subschemas and might be a subschema of another, larger schema. Hierarchical RL algorithms (Badre, 2008; Barto & Mahadevan, 2003; Botvinick, 2008, 2012; Botvinick et al., 2009; A. G. E. Collins, 2018; Correa et al., 2022; Tomov et al., 2020) might provide a blueprint for how such a schema hierarchy is acquired (Fig. 1, bottom). In RL, hierarchical RL alleviates the scaling problem (i.e., that learning via RL algorithms becomes prohibitively slow in complex environments) by grouping together states and actions into larger units in a process termed “temporal abstraction” (Barto & Mahadevan, 2003; Sutton et al., 1999). In temporal abstraction, a temporally extended task is divided into different subunits, called “subtasks”. A subtask is defined by states that are possible start states, a policy that includes a sequence of actions and is sometimes called an “option”, the transitional probabilities between states, and a set of termination states (also called “subgoals”) in which the subtask will terminate and cede control back to the overarching model of the entire task (Botvinick et al., 2009; Correa et al., 2022; Solway et al., 2014; Sutton et al., 1999; Tomov et al., 2020). For example, ‘ordering food’ can be a subtask in a restaurant that starts upon receiving a menu, continues with a sequence of actions including reading the menu, deciding on a dish, waiting for the server, and conveying your choices to them, and ends when the subgoal is reached: the server successfully obtained your request. The term “subgoal” is used to distinguish the termination state of the subtask – having conveyed your choices to a staff member – from the final goal of the larger task at hand (having a full stomach). In some hierarchical RL algorithms, reaching a subgoal leads to obtaining a pseudo-reward signal (Botvinick et al., 2009; Diuk et al., 2013; Ribas-Fernandes et al., 2011). This signal allows a standard reward-maximizing algorithm to discover the optimal policy for the subtask using standard RL mechanisms. 

An additional important feature of hierarchical organization is that subtasks can be shared across tasks – the subtask of ‘adding salt,’ which includes some starting state, a series of basic actions, and a termination state, can be shared by both ‘dining at a restaurant’ and ‘having dinner at home’ task. Thus, we offer that such temporal abstraction may play a role in 

12 

how simple sequences of states and actions are grouped into sub-schemas, that are in turn grouped into a sequence comprising a larger schema. 

An important question in hierarchical RL is: how are subgoals selected? In terms of schemas, this will address how continuous experience is segmented into discrete event schemas (Zacks, 2020). Hierarchical RL offers more than one mechanism (Botvinick et al., 2009; Correa et al., 2022; Solway et al., 2014; Tomov et al., 2020). Some ideas draw on statistical learning literature, which has established that as early as infancy, we learn to identify frequently repeating patterns, including hierarchical structures in streams of perceptual input (Frost et al., 2015; Saffran et al., 1996; Saffran & Wilson, 2003; Schapiro & Turk-Browne, 2015; Turk-Browne et al., 2005). Thus, an agent can explore an environment, keeping track of sequences of states and actions that co-occur frequently and identify the transitions between sequences. These transitions are good candidates for becoming subgoals. For example, a state initializing an ‘adding salt’ sequence would lead to a series of states and actions, which upon completion might transition to other sequences, depending on whether we are cooking a chicken dish or seasoning a salad. The end state of ‘salt added’  could turn into a subgoal, towards the final goal of having a delicious dinner (Balaguer et al., 2016; Barto & Mahadevan, 2003; Botvinick, 2012). Other algorithms introduce Bayesian inference to maximize the discovery of optimal hierarchies given the structure of the environment (Solway et al., 2014) while accounting for similarity in the reward probabilities across states and changes in task demands (Tomov et al., 2020), or the cost of planning (Correa et al., 2022). These algorithms rely on repeated experience to construct a hierarchical model of the world. 

Another idea is that salient events trigger the creation of a subgoal. Salient events create an intrinsic reward signal and engage motivation-related neural systems, much like reward (Bunzeck et al., 2010; Bunzeck & Düzel, 2006; E. T. Cowan et al., 2021; Düzel et al., 2010; Kamiński et al., 2018; Murty & Adcock, 2014; Wittmann et al., 2007). Therefore, salient events are suitable for becoming subgoals. Research on event segmentation that focuses on how ongoing and continuous experience is chunked into discrete events (Clewett et al., 2019; Shin & DuBrow, 2021; Zacks, 2020) has shown that saliant changes, termed “event boundaries,” cause humans to segment their experiences, both during perception and as they are stored in 

13 

memory. For example, events that span a boundary are remembered as happening further apart in time from each other, and memory of their temporal order is often impaired compared to that of events not separated by a boundary (Clewett et al., 2020; DuBrow & Davachi, 2013; Ezzyat & Davachi, 2014). This suggests that event boundaries, like subgoals, structure our experiences into discrete, segmented units. Interestingly, this role of structuring of memories has been shown for reward prediction errors as well (Rouhani et al., 2020), consistent with the notion that salient prediction errors can act as subgoals. 

Of note, a mechanism that relies on salient changes to create subgoals does not require repetition (i.e., statistical learning). A change of context, perceptual details, or internal state, can trigger segmentation in the first instance (Clewett et al., 2019; DuBrow et al., 2017; DuBrow & Davachi, 2013; Shin & DuBrow, 2021). This discrete event representation can form a base that future instances will join to build an event schema. This proposal resonates with recent behavioral work in humans suggesting that schema memories can be created rapidly (Tompary et al., 2020; see Box 1 for the importance of initial learning). Such rapid extraction of structure can facilitate goal-oriented learning and behavior in new situations (A. G. E. Collins & Frank, 2013, 2016; Eckstein & Collins, 2020), with additional learning following more experience refining the initial structure to construct the full event schema (Davachi & DuBrow, 2015). 

Latent-cause inference might be the computation by which salient changes might trigger the instantiation of an existing schema or subschema or the initiation of a new (sub)schema. Latent-cause inference is a computational theory of how observations in the world are grouped according to similarity, with each group representing a set of observations that are presumed to stem from similar sources, namely, from a single “latent cause” (Franklin et al., 2020; Gershman & Niv, 2010; Niv, 2019). According to this framework, the latent cause underlying the current observations can be inferred by combining prior knowledge of the probability of various latent causes with evidence from the current external environment using Bayesian inference. When current external observations are sufficiently different from past knowledge, a new latent cause is created (Gershman, 2015; Gershman et al., 2017). For example, upon entering a restaurant, the myriad of perceptual cues (tables set up for dining, customers enjoying their meal, etc.) may lead to the inference that the current relevant schema is that of a dinner in a 

14 

restaurant. However, when entering a restaurant and seeing the chairs organized in front of a screen, you might realize this is a fundraiser, not an ordinary dinner. Thus, it would be adaptive to infer another latent cause, or initiate a completely new one, because the sequence of unfolding events and the relevant behaviors will likely differ from those at a dinner. Inferring a new latent cause would support learning a new state-transition model and submodels and their respective policies. Recent theoretical work has begun to explore how salient changes such as event boundaries might trigger the inference of a new latent cause (Franklin et al., 2020; Shin & DuBrow, 2021) and how that invokes the instantiation of a relevant event schema (Franklin et al., 2020). In sum, we offer that latent-cause inference can be used to instantiate an existing schema, or to initiate a new schema (or subschema). The content of this schema is the model and policy, where the model can include submodels terminating in subgoals that are used to train optimal subpolicies through RL mechanisms. 

## Box 1: Rapid learning in the hippocampus shapes new schemas 

The idea that event boundaries can become subgoals could mean that first instances of events – in which the subgoal is created – might be highly influential in shaping our beliefs about the structure of the world, on which further learning is then based. This is in contrast to the idea that structure is extracted through incremental and relatively slow learning (McClelland, McNaughton, & O’Reilly, 1995; Schapiro & Turk-Browne, 2015). In RL, the parameters with which a model is initialized (which are often random) bias learning and can be hard to overcome (Sutton & Barto, 2018). To avoid this, in many algorithms, the learning rate is high at the beginning of a task and decreases with time. The learning rate effectively determines the weighting on new versus old knowledge, so a high learning rate results in substituting data from initial examples instead of the random parameters from initialization. While this makes sense computationally, it further underscores the idea that early learning is important (Sutton & Barto, 2018). Indeed, Shteingart et al. (2013) showed that human learning is best explained by a learning rate of 1 (maximal rate) on the first trial, and that the first experience is highly influential on choices in future trials. Other studies showed relatively quick learning of regularities (Schapiro et al., 2013; Schapiro & Turk-Browne, 2015) and generalization based on 

15 

such regularities (Tompary et al., 2020) in a single lab session. 

The hippocampus, known to be involved in rapid learning (Eichenbaum, 2004; McClelland, McNaughton, & O’Reilly, 1995; Moscovitch et al., 2016; Norman & O’Reilly, 2003), and event segmentation (Ben-Yakov & Dudai, 2011; Ben-Yakov & Henson, 2018; Clewett et al., 2019), also mediates learning the structure of the environment (Farzanfar et al., 2022; Kumaran et al., 2009; McKenzie et al., 2014; Schapiro et al., 2014, 2016; Shohamy & Turk-Browne, 2013; Theves et al., 2019, 2021). Thus, converging behavioral and neural evidence suggests that rapid initial learning largely shapes our schemas. Another, not mutually exclusive, theoretical proposal for the role of the hippocampus in learning structure attributes relatively slow learning to one hippocampal pathway (entorhinal cortex-subregion CA1) that might underly the extraction of regularities and learning structure, while rapid learning is mediated by another hippocampal pathway (entorhinal cortex-subregions CA3-dentate gyrus-CA1; Schapiro et al., 2017). The proximity of these hippocampal pathways, and the convergence of both in the same hippocampal subregion (CA1), makes the interaction between the pathways a candidate mechanism by which initial learning can quickly sketch a schema, which in turn influences how further slow learning refines that schema. 

----- end of Box 1----- 

## **Dimensionality reduction through selective attention might mediate schema learning** 

Schemas summarize information across multiple multidimensional episodes. In some dimensions, features might repeat across episodes (e.g., upon entering a restaurant, we interact with a host to be seated). Such repeating features could be, but are not necessarily, goal relevant. In other dimensions of experience, features might change each time (e.g., the color of the host’s shirt) and are likely goal irrelevant. Does schema learning simply ‘average’ across features in all dimensions, such that features that repeat across episodes persist, while features that change average out? Or, does schema learning involve goal-sensitive dimensionality reduction, whereby dimensions that include repeating goal relevant features are prioritized, while dimensions that include unique episodic features are down-weighted? 

In RL, an optimal representation of a state focuses on only goal-relevant information in 

16 

the environment (Langdon et al., 2019; Schuck et al., 2018; Sutton & Barto, 2018). The process by which an agent learns what dimensions of the environment are important to a given task has been termed “representation learning” (Niv, 2019), and often involves dimensionality reduction. Through experience, we learn what dimensions of our environment are relevant to our goals and therefore should be attended to, and what dimensions are irrelevant and thus can be ignored. For example, when choosing a meal at a restaurant, the prices of dishes is relevant, but not the location of our table. Research has shown that learning the relevant (i.e., reward-predicting) dimensions of a state guides attention to these dimensions, which in turn prioritizes learning predictions associated with these dimensions (Daniel et al., 2020; Farashahi et al., 2017; Leong et al., 2017; Niv, 2019; Niv et al., 2015; Radulescu et al., 2016, 2019). These studies suggest that goal relevance and selective attention might mediate dimensionality reduction during schema learning. 

However, repetition of features might prioritize learning of goal-irrelevant dimensions. Including goal-irrelevant but regular information in schema representations might be adaptive because it allows flexible behavior when the world changes (Ghosh & Gilboa, 2014; Tolman, 1948). For example, in restaurants, the cashier is typically close to the bar. Although this is mostly goal irrelevant because we pay with a server, it might become useful if ever we are asked to pay at the cashier. Vast literature shows that indeed, we learn regularities, namely, features of the environment that are statistically reliable, even when these are goal irrelevant (for reviews, see Frost et al., 2015; Schapiro & Turk-Browne, 2015; Sherman et al., 2020). Studies suggest that attention is drawn towards repeated but goal-irrelevant information. For example, participants are faster to identify a target stimulus if it appears in a location where, on other trials, regularities existed in a stream of symbols (Zhao et al., 2013). Similarly, memory for item pairs that are semantically congruent and encountered repeatedly in daily life  (e.g., restaurant and menu) is typically enhanced (reduced reaction times and increased accuracy) compared to incongruent pairs that are rarely encountered (e.g., spinach and train; Bein et al., 2015; Gronau, 2021; van Kesteren et al., 2013). This is true even if congruency is task irrelevant (Bein et al., 2015) and pairs are presented only briefly (Gronau, 2021; Gronau et al., 2008). Task-irrelevant congruence also enhances long-term memory (Gronau & Shachar, 2015). 

17 

However, the prediction of a feature in a goal-irrelevant but repeating dimension comes at the expense of later memory of unique episodic details (G. Kim et al., 2014; H. Kim et al., 2020; Sherman & Turk-Browne, 2020). Together, these findings suggest that attentional mechanisms might prioritize the learning of repeating information, goal-relevant or not, potentially at the expense of down-weighting episodic details. 

## Box 2: schemas versus cognitive maps 

Similarly to schemas, a cognitive map is a representation that organizes aspects of an experience, which can be used to flexibly guide behavior (Behrens et al., 2018; Bellmund et al., 2018; Schiller et al., 2015; Tolman, 1948). We suggest that schemas are broader than cognitive maps, and can include additional types of information (Alba & Hasher, 1983; A. M. Collins & Quillian, 1969; Farzanfar et al., 2022; Kumar, 2021; Rumelhart & Ortony, 1977). For example, most conceptualizations of cognitive maps represent information through some notion of distance, which can be physical or mental (Behrens et al., 2018; Bellmund et al., 2018). Indeed, while cognitive maps have been studied extensively in spatial navigation, recent research extended the notion of cognitive maps to non-spatial maps (Constantinescu et al., 2016; Garvert et al., 2017; Park et al., 2020; Schapiro et al., 2013; Tavares et al., 2015; Theves et al., 2019, 2020; Viganò & Piazza, 2020). This work focused predominantly on relationships that can be mapped to distance measures and used such distances to identify neural correlates. Distance is, by definition, symmetric. However, hierarchical semantic relationships that may be important in schemas are not symmetric: menus are found in restaurants, but restaurants are not found in menus. Thus, hierarchical information cannot be mapped to a distance measure in a straightforward way. Interestingly, some frameworks propose that even spatial navigation might rely on strategies or computations that are not based solely on distance (e.g., Brunec et al., 2018; Ekstrom et al., 2020; Farzanfar et al., 2022; Peer et al., 2021; Warren, 2019). ---- end of Box 2 ----- 

18 

## **Orbito-medial PFC involvement in schemas and states: dimensionality reduction and the guidance of memory reactivation in posterior brain regions.** 

There is a wide agreement that the orbitofrontal (OFC) and medial prefrontal cortex (mPFC) are involved in both RL and schema-related processes. However, the functions these regions play are a topic of intense debate (Delgado et al., 2016; Frankland & Bontempi, 2005; Gilboa & Marlatte, 2017; Klein-Flügge et al., 2022; Padoa-Schioppa & Conen, 2017; Stalnaker et al., 2015; Varga et al., 2022; Wilson et al., 2014). In this part, we focus on the medial part of the OFC and ventromedial PFC (mOFC/vmPFC) and the mid-mPFC (the area dorsal to the mOFC/vmPFC on the medial wall, but ventral to the most dorsal part of the mPFC, which is more traditionally thought of as dorsal mPFC), using “mPFC” to collectively refer to these areas. We first summarize findings that suggest that these regions represent both states in RL and schemas. Then we offer that dimensionality reduction in the mPFC might underlie these representations (Varga et al., 2022). We go on to propose that these low-dimensional representations in the mPFC guide memory reactivation in more posterior brain regions. Motivated by the anatomical heterogeneity of the mPFC and its varied connectivity patterns (Cavada et al., 2000; Kahnt et al., 2012; Mackey & Petrides, 2010; Öngür et al., 2003; Price, 2007), we postulate that the gradual involvement of subparts along the ventral-lateral and anterior-posterior axis of the mPFC might be driven by the amount of dimensionality reduction, that is, by levels of specificity vs. abstractions of schemas and states. 

A prominent theory suggests that the mPFC and OFC represent a map of task states, and more specifically, the current state of the task at any point in time (Boorman et al., 2021; KleinFlügge et al., 2022; Vaidya & Badre, 2022; Wilson et al., 2014; Zhou, Gardner, et al., 2021). Recent work indeed shows that a representation of states and the relationships between them can be found in the mOFC/vmPFC as participants navigate a conceptual space (Constantinescu et al., 2016) and sequential structures (Baram et al., 2021; Klein-Flügge et al., 2019; Schapiro et al., 2013), as well as in the absence of active navigation (Viganò & Piazza, 2020). Some theories suggest that the mOFC/vmPFC is particularly needed when states cannot be determined based on perceptual input alone but are latent (like latent causes above) and require the retrieval of information from memory (Boorman et al., 2021; Wilson et al., 2014). Empirically, multivoxel 

19 

activation patterns in mOFC/vmPFC are consistent with Bayesian inference about the current state when this requires integrating retrieved prior memories and current observations (Chan et al., 2016). Another study successfully classified from mOFC/vmPFC activity patterns states that included information from the current and the previous trial, and thus relied on memory (Schuck et al., 2016). 

Findings additionally suggest that the mOFC/vmPFC represents relationships between states. In Schuck et al. (2016), the similarity of mOFC/vmPFC multivoxel activity patterns was higher for states that were more similar in their cognitive function. Similar results were obtained in the social domain (Park et al., 2020; see Mızrak et al., 2021 for findings in the lateral OFC). The mid-mPFC was also found to be sensitive to the transition probability and physical distance between states (Klein-Flügge et al., 2019) and to mediate the retrieval and recombination of memories needed to make choices about novel stimuli (Barron, Dolan, & Behrens, 2013). Together, these studies are consistent with the hypothesis that the mOFC/vmPFC and the mid-mPFC represent states within a cognitive map, in particular when information needs to be retrieved from memory. 

As proposed above, schemas include hierarchically organized states. Further, schemas hold knowledge of what typically occurs in an event, and therefore require retrieving information from memory. Consistent with the view that the mPFC represents latent states that rely on memory, growing evidence demonstrates the involvement of the mPFC in schemas (Gilboa & Marlatte, 2017; Varga et al., 2022). For instance, lesions to the mOFC/vmPFC impair the appropriate deployment of schema knowledge (Ghosh et al., 2014; Gilboa, 2010; Giuliano et al., 2021; Spalding et al., 2015). Activation in the mPFC is modulated by whether information is consistent or inconsistent with schematic knowledge in both humans and rodents (Alonso et al., 2020; Amer et al., 2019; Bonasia et al., 2018; Brod & Shing, 2018; Preston & Eichenbaum, 2013; Reggev et al., 2016; Tse et al., 2007, 2011; van Kesteren et al., 2013; van Kesteren, Rijpkema, et al., 2010; Wang et al., 2012; Yacoby et al., 2021). Moreover, a recent study showed that activation patterns in the mid-mPFC were more similar for events that belonged to the same schema (e.g., different examples of visiting a restaurant) compared to different schemas (visiting a restaurant versus an airport), even when similarity was computed across 

20 

video and audio stimuli, suggesting a schematic representation in the mid-mPFC that goes beyond perceptual features (Baldassano, Hasson, & Norman, 2018). Another study found similar results and added that the similarity of neural representations of a movie to itself (across repetitions) was comparable to its similarity to other movies belonging to the same schema, as if the mPFC predominantly encodes schematic information, and does not differentiate specific instances of schemas (Reagh & Ranganath, 2023); though see MasisObando et al. (2022), who found both schematic and specific movie representations in the mPFC. Together with the finding above that mPFC representations follow Bayesian inference (Chan et al., 2016), these findings strengthen the proposal that schemas are instantiated via Bayesian latent cause inference (Varga et al., 2022). 

The mPFC might represent schemas and states through dimensionality reduction Learning and representing schemas and states both involve dimensionality reduction: the creation of a simplified representation of information (Fig. 2). In an RL task, mid-mPFC activation was correlated with predicted rewards computed based on attending to one relevant task dimension out of three available (Leong et al., 2017; Fig. 2a). More generally, the mOFC/vmPFC has been shown to similarly represent episodes that have similar attentional goals (Günseli & Aly, 2020). Additionally, the mPFC is involved in categorization, especially when categorization relies on extracting rules from multiple instances or developing a summary representation (e.g., prototype; Bowman et al., 2020; Bowman & Zeithamova, 2018; Goldstone et al., 2012; Kumaran et al., 2009; Nosofsky, 1986; Zeithamova et al., 2019). A recent fMRI study used a categorization task and principal component analysis (PCA) to extract the number of orthogonal components that account for variance in mOFC/vmPFC multivoxel activity patterns (Mack et al., 2020; Fig. 2b). A lower number of components was interpreted as a simpler neural representation. Simpler categorization rules corresponded to fewer components needed to explain mOFC/vmPFC activity patterns, consistent with dimensionality reduction (see (Zhou et al., 2020) for a similar finding in rodents, slightly lateral to the mOFC). 

As mentioned above, schemas involve eliminating episodic details to represent a typical course of events, potentially through dimensionality reduction. Studies showing schematic 

21 

representations and a lack of episodic details in the mPFC are consistent with this notion (Baldassano et al., 2018; Reagh & Ranganath, 2023; Fig. 2c). Additional work allows more direct inference of dimensionality reduction. These studies exposed participants to item-scene associations, with some items sharing the same scene (Audrain & McAndrews, 2020; Tompary & Davachi, 2017). After consolidation, the neural representations of items that shared the same scene, but not different scenes, showed stronger similarity to each other in the mid-mPFC. These results suggest that specific episodes (each item-scene pair) were grouped based on a shared feature (the scene), while the details of each episode were reduced, or eliminated, in mid-mPFC representations (Fig. 2d; see Richards et al., 2014 for similar findings in rodents). 

Consistent with our proposal that dimensionality reduction prioritizes goal-relevant as well as repeating but goal-irrelevant dimensions, evidence suggests that the mPFC represents both types of information (Boorman et al., 2021; Moneta et al., 2023; Rushworth et al., 2011; Wilson et al., 2014; Zhou, Gardner, et al., 2021). Regarding goal-relevant dimensions, a wealth of research has established that mPFC activity correlates with subjective preferences ~~e~~ used for goal-oriented behavior, namely, choices aimed toward maximizing reward (Padoa-Schioppa & Conen, 2017; Rushworth et al., 2011). The studies above that support a broader role of the mPFC in representing cognitive maps tested mPFC representations in the service of solving a task, and therefore are goal-oriented (Schuck et al., 2016; Wilson et al., 2014). Studies that found differential activity and connectivity of the mPFC during encoding of semantically congruent (vs. incongruent) information required participants to indicate congruency, thus making semantic knowledge goal relevant (Bein et al., 2014; van Kesteren et al., 2013). This is also the case in mOFC/vmPFC involvement in object recognition tasks that require access to semantic information (Bar et al., 2006). During movie watching, where the mPFC has been shown to represent schemas (Baldassano et al., 2018; Reagh & Ranganath, 2023; van Kesteren, Fernández, et al., 2010), it can be argued that the goal is to understand and interpret the movie, and toward that goal, retrieval of prior semantic knowledge is advantageous. Thus, goalrelevant schematic and state representations are represented in the mPFC. 

Regarding goal-irrelevant information, the mOFC/vmPFC represents the values of outcomes even when these values are task-irrelevant (Lebreton et al., 2009; Moneta et al., 

22 

2023). The mOFC/vmPFC also encoded a map of a two-dimensional well-learned social hierarchy, even in a task that asked participants to make inferences only based on one dimension (Park et al., 2020). Likewise, mid-mPFC representations tracked the structure of a task even when it was goal-irrelevant (Klein-Flügge et al., 2019; for similar findings in rodents, see Zhou et al., 2020; Zhou, Gardner, et al., 2019). The mPFC also seems to be engaged in schema processing even when participants are involved in an unrelated task: mid-mPFC BOLD signal is higher for encoding semantically congruent vs. incongruent information when participants indicate the grammatical correctness of word stimuli, regardless of semantics (Reggev et al., 2016; Yacoby et al., 2021, 2023). In line with dimensionality reduction, similar neural representations of items that share a dimension (e.g., the context of learning) are found in the mOFC/vmPFC when participants perform an unrelated task (E. Cowan et al., 2020; Schlichting et al., 2015). 

Temporal order seems to be an important dimension in mPFC schematic representations. Sequentially – akin to the transition probabilities between states, is an essential part of the world model in model-based RL. Interestingly, scrambling the order of events in a schema disrupts mPFC representation, evidence that mPFC schematic representations retain sequential order (Baldassano et al., 2018). In rodents, lesions to the mPFC impair temporal memory (Chiba et al., 1997). In humans, mPFC lesions specifically impair schema knowledge, while sparing category knowledge (Giuliano et al., 2021). Arguably, the temporal order of events is a critical aspect of schemas but not of categories. The representation of sequential order might be supported by strong anatomical connections to the hippocampus (Barbas & Blatt, 1995; Cavada et al., 2000; Öngür & Price, 2000; Price, 2007), which represents temporal and sequential information (Buzsáki & Tingley, 2018; Davachi & DuBrow, 2015; Eichenbaum, 2014; Kesner & Hunsaker, 2010; Ranganath & Hsieh, 2016). Consistent with that, mPFC-hippocampal functional connectivity supports learning and memory of sequential information (DuBrow & Davachi, 2016; Schapiro et al., 2016). 

23 

**==> picture [474 x 406] intentionally omitted <==**

_Figure 2._ Dimensionality reduction in the mPFC. a. Participants learned that one of three category-dimensions is relevant for obtaining reward. A model that biased attention towards that category best explained behavior, suggesting a dimensionality reduced representation of the task. Activity in the mPFC correlated with values as estimated by that dimensionality reduced representation (Leong et al., 2017). b. Participants categorized bugs based on 1/2/3 dimensions. PCA was used to extract the dimensions of vmPFC multivoxel activity patterns, and dimensionality reduction (‘compression’) was quantified as the % of PCA components that explained 90% of the variance in vmPFC activity patterns, with fewer components mean stronger compression. As participants learned the categories, stronger compression was observed in the vmPFC the simpler was the categorization, suggesting that dimensionality reduction in vmPFC tracked the dimensions of the categories (Mack et al., 2020). c. Participants encoded associations between objects and overlapping scenes. During retrieval, greater neural similarity was observed in the mPFC between objects that appeared with the same scene compared to different (nonoverlapping) scenes during encoding. This greater similarity potentially reflects loss of distinct details, i.e., fewer dimensions in the representation of these objects, based on scene overlap. This study also showed that similarity only emerged following a period of consolidation (remote memories; Tompary and Davachi, 2017). d. Participants watched movie clips showing different instances of schemas. MPFC representations generalized across instances (e.g., all café clips) of schemas, as indicated by instances being relatively similar within the same schema, but different from another schema (top right, Reagh et al., 2023). This indicate reduced dimensions, as specific details of each instance were not represented in the mPFC. Similar representations were also found across visual vs. auditory modalities, but not when the order of events was compromised (left side, Baldassano et al., 2018). This suggest that the modality dimension is reduced in mPFC schematic representations, while sequential information is preserved. 

24 

MPFC schematic representations guide memory reactivation in posterior brain regions. One potential role of schema and state representations in the mPFC is to guide the retrieval of task-relevant knowledge via memory reactivation in posterior brain regions including the hippocampus (Varga et al., 2022). Place et al. (2016) found in rodents electrophysiology that mPFC activity preceded hippocampal activity during memory retrieval. Correspondingly, in humans, magnetoencephalography (MEG) studies found that mOFC/vmPFC activity precedes and correlates with hippocampal activity during retrieval (McCormick et al., 2020). Similarly, during object recognition, activity in the mOFC/vmPFC correlates with and precedes that in ventral-temporal regions involved in object recognition (Bar, 2009; Bar et al., 2006). Mid-mPFC activity also correlated with the persistence (across time) of ventral-temporal and hippocampal representations of items experienced within the same context (Ezzyat & Davachi, 2021). Lesion studies demonstrate causality: in a reversal-learning task that required resolving interference to infer the correct state, mPFC lesions in rodents impaired hippocampal representations that mediated interference resolution (Guise & Shapiro, 2017). In humans, neurotypical participants demonstrate an increase in an N170 EEG signal for familiar versus unfamiliar faces. This increase, which is localized to posterior brain regions and indicates knowledge about familiar faces, is diminished in patients with mOFC/vmPFC lesions (Gilboa & Moscovitch, 2017). MOFC/vmPFC lesions further impair the evaluation of retrieved memories (Hebscher et al., 2016; Hebscher & Gilboa, 2016), which can result in confabulation – retrieval of memories that are irrelevant to a specific context (Gilboa, 2010; Gilboa et al., 2009). 

Studies that specifically target schema instantiation converge on the same idea  (Gilboa & Marlatte, 2017). Consistency versus inconsistency with prior knowledge modulates mPFC functional connectivity towards posterior cortical regions versus the hippocampus, respectively (Alonso et al., 2020; Bein et al., 2014; Bonasia et al., 2018; Preston & Eichenbaum, 2013; van Kesteren et al., 2012, 2013; van Kesteren, Fernández, et al., 2010; van Kesteren, Rijpkema, et al., 2010). These differential interactions support memory encoding and retrieval, suggesting that the mPFC routes the involvement of cortical vs. hippocampal memory systems based on whether information encoded or retrieved is consistent with schematic knowledge or not (van Kesteren et al., 2012). More directly, a recent study showed that the extent of schematic 

25 

representation in the mPFC correlated with the strength of the representation of specific instances of that schema (i.e., a specific movie belonging to that schema) in a posterior medial cortical region (Masís-Obando et al., 2022). 

Dimensionally reduced representation and guided memory retrieval could be used for predictions and inference because both functions rely on the reactivation of learned representations. Indeed, the mPFC is involved in both (Boorman et al., 2021; DeVito et al., 2010; Preston & Eichenbaum, 2013; Rushworth et al., 2011; Sherrill et al., 2023; Spalding et al., 2018; Zhou, Gardner, et al., 2021; Zhou, Zong, et al., 2021). In the case of inference, the retrieval of learned representations is needed to construct an accurate representation of the current situation. Lesion to the mOFC/vmPFC impair both transitive inference (if A > B and B > C, then A > C) and associative inference (if A is associated with B and B is associated with C, then A is associated with C; DeVito et al., 2010; Preston & Eichenbaum, 2013; Spalding et al., 2018). Such inferences might be mediated by similar representations for the A and C items in the mOFC/vmPFC (Morton et al., 2017; Schlichting et al., 2015), consistent with dimensionality reduction. Regarding the prediction of future events, “expected value”, thought to be represented in the mPFC, is by definition a predictive representation. Moreover, several recent studies found neural evidence consistent with prediction of complex events in the mPFC. For instance, with repeated exposure to a movie, mPFC activity patterns that represent segments of the movie shifted back in time, as if predicting future events (Lee et al., 2021). A navigation study showed that activity patterns in the mPFC became more similar across time points when participants navigated toward a goal compared to following a GPS, suggesting prediction of goal location (Brunec & Momennejad, 2022). 

We conclude that the mPFC represents dimensionality-reduced knowledge of the structure of the environment, including both goal-relevant and irrelevant but statisticallyreliable information—the hallmarks of schemas. This representation guides the reactivation of learned representations in other brain regions and can support prediction and inference. We postulate that guiding reactivation might be achieved through different populations of mPFC neurons communicating with different populations of neurons in posterior brain regions, and thus activating different representations in these regions. This suggestion is consistent with 

26 

ideas about the mPFC as a ‘hub’ linking together well-learned and consolidated memories (Frankland & Bontempi, 2005; van Kesteren et al., 2012). Potentially for this reason, the mPFC is critical for tasks involving partially observed states, where memory reactivation is needed, but not for fully observed states (Bradfield et al., 2015; Wilson et al., 2014). 

## Potential gradients of dimensionality reduction along mPFC axes 

The findings reviewed here were reported in different loci in the mPFC. We hypothesize that the level of dimensionality reduction, or the degree to which memories are schematized and lack specific details, might underlie the gradual involvement of subregions along the anterior to posterior and the ventral to dorsal axes of the mPFC[2] . Our proposal is motivated by gradual changes in the anatomical structure and connectivity along the mPFC. While the anatomical properties of the mPFC are a topic of ongoing investigation, there is a wide agreement on a gradual transition from agranular to granular cortex along the posterioranterior axis of the mPFC (Mackey & Petrides, 2010, 2014; Uylings et al., 2010). Whether this is accompanied by differences in functional and structural connectivity is still an open question (Jackson et al., 2020; Kahnt et al., 2012). Along the ventral-dorsal axis, studies in humans and monkeys generally show that the mid-mPFC is connected to posterior medial cortical regions including the precuneus, as well as to the parahippocampal cortex, angular gyrus and anterolateral temporal lobe (Price, 2007). The mOFC/vmPFC cluster, in contrast, is connected to the ventral temporal lobe, the retrosplenial cortex, the hippocampus and entorhinal cortex, as well as parahippocampal and perirhinal cortices (Barbas & Blatt, 1995; Cavada et al., 2000; Öngür & Price, 2000). A recent study found that these changes in functional and structural connectivity are graded along the ventral-dorsal axis of the mPFC (Jackson et al., 2020). 

Abstract representations might recruit more anterior parts of the mPFC, while detailed memories might recruit the posterior mPFC and its connectivity with the hippocampus. Research suggests that the anterior part of the PFC is involved in future or counterfactual states 

> 2 The medial to lateral axis in the OFC, with some focus on the lateral OFC, has been discussed elsewhere, suggesting that while vmPFC/mOFC is involved in latent states that require memory retrieval, the lateral OFC is involved in representing states based on observable information (Rushworth et al., 2011; Stalnaker et al., 2015; Wilson et al., 2014) 

27 

and actions, but not current ones (Boorman et al., 2009, 2011; Haynes et al., 2007; Momennejad & Haynes, 2012, 2013). Further, studies on prospective planning and predictions found a gradient of predictions in mPFC, whereby predictions of the near future are represented more posteriorly and  predictions of the far future are represented more anteriorly (Brunec & Momennejad, 2022; Lee et al., 2021). Potentially, the farther we prospect to the future, the more abstract and less concrete and detailed are our thoughts (Liberman et al., 2002; Trope & Liberman, 2003, 2010), and therefore they are represented more anteriorly. This might be true also for counterfactual thoughts compared to actions and events that have materialized. Additionally, judging values on a relative scale engages a posterior cluster of voxels, compared to making binary decisions which engages a more anterior cluster (Grabenhorst et al., 2008). A relative judgment might require attending to more details, as compared to when making a simpler binary decision. The specific identity of an expected reward has also been found more posteriorly, at least in humans (Howard & Kahnt, 2017, 2021). Finally, studies reporting dimensionality reduction in simple and abstract tasks in the mOFC/vmPFC find a more anterior cluster of voxels (Leong et al., 2017; Mack et al., 2020) compared to studies addressing retrieval of autobiographic memories of specific events (Takashima et al., 2006). 

In terms of connectivity, the more posterior (and ventral) part of the mPFC is connected to the hippocampus (Barbas & Blatt, 1995; Cavada et al., 2000; Öngür & Price, 2000; Price, 2007). The hippocampus is critical for the retrieval of detailed memories that support fine discrimination, potentially through pattern separation, namely, the allocation of distinct representations to similar stimuli (Baker et al., 2016; Bakker et al., 2008; Berron et al., 2016; Leutgeb et al., 2007; Yassa & Stark, 2011). Recent studies have shown that the hippocampus supports fine discrimination of states (Ballard et al., 2019; Jiang et al., 2020; Zhou, MontesinosCartagena, et al., 2019). Thus, the posterior mOFC/vmPFC might guide the retrieval of detailed state representations through interaction with the hippocampus. 

Specificity versus abstraction might also underlie graded involvement from ventral to dorsal mPFC, supported by changes in functional connectivity. For instance, identity-specific expected value representations have been found ventral to general (scalar) expected value 

28 

representations in the mPFC (Howard et al., 2015; McNamee et al., 2013). Further, while retrieval of specific autobiographical memories tends to involve a ventral cluster of voxels (Takashima et al., 2006), a study addressing rule learning that requires abstraction across multiple episodes showed a mid-mPFC activation (Sweegers et al., 2014). While the mOFC/vmPFC is connected to the hippocampus (important for detailed memories), the midmPFC is functionally connected with the posterior medial cortex (Jackson et al., 2020; Kahnt et al., 2012; Price, 2007). The posterior medial cortex has been shown to represent events over large timescales, potentially abstracting away more specific details (Baldassano et al., 2017; Chen et al., 2017; Hasson et al., 2015; Masís-Obando et al., 2022). Of note, the studies mentioned here employed different learning protocols and stimuli. Nevertheless, they are in line with our proposal that the extent of dimensionality reduction underlies differential involvement of mPFC subregions, and the change in connectivity patterns along mPFC axes. 

Abstraction or schematization are related to consolidation, namely, the transformation of memories in the brain over time (Alvarez & Squire, 1994; Antony & Schapiro, 2019; Gilboa & Moscovitch, 2021; Nadel et al., 2000). Consolidated memories tend to be more schematic and involve fewer specific details (Gilboa & Moscovitch, 2021; Moscovitch et al., 2016; Robin & Moscovitch, 2017). Thus, consolidation may also play a part in whether more ventral or dorsal mPFC subregions are involved in event schemas and states. For example, studies examining the integration of memory representations show a ventral cluster immediately after learning or only 1-day of consolidation (E. Cowan et al., 2020; Schlichting et al., 2015). However, a more dorsal cluster in the mid-mPFC is revealed after one week (Tompary & Davachi, 2017), or for well-consolidated schemes (Baldassano et al., 2018). Given that the retrieval of consolidated but specific autobiographical memories involves the mOFC/vmPFC, it is possible that more consolidated memories involve more dorsal regions because these memories are more abstract, but this should be directly tested. 

Other proposals for mPFC function have been made, such as the ~~m~~ evaluation of retrieved memories (Hebscher & Gilboa, 2016), indicating confidence (Barron et al., 2015; Hebscher & Gilboa, 2016), or signaling the match between prior schemas and perceptual information (van Kesteren et al., 2012). In our view, recent studies that examined multivoxel 

29 

activity patterns better support state or schematic representations, because these studies show different representations for memories that are retrieved with similar confidence levels or that have similar levels of match to prior memories (Masís-Obando et al., 2022; Schuck et al., 2016; Tompary & Davachi, 2017). Coding of different identities of equally valued stimuli is also consistent with our proposal (McNamee et al., 2013; for reviews, see Howard & Kahnt, 2021; Zhou, Gardner, et al., 2021). An interesting possibility is that multiple codes exist in the mPFC: different populations of neurons might represent different states and schemas, leading to the multivariate effects reviewed here, whereas the overall level of activity in the neurons (total firing rate or average BOLD signal) can signal value, match with prior memories or other monitoring signals. Indeed a recent rodent study found a multiplicity of codes more laterally in the OFC (Zhou et al., 2020), and similar notions can potentially explain mPFC coding as well. 

## **Conclusion** 

We outlined how RL, state representations, and event schemas might be related. We proposed that schemas might be learned via RL-related mechanisms such as learning through prediction errors, hierarchical RL, and dimensionality reduction. We then hypothesized that dimensionality reduction might underlie the involvement of the mPFC in both schemas and reinforcement learning and postulated that the extent of abstraction might determine the locus of involvement along mPFC axes. Broadly, we hope to facilitate integration of the fields of learning and memory (e.g., Biderman et al., 2020; Ergo et al., 2020; Hartley et al., 2021), to advance our understanding of human cognition and how it is implemented in the brain. 

30 

## _References_ 

Akam, T., Rodrigues-Vaz, I., Marcelo, I., Zhang, X., Pereira, M., Oliveira, R. F., Dayan, P., & Costa, R. M. (2021). The Anterior Cingulate Cortex Predicts Future States to Mediate ModelBased Action Selection. _Neuron_ , _109_ (1), 149-163.e7. 

https://doi.org/10.1016/j.neuron.2020.10.013 

Alba, J. W., & Hasher, L. (1983). Is memory schematic? _Psychological Bulletin_ , _93_ (2), 203–231. https://doi.org/10.1037//0033-2909.93.2.203 

Alonso, A., van der Meij, J., Tse, D., & Genzel, L. (2020). Naïve to expert: Considering the role of previous knowledge in memory. _Brain and Neuroscience Advances_ , _4_ , 239821282094868. https://doi.org/10.1177/2398212820948686 

Alvarez, P., & Squire, L. R. (1994). Memory consolidation and the medial temporal lobe: A 

simple network model. _Proceedings of the National Academy of Sciences of the United States of America_ , _91_ (15), 7041–7045. https://doi.org/10.1073/pnas.91.15.7041 

Amer, T., Giovanello, K. S., Nichol, D. R., Hasher, L., & Grady, C. L. (2019). Neural Correlates of Enhanced Memory for Meaningful Associations with Age. _Cerebral Cortex_ , _29_ (11), 4568– 4579. https://doi.org/10.1093/cercor/bhy334 

Anderson, J. R., & Reder, L. M. (1999). The fan effect: New results and new theories. _Journal of Experimental Psychology: General_ , _128_ (2), 186–197. https://doi.org/10.1037/00963445.128.2.186 

Antony, J. W., Hartshorne, T. H., Pomeroy, K., Gureckis, T. M., Hasson, U., McDougle, S. D., & 

Norman, K. A. (2020). Behavioral, Physiological, and Neural Signatures of Surprise during 

31 

Naturalistic Sports Viewing. _Neuron_ , 1–14. 

https://doi.org/10.1016/j.neuron.2020.10.029 

Antony, J. W., & Schapiro, A. C. (2019). Active and effective replay: Systems consolidation 

reconsidered again. _Nature Reviews Neuroscience_ , _20_ (8), 506–507. https://doi.org/10.1038/s41583-019-0191-8 

Audrain, S., & McAndrews, M. P. (2020). _Schemas provide a scaffold for neocortical integration at the cost of memory specificity over time_ [Preprint]. Neuroscience. 

https://doi.org/10.1101/2020.10.11.335166 

Badre, D. (2008). Cognitive control, hierarchy, and the rostro-caudal organization of the frontal lobes. _Trends Cogn. Sci._ , _12_ (5), 193–200. https://doi.org/10.1016/j.tics.2008.02.004 

Baker, S., Vieweg, P., Gao, F., Gilboa, A., Wolbers, T., Black, S. E., & Rosenbaum, R. S. (2016). The Human Dentate Gyrus Plays a Necessary Role in Discriminating New Memories. _Curr. Biol._ , _26_ (19), 2629–2634. https://doi.org/10.1016/j.cub.2016.07.081 

Bakker, A., Kirwan, C. B., Miller, M., & Stark, C. E. L. (2008). Pattern separation in the human hippocampal CA3 and dentate gyrus. _Science_ , _319_ (5870), 1640–1642. https://doi.org/10.1126/science.1152882 

Balaguer, J., Spiers, H., Hassabis, D., & Summerfield, C. (2016). Neural Mechanisms of 

Hierarchical Planning in a Virtual Subway Network. _Neuron_ , _90_ (4), 893–903. https://doi.org/10.1016/j.neuron.2016.03.037 

Baldassano, C., Chen, J., Zadbood, A., Pillow, J. W., Hasson, U., & Norman, K. A. (2017). 

Discovering Event Structure in Continuous Narrative Perception and Memory. _Neuron_ , _95_ (3), 709-721.e5. https://doi.org/10.1016/j.neuron.2017.06.041 

32 

Baldassano, C., Hasson, U., & Norman, K. A. (2018). Representation of real-world event schemas during narrative perception. _Journal of Neuroscience_ , _38_ (45), 9689–9699. 

https://doi.org/10.1523/JNEUROSCI.0251-18.2018 

Ballard, I. C., Wagner, A. D., & McClure, S. M. (2019). Hippocampal pattern separation supports reinforcement learning. _Nat. Commun._ , _10_ (1), 1073. https://doi.org/10.1038/s41467019-08998-1 

Bar, M. (2009). The proactive brain: Memory for predictions. _Philos. Trans. R. Soc. Lond. B Biol._ 

_Sci._ , _364_ (1521), 1235–1243. https://doi.org/10.1098/rstb.2008.0310 

Bar, M., Kassam, K. S., Ghuman, A. S., Boshyan, J., Schmid, A. M., Dale, A. M., Hamalainen, M. S., Marinkovic, K., Schacter, D. L., Rosen, B. R., & Halgren, E. (2006). Top-down facilitation of visual recognition. _Proceedings of the National Academy of Sciences_ , _103_ (2), 449–454. https://doi.org/10.1073/pnas.0507062103 

Baram, A. B., Muller, T. H., Nili, H., Garvert, M. M., & Behrens, T. E. J. (2021). Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems. _Neuron_ , _109_ (4), 713-723.e7. 

https://doi.org/10.1016/j.neuron.2020.11.024 

Barbas, H., & Blatt, G. J. (1995). Topographically specific hippocampal projections target 

functionally distinct prefrontal areas in the rhesus monkey. _Hippocampus_ , _5_ (6), 511– 533. https://doi.org/10.1002/hipo.450050604 

Barron, H. C., Garvert, M. M., & Behrens, T. E. J. (2015). Reassessing VMPFC: full of confidence? 

_Nat. Neurosci._ , _18_ (8), 1064–1066. https://doi.org/10.1038/nn.4076 

33 

Bartlett, F. C. (1932). _Remembering: A study in experimental and social psychology_ . Cambridge University Press. 

Barto, A. G., & Mahadevan, S. (2003). Recent Advances in Hierarchical Reinforcement Learning. 

_Discrete Event Dyn. Syst.: Theory Appl._ , _13_ , 41–77. 

Bartolo, R., & Averbeck, B. B. (2020). Prefrontal Cortex Predicts State Switches during Reversal 

Learning. _Neuron_ , _106_ (6), 1044-1054.e4. https://doi.org/10.1016/j.neuron.2020.03.024 Behrens, T. E. J., Muller, T. H., Whittington, J. C. R., Mark, S., Baram, A. B., Stachenfeld, K. L., & Kurth-Nelson, Z. (2018). What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior. _Neuron_ , _100_ (2), 490–509. https://doi.org/10.1016/j.neuron.2018.10.002 

Bein, O., Livneh, N., Reggev, N., Gilead, M., Goshen-Gottstein, Y., & Maril, A. (2015). Delineating the effect of semantic congruency on episodic memory: The role of integration and relatedness. _PLoS ONE_ , _10_ (2), e0115624. 

Bein, O., Plotkin, N. A., & Davachi, L. (2021). Mnemonic prediction errors promote detailed 

memories. _Learn. Mem._ , _28_ (11), 422–434. https://doi.org/10.1101/lm.053410.121 

Bein, O., Reggev, N., & Maril, A. (2014). Prior knowledge influences on hippocampus and medial prefrontal cortex interactions in subsequent memory. _Neuropsychologia_ , _64_ , 320–330. https://doi.org/10.1016/j.neuropsychologia.2014.09.046 

Bein, O., Trzewik, M., & Maril, A. (2019). The role of prior knowledge in incremental associative 

learning: An empirical and computational approach. _J. Mem. Lang._ , _107_ , 1–24. https://doi.org/10.1016/j.jml.2019.03.006 

34 

Bellana, B., Mansour, R., Ladyka-Wojcik, N., Grady, C. L., & Moscovitch, M. (2021). The influence 

of prior knowledge on the formation of detailed and durable memories. _J. Mem. Lang._ , 

_121_ , 104264. https://doi.org/10.1016/j.jml.2021.104264 

Bellmund, J. L. S., Gärdenfors, P., Moser, E. I., & Doeller, C. F. (2018). Navigating cognition: Spatial codes for human thinking. _Science_ , _362_ (6415). 

https://doi.org/10.1126/science.aat6766 

Ben-Yakov, A., & Dudai, Y. (2011). Constructing realistic engrams: Poststimulus activity of 

hippocampus and dorsal striatum predicts subsequent episodic memory. _J. Neurosci._ , _31_ (24), 9032–9042. https://doi.org/10.1523/JNEUROSCI.0702-11.2011 

Ben-Yakov, A., & Henson, R. N. (2018). The Hippocampal Film Editor: Sensitivity and Specificity to Event Boundaries in Continuous Experience. _J. Neurosci._ , _38_ (47), 10057–10068. https://doi.org/10.1523/JNEUROSCI.0524-18.2018 

Berron, D., Schütze, H., Maass, A., Cardenas-Blanco, A., Kuijf, H. J., Kumaran, D., & Düzel, E. (2016). Strong Evidence for Pattern Separation in Human Dentate Gyrus. _J. Neurosci._ , _36_ (29), 7569–7579. https://doi.org/10.1523/JNEUROSCI.0518-16.2016 

Biderman, N., Bakkour, A., & Shohamy, D. (2020). What Are Memories For? The Hippocampus Bridges Past Experience with Future Decisions. _Trends in Cognitive Sciences_ , _24_ (7), 542– 556. https://doi.org/10.1016/j.tics.2020.04.004 

Bonasia, K., Sekeres, M. J., Gilboa, A., Grady, C. L., Winocur, G., & Moscovitch, M. (2018). Prior knowledge modulates the neural substrates of encoding and retrieving naturalistic events at short and long delays. _Neurobiol. Learn. Mem._ , _153_ (Pt A), 26–39. https://doi.org/10.1016/j.nlm.2018.02.017 

35 

Boorman, E. D., Behrens, T. E. J., Woolrich, M. W., & Rushworth, M. F. S. (2009). How green is 

the grass on the other side? Frontopolar cortex and the evidence in favor of alternative courses of action. _Neuron_ , _62_ (5), 733–743. 

https://doi.org/10.1016/j.neuron.2009.05.014 

Boorman, E. D., Behrens, T. E., & Rushworth, M. F. (2011). Counterfactual Choice and Learning in a Neural Network Centered on Human Lateral Frontopolar Cortex. _PLoS Biology_ , _9_ (6), e1001093. https://doi.org/10.1371/journal.pbio.1001093 

Boorman, E. D., Witkowski, P. P., Zhang, Y., & Park, S. A. (2021). The orbital frontal cortex, task structure, and inference. _Behav. Neurosci._ , _135_ (2), 291–300. https://doi.org/10.1037/bne0000465 

Botvinick, M. M. (2008). Hierarchical models of behavior and prefrontal function. _Trends Cogn._ 

_Sci._ , _12_ (5), 201–208. https://doi.org/10.1016/j.tics.2008.02.009 

Botvinick, M. M. (2012). Hierarchical reinforcement learning and decision making. _Curr. Opin. Neurobiol._ , _22_ (6), 956–962. https://doi.org/10.1016/j.conb.2012.05.008 

Botvinick, M. M., Niv, Y., & Barto, A. G. (2009). Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective. _Cognition_ , _113_ (3), 262–280. https://doi.org/10.1016/j.cognition.2008.08.011 

Bowman, C. R., Iwashita, T., & Zeithamova, D. (2020). Tracking prototype and exemplar 

representations in the brain across learning. _eLife_ , _9_ , e59360. https://doi.org/10.7554/eLife.59360 

36 

Bowman, C. R., & Zeithamova, D. (2018). Abstract Memory Representations in the 

Ventromedial Prefrontal Cortex and Hippocampus Support Concept Generalization. _J._ 

_Neurosci._ , _38_ (10), 2605–2614. https://doi.org/10.1523/JNEUROSCI.2811-17.2018 

Bradfield, L. A., Dezfouli, A., van Holstein, M., Chieng, B., & Balleine, B. W. (2015). Medial 

Orbitofrontal Cortex Mediates Outcome Retrieval in Partially Observable Task 

Situations. _Neuron_ , _88_ (6), 1268–1280. https://doi.org/10.1016/j.neuron.2015.10.044 Brod, G., Breitwieser, J., Hasselhorn, M., & Bunge, S. A. (2020). Being proven wrong elicits 

learning in children—But only in those with higher executive function skills. _Dev. Sci._ , _23_ (3), e12916. https://doi.org/10.1111/desc.12916 

Brod, G., Hasselhorn, M., & Bunge, S. A. (2018). When generating a prediction boosts learning: The element of surprise. _Learning and Instruction_ , _55_ , 22–31. 

https://doi.org/10.1016/j.learninstruc.2018.01.013 

Brod, G., & Shing, Y. L. (2018). Specifying the role of the ventromedial prefrontal cortex in 

memory formation. _Neuropsychologia_ , _111_ , 8–15. 

https://doi.org/10.1016/j.neuropsychologia.2018.01.005 

Brunec, I. K., & Momennejad, I. (2022). Predictive Representations in Hippocampal and 

Prefrontal Hierarchies. _The Journal of Neuroscience_ , _42_ (2), 299–312. 

https://doi.org/10.1523/JNEUROSCI.1327-21.2021 

Brunec, I. K., Moscovitch, M., & Barense, M. D. (2018). Boundaries Shape Cognitive 

Representations of Spaces and Events. _Trends Cogn. Sci._ , _22_ (7), 637–650. 

https://doi.org/10.1016/j.tics.2018.03.013 

37 

Bunzeck, N., Dayan, P., Dolan, R. J., & Duzel, E. (2010). A common mechanism for adaptive 

scaling of reward and novelty. _Hum. Brain Mapp._ , _31_ (9), 1380–1394. 

https://doi.org/10.1002/hbm.20939 

Bunzeck, N., & Düzel, E. (2006). Absolute coding of stimulus novelty in the human substantia 

nigra/VTA. _Neuron_ , _51_ (3), 369–379. https://doi.org/10.1016/j.neuron.2006.06.021 Buzsáki, G., & Tingley, D. (2018). Space and Time: The Hippocampus as a Sequence Generator. 

_Trends Cogn. Sci._ , _22_ (10), 853–869. https://doi.org/10.1016/j.tics.2018.07.006 

Cavada, C., Compañy, T., Tejedor, J., Cruz-Rizzolo, R. J., & Reinoso-Suárez, F. (2000). The Anatomical Connections of theMacaque Monkey Orbitofrontal Cortex.A Review. _Cerebral Cortex_ , _10_ , 220–242. 

Chan, S. C. Y., Niv, Y., & Norman, K. A. (2016). A Probability Distribution over Latent Causes, in the Orbitofrontal Cortex. _J. Neurosci._ , _36_ (30), 7817–7828. https://doi.org/10.1523/JNEUROSCI.0659-16.2016 

Chen, J., Leong, Y. C., Honey, C. J., Yong, C. H., Norman, K. A., & Hasson, U. (2017). Shared memories reveal shared structure in neural activity across individuals. _Nat. Neurosci._ , _20_ (1), 115–125. https://doi.org/10.1038/nn.4450 

Chiba, A. A., Kesner, R. P., & Gibson, C. J. (1997). Memory for temporal order of new and familiar spatial location sequences: Role of the medial prefrontal cortex. _Learning & Memory_ , _4_ (4), 311–317. https://doi.org/10.1101/lm.4.4.311 

Clewett, D., DuBrow, S., & Davachi, L. (2019). Transcending time in the brain: How event 

memories are constructed from experience. _Hippocampus_ , _29_ (3), 162–183. https://doi.org/10.1002/hipo.23074 

38 

Clewett, D., Gasser, C., & Davachi, L. (2020). Pupil-linked arousal signals track the temporal 

organization of events in memory. _Nature Communications_ , _11_ (1), 1–14. 

https://doi.org/10.1038/s41467-020-17851-9 

Collins, A. G. E. (2018). Chapter 5—Learning Structures Through Reinforcement. In R. Morris, A. Bornstein, & A. Shenhav (Eds.), _Goal-Directed Decision Making_ (pp. 105–123). Academic Press. https://doi.org/10.1016/B978-0-12-812098-9.00005-X 

Collins, A. G. E., & Frank, M. J. (2013). Cognitive control over learning: Creating, clustering, and generalizing task-set structure. _Psychol. Rev._ , _120_ (1), 190–229. https://doi.org/10.1037/a0030852 

Collins, A. G. E., & Frank, M. J. (2016). Neural signature of hierarchically structured expectations 

predicts clustering and transfer of rule sets in reinforcement learning. _Cognition_ , _152_ , 160–169. https://doi.org/10.1016/j.cognition.2016.04.002 

Collins, A. M., & Loftus, E. F. (1975). Spreading activation theory of semantic processing. 

_Psychological Review_ , _82_ (6), 407–428. https://doi.org/10.1037//0033-295X.82.6.407 

Collins, A. M., & Quillian, M. R. (1969). Retrieval time from semantic memory. _Journal of Verbal Learning and Verbal Behavior_ , _8_ , 240–247. 

Constantinescu, A. O., O’Reilly, J. X., & Behrens, T. E. J. (2016). Organizing conceptual 

knowledge in humans with a gridlike code. _Science_ , _352_ (6292), 1464–1467. 

Correa, C. G., Ho, M. K., Callaway, F., Daw, N. D., & Griffiths, T. L. (2022). _Humans decompose tasks by trading off utility and computational cost_ (arXiv:2211.03890). arXiv. 

http://arxiv.org/abs/2211.03890 

39 

Cowan, E., Liu, A., Henin, S., Kothare, S., Devinsky, O., & Davachi, L. (2020). Sleep Spindles Promote the Restructuring of Memory Representations in Ventromedial Prefrontal 

Cortex through Enhanced Hippocampal-Cortical Functional Connectivity. _J. Neurosci._ , _40_ (9), 1909–1919. https://doi.org/10.1523/JNEUROSCI.1946-19.2020 

Cowan, E. T., Schapiro, A. C., Dunsmoor, J. E., & Murty, V. P. (2021). Memory consolidation as an adaptive process. _Psychon. Bull. Rev._ https://doi.org/10.3758/s13423-021-01978-x d’Acremont, M., Schultz, W., & Bossaerts, P. (2013). The human brain encodes event 

frequencies while forming subjective beliefs. _J. Neurosci._ , _33_ (26), 10887–10897. https://doi.org/10.1523/JNEUROSCI.5829-12.2013 

Daniel, R., Radulescu, A., & Niv, Y. (2020). Intact Reinforcement Learning But Impaired 

Attentional Control During Multidimensional Probabilistic Learning in Older Adults. _The Journal of Neuroscience_ , _40_ (5), 1084–1096. https://doi.org/10.1523/JNEUROSCI.025419.2019 

Davachi, L., & DuBrow, S. (2015). How the hippocampus preserves order: The role of prediction and context. _Trends Cogn. Sci._ , _19_ (2), 92–99. https://doi.org/10.1016/j.tics.2014.12.004 

Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based 

influences on humans’ choices and striatal prediction errors. _Neuron_ , _69_ (6), 1204–1215. https://doi.org/10.1016/j.neuron.2011.02.027 

Daw, N. D., Niv, Y., & Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. _Nature Neuroscience_ , _8_ (12), 1704– 1711. https://doi.org/10.1038/nn1560 

40 

Dayan, P., & Niv, Y. (2008). Reinforcement learning: The good, the bad and the ugly. _Curr. Opin. Neurobiol._ , _18_ (2), 185–196. https://doi.org/10.1016/j.conb.2008.08.003 

Delgado, M. R., Beer, J. S., Fellows, L. K., Huettel, S. A., Platt, M. L., Quirk, G. J., & Schiller, D. 

(2016). Viewpoints: Dialogues on the functional role of the ventromedial prefrontal cortex. _Nat. Neurosci._ , _19_ (12), 1545–1552. https://doi.org/10.1038/nn.4438 

DeVito, L. M., Lykken, C., Kanter, B. R., & Eichenbaum, H. (2010). Prefrontal cortex: Role in acquisition of overlapping associations and transitive inference. _Learning & Memory_ , _17_ (3), 161–167. https://doi.org/10.1101/lm.1685710 

Diuk, C., Tsai, K., Wallis, J., Botvinick, M., & Niv, Y. (2013). Hierarchical learning induces two simultaneous, but separable, prediction errors in human basal ganglia. _J. Neurosci._ , _33_ (13), 5797–5805. https://doi.org/10.1523/JNEUROSCI.5445-12.2013 

Doya, K., Samejima, K., Katagiri, K., & Kawato, M. (2002). _Multiple Model-Based Reinforcement Learning_ . _1369_ , 1347–1369. 

DuBrow, S., & Davachi, L. (2013). The influence of context boundaries on memory for the 

sequential order of events. _Journal of Experimental Psychology: General_ , _142_ (4), 1277– 1286. https://doi.org/10.1037/a0034024 

DuBrow, S., & Davachi, L. (2016). Temporal binding within and across events. _Neurobiol. Learn._ 

_Mem._ , _134 Pt A_ , 107–114. https://doi.org/10.1016/j.nlm.2016.07.011 

DuBrow, S., Rouhani, N., Niv, Y., & Norman, K. A. (2017). Does mental context drift or shift? _Curr Opin Behav Sci_ , _17_ , 141–146. https://doi.org/10.1016/j.cobeha.2017.08.003 

Düzel, E., Bunzeck, N., Guitart-Masip, M., & Düzel, S. (2010). NOvelty-related motivation of 

anticipation and exploration by dopamine (NOMAD): Implications for healthy aging. 

41 

_Neurosci. Biobehav. Rev._ , _34_ (5), 660–669. 

https://doi.org/10.1016/j.neubiorev.2009.08.006 

Eckstein, M. K., & Collins, A. G. E. (2020). Computational evidence for hierarchically structured 

reinforcement learning in humans. _Proc. Natl. Acad. Sci. U. S. A._ , _117_ (47), 29381–29389. https://doi.org/10.1073/pnas.1912330117 

Eichenbaum, H. (2004). Hippocampus: Cognitive processes and neural representations that underlie declarative memory. _Neuron_ , _44_ (1), 109–120. 

https://doi.org/10.1016/j.neuron.2004.08.028 

Eichenbaum, H. (2014). Time cells in the hippocampus: A new dimension for mapping 

memories. _Nature Reviews Neuroscience_ , _15_ (11), 732–744. 

https://doi.org/10.1038/nrn3827 

Ekstrom, A. D., Harootonian, S. K., & Huffman, D. J. (2020). Grid coding, spatial representation, and navigation: Should we assume an isomorphism? _Hippocampus_ , _30_ (4), 422–432. https://doi.org/10.1002/hipo.23175 

Elman, J. L., & McRae, K. (2019). A model of event knowledge. _Psychol. Rev._ , _126_ (2), 252–291. https://doi.org/10.1037/rev0000133 

Ergo, K., De Loof, E., & Verguts, T. (2020). Reward Prediction Error and Declarative Memory. 

_Trends Cogn. Sci._ , _24_ (5), 388–397. https://doi.org/10.1016/j.tics.2020.02.009 

Ezzyat, Y., & Davachi, L. (2014). Similarity breeds proximity: Pattern similarity within and across contexts is related to later mnemonic judgments of temporal proximity. _Neuron_ , _81_ (5), 1179–1189. https://doi.org/10.1016/j.neuron.2014.01.042 

42 

Ezzyat, Y., & Davachi, L. (2021). Neural Evidence for Representational Persistence Within 

Events. _The Journal of Neuroscience_ , _41_ (37), 7909–7920. 

https://doi.org/10.1523/JNEUROSCI.0073-21.2021 

Farashahi, S., Rowe, K., Aslami, Z., Lee, D., & Soltani, A. (2017). Feature-based learning improves adaptability without compromising precision. _Nat. Commun._ , _8_ (1), 1768. https://doi.org/10.1038/s41467-017-01874-w 

Farzanfar, D., Spiers, H. J., Moscovitch, M., & Rosenbaum, R. S. (2022). From cognitive maps to spatial schemas. _Nature Reviews Neuroscience_ . https://doi.org/10.1038/s41583-02200655-9 

Frankland, P. W., & Bontempi, B. (2005). The organization of recent and remote memories. _Nat. Rev. Neurosci._ , _6_ (2), 119–130. https://doi.org/10.1038/nrn1607 

Franklin, N. T., Norman, K. A., Ranganath, C., Zacks, J. M., & Gershman, S. J. (2020). Structured Event Memory: A neuro-symbolic model of event cognition. _Psychol. Rev._ , _127_ (3), 327– 361. https://doi.org/10.1037/rev0000177 

Frost, R., Armstrong, B. C., Siegelman, N., & Christiansen, M. H. (2015). Domain generality versus modality specificity: The paradox of statistical learning. _Trends in Cognitive Sciences_ , _19_ (3), 117–125. https://doi.org/10.1016/j.tics.2014.12.010 

Garvert, M. M., Dolan, R. J., & Behrens, T. E. J. (2017). A map of abstract relational knowledge in 

the human hippocampal–entorhinal cortex. _Elife_ , _6_ , e17086. https://doi.org/10.7554/eLife.17086 

Gasser, C., & Davachi, L. (2022). _Cross-modal facilitation of memory through actions_ [Preprint]. In Review. https://doi.org/10.21203/rs.3.rs-1466467/v1 

43 

Gershman, S. J. (2015). A Unifying Probabilistic View of Associative Learning. _PLoS Comput. Biol._ , _11_ (11), e1004567. https://doi.org/10.1371/journal.pcbi.1004567 

Gershman, S. J., Monfils, M.-H., Norman, K. A., & Niv, Y. (2017). The computational nature of memory modification. _Elife_ , _6_ . https://doi.org/10.7554/eLife.23763 

Gershman, S. J., & Niv, Y. (2010). Learning latent structure: Carving nature at its joints. _Curr._ 

_Opin. Neurobiol._ , _20_ (2), 251–256. https://doi.org/10.1016/j.conb.2010.02.008 

Ghosh, V. E., & Gilboa, A. (2014). What is a memory schema? A historical perspective on current 

neuroscience literature. _Neuropsychologia_ , _53_ (1), 104–114. https://doi.org/10.1016/j.neuropsychologia.2013.11.010 

Ghosh, V. E., Moscovitch, M., Melo Colella, B., & Gilboa, A. (2014). Schema representation in 

patients with ventromedial PFC lesions. _J. Neurosci._ , _34_ (36), 12057–12070. https://doi.org/10.1523/JNEUROSCI.0740-14.2014 

Gilboa, A. (2010). Strategic retrieval, confabulations, and delusions: Theory and data. _Cogn. Neuropsychiatry_ , _15_ (1), 145–180. https://doi.org/10.1080/13546800903056965 Gilboa, A., Alain, C., He, Y., Stuss, D. T., & Moscovitch, M. (2009). Ventromedial prefrontal cortex lesions produce early functional alterations during remote memory retrieval. _J. Neurosci._ , _29_ (15), 4871–4881. https://doi.org/10.1523/JNEUROSCI.5210-08.2009 Gilboa, A., & Marlatte, H. (2017). Neurobiology of Schemas and Schema-Mediated Memory. _Trends in Cognitive Sciences_ , _xx_ , 1–14. https://doi.org/10.1016/j.tics.2017.04.013 Gilboa, A., & Moscovitch, M. (2017). Ventromedial prefrontal cortex generates pre-stimulus 

theta coherence desynchronization: A schema instantiation hypothesis. _Cortex_ , _87_ , 16– 30. https://doi.org/10.1016/j.cortex.2016.10.008 

44 

Gilboa, A., & Moscovitch, M. (2021). No consolidation without representation: Correspondence 

between neural and psychological representations in recent and remote memory. 

_Neuron_ , _109_ (14), 2239–2255. https://doi.org/10.1016/j.neuron.2021.04.025 

Giuliano, A. E., Bonasia, K., Ghosh, V. E., Moscovitch, M., & Gilboa, A. (2021). Differential 

influence of ventromedial prefrontal cortex lesions on neural representations of schema and semantic category knowledge. _J. Cogn. Neurosci._ , 1–28. 

https://doi.org/10.1162/jocn_a_01746 

Goldstone, R. L., Kersten, A., & Carvalho, P. F. (2012). Concepts and Categorization. In 

_Handbook of psychology: Experimental psychology_ (pp. 607–630). John Wiley & Sons, Inc.. 

Grabenhorst, F., Rolls, E. T., & Parris, B. A. (2008). From affective value to decision-making in the prefrontal cortex. _European Journal of Neuroscience_ , _28_ (9), 1930–1939. https://doi.org/10.1111/j.1460-9568.2008.06489.x 

Gravina, M. T., & Sederberg, P. B. (2017). The neural architecture of prediction over a 

continuum of spatiotemporal scales. _Current Opinion in Behavioral Sciences_ , _17_ , 194– 202. https://doi.org/10.1016/j.cobeha.2017.09.001 

Greve, A., Cooper, E., Kaula, A., Anderson, M. C., & Henson, R. (2017). Does prediction error drive one-shot declarative learning? _Journal of Memory and Language_ , _94_ (June), 149– 165. https://doi.org/10.1016/j.jml.2016.11.001 

Greve, A., Cooper, E., Tibon, R., & Henson, R. N. (2019). Knowledge is power: Prior knowledge 

aids memory for both congruent and incongruent events, but in different ways. _Journal_ 

45 

_of Experimental Psychology. General_ , _148_ (2), 325–341. 

https://doi.org/10.1037/xge0000498 

Gronau, N. (2021). To Grasp the World at a Glance: The Role of Attention in Visual and 

Semantic Associative Processing. _J. Imaging Sci. Technol._ , _7_ (9). https://doi.org/10.3390/jimaging7090191 

Gronau, N., Neta, M., & Bar, M. (2008). Integrated Contextual Representation for Objects’ 

Identities and Their Locations. _Journal of Cognitive Neuroscience_ , _20_ (3), 371–388. Gronau, N., & Shachar, M. (2015). Contextual consistency facilitates long-term memory of perceptual detail in barely seen images. _Journal of Experimental Psychology. Human Perception and Performance_ , _41_ (4), 1095–1111. https://doi.org/10.1037/xhp0000071 Guise, K. G., & Shapiro, M. L. (2017). Medial Prefrontal Cortex Reduces Memory Interference by Modifying Hippocampal Encoding. _Neuron_ , _94_ (1), 183-192.e8. https://doi.org/10.1016/j.neuron.2017.03.011 

Günseli, E., & Aly, M. (2020). Preparation for upcoming attentional states in the hippocampus and medial prefrontal cortex. _Elife_ , _9_ . https://doi.org/10.7554/eLife.53191 

Hartley, C. A., Nussenbaum, K., & Cohen, A. O. (2021). Interactive Development of Adaptive Learning and Memory. _Annu. Rev. Dev. Psychol._ , _3_ , 59–85. 

Hasson, U., Chen, J., & Honey, C. J. (2015). Hierarchical process memory: Memory as an integral component of information processing. _Trends Cogn. Sci._ , _19_ (6), 304–313. https://doi.org/10.1016/j.tics.2015.04.006 

46 

Haynes, J.-D., Sakai, K., Rees, G., Gilbert, S., Frith, C., & Passingham, R. E. (2007). Reading 

Hidden Intentions in the Human Brain. _Curr. Biol._ , _17_ (4), 323–328. 

https://doi.org/10.1016/j.cub.2006.11.072 

Hebscher, M., Barkan-Abramski, M., Goldsmith, M., Aharon-Peretz, J., & Gilboa, A. (2016). 

Memory, Decision-Making, and the Ventromedial Prefrontal Cortex (vmPFC): The Roles of Subcallosal and Posterior Orbitofrontal Cortices in Monitoring and Control Processes. _Cerebral Cortex_ , _26_ (12), 4590–4601. https://doi.org/10.1093/cercor/bhv220 

Hebscher, M., & Gilboa, A. (2016). A boost of confidence: The role of the ventromedial prefrontal cortex in memory, decision-making, and schemas. _Neuropsychologia_ , _90_ , 46– 58. https://doi.org/10.1016/j.neuropsychologia.2016.05.003 

Henson, R. N., & Gagnepain, P. (2010). Predictive, interactive multiple memory systems. 

_Hippocampus_ , _20_ (11), 1315–1326. https://doi.org/10.1002/hipo.20857 

Howard, J. D., Gottfried, J. A., Tobler, P. N., & Kahnt, T. (2015). Identity-specific coding of future rewards in the human orbitofrontal cortex. _Proc. Natl. Acad. Sci. U. S. A._ , _112_ (16), 5195– 5200. https://doi.org/10.1073/pnas.1503550112 

Howard, J. D., & Kahnt, T. (2017). Identity-Specific Reward Representations in Orbitofrontal 

Cortex Are Modulated by Selective Devaluation. _J. Neurosci._ , _37_ (10), 2627–2638. https://doi.org/10.1523/JNEUROSCI.3473-16.2017 

Howard, J. D., & Kahnt, T. (2021). To be specific: The role of orbitofrontal cortex in signaling 

reward identity. _Behav. Neurosci._ , _135_ (2), 210–217. 

https://doi.org/10.1037/bne0000455 

47 

Jackson, R. L., Bajada, C. J., Lambon Ralph, M. A., & Cloutman, L. L. (2020). The Graded Change in Connectivity across the Ventromedial Prefrontal Cortex Reveals Distinct Subregions. 

_Cereb. Cortex_ , _30_ (1), 165–180. https://doi.org/10.1093/cercor/bhz079 

Jiang, J., Wang, S.-F., Guo, W., Fernandez, C., & Wagner, A. D. (2020). Prefrontal reinstatement of contextual task demand is predicted by separable hippocampal patterns. _Nat. Commun._ , _11_ (1), 2053. https://doi.org/10.1038/s41467-020-15928-z 

Kafkas, A., & Montaldi, D. (2018). Expectation affects learning and modulates memory 

experience at retrieval. _Cognition_ , _180_ , 123–134. https://doi.org/10.1016/j.cognition.2018.07.010 

Kahnt, T., Chang, L. J., Park, S. Q., Heinzle, J., & Haynes, J.-D. (2012). Connectivity-based 

parcellation of the human orbitofrontal cortex. _J. Neurosci._ , _32_ (18), 6240–6250. https://doi.org/10.1523/JNEUROSCI.0257-12.2012 

Kamin, L. J. (1968). “Attention-like” processes in classical conditioning. In M. R. Jones (Ed.), 

_Miami Symposium on the Prediction of Behavior, 1967: Aversive Stimulation_ (pp. 9–31). University of Miami Press. 

https://psychology.nottingham.ac.uk/staff/mxh/C82MPR/Useful%20reading%20(pdfs)/ Kamin%20(1968).pdf 

Kamin, L. J. (1969). Predictability, surprise, attention, and conditioning. In B. A. Campbell & R. 

M. Church (Eds.), _Punishment and Aversive Behavior_ (pp. 279–296). Appleton-CenturyCrofts. https://ntrs.nasa.gov/api/citations/19680014821/downloads/19680014821.pdf 

Kamiński, J., Mamelak, A. N., Birch, K., Mosher, C. P., Tagliati, M., & Rutishauser, U. (2018). 

Novelty-Sensitive Dopaminergic Neurons in the Human Substantia Nigra Predict Success 

48 

of Declarative Memory Formation. _Curr. Biol._ , _28_ (9), 1333-1343.e4. https://doi.org/10.1016/j.cub.2018.03.024 

Kenett, Y. N., Levi, E., Anaki, D., & Faust, M. (2017). The Semantic Distance Task: Quantifying 

Semantic Distance With Semantic Network Path Length. In _Journal of Experimental Psychology: Learning, Memory, and Cognition_ (Issue February). https://doi.org/10.1037/xlm0000391 

Kesner, R. P., & Hunsaker, M. R. (2010). The temporal attributes of episodic memory. 

_Behavioural Brain Research_ , 11. 

Kim, G., Lewis-Peacock, J. A., Norman, K. A., & Turk-Browne, N. B. (2014). Pruning of memories 

by context-based prediction error. _Proceedings of the National Academy of Sciences_ , 

_111_ (24), 8997–9002. https://doi.org/10.1073/pnas.1319438111 

Kim, H., Schlichting, M. L., Preston, A. R., & Lewis-Peacock, J. A. (2020). Predictability Changes What We Remember in Familiar Temporal Contexts. _Journal of Cognitive Neuroscience 32_ (1), 124–140. https://doi.org/10.1162/jocn_a_01473 

Klein-Flügge, M. C., Bongioanni, A., & Rushworth, M. F. S. (2022). Medial and orbital frontal 

cortex in decision-making and flexible behavior. _Neuron_ , S0896627322004639. https://doi.org/10.1016/j.neuron.2022.05.022 

Klein-Flügge, M. C., Wittmann, M. K., Shpektor, A., Jensen, D. E. A., & Rushworth, M. F. S. 

(2019). Multiple associative structures created by reinforcement and incidental 

statistical learning mechanisms. _Nature Communications_ , _10_ (1), 4835. 

https://doi.org/10.1038/s41467-019-12557-z 

49 

Kumar, A. A. (2021). Semantic memory: A review of methods, models, and current challenges. 

In _Psychonomic Bulletin and Review_ (Vol. 28, Issue 1). Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-020-01792-x 

Kumaran, D., Summerfield, J. J., Hassabis, D., & Maguire, E. A. (2009). Tracking the Emergence of Conceptual Knowledge during Human Decision Making. _Neuron_ , _63_ (6), 889–901. https://doi.org/10.1016/j.neuron.2009.07.030 

Langdon, A. J., Song, M., & Niv, Y. (2019). Uncovering the ‘state’: Tracing the hidden state 

representations that structure learning and decision-making. _Behavioural Processes_ , _167_ (May), 103891. https://doi.org/10.1016/j.beproc.2019.103891 

Lebreton, M., Jorge, S., Michel, V., Thirion, B., & Pessiglione, M. (2009). An Automatic Valuation System in the Human Brain: Evidence from Functional Neuroimaging. _Neuron_ , _64_ (3), 431–439. https://doi.org/10.1016/j.neuron.2009.09.040 

Lee, C. S., Aly, M., & Baldassano, C. (2021). Anticipation of temporally structured events in the brain. _Elife_ , _10_ . https://doi.org/10.7554/eLife.64972 

Leong, Y. C., Radulescu, A., Daniel, R., DeWoskin, V., & Niv, Y. (2017). Dynamic Interaction between Reinforcement Learning and Attention in Multidimensional Environments. _Neuron_ , _93_ (2), 451–463. https://doi.org/10.1016/j.neuron.2016.12.040 

Leutgeb, J. K., Leutgeb, S., Moser, M.-B., & Moser, E. I. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. _Science_ , _315_ (5814), 961–966. https://doi.org/10.1126/science.1135801 

50 

Levy, D. J., & Glimcher, P. W. (2012). The root of all value: A neural common currency for 

choice. _Current Opinion in Neurobiology_ , _22_ (6), 1027–1038. 

https://doi.org/10.1016/j.conb.2012.06.001 

Liberman, N., Sagristano, M. D., & Trope, Y. (2002). The effect of temporal distance on level of mental construal. _Journal of Experimental Social Psychology_ , 12. 

Long, N. M., Lee, H., & Kuhl, B. A. (2016). Hippocampal Mismatch Signals Are Modulated by the Strength of Neural Predictions and Their Similarity to Outcomes. _J. Neurosci._ , _36_ (50), 12677–12687. https://doi.org/10.1523/JNEUROSCI.1850-16.2016 

Love, B. C., Medin, D. L., & Gureckis, T. M. (2004). SUSTAIN: A Network Model of Category 

Learning. _Psychological Review_ , _111_ (2), 309–332. https://doi.org/10.1037/0033295X.111.2.309 

Mack, M. L., Preston, A. R., & Love, B. C. (2020). Ventromedial prefrontal cortex compression 

during concept learning. _Nat. Commun._ , _11_ (1), 46. https://doi.org/10.1038/s41467-01913930-8 

Mackey, S., & Petrides, M. (2010). Quantitative demonstration of comparable architectonic areas within the ventromedial and lateral orbital frontal cortex in the human and the macaque monkey brains. _Eur. J. Neurosci._ , _32_ (11), 1940–1950. 

https://doi.org/10.1111/j.1460-9568.2010.07465.x 

Mackey, S., & Petrides, M. (2014). Architecture and morphology of the human ventromedial 

prefrontal cortex. _Eur. J. Neurosci._ , _40_ (5), 2777–2796. 

https://doi.org/10.1111/ejn.12654 

51 

Masís-Obando, R., Norman, K. A., & Baldassano, C. (2022). Schema representations in distinct 

brain networks support narrative memory during encoding and retrieval. _eLife_ , _11_ , 

e70445. https://doi.org/10.7554/eLife.70445 

McClelland, J. L., McNaughton, B. L., & O’Reilly, R. C. (1995). Why there are complementary 

learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. _Psychological Review_ , _102_ (3), 419–457. https://doi.org/10.1037/0033-295X.102.3.419 

McClelland, J. L., McNaughton, B. L., & Oreilly, R. C. (1995). Why there are complementary learning-systems in the hippocampus and neocortex – insights from the success and failures of connectionist models of learning and memory. _Psychological Review_ , _102_ (3), 419–457. https://doi.org/10.1037/0033-295x.102.3.419 

McCormick, C., Barry, D. N., Jafarian, A., Barnes, G. R., & Maguire, E. A. (2020). vmPFC Drives 

Hippocampal Processing during Autobiographical Memory Recall Regardless of Remoteness. _Cerebral Cortex_ , _30_ , 5972–5987. 

McKenzie, S., Frank, A. J., Kinsky, N. R., Porter, B., Rivière, P. D., & Eichenbaum, H. (2014). 

Hippocampal representation of related and opposing memories develop within distinct, hierarchically organized neural schemas. _Neuron_ , _83_ (1), 202–215. 

https://doi.org/10.1016/j.neuron.2014.05.019 

McNamee, D., Rangel, A., & O’Doherty, J. P. (2013). Category-dependent and category- 

independent goal-value codes in human ventromedial prefrontal cortex. _Nat. Neurosci._ , 

_16_ (4), 479–485. https://doi.org/10.1038/nn.3337 

52 

Mızrak, E., Bouffard, N. R., Libby, L. A., Boorman, E. D., & Ranganath, C. (2021). The 

hippocampus and orbitofrontal cortex jointly represent task structure during memoryguided decision making. _Cell Rep._ , _37_ (9), 110065. 

https://doi.org/10.1016/j.celrep.2021.110065 

Momennejad, I., & Haynes, J.-D. (2012). Human anterior prefrontal cortex encodes the “what” and “when” of future intentions. _Neuroimage_ , _61_ (1), 139–148. 

https://doi.org/10.1016/j.neuroimage.2012.02.079 

Momennejad, I., & Haynes, J.-D. (2013). Encoding of prospective tasks in the human prefrontal cortex under varying task loads. _J. Neurosci._ , _33_ (44), 17342–17349. https://doi.org/10.1523/JNEUROSCI.0492-13.2013 

Momennejad, I., Russek, E. M., Cheong, J. H., Botvinick, M. M., Daw, N. D., & Gershman, S. J. (2017). The successor representation in human reinforcement learning. _Nat Hum Behav_ , _1_ (9), 680–692. https://doi.org/10.1038/s41562-017-0180-8 

Moneta, N., Garvert, M. M., Heekeren, H. R., & Schuck, N. W. (2023). Task state representations in vmPFC mediate relevant and irrelevant value signals and their behavioral influence. _Nature Communications_ , _14_ (1), 3156. https://doi.org/10.1038/s41467-023-38709-w Morton, N. W., Sherrill, K. R., & Preston, A. R. (2017). Memory integration constructs maps of space, time, and concepts. _Curr Opin Behav Sci_ , _17_ , 161–168. https://doi.org/10.1016/j.cobeha.2017.08.007 

Moscovitch, M., Cabeza, R., Winocur, G., & Nadel, L. (2016). Episodic Memory and Beyond: The 

Hippocampus and Neocortex in Transformation. _Annu. Rev. Psychol._ , _67_ , 105–134. https://doi.org/10.1146/annurev-psych-113011-143733 

53 

Murphy, G. L. (2004). _The big book of concepts_ . MIT press. 

Murty, V. P., & Adcock, R. A. (2014). Enriched encoding: Reward motivation organizes cortical 

networks for hippocampal detection of unexpected events. _Cereb. Cortex_ , _24_ (8), 2160– 2168. https://doi.org/10.1093/cercor/bht063 

Nadel, L., Samsonovich, A., Ryan, L., & Moscovitch, M. (2000). Multiple trace theory of human memory: Computational, neuroimaging, and neuropsychological results. _Hippocampus_ , _10_ , 352–368. 

Niv, Y. (2019). Learning task-state representations. _Nature Neuroscience_ , _22_ (10), 1544–1553. https://doi.org/10.1038/s41593-019-0470-8 

Niv, Y., Daniel, R., Geana, A., Gershman, S. J., Leong, Y. C., Radulescu, A., & Wilson, R. C. (2015). Reinforcement learning in multidimensional environments relies on attention mechanisms. _Journal of Neuroscience_ , _35_ (21), 8145–8157. 

https://doi.org/10.1523/JNEUROSCI.2978-14.2015 

Niv, Y., & Langdon, A. (2016). Reinforcement learning with Marr. _Current Opinion in Behavioral_ 

_Sciences_ , _11_ , 67–73. https://doi.org/10.1016/j.cobeha.2016.04.005 

Niv, Y., & Schoenbaum, G. (2008). Dialogues on prediction errors. _Trends in Cognitive Sciences_ , _12_ (7), 265–272. https://doi.org/10.1016/j.tics.2008.03.006 

Norman, K. A., & O’Reilly, R. C. (2003). Modeling hippocampal and neocortical contributions to 

recognition memory: A complementary-learning-systems approach. _Psychological Review_ , _110_ (4), 611–646. https://doi.org/10.1037/0033-295X.110.4.611 

Nosofsky, R. M. (1986). Attention, Similarity, and the Identification-Categorization Relationship. 

_Journal of Experimental Psychology: General_ , _115_ (1), 39–57. 

54 

Öngür, D., Ferry, A. T., & Price, J. L. (2003). Architectonic subdivision of the human orbital and medial prefrontal cortex. _J. Comp. Neurol._ , _460_ (3), 425–449. 

https://doi.org/10.1002/cne.10609 

Öngür, D., & Price, J. L. (2000). The Organization of Networks within the Orbital and Medial Prefrontal Cortex of Rats, Monkeys and Humans. _Cereb. Cortex_ , _10_ , 206–219. Padoa-Schioppa, C., & Conen, K. E. (2017). Orbitofrontal Cortex: A Neural Circuit for Economic Decisions. _Neuron_ , _96_ (4), 736–754. https://doi.org/10.1016/j.neuron.2017.09.031 Park, S. A., Miller, D. S., Nili, H., Ranganath, C., & Boorman, E. D. (2020). Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps. _Neuron_ , _107_ (6), 1226-1238.e8. https://doi.org/10.1016/j.neuron.2020.06.030 

Peer, M., Brunec, I. K., Newcombe, N. S., & Epstein, R. A. (2021). Structuring Knowledge with Cognitive Maps and Cognitive Graphs. _Trends Cogn. Sci._ , _25_ (1), 37–54. https://doi.org/10.1016/j.tics.2020.10.004 

Piaget, J. (1952). _The origins of intelligence in children_ . International Universities Press. Place, R., Farovik, A., Brockmann, M., & Eichenbaum, H. (2016). Bidirectional prefrontal- 

hippocampal interactions support context-guided memory. _Nat. Neurosci._ , _19_ (8), 992– 994. https://doi.org/10.1038/nn.4327 

Preston, A. R., & Eichenbaum, H. (2013). Interplay of hippocampus and prefrontal cortex in memory. _Curr. Biol._ , _23_ (17), R764-73. https://doi.org/10.1016/j.cub.2013.05.041 

Price, J. L. (2007). Definition of the orbital cortex in relation to specific connections with limbic 

and visceral structures and other cortical regions. _Ann. N. Y. Acad. Sci._ , _1121_ , 54–71. https://doi.org/10.1196/annals.1401.008 

55 

Quent, J. A., Henson, R. N., & Greve, A. (2021). A predictive account of how novelty influences 

declarative memory. _Neurobiol. Learn. Mem._ , _179_ , 107382. 

https://doi.org/10.1016/j.nlm.2021.107382 

Radulescu, A., Daniel, R., & Niv, Y. (2016). The effects of aging on the interaction between reinforcement learning and attention. _Psychology and Aging_ , _31_ (7), 747–757. https://doi.org/10.1037/pag0000112 

Radulescu, A., Niv, Y., & Ballard, I. (2019). Holistic Reinforcement Learning: The Role of 

Structure and Attention. _Trends in Cognitive Sciences_ , _23_ (4), 278–292. https://doi.org/10.1016/j.tics.2019.01.010 

Ranganath, C., & Hsieh, L.-T. (2016). The hippocampus: A special place for time. _Ann. N. Y. Acad. Sci._ , _1369_ (1), 93–110. https://doi.org/10.1111/nyas.13043 

Reagh, Z. M., & Ranganath, C. (2023). Flexible reuse of cortico-hippocampal representations 

during encoding and recall of naturalistic events. _Nature Communications_ , _14_ (1), 1279. https://doi.org/10.1038/s41467-023-36805-5 

Reder, L. M., Paynter, C., Diana, R. A., Ngiam, J., & Dickison, D. (2007). Experience is a DoubleEdged Sword: A Computational Model of The Encoding/Retrieval Trade-Off With Familiarity. In _Psychology of Learning and Motivation_ (Vol. 48, pp. 271–312). Elsevier. https://doi.org/10.1016/S0079-7421(07)48007-0 

Reggev, N., Bein, O., & Maril, A. (2016). Distinct Neural Suppression and Encoding Effects for Conceptual Novelty and Familiarity. _J. Cogn. Neurosci._ , _28_ (10), 1455–1470. 

https://doi.org/10.1162/jocn_a_00994 

56 

Rescorla, R. A. (1988). Pavlovian conditioning. It’s not what you think it is. _The American_ 

_Psychologist_ , _43_ (3), 151–160. https://doi.org/10.1037/0003-066X.43.3.151 

Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning. In _Classical_ 

_conditioning II current research and theory_ (p. 497). 

https://doi.org/10.1101/gr.110528.110 

Ribas-Fernandes, J. J. F., Solway, A., Diuk, C., McGuire, J. T., Barto, A. G., Niv, Y., & Botvinick, M. M. (2011). A neural signature of hierarchical reinforcement learning. _Neuron_ , _71_ (2), 370–379. https://doi.org/10.1016/j.neuron.2011.05.042 

Richards, B. A., Xia, F., Santoro, A., Husse, J., Woodin, M. A., Josselyn, S. A., & Frankland, P. W. (2014). Patterns across multiple memories are identified over time. _Nat. Neurosci._ , _17_ (7), 981–986. https://doi.org/10.1038/nn.3736 

Robin, J., & Moscovitch, M. (2017). Details, gist and schema: Hippocampal–neocortical interactions underlying recent and remote episodic and spatial memory. _Current Opinion in Behavioral Sciences_ , _17_ , 114–123. 

https://doi.org/10.1016/j.cobeha.2017.07.016 

Rouhani, N., & Niv, Y. (2021). Signed and unsigned reward prediction errors dynamically 

enhance learning and memory. _Elife_ , _10_ . https://doi.org/10.7554/eLife.61077 Rouhani, N., Norman, K. A., & Niv, Y. (2018). Dissociable effects of surprising rewards on 

learning and memory. _J. Exp. Psychol. Learn. Mem. Cogn._ , _44_ (9), 1430–1443. https://doi.org/10.1037/xlm0000518 

57 

Rouhani, N., Norman, K. A., Niv, Y., & Bornstein, A. M. (2020). Reward prediction errors create event boundaries in memory. _Cognition_ , _203_ , 104269. 

https://doi.org/10.1016/j.cognition.2020.104269 

Rumelhart, D. E., & Ortony, A. (1977). The Representation of Knowledge in Memory. _Schooling and the Acquisition of Knowledge_ , 99–135. https://doi.org/10.4324/9781315271644-10 Rushworth, M. F. S., Noonan, M. P., Boorman, E. D., Walton, M. E., & Behrens, T. E. (2011). 

Frontal cortex and reward-guided learning and decision-making. _Neuron_ , _70_ (6), 1054– 1069. https://doi.org/10.1016/j.neuron.2011.05.014 

Saffran, J. R., Aslin, R. N., & Newport, E. L. (1996). Statistical learning by 8-month-old infants. 

_Science_ , _274_ (5294), 1926–1928. https://doi.org/10.1126/science.274.5294.1926 

Saffran, J. R., & Wilson, D. P. (2003). From syllables to syntax: Multilevel statistical learning by 12-month-old infants. _Infancy_ , _4_ (2), 273–284. 

https://doi.org/10.1207/s15327078in0402_07 

Schank, R., & Abelson, R. (1977). Scripts. In _Scripts Plans Goals and Understanding: An inquiry_ 

_into human knowledge structures_ (pp. 36–68). https://doi.org/10.1515/9789048536825005 

Schapiro, A. C., Gregory, E., Landau, B., McCloskey, M., & Turk-Browne, N. B. (2014). The 

necessity of the medial temporal lobe for statistical learning. _J. Cogn. Neurosci._ , _26_ (8), 1736–1747. https://doi.org/10.1162/jocn_a_00578 

Schapiro, A. C., Rogers, T. T., Cordova, N. I., Turk-Browne, N. B., & Botvinick, M. M. (2013). 

Neural representations of events arise from temporal community structure. _Nat. Neurosci._ , _16_ (4), 486–492. https://doi.org/10.1038/nn.3331 

58 

Schapiro, A. C., & Turk-Browne, N. (2015). Statistical Learning. _Brain Mapping: An Encyclopedic Reference_ , _3_ , 501–506. https://doi.org/10.1016/B978-0-12-397025-1.00276-1 

Schapiro, A. C., Turk-Browne, N. B., Botvinick, M. M., & Norman, K. A. (2017). Complementary learning systems within the hippocampus: A neural network modelling approach to reconciling episodic memory with statistical learning. _Philos. Trans. R. Soc. Lond. B Biol. Sci._ , _372_ (1711), 20160049. https://doi.org/10.1098/rstb.2016.0049 

Schapiro, A. C., Turk-Browne, N. B., Norman, K. A., & Botvinick, M. M. (2016). Statistical learning 

of temporal community structure in the hippocampus. _Hippocampus_ , _26_ (1), 3–8. https://doi.org/10.1002/hipo.22523 

Schiller, D., Eichenbaum, H., Buffalo, E. A., Davachi, L., Foster, D. J., Leutgeb, S., & Ranganath, C. (2015). Memory and space: Towards an understanding of the cognitive map. _Journal of Neuroscience_ , _35_ (41), 13904–13911. https://doi.org/10.1523/JNEUROSCI.2618-15.2015 Schlichting, M. L., Mumford, J. A., & Preston, A. R. (2015). Learning-related representational changes reveal dissociable integration and separation signatures in the hippocampus and prefrontal cortex. _Nature Communications_ , _6_ , 1–10. https://doi.org/10.1038/ncomms9151 

Schuck, N. W., Cai, M. B., Wilson, R. C., Niv, Y., Schuck, N. W., Cai, M. B., Wilson, R. C., & Niv, Y. (2016). Human Orbitofrontal Cortex Represents a Cognitive Map of State Space Article Human Orbitofrontal Cortex Represents a Cognitive Map of State Space. _Neuron_ , _91_ (6), 1402–1412. https://doi.org/10.1016/j.neuron.2016.08.019 

Schuck, N. W., Wilson, R., & Niv, Y. (2018). A state representation for reinforcement learning and decision-making in the orbitofrontal cortex. In _Goal-Directed Decision Making:_ 

59 

_Computations and Neural Circuits_ . Elsevier Inc. https://doi.org/10.1016/B978-0-12812098-9.00012-7 

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. 

_Science_ , _275_ (5306), 1593–1599. https://doi.org/10.1126/science.275.5306.1593 

Sharp, P. B., Dolan, R. J., & Eldar, E. (2021). Disrupted state transition learning as a 

computational marker of compulsivity. _Psychological Medicine_ , 1–11. https://doi.org/10.1017/S0033291721003846 

Sharp, P. B., Russek, E. M., Huys, Q. J., Dolan, R. J., & Eldar, E. (2022). Humans perseverate on punishment avoidance goals in multigoal reinforcement learning. _eLife_ , _11_ , e74402. https://doi.org/10.7554/eLife.74402 

Sharpe, M. J., Batchelor, H. M., Mueller, L. E., Yun Chang, C., Maes, E. J. P., Niv, Y., & 

Schoenbaum, G. (2020). Dopamine transients do not act as model-free prediction errors during associative learning. _Nature Communications_ , _11_ (1), 106. 

https://doi.org/10.1038/s41467-019-13953-1 

Sharpe, M. J., Chang, C. Y., Liu, M. A., Batchelor, H. M., Mueller, L. E., Jones, J. L., Niv, Y., & Schoenbaum, G. (2017). Dopamine transients are sufficient and necessary for acquisition of model-based associations. _Nat. Neurosci._ , _20_ (5), 735–742. https://doi.org/10.1038/nn.4538 

Sherman, B. E., Graves, K. N., & Turk-Browne, N. B. (2020). The prevalence and importance of statistical learning in human cognition and behavior. _Curr Opin Behav Sci_ , _32_ , 15–20. https://doi.org/10.1016/j.cobeha.2020.01.015 

60 

Sherman, B. E., & Turk-Browne, N. B. (2020). Statistical prediction of the future impairs episodic 

encoding of the present. _Proceedings of the National Academy of Sciences_ . https://doi.org/10.1101/851147 

Sherrill, K. R., Molitor, R. J., Karagoz, A. B., Atyam, M., Mack, M. L., & Preston, A. R. (2023). Generalization of cognitive maps across space and time. _Cerebral Cortex_ , bhad092. https://doi.org/10.1093/cercor/bhad092 

Shin, Y. S., & DuBrow, S. (2021). Structuring Memory Through Inference-Based Event 

Segmentation. _Top. Cogn. Sci._ , _13_ (1), 106–127. https://doi.org/10.1111/tops.12505 Shohamy, D., & Turk-Browne, N. B. (2013). Mechanisms for widespread hippocampal involvement in cognition. _J. Exp. Psychol. Gen._ , _142_ (4), 1159–1170. https://doi.org/10.1037/a0034461 

Shteingart, H., Neiman, T., & Loewenstein, Y. (2013). The role of first impression in operant learning. _Journal of Experimental Psychology: General_ , _142_ (2), 476–488. https://doi.org/10.1037/a0029550 

Sinclair, A. H., & Barense, M. D. (2018). Surprise and destabilize: Prediction error influences 

episodic memory reconsolidation. _Learning & Memory_ , _25_ , 369–381. https://doi.org/10.1101/lm.046912.117 

Sinclair, A. H., Manalili, G. M., Brunec, I. K., Adcock, R. A., & Barense, M. D. (2021). Prediction 

errors disrupt hippocampal representations and update episodic memories. _Proceedings of the National Academy of Sciences_ , _118_ (51), e2117625118. 

https://doi.org/10.1073/pnas.2117625118 

61 

Solway, A., Diuk, C., Córdova, N., Yee, D., Barto, A. G., Niv, Y., & Botvinick, M. M. (2014). 

Optimal behavioral hierarchy. _PLoS Comput. Biol._ , _10_ (8), e1003779. 

https://doi.org/10.1371/journal.pcbi.1003779 

Spalding, K. N., Jones, S. H., Duff, M. C., Tranel, D., & Warren, D. E. (2015). Investigating the Neural Correlates of Schemas: Ventromedial Prefrontal Cortex Is Necessary for Normal Schematic Influence on Memory. _J. Neurosci._ , _35_ (47), 15746–15751. https://doi.org/10.1523/JNEUROSCI.2767-15.2015 

Spalding, K. N., Schlichting, M. L., Zeithamova, D., Preston, A. R., Tranel, D., Duff, M. C., & Warren, D. E. (2018). Ventromedial Prefrontal Cortex Is Necessary for Normal Associative Inference and Memory Integration. _J. Neurosci._ , _38_ (15), 3767–3775. https://doi.org/10.1523/JNEUROSCI.2501-17.2018 

Squire, L. R., & Alvarez, P. (1995). Retrograde amnesia and memory consolidation: A 

neurobiological perspective. _Curr. Opin. Neurobiol._ , _5_ (2), 169–177. 

https://doi.org/10.1016/0959-4388(95)80023-9 

Stalnaker, T. A., Cooch, N. K., & Schoenbaum, G. (2015). What the orbitofrontal cortex does not do. _Nat. Neurosci._ , _18_ (5), 620–627. https://doi.org/10.1038/nn.3982 

Sutton, R. S., & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (second edi). MIT press. https://doi.org/10.1016/S0140-6736(51)92942-X 

Sutton, R. S., Precup, D., & Singh, S. (1999). Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning. _Artificial Intelligence_ , _112_ (1–2), 181– 211. https://doi.org/10.1016/S0004-3702(99)00052-1 

62 

Sweegers, C. C. G., Takashima, A., Fernández, G., & Talamini, L. M. (2014). Neural mechanisms 

supporting the extraction of general knowledge across episodic memories. _Neuroimage_ , _87_ , 138–146. https://doi.org/10.1016/j.neuroimage.2013.10.063 

Takashima, A., Petersson, K. M., Rutters, F., Tendolkar, I., Jensen, O., Zwarts, M. J., 

McNaughton, B. L., & Fernández, G. (2006). Declarative memory consolidation in humans: A prospective functional magnetic resonance imaging study. _Proc. Natl. Acad. Sci. U. S. A._ , _103_ (3), 756–761. https://doi.org/10.1073/pnas.0507774103 

Tavares, R. M., Mendelsohn, A., Grossman, Y., Williams, C. H., Shapiro, M., Trope, Y., & Schiller, D. (2015). A Map for Social Navigation in the Human Brain. _Neuron_ , _87_ (1), 231–243. https://doi.org/10.1016/j.neuron.2015.06.011 

Theves, S., Fernandez, G., & Doeller, C. F. (2019). The Hippocampus Encodes Distances in 

Multidimensional Feature Space. _Current Biology_ , _29_ (7), 1226-1231.e3. https://doi.org/10.1016/j.cub.2019.02.035 

Theves, S., Fernández, G., & Doeller, C. F. (2020). The hippocampus maps concept space, not feature space. _Journal of Neuroscience_ , _40_ (38), 7318–7325. https://doi.org/10.1523/JNEUROSCI.0494-20.2020 

Theves, S., Neville, D., Fernández, G., & Doeller, C. F. (2021). Learning and Representation of 

Hierarchical Concepts in Hippocampus and Prefrontal Cortex. _J. Neurosci._ https://doi.org/10.1523/JNEUROSCI.0657-21.2021 

Tolman, E. C. (1948). Cognitive maps in rats and men. _Psychological Review_ , _55_ (4), 189–208. https://doi.org/10.1037/h0061626 

63 

Tomov, M. S., Yagati, S., Kumar, A., Yang, W., & Gershman, S. J. (2020). Discovery of hierarchical representations for efficient planning. _PLoS Comput. Biol._ , _16_ (4), e1007594. 

https://doi.org/10.1371/journal.pcbi.1007594 

Tompary, A., & Davachi, L. (2017). Consolidation Promotes the Emergence of Representational Overlap in the Hippocampus and Medial Prefrontal Cortex. _Neuron_ , _96_ (1), 228–241. https://doi.org/10.1016/j.neuron.2017.09.005 

Tompary, A., & Thompson-Schill, S. L. (2021). Semantic influences on episodic memory 

distortions. _J. Exp. Psychol. Gen._ https://doi.org/10.1037/xge0001017 

Tompary, A., Zhou, W., & Davachi, L. (2020). Schematic memories develop quickly, but are not expressed unless necessary. _Sci. Rep._ , _10_ (1), 16968. https://doi.org/10.1038/s41598020-73952-x 

Trope, Y., & Liberman, N. (2003). Temporal construal. _Psychological Review_ , _110_ (3), 403–421. https://doi.org/10.1037/0033-295x.110.3.403 

Trope, Y., & Liberman, N. (2010). Construal-Level Theory of Psychological Distance. 

_Psychological Review_ , _117_ (2), 440–463. 

Tse, D., Langston, R. F., Kakeyama, M., Bethus, I., Spooner, P. A., Wood, E. R., Witter, M. P., & Morris, R. G. M. (2007). Schemas and Memory Consolidation. _Science_ , _316_ (5821), 76–82. https://doi.org/10.1126/science.1135935 

Tse, D., Takeuchi, T., Kakeyama, M., Kajii, Y., Okuno, H., Tohyama, C., Bito, H., & Morris, R. G. M. (2011). Schema-Dependent Gene Activation and Memory Encoding in Neocortex. 

_Science_ , _333_ (6044), 891–895. https://doi.org/10.1126/science.1205274 

64 

Turk-Browne, N. B., Jungé, J., & Scholl, B. J. (2005). The automaticity of visual statistical 

learning. _Journal of Experimental Psychology. General_ , _134_ (4), 552–564. 

https://doi.org/10.1037/0096-3445.134.4.552 

Uylings, H. B. M., Sanz-Arigita, E. J., de Vos, K., Poolc, C. W., Evers, P., & Rajkowska, G. (2010). 3- 

D Cytoarchitectonic parcellation of human orbitofrontal cortex: Correlation with postmortem MRI Author links open overlay panel. _Psychiatry Research: Neuroimaging_ , _183_ (1), 1–20. 

Vaidya, A. R., & Badre, D. (2022). Abstract task representations for inference and control. 

_Trends in Cognitive Sciences_ , _26_ (6), 484–498. https://doi.org/10.1016/j.tics.2022.03.009 van Kesteren, M. T. R., Beul, S. F., Takashima, A., Henson, R. N., Ruiter, D. J., & Fernández, G. (2013). Differential roles for medial prefrontal and medial temporal cortices in schemadependent encoding: From congruent to incongruent. _Neuropsychologia_ , _51_ (12), 2352– 2359. https://doi.org/10.1016/j.neuropsychologia.2013.05.027 

van Kesteren, M. T. R., Fernández, G., Norris, D. G., & Hermans, E. J. (2010). Persistent schema- 

dependent hippocampal-neocortical connectivity during memory encoding and postencoding rest in humans. _Proc. Natl. Acad. Sci. U. S. A._ , _107_ (16), 7550–7555. https://doi.org/10.1073/pnas.0914892107 

van Kesteren, M. T. R., Rijpkema, M., Ruiter, D. J., & Fernández, G. (2010). Retrieval of 

associative information congruent with prior knowledge is related to increased medial prefrontal activity and connectivity. _J. Neurosci._ , _30_ (47), 15888–15894. 

https://doi.org/10.1523/JNEUROSCI.2674-10.2010 

65 

van Kesteren, M. T. R., Ruiter, D. J., Fernández, G., & Henson, R. N. (2012). How schema and 

novelty augment memory formation. _Trends Neurosci._ , _35_ (4), 211–219. 

https://doi.org/10.1016/j.tins.2012.02.001 

Varga, N., Morton, N., & Preston, A. (2022). Schema, Inference, and Memory. In M. J. Kahana & 

A. D. Wagner (Eds.), _The Oxford Handbook of Human Memory_ . Oxford University Press. https://doi.org/10.31234/osf.io/m9adb 

Viganò, S., & Piazza, M. (2020). Distance and Direction Codes Underlie Navigation of a Novel 

Semantic Space in the Human Brain. _J. Neurosci._ , _40_ (13), 2727–2736. https://doi.org/10.1523/JNEUROSCI.1849-19.2020 

Wang, S.-H., Tse, D., & Morris, R. G. M. (2012). Anterior cingulate cortex in schema assimilation 

and expression. _Learn. Mem._ , _19_ (8), 315–318. https://doi.org/10.1101/lm.026336.112 Warren, W. H. (2019). Non-Euclidean navigation. _Journal of Experimental Biology_ , _222_ . https://doi.org/10.1242/jeb.187971 

Wilson, R. C., Takahashi, Y. K., Schoenbaum, G., & Niv, Y. (2014). Orbitofrontal cortex as a cognitive map of task space. _Neuron_ , _81_ (2), 267–279. 

https://doi.org/10.1016/j.neuron.2013.11.005 

Wittmann, B. C., Bunzeck, N., Dolan, R. J., & Düzel, E. (2007). Anticipation of novelty recruits reward system and hippocampus while promoting recollection. _Neuroimage_ , _38_ (1), 194–202. https://doi.org/10.1016/j.neuroimage.2007.06.038 

Yacoby, A., Reggev, N., & Maril, A. (2021). Examining the transition of novel information toward 

familiarity. _Neuropsychologia_ , _161_ , 107993. 

https://doi.org/10.1016/j.neuropsychologia.2021.107993 

66 

Yacoby, A., Reggev, N., & Maril, A. (2023). Lack of source memory as a potential marker of early assimilation of novel items into current knowledge. _Neuropsychologia_ , _185_ , 108569. https://doi.org/10.1016/j.neuropsychologia.2023.108569 

Yassa, M. A., & Stark, C. E. L. (2011). Pattern separation in the hippocampus. _Trends Neurosci._ , _34_ (10), 515–525. https://doi.org/10.1016/j.tins.2011.06.006 

Zacks, J. M. (2020). Event Perception and Memory. _Annual Review of Psychology_ , _71_ (1), 165– 191. https://doi.org/10.1146/annurev-psych-010419-051101 

Zeithamova, D., Mack, M. L., Braunlich, K., Davis, T., Seger, C. A., van Kesteren, M. T. R., & Wutz, A. (2019). Brain Mechanisms of Concept Learning. _J. Neurosci._ , _39_ (42), 8259–8266. https://doi.org/10.1523/JNEUROSCI.1166-19.2019 

Zhao, J., AI-Aidroos, N., & Turk-Browne, N. B. (2013). Attention is spontanesouly biased toward regularities. _Psychological Science_ , _24_ (5), 667–677. 

https://doi.org/10.1177/0956797612460407.Attention 

Zhou, J., Gardner, M. P. H., & Schoenbaum, G. (2021). Is the core function of orbitofrontal 

cortex to signal values or make predictions? _Curr Opin Behav Sci_ , _41_ , 1–9. https://doi.org/10.1016/j.cobeha.2021.02.011 

Zhou, J., Gardner, M. P. H., Stalnaker, T. A., Ramus, S. J., Wikenheiser, A. M., Niv, Y., & 

Schoenbaum, G. (2019). Rat Orbitofrontal Ensemble Activity Contains Multiplexed but 

Dissociable Representations of Value and Task Structure in an Odor Sequence Task. _Curr. Biol._ , _29_ (6), 897-907.e3. https://doi.org/10.1016/j.cub.2019.01.048 

67 

Zhou, J., Jia, C., Montesinos-Cartagena, M., Gardner, M. P. H., Zong, W., & Schoenbaum, G. (2020). Evolving schema representations in orbitofrontal ensembles during learning. _Nature_ , _590_ (7847), 606–611. https://doi.org/10.1038/s41586-020-03061-2 

Zhou, J., Montesinos-Cartagena, M., Wikenheiser, A. M., Gardner, M. P. H., Niv, Y., & Schoenbaum, G. (2019). Complementary Task Structure Representations in Hippocampus and Orbitofrontal Cortex during an Odor Sequence Task. _Curr. Biol._ , _29_ (20), 3402-3409.e3. https://doi.org/10.1016/j.cub.2019.08.040 

Zhou, J., Zong, W., Jia, C., Gardner, M. P. H., & Schoenbaum, G. (2021). Prospective 

representations in rat orbitofrontal ensembles. _Behavioral Neuroscience_ , _135_ (4), 518– 527. https://doi.org/10.1037/bne0000451 

68 

