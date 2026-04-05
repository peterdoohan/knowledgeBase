## PERSPECTIVES 

## OPINION 

## Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex 

## _Andrew M. Wikenheiser and Geoffrey Schoenbaum_ 

Abstract | The hippocampus and the orbitofrontal cortex (OFC) both have important roles in cognitive processes such as learning, memory and decision making. Nevertheless, research on the OFC and hippocampus has proceeded largely independently, and little consideration has been given to the importance of interactions between these structures. Here, evidence is reviewed that the hippocampus and OFC encode parallel, but interactive, cognitive ‘maps’ that capture complex relationships between cues, actions, outcomes and other features of the environment. A better understanding of the interactions between the OFC and hippocampus is important for understanding the neural bases of flexible, goal-directed decision making. 

Despite possessing distinct neurochemical, anatomical and physiological properties, the hippocampal formation and the orbitofrontal cortex (OFC) have been ascribed broadly similar functional roles. For instance, a core feature of OFC function has been identified as “predicting the specific outcomes that should follow either sensory events or behavioral choices” (REF. 1), whereas others have conceptualized the hippocampal formation as a “system that facilitates predictions about upcoming events” (REF. 2). Although these statements are, of course, meant to provide very general descriptions of how each structure functions, the similarities are striking. Both structures are implicated in forming predictions about the future to support flexible behaviour and in leveraging general knowledge about the world rather than relying exclusively on specific previous experiences[1,2] . 

of hippocampal information processing. Although this mapping function is frequently thought of in terms of spatial mapping, the cognitive map framework revisited the older concept of a cognitive map, as proposed by Tolman[4] . This referred not to a literal map of space, but rather to an abstract map of causal relationships in the world: that is, a set of mental representations that binds external sensory features with internal motivational or emotional factors to form an integrated relational ‘database’ (REFS 4–6; BOX 1). Subsequent work has shown that, beyond the spatial tuning of its principal neurons, many aspects of hippocampal physiology are consistent with the cognitive map function that Tolman envisaged, and it is well established that the hippocampus has a role in encoding information about the world in a way that facilitates flexible and inferential cognitive processes[7–12] . 

More formal theories have also arrived at similar functional specifications for these two structures. For decades, the hippocampus has been synonymous with mapping. Indeed, the cognitive map framework of hippocampal function — first proposed more than 40 years ago in the now classic 1978 work by O’Keefe and Nadel[3] — is the most enduring theory 

By contrast, the OFC has historically been associated with reward- and value-based behaviour[13–20] . Recent thinking, however, has suggested that the OFC also has a cognitive-map-like role. Drawing on ideas from computational reinforcement-learning models, it has been proposed that a fundamental function of the OFC is to form and to 

maintain neural representations of task state: that is, a representation of all the relevant internal and external stimuli or features that define a particular situation in the world[21,22] . Because this function requires the OFC to encode both features of the environment (including observable sensory properties and unobservable, implicit variables that must be inferred) and how relationships between those features might change in different situations, the OFC has been described as a cognitive map of task state[22] . Viewed from this perspective, the OFC and hippocampus appear to be involved in very similar cognitive processes. 

Here, we examine similarities and differences in OFC and hippocampal contributions to cognitive mapping and flexible behaviour. We propose an updated definition of the cognitive map that is faithful to Tolman’s conception but that is grounded in contemporary computational models of reinforcement learning. We review evidence that the hippocampus and OFC have separate roles in cognitive mapping and examine in detail a handful of studies that have directly compared hippocampal and OFC processing in similar behavioural paradigms. Finally, we consider how information might be passed between the OFC and hippocampus and how such a cross-structural dialogue might contribute to behaviour that is dependent on cognitive mapping. Our discussion focuses on studies of the rodent dorsal hippocampus and lateral OFC, although anatomical diversity in both regions[18,23] and potentially across species[24,25] is an important consideration. The overarching message that we hope to convey is that the cognitive map perspective offers a productive unifying direction for future studies of hippocampal and orbitofrontal function. 

## **The road to a cognitive map** 

_**Hippocampus.**_ The discovery of place cells (FIG. 1a–c) quickly transformed our understanding of the hippocampus[26] . In a masterful synthesis, O’Keefe and Nadel[3] proposed the hippocampus as the seat of a Tolmanian cognitive map (BOX 1). However, the parallels between hippocampal function and Tolman’s ideas run far deeper than the existence of place cells. Beyond the intuitive correspondence between Tolman’s 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **513** 

PERSPECTIVES 

## Box 1 | **A modern twist on Tolman’s cognitive map** 

Tolman’s conception of learning was developed in reaction to the prominent stimulus–response theorizing that dominated in his day. In contrast to other researchers of the time, Tolman framed learning as an active process of extracting information from the world, rather than as a passive accumulation of associations imposed on the animal by the environment[5,143–145] . Instead of learning individual action–outcome or cue–outcome relationships by storing specific instances of events, Tolman posited that animals track the underlying structure of the world in a map-like representation of causal associations. Tolman named this mental construct the cognitive map, an evocative description of the mental architecture he was proposing[4] . Just as a physical map allows one to plan novel or unique routes to a previously visited destination, a cognitive map would allow one to combine knowledge about causal relationships in the world in a manner that would enable one to derive novel and unique means of achieving outcomes. Importantly, although Tolman tested his ideas using spatial paradigms[146,147] , he did not intend for cognitive maps to explain spatial planning alone. Instead, he envisioned a much more general system for creating schemas that encapsulate how the world works by tracking latent causal relationships between stimuli, actions, and outcomes. 

Although much of Tolman’s thinking is now accepted[148] , his ideas met resistance when they were first introduced, partially because of his difficulty in developing a theoretical framework that articulated his rather complex perspective[143] . Although a mathematical description of the cognitive map eluded Tolman, subsequent advances in 

computational modelling of cognition and behaviour have expanded the range of processes than can be described mathematically. Many of the ideas that Tolman expressed have been subsumed by current models of learning and decision making. In particular, reinforcement-learning models[61] and their progenitors from psychological learning theory[149–151] have proved to be useful for quantitatively describing different forms of value learning and decision making. Such models distinguish between two fundamental forms of learning and decision making, often labelled 

‘model-free’ and ‘model-based’. Model-free algorithms learn the value of actions but do not learn specific information about the sensory properties, identity or other features of outcomes. Model-based systems store a richer set of associations and capitalize on a world model that tracks how different states of the world are linked together and the specific identity of the outcomes those states contain[152–154] . 

Many behaviours that Tolman attributed to cognitive map function can be solved using model-based reasoning[143,152,154,155] . The cognitive map can thus be defined as an associative structure that facilitates model-based learning and behaviour. This definition remains true to Tolman’s thinking but also takes advantage of recent advances in computational modelling of complex behaviours to understand neural function. In line with this definition, we suggest that the cognitive map entails a number of components. First, there must be a mechanism for recognizing and categorizing the world into discrete states based on features that are relevant to current behavioural demands. Second, the cognitive map requires a means of learning and storing the relationships between world states (that is, how states are connected and how they are arranged relative to one another in the broader space of possible states). Third, the map must encode rich representations of outcomes that are associated with states (including their sensory features and identities) that can be used both to predict specific outcomes and, more generally, to estimate how ‘good’ or ‘bad’ states are expected to be in a way that reflects fluctuations in motivation, changes in the outcomes themselves and animals’ current needs or goals. Finally, there must be a mechanism to use all of this information prospectively to construct novel plans for reaching goals and to predict the outcomes that are likely to follow from combinations of cues or states that have never previously been experienced. The consilience of these modern constructs with Tolman’s older ideas suggests that the neural instantiation of the cognitive map might be distributed across the constellation of structures that support model-based, goal-directed behaviour, including the orbitofrontal complex and the hippocampus. 

use of the term ‘map’ and the spatial tuning of place cells, other properties of hippocampal representations fulfil Tolman’s cognitive criteria. 

For instance, ensembles of hippocampal neurons quickly and obligatorily adopt place-specific firing patterns without explicit reinforcement, and place-cell activity holistically reflects the topology of the environment, as Tolman’s cognitive map was proposed to do[3,12] . However, just as Tolman’s cognitive map extended beyond the spatial domain, place-cell activity encodes more than an objective, allocentric map of space. The spatial firing patterns of hippocampal neurons are often modulated by non-spatial factors, such as the presence or absence of objects[27,28] , attention[29] , conditioned stimuli[30] , novelty[31,32] , perceptual features of the environment[33] and an animal’s internal state[34] . Place cells sometimes cluster their firing fields around — or show ancillary firing fields near — goal locations[35] or places that animals receive reward[36] , indicating that motivational information can be tied to hippocampal spatial representations. 

Moreover, the moment-to-moment dynamics of hippocampal activity suggest a mechanism by which animals might prospectively explore their mental models of the world to aid action selection. For example, in rats carrying out a goal-directed navigation task, hippocampal representations recorded just before an animal initiated a journey encoded paths that led to the next location the animal would visit[37] . In another study, the extent to which pre-trial hippocampal activity was coordinated at an ensemble level predicted future correct choices[38] . Even more 

surprisingly, the hippocampus synthesizes representations that include information beyond the animal’s direct experience. For example, in rats that had been trained on an apparatus with visible but inaccessible corridors, hippocampal representations encoded paths through the environment that crossed into corridors that the animals had never physically entered[39,40] . 

Lest it be thought that the hippocampal cognitive map is solely spatial, we would further emphasize that explicitly non-spatial information is also encoded by hippocampal 

neurons. This is frequently shown in studies of human hippocampal function. For instance, in a task that challenged participants to estimate the value of never-experienced outcomes composed of unusual combinations of familiar foods, the hippocampus repurposed existing representations of the component familiar foods to construct a representation of the composite snacks[41] . The hippocampus was also shown to map social relationships when participants were forced to use this information in order to perform well on a role-playing video game that required interaction with multiple virtual characters[42] . Hippocampal activity has also been shown to reflect the learning of predictive relationships embedded in sequences of visual cues, and the hippocampus is engaged when participants use these implicit stimulus–stimulus associations to guide their decisions[43–46] . 

Such non-spatial representations are not limited to humans. In rats that had been trained to expect sequences of odour cues in a consistent temporal order, hippocampal neurons showed sequence-dependent selectivity for individual odours: that is, 

**514**[|] AUGUST 2016[|] VOLUME 17 

**www.nature.com/nrn** 

PERSPECTIVES 

**==> picture [465 x 313] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b Right turn Left turn<br>c<br>Cell 7<br>Cell 6<br>Cell 5<br>Cell 4<br>Cell 3<br>Cell 2<br>Cell 1<br>d e Right response Left response<br>Left<br>Outcome 1<br>response f<br>Cell 6<br>Cell 5<br>Nose poke Odour Cell 4<br>Cell 3<br>Cell 2<br>Right  Outcome 2 Cell 1<br>response<br>Hippocampal neurons<br>OFC neurons<br>**----- End of picture text -----**<br>


Figure 1[|] **Hippocampal and orbitofrontal cognitive mapping. a** | In spatial tasks, many hippocampal neurons exhibit spatially specific firing. The firing fields (place fields, represented in the image by coloured ellipsoids) of these ‘place cells’ tile the environment. At an ensemble level, the firing of place cells encodes the animal’s position in the environment. **b** | In a reinforcement-learning framework, the ensemble firing of spatially tuned place cells could be thought of as encoding an environmental state space: that is, it would represent both individual states (the circumscribed portions of the environment within which each individual place cell is most active) and how they connect to one another. States in this example environmental state space are coloured to correspond to the place fields shown in part **a** . **c** | As animals traverse the environment, the activity of hippocampal neurons could be thought of as representing trajectories through the environmental state space. The figure shows raster plots that illustrate the firing of seven individual hippocampal cells representing two different state space trajectories (coloured to match parts **a** and **b** ). The trajectories overlap as the animal travels along the central arm of a T-maze but diverge for left and right turns. Different sets of place cells represent positions to the left and 

right of the choice point. In a similar manner, the activity of non-spatially tuned hippocampal neurons could represent position in a more abstract, non-spatial state space. **d** | Similarly, as animals are engaged in decision-making tasks, orbitofrontal cortex (OFC) neurons that are active during the performance of actions or other task events (such as the presentation of cues and outcomes) could encode the current task state. **e** | In contrast to the example state space shown in part **b** , which was defined entirely by position in the environment, the state space for an operant decision-making task might be structured around important task events, including actions (such as making an initial nose poke in an odour sample port), cues (such as the presentation of an odour) and outcomes (such as the delivery of a liquid reward). In these examples, the states represented might be the ‘odour-sampling state’ or the ‘reward-delivery state’. **f** | Because different OFC neurons are activated by specific actions and events (for example, they fire in response to particular odour cues rather than to general odour presentation), the trajectories through state space encoded by OFC ensembles vary depending on the animal’s actions (in this case, a left or right response) and on the information received from the environment. 

they responded to a given odour only when it was a member of one sequence and not when the odour was presented in a different sequence[47,48] . This sort of contextual modulation is also observed in directional place cells[49] , which fire only when an animal passes through a place field in one direction of travel. Just as place cells encode sequences of positions in a way that reflects the order in which they are traversed, the activity of these odour-selective neurons preserved the temporal structure that was present in the environment. 

In all, these data suggest that the hippocampus provides a supremely flexible system for rapidly encoding complex features of the world (both those that are directly experienced and those that are inferred), allowing important information about experience to be encoded in a way that preserves higher-order spatial and relational information. 

_**Orbitofrontal cortex.**_ Although it has long been known that the OFC is important for selecting behaviour that is suited to 

the current context, agreeing on a more precise specification of OFC function has been difficult[1,18,50,51] . Early theories of OFC function centred on its role in suppressing actions that are inappropriate to the current context. However, more recent experimental work has argued against response inhibition as the primary function of the OFC[50,52] , and contemporary theories have arisen from studies of OFC function in associative learning and decision making. Interestingly, OFC activity is not necessary for simple conditioning or even for certain forms 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **515** 

PERSPECTIVES 

## **Glossary** 

## Economic value 

An integrative measure of how good an outcome is to a decision maker that distils the many multidimensional features of that outcome into a unidimensional measure of worth. 

## Outcome devaluation 

The process of rendering a normally appetitive outcome aversive, typically by pairing it with illness. 

## Place cells 

Pyramidal neurons in the hippocampus that fire action potentials when an animal occupies or passes through particular portions of the environment. 

## Reinforcement-learning models 

A collection of machine-learning models that are inspired by psychological learning theory and that are aimed at solving the problem of using experience of the world to guide future behaviour. 

## Representational similarity analysis 

An analysis approach that quantifies the similarity (or dissimilarity) of neural ensemble representations evoked by different conditions. 

## Response inhibition 

The active suppression of actions that are not adaptive in the current setting. 

## Specific satiety 

A means of devaluing a particular outcome by allowing an animal unrestricted access to it before a test session. 

## Stimulus–stimulus associations 

Associations that are formed between neutral stimuli in the environment in the absence of explicit reinforcement. 

## Vicarious trial and error 

(VTE). A pause and orient pattern of behaviour that decision makers often show when deliberating over potential choices. This is thought to be an overt marker of covert, mental processes that simulate potential outcomes of each course of action. 

of more complex learning[52] . However, tasks that force subjects to adjust their behaviour in light of new learning generally depend on OFC function. For instance, in outcome devaluation studies, an intact OFC is necessary for animals to respond to previously acquired cue–outcome and response–outcome associations in a manner that accords with recent changes in outcome value[13,53–56] . Similarly, tasks that hinge on subjects’ knowledge of the specific sensory features of outcomes rather than their more general hedonic properties require OFC function[57–59] . Such diverse findings have proved to be difficult for any single theoretical model to explain[50] . These results might reflect a multiplicity of function within OFC circuits, or it might show that the OFC may have a general underlying function that accounts for its involvement in such a range of behaviours. 

A potentially unifying account suggests that OFC represents task state[22] (FIG. 1d–f). Reinforcement-learning models hinge on the ability of decision-making agents to parse the complexity of the world into discrete, well-defined states[60–63] . According to these models, by segmenting the world in this way and tracking information about the collection of possible world states (that is, the ‘state space’), individuals can assign values to different states, depending on how good or bad those states themselves are and whether they predict future reward or punishment. A recent paper[22] , drawing on previous work that modelled how animals learn deeper world structure when solving conditioning paradigms[62,64,65] , tested reinforcement learning models on a number of behavioural tasks, including classic benchmarks of OFC function, such as reversal learning and devaluation. The results showed that reinforcement-learning models in which the capacity to represent task states was absent or impoverished behaved remarkably like animals with OFC lesions. This suggested a role for the OFC in representing task state, particularly in cases in which states are abstract or not directly observable and must be derived from experience. 

Patterns of activity in the OFC are broadly consistent with task state representations. For example, several results suggest that OFC neurons track variables that are crucial for task performance but that are not directly observable[50,66,67] . In a task in which correct responses depended on the identity of odour cues presented in both the current and previous trials, OFC neurons encoded cue matches and mismatches[66] . Moreover, recent work suggests that OFC ensembles might even encode counterfactual outcomes[68–70] — that is, consequences that would have occurred had the animal behaved differently. Animals could use this sort of ‘what if’ representation to improve future behavioural performance. In agreement with this, it was found that when animals are given incomplete information about a change in task contingencies, OFC neurons update their outcome expectancies before experiencing the complete set of new action– outcome pairings[71] . The OFC also tracks rule or strategy cues that define correct task performance[72,73] . 

Although the OFC is proposed to be especially important for tracking unobservable states, this does not preclude a role in processing sensory-bound state information. Indeed, evidence for OFC encoding of sensory information related to 

task performance is abundant. For instance, OFC neurons encode odour identity when odour cues predict a subsequent outcome and also prospectively signal features of impending rewards predicted by cues[67] . However, just as hippocampal place cells show spatial tuning on tasks that do not explicitly tax spatial abilities, the OFC may encode observable state information even when such encoding is not necessary for the behaviour. This proposal is consistent with recent experimental work[74] showing that rats lacking medial OFC function behaved normally when task state was explicitly signalled but showed deficits when task state was unobservable. This work also highlights a challenge in matching OFC neural activity to animals’ state space representations: even well-controlled behavioural tasks are somewhat under-constrained and could be solved in different ways by individual subjects. Going forward, it will be important to construct paradigms that provide a behavioural readout of the state space that subjects are using[75] or that bias participants towards using particular state spaces[76] . These approaches — combined with ensemble analyses that measure and interpret high-dimensional state space representations[77] — will be necessary to rigorously test the idea that OFC maps task state space. 

These challenges aside, the state space perspective unifies a broad range of data on OFC function. For instance, economic value representations figure prominently in some models of OFC function[17,51] . Such value coding might emerge from the representation of task state, particularly when state value most directly drives behaviour. Similarly, behaviours in which other factors dominate task structure would be expected to elicit more diverse OFC representations. For instance, tasks that depend heavily on action–outcome associations drive strong OFC encoding of action information that is absent in other situations[78,79] . 

It should also be noted that other brain regions, particularly other portions of frontal cortex, may also have an important role in cognitive mapping. Parts of the frontal cortex beyond the OFC have been associated with working memory, representation of task rules and top-down control of behaviour[18] . Such processes are clearly related to the cognitive map proposal, although they may, in some situations, be dissociable (this issue is explored in more detail in REF. 22). More work is necessary to determine how each of these brain regions fits within the framework described here. 

**516**[|] AUGUST 2016[|] VOLUME 17 

**www.nature.com/nrn** 

PERSPECTIVES 

## **Cognitive maps in action** 

Anatomy suggests various pathways by which cognitive maps in the hippocampus and OFC might interact to influence behaviour (BOX 2). Studies that have recorded or manipulated activity in these structures under the same behavioural conditions are of particular value in understanding the nature of this interaction. Here, we discuss four parallel data sets that are particularly amenable to direct comparison of OFC and hippocampal function. 

_**Goal-directed spatial decision making.**_ A series of studies have compared hippocampal and OFC neural representations in rats that perform a T-maze decision-making task[69,80–83] 

(FIG. 2a,b). In this task, rats made decisions by turning left or right at the choice point of the maze. At the beginning of each session, rats relied on trial and error to determine which of three behavioural patterns (always turn left, always turn right or alternate left and right decisions) would be rewarded. Once animals found the correct strategy, a non-signalled switch in reward contingency occurred, and rats were again forced to identify which strategy would be reinforced. At the beginning of task sessions, when reward contingencies were unknown, rats often paused at the choice point before committing to a left or right turn. Tolman called this behaviour vicarious trial and error (VTE) and suggested that animals, when confronted 

with difficult decisions, were mentally simulating the consequences of potential actions before deciding which course of action to undertake[84–86] . In agreement with this, VTE behaviour in the T-maze was found to follow rats’ performance: it decreased as they acquired the correct strategy but then re-emerged following the contingency switch later in the session. 

Hippocampal ensemble activity was recorded as rats performed this T-maze task, and representations at the choice point were examined[83] . During VTE, hippocampal place-cell ensembles encoded paths ahead of the animal, along the potential left- and right-turn options, suggesting that the hippocampus 

## Box 2 | **Hippocampus and orbitofrontal cortex: pathways for interaction** 

There are at least three (not mutually exclusive) pathways by which the hippocampus and orbitofrontal cortex (OFC) might interact to influence behaviour: direct projections between the two structures, indirect projections and convergence on a common target (see the figure). We highlight several candidate pathways that could foster cross-structural communication. 

The ventral striatum (vStr), which is another structure that has long been implicated in reward and motivational processes[171–173] , also receives robust inputs from the OFC and the hippocampus. One subset of ventral striatal neurons encodes proximity to reinforcement with graded increases in firing rate[174–176] (‘ramp cells’), and the temporal patterning of ramp cell spiking is organized with respect to oscillations in the hippocampus[177] , suggesting that hippocampal information processing may ‘clock’ reward-related representations in the ventral striatum[131] . Interestingly, OFC lesions interfere with the coding of reward magnitude in ventral striatal neurons[178] , suggesting that OFC and hippocampal inputs converging in the ventral striatum may support complex, multi-attribute representations of predicted outcomes. 

Direct projections from the hippocampus reach multiple targets in the frontal cortex, including orbitofrontal regions[26,156–158] . These projections are densest from the ventral hippocampus and become gradually scarcer towards the dorsal hippocampus. Projections that arise from the subiculum (which receives a strong, direct projection from CA1) largely mirror the CA1 projection to the cortex, contacting a similar constellation of frontal cortical targets, including the OFC[159] . The OFC does not appear to return a direct projection to the hippocampus. Instead, there are several indirect channels through which orbitofrontal output might reach the **a** hippocampal area. Recent anatomical work has mapped two polysynaptic pathways that link the frontal cortex with dorsal and ventral regions of the hippocampus by thalamic nuclei[160] . In fact, both OFC and hippocampus send projections to and receive projections from the thalamic nucleus reuniens, which appears to have a particularly important role in coordinating bidirectional interactions between frontal cortex and hippocampal nuclei[161–165] . In addition, OFC projections to 

**==> picture [291 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
PFC, prefrontal cortex.<br>a<br>OFC Hippocampus<br>vStr<br>VTA<br>b<br>Postrhinal cortex<br>Perirhinal cortex<br>PFC Subiculum<br>Entorhinal cortex<br>OFC Hippocampus<br>Nucleus reuniens<br>Ventral striatum<br>VTA<br>**----- End of picture text -----**<br>


parahippocampal structures, including the entorhinal, perirhinal and postrhinal cortices, are another path that links OFC and hippocampal processing streams[166] . Additionally, many brain regions receive broadly overlapping projections from the OFC and hippocampus. Several in particular seem striking for their role in learning and decision making. For instance, the ventral tegmental area (VTA) receives indirect input from both the hippocampus and the OFC. Dopamine-containing neurons in the VTA are thought to have a crucial role in associative learning[167] , signalling reward prediction errors that drive learning. Lesions of the OFC alter the encoding of prediction errors in VTA neurons[21,168] . Disrupting hippocampal outflow to VTA also has behavioural consequences, preventing context-induced reinstatement of drug seeking[169] . In addition, electrophysiological experiments have found that hippocampus, VTA and frontal cortical regions are coupled by coherent, low-frequency local field potential oscillations[170] . 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **517** 

## PERSPECTIVES 

**==> picture [533 x 388] intentionally omitted <==**

**----- Start of picture text -----**<br>
Goal-directed spatial decision making: T-maze task<br>a Learning Deliberation b Hippocampus OFC<br>Spatial path simulation Outcome simulation<br>?<br>Food<br>reward<br>Inferring implicit value: sensory-preconditioning task<br>c<br>Preconditioning phase Conditioning phase Test phase<br>Tone A Tone B  Tone B  Reward Tone A<br>Hippocapmus OFC Food reward<br>Tone A Tone B Reward Tone–reward expectancy<br>Left-turn  simulation<br>Right-turn  simulation<br>**----- End of picture text -----**<br>


Figure 2[|] **Cognitive maps in action. a** | In the T-maze decision-making task, animals learn by trial and error that a particular pattern of choices (for example, always turn left at the choice point) will be rewarded. **b** | When animals deliberate over their options at the choice point, hippocampal ensembles simulate spatial trajectories towards potential reward sites. At the same time, reward-sensitive neurons in the orbitofrontal cortex (OFC) become active. It has been proposed that these neurons are engaged in outcome simulation, potentially providing a substrate for the evaluation of action plans represented by hippocampal ensembles. **c** | In the sensory-preconditioning task (as depicted on the top row), animals learn a predictive relationship between two neutral stimuli, such as tones, during the preconditioning phase. During the conditioning phase 

of this task, one of these stimuli is paired with reward. In test sessions, animals responded to the preconditioned cue that, although never directly paired with reward, predicts the occurrence of the conditioned cue. This behaviour has been likened to inference, as animals seem to correctly derive the implicit causal structure of the task (that is, tone A is followed by tone B, which is followed by a reward) despite never having directly experienced this arrangement. Lesion and inactivation data suggest a potential neural model of this task (as depicted on the bottom row) in which hippocampal ensembles encode the relationships between elemental stimuli during the preconditioning and conditioning phases of the task, and this information is accessed by the OFC to support responding during the test session. 

simulated each of the available options to aid decision making. Similar ‘look ahead’ representations in the hippocampus have been observed in rats navigating towards goal locations[87,88] and in human participants carrying out virtual navigation tasks[89,90] . In computational terms, place-cell representations of locations removed from the rats’ actual positions could be thought of as a neural mechanism for exploring the environmental state space encoded in the hippocampus. However, for these sorts of 

state space searches to inform decisions in a useful way, information about the potential outcomes associated with environmental states must also be retrieved. One possibility is that the evaluation of trajectories represented by the hippocampus might take place in structures that receive hippocampal inputs, such as the OFC[83] . 

Subsequent work tested this directly by recording ensembles of OFC neurons as rats performed the T-maze task[69] . OFC cells responded to reward receipt on correct 

trials, which is consistent with previous work. Surprisingly, however, these same reward-responsive OFC neurons were also active when rats paused at the choice point during VTE. Thus, prospective OFC reward-cell activity occurs approximately when an evaluation of hippocampal VTE representations would be expected to arise. Simultaneous recordings of hippocampal and OFC ensembles could clarify the precise temporal relationship between representations in each structure. 

**518**[|] AUGUST 2016[|] VOLUME 17 

**www.nature.com/nrn** 

PERSPECTIVES 

Nevertheless, these data suggest that the hippocampus aids action planning by searching through the space of previously learned (in this case, spatial) associations, whereas the OFC evaluates candidate actions that are represented by the hippocampus to determine which is best. Note that such an evaluative role for the OFC is not inconsistent with its proposed function of state representation, because expected state value is likely to be an important feature of the trajectories that are proposed by the hippocampus. 

The foregoing studies examined hippocampal and OFC activity under behavioural uncertainty and specifically during punctate moments of deliberation. An interesting counterpoint to these data comes from work that examined OFC and hippocampal coding throughout the course of entire trials[91–95] . These experiments tested rats on a plus-shaped maze. Animals began each trial in one of the north or south start arms and had to travel to either the east or west goal arm, where food was delivered. In the ‘place’ version of this task, the reward was reliably located in one of the goal arms, and animals needed to approach this arm regardless of which start arm they began from. In the ‘response’ version of the task, animals learned to make a single response (turn left, for example), regardless of which arm they began from. The structure of the task allowed neural representations to be probed by several challenges, such as reversals of reward contingency or changes between response- and place-based task variants. 

Hippocampal neurons recorded on the task showed spatial responses that were strongly context- or state-dependent[91,94,96] . For instance, a place field located on the south start arm might only be active as the animal ran towards the west goal arm, showing no firing at all when the animal passed in the same direction through the identical location en route to the east goal arm. Similarly, a place field located on the west goal arm might be active only when the animal began its journey from the north start arm, showing no response when the animal began from the south. Thus, these prospective and retrospective place cells signalled spatial information only in the context of where the animal began from, or where it was going to, respectively. These data show that the hippocampus differentially parses identical instances of behaviour depending on non-spatial factors. 

OFC neurons recorded on the same plus-maze task shared common features with hippocampal responses but also 

showed telling differences[92] . Rather than forming discrete place fields, OFC neurons tended to fire evenly along entire paths between start and goal arms. These neurons did not encode space per se; instead, path-sensitive OFC neurons reflected the probability that a particular path would lead to reward delivery, and the firing patterns of these cells tracked behavioural performance following contingency reversals and switches between tasks. This suggests that OFC representations integrated information about responses and reward expectation. Like the context-sensitive place cells observed in this task, OFC responses discriminated journeys through the same physical space depending on where the animal was travelling to and where the journey began. Interestingly, because OFC firing was spread over entire journeys rather than concentrated within discrete locations, as is the case for hippocampal responses, single OFC cells could reflect prospective information before reaching the choice point and retrospective information on final approach to the goal arm. This perhaps suggests a more integrated, large-scale representation of the task in single OFC neurons and a more granular, distributed encoding scheme by hippocampal ensembles[92,97,98] . 

Intriguingly, analyses of local field potentials (LFPs) that were recorded simultaneously from the OFC and hippocampus as rats carried out the plus-maze task hinted at interactions between these structures. During stable task performance, LFPs in the OFC and hippocampus oscillated coherently at theta (5–12 Hz) frequency. However, coherence fell following reversals of reward contingency or switches in task type only to rise again slowly as rats acquired the new behaviour[92] . Thus, learning resulted in a transient decoupling of activity in the hippocampus and the OFC, whereas consistent performance on the task was accompanied by stable interactions between these structures. 

Taken together, the single-unit recordings suggest that both OFC and hippocampal firing patterns are influenced by contextual information related to task performance, such as the start and end locations of journeys across the maze. However, only in OFC ensembles was this contextual modulation dependent on the presence or absence of a food outcome at the end of trajectories. This suggests that the general spatial context modulation observed in the hippocampus gives way to a more elaborate representation in the OFC that is coloured by biological meaning — that is, factors that 

are closely related to the animals’ current needs or goals. The field potential data provide intriguing evidence that information flow between the hippocampus and OFC is a dynamic process that varies with learning. 

One way to conceptualize OFC and hippocampal responses in the plus-maze task is to assume that both structures encoded somewhat overlapping information but with different emphases. Whereas neurons in the hippocampus encoded context information about rats’ journeys while preserving single-cell representations of position, neurons in the OFC seemed to average across large swaths of space, placing a premium on outcome encoding[91,97] . This suggests that cognitive maps in the hippocampus and OFC might contain similar types of information but that they might format this information in different ways. This is consistent with recent work that assesses the hierarchy of spatial, contextual and outcome representations in the OFC and hippocampus[99,100] . In these studies, rats were trained to choose between objects presented in the corners of a testing chamber to earn food reward. However, the objects were not consistently presented in the same corner, and the association between objects and reward was context-dependent: an object that was rewarded in one chamber was unrewarded when presented in the context of a second testing chamber. In this way, the task dissociated the location at which objects were presented from the outcomes that they predicted and also dissociated objects’ reward contingency from their sensory properties, making it possible to test how these task variables are encoded relative to one another. The authors used representational similarity analysis to determine which combinations of task variables evoked the greatest divergence in ensemble representations and which trial types were coded most similarly. 

In hippocampal ensembles, spatial information fractionated neural representations: that is, trials that occurred in different contexts were encoded by anti-correlated patterns of activity, and the location of objects within a context drove the next-greatest divergence in ensemble representations[100] . Nevertheless, non-spatial information was also encoded: representations of object–reward associations were more strongly segregated than representations of the individual objects’ identities. In OFC ensembles, a different hierarchy of representations emerged. Neurons in the OFC distinguished most sharply between rewarded and non-rewarded objects, suggesting that 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **519** 

## PERSPECTIVES 

reward contingency is the major dimension along which OFC representations are constructed in this task[99] . The next greatest separation in ensemble representations reflected the location of items within each context. Finally, the absolute position at which trials occurred was most similarly represented by ensemble activity. These data suggest that, unlike hippocampal representations, which strongly reflected where events occurred, OFC activity principally favoured reward contingency over location. Thus, hippocampal and OFC ensembles both encode a variety of task-relevant information, but each is specialized to emphasize different aspects of the resultant cognitive map. 

_**Inferring implicit value.**_ The OFC and hippocampus are both known to be involved in situations in which previous learning is essential — but in itself insufficient — to support behaviour. A particularly salient example of this is sensory preconditioning[101] (FIG. 2c). In this task, subjects are first exposed to an arbitrary pairing of two neutral stimuli (for example, tone A is followed by tone B). Neither stimulus is paired with reward: subjects are simply presented with the cues in a reliable order. Next, in the conditioning phase of the experiment, one of the previously unrewarded cues is paired with a valuable outcome (for example, tone B is followed by a reward). Finally, in the test session, animals are presented with the preconditioned tone A. Across a range of species[102–110] , subjects’ response to the preconditioned cue is found to be similar to that evoked by the directly conditioned cue (that is, tone B). The interpretation is that subjects inferred the complete causal chain that was made implicit in a piecemeal manner over the different phases of the experiment (tone A is followed by tone B, which is followed by a reward). Model-free cue values are insufficient to explain subjects’ responding at test, suggesting that model-based inference must be at work. 

Parahippocampal structures have long been implicated in supporting inferential behaviour in studies of sensory preconditioning. Early work suggested that hippocampal lesions prevented value inference from the directly conditioned stimulus to its preconditioned partner[104,111] . Although subsequent work has reported that the hippocampus is not necessary for sensory preconditioning, when cues are presented simultaneously as compounds[112] , rather than serially as described above[106] , 

other structures within the hippocampal network have also been implicated. For instance, lesions of the perirhinal[113] or retrosplenial[114] cortex abolish sensory preconditioning. Although these studies leave open what function is supported by processing through the circuit, recent work using a chemogenetic approach found that specifically silencing the retrosplenial cortex during the preconditioning phase prevented value inference at test without influencing first-order conditioning[115] . Thus, hippocampal outflow is potentially crucial to the establishment of the associative scaffolding that is later used to infer the value of the preconditioned cue at test. Consistent with this idea, humans tested on a task that was similar to the sensory preconditioning paradigm used in animals[108] showed enhanced preference for the preconditioned cue at test, and the strength of this preference correlated with hippocampal activity during the learning phase of the task. 

Notably, these data dovetail with evidence that the OFC is necessary for this inference process[116] . Pharmacological inactivation of the rat OFC during the test session abolished responding to the preconditioned cue without affecting responding to the cue that underwent first-order conditioning by being paired directly with reward. These data indicate that the OFC is necessary for using the hippocampus-dependent associative scaffolding acquired in the first phase to predict reward at test. 

Overall, these data suggest that both regions are crucial for value inference in sensory preconditioning but that the dynamics of hippocampal and OFC involvement differ in important ways. For example, whereas OFC function was found to be important for inference at the test stage[116] , hippocampal involvement was confined to the conditioning portion of the experiment in both the human[108] and animal work[115] . These data suggest that the hippocampus is perhaps crucial for encoding a world model that links preconditioned cues with reward, whereas the OFC is more important for accessing this information in the test session to drive responding. 

## **Putting it all together** 

The evidence reviewed here suggests that the OFC and hippocampus each contribute to cognitive mapping and the resultant behaviour. We have emphasized experiments that demonstrate the striking similarity in OFC and hippocampal function. This is not to say, however, that the hippocampus 

and OFC operate synergistically in every situation. For instance, hippocampal lesions selectively alter rats’ preferences for delayed outcomes[117–119] (at least in some testing paradigms; also see REF. 120) without affecting decisions between probabilistic outcomes, whereas OFC lesions produce an inverted pattern of impairment[117] . Similarly, tests of outcome devaluation paint a somewhat divergent picture in which the OFC appears to be involved in behavioural changes that are induced by specific satiety manipulations[121–123] , whereas the hippocampus is not[124–129] . Differences in experimental design often make direct comparisons difficult, but these discrepancies point to potential functional differences. 

It also seems clear that OFC and hippocampus, although perhaps contributing to similar types of behaviours, show some level of domain specificity in their information processing. This arises both from the unique anatomical organization within each structure and the pattern of inputs they receive from other brain regions. The hippocampus is remarkably adept at linking information into temporally patterned sequences that span large ensembles of neurons[130,131] and seems particularly concerned with organizing experience along the axes of space and time. This ability to connect elemental representations and to flexibly produce sequences that reflect learned connections makes the hippocampus well suited to encoding, retrieving and exploring mental models of state spaces[132–134] . By contrast, representations of similar information in the OFC are more rooted in biological importance[20,135,136] . Although it is clear that the OFC has an important role in cognitive processes such as learning and decision making, the behaviours that depend on the OFC are motivated by biological needs. This includes, for instance, learning how to respond to obtain food or liquid reward or, in the case of devaluation, updating associations to direct behaviour away from food that had previously been linked with illness, as well as behaving appropriately in social situations[137–139] . These data argue that, whereas the hippocampus is a flexible and promiscuous processer of abstract associations, OFC information processing may be more grounded in items of immediate biological relevance. 

One way to view these distinctions is to consider that there are multiple components to the cognitive map. In other words, just as real-world maps often consist of multiple 

**520**[|] AUGUST 2016[|] VOLUME 17 

**www.nature.com/nrn** 

PERSPECTIVES 

overlays that describe different aspects of the environment, so too must our global cognitive map be constructed of multiple informational layers that can be turned on and off as necessary. One efficient way of doing this is to task different modules in the brain with representing different informational layers of the global map, thereby distributing cognitive maps across multiple neural structures. If cognitive maps were to be distributed across multiple neural structures, coordination between brain regions would be important for supporting adaptive behaviour. What precise form might this cross-structural dialogue take? One intuitive idea is that OFC input to hippocampus contributes to the extra-spatial modulation of place-selective hippocampal neurons, giving rise to spatial representations that are sensitive to reward, goals or motivational states. The OFC might be thought of as imbuing the hippocampal map with information about expected outcomes to facilitate goal-dependent navigation. Conversely, spatial or relational information conveyed by the hippocampus to the OFC might allow OFC outcome expectancies to become bound with information about spatial positions or more abstract relationships between potential outcomes and ‘paths’ to obtain those outcomes, whether spatial, as in a maze, or non-spatial, as in sensory preconditioning. Organizing OFC representations in this way could facilitate the development of integrated action–outcome associations by tying abstract outcome predictions (such as a cherry- or banana-flavoured sucrose pellet) to locations that are reached by particular responses (for example, go left at a maze choice point to get the banana pellet, or press the right lever in an operant box to get the cherry pellet). Time-sensitive hippocampal representations[140–142] might also confer temporal specificity to OFC expectancy representations, either directly or through interactions in some downstream areas, such as the ventral striatum. 

Although we are in the early stages of understanding the interplay between brain regions, the increasing sophistication of techniques for measuring and manipulating the activity of neural circuits in projectionand cell-type-specific ways draws the issue of cross-structural interactions to the fore. We suggest that these approaches, when applied to interactions between hippocampus and OFC, might be particularly fruitful in improving our understanding of how cognitive-map-dependent behaviour is learned and deployed. 

_Andrew M. Wikenheiser is at the Intramural Research Program, National Institute on Drug Abuse, Baltimore, Maryland 21224, USA._ 

_andrew.wikenheiser@nih.gov_ 

_Geoffrey Schoenbaum is at the Intramural Research Program, National Institute on Drug Abuse, Baltimore, Maryland 21224, USA; the Department of Anatomy and Neurobiology, University of Maryland, Baltimore, Maryland 21201, USA; and the Department of Neuroscience, Johns Hopkins University, Baltimore, Maryland 21205, USA._ 

_geoffrey.schoenbaum@nih.gov_ 

doi:10.1038/nrn.2016.56 Published online 3 Jun 2016 

1. Rudebeck, P. H. & Murray, E. A. The orbitofrontal oracle: cortical mechanisms for the prediction and evaluation of specific behavioral outcomes. _Neuron_ **84** , 1143–1156 (2014). 

2. Buckner, R. L. The role of the hippocampus in prediction and imagination. _Annu. Rev. Psychol._ **61** , 27–48 (2010). 

3. O’Keefe, J. & Nadel, L. _The Hippocampus as a Cognitive Map_ (Clarendon Press, 1978). 

4. Tolman, E. C. Cognitive maps in rats and men. _Psychol. Rev._ **55** , 189–208 (1948). 

5. Tolman, E. C. _Purposive Behavior in Animals and Men_ (Appleton-Century-Crofts, 1932). 

6. Tolman, E. C. & Brunswik, E. The organism and the causal texture of the environment. _Psychol. Rev._ **42** , 43 (1935). 

7. Buzsáki, G. & Moser, E. I. Memory, navigation and theta rhythm in the hippocampal–entorhinal system. _Nat. Neurosci._ **16** , 130–138 (2013). 

8. Eichenbaum, H. & Cohen, Neal, J. Can we reconcile the declarative memory and spatial navigation views on hippocampal function? _Neuron_ **83** , 764–770 (2014). 

9. Eichenbaum, H., Dudchenko, P., Wood, E., Shapiro, M. 

   - & Tanila, H. The hippocampus, memory, and place 

   - cells: is it spatial memory or a memory space? _Neuron_ **23** , 209–226 (1999). 

10. Wikenheiser, A. M. & Redish, A. D. Decoding the cognitive map: ensemble hippocampal sequences and decision making. _Curr. Opin. Neurobiol._ **32** , 8–15 (2015). 

11. Dudchenko, P. A. & Wood, E. R. Place fields and the cognitive map. _Hippocampus_ **25** , 709–712 (2015). 

12. Redish, A. D. _Beyond the Cognitive Map: From Place Cells to Episodic Memory_ (MIT Press, 1999). 

13. Gallagher, M., McMahan, R. & Schoenbaum, G. Orbitofrontal cortex and representation of incentive value in associative learning. _J. Neurosci._ **19** , 6610–6614 (1999). 

14. Tremblay, L. & Schultz, W. Relative reward preference in primate orbitofrontal cortex. _Nature_ **398** , 704–708 (1999). 

15. O’Doherty, J., Kringelbach, M. L., Rolls, E. T., Hornak, J. & Andrews, C. Abstract reward and punishment representations in the human orbitofrontal cortex. _Nat. Neurosci._ **4** , 95–102 

   - (2001). 

16. Gottfried, J. A., O’Doherty, J. & Dolan, R. J. Encoding predictive reward value in human amygdala and orbitofrontal cortex. _Science_ **301** , 1104–1107 (2003). 

17. Padoa-Schioppa, C. & Assad, J. A. Neurons in the orbitofrontal cortex encode economic value. _Nature_ **441** , 223–226 (2006). 

18. Wallis, J. D. Orbitofrontal cortex and its contribution to decision-making. _Annu. Rev. Neurosci._ **30** , 31–56 (2007). 

19. McDannald, M. A., Jones, J. L., Takahashi, Y. K. & Schoenbaum, G. Learning theory: a driving force in understanding orbitofrontal function. _Neurobiol. Learn. Mem._ **108** , 22–27 (2014). 

20. Thorpe, S., Rolls, E. & Maddison, S. The orbitofrontal cortex: neuronal activity in the behaving monkey. _Exp. Brain Res._ **49** , 93–115 (1983). 

21. Takahashi, Y. K. _et al._ Expectancy-related changes in firing of dopamine neurons depend on orbitofrontal cortex. _Nat. Neurosci._ **14** , 1590–1597 (2011). 

22. Wilson, R. C., Takahashi, Y. K., Schoenbaum, G. & Niv, Y. Orbitofrontal cortex as a cognitive map of task space. _Neuron_ **81** , 267–279 (2014). 

23. Fanselow, M. S. & Dong, H. W. Are the dorsal and ventral hippocampus functionally distinct structures? _Neuron_ **65** , 7–19 (2010). 

24. Wallis, J. D. Cross-species studies of orbitofrontal cortex and value-based decision-making. _Nat. Neurosci._ **15** , 13–19 (2012). 

25. Strange, B. A., Witter, M. P., Lein, E. S. & Moser, E. I. Functional organization of the hippocampal longitudinal axis. _Nat. Rev. Neurosci._ **15** , 655–669 (2014). 

26. Andersen, P., Morris, R., Amaral, D., Bliss, T. & O’Keefe, J. _The Hippocampus Book_ (Oxford Univ. Press, 2006). 

27. Komorowski, R. W., Manns, J. R. & Eichenbaum, H. Robust conjunctive item–place coding by hippocampal neurons parallels learning what happens where. 

   - _J. Neurosci._ **29** , 9918–9929 (2009). 

28. Manns, J. R. & Eichenbaum, H. A cognitive map for object memory in the hippocampus. _Learn. Mem._ **16** , 616–624 (2009). 

29. Fenton, A. A. _et al._ Attention-like modulation of hippocampus place cell discharge. _J. Neurosci._ **30** , 4613–4625 (2010). 

30. Moita, M. A., Rosis, S., Zhou, Y., LeDoux, J. E. & Blair, H. T. Hippocampal place cells acquire locationspecific responses to the conditioned stimulus during auditory fear conditioning. _Neuron_ **37** , 485–497 (2003). 

31. Larkin, M. C., Lykken, C., Tye, L. D., Wickelgren, J. G. & Frank, L. M. Hippocampal output area CA1 broadcasts a generalized novelty signal during an object–place recognition task. _Hippocampus_ **24** , 773–783 (2014). 

32. Lever, C. _et al._ Environmental novelty elicits a later theta phase of firing in CA1 but not subiculum. _Hippocampus_ **20** , 229–234 (2010). 

33. Quirk, G. J., Muller, R. U. & Kubie, J. L. The firing of hippocampal place cells in the dark depends on the rat’s recent experience. _J. Neurosci._ **10** , 2008–2017 (1990). 

34. Kennedy, P. J. & Shapiro, M. L. Motivational states activate distinct hippocampal representations to guide goal-directed behaviors. _Proc. Natl Acad. Sci. USA_ **106** , 10805–10810 (2009). 

35. Hollup, S. A., Molden, S., Donnett, J. G., Moser, M.-B. & Moser, E. I. Accumulation of hippocampal place fields at the goal location in an annular watermaze task. _J. Neurosci._ **21** , 1635–1644 (2001). 

36. Hok, V. _et al._ Goal-related activity in hippocampal place cells. _J. Neurosci._ **27** , 472–482 (2007). 

37. Pfeiffer, B. E. & Foster, D. J. Hippocampal place-cell sequences depict future paths to remembered goals. _Nature_ **497** , 74–79 (2013). 

38. Singer, A. C., Carr, M. F., Karlsson, M. P. & Frank, L. M. Hippocampal SWR activity predicts correct decisions during the initial learning of an alternation task. _Neuron_ **77** , 1163–1173 (2013). 

39. Dragoi, G. & Tonegawa, S. Preplay of future place cell sequences by hippocampal cellular assemblies. _Nature_ **469** , 397–401 (2011). 

40. Ólafsdóttir, H. F., Barry, C., Saleem, A. B., Hassabis, D. & Spiers, H. J. Hippocampal place cells construct reward related sequences through unexplored space. _eLife_ **4** , e06063 (2015). 

41. Barron, H. C., Dolan, R. J. & Behrens, T. E. J. Online evaluation of novel choices by simultaneous representation of multiple memories. _Nat. Neurosci._ **16** , 1492–1498 (2013). 

42. Tavares, R. M. _et al._ A map for social navigation in the human brain. _Neuron_ **87** , 231–243 (2015). 

43. Bornstein, A. M. & Daw, N. D. Cortical and hippocampal correlates of deliberation during modelbased decisions for rewards in humans. _PLoS Comput. Biol._ **9** , e1003387 (2013). 

44. Bornstein, A. M. & Daw, N. D. Dissociating hippocampal and striatal contributions to sequential prediction learning. _Eur. J. Neurosci._ **35** , 1011–1023 (2012). 

45. Schapiro, A. C., Turk-Browne, N. B., Norman, K. A. & Botvinick, M. M. Statistical learning of temporal community structure in the hippocampus. _Hippocampus_ **26** , 3–8 (2015). 

46. Shohamy, D. & Turk-Browne, N. B. Mechanisms for widespread hippocampal involvement in cognition. _J. Exp. Psychol. Gen._ **142** , 1159 (2013). 

47. Ginther, M. R., Walsh, D. F. & Ramus, S. J. Hippocampal neurons encode different episodes in an overlapping sequence of odors task. _J. Neurosci._ **31** , 2706–2711 (2011). 

48. Allen, T. A., Salz, D. M., McKenzie, S. & Fortin, N. J. Nonspatial sequence coding in CA1 neurons. _J. Neurosci._ **36** , 1547–1563 (2016). 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **521** 

## PERSPECTIVES 

   73. Tsujimoto, S. & Sawaguchi, T. Neuronal activity representing temporal prediction of reward in the primate prefrontal cortex. _J. Neurophysiol._ **93** , 3687–3692 (2005). 

49. McNaughton, B. L., Barnes, C. A. & O’Keefe, J. The contributions of position, direction, and velocity to single unit activity in the hippocampus of freelymoving rats. _Exp. Brain Res._ **52** , 41–49 (1983). 

   74. Bradfield, L. A., Dezfouli, A., van Holstein, M., Chieng, B. & Balleine, B. W. Medial orbitofrontal cortex mediates outcome retrieval in partially observable task situations. _Neuron_ **88** , 1268–1280 (2015). 

50. Stalnaker, T. A., Cooch, N. K. & Schoenbaum, G. What the orbitofrontal cortex does not do. _Nat. Neurosci._ **18** , 620–627 (2015). 

51. Padoa-Schioppa, C. Neurobiology of economic choice: a good-based model. _Annu. Rev. Neurosci._ **34** , 333 (2011). 

   75. Gläscher, J., Daw, N., Dayan, P. & O’Doherty, J. P. States versus rewards: dissociable neural prediction error signals underlying model-based and modelfree reinforcement learning. _Neuron_ **66** , 585–595 (2010). 

52. Schoenbaum, G., Roesch, M. R., Stalnaker, T. A. & Takahashi, Y. K. A new perspective on the role of the orbitofrontal cortex in adaptive behaviour. _Nat. Rev. Neurosci._ **10** , 885–892 (2009). 

   76. Riceberg, J. S. & Shapiro, M. L. Reward stability determines the contribution of orbitofrontal cortex to adaptive behavior. _J. Neurosci._ **32** , 16402–16409 (2012). 

53. West, E. A., Forcelli, P. A., McCue, D. L. & Malkova, L. Differential effects of serotonin-specific and excitotoxic lesions of OFC on conditioned reinforcer devaluation and extinction in rats. _Behav. Brain Res._ **246** , 10–14 (2013). 

   77. Doll, B. B., Duncan, K. D., Simon, D. A., Shohamy, D. 

54. Rhodes, S. E. & Murray, E. A. Differential effects of amygdala, orbital prefrontal cortex, and prelimbic lesions on goal-directed behavior in rhesus macaques. _J. Neurosci._ **33** , 3380–3389 (2013). 

55. Izquierdo, A. D., Suda, R. K. & Murray, E. A. Bilateral orbital prefrontal cortex lesions in rhesus monkeys disrupt choices guided by both reward value and reward contingency. _J. Neurosci._ **24** , 7540–7548 (2004). 

      - & Daw, N. D. Model-based choices involve prospective neural activity. _Nat. Neurosci._ **18** , 767–772 (2015). 

   78. Feierstein, C. E., Quirk, M. C., Uchida, N., Sosulski, D. L. & Mainen, Z. F. Representation of spatial goals in rat orbitofrontal cortex. _Neuron_ **60** , 495–507 (2006). 

   79. Roesch, M. R., Taylor, A. R. & Schoenbaum, G. Encoding of time-discounted rewards in orbitofrontal cortex is independent of value representation. _Neuron_ **51** , 509–520 (2006). 

56. Gremel, C. M. & Costa, R. M. Orbitofrontal and striatal circuits dynamically encode the shift between goal-directed and habitual actions. _Nat. Commun._ **4** , 2264 (2013). 

57. Ostlund, S. B. & Balleine, B. W. Orbitofrontal cortex mediates outcome encoding in Pavlovian but not instrumental learning. _J. Neurosci._ **27** , 4819–4825 (2007). 

   80. Gupta, A. S., van der Meer, M. A., Touretzky, D. S. & Redish, A. D. Segmentation of spatial experience by hippocampal theta sequences. _Nat. Neurosci._ **15** , 1032–1039 (2012). 

   81. Blumenthal, A., Steiner, A., Seeland, K. D. & Redish, A. D. Effects of pharmacological manipulations of NMDA-receptors on deliberation in the multiple-T task. _Neurobiol. Learn. Mem._ **95** , 376–384 (2011). 

   82. Gupta, A. S., van der Meer, M. A., Touretzky, D. S. & Redish, A. D. Hippocampal replay is not a simple function of experience. _Neuron_ **65** , 695–705 (2010). 

   83. Johnson, A. & Redish, A. D. Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. _J. Neurosci._ **27** , 12176–12189 (2007). 

58. McDannald, M. A., Saddoris, M. P., Gallagher, M. & Holland, P. C. Lesions of orbitofrontal cortex impair rats’ differential outcome expectancy learning but not conditioned stimulus-potentiated feeding. _J. Neurosci._ **25** , 4626–4632 (2005). 

59. McDannald, M. A., Lucantonio, F., Burke, K. A., Niv, Y. & Schoenbaum, G. Ventral striatum and orbitofrontal cortex are both required for model-based, but not model-free, reinforcement learning. _J. Neurosci._ **31** , 2700–2705 (2011). 

   84. Tolman, E. C. Prediction of vicarious trial and error by means of the schematic sowbug. _Psychol. Rev._ **46** , 318–336 (1939). 

60. Redish, A. D., Jensen, S., Johnson, A. & KurthNelson, Z. Reconciling reinforcement learning models with behavioral extinction and renewal: Implications for addiction, relapse, and problem gambling. _Psychol. Rev._ **114** , 784–805 (2007). 

   85. Muenzinger, K. F. Vicarious trial and error at a point of choice: I. A general survey of its relation to learning efficiency. _Pedagog. Semin. J. Genet. Psychol._ **53** , 75–86 (1938). 

   86. Redish, A. D. Vicarious trial and error. _Nat. Rev. Neurosci._ **17** , 147–159 (2016). 

61. Sutton, R. S. & Barto, A. G. _Reinforcement Learning: An Introduction_ (MIT Press, 1998). 

   87. Wikenheiser, A. M. & Redish, A. D. Hippocampal theta sequences reflect current goals. _Nat. Neurosci._ **18** , 289–294 (2015). 

62. Gershman, S. J. & Niv, Y. Learning latent structure: carving nature at its joints. _Curr. Opin. Neurobiol._ **20** , 251–256 (2010). 

63. O’Doherty, J. P., Lee, S. W. & McNamee, D. The 88. Bieri, K. W., Bobbitt, K. N. & Colgin, L. L. Slow and structure of reinforcement-learning mechanisms in the fast gamma rhythms coordinate different spatial human brain. _Curr. Opin. Behav. Sci._ **1** , 94–100 coding modes in hippocampal place cells. _Neuron_ **82** , (2015). 670–681 (2014). 

   89. Simon, D. A. & Daw, N. D. Neural correlates of forward planning in a spatial decision task in humans. _J. Neurosci._ **31** , 5526–5539 (2011). 

64. Gershman, S. J., Blei, D. & Niv, Y. Context, learning and extinction. _Psychol. Rev._ **117** , 197–209 (2010). 

65. Courville, A. C., Daw, N. D. & Touretzky, D. S. Similarity and discrimination in classical conditioning: a latent variable account. _Adv. Neural Inform. Process. Syst._ **17** , 313–320 (2005). 

   90. Chadwick, M. J., Jolly, A. E., Amos, D. P., Hassabis, D. & Spiers, H. J. A goal direction signal in the human entorhinal/subicular region. _Curr. Biol._ **25** , 87–92 (2015). 

66. Ramus, S. J. & Eichenbaum, H. Neural correlates of olfactory recognition memory in the rat orbitofrontal cortex. _J. Neurosci._ **20** , 8199–8208 (2000). 

67. Schoenbaum, G. & Eichenbaum, H. Information coding in the rodent prefrontal cortex. I. Single-neuron activity in orbitofrontal cortex compared with that in piriform cortex. _J. Neurophysiol._ **74** , 733–750 (1995). 

68. Steiner, A. P. & Redish, A. D. Behavioral and neurophysiological correlates of regret in rat decisionmaking on a neuroeconomic task. _Nat. Neurosci._ **17** , 995–1002 (2014). 

69. Steiner, A. P. & Redish, A. D. The road not taken: neural correlates of decision making in orbitofrontal cortex. _Front. Neurosci._ **6** , 131 (2012). 

70. Abe, H. & Lee, D. Distributed coding of actual and hypothetical outcomes in the orbital and dorsolateral prefrontal cortex. _Neuron_ **70** , 731–741 (2011). 

71. Stalnaker, T. A. _et al._ Orbitofrontal neurons infer the value and identity of predicted outcomes. _Nat. Commun._ **5** , 3926 (2014). 

   91. Ferbinteanu, J., Shirvalkar, P. & Shapiro, M. L. Memory modulates journey-dependent coding in the rat hippocampus. _J. Neurosci._ **31** , 9135–9146 (2011). 

   92. Young, J. J. & Shapiro, M. L. Dynamic coding of goaldirected paths by orbital prefrontal cortex. _J. Neurosci._ **31** , 5989–6000 (2011). 

   93. Rich, E. L. & Shapiro, M. Rat prefrontal cortical neurons selectively code strategy switches. _J. Neurosci._ **29** , 7208–7219 (2009). 

   94. Ferbinteanu, J. & Shapiro, M. L. Prospective and retrospective memory coding in the hippocampus. _Neuron_ **40** , 1227–1239 (2003). 

   95. Bahar, A. S. & Shapiro, M. L. Remembering to learn: independent place and journey coding mechanisms contribute to memory transfer. _J. Neurosci._ **32** , 2191–2203 (2012). 

   96. Shapiro, M. L. & Ferbinteanu, J. Relative spike timing in pairs of hippocampal neurons distinguishes the beginning and end of journeys. _Proc. Natl Acad. Sci. USA_ **103** , 4287–4292 (2006). 

   97. Young, J. J. & Shapiro, M. L. The orbitofrontal cortex and response selection. _Ann. NY Acad. Sci._ **1239** , 25–32 (2011). 

72. Tsujimoto, S., Genovesio, A. & Wise, S. P. Monkey orbitofrontal cortex encodes response choices near feedback time. _J. Neurosci._ **29** , 2569–2574 (2009). 

98. Shapiro, M. L., Riceberg, J. S., Seip-Cammack, K. & Guise, K. G. in _Space, Time and Memory in the Hippocampal Formation_ (eds Derdikman, D. & Knierim, J. J.) 517–560 (Springer, 2014). 

99. Farovik, A. _et al._ Orbitofrontal cortex encodes memories within value-based schemas and represents contexts that guide memory retrieval. _J. Neurosci._ **35** , 8333–8344 (2015). 

100. McKenzie, S. _et al._ Hippocampal representation of related and opposing memories develop within distinct, hierarchically organized neural schemas. _Neuron_ **83** , 202–215 (2014). 

101. Brogden, W. J. Sensory pre-conditioning. _J. Exp. Psychol._ **25** , 323–332 (1939). 

102. Matsumoto, Y., Hirashima, D. & Mizunami, M. Analysis and modeling of neural processes underlying sensory preconditioning. _Neurobiol. Learn. Mem._ **101** , 103–113 (2013). 

103. Muller, D., Gerber, B., Hellstern, F., Hammer, M. & Menzel, R. Sensory preconditioning in honeybees. _J. Exp. Biol._ **203** , 1351–1364 (2000). 

104. Port, R. L., Beggs, A. L. & Patterson, M. M. Hippocampal substrate of sensory associations. _Physiol. Behav._ **39** , 643–647 (1987). 

105. Hall, D. & Suboski, M. D. Sensory preconditioning and secord-order conditioning of alarm reactions in zebra danio fish ( _Brachydanio rerio_ ). _J. Comp. Psychol._ **109** , 76 (1995). 

106. Ward-Robinson, J. _et al._ Excitotoxic lesions of the hippocampus leave sensory preconditioning intact: implications for models of hippocampal functioning. _Behav. Neurosci._ **115** , 1357–1362 (2001). 

107. Yu, T., Lang, S., Birbaumer, N. & Kotchoubey, B. Neural correlates of sensory preconditioning: a preliminary fMRI investigation. _Hum. Brain Mapp._ **35** , 1297–1304 (2014). 

108. Wimmer, G. E. & Shohamy, D. Preference by association: how memory mechanisms in the hippocampus bias decisions. _Science_ **338** , 270–273 (2012). 

109. Karn, H. W. Sensory pre-conditioning and incidental learning in human subjects. _J. Exp. Psychol._ **37** , 540 (1947). 

110. Kojima, S. _et al._ Sensory preconditioning for feeding response in the pond snail, _Lymnaea stagnalis_ . _Brain Res._ **808** , 113–115 (1998). 

111. Port, R. L. & Patterson, M. M. Fimbrial lesions and sensory preconditioning. _Behav. Neurosci._ **98** , 584 (1984). 

112. Rescorla, R. A. & Cunningham, C. L. Within-compound flavor associations. _J. Exp. Psychol. Anim. Behav. Process_ **4** , 267–275 (1978). 

113. Nicholson, D. A. & Freeman Jr, J. H. Lesions of the perirhinal cortex impair sensory preconditioning in rats. _Behav. Brain Res._ **112** , 69–75 (2000). 

114. Robinson, S., Keene, C. S., Iaccarino, H. F., Duan, D. & Bucci, D. J. Involvement of retrosplenial cortex in forming associations between multiple sensory stimuli. _Behav. Neurosci._ **125** , 578 (2011). 

115. Robinson, S. _et al._ Chemogenetic silencing of neurons in retrosplenial cortex disrupts sensory preconditioning. _J. Neurosci._ **34** , 10982–10988 (2014). 

116. Jones, J. L. _et al._ Orbitofrontal cortex supports behavior and learning using inferred but not cached values. _Science_ **338** , 953–956 (2012). 

117. Abela, A. R. & Chudasama, Y. Dissociable contributions of the ventral hippocampus and orbitofrontal cortex to decision-making with a delayed or uncertain outcome. _Eur. J. Neurosci._ **37** , 640–647 (2013). 

118. Mariano, T. Y. _et al._ Impulsive choice in hippocampal but not orbitofrontal cortex-lesioned rats on a nonspatial decision-making maze task. _Eur._ 

   - _J. Neurosci._ **30** , 472–484 (2009). 

119. Cheung, T. H. C. & Cardinal, R. N. Hippocampal lesions facilitate instrumental learning with delayed reinforcement but induce impulsive choice in rats. _BMC Neurosci._ **6** , 36 (2005). 

120. Bett, D., Murdoch, L. H., Wood, E. R. & Dudchenko, P. A. Hippocampus, delay discounting, and vicarious trial-and-error. _Hippocampus_ **25** , 643–654 (2015). 

121. O’Doherty, J. _et al._ Sensory-specific satiety-related olfactory activation of the human orbitofrontal cortex. _Neuroreport_ **11** , 399–403 (2000). 

122. West, E. A., DesJardin, J. T., Gale, K. & Malkova, L. Transient inactivation of orbitofrontal cortex blocks reinforcer devaluation in macaques. _J. Neurosci._ **31** , 15128–15135 (2011). 

123. Schoenbaum, G. & Roesch, M. Orbitofrontal cortex, associative learning, and expectancies. _Neuron_ **47** , 633–636 (2005). 

**522**[|] AUGUST 2016[|] VOLUME 17 

**www.nature.com/nrn** 

PERSPECTIVES 

124. Higgs, S., Williamson, A. C., Rotshtein, P. & Humphreys, G. W. Sensory-specific satiety is intact in amnesics who eat multiple meals. _Psychol. Sci._ **19** , 623–628 (2008). 

125. Corbit, L. H., Ostlund, S. B. & Balleine, B. W. Sensitivity to instrumental contingency degradation is mediated by the entorhinal cortex and its efferents via the dorsal hippocampus. _J. Neurosci._ **22** , 10976–10984 (2002). 

126. Corbit, L. H. & Balleine, B. W. The role of the hippocampus in instrumental conditioning. _J. Neurosci._ **20** , 4233–4239 (2000). 

127. Chudasama, Y., Wright, K. S. & Murray, E. A. Hippocampal lesions in rhesus monkeys disrupt emotional responses but not reinforcer devaluation effects. _Biol. Psychiatry_ **63** , 1084–1091 (2008). 

128. Machado, C. J. & Bachevalier, J. The impact of selective amygdala, orbital frontal cortex, or hippocampal formation lesions on established social relationships in rhesus monkeys ( _Macaca mulatta_ ). _Behav. Neurosci._ **120** , 761 (2006). 

129. Reichelt, A. C., Lin, T. E., Harrison, J. J., Honey, R. C. & Good, M. A. Differential role of the hippocampus in response-outcome and context-outcome learning: evidence from selective satiation procedures. _Neurobiol. Learn. Mem._ **96** , 248–253 (2011). 

130. Carr, M. F., Jadhav, S. P. & Frank, L. M. Hippocampal replay in the awake state: a potential substrate for memory consolidation and retrieval. _Nat. Neurosci._ **14** , 147–153 (2011). 

131. Malhotra, S., Cross, R. W. & van der Meer, M. A. Theta phase precession beyond the hippocampus. _Rev. Neurosci._ **23** , 39–65 (2012). 

132. van der Meer, M., Kurth-Nelson, Z. & Redish, A. D. Information processing in decision-making systems. _Neuroscientist_ **18** , 342–359 (2012). 

133. Johnson, A., van der Meer, M. A. & Redish, A. D. Integrating hippocampus and striatum in decisionmaking. _Curr. Opin. Neurobiol._ **17** , 692–697 (2007). 

134. Kurth-Nelson, Z., Bickel, W. & Redish, A. D. A theoretical account of cognitive effects in delay discounting. _Eur. J. Neurosci._ **35** , 1052–1064 (2012). 

135. Rolls, E., Sienkiewicz, Z. & Yaxley, S. Hunger modulates the responses to gustatory stimuli of single neurons in the caudolateral orbitofrontal cortex of the macaque monkey. _Eur. J. Neurosci._ **1** , 53–60 (1989). 

136. Rolls, E. T. The functions of the orbitofrontal cortex. _Brain Cogn._ **55** , 11–29 (2004). 

137. Pearson, J. M., Watson, K. K. & Platt, M. L. Decision making: the neuroethological turn. _Neuron_ **82** , 950–965 (2014). 

138. Watson, K. K. & Platt, M. L. Social signals in primate orbitofrontal cortex. _Curr. Biol._ **22** , 2268–2273 (2012). 

139. Ross, R., LoPresti, M., Schon, K. & Stern, C. Role of the hippocampus and orbitofrontal cortex during the disambiguation of social cues in working memory. 

   - _Cogn. Affect. Behav. Neurosci._ **13** , 900–915 (2013). 

140. Eichenbaum, H. Memory on time. _Trends Cogn. Sci._ **17** , 81–88 (2013). 

141. Eichenbaum, H. Time cells in the hippocampus: a new dimension for mapping memories. _Nat. Rev. Neurosci._ **15** , 732–744 (2014). 

142. MacDonald, C. J., Lepage, K. Q., Eden, U. T. & Eichenbaum, H. Hippocampal “time cells” bridge the gap in memory for discontiguous events. _Neuron_ **71** , 737–749 (2011). 

143. Johnson, A. & Crowe, D. Revisiting Tolman: theories and cognitive maps. _Cognitive Critique_ **1** , 43–72 (2009). 

144. Tolman, E. C. There is more than one kind of learning. _Psychol. Rev._ **56** , 144 (1949). 

145. Tolman, E. C. The determiners of behavior at a choice point. _Psychol. Rev._ **45** , 1–41 (1938). 

146. Tolman, E. C., Ritchie, B. F. & Kalish, D. Studies in spatial learning. I. Orientation and the short-cut. _J. Exp. Psychol._ **36** , 13–24 (1946). 

147. Tolman, E. C., Ritchie, B. F. & Kalish, D. Studies in spatial learning. II. Place learning versus response learning. _J. Exp. Psychol._ **36** , 221–229 (1946). 

148. Schiller, D. _et al._ Memory and space: towards an understanding of the cognitive map. _J. Neurosci._ **35** , 13904–13911 (2015). 

149. Rescorla, R. A. & Wagner, A. R. in _Classical_ 

_Conditioning II: Current Research and Theory_ (eds Black, A. H. & Prokasy, W. F.) 64–99 (AppletonCentury-Crofts, 1972). 

150. Pearce, J. M. & Hall, G. A model for Pavlovian learning: variations in the effectiveness of conditioned but not of unconditioned stimuli. _Psychol. Rev._ **87** , 532–552 (1980). 

151. Mackintosh, N. J. A theory of attention: variations in the associability of stimuli with reinforcement. _Psychol. Rev._ **82** , 276–298 (1975). 

152. Doll, B. B., Shohamy, D. & Daw, N. D. Multiple memory systems as substrates for multiple decision systems. _Neurobiol. Learn. Mem._ **117** , 4–13 (2015). 

153. Dayan, P. & Daw, N. D. Decision theory, reinforcement learning, and the brain. _Cogn. Affect. Behav. Neurosci._ **8** , 429–453 (2008). 

154. Balleine, B. W., Daw, N. D. & O’Doherty, J. P. in _Neuroeconomics: Decision Making and the Brain_ (eds Glimcher, P. W. & Fehr, E.) 367–385 (Academic Press, 2008). 

155. Daw, N. D., Niv, Y. & Dayan, P. Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. _Nat. Neurosci._ **8** , 1704–1711 (2005). 

156. Jay, T. M. & Witter, M. P. Distribution of hippocampal CA1 and subicular efferents in the prefrontal cortex of the rat studied by means of anterograde transport of _Phaseolus vulgaris_ -leucoagglutinin. _J. Comp. Neurol._ **313** , 574–586 (1991). 

157. Barbas, H. & Blatt, G. J. Topographically specific hippocampal projections target functionally distinct prefrontal areas in the rhesus monkey. _Hippocampus_ **5** , 511–533 (1995). 

158. Insausti, R. & Munoz, M. Cortical projections of the non-entorhinal hippocampal formation in the cynomolgus monkey ( _Macaca fascicularis_ ). _Eur. J. Neurosci._ **14** , 435–451 (2001). 

159. Aggleton, J. P. & Christiansen, K. The subiculum: the heart of the extended hippocampal system. _Prog. Brain Res._ **219** , 65–82 (2015). 

160. Prasad, J. A. & Chudasama, Y. Viral tracing identifies parallel disynaptic pathways to the hippocampus. _J. Neurosci._ **33** , 8494–8503 (2013). 

161. McKenna, J. T. & Vertes, R. P. Afferent projections to nucleus reuniens of the thalamus. _J. Comp. Neurol._ **480** , 115–142 (2004). 

162. Vertes, R. P., Hoover, W. B., Szigeti-Buck, K. & Leranth, C. Nucleus reuniens of the midline thalamus: link between the medial prefrontal cortex and the hippocampus. _Brain Res. Bull._ **71** , 601–609 (2007). 

163. Griffin, A. L. Role of the thalamic nucleus reuniens in mediating interactions between the hippocampus and medial prefrontal cortex during spatial working memory. _Front. Syst. Neurosci._ **9** , 29 (2015). 

164. Varela, C., Kumar, S., Yang, J. Y. & Wilson, M. A. Anatomical substrates for direct interactions between 

hippocampus, medial prefrontal cortex, and the thalamic nucleus reuniens. _Brain Struct. Funct._ **219** , 911–929 (2014). 

165. Mitchell, A. S. _et al._ Advances in understanding mechanisms of thalamic relays in cognition and behavior. _J. Neurosci._ **34** , 15340–15346 (2014). 

166. Witter, M. P. _et al._ Cortico-hippocampal communication by way of parallel parahippocampalsubicular pathways. _Hippocampus_ **10** , 398–410 (2000). 

167. Schultz, W., Dayan, P. & Montague, R. A neural substrate of prediction and reward. _Science_ **275** , 1593–1599 (1997). 

168. Jo, Y. S. & Mizumori, S. J. Y. Prefrontal regulation of neuronal activity in the ventral tegmental area. _Cereb. Cortex_ http://dx.doi.org/10.1093/cercor/bhv215 (2015). 

169. Luo, A. H., Tahsili-Fahadan, P., Wise, R. A., Lupica, C. R. & Aston-Jones, G. Linking context with reward: a functional circuit from hippocampal CA3 to ventral tegmental area. _Science_ **333** , 353–357 (2011). 

170. Fujisawa, S. & Buzsáki, G. A. 4 Hz oscillation adaptively synchronizes prefrontal, VTA, and hippocampal activities. _Neuron_ **72** , 153–165 (2011). 

171. Groenewegen, H. J., Wright, C. I. & Beijer, A. V. J. in _The Emotional Motor System_ (eds Holstege, G., Bandler, R. & Saper, C. B.) 485–512 (Elsevier, 1996). 

172. Mogenson, G. J., Jones, D. L. & Yim, C. Y. From motivation to action: Functional interface between the limbic system and the motor system. _Prog. Neurobiol._ **14** , 69–97 (1980). 

173. van der Meer, M. A. & Redish, A. D. Expectancies in decision making, reinforcement learning, and ventral striatum. _Front. Neurosci._ **4** , 6 (2010). 

174. Lavoie, A. M. & Mizumori, S. J. Y. Spatial-, movementand reward-sensitive discharge by medial ventral striatum neurons in rats. _Brain Res._ **638** , 157–168 (1994). 

175. van der Meer, M. A & Redish, A. D. Covert expectation-of-reward in rat ventral striatum at decision points. _Front. Integr. Neurosci._ **3** , 1–15 (2009). 

176. Miyazaki, K., Miwazaki, K. W. & Matsumoto, G. Different representation of forthcoming reward in nucleus accumbens and medial prefrontal cortex. 

   - _Neuroreport_ **15** , 721–726 (2003). 

177. van der Meer, M. A. A. & Redish, A. D. Theta phase precession in rat ventral striatum links place and reward information. _J. Neurosci._ **31** , 2843–2854 (2011). 

178. Cooch, N. K. _et al._ Orbitofrontal lesions eliminate signalling of biological significance in cue-responsive ventral striatal neurons. _Nat. Commun._ **6** , 7195 (2015). 

## **Acknowledgements** 

The authors thank members of the Schoenbaum laboratory for helpful discussions on the topics addressed here and for feedback on earlier versions of this manuscript. This work was supported by funding from the US National Institute on Drug Abuse at the Intramural Research Program. The opinions expressed in this article are the authors’ own and do not reflect the view of the US National Institutes of Health, the US Department of Health and Human Services or the US government. 

## **Competing interests statement** 

The authors declare no competing interests. 

NATURE REVIEWS[|] **NEUROSCIENCE** 

VOLUME 17[|] AUGUST 2016[|] **523** 

