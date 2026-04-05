REVIEW published: 20 March 2015 doi: 10.3389/fnhum.2015.00125 

**==> picture [74 x 32] intentionally omitted <==**

# Solving the detour problem in navigation: a model of prefrontal and hippocampal interactions 

_Hugo J. Spiers[1] * and Sam J. Gilbert[2]_ 

_1 Department of Experimental Psychology, UCL Institute of Behavioural Neuroscience, Division of Psychology and Language Sciences, University College London, London, UK,[2] UCL Institute of Cognitive Neuroscience, Division of Psychology and Language Sciences, University College London, London, UK_ 

_Edited by: Arne Ekstrom, University of California, Davis, USA_ 

_Reviewed by: Giuseppe Iaria, University of Calgary, Canada Lindsay Katherine Vass, University of California, Davis, USA_ 

_*Correspondence: Hugo J. Spiers, Department of Experimental Psychology, UCL Institute of Behavioural Neuroscience, Division of Psychology and Language Sciences, University College London, 26 Bedford Way, London, WC1H 0AP, UK h.spiers@ucl.ac.uk_ 

_Received: 23 December 2014 Accepted: 22 February 2015 Published: 20 March 2015_ 

_Citation:_ 

_Spiers HJ and Gilbert SJ (2015) Solving the detour problem in navigation: a model of prefrontal and hippocampal interactions. Front. Hum. Neurosci. 9:125. doi: 10.3389/fnhum.2015.00125_ 

Adapting behavior to accommodate changes in the environment is an important function of the nervous system. A universal problem for motile animals is the discovery that a learned route is blocked and a detour is required. Given the substantial neuroscience research on spatial navigation and decision-making it is surprising that so little is known about how the brain solves the detour problem. Here we review the limited number of relevant functional neuroimaging, single unit recording and lesion studies. We find that while the prefrontal cortex (PFC) consistently responds to detours, the hippocampus does not. Recent evidence suggests the hippocampus tracks information about the future path distance to the goal. Based on this evidence we postulate a conceptual model in which: Lateral PFC provides a prediction error signal about the change in the path, frontopolar and superior PFC support the re-formulation of the route plan as a novel subgoal and the hippocampus simulates the new path. More data will be required to validate this model and understand (1) how the system processes the different options; and (2) deals with situations where a new path becomes available (i.e., shortcuts). 

Keywords: prediction error, hippocampus, planning, reinforcement learning, goals, virtual reality, place cells, artificial intelligence 

## Introduction 

## The Detour Problem and Background on Neural Systems for Navigation 

Survival depends on being able to adapt behavior in response to changes in the world. One of the most common and problematic alterations to an environment is the discovery that the current path is blocked and a new path must be found. All motile animals must be able to adjust their movements to reach food and safety. Those animals with a sophisticated nervous system have evolved the capacity to learn a long-term internal representation of the environment. Such representations contain knowledge of the possible rewards associated with different path choices. While many studies have explored how neural systems support complex navigation or decision-making, surprisingly little is known about the brain regions that support adjusting a route when a forced detour is required. 

Tolman (1948) provided some of the earliest behavioral studies where rats encountered a blocked path and were required find alternative routes. He found that rats with prior experience in the maze made impressively rapid adjustments in their path to the goal (Tolman and Honzik, 1930). From this, and other evidence, he argued that the rats had developed a flexible internal representation of the spatial relationships within the environment; 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

1 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

a representation he termed a ‘‘cognitive map’’ (Tolman, 1948). Since this initial research a number of studies have documented the capacity of rodents and other animals to adapt their path to a goal in response to changes in the environment or barriers (Poucet et al., 1983; Chapuis, 1987; Chapuis et al., 1987; Jovalekic et al., 2011). 

While the behavioral evidence for a cognitive map has been disputed (Bennett, 1996), the neural evidence has been compelling (O’Keefe and Nadel, 1978; Burgess, 2008; Spiers, 2012). Place cells, head-direction cells, grid cells and boundary cells (and their conjunctions) in hippocampal-parahippocampal regions provide evidence of an allocentric long-term spatial memory system (O’Keefe and Dostrovsky, 1971; Taube et al., 1990; Hafting et al., 2005; Sargolini et al., 2006; Lever et al., 2009). This system is capable of flexibly representing the geometric structure of the environment and maintaining it in long-term memory (Lever et al., 2002). Consistent with this, lesions to hippocampal and parahippocampal regions result in striking spatial deficits (e.g., Morris et al., 1982; Steffenach et al., 2005; Winocur et al., 2010). 

Human neuroimaging and neuropsychological studies employing real or virtual reality (VR) environments have provided convergent evidence that hippocampal-parahippocampal regions are engaged by navigation requiring an internal representation of the environment (Bohbot et al., 1998; Spiers et al., 2001a; Burgess, 2008; Spiers and Barry, 2015). This work has highlighted the importance of a network of brain regions for navigation that encompass not only hippocampalparahippocampal structures but also retrosplenial cortex, posterior parietal cortex, cerebellum, prefrontal cortex (PFC) and striatum (see e.g., Spiers and Maguire, 2007a; Chadwick and Spiers, 2014; Ekstrom et al., 2014; Rondi-Reig et al., 2014; Spiers and Barry, 2015). These brain circuits appear to be central for navigation, but also to serve long-term memory for non-spatial information (see e.g., Moscovitch et al., 2005; Spiers, 2012). However, despite this substantial research with a wide variety of methods, few studies have explored one of the hallmarks of flexible navigation---the ability to take optimal detours when the shortest path is blocked. 

## Theoretical Perspectives 

## Model-Free and Model-Based Navigation Control Systems 

In order for an animal to change its behavior in response to an obstructed path, it must have the capacity to: (a) detect the change to the environment; (b) inhibit the current action plan; and (c) select the next most appropriate course of action. In detecting the change it is also efficient for the animal to update its knowledge of the possible paths available for future journeys. The selection of the most appropriate course of action can rely on a range of information. If the goal happens to be visible along another path, a simple Pavlovian approach response would suffice to reach the goal (van der Meer et al., 2012). If, however, the goal is not visible but the environment or relationship to the goal is 

known, other mechanisms can be used to select the path. This may involve the generation of a new subgoal, which counterintuitively, might require an initial movement _away_ from the ultimate goal. 

In formulating their theory of the hippocampus as a cognitive map, O’Keefe and Nadel (1978) argued that it was the capacity for flexible place-based (‘‘locale’’) navigation that distinguished the hippocampus from cue-guidance (‘‘taxon’’) based systems. Since this initial perspective a number of researchers have developed the idea of navigational guidance drawing on concepts in the reinforcement-learning framework (Sutton and Barto, 1998). A hippocampal navigation system that uses a representation of the paths in the environment has been conceptualized as providing ‘‘model-based’’ representation for a controller to guide navigation (Hasselmo, 2005; Lengyel and Dayan, 2007; Gustafson and Daw, 2011; Martinet et al., 2011; Simon and Daw, 2011; Hirel et al., 2013; Penny et al., 2013). This model-based system would allow for a ‘‘tree-search’’ of the possible paths to the goal. This would allow the animal to select the shortest most efficient path. This system contrasts with a cache-based habit (‘‘modelfree’’) system capable of guiding navigation based on learned associations between actions and stimuli. This system is thought to involve the striatum (Gläscher et al., 2010; van der Meer and Redish, 2011) and is less computationally demanding because no tree-search or planning is required. Conversely model-free controllers of behavior suffer from being less flexible and more rigid in nature (Johnson et al., 2007; van der Meer et al., 2012). In addition it is possible that hippocampal regions may also determine the route by episodic retrieval of recent one-shot experiences, obviating the need for an elaborative tree-search and specifying the full route to the goal (Lengyel and Dayan, 2007). 

In reinforcement learning theory (Sutton and Barto, 1998), learning systems make predictions about the future outcome of certain actions, such as taking one path over another. When these predictions deviate from the sensory information from the environment, such as when a path is blocked, the systems signal a prediction error that leads to updating in the representation of rewarded actions (Sutton and Barto, 1998). Prediction errors may arise due a variety of changes to the sensory stimuli, but not all of these will affect the current path of the animal to its goal. For example, a known bridge might be encountered which has changed its color, but the path across it remains the same, or the bridge may have be broken making the current planned path void. In the latter case the animal must find an alternative route, a detour, to the goal and update the reward associated with the action of taking a new path. 

## A Homing Signal: Vector-Based Navigation 

In contrast to reinforcement learning theory approaches to path selection, another source of information has been argued to guide navigation---a goal vector that combines the direction and Euclidean distance to the goal (Burgess and O’Keefe, 1996; Kubie and Fenton, 2009, 2012). In vector navigation the animal retrieves and monitors a vector between their location and the goal location (Kubie and Fenton, 2009, 2012). When returning to a recently vacated goal, a vector can be determined by 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

2 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

computing self-motion information about distance traveled and rotations made. This is referred to as ‘‘path integration’’ or ‘‘dead reckoning’’ (see Etienne and Jeffery, 2004) and may (Worsley et al., 2001; Wolbers et al., 2007), or may not (Shrager et al., 2008; Kim et al., 2013), involve hippocampal-parahippocampal structures, perhaps depending on the distance navigated (Arnold et al., 2014). Such a homing system may also be used to guide navigation to locations retrieved from long-term memory (Kubie and Fenton, 2009, 2012). Recent fMRI evidence indicates that the entorhinal/subicular region encodes both the distance along vector to the goal (Spiers and Maguire, 2007b; Howard et al., 2014) and the direction to the goal relative to the environment’s axis (Chadwick et al., 2015). Such information about the direction to the goal would potentially be useful in determining the next most optimal route towards the goal (Kubie and Fenton, 2009, 2012). Neuroimaging data suggests an entorhinal Euclidean distance signal is dissociable from a hippocampal simulation of future paths (Howard et al., 2014; Spiers and Barry, 2015). 

## Background on Prefrontal Cortex 

## Caveats 

A small number of human neuroimaging and rodent single unit studies have reported on how brain regions respond to forced detours. In the next section we discuss these, focusing on the PFC and the hippocampus. We note that some evidence suggests the posterior parietal cortex also plays an important role in flexibly responding to detours and route planning (Nitz, 2006, 2014; Spiers and Maguire, 2006; Rauchs et al., 2008; Whitlock et al., 2008; Calton and Taube, 2009; Viard et al., 2011; Howard et al., 2014) and spatial novelty detection (Howard et al., 2013). However, we do not discuss the role of the parietal cortex here because of the lack of single unit, lesion and neuropsychological evidence, and also because posterior parietal lobe responses have been less consistent in relevant neuroimaging studies (e.g., Maguire et al., 1998; Iaria et al., 2008). Future research will be important to address this limitation and provide sufficient data for a formal meta-analysis of neuroimaging studies. 

## A Brief Primer on Prefrontal Function 

The human frontal lobes have long been recognized to play an important role in adaptive, flexible behavior, and ‘‘executive functions’’ (e.g., Penfield and Evans, 1935; Luria, 1966; for reviews see Miller and Cohen, 2001; Gilbert and Burgess, 2008; Duncan, 2010; Shallice and Cooper, 2011; Passingham and Wise, 2012). For example, lesions to this region have been associated with impairments in inhibiting prepotent responses (Aron et al., 2003), switching flexibly from one behavior to another (Milner, 1963), goal-directed planning (Shallice, 1982), and strategy application (Shallice and Burgess, 1991). PFC is thought to support these abilities via modulatory interactions with posterior cortical regions and subcortical structures such as the basal ganglia and hippocampus (Miller and Cohen, 2001; Simons and Spiers, 2003; Preston and Eichenbaum, 2013). 

One major research question has been whether the high-level control processes supported by the PFC can be fractionated, and if so to what extent these processes can be mapped onto distinct anatomical subdivisions. Evidence from functional neuroimaging has suggested that diverse cognitive demands can yield similar patterns of signal change in regions such as the dorsolateral PFC and anterior cingulate (Duncan and Owen, 2000; Duncan, 2010). However, other regions such as the anterior PFC appear to be recruited in a more circumscribed set of situations such as those involving multitasking (Roca et al., 2011). Furthermore, anterior PFC is itself a functionally heterogeneous region (Gilbert et al., 2006, 2010). Thus, we will consider below whether the processes involved in dealing with detours can be linked with specific regions of PFC, and to what extent these prefrontal regions may be considered to play related roles across spatial and non-spatial tasks. 

## Neuroimaging Studies of Forced Detours during Navigation: A Prefrontal Affair 

## Comparing Navigation Periods with and without Detours 

While numerous human neuroimaging studies have explored the brain regions involved in spatial navigation, only nine studies have examined the response to forced detours. These studies have all reported increased PFC activity when taking detours was compared to a control condition (see **Table 1** ; **Figure 1** ). This is consistent with the prediction that the PFC would be important for supporting flexible behavior in response to changing environmental contingencies and generating subgoals (e.g., Shallice and Burgess, 1991; Miller and Cohen, 2001; Spiers, 2008; Kim et al., 2011; Ullsperger et al., 2014). Based on theoretical considerations one might predict that the hippocampus would be more active when detours are required. This is because detours should be more demanding on memory retrieval and require some new learning. In contrast to this prediction, none of the nine studies that have explored detours found more hippocampal activity in response to detours. Moreover, two studies showed less activity in response to detours (Xu et al., 2010; Viard et al., 2011). We return to why this may be the case after discussing the pattern of responses in the PFC and the experimental design used in each study. 

The first neuroimaging study to explore the impact of forced detours recorded cerebral blood flow with positron emission tomography (PET) while subjects navigated a VR town learned just prior to scanning (Maguire et al., 1998). Three experimental tasks were examined with a block design. The tasks were: following arrows to a target destination (control condition), navigating the environment learned prior to testing (navigation condition), and navigating the environment taking detours caused by added barriers (detour condition). While the hippocampus was more active during the navigation condition compared to following arrows, it was not more active when the barriers were present. By contrast, prefrontal activity was not observed when navigation was compared to following arrows, but two regions of the PFC, frontal pole and middle frontal gyrus, were more active when subjects navigated the town with 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

3 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

TABLE 1 | Prefrontal cortex activations in studies examining detours in spatial navigation tasks. 

|Authors, year|Task|PFC Areas Active in Detour Condition|
|---|---|---|
|Maguire et al. (1998)|Navigate VR town learned 40--60 min prior to scanning.|L frontopolar PFC, L ventrolateral PFC|
||Analysis: Detour epochs_>_non-detour epochs.||
|Rosenbaum et al. (2004, 2007)|Plan a route between two familiar real-world landmarks.|L superior frontal gyrus (BA6), R middle frontal gyrus (BA6)|
||Analysis: Comparison conditions, proximity judgments and||
||route sequencing.||
|Spiers and Maguire (2006)|Navigate in VR simulation of familiar city. Analysis: (1) Detection|(1) Detecting unexpected events: Bilateral lateral PFC, (2)|
||of changes in the environment, (2) Re-planning. Both were|Re-planning: Bilateral frontopolar PFC, R lateral PFC|
||compared to baseline navigation periods.||
|Iaria et al. (2008)|Navigate VR paths with fences, which could change locations.|Right lateral PFC (BA 45 47/12)|
||Analysis: Detour events_>_non-detour events.||
|Rauchs et al. (2008)|Navigate VR town learned 40--60 min prior to scanning.|L inferior frontal operculum Left superior frontal gyrus|
||Analysis: Detour epochs_>_non-detour epochs.||
|Xu et al. (2010)|Navigate VR museum learned 40--60 min prior to scanning.|R middle frontal gyrus, L medial superior frontal gyrus|
||Analysis: Detour epochs_>_non-detour epochs.||
|Viard et al. (2011)|Spatial decision making about which of two paths to take to|L frontopolar PFC (BA10), Bilateral medial PFC (BA6), R|
||reach a goal. Analysis: Detours events_>_non-detour events.|ventromedial PFC (BA9)|
|Simon and Daw (2011)|Navigate a grid-maze, with a changing one-way system,|Model-based planning representations of value: Lateral|
||to reach rewarded locations. Behavior analyzed with a|PFC|
||reinforcement learning model inversion to predict parameters||
||associated with value coding.||
|Howard et al. (2014)|Navigate a city region learned days prior to scanning. Analysis:|(1) Detour events_>_non-detour events: Bilateral frontopolar|
||(1) Detour events _>_ non-detour events, (2) Detour events _>_|PFC, Bilateral lateral PFC. L superior frontal gyrus (2) Detour|
||Detours events in non-navigation control task. See Figure 3,|events _>_ detour control events Bilateral frontopolar PFC,|
||for additional parametric analysis.|Bilateral lateral PFC. Bilateral superior frontal gyrus|



_VR = Virtual reality. BA = Brodmann area. L = Left, R = Right. All used fMRI except Maguire et al. (1998), which used PET._ 

barriers than without barriers ( **Figure 1A** ; **Table 1** ). This has been considered as evidence that while the hippocampus is a core region for navigation, its computations are not more needed when alternative routes need to be taken (Maguire et al., 1998). Rather the PFC regions are key in supporting the inhibition of prior planned routes and the forward planning of future decisions (Maguire et al., 1998; Spiers and Maguire, 2006, 2007a). 

Since the study by Maguire et al. (1998) two other studies using a similar design with VR and fMRI have reported similar results (Rauchs et al., 2008; Xu et al., 2010). Both studies found PFC activity during the detours condition compared to the no-detours condition ( **Figure 1** ). Again, the hippocampus was not more active in the barriers condition compared to the no-barriers conditions. While Rauchs et al. (2008) reported a more widespread pattern of active brain regions, including superior frontal regions ( **Figure 1J** ), Xu et al. (2010) found a smaller subset more active in the barriers condition ( **Figure 1B** ). This difference may have related to differences in statistical thresholding and power, but both studies also reported some increased posterior parietal lobe (angular gyrus) activity in the detour condition. 

## Event-Related Analysis of Detours: Consideration of the Prediction Error 

A pitfall with the block designs, which compare activity during epochs with and without detours, is that the activity is not specific to the event of discovering a detour is needed. Instead it may relate to expectation prior to the detour and/or the experience in the period after taking the detour along a novel route. To determine how brain regions react to forced detours several 

studies have employed an event-related analysis. Spiers and Maguire (2006) recorded brain activity from London licensed taxi drivers as they navigated through a highly detailed virtual simulation of London (UK). Using a retrospective verbal report and a video replay it was possible to determine when the taxi drivers encountered unexpected changes to the environment (expectation violations) and events where they decided to replan their route. Re-planning and expectation violation events were not highly correlated since taxi drivers did not always report re-planning in the same moment they discovered the change to the environment (see Spiers and Maguire, 2008). Re-planning the route evoked more activity in frontopolar PFC than matched events when the taxi drivers reported simply traveling along ( **Figure 1C** ). Re-planning also elicited increased activity in a more posterior right lateral PFC region ( **Figure 1C** ). A similar right lateral region, extending more dorsally, was also active when subjects reported detecting unexpected changes to the environment ( **Figure 1H** ). This suggests it is possible that the frontopolar PFC regions may relate to re-planning paths during epochs involving forced detours, while a predominately right lateral region of PFC may also be specifically involved in the event of detecting the deviation from what was expected (Spiers and Maguire, 2006). Such a result is consistent with fMRI research using a range of paradigms that find lateral PFC regions are active when detecting occurrences of stimuli that deviate from expectations, particularly when those deviations have behavioral relevance (Fletcher et al., 2001; Corlett et al., 2004; Gläscher et al., 2010). This perspective is also supported by evidence that damage to lateral PFC disrupts the detection of novelty (e.g., Løvstad et al., 2012). 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

4 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

**==> picture [369 x 389] intentionally omitted <==**

FIGURE 1 | Statistical parametric maps of brain imaging data in studies involving detours in navigation. (A--E) frontopolar prefrontal cortex (PFC) activations. L = left. (B) (Xu et al., 2010): Areas in yellow indicate regions activated by detours more than non-detours. Areas in red indicate navigation more than line following. The red circle indicates a frontopolar region relatively selective to the detour condition. (F--I) Lateral prefrontal regions more active in 

a detour condition than a no-detour condition, or responsive to value prediction (Simon and Daw, 2011). (J--L) Superior frontal gyrus active more in a detour than control conditions. Images adapted from the articles cited under the images with permission. Image in (J) shows a coronal section of the canonical T1 image from SPM8 with a white marker indicating the location of the peak coordinate in the left frontal gyrus activation reported by Rauchs et al. (2008). 

An important consideration when exploring the neural responses to forced detours is that not all changes in the environment require a detour. As noted earlier, if a familiar bridge is discovered to be painted a new color this would be surprising and generate sensory prediction errors, but it would not affect the prediction about what path will be accessible to the goal. To separate the neural responses to changes that require a new route from those that do not Iaria et al. (2008) scanned subjects whilst they navigated a virtual route round fences. On some journeys the fences changed position requiring a detour, on other journeys they changed to a new position that did not affect the current route to the goal. While detection of perceptual changes to the layout of the fences resulted in more posterior cortical responses 

(e.g., temporo-parietal junction), changes that required a change in the path to the goal resulted in right lateral PFC response ( **Figure 1F** ). This PFC region overlaps with the region showing increased activity to both re-planning ( **Figure 1C** ) and expectation violation ( **Figure 1H** ), providing further evidence that the lateral PFC is a region important for detecting prediction errors with behavioral relevance to the current route plan. 

## Neural Responses when Detours are Expected 

In the neuroimaging studies considered so far, the detours were surprising events, detected in periods of continuous navigation of the environment. Thus, it is possible that the posterior lateral PFC response may be in part due to the detection of change 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

5 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

during on-going behavior. In support of this it is notable that in two studies no increased responses in lateral PFC were observed when subjects were expecting the detours on all, or half, of the trials and purely focused on the event of planning an alternate route (Rosenbaum et al., 2004, 2007; Viard et al., 2011). Rosenbaum et al. (2004, 2007) had subjects view photographs of pairs of landmarks in a familiar city (Toronto) and imagine navigating between them in the context that the main road linking the locations was blocked. Subjects also performed a range of other tasks, such as making proximity judgments about the landmarks with reference to a third landmark. Activity that distinguished the blocked-route tasks from the other spatial tasks was located in the superior PFC ( **Figure 1K** ), again consistent with the notion that PFC is particularly engaged by flexible behavior. However, unlike other studies considered in this review, the task investigated by Rosenbaum et al. (2004, 2007) did not involve inhibiting a previously established plan and developing a new plan, seeing as participants were merely instructed to find a route between two points having previously been told that an obvious route was not available. Thus, the superior PFC activation may have reflected a conflict effect between alternative routes under consideration, akin to conflict effects reported in non-spatial decision-making tasks that have reported activity in similar regions (BA6; Wendelken et al., 2009). 

Further insights into prefrontal response to detours were provided by a task used by Viard et al. (2011) in which subjects made decisions on each trial about the path they would take to reach a man on the other side of a room. Half of the trials involved the need for a detour round a barrier, which was not pre-warned before the beginning of the trial. Thus, while detours were not surprising (occurring on 50% of trials), they could not be predicted on a trial-by-trial basis and therefore may have necessitated re-planning from the most direct route when they occurred. This may explain the frontopolar activity observed by Viard et al. (2011); **Figure 1D** , but not Rosenbaum et al. (2004, 2007). 

## Model-Based Analysis of fMRI Data 

As we discussed in the section on Model-free and model-based navigation control systems, when the goal to be navigated to cannot be seen, route choice may rely either on a retrieved map of the environment (a ‘‘model-based’’ representation) or on a learned association between the expected value and the action of choosing a particular path (a ‘‘model-free’’ representation)(van der Meer et al., 2012). In the studies discussed so far it was not possible to dissociate these possibilities. To address this Simon and Daw (2011) scanned subjects while they navigated a learned environment consisting of four rewarded goals randomly located in a virtual world composed of Manhattan-like 4 × 4 grid of 16 locations. Grid locations were connected by one-way doors. As subjects moved between locations each door had a 1/24 chance of reversing its direction. Thus, previously-available routes between locations might suddenly become impassible, requiring a detour along a new route. Simon and Daw (2011) fit the behavioral choices of the subjects to reinforcement learning models to estimate the changing representations of value associated with 

different choices made. For example, for a given participant, the choice to travel along a path from location one to two might be estimated to have a high value for the first 10 journeys because it was frequently chosen and provided a quick route to obtain reward. However, in the trials after one of the one-way doors on that route changed direction, the value of the choosing to travel along that path would diminish subsequently. In this scenario prediction-errors and value were correlated. One estimated set of values was determined assuming a model-free system; the other set was estimated assuming a model-based system. The authors found evidence that the subjects’ behavior was better captured by the model-based fit and that activity in a range of striatal regions tracked value as would be predicted from many prior fMRI studies on reinforcement learning (see O’Doherty et al., 2007). Additionally, lateral PFC regions extending into the frontal pole were correlated with the value of chosen paths derived from a model-based system ( **Figure 1I** ). This provides more precise evidence that lateral PFC regions represent the changing value of particular actions in response to alterations in the environment. 

## Forced Detours in the Absence of Visual Cues 

The method used by Simon and Daw (2011) provides a helpful approach to quantifying the impact of changes of the environment on behavior and internal representations. However, with the design used it was not simple to quantify the impact the detour had on the possible path to the goal, and like all the previous studies discussed, the change was correlated with a visual change in the structure of the environment (door entry signs changed). Furthermore, while Iaria et al. (2008) demonstrated that lateral PFC responses can be distinguished between perceptual changes that evoke a change in the route or not, they were still visually driven and the period after the detour was encountered differed from the non-detour events due to the change in path taken. In a recent fMRI study, Howard et al. (2014) examined: (a) the impact of forced detours on the representation of the distance to the goal; and (b) forced detours where no visual information signaled the need for a detour. Subjects learned, by studying maps and a two-hour walking tour, the layout of London’s (UK) Soho region. The next day subjects were scanned with fMRI while they watched a filmbased first-person-view simulation of routes through the streets. During half of the routes the subject had to navigate to goal locations; for the other half the subjects just watched the routes and followed instructions about which path to select. In the navigation routes, just prior to each junction, subjects had to make a choice about the optimal path to the goal. The routes were fixed and subjects were told that most of the time the route would take the optimal path, but occasionally the route would take a forced detour. This meant that detours could only be distinguished from non-detours by the mismatch between choice prior to the turn and the outcome at the turn. Increased activity in frontopolar ( **Figure 1E** ), lateral ( **Figure 1G** ) and superior PFC ( **Figure 1L** ) regions reported in previous studies was found when detours were compared to non-detours. Similar regions were also found to be more active when detours in the navigation task were compared with equivalent events in the control routes (e.g., 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

6 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

where a subject was instructed to select to turn left, but the route turned right). This supports the view that the PFC responses are not driven by visual changes in the environment but rather by the need to adapt the route plan. Notably, the study by Howard et al. had subjects navigate along paths only experienced once or twice before, and studied from maps, emphasizing the use of the model-based planning system. Thus, it seems likely that these responses are specific to the use of a model-based representation of the environment. 

## Summary of Insights from Neuroimaging Studies 

In summary, it is apparent that all neuroimaging studies exploring brain activity in response to forced detours reported increased PFC activity ( **Table 1** ). Frontopolar cortex appears to be region most consistently activated by the need to take detours compared to not having to take detours. More posterior lateral PFC regions are notably activated in response to detecting surprising events that necessitate detour planning. This response is consistent with the lateral PFC representing a model-based prediction error about the expectation that current planned route will succeed. Such a prediction-error signal could trigger inhibition of the ongoing navigation behavior (Chatham et al., 2012), leading to flexible route re-planning. Notably, we do not see reliable responses in the dorsomedial PFC/anterior cingulate or orbital frontal PFC regions. Other evidence indicates that these regions might be expected to play a role in aspects of navigation, such as coding the reward of reaching the goal (Feierstein et al., 2006; Spiers and Maguire, 2007b; Howard et al., 2014), ‘‘regret’’ in not obtaining reward (Steiner and Redish, 2014), dealing with overlapping routes (Brown et al., 2010; Brown and Stern, 2014) and strategy applications (Dahmani and Bohbot, 2015). Such processes may not be a key component in all detour taking and thus explain why such regions were less consistently responsive, or not responsive, to forced detours. 

## How do Prefrontal Responses in Navigation Paradigms Relate to Responses in other Cognitive Tasks? 

It is notable that a majority of studies investigating route re-planning in response to detours have reported prominent activation in frontopolar PFC (BA 10; **Figures 1A--E** ). This is anterior to the lateral PFC regions most commonly activated by diverse cognitive demands (Duncan, 2013), suggesting that the processes involved in dealing with detours show some selectivity for this anterior region. Such a result would be consistent with neuroimaging investigations of non-spatial tasks, which have suggested that frontopolar regions are involved in ‘‘goalsubgoal integration’’ (Braver and Bongiolatti, 2002) or cognitive ‘‘branching’’ (Koechlin et al., 1999), i.e., the process of pursuing a subtask or subgoal whilst holding an overarching goal in mind (see also Ramnani and Owen, 2004). Conceptually, this fits well with a model whereby detours force participants to navigate towards a subgoal destination, whilst holding in mind an ultimate destination as an overall goal. Thus, both spatial navigation and non-spatial planning tasks implicate frontopolar PFC in 

subgoal processing. More broadly, dealing with forced detours would be a good example of a situation requiring attention to be balanced between internally-represented information (i.e., navigation goals and subgoals) and ongoing perceptual input as one moves through the environment. Frontopolar PFC has been proposed to play a key role in just such situations (Gilbert et al., 2005; Burgess et al., 2007). 

A further point of consistency might be with Goel and Grafman’s (1995) neuropsychological study of the Tower of Hanoi planning task. Goel and Grafman argue that their frontal lobe patients’ difficulties with this task stem especially from the process of resolving a goal-subgoal conflict, particularly when pursuing a subgoal necessitates an initial move away from the ultimate goal state. Notably, of the 11 patients studied by Goel and Grafman for whom lesion localization in terms of Brodmann Areas (BA) was possible, nine had damage including (albeit not limited to) frontopolar region BA 10. 

## Prefrontal Contributions from Single Unit and Lesion Studies 

## Single Unit Recording and Lesion Studies in Rodents: A Short Tale 

It would be highly beneficial if single unit recording or lesion studies in rodents and primates could help provide convergent evidence to support neuroimaging data. Alas, to our knowledge prefrontal responses to detours have not been characterized in rodents or non-human primates. The imperfect homology between primate and rodent PFC precludes making straightforward comparisons across species (Simons and Spiers, 2003). In rodents research on PFC contributions to navigation have focused on the prelimbic/infralimbic regions of the medial PFC, which receive mono-synaptic afferents from the hippocampus (Ferino et al., 1987). Neurons in medial PFC show activity related to the goal location (Hok et al., 2005) and medial PFC lesions impair switching from navigating from one learned goal to a new goal location (de Bruin et al., 1994; Granon and Poucet, 1995; Delatour and Gisquet-Verrier, 2000; Boulougouris et al., 2007) and switching between response and place strategies (Ragozzino et al., 1999a,b). Thus, it seems plausible that medial PFC damage would impair the inhibition of the current route and switching to a new route required in forced detour taking. 

## Neuropscyhological Evidence from Humans: An Even Shorter Tale 

In humans, anterior PFC lesions have been shown to result in impaired planning of routes to collect items from a set of different shops (Shallice and Burgess, 1991). Such deficits may relate more generally to poor application of strategy than to accommodating detours during navigation (Shallice and Burgess, 1991; Szczepanski and Knight, 2014). In relation to large-scale navigation, a lesion encompassing much of ventral medial PFC extending to frontopolar regions was found to result in an impaired ability to maintain the current spatial goal (Ciaramelli, 2008; Spiers, 2008). The patient often arrived at non-intended locations, showing a diminished ability to flexibly navigate across 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

7 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

the town they were familiar with. Unfortunately there have been no reports of patients with frontal lobe damage being tested on their capacity to take optimal detours to a goal. 

## A Role for the Hippocampus? 

## Evidence from Neuropsychological Studies 

Given the dominant theory that the hippocampus is essential for flexible navigation (O’Keefe and Nadel, 1978), one might expect it to play a prominent role in processing information to support detour taking. As noted above, in all nine neuroimaging studies reviewed none showed more activity when detours were required, compared to when they were not. Damage to the hippocampus in humans impairs the ability to learn and navigate a new environment (e.g., Spiers et al., 2001b), a problem noted in the case of the famous amnesic HM (Scoville and Milner, 1957). This makes testing patients on detour taking in novel environments not particularly informative. More relevant are tests of detour taking in environments pre-morbidly learned. Four studies have examined the ability of patients with hippocampal damage to navigate remotely learned environments and take detours (see for review Spiers and Maguire, 2007a). Patients EP (Teng and Squire, 1999), and KC (Rosenbaum et al., 2000), both with extensive medial temporal lobe damage, were tested on their ability to mentally describe routes between locations in their hometown with the requirement that they take detours to avoid a major road. Both patients, despite being densely amnesic, were able to perform this task as well as matched healthy controls, suggesting the hippocampus is not specifically needed for mentally planning routes in welllearned environments. However, more recently, different pattern of results was provided by a patient (HC) with congenital damage to their hippocampal anatomy (hippocampus, fornix and mammillary bodies). Patient HC was tested on her ability to provide route descriptions accommodating detours in a familiar environment (Rosenbaum et al., 2015). While she was able to describe routes that reached the destination, these routes were significantly longer than those described by the matched control subjects and her sketch maps suggested she had access to only schematic information about the environment. This suggests that gradual acquisition of the structure of the environment can occur in the context of congenital hippocampal damage, but that the hippocampus is needed to form detailed knowledge structures needed for accurate navigation and detour taking. 

While the studies of patients HC, EP and KC have provided insights in the ability of hippocampal patients to perform mental navigation, they did not assess whether when the patient was able to actively navigate the environment. It is possible that cues in the environment might aid navigation, allowing patients with hippocampal damage to navigate remotely learned environments accurately. In order to test _in situ_ navigation of a remotely learned environment Maguire et al. (2006) tested a retired London taxi driver with extensive bilateral hippocampal lesions (patient TT) on his ability to navigate the virtual simulation of London used by Spiers and Maguire (2006). Patient TT showed a mixture of impaired and unimpaired navigation. Some routes were 

navigated well, others very inaccurately. A variety of 29 different factors were quantified to determine whether any of them explained the pattern of impairments. One of these salient factors was the need to take detours in the environment. Routes that required detours were not more impaired than routes that did, rather it was the requirement to navigate along the minor roads of London that was the most significantly powerful predictor of performance. Thus, the human hippocampus does not appear to be specifically required to take detours in environments well learned prior to the lesion, but when the route requires a less often traveled path it may be needed to aid navigation. 

## Hippocampal Contributions based on Single Unit Recording and Lesion Studies in Rodents 

One might imagine, given the extensive research on spatial navigation in rodents, that we would know more about detour processing in the hippocampus from single unit recording or lesion studies. We do not. Much of the large body of research on navigation has explored maze learning, object location learning, or goal switching (e.g., Morris et al., 1982; Packard and McGaugh, 1996; Gilbert and Kesner, 2004; Tse et al., 2007). Only one study, to our knowledge, has examined the impact of hippocampal lesions on a detour task (Winocur et al., 2010), see **Figure 2A** . The lesioned rats were impaired at making use of optimal detours to reach the goal when a barrier was placed in environment learned 2 weeks prior to lesions. While the control rats were able to readily switch to the next most optimal route, hippocampal rats were not ( **Figure 2B** ). They often made errors that persisted over many days. However, their routes were not random. Winocur et al. (2010) noted that the rats made clear purposeful movement to reach the goal and showed ‘‘no outward signs of agitation’’ (p.12). Furthermore, while the rats failed to adopt optimal detours, they were markedly better than a group of rats with hippocampal lesions first exposed to the environment after their lesions. Thus, while non-hippocampal circuits are sufficient for navigation of blocked detours in a variety of situations, damage to the hippocampus can disrupt optimal path taking when explicitly tested. This result is consistent with the recent evidence from patient HC (see Rosenbaum et al., 2015). Current theories would suggest the hippocampus is needed in order to construct detailed precise spatial representations, and the coarse schematic representations of the environment can be formed elsewhere (Moscovitch et al., 2005; Tse et al., 2007; Maguire and Mullally, 2013). Further research using a detour task that requires both fine-grained and coarse-schematic route choices may prove useful in developing a better characterization to the hippocampal contribution. 

Similar to lesion studies, single unit recording studies have rarely examined responses to obstructing the path to the goal. Alvernhe et al. examined the impact of forced detours (Alvernhe et al., 2011) and shortcuts (Alvernhe et al., 2008) on the place cell activity in CA1 and CA3 of the dorsal hippocampus. Hippocampal place cells fire action potentials when the animal occupies a specific region of space. The region of space is specific for each cell (referred to as the cell’s place field), allowing the place cells to provide a population code for the whole 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

8 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

**==> picture [373 x 368] intentionally omitted <==**

FIGURE 2 | Detour studies with rodents. (A) Maze used by Winocur et al. (2010). (B) Map of the maze with the path taken by hippocampal lesioned rat and a sham control rat. Black rectangle marks the barrier. Note the longer path taken by the hippocampal lesioned animal. (C) Maze used by Alvernhe et al. 

(2011) adapted from Tolman and Honzik (1930). P1 and P2 mark the points where barriers were inserted on different trials. (D) Place cell firing rate maps from two example cells in the study shown before (left), during (middle) and after (right) a barrier has been inserted. Images adapted with permission. 

environment. Evidence indicates that they provide a long-term memory of the environment (Lever et al., 2002). To explore shortcut taking Alvernhe et al. (2008) recorded as rats navigated an M-shaped track for reward in a learned configuration. The shortcut was introduced by having part of the maze removed. To explore detours the researchers tested rats with the paradigm of Tolman and Honzik (1930), in which they initially explore a maze with three possible paths to the goal ( **Figure 2C** ). After learning to take the shortest path, this path is blocked and the rats must switch to taking an optimal alternative path. Rats rapidly switch to choosing the second most optimal path, demonstrating some latent learning. In both experiments place cells in areas CA1 and CA3 showed some local remapping of their place fields near the region of the maze with the changed geometry, while cells far from the goal showed little change in their firing rate ( **Figure 2D** ). This is consistent with many other studies showing similar place cell responses to geometric change (O’Keefe and Burgess, 1996; Lever et al., 2002; Wills et al., 2005; 

Spiers et al., 2015), and thus is not a response specific to detour or shortcut taking. However, in the shortcut experiment CA3 cells were found to also show non-local remapping---altering their firing patterns at locations in the maze not near the change. Purely local geometric response models (Hartley et al., 2000) cannot easily account for this change. Instead it may relate to the prospective activity place cells, which change their firing rate depending on the future path of the rat (Wood et al., 2000). 

While the studies by Alvernhe et al. (2008, 2011) show how spatial maps in the hippocampus alter in response to changes in the environment that affect the path to the goal it is difficult to relate these findings to neuroimaging data ( **Table 1** ). This is because place cells are typically not examined in terms of evoked responses to events. Thus, it is not clear from the data in Alvernhe et al. (2011) how the hippocampal cells responded to the initial discovery of the barrier, and at what point the rat made a decision to change its path. This is also the case 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

9 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

**==> picture [397 x 266] intentionally omitted <==**

FIGURE 3 | Hippocampal activity correlated with the change in distance to the goal at a detour. (A) View from the film simulation of London used by Howard et al. (2014). (B) Map of the part of the region navigated. Black line shows the path taken. Red dotted line indicates the optimal future path to be taken to the goal (black dot). Blue dotted line indicates the Euclidean distance to the goal. Left map show the path to the goal before the subject discovers that the simulation has led the subject left rather than allowing them to travel straight. No detour was marked in the film simulation; rather the simulation simply did not take the path the subject had requested prior to the junction. (C) The amount of change in the path distance is plotted against time for one of the 10 

routes navigated in the experiment. (D) Middle: Right posterior hippocampal activity significantly correlated ( _p <_ 0.05 family-wise error corrected) with the change in path distance at detours is plotted on a mean structural scan, thresholded at _p <_ 0.005 uncorrected. Left: Parameter estimates from the peak voxel are plotted for three different ranges of the change in the path distance. Right: parameter estimates of the significant correlation in the navigation condition, but non-significant parameter estimates in the control routes. Note: a significantly greater response was observed in the posterior right hippocampus for navigation routes compared with control routes (see Howard et al., 2014). Images adapted with permission from Howard et al. (2014). 

for a study by Muir and Taube (2004) in which postsubiculum (dorsal presubiculum) head-direction cells were recorded during the blocked path ‘‘sunburst maze’’ task of Tolman (1948). In this task the rats learn to take a particular set path to a goal. After initial training the learned path is blocked and 8 novel path options are made available, with one of the new paths leading directly to the goal. Tolman (1948) found rats were more likely to take the novel paths oriented to the goal than paths not oriented toward the goal. Because each head-direction cell fires when the rat’s head is oriented in a preferred direction in the environment it is possible to use the variation in their firing as a proxy for how oriented the rats were. Muir and Taube (2004) found no relationship between the consistency of rat’s headdirection representations and their ability to choose optimal novel paths. 

Recent developments in large-scale recording have made it possible to decode information about the rat’s position during brief spiking events in open field environments (Pfeiffer and Foster, 2013). These spiking events can show decoding of the rats’ representation of location sweep ahead towards goal locations (Pfeiffer and Foster, 2013). This result is broadly consistent with a mechanism for future path searches using a model-based 

system (van der Meer et al., 2012). It will be important in future work to explore such activity during forced detour tasks to test whether such spiking event activity is related to future path selection. 

## fMRI Evidence for the Contribution of the 

## Hippocampus to Processing the New Path to the Goal 

Recent evidence from several fMRI studies has provided convergent evidence that the hippocampus represents the distance to the goal during navigation (Viard et al., 2011; Sherrill et al., 2013; Howard et al., 2014; for review see Spiers and Barry, 2015). Such activation patterns may relate to the forward sweeps of activity observed during travel periods (Johnson et al., 2007; Wikenheiser and Redish, 2015) or brief ensemble spiking events (Pfeiffer and Foster, 2013). More explicitly, Wikenheiser and Redish (2015) have shown that the activity prior to running to a goal is related to the distance to that goal. In the case of detours, the path distance always increases to the goal. For some detours this might be a small change in the distance for others a very large change. To understand how brain regions respond to 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

10 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

**==> picture [369 x 221] intentionally omitted <==**

FIGURE 4 | A conceptual model of prefrontal and hippocampal contributions to navigating detours. The model provides a summary of the contributions of three prefrontal cortical (PFC) regions and the hippocampus based on our review of empirical data. This model relates to navigating recently learned environments and involves the use of path-based representations for planning. Activity associated with detecting the detour in lateral PFC propagates to the hippocampal circuitry and the other PFC regions to support path-based planning. Activity arising from 

path processing in the hippocampus propagates to rostral PFC and superior PFC regions for the setting of subgoals and dealing with conflict between possible routes, respectively. Based on computational theories of PFC---hippocampal networks (e.g., Martinet et al., 2011; Hirel et al., 2013), it is predicted that activity would re-route multiple times between anterior/superior PFC regions and the hippocampal network to provide processing of alternative routes, depending on the complexity of the potential route and its options. 

the change in distance to the goal at detours, Howard et al. (2014) examined activity related to the change in the path distance to the goal (see **Figures 3A,B** ). **Figure 3B** shows an example of a change in the path needed to reach a goal for one of the detours in the experiment. By plotting the change in the path distance for each second of a route it is possible to identify when various detours occurred and observe how they changed the distance to the goal. **Figure 2C** shows an example of one of the 10 routes subjects navigated. Right posterior hippocampal activity was found to positively correlate with the amount of change in the detour during navigation routes ( **Figure 2D** ). This correlation was absent and significantly lower in the control routes (where subjects did not need to rely on memory to navigate), indicating that the response required goal-directed navigation to be elicited. Notably, no PFC region was correlated with the change in the path distance to the goal. This suggests a division between the PFC for detecting and manipulating information, and the hippocampus for representing information about the path required to reach the goal. 

When reconsidering the route to the goal it is possible that the direction to the goal might be computed. Recent evidence suggests that the entorhinal/subicular region represents the allocentric direction to the goal during path planning (Chadwick et al., 2015). Whether this region also represents the direction to the goal when detours are required is unknown. Models of vector navigation argue that such allocentric 

direction information would be important for guiding the navigator along the optimal new path (Kubie and Fenton, 2009, 2012). 

## Conclusion and a Speculative Conceptual Model 

Reviewing the limited literature we are able to provide a speculative conceptual model involving: lateral, superior and frontopolar PFC and posterior hippocampus. This model is currently specific to environments that have been learned recently. Lateral PFC is involved in detecting that an alteration in the environment will require a change in the route plan. Frontopolar PFC subsequently provides a mechanism for replanning, possibly involving the generation of subgoals. The posterior hippocampus pre-activates representations of the future path to the goal to adjudicate between possible routes and superior PFC regions deals with the conflict between options. See **Figure 4** for diagram outlining the model. 

Replication of the data that supports this division of functions between regions will be invaluable, as will new tests of the model. The current model predicts that the conflict between paths will lead to increased activity in superior PFC, but not other regions. However, it may be that rostral PFC regions also contribute to this function. If frontopolar PFC is related to constructing the new route plan, then the number of subgoals to be considered may correlate specifically with 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

11 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

responses in this region. If the hippocampus simulates the future path to the goal then the length of a new shortcut will be expected correlate with hippocampal, but not PFC activity. In addition to these manipulations, future studies teasing apart the involvement of model-based and model-free responses and investigating environments learned in the remote past will be highly beneficial. 

A crucial question is how does the PFC interact with the hippocampus during detecting the detour and planning the new route. In our current model we speculate that there is a reciprocal interaction between the hippocampus and the PFC to support this function (Simons and Spiers, 2003; Martinet et al., 2011; Hirel et al., 2013; Preston and Eichenbaum, 2013). Initially, lateral PFC activity propagates to the hippocampal circuitry, and other PFC regions to support path-based planning. Activity arising from path processing in the hippocampus is propagated to rostral PFC and superior PFC regions for the setting of subgoals and dealing with conflict between possible routes. PFC processing may give rise to further perturbation of the hippocampal network to provide more processing of potential routes, which would lead to further processing in PFC 

## References 

- Alvernhe, A., Save, E., and Poucet, B. (2011). Local remapping of place cell firing in the Tolman detour task. _Eur. J. Neurosci._ 33, 1696--1705. doi: 10.1111/j.14609568.2011.07653.x 

- Alvernhe, A., Van Cauter, T., Save, E., and Poucet, B. (2008). Different CA1 and CA3 representations of novel routes in a shortcut situation. _J. Neurosci._ 28, 7324--7333. doi: 10.1523/JNEUROSCI.1909-08.2008 

- Arnold, A. E. F., Burles, F., Bray, S., Levy, R. M., and Iaria, G. (2014). Differential neural network configuration during human path integration. _Front. Hum. Neurosci._ 8:263. doi: 10.3389/fnhum.2014.00263 

- Aron, A. R., Fletcher, P. C., Bullmore, E. T., Sahakian, B. J., and Robbins, T. W. (2003). Stop-signal inhibition disrupted by damage to right inferior frontal gyrus in humans. _Nat. Neurosci._ 6, 115--116. doi: 10.1038/nn1003 

- Bennett, A. T. (1996). Do animals have cognitive maps?. _J. Exp. Biol._ 199, 219--224. 

- Bohbot, V. D., Kalina, M., Stepankova, K., Spackova, N., Petrides, M., and Nadel, L. (1998). Spatial memory deficits in patients with lesions to the right hippocampus and to the right parahippocampal cortex. _Neuropsychologia_ 36, 1217--1238. doi: 10.1016/s0028-3932(97)00161-9 

- Boulougouris, V., Dalley, J. W., and Robbins, T. W. (2007). Effects of orbitofrontal, infralimbic and prelimbic cortical lesions on serial spatial reversal learning in the rat. _Behav. Brain Res._ 179, 219--228. doi: 10.1016/j.bbr.2007.02.005 

- Braver, T. S., and Bongiolatti, S. R. (2002). The role of frontopolar cortex in subgoal processing during working memory. _Neuroimage_ 15, 523--536. doi: 10. 1006/nimg.2001.1019 

- Brown, T. I., Ross, R. S., Keller, J. B., Hasselmo, M. E., and Stern, C. E. (2010). Which way was I going? Contextual retrieval supports the disambiguation of well learned overlapping navigational routes. _J. Neurosci._ 30, 7414--7422. doi: 10.1523/JNEUROSCI.6021-09.2010 

- Brown, T. I., and Stern, C. E. (2014). Contributions of medial temporal lobe and striatal memory systems to learning and retrieving overlapping spatial memories. _Cereb. Cortex_ 24, 1906--1922. doi: 10.1093/cercor/bht041 

- Burgess, N. (2008). Spatial cognition and the brain. _Ann. N Y Acad. Sci._ 1124, 77-97. doi: 10.1196/annals.1440.002 

- Burgess, P. W., Dumontheil, I., and Gilbert, S. J. (2007). The gateway hypothesis of rostral prefrontal cortex (area 10) function. _Trends Cogn. Sci._ 11, 290--298. doi: 10.1016/j.tics.2007.05.004 

- Burgess, N., and O’Keefe, J. (1996). Neuronal computations underlying the firing of place cells and their role in navigation. _Hippocampus_ 6, 749--762. doi: 10. 1002/(sici)1098-1063(1996)6:6 _<_ 749::aid-hipo16 _>_ 3.3.co;2-x 

and ultimately action. The extent of the interaction between PFC and hippocampus may likely depend on the complexity of the new route to be considered and how much time the individual is willing to invest in considering the options. Formulation of the computations that may be performed in interactions between PFC and hippocampus can be found in the computational models of Martinet et al. (2011) and Hirel et al. (2013). However, currently these models focus on rodent navigation and implement a single PFC region responsible for goal directed route planning. This review points at the need to consider different regions engaged and different situations in which detours may be required (e.g., when expected or not). 

## Acknowledgments 

HJS is supported by funding from the Wellcome Trust, UK and the James S. McDonnell Foundation, USA. SJG is supported by a Royal Society University Research Fellowship. We thank Fiona E. Zisch for producing the diagram in **Figure 4** and Sophie Renaudineau for helpful discussions. 

- Calton, J. L., and Taube, J. S. (2009). Where am I and how will I get there from here? A role for posterior parietal cortex in the integration of spatial information and route planning. _Neurobiol. Learn. Mem._ 91, 186--196. doi: 10. 1016/j.nlm.2008.09.015 

- Chadwick, M. J., Jolly, E. J., Amos, D. P., Hassabis, D., and Spiers, H. J. (2015). A goal direction signal in the human entorhinal/subicular region. _Curr. Biol._ 25, 87--92. doi: 10.1016/j.cub.2014.11.001 

- Chadwick, M. J., and Spiers, H. J. (2014). A local anchor for the brain’s compass. _Nat. Neurosci._ 17, 1436--1437. doi: 10.1038/nn.3841 

- Chapuis, N. (1987). Detour and shortcut abilities in several species of mammals. _Cogn. Process. Spat. Orientat. Anim. Man_ 36, 97--106. doi: 10.1007/978-94-0093531-0_7 

- Chapuis, N., Durup, M., and Thinus-Blanc, C. (1987). The role of exploratory experience in a shortcut task by golden hamsters (Mesocricetus auratus). _Anim. Learn. Behav._ 15, 174--178. doi: 10.3758/bf03204960 

- Chatham, C. H., Claus, E. D., Kim, A., Curran, T., Banich, M. T., and Munakata, Y. (2012). Cognitive control reflexts context monitoring, not motoric stopping, in response inhibition. _PLoS One_ 7:e31546. doi: 10.1371/journal.pone. 0031546 

- Ciaramelli, E. (2008). The role of ventromedial prefrontal cortex in navigation: a case of impaired wayfinding and rehabilitation. _Neuropsychologia_ 46, 2099--2105. doi: 10.1016/j.neuropsychologia.2007.11.029 

- Corlett, P. R., Aitken, M. R., Dickinson, A., Shanks, D. R., Honey, G. D., Honey, R. A., et al. (2004). Prediction error during retrospective revaluation of causal associations in humans: fMRI evidence in favor of an associative model of learning. _Neuron_ 44, 877--888. doi: 10.1016/s0896-6273(04) 00756-1 

- Dahmani, L., and Bohbot, V. D. (2015). Dissociable contributions of the prefrontal cortex to hippocampus-and caudate nucleus-dependent virtual navigation strategies. _Neurobiol. Learn. Mem._ 117, 42--50. doi: 10.1016/j.nlm.2014. 07.002 

- de Bruin, J. P., Sànchez-Santed, F., Heinsbroek, R. P., Donker, A., and Postmes, P. (1994). A behavioural analysis of rats with damage to the medial prefrontal cortex using the Morris water maze: evidence for behavioural flexibility, but not for impaired spatial navigation. _Brain Res._ 652, 323--333. doi: 10.1016/00068993(94)90243-7 

- Delatour, B., and Gisquet-Verrier, P. (2000). Functional role of rat prelimbicinfralimbic cortices in spatial memory: evidence for their involvement in attention and behavioural flexibility. _Behav. Brain Res._ 109, 113--128. doi: 10. 1016/s0166-4328(99)00168-0 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

12 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

Duncan, J. (2010). The multiple-demand (MD) system of the primate brain: mental programs for intelligent behaviour. _Trends Cogn. Sci._ 14, 172--179. doi: 10.1016/j.tics.2010.01.004 

- Duncan, J. (2013). The structure of cognition: attentional episodes in mind and brain. _Neuron_ 80, 35--50. doi: 10.1016/j.neuron.2013.09.015 

- Duncan, J., and Owen, A. M. (2000). Common regions of the human frontal lobe recruited by diverse cognitive demands. _Trends Neurosci._ 23, 475--483. doi: 10. 1016/s0166-2236(00)01633-7 

- Ekstrom, A. D., Arnold, A. E., and Iaria, G. (2014). A critical review of the allocentric spatial representation and its neural underpinnings: toward a network-based perspective. _Front. Hum. Neurosci._ 8:803. doi: 10.3389/fnhum. 2014.00803 

- Etienne, A. S., and Jeffery, K. J. (2004). Path integration in mammals. _Hippocampus_ 14, 180--192. doi: 10.1002/hipo.10173 

- Feierstein, C. E., Quirk, M. C., Uchida, N., Sosulski, D. L., and Mainen, Z. F. (2006). Representation of spatial goals in rat orbitofrontal cortex. _Neuron_ 51, 495--507. doi: 10.1016/j.neuron.2006.06.032 

- Ferino, F., Thierry, A. M., and Glowinski, J. (1987). Anatomical and electrophysiological evidence for a direct projection from Ammon’s horn to the medial prefrontal cortex in the rat. _Exp. Brain Res._ 65, 421--426. doi: 10. 1007/bf00236315 

- Fletcher, P. C., Anderson, J. M., Shanks, D. R., Honey, R., Carpenter, T. A., Donovan, T., et al. (2001). Responses of human frontal cortex to surprising events are predicted by formal associative learning theory. _Nat. Neurosci._ 4, 1043--1048. doi: 10.1038/nn733 

- Gilbert, S. J., and Burgess, P. W. (2008). Executive function. _Curr. Biol._ 18, R110--R114. doi: 10.1016/j.cub.2007.12.014 

- Gilbert, S. J., Frith, C. D., and Burgess, P. W. (2005). Involvement of rostral prefrontal cortex in selection between stimulus-oriented and stimulusindependent thought. _Eur. J. Neurosci._ 21, 1423--1431. doi: 10.1111/j.14609568.2005.03981.x 

- Gilbert, S. J., Henson, R. N. A., and Simons, J. S. (2010). The scale of functional specialization within human prefrontal cortex. _J. Neurosci._ 30, 1233--1237. doi: 10.1523/JNEUROSCI.3220-09.2010 

- Gilbert, P. E., and Kesner, R. P. (2004). Memory for objects and their locations: the role of the hippocampus in retention of object-place associations. _Neurobiol. Learn. Mem._ 81, 39--45. doi: 10.1016/s1074-7427(03)00069-8 

- Gilbert, S. J., Spengler, S., Simons, J. S., Steele, J. D., Lawrie, S. M., Frith, C. D., et al. (2006). Functional specialization within rostral prefrontal cortex (area 10): a meta-analysis. _J. Cogn. Neurosci._ 18, 932--948. doi: 10.1162/jocn.2006.18. 6.932 

- Gläscher, J., Daw, N., Dayan, P., and O’Doherty, J. P. (2010). States versus rewards: dissociable neural prediction error signals underlying model-based and modelfree reinforcement learning. _Neuron_ 66, 585--595. doi: 10.1016/j.neuron.2010. 04.016 

- Goel, V., and Grafman, J. (1995). Are the frontal lobes implicated in ‘‘planning’’ functions? Interpreting data from the Tower of Hanoi. _Neuropsychologia_ 33, 623--642. doi: 10.1016/0028-3932(95)90866-p 

- Granon, S., and Poucet, B. (1995). Medial prefrontal lesions in the rat and spatial navigation: evidence for impaired planning. _Behav. Neurosci._ 109, 474--484. doi: 10.1037//0735-7044.109.3.474 

- Gustafson, N. J., and Daw, N. D. (2011). Grid cells, place cells and geodesic generalization for spatial reinforcement learning. _PLoS Comput. Biol._ 7:e1002235. doi: 10.1371/journal.pcbi.1002235 

- Hafting, T., Fyhn, M., Molden, S., Moser, M. B., and Moser, E. I. (2005). Microstructure of a spatial map in the entorhinal cortex. _Nature_ 436, 801--806. doi: 10.1038/nature03721 

- Hartley, T., Burgess, N., Lever, C., Cacucci, F., and O’Keefe, J. (2000). Modeling place fields in terms of the cortical inputs to the hippocampus. _Hippocampus_ 10, 369--379. doi: 10.1002/1098-1063(2000)10:4 _<_ 369::aid-hipo3 _>_ 3.0. co;2-0 

- Hasselmo, M. E. (2005). A model of prefrontal cortical mechanisms for goal-directed behavior. _J. Cogn. Neurosci._ 17, 1115--1129. doi: 10. 1162/0898929054475190 

- Hirel, J., Gaussier, P., Quoy, M., Banquet, J. P., Save, E., and Poucet, B. (2013). The hippocampo-cortical loop: spatio-temporal learning and goal-oriented planning in navigation. _Neural Netw._ 43, 8--21. doi: 10.1016/j.neunet.2013. 01.023 

- Hok, V., Save, E., Lenck-Santini, P. P., and Poucet, B. (2005). Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex. _Proc. Natl. Acad. Sci. U S A_ 102, 4602--4607. doi: 10.1073/pnas.0407332102 

- Howard, L. R., Javadi, A. H., Yu, Y., Mill, R. D., Morrison, L. C., Knight, R., et al. (2014). The hippocampus and entorhinal cortex encode the path and Euclidean distances to goals during navigation. _Curr. Biol._ 24, 1331--1340. doi: 10.1016/j. cub.2014.05.001 

- Howard, L. R., Kumaran, D., Ólafsdóttir, H. F., and Spiers, H. J. (2013). Dissociation between dorsal and ventral posterior parietal cortical responses to incidental changes in natural scenes. _PLoS One_ 8:e67988. doi: 10.1371/journal. pone.0067988 

- Iaria, G., Fox, C. J., Chen, J. K., Petrides, M., and Barton, J. J. (2008). Detection of unexpected events during spatial navigation in humans: bottom-up attentional system and neural mechanisms. _Eur. J. Neurosci._ 27, 1017--1025. doi: 10.1111/j. 1460-9568.2008.06060.x 

- Johnson, A., van der Meer, M. A., and Redish, A. D. (2007). Integrating hippocampus and striatum in decision-making. _Curr. Opin. Neurobiol._ 17, 692--697. doi: 10.1016/j.conb.2008.01.003 

- Jovalekic, A., Hayman, R., Becares, N., Reid, H., Thomas, G., Wilson, J., et al. (2011). Horizontal biases in rats’ use of three-dimensional space. _Behav. Brain Res._ 222, 279--288. doi: 10.1016/j.bbr.2011.02.035 

- Kim, C., Johnson, N. F., Cilles, S. E., and Gold, B. T. (2011). Common and distinct mechanisms of cognitive flexibility in prefrontal cortex. _J. Neurosci._ 31, 4771--4779. doi: 10.1523/JNEUROSCI.5923-10.2011 

- Kim, S., Sapiurka, M., Clark, R. E., and Squire, L. R. (2013). Contrasting effects on path integration after hippocampal damage in humans and rats. _Proc. Natl. Acad. Sci. U S A_ 110, 4732--4737. doi: 10.1073/pnas.1300869110 

- Koechlin, E., Basso, G., Pietrini, P., Panzer, S., and Grafman, J. (1999). The role of the anterior prefrontal cortex in human cognition. _Nature_ 399, 148--151. doi: 10.1038/20178 

- Kubie, J. L., and Fenton, A. A. (2009). Heading-vector navigation based on head-direction cells and path integration. _Hippocampus_ 19, 456--479. doi: 10. 1002/hipo.20532 

- Kubie, J. L., and Fenton, A. A. (2012). Linear look-ahead in conjunctive cells: an entorhinal mechanism for vector-based navigation. _Front. Neural Circuits_ 6:20. doi: 10.3389/fncir.2012.00020 

- Lengyel, M., and Dayan, P. (2007). Hippocampal contributions to control: the third way. _NIPS_ 20, 889--896. 

- Lever, C., Burton, S., Jeewajee, A., O’Keefe, J., and Burgess, N. (2009). Boundary vector cells in the subiculum of the hippocampal formation. _J. Neurosci._ 29, 9771--9777. doi: 10.1523/JNEUROSCI.1319-09.2009 

- Lever, C., Wills, T., Cacucci, F., Burgess, N., and O’Keefe, J. (2002). Long-term plasticity in hippocampal place-cell representation of environmental geometry. _Nature_ 416, 90--94. doi: 10.1038/416090a 

- Løvstad, M., Funderud, I., Lindgren, M., Endestad, T., Due-Tønnessen, P., Meling, T., et al. (2012). Contribution of subregions of human frontal cortex to novelty processing. _J. Cogn. Neurosci._ 24, 378--395. doi: 10.1162/jocn_a_00099 

- Luria, A. R. (1966). _Higher Cortical Functions in Man._ London: Tavistock. 

- Maguire, E. A., Burgess, N., Donnett, J. G., Frackowiak, R. S., Frith, C. D., and O’Keefe, J. (1998). Knowing where and getting there: a human navigation network. _Science_ 280, 921--924. doi: 10.1126/science.280.5365.921 

- Maguire, E. A., and Mullally, S. L. (2013). The hippocampus: a manifesto for change. _J. Exp. Psychol. Gen._ 142, 1180--1189. doi: 10.1037/a0033650 

- Maguire, E. A., Nannery, R., and Spiers, H. J. (2006). Navigation around London by a taxi driver with bilateral hippocampal lesions. _Brain_ 129, 2894--2907. doi: 10.1093/brain/awl286 

- Martinet, L. E., Sheynikhovich, D., Benchenane, K., and Arleo, A. (2011). Spatial learning and action planning in a prefrontal cortical network model. _PLoS Comput. Biol._ 7:e1002045. doi: 10.1371/journal.pcbi.1002045 

- Miller, E. K., and Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. _Annu. Rev. Neurosci._ 24, 167--202. doi: 10.1146/annurev.neuro. 24.1.167 

- Milner, B. (1963). Effects of different brain lesions on card sorting: the role of the frontal lobes. _Arch. Neurol._ 9, 90--100. doi: 10.1001/archneur.1963. 00460070100010 

- Morris, R. G. M., Garrud, P., Rawlins, J. N. P., and O’Keefe, J. (1982). Place navigation impaired in rats with hippocampal lesions. _Nature_ 297, 681--683. doi: 10.1038/297681a0 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

13 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

- Moscovitch, M., Rosenbaum, R. S., Gilboa, A., Addis, D. R., Westmacott, R., Grady, C., et al. (2005). Functional neuroanatomy of remote episodic, semantic and spatial memory: a unified account based on multiple trace theory. _J. Anat._ 207, 35--66. doi: 10.1111/j.1469-7580.2005.00421.x 

- Muir, G. M., and Taube, J. S. (2004). Head direction cell activity and behavior in a navigation task requiring a cognitive mapping strategy. _Behav. Brain Res._ 153, 249--253. doi: 10.1016/j.bbr.2003.12.007 

- Nitz, D. A. (2006). Tracking route progression in the posterior parietal cortex. _Neuron_ 49, 747--756. doi: 10.1016/j.neuron.2006.01.037 

- Nitz, D. A. (2014). The posterior parietal cortex: interface between maps of external spaces and the generation of action sequences. _Space Time Mem. Hippocampal Formation_ 27--54. doi: 10.1007/978-3-7091-1292-2_2 

- O’Doherty, J. P., Hampton, A., and Kim, H. (2007). Model-based fMRI and its application to reward learning and decision making. _Ann. N Y Acad. Sci._ 1104, 35--53. doi: 10.1196/annals.1390.022 

- O’Keefe, J., and Burgess, N. (1996). Geometric determinants of the place fields of hippocampal neurons. _Nature_ 381, 425--428. doi: 10.1038/381425a0 

- O’Keefe, J., and Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. _Brain Res._ 34, 171--175. doi: 10.1016/0006-8993(71)90358-1 

- O’Keefe, J., and Nadel, L. (1978). _The Hippocampus as a Cognitive Map_ . Oxford: Clarendon Press. 

- Packard, M. G., and McGaugh, J. L. (1996). Inactivation of hippocampus or caudate nucleus with lidocaine differentially affects expression of place and response learning. _Neurobiol. Learn. Mem._ 65, 65--72. doi: 10.1006/nlme. 1996.0007 

- Passingham, R. E., and Wise, S. P. (2012). _The Neurobiology of the Prefrontal Cortex: Anatomy, evolution and the Origin of Insight._ Oxford: OUP. 

- Penfield, W., and Evans, J. (1935). The frontal lobe in man: a clinical study of maximum removals. _Brain_ 58, 115--133. doi: 10.1093/brain/58.1.115 

- Penny, W. D., Zeidman, P., and Burgess, N. (2013). Forward and backward inference in spatial cognition. _PLoS Comput. Biol._ 9:e1003383. doi: 10. 1371/journal.pcbi.1003383 

- Pfeiffer, B. E., and Foster, D. J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. _Nature_ 497, 74--79. doi: 10. 1038/nature12112 

- Poucet, B., Thinus-Blanc, C., and Chapuis, N. (1983). Route planning in cats, in relation to the visibility of the goal. _Anim. Behav._ 31, 594--599. doi: 10. 1016/s0003-3472(83)80083-9 

- Preston, A. R., and Eichenbaum, H. (2013). Interplay of hippocampus and prefrontal cortex in memory. _Curr. Biol._ 23, R764--R773. doi: 10.1016/j.cub. 2013.05.041 

- Ragozzino, M. E., Detrick, S., and Kesner, R. P. (1999a). Involvement of the prelimbic-infralimbic areas of the rodent prefrontal cortex in behavioral flexibility for place and response learning. _J. Neurosci._ 19, 4585--4594. 

- Ragozzino, M. E., Wilcox, C., Raso, M., and Kesner, R. P. (1999b). Involvement of rodent prefrontal cortex subregions in strategy switching. _Behav. Neurosci._ 113, 32--41. doi: 10.1037//0735-7044.113.1.32 

- Ramnani, N., and Owen, A. M. (2004). Anterior prefrontal cortex: insights into function from anatomy and neuroimaging. _Nat. Rev. Neurosci._ 5, 184--194. doi: 10.1038/nrn1343 

- Rauchs, G., Orban, P., Balteau, E., Schmidt, C., Degueldre, C., Luxen, A., et al. (2008). Partially segregated neural networks for spatial and contextual memory in virtual navigation. _Hippocampus_ 18, 503--518. doi: 10.1002/hipo.20411 

- Roca, M., Torralva, T., Gleichgerrcht, E., Woolgar, A., Thompson, R., Duncan, J., et al. (2011). The role of area 10 (BA10) in human multitasking and in social cognition: a lesion study. _Neuropsychologia_ 49, 3525--3531. doi: 10.1016/j. neuropsychologia.2011.09.003 

- Rondi-Reig, L., Paradis, A. L., Lefort, J. M., Babayan, B. M., and Tobin, C. (2014). How the cerebellum may monitor sensory information for spatial representation. _Front. Syst. Neurosci._ 8:205. doi: 10.3389/fnsys.2014.00205 

- Rosenbaum, R. S., Cassidy, B., and Herdman, K. A. (2015). Patterns of preserved and impaired spatial memory in a case of developmental amnesia. _Front. Hum. Neurosci._ 

- Rosenbaum, R. S., Priselac, S., Köhler, S., Black, S. E., Gao, F., Nadel, L., et al. (2000). Remote spatial memory in an amnesic person with extensive bilateral hippocampal lesions. _Nat. Neurosci._ 3, 1044--1048. doi: 10.1038/79867 

- Rosenbaum, R. S., Winocur, G., Grady, C. L., Ziegler, M., and Moscovitch, M. (2007). Memory for familiar environments learned in the remote past: fMRI 

- studies of healthy people and an amnesic person with extensive bilateral hippocampal lesions. _Hippocampus_ 17, 1241--1251. doi: 10.1002/hipo.20354 

- Rosenbaum, R. S., Ziegler, M., Winocur, G., Grady, C. L., and Moscovitch, M. (2004). ‘‘I have often walked down this street before’’: fMRI studies on the hippocampus and other structures during mental navigation of an old environment. _Hippocampus_ 14, 826--835. doi: 10.1002/hipo.10218 

- Sargolini, F., Fyhn, M., Hafting, T., McNaughton, B. L., Witter, M. P., Moser, M. B., et al. (2006). Conjunctive representation of position, direction and velocity in entorhinal cortex. _Science_ 312, 758--762. doi: 10.1126/science.1125572 

- Scoville, W. B., and Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. _J. Neurol. Neurosurg. Psychiatry_ 20, 11--21. doi: 10. 1136/jnnp.20.1.11 

- Shallice, T. (1982). Specific impairments of planning. _Philos. Trans. R. Soc. Lond. B Biol. Sci._ 298, 199--209. doi: 10.1098/rstb.1982.0082 

- Shallice, T., and Burgess, P. W. (1991). Deficits in strategy application following frontal lobe damage in man. _Brain_ 114, 727--741. doi: 10.1093/brain/114.2.727 

- Shallice, T., and Cooper, R. P. (2011). _The Organization of Mind._ Oxford: OUP. Sherrill, K. R., Erdem, U. M., Ross, R. S., Brown, T. I., Hasselmo, M. E., and Stern, C. E. (2013). Hippocampus and retrosplenial cortex combine path integration signals for successful navigation. _J. Neurosci._ 33, 19304--19313. doi: 10.1523/JNEUROSCI.1825-13.2013 

- Shrager, Y., Kirwan, C. B., and Squire, L. R. (2008). Neural basis of the cognitive map: path integration does not require hippocampus or entorhinal cortex. _Proc. Natl. Acad. Sci. U S A_ 105, 12034--12038. doi: 10.1073/pnas.0805414105 

- Simon, D. A., and Daw, N. D. (2011). Neural correlates of forward planning in a spatial decision task in humans. _J. Neurosci._ 31, 5526--5539. doi: 10. 1523/JNEUROSCI.4647-10.2011 

- Simons, J. S., and Spiers, H. J. (2003). Prefrontal and medial temporal lobe interactions in long-term memory. _Nat. Rev. Neurosci._ 4, 637--648. doi: 10. 1038/nrn1178 

- Spiers, H. J. (2008). Keeping the goal in mind: prefrontal contributions to spatial navigation. _Neuropsychologia_ 46, 2106--2108. doi: 10.1016/j.neuropsychologia. 2008.01.028 

- Spiers, H. J. (2012). Hippocampal formation. _Encyclopedia Hum. Behav._ 2, 297--304. doi: 10.1016/b978-0-12-375000-6.00190-7 

- Spiers, H. J., and Barry, C. (2015). Neural systems supporting navigation. _Curr. Opin. Behav. Sci._ 1, 47--55. doi: 10.1016/j.cobeha.2014.08.005 

- Spiers, H. J., Burgess, N., Hartley, T., Vargha-Khadem, F., and O’Keefe, J. (2001b). Bilateral hippocampal pathology impairs topographical and episodic memory but not visual pattern matching. _Hippocampus_ 11, 715--725. doi: 10.1002/ hipo.1087 

- Spiers, H. J., Burgess, N., Maguire, E. A., Baxendale, S. A., Hartley, T., Thompson, P. J., et al. (2001a). Unilateral temporal lobectomy patients show lateralized topographical and episodic memory deficits in a virtual town. _Brain_ 124, 2476--2489. doi: 10.1093/brain/124.12.2476 

- Spiers, H. J., Hayman, R. M., Jovalekic, A., Marozzi, E., and Jeffery, K. J. (2015). Place field repetition and purely local remapping in a multicompartment environment. _Cereb. Cortex_ 25, 10--25. doi: 10.1093/cercor/bht198 

- Spiers, H. J., and Maguire, E. A. (2006). Thoughts, behaviour and brain dynamics during navigation in the real world. _Neuroimage_ 31, 1826--1840. doi: 10.1016/j. neuroimage.2006.01.037 

- Spiers, H. J., and Maguire, E. A. (2007a). The neuroscience of remote spatial memory: a tale of two cities. _Neuroscience_ 149, 7--27. doi: 10.1016/j. neuroscience.2007.06.056 

- Spiers, H. J., and Maguire, E. A. (2007b). A navigational guidance system in the human brain. _Hippocampus_ 17, 618--626. doi: 10.1002/hipo.20298 

- Spiers, H. J., and Maguire, E. A. (2008). The dynamic nature of cognition during wayfinding. _J. Environ. Psychol._ 28, 232--249. doi: 10.1016/j.jenvp.2008.02.006 

- Steffenach, H. A., Witter, M., Moser, M. B., and Moser, E. I. (2005). Spatial memory in the rat requires the dorsolateral band of the entorhinal cortex. _Neuron_ 45, 301--313. doi: 10.1016/j.neuron.2004.12.044 

- Steiner, A. P., and Redish, A. D. (2014). Behavioral and neurophysiological correlates of regret in rat decision-making on a neuroeconomic task. _Nat. Neurosci._ 17, 995--1002. doi: 10.1038/nn.3740 

- Sutton, R. S., and Barto, A. G. (1998). _Introduction to Reinforcement Learning._ MIT Press. 

- Szczepanski, S. M., and Knight, R. T. (2014). Insights into human behavior from lesions to the prefrontal cortex. _Neuron_ 83, 1002--1018. doi: 10.1016/j.neuron. 2014.08.011 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

14 

Spiers and Gilbert 

Prefrontal-hippocampal interactions for navigation 

- Taube, J. S., Muller, R. U., and Ranck, J. B. (1990). Head-direction cells recorded from the postsubiculum in freely moving rats. I. Description and quantitative analysis. _J. Neurosci._ 10, 420--435. 

- Teng, E., and Squire, L. R. (1999). Memory for places learned long ago is intact after hippocampal damage. _Nature_ 400, 675--677. doi: 10.1038/23276 

- Tolman, E. C. (1948). Cognitive maps in rats and men. _Psychol. Rev._ 55, 189--208. doi: 10.1037/h0061626 

- Tolman, E. C., and Honzik, C. H. (1930). _Introduction and Removal of Reward and Maze Performance in Rats._ University of California Publications in Psychology. 

- Tse, D., Langston, R. F., Kakeyama, M., Bethus, I., Spooner, P. A., Wood, E. R., et al. (2007). Schemas and memory consolidation. _Science_ 316, 76--82. doi: 10. 1126/science.1135935 

- Ullsperger, M., Danielmeier, C., and Jocham, G. (2014). Neurophysiology of performance monitoring and adaptive behavior. _Physiol. Rev._ 94, 35--79. doi: 10.1152/physrev.00041.2012 

- van der Meer, M., Kurth-Nelson, Z., and Redish, A. D. (2012). Information processing in decision-making systems. _Neuroscientist_ 18, 342--359. doi: 10. 1177/1073858411435128 

- van der Meer, M. A., and Redish, A. D. (2011). Ventral striatum: a critical look at models of learning and evaluation. _Curr. Opin. Neurobiol._ 21, 387--392. doi: 10. 1016/j.conb.2011.02.011 

- Viard, A., Doeller, C. F., Hartley, T., Bird, C. M., and Burgess, N. (2011). Anterior hippocampus and goal-directed spatial decision making. _J. Neurosci._ 31, 4613--4621. doi: 10.1523/jneurosci.4640-10.2011 

- Wendelken, C., Ditterich, J., Bunge, S. A., and Carter, C. S. (2009). Stimulus and response conflict processing during perceptual decision making. _Cogn. Affect. Behav. Neurosci._ 9, 434--447. doi: 10.3758/cabn.9.4.434 

- Whitlock, J. R., Sutherland, R. J., Witter, M. P., Moser, M. B., and Moser, E. I. (2008). Navigating from hippocampus to parietal cortex. _Proc. Natl. Acad. Sci. U S A_ 105, 14755--14762. doi: 10.1073/pnas.0804216105 

- Wikenheiser, A. M., and Redish, A. D. (2015). Hippocampal theta sequences reflect current goals. _Nat. Neurosci._ 18, 289--294. doi: 10.1038/nn.3909 

- Wills, T. J., Lever, C., Cacucci, F., Burgess, N., and O’Keefe, J. (2005). Attractor dynamics in the hippocampal representation of the local environment. _Science_ 308, 873--876. doi: 10.1126/science.1108905 

- Winocur, G., Moscovitch, M., Rosenbaum, R. S., and Sekeres, M. (2010). An investigation of the effects of hippocampal lesions in rats on pre-and postoperatively acquired spatial memory in a complex environment. _Hippocampus_ 20, 1350--1365. doi: 10.1002/hipo.20721 

- Wolbers, T., Wiener, J. M., Mallot, H. A., and Büchel, C. (2007). Differential recruitment of the hippocampus, medial prefrontal cortex and the human motion complex during path integration in humans. _J. Neurosci._ 27, 9408--9416. doi: 10.1523/jneurosci.2146-07.2007 

- Wood, E. R., Dudchenko, P. A., Robitsek, R. J., and Eichenbaum, H. (2000). Hippocampal neurons encode information about different types of memory episodes occurring in the same location. _Neuron_ 27, 623--633. doi: 10. 1016/s0896-6273(00)00071-4 

- Worsley, C. L., Recce, M., Spiers, H. J., Marley, J., Polkey, C. E., and Morris, R. G. (2001). Path integration following temporal lobectomy in humans. _Neuropsychologia_ 39, 452--464. doi: 10.1016/s0028-3932(00)00140-8 

- Xu, J., Evensmoen, H. R., Lehn, H., Pintzka, C. W., and Håberg, A. K. (2010). Persistent posterior and transient anterior medial temporal lobe activity during navigation. _Neuroimage_ 52, 1654--1666. doi: 10.1016/j.neuroimage.2010.05.074 

**Conflict of Interest Statement** : The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. 

_Copyright © 2015 Spiers and Gilbert. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution and reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms_ . 

Frontiers in Human Neuroscience | www.frontiersin.org 

March 2015 | Volume 9 | Article 125 

15 

