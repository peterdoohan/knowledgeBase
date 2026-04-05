**==> picture [38 x 35] intentionally omitted <==**

## _Annual Review of Neuroscience_ 

## Basal Ganglia Circuits for Action Specification 

## Junchol Park,[∗] Luke T. Coddington,[∗] and Joshua T. Dudman[∗] 

Janelia Research Campus, Howard Hughes Medical Institute, Ashburn, Virginia 20147, USA; email: dudmanj@janelia.hhmi.org 

Annu. Rev. Neurosci. 2020. 43:485–507 

First published as a Review in Advance on April 17, 2020 

The _Annual Review of Neuroscience_ is online at neuro.annualreviews.org 

https://doi.org/10.1146/annurev-neuro-070918050452 

Copyright © 2020 by Annual Reviews. All rights reserved 

~~∗These authors contributed equally to this article~~ 

## **Keywords** 

basal ganglia, dopamine, reinforcement learning, motor control, action selection, motor cortex 

## **Abstract** 

Behavior is readily classified into patterns of movements with inferred common goals—actions. Goals may be discrete; movements are continuous. Through the careful study of isolated movements in laboratory settings, or via introspection, it has become clear that animals can exhibit exquisite graded specification to their movements. Moreover, graded control can be as fundamental to success as the selection of which action to perform under many naturalistic scenarios: a predator adjusting its speed to intercept moving prey, or a tool-user exerting the perfect amount of force to complete a delicate task. The basal ganglia are a collection of nuclei in vertebrates that extend from the forebrain (telencephalon) to the midbrain (mesencephalon), constituting a major descending extrapyramidal pathway for control over midbrain and brainstem premotor structures. Here we discuss how this pathway contributes to the continuous specification of movements that endows our voluntary actions with vigor and grace. 

_485_ 

## **Contents** 

|**Contents**||
|---|---|
|INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|486|
|ENCODING OF CONTINUOUS MOVEMENT PARAMETERS||
|IN BASAL GANGLIA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|488|
|ACTION-SPECIFIC ENCODING IS CONSISTENT||
|WITH GAIN MODULATION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|490|
|CIRCUIT-LEVEL COMPUTATIONS BY INHIBITION||
|IN THE BASAL GANGLIA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|493|
|BASAL GANGLIA OUTPUT: RELATION TO MAJOR DESCENDING||
|MOTOR PATHWAYS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>FEEDFORWARD CONTROL OVER MIDBRAIN BY BASAL GANGLIA. . . . . . . . <br>BASAL GANGLIA FEEDBACK THROUGH THALAMOCORTICAL<br>CIRCUITS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>SUMMARY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|494<br> 494<br>497<br>498|



## **INTRODUCTION** 

Consider an engineered system with multiple components that provides continuous modulation of a highly variable input—a stereo. This is a system in which the specification of the audio waveform comes from a source that converts a physical (or digital) representation of music to an analog waveform. The analog waveform is then amplified as it is routed to speakers. If one wants a stereo that works in diverse rooms or with speakers of variable characteristics, one might also include a graphic equalizer (Bohn 1986) (schematized in **Figure 1** _**a**_ ). A (neuro)scientist trying to understand the equalizer component of a stereo would have access to recordings of internal voltages while monitoring output, the ability to perform various functional perturbations, and so on (Yazebnik 2012). Internal voltages would be observed to correlate with the sound measured in front of the speakers; perturbation of equalizer function could produce graded, systematic changes in volume; and some perturbations yield no sound at all.If we change the music being played at its source,then voltages in a particular channel of the equalizer will show a different pattern that is now correlated with the identity of the source music and not fully explained by volume of the output. In the case of a stereo, it is obvious that these observations are all consistent with an interpretation that there is a dedicated component allowing continuous control over distinct frequency components of the output (an equalizer). How would one distinguish between changes in an unknown source or changes in the amplification of a subset of frequency bands? Or how would one determine whether a perturbation that produced no output resulted from reducing gain to zero or change in the analog input? It is clear that without an appreciation of the system, these observations are easily misinterpreted ( Jonas & Kording 2017), be it the element of an engineered system like a graphic equalizer or a biological component (circuit) of the descending system for control over voluntary movements like the basal ganglia (BG). 

The BG are a collection of nuclei found in all vertebrates that extend from a major forebrain nucleus to a set of output nuclei in the ventral midbrain that project to premotor structures in the brainstem, midbrain, and forebrain (anatomical organization of BG is summarized in **Figure 1** ). We begin by reviewing observations of BG modulation during the execution of voluntary actions, from early physiological recordings to recent large-scale imaging and electrophysiological recordings of ensembles of BG neurons. We then delve into how BG activity during movement execution is consistent with a role in the continuous parameterization of movement execution for the 

_486 Park[•] Coddington[•] Dudman_ 

**==> picture [455 x 337] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>Cut Boost Out Anterior<br>In<br>f 1 f 2 f 3 f 4 f 5<br>FSI<br>Striatum<br>dMSN iMSN<br>Cut<br>output Inhibitory<br>connection Globus<br>Adjustable pallidus<br>gain Excitatory<br>connection<br>Boost Modulatory Subthalamic<br>output connection mDA nucleus<br>Direct<br>pathway<br>Filter f 3 SNc<br>Indirect<br>pathway SNr<br>GPi<br>Dorsal<br>Corticothalamic input channels<br>Multiple channel equalizer circuit<br>Telencephalon<br>Forebrain<br>Diencephalon<br>Intrinsic circuit element Intrinsic circuitry of basal ganglia<br>Midbrain<br>**----- End of picture text -----**<br>


## **Figure 1** 

Intrinsic circuitry of an engineered gain circuit and the mouse basal ganglia (BG). ( _a_ ) Upper image is of a RANE graphic equalizer. Lower images show the schematic circuit diagram of five channels of the graphic equalizer circuit. Inputs are filtered into largely nonoverlapping frequency bands through bandpass filters ( _colored bars_ , _fx_ ). An adjustable resistor determines whether the output from that frequency band should be added to the output (boost amplifier, _blue_ ) or removed from the output (cut amplifier, _red_ ). Image of RANE equalizer labelled for reuse. ( _b_ ) Upper image shows a sagittal section through the mouse brain, with topography of cortico-BG circuits schematized with colored arrows. The BG integrate input from superficial and deep-layer projection neurons across much of the cortical mantle, multiple thalamic nuclei, and limbic structures (Alexander et al. 1986, Dudman & Gerfen 2015, Haber 2003, Hunnicutt et al. 2016, Pan et al. 2010). The primary input structure is the striatum ( _bottom_ ). Corticofugal neurons also convey direct inputs to intrinsic BG nuclei, the globus pallidus externus and subthalamic nucleus. Although an approximate topographic organization is present, it is also important to note that in vertebrates as diverse as rodents and primates, substantial integration of input can also be observed (Averbeck et al. 2014, Pan et al. 2010). BG output is carried by GABAergic projection neurons in the substantia nigra pars reticulata (SNr), internal globus pallidus (GPi), and ventral tegmental area (VTA). Output projections both descend to target premotor areas that directly influence the spinal cord and ascend, feeding back to the forebrain via the thalamus. The midbrain dopamine nuclei [VTA and substantia nigra pars compacta (SNc)] integrate extensive action- and sensory-related input (Coddington & Dudman 2019) and provide modulatory feedback most strongly at the striatal input layer. GABAergic projection neurons in striatum, the medium spiny neurons (MSNs), can be separated according to whether they influence BG output through direct projections to the SNr/GPi (dMSNs) or indirectly (iMSNs) via projections to the internal BG nuclei (Gerfen & Surmeier 2010). Core nuclei of BG intrinsic circuitry are indicated with colored boxes in the upper image and correspond to the circuit schematic shown below. ( _Bottom_ ) Intrinsic circuitry of BG is depicted, including major internal circuit organization of striatal cell types. Local inhibition is depicted as a single major class of fast-spiking interneurons (FSIs) but is composed of multiple cell types, as reviewed elsewhere (Assous & Tepper 2019). Direct ( _blue_ ) and indirect ( _red_ ) pathways are suggested to relate to the cut and boost components of the equalizer circuit in panel _a_ , analogous to the ability of dMSNs and iMSNs to continuously increase and decrease movement speed, respectively (Yttri & Dudman 2016). 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 487_ 

presumed purpose of refining action performance. As BG inputs are collaterals of pathways that have their own key functional contributions to forebrain activity, we attempt to clarify the position of BG circuits within the larger functional organization of descending motor pathways, highlighting their complementary and interdependent control of subcortical and spinal motor nuclei. 

## **ENCODING OF CONTINUOUS MOVEMENT PARAMETERS IN BASAL GANGLIA** 

Striatal neurons of the BG display gross directional selectivity as revealed by studies using animals trained to make cue-guided leftward or rightward actions (Alexander & Crutcher 1990a, Brown & Robbins 1989,Gage et al.2010,Packard & McGaugh 1996) or animals that freely navigate an open space (Kravitz et al. 2010, Markowitz et al. 2018, Schwarting & Huston 1996). Unilateral striatal perturbations by lesion (Brown & Robbins 1989), inactivation (Packard & McGaugh 1996), or dopamine depletion (Parker et al. 2018, Schwarting & Huston 1996) bias animals’ actions toward the perturbed side. Unilateral optogenetic stimulation of direct-pathway medium spiny neurons (dMSNs) and indirect-pathway medium spiny neurons (iMSNs) in the dorsomedial striatum results in lateralized turning (Kravitz et al. 2010, Tai et al. 2012), corroborating that the interplay between the two striatal opponent pathways modulates movement direction (Klaus et al. 2017, Markowitz et al. 2018, Meng et al. 2018). Recent studies have used unsupervised machine learning algorithms to discretize mouse behavioral repertoires, e.g., left/right turns, rear, grooming, walk, and lunge (Wiltschko et al. 2015). Simultaneous calcium imaging of striatal dMSN and iMSN neural populations has revealed spatiotemporal properties of the striatal tuning for the machinediscretized behavioral clusters (Klaus et al. 2017, Markowitz et al. 2018). Medium spiny neurons (MSNs) active during a particular behavior appeared to be more correlated and spatially clustered (Klaus et al. 2017). Activity of dMSNs measured with fiber photometry displayed a significant correlation with three-dimensional (3D) velocity of movement, while the activity of iMSNs was anticorrelated,thus the difference in activity between the pathways was a better predictor of 3D velocity than either pathway alone (Markowitz et al. 2018, Meng et al. 2018, Yttri & Dudman 2016). This observation, that distinct striatal ensembles are recruited as a function of movement direction or specific behavioral repertoire, has often been considered to provide evidence that the BG implement a discrete, switchboard-like selection of action (Alexander & Crutcher 1990b, Frank 2011, Graybiel 1998, Humphries et al. 2006, Klaus et al. 2019, Markowitz et al. 2018, Surmeier et al. 2009). 

Action selection models have successfully explained abstractions of behavior such as the choice between two levers to press (e.g., see discussion in Collins & Frank 2014). However, the presence of action-specific ensembles of activity in BG does not necessarily imply a switchboard-like selection function. To illustrate this point, let us first consider that early studies of BG physiology in behaving animals also observed movement-specific activity and yet arrived at the conclusion that BG were critical for online control of movement execution. DeLong et al. (1984), for example, concluded “that basal ganglia output plays a role in controlling the direction and amplitude of movement but is not primarily involved in the initiation of limb movement or selection of specific muscles” (p. 235). Indeed, these conclusions were often reached despite a bias toward a selection/initiation interpretation (Buchwald et al. 1979). As an example, Aldridge et al. (1980, p. 3) wrote that, 

The experiments were designed to examine the relationship between activity of single neurons in [globus pallidus] and movement initiation _. . ._ neurons were activated after the onset of muscle activity and subsequent movement. It is thus unlikely that these cells were involved in movement initiation. However a role in movement execution is not excluded _. . ._ 

_488 Park[•] Coddington[•] Dudman_ 

An interpretation that BG were primarily involved in controlling movement execution was informed by the fact that inactivation or lesion experiments done around this period failed to produce any effect on initiation of an action (putatively selection) and generally only resulted in execution deficits (Horak & Anderson 1984a,b; Mink & Thach 1991a). For Kornhuber (1971), observations of Parkinsonian patients informed his conclusion that BG were primarily involved in the continuous control of movement speed (ramps)—a perspective we have previously argued was largely sound and prescient (Dudman & Krakauer 2016). One additional persuasive observation at that time appears to have been the fact that a substantial majority of BG output neurons are modulated primarily or only during movement execution (Alexander 1987, Alexander & Crutcher 1990c, Anderson & Horak 1985, Hikosaka & Wurtz 1985, Liles 1985, Neafsey et al. 1978, Turner & Anderson 1997), especially when contrasted with cortical areas (Alexander & Crutcher 1990a). 

However, in subsequent decades many authors turned to an interest in BG activity modulated by expected outcome (Kawagoe et al. 1998), inspired by observations of the strong subjective modulation of activity in midbrain dopamine neurons (Schultz & Romo 1990, Schultz et al. 1997) and the increasing use of tasks that incorporated reinforcement (Hikosaka et al. 2000). [See **Supplemental Appendix 1** , Section 1, for discussion of additional details.] This change in focus seems to have led to a substantial conceptual shift in what was meant by “selection” in earlier influential reviews (e.g., Mink 1996) versus more recently (e.g., Frank 2011, Klaus et al. 2019). For example, Mink (1996) articulated a model of selection to address observations that transient inactivation of BG output nuclei produced deficits in execution of actions—primarily movement slowing— with no effect on initiation or the correct choice of action (e.g., Mink & Thach 1991a,b,c). Electromyographic recordings revealed that this slowing could be accompanied by cocontraction of agonist/antagonist muscles. As a result, Mink proposed that BG select appropriate sets of muscles during movement execution and are primarily involved in relaxing muscle groups. This is quite a distinct conception from selecting an action prior to execution. However, many authors have tended to view initiation deficits in Parkinson’s disease as primary and deficits in continuous control of movement kinematics as secondary (Albin et al. 1989, Redgrave et al. 2010), while others have argued the converse (Desmurget & Turner 2010, Dudman & Krakauer 2016, Kornhuber 1971). The observation that BG lesions tend to primarily alter continuous properties of movement execution has only been strengthened in more recent studies (Desmurget & Turner 2010), as has the observation that the majority of BG activity modulation occurs during movement execution. Moreover, while kinematic deficits have frequently been observed in the absence of initiation deficits, the converse dissociation has not, to our knowledge (Yttri & Dudman 2018), ever been demonstrated. For such reasons, here we focus on the role of BG in shaping voluntary action through their role in the continuous specification of movement execution. 

**==> picture [101 x 17] intentionally omitted <==**

Recently, BG activity has begun to be observed in the context of increasingly diverse actions with highly variable execution of movements (movement of a lever or joystick, free locomotion, running on a treadmill, approach toward a location in the environment, grooming, and rearing). This diversity and variability provide regressors to distinguish the aspects of behavior with which BG activity covaries. In addition, recent work has begun to make cell type–specific recordings, notably in striatum, that provide further insight into the coordinated activity in the major opponent pathways. These experiments have utilized bulk estimates of activity in axons and somata (Cui et al. 2013, 2014; Kupferschmidt et al. 2017; Markowitz et al. 2018; Meng et al. 2018) as well as measurements resolved to individual cells or even subcellular compartments (Barbera et al. 2016, Bocarsly et al. 2015, Kim et al. 2019, Klaus et al. 2017, Meng et al. 2019, Owen et al. 2018, Parker et al. 2018, Roberts et al. 2019). These studies have revealed that both principal neurons (MSNs) and interneurons can have clear correlates to movement speed, often allowing accurate decoding of speed from imaging data (Barbera et al. 2016, Fobbs et al. 2020, Kim et al. 2019, Roberts et al. 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 489_ 

2019). Simultaneous multicolor imaging of both dMSNs and iMSNs has revealed that the ratio with which these two pathways are recruited is best correlated with the speed of a given action (Markowitz et al. 2018, Meng et al. 2018). On the other hand, some imaging studies have failed to observe clear correlates to movement kinematics (Klaus et al. 2017, 2019). One possibility is that neither calcium imaging nor gross movement clusters have sufficient resolution to detect continuous modulation during movement (see discussion in Fobbs et al. 2020, Kim et al. 2019), and events detected in imaging are substantially lower frequency than equivalent electrophysiological recordings in striatum (Owen et al.2018).We thus turn our attention to correlates of continuous parameters of movement observed with increased temporal resolution in electrophysiological recordings. 

As a representative sample, recordings in striatum reveal individual neurons that tend to be specifically activated by a circumscribed range of actions such as locomotion (Costa et al. 2004, Jin et al. 2014, Rueda-Orozco & Robbe 2015, Sales-Carbonell et al. 2018), discrete limb movements (DeLong et al. 1984, Panigrahi et al. 2015, Turner & Anderson 1997, Yttri & Dudman 2016), rearing (Markowitz et al. 2018), approach behavior (McGinty et al. 2013), licking (Rossi et al. 2016), or movements of the head and body (Barter et al. 2015, Kim et al. 2014). In a subset of studies, the dynamics of changes in activity (largely of individual cells) have revealed partially dissociable temporal components of activity that correlate with movement kinematics. For discrete movement of a limb in mice, it was observed that some striatal cell activity mirrors the acceleration and deceleration of the limb with transient activity at the early phase of movement initiation or at the time of peak amplitude (Panigrahi et al. 2015) [as expected from control models (Baraduc et al. 2013)]. Similarly, subsets of cells in dorsal striatum also preferentially reflect the acceleration and deceleration phases of locomotion in mice running on a treadmill (Sales-Carbonell et al. 2018). Other subsets of neurons appear to encode other aspects of kinematics, reflecting more delayed components corresponding to amplitude or possibly sensory-mediated feedback during movement (Coffey et al. 2016, Panigrahi et al. 2015, Sales-Carbonell et al. 2018, West et al. 1990). 

## **ACTION-SPECIFIC ENCODING IS CONSISTENT WITH GAIN MODULATION** 

A generalized, action-independent representation of speed in BG would not be appropriate for continuous specification of movement kinematics across multiple, distinct actions (distinguished by the muscle effectors used). The earliest ideas of BG determining ramps (continuous variation in movement) (Kornhuber 1971) through ideas on the regulation of movement speed (DeLong et al. 1984) and to more recent formulations of BG regulating movement vigor (Dudman & Krakauer 2016, Turner & Desmurget 2010) all demand action-specific representations of movement kinematics. There are a few key features of these formulations that span some four decades. First, activity in BG is related to kinematics without reflecting the involved muscle forces (kinetics) per se. Second, the representation must be action specific in the sense that at least partially distinct ensembles of BG neurons represent kinematics of actions implemented with distinct muscle effectors. As reviewed above, there are now substantial experimental data from diverse measurement techniques to support both of these key features in multiple vertebrate species. 

We tend to use terms like motivation or arousal to refer to generalized changes in behavior that are not necessarily specific to a given action. There is ample evidence that BG can exert more specific changes in an action without such effects generalizing across all of behavior (e.g., Yttri & Dudman 2016). To see why this implies a continuous encoding of kinematics that is action specific, consider a simple model constructed to provide continuous, independent control over the amplitude of distinct actions (as in Brown et al. 2016, Yttri & Dudman 2016) ( **Figure 2** _**a**_ ). This model is characterized by two distinct, action-specific ensembles of active neurons (schematized 

_490 Park[•] Coddington[•] Dudman_ 

as actions A and B). An increase in the net output of either population can produce an increase in the output of one or the other action, respectively. Activity in this constructed model of multiple neurons can be viewed in terms of its low-dimensional population dynamics obtained by projecting the population data onto their principal components (Shenoy et al. 2013). This reveals 

## **a** Constructed gain model 

**b** Striatal population activity 

**==> picture [359 x 495] intentionally omitted <==**

**----- Start of picture text -----**<br>
0<br>0 0<br>0<br>20<br>50<br>40<br>100<br>60<br>150<br>80<br>200 100<br>250 120<br>140<br>300<br>0 0<br>1 1<br>0 1 0 1<br>Time (s) Time (s)<br>c    Gain model dynamics d    Striatal population dynamics<br>Time<br>High gain Fastest<br>Low gain Slowest<br>Time<br>PC1 PC1<br>( Caption appears on following page )<br>Joystick move<br>Action A Action B Thresholdcross Rewarddelivery<br>Action A<br>Action B<br>Reward consume<br>A magnitude B magnitude Lick rate (a.u.)<br>Joystick speed (a.u.)<br>Sorted cell number Sorted cell number<br>Time (s) Time (s)<br>PC 2 PC 2<br>**----- End of picture text -----**<br>


_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 491_ 

## **Figure 2** ( _Figure appears on preceding page_ ) 

Encoding of action in a neural network constructed for continuous modulation and in the mouse striatum. ( _a_ , _top_ ) Schematic of simulated behavioral paradigm in which a network executes two actions (action A, _blue_ ; action B, _red_ ) in a nonoverlapping sequence; this is analogous to paradigms in which mice are trained to move a two-dimensional joystick followed by consumption of a delayed water reward (panel _b_ ) (as in Brown et al. 2016, Panigrahi et al. 2015, Park et al. 2019, Yttri & Dudman 2016). ( _b_ , _top_ ) Normalized mean joystick velocity ( _blue_ ) and lick rate ( _red_ ) are shown for an example session of data from Park et al. (2019). ( _a_ , _middle_ ) Simulated activity of individual network units modeled to approximately match distribution of observed responses plotted as a heat map (max., _red_ ; min., _blue_ ; zero, _white_ ). Data from Brown et al. (2016), Panigrahi et al. (2015), Park et al. (2019), and Yttri & Dudman (2016). ( _a_ , _bottom_ ) Cross-correlation of the population vector (set of active units) as a function of time illustrating that ensembles of active units during actions A and B are negatively correlated. ( _b_ ; _middle_ , _bottom_ ) Individual unit activity correlated with task performance is plotted for an example recording that spans ∼2.5 mm of dorsoventral axis of mouse striatum. Individual units are sorted according to latency of peak firing to illustrate two largely distinct active populations during joystick movement and reward collection. Data from Park et al. (2019). ( _c_ ) To illustrate expected changes in population activity, the _N_ (number of units)-dimensional activity is plotted along its first two principal components. Neural populations are scaled according to the prediction of the model in Yttri & Dudman (2016) to obtain the high gain ( _purple_ ) and low gain ( _gray_ ) trajectories. Of note is that the trajectory corresponding to action A (target of gain change) is lengthened, with more modest changes in trajectory corresponding to action B. Trajectories evolve over time in a counterclockwise manner. ( _d_ ) Plotting is the same as in panel _c_ but for data from an example session described in Park et al. (2019). Average trajectories are given for neural activity recorded during the fastest ( _purple_ ) and slowest ( _gray_ ) tercile of movements in the example session. A model in which basal ganglia adjust the gain of descending motor commands (e.g., movement amplitude) for specific actions implies both action-specific ensembles of active units and scaling of activity dynamics similar to what is observed in large-scale physiological recordings from striatum of behaving mice; see main text for additional details. 

two, roughly orthogonal, modes of activity. If the network modulates the kinematics of one action (action A) by, for example, increasing activity in this population, then these changes are isolated to the dimension of population activity for the corresponding action; the same will be true for the other action. This leads to a pattern of activity in which both the action and the kinematics are decodable. Thus, contrary to a recent proposal (Klaus et al. 2017, 2019), the observation of action-specific ensembles of neurons does not foreclose that BG populations regulate continuous kinematics of action; indeed, quite the opposite. As is clear from the analogy to a graphic equalizer ( **Figure 1** _**a**_ ), the fact that a given channel exhibits distinct waveforms does not imply that it is necessarily selecting the particular music as opposed to, for instance, selectively amplifying distinct components of the source signal. 

We may compare this constructed gain circuit to the observation of neural activity in a population of neurons recorded in motor cortex and striatum during a task in which a mouse has to move a joystick to varying amplitudes to elicit a delayed drop of water, which it then consumes (by licking) a second later (adapted from Panigrahi et al. 2015, Yttri & Dudman 2016, Park et al. 2019). In these population recordings, it is clear that activity scales with the speed and amplitude of forelimb movements ( **Figure 2** ). In comparing this to the model, we can examine the encoding of two distinct actions—movement of the limb and reward consumption, respectively—in striatal activity. It is clear that there are action-specific ensembles of neurons recruited during these two behavior components ( **Figure 2** _**b**_ ). If we again look at the low-dimensional dynamics of activity, modulation of activity is nearly orthogonal for the two distinct actions. Moreover, if we separate out activity according to whether a fast or slow movement of the joystick was made, the limb movement–related dimension of population activity is scaled in magnitude, with little change in the dimension related to licking. These experimental data illustrate that the encoding of action in striatum is, at a minimum, consistent with the expected pattern of activity in a circuit constructed to selectively apply gain to multiple actions (Brown et al. 2016, Yttri & Dudman 2018). However, 

_492 Park[•] Coddington[•] Dudman_ 

the construction of circuits (Bohn 1986) to selectively apply gain to diverse and dynamic inputs is complex. Indeed, this depends very much on the details of how actions are represented in descending circuits for the control of voluntary movement. We now turn to a consideration of more detailed features of the intrinsic circuitry of BG that may be critical to such implementation. 

## **CIRCUIT-LEVEL COMPUTATIONS BY INHIBITION IN THE BASAL GANGLIA** 

MSNs receive excitatory input from a broad distribution of cortical areas that often appear to be correlated in their activity, especially during movement (Musall et al. 2019, Stringer et al. 2019), making decoding of cortical sensory or motor signals challenging in downstream targets (Averbeck et al. 2006). In principle, there could be cortical states that drive spiking in multiple MSN ensembles and require competition for disambiguation. The inhibitory circuitry of BG has often been proposed to support competition between overlapping ensembles as a mechanism for action selection (DeLong 1990) or refinement of execution (Mink 1996), analogous to the way that lateral inhibition produces center-surround suppression in other systems (Adesnik & Scanziani 2010, Hartline et al. 1956). However, gain computations are also common at the neuronal level, appearing as a change in the slope of input-output curves (Salinas & Thier 2000) and often involving interactions between inhibition and excitation, active dendritic integration, or neuromodulation (Gabbiani et al. 2002, Larkum et al. 2004, Mitchell & Silver 2003, Polack et al. 2013, Rothman et al. 2009, Royer et al. 2012). 

Local inhibition in the BG is mediated by axon collaterals between projection neurons in STR, external globus pallidus, and substantia nigra pars reticulata (SNr) (Brown et al. 2014, Koós & Tepper 1999, Silberberg & Bolam 2015, Tepper et al. 2004) and by local interneurons in STR (Burke et al. 2017). In the striatum, anatomical studies confirmed that both dMSNs and iMSNs elaborate axon collaterals that synapse on neighboring MSNs (Kawaguchi et al. 1990, Preston et al. 1980, Somogyi et al. 1981, Tepper et al. 2004). Several studies have found evidence for monosynaptic connections between MSNs, albeit sparse (less than 20% of pairs) and with high failure rates of evoked synaptic responses (Czubayko & Plenz 2002, Koos et al. 2004, Taverna et al. 2004, Tunstall et al. 2002). These sparse, weak connections seem unlikely to enforce lateral competition (Koos et al. 2004), though their integrity is essential to normal striatal function (Dobbs et al. 2016). In comparison to collateral inhibition, fast-spiking interneurons (FSIs) provide strong inhibitory synapses on somas of MSNs in vitro (Gittis et al. 2010, Koós & Tepper 1999, Planert et al. 2010), and FSIs respond to cortical stimulation with shorter latency and lower thresholds (Mallet et al. 2005). However, ablation or acute inhibition of FSI activity does not affect baseline motor performance (Lee et al. 2018, Owen et al. 2018, Xu et al. 2016). Rather, FSIs seem to primarily affect learning (Lee et al. 2018, Owen et al. 2018) by regulating the amplitude and timing of MSN responses to input (Owen et al. 2018). In mice performing a target pursuit task, FSI activity contributed to BG-dependent adjustments of pursuit velocity (Kim et al. 2019), consistent with a role for striatal feedforward inhibition in the continuous modulation of gain of BG output. 

In BG output nuclei, local microcircuitry is formed by collaterals of projection neurons, and there are no known interneurons (Deniau et al. 2007). To date, there is little evidence for competition being mediated by these collateral synapses; rather, the microcircuit appears to implement a potent divisive gain control of BG output (Brown et al. 2014). In addition, in other regimes of activation, collateral connectivity can regulate spike timing (Higgs & Wilson 2016). Population recordings in vivo are consistent with feedback gain control (Brown et al. 2014), and reducing intranigral feedback via chemogenetic perturbation significantly increased variance of movement kinematics without alteration of the mean (Brown et al. 2016), consistent with a role in regulating the gain of BG output rather than action selection. 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 493_ 

In summary, the evidence reviewed here indicates that inhibitory connectivity within the BG does not enforce switchboard-like competition between action-specific ensembles. Instead, action specificity of striatal ensembles is predominantly inherited from afferents rather than first emerging through local computations in the BG ( **Figure 2** ). This is consistent with ( _a_ ) observations that BG action encoding follows, rather than leads, cortical (Park et al. 2019, Seo et al. 2012) and thalamic (Schwab et al. 2019) encoding of movement kinematics; ( _b_ ) the preferential disruptions to movement kinematics following BG perturbation (Dudman & Krakauer 2016); and ( _c_ ) conceptual points about selective modulation of kinematics reviewed above ( **Figures 1** and **2** ). 

In comparison to categorical selection, continuous modulation can seem overly subtle: Can it really account for proposed BG roles in action control and adaptation? We first note that in our initial sound system analogy ( **Figure 1** ), large gain modulations can have the practical effect of turning a given equalizer channel on or off. This may be similar to the consequences of exogenous manipulations or pathological perturbations of striatal ensembles (Yttri & Dudman 2018) that can create seemingly categorical effects on action. Furthermore, multiplicative gain models have been invoked to explain key aspects of sensorimotor transforms in other circuits previously (see also **Supplemental Appendix 1** , Section 2, and **Supplemental Figure 1** ). To further address the plausibility of this account of BG function, we next turn to consider the downstream targets of BG output and putative roles for gain in the continuous specification of movement parameters. 

## **BASAL GANGLIA OUTPUT: RELATION TO MAJOR DESCENDING MOTOR PATHWAYS** 

Activity in BG is consistent with models of selective gain control of descending motor control signals ( **Figures 1** and **2** ). However, to further understand the role of BG in the specification of actions, it is critical to understand how BG output integrates with other major descending motor pathways. The structure and function of BG output have received relatively little attention compared to the theory and experiments dealing with its internal circuitry (e.g., Frank 2011, Graybiel 1998, Klaus et al. 2019, Nelson & Kreitzer 2014), and thus we summarize work on the BG output pathways below. 

Motor information is conveyed to the BG directly from motor-associated cortical areas, as well as via the thalamus, which conveys information from the cortex, SC, and cerebellum (Smith et al. 2014). Signals related to action initiation may also arise from limbic structures such as the amygdala (Ambroggi et al. 2008, Pan et al. 2010). Meanwhile, most BG output projects via descending pathways to midbrain and brainstem premotor areas, which also receive corticofugal input from deep-layer cortical neurons (Dudman & Gerfen 2015). Thus, the descending projection forms a convergent, feedforward pathway that targets premotor nuclei of the extrapyramidal motor system (tectum, red nucleus, pontine reticular areas) and integrates with descending corticofugal output that targets these same nuclei (Dudman & Krakauer 2016, Yttri & Dudman 2018). A smaller but substantial projection from BG output nuclei targets higher-order thalamic nuclei (Phillips et al. 2019), including the ventroanterior and ventromedial aspects of motor thalamus, as well as intralaminar nuclei (Alexander et al. 1986). These pathways provide indirect feedback to neocortex and are thought to modulate cortical output (and thus also BG inputs) ( **Figure 3** ). 

## **FEEDFORWARD CONTROL OVER MIDBRAIN BY BASAL GANGLIA** 

As noted above, the BG provide a major source of descending forebrain input to premotor nuclei of the extrapyramidal motor system, e.g., the superior colliculus (SC), pontine reticular areas, and red nucleus.The BG output targeting the SC has received by far the most attention of these nuclei, 

_494 Park[•] Coddington[•] Dudman_ 

**==> picture [453 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cortex<br>a<br>1<br>2/3<br>5<br>6<br>BG Cerebellum b<br>Motor<br>thalamus<br>Intralaminar<br>thalamus<br>Deep<br>SC<br>Midbrain<br>and Action<br>brainstem<br>nuclei<br>Feedback<br>Feedforward<br>**----- End of picture text -----**<br>


## **Figure 3** 

Connectivity enabling action control by basal ganglia (BG) output. ( _a_ ) Schematic of some of the interactions of BG output with other circuits for action control. In the feedback (ascending) pathway, BG output modulates the higher-order motor thalamus, which operates within a loop driven by descending cortical excitation and projects to upper cortical layers. This is paralleled by a cerebellar pathway through lower-order motor thalamus, which provides more direct feedforward excitation all the way through to motor-associated cortex. In the feedforward (descending) pathway, BG output regulates activity in the deep superior colliculus (SC) as well as actionrelated midbrain and brainstem nuclei, many of which also receive cerebellar or corticofugal projections. ( _b_ ) Shapes of major regions from panel _a_ are copied onto their approximate positions on a parasagittal section from a mouse brain for illustration of anatomical organization. 

and as such, here we focus on articulating how action specification via regulation of gain might function in the SC. Feedforward control over the SC from BG was initially thought to act as a requisite gate on output activity (Chevalier et al. 1985, Hikosaka et al. 2000) but more recently has been appreciated to exert a more complex, graded influence. The projection between SNr to SC is inhibitory, as confirmed by electrical and pharmacological manipulation in anesthetized rats (Chevalier et al. 1981, 1985; Deniau & Chevalier 1985). These manipulations resulted in large unambiguous responses: For instance, when a group of SNr neurons were strongly activated, recipient neurons in SC completely paused their activity. Meanwhile, studies in alert monkeys found decreases in SC-projecting SNr neuron activity during saccadic eye movements (Hikosaka & Wurtz 1983a) that rather precisely preceded increases in activity in simultaneously recorded SC neurons (Hikosaka & Wurtz 1983b), though this could partially depend on whether saccades were visually guided or memory guided. These observations led to proposals that SNr activity switched between basal high firing rates and complete silence to function as a categorical gate for movement (Chevalier & Deniau 1990; but see Basso & Sommer 2011, Bayer et al. 2004). However, subsequent work has found high variability in individual SNr neuron responses to even similarly targeted saccades,including some excitation (Handel & Glimcher 1999,Sato & Hikosaka 2002, Shin & Sommer 2010). Even in subpopulations of SNr neurons inhibited around saccades, average responses appear as graded decreases in activity rather than pauses (Basso & Wurtz 2002). 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 495_ 

Thus, several lines of evidence suggest that SNr to SC circuitry does not act as a categorical gate under normal physiological function. What role might the continuous regulation of SC via graded changes in SNr activity play in its premotor functions? 

**==> picture [101 x 16] intentionally omitted <==**

The mammalian SC and its nonmammalian homolog, the optic tectum, transform multimodal sensory inputs into spatially targeted movement commands thought to be critical for orienting the upper body (Wolf et al. 2015). Superficial SC neurons respond nearly exclusively to visual stimuli appearing at specific locations in the contralateral hemifield, forming a retinotopically ordered map (Gandhi & Katnani 2011, Hikosaka et al. 2000, Wallace et al. 1996). SC neurons in the intermediate and deep layers subserve motor functions—perhaps the most well studied are saccadic eye movements (see also **Supplemental Appendix 1** , Section 3, and **Supplemental Figure 2** ) (Gandhi & Katnani 2011, Hikosaka et al. 2000, Sparks 1986)—but the SC is also a key premotor structure for upper-body movements in general, including limbs (Philipp & Hoffmann 2014, Rubelowski et al. 2013, Werner et al. 1997), whisker movements (Hemelt & Keller 2008), and more complicated orienting behaviors involved in prey capture (Hoy et al. 2019) or targeted escape (Evans et al. 2018). 

The location of the active population of collicular neurons within the map of movement fields determines saccadic direction, whereas gain modulation of SC firing rate appears to determine saccade speed ( **Supplemental Figure 2** ). A positive correlation between the average firing rate of SC cells and saccadic velocity was observed in monkeys (Sparks & Mays 1990) and cats (Munoz & Guitton 1986).Peak eye velocity is correlated with frequency and intensity of electrical microstimulation (Katnani & Gandhi 2012, Stanford et al. 1996) and attenuated by reversible inactivation of the SC (Hikosaka & Wurtz 1986, Lee et al. 1988). Instantaneous SC activity and eye velocity are correlated within and across trials throughout the duration of a saccade, and this correlation is apparent even within amplitude-matched saccades (Smalianchuk et al. 2018). This modulation of gain of SC output is thought to explain multiple key functions. For example, gain field modulation aligned to a preferred saccadic direction may act to compensate for inhomogeneous muscle properties as a function of initial eye position (Van Opstal et al. 1995). In addition, gain modulation appears to explain the enhanced sensitivity of behavior to multimodal sensory input (Hughes et al. 1994, Perrott et al. 1990, Wallace et al. 1996, Zahn et al. 1978). 

Thus, an input pathway from BG, predominantly via the SNr, could be used to modulate SC output continuously to specify the execution of actions such as fine-tuning saccade velocity or limb kinematics (Gandhi & Katnani 2011, Sparks & Mays 1990). This is consistent with the classic results that muscimol inactivation of the SNr speeds up saccades (Hikosaka & Wurtz 1985). More recently, strong activation of SNr output was shown to decrease the rate of SC-dependent licking (Rossi et al. 2016), and activation of striatal MSNs could modulate SC-dependent attention processes associated with orienting responses (Wang et al. 2018). Continuous modulation of SC activity appears even more appropriate as the full range of SC participation in movement and choice behavior is considered (Evans et al. 2018, Wolf et al. 2015). Moreover, for limb movements, modulation of the majority of individual BG output neurons increases activity during movement (Turner & Anderson 1997), and SNr output projections also target intrinsic GABAergic neurons of SC (Kaneda et al. 2008), underscoring the fact that the BG provide only some portion of the inhibitory control of SC premotor neurons (Appell & Behan 1990). 

Interestingly, the deep SC also appears to be a substrate for the direct interaction of BG and cerebellar output, as in the rat at least some of the same neurons receive both cerebellar excitation and BG inhibition (Westby et al. 1994) ( **Figure 3** ). Thus, the likely continuous specification of SC activity modulated by BG output may serve as a useful template for exploring BG integration with output from other subcortical components of descending motor pathways (Grillner et al. 2013, Roseberry et al. 2016). We propose that BG output may thus regulate relatively open-loop 

_496 Park[•] Coddington[•] Dudman_ 

components of motor control (e.g., movement vigor), whereas cerebellar output may regulate closed-loop components of motor control (e.g., end point accuracy) that are unaffected by disruption of BG function (Dudman & Krakauer 2016). 

## **BASAL GANGLIA FEEDBACK THROUGH THALAMOCORTICAL CIRCUITS** 

The major BG-recipient thalamic nuclei include the intralaminar nucleus, which feeds back on to the striatum, and the motor thalamus (Bosch-Bouju et al. 2013, Dudman & Gerfen 2015). The motor thalamus integrates cortical, BG, and cerebellar afferents and projects to distinct layers within motor-related cortical areas to constitute a feedback pathway for the regulation of cortical control of action (Ohno et al. 2012, Winnubst et al. 2019). Whereas large driver glutamatergic synapses predominate in cerebellar-recipient motor thalamus and many other thalamic nuclei, BG-recipient regions exhibit smaller glutamatergic afferent terminals and large GABAergic inhibitory terminals (Bodor et al. 2008, Rovó et al. 2012). Pharmacological disruption of BG output has strong effects on thalamocortical (TC) neuron activity (Deniau & Chevalier 1985), while exogenous stimulation of BG output results in disinhibitory burst firing in the thalamus (Kim et al. 2017, Person & Perkel 2005). Disinhibitory bursting-like activity was observed infrequently in rats performing a skilled reaching task (Bosch-Bouju et al. 2014), suggesting that such a firing mode results from a specific, and rare, circuit state rather than as a consistent result of BG output (Edgerton & Jaeger 2014). While brief (5 ms) optogenetic activation of the mouse internal globus pallidus (GPi) resulted in motor thalamus inhibition with no muscular responses, longer inhibitions induced significant motor thalamus rebound excitation and abnormal muscle movements (Kim et al. 2017). Endogenous occurrence of such rebound excitation was significantly higher and associated with motor symptoms in a mouse model of Parkinson’s disease (Kim et al. 2017). In seizure and dopamine depletion models, aberrant synchronous oscillations in the BG appear to drive BG-recipient TC activity (Brazhnik et al. 2016, Parr-Brownlie et al. 2009, Paz et al. 2007). 

Thus, exogenous or aberrant synchronization of BG output can entrain corticothalamic neurons. However, physiological function may not involve such overt control. Rather, neurons in the BG output nuclei and BG-recipient motor thalamus respond as though they receive common, partially temporally overlapping inputs (Nakamura et al. 2012). Over separate recordings of the same monkeys making controlled reaches, movement-related activity appeared earlier with respect to movement in the motor thalamus than it did in BG output neurons in the GPi (Anderson & Turner 1991a,b). Furthermore, pharmacological inactivation of BG output had no effect on phasic movement-related activity in the motor thalamus (Inase et al. 1996). Experiments in avian (Goldberg & Fee 2012) and rodent (Guo et al. 2017) models have indicated that corticothalamic inputs in fact drive the majority of movement-related activity in BG-recipient motor thalamus. Inhibitory afferents from the BG may play more of a modulatory role, shaping responses to excitation rather than gating them or driving disinhibitory bursting (Goldberg et al. 2012, 2013). A recent study performing simultaneous recordings in monkey GPi and motor thalamus found little (and positive) covariation between the two nuclei and that movement-related activity in motor thalamus emerges before GPi (Schwab et al. 2019). Finally, many BG-recipient thalamic neurons send collaterals into the striatum (Hunnicutt et al. 2016, Pan et al. 2010), placing motor thalamus both up- and downstream of BG output and providing a substrate for precise temporal coordination. Thus, contrary to some predictions from anatomy (Alexander et al. 1986) and exogeneous manipulations, physiological BG output may not gate motor thalamus activity, which helps to explain some perplexing observations from lesion studies (DeLong & Wichmann 2010). The detailed timing of integration will likely be critical to understand the modulation of thalamic nuclei by BG output. 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 497_ 

Motor thalamus can be divided into BG-recipient and cerebellar-recipient zones distinguished by differences in molecularly defined cell types in recipient areas (Kuramoto et al. 2011, Phillips et al. 2019), and this division is clearly reflected in the structure of ascending projections in singlecell reconstruction studies (Kuramoto et al. 2009, 2015; Phillips et al. 2019). Cerebellum is an interesting complement to BG (Bostan & Strick 2010,Kornhuber 1971),sending excitatory output projections to many of the same regions that are inhibited by BG output, including the motor thalamus (Anderson & Turner 1991a,Phillips et al.2019),SC (May 2006),and midbrain locomotor region (Semba & Fibiger 1992). Within multiple motor-associated areas of cortex, a majority of BG-recipient TC axons terminate in layer 1 [ _>_ 50% from the ventral anterior and ventral lateral nuclei (Kuramoto et al.2009), _>_ 70% from the ventromedial nucleus (Kuramoto et al.2015)],while cerebellar-recipient TC axons terminate in deeper layers (Phillips et al. 2019). Motor thalamus may thus be separated into first-order, cerebellar-recipient neurons that strongly drive cortical activity and are modulated by layer 6 corticothalamic feedback, and higher-order, BG-recipient neurons that are strongly driven by layer 5 cortical input and return modulatory feedback to the cortex (Phillips et al. 2019, Sherman 2016). In considering how these superficial BG-recipient TC axons might influence motor-related activity in layer 5 neurons, it is notable that distal inputs onto such neurons have been shown to modulate the gain of their responses to somatic current injection (Larkum et al. 2004) and synaptic plasticity (Williams & Holtmaat 2019). A recent study imaging mouse superficial TC axons during a lever-pulling task found that putative BG-recipient TC axons encoded the vigor of lever pulls, and their activity was important for motor adaptations that occurred across training (Tanaka et al. 2018). Together, these observations are consistent with a model in which BG output activity can modulate synaptic plasticity or burst activity within corticofugal projection neurons to shape action specification upstream of BG, contingent upon feedback from BG output. 

## **SUMMARY** 

**==> picture [101 x 17] intentionally omitted <==**

Activity in BG continuously encodes the kinematics of movement during the execution of diverse purposive actions. Perturbations of BG function, from chronic manipulations and disease states to rapid acute manipulations at the timescale of individual movements, produce reliable changes in movement kinematics while often preserving the initiation (and selection) of action. Moreover, properties of BG intrinsic circuitry appear consistent with functions such as the modulation of temporal dynamics of activity, feedback gain control, and plasticity. Finally, the anatomy of BG circuits from feedforward convergence onto midbrain and brainstem premotor areas to their feedback through high-order thalamic nuclei suggests that BG function must be understood in terms of its integration with and modulation of descending control signals that shape movement execution. One major function of BG is to specify continuous parameters of movement execution such as movement vigor—a function that could be implemented via gain modulation. To exemplify the importance of gain modulation, we summarized its role in shaping sensorimotor transforms both in a separate cortical region ( **Supplemental Appendix 1** ) and in the major downstream target of BG output (SC). In both cases, smooth changes in the gain of activity play critical roles in affording stable performance despite inherent variability in sensory-guided actions. 

Adaptive behavior requires continuous specification of the movements that constitute action. BG plays a critical role in the implicit specification of continuous movement parameters that allow for stable and robust actions directed toward explicit goals. Why use BG circuits for continuous modulation of movement? We return to the analogy of an engineered system—the graphic equalizer—in which instantaneous response and broad bandwidth are critical to amplifier performance. Recurrent excitatory connectivity, which gives rise to the robust and slow timescale 

_498 Park[•] Coddington[•] Dudman_ 

dynamics that are critical to many aspects of behavior, presents significant challenges for gain modulation [although they are surmountable with clever engineering of networks (Stroud et al. 2018)]. We suggest that the lack of recurrent excitation and the feedforward, convergent organization of BG circuits provide an ideal circuit motif for systems-level gain modulation. 

There are significant open questions that remain to be addressed. First, we currently lack an understanding of how the topography of BG output is related to the topography of other descending input pathways, for example, corticofugal projections. The SC would seem to be an ideal place to examine how these projection maps relate to each other; however, it will require synapse-level resolution mapping of connectivity at mesoscale—a daunting technical challenge. Second, it is unclear whether rate models that consider average modulation of output or slow dynamics of activity are sufficient to describe the activity underlying movement execution, and there is substantial evidence that BG output may play an even more critical role in modulating precise timing of activity. Spike-timing codes are known to be important at the periphery (Sober et al. 2018), and a deeper appreciation of the importance of precise spike timing in premotor areas like SC or feedback pathways through thalamus is necessary. Third, it will be critical that reinforcement learning algorithms that have largely described behavior at the level of action selection begin to incorporate the critical role for continuous specification of movement execution. There has been some progress on such models, which highlights important differences (Yttri & Dudman 2016), but much work remains to be done. 

## **DISCLOSURE STATEMENT** 

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review. 

## **ACKNOWLEDGMENTS** 

The authors thank members of the Dudman Lab for comments on earlier drafts of the manuscript. In particular, James Phillips provided many helpful discussions and insight into the section on thalamus. J.T.D. is a Senior Group Leader at the Janelia Research Campus of the Howard Hughes Medical Institute (HHMI). This work was supported by funding from HHMI. All authors contributed equally to the writing of this review. 

## **LITERATURE CITED** 

Adesnik H, Scanziani M. 2010. Lateral competition for cortical space by layer-specific horizontal circuits. _Nature_ 464(7292):1155–60 

Albin RL, Young AB, Penney JB. 1989. The functional anatomy of basal ganglia disorders. _Trends Neurosci_ . 12(10):366–75 

Aldridge JW,Anderson RJ,Murphy JT.1980.The role of the basal ganglia in controlling a movement initiated by a visually presented cue. _Brain Res_ . 192(1):3–16 

Alexander GE. 1987. Selective neuronal discharge in monkey putamen reflects intended direction of planned limb movements. _Exp. Brain Res._ 67(3):623–34 

Alexander GE, Crutcher MD. 1990a. Preparation for movement: neural representations of intended direction in three motor areas of the monkey. _J. Neurophysiol._ 64(1):133–50 

Alexander GE, Crutcher MD. 1990b. Functional architecture of basal ganglia circuits: neural substrates of parallel processing. _Trends Neurosci_ . 13(7):266–71 

Alexander GE, Crutcher MD. 1990c. Neural representations of the target (goal) of visually guided arm movements in three motor areas of the monkey. _J. Neurophysiol._ 64(1):164–78 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 499_ 

Alexander GE, DeLong MR, Strick PL. 1986. Parallel organization of functionally segregated circuits linking basal ganglia and cortex. _Annu. Rev. Neurosci._ 9:357–81 

Ambroggi F, Ishikawa A, Fields HL, Nicola SM. 2008. Basolateral amygdala neurons facilitate reward-seeking behavior by exciting nucleus accumbens neurons. _Neuron_ 59(4):648–61 

Anderson ME, Horak FB. 1985. Influence of the globus pallidus on arm movements in monkeys. III. Timing of movement-related information. _J. Neurophysiol._ 54(2):433–48 

Anderson ME, Turner RS. 1991a. Activity of neurons in cerebellar-receiving and pallidal-receiving areas of the thalamus of the behaving monkey. _J. Neurophysiol._ 66(3):879–93 

Anderson ME, Turner RS. 1991b. A quantitative analysis of pallidal discharge during targeted reaching movement in the monkey. _Exp. Brain Res._ 86:623–32 

Appell PP, Behan M. 1990. Sources of subcortical GABAergic projections to the superior colliculus in the cat. _J. Comp. Neurol._ 302(1):143–58 

Assous M, Tepper JM. 2019. Excitatory extrinsic afferents to striatal interneurons and interactions with striatal microcircuitry. _Eur. J. Neurosci._ 49(5):593–603 

Averbeck BB, Latham PE, Pouget A. 2006. Neural correlations, population coding and computation. _Nat. Rev. Neurosci._ 7(5):358–66 

Averbeck BB, Lehman J, Jacobson M, Haber SN. 2014. Estimates of projection overlap and zones of convergence within frontal-striatal circuits. _J. Neurosci._ 34(29):9497–505 

Baraduc P, Thobois S, Gan J, Broussolle E, Desmurget M. 2013. A common optimization principle for motor execution in healthy subjects and parkinsonian patients. _J. Neurosci._ 33(2):665–77 

Barbera G, Liang B, Zhang L, Gerfen CR, Culurciello E, et al. 2016. Spatially compact neural clusters in the dorsal striatum encode locomotion relevant information. _Neuron_ 92(1):202–13 

Barter JW, Li S, Sukharnikova T, Rossi MA, Bartholomew RA, Yin HH. 2015. Basal ganglia outputs map instantaneous position coordinates during behavior. _J. Neurosci._ 35(6):2703–16 

Basso MA, Sommer MA. 2011. Exploring the role of the substantia nigra pars reticulata in eye movements. _Neuroscience_ 198:205–12 

Basso MA, Wurtz RH. 2002. Neuronal activity in substantia nigra pars reticulata during target selection. _J. Neurosci._ 22(5):1883–94 

Bayer HM, Handel A, Glimcher PW. 2004. Eye position and memory saccade related responses in substantia nigra pars reticulata. _Exp. Brain Res._ 154(4):428–41 

Bocarsly ME, Jiang W-C, Wang C, Dudman JT, Ji N, Aponte Y. 2015. Minimally invasive microendoscopy system for in vivo functional imaging of deep nuclei in the mouse brain. _Biomed. Opt. Express_ 6(11):4546– 56 

Bodor ÁL, Giber K, Rovó Z, Ulbert I, Acsády L. 2008. Structural correlates of efficient GABAergic transmission in the basal ganglia-thalamus pathway. _J. Neurosci._ 28(12):3090–102 

Bohn DA. 1986. Constant-Q graphic equalizers. _J. Audio Eng. Soc._ 34(9):611–26 

Bosch-Bouju C, Hyland BI, Parr-Brownlie LC. 2013. Motor thalamus integration of cortical, cerebellar and 

basal ganglia information: implications for normal and parkinsonian conditions. _Front. Comput. Neurosci._ 7:163 

Bosch-Bouju C,Smither RA,Hyland BI,Parr-Brownlie LC.2014.Reduced reach-related modulation of motor thalamus neural activity in a rat model of Parkinson’s disease. _J. Neurosci._ 34(48):15836–50 

Bostan AC,Strick PL.2010.The cerebellum and basal ganglia are interconnected. _Neuropsychol.Rev._ 20(3):261– 70 

Brazhnik E, McCoy AJ, Novikov N, Hatch CE, Walters JR. 2016. Ventral medial thalamic nucleus promotes synchronization of increased high beta oscillatory activity in the basal ganglia-thalamocortical network of the hemiparkinsonian rat. _J. Neurosci._ 36:4196–208 

Brown J, Martin KA, Dudman JT. 2016. Behavioral evidence for feedback gain control by the inhibitory microcircuit of the substantia nigra. bioRxiv 090209. **https://doi.org/10.1101/090209** 

Brown J, Pan W-X, Dudman JT. 2014. The inhibitory microcircuit of the substantia nigra provides feedback gain control of the basal ganglia output. _eLife_ 3:e02397 

Brown VJ, Robbins TW. 1989. Elementary processes of response selection mediated by distinct regions of the striatum. _J. Neurosci._ 9(11):3760–65 

_500 Park[•] Coddington[•] Dudman_ 

Buchwald NA, Hull CD, Levine MS. 1979. Basal ganglionic neuronal activity and behavioral set. _Appl. Neurophysiol._ 42(1–2):109–12 

Burke DA, Rotstein HG, Alvarez VA. 2017. Striatal local circuitry: a new framework for lateral inhibition. _Neuron_ 96(2):267–84 

Chevalier G, Deniau JM. 1990. Disinhibition as a basic process in the expression of striatal functions. _Trends Neurosci_ . 13(7):277–80 

Chevalier G, Deniau JM, Thierry AM, Feger J. 1981. The nigro-tectal pathway. An electrophysiological reinvestigation in the rat. _Brain Res_ . 213(2):253–63 

Chevalier G, Vacher S, Deniau JM, Desban M. 1985. Disinhibition as a basic process in the expression of striatal functions. I. The striato-nigral influence on tecto-spinal/tecto-diencephalic neurons. _Brain Res_ . 334(2):215–26 

Coddington LT, Dudman JT. 2019. Learning from action: reconsidering movement signaling in midbrain dopamine neuron activity. _Neuron_ 104(1):63–77 

Coffey KR, Nader M, West MO. 2016. Single body parts are processed by individual neurons in the mouse dorsolateral striatum. _Brain Res_ . 1636:200–7 

Collins AG, Frank MJ. 2014. Opponent actor learning (OpAL): modeling interactive effects of striatal dopamine on reinforcement learning and choice incentive. _Psychol. Rev._ 121(3):337–66 

Costa RM, Cohen D, Nicolelis MAL. 2004. Differential corticostriatal plasticity during fast and slow motor skill learning in mice. _Curr. Biol._ 14(13):1124–34 

Cui G, Jun SB, Jin X, Luo G, Pham MD, et al. 2014. Deep brain optical measurements of cell type-specific neural activity in behaving mice. _Nat. Protoc._ 9(6):1213–28 

Cui G, Jun SB, Jin X, Pham MD, Vogel SS, et al. 2013. Concurrent activation of striatal direct and indirect pathways during action initiation. _Nature_ 494(7436):238–42 

Czubayko U, Plenz D. 2002. Fast synaptic transmission between striatal spiny projection neurons. _PNAS_ 99(24):15764–69 

DeLong M, Wichmann T. 2010. Changing views of basal ganglia circuits and circuit disorders. _Clin. EEG Neurosci._ 41(2):61–67 

DeLong MR. 1990. Primate models of movement disorders of basal ganglia origin. _Trends Neurosci_ . 13(7):281– 85 

DeLong MR, Alexander GE, Georgopoulos AP, Crutcher MD, Mitchell SJ, Richardson RT. 1984. Role of basal ganglia in limb movements. _Hum. Neurobiol._ 2(4):235–44 

Deniau JM, Chevalier G. 1985. Disinhibition as a basic process in the expression of striatal functions. II. 

The striato-nigral influence on thalamocortical cells of the ventromedial thalamic nucleus. _Brain Res_ . 334(2):227–33 

Deniau JM, Mailly P, Maurice N, Charpier S. 2007. The pars reticulata of the substantia nigra: a window to basal ganglia output. _Prog. Brain Res._ 160:151–72 

Desmurget M, Turner RS. 2010. Motor sequences and the basal ganglia: kinematics, not habits. _J. Neurosci._ 30(22):7685–90 

Dobbs LK, Kaplan AR, Lemos JC, Matsui A, Rubinstein M, Alvarez VA. 2016. Dopamine regulation of lateral inhibition between striatal neurons gates the stimulant actions of cocaine. _Neuron_ 90(5):1100–13 

Dudman JT, Gerfen CR. 2015. The basal ganglia. In _The Rat Nervous System_ , ed. G Paxinos, pp. 391–440. New York: Elsevier 

Dudman JT, Krakauer JW. 2016. The basal ganglia: from motor commands to the control of vigor. _Curr. Opin. Neurobiol._ 37:158–66 

Edgerton JR, Jaeger D. 2014. Optogenetic activation of nigral inhibitory inputs to motor thalamus in the mouse reveals classic inhibition with little potential for rebound activation. _Front. Cell. Neurosci._ 8:36 

Evans DA, Stempel AV, Vale R, Ruehle S, Lefler Y, Branco T. 2018. A synaptic threshold mechanism for computing escape decisions. _Nature_ 558(7711):590–94 

Fobbs WC, Bariselli S, Licholai JA, Miyazaki NL, Matikainen-Ankney BA, et al. 2020. Continuous representations of speed by striatal medium spiny neurons. _J. Neurosci._ 40(8):1679–88 

Frank MJ. 2011. Computational models of motivated action selection in corticostriatal circuits. _Curr. Opin. Neurobiol._ 21(3):381–86 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 501_ 

Gabbiani F, Krapp HG, Koch C, Laurent G. 2002. Multiplicative computation in a visual neuron sensitive to looming. _Nature_ 420(6913):320–24 

Gage GJ, Stoetzner CR, Wiltschko AB, Berke JD. 2010. Selective activation of striatal fast-spiking interneurons during choice execution. _Neuron_ 67:466–79 

Gandhi NJ, Katnani HA. 2011. Motor functions of the superior colliculus. _Annu. Rev. Neurosci._ 34:205–31 

Gerfen C, Surmeier D. 2010. Dichotomous modulation of striatal direct and indirect pathway neurons by dopamine. _Annu. Rev. Neurosci._ 34:441–66 

Gittis AH, Nelson AB, Thwin MT, Palop JJ, Kreitzer AC. 2010. Distinct roles of GABAergic interneurons in the regulation of striatal output pathways. _J. Neurosci._ 30(6):2223–34 

Goldberg JH, Farries MA, Fee MS. 2012. Integration of cortical and pallidal inputs in the basal gangliarecipient thalamus of singing birds. _J. Neurophysiol._ 108(5):1403–29 

Goldberg JH, Farries MA, Fee MS. 2013. Basal ganglia output to the thalamus: still a paradox. _Trends Neurosci_ . 36(12):695–705 

Goldberg JH, Fee MS. 2012. A cortical motor nucleus drives the basal ganglia-recipient thalamus in singing birds. _Nat. Neurosci._ 15(4):620–27 

Graybiel AM. 1998. The basal ganglia and chunking of action repertoires. _Neurobiol. Learn. Mem._ 70(1–2):119– 36 

Grillner S, Robertson B, Stephenson-Jones M. 2013. The evolutionary origin of the vertebrate basal ganglia and its role in action selection. _J. Physiol._ 591(22):5425–31 

Guo ZV, Inagaki HK, Daie K, Druckmann S, Gerfen CR, Svoboda K. 2017. Maintenance of persistent activity in a frontal thalamocortical loop. _Nature_ 545(7653):181–86 

Haber SN. 2003. The primate basal ganglia: parallel and integrative networks. _J. Chem. Neuroanat._ 26(4):317– 30 

Handel A,Glimcher PW.1999.Quantitative analysis of substantia nigra pars reticulata activity during a visually guided saccade task. _J. Neurophysiol._ 82(6):3458–75 

Hartline HK, Wagner HG, Ratliff F. 1956. Inhibition in the eye of _Limulus_ . _J. Gen. Physiol._ 39(5):651–73 Hemelt ME, Keller A. 2008. Superior colliculus control of vibrissa movements. _J. Neurophysiol._ 100(3):1245– 54 

Higgs MH, Wilson CJ. 2016. Unitary synaptic connections among substantia nigra pars reticulata neurons. _J. Neurophysiol._ 115(6):2814–29 

Hikosaka O, Takikawa Y, Kawagoe R. 2000. Role of the basal ganglia in the control of purposive saccadic eye movements. _Physiol. Rev._ 80(3):953–78 

Hikosaka O, Wurtz RH. 1983a. Visual and oculomotor functions of monkey substantia nigra pars reticulata. 

I. Relation of visual and auditory responses to saccades. _J. Neurophysiol._ 49(5):1230–53 

Hikosaka O, Wurtz RH. 1983b. Visual and oculomotor functions of monkey substantia nigra pars reticulata. IV. Relation of substantia nigra to superior colliculus. _J. Neurophysiol._ 49(5):1285–301 

Hikosaka O, Wurtz RH. 1985. Modification of saccadic eye movements by GABA-related substances. II. Effects of muscimol in monkey substantia nigra pars reticulata. _J. Neurophysiol._ 53(1):292–308 

Hikosaka O, Wurtz RH. 1986. Saccadic eye movements following injection of lidocaine into the superior colliculus. _Exp. Brain Res._ 61(3):531–39 

Horak FB, Anderson ME. 1984a. Influence of globus pallidus on arm movements in monkeys. I. Effects of kainic acid-induced lesions. _J. Neurophysiol._ 52(2):290–304 

Horak FB, Anderson ME. 1984b. Influence of globus pallidus on arm movements in monkeys. II. Effects of stimulation. _J. Neurophysiol._ 52(2):305–22 

Hoy JL, Bishop HI, Niell CM. 2019. Defined cell types in superior colliculus make distinct contributions to prey capture behavior in the mouse. _Curr. Biol._ 29(23):4130–38.e5 

Hughes HC, Reuter-Lorenz PA, Nozawa G, Fendrich R. 1994. Visual-auditory interactions in sensorimotor processing: saccades versus manual responses. _J. Exp. Psychol. Hum. Percept. Perform._ 20(1):131–53 

Humphries MD, Stewart RD, Gurney KN. 2006. A physiologically plausible model of action selection and oscillatory activity in the basal ganglia. _J. Neurosci._ 26(50):12921–42 

Hunnicutt BJ, Jongbloets BC, Birdsong WT, Gertz KJ, Zhong H, Mao T. 2016. A comprehensive excitatory input map of the striatum reveals novel functional organization. _eLife_ 5:e19103 

_502 Park[•] Coddington[•] Dudman_ 

- Inase M, Buford JA, Anderson ME. 1996. Changes in the control of arm position, movement, and thalamic discharge during local inactivation in the globus pallidus of the monkey. _J. Neurophysiol._ 75(3):1087–104 

- Jin X, Tecuapetla F, Costa RM. 2014. Basal ganglia subcircuits distinctively encode the parsing and concatenation of action sequences. _Nat. Neurosci._ 17(3):423–30 

- Jonas E, Kording KP. 2017. Could a neuroscientist understand a microprocessor? _PLoS Comput. Biol._ 13(1):e1005268 

- Kaneda K, Isa K, Yanagawa Y, Isa T. 2008. Nigral inhibition of GABAergic neurons in mouse superior colliculus. _J. Neurosci._ 28(43):11071–78 

- Katnani HA, Gandhi NJ. 2012. The relative impact of microstimulation parameters on movement generation. _J. Neurophysiol._ 108(2):528–38 

- Kawagoe R, Takikawa Y, Hikosaka O. 1998. Expectation of reward modulates cognitive signals in the basal ganglia. _Nat. Neurosci._ 1(5):411–16 

- Kawaguchi Y, Wilson CJ, Emson PC. 1990. Projection subtypes of rat neostriatal matrix cells revealed by intracellular injection of biocytin. _J. Neurosci._ 10(10):3421–38 

- Kim J, Kim Y, Nakajima R, Shin A, Jeong M, et al. 2017. Inhibitory basal ganglia inputs induce excitatory motor signals in the thalamus. _Neuron_ 95(5):1181–96.e8 

- Kim N, Barter JW, Sukharnikova T, Yin HH. 2014. Striatal firing rate reflects head movement velocity. _Eur. J. Neurosci._ 40(10):3481–90 

- Kim N, Li HE, Hughes RN, Watson GDR, Gallegos D, et al. 2019. A striatal interneuron circuit for continuous target pursuit. _Nat. Commun._ 10:2715 

- Klaus A, Alves da Silva J, Costa RM. 2019. What, if, and when to move: basal ganglia circuits and self-paced action initiation. _Annu. Rev. Neurosci._ 42:459–83 

- Klaus A, Martins GJ, Paixao VB, Zhou P, Paninski L, Costa RM. 2017. The spatiotemporal organization of the striatum encodes action space. _Neuron_ 95(5):1171–80.e7. Erratum. 2017. _Neuron_ 96(4):949 

- Koós T, Tepper JM. 1999. Inhibitory control of neostriatal projection neurons by GABAergic interneurons. _Nat. Neurosci._ 2(5):467–72 

- Koos T, Tepper JM, Wilson CJ. 2004. Comparison of IPSCs evoked by spiny and fast-spiking neurons in the neostriatum. _J. Neurosci._ 24(36):7916–22 

- Kornhuber HH. 1971. Motor functions of cerebellum and basal ganglia: the cerebellocortical saccadic (bal- 

   - listic) clock, the cerebellonuclear hold regulator, and the basal ganglia ramp (voluntary speed smooth movement) generator. _Kybernetik_ 8(4):157–62 

- Kravitz AV, Freeze BS, Parker PRL, Kay K, Thwin MT, et al. 2010. Regulation of parkinsonian motor behaviours by optogenetic control of basal ganglia circuitry. _Nature_ 466(7306):622–26 

- Kupferschmidt DA,Juczewski K,Cui G,Johnson KA,Lovinger DM.2017.Parallel,but dissociable,processing in discrete corticostriatal inputs encodes skill learning. _Neuron_ 96(2):476–89.e5 

- Kuramoto E, Fujiyama F, Nakamura KC, Tanaka Y, Hioki H, Kaneko T. 2011. Complementary distribution of glutamatergic cerebellar and GABAergic basal ganglia afferents to the rat motor thalamic nuclei. _Eur. J. Neurosci._ 33(1):95–109 

- Kuramoto E, Furuta T, Nakamura KC, Unzai T, Hioki H, Kaneko T. 2009. Two types of thalamocortical projections from the motor thalamic nuclei of the rat: a single neuron-tracing study using viral vectors. _Cereb. Cortex_ 19(9):2065–77 

- Kuramoto E, Ohno S, Furuta T, Unzai T, Tanaka YR, et al. 2015. Ventral medial nucleus neurons send thalamocortical afferents more widely and more preferentially to layer 1 than neurons of the ventral anteriorventral lateral nuclear complex in the rat. _Cereb. Cortex_ 25(1):221–35 

- Larkum ME, Senn W, Lüscher H-R. 2004. Top-down dendritic input increases the gain of layer 5 pyramidal neurons. _Cereb. Cortex_ 14(10):1059–70 

- Lee C,Rohrer WH,Sparks DL.1988.Population coding of saccadic eye movements by neurons in the superior colliculus. _Nature_ 332(6162):357–60 

- Lee K, Holley SM, Shobe JL, Chong NC, Cepeda C, et al. 2018. Parvalbumin interneurons modulate striatal output and enhance performance during associative learning. _Neuron_ 93(6):1451–63.e4 

- Liles SL. 1985. Activity of neurons in putamen during active and passive movements of wrist. _J. Neurophysiol._ 53(1):217–36 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 503_ 

Mallet N, Le Moine C, Charpier S, Gonon F. 2005. Feedforward inhibition of projection neurons by fastspiking GABA interneurons in the rat striatum in vivo. _J. Neurosci._ 25(15):3857–69 

- Markowitz JE, Gillis WF, Beron CC, Neufeld SQ, Robertson K, et al. 2018. The striatum organizes 3D behavior via moment-to-moment action selection. _Cell_ 174(1):44–58.e17 

- May PJ. 2006. The mammalian superior colliculus: laminar structure and connections. _Prog. Brain Res._ 151:321–78 

- McGinty VB, Lardeux S, Taha SA, Kim JJ, Nicola SM. 2013. Invigoration of reward seeking by cue and proximity encoding in the nucleus accumbens. _Neuron_ 78(5):910–22 

- Meng C, Zhou J, Papaneri A, Peddada T, Xu K, Cui G. 2018. Spectrally resolved fiber photometry for multicomponent analysis of brain circuits. _Neuron_ 98(4):707–17.e4 

Meng G, Liang Y, Sarsfield S, Jiang W-C, Lu R, et al. 2019. High-throughput synapse-resolving two-photon fluorescence microendoscopy for deep-brain volumetric imaging in vivo. _eLife_ 8:e40805 

- Mink JW. 1996. The basal ganglia: focused selection and inhibition of competing motor programs. _Prog. Neurobiol._ 50(4):381–425 

- Mink JW, Thach WT. 1991a. Basal ganglia motor control. III. Pallidal ablation: normal reaction time, muscle cocontraction, and slow movement. _J. Neurophysiol._ 65(2):330–51 

Mink JW, Thach WT. 1991b. Basal ganglia motor control. II. Late pallidal timing relative to movement onset and inconsistent pallidal coding of movement parameters. _J. Neurophysiol._ 65(2):301–29 

Mink JW, Thach WT. 1991c. Basal ganglia motor control. I. Nonexclusive relation of pallidal discharge to five movement modes. _J. Neurophysiol._ 65(2):273–300 

Mitchell SJ, Silver RA. 2003. Shunting inhibition modulates neuronal gain during synaptic excitation. _Neuron_ 38(3):433–45 

Munoz DP, Guitton D. 1986. Presaccadic burst discharges of tecto-reticulo-spinal neurons in the alert headfree and -fixed cat. _Brain Res_ . 398(1):185–90 

Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. 2019. Single-trial neural dynamics are dominated by richly varied movements. _Nat. Neurosci._ 22:1677–1686 

Nakamura KC, Sharott A, Magill PJ. 2012. Temporal coupling with cortex distinguishes spontaneous neuronal 

activities in identified basal ganglia-recipient and cerebellar-recipient zones of the motor thalamus. _Cereb. Cortex_ 24(1):81–97 

Neafsey EJ, Hull CD, Buchwald NA. 1978. Preparation for movement in the cat. II. Unit activity in the basal ganglia and thalamus. _Electroencephalogr. Clin. Neurophysiol._ 44(6):714–23 

Nelson AB, Kreitzer AC. 2014. Reassessing models of basal ganglia function and dysfunction. _Annu. Rev. Neurosci._ 37:117–35 

Ohno S, Kuramoto E, Furuta T, Hioki H, Tanaka YR, et al. 2012. A morphological analysis of thalamocortical axon fibers of rat posterior thalamic nuclei: a single neuron tracing study with viral vectors. _Cereb. Cortex_ 22(12):2840–57 

Owen SF, Berke JD, Kreitzer AC. 2018. Fast-spiking interneurons supply feedforward control of bursting, calcium, and plasticity for efficient learning. _Cell_ 172(4):683–95.e15 

Packard MG, McGaugh JL. 1996. Inactivation of hippocampus or caudate nucleus with lidocaine differentially affects expression of place and response learning. _Neurobiol. Learn. Mem._ 65(1):65–72 

Pan WX, Mao T, Dudman JT. 2010. Inputs to the dorsal striatum of the mouse reflect the parallel circuit architecture of the forebrain. _Front. Neuroanat._ 4:147 

Panigrahi B, Martin KA, Li Y, Graves AR, Vollmer A, et al. 2015. Dopamine is required for the neural representation and control of movement vigor. _Cell_ 162(6):1418–30 

Park J, Phillips JW, Martin KA, Hantman AW, Dudman JT. 2019. Flexible routing of motor control signals through neocortical projection neuron classes. bioRxiv 772517. **https://doi.org/10.1101/772517** 

Parker JG, Marshall JD, Ahanonu B, Wu Y-W, Kim TH, et al. 2018. Diametric neural ensemble dynamics in parkinsonian and dyskinetic states. _Nature_ 557(7704):177–82 

Parr-Brownlie LC, Poloskey SL, Bergstrom DA, Walters JR. 2009. Parafascicular thalamic nucleus activity in a rat model of Parkinson’s disease. _Exp. Neurol._ 217(2):269–81 

Paz JT, Chavez M, Saillet S, Deniau JM, Charpier S. 2007. Activity of ventral medial thalamic neurons during absence seizures and modulation of cortical paroxysms by the nigrothalamic pathway. _J. Neurosci._ 27(4):929–41 

_504 Park[•] Coddington[•] Dudman_ 

Perrott DR, Saberi K, Brown K, Strybel TZ. 1990. Auditory psychomotor coordination and visual search performance. _Percept. Psychophys._ 48(3):214–26 

Person AL, Perkel DJ. 2005. Unitary IPSPs drive precise thalamic spiking in a circuit required for learning. _Neuron_ 46(1):129–40 

Philipp R, Hoffmann K-P. 2014. Arm movements induced by electrical microstimulation in the superior colliculus of the macaque monkey. _J. Neurosci._ 34(9):3350–63 

Phillips JW, Schulmann A, Hara E, Winnubst J, Liu C, et al. 2019. A repeated molecular architecture across thalamic pathways. _Nat. Neurosci._ 22:1925–35 

Planert H, Szydlowski SN, Hjorth JJJ, Grillner S, Silberberg G. 2010. Dynamics of synaptic transmission between fast-spiking interneurons and striatal projection neurons of the direct and indirect pathways. _J. Neurosci._ 30(9):3499–507 

Polack P-O, Friedman J, Golshani P. 2013. Cellular mechanisms of brain state–dependent gain modulation in visual cortex. _Nat. Neurosci._ 16(9):1331–39 

Preston RJ,Bishop GA,Kitai ST.1980.Medium spiny neuron projection from the rat striatum: an intracellular horseradish peroxidase study. _Brain Res_ . 183(2):253–63 

Redgrave P, Rodriguez M, Smith Y, Rodriguez-Oroz MC, Lehericy S, et al. 2010. Goal-directed and habitual 

control in the basal ganglia: implications for Parkinson’s disease. _Nat. Rev. Neurosci._ 11(11):760–72 Roberts BM, White MG, Patton MH, Chen R, Mathur BN. 2019. Ensemble encoding of action speed by striatal fast-spiking interneurons. _Brain Struct. Funct._ 224(7):2567–76 

Roseberry TK, Lee AM, Lalive AL, Wilbrecht L, Bonci A, Kreitzer AC. 2016. Cell-type-specific control of brainstem locomotor circuits by basal ganglia. _Cell_ 164(3):526–37 

Rossi MA, Li HE, Lu D, Kim IH, Bartholomew RA, et al. 2016. A GABAergic nigrotectal pathway for coordination of drinking behavior. _Nat. Neurosci._ 19(5):742–48 

Rothman JS, Cathala L, Steuber V, Silver RA. 2009. Synaptic depression enables neuronal gain control. _Nature_ 457(7232):1015–18 

Rovó Z, Ulbert I, Acsády L. 2012. Drivers of the primate thalamus. _J. Neurosci._ 32(49):17894–908 Royer S, Zemelman BV, Losonczy A, Kim J, Chance F, et al. 2012. Control of timing, rate and bursts of hippocampal place cells by dendritic and somatic inhibition. _Nat. Neurosci._ 15:769–75 

Rubelowski JM, Menge M, Distler C, Rothermel M, Hoffmann K-P. 2013. Connections of the superior colliculus to shoulder muscles of the rat: a dual tracing study. _Front. Neuroanat._ 7:17 

Rueda-Orozco PE, Robbe D. 2015. The striatum multiplexes contextual and kinematic information to constrain motor habits execution. _Nat. Neurosci._ 18(3):453–60 

Sales-Carbonell C, Taouali W, Khalki L, Pasquet MO, Petit LF, et al. 2018. No discrete start/stop signals in the dorsal striatum of mice performing a learned action. _Curr. Biol._ 28(19):3044–55.e5 

Salinas E, Thier P. 2000. Gain modulation: a major computational principle of the central nervous system. _Neuron_ 27(1):15–21 

Sato M, Hikosaka O. 2002. Role of primate substantia nigra pars reticulata in reward-oriented saccadic eye movement. _J. Neurosci._ 22(6):2363–73 

Schultz W,Dayan P,Montague PR.1997.A neural substrate of prediction and reward. _Science_ 275(5306):1593– 99 

Schultz W, Romo R. 1990. Dopamine neurons of the monkey midbrain: contingencies of responses to stimuli eliciting immediate behavioral reactions. _J. Neurophysiol._ 63(3):607–24 

Schwab BC, Kase D, Zimnik A, Rosenbaum R, Rubin JE, Turner RS. 2019. Weak modulation of thalamic discharge by basal ganglia output in association with a reaching task. bioRxiv 546598. **https://doi.org/ 10.1101/546598** 

Schwarting RK, Huston JP. 1996. Unilateral 6-hydroxydopamine lesions of meso-striatal dopamine neurons and their physiological sequelae. _Prog. Neurobiol._ 49(3):215–66 

Semba K, Fibiger HC. 1992. Afferent connections of the laterodorsal and the pedunculopontine tegmental nuclei in the rat: a retro-and antero-grade transport and immunohistochemical study. _J. Comp. Neurol._ 323(3):387–410 

Seo M, Lee E, Averbeck BB. 2012. Action selection and action value in frontal-striatal circuits. _Neuron_ 74(5):947–60 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 505_ 

Shenoy KV, Sahani M, Churchland MM. 2013. Cortical control of arm movements: a dynamical systems perspective. _Annu. Rev. Neurosci._ 36:337–59 

Sherman SM. 2016. Thalamus plays a central role in ongoing cortical functioning. _Nat. Neurosci._ 19(4):533–41 Shin S, Sommer MA. 2010. Activity of neurons in monkey globus pallidus during oculomotor behavior compared with that in substantia nigra pars reticulata. _J. Neurophysiol._ 103(4):1874–87 

Silberberg G, Bolam JP. 2015. Local and afferent synaptic pathways in the striatal microcircuitry. _Curr. Opin. Neurobiol._ 33:182–87 

Smalianchuk I,Jagadisan UK,Gandhi NJ.2018.Instantaneous midbrain control of saccade velocity. _J.Neurosci._ 38(47):10156–67 

Smith Y, Galvan A, Ellender TJ, Doig N, Villalba RM, et al. 2014. The thalamostriatal system in normal and diseased states. _Front. Syst. Neurosci._ 8:5 

Sober SJ, Sponberg S, Nemenman I, Ting LH. 2018. Millisecond spike timing codes for motor control. _Trends Neurosci_ . 41(10):644–48 

Somogyi P, Bolam JP, Smith AD. 1981. Monosynaptic cortical input and local axon collaterals of identified striatonigral neurons. A light and electron microscopic study using the Golgi-peroxidase transportdegeneration procedure. _J. Comp. Neurol._ 195(4):567–84 

Sparks DL. 1986. Translation of sensory signals into commands for control of saccadic eye movements: role of primate superior colliculus. _Physiol. Rev._ 66(1):118–71 

Sparks DL, Mays LE. 1990. Signal transformations required for the generation of saccadic eye movements. _Annu. Rev. Neurosci._ 13:309–36 

Stanford TR, Freedman EG, Sparks DL. 1996. Site and parameters of microstimulation: evidence for independent effects on the properties of saccades evoked from the primate superior colliculus. _J. Neurophysiol._ 76(5):3360–81 

Stringer C, Pachitariu M, Steinmetz N, Reddy CB, Carandini M, Harris KD. 2019. Spontaneous behaviors drive multidimensional, brainwide activity. _Science_ 364(6437):eaav7893 

Stroud JP, Porter MA, Hennequin G, Vogels TP. 2018. Motor primitives in space and time via targeted gain modulation in cortical networks. _Nat. Neurosci_ . 21(12):1774–83. Erratum. 2018. _Nat. Neurosci_ . 22:504 

Surmeier DJ, Plotkin J, Shen W. 2009. Dopamine and synaptic plasticity in dorsal striatal circuits controlling action selection. _Curr. Opin. Neurobiol._ 19(6):621–28 

Tai LH, Lee AM, Benavidez N, Bonci A, Wilbrecht L. 2012. Transient stimulation of distinct subpopulations of striatal neurons mimics changes in action value. _Nat. Neurosci._ 15(9):1281–89 

Tanaka YH, Tanaka YR, Kondo M, Terada S-I, Kawaguchi Y, Matsuzaki M. 2018. Thalamocortical axonal ac- 

tivity in motor cortex exhibits layer-specific dynamics during motor learning. _Neuron_ 100(1):244–58.e12 Taverna S, van Dongen YC, Groenewegen HJ, Pennartz CMA. 2004. Direct physiological evidence for synap- 

tic connectivity between medium-sized spiny neurons in rat nucleus accumbens in situ. _J. Neurophysiol_ . 91(3):1111–21 

Tepper JM, Koós T, Wilson CJ. 2004. GABAergic microcircuits in the neostriatum. _Trends Neurosci_ . 27(11):662–69 

Tunstall MJ, Oorschot DE, Kean A, Wickens JR. 2002. Inhibitory interactions between spiny projection neurons in the rat striatum. _J. Neurophysiol._ 88(3):1263–69 

Turner RS, Anderson ME. 1997. Pallidal discharge related to the kinematics of reaching movements in two dimensions. _J. Neurophysiol._ 77(3):1051–74 

Turner RS, Desmurget M. 2010. Basal ganglia contributions to motor control: a vigorous tutor. _Curr. Opin. Neurobiol._ 20(6):704–16 

Van Opstal AJ, Hepp K, Suzuki Y, Henn V. 1995. Influence of eye position on activity in monkey superior colliculus. _J. Neurophysiol._ 74(4):1593–610 

Wallace MT, Wilkinson LK, Stein BE. 1996. Representation and integration of multiple sensory inputs in primate superior colliculus. _J. Neurophysiol._ 76(2):1246–66 

Wang L, Rangarajan KV, Gerfen CR, Krauzlis RJ. 2018. Activation of striatal neurons causes a perceptual decision bias during visual change detection in mice. _Neuron_ 97(6):1369–81.e5 

Werner W, Dannenberg S, Hoffmann K-P. 1997. Arm-movement-related neurons in the primate superior 

colliculus and underlying reticular formation: comparison of neuronal activity with EMGs of muscles of the shoulder, arm and trunk during reaching. _Exp. Brain Res._ 115(2):191–205 

_506 Park[•] Coddington[•] Dudman_ 

West MO,Carelli RM,Pomerantz M,Cohen SM,Gardner JP,et al.1990.A region in the dorsolateral striatum of the rat exhibiting single-unit correlations with specific locomotor limb movements. _J. Neurophysiol._ 64(4):1233–46 

- Westby GWM, Collinson C, Redgrave P, Dean P. 1994. Opposing excitatory and inhibitory influences from the cerebellum and basal ganglia converge on the superior colliculus: an electrophysiological investigation in the rat. _Eur. J. Neurosci._ 6(8):1335–42 

- Williams LE, Holtmaat A. 2019. Higher-order thalamocortical inputs gate synaptic long-term potentiation via disinhibition. _Neuron_ 101(1):91–102.e4 

- Wiltschko AB, Johnson MJ, Iurilli G, Peterson RE, Katon JM, et al. 2015. Mapping sub-second structure in mouse behavior. _Neuron_ 88(6):1121–35 

- Winnubst J, Bas E, Ferreira TA, Wu Z, Economo MN, et al. 2019. Reconstruction of 1,000 projection neurons reveals new cell types and organization of long-range connectivity in the mouse brain. _Cell_ 179(1):268– 81.e13 

- Wolf AB, Lintz MJ, Costabile JD, Thompson JA, Stubblefield EA, Felsen G. 2015. An integrative role for the superior colliculus in selecting targets for movements. _J. Neurophysiol._ 114(4):2118–31 

- Xu M, Li L, Pittenger C. 2016. Ablation of fast-spiking interneurons in the dorsal striatum, recapitulating abnormalities seen post-mortem in Tourette syndrome, produces anxiety and elevated grooming. _Neuroscience_ 324:321–29 

- Yazebnik Y. 2012. Can a biologist fix a radio?—Or, what I learned while studying apoptosis. _Cancer Cell_ 2(3):179–82 

- Yttri EA, Dudman JT. 2016. Opponent and bidirectional control of movement velocity in the basal ganglia. _Nature_ 533(7603):402–6 

- Yttri EA, Dudman JT. 2018. A proposed circuit computation in basal ganglia: history-dependent gain. _Mov. Disord._ 33(5):704–16 

- Zahn JR, Abel LA, Dell’Osso LF. 1978. Audio-ocular response characteristics. _Sens. Processes_ 2(1):32–37 

_www.annualreviews.org[•] Basal Ganglia Circuits for Action Specification 507_ 

**Annual Review of Neuroscience** Volume 43, 2020 

## Contents 

Interneuron Types as Attractors and Controllers _Gord Fishell and Adam Kepecs_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 1 Mechanisms Underlying the Neural Computation of Head Direction _Brad K. Hulse and Vivek Jayaraman_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 31 CA2: A Highly Connected Intrahippocampal Relay _Steven J. Middleton and Thomas J. McHugh_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 55 Navigating Through Time: A Spatial Navigation Perspective on How the Brain May Encode Time _John B. Issa, Gilad Tocker, Michael E. Hasselmo, James G. Heys, and Daniel A. Dombeck_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 73 Synaptic Plasticity Forms and Functions _Jeffrey C. Magee and Christine Grienberger_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 95 The Glial Perspective on Sleep and Circadian Rhythms _Gregory Artiushin and Amita Sehgal_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 119 Reward Contributions to Serotonergic Functions _Zhixiang Liu, Rui Lin, and Minmin Luo_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 141 Calcium Signaling in the Oligodendrocyte Lineage: Regulators and Consequences _Pablo M. Paez and David A. Lyons_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 163 Neural Mechanisms of Itch _Mark Lay and Xinzhong Dong_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 187 Mechanosensitive Ion Channels: Structural Features Relevant to Mechanotransduction Mechanisms _Peng Jin, Lily Yeh Jan, and Yuh-Nung Jan_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 207 The Anatomy and Physiology of Claustrum-Cortex Interactions _Jesse Jackson, Jared B. Smith, and Albert K. Lee_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 231 Computation Through Neural Population Dynamics _Saurabh Vyas, Matthew D. Golub, David Sussillo, and Krishna V. Shenoy_ **p p p p p p p p p p p p p** 249 Finding the Brain in the Nose _David H. Brann and Sandeep Robert Datta_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 277 

_v_ 

Impairments to Consolidation, Reconsolidation, and Long-Term Memory Maintenance Lead to Memory Erasure _Josu´e Haubrich, Matteo Bernabo, Andrew G. Baker, and Karim Nader_ **p p p p p p p p p p p p p p p p** 297 Suckling, Feeding, and Swallowing: Behaviors, Circuits, and Targets for Neurodevelopmental Pathology _Thomas M. Maynard, Irene E. Zohn, Sally A. Moody, and Anthony-S. LaMantia_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 315 Neuropod Cells: The Emerging Biology of Gut-Brain Sensory Transduction _Melanie Maya Kaelberer, Laura E. Rupprecht, Winston W. Liu, Peter Weng, and Diego V. Boh´orquez_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 337 Endogenous Opioids at the Intersection of Opioid Addiction, Pain, and Depression: The Search for a Precision Medicine Approach _Michael A. Emery and Huda Akil_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 355 3D Brain Organoids: Studying Brain Development and Disease Outside the Embryo _Silvia Velasco, Bruna Paulsen, and Paola Arlotta_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 375 Neuromodulation of Brain State and Behavior _David A. McCormick, Dennis B. Nestvogel, and Biyu J. He_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 391 The Neural Basis of Escape Behavior in Vertebrates _Tiago Branco and Peter Redgrave_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 417 Toward Community-Driven Big Open Brain Science: Open Big Data and Tools for Structure, Function, and Genetics _Adam S. Charles, Benjamin Falk, Nicholas Turner, Talmo D. Pereira, Daniel Tward, Benjamin D. Pedigo, Jaewon Chung, Randal Burns, Satrajit S. Ghosh, Justus M. Kebschull, William Silversmith, and Joshua T. Vogelstein_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 441 The _Drosophila_ Mushroom Body: From Architecture to Algorithm in a Learning Circuit _Mehrab N. Modi, Yichun Shuai, and Glenn C. Turner_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 465 Basal Ganglia Circuits for Action Specification _Junchol Park, Luke T. Coddington, and Joshua T. Dudman_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 485 The Genetic Control of Stoichiometry Underlying Autism _Robert B. Darnell_ **p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p p** 509 **Indexes** Cumulative Index of Contributing Authors, Volumes 34–43 **p p p p p p p p p p p p p p p p p p p p p p p p p p p** 535 

_vi Contents_ 

