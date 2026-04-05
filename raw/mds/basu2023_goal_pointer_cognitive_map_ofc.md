Available online at www.sciencedirect.com 

**Current Opinion in Neurobiology** 

**==> picture [47 x 51] intentionally omitted <==**

## ScienceDirect 

## A goal pointer for a cognitive map in the orbitofrontal cortex Raunak Basu[1] and Hiroshi T. Ito[2] 

**==> picture [25 x 25] intentionally omitted <==**

## Abstract 

Knowing where you are and where you go is a prerequisite for planning a goal-directed journey. The discovery of spatially tuned neurons in the hippocampus and parahippocampal cortices provides a mechanism by which the brain pinpoints an animal’s own position in an environment. By contrast, how the brain encodes a remote navigational goal remained largely obscure until recently. In this review, we discuss algorithmic challenges and requirements for the brain to form a representation of a remote navigational goal at which an animal is not present. We then highlight a line of evidence that neurons in the orbitofrontal cortex (OFC) represent a goal location persistently while an animal navigates to this destination. Finally, we propose a new perspective of navigation research opened by this recently reported brain’s goal map. 

chore sets up an interesting conundrum. At the beginning of the journey, all the incoming sensory signals to the brain are associated with your current location (home). However, the brain is still required to form a representation of a future destination (store) that is located outside your sensory perception. Furthermore, as you walk down the path, the brain should keep track of your instantaneous location while maintaining a representation of the store. Hence, a brain’s circuitry encoding a navigational goal must be somewhat independent of constantly changing sensory inputs from the external world. This raises the question of whether the brain has two separate spatial representation systems d one that keeps track of one self’s location and the other that points to a navigational goal throughout the journey. 

## Addresses 

> 1 Edmond and Lily Safra Center for Brain Sciences, The Hebrew University of Jerusalem, Jerusalem 9190401, Israel 

> 2 Max Planck Institute for Brain Research, Frankfurt am Main 60438, Germany 

Corresponding authors: Ito, Hiroshi T. (hiroshi.ito@brain.mpg.de); Basu, Raunak (raunak.basu@mail.huji.ac.il) 

(Basu R.) 

## Current Opinion in Neurobiology 2023, 83:102803 

This review comes from a themed issue on Computational Neuroscience 2023 

Edited by Jeanette Hellgreny Kotaleski and Tatjana Tchumatchenko For a complete overview see the Issue and the Editorial Available online xxx 

https://doi.org/10.1016/j.conb.2023.102803 

0959-4388/© 2023 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC license ( http:// creativecommons.org/licenses/by-nc/4.0/). 

## Introduction 

Imagine a situation where you navigate to a local grocery store from your home. Before initiating this journey, you typically start by thinking about the store, such as its location and appearance. This mental imagination process would give you an intuitive sense of the direction and distance of the store, which helps you plan the subsequent journey. Here, this daily 

Navigation studies pioneered by Edward Tolman almost a century ago revealed that, like humans, rodents could take an efficient strategy to reach a target destination in a complex environment [1]. These studies led to the hypothesis that the brain forms its internal model of the environment, the so-called cognitive map, by which an animal can plan a goaldirected trajectory, even including unseen parts of the environment [2]. The subsequent investigation for neural substrates of a cognitive map led to the discovery of place cells in the hippocampus and grid cells in the medial entorhinal cortex [3,4]. Each place cell encodes a particular location in a behavioral apparatus, while a grid cell fires at multiple locations, forming a hexagonal metric that tiles the entire arena. The advances in large-scale neural recording technology further enabled researchers to confirm that, at any given point in time, an ensemble activity pattern of place cells or grid cells can accurately pinpoint an animal’s location in an environment [5e7]. However, if the activity of these neurons in the hippocampus and parahippocampal cortices encode an animal’s instantaneous position, how can the same map be used for representing a future goal location (Figure 1) [8]? This question motivated many researchers to investigate the impact of a navigational goal on the hippocampalentorhinal spatial map. In the following section, we will highlight some of these results and discuss whether the proposed mechanisms can solve the issue of goal representation in the brain. 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

2 Computational Neuroscience 2023 

Figure 1 

**==> picture [353 x 162] intentionally omitted <==**

Algorithmic challenge for goal representation in the brain. Schematics show an animal’s journey towards a goal at three different time points during navigation. The Gaussians underneath the maze represent the firing fields of individual place cells. The animal’s location at each time point is accurately encoded by the corresponding place cell shown in green. However, the brain must also encode the goal location persistently throughout the journey. The schematic on the right highlights the brain’s need for two distinct spatial mapping systems to execute goal-directed navigation. 

## Neural correlates of navigation in the hippocampal spatial map 

A navigational goal is usually a location with high incentive value. If so, is such a high-value location represented differently on the hippocampal spatial map? By using an annular water maze task, Hollup et al. [9] demonstrated that place cells were more densely clustered near the region where the escape platform was located. The same conclusions were obtained from experiments using other reward-guided tasks [10,11]. Recent studies further demonstrated that, as an animal learns a new reward location, a subset of place cells and grid cells shift their firing fields toward this high-value area [12e14]. On the other hand, another study identified a distinct subset of hippocampal CA1 neurons that exhibit elevated firing as an animal approaches a reward location, and the firing location of these neurons shifts accordingly when the reward delivery site is moved [15]. A subsequent study further demonstrated that the optogenetic activation of these CA1 neurons that fire near reward locations was able to evoke an animal’s consummatory behaviors even without an actual reward [16]. These studies together indicate that motivationally salient locations are encoded by a statistically larger number of hippocampal neurons (compared to other locations) whose activity can even drive rewardassociated behaviors. However, such reward-related activity in the hippocampus occurs only when the animal is near or at the goal location, and it is thus unlikely that this information can be used for planning a goal-directed journey at the beginning of navigation. 

As an alternative mechanism for navigation, several studies have suggested a key role of sequential spiking among place cell ensembles during navigation. Such 

spiking occurs outside the firing fields of place cells, and the positions encoded by these sequences are often correlated with an animal’s upcoming trajectory from the current position to the destination. These trajectory sequences are observed either before the navigation onset as a phenomenon called replay [6] or during navigation using spike-phase coding relative to hippocampal theta oscillations [17,18]. However, other studies have argued that such events are not necessarily correlated with the animal’s future goal-bound trajectory but rather represent either previous journeys [19e21] or alternative trajectories without a particular bias toward the animal’s subsequently chosen path [22]. 

In addition to trajectory sequences, several lines of evidence suggest that hippocampal neurons can also encode the direction toward the goal. A study in bats revealed that CA1 neurons encode a relative angle from the animal’s heading direction to the goal [23]. A similar result was reported in rats, demonstrating that a fraction of CA1 neurons encode the animal’s heading direction toward a neuron’s ‘sink’ position that is often located near the goal [24]. Finally, CA1 place cells are known to fire at distinct rates as the animal crosses the same location but with different subsequent trajectories [25,26]. However, by using a task in which multiple routes lead to the same goal, this differential firing of place cells was shown to represent an animal’s decision about trajectory rather than goal [27,28]. 

These previous observations together suggest that neurons in the hippocampus are indeed influenced by a navigational goal, either through overrepresenting a reward location, generating brief trajectory sequences, or forming a goal-directed vector. A plausible navigation 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

A goal map in the brain Basu and Ito 3 

mechanism from these findings would be that the overrepresentation of a reward location by place cells may somehow modulate brief trajectory sequences or a goal vector in the hippocampal map, which may help the planning of a goal-directed journey. However, an important algorithmic question here is whether this mechanism can fully support the animal’s ability of flexible navigation because whenever a goal location switches, it imposes connectivity changes in the hippocampal circuitry. Another plausible explanation of these previous findings is the existence of a brain region that can feed the goal information into the hippocampus. The key advantage of this mechanism is that this plausible goal-coding region would be free from the duty of tracking an animal’s instantaneous position and can entirely be dedicated to encoding a goal location throughout the journey. In fact, several theoretical models have assumed the existence of an external source of goal signal to explain the role of place cells and grid cells in goal-directed navigation [29e31]. For example, a recent theoretical model inspired by reinforcement learning theory suggests that a machinelearning agent can perform gradient ascent along the value function, defined as the value of each location in the environment, to navigate to a target destination [32]. Such a value function can be computed by multiplying a successor representation matrix, which contains the probabilities of eventually transitioning from one state to another, with a vector comprising the probabilities of reward at individual states (a reward vector) [33]. Interestingly, the columns of the successor representation matrix have properties that resemble the firing fields of individual place cells [34]. This elegant formulation separates state transition (successor representation) from reward representation, allowing a new journey to a different goal to be executed simply by changing a reward vector applied to the same successor representation. Applying this idea to the brain suggests the advantage of separating the hippocampal map from a goal-representing circuitry, but this mechanism instead requires an extra-hippocampal source of a reward vector to compute a value function. Furthermore, although a theory suggests that updating the reward vector and computing the value function can occur at the reward location, there are scenarios in which maintaining a prospective reward representation during navigation is necessary. For example, if an agent needs to decide between journeys toward different reward locations, it would be required to play out and evaluate trajectories originating from the same starting location to different goals by applying corresponding reward vectors [32]. In addition, if an agent encounters an obstacle during the journey, it would need to re-calculate a new value function on site, thereby again requiring the reward vector. Hence, the existence of a brain region that persistently provides a reward-state representation is likely advantageous for real-world navigation problems. 

Overall, neurons in the hippocampus and parahippocampal regions exhibit goal-related activities that have long been considered to play a key role in goaldirected navigation. However, both experimental and theoretical results point to the advantage of having a separate brain region that maintains a persistent goal representation to support flexible navigation. 

## Representation of spatial goals in the orbitofrontal cortex 

As a notable clinical case, Ciaramelli reported a patient with a lesion in the ventromedial prefrontal cortex (including the OFC) who had difficulty in maintaining the goal location during navigation [35]. Remarkably, this patient’s navigation ability significantly improved when a periodic reminder of the goal location was provided, suggesting that this prefrontal region plays an essential role in goal maintenance during navigation. Analogous results were observed in rats where silencing of the OFC activity resulted in spatial memory deficits in a Morris water maze task and a place avoidance task [36]. These results together indicate that the OFC may be a crucial brain region representing navigational goals. However, what kind of neural coding principles underlie the representation of a future goal location? 

In the earlier example of navigation setting to a local grocery store, your decision to visit either this store or other locations should elicit distinct patterns of neural activity to discriminate individual destinations. In addition, this goal-specific pattern should arise even prior to the onset of navigation. This idea is consistent with previous studies focusing on goal-directed behavior in rats, showing that OFC neurons fire differentially depending on the animal’s choice. In an experiment where rats were trained to nose-poke at a beaconed location to receive a water reward, OFC neurons exhibited target-location-specific firing as the animal approached there [37]. However, whether this targetspecific OFC activity emerged at the onset of goaldirected movement was unclear. In a subsequent study, rats were trained to choose either the left or the right reward-delivery port depending on the odor cue delivered at the central port [38]. The authors found that the OFC neural ensembles encode the animal’s subsequent movement direction even before motion onset (Figure 2a). Similar results were reported in other studies using a variant of this task [39,40]. Furthermore, Riceberg and Shapiro recorded the activity of OFC neurons while an animal performed a plus maze task in which the animal was trained to navigate to either the east or the west arm of the maze from a starting position at the north or the south arm [41]. Interestingly, a fraction of OFC neurons exhibited target-specific firing even before the animal made a trajectory choice. These results together suggest that OFC neurons fire prospectively and differentially depending on an animal’s 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

4 Computational Neuroscience 2023 

Figure 2 

**==> picture [463 x 341] intentionally omitted <==**

Goal representation in the OFC. (a), Left, schematic of a task design where animals are required to target either the left or the right reward port depending on the odor identity delivered in the central port. Middle, raster plots and mean firing rates of a representative OFC neuron that fires more whenever the animal targets the right port irrespective of the odor identity. Note that the elevated spiking occurs immediately after the animal recedes from the odor port and prior to reaching the reward port. Right, a significant fraction of OFC neurons exhibit firing specific to the target direction. Reproduced with permission from the study by Feierstein et al. [38]. (b), Left, schematic of a navigation task comprising ten equally spaced reward locations, where animals need to alternate between two given locations to obtain a reward. The rewarding pair of locations changes periodically, thereby requiring continuous updating of the goal. The bottom panel shows the firing rates of a representative OFC neuron aligned to the onset of navigation and the subsequent onset of licking at the goal well. Trials are averaged and color-coded based on the target well location. Note that the destination-specific firing pattern at the motion onset resembles the activity during subsequent approach and reward consumption at the destination. Middle, decoding probability of the start position and the future goal as well as their neighboring locations, aligned at the onset of navigation. Note that the decoding of the future goal starts exceeding the chance level approximately 1 s prior to the motion onset. The goal representation of OFC neural ensembles is resistant to interference by intermediate locations during navigation, including the well next to the start or the well prior to the goal, as evident from their weak decoding probabilities. Right, OFC neural ensemble activity projected onto three principle components reveal that destination-specific neural trajectories originate at the onset of navigation and evolve by keeping their resemblance until the animal reaches the target destination. Neural trajectories are trial averaged based on goal wells. Reproduced with permission from the study by Basu et al. [44]. OFC. 

target location. However, the task designs used in these previous studies do not allow us to distinguish whether neurons encode a goal location itself or its associated goal-directed actions. 

Goal-specific prospective activity has also been reported in the OFC of human subjects. In a virtual navigational task, subjects undergoing functional magnetic resonance imaging (fMRI) were required to navigate from different starting positions to one of five locations instructed by a given sensory cue [42]. The authors 

observed the goal-specific activity modulation in the voxels of both the hippocampus and the OFC before the subject started navigation. However, while this activity in the OFC can distinguish the subject’s future goal destinations, it is not clear whether it encodes the goal location per se or its associated instructive cues. Moreover, to define a neural representation of spatial goals, the observation of distinct goal-specific neural activity patterns is not sufficient because they may simply reflect different behavioral states rather than spatial goals. A critical aspect of spatial goal representation is 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

A goal map in the brain Basu and Ito 5 

that the neural activity elicited at the onset of navigation should maintain its resemblance until the subject or animal reaches the target destination, irrespective of midway routes or actions. This idea was first proposed several decades ago, in which a neural representation of future goals was referred to as a “statistical facsimile” of the neural activity that was observed while the animal experienced these exact goal states [43]. Furthermore, this coding scheme will have two accompanying features in the context of navigation. First, a brain region representing goals should exhibit distinct firing patterns depending on the animal’s visiting locations, implying the formation of a spatial map. Second, a target-specific neural activity pattern should not be perturbed by intermediate locations crossed over by the animal. 

To test the coding principles of goal representation in the OFC, Basu et al. designed a linear track with ten equally spaced reward locations, and rats needed to alternate between two given locations at a time to obtain a water reward (Figure 2b) [44]. After several successful alternations, the rewarding pair of locations was changed, thereby requiring continuous updates of the goal location. The task design ensured that the same goal was approached from different starting locations and directions, thereby largely uncoupling the goal location from the action needed to reach there. As rats performed this task, the OFC neural activity distinctly encoded the animal’s target locations during reward consumption at both the single neuron and the ensemble levels, implying the presence of a locationspecific map in the OFC. Tracking the temporal origin of this target-specific activity revealed that, prior to the onset of navigation when the animal is still at a starting location, OFC neurons exhibit a representational switch from the animal’s position to the subsequent goal location. This goal representation then persists throughout the entire journey until the animal reaches the destination without being influenced by intermediate locations that the animal crosses over during the journey. Further, population-level analysis revealed that this persistent goal coding is maintained through destination-specific neural activity trajectories that are defined at navigation onset and evolve during navigation in a largely deterministic manner. Overall, these results indicate that OFC neural ensembles form goal-specific firing patterns before the onset of navigation, and this pattern is expressed persistently and dynamically throughout the journey. This dynamic coding scheme ensures that a goal-specific neural firing pattern at navigation onset is tightly linked to that at the goal destination through target-invariant deterministic evolution of neural dynamics. Finally, a causal role of the OFC in deciding the goal location was confirmed by manipulating the OFC activity, in which the optogenetic perturbation of OFC neurons, specifically at the navigation onset, caused the animal to navigate to an 

incorrect destination. Taken together, several lines of evidence across species point to the OFC as a critical part of the brain’s internal map that represents the animal’s decision of navigational goals. 

## Wider brain circuits for goal-directed navigation 

Although a well-defined prospective coding of spatial goals has been described only in the OFC so far, several studies suggest the importance of other brain regions for the execution of successful goal-directed navigation. For example, a recent study reported that projections from the retrosplenial cortex (RSC) to the superior colliculus (SC) are critical for shelter-directed escape behavior [45]. Specifically, in a setup where mice could escape to a shelter upon hearing an auditory threat signal, a population of both RSC and SC neurons was tuned to the shelter direction. Notably, silencing RSC inputs to SC resulted in the incorrect orientation of the animal towards the shelter, specifically during the escape behavior, whereas the same perturbation did not affect a navigation task where the animal was required to visit a reward location. These results imply that there may be distinct circuits in the brain dedicated to different kinds of goal-directed navigation depending on the valence and urgency of behaviors. 

Another candidate brain region for spatial goal representation is the medial prefrontal cortex (mPFC). The role of mPFC has been implicated in supporting spatial working memory [46] and trajectory planning during navigation [27,47]. Whether mPFC neurons exhibit goal-dependent activity was explored using a task in which rats needed to visit a particular target location in an arena to obtain a reward dispensed elsewhere [48]. The authors found that a fraction of mPFC neurons fired specifically when the animal visited the target or near the feeder, although the prospective nature of this goal coding was not tested. A recent study carefully examined whether prospective goal coding exists in mPFC by using an elegant task design in which an animal was required to visit a given goal location from a specific starting location via a route that could be determined in each trial based on a flexible bridge mechanism controlled by the experimenter [49]. However, the authors reported that the goal location could not be decoded at either the beginning or the middle of navigation before the animal reached the goal. This result indicates that the prospective and persistent goal coding observed in the OFC [42] is not likely derived from mPFC neurons. However, it is also plausible that high cognitive demand for flexible route planning in this task may impose the brain to re-distribute the workload across regions, including mPFC and OFC. Hence, to decipher task dependence of goal representation in the brain, neural activity from multiple brain areas must be monitored across different navigation tasks. 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

6 Computational Neuroscience 2023 

## A new perspective for a neural mechanism of navigation 

The recent report on the goal map in the OFC [44] inspires new sets of questions in navigation research. Below we describe two broad questions d how a spatial map is formed and how a goal representation emerges in the OFC. 

Converging evidence from many studies suggests that OFC neurons exhibit location-specific firing even when these locations dispense an identical reward [37,38,41,44]. Basu et al. further showed that this location-specific activity emerges prior to the onset of navigation and is maintained throughout the journey [44]. But how are such spatial representations formed in the OFC? Location-specific activity has been described in brain regions outside the entorhinal-hippocampal regions, such as the RSC [50], the anterior cingulate cortex [51], and the piriform cortex [52]. These previous studies suggested that inputs from the hippocampus support the spatial tuning of neurons in these extrahippocampal regions. Does spatial map formation in the OFC also depend on hippocampal inputs? Anatomically, the OFC receives direct projections from the ventral part of the hippocampal CA1 and the subiculum [53] while being disynaptically and reciprocally connected with the CA1 via the nucleus reuniens [54], which enables bidirectional communication between the two brain regions. In support of the direct anatomical connection, Wikenheiser et al. showed that silencing the ventral hippocampus specifically impaired the OFC’s representation of target direction but no other reward attributes (type or amount) during a decision-making task requiring a choice between left and right reward ports [40]. However, whether the position coding in the OFC depends on inputs from the hippocampus remains an open question. In addition, as previously mentioned, the OFC spatial map differs from the entorhinal-hippocampal spatial maps in terms of not representing locations midway during the journey. Hence, the formation of location-specific representations in the OFC using the hippocampal map may only be facilitated when the animal arrives at reward-delivery locations, potentially by relying on reinforcement signals from dopaminergic nuclei [55] or the amygdala [56]. On the other hand, once the animal starts a journey, a lack of reinforcement signals may force the OFC to ignore spatial inputs from the hippocampus but instead maintain a representation of the target location (Figure 3a). 

The existence of multiple spatial maps in the brain raises another important question d how can a navigational route be planned through interactions between the OFC and the hippocampus-parahippocampal system? As we described in the prior section, one of the prominent neural correlates of route planning is the brief trajectory sequences generated by hippocampal CA1 place cells 

before the onset of navigation [6]. Because many of these sequences are directed toward the subsequent goal location, it is possible that these goal-directed sweeps may depend on the goal signal from the OFC. If so, how can a particular goal-specific pattern of OFC neural activity indicate the exact same goal location on the hippocampal spatial map? A plausible solution for this map registration problem would be that, during reward consumption, the reward-evoked elevation of neural activity in both the OFC and hippocampus may strengthen interregional coupling between the two regions’ representations of the same goal location. Then, later during trajectory planning, while multiple trajectory sequences are generated in the hippocampus, the ones that terminate at the goal location encoded in the OFC may selectively be coactivated between the regions, thereby becoming leading candidates for the animal’s trajectory decision (Figure 3b) [57]. 

The next major question warranting further investigation is how a goal representation emerges in the OFC circuitry. This question can also be considered as deciphering the neural mechanism of spatial decisionmaking. The role of OFC in value-based decisionmaking has been intensively investigated over the past several decades [58,59]. Previous recording studies from the OFC have identified neural correlates for several decision-related variables, for example, the identity [60,61], absolute value [62], relative value [63], and associated attributes [39,40] of an animal’s chosen options, as well as the overall value of available options [62], decision confidence [64e66], and previous choices with their associated reward history [65,67,68]. However, how different options and their attributes are compared to make a final decision remains largely unknown. A recent study, however, provided a new insight into this process, in which the authors recorded from OFC neurons while monkeys chose between two images, each of which predicted a certain reward amount [60]. During the decision-making process, OFC neural ensembles continuously switched between the representation of the two images but with a longer dwelling time for an eventually chosen image. A similar mechanism might also explain the formation of goal representation in the context of spatial decision-making where an animal needs to choose between locations with different values (Figure 3c). However, the cognitive demands of spatial decisions differ from that of traditional value-based decisions in an important aspect. During spatial decisionmaking, an animal cannot perceive the candidate options (locations), and thus, this decision must be implemented purely based on an animal’s internal map of locations and their associated values. It is thus an important question of how the brain can form such a conjunctive code of position and value, which can be accessed from a distant starting location without relying on explicit sensory triggers. Furthermore, the goal values 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

A goal map in the brain Basu and Ito 7 

Figure 3 

**==> picture [460 x 275] intentionally omitted <==**

New perspectives on neural mechanisms of navigation. (a), Neural pathways that may underlie the formation of spatial representations in the OFC. During reward consumption, OFC neurons may form reward location-specific representations using spatially tuned inputs from the dorsal and ventral hippocampus as well as reward-related signals from the amygdala, and dopaminergic nuclei. However, during a goal-directed journey, the absence of strong reinforcement signals may enable the OFC to represent the goal location persistently by ignoring inputs from the hippocampus. HPC: hippocampus, Amy: amygdala, DA: dopaminergic nuclei comprising ventral tegmental area and substantia nigra pars compacta. Disynaptic input from the hippocampus is shown by dotted lines. (b), Schematic highlighting overrepresentation of hippocampal trajectory sequences targeting the goal location (red dotted lines) as observed by Pfeiffer and Foster, 2013 [6]. Dotted lines represent trajectory sequences originating from the animal’s starting location, reaching either the goal (red) or non-goal (black) locations. Place fields along two example trajectories are depicted in ovals. Representation of the future goal location by the OFC may act as an instructive signal (as suggested by the theoretical model of Erdem and Hasselmo, 2012 [57]) that would facilitate the enrichment of hippocampal trajectory sequences that target the goal location. (c), A potential mechanism for the formation of goal representation in the OFC during a spatial-decision task. Schematic shows two possible locations, each of which offers different amounts of reward. Based on the dynamics of decisionmaking observed by Rich and Wallis, 2016 [60], we suggest that prior to the onset of navigation, OFC neural ensembles would switch between representations of the two locations, and the one with the highest dwell time will be chosen as the future goal (blue in this case). (d), Schematic of a continuous alternation task where the animal needs to visit the reward port opposite to the one visited in the previous trial. This task comprises two states, each of which corresponds to the journey to either the left (red) or right (blue) reward port. Shading indicates the fraction of the journey completed within each state. OFC neural ensembles can distinguish individual states irrespective of dynamically-evolving neural activity trajectories over navigation (based on observations reported in the study by Basu et al. [44] and Zhou et al. [71]). The end of the state would trigger a transition to the beginning of the other state, resulting in alternations between the two states. This representational scheme ensures the encoding of the next goal throughout the journey, even when the animal is at the common stem region of the maze. 

should be determined not only by their directly associated attributes but also based on the self’s position and the geometry of the environment. For example, even a highly rewarding location may not be so valuable if it is too far from an animal or if the path is hindered by an obstacle. Hence, the decision of a goal is intertwined with the evaluation of candidate routes, and this process will involve larger brain-wide circuits that perform route planning and effort-based tradeoff. 

Although the mechanism of spatial goal representation could be understood through the lens of value-based 

decision-making, it is important to note that, in most lab experiments, a goal is defined based on a corresponding task rule. Hence, to determine how a goal representation emerges in the OFC, it is important to understand how a task rule is encoded in the OFC or other brain regions. Specifically, a task rule is often structured as a sequence of state transitions. For example, a continuous alternation task in a T-maze may comprise two states, one in which the animal targets the left reward port and the other where the animal approaches the right. For the successful execution of the goal alternation task, one state should transition to the 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

8 Computational Neuroscience 2023 

other with a high probability at the beginning of individual trials, followed by persistent state maintenance during the subsequent goal-directed journey (Figure 3d). Recent theories on the OFC function indicate that the OFC forms a model of task structure with distinct representations of task states as well as transition probabilities between them [69,70]. In support of this hypothesis, Zhou and colleagues designed a task where rats were presented with a sequence of six different odors, each of which was associated with a go or a no-go response [71]. Although the identities and reward contingency of odors within a sequence changed in each loop of a behavioral session, the authors found that OFC neural ensembles formed generalized representations of individual odors within a sequence, which seems to facilitate the animal’s learning of a new odor sequence and corresponding choice responses. This result implies that the OFC parsed a task into relevant states and mapped their positions in an abstract task sequence. Similar results have been observed in fMRI studies involving human subjects performing a task involving multiple states with defined state transition rules [72]. Therefore, clarifying how the rules of navigational tasks are encoded in the brain and used for deciding the goal location will provide a holistic view of the OFC’s function across behaviors. 

## Conclusions 

Successful execution of goal-directed navigation requires a set of multilevel computational processes to be combined as a coherent sequence of actions, like a cognitive jigsaw puzzle that has kept attracting many neuroscientists’ interests over a century. The pieces of this puzzle have been slowly filled since Tolman’s cognitive map hypothesis through bouts of major discoveries, including the identification of spatially tuned neurons in the hippocampus and parahippocampal cortices. We propose that another major piece of the puzzle has been filled by the recent discoveries on the OFC’s functions, such as prospective coding of navigational goals, neural correlates of value-based decisionmaking, and the formation of an internal model of task structure. These results open up new research questions, some of which we have highlighted here. Further investigations on the OFC’s role in navigation will give us many insights into neural mechanisms deeper into our internal deliberation process, for example, how we choose a particular goal, how we can obtain a sense of the distance and direction of an unseen goal far from us, and how this goal representation interacts with the brain’s internal map to generate a seamless route plan to a desired destination even before initiating behaviors. 

## Declaration of competing interest 

The authors declare that they have no competing financial or other interests that could affect the discussion presented in this article. 

## Data availability 

No data was generated for the research described in the article. 

## Acknowledgements 

We thank the members of Basu lab and Ito lab for discussions. This work was supported by the Max Planck Society, the European Research Council (‘NavigationCircuits’ Grant Agreement no. 714642), the Alexander von Humboldt Foundation (Postdoctoral Research Fellowship), and startup grant from the Hebrew University of Jerusalem. 

## References 

Papers of particular interest, published within the period of review, have been highlighted as: 

- of special interest 

- * * of outstanding interest 

1. Tolman EC, Ritchie BF, Kalish D: Studies in spatial learning. I. Orientation and the short-cut. J Exp Psychol 1946, 36:13–24. 

2. Tolman EC: Cognitive maps in rats and men.pdf. Psychol Rev 1948, 55:189–208. 

3. O’Keefe J, Dostrovsky J: The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res 1971, 34:171–175. 

4. Hafting T, Fyhn M, Molden S, Moser M-B, Moser EI: Microstructure of a spatial map in the entorhinal cortex. Nature 2005, 436:801–806. 

5. Wilson M, McNaughton B: Dynamics of the hippocampal ensemble code for space. Science 1993, 261:1055–1058. 

6. Pfeiffer BE, Foster DJ: Hippocampal place-cell sequences depict future paths to remembered goals. Nature 2013, 497: 74–79. 

7. Waaga T, Agmon H, Normand VA, Nagelhus A, Gardner RJ, Moser M-B, Moser EI, Burak Y: Grid-cell modules remain coordinated when neural activity is dissociated from external sensory cues. Neuron 2022, https://doi.org/10.1016/ j.neuron.2022.03.011. 

8. Morris RGM: Distinctive computations and relevant associative processes: hippocampal role in processing, retrieval, but not storage of allocentric spatial memory. Hippocampus 1991, 1:287–290. 

9. Hollup SA, Molden S, Donnett JG, Moser M-B, Moser EI: Accumulation of hippocampal place fields at the goal location in an annular watermaze task. J Neurosci 2001, 21:1635–1644. 

10. Lee JS, Briguglio JJ, Cohen JD, Romani S, Lee AK: The statistical structure of the hippocampal code for space as a function of time, context, and value. Cell 2020, 183:620–635.e22. 

- 11* . Grienbergerrelated changesC, Mageein CA1JC:representationsEntorhinal cortex. Naturedirects2022,learning-611: 554–562. 

This study provides a mechanistic underpinning of place cell clustering near reward locations. Using two-photon calcium imaging of CA1 neuron cell bodies as well as the incoming axonal boutons from neurons in layer 3 of the entorhinal cortex (EC3), the authors demonstrated that the correlation between individual EC3 bouton activities increased near a reward location. This enhanced input correlation further acts as an instructive signal to induce behavioral timescale synaptic plasticity in CA1 neurons, resulting in the formation of place cells. 

12. Dupret D, O’Neill J, Pleydell-Bouverie B, Csicsvari J: The reorganization and reactivation of hippocampal maps predict spatial memory performance. Nat Neurosci 2010, 13: 995–1002. 

13. Boccara CN, Nardin M, Stella F, O’Neill J, Csicsvari J: The entorhinal cognitive map is attracted to goals. Science 2019, 363:1443–1447. 

14. Butler WN, Hardcastle K, Giocomo LM: Remembered reward locations restructure entorhinal spatial maps. Science 2019, 363:1447–1452. 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

A goal map in the brain Basu and Ito 9 

15. Gauthier JL, Tank DW: A dedicated population for reward coding in the Hippocampus. Neuron 2018, 99:179–193.e7. 

- 16* . RobinsonBicknell BA,NTM,AntonovDescampsGK, LauLAL,JYN,RussellNutbrownLE, BuchholzR, Schmidt-MO, Hieber C, Häusser M: Targeted activation of hippocampal place cells drives memory-guided spatial behavior. Cell 2020, https://doi.org/10.1016/j.cell.2020.09.061. 

This study demonstrated that, when hippocampal CA1 neurons that fire near the reward location were optogenetically activated midway during the journey, the animal slowed down and displayed consummatory behavior. These results point towards the functional role of the rewardsite overrepresentation in the hippocampus in eliciting anticipatory behavior associated with reward consumption. 

17. Wikenheiser AM, Redish AD: Hippocampal theta sequences reflect current goals. Nat Neurosci 2015, 18:289–294. 

18. Wang M, Foster DJ, Pfeiffer BE: Alternating sequences of future and past behavior encoded within hippocampal theta oscillations. Science 2020, 370:247–250. 

19. Carey AA, Tanaka Y, van der Meer MAA: Reward revaluation biases hippocampal replay content away from the preferred outcome. Nat Neurosci 2019, 22:1450–1459. 

20. Gillespie AK, Astudillo Maya DA, Denovellis EL, Liu DF, Kastner DB, Coulter ME, Roumis DK, Eden UT, Frank LM: Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice. Neuron 2021, 109: 3149–3163.e6. 

21. Jiang W-C, Xu S, Dudman JT: Hippocampal representations of foraging trajectories depend upon spatial context. Nat Neurosci 2022, 25:1693–1705. 

22. Kay K, Chung JE, Sosa M, Schor JS, Karlsson MP, Larkin MC, Liu DF, Frank LM: Constant sub-second cycling between representations of possible futures in the Hippocampus. Cell 2020, 180:552–567.e25. 

23. Sarel A, Finkelstein A, Las L, Ulanovsky N: Vectorial representation of spatial goals in the hippocampus of bats. Science 2017, 355:176–180. 

- 24* . Ormond J, O’Keefe J: Hippocampal place cells have goaloriented vector fields during navigation. Nature 2022, 607: 741–746. 

Thistuned to a neuron-specificstudy demonstrates that ’sinkrodent’ location in the environment that is oftenhippocampal CA1 place cells are locatedmaze withclosea ’honeycombto the goal.’Thesepattern,experimentsin which anwereanimalconducted’s goal-directedusing a trajectory is discretized through a series of binary choices. At each choice point, a place cell exhibits peak firing when the animal faces its sink location. Hence a population of such neurons can continuously monitor the direction towards the goal even when the animal undertakes a tortuous path. 

25. Wood ER, Dudchenko PA, Robitsek RJ, Eichenbaum H: Hippocampal neurons encode information about different types of memory episodes occurring in the same location. Neuron 2000, 27:623–633. 

26. Frank LM, Brown EN, Wilson M: Trajectory encoding in the Hippocampus and entorhinal cortex. Neuron 2000, 27: 169–178. 

27. Ito HT, Zhang S-J, Witter MP, Moser EI, Moser M-B: A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation. Nature 2015, 522:50–55. 

28. Grieves RM, Wood ER, Dudchenko PA: Place cells on a maze encode routes rather than destinations. Elife 2016, 5, e15986. 

29. Foster DJ, Morris RGM, Dayan P: A model of hippocampally dependent navigation, using the temporal difference learning rule. Hippocampus 2000, 10:1–16. 

30. Bush D, Barry C, Manson D, Burgess N: Using grid cells for navigation. Neuron 2015, 87:507–520. 

31. Rueckert E, Kappel D, Tanneberg D, Pecevski D, Peters J: Recurrent spiking networks solve planning tasks. Sci Rep 2016, 6:21142. 

32. Russek EM, Momennejad I, Botvinick MM, Gershman SJ, Daw ND: Predictive representations can link model-based 

   - reinforcement learning to model-free mechanisms. PLoS Comput Biol 2017, 13, e1005768. 

33. Dayan P: Improving generalisation for temporal difference learning: the successor representation. Neural Comput 1993, 5:613–624. 

34. Stachenfeld KL, Botvinick MM, Gershman SJ: The hippocampus as a predictive map. Nat Neurosci 2017, 20:1643–1653. 

35. Ciaramelli E: The role of ventromedial prefrontal cortex in navigation: a case of impaired wayfinding and rehabilitation. Neuropsychologia 2008, 46:2099–2105. 

36. Vafaei AA, Rashidy-Pour A: Reversible lesion of the rat’s orbitofrontal cortex interferes with hippocampus-dependent spatial memory. Behav Brain Res 2004, 149:61–68. 

37. Lipton PA, Alvarez P, Eichenbaum H: Crossmodal associative memory representations in rodent orbitofrontal cortex. Neuron 1999, 22:349–359. 

38. Feierstein CE, Quirk MC, Uchida N, Sosulski DL, Mainen ZF: Representation of spatial goals in rat orbitofrontal cortex. Neuron 2006, 51:495–507. 

39. Stalnaker TA, Cooch NK, McDannald MA, Liu T-L, Wied H, Schoenbaum G: Orbitofrontal neurons infer the value and identity of predicted outcomes. Nat Commun 2014, 5:3926. 

40. Wikenheiser AM, Marrero-Garcia Y, Schoenbaum G: Suppression of ventral hippocampal output impairs integrated orbitofrontal encoding of task structure. Neuron 2017, 95: 1197–1207.e3. 

41. Riceberg JS, Shapiro ML: Orbitofrontal cortex signals expected outcomes with predictive codes when stable contingencies promote the integration of reward history. J Neurosci 2017, 37:2010–2021. 

42. Brown TI, Carr VA, LaRocque KF, Favila SE, Gordon AM, Bowles B, Bailenson JN, Wagner AD: Prospective representation of navigational goals in the human hippocampus. Science 2016, 352:1323–1326. 

43. John ER: A neurophysiological model of purposive behavior. In Neural mechanisms of goal-directed behavior and learning. Elsevier; 1980:93–115. 

44. Basu R, Gebauer R, Herfurth T, Kolb S, Golipour Z, * * Tchumatchenko T, Ito HT: The orbitofrontal cortex maps future navigational goals. Nature 2021, https://doi.org/10.1038/ s41586-021-04042-9. 

Using a task design that requires continuous goal updating, this study identified a brain region that represents a future goal location persistently throughout navigation. This goal representation in the orbitofrontal cortex (OFC) originates prior to the onset of navigation and remainsmal’s journey.undeterredFurther,by locationsoptogeneticencounteredperturbationmidwayof OFCduringactivitythe ani-at navigationsupporting onsetthe causalcausedroletheofanimalOFC intodeterminingnavigate to incorrectthe animallocations,’s future destination. 

45. Campagner D, Vale R, Tan YL, Iordanidou P, Pavón Arocas O, * * Claudi F, Stempel AV, Keshavarzi S, Petersen RS, Margrie TW, et al.: A cortico-collicular circuit for orienting to shelter during escape. Nature 2023, 613:111–119. 

This study identified the neural mechanisms underlying mammalian escape behavior towards a shelter. Using a threat escape task, the authors report that neurons in the retrosplenial cortex, and its downstream subcortical target superior colliculus, are tuned to the direction of the shelter location. Furthermore, chemogenetic silencing of superior colliculus projecting retrosplenial neurons resulted in incorrect orientation to the shelter, implying the necessity of this circuit in shelterdirected navigation during the escape. 

46. Spellman T, Rigotti M, Ahmari SE, Fusi S, Gogos JA, Gordon JA: Hippocampal–prefrontal input supports spatial encoding in working memory. Nature 2015, 522:309–314. 

47. Fujisawa S, Amarasingham A, Harrison MT, Buzsáki G: Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. Nat Neurosci 2008, 11:823–833. 

48. Hok V, Save E, Lenck-Santini PP, Poucet B: Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex. Proc Natl Acad Sci USA 2005, 102:4602–4607. 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

10 Computational Neuroscience 2023 

49. Böhm C, Lee AK: Canonical goal-selective representations are * * absent from prefrontal cortex in a spatial working memory task requiring behavioral flexibility. Elife 2020, 9, e63035. 

Using a novel task design to uncouple goal representation from route planning, the authors show that the goal location cannot be decoded from ensemble neural activity in the medial prefrontal cortex, either at the onset of navigation or midway during the journey. 

50. Esteves IM, Chang H, Neumann AR, Sun J, Mohajerani MH, McNaughton BL: Spatial information encoding across multiple neocortical regions depends on an intact Hippocampus. J Neurosci 2021, 41:307–319. 

51. Bota A, Goto A, Tsukamoto S, Schmidt A, Wolf F, Luchetti A, Nakai J, Hirase H, Hayashi Y: Shared and unique properties of place cells in anterior cingulate cortex and hippocampus. bioRxiv 2021. 

52. Poo C, Agarwal G, Bonacchi N, Mainen ZF: Spatial maps in piriform cortex during olfactory navigation. Nature 2021, 601: 595–599. 

53. Murphy MJM, Deutch AY: Organization of afferents to the orbitofrontal cortex in the rat. J Comp Neurol 2018, 526: 1498–1526. 

54. Hoover WB, Vertes RP: Projections of the medial orbital and ventral orbital cortex in the rat. J Comp Neurol 2011, 519: 3766–3801. 

55. Menegas W, Bergan JF, Ogawa SK, Isogai Y, Umadevi Venkataraju K, Osten P, Uchida N, Watabe-Uchida M: Dopamine neurons projecting to the posterior striatum form an anatomically distinct subclass. Elife 2015, 4, e10032. 

56. Rudebeck PH, Mitz AR, Chacko RV, Murray EA: Effects of amygdala lesions on reward-value coding in orbital and medial prefrontal cortex. Neuron 2013, 80:1519–1531. 

57. Erdem UM, Hasselmo M: A goal-directed spatial navigation model using forward trajectory planning based on grid cells: forward linear look-ahead trajectory model. Eur J Neurosci 2012, 35:916–931. 

58. Murray EA, Rudebeck PH: Specializations for reward-guided decision-making in the primate ventral prefrontal cortex. Nat Rev Neurosci 2018, 19:404–417. 

59. Fellows LK: Orbitofrontal contributions to value-based decision making: evidence from humans with frontal lobe damage: the human frontal lobes in choice and learning. Ann N Y Acad Sci 2011, 1239:51–58. 

60. Rich EL, Wallis JD: Decoding subjective decisions from orbitofrontal cortex. Nat Neurosci 2016, 19:973–980. 

61. Cai X, Padoa-Schioppa C: Contributions of orbitofrontal and lateral prefrontal cortices to economic choice and the goodto-action transformation. Neuron 2014, 81:1140–1151. 

62. Padoa-Schioppa C, Assad JA: Neurons in the orbitofrontal cortex encode economic value. Nature 2006, 441:223–226. 

63. Tremblay L, Schultz W: Relative reward preference in primate orbitofrontal cortex. Nature 1999, 398:704–708. 

64. Kepecs A, Uchida N, Zariwala HA, Mainen ZF: Neural correlates, computation and behavioural impact of decision confidence. Nature 2008, 455:227–231. 

65. Hirokawa J, Vaughan A, Masset P, Ott T, Kepecs A: Frontal cortex neuron types categorically encode single decision variables. Nature 2019, 576:446–451. 

66. Masset P, Ott T, Lak A, Hirokawa J, Kepecs A: Behavior- and modality-general representation of confidence in orbitofrontal cortex. Cell 2020, 182:112–126.e18. 

67. Walton ME, Behrens TEJ, Buckley MJ, Rudebeck PH, Rushworth MFS: Separable learning systems in the macaque brain and the role of orbitofrontal cortex in contingent learning. Neuron 2010, 65:927–939. 

68. Kennerley SW, Behrens TEJ, Wallis JD: Double dissociation of value computations in orbitofrontal and anterior cingulate neurons. Nat Neurosci 2011, 14:1581–1589. 

69. Wilson RC, Takahashi YK, Schoenbaum G, Niv Y: Orbitofrontal cortex as a cognitive map of task space. Neuron 2014, 81: 267–279. 

70. Wikenheiser AM, Schoenbaum G: Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex. Nat Rev Neurosci 2016, 17:513–523. 

71. Zhou J, Jia C, Montesinos-Cartagena M, Gardner MPH, Zong W, * * Schoenbaum G: Evolving schema representations in orbitofrontal ensembles during learning. Nature 2021, 590:606–611. 

This study reports that neural ensembles in the orbitofrontal cortex (OFC) can parse a task structure into discrete states and encode the corresponding state transition rules. Using a sequence of six odors, each with different reward contingencies, the authors show that OFC ensembles can form generalized representations of odor positions in a sequence, largely invariant to the odor identities. This generalized representation was suggested to facilitate the learning of a new-odor sequence and associated choice responses. 

72. Schuck NW, Cai MB, Wilson RC, Niv Y: Human orbitofrontal cortex represents a cognitive map of state space. Neuron 2016, 91:1402–1412. 

Current Opinion in Neurobiology 2023, 83:102803 

www.sciencedirect.com 

