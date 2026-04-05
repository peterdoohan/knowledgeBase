**ll** 

## Review 

## Spatial goal coding in the hippocampal formation 

Nils Nyberg,[1][,] * E[´ ] le´ onore Duvelle,[2] Caswell Barry,[3] and Hugo J. Spiers[1][,] * 

1Institute of Behavioural Neuroscience, Department of Experimental Psychology, University College London, London, UK 

2Department of Psychological and Brain Sciences, Dartmouth College, Hanover, NH, USA 

3Department of Cell and Developmental Biology, University College London, London, UK *Correspondence: h.spiers@ucl.ac.uk (H.J.S.), nils.nyberg10@gmail.com (N.N.) https://doi.org/10.1016/j.neuron.2021.12.012 

## SUMMARY 

The mammalian hippocampal formation contains several distinct populations of neurons involved in representing self-position and orientation. These neurons, which include place, grid, head direction, and boundary cells, are thought to collectively instantiate cognitive maps supporting flexible navigation. However, to flexibly navigate, it is necessary to also maintain internal representations of goal locations, such that goaldirected routes can be planned and executed. Although it has remained unclear how the mammalian brain represents goal locations, multiple neural candidates have recently been uncovered during different phases of navigation. For example, during planning, sequential activation of spatial cells may enable simulation of future routes toward the goal. During travel, modulation of spatial cells by the prospective route, or by distance and direction to the goal, may allow maintenance of route and goal-location information, supporting navigation on an ongoing basis. As the goal is approached, an increased activation of spatial cells may enable the goal location to become distinctly represented within cognitive maps, aiding goal localization. Lastly, after arrival at the goal, sequential activation of spatial cells may represent the just-taken route, enabling route learning and evaluation. Here, we review and synthesize these and other evidence for goal coding in mammalian brains, relate the experimental findings to predictions from computational models, and discuss outstanding questions and future challenges. 

## INTRODUCTION 

## Navigating in the wild and in the laboratory 

The central purpose of spatial navigation is to arrive at a goal location. For most animals, goal locations contain rewarding resources, such as food, shelter, or mates, and although navigating between these sites can be challenging, success is crucial for survival. Animals, including mammals, which we focus on here, must therefore have evolved to overcome the unique navigation difficulties posed by their specific habitats. For instance, chimpanzees, found throughout equatorial Africa, use knowledge of their surroundings, such as the steepness of slopes and thickness of vegetation, to plan energy-efficient navigation routes (Green et al., 2019). Rats, found in most cities around the world, adaptively switch between navigation routes so as to minimize contact with humans (Byers et al., 2019). Egyptian fruit bats, inhabiting large swaths of Africa and the Middle East, rely on hills and other distal landmarks to navigate tens of kilometers in daylight but switch to echolocation to orient locally in dark feeding or roosting areas (Harten et al., 2020; Toledo et al., 2020). 

Many taxonomies for classifying navigational strategies have been proposed (e.g., Arleo and Rondi-Reig, 2007; O’Keefe and Nadel, 1978; Redish, 1999). Here, we describe four commonly described types, which are in part subserved by separate neural systems (Figure 1A, also see: "Neural systems underlying navigation"). If the goal location is immediately visible, animals simply have to orient their movement toward this site, called ‘‘beacon 

navigation’’ (Gallistel, 1990; O’Keefe and Nadel, 1978). However, if the goal location is not immediately visible, animals may in some circumstances execute learned movement responses leading to this site. Researchers occasionally distinguish between ‘‘response navigation,’’ for when a single movement response has been learned (e.g., orienting the body left or right at a single decision point) (Tolman et al., 1946a) and ‘‘sequential-egocentric navigation,’’ for when a temporally ordered sequence of movement responses has been learned (e.g., orienting the body left or right at a set of consecutively encountered decision points) (Arleo and Rondi-Reig, 2007; Rondi-Reig et al., 2006). Importantly, each movement response becomes determined either by a previous movement response or by a specific stimulus. The three strategies described so far require that the animal rely on specific viewpoint-dependent (i.e., egocentric) information, and they are therefore considered inflexible, because new learning is generally required each time the starting orientation, location, or guiding stimuli changes. In order for animals to navigate in non-constrained and flexible manner, they must instead rely on viewpoint-independent spatial relational (i.e., allocentric) knowledge of the environment, from which they can determine both the current self- and goal location and a route between these sites, called ‘‘place navigation’’ (Goodman, 2021; Tolman et al., 1946a). Although not the focus of this review, many animal species also have the ability to integrate internal self-motion information, as opposed to external perceptual information, and use this information to flexibly navigate back to a 

**==> picture [16 x 17] intentionally omitted <==**

394 Neuron 110, February 2, 2022 ª 2021 Elsevier Inc. 

**ll** 

Review 

**==> picture [46 x 35] intentionally omitted <==**

## **A** 

**==> picture [7 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>**----- End of picture text -----**<br>


**==> picture [415 x 266] intentionally omitted <==**

Figure 1. Different types of navigation and examples of spatial goal-related parameters (A) Examples of different types of navigation. Beacon navigation entails navigating toward a beacon signifying the goal location, response navigation entails navigating by following a simple learned route (e.g., making a single left-right response), sequential-egocentric navigation entails navigating by following a more complicated learned route (e.g., making a sequence of left-right responses, such as between many consecutive goal locations, example based on protocol used in Dupret et al., 2010), and place navigation entails navigating based on a constellation of distal cues that have specific spatial relations to the goal (exampled based on protocol used in Pfeiffer and Foster, 2013). Beacon, response, and sequential-egocentric navigation rely on specific egocentric spatial information (i.e., viewpoint-dependent movement responses are determined either by a previous movement or by a specific stimulus), and in the examples, the same goaldirected route is repeated across trials. Place navigation instead relies on allocentric spatial information (i.e., viewpoint-independent responses are made based on internalized spatial-relational knowledge), and in the example, different goal-directed routes need to be determined in each trial, as the hidden random reward location changes pseudorandomly across trials. 

(B) Example of different spatial parameters in relation to the current goal location, referenced to either the current head direction or an allocentric reference direction (north). Rat illustrations from scidraw.io. 

recently visited starting position, even if the environment is novel, called ‘‘path integration’’ (Barlow, 1964; Etienne and Jeffery, 2004). 

Notably, different navigation strategies can be learned in parallel and can compete for control of behavior (Arleo and RondiReig, 2007; Iglo´ i et al., 2009; Packard and McGaugh, 1996). The type of task and experience with the task can also influence the navigational strategy employed. For example, in appetitively motivated dual-choice tasks (when food is used as reward at goal), rats have been found to initially adopt a place navigation strategy but switch to a response navigation strategy as a function of experience (Packard and McGaugh, 1996). However, in similar but aversively motivated dual-choice tasks in water (where ‘‘reward’’ is a submerged escape platform offering refuge from swimming), the opposite pattern has been reported (Asem and Holland, 2013). 

Rats can also acquire allocentric knowledge of maze layouts latently, during non-reinforced exploration, and use this knowledge to guide navigation after explicit goals become introduced 

(Blodgett, 1929; Tolman and Honzik, 1930; Tolman et al., 1946b). This finding prompted Tolman (1948) to propose that mammals may form internal models of their experienced environments, so-called ‘‘cognitive maps.’’ For a cognitive map to guide navigation, it has to both represent spatial locations, including the current self- and goal locations, and the spatial relations between these sites within a common coordinate framework (O’Keefe and Nadel, 1978; Poucet, 1993). Such a framework would enable estimates of the current distance and direction to the goal. Distance to the goal can be represented in either Euclidean terms, referring to the straight-line distance between the current position and the goal, or in path terms, referring to the actual distance needed to travel to the goal taking into account detours (Figure 1B). Similarly, direction to the goal can be represented in either egocentric terms, where the goal direction is referenced relative to the current head direction, or in allocentric terms, where the goal direction is referenced relative to an allocentric direction (or, alternatively, a stable distal landmark) (Figure 1B). 

Neuron 110, February 2, 2022 395 

Review 

## **ll** 

**==> picture [419 x 284] intentionally omitted <==**

Figure 2. Standard description of connectivity and neural representation of space within the rodent hippocampal formation Illustration of main hippocampal formation (HF) circuitry in the rodent brain and the subregions where the most well-researched spatially tuned neurons were first discovered. Although the main HF is often described as a simple unidirectional network, many bidirectional and parallel projection streams exist, only some of which are shown here. In the classic ‘‘trisynaptic pathway,’’ projections from the medial and lateral entorhinal cortex (mEc and lEC) are sent to the dentate gyrus (DG), and from there to CA3 (called the ‘‘mossy fiber pathway’’), and on to CA1 (called ‘‘Schaffer collaterals’’). CA3 pyramidal cells also send direct projections to each other in a recurrent excitatory network. Besides the DG, both mEC and lEC also send direct projections to CA3, CA1 and subiculum (SUB) via the ‘‘perforant pathway.’’ CA1 in turn projects to mEC/lEC both directly and via SUB, and SUB also projects to mEC/lEC both directly and via presubiculum (PrS) and parasubiculum (PaS), closing the loop. Of note, some important projections are omitted for illustration clarity, including, but not limited to, commissural projections between hemispheres and projections to/from structures outside the HF. The circular-shaped neuron in DG illustrates a granule cell, the triangular neurons across regions illustrate pyramidal cells, and the star-shaped neurons in mEC/lEC illustrate stellate cells. Schematic inspired by Hartley et al. (2014). For place, border, and grid cells, the leftmost example illustration shows a rodent’s behavioral trajectory, with regions where the spatial cell fired overlaid as colored dots. The right illustration demonstrates the spiking activity as a heatmap, with warmer colors denoting areas of increased activity. For the head-direction cell, the left illustration shows allocentric head direction according to the four cardinal directions, and the right illustration shows the tuning of a head-direction cell according to the cardinal directions. 

The color-coded mouse brain was created using Brainrender software (Claudi et al., 2021), and the cartoon mouse head was created by the MRC Laboratory of Molecular Biology (LMB visual aids; http://www.visaids.net/) and is used with permission. 

Regardless of the strategy used to navigate, and despite the many nuanced dynamics and unexpected challenges that may occur (e.g., Patai and Spiers, 2021), all forms of navigation fundamentally consists of three core phases: (1) planning/initiating goal-directed routes, (2) traveling to the goal, and (3) arriving at the goal (including approaching and post-arrival periods) (Figure 1A). The empirical sections of this review have been structured in accordance with these phases. 

## Spatially tuned neurons in the hippocampal formation 

The hippocampal formation (HF) consists of the dentate gyrus (DG), the hippocampus proper (HPC; containing three subfields: CA1, CA2, and CA3), the subicular complex (containing three subdivisions: subiculum [SUB], presubiculum [PrS], and parasubiculum [PaS]), and the entorhinal cortex (EC; commonly divided into medial [mEC] and lateral parts) (Figure 2; Cappaert et al., 2015). See Table 1 for summaryofacronymsused throughoutthe review. 

Following the development of techniques allowing recordings of single neuron activity in freely moving rodents (e.g., Ainsworth et al., 1969; McNaughton et al., 1983), spatially tuned neurons were first discovered in the rat CA1 (specifically in dorsal CA1, which is the subregion referred to throughout this review unless otherwise specified, O’Keefe and Dostrovsky, 1971). These cells were given the name ‘‘place cells’’ as they preferentially fired within localized areas of an environment (i.e., ‘‘place fields’’; O’Keefe, 1976). As such firing patterns appear to form neural representations of allocentric locations, O’Keefe and Nadel (1978) first speculated that CA1 place cells might constitute a fundamental substrate of cognitive maps. Neurons with similar place-like properties have since been discovered throughout the HF, including in the DG (e.g., Leutgeb et al., 2007) and CA3 (e.g., Olton et al., 1978), throughout the subicular complex (e.g., Sharp and Green, 1994; Taube, 1995), and in the mEC (e.g., Fyhn et al., 2004; Quirk et al., 1992). In parallel, other types 

396 Neuron 110, February 2, 2022 

## Review 

Table 1. Acronyms used throughout the review 

|Name|Acronym|Acronym|
|---|---|---|
|Blood-oxygen-level-dependent signal|BOLD||
|Dentategyrus|DG||
|Dorsolateral and dorsomedial striatum|DLS, DMS||
|Entorhinal cortex,medial and lateral|EC,mEC,lEC||
|Functional magnetic resonance imaging<br>fMRI|||
|Hippocampal formation|HF||
|Hippocampus proper|HPC||
|Lateral septum|LS||
|Locus coeruleus|LC||
|Long-termpotentiation|LTP||
|Medial prefrontal cortex|mPFC||
|Nucleus reuniens|NR||
|Orbitofrontal cortex|OFC||
|Parasubiculum|PaS||
|Posterior parietal cortex|PPC||
|Presubiculum|PrS||
|Spike-timing dependent plasticity|STDP||
|Subiculum|SUB||
|Successor representation|SR||
|Temporal difference|TD||
|Ventral tegmental area|VTA||
||||



of spatially tuned neurons have gradually been discovered throughout the HF (Figure 2). The most researched of these, which are now believed to collectively form the backbone of cognitive mapping, include (1) ‘‘head direction cells,’’ which preferentially fire when an animal’s head faces a specific allocentric head direction (Figure 1B), originally discovered in the PrS (e.g., Taube et al., 1990a, 1990b) and later in the PaS (e.g., Tang et al., 2016) and mEC (e.g., Sargolini et al., 2006), (2) ‘‘grid cells,’’ which exhibit multiple firing fields organized in a hexagonal lattice pattern, originally discovered in the mEC (Fyhn et al., 2004; Hafting et al., 2005) and later in the PrS and PaS (Boccara et al., 2010), and (3) ‘‘boundary cells,’’ which exhibit firing fields at specific allocentric distances and directions from environmental boundaries, originally discovered in the SUB (Barry et al., 2006; Lever et al., 2009) and later in the mEC (Savelli et al., 2008; Solstad et al., 2008), PrE and PaS (Boccara et al., 2010). Despite decades of progress, we are still unearthing the full extent of spatial processing in mammalian brains, with novel spatially tuned neurons still being discovered within, as well as outside, the HF (Grieves and Jeffery, 2017; O’Mara and Aggleton, 2019). However, the spatial tuning properties of neurons outside the HF seemingly depend on an intact HPC, cementing this structure as foundational for spatial processing (e.g., Esteves et al., 2021; Mao et al., 2018). 

For the study of the human brain, in rare cases epileptic patients may need intracranial depth electrodes implanted to monitor seizures prior to surgery, and it is possible to record from such patients during navigation of virtual and real environments (Ekstrom et al., 2018). In healthy humans, neuroimaging methods such as functional magnetic resonance imaging (fMRI) 

## **ll** 

have provided important advances in our understanding of the neural correlates of navigation (Spiers and Barry, 2015). Although fMRI lacks the precision of rodent electrophysiology, it makes it possible to examine whole brain dynamics and probe participants (including HPC amnesics) about their experience and strategies (Brunec et al., 2017; Spiers and Maguire, 2006). Such studies have shown relatively consistent correspondence from rodent studies when translating tasks to humans (Epstein et al., 2017). Because fMRI provides an indirect measure of neural activity via the blood-oxygen-level-dependent (BOLD) response summed over several mm[3] of tissue, changes in dynamics are typically best considered as regional demands in processing (Logothetis et al., 2001) rather than a simple readout of the activity of principal cells in a region. Although evidence for goal codes in non-human primates is currently lacking, advances have recently been made in recording spatial correlates from such species (Mao et al., 2021; Rueckemann and Buffalo, 2017). 

## Neural systems underlying navigation 

A convergence of brain recording techniques, lesioning, and molecular/genetic approaches has determined that different navigation strategies are in part subserved by separate, albeit parallel, memory systems. Specifically, response navigation is principally supported by a habitual stimulus-response memory system dependent on the dorsolateral striatum (DLS), whereas place navigation is primarily mediated by a cognitive memory system subserved by the HPC and dorsomedial striatum (DMS) (Devan et al., 2011; Gahnstrom and Spiers, 2020; Goodman, 2021). Specifically, inactivation of the DLS in the dual-solution plus-maze task causes rats to primarily use a place strategy, whereas inactivation of the HPC or DMS causes rats to primarily use a response strategy (e.g., Jacobson et al., 2012; Packard and McGaugh, 1996; Yin and Knowlton, 2004). Similarly, lesions to HPC (e.g., Hollup et al., 2001a; Morris et al., 1982; O’Keefe et al., 1975), as well as to DMS (e.g., Devan and White, 1999; Lee et al., 2014), render rats unable to flexibly use a place strategy to locate a hidden escape platform in the Morris water maze task. More recently, it was discovered that lesions to either HPC or DMS also impaired sequential-egocentric navigation in a starmaze task with multiple sequential decision points (Fouquet et al., 2013). One interpretation is that HPC is required for organizing not just spatial but also sequential event information, in line with the purported role of this structure in spatiotemporal relational memory processes (e.g., Eichenbaum, 2017). The DMS is in turn purported to have roles in behavioral flexibility and in learning the specific actions leading to the goal (Devan et al., 2011; Goodman, 2021). Lastly, rats can still beacon navigate to a visible goal location, such as an escape platform in the water maze, following lesions to either the DLS, DMS, or HPC (Devan and White, 1999; McDonald and White, 1994). This strategy might instead be subserved by regions more directly involved in transforming egocentric visual information into action, with the posterior parietal cortex (PPC) proposed as one essential hub (e.g., Byrne et al., 2007; Wolbers et al., 2008). 

Interestingly, both rats (Winocur et al., 2005, 2010) and humans (Maguire et al., 2006; Rosenbaum et al., 2005a, 2005b; for a review, see: Squire and Wixted, 2011) with bilateral HPC 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 397 

Review 

## **ll** 

lesions occasionally retain an ability to navigate to remembered goal locations without repeating specifically learned routes but only when the environment is simple, non-dynamic, and well learned. Spatial relational knowledge consolidated to regions outside the HF may therefore, in some situations, enable a rigid ‘‘map-like’’ form of navigation, whereas the HPC remains necessary for truly flexible map-based (i.e., place) navigation (Winocur and Moscovitch, 2011). 

In this review, we present evidence across species for multiple types of goal-related codes in the HF that may guide navigation during its different phases (Figure 1A). We begin our examination by reviewing influential computational models and highlighting predictions made about goal codes, and in subsequent sections, we explore the extent to which these predictions have been supported by experimental findings. 

## THEORETICAL PREDICTIONS OF GOAL CODING 

Computational models have played an important role in linking the known properties of neurons in the HF to a role in navigation, proposing hypotheses and making predictions at both the neural and behavioral levels. Although a wide range of approaches has been deployed, the majority can be classified into one of the three broad groups: ‘‘model-free,’’ ‘‘topological,’’ and "vectorbased". Although both topological and vector-based approaches are model based (i.e., involving learning a ‘‘model’’ of the environment, such as transition probabilities between ‘‘states’’), we describe them separately here as they, in some instances, make distinct predictions. For the first group, we include approaches that use the formalism of model-free reinforcement learning (e.g., Dayan, 1991; Foster et al., 2000; Sutton and Barto, 2018) but also other approaches focusing on learning the best action to perform at a given location to reach a goal (e.g., Brown and Sharp, 1995). In the second group, we include approaches that emphasize the learned connectivity of an environment and the routes available within it (e.g., Muller et al., 1996; Recce and Harris, 1996; Stachenfeld et al., 2017). Finally, in the last group, we include approaches that make use of a map-like coordinate system to directly calculate the relative position of places in space (e.g., Banino et al., 2018; Bush et al., 2015). Although the focus, style of implementation, and biological plausibility of these approaches vary greatly, they invariably present some method to learn, or compute actions based on, the representations of the current location and goal location. It is these elements that yield the clearest predictions regarding goal codes and that we examine below and summarize in Table 2. It should be noted that although model-free approaches are often linked to egocentric-based navigation and model-based approaches to allocentric-based navigation (see: "Navigating in the wild and in the laboratory"; Figure 1), a straightforward mapping between these separate conceptual frameworks is not always possible. Most approaches also do not make specific predictions for different phases of navigation. Simple model-free approaches tend not to have a clear planning phase, as the decision about how to move is typically contingent upon the animal’s current location and so likely occurs sequentially during navigation. In contrast, topological and vector-based approaches imply some knowledge about the structure of an envi- 

ronment, meaning route planning prior to travel is possible even if individual models are often not explicit about this point. 

## Model-free predictions 

Prior to the identification of EC grid cells, models of navigation primarily focused on HPC place cells. Conceptually, the simplest of these models proposed a goal-cell implementation (e.g., Burgess and O’Keefe, 1996; Burgess et al., 1994, 1997), with each remembered goal being stored as the snapshot of place cell activity at that location. Specifically, a goal location was proposed to be memorized via the Hebbian updating of synapses between place cells active at the goal and dedicated ‘‘goal cells,’’ assumed to exist either within the HF, such as in HPC or SUB, or in other brain regions, such as the ventral striatum or prefrontal cortex. A single goal cell, or more likely a small number of goal cells, would be maximally active at each remembered goal, with activity decreasing as a function of distance from that location, resembling a large place field. Navigation would be performed by searching over the possible directions for the one that increases the activity of the goal cell(s). It has also been proposed that re-locating and accumulating place cells at goals would enable a similar gradient of activity that could be searched (Bilkey and Clearwater, 2005). A limit of these approaches is that a gradient of activity would only be maintained up to a diameter equal to the size of the largest place field, unless navigation occurs via a set of sub-goals. As an extension to their simple goal-cell model, Burgess et al. (1994, 1996) also proposed that multiple goal cells could be offset over different distances and directions from the goal, and from this population activity the current egocentric goal-vector could be determined during both mobility and immobility periods (also see vector-based predictions). 

Although simple, the goal-cell models incorporate a number of key elements shared with most other model-free treatments of navigation: place cells or other spatial cells are viewed as defining states (e.g., locations in the world) on which actions are learned without needing to know the structure of the environment. The challenge for any such system, and for navigation in general, is that reward (e.g., arrival at the goal) is temporally and spatially separated from the decisions leading to it. As such, it is not entirely trivial to decide which actions were appropriate and should be repeated in the future and which were not (i.e., the temporal credit assignment problem; Sutton and Barto, 2018). 

Dayan (1991) addressed this problem using a reinforcement learning framework and demonstrated that temporal difference (TD) learning (Sutton, 1988; Sutton and Barto, 2018) could be used to approximate the value of each location. Subsequent work developed this idea further, using place cells (Foster et al., 2000) and grid cells (Banino et al., 2018; Gustafson and Daw, 2011) as a spatial basis set (i.e., a way of dividing up space using tractable functions) on which to conduct learning. In these approaches, the value of a location (or state) was considered proportional to its proximity to reward. As such, they predict the presence of neural representations that track the distance to goals. Although in contrast to the simple models described above, this gradient can extend beyond the width of the largest field. In particular, if the spatial basis sets used are constrained 

398 Neuron 110, February 2, 2022 

Table 2. Summary of main goal codes predicted from computational models 

|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|Table 2. Summary of main goal codes predicted from computational models|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Class<br>General model type<br>Specifc examples<br>Non-local<br>goal<br>activity<br>during<br>planning<br>Neural<br>activity<br>modulated<br>by distance<br>to goal<br>Place<br>felds<br>move<br>toward<br>goal<br>Place felds<br>overrepresent<br>goal<br>Navigation<br>range<br>exceeds<br>place feld<br>diameter<br>Vector<br>based<br>navigation<br>Novel<br>shortcut<br>Indirect<br>routes<br>Notes|||||||||||||||||||||||
|Model free<br>Goal cell<br>Burgess et al., 1994;<br>Burgess and O’Keefe,<br>1996;<br>Bilkey and Clearwater,<br>2005<br>X<br>U<br>X/U<br>U<br>X<br>X/U<br>X<br>?<br>Goal cells would be<br>indistinguishable from place<br>cells at goal. Revised model<br>allows vector-based<br>navigation.<br>Model-free RL<br>Dayan, 1991;Foster<br>et al., 2000;Gustafson<br>and Daw, 2011<br>X/U<br>U<br>X<br>X/U<br>U<br>X<br>X<br>U<br>Reward prediction signal<br>would resemble a large place<br>feld centered at goal. Inclusion<br>of Dyna architecture allows<br>for non-local resampling of<br>remote routes.<br>‘‘Flexible’’ stimulus-<br>response model<br>Brown and Sharp, 1995<br>X<br>X<br>X<br>X<br>U<br>X<br>X<br>U|||||||||||||||||||||||
|Topological Resistive grid<br>Muller et al., 1996<br>U<br>X<br>X<br>X<br>U<br>X<br>X<br>U<br>Successor<br>representation<br>Stachenfeld et al., 2017;<br>Momennejad and<br>Howard, 2018;de Cothi<br>and Barry, 2020;<br>Geerts et al., 2020<br>X<br>X<br>?<br>?<br>X/U<br>X<br>X<br>U<br>SR can lead to over-<br>representation of commonly<br>visited locations, but generally,<br>felds are anticipatory. Note<br>in simple formulation place<br>felds are the successor<br>features and navigation<br>range is limited.<br>Allo - egocentric<br>attractor<br>Recce and Harris, 1996<br>?<br>?<br>X<br>X<br>U<br>X<br>X<br>U<br>Search algorithm is not<br>biologically plausible.|||||||||||||||||||||||
|Vector<br>based<br>Grid cell - deep<br>network<br>Banino et al., 2018<br>X<br>U<br>X<br>X<br>U<br>U<br>U<br>U<br>Full model tracks value of<br>current state and is capable<br>of indirect navigation.<br>Grid cell - vector<br>computation<br>Bush et al., 2015;<br>Erdem and Hasselmo,<br>2012,2014;<br>Kubie and Fenton, 2012;<br>Masson and Girard, 2011<br>X/U<br>X/U<br>X<br>X<br>U<br>U<br>U<br>X/U<br>Some formulations would<br>exhibit ‘‘replay’’ and/or activity<br>proportional to goal distance.<br>Others (e.g.,Erdem and<br>Hasselmo, 2012) can traverse<br>indirect routes by setting<br>sub goals.<br>Hybrid - grid & place<br>cells allow vector &<br>topological navigation<br>Edvardsen et al., 2020<br>U<br>X<br>X<br>X<br>U<br>U<br>U<br>U<br>Hybrid of vector based and<br>topological models. Subgoals<br>used to reach indirect goals.|||||||||||||||||||||||
||||||||||||||||||||||||



**==> picture [35 x 46] intentionally omitted <==**

Review 

## **ll** 

by barriers, similarly to place fields, then this representation would likely follow the path distance to the goal (Gustafson and Daw, 2011) as opposed to the Euclidean distance (Banino et al., 2018). A plausible implementation of such a signal would be neurons that ramp their firing rates as the animal approaches a reward location. However, less clear is the precise neural substrate of such a value representation. Foster et al. (2000) suggested a structure outside of the HPC, whereas others did not commit to a specific location (Banino et al., 2018; Dayan, 1991; Gustafson and Daw, 2011). Still, the anatomical constraints are likely to be similar to those described for goal-cell models, with much of the HF and its immediate cortical targets being plausible loci. 

Although a value function alone can be used as a basis on which to conduct gradient ascent, reinforcement-learning models typically assume that animals learn a movement policy to control efficient navigation. For example, Foster et al. (2000) suggested the ‘‘actor’’ (the component of the algorithm learning which action to take in a given position) was instantiated in dorsal striatal networks, a view also supported by more recent models (Geerts et al., 2020). Albeit not formally a reinforcement-learning model, Brown and Sharp (1995) described an alternative framework whereby, after encountering a goal, a temporally decaying learning rule would strengthen recently active synapses between place and head-direction cells in the HF on the one hand, and ‘‘motor’’ cells in the ventral striatum on the other hand, reinforcing recent behaviors (for a similar implementation, see McNaughton, 1989). Although the actor would likely be presumed distinct from any value function and exist outside the HPC, these points are not made explicit. 

Model-free approaches are often criticized as being data inefficient and inflexible, as new navigational rules must be relearned for each goal given that there is no latent learning, which requires slow trial-and-error exploration (Sutton and Barto, 2018). Whereas topologic and vector-based approaches explicitly address this shortcoming, some authors have dealt with the issue by coupling model-free and other approaches (Geerts et al., 2020) or by using TD-learning to capture information about the environmental structure (Foster et al., 2000). For the most part these advances do not make materially different predictions about goal representations. However, the Dyna algorithm (Sutton, 1991) stands out, as it provides a facility for animals or agents to learn by simulation, effectively resampling from previous experiences. Applied to navigational tasks this resampling would plausibly resemble activation of sequences of place cells (Dayan, 1991; Mattar and Daw, 2018; Momennejad, 2020; Momennejad et al., 2017; similar to ‘‘replay,’’ described in: "Representation of prospective goal-directed routes by hippocampal replay"). 

## Topological predictions 

Overlaps between adjacent place fields can convey information about the connectedness of locations and describe the topology of environments, which has been exploited by a number of models. Two components are typically emphasized: (1) a mechanism to retain information about the overlap between spatial cells (usually place cells) and (2) a means to interrogate the learned connectivity to plan goal-directed routes. For example, 

Muller et al. (1996) identified the recurrent connectivity of place cells in CA3 (Figure 2) as a plausible substrate for such computations. Specifically, during exploration of an environment, longterm potentiation (LTP, Bliss and Lomo, 1973) between place cells with overlapping fields was proposed to capture information about available routes, allowing a ‘‘cognitive graph’’ to be built where each node consists of a different place cell. These graphs could then be searched for an optimal path between any nodes that represent locations in the environment. The authors speculated that sharp-wave ripples (SWRs, a distinct oscillatory pattern in the HPC local-field potential, see: "Representation of prospective goal-directed routes by hippocampal replay"), which had yet to be identified with replay, might provide a mechanism by which that activity could spread along, and select, potential routes. Thus, the most obvious hallmarks of this framework would be goal-centered activity during planning and potentially other phases of navigation, as well as reactivations moving away from the goal. A shortcoming is that a route must have been experienced before being considered as an option, excluding the possibility of novel shortcuts and detours. The potential for CA3 recurrents to capture topological information has not been overlooked by other authors. Blum and Abbott (1996) suggested that as animals repeat trajectories toward a goal, plasticity between place cells in CA3 would cause their ensemble activity to shift away from the current location, providing prospective spatial representations toward the goal, with comparison between shifted CA3 and non-shifted CA1 place fields guiding navigation behavior. Redish and Touretzky (1998) formulated a model using spike-timing-dependent plasticity (STDP, Bi and Poo, 1998) between CA3 cells to store directed graphs, proposing that the replay would favor potentiated routes leading to goals and that SUB would host a goal proximity code. Similar approaches have been proposed elsewhere (e.g., Recce and Harris, 1996). 

A convergent line of thinking has developed from the reinforcement-learning field. Dayan (1993) proposed the successor representation (SR) as an approach where the long-run transitions statistics between states might be learned separately from rewards, yielding some of the flexibility of model-based learning but with reduced complexity, similar to model-free approaches (Gershman, 2018; Momennejad and Howard, 2018). Applied to a spatial setting (de Cothi and Barry, 2020; de Cothi et al., 2021; Stachenfeld et al., 2017; Whittington et al., 2020), the SR learns about the transition probabilities between locations. Although formally distinct, applied in this way to produce a predictive map (Stachenfeld et al., 2017), the SR shares three commonalities with topological models such as cognitive graphs: (1) learn transitions during exploration, (2) resemble place fields, and (3) can be used as a basis on which to plan routes between states. Hence, where paths skirt around barriers or objects, the SR generates plausible place fields that conform to environmental boundaries. 

More generally, this framework posits that HPC activity represents a prediction of an animal’s future state (Momennejad, 2020; Momennejad and Howard, 2018; Stachenfeld et al., 2017). Thus, at least during situations when future states can be reliably predicted, such as in simplified track-based tasks, place fields are expected to disambiguate intersecting paths, 

400 Neuron 110, February 2, 2022 

## Review 

become increasingly prospective during runs toward a goal location (e.g., activity skewed opposite the direction of travel, with increased activity as the goal is approached), and cluster around goal locations or other commonly visited locations. Beyond this, the SR framework also describes how spatially periodic patterns, resembling grid cells, can be generated through the Eigen decomposition of the learned transition matrix (Stachenfeld et al., 2017). Notably, the grid patterns would exhibit distortions commensurate with the place fields, and be distorted by environmental features, which in turn would enable predictions about biases in spatial behaviors (Bellmund et al., 2020). Dyna implementations (Mattar and Daw, 2018; Momennejad, 2020; Sutton, 1991) have also been applied to a SR framework and, similar to model-free systems, predict replay-like reactivations that may potentially favor goal locations (Russek et al., 2017). 

Hybrid implementations incorporating distinct elements of model-free and topology-based approaches have also been proposed. Although combined approaches can generate more sophisticated behaviors, their neural characteristics are not materially different from those of more simplistic systems. For example, Geerts et al. (2020) described a system in which model-free TD-based learning occurs in the DLS, enabling egocentric navigation, whereas SR-based learning occurs in the HPC with place cells representing transition statistics, enabling allocentric navigation. 

## Vector-based predictions 

A system enabling truly flexible navigation must incorporate information beyond the topology of an environment by also describing the spatial relations between places. A considerable number of models have proposed that the regular spatially periodic activity of EC grid cells can form a neural correlate for such a spatial metric (e.g., Banino et al., 2018; Bush et al., 2015; Erdem and Hasselmo, 2012, 2014; Fiete et al., 2008; Kubie and Fenton, 2012; Masson and Girard, 2011). However, because earlier models typically looked to HPC place cells as a substrate on which to conduct vector-based navigation, we turn to these first. 

A vector-based navigation system must be able to determine the heading vector between an animal’s current location and a remembered goal (Bush et al., 2015). Hence, almost all such models predict that, following some form of neural computation, the system will come to represent a goal-directed Euclidean vector that cuts across environmental barriers. The challenge for models based on place cells is that although their ensemble activity can capture information about topology, the irregularity of their firing fields suggests that they do not explicitly form a coordinate system. To address this issue, O’Keefe (1990, 1991) proposed that place cells, via input elicited from different visual cues, could enable an allocentric centroid location to be determined, defined as the average of the egocentric vectors between the cues and the animal’s current location. Different locations in the environment would be stored as matrices of centroid-related place cell firing, and translations between these matrices computed via vector algebra. However, where and how such calculations take place are not made explicit. 

More recent models have focused on grid cells, which convey information about the relative positions of points in space. Grid cells are organized into functional modules that share the 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


same scale (distance between the fields) and orientation (tilt of the grid relative to a reference axis) but with different phases (displacement of the fields in x and y directions relative to a reference point; Hafting et al., 2005; Stensola et al., 2012). Therefore, within some range defined by the number of distinct grid modules and their relative scales, it is theoretically possible to determine the spatial vector between two locations by comparing their grid population codes (Banino et al., 2018; Bush et al., 2015; Fiete et al., 2008; Kubie and Fenton, 2012; Masson and Girard, 2011; Stemmler et al., 2015). 

It has been suggested that grid codes can be multifaceted, sometimes representing the current location and sometimes the intended goal location (Bush et al., 2015), or these representations might be split between different grid-cell populations (Banino et al., 2018). However, less clear is how the grid codes for these locations become compared. Bush et al. (2015) proposed several implementations, ranging from storing and using a simple but inefficient ‘‘table’’ of all possible vectorial combinations to more complex methods allowing a vector between the current self- and goal location to gradually accumulate. Respectively, these would predict the presence of cell populations that represent specific distances and directions to a goal, located either within the EC itself or in downstream structures such as the HPC (Figure 2), or neurons with activity that ramps when the goal is displaced in a specific direction. Alternatively, a sequential search process, potentially resembling replay (see: "Representation of prospective goal-directed routes by hippocampal replay") through grid cells, might provide an appropriate mechanism to determine goal distance (Bush et al., 2015). 

Notably, the role of grid cells as a substrate for vector-based navigation was recently tested using deep reinforcement learning (Banino et al., 2018). An agent endowed with grid-like representations was shown to exhibit flexible navigation, including taking novel shortcuts. Analysis of the network revealed activity that correlated with the Euclidean distance and allocentric direction to the goal, intimating that a similar analysis might reveal the presence of equivalent computations in real grid cells. 

Grid-cell networks are widely held to play a role in updating a representation of self-location based on movement vectors (i.e., path integration). Some models have adopted a similar approach to simulate the planning phase of navigation, where the model searches potential heading vectors for one that leads to a goal (Erdem and Hasselmo, 2012, 2014; Kubie and Fenton, 2012). Essentially, activity would be driven out from the animal’s current location by applying constant high velocity movement vectors to the grid-cell network, incrementally searching over directions until the goal is encountered. Furthermore, in this approach, HPC place cells have been proposed as the likely substrate in which the comparison between simulated trajectories and the goal location would be checked (Erdem and Hasselmo, 2012, 2014). Conceivably, the process could also run in the opposite direction, moving out from the goal until the current location is encountered. Either way, network activity would likely resemble replay (see: "Representation of prospective goal-directed routes by hippocampal replay") or theta sweeps (see: "Route deliberation and maintenance by hippocampal theta sequences during travel") in both EC and HPC networks. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 401 

Review 

## **ll** 

Recently, Edvardsen et al. (2020) described a hybrid model able to use grid-cell-based vector navigation to transit across open spaces while relying on a topological strategy dependent on boundary cells and place cells to bypass obstacles. As with other hybrid models, the neurobiological predictions generated by the model are not overly distinct from the non-hybrid models. However, the authors emphasized that this combined strategy would enable interim goals to be defined, such that a direct vector could be followed to the edge of an obstruction before continuing on to the main goal, and similar approaches had been noted elsewhere (Erdem and Hasselmo, 2012, 2014; Kubie and Fenton, 2012). 

A summary of some of the main predictions of goal codes discussed here can be found in Table 2. In the next sections, we present recent experimental evidence for some of these predictions. 

## PHASE I: PLANNING/INITIATING ROUTE TO GOAL 

In the first phase of navigation, a route toward the goal must be planned, or a learned movement response retrieved and initiated. Here, we primarily discuss evidence for planning, and in this and subsequent sections we begin by discussing animal studies, which make up the majority of navigation studies, before discussing complementary evidence from human studies. As discussed in the preceding sections, some models have predicted activation of non-local goal-related information during planning (Table 2), and we discuss experimental evidence for such predictions below. 

## Representation of prospective goal-directed routes by hippocampal replay 

During sleep or awake pauses, place cell ensembles in the rodent CA1 become active in temporally compressed sequences that can representroutes through the environment(Foster andWilson, 2006; Wilson and McNaughton, 1994; for reviews, see O[´ ] lafsdo´ ttir et al., 2018; Pfeiffer, 2020). The represented routes can occur either along previously experienced space, termed "replay" (e.g., Foster and Wilson, 2006; Louie and Wilson, 2001), or along yet-to-be experienced space, termed ‘‘preplay’’ (e.g., Dragoi and Tonegawa, 2011; Grosmark and Buzsa´ ki, 2016; O[´ ] lafsdo´ ttir et al., 2015). In paradigms where spatial cells have different field activity depending on the direction of travel, such as often occurs when stereotyped trajectories become repeated (Markus et al., 1995), replay or preplay events can be classified as occurring either in the same (‘‘forward’’) or opposite (‘‘reverse’’) direction relative to experience. The term ‘‘reactivations’’ can refer to replay events but also other events that are not necessarily spatially ordered (for clarity on definitions, see: Genzel et al., 2020). 

Replay typically coincides with SWRs, which can be recorded along the trisynaptic pathway (Figure 2) and consist of �0.01– 3 Hz ‘‘sharp waves,’’ likely originating from the recurrent connectivity of CA3 (Figure 2) and �110–250 Hz ‘‘ripples,’’ which may be locally generated in CA1 (Buzsa´ ki, 2015; O’Keefe and Nadel, 1978). Although replay events have been primarily defined in CA1, their informational content fidelity depends on input from both CA2 (He et al., 2021) and CA3 (Middleton and McHugh, 2016; Nakashiba et al., 2009). Coordinated replay events have 

also been reported between CA1 and the medial prefrontal cortex (mPFC; Shin et al., 2019; Tang et al., 2017) and visual cortex (Ji and Wilson, 2007), suggesting that replay-related mnemonic functions are distributed throughout hippocampo-cortical circuits. 

Planning may or may not involve deliberation, whereby different possible routes toward one or more goals become considered, and some studies have suggested that this process may be reflected in replay events. However, current empirical evidence for a role of replay in planning (with or without deliberation) is inconclusive. A classic study with rats running back and forth on a simple linear track with reward at each end found an increase of forward replay before the initiation of a new lap (Diba and Buzsa´ ki, 2007). However, as the linear track required no spatial choice, the planning demand was low, and the forward replay may therefore have reflected other anticipatory or mnemonic functions. Indeed, evidence from more recent studies using mazes with more than one route option suggests that the relationship between replay and upcoming behavior is not always simple. For example, one study using a W-maze spatial alternation task reported that during correct trials, replay at the center decision point was biased toward the upcoming route after performance was high (>85% correct performance) (Singer et al., 2013). However, this was not replicated in a recent study using the same task, which instead found that replay events at the center decision point represented both the correct and incorrect choice in an unbiased manner (Shin et al., 2019). One possibility is that this pattern reflected route deliberation, a notion supported by the fact that optogenetically disrupting SWRs (and thus presumably replay) at the center decision point causes performance deficits while leaving place-cell activity intact (Jadhav et al., 2012). Shin et al. (2019) also reported that the coherence between replay events in CA1 and mPFC increased when the correct past and future routes became replayed and that the strength of the coherence correlated with task performance. One interpretation of this finding is that mPFC might make the final planning decision, based on both retrospective and prospective information provided by the HPC (Patai and Spiers, 2021). 

In a clearer example of how replay might be involved in planning, rats navigating an eight-arm maze task were found to replay the correct future route in a forward order when at the central decision platform (Xu et al., 2019). Interestingly, this only occurred when the rats had to memorize and move between the goal arms by avoiding the non-goal arms and not when access to the non-goal arms was blocked, which lifted the memory requirement. In addition, on error trials, replay no longer represented the future behavior, suggesting that this activity was related to correct performance. A similar finding has been reported using an open field task, where rats alternated between goal-directed navigation to a remembered ‘‘home’’ well (which remained constant within a session but changed across sessions) and random foraging for a random reward well (which changed location following each visit to the home well) (Figure 3A; Pfeiffer and Foster, 2013). Replay events at the random reward wells preferentially represented routes that ended at the home well, and these routes had a significantly higher correspondence with the rats’ actual future behavior (i.e., began close to the rats’ current location and ended close 

402 Neuron 110, February 2, 2022 

**ll** 

Review 

**==> picture [7 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>**----- End of picture text -----**<br>


**==> picture [405 x 251] intentionally omitted <==**

**==> picture [46 x 35] intentionally omitted <==**

Figure 3. Hippocampal replay can reflect both the future and non-future goal route (A) Left and middle: illustration of the maze and task used by Pfeiffer and Foster (2013). Rats had to continuously switch between flexible navigation to a remembered and rewarded goal location and random foraging for a randomly rewarded location. Replay events at the randomly rewarded locations, which occurred just before goal-directed navigation, better predicted the rats future behavior than replay events at the home goal (not shown), which occurred just before foraging.. Right: replay events at the randomly rewarded locations had a bias to end at the remembered goal location. The behavioral and replay trajectories shown in the left and middle illustrations and the right data plot are modified from original data plots in Pfeiffer and Foster (2013). (B) Left and middle: illustration of the maze and task used by Carey et al. (2019). Rats were either food or water deprived and could choose to navigate to either a food or water reward, located at the end of separate arms in a T-maze. Replay at the session-by-session basis, but not trial-by-trial basis , preferentially encoded the opposite route to the behaviorally preferred route. Right: data plot showing the opposite relationship between preferred replayed route in orange (toward food; above midline, or water; below midline) and behaviorally preferred route in black (plotted as proportion of food choices). Data plot modified from original data plot in Carey et al. (2019). Rat illustrations from scidraw.io. 

to the home-well location) relative to replay events occurring at the home well (for more in-depth discussion, see: Pfeiffer, 2020). Collectively, these studies suggest that replay might aid planning only under specific circumstances, such as when there is a high mnemonic demand to keep track of the current goal location. Indeed, especially in the case of Pfeiffer and Foster (2013), the lack of pre-defined tracks toward the goal meant that the demand to plan a route toward this site was high. However, another rarely considered possibility is that, in continuous navigation tasks, replay may reflect a latent path-integration process with no direct role in planning. Future studies may investigate this by incorporating discontinuous trials into their tasks, such as by carrying the animal to different random start locations, thereby disrupting the path-integration process (e.g., de Cothi et al., 2021). When reward is given at a goal, it is also possible that replay reflects reactivation of previously rewarded locations without aiding planning per se (e.g., Gillespie et al., 2021; see: "Representation of non-preferred routes by hippocampal replay"). One way to investigate this is to separate goal and reward sites (e.g., Hok et al., 2007a). 

Task engagement might be one factor influencing whether replay supports planning. For example, it was discovered that 

in a task where rats ran back and forth on a Z-shaped track and had just arrived at or were about to depart from a reward location (bend in the track), replay preferentially represented the rats’ future route in a forward order (O[´ ] lafsdo´ ttir et al., 2017). However, when the rats lingered at these sites and were presumably less task engaged, replay preferentially represented routes in other parts of the maze in both forward and reverse orders. Additionally, replay recorded from rats foraging with no reliable goal has been found to reflect random walks (i.e., brownian diffusion) rather than experienced trajectories (Stella et al., 2019). In any case, other factors likely also influence the content and directionality of replay. For example, it was recently found that during learning of a new subgoal location in an open field, rats would preferentially replay an optimal route toward this location multiple trials before the route became preferred behaviorally (Igata et al., 2021). One possibility is that this finding reflected a competition between a place strategy (supported by CA1 replays of an optimal route) and a response strategy (supported by neural processes in the DLS, see navigating in the wild and in the laboratory). 

Although a few recent studies have reported replay-like reactivations at different neural scales in humans (Higgins et al., 

Neuron 110, February 2, 2022 403 

Review 

**==> picture [76 x 35] intentionally omitted <==**

**==> picture [17 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [246 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
A D<br>E<br>B<br>F<br>G<br>C<br>H<br>**----- End of picture text -----**<br>


**==> picture [73 x 41] intentionally omitted <==**

**==> picture [72 x 53] intentionally omitted <==**

**==> picture [72 x 43] intentionally omitted <==**

**==> picture [76 x 51] intentionally omitted <==**

**==> picture [73 x 52] intentionally omitted <==**

**==> picture [40 x 35] intentionally omitted <==**

**==> picture [40 x 35] intentionally omitted <==**

**==> picture [44 x 40] intentionally omitted <==**

**==> picture [46 x 41] intentionally omitted <==**

**==> picture [41 x 40] intentionally omitted <==**

**==> picture [40 x 35] intentionally omitted <==**

Figure 4. Evidence for goal codes in the human hippocampal formation (A) Hippocampal (HPC) activity measured with fMRI when planning routes shows higher similarity to activity evoked at the future goal and subgoal locations than at non-goal locations (Brown et al., 2016). 

(B) Evidence for allocentric goal direction coding. Bar graph provides an illustrative summary of the key result from both Chadwick et al. (2015) and Shine et al. (2019); increased matching in voxel patterns in subicular (SUB) and entorhinal (EC) regions for trials where the goal direction matched. Brain image demonstrates statistical parametric map of the regions showing allocentric direction coding from Chadwick et al. (2015). 

(C) Evidence of single unit activity in the human hippocampal formation showing goal-specific activity during navigation of a virtual environment (Ekstrom et al., 2003). 

(D) Right EC activity decreases with Euclidean proximity to the goal, and right posterior HPC activity decreases with path proximity to the goal when participants navigate a first-person view movie-based simulation of London’s Soho (Howard et al., 2014). 

(E) Right EC/SUB activity decreases with the Euclidean proximity to the goal for London taxi drivers navigating a virtual simulation of London (Spiers and Maguire, 2007). 

(F) Right posterior HPC activity decreases with proximity to the goal when navigating to learned goals in two real-world environments presented via Google Street View navigation during fMRI (Patai et al., 2019). ‘‘Distance’’ refers to the Euclidean proximity to the goal at each time step, but collinear with the path proximity due to minimal barriers (same in G and H). 

(G) Bilateral posterior hippocampal (HPC) activity increases with proximity to a remembered goal when navigating in a featureless plane (Sherrill et al., 2013). (H) Bilateral HPC activity increases with proximity to the goal when deciding which of two paths is shortest to a visible goal (Viard et al., 2011). Figures are used with permission, and data plots are not based on original data but are illustrative of main results. 

2021; Liu et al., 2019, 2021; Vaz et al., 2020), there is, to the best of our knowledge, as of yet no studies investigating human replay during a pure spatial navigation task. Nonetheless, recalling a distant location has been found to drive the activity of single neurons in the HF previously active near that location during virtual reality (VR) navigation (Miller et al., 2013). Similarly, larger-scale fMRI activation patterns in the HPC for goals and sub-goals have also been found to become reactivated away from the goal during VR navigation (Figure 4A; Brown et al., 2016; also see: Kunz et al., 2019). 

## Representation of non-preferred routes by hippocampal replay 

Although successful navigation often requires keeping track of the route(s) leading to a goal, it may under some circumstances be more informative to keep track of the route(s) to be avoided. If 

so, it might be expected that this information would also become represented in the content of replay events. In support of this notion, one study reported that, when rats were running along a linear track containing a region triggering a foot shock, they gradually learned to avoid this region but at the same time began replaying routes toward it from their location in other parts of the track (Wu et al., 2017). In another study, rats were either food or water deprived in different sessions and could in each trial choose to navigate to a food or water reward, located in either end of a T-maze (Figure 3B; Carey et al., 2019). Although rats preferred to navigate to the location containing the reward of which they had been deprived, replay events during both rest and pauses preferentially represented the non-preferred route, on a session-by-session basis (no clear relationship between replay content and behavior could be established on a trial-bytrial basis). This discovery might be related to the recent finding 

404 Neuron 110, February 2, 2022 

**ll** 

## Review 

that, in an eight-arm maze where the goal arm changed multiple times within a session, replay events prior to choice did not relate to immediate future behavior but preferentially represented routes toward previously rewarded locations that had become infrequently visited (Gillespie et al., 2021; also see Gupta et al., 2010). From a computational perspective, one reason to replay less-visited parts of a maze might be related to memory maintenance, such as for maintaining sufficiently flexible (i.e., policy-independent) SRs (see: "Topological predictions"; Table 2). As these representations predict future states based on current and past occupancy, their estimates could risk becoming biased by a non-homogenous sampling of space (Mattar and Daw, 2018; Momennejad, 2020; Momennejad and Howard, 2018; Stachenfeld et al., 2017). 

## Role of mEC grid cells in planning? 

Althoughsomecomputationalmodels havepredicted grid cells to have a role in planning routes toward goals (see: "Theoretical predictions of goal coding"; Table 2), only a few experimental studies have so far investigated grid-cell replay (O[´ ] lafsdo´ ttir et al., 2016; O’Neill et al., 2017). Notably, coordination between CA1 place cell and mEC grid-cell replay events increased when place cells replayed routes in a forward order (O[´ ] lafsdo´ ttir et al., 2016). Additionally, inhibiting mEC layer II input to CA1 during quiet awakeness reduced the spatial coverage of place cell replay events, suggesting that input from mEC might be needed for properly simulating routes in CA1 (Yamamoto and Tonegawa, 2017). mEC grid cells can also replay trajectories independently of CA1 place cells and without a reliance on HPC-related SWRs (O’Neill et al., 2017). Whether this meansthat themEC has a separate role in planning relative to the HPC remains to be determined. 

Recent evidence from humans supports the idea that the EC may play a role in navigational planning. Specifically, during imagined navigation in virtual environments, fMRI activity consistent with a grid-like structure increased when imagining navigating to goals (Bellmund et al., 2016; Horner et al., 2016). Furthermore, when a new goal was presented during navigation of a newly learned city, activity in the EC increased significantly if the new goal required a large change in the Euclidean distance to the goal (Figure 1B), but not the path distance (Figure 4D; Howard et al., 2014). This is consistent with models proposing that grid-cell activity in the mEC is used to calculate the vector to the goal, with larger vector updates for new goals potentially requiring more processing (Bush et al., 2015, see vector-based predictions; Table 2). 

Allocentric goal direction codes in the human entorhinal and subicular regions during planning and goal setting Recent fMRI studies have shed light on how allocentric and egocentric direction to goals might be represented in the human brain during planning (Chadwick et al., 2015; Shine et al., 2019). Specifically, these studies explored the possibility the HF might contain neurons active when a goal is at particular bearing from the navigator, e.g., ‘‘north goal cells’’ would be active whenever the goal is located to the north (e.g., Burgess and O’Keefe, 1996). It is possible for such cells to be nonhomogeneously distributed in the HF such that any given fMRI voxel might have slightly more cells coding for some directions than others (Epstein et al., 2017). 

This would lead to a consistent set of patterns elicited across voxels for each goal direction in the brain region coding goal direction. Using multi-voxel decoding, it is possible to search for these patterns in fMRI activity, and this is exactly what Chadwick et al., (2015) and Shine et al., (2019) did. Specifically, Chadwick et al., (2015) had participants make allocentric and egocentric judgments about the direction of a set of goal locations in a square environment with distinct landscapes in each direction (mountains, desert, sea, and forest). For the allocentric question this was ‘‘is the goal toward the mountains, sea, desert or forest?’’ For the egocentric, ‘‘is the goal to your left, right, forward, or backward?’’ Greater multi-voxel pattern similarity was observed in the EC/SUB region across pairs of trials with the same allocentric direction to a goal (e.g., north), consistent with the proposal neurons coding goal direction might exist in EC/SUB (Figure 4B). In addition, EC/SUB showed a greater match across trials where the head direction was the same, consistent with head-direction modulated cells in the EC/SUB (Grieves and Jeffery, 2017). Multi-voxel patterns in PPC were more similar for pairs of trials that matched the same egocentric direction to a goal, consistent with PPC coding egocentric space (Byrne et al., 2007). Using higher spatial resolution fMRI and a virtual environment with distant goals and internal barriers, Shine et al. (2019) asked participants to judge the allocentric direction to goals and similarly found activity in anterior SUB and anterior EC that signaled allocentric goal direction, which, interestingly, was separable from a local boundary direction signal in the posterior SUB and posterior EC (Figure 4B). Thus, it would be conducive for future research with rodents to explore these regions for allocentric goal-direction signals (Figure 1B). 

## PHASE II: TRAVELING TO GOAL 

After route planning or initiation of a stored response program, the next broad phase of navigation involves traveling to the goal. Spatial decision making and route deliberation may occur during this time, such as for ensuring that the initially planned route is being followed and/or for evaluating other possible routes towards the goal. This requires keeping continuous track of where the goal is located relative to the dynamic self-location. Activity signaling the distance and/or vector to the goal has been predicted by various computational models (see: "Theoretical predictions of goal coding"; Table 2), and below we discuss experimental evidence for these and similar codes in the HF. 

## Route deliberation and maintenance by hippocampal theta sequences during travel 

Unlike replay, which is strongly related to quiescent SWRs, theta sequences in CA1 and CA3 refer to temporally compressed activations of place cells within each oscillation cycle in the theta frequency band (4–12 Hz; Vanderwolf, 1969), which primarily occurs during movement or during brief pauses of locomotion (albeit typically with active head sweeps) at decision points (Dragoi and Buzsa´ ki, 2006; Foster and Wilson, 2007; Johnson and Redish, 2007, for a review, see Drieu and Zugaro, 2019). Theta sequences represent a trajectory slightly behind to slightly ahead of the animal and tend to be ‘‘chunked,’’ by preferentially starting and stopping at maze landmarks such as turns (Gupta 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 405 

Review 

## **ll** 

et al., 2012). Similar to replay, theta sequences have also been reported in the mPFC (Hasz and Redish, 2020; Tang et al., 2021). 

There is a strong consensus that during vicarious trial and errors (VTEs), when rats pause and deliberate over possible route options (Muenzinger and Gentry, 1931; Redish, 2016; Tolman, 1939), the look-ahead content of theta sequences also typically alternate between representing the different routes (e.g., Amemiya and Redish, 2016; Johnson and Redish, 2007; Papale et al., 2016; Tang et al., 2021). However, it is important to note that theta sequences can also cycle between representing potential routes when no VTEs are present (Kay et al., 2020; Wang et al., 2020). When VTEs are present relative to when they are not, theta sequences have been found to extend further ahead of the animal (Hasz and Redish, 2020), and there may be increased decoding of goal locations (Papale et al., 2016), possibly so as to integrate more spatial information into the deliberation process. However, when the animal has learned the goal location and the presence of VTEs has diminished or is absent, theta sequences have in some studies instead been reported to preferentially represent the correct future route, suggesting a role in route maintenance (Amemiya and Redish, 2016; Johnson and Redish, 2007; Papale et al., 2016). The look-ahead projection distance of theta sequences has also been found to vary according to whether the animal intends to navigate toward a distal or proximal goal (Wikenheiser and Redish, 2015). Theta sequences may therefore represent route information in both qualitative (e.g., informing whether to turn left or right at a decision point) and quantitative (e.g., varying the look-ahead projection distance as a function of current distance to the goal) manners depending on current navigational demands. 

It was recently reported that when HPC theta sequences alternated between representing different route options, mPFC theta sequences more strongly predicted the upcoming choice (Tang et al., 2021). Taken together with results on mPFC replay described previously (see: "Representation of prospective goal-directed routes by hippocampal replay"), this suggests that the HPC may supply mPFC with bottom-up goal-related information, which the mPFC may in turn use in a top-down manner to influence prospective spatial representations in the HPC (cf. Hasz and Redish, 2020). However, the full extent and nature of hippocampo-cortical interactions during HPC sequence generation remain to be fully determined (cf. Berners-Lee et al., 2021). 

## Route deliberation by hippocampal splitter cells during travel 

When rodents repeatedly run through overlapping maze segments, a large proportion of both CA1 and CA3 place cells (up to two-thirds) become modulated depending on the animals’ past (retrospective) and/or future (prospective) trajectory (Frank et al., 2000; Wood et al., 2000, for a review, see Dudchenko and Wood 2014). However, these so-called ‘‘splitter’’ cells can also be found in other regions both within the HF, including in the mEC (Frank et al., 2000; Lipton et al., 2007) and SUB (Kitanishi et al., 2021), and outside the HF, including in the nucleus reuniens (NR; Ito et al., 2015), mPFC (Baeg et al., 2003; Ito et al., 2015; Shin et al., 2019), and orbitofrontal cortex (OFC, Young and Shapiro, 2011). 

Although early studies showed splitter activity in simple mazes with one binary decision point (Frank et al., 2000; Wood et al., 2000), subsequent studies used more complex mazes that had, for example, multiple sequential decision points (Ainge et al., 2007a; Grieves et al., 2016) or one decision point with more than two options (Xu et al., 2019). Interestingly, splitter cells seemed to encode not just specific spatial decisions (i.e., a single left-right choice) but specific route identities (i.e., the whole sequence of left-right choices). This was found to be true both when each route led to a different goal (Ainge et al., 2007a) and when subsets of routes led to the same goal (Grieves et al., 2016). In the latter study, only two place cells (making up 0.5% of recorded place cells, or 4.2% of recorded splitter cells) showed differential firing depending on the intended goal and not the current route. Although this activity might have occurred by chance, the existence of a very small population of dedicated ‘‘goal-route’’ cells that fire whenever any route is followed toward a specific goal cannot be ruled out. Future studies using highdensity recordings or calcium imaging might shed light on whether such a population of cells indeed exists (cf. Gauthier and Tank, 2018). The recency by which a goal location has been learned also impacts splitter activity, with both retrospective and prospective firing increasing when rats move between recently learned (same day) goals as opposed to well-learned (previous day) goals (Xu et al., 2019). 

Similar to theta sequences, splitter cells appear as another candidate for supporting ongoing goal-directed navigation by keeping track of the current route. In support of this notion, splitter firing issometimesdegraded inerror trialsor whenperformanceis low (e.g., Ferbinteanu and Shapiro, 2003; Ferbinteanu et al., 2011) but not always (Levy et al., 2021; Pastalkova et al., 2008). During switching from a continuous-alternation to a continuous task, rate remapping in splitter cells can also precede behavioral change, suggestive of a learning mechanism (Ji and Wilson, 2008). However, other evidence suggests that splitter cells may not have a functional role in guiding navigation. For example, when rats repeatedly navigated between a series of goal locations via a learned sequence in an open field, splitter activity did not emerge, unless guiding barriers had been introduced during initial training (Bower et al., 2005). Splitter activity may therefore, in some situations, depend on how the task had originally been learned. However, other studies have found that increasing the spatial or memory processing demands does not significantly affect the proportion of splitter cells (Ainge et al., 2007b, 2012; Ferbinteanu et al., 2011). Splitter cells are also active in track-based tasks that can be solved without an intact HPC, such as continuous-alternation tasks (Ainge et al., 2007b; Wood et al., 2000) or when a beacon signifies the goal location (Ferbinteanu et al., 2011). Indeed, HPC lesions (Ainge et al., 2007b) or RE lesions or optogenetic silencing (Ito et al., 2015) do not impair learning or performance in continuous-alternation tasks despite abolishing or significantly diminishing splitter activity in CA1. As the NR is a main relay between the mPFC and CA1 (Vertes et al., 2007), it is likely that that top-down control from mPFC participates in driving the splitter activity in the HPC (Ito et al., 2015). If splitter cells do not immediately guide navigation, another possibility is that they signal latent mnemonic representations of learned routes (Sanders et al., 2020; Smith and Mizumori, 2006). 

406 Neuron 110, February 2, 2022 

## Review 

**==> picture [7 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>C<br>**----- End of picture text -----**<br>


**==> picture [141 x 57] intentionally omitted <==**

**==> picture [138 x 71] intentionally omitted <==**

**==> picture [51 x 41] intentionally omitted <==**

Figure 5. Neural representations of route, distance, and direction to goal 

(A) Left and middle: illustration of the maze and task used by Grieves et al. (2016). Notably, rats could take two routes to the same goal location, and the activity of splitter cells predominantly reflected the intended route instead of the intended goal location. Right: the proportion of active place cells increased with distance from the goal, analyzed by maze compartments (a stem or choice point). Data plot is modified from original data plot. 

(B) Left and middle: illustration of the maze and task used by Spiers et al. (2018). Rats navigated to the same goal location from four different starting positions. Right: normalized population activity in CA1 increased as a function of normalized distance to the goal. AU, arbitrary units. Data plot is modified from original data plot. 

(C) Left and middle: illustration of the setup and task used by Sarel et al. (2017). A food platform was either visible or hidden behind a curtain, and the bats flew complex trajectories before landing, allowing sampling of all 360[�] egocentric goal directions and path distances as far as 10 m toward the goal. Right: illustrative example of a conjunctive goal distance X direction goal-vector cell in CA1. Notably, the path-distance tuning peaked close to the goal, and the egocentric goal-direction tuning peaked when the bats’ head direction was pointed toward the food platform, which was representative for most cells. Data plot is modified from original data plot. Rat illustrations from scidraw.io. 

Although there is limited evidence for splitter activity in the human HF (Jacobs et al., 2010), there have been reports of splitterlike goal cells, which show differential activity during travel depending on the identity of the goal (Figure 4C; Ekstrom et al., 2003). Such goal-related activations appear phase locked to local oscillations (Kunz et al., 2019; Qasim et al., 2021; Tsitsiklis et al., 2020; Watrous et al., 2018), but any functional significance of such coupling remains to be determined. Similarly, Tsitsiklis et al. (2020) reported ‘‘spatial target’’ cells in the HPC, EC, and parahippocampal structures whose activity was modulated during travel depending on the remembered position of the current goal. In contrast to Ekstrom et al. (2003), these activity modulations were determined by the goals locations, rather than the identity of the goals themselves. How these cells relate to other goal-coding correlates in rodents remains an open question. 

## **ll** 

## Representation of distance toward the goal during travel 

Knowing the distance to a goal is important to avoid traveling too far or searching for the goal at locations too early in the route. In the last few years, such codes have been reported in the HF of multiple mammalian species. 

In studies using track-based mazes with multiple sequential decision points, it has been reported that the proportion of active place cells decreases with proximity to the goal (Figure 5A; Ainge et al., 2007a; Grieves et al., 2016). Similarly, in a study using an open field navigation task, population activity in CA1 decreased with proximity to the goal, and the rate of decrease correlated with task performance (Figure 5B; Spiers et al., 2018). However, it is possible that these findings simply reflected an overrepresentation of place cells at maze segments most commonly experienced, without providing a goal-distance code per se. More recently, during navigation to an unmarked goal in a VR task, a subpopulation of cells encoding distance from the start was reported (Moore et al., 2021). These cells overrepresented very short distances (e.g., closer to the start), and their activity was better explained by coding of distance from start rather than proximity to the goal or time passed. The path and Euclidean distance to the goal were also similar across these studies, making it impossible to disentangle these metrics. Only a few studies in humans (e.g., Brunec et al., 2017; Howard et al., 2014) and one recent study in Egyptian fruit bats (Sarel et al., 2017) have used navigation paradigms where these metrics can be dissociated. 

In the study by Sarel et al. (2017), principal cells in CA1 were recorded from bats as they circled either a visible or hidden food platform in a large room (Figure 5C). The researchers discovered that, in addition to typical place cells, ‘‘goal-distance’’ cells (making up �16% of recorded principal cells) exhibited tuning to different path proximities or, more rarely, Euclidean proximitiestoward the platform. This was only investigated when the goal was visible, presumably because the bats trajectories were more circuitous, thereby allowing separation of Euclidean and path metrics. Although most of the goal-distance cells fired maximally at 0–2 m from the platform, some fired maximally up to 10 m away, allowing their combined population activity to represent the complete path distance toward the platform. However, evidence for such cells has not yet been reported in tasks with hidden goals, wherein a more complex navigation strategy might be required. 

Activity signaling distance to goal during travel has also been investigated in numerous human studies during VR navigation. For example, activity in the right SUB/EC has been found to decrease with Euclidean proximity to the goal (Figures 4D and 4E; Howard et al., 2014; Spiers and Maguire, 2007). In the study by Howard et al., (2014), activity in the posterior HPC (homolog of the rodent dorsal HPC) also decreased with path proximity to the goal (Figure 4D), with similar results reported elsewhere (Figure 4F; Patai et al., 2019). However, other studies support the notion that activity in anterior HPC might also signal goal-distance information. For example, activity in this region decreased with proximity between remembered landmarks (Morgan et al., 2011) and with proximity to the goal/starting position in a path-integration task (Chrastil et al., 2015). However, on the contrary, other navigation tasks have found that activity in this region increased with proximity to 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 407 

Review 

## **ll** 

**==> picture [419 x 286] intentionally omitted <==**

Figure 6. CA1 Place cell fields accumulate around goal locations 

(A) Illustration of the experimental protocol and main findings from Dupret et al. (2010). Each experimental day consisted of five sessions: a pre-probe session (�25 min), a sleep/rest session (�25 min), a learning session (�40 trials, �25 min), another sleep/rest session (�25 min), and a final post-probe session (�25 min). The final post-probe session was conducted �2 h after the learning session. Each probe session was unrewarded. In the first type of learning session (top row), rats had to learn the location of three goal locations, consume the rewards at these sites, and return to a start box to consume another reward and initiate a new trial. CA1, but not CA3, place fields gradually moved toward the goal locations, and place fields still accumulated at the goals in the post-probe session demonstrating memory retention. The proportion of place fields at the goal locations at the end of the learning session (last 10 trials) and during the post-probe session also predicted memory performance (defined as the number of crossings of the goal locations). For rats injected with the NMDA receptor (NMDAR) antagonist CPP after the pre-probe session (middle row), place fields also gradually moved toward the goals in the learning session. However, place fields no longer accumulated at the goals in the post-probe session. Lastly, when the goal locations were cued with visible falcon tubes (bottom row), place fields did not move toward the goal locations despite the rats having intact performance. In addition, the rats demonstrated no memory retention for the goal locations in the post-probe session. Within each learning session, the rats’ trajectories became increasingly stereotyped over time, indicating that they might have switched from using a place strategy to using a sequential-egocentric strategy. 

(B) Proportion of place fields at the goal locations (defined in the learning session) in the pre- and post-probe sessions. Note the significantly larger proportion of CA1, but not CA3, place fields at the goal locations in the post- versus pre-probe session when goal locations were hidden. Data plots modified from original data plots in Dupret et al. (2010). 

Rat illustrations from scidraw.io. 

the goal (Figures 4G and 4H; Sherrill et al., 2013; Viard et al., 2011; also see Balaguer et al., 2016). 

We currently lack sufficient data to determine why activity in different regions of the HF might be positively or negatively correlated with the distance to the goal across different tasks. Current research suggests that when processing the route to a goal in larger environments, posterior HPC activity decreases with proximity to the goal (Howard et al., 2014; Patai et al., 2019), whereas in smaller more constrained environments, anterior HPC activity increases with proximity to the goal (Balaguer et al., 2016; Sherrill et al., 2013; Viard et al., 2011), but why this might be the case requires further investigation. Many factors are likely at play, such as differences in navigation strategies employed or specific phases of navigation where activity is investigated. For example, in a recent study where students navigated a virtual simulation of familiar or recently learned college cam- 

puses, posterior HPC activity decreased with proximity to the goal during travel but increased with proximity to the goal at decision points (Figure 6C; Patai et al., 2019; also see Howard et al., 2014). Many challenges also exist for investigating goal-distance estimations. For example, having to circumnavigate a region of space (Brunec et al., 2017) or having increased familiarity over months with a space (Jafarpour and Spiers, 2017) can result in distortions in estimated distances. It is also possible that the presence of sub-goals can distort estimated distances, but to the best of our knowledge, this has not yet been tested. 

## Representation of direction toward the goal during travel 

Although it can be important to gauge the correct distance to a remembered goal, miscalculating the direction can often be more deleterious for successful navigation. In rodents, 

408 Neuron 110, February 2, 2022 

**ll** 

## Review 

head-direction cells provide an allocentric representation of azimuthal orientation, which has been proposed to function as an ‘‘internal compass’’ during navigation (Butler et al., 2017). Although a few studies have investigated head-direction cells in goal-directed tasks, no modulation by goal locations has as of yet been reported (e.g., Muir and Taube, 2004; SanguinettiScheck and Brecht, 2020). 

Some older studies have reported the existence of ‘‘goalapproach cells’’ in CA1 that fired as rats turned to and/or moved toward visible goals (Eichenbaum et al., 1987; Gothard et al., 1996; Wiener et al., 1989). A similar finding was more recently reported by Aoki et al. (2019), who found increased in-field activity of place cells as rats moved toward cued goals in an open field. Additionally, this activity was maintained when the cues were removed and reward was randomly scattered in the maze—but only when the rats ran similar ballistic trajectories toward the remembered cue/goal location as they had done in the cued task. One possibility is therefore that this activity reflected the execution of a learned motor sequence and not a goal-direction tuning per se. 

One of the clearest examples of a potential goal-direction code in the HF comes from Sarel et al. (2017), who, in addition to goaldistance cells, reported goal-direction cells in the bat CA1 (Figure 5C). These cells represented different egocentric angles between the bats’ heading direction and the food platform (making up �19% of recorded principal cells, Figure 1B). Importantly, this tuning occurred both when the platform was visible and when it was hidden behind a curtain, indicating that the tuning was memory based. The majority of goal-direction cells (81%) were tuned only to one of the visible or hidden platforms, indicating goal-specific representations. Although most goal-direction cells preferentially fired when the bat was turned toward the platform direction, they could be tuned to any egocentric goal direction relative to the platform (Figure 1B), and their combined ensemble activity represented all 360 degrees of goal directions relative to the platform. Additionally, �5% of cells were found to conjunctively represent information about both the distance and direction to the goal (Figure 5C). Lastly, a recent preliminary study reported that place cell ensemble activity might enable both allocentric and egocentric goal-vectorial computations by creating ‘‘sinks’’ of activity leading to the goal location from the current self-location (Ormond and O’Keefe, 2021). Given these findings, it is possible that different types of goal-directed signals stably coexist within the HF. 

Although fMRI studies have found evidence of activity signaling allocentric direction in the human HF during planning (see: "Allocentric goal direction codes in the human entorhinal and subicular regions during planning and goal setting"), similar activity has not been reported during travel. Rather, the PPC has been implicated in keeping continuous track of the egocentric direction to the goal during travel (Howard et al., 2014; Spiers and Maguire, 2007), similar to that reported during planning (see: "Representation of prospective goal-directed routes by hippocampal replay"; Chadwick et al., 2015). 

## Extending goal codes to ‘‘traveling’’ in abstract spaces 

It has recently been suggested that common circuit mechanisms exist for mapping out position in both spatial and non-spatial 

domains (Behrens et al., 2018; Bellmund et al., 2018; Epstein et al., 2017), suggesting that similar goal-related representation as discussed above might also guide navigation through more abstract spaces. For example, in rodents, single neurons in HPC and EC can form place fields along specific frequency ranges in auditory space, when keeping track of this information is relevant for receiving reward (Aronov et al., 2017). In humans, recent studies have shown that activity in the HF can signal distance and direction information in verbal memories (Solomon et al., 2019), learned semantic spaces (Vigano` and Piazza, 2020), social hierarchies (Park et al., 2020), and narratives (Tavares et al., 2015). For example, when recalling words in a learned list, the evoked theta power for each word can be predicted in part by the distance between words in a measure of semantic similarity (Solomon et al., 2019). Recalling ‘‘dog’’ then recalling ‘‘fur’’ would likely result in a small change in theta power, whereas recalling ‘‘cat’’ and then ‘‘lightbulb’’ would be expected to result in a larger change in theta power because cat and lightbulb are less semantically similar (Solomon et al., 2019). It will be useful for future studies to more directly compare navigation in spatial and non-spatial dimensions to determine the extent to which generalization across these domains occur (Spiers, 2020; Whittington et al., 2020). Indeed, such approaches will inform our understanding of how the mammalian brain enables navigation at basic, clinical, and translational levels. So far, most human studies in this domain have explored evoked responses to learned sequences of stimuli (e.g., a sequence of words recalled) rather than responses to stimuli in a space that needs to be more explicitly navigated (e.g., navigating a learned social network of friends to seek, gather, and share information). 

## PHASE III: ARRIVING AT GOAL 

In the final operational stage of navigation, animals approach and arrive at a goal location, where reward may be obtained and there is an opportunity to process the recent navigation epoch. Various computational models have predicted cells that fire proximal to goals, enabling a gradient of activity that can guide navigation (see: "Theoretical predictions of goal coding"; Table 2). Multiple experimental studies have also reported that during goal approach, a significantly higher (typically approximately two to three times) proportion of place cells in CA1 become active relative to when other equally large areas become visited, overrepresenting goal locations in HPC maps (for reviews, see O’Keefe and Krupic, 2021; Poucet and Hok, 2017; Sosa and Giocomo, 2021). More recently, a similar goal-oriented reorganization has also been reported in EC grid and nongrid spatial cells (Boccara et al., 2019; Butler et al., 2019). Do these phenomena aid goal-directed navigation, or are they a consequence of other factors such as biased behavior or reward expectation? 

## Reorganization of hippocampal activity around goals 

The phenomenon of goal overrepresentation by place cells has been reported in many different types of navigation studies and found to occur gradually, as a function of experience with the task (e.g., Dupret et al., 2010; Lee et al., 2006; Zaremba et al., 2017). Most studies have used tetrode recordings in freely 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 409 

Review 

## **ll** 

moving rats navigating either track-based (e.g., Fyhn et al., 2002; Hollup et al., 2001b; Mamad et al., 2017; Xu et al., 2019) or open (e.g., Breese et al., 1989; Dupret et al., 2010; Kobayashi et al., 1997, 2003; Xiao et al., 2020) mazes, but more recent studies have also employed calcium imaging in either freely moving mice navigating an open maze (Jarzebowski et al., 2022) or head-restrained mice navigating either repeating VR environments (Gauthier and Tank, 2018; Lee et al., 2020; Robinson et al., 2020; Sato et al., 2020) or treadmills with tactile cues (Danielson et al., 2016; Kaufman et al., 2020; Turi et al., 2019; Zaremba et al., 2017). Across these studies, goal locations have become associated with rewards, either appetitively motivated rewards, such as food and water (e.g., Danielson et al., 2016; Dupret et al., 2010; Kaufman et al., 2020; Lee et al., 2012; Turi et al., 2019; Xu et al., 2019; Zaremba et al., 2017, 2017), or aversively motivated rewards, such as when a platform is introduced that offers an escape from swimming (Fyhn et al., 2002; Hollup et al., 2001b). However, goal overrepresentation is not a simple function of reward acquisition, as this activity tends to begin slightly before the goal is reached and reward has been obtained (Gauthier and Tank, 2018; Zaremba et al., 2017) and can persist, at least transiently, when rewards are removed from the goal (Dupret et al., 2010; Jarzebowski et al., 2022). It is also unlikely that this phenomenon reflects reactivations of non-local locations (see: "Representation of prospective goal-directed routes by hippocampal replay") because such activations typically occur during immobility periods, which are normally removed in place-field analyses. 

The nature of the goal code provided by an overrepresentation of place cells has recently been debated (O’Keefe and Krupic, 2021; Sosa and Giocomo, 2021). For example, in most studies with more than one goal, with either one goal active at a time (Danielson et al., 2016; Fyhn et al., 2002; Kaufman et al., 2020; Sato et al., 2020; Turi et al., 2019) or multiple goals active simultaneously (Dupret et al., 2010; Duvelle et al., 2019; Jarzebowski et al., 2022; Lee et al., 2020; Xu et al., 2019), different place cells have been found to form fields at different goals. Only one study has reported finding a dedicated population of place cells active at all possible goals (Gauthier and Tank, 2018). This population was found in both the CA1 and the SUB and comprised only 0.8% of all recorded cells. However, a more recent and similar study did not support this finding, reporting that only a single place cell tracked all goals, and this, as well as other cells with fields at multiple goals, also formed fields elsewhere, supporting a goal-by-place code (Lee et al., 2020). This discrepancy might result from having one (Gauthier and Tank, 2018) versus many (Lee et al., 2020) simultaneously active goals or having relatively small (�2–4 m, Gauthier and Tank, 2018) versus relatively large (�40 m, Lee et al., 2020) environments. However, the contributions of such factors to goal overrepresentation remain unclear. We also note that both of these studies used VR tasks in which HPC correlates might be quite different from real-world tasks and could more strongly reflect parameters such as distance, time, or reward rather than allocentric space (e.g., Moore et al., 2021). 

Distinct populations of HPC place cells appear to become differentially modulated by goal locations, possibly owing to differences in afferent and/or efferent projections (Ciocchi et al., 

2015; Lee et al., 2020). Indeed, differences have been noted across the principal axes of CA1 (consisting of the dorsalventral ‘‘long’’ axis, the superficial-deep ‘‘radial’’ axis, and the proximal-distal ‘‘transverse’’ axis, Cappaert et al., 2015). In regard to the long axis, one recent study reported that place cells in intermediate-to-ventral CA1 (ivCA1) had a higher rate of goal overrepresentation relative to place cells in the dorsal CA1 (dCA1) and only place cells in the former region incorporated information about the changing reward value of goals (Jin and Lee, 2021). However, another recent study reported that only dCA1 and not ivCA1 place cells overrepresented goals (Jarzebowski et al., 2022). Instead, ivCA1 place cells were found to have a higher propensity to form fields at multiple goals relative to dCA1 place cells, and population activity of non-place cells in ivCA1 significantly decreased near goals, suggestive of complementary goal codes in this region. More research is needed to investigate these discrepant findings, and whether they might be task-dependent (see below). In regard to the radial axis, one study reported that superficial CA1 (supCA1) place cells remained more stable (defined as having high correlations between firing rate maps) both within and across days relative to deep CA1 (dpCA1) place cells, but dpCA1 place cells near a goal became selectively stabilized—albeit with comparable stability to an average supCA1 place cell (Danielson et al., 2016). In addition, dpCA1 place cells remained more stable across sessions of a goal-directed task than across sessions of a random foraging task, whereas no such task-dependent difference was found for supCA1 place cells. To the best of our knowledge, no differences in goal coding have as of yet been reported in the transverse axis, which requires further investigation. Differences in goal modulation have also been reported across HPC subfields (recording in the dorsal subregion), with CA3 place cells not found to overrepresent goals when this has simultaneously been reported for CA1 place cells (Dupret et al., 2010). Reward probability-related signals also appear stronger in CA1 compared with CA3 (Lee et al., 2017). Whether CA2 place cells overrepresent goals is currently not known. 

Identifying the conditions causing place cells to overrepresent goals is challenging, with some seemingly conflicting results in the literature. However, certain patterns can be deduced. For example, in the vast majority of studies where place cells overrepresent goals, animals have followed very similar goal-directed trajectories across trials. Indeed, the degree of overlap among repeated trajectories has been found to correlate with the proportion of place cells moving toward the goal (Mamad et al., 2017). However, using a specific navigational strategy does not seem to be a determining factor, as goal overrepresentation has been noted in tasks where a specific movement response is learned at a single decision point (i.e., response navigation, e.g., Mamad et al., 2017), in tasks where a sequence of movement responses is learned between multiple goal locations (i.e., sequential-egocentric navigation; Dupret et al., 2010; Xu et al., 2019), and in tasks where the goal location has to be determined based on its relation to a constellation of distal cues from different starting positions (i.e., place navigation; Fyhn et al., 2002; Hollup et al., 2001b). Although it can be difficult to infer navigation strategies in head-restrained animals, these tasks often require that 

410 Neuron 110, February 2, 2022 

## Review 

the goal become memorized relative to non-contiguous (tactile or visual) cues, which is HPC dependent (Sato et al., 2017; Zaremba et al., 2017). 

These findings strongly suggest that overlapping goaldirected trajectories constitute a necessary condition for goal overrepresentation. However, other studies have suggested that it does not constitute a sufficient condition. For example, although place cells overrepresented three recently learned (same day) and hidden goals that rats sequentially visited in an open field, this no longer occurred when the goals were made visible by a cue, despite the rats’ behavior and performance being comparable (Dupret et al., 2010, for illustration of experimental protocol, see: Figure 6). Only in the former case did the rats demonstrate subsequent memory for the goal locations, and the rate of overrepresentation predicted the strength of the memory performance. Similarly, in an eight-arm maze task previously described (Xu et al., 2019, see: "Representation of prospective goal-directed routes by hippocampal replay"), place fields gradually accumulated at goal arms when the rats had to memorize these arms (when replay also predicted future behavior), but not when access to the non-goal arms were blocked, lifting the memory requirement. Interestingly, place cells only overrepresented the two recently learned (same day) goal arms, but not the one well-learned (previous day) goal arm, suggesting that goal overrepresentation might, at least in some tasks, reflect a transient learning process. 

Only two studies have reported that place cells overrepresent visible goals (Breese et al., 1989; Xiao et al., 2020). In both of these studies, rats continuously moved between potential goal sites, where a reward could appear at random. A simple beaconing was therefore not sufficient to obtain reward, as had been the case in the cued task in Dupret et al. (2010) or when all available arms were goal arms in Xu et al. (2019). Although the rats’ trajectories were seemingly not as overlapping as has been noted in the other studies, the rats nonetheless primarily moved between the visible goals in search of reward. It is therefore possible that additional mnemonic memory processes became recruited, which influenced place cells to overrepresent the goals, but this remains speculative. Collectively, these studies suggest that there are two necessary and sufficient conditions that need to be met in order for place cells to overrepresent goals: (1) having overlapping trajectories across trials and (2) having memorized these trajectories and/or the goal location(s). 

A remaining question is whether goal overrepresentation has any functional role in guiding navigation. Against this interpretation is the fact that place fields do not overrepresent goals in tasks where rats have to continuously plan and execute different goal-directed routes across trials (i.e., using a place strategy not just for localizing the goal but also for continuously planning novel routes toward it, Duvelle et al., 2019; Hok et al., 2007a, 2007b, 2013; Jeffery et al., 2003; Pfeiffer and Foster, 2013; Spiers et al., 2018). Furthermore, a recent causal study both induced and inhibited goal overrepresentation and found that neither manipulation had any effect on task performance (see: "Role of hippocampal replay in learning goal-directed routes"; Kaufman et al., 2020). Other causal studies further support the notion that place cells primarily provide a self-localization code. For example, activating place cells normally active at the 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


goal before this site was reached induced goal-associated licking behavior in rats, as if the animalsbelieved they were at the goal. In the same task, activating place cells normally active at the start zone at a later location made the rats run past the goal, as if they believed that they were at the start zone when the cells were being activated (Robinson et al., 2020). In addition, pairing rewarding medial-forebrain stimulation with the firing of a place cell during sleep biases subsequent awake behavior toward the cell’s place-field location (de Laville´ on et al., 2015). However, this does not necessarily mean that place cells have no role in signifying the goal location, as they could do so via a goal-by-place code, as previously described (Lee et al., 2020). Indeed, even when place fields are not overrepresenting the goal, place cells normally active at the goal may nonetheless become preferentially reactivated during both immobile planning (e.g., Miller et al., 2013; Pfeiffer and Foster, 2013; Xu et al., 2019) and travel to the goal (e.g., Papale et al., 2016). 

Besides goals, place cells have also been found to overrepresent other locations, such as landmarks (Bourboulou et al., 2019; Sato et al., 2020), compartment entryways (Grieves et al., 2018; Spiers et al., 2015; but also see Duvelle et al., 2021), turning points (Grieves et al., 2016, 2018), starting locations (Ainge et al., 2007a; Grieves et al., 2016; Spiers et al., 2018), and aversive stimuli (an air puff; Okada et al., 2017). Overrepresentation may therefore serve a broader role in signaling saliency. However, overrepresentation of goals occurs faster than for landmarks, and mice lacking a specific glutamatergic scaffold protein demonstrate increased overrepresentation of goals but absent overrepresentation of landmarks (Sato et al., 2020). Whether these results mean that different types of overrepresentations serve different functions requires further investigation. 

Lastly, in some tasks where rats have to continuously determine novel goal-directed routes and goal overrepresentation by place fields does not occur, extra-field firing of CA1 and CA3 place cells has been reported to occur at the goal, with peak activity �1 s after arrival (Duvelle et al., 2019; Hayashi et al., 2016; Hok et al., 2007a, 2007b, 2013). Importantly, in these tasks, reward was separated from the goal, suggesting that rewardassociated processes did not cause the increased firing. Although the extra-field firing was weak at the individual-cell level, it was prominent at the ensemble level and included spikes from otherwise ‘‘silent’’ pyramidal cells (Duvelle et al., 2019; Poucet and Hok, 2017). One possibility is that this activity reflected replay of previous or future routes. However, ripple rate is generally low while rats wait for a reward but increases during reward consumption (Hok et al., 2007a; McKenzie et al., 2013; Sosa et al., 2020). Furthermore, in a specific strain of mutant mice with disrupted goal-related firing, the rate of SWRs at the goal was similar to that of control mice with normal goal-related firing (Hayashi et al., 2016). Another possibility is that the activity reflected the anticipation or expectation of reward. However, the extra-field firing did not change when a goal provided a higherthan-usual reward (Duvelle et al., 2019). It could also have reflected an inhibition signal, to slow down and stop. However, the signal occurred earlier on a cued version of the task, although the behavioral profile was similar to the uncued version (Hok et al., 2007a). Alternatively, it could have reflected a confirmation-of-arrival signal, after matching the external sensory input 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 411 

Review 

## **ll** 

to an internal goal representation instantiated in neural activity elsewhere. Indeed, having a cue at the goal might mean a confirmation signal could be activated sooner relative to when no such prominent cue was present. In support of the notion that other brain regions might instead represent the goal, mPFC neurons have been found to form large fields centered at the goal in the same task (Hok et al., 2005). It is possible that these cells constitute an experimental verification of ‘‘goal’’ cells (see: "Model-free predictions"; Table 2) especially as large goal fields were predicted with PFC hypothesized as possible loci. However, importantly, a recent study did not find any goal representation in mPFC in rats performing a similar flexible, albeit track-based, navigation task (Bo¨ hm and Lee, 2020). This discrepancy may result from varying cognitive demands of the tasks, or strategies adopted, since the rats in Hok et al. (2005) required �4 weeks of training to reach criterion, whereas the rats in Bo¨ hm and Lee (2020) required �3.5–6 months. Notably, besides the mPFC, the OFC has also been implicated in representing goal locations (Basu et al., 2021; Feierstein et al., 2006), possibly as part of a broader purported role of this region in representing a cognitive map of the current task space (Bradfield and Hart, 2020; Wilson et al., 2014). 

## Reorganization of entorhinal activity around goals 

Two recent studies have given insights into how grid and nongrid spatial cells in mEC reorganize around goal locations during different navigation tasks (Boccara et al., 2019; Butler et al., 2019). Boccara et al. (2019) used the same task as in Dupret et al. (2010) (Figure 6) and found that both CA1 place fields and mEC grid fields overrepresented the goal locations, which also positively correlated with memory retention. Although CA1 place fields were faster in shifting toward the goal locations during learning relative to mEC grid fields, only mEC grid fields still overrepresented the goal locations the next day. Goal-oriented reorganization therefore seems to occur faster but more transiently in CA1 relative to mEC. Butler et al. (2019) instead recorded from mEC in two same-sized open arena environments that were distinguishable by different wall colors and scents. In the first arena (ENV1), rats freely foraged for randomly scattered food rewards, whereas in the second (ENV2), they alternated between freely foraging and navigating to an unmarked but remembered goal (i.e., place navigation) after hearing an auditory cue. In contrast to Boccara et al. (2019), the researchers found no accumulation of grid fields close to the goal location in ENV2, matching the finding that CA1 place fields do not overrepresent goals in similar flexible navigation tasks (see: "Reorganization of hippocampal activity around goals"). Instead, subsets of nongrid spatial cells formed a clear spatial field near the goal in ENV2 despite having indiscriminate firing in ENV1, and the peak firing rate of grid fields close to the goal was higher in ENV2 relative to the same location in ENV1. One possibility is that these modulations also aid in providing a confirmation-ofarrival signal, similar to the extra-field firing of CA1 place cells noted in other studies (see: "Reorganization of hippocampal activity around goals," e.g., Hok et al., 2007a; Duvelle et al., 2019), 

Notably, mEC grid cells were also found to shift their fields toward the location of a home cage after it was introduced in an open field where rats foraged (Sanguinetti-Scheck and Brecht, 2020). However, a control experiment demonstrated that this 

was likely a result of the change to the internal geometric structure of the space and not any cognitive or motivational processes related to the home cage itself (e.g., that it had taken on the quality of a ‘‘goal’’). As the geometry of the maze remained constant in Boccara et al. (2019) and Butler et al. (2019), it is unlikely that their results could be explained by such factors. 

## Role of hippocampal replay in learning goal-directed routes 

While replay events before movement initiation has been purported to have a role in forward planning (see: "Representation of prospective goal-directed routes by hippocampal replay"), replay events after arrival at the goal have been found to represent the just-taken, or occasionally the future, route but typically played in a reversed order, which has been linked to learning and/or evaluating the goal location and its associated routes (Ambrose et al., 2016; Bhattarai et al., 2020; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006; Igata et al., 2021; Michon et al., 2019; Shin et al., 2019; Xu et al., 2019). Indeed, this phenomenon may constitute a neural mechanism for solving the temporal credit assignment problem (see: "Model-free predictions"), as information about the goal/reward can be propagated to place cells leading to or from this site (Sutton and Barto, 2018). It is important to note that (reverse) replay of the just-taken route after arrival at the goal has only been found in stereotyped track-based tasks (i.e., likely relying on either response or sequential-egocentric navigation) and not in flexible tasks where novel goal-directed routes need to be continuously determined (i.e., that emphasize place navigation, e.g., Pfeiffer and Foster, 2013). Although the need to learn specific routes is diminished in such tasks, it suggests that other mechanisms contribute toward learning goal locations. 

In line with a role of replay in learning, novelty with a task is associated with an increased rate (Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006) and temporal precision (Cheng and Frank, 2008) of replay events, and this precision may contribute to learning by increasing the rate of STDP (Bi and Poo, 1998). A STDP-dependent strengthening of adjacent place and grid cells may in turn influence the movement of their fields toward goals, underlying the phenomenon of goal overrepresentation. More specifically, the rate of CA1 SWRs, and thus presumably replay, is increased at rewarded goal locations relative to other sites in the environment (Dupret et al., 2010; Singer and Frank, 2009), especially when goals remain fixed and routes become repeated (Jackson et al., 2006). Increasing the magnitude of reward at goals also increases the rate of reverse replays (Ambrose et al., 2016; Bhattarai et al., 2020; Michon et al., 2019). 

Replay during sleep has also been proposed to have a role in the long-term consolidation of newly formed memories (O[´ ] lafsdo´ ttir et al., 2018). For example, cell assemblies co-active during novel spatial experiences become increasingly reactivated during subsequent sleep (O’Neill et al., 2008). In addition, disrupting sleep-related SWRs (Ego-Stengel and Wilson, 2010; Girardeau et al., 2009) or replay events (Gridchyn et al., 2020) following spatial learning impairs post-sleep performance. 

## Role of reward- and value-related processes 

Midbrain dopaminergic fibers from the ventral tegmental area (VTA) have been identified as having a key role in multiple 

412 Neuron 110, February 2, 2022 

**ll** 

## Review 

reward- and motivation-related behaviors and cognitions (for a review, see Sosa and Giocomo, 2021). For example, in spatial tasks, activating dopaminergic VTA fibers directly (de Laville´ on et al., 2015; Stamatakis et al., 2013; Tsai et al., 2009), or indirectly via medial-forebrain stimulation (Kobayashi et al., 1997, 2003), can elicit a place preference and shift place fields toward the activation area (Kobayashi et al., 1997, 2003), whereas suppression can elicit a place avoidance (Lammel et al., 2012; Mamad et al., 2017) and a shift of place fields away from the activation area (Mamad et al., 2017). The HPC and VTA have been proposed to form a functional loop, with novelty and goal/rewardrelated information sent from HPC to the VTA to influence dopaminergic release, in turn leading to LTP-mediated learning and memory formation in the HPC (Lisman and Grace, 2005; Otmakhova et al., 2013). In support of this notion, one study found that optogenetically stimulating VTA-CA1 fibers during spatial learning both stabilized performance and increased the rate at which newly formed cell assemblies became reactivated during subsequent sleep (McNamara et al., 2014). During quiet wakefulness, reward-responsive neurons from the VTA also become active when reactivations in CA1 reflect recent learning of goal locations (Gomperts et al., 2015). 

The communication between HPC and VTA likely occurs via many subcortical relay regions. One such region might be the lateral septum (LS) as a recent study reported that a higher proportion of place cells in LS relative to CA1 became active at goal locations, suggesting that goal-related information became strengthened in the LS (Wirtshafter and Wilson, 2020). Another likely relay station is the striatum, with principal cells in especially ventral striatum showing reward-predictive firing or signal receipt of reward (for reviews, see Cox and Witten, 2019; Sosa and Giocomo, 2021). 

Besides the VTA, the locus coeruleus (LC) also contains dopaminergic neurons, and a recent study found that activating LCCA1 fibers at the goal induced place cells to move toward this site, whereas inhibition suppressed such remapping (Kaufman et al., 2020). However, as has been noted previously, neither of these manipulations affected task performance, and LC-CA1 stimulation outside of a learned goal location did not elicit a similar movement of place fields. These results imply that potential roles of dopamine in influencing spatial representations in the HF likely depend on concurrent behavior and task demands, such as the type and phase of navigation. 

Lastly, there have been conflicting reports in regard to whether or not place cell firing represents the value of rewards at goal locations. In tasks where rewards of different values (such as magnitudes or type of reward) were predictably given at different locations, CA1 place cell firing did not incorporate value-related information (Duvelle et al., 2019; Jin and Lee, 2021; Tabuchi et al., 2003). However, place cells have been reported to represent such information in tasks where rewards are given probabilistically (Lee et al., 2012; Tryon et al., 2017). One possibility is that CA1 place cells incorporate information about rewards when more complex integration is needed. Alternatively, other subregions of CA1, or subfields of the HPC, may incorporate this information. Indeed, as has been previously noted, a recent study found that intermediate-to-ventral CA1 place cells incorporated information about changing reward 

value, whereas this was not found for dorsal CA1 place cells (Jin and Lee, 2021). 

## CONCLUSION 

In this review, we have highlighted specific neural computations relevant for representing a goal location, or a route toward this site. We have described different goal-related representations in relation to the different phases in which they were discovered, but it is important to note that a specific goal-related representation may be used in more than one phase (e.g., goal-direction coding may be used during both planning and travel phases). Furthermore, although we have mainly focused on regions in the HF, it is important to recognize that this compound structure does not operate in isolation but is part of a brain-wide network that supports behavior and cognition via a complex flow of both local and interregional efferent and afferent projections. Outside the HF, we have emphasized a role for mPFC in making final route decisions and exerting top-down control of spatial processing in the HPC, and brainstem dopaminergic structures as having roles in reward-related processes. It is also important to note that the specific neural dynamics can be influenced by many different factors, such as the current state of the system (e.g., the neuromodulatory tone) and the intrinsic capability of the brain network (e.g., not all navigators are equally adept). Ultimately, it is these complex interactions, and not any single brain process or structure, that enable goal-directed navigation. Although current theoretical models capture some of these features, there is as of yet no exhaustive framework of how such a brain-wide system operates. We provide a summary and predictive framework of the goal-related neural dynamics most supported by evidence in Figure 7. Next, we discuss outstanding conceptual questions and remaining challenges. 

## Outstanding questions and future challenges 

Given that goal codes may differ depending on the type and phase of navigation, we believe it is important for future studies to make clear the navigational strategies and demands that have elicited the goal code claimed to have been discovered. Additionally, one of the main challenges for future research pertains to elucidating how goal-related representations become communicated and transformed throughout the HF and beyond. In this review, we have mainly focused on brain regions independently, as single-region recordings are still the norm. Although the EC is typically described as a major input structure to the HF, supplying HPC with information that is sent to the SUB, which acts as a major output structure, these regions also receive and send multitudinous other projections, between regions both within and outside the HF (Figure 2; Cappaert et al., 2015). This fact complicates simple models of how goal codes might become transformed and communicated between regions in the HF. Future studies using multi-site recordings or imaging techniques (e.g., Gauthier and Tank, 2018; Shin et al., 2019; Tang et al., 2021) in conjunction with detailed inactivation (e.g., Ito et al., 2015) and/or tracing (e.g., Kitanishi et al., 2021) methods will help shed light on these questions. 

Another future challenge pertains to the fact that the commonly described spatial cells in the HF (highlighted 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 413 

Review 

## **ll** 

**==> picture [324 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A C<br>**----- End of picture text -----**<br>


Figure 7. Goal-related representations predicted during different phases of navigation based on current findings The predicted goal-related representations are illustrated using a place navigation task (see Figure 1). 

(A) When the spatial-planning demand is high, replay events in CA1 may aid navigation by representing routes toward the current goal (e.g., Pfeiffer and Foster, 2013; Xu et al., 2019, but also see Gillespie et al., 2021), using input from CA3 (Middleton and McHugh, 2016; Nakashiba et al., 2009). Entorhinal cortex (EC) and subiculum (SUB) may also shift to represent allocentric goal direction, aiding goal setting and planning (Chadwick et al., 2015; Shine et al., 2019). (B) During goal-directed locomotion, theta sequences in both CA1 (Amemiya and Redish, 2016; Kay et al., 2020; Papale et al., 2016; Tang et al., 2021; Wang et al., 2020) and CA3 (Johnson and Redish, 2007) may cycle between representing possible future routes or heading directions, especially during deliberation and/or uncertainty but may also preferentially represent the future route during periods of low uncertainty (Amemiya and Redish, 2016; Johnson and Redish, 2007; Papale et al., 2016). Neural representations of egocentric distance and direction to goal may be widespread in the hippocampal formation, having 

been reported in the hippocampus (HPC), SUB, and EC (e.g., Aoki et al., 2019; Howard et al., 2014; Ormond and O’Keefe, 2021; Sarel et al., 2017; Spiers and Maguire, 2007). We predict that these representations become especially important in tasks where memory of the goal location guides navigation. Lastly, if goaldirected routes become repeated (not shown), trajectory-dependent firing (i.e., ‘‘splitter’’ activity) may emerge in CA1 (Frank et al., 2000; Wood et al., 2000), mEC (Frank et al., 2000), and SUB (Kitanishi et al., 2021), enabling spatial-memory representations of different routes to become orthogonalized, thereby aiding egocentric-based navigation. (C) When novel goal-directed routes need to be continuously determined toward a remembered goal, spatial cells do not overrepresent goal locations (e.g., Hok et al., 2007a; Pfeiffer and Foster, 2013). This phenomenon has instead been reported in some tasks where goal-directed routes become repeated (not shown), for both mEC grid cells (Boccara et al., 2019) and CA1 (but not CA3; Dupret et al., 2010; Gauthier and Tank, 2018; Hollup et al., 2001b) and SUB place cells (Gauthier and Tank, 2018). Increased peak firing rate of grid cells and increased spatial tuning of non-grid spatial cells proximal to the goal (Butler et al., 2019), as well as extra-field firing of CA1 and CA3 place cells (e.g., Duvelle et al., 2019; Hok et al., 2007a) after arrival at the goal, may instead provide a confirmation-of-arrival signal. CA1 place cells also do not replay the just-taken route after arrival at the goal, because learning specific routes does not aid future navigation in this type of task. This phenomenon has instead been noted in tasks where optimal routes can be learned over time, leading to route repetition and behavioral stereotypy (e.g., Ambrose et al., 2016; Bhattarai et al., 2020; Singer and Frank, 2009). 

in: "Spatially tuned neurons in the hippocampal formation") may not form as functionally discrete cell classes as is often described, given their propensity for mixed or dedicated tuning to various spatial and non-spatial variables (e.g., Hardcastle et al., 2017; Stefanini et al., 2020). Indeed, although allocentric spatial location (within a specific context) typically appears as the main factor governing the activity of HPC place cells and EC grid cells, we have highlighted that these cells can also show mixed tuning to goal locations (e.g., goal-direction tuning in place cells, cf. Aoki et al., 2019). It remains a challenge to control all potential parameters influencing the tuning of spatial cells, and there is a risk that non-controlled parameters act as confounds, leading to wrongful interpretations. Besides mixed tuning, studies have also claimed to find cells with dedicated tuning related to goal locations (e.g., dedicated goal-direction cells, cf. Sarel et al., 2017). Although the same interpretative difficulties exist for these cells, it remains possible that there exists a distribution of goal tuning in single cells, ranging from fully dedicated goal tuning to mixed goal-and-‘‘other’’ tuning to fully dedicated ‘‘other’’ tuning. Whether the mammalian brain handles these codes differently, such as projecting to different targets, is currently not known. Besides excitatory principal cells, both inhibitory interneurons (Turi et al., 2019) and glial cells in the HPC (Doron et al., 2021) may also aid in represent- 

ing goal-related spatial information, which requires further investigation. 

Relatedly, although most animal studies infer goal-related representations from single-cell tuning properties or other microcircuit mechanisms, most human studies rely on macroscale hemodynamic activations recorded using fMRI. Indeed, in humans, many neural computations underlying higher-order cognitive functions and representations are described at the ensemble, rather than the single-cell, level (e.g., Yuste, 2015). This suggests that information about goal locations might be represented across different neural scales. If so, this begs the question of whether goal representations present in larger-scale population or smaller-scale multi-neuron activity patterns might have been overlooked in studies investigating only single-cell dynamics, as has been suggested by recent studies (El-Gaby et al., 2021; Jarzebowski et al., 2022; Nieh et al., 2021). 

A fundamental challenge for investigating goal-related representations also pertains to the potential nature of such representations. For example, there might exist some neural activity that becomes engaged whenever an animal activates a spatial memory representation of a goal for guiding navigation. This has received support in both humans studies, as single cells or patterns of fMRI activity normally active at the goal can become reactive when thinking about this site (e.g., Brown et al., 2016; 

414 Neuron 110, February 2, 2022 

## Review 

Miller et al., 2013), and in rodent studies, as re-activating place cells normally active at the goal elsewhere elicits goal-associated licking behaviors (Robinson et al., 2020). However, if this mnemonic goal representation becomes activated at varying phases and times of navigation, and thus locations in the environment, the associated neural activity would likely appear ‘‘untuned’’ in both the spatial and temporal domains. Given this investigative difficulty, it has been suggested elsewhere that discovered goal representations may only in an indirect manner, and not in a direct and ongoing basis, represent information about goals (Poucet and Hok, 2017). Using clever experimental designs and analyses methods, which allow estimations of task engagement and cognitive demands on a moment-bymoment basis, may help unravel when such potentially elusive goal representations are likely to be activated. 

Lastly, it remains a challenge to separate neural representations relating to the goal itself, from representations relating to the reward at the goal (e.g., reward identity, expectation of reward, receipt of reward, etc.)—particularly as it is currently not known to what extent the mammalian brain differentially represents these variables (Sosa and Giocomo, 2021). Only a few animal studies to date have used tasks where a goal location is separated from a rewarded location (e.g., Duvelle et al., 2019; Hayashi et al., 2016; Hok et al., 2007a, 2007b, 2013), and similar approaches may prove beneficial for future studies interested in investigating goal representations. 

## Concluding remarks 

There has been a wide variety of discoveries in recent years that provide insights into how the HF might support spatial navigation. Evidence suggests that far from being a simple map to be readout for downstream regions performing goal coding, activity in the HF also becomes modulated in a variety of ways by goal locations, but this may depend on multiple parameters both internal (e.g., task engagement and uncertainty) and external (e.g., type of task and environmental constraints). There is much we stand to gain in the coming years with advances in methods and with a deeper appreciation of the behaviors and cognitive demands involved in different types and phases of navigation. 

## ACKNOWLEDGMENTS 

This work was supported by a European Union’s Horizon 2020 Framework Programme for Research under a Marie Sk1odowska-Curie Innovative Training Network grant (EU-M-GATE 765549) to H.J.S. and a Wellcome Senior Research Fellowship grant (212281/Z/18/Z) to C.B. We thank Neil Burgess, Kate Jeffery, and Roddy Grieves for comments on the initial manuscript. We apologize to authors whose relevant work we might have missed or been unable to cite due to space restrictions. 

## REFERENCES 

Ainge, J.A., van der Meer, M.A.A., Langston, R.F., and Wood, E.R. (2007b). Exploring the role of context-dependent hippocampal activity in spatial alternation behavior. Hippocampus 17, 988–1002. 

Ainge, J.A., Tamosiunaite, M., Woergoetter, F., and Dudchenko, P.A. (2007a). Hippocampal CA1 place cells encode intended destination on a maze with multiple choice points. J. Neurosci. 27, 9769–9779. 

Ainge, J.A., Tamosiunaite, M., Wo¨ rgo¨ tter, F., and Dudchenko, P.A. (2012). Hippocampal place cells encode intended destination, and not a discriminative stimulus, in a conditional T-maze task. Hippocampus 22, 534–543. 

## **ll** 

Ainsworth, A., Gaffan, G.D., O’Keefe, J., and Sampson, R. (1969). A technique for recording units in the medulla of the awake, freely moving rat. J. Physiol. 202, 80P–82P. 

Ambrose, R.E., Pfeiffer, B.E., and Foster, D.J. (2016). Reverse replay of hippocampal place cells is uniquely modulated by changing reward. Neuron 91, 1124–1136. 

Amemiya, S., and Redish, A.D. (2016). Manipulating decisiveness in decision making: effects of clonidine on hippocampal search strategies. J. Neurosci. 36, 814–827. 

Aoki, Y., Igata, H., Ikegaya, Y., and Sasaki, T. (2019). The integration of goaldirected signals onto spatial maps of hippocampal place cells. Cell Rep 27, 1516–1527.e5. 

Arleo, A., and Rondi-Reig, L. (2007). Multimodal sensory integration and concurrent navigation strategies for spatial cognition in real and artificial organisms. J. Integr. Neurosci. 6, 327–366. 

Aronov, D., Nevers, R., and Tank, D.W. (2017). Mapping of a non-spatial dimension by the hippocampal-entorhinal circuit. Nature 543, 719–722. 

Asem, J.S.A., and Holland, P.C. (2013). Immediate response strategy and shift to place strategy in submerged T-maze. Behav. Neurosci. 127, 854–859. 

Baeg, E.H., Kim, Y.B., Huh, K., Mook-Jung, I., Kim, H.T., and Jung, M.W. (2003). Dynamics of population code for working memory in the prefrontal cortex. Neuron 40, 177–188. 

Balaguer, J., Spiers, H., Hassabis, D., and Summerfield, C. (2016). Neural mechanisms of hierarchical planning in a virtual subway network. Neuron 90, 893–903. 

Banino, A., Barry, C., Uria, B., Blundell, C., Lillicrap, T., Mirowski, P., Pritzel, A., Chadwick, M.J., Degris, T., Modayil, J., et al. (2018). Vector-based navigation using grid-like representations in artificial agents. Nature 557, 429–433. 

Barlow, J.S. (1964). Inertial navigation as a basis for animal navigation. J. Theor. Biol. 6, 76–117. 

Barry, C., Lever, C., Hayman, R., Hartley, T., Burton, S., O’Keefe, J., Jeffery, K., and Burgess, N. (2006). The boundary vector cell model of place cell firing and spatial memory. Rev. Neurosci. 17, 71–97. 

Basu, R., Gebauer, R., Herfurth, T., Kolb, S., Golipour, Z., Tchumatchenko, T., and Ito, H.T. (2021). The orbitofrontal cortex maps future navigational goals. Nature 599, 449–452. 

Behrens, T.E.J., Muller, T.H., Whittington, J.C.R., Mark, S., Baram, A.B., Stachenfeld, K.L., and Kurth-Nelson, Z. (2018). What is a cognitive map? Organizing knowledge for flexible behavior. Neuron 100, 490–509. 

Bellmund, J.L., Deuker, L., Navarro Schro¨ der, T., and Doeller, C.F. (2016). Grid-cell representations in mental simulation. Elife 5, e17089. 

Bellmund, J.L.S., de Cothi, W., Ruiter, T.A., Nau, M., Barry, C., and Doeller, C.F. (2020). Deforming the metric of cognitive maps distorts memory. Nat. Hum. Behav. 4, 177–188. 

Bellmund, J.L.S., Gardenfors,€ P., Moser, E.I., and Doeller, C.F. (2018). Navigating cognition: spatial codes for human thinking. Science 362, eaat6766. 

Berners-Lee, A., Wu, X., and Foster, D.J. (2021). Prefrontal cortical neurons are selective for non-local hippocampal representations during replay and behavior. J. Neurosci. 41, 5894–5908. 

Bhattarai, B., Lee, J.W., and Jung, M.W. (2020). Distinct effects of reward and navigation history on hippocampal forward and reverse replays. Proc. Natl. Acad. Sci. USA 117, 689–697. 

Bi, G.Q., and Poo, M.M. (1998). Synaptic modifications in cultured hippocampal neurons: dependence on spike timing, synaptic strength, and postsynaptic cell type. J. Neurosci. 18, 10464–10472. 

Bilkey, D.K., and Clearwater, J.M. (2005). The dynamic nature of spatial encoding in the hippocampus. Behav. Neurosci. 119, 1533–1545. 

Bliss, T.V., and Lomo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. J. Physiol. 232, 331–356. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 415 

Review 

## **ll** 

Blodgett, H. (1929). The effects of the introduction of reward upon the maze performance of rats. Univ. Calif. Publ. Psychol. 4, 113–134. 

Blum, K.I., and Abbott, L.F. (1996). A model of spatial map formation in the hippocampus of the rat. Neural Comput 8, 85–93. 

Boccara, C.N., Nardin, M., Stella, F., O’Neill, J., and Csicsvari, J. (2019). The entorhinal cognitive map is attracted to goals. Science 363, 1443–1447. 

Boccara, C.N., Sargolini, F., Thoresen, V.H., Solstad, T., Witter, M.P., Moser, E.I., and Moser, M.-B. (2010). Grid cells in pre- and parasubiculum. Nat. Neurosci. 13, 987–994. 

Bo¨ hm, C., and Lee, A.K. (2020). Canonical goal-selective representations are absent from prefrontal cortex in a spatial working memory task requiring behavioral flexibility. Elife 9, e63035. Bourboulou, R., Marti, G., Michon, F.-X., El Feghaly, E., Nouguier, M., Robbe, D., Koenig, J., and Epsztein, J. (2019). Dynamic control of hippocampal spatial coding resolution by local visual cues. Elife 8, e44487. Bower, M.R., Euston, D.R., and McNaughton, B.L. (2005). Sequential-contextdependent hippocampal activity is not necessary to learn sequences with repeated elements. J. Neurosci. 25, 1313–1323. Bradfield, L.A., and Hart, G. (2020). Rodent medial and lateral orbitofrontal cortices represent unique components of cognitive maps of task space. Neurosci. Biobehav. Rev. 108, 287–294. Breese, C.R., Hampson, R.E., and Deadwyler, S.A. (1989). Hippocampal place cells: stereotypy and plasticity. J. Neurosci. 9, 1097–1111. Brown, M.A., and Sharp, P.E. (1995). Simulation of spatial learning in the Morris water maze by a neural network model of the hippocampal formation and nucleus accumbens. Hippocampus 5, 171–188. Brown, T.I., Carr, V.A., LaRocque, K.F., Favila, S.E., Gordon, A.M., Bowles, B., Bailenson, J.N., and Wagner, A.D. (2016). Prospective representation of navigational goals in the human hippocampus. Science 352, 1323–1326. Brunec, I.K., Javadi, A.-H., Zisch, F.E.L., and Spiers, H.J. (2017). Contracted time and expanded space: the impact of circumnavigation on judgements of space and time. Cognition 166, 425–432. Burgess, N., Donnett, J.G., Jeffery, K.J., and O’Keefe, J. (1997). Robotic and neuronal simulation of the hippocampus and rat navigation. Philos. Trans. R. Soc. Lond. B Biol. Sci. 352, 1535–1543. Burgess, N., and O’Keefe, J. (1996). Neuronal computations underlying the firing of place cells and their role in navigation. Hippocampus 6, 749–762. Burgess, N., Recce, M., and O’Keefe, J. (1994). A model of hippocampal function. Neural Netw 7, 1065–1081. 

Bush, D., Barry, C., Manson, D., and Burgess, N. (2015). Using grid cells for navigation. Neuron 87, 507–520. Butler, W.N., Hardcastle, K., and Giocomo, L.M. (2019). Remembered reward locations restructure entorhinal spatial maps. Science 363, 1447–1452. Butler, W.N., Smith, K.S., van der Meer, M.A.A., and Taube, J.S. (2017). The head-direction signal plays a functional role as a neural compass during navigation. Curr. Biol. 27, 1259–1267. 

Buzsa´ ki, G. (2015). Hippocampal sharp wave-ripple: a cognitive biomarker for episodic memory and planning. Hippocampus 25, 1073–1188. 

Byers, K.A., Lee, M.J., Patrick, D.M., and Himsworth, C.G. (2019). Rats about town: a systematic review of rat movement in urban ecosystems. Front. Ecol. Evol. 7. https://doi.org/10.3389/fevo.2019.00013. 

Byrne, P., Becker, S., and Burgess, N. (2007). Remembering the past and imagining the future: a neural model of spatial memory and imagery. Psychol. Rev. 114, 340–375. 

Cappaert, N.L.M., Van Strien, N.M., and Witter, M.P. (2015). Chapter 20. Hippocampal formation. In The Rat Nervous System, G. Paxinos, ed. (Academic Press), pp. 511–573. 

Carey, A.A., Tanaka, Y., and van der Meer, M.A.A. (2019). Reward revaluation biases hippocampal replay content away from the preferred outcome. Nat. Neurosci. 22, 1450–1459. 

Chadwick, M.J., Jolly, A.E.J., Amos, D.P., Hassabis, D., and Spiers, H.J. (2015). A goal direction signal in the human entorhinal/subicular region. Curr. Biol. 25, 87–92. 

Cheng, S., and Frank, L.M. (2008). New experiences enhance coordinated neural activity in the hippocampus. Neuron 57, 303–313. 

Chrastil, E.R., Sherrill, K.R., Hasselmo, M.E., and Stern, C.E. (2015). There and back again: hippocampus and retrosplenial cortex track homing distance during human path integration. J. Neurosci. 35, 15442–15452. 

Ciocchi, S., Passecker, J., Malagon-Vina, H., Mikus, N., and Klausberger, T. (2015). Brain computation. Selective information routing by ventral hippocampal CA1 projection neurons. Science 348, 560–563. 

Claudi, F., Tyson, A.L., Petrucco, L., Margrie, T.W., Portugues, R., and Branco, T. (2021). Visualizing anatomically registered data with brainrender. Elife 10, e65751. 

Cox, J., and Witten, I.B. (2019). Striatal circuits for reward learning and decision-making. Nat. Rev. Neurosci. 20, 482–494. 

Danielson, N.B., Zaremba, J.D., Kaifosh, P., Bowler, J., Ladow, M., and Losonczy, A. (2016). Sublayer-specific coding dynamics during spatial navigation and learning in hippocampal area CA1. Neuron 91, 652–665. 

Dayan, P. (1991). Navigating through temporal difference. In Advances in Neural Information Processing Systems (Morgan-Kaufmann)), pp. 464–470. 

Dayan, P. (1993). Improving generalization for temporal difference learning: the successor representation. Neural Computation 5, 613–624. 

de Cothi, W., and Barry, C. (2020). Neurobiological successor features for spatial navigation. Hippocampus 30, 1347–1355. 

de Cothi, W., Nyberg, N., Griesbauer, E.-M., Ghaname´ , C., Zisch, F., Lefort, J., Fletcher, L., Newton, C., Renaudineau, S., Bendor, D., et al. (2021). Predictive maps in rats and humans for spatial navigation: the successor representation explains flexible behaviour. bioRxiv. https://doi.org/10.1101/2020.09.26. 314815. 

de Laville´ on, G., Lacroix, M.M., Rondi-Reig, L., and Benchenane, K. (2015). Explicit memory creation during sleep demonstrates a causal role of place cells in navigation. Nat. Neurosci. 18, 493–495. 

Devan, B.D., Hong, N.S., and McDonald, R.J. (2011). Parallel associative processing in the dorsal striatum: segregation of stimulus–response and cognitive control subregions. Neurobiol. Learn. Mem. 96, 95–120. 

Devan, B.D., and White, N.M. (1999). Parallel information processing in the dorsal striatum: relation to hippocampal function. J. Neurosci. 19, 2789–2798. 

Diba, K., and Buzsa´ ki, G. (2007). Forward and reverse hippocampal place-cell sequences during ripples. Nat. Neurosci. 10, 1241–1242. 

Doron, A., Rubin, A., Benmelech-Chovav, A., Benaim, N., Carmi, T., Kreisel, T., Ziv, Y., and Goshen, I. (2021). Hippocampal astrocytes encode reward location. bioRxiv. https://doi.org/10.1101/2021.07.07.451434. 

Dragoi, G., and Buzsa´ ki, G. (2006). Temporal encoding of place sequences by hippocampal cell assemblies. Neuron 50, 145–157. 

Dragoi, G., and Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. Nature 469, 397–401. 

Drieu, C., and Zugaro, M. (2019). Hippocampal sequences during exploration: mechanisms and functions. Front. Cell. Neurosci. 13, 232. 

Dudchenko, P.A., and Wood, E.R. (2014). Splitter cells: hippocampal place cells whose firing is modulated by where the animal is going or where it has been. In Space,Time and Memory in the Hippocampal Formation, D. Derdikman and J.J. Knierim, eds. (Springer), pp. 253–272. 

Dupret, D., O’Neill, J., Pleydell-Bouverie, B., and Csicsvari, J. (2010). The reorganization and reactivation of hippocampal maps predict spatial memory performance. Nat. Neurosci. 13, 995–1002. 

Duvelle, E[´ ] ., Grieves, R.M., Hok, V., Poucet, B., Arleo, A., Jeffery, K.J., and Save, E. (2019). Insensitivity of place cells to the value of spatial goals in a two-choice flexible navigation task. J. Neurosci. 39, 2522–2541. 

416 Neuron 110, February 2, 2022 

**ll** 

## Review 

Duvelle, E[´ ] ., Grieves, R.M., Liu, A., Jedidi-Ayoub, S., Holeniewska, J., Harris, A., Nyberg, N., Donnarumma, F., Lefort, J.M., Jeffery, K.J., et al. (2021). Hippocampal place cells encode global location but not connectivity in a complex space. Curr. Biol. 31, 1221–1233.e9. 

Edvardsen, V., Bicanski, A., and Burgess, N. (2020). Navigating with grid and place cells in cluttered environments. Hippocampus 30, 220–232. 

Ego-Stengel, V., and Wilson, M.A. (2010). Disruption of ripple-associated hippocampal activity during rest impairs spatial learning in the rat. Hippocampus 20, 1–10. 

Fyhn, M., Molden, S., Hollup, S., Moser, M.-B., and Moser, E.I. (2002). Hippocampal neurons responding to first-time dislocation of a target object. Neuron 35, 555–566. 

Fyhn, M., Molden, S., Witter, M.P., Moser, E.I., and Moser, M.-B. (2004). Spatial representation in the entorhinal cortex. Science 305, 1258–1264. 

Gahnstrom, C.J., and Spiers, H.J. (2020). Striatal and hippocampal contributions to flexible navigation in rats and humans. Brain Neurosci. Adv. 4, 2398212820979772. 

**==> picture [46 x 35] intentionally omitted <==**

Gallistel, C.R. (1990). The Organization of Learning (The MIT Press). 

Eichenbaum, H. (2017). On the integration of space, time, and memory. Neuron 95, 1007–1018. 

Eichenbaum, H., Kuperstein, M., Fagan, A., and Nagode, J. (1987). Cue-sampling and goal-approach correlates of hippocampal unit activity in rats performing an odor-discrimination task. J. Neurosci. 7, 716–732. 

Ekstrom, A.D., Kahana, M.J., Caplan, J.B., Fields, T.A., Isham, E.A., Newman, E.L., and Fried, I. (2003). Cellular networks underlying human spatial navigation. Nature 425, 184–188. Ekstrom, A.D., Spiers, H.J., Bohbot, V.D., and Rosenbaum, R.S. (2018). Human Spatial Navigation (Princeton University Press). 

El-Gaby, M., Reeve, H.M., Lopes-dos-Santos, V., Campo-Urriza, N., Perestenko, P.V., Morley, A., Strickland, L.A.M., Luka´ cs, I.P., Paulsen, O., and Dupret, D. (2021). An emergent neural coactivity code for dynamic memory. Nat. Neurosci. 24, 694–704. 

Epstein, R.A., Patai, E.Z., Julian, J.B., and Spiers, H.J. (2017). The cognitive map in humans: spatial navigation and beyond. Nat. Neurosci. 20, 1504–1513. Erdem, U.M., and Hasselmo, M. (2012). A goal-directed spatial navigation model using forward trajectory planning based on grid cells. Eur. J. Neurosci. 35, 916–931. Erdem, U.M., and Hasselmo, M.E. (2014). A biologically inspired hierarchical goal directed navigation model. J. Physiol. Paris 108, 28–37. 

Esteves, I.M., Chang, H., Neumann, A.R., Sun, J., Mohajerani, M.H., and McNaughton, B.L. (2021). Spatial information encoding across multiple neocortical regions depends on an intact hippocampus. J. Neurosci. 41, 307–319. 

Etienne, A.S., and Jeffery, K.J. (2004). Path integration in mammals. Hippocampus 14, 180–192. 

Feierstein, C.E., Quirk, M.C., Uchida, N., Sosulski, D.L., and Mainen, Z.F. (2006). Representation of spatial goals in rat orbitofrontal cortex. Neuron 51, 495–507. 

Ferbinteanu, J., and Shapiro, M.L. (2003). Prospective and retrospective memory coding in the hippocampus. Neuron 40, 1227–1239. Ferbinteanu, J., Shirvalkar, P., and Shapiro, M.L. (2011). Memory modulates journey-dependent coding in the rat hippocampus. J. Neurosci. 31, 9135–9146. Fiete, I.R., Burak, Y., and Brookings, T. (2008). What grid cells convey about rat location. J. Neurosci. 28, 6858–6871. 

Foster, D.J., Morris, R.G., and Dayan, P. (2000). A model of hippocampally dependent navigation, using the temporal difference learning rule. Hippocampus 10, 1–16. 

Foster, D.J., and Wilson, M.A. (2006). Reverse replay of behavioural sequences in hippocampal place cells during the awake state. Nature 440, 680–683. 

Foster, D.J., and Wilson, M.A. (2007). Hippocampal theta sequences. Hippocampus 17, 1093–1099. 

Fouquet, C., Babayan, B.M., Watilliaux, A., Bontempi, B., Tobin, C., and Rondi-Reig, L. (2013). Complementary roles of the hippocampus and the dorsomedial striatum during spatial and sequence-based navigation behavior. PLoS One 8, e67232. 

Frank, L.M., Brown, E.N., and Wilson, M. (2000). Trajectory encoding in the hippocampus and entorhinal cortex. Neuron 27, 169–178. 

Gauthier, J.L., and Tank, D.W. (2018). A dedicated population for reward coding in the hippocampus. Neuron 99, 179–193, e7. 

Geerts, J.P., Chersi, F., Stachenfeld, K.L., and Burgess, N. (2020). A general model of hippocampal and dorsal striatal learning and decision making. Proc. Natl. Acad. Sci. USA 117, 31427–31437. 

Genzel, L., Dragoi, G., Frank, L., Ganguly, K., de la Prida, L., Pfeiffer, B., and Robertson, E. (2020). A consensus statement: defining terms for reactivation analysis. Philos. Trans. R. Soc. Lond. B Biol. Sci. 375, 20200001. 

Gershman, S.J. (2018). The successor representation: its computational logic and neural substrates. J. Neurosci. 38, 7193–7200. 

Gillespie, A.K., Astudillo Maya, D.A., Denovellis, E.L., Liu, D.F., Kastner, D.B., Coulter, M.E., Roumis, D.K., Eden, U.T., and Frank, L.M. (2021). Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice. Neuron 109, 3149–3163.e6. 

Girardeau, G., Benchenane, K., Wiener, S.I., Buzsa´ ki, G., and Zugaro, M.B. (2009). Selective suppression of hippocampal ripples impairs spatial memory. Nat. Neurosci. 12, 1222–1223. 

Gomperts, S.N., Kloosterman, F., and Wilson, M.A. (2015). VTA neurons coordinate with the hippocampal reactivation of spatial experience. Elife 4, e05360. Goodman, J. (2021). Place vs. response learning: history, controversy, and neurobiology. Front. Behav. Neurosci. 14, 598570. 

Gothard, K.M., Skaggs, W.E., and McNaughton, B.L. (1996). Dynamics of mismatch correction in the hippocampal ensemble code for space: interaction between path integration and environmental cues. J. Neurosci. 16, 8027–8040. 

Green, S.J., Boruff, B.J., and Grueter, C.C. (2019). Chimpanzees use advanced spatial cognition to plan least-cost routes. bioRxiv. https://doi. org/10.1101/793562. 

Gridchyn, I., Schoenenberger, P., O’Neill, J., and Csicsvari, J. (2020). Assembly-specific disruption of hippocampal replay leads to selective memory deficit. Neuron 106, 291–300.e6. 

Grieves, R.M., Duvelle, E[´ ] ., and Dudchenko, P.A. (2018). A boundary vector cell model of place field repetition. Spat. Cogn. Comput. 18, 217–256. 

Grieves, R.M., and Jeffery, K.J. (2017). The representation of space in the brain. Behav. Processes 135, 113–131. 

Grieves, R.M., Wood, E.R., and Dudchenko, P.A. (2016). Place cells on a maze encode routes rather than destinations. Elife 5, e15986. 

Grosmark, A.D., and Buzsa´ ki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443. 

Gupta, A.S., van der Meer, M.A.A., Touretzky, D.S., and Redish, A.D. (2010). Hippocampal replay is not a simple function of experience. Neuron 65, 695–705. 

Gupta, A.S., van der Meer, M.A.A., Touretzky, D.S., and Redish, A.D. (2012). Segmentation of spatial experience by hippocampal q sequences. Nat. Neurosci. 15, 1032–1039. 

Gustafson, N.J., and Daw, N.D. (2011). Grid cells, place cells, and geodesic generalization for spatial reinforcement learning. PLoS Comput. Biol. 7, e1002235. 

Hafting, T., Fyhn, M., Molden, S., Moser, M.-B., and Moser, E.I. (2005). Microstructure of a spatial map in the entorhinal cortex. Nature 436, 801–806. 

Neuron 110, February 2, 2022 417 

Review 

## **ll** 

Hardcastle, K., Maheswaranathan, N., Ganguli, S., and Giocomo, L.M. (2017). A multiplexed, heterogeneous, and adaptive code for navigation in medial entorhinal cortex. Neuron 94, 375–387.e7. 

Harten, L., Katz, A., Goldshtein, A., Handel, M., and Yovel, Y. (2020). The ontogeny of a mammalian cognitive map in the real world. Science 369, 194–197. 

Hartley, T., Lever, C., Burgess, N., and O’Keefe, J. (2014). Space in the brain: how the hippocampal formation supports spatial cognition. Philos. Trans. R. Soc. Lond. B Biol. Sci. 369, 20120510. 

Hasz, B.M., and Redish, A.D. (2020). Spatial encoding in dorsomedial prefrontal cortex and hippocampus is related during deliberation. Hippocampus 30, 1194–1208. 

Hayashi, Y., Sawa, A., and Hikida, T. (2016). Impaired hippocampal activity at the goal zone on the place preference task in a DISC1 mouse model. Neurosci. Res. 106, 70–73. 

He, H., Boehringer, R., Huang, A.J.Y., Overton, E.T.N., Polygalov, D., Okanoya, K., and McHugh, T.J. (2021). CA2 inhibition reduces the precision of hippocampal assembly reactivation. Neuron 109, 3674–3687.e7. 

Higgins, C., Liu, Y., Vidaurre, D., Kurth-Nelson, Z., Dolan, R., Behrens, T., and Woolrich, M. (2021). Replay bursts in humans coincide with activation of the default mode and parietal alpha networks. Neuron 109, 882–893.e7. 

Hok, V., Chah, E., Save, E., and Poucet, B. (2013). Prefrontal cortex focally modulates hippocampal place cell firing patterns. J. Neurosci. 33, 3443–3451. 

Hok, V., Lenck-Santini, P.-P., Roux, S., Save, E., Muller, R.U., and Poucet, B. (2007a). Goal-related activity in hippocampal place cells. J. Neurosci. 27, 472–482. 

Hok, V., Lenck-Santini, P.-P., Save, E., Gaussier, P., Banquet, J.-P., and Poucet, B. (2007b). A test of the time estimation hypothesis of place cell goalrelated activity. J. Integr. Neurosci. 6, 367–378. 

Hok, V., Save, E., Lenck-Santini, P.P., and Poucet, B. (2005). Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex. Proc. Natl. Acad. Sci. USA 102, 4602–4607. 

Hollup, S.A., Kjelstrup, K.G., Hoff, J., Moser, M.-B., and Moser, E.I. (2001a). Impaired recognition of the goal location during spatial navigation in rats with hippocampal lesions. J. Neurosci. 21, 4505–4513. 

Hollup, S.A., Molden, S., Donnett, J.G., Moser, M.-B., and Moser, E.I. (2001b). Accumulation of hippocampal place fields at the goal location in an annular Watermaze task. J. Neurosci. 21, 1635–1644. 

Horner, A.J., Bisby, J.A., Zotow, E., Bush, D., and Burgess, N. (2016). Grid-like processing of imagined navigation. Curr. Biol. 26, 842–847. 

Howard, L.R., Javadi, A.H., Yu, Y., Mill, R.D., Morrison, L.C., Knight, R., Loftus, M.M., Staskute, L., and Spiers, H.J. (2014). The hippocampus and entorhinal cortex encode the path and euclidean distances to goals during navigation. Curr. Biol. 24, 1331–1340. 

Igata, H., Ikegaya, Y., and Sasaki, T. (2021). Prioritized experience replays on a hippocampal predictive map for learning. Proc. Natl. Acad. Sci. USA 118, e2011266118. 

Iglo´ i, K., Zaoui, M., Berthoz, A., and Rondi-Reig, L. (2009). Sequential egocentric strategy is acquired as early as allocentric strategy: parallel acquisition of these two navigation strategies. Hippocampus 19, 1199–1211. 

Ito, H.T., Zhang, S.-J., Witter, M.P., Moser, E.I., and Moser, M.-B. (2015). A prefrontal-thalamo-hippocampal circuit for goal-directed spatial navigation. Nature 522, 50–55. 

Jackson, J.C., Johnson, A., and Redish, A.D. (2006). Hippocampal sharp waves and reactivation during awake states depend on repeated sequential experience. J. Neurosci. 26, 12415–12426. 

Jacobs, J., Kahana, M.J., Ekstrom, A.D., Mollison, M.V., and Fried, I. (2010). A sense of direction in human entorhinal cortex. Proc. Natl. Acad. Sci. USA 107, 6487–6492. 

Jacobson, T.K., Gruenbaum, B.F., and Markus, E.J. (2012). Extensive training and hippocampus or striatum lesions: effect on place and response strategies. Physiol. Behav. 105, 645–652. 

Jadhav, S.P., Kemere, C., German, P.W., and Frank, L.M. (2012). Awake hippocampal sharp-wave ripples support spatial memory. Science 336, 1454–1458. 

Jafarpour, A., and Spiers, H. (2017). Familiarity expands space and contracts time. Hippocampus 27, 12–16. 

Jarzebowski, P., Hay, Y.A., Grewe, B.F., and Paulsen, O. (2022). Different encoding of reward location in dorsal and intermediate hippocampus. Curr. Biol. Published online January 10, 2022. https://doi.org/10.1016/j.cub.2021.12.024. 

Jeffery, K.J., Gilbert, A., Burton, S., and Strudwick, A. (2003). Preserved performance in a hippocampal-dependent spatial task despite complete place cell remapping. Hippocampus 13, 175–189. 

Ji, D., and Wilson, M.A. (2007). Coordinated memory replay in the visual cortex and hippocampus during sleep. Nat. Neurosci. 10, 100–107. 

Ji, D., and Wilson, M.A. (2008). Firing rate dynamics in the hippocampus induced by trajectory learning. J. Neurosci. 28, 4679–4689. 

Jin, S.-W., and Lee, I. (2021). Differential encoding of place value between the dorsal and intermediate hippocampus. Curr. Biol. 31, 3053–3072.e5. 

Johnson, A., and Redish, A.D. (2007). Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. J. Neurosci. 27, 12176–12189. 

Kaufman, A.M., Geiller, T., and Losonczy, A. (2020). A role for the locus coeruleus in hippocampal CA1 place cell reorganization during spatial reward learning. Neuron 105, 1018–1026.e4. 

Kay, K., Chung, J.E., Sosa, M., Schor, J.S., Karlsson, M.P., Larkin, M.C., Liu, D.F., and Frank, L.M. (2020). Constant sub-second cyclinG between representations of possible futures in the hippocampus. Cell 180, 552–567.e25. 

Kitanishi, T., Umaba, R., and Mizuseki, K. (2021). Robust information routing by dorsal subiculum neurons. Sci. Adv. 7, eabf1913. 

Kobayashi, T., Nishijo, H., Fukuda, M., Bures, J., and Ono, T. (1997). Taskdependent representations in rat hippocampal place neurons. J. Neurophysiol. 78, 597–613. 

Kobayashi, T., Tran, A.H., Nishijo, H., Ono, T., and Matsumoto, G. (2003). Contribution of hippocampal place cell activity to learning and formation of goal-directed navigation in rats. Neuroscience 117, 1025–1035. 

Kubie, J.L., and Fenton, A.A. (2012). Linear look-ahead in conjunctive cells: an entorhinal mechanism for vector-based navigation. Front. Neural Circuits 6, 20. 

Kunz, L., Wang, L., Lachner-Piza, D., Zhang, H., Brandt, A., Dumpelmann, M.,€ Reinacher, P.C., Coenen, V.A., Chen, D., Wang, W.-X., et al. (2019). Hippocampal theta phases organize the reactivation of large-scale electrophysiological representations during goal-directed navigation. Sci. Adv. 5, eaav8192. 

Lammel, S., Lim, B.K., Ran, C., Huang, K.W., Betley, M.J., Tye, K.M., Deisseroth, K., and Malenka, R.C. (2012). Input-specific control of reward and aversion in the ventral tegmental area. Nature 491, 212–217. 

Lee, A.S., Andre´ , J.M., and Pittenger, C. (2014). Lesions of the dorsomedial striatum delay spatial learning and render cue-based navigation inflexible in a water maze task in mice. Front. Behav. Neurosci. 8, 42. 

Lee, H., Ghim, J.-W., Kim, H., Lee, D., and Jung, M. (2012). Hippocampal neural correlates for values of experienced events. J. Neurosci. 32, 15053–15065. 

Lee, I., Griffin, A.L., Zilli, E.A., Eichenbaum, H., and Hasselmo, M.E. (2006). Gradual translocation of spatial correlates of neuronal firing in the hippocampus toward prospective reward locations. Neuron 51, 639–650. 

Lee, J.S., Briguglio, J.J., Cohen, J.D., Romani, S., and Lee, A.K. (2020). The statistical structure of the hippocampal code for space as a function of time, context, and value. Cell 183, 620–635.e22. 

Lee, S.-H., Huh, N., Lee, J.W., Ghim, J.-W., Lee, I., and Jung, M.W. (2017). Neural signals related to outcome evaluation are stronger in CA1 than CA3. Front. Neural Circuits 11, 40. 

Leutgeb, J.K., Leutgeb, S., Moser, M.-B., and Moser, E.I. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. Science 315, 961–966. 

418 Neuron 110, February 2, 2022 

**ll** 

## Review 

Lever, C., Burton, S., Jeewajee, A., O’Keefe, J., and Burgess, N. (2009). Boundary vector cells in the subiculum of the hippocampal formation. J. Neurosci. 29, 9771–9777. 

Levy, S.J., Kinsky, N.R., Mau, W., Sullivan, D.W., and Hasselmo, M.E. (2021). Hippocampal spatial memory representations in mice are heterogeneously stable. Hippocampus 31, 244–260. Lipton, P.A., White, J.A., and Eichenbaum, H. (2007). Disambiguation of overlapping experiences by neurons in the medial entorhinal cortex. J. Neurosci. 27, 5787–5795. Lisman, J.E., and Grace, A.A. (2005). The hippocampal-VTA loop: controlling the entry of information into long-term memory. Neuron 46, 703–713. Liu, Y., Dolan, R.J., Kurth-Nelson, Z., and Behrens, T.E.J. (2019). Human replay spontaneously reorganizes experience. Cell 178, 640–652.e14. Liu, Y., Mattar, M.G., Behrens, T.E.J., Daw, N.D., and Dolan, R.J. (2021). Experience replay is associated with efficient nonlocal learning. Science 372, eabf1357. Logothetis, N.K., Pauls, J., Augath, M., Trinath, T., and Oeltermann, A. (2001). Neurophysiological investigation of the basis of the fMRI signal. Nature 412, 150–157. Louie, K., and Wilson, M.A. (2001). Temporally structured replay of awake hippocampal ensemble activity during rapid eye movement sleep. Neuron 29, 145–156. Maguire, E.A., Nannery, R., and Spiers, H.J. (2006). Navigation around London by a taxi driver with bilateral hippocampal lesions. Brain 129, 2894–2907. Mamad, O., Stumpp, L., McNamara, H.M., Ramakrishnan, C., Deisseroth, K., Reilly, R.B., and Tsanov, M. (2017). Place field assembly distribution encodes preferred locations. PLoS Biol 15, e2002365. Mao, D., Avila, E., Caziot, B., Laurens, J., Dickman, J.D., and Angelaki, D.E. (2021). Spatial modulation of hippocampal activity in freely moving macaques. Neuron 109, 3521–3534.e6. Mao, D., Neumann, A.R., Sun, J., Bonin, V., Mohajerani, M.H., and McNaughton, B.L. (2018). Hippocampus-dependent emergence of spatial sequence coding in retrosplenial cortex. Proc. Natl. Acad. Sci. USA 115, 8015–8018. Markus, E.J., Qin, Y.L., Leonard, B., Skaggs, W.E., McNaughton, B.L., and Barnes, C.A. (1995). Interactions between location and task affect the spatial and directional firing of hippocampal neurons. J. Neurosci. 15, 7079–7094. Masson, C., and Girard, B. (2011). Decoding the grid cells for metric navigation using the residue numeral system. In Advances in Cognitive Neurodynamics (II), R. Wang and F. Gu, eds. (Springer Netherlands), pp. 459–464. Mattar, M.G., and Daw, N.D. (2018). Prioritized memory access explains planning and hippocampal replay. Nat. Neurosci. 21, 1609–1617. McDonald, R.J., and White, N.M. (1994). Parallel information processing in the water maze: evidence for independent memory systems involving dorsal striatum and hippocampus. Behav. Neural Biol. 61, 260–270. McKenzie, S., Robinson, N.T.M., Herrera, L., Churchill, J.C., and Eichenbaum, H. (2013). Learning causes reorganization of neuronal firing patterns to represent related experiences within a hippocampal schema. J. Neurosci. 33, 10243–10256. McNamara, C.G., Tejero-Cantero, A[´ ] ., Trouche, S., Campo-Urriza, N., and Dupret, D. (2014). Dopaminergic neurons promote hippocampal reactivation and spatial memory persistence. Nat. Neurosci. 17, 1658–1660. McNaughton, B.L. (1989). Neuronal mechanisms for spatial computation and information storage. In Neural Connections, Mental Computation (The MIT Press), pp. 285–350. McNaughton, B.L., O’Keefe, J., and Barnes, C.A. (1983). The stereotrode: a new technique for simultaneous isolation of several single units in the central nervous system from multiple unit records. J. Neurosci. Methods 8, 391–397. Michon, F., Sun, J.-J., Kim, C.Y., Ciliberti, D., and Kloosterman, F. (2019). Post-learning hippocampal replay selectively reinforces spatial memory for highly rewarded locations. Curr. Biol. 29, 1436–1444.e5. 

Middleton, S.J., and McHugh, T.J. (2016). Silencing CA3 disrupts temporal coding in the CA1 ensemble. Nat. Neurosci. 19, 945–951. 

Miller, J.F., Neufang, M., Solway, A., Brandt, A., Trippel, M., Mader, I., Hefft, S., Merkow, M., Polyn, S.M., Jacobs, J., et al. (2013). Neural activity in human hippocampal formation reveals the spatial context of retrieved memories. Science 342, 1111–1114. 

Momennejad, I. (2020). Learning structures: predictive representations, replay, and generalization. Curr. Opin. Behav. Sci. 32, 155–166. 

Momennejad, I., and Howard, M.W. (2018). Predicting the future with multiscale successor representations. bioRxiv. https://doi.org/10.1101/449470. 

Momennejad, I., Russek, E.M., Cheong, J.H., Botvinick, M.M., Daw, N.D., and Gershman, S.J. (2017). The successor representation in human reinforcement learning. Nat. Hum. Behav. 1, 680–692. 

Moore, J.J., Cushman, J.D., Acharya, L., Popeney, B., and Mehta, M.R. (2021). Linking hippocampal multiplexed tuning, Hebbian plasticity and navigation. Nature 599, 442–448. 

Morgan, L.K., Macevoy, S.P., Aguirre, G.K., and Epstein, R.A. (2011). Distances between real-world locations are represented in the human hippocampus. J. Neurosci. 31, 1238–1245. 

Morris, R.G.M., Garrud, P., Rawlins, J.N.P., and O’Keefe, J. (1982). Place Navigation Impaired in Rats with Hippocampal Lesions (McGraw-Hill). 

Muenzinger, K.F., and Gentry, E. (1931). Tone discrimination in white rats. J. Comp. Psychol. 12, 195–206. 

Muir, G.M., and Taube, J.S. (2004). Head direction cell activity and behavior in a navigation task requiring a cognitive mapping strategy. Behav. Brain Res. 153, 249–253. 

Muller, R.U., Stead, M., and Pach, J. (1996). The hippocampus as a cognitive graph. J. Gen. Physiol. 107, 663–694. 

Nakashiba, T., Buhl, D.L., McHugh, T.J., and Tonegawa, S. (2009). Hippocampal CA3 output is crucial for ripple-associated reactivation and consolidation of memory. Neuron 62, 781–787. 

Nieh, E.H., Schottdorf, M., Freeman, N.W., Low, R.J., Lewallen, S., Koay, S.A., Pinto, L., Gauthier, J.L., Brody, C.D., and Tank, D.W. (2021). Geometry of abstract learned knowledge in the hippocampus. Nature 595, 80–84. 

O’Keefe, J. (1976). Place units in the hippocampus of the freely moving rat. Exp. Neurol. 51, 78–109. 

O’Keefe, J. (1990). A computational theory of the hippocampal cognitive map. Prog. Brain Res. 83, 301–312. 

O’Keefe, J. (1991). An allocentric spatial model for the hippocampal cognitive map. Hippocampus 1, 230–235. 

O’Keefe, J., and Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res 34, 171–175. 

O’Keefe, J., and Krupic, J. (2021). Do hippocampal pyramidal cells respond to nonspatial stimuli? Physiol. Rev. 101, 1427–1456. 

O’Keefe, J., and Nadel, L. (1978). The Hippocampus as a Cognitive Map (Oxford: Clarendon Press). 

O’Keefe, J., Nadel, L., Keightley, S., and Kill, D. (1975). Fornix lesions selectively abolish place learning in the rat. Exp. Neurol. 48, 152–166. 

O’Mara, S.M., and Aggleton, J.P. (2019). Space and memory (far) Beyond the hippocampus: many subcortical structures also support cognitive mapping and mnemonic processing. Front. Neural Circuits 13, 52. 

O’Neill, J., Boccara, C.N., Stella, F., Schoenenberger, P., and Csicsvari, J. (2017). Superficial layers of the medial entorhinal cortex replay independently of the hippocampus. Science 355, 184–188. 

O’Neill, J., Senior, T.J., Allen, K., Huxter, J.R., and Csicsvari, J. (2008). Reactivation of experience-dependent cell assembly patterns in the hippocampus. Nat. Neurosci. 11, 209–215. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 419 

Review 

## **ll** 

Okada, S., Igata, H., Sasaki, T., and Ikegaya, Y. (2017). Spatial representation of hippocampal place cells in a T-maze with an aversive stimulation. Front. Neural Circuits 11, 101. 

O[´ ] lafsdo´ ttir, H.F., Barry, C., Saleem, A.B., Hassabis, D., and Spiers, H.J. (2015). Hippocampal place cells construct reward related sequences through unexplored space. Elife 4, e06063. 

O[´ ] lafsdo´ ttir, H.F., Bush, D., and Barry, C. (2018). The role of hippocampal replay in memory and planning. Curr. Biol. 28, R37–R50. 

O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2016). Coordinated grid and place cell replay during rest. Nat. Neurosci. 19, 792–794. 

O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2017). Task demands predict a dynamic switch in the content of awake hippocampal replay. Neuron 96, 925–935.e6. 

Olton, D.S., Branch, M., and Best, P.J. (1978). Spatial correlates of hippocampal unit activity. Exp. Neurol. 58, 387–409. 

Ormond, J., and O’Keefe, J. (2021). Hippocampal place cells use vector computations to navigate. bioRxiv. https://doi.org/10.1101/2021.06.23.449621. 

Otmakhova, N., Duzel, E., Deutch, A.Y., and Lisman, J. (2013). The hippocampal-VTA loop: the role of novelty and motivation in controlling the entry of information into long-term memory. In Intrinsically Motivated Learning in Natural and Artificial Systems, G. Baldassarre and M. Mirolli, eds. (Springer), pp. 235–254. 

Packard, M.G., and McGaugh, J.L. (1996). Inactivation of hippocampus or caudate nucleus with lidocaine differentially affects expression of place and response learning. Neurobiol. Learn. Mem. 65, 65–72. 

Papale, A.E., Zielinski, M.C., Frank, L.M., Jadhav, S.P., and Redish, A.D. (2016). Interplay between hippocampal sharp-wave-ripple events and vicarious trial and error behaviors in decision making. Neuron 92, 975–982. 

Park, S.A., Miller, D.S., Nili, H., Ranganath, C., and Boorman, E.D. (2020). Map making: constructing, combining, and inferring on abstract cognitive maps. Neuron 107, 1226–1238.e8. 

Pastalkova, E., Itskov, V., Amarasingham, A., and Buzsa´ ki, G. (2008). Internally generated cell assembly sequences in the rat hippocampus. Science 321, 1322–1327. 

Patai, E.Z., Javadi, A.-H., Ozubko, J.D., O’Callaghan, A., Ji, S., Robin, J., Grady, C., Winocur, G., Rosenbaum, R.S., Moscovitch, M., and Spiers, H.J. (2019). Hippocampal and retrosplenial goal distance coding after long-term consolidation of a real-world environment. Cereb. Cortex 29, 2748–2758. 

Patai, E.Z., and Spiers, H.J. (2021). The versatile wayfinder: prefrontal contributions to spatial navigation. Trends Cogn. Sci. 25, 520–533. 

Pfeiffer, B.E. (2020). The content of hippocampal ‘‘replay. Hippocampus 30, 6–18. 

Pfeiffer, B.E., and Foster, D.J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. Nature 497, 74–79. 

Poucet, B. (1993). Spatial cognitive maps in animals: new hypotheses on their structure and neural mechanisms. Psychol. Rev. 100, 163–182. 

Poucet, B., and Hok, V. (2017). Remembering goal locations. Curr. Opin. Behav. Sci. 17, 51–56. 

Qasim, S.E., Fried, I., and Jacobs, J. (2021). Phase precession in the human hippocampus and entorhinal cortex. Cell 184, 3242–3255.e10. 

Quirk, G.J., Muller, R.U., Kubie, J.L., and Ranck, J.B. (1992). The positional firing properties of medial entorhinal neurons: description and comparison with hippocampal place cells. J. Neurosci. 12, 1945–1963. 

Recce, M., and Harris, K.D. (1996). Memory for places: a navigational model in support of Marr’s theory of hippocampal function. Hippocampus 6, 735–748. 

Redish, A.D. (1999). Beyond the Cognitive Map: From Place Cells to Episodic Memory (MIT Press). 

Redish, A.D. (2016). Vicarious trial and error. Nat. Rev. Neurosci. 17, 147–159. 

Redish, A.D., and Touretzky, D.S. (1998). The role of the hippocampus in solving the Morris water maze. Neural Comput 10, 73–111. 

Robinson, N.T.M., Descamps, L.A.L., Russell, L.E., Buchholz, M.O., Bicknell, B.A.,Hausser,€ Antonov,M. (2020).G.K.,TargetedLau, J.Y.N.,activationNutbrown,of hippocampalR., Schmidt-Hieber,place cellsC.,drivesand memory-guided spatial behavior. Cell 183, 1586–1599.e10. 

Rondi-Reig, L., Petit, G.H., Tobin, C., Tonegawa, S., Mariani, J., and Berthoz, A. (2006). Impaired sequential egocentric and allocentric memories in forebrain-specific–NMDA receptor knock-out mice during a new task dissociating strategies of navigation. J. Neurosci. 26, 4071–4081. 

Rosenbaum, R.S., Gao, F., Richards, B., Black, S.E., and Moscovitch, M. (2005b). ‘‘Where to?’’ remote memory for spatial relations and landmark identity in former taxi drivers with Alzheimer’s disease and encephalitis. J. Cogn. Neurosci. 17, 446–462. 

Rosenbaum, R.S., Ko¨ hler, S., Schacter, D.L., Moscovitch, M., Westmacott, R., Black, S.E., Gao, F., and Tulving, E. (2005a). The case of K.C.: contributions of a memory-impaired person to memory theory. Neuropsychologia 43, 989–1021. 

Rueckemann, J.W., and Buffalo, E.A. (2017). Spatial responses, immediate experience, and memory in the monkey hippocampus. Curr. Opin. Behav. Sci. 17, 155–160. 

Russek, E.M., Momennejad, I., Botvinick, M.M., Gershman, S.J., and Daw, N.D. (2017). Predictive representations can link model-based reinforcement learning to model-free mechanisms. PLoS Comput. Biol. 13, e1005768. 

Sanders, H., Wilson, M.A., and Gershman, S.J. (2020). Hippocampal remapping as hidden state inference. Elife 9, e51140. 

Sanguinetti-Scheck, J.I., and Brecht, M. (2020). Home, head direction stability, and grid cell distortion. J. Neurophysiol. 123, 1392–1406. 

Sarel, A., Finkelstein, A., Las, L., and Ulanovsky, N. (2017). Vectorial representation of spatial goals in the hippocampus of bats. Science 355, 176–180. 

Sargolini, F., Fyhn, M., Hafting, T., McNaughton, B.L., Witter, M.P., Moser, M.B., and Moser, E.I. (2006). Conjunctive representation of position, direction, and velocity in entorhinal cortex. Science 312, 758–762. 

Sato, M., Kawano, M., Mizuta, K., Islam, T., Lee, M.G., and Hayashi, Y. (2017). Hippocampus-dependent goal localization by head-fixed mice in virtual reality. eNeuro 4, ENEURO.0369-16.2017. 

Sato, M., Mizuta, K., Islam, T., Kawano, M., Sekine, Y., Takekawa, T., GomezDominguez, D., Schmidt, A., Wolf, F., Kim, K., et al. (2020). Distinct mechanisms of over-representation of landmarks and rewards in the hippocampus. Cell Rep 32, 107864. 

Savelli, F., Yoganarasimha, D., and Knierim, J.J. (2008). Influence of boundary removal on the spatial representations of the medial entorhinal cortex. Hippocampus 18, 1270–1282. 

Sharp, P.E., and Green, C. (1994). Spatial correlates of firing patterns of single cells in the subiculum of the freely moving rat. J. Neurosci. 14, 2339–2356. 

Sherrill, K.R., Erdem, U.M., Ross, R.S., Brown, T.I., Hasselmo, M.E., and Stern, C.E. (2013). Hippocampus and retrosplenial cortex combine path integration signals for successful navigation. J. Neurosci. 33, 19304–19313. 

Shin, J.D., Tang, W., and Jadhav, S.P. (2019). Dynamics of awake hippocampal-prefrontal replay for spatial learning and memory-guided decision making. Neuron 104, 1110–1125.e7. 

Shine, J.P., Valde´ s-Herrera, J.P., Tempelmann, C., and Wolbers, T. (2019). Evidence for allocentric boundary and goal direction information in the human entorhinal cortex and subiculum. Nat. Commun. 10, 4004. 

Singer, A.C., Carr, M.F., Karlsson, M.P., and Frank, L.M. (2013). Hippocampal SWR activity predicts correct decisions during the initial learning of an alternation task. Neuron 77, 1163–1173. 

Singer, A.C., and Frank, L.M. (2009). Rewarded outcomes enhance reactivation of experience in the hippocampus. Neuron 64, 910–921. 

Smith, D.M., and Mizumori, S.J.Y. (2006). Hippocampal place cells, context, and episodic memory. Hippocampus 16, 716–729. 

420 Neuron 110, February 2, 2022 

**ll** 

## Review 

Solomon, E.A., Lega, B.C., Sperling, M.R., and Kahana, M.J. (2019). Hippocampal theta codes for distances in semantic and temporal spaces. Proc. Natl. Acad. Sci. USA 116, 24343–24352. 

Solstad, T., Boccara, C.N., Kropff, E., Moser, M.B., and Moser, E.I. (2008). Representation of geometric borders in the entorhinal cortex. Science 322, 1865–1868. 

Sosa, M., and Giocomo, L.M. (2021). Navigating for reward. Nat. Rev. Neurosci. 22, 472–487. 

Sosa, M., Joo, H.R., and Frank, L.M. (2020). Dorsal and ventral hippocampal sharp-wave ripples activate distinct nucleus accumbens networks. Neuron 105, 725–741.e8. 

Spiers, H.J. (2020). The hippocampal cognitive map: one space or many? Trends Cogn. Sci. 24, 168–170. 

Spiers, H.J., and Barry, C. (2015). Neural systems supporting navigation. Curr. Opin. Behav. Sci. 1, 47–55. 

Spiers, H.J., Hayman, R.M.A., Jovalekic, A., Marozzi, E., and Jeffery, K.J. (2015). Place field repetition and purely local remapping in a multicompartment environment. Cereb. Cortex 25, 10–25. 

Spiers, H.J., and Maguire, E.A. (2006). Thoughts, behaviour, and brain dynamics during navigation in the real world. Neuroimage 31, 1826–1840. 

Spiers, H.J., and Maguire, E.A. (2007). A navigational guidance system in the human brain. Hippocampus 17, 618–626. 

Spiers, H.J., Olafsdottir, H.F., and Lever, C. (2018). Hippocampal CA1 activity correlated with the distance to the goal and navigation performance. Hippocampus 28, 644–658. 

Squire, L.R., and Wixted, J.T. (2011). The cognitive neuroscience of human memory since H.M. . Annu. Rev. Neurosci. 34, 259–288. 

Stachenfeld, K.L., Botvinick, M.M., and Gershman, S.J. (2017). The hippocampus as a predictive map. Nat. Neurosci. 20, 1643–1653. 

Stamatakis, A.M., Jennings, J.H., Ung, R.L., Blair, G.A., Weinberg, R.J., Neve, R.L., Boyce, F., Mattis, J., Ramakrishnan, C., Deisseroth, K., and Stuber, G.D. (2013). A unique population of ventral tegmental area neurons inhibits the lateral habenula to promote reward. Neuron 80, 1039–1053. 

Stefanini, F., Kushnir, L., Jimenez, J.C., Jennings, J.H., Woods, N.I., Stuber, G.D., Kheirbek, M.A., Hen, R., and Fusi, S. (2020). A distributed neural code in the dentate gyrus and in CA1. Neuron 107, 703–716.e4. 

Stella, F., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). Hippocampal reactivation of random trajectories resembling brownian diffusion. Neuron 102, 450–461.e7. 

Stemmler, M., Mathis, A., and Herz, A.V.M. (2015). Connecting multiple spatial scales to decode the population activity of grid cells. Sci. Adv. 1, e1500816. 

Stensola, H., Stensola, T., Solstad, T., Frøland, K., Moser, M.-B., and Moser, E.I. (2012). The entorhinal grid map is discretized. Nature 492, 72–78. 

Sutton, R.S. (1988). Learning to predict by the methods of temporal differences. Mach. Learn. 3, 9–44. 

Sutton, R.S. (1991). Dyna, an integrated architecture for learning, planning, and reacting. ACM SIGART Bull 2, 160–163. 

Sutton, R.S., and Barto, A.G. (2018). Reinforcement Learning: An Introduction (MIT Press). 

Tabuchi, E., Mulder, A.B., and Wiener, S.I. (2003). Reward value invariant place responses and reward site associated activity in hippocampal neurons of behaving rats. Hippocampus 13, 117–132. 

Tang, Q., Burgalossi, A., Ebbesen, C.L., Sanguinetti-Scheck, J.I., Schmidt, H., Tukker, J.J., Naumann, R., Ray, S., Preston-Ferrer, P., Schmitz, D., and Brecht, M. (2016). Functional architecture of the rat parasubiculum. J. Neurosci. 36, 2289–2301. 

Tang, W., Shin, J.D., Frank, L.M., and Jadhav, S.P. (2017). Hippocampal-prefrontal reactivation during learning is stronger in awake compared with sleep states. J. Neurosci. 37, 11789–11805. 

Tang, W., Shin, J.D., and Jadhav, S.P. (2021). Multiple time-scales of decisionmaking in the hippocampus and prefrontal cortex. Elife 10, e66227. 

Taube, J.S. (1995). Place cells recorded in the parasubiculum of freely moving rats. Hippocampus 5, 569–583. 

Taube, J.S., Muller, R.U., and Ranck, J.B., Jr. (1990a). Head-direction cells recorded from the postsubiculum in freely moving rats. I. Description and quantitative analysis. J. Neurosci. 10, 420–435. 

Taube, J.S., Muller, R.U., and Ranck, J.B., Jr. (1990b). Head-direction cells recorded from the postsubiculum in freely moving rats. II. Effects of environmental manipulations. J. Neurosci. 10, 436–447. 

Tavares, R.M., Mendelsohn, A., Grossman, Y., Williams, C.H., Shapiro, M., Trope, Y., and Schiller, D. (2015). A map for social navigation in the human brain. Neuron 87, 231–243. 

Toledo, S., Shohami, D., Schiffner, I., Lourie, E., Orchan, Y., Bartan, Y., and Nathan, R. (2020). Cognitive map–based navigation in wild bats revealed by a new high-throughput tracking system. Science 369, 188–193. 

Tolman, E.C., and Honzik, C.H. (1930). Introduction and removal of reward, and maze performance in rats. Univ. Calif. Publ. Psychol. 4, 257–275. 

Tolman, E.C. (1939). Prediction of vicarious trial and error by means of the schematic sowbug. Psychol. Rev. 46, 318–336. 

Tolman, E.C. (1948). Cognitive maps in rats and men. Psychol. Rev. 55, 189–208. 

Tolman, E.C., Ritchie, B.F., and Kalish, D. (1946a). Studies in spatial learning; place learning versus response learning. J. Exp. Psychol. 36, 221–229. 

Tolman, E.C., Ritchie, B.F., and Kalish, D. (1946b). Studies in spatial learning. I. Orientation and the short-cut. 1946. J. Exp. Psychol. Gen. 36, 13–24. 

Tryon, V.L., Penner, M.R., Heide, S.W., King, H.O., Larkin, J., and Mizumori, S.J.Y. (2017). Hippocampal neural activity reflects the economy of choices during goal-directed navigation. Hippocampus 27, 743–758. 

Tsai, H.-C., Zhang, F., Adamantidis, A., Stuber, G.D., Bonci, A., de Lecea, L., and Deisseroth, K. (2009). Phasic firing in dopaminergic neurons is sufficient for behavioral conditioning. Science 324, 1080–1084. 

Tsitsiklis, M., Miller, J., Qasim, S.E., Inman, C.S., Gross, R.E., Willie, J.T., Smith, E.H., Sheth, S.A., Schevon, C.A., Sperling, M.R., et al. (2020). Singleneuron representations of spatial targets in humans. Curr. Biol. 30, 245–253.e4. 

Turi, G.F., Li, W.-K., Chavlis, S., Pandi, I., O’Hare, J., Priestley, J.B., Grosmark, A.D., Liao, Z., Ladow, M., Zhang, J.F., et al. (2019). Vasoactive intestinal polypeptide-expressing interneurons in the hippocampus support goal-oriented spatial learning. Neuron 101, 1150–1165.e8. 

Vanderwolf, C.H. (1969). Hippocampal electrical activity and voluntary movement in the rat. Electroencephalogr. Clin. Neurophysiol. 26, 407–418. 

Vaz, A.P., Wittig, J.H., Jr., Inati, S.K., and Zaghloul, K.A. (2020). Replay of cortical spiking sequences during human memory retrieval. Science 367, 1131–1134. 

Vertes, R.P., Hoover, W.B., Szigeti-Buck, K., and Leranth, C. (2007). Nucleus reuniens of the midline thalamus: link between the medial prefrontal cortex and the hippocampus. Brain Res. Bull. 71, 601–609. 

Viard, A., Doeller, C.F., Hartley, T., Bird, C.M., and Burgess, N. (2011). Anterior hippocampus and goal-directed spatial decision making. J. Neurosci. 31, 4613–4621. 

Vigano` , S., and Piazza, M. (2020). Distance and direction codes underlie navigation of a novel semantic space in the human brain. J. Neurosci. 40, 2727–2736. 

Wang, M., Foster, D.J., and Pfeiffer, B.E. (2020). Alternating sequences of future and past behavior encoded within hippocampal theta oscillations. Science 370, 247–250. 

Watrous, A.J., Miller, J., Qasim, S.E., Fried, I., and Jacobs, J. (2018). Phasetuned neuronal firing encodes human contextual representations for navigational goals. Elife 7, e32554. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, February 2, 2022 421 

Review 

## **ll** 

Whittington, J.C.R., Muller, T.H., Mark, S., Chen, G., Barry, C., Burgess, N., and Behrens, T.E.J. (2020). The Tolman-Eichenbaum machine: unifying space and relational memory through generalization in the hippocampal formation. Cell 183, 1249–1263.e23. 

Wiener, S.I., Paul, C.A., and Eichenbaum, H. (1989). Spatial and behavioral correlates of hippocampal neuronal activity. J. Neurosci. 9, 2737–2763. 

Wikenheiser, A.M., and Redish, A.D. (2015). Hippocampal theta sequences reflect current goals. Nat. Neurosci. 18, 289–294. 

Wilson, M.A., and McNaughton, B.L. (1994). Reactivation of hippocampal ensemble memories during sleep. Science 265, 676–679. 

Wilson, R.C., Takahashi, Y.K., Schoenbaum, G., and Niv, Y. (2014). Orbitofrontal cortex as a cognitive map of task space. Neuron 81, 267–279. 

Winocur, G., and Moscovitch, M. (2011). Memory transformation and systems consolidation. J. Int. Neuropsychol. Soc. 17, 766–780. 

Winocur, G., Moscovitch, M., Fogel, S., Rosenbaum, R.S., and Sekeres, M. (2005). Preserved spatial memory after hippocampal lesions: effects of extensive experience in a complex environment. Nat. Neurosci. 8, 273–275. 

Winocur, G., Moscovitch, M., Rosenbaum, R.S., and Sekeres, M. (2010). An investigation of the effects of hippocampal lesions in rats on pre- and postoperatively acquired spatial memory in a complex environment. Hippocampus 20, 1350–1365. 

Wirtshafter, H.S., and Wilson, M.A. (2020). Differences in reward biased spatial representations in the lateral septum and hippocampus. Elife 9, e55252. 

Wolbers, T., Hegarty, M., Buchel, C., and Loomis, J.M. (2008). Spatial updat-€ ing: how the brain keeps track of changing object locations during observer motion. Nat. Neurosci. 11, 1223–1230. 

Wood, E.R., Dudchenko, P.A., Robitsek, R.J., and Eichenbaum, H. (2000). Hippocampal neurons encode information about different types of memory episodes occurring in the same location. Neuron 27, 623–633. 

Wu, C.-T., Haggerty, D., Kemere, C., and Ji, D. (2017). Hippocampal awake replay in fear memory retrieval. Nat. Neurosci. 20, 571–580. 

Xiao, Z., Lin, K., and Fellous, J.-M. (2020). Conjunctive reward–place coding properties of dorsal distal CA1 hippocampus cells. Biol. Cybern. 114, 285–301. 

Xu, H., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). Assembly responses of hippocampal CA1 place cells predict learned behavior in goal-directed spatial tasks on the radial eight-arm maze. Neuron 101, 119–132.e4. 

Yamamoto, J., and Tonegawa, S. (2017). Direct medial entorhinal cortex input to hippocampal CA1 is crucial for extended quiet awake replay. Neuron 96, 217–227.e4. 

Yin, H.H., and Knowlton, B.J. (2004). Contributions of striatal subregions to place and response learning. Learn. Mem. 11, 459–463. 

Young, J.J., and Shapiro, M.L. (2011). Dynamic coding of goal-directed paths by orbital prefrontal cortex. J. Neurosci. 31, 5989–6000. 

Yuste, R. (2015). From the neuron doctrine to neural networks. Nat. Rev. Neurosci. 16, 487–497. 

Zaremba, J.D., Diamantopoulou, A., Danielson, N.B., Grosmark, A.D., Kaifosh, P.W., Bowler, J.C., Liao, Z., Sparks, F.T., Gogos, J.A., and Losonczy, A. (2017). Impaired hippocampal place cell dynamics in a mouse model of the 22q11.2 deletion. Nat. Neurosci. 20, 1612–1623. 

422 Neuron 110, February 2, 2022 

