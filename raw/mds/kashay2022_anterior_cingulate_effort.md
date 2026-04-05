bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

## 1 **Neural activity in the anterior cingulate cortex is required for effort-based** 2 **decision making** 

## 3 

## 4 

5 Adrienne Q. Kashay[1] , Jovian Y. Cheung[1] , Rahil N. Vaknalli[1] , Molly J. Delaney[1] , Michael B. Navarro Jr.[1] , 6 Christabelle Junaidi[1] , Faith Veenker[1] , Morgan E. Neuwirth[1] , Christopher J. Gabriel[1,3] , Laura A. DeNardo[2] and 7 Scott A. Wilke[1,#] 

- 8 

9 1Semel Institute for Neuroscience and Human Behavior, Department of Psychiatry; 2Department of Physiology; 10 3Neuroscience Interdepartmental Program. David Geffen School of Medicine, University of California, Los 11 Angeles, California 90024. 

- 12 

13 

14 

#Correspondence: Dr. Scott Wilke, 760 Westwood Plaza, Semel Institute Rm. #57-438, David Geffen School of Medicine at UCLA, Los Angeles, CA 90024 - swilke@mednet.ucla.edu 

15 

16 

17 **Short title:** ACC activity mediates effort-based decision making 

18 

- 19 

**Conflict of interest** : The authors declare no competing financial interests 

20 

- 21 **Acknowledgements:** This work was funded by NIH K08MH116125 (SAW). 

22 

23 

**Keywords** : prefrontal cortex, anterior cingulate cortex, effort, decision making, T-maze. 

24 

25 

26 

27 

28 29 30 31 32 

33 34 

35 

36 

37 

38 

39 

40 

41 

42 

43 

44 

45 

46 47 

48 49 50 51 52 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 53 **ABSTRACT** 

- 54 Adaptive decision making requires the evaluation of cost-benefit tradeoffs to guide action selection. Effort- 

- 55 based decision making (EBD) involves weighing predicted gains against effort costs and is disrupted in several 56 neuropsychiatric disorders. The anterior cingulate cortex (ACC) is postulated to control effort-based choice via 

- 57 its role in encoding the value of overcoming effort costs in rodent EBD assays. However, temporally precise 

- 58 methods of manipulating neural activity have rarely been applied to EBD. We developed and validated a 

- 59 mouse version of the barrier T-maze EBD task, in which action selection is spatiotemporally segregated from 

- 60 surmounting an effortful obstacle and effort is minimally confounded with time cost. Optogenetic silencing of 61 ACC excitatory neurons during action selection, rapidly and reversibly impaired preference to exert greater 

- 62 effort for a larger reward, when a less effortful alternative was available. Detailed analysis of mouse choice 63 trajectories revealed that silencing ACC disrupts kinematics, especially prior to high effort choices. However, 

- 64 there were no effects on overall mobility or tendency to exert effort in non-choice assays. These findings 

- 65 establish causality between ACC neural activity and effortful action selection during spatial cost-benefit 

- 66 decision making. 

- 67 

- 68 **SIGNIFICANCE STATEMENT** Disturbances in evaluating effort-based costs during decision making occur in 69 depression, schizophrenia, addiction and Parkinson's disease. Precisely resolving the function of prefrontal 

- 70 brain regions in mediating these processes will reveal key loci of dysfunction and potential therapeutic 

- 71 intervention in these disorders. 

- 72 

- 73 

- 74 

- 75 

- 76 

- 77 

- 78 

- 79 

- 80 

- 81 

- 82 

- 83 

- 84 

- 85 

- 86 

- 87 

- 88 

89 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 90 **INTRODUCTION:** 

- 91 Goal-directed decision making requires prospectively evaluating cost-benefit tradeoffs to guide action 

- 92 selection. Effort costs, the motor and cognitive resources required for performing an action, are a critical 

- 93 consideration in making adaptive choices. Effort-based decision making (EBD) is specifically impaired in 

- 94 patients with depression, schizophrenia, addiction and Parkinson's disease[1–6] . The anterior cingulate cortex 

- 95 (ACC) is a prefrontal region that has consistently been implicated in evaluating both cognitive and physical 

- 96 effort costs[7–15] . Moreover, the ACC has been associated with a wide variety of behavioral functions relevant to 

- 97 decision making more broadly. These include computation of reward value and action outcomes, representing 

- 98 reward prediction errors, model-based action selection, exploration of alternative strategies, tracking outcomes 

- 99 across trials, and others[16–25] . Thus, the ACC is well positioned to mediate effort-based decision making 

- 00 including evaluating the effort-related value of potential actions, selecting between these options and carrying 01 them to completion. 

- 02 Much of the seminal work on the neurobiology of spatial EBD has been done using the barrier T-maze 

- 03 task, originally developed by Salamone and colleagues[26,27] . In this task, animals must choose between 

- 04 climbing a vertical barrier to access a large reward or taking an unobstructed path to a smaller reward. Lesion 

- 05 studies, done primarily in rats, have found that ACC, but not prelimbic or orbitofrontal regions, disrupts spatial 

- 06 EBD[7,8,13,28,29] (though see a null result in mice[30] ). However, ACC lesions or inactivation do not universally 

- 07 impair effortful behavior or effortful choice tasks[13,29] . For example, operant lever-pressing choice tasks have 

- 08 yielded both negative results[13] and findings suggesting a reduced preference to exert effort for larger 

- 09 rewards[31–33] . This work clearly implicates ACC in rodent EBD, but studies have primarily used lesions or 

- 10 pharmacology to establish causal linkages. These approaches generally affect larger regions, produce 

- 11 observations lacking temporal precision and cannot address cell-type specific contributions in ACC. 

- 12 The temporal relationship between the activity of ACC neurons and effort-based decision making has 

- 13 been explored using electrophysiological approaches. Recordings of population or single neuron activity from 

- 14 ACC find representations of choice options with the highest utility based on integrating effort cost and reward 

- 15 value[11,14,34,35] . These studies find clear encoding of effort-related value, but also high degrees of heterogeneity 

- 16 indicating that ACC neurons can respond to a broad set of task features.  Other studies have begun to explore 

- 17 the encoding of effort-related behaviors at the ensemble level using miniaturized head-mounted microscopes, 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 18 or multielectrode recordings[32,36] . Similarly, local field potential recordings between ACC and reward related 

- 19 regions implicate oscillatory activity in spatial effort-based decision making[37–39] . Thus, ACC is critical for 

- 20 representing the effort-related value of actions and activity is temporally aligned with specific aspects of 21 decision making. 

- 22 Here, we overcome some of the limitations of traditional lesion and pharmacologic methods used to 

- 23 study the causal role of ACC in EBD. Because prior studies used methods lacking temporal precision, the 

- 24 question of when during a trial ACC is required for EBD is not known. Moreover, when ACC function is 

- 25 disrupted, it is not known how this impacts the action sequences required to select and carry out a choice. In 

- 26 this study we resolve these questions in order to shed light on the mechanistic function of ACC in EBD. We 

- 27 use mice to clarify conflicting results as to the role of ACC for EBD across species and to enable work in a 

- 28 genetically tractable model. To do this, we developed a protocol for training and testing mice in the barrier T- 

- 29 maze. Mice readily learn the task and behavior is sensitive to altering choice utility by changing reward 

- 30 magnitude or effort cost with minimal confounding due to time cost. We then show that bilateral optogenetic 

- 31 silencing of ACC excitatory neurons prior to or during action selection can rapidly and reversibly disrupt 

- 32 preference for high effort, high reward choices on a trial-by-trial basis. When effort cost was equalized, mice 

- 33 switched to choosing the more rewarded arm on all trials, indicating that spatial memory, reward preference 

- 34 and ability to enact effortful behavior were not disrupted. We then used machine learning based behavior 

- 35 tracking and custom zone-based analysis software to investigate how silencing ACC affects choice trajectory 

- 36 during EBD. Silencing ACC disrupts the microstructure of choice behavior, introducing brief pauses as mice 

- 37 approach the maze choice point suggesting that ACC mediates online control over ballistic movements during 

- 38 EBD. These effects were specific to an explicitly goal-directed context as silencing ACC did not disrupt effort or 

- 39 movement when overt decision making is not required. 

- 40 

- 41 **MATERIALS AND METHODS:** 

- 42 All experiments were conducted in accordance with procedures established by the administrative panels on 43 laboratory animal care at the University of California, Los Angeles. 

- 44 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 45 **Animals** : All experiments use C57BL/6J wildtype mice of either sex (12-18 weeks of age), bred in house or 

- 46 ordered from Jackson Laboratories. 

- 47 

- 48 **Viral vectors and targeting/expression** : Adult mice were stereotaxically injected at 7-10 weeks of age with 

- 49 600 nl of 1.5x10[13] vg/ml AAV1-CKIIa-stGtACR2-FusionRed (AddGene) or 7x10[12] vg/ml AAV1-CKIIa-mCherry 

- 50 control at bilateral ACC (antero-posterior (AP) +1.4, medio-lateral (ML) ±0.35, dorso-ventral (DV) -1.3mm 

- 51 relative to bregma). Bilateral 200 µm diameter, 0.37NA fiber optic cannulae (Newdoon) were implanted over 

- 52 ACC at +1.4 AP, ±0.35 ML, -1.3 DV. Implants were affixed onto the skull using Metabond dental cement 

- 53 (Parkell). Targeting of viral constructs/cannulae were confirmed via post-hoc histology without immunostaining. 

- 54 

- 55 **T-maze Behavior Apparatus:** Our T-Maze was constructed in-house using white corrugated plastic 

- 56 (Coroplast). Removable, transparent food cups were inserted into slots in each arm. Barriers were constructed 

- 57 from diamond pattern wire-mesh and were 5 or 10 cm in vertical height with ~45 degrees sloping ramp on the 

- 58 backside and placed at a standard position in the maze. Removable guillotine style doors were inserted to 

- 59 create a start box, and to block off one arm of the maze during forced trials or after mice made a choice on a 

- 60 given trial. Experiments were conducted inside specialized chambers with an open front, LED lighting and 

- 61 ports to pass cabling in and out. The maze was fixed in place within the chamber and a webcam was mounted 

- 62 overhead in a fixed location (ELP 2.8-12mm Varifocal 1.3 megapixels, 30 fps). Mazes were hand-operated by 

- 63 an experimenter standing in front of the chamber. 

- 64 

- 65 **T-maze Behavioral Procedures** : Mice were housed under standard 12-h light/dark cycles, and all 

- 66 experiments were performed during the light portion of the cycle. Mice were group housed and allowed to fully 

- 67 recover post-operatively (~1 week). Mice were habituated to human handling and food intake was restricted 

- 68 until mice were 80-85% of the _ad libitum_ feeding weight. Throughout the experiment, mice were weighed and 

- 69 fed daily rations. Reward pellets were peanut butter chips (Reese's), precisely cut into small cubes (~0.01g; 

- 70 tolerance 0.08-0.12g). A random subset of pellets were weighed to ensure consistency across batches. After 

- 71 mice reached target weight, they are allowed to explore the maze with 20 food pellets scattered throughout. 

- 72 Once mice ate all the food pellets in <5 minutes, behavior was further shaped so that mice ran trials and could 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 73 easily locate single food pellets in each reward cup. Thereafter, one maze arm was designated as high reward 

- 74 (HR, 3 pellets) and the other as low reward (LR, 1 pellet). The HR arm was counterbalanced (left vs. right) 

- 75 across mice, with mice trained against any inherent initial side biases. On each training day, mice were forced 

- 76 to sample each arm and then ran 15 choice trials. Once mice learned to choose the HR arm (>70%, ~2-7days), 

- 77 barrier training commenced. Mice were trained on a 5cm, then 10cm barrier in the HR arm. If mice refused to 

- 78 climb the barrier, additional forced trials were introduced to ensure adequate sampling of HR arm (up to 4/day). 

- 79 Training was complete when mice achieved >70% high effort/HR choices on 2 consecutive days (~5-10 days). 

- 80 For some experiments, the reward differential was manipulated and/or a second 10cm barrier was introduced 

- 81 in the LR arm to equalize effort cost between choices. Mice ran behavior trials 5 days per week, with food 

- 82 deprivation maintained during the weekend. After each trial, mice were placed in a home cage during the inter- 

- 83 trial interval (ITI), while the maze was reset (timed to ~60 seconds). Trials were run consecutively for each 

- 84 individual mouse and the maze was cleaned thoroughly with 70% ethanol in between mice. For optogenetics 

- 85 experiments we utilized white barriers and transparent food cups to enhance contrast between subject and 

- 86 background to facilitate segmentation of animals during behavior. 

- 87 

- 88 **Tail suspension test (TST):** For the TST, mice were suspended by taping their tail to a bar ~12 inches above 

- 89 the tabletop, within 4 inch wide stalls of a custom apparatus constructed for this purpose. A 1.5 ml 

- 90 microcentrifuge tube was cut and placed over the tail base to prevent the mouse from climbing its tail during 

- 91 testing. Per standard protocols, and to ensure a stable base level of struggling, the first 2 minutes of the TST 

- 92 was not analyzed. The TST for optogenetics experiments was 14 minutes in duration and only one mouse was 

- 93 run at a time. Laser light for optogenetics was delivered in 4x, 3 minute blocks (OFF-ON-OFF-ON) with laser 

- 94 stimulation parameters as per below. The apparatus was thoroughly cleaned between uses. TST videos were 

- 95 analyzed manually on a per minute basis by an experimenter that was blinded to the conditions being tested 

- 96 and using an established method[40] . 

- 97 

- 98 **Open field (OF):** OF testing was conducted in a standard sized arena (40x40cm), with a height of 30cm on 

- 99 each side. Video was collected from above and subsequent analysis was done using Bioviewer software to 

- 00 automatically track mice in the maze. Open field testing was 8 minutes in duration and the mouse was placed 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 01 by hand into the lower right corner of the apparatus. Optogenetic stimulation was delivered in 4x, 2 minute 

- 02 blocks (OFF-ON-OFF-ON) with laser stimulation parameters as per below. Mean velocity in the apparatus, 

- 03 during total light OFF vs. ON epochs was analyzed as a measure of overall activity level. The OF apparatus 

- 04 was cleaned thoroughly between uses. 

- 05 

- 06 **Optogenetic Protocols** : For optogenetic silencing during behavior, light stimulation was delivered via a 

- 07 fiberoptic cable fed through a rotary joint commutator to a bifurcated optogenetic patch cable (Doric Lenses), 

- 08 and attached to a 150 mW, 473 nm DPSS fiber coupled laser (Shanghai Lasercentury). For optogenetic 

- 09 silencing the laser was triggered with commercial software and an external pulse generator (Prizmatix), or 

- 10 triggered manually. Light power was measured at the beginning of each behavior session using a light power 

- 11 meter (Thorlabs), measured as 5mW total light power (2.5 mW/side). Light OFF and ON trials were 

- 12 interspersed pseudorandomly within each set of behavior trials with light delivered with spatiotemporal 

- 13 precision relative to T-maze zones. For some experiments the laser was turned on and off manually based on 

- 14 the location of the mouse in the maze or at specific times during the intertrial-interval (ITI) or in the start box. 

- 15 Mice were maintained in the start box of the maze for 6 seconds before opening the door to initiate a trial. For 

- 16 all optogenetic experiments, mice first ran two forced trials to either arm, followed by 16 choice trials each day 

- 17 (8 light OFF and 8 light ON). We delivered blue laser light to optogenetically silence the bilateral ACC at 

- 18 specific times during the ITI, while the mouse was in the start box of the maze, or during a period extending 

- 19 from start gate through the choice point of the T-maze. Light was delivered during discrete periods designated 

- 20 for optogenetic testing. Mice were run up to 3 consecutive days with a given maze arrangement. There was no 

- 21 apparent change in responsiveness to silencing over the course of the experiments. T-maze experiments 

- 22 ended with 1-3 days in which a second barrier was inserted to equalize effort between conditions. Because 

- 23 control mice typically chose the HR barrier arm on most trials, we did not run them on the 2-barrier condition. 

- 24 The OF and TST were performed as described above to examine effects of optogenetic silencing on overall 

- 25 effort and mobility. 

- 26 

- 27 **Behavior Analyses** : In all cases, the experimenter manually recorded the choice of mice in the T-maze, and 

- 28 these data were cross-checked against recorded videos to verify accuracy, and correct timing of laser 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 29 triggering. These choice data are reflected in plots of %HR choice throughout. In our initial validation dataset, 

- 30 we manually annotated videos to determine the length of each choice trial from the time point just after the 

- 31 start until the point at which the tip of the mouse's nose reached the reward cup in either arm. For subsequent 

- 32 optogenetic experiments, we employed a more detailed, automated analysis of choice trials. This analysis was 

- 33 not done for the validation data due to difficulties with automated tracking of mice in the original version of the 

- 34 maze. For automated analyses we first used DeepLabCut (DLC)[41] to train a neural network to track multiple 

- 35 points on the mouse during choice trials. We used a point centered on the implant as our main tracking point 

- 36 for subsequent analysis of time in zones for mice in distinct parts of the maze. Maze zones were defined in a 

- 37 consistent manner based on standardized markings on the maze itself. The barrier, reward cups and start gate 

- 38 were placed in identical locations for each trial based on specialized slots or marks on the outside of the maze. 

- 39 We used BehaviorDEPOT[42] software and custom MATLAB code to define the choice made on each trial and to 

- 40 divide the maze into zones for further analysis. We calculated time in each zone and parsed these based on 

- 41 choice (HR vs. LR) and laser status (light OFF vs. ON). The microstructure of choice trajectories was analyzed 

- 42 manually from behavior videos on a frame-by-frame basis with a pause defined as >2 frames in which mice did 43 not progress towards goal. 

- 44 

- 45 **Statistics:** Unless otherwise specified, nonparametric tests or ANOVA was used to assess significance. 

- 46 Statistics were calculated using custom MATLAB code or Graphpad Prism. All statistical parameters, including 

- 47 test statistics, correction for multiple comparisons, and sampling of repeated measurements are stated in the 

- 48 main figure legends. Error bars represent ±SEM. The code and data used to generate and support the findings 

- 49 of this study are available from the corresponding author upon reasonable request. 

- 50 

- 51 **RESULTS:** 

- 52 **Behavioral Validation** 

- 53 Most studies exploring the role of the ACC in spatial, effort-based choice tasks used rats. To investigate the 

- 54 role of the ACC in mouse models, we designed and validated a barrier T-maze training and testing procedure 

- 55 for use in mice (see methods). We built a custom, scaled down version of a standard rat T-maze, with 

- 56 manually removable guillotine style doors, wire mesh barriers of different sizes and transparent food cups to 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 57 hold reward pellets ( **Fig. 1A and B** ). Mice were food deprived, habituated to human handling and behavior was 

- 58 shaped such that mice sought food in the reward wells. Next, animals were trained using 3 reward pellets in a 

- 59 high reward (HR) arm and one pellet in the low reward (LR) arm ( **Fig. 1A** ). Mice were trained to a threshold of 

- 60 >70% HR choices, first without a barrier and then sequentially with 5 and 10 cm wire mesh barriers before 

- 61 initiating experimental testing procedures ( **Fig. 1C** ). Mice initially ran 1 forced trial to each arm, followed by 16 62 choice trials during training and testing. 

- 63 

- 64 To validate that the behavior of mice in our T-maze assay was sensitive to manipulations of reward differential 

- 65 between HR vs. LR arms or effort cost (barrier), we performed an initial validation experiment in wildtype mice 

- 66 ( **Fig. 2** ). Following training, we systematically changed the number of HR reward pellets and/or the effort 

- 67 associated with HR vs. LR arms of the maze and recorded the resulting pattern of choices ( **Fig. 2A and B** ). 

- 68 For consistency, we have used 'HR' to indicate the original high effort, high reward arm of the maze throughout 

- 69 ( **Fig. 2B** ). Mice initially chose the high effort, high reward arm ~50% of the time, gradually approaching ~80% 

- 70 HR choices ( **Fig. 2B** ). Reducing the reward differential (from 3:1 to 2:1 to 1:1) resulted in mice making fewer 

- 71 HR choices, particularly after changing to a 1:1 reward ratio (no differential) such that there was no additional 

- 72 utility associated with climbing the barrier ( **Fig. 2B** ). HR choices increased slightly after reinstating a 2:1 reward 

- 73 differential, though remained lower than during the initial 2:1 stage ( **Fig. 2B** ). These data indicate that mice 

- 74 adjust their willingness to exert effort in proportion to the magnitude of associated reward ( **Fig. 2B** ). The lower 

- 75 proportion of HR choices after reinstating a reward differential suggests that choices are partially influenced by 

- 76 recent history of reward across recent days. Finally, in order to determine whether mice are sensitive to 

- 77 changes in the amount of effort, independent of reward differential, we inserted a second 10 cm barrier in the 

- 78 LR arm of the maze. When effort cost was equivalent, mice rapidly adjusted their strategy to choose the more 

- 79 highly rewarded arm on nearly every trial ( **Fig. 2B** ). Thus, mice in our assay actively organize their behavior to 

- 80 optimize the utility of choices based on effort-reward tradeoffs. Learning of new contingencies could be 

- 81 observed within-session, but also appear to consolidate across days ( **Fig. 2C** ). 

- 82 

- 83 The time required for decision making is a relevant variable that may reflect differential engagement of distinct 

- 84 systems for action selection[43,44] . We hypothesized that if mice are making deliberative, goal-directed choices 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 85 then this would be reflected in the timing of choice trials. Thus, we calculated trial length using overhead videos 

- 86 collected during EBD ( **Fig. 2D** ). At the start of 10 cm barrier training mice were significantly slower to complete 

- 87 high effort, HR trials compared to LR trials ( **Fig. 2E** ). However, at the end of training when mice approach 

- 88 asymptotic performance there was no difference in time required to complete trials regardless of choice type 

- 89 ( **Fig. 2E** ). Importantly, this indicates that the additional time cost incurred by climbing the barrier is minimal 

- 90 once mice are well trained on the task. This underscore the value of this assay for disambiguating effort from 

- 91 time-related costs which is a known issue with operant effort-based decision making tasks that require lever 

- 92 pressing[45] . Subsequent changes in reward differential had minimal impact on trial length, though a slight 

- 93 difference between HR and LR trial lengths did emerge when contingencies had recently changed ( **Fig. 2F** 

- 94 **and G** ). This may reflect an increase in cognitive effort or deliberative processing required to overcome an 

- 95 effort cost when outcomes are dynamic or uncertain. Finally, making effort equivalent by adding a second 

- 96 barrier resulted in a significant increase in LR choice time ( **Fig. 2G** ). Overall, these data demonstrate that mice 

- 97 pursue goal-directed choice strategies in our assay that are highly sensitive to relative reward magnitude and 

- 98 effort cost. Thus, this approach is a valid strategy for studying the neural basis of EBD in mouse models. 

- 99 

- 00 **Optogenetic silencing of the ACC disrupts effort-based decision making** 

- 01 To investigate the spatiotemporal requirement for ACC activity during EBD we expressed an inhibitory opsin 

- 02 (AAV-CKII-stGtACR2) in bilateral ACC  and silenced excitatory neurons by delivering blue light via implanted 

- 03 cannulae ( **Fig. 3A-C** ). This approach consistently targeted a relatively restricted region of dorsal, anterior ACC 

- 04 (Cg1; **Fig. 3E** ). We hypothesized that neural activity in this region would be required during the process of 

- 05 making effort-related choices on a trial-by-trial basis. To test this hypothesis, we trained mice as previously 

- 06 described and tested the effects of optogenetic silencing during discrete phases of our training and testing 

- 07 protocol ( **Fig. 3D** ). Following T-maze behavior, we tested the effects of our manipulation on overall mobility in 

- 08 an open field (OF) and in a more generalized test of effortful behavior using the tail suspension test (TST) ( **Fig.** 

- 09 **3D** ). During T-maze testing, we made within-subject comparisons for light OFF vs. light ON trials that were 

- 10 pseudorandomly interleaved during each testing day ( **Fig. 3F** ). 

- 11 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 12 To test the acute necessity of ACC activity for EBD, we first examined the requirement for neural activity at 

- 13 discrete times during the trial cycle in our behavior. Mice were placed into the start box of the maze for 6 

- 14 seconds before lifting the start gate to initiate a trial, with an ~60 second intertrial interval (ITI) ( **Fig. 4A** ). Light 

- 15 was delivered to silence the ACC during discrete phases of this cycle, and we compared the %HR choices for 

- 16 light OFF vs light ON trials. Light delivered during the trial itself was spatially restricted to cover the stem and 

- 17 choice point regions of the T-maze such that mice would need to commit to a choice while the ACC was 

- 18 silenced ( **Fig. 4B** ). We initially silenced the ACC from the end of the ITI through the choice point of the maze 

- 19 and observed a robust reduction in high effort, HR choices for light ON vs. OFF trials ( **Fig. 4C** ). We observed a 

- 20 similar reduction in HR choices when light was delivered during the ITI and in the start box, but not during the 

- 21 trial itself ( **Fig. 4D** ). However, there was no effect of silencing the ACC on %HR choices when light ON was 

- 22 limited to the home cage ITI ( **Fig. 4E** ). Notably, the largest effects were observed when ACC was silenced only 

- 23 during the choice part of the trial itself (between lifting the start gate and committing to a choice) ( **Fig. 4F** ). 

- 24 There was no effect in mCherry-expressing, laser only mice for any of the conditions ( **Fig. 4C-F** ). These data 

- 25 demonstrate that the activity of ACC excitatory neurons is required on a trial-by-trial basis for mice to choose to 

- 26 exert greater effort for a larger reward, when a less effortful, lower reward alternative is available. Moreover, 

- 27 this activity is most critical during periods of time when mice are preparing for, evaluating and ultimately 

- 28 selecting an effortful action. The requirement for activity in the start box was somewhat surprising. Although we 

- 29 cannot rule out that this reflects some delay in re-establishing meaningful, task-related ACC representations 

- 30 after an extended period of silencing, this finding suggests that ACC activity may be important during a choice- 

- 31 planning phase immediately preceding the trial. 

- 32 

- 33 To better interpret these results, we equalized effort by adding a second barrier to the LR arm and continued to 

- 34 run trials with silencing during the trial itself ( **Fig. 4G** ). While mice initially persisted in choosing the LR arm 

- 35 when the ACC was silenced, they did adjust their behavior to select the more highly rewarded arm for both 

- 36 light OFF and ON trials ( **Fig. 4H** ). This suggests that absolute deficits in spatial recall, ability to enact an 

- 37 effortful response or motivation/preference for larger rewards cannot explain our results. The initial persistence 

- 38 in choosing the formerly low effort, LR arm is reminiscent of effects seen in ACC lesioned rats[7,28] . Because our 

- 39 manipulation is limited to the pre-choice period and light OFF trials are interspersed, it seems unlikely this 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 40 reflects impaired updating of task models. However, ACC activity may be required to initially translate updated 

- 41 models into action selection. 

- 42 

- 43 To better understand the effects of silencing ACC on T-maze decision making we also conducted a separate 

- 44 experiment in which silencing was delivered in 3-day blocks during trials themselves ( **Fig. 5A and B** ). This 

- 45 design is more similar to how barrier T-maze experiments have typically been conducted, allowing better 

- 46 comparison with pharmacology or lesion studies. In this experiment, we initially silenced the ACC during three 

- 47 consecutive days in the no barrier training condition ( **Fig. 5C** ). There was minimal impact of silencing the ACC 

- 48 during choice trials that occurred before a barrier was introduced, although mice were slightly more likely to 

- 49 choose the LR arm when the light was ON ( **Fig. 5C** ). Like our other data, silencing ACC resulted in a large and 

- 50 highly significant disruption in high-effort choices after a barrier was introduced and this was stable over at 

- 51 least several days ( **Fig. 5D** ). When a second barrier was added to the maze, we again saw that silencing ACC 

- 52 continued to bias mice towards LR choices, but this effect was limited to the first day of the 2-barrier block ( **Fig.** 

- 53 **5E** ). There was no effect of light alone in a similar 3-day block in mCherry expressing control mice indicating 

- 54 observed results are not due to effects of laser by itself ( **Fig. 5F** ). Taken together, these data support our 

- 55 conclusion that ACC activity is stably required during the evaluation and selection of actions which will incur an 

- 56 effort cost. 

- 57 

- 58 **Silencing ACC disrupts choice trajectory during decision making** 

- 59 Our validation analyses revealed that choice trial duration is sensitive to changes in effort-reward tradeoffs 

- 60 ( **Fig. 2** ). Therefore, we predicted that a more detailed evaluation of choice behavior might reveal a more 

- 61 nuanced understanding of the role of ACC in EBD. A critical advantage of our assay, over operant tasks, is that 

- 62 task events are spatially and temporally segregated[45] . For example, evaluation of effort-reward tradeoffs and 

- 63 action selection occur prior to effort itself (climbing the barrier). A commonly employed alternative involves 

- 64 lever pressing in an operant chamber where mice must decide when to stop pressing a lever for a preferred 

- 65 reward over pursuing a less desired alternative. We hypothesized that the effects of silencing ACC activity on 

- 66 T-maze decision making would impact the time it takes mice to make choices in our maze and that these 

- 67 effects might be distinct for different zones within the maze. We used DeepLabCut[41] to train a neural network 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 68 for precise key point tracking of mice in our assay and custom software to analyze these data ( **Fig. 6A** ). Our 

- 69 lab recently developed BehaviorDEPOT, an open-source, flexible software package that allows customizable 

- 70 behavior analysis approaches based on machine-learning based tracking[42] . 

- 71 

- 72 We developed custom BehaviorDEPOT automated algorithms to process key point tracking data to segregate 

- 73 choice trials based on position as mice traverse zones sequentially during a choice. The specific sequence 

- 74 further defines whether the individual trials correspond to HR or LR choices, and we have validated 

- 75 performance of this process by comparison with manual annotations ( **Fig. 6A** ). We then assign the identity of 

- 76 trials as light OFF vs. light ON and automatically collect trial statistics segregated by zone and trial identity 

- 77 (light OFF/ON, HR/LR) ( **Fig. 6A** ). We processed and analyzed videos this way for testing days in which ACC 

- 78 was silenced during choice trials only (corresponding with 'approach' and 'choice' zones) ( **Fig. 6B-D** ). In this 

- 79 way, we can plot and analyze choice trajectories in the maze for light OFF vs. light ON conditions ( **Fig. 6E-F** 

- 80 We analyzed the time mice spent in the approach and choice zones of the maze segregated by light condition 81 (OFF vs. ON) for all choices together and separated by choice type. When choice types were grouped, there 

- 82 was a highly significant increase in approach zone time for light ON vs. OFF trials, but not for the choice zone 83 ( **Fig. 6G** ). 

- 84 

- 85 When we examined HR choices by themselves, time in approach and choice zones was significantly greater 

- 86 for the light ON condition, but we found no significant effects for LR choices ( **Fig. 6H-I** ). These data indicate 

- 87 that mice are slower to approach the maze choice point when ACC is silenced, particularly if they ultimately 

- 88 make a high effort choice. We next wondered what accounted for the increase time in the approach zone, 

- 89 which led us to examine choice trajectories in greater detail. We noticed that light ON trajectories were less 

- 90 smooth and that this was due to changes in the microstructure of ballistic movements ( **Fig. 6J** ). Specifically, 

- 91 mice exhibited brief micropauses that chunked movements into discrete segments when ACC was silenced 

- 92 ( **Fig. 6K** ). Video analyses revealed that micropauses were common in the approach zone when ACC was 

- 93 silenced, but almost never occurred during light OFF trials ( **Fig. 6L** ). In contrast, choice zone pauses were 

- 94 common for both conditions ( **Fig. 6L** ). When dividing by choice type, this difference was only significant for 

- 95 high effort choices ( **Fig. 6M** ). This indicates that approach zone micropauses occur on trials in which mice 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 96 make a high effort choice despite silencing of ACC activity. There was no difference in micropause duration for 

- 97 any condition ( **Fig. 6N-O** ). Taken together, these results suggest that silencing ACC has the greatest effects 

- 98 on behavior in the approach zone, when mice may be evaluating or planning their choice. Thus, ACC may be 

- 99 required to support the efficiency or continuity of effortful action selection processes. 

- 00 

- 01 **Silencing ACC does not disrupt movement or effortful responses outside a decision-making context** 

- 02 Our results indicate that ACC activity is required for choosing to exert greater effort for a larger reward when a 

- 03 less effortful, lower reward alternative exists. We therefore wondered if silencing ACC would have more 

- 04 generalized effects on willingness or ability of mice to exert effort during behavior that is not explicitly reward- 

- 05 based or goal-directed. To investigate this, we examined the effects of silencing ACC during a tail suspension 

- 06 test (TST). The TST is a widely employed test for depression-related behavior in which mice are exposed to an 

- 07 inescapable acute stressor (tail suspension). Mice confronted with tail suspension stress either engage in 

- 08 bouts of effortful escape-related behavior or adopt an energy conserving immobile posture. While immobility 

- 09 has generally been taken as a measure of 'behavioral despair' – a purportedly depression-like response – a 

- 10 more conservative interpretation is that both immobility and struggling can be considered potentially adaptive 

- 11 responses. In this case, we are not making any claims about relevance to depression and only using the assay 

- 12 as a measure of tendency to exert effort. Silencing neural activity in ACC during the TST did not reduce 

- 13 effortful struggling behavior ( **Fig. 7A-B** ). This suggests that silencing the ACC does not cause generalized 

- 14 reductions in effort outside the context of goal-directed decision making. 

- 15 

- 16 Our data also indicate that silencing ACC disrupts motoric aspects of behavior as mice approach a maze 

- 17 choice point. We therefore wondered whether this reflects generalized deficits in mobility, or is specific to 

- 18 situations that involve explicit decision making. To test this, we observed the effects of silencing the ACC when 

- 19 mice are exploring an open field (OF). We found that there is no difference in the average velocity of mice 

- 20 during light OFF vs. ON epochs for either stGtACR2 expressing mice or mCherry controls ( **Fig. 7C** ). This 

- 21 suggests that the observed disruptions in choice trajectory are specific to decision making, supporting the 

- 22 conclusion that they represent disturbances in goal-directed cognition. 

- 23 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 24 **DISCUSSION:** 

- 25 Here we report on the development and validation of a mouse version of the barrier T-maze assay. Mice 

- 26 rapidly modify their choices based on effort-reward tradeoffs and barrier climbing incurs a minimal time cost. 

- 27 Briefly silencing ACC excitatory neurons during action selection, or when mice are waiting to start a trial, 

- 28 rapidly and reversibly disrupts preference to exert greater effort for a larger reward. Instead, mice express a 

- 29 preference for a low effort, low reward alternative. This effect was absent when there was no effort cost, and 

- 30 reversed when effort cost was equalized, indicating that our results are not due to impairment in recall, 

- 31 capacity to perform the effortful action or preference for larger rewards. Silencing ACC also disrupts choice 

- 32 trajectory, causing mice to take longer to approach the maze choice point and select an action. This is at least 

- 33 in part due to changes in the microstructure of ballistic movements towards the choice point. Silencing ACC 

- 34 disrupts the typically continuous trajectory to the choice point, introducing frequent micropauses into the 

- 35 approach trajectory. In contrast, effortful behavior and overall movement were not impaired outside a goal- 

- 36 directed context. These findings indicate a role for ACC excitatory neurons in the evaluation and selection of 

- 37 effortful actions and online control of goal-directed action sequences. 

- 38 

- 39 The prefrontal cortex is postulated to exhibit a modular organization, but the role of ACC is extensively 

- 40 debated[46] . Prominent theories posit primary roles in resolving conflict, computing the value of effortful cognitive 

- 41 control over task performance and comparing the value of alternative actions in a decision oriented 

- 42 context[16,47,48] . Our data are consistent with prior lesion studies done in rats making effort-based choices[7,8,13,28] . 

- 43 However, we extend this work to define a role for ACC in computations that occur before and/or during effortful 

- 44 action selection. ACC neurons can dynamically encode potential actions with multiplexed representation of 

- 45 value, cost, and reward probability[49–52] . In rats, ACC activity in both single units and at the population level 

- 46 encode choice value that integrates reward magnitude and effort cost[11,14,15,36] . We find that silencing ACC 

- 47 during a choice, or when preparing for choice trials in the start box, disrupts effortful action selection. This may 

- 48 occur because ACC is required for the action-value associations which are necessary for making 

- 49 advantageous choices. Notably, this does not simply result in chance levels of performance, but instead biases 

- 50 mice towards low effort choices. This is consistent with computational models which propose that top-down 

- 51 ACC control is necessary to override effort-averse action selection systems in the striatum[53] . 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 52 

- 53 In addition to changing choice preference, mice also exhibit changes in choice trajectory on trials where ACC 

- 54 was silenced. Beyond assigning effort-related value to actions, successful EBD requires monitoring and 

- 55 controlling action sequences required to reach the desired goal. Several studies find ACC population activity is 

- 56 involved in tracking or maintaining progress through a sequence of goal-directed actions[17,54,55] . If silencing 

- 57 ACC disrupts monitoring of progress towards a goal, then mice might need to pause and reorient frequently. 

- 58 The ACC is also intimately linked with motor output structures in the brain. ACC damage in patients can result 

- 59 in akinetic mutism, an absence of willed motor actions, and stimulation prompts reports of enhanced will to 

- 60 persevere through a challenge[56,57] . ACC neurons are particularly responsive to the organization or execution of 

- 61 goal-directed action sequences[58–62] . Thus, in addition to tracking progress, ACC may exert online control over 

- 62 the initiation and maintenance of goal-directed motor output responsible for lower level action sequences. Our 

- 63 results suggest a role for ACC in trial preparation, and as mice approach the choice zone and select an action. 

- 64 However, it is likely that ACC is important throughout a trial. One study found that ACC lesioned rats initially 

- 65 turned towards the barrier on the first few trials after a lesion, but failed to climb the barrier[29] . They suggest that 66 ACC is important for maintaining effort while carrying an action sequence to completion. For the most part, we 

- 67 have not seen this type of behavior and mice typically turn directly to the low effort arm on trials where ACC 

- 68 was silenced. This is consistent with a role in processes occurring prior to action selection, though does not 

- 69 rule out important functions of ACC in carrying out effort or interpreting outcome. 

- 70 

- 71 Distinct cortical output pathways may segregate specific functions[19,63–65] . Our study expressed an inhibitory 

- 72 opsin driven by a promoter with some specificity for excitatory neurons (CaMKII), so our results may be driven 

- 73 by excitatory rather than inhibitory ACC neurons. A similar study using chemogenetics found that either 

- 74 activating or inhibiting ACC excitatory neurons disrupts effortful choices[32] . This suggests that increasing overall 

- 75 activity, if not timed precisely or coordinated appropriately amongst excitatory neurons, can also disrupt 

- 76 effortful choices. ACC projection neurons densely innervate dorsal striatum and mediodorsal thalamus[66] , but 

- 77 also target a number of other cortical and subcortical structures implicated in motivated behavior[67] . Lesions 

- 78 that disconnect ACC from basolateral amygdala or ventral striatum disrupt effortful choices in the barrier T- 

- 79 maze[9,68] and other ACC targets including the habenula and anterior insula are also implicated in spatial EBD[69–] 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 80 71. Moreover, dopaminergic input to both ventral striatum and ACC are important for EBD26,27,72–76. These data 

- 81 begin to define circuits interconnecting these regions that form distributed neural networks mediating EBD[45,77] . 

- 82 Future studies should investigate these cell-type specific circuits, by targeting genetically encoded opsins 

- 83 and/or calcium indicators. A deeper understanding of these ACC circuits will shed light on relevant 

- 84 neuropsychiatric disorders and their effective treatment. 

- 85 

- 86 

- 87 

- 88 

- 89 

- 90 

- 91 

- 92 

- 93 

- 94 

- 95 

- 96 

- 97 

- 98 

- 99 

00 

- 01 

02 

- 03 

- 04 

05 

06 

07 08 09 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

10 **REFERENCES:** 

- 11 **1** . Green, M. F.; Horan, W. P.; Barch, D. M.; Gold, J. M. Effort-Based Decision Making: A Novel Approach 12 for Assessing Motivation in Schizophrenia. _Schizophrenia bulletin_ **41** , 1035–1044 (2015). 13 [PMID:26089350] 

- 14 **2** . Gold, J. M.; Waltz, J. A.; Frank, M. J. Effort cost computation in schizophrenia: a commentary on the 15 recent literature. _Biological psychiatry_ **78** , 747–753 (2015). [PMID:26049208] 

- 15 16 **3** . 

16 **3** . Barch, D. M.; Pagliaccio, D.; Luking, K. In _Current Topics in Behavioral Neurosciences_ ; Springer, Cham, 17 2016; Vol. 27, pp 411–449 18 **4** . 

18 **4** . Culbreth, A. J.; Moran, E. K.; Barch, D. M. Effort-cost decision-making in psychosis and depression: 19 could a similar behavioral deficit arise from disparate psychological and neural mechanisms? 20 _Psychological medicine_ **48** , 889–904 (2018). [PMID:28889803] 21 **5** . Stuppy-Sullivan, A. M.; Buckholtz, J. W.; Baskin-Sommers, A. Aberrant Cost–Benefit Integration During 22 Effort-Based Decision Making Relates to Severity of Substance Use Disorders: 23 _https://doi.org/10.1177/2167702619868155_ **8** , 155–168 (2019). 24 **6** . Horne, S. J.; Topp, T. E.; Quigley, L. Depression and the willingness to expend cognitive and physical 25 effort for rewards: A systematic review. _Clinical psychology review_ **88** , (2021). [PMID:34274800] 26 **7** . Walton, M. E.; Bannerman, D. M.; Alterescu, K.; Rushworth, M. F. S. Functional specialization within 27 medial frontal cortex of the anterior cingulate for evaluating effort-related decisions. _The Journal of_ 28 _neuroscience : the official journal of the Society for Neuroscience_ **23** , 6475–6479 (2003). 29 [PMID:12878688] 30 **8** . Rudebeck, P. H.; Walton, M. E.; Smyth, A. N.; Bannerman, D. M.; Rushworth, M. F. S. Separate neural 31 pathways process different decision costs. _Nature Neuroscience_ (2006). 32 **9** . Floresco, S. B.; Ghods-Sharifi, S. Amygdala-prefrontal cortical circuitry regulates effort-based decision 33 making. _Cerebral cortex (New York, N.Y. : 1991)_ **17** , 251–260 (2007). [PMID:16495432] 34 **10** . Hauber, W.; Sommer, S. Prefrontostriatal circuitry regulates effort-related decision making. _Cerebral_ 35 _Cortex_ **19** , 2240–2247 (2009). 

36 **11** . Cowen, S. L.; Davis, G. A.; Nitz, D. A. Anterior cingulate neurons in the rat map anticipated effort and 37 reward to their associated action sequences. _Journal of neurophysiology_ **107** , 2393–2407 (2012). 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

38 [PMID:22323629] 

39 **12** . Walton, M. E.; Kennerley, S. W.; Bannerman, D. M.; Phillips, P. E. M.; Rushworth, M. F. S. Weighing up 40 the benefits of work: behavioral and neural analyses of effort-related decision making. _Neural networks :_ 41 _the official journal of the International Neural Network Society_ **19** , 1302–1314 (2006). [PMID:16949252] 

42 **13** . Schweimer, J.; Hauber, W. Involvement of the rat anterior cingulate cortex in control of instrumental 43 responses guided by reward expectancy. _Learning & memory (Cold Spring Harbor, N.Y.)_ **12** , 334–342 44 (2005). [PMID:15930509] 

45 **14** . Hillman, K. L.; Bilkey, D. K. Neural encoding of competitive effort in the anterior cingulate cortex. _Nature_ 46 _neuroscience_ **15** , 1290–1297 (2012). [PMID:22885851] 

47 **15** . Hillman, K. L.; Bilkey, D. K. Neurons in the rat anterior cingulate cortex dynamically encode cost-benefit 48 in a spatial decision-making task. _The Journal of neuroscience : the official journal of the Society for_ 49 _Neuroscience_ **30** , 7705–7713 (2010). [PMID:20519545] 

50 **16** . 

51 

52 

Kolling, N.; Wittmann, M. K.; Behrens, T. E. J.; Boorman, E. D.; Mars, R. B.; Rushworth, M. F. S. Value, search, persistence and model updating in anterior cingulate cortex. _Nature neuroscience_ **19** , 1280– 1285 (2016). [PMID:27669988] 

53 **17** . 

54 

55 

Lapish, C. C.; Durstewitz, D.; Chandler, L. J.; Seamans, J. K. Successful choice behavior is associated with distinct and coherent network states in anterior cingulate cortex. _Proceedings of the National Academy of Sciences of the United States of America_ **105** , 11963–11968 (2008). [PMID:18708525] 

56 **18** . 

57 

58 

Akam, T.; Rodrigues-Vaz, I.; Marcelo, I.; Zhang, X.; Pereira, M.; Oliveira, R. F.; Dayan, P.; Costa, R. M. The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection. _Neuron_ **109** , 149-163.e7 (2021). [PMID:33152266] 

59 **19** . 

60 

61 

Tervo, D. G. R.; Kuleshova, E.; Manakov, M.; Proskurin, M.; Karlsson, M.; Lustig, A.; Behnam, R.; Karpova, A. Y. The anterior cingulate cortex directs exploration of alternative strategies. _Neuron_ **109** , 1876-1887.e6 (2021). [PMID:33852896] 

62 **20** . Bernacchia, A.; Seo, H.; Lee, D.; Wang, X. J. A reservoir of time constants for memory traces in cortical 63 neurons. _Nature neuroscience_ **14** , 366–372 (2011). [PMID:21317906] 

64 **21** . Kennerley, S. W.; Behrens, T. E. J.; Wallis, J. D. Double dissociation of value computations in 

65 

orbitofrontal and anterior cingulate neurons. _Nature neuroscience_ **14** , 1581–1589 (2011). 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

66 [PMID:22037498] 

67 **22** . Hyman, J. M.; Holroyd, C. B.; Seamans, J. K. A Novel Neural Prediction Error Found in Anterior 68 Cingulate Cortex Ensembles. _Neuron_ **95** , 447-456.e3 (2017). [PMID:28689983] 69 **23** . Heilbronner, S. R.; Hayden, B. Y. Dorsal Anterior Cingulate Cortex: A Bottom-Up View. _Annual review of_ 70 _neuroscience_ **39** , 149–170 (2016). [PMID:27090954] 71 **24** . Holroyd, C. B.; Coles, M. G. H. The neural basis of human error processing: reinforcement learning, 72 dopamine, and the error-related negativity. _Psychological review_ **109** , 679–709 (2002). 73 [PMID:12374324] 74 **25** . Rushworth, M. F. S.; Behrens, T. E. J. Choice, uncertainty and value in prefrontal and cingulate cortex. 75 _Nature neuroscience_ **11** , 389–397 (2008). [PMID:18368045] 

76 **26** . Salamone, J. D.; Cousins, M. S.; Bucher, S. Anhedonia or anergia? Effects of haloperidol and nucleus 77 accumbens dopamine depletion on instrumental response selection in a T-maze cost/benefit procedure. 78 _Behavioural Brain Research_ **65** , 221–229 (1994). [PMID:7718155] 79 **27** . Cousins, M. S.; Atherton, A.; Turner, L.; Salamone, J. D. Nucleus accumbens dopamine depletions alter 80 relative response allocation in a T-maze cost/benefit task. _Behavioural brain research_ **74** , 189–197 81 (1996). [PMID:8851929] 82 **28** . Walton, M. E.; Bannerman, D. M.; Rushworth, M. F. S. The role of rat medial frontal cortex in effort83 based decision making. _The Journal of neuroscience : the official journal of the Society for Neuroscience_ 84 **22** , 10996–11003 (2002). [PMID:12486195] 85 **29** . Holec, V.; Pirot, H. L.; Euston, D. R. Not all effort is equal: The role of the anterior cingulate cortex in 86 different forms of effort-reward decisions. _Frontiers in Behavioral Neuroscience_ **8** , 12 (2014). 87 **30** . Solinsky, C.; Kirby, B. P. Medial prefrontal cortex lesions in mice do not impair effort-based decision 88 making. _Neuropharmacology_ **65** , 223–231 (2013). [PMID:23092919] 89 **31** . Hart, E. E.; Gerson, J. O.; Zoken, Y.; Garcia, M.; Izquierdo, A. Anterior cingulate cortex supports effort 90 allocation towards a qualitatively preferred option. _The European journal of neuroscience_ **46** , 1682–1688 91 (2017). [PMID:28543944] 92 **32** . Hart, E. E.; Blair, G. J.; O’Dell, T. J.; Blair, H. T.; Izquierdo, A. Chemogenetic Modulation and Single93 Photon Calcium Imaging in Anterior Cingulate Cortex Reveal a Mechanism for Effort-Based Decisions. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

94 _The Journal of neuroscience : the official journal of the Society for Neuroscience_ **40** , 5628–5643 (2020). 95 [PMID:32527984] 

96 **33** . Walton, M. E.; Groves, J.; Jennings, K. A.; Croxson, P. L.; Sharp, T.; Rushworth, M. F. S.; Bannerman, 97 D. M. Comparing the role of the anterior cingulate cortex and 6-hydroxydopamine nucleus accumbens 98 lesions on operant effort-based decision making. _The European journal of neuroscience_ **29** , 1678–1691 99 (2009). [PMID:19385990] 

00 **34** . KL, H.; DK, B. Neurons in the rat anterior cingulate cortex dynamically encode cost-benefit in a spatial 01 decision-making task. _The Journal of neuroscience : the official journal of the Society for Neuroscience_ 02 **30** , 7705–7713 (2010). [PMID:20519545] 

03 **35** . Porter, B. S.; Hillman, K. L.; Bilkey, D. K. Anterior cingulate cortex encoding of effortful behavior. _Journal_ 04 _of neurophysiology_ **121** , 701–714 (2019). [PMID:30625016] 

05 **36** . Porter, B. S.; Hillman, K. L. Dorsomedial prefrontal neural ensembles reflect changes in task utility that 06 culminate in task quitting. _Journal of neurophysiology_ **126** , 313–329 (2021). [PMID:34133233] 

07 **37** . Elston, T. W.; Kalhan, S.; Bilkey, D. K. Conflict and adaptation signals in the anterior cingulate cortex 08 and ventral tegmental area. _Scientific reports_ **8** , (2018). [PMID:30082775] 

09 **38** . Elston, T. W.; Bilkey, D. K. Anterior Cingulate Cortex Modulation of the Ventral Tegmental Area in an 10 Effort Task. _Cell reports_ **19** , 2220–2230 (2017). [PMID:28614710] 

11 **39** . Elston, T. W.; Croy, E.; Bilkey, D. K. Communication between the Anterior Cingulate Cortex and Ventral 12 Tegmental Area during a Cost-Benefit Reversal Task. _Cell reports_ **26** , 2353-2361.e3 (2019). 13 [PMID:30811986] 

14 **40** . Can, A.; Dao, D. T.; Terrillion, C. E.; Piantadosi, S. C.; Bhat, S.; Gould, T. D. The tail suspension test. 15 _Journal of Visualized Experiments_ No. 58 e3769 (2011). [PMID:22315011] 

16 **41** . Mathis, A.; Mamidanna, P.; Cury, K. M.; Abe, T.; Murthy, V. N.; Mathis, M. W.; Bethge, M. DeepLabCut: 17 markerless pose estimation of user-defined body parts with deep learning. _Nature Neuroscience 2018_ 18 _21:9_ **21** , 1281–1289 (2018). [PMID:30127430] 19 **42** . Gabriel, C. J.; Zeidler, Z.; Jin, B.; Guo, C.; Goodpaster, C. M.; Kashay, A. Q.; Wu, A.; Delaney, M.; 20 Cheung, J.; DiFazio, L. E.; Sharpe, M. J.; Aharoni, D.; Wilke, S. A.; DeNardo, L. A. BehaviorDEPOT is a 21 simple, flexible tool for automated behavioral detection based on markerless pose tracking. _eLife_ **11** , 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

22 (2022). [PMID:35997072] 

23 **43** . Redish, A. D. Vicarious trial and error. _Nature reviews. Neuroscience_ **17** , 147–159 (2016). 24 [PMID:26891625] 

25 **44** . McLaughlin, A. E.; Diehl, G. W.; Redish, A. D. Potential roles of the rodent medial prefrontal cortex in 26 conflict resolution between multiple decision-making systems. _International review of neurobiology_ **158** , 27 249–281 (2021). [PMID:33785147] 

28 **45** . Bailey, M. R.; Simpson, E. H.; Balsam, P. D. Neural substrates underlying effort, time, and risk-based 29 decision making in motivated behavior. _Neurobiology of Learning and Memory_ **133** , 233–256 (2016). 30 [PMID:27427327] 

31 **46** . Ebitz, R. B.; Hayden, B. Y. Dorsal anterior cingulate: a Rorschach test for cognitive neuroscience. 32 _Nature neuroscience_ **19** , 1278–1279 (2016). [PMID:27669987] 

33 **47** . Botvinick, M.; Nystrom, L. E.; Fissell, K.; Carter, C. S.; Cohen, J. D. Conflict monitoring versus selection34 for-action in anterior cingulate cortex. _Nature_ **402** , 179–181 (1999). [PMID:10647008] 

35 **48** . Shenhav, A.; Cohen, J. D.; Botvinick, M. M. Dorsal anterior cingulate cortex and the value of control. 36 _Nature neuroscience_ **19** , 1286–1291 (2016). [PMID:27669989] 

37 **49** . 

38 

39 

Kennerley, S. W.; Walton, M. E. Decision making and reward in frontal cortex: complementary evidence from neurophysiological and neuropsychological studies. _Behavioral neuroscience_ **125** , 297–317 (2011). [PMID:21534649] 

40 **50** . Wallis, J. D.; Kennerley, S. W. Contrasting reward signals in the orbitofrontal cortex and anterior 41 cingulate cortex. _Annals of the New York Academy of Sciences_ **1239** , 33–42 (2011). [PMID:22145873] 42 **51** . Kennerley, S. W.; Dahmubed, A. F.; Lara, A. H.; Wallis, J. D. Neurons in the frontal lobe encode the 43 value of multiple decision variables. _Journal of cognitive neuroscience_ **21** , 1162–1178 (2009). 44 [PMID:18752411] 

45 **52** . Williams, Z. M.; Bush, G.; Rauch, S. L.; Cosgrove, G. R.; Eskandar, E. N. Human anterior cingulate 46 neurons and the integration of monetary reward with motor responses. _Nature neuroscience_ **7** , 1370– 47 1375 (2004). [PMID:15558064] 

48 **53** . Holroyd, C. B.; McClure, S. M. Hierarchical control over effortful behavior by rodent medial frontal 49 cortex: A computational model. _Psychological review_ **122** , 54–83 (2015). [PMID:25437491] 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

50 **54** . Holroyd, C. B.; Ribas-Fernandes, J. J. F.; Shahnazian, D.; Silvetti, M.; Verguts, T. Human midcingulate 51 cortex encodes distributed representations of task progress. _Proceedings of the National Academy of_ 52 _Sciences of the United States of America_ **115** , 6398–6403 (2018). [PMID:29866834] 

53 **55** . Ma, L.; Hyman, J. M.; Phillips, A. G.; Seamans, J. K. Tracking progress toward a goal in corticostriatal 54 ensembles. _The Journal of neuroscience : the official journal of the Society for Neuroscience_ **34** , 2244– 55 2253 (2014). [PMID:24501363] 56 **56** . Devinsky, O.; Morrell, M. J.; Vogt, B. A. Contributions of anterior cingulate cortex to behaviour. _Brain : a_ 57 _journal of neurology_ **118 ( Pt 1)** , 279–306 (1995). [PMID:7895011] 58 **57** . Parvizi, J.; Rangarajan, V.; Shirer, W. R.; Desai, N.; Greicius, M. D. The will to persevere induced by 59 electrical stimulation of the human cingulate gyrus. _Neuron_ **80** , 1359–1367 (2013). [PMID:24316296] 60 **58** . Cowen, S. L.; McNaughton, B. L. Selective delay activity in the medial prefrontal cortex of the rat: 61 contribution of sensorimotor information and contingency. _Journal of neurophysiology_ **98** , 303–316 62 (2007). [PMID:17507507] 

63 **59** . Fujisawa, S.; Amarasingham, A.; Harrison, M. T.; Buzsáki, G. Behavior-dependent short-term assembly 64 dynamics in the medial prefrontal cortex. _Nature neuroscience_ **11** , 823–833 (2008). [PMID:18516033] 65 **60** . Hayden, B. Y.; Pearson, J. M.; Platt, M. L. Neuronal basis of sequential foraging decisions in a patchy 66 environment. _Nature neuroscience_ **14** , 933–939 (2011). [PMID:21642973] 

67 **61** . 68 69 70 **62** . 71 72 **63** . 73 

Mulder, A. B.; Nordquist, R. E.; Örgüt, O.; Pennartz, C. M. A. Learning-related changes in response patterns of prefrontal neurons during instrumental conditioning. _Behavioural Brain Research_ **146** , 77–88 (2003). [PMID:14643461] 

Procyk, E.; Tanaka, Y. L.; Joseph, J. P. Anterior cingulate activity during routine and non-routine sequential behaviors in macaques. _Nature neuroscience_ **3** , 502–508 (2000). [PMID:10769392] Hirokawa, J.; Vaughan, A.; Masset, P.; Ott, T.; Kepecs, A. Frontal cortex neuron types categorically encode single decision variables. _Nature_ **576** , 446–451 (2019). [PMID:31801999] 

74 **64** . Li, B.; Nguyen, T. P.; Ma, C.; Dan, Y. Inhibition of impulsive action by projection-defined prefrontal 75 pyramidal neurons. _Proceedings of the National Academy of Sciences of the United States of America_ 76 **117** , 17278–17287 (2020). [PMID:32631999] 

77 **65** . Vavladeli, A.; Daigle, T.; Zeng, H.; Crochet, S.; Petersen, C. C. H. Projection-specific Activity of Layer 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

78 2/3 Neurons Imaged in Mouse Primary Somatosensory Barrel Cortex During a Whisker Detection Task. 79 _Function (Oxford, England)_ **1** , (2020). [PMID:35330741] 

80 **66** . Vogt, B. A.; Paxinos, G. Cytoarchitecture of mouse and rat cingulate cortex with human homologies. 81 _Brain structure & function_ **219** , 185–192 (2014). [PMID:23229151] 

82 **67** . Gabbott, P. L. A.; Warner, T. A.; Jays, P. R. L.; Salway, P.; Busby, S. J. Prefrontal cortex in the rat: 83 projections to subcortical autonomic, motor, and limbic centers. _The Journal of comparative neurology_ 84 **492** , 145–177 (2005). [PMID:16196030] 

84 **492** , 145–177 (2005). [PMID:16196030] 85 **68** . Hauber, W.; Sommer, S. Prefrontostriatal circuitry regulates effort-related decision making. _Cerebral_ 86 _cortex (New York, N.Y. : 1991)_ **19** , 2240–2247 (2009). [PMID:19131436] 

87 **69** . Porter, B. S.; Li, K.; Hillman, K. L. Regional Activity in the Rat Anterior Cingulate Cortex and Insula 88 during Persistence and Quitting in a Physical-Effort Task. _eNeuro_ **7** , 1–13 (2020). [PMID:32859724] 89 **70** . Cabeza, L.; Ramadan, B.; Cramoisy, S.; Houdayer, C.; Haffen, E.; Risold, P. Y.; Fellmann, D.; 90 Peterschmitt, Y. Chronic Distress in Male Mice Impairs Motivation Compromising Both Effort and 91 Reward Processing With Altered Anterior Insular Cortex and Basolateral Amygdala Neural Activation. 92 _Frontiers in behavioral neuroscience_ **15** , (2021). [PMID:34588963] 

93 **71** . Sevigny, J. P.; Bryant, E. N.; Encarnacion, É.; Smith, D. F.; Acosta, R.; Baker, P. M. Lateral Habenula 94 Inactivation Alters Willingness to Exert Physical Effort Using a Maze Task in Rats. _Frontiers in_ 95 _behavioral neuroscience_ **15** , (2021). [PMID:34447300] 96 **72** . Schweimer, J.; Hauber, W. Dopamine D1 receptors in the anterior cingulate cortex regulate effort-based 97 decision making. _Learning and Memory_ **13** , 777–782 (2006). [PMID:17142306] 98 **73** . Salamone, J. D.; Steinpreis, R. E.; McCullough, L. D.; Smith, P.; Grebel, D.; Mahan, K. Haloperidol and 99 nucleus accumbens dopamine depletion suppress lever pressing for food but increase free food 00 consumption in a novel food choice procedure. _Psychopharmacology_ **104** , 515–521 (1991). 01 [PMID:1780422] 

02 **74** . Sokolowski, J. D.; Salamone, J. D. The role of accumbens dopamine in lever pressing and response 03 allocation: effects of 6-OHDA injected into core and dorsomedial shell. _Pharmacology, biochemistry, and_ 04 _behavior_ **59** , 557–566 (1998). [PMID:9512057] 

05 **75** . Salamone, J. D.; Correa, M.; Farrar, A.; Mingote, S. M. Effort-related functions of nucleus accumbens 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 06 dopamine and associated forebrain circuits. _Psychopharmacology_ **191** , 461–482 (2007). 07 [PMID:17225164] 

- 08 **76** . Schweimer, J.; Saft, S.; Hauber, W. Involvement of catecholamine neurotransmission in the rat anterior 09 cingulate in effort-related decision making. _Behavioral neuroscience_ **119** , 1687–1692 (2005). 10 [PMID:16420173] 

- 11 **77** . Floresco, S. B.; St. Onge, J. R.; Ghods-Sharifi, S.; Winstanley, C. A. Cortico-limbic-striatal circuits 12 subserving different forms of cost-benefit decision making. _Cognitive, affective & behavioral_ 

- 13 _neuroscience_ **8** , 375–389 (2008). [PMID:19033236] 

- 14 

- 15 

- 16 

- 17 

- 18 

- 19 

- 20 

- 21 

- 22 

- 23 

24 

25 

26 

27 

28 

- 29 

30 

31 

32 

33 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

34 

35 

36 

37 

38 

## 39 **FIGURES:** 

40 

41 

42 

43 

44 

**==> picture [338 x 232] intentionally omitted <==**

## **Figure 1  Mouse barrier T-maze schematic and training protocol** 

45 **A** ) Barrier T-maze design with 10cm wire mesh barrier, and 3:1 reward differential for high effort, high reward 46 (HR) vs. low effort, low reward (LR) arms. **B** ) Side view of barrier showing 10 cm vertical side with 45 degree 47 slope down to reward cup. **C** ) Overview of general approach for training and testing mice in the assay - Following 48 habituation/shaping, mice are trained to >70% HR choices with no barrier, 5cm barrier and 10cm barriers 49 preceding testing phase. 

50 

51 

- 52 

- 53 

54 

55 

56 57 58 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

70 71 72 73 74 75 

59 

- 60 

**==> picture [427 x 346] intentionally omitted <==**

## **Figure 2 Validation of T-maze training and testing protocol in mice** 

61 **A** ) For validation experiment, resutls are shown for the 3:1 +10cm barrier training portion of the task, followed by 62 manipulations of reward differential or barrier arrangement (Test). **B** ) Outcome of training and testing phase 63 shown as %HR choices. Reward in high effort arm is systematically changed, and a second barrier is added to 64 equalize effort in the final phase. **C** ) Same data as B, but shown with mean %HR on a per trial basis to reveal 65 within session changes. To examine behavior in greater detail, we calculated the time it takes mice to complete 66 HR and LR choices (from start of a trial through reaching reward cup). **D** ) Schematic representation of how trial 67 lengths were calculated for **E-G. E** ) Quantification of trial length for start vs. end of barrier training, 68 [ _FInteraction_ (1,20)=5.84, _P_ =0.025, _FTime_ (1,20)=9.21, _P_ =0.007, _FChoice_ (1,20)=8.58, _P_ =0.008], 2-way ANOVA with 69 Sidak posthoc test. **F** ) Quantification of trial length before vs. after eliminating reward differential (2v1-to-1v1), 70 [ _FInteraction_ (1,19)=1.20, _P_ =0.288, _FReward_ (1,19)=0.363, _P_ =0.55, _FChoice_ (1,19)=5.98, _P_ =0.024], 2-way ANOVA with 71 Sidak posthoc test. **G** ) Quantification of trial length before vs. after eliminating effort differential (1Barrier-to72 2Barriers), [ _FInteraction_ (1,20)=20.97, _P_ =0.0002, _FBarrier_ (1,20)=37.14, _P_ <0.0001, _FChoice_ (1,20)=0.037, _P_ =0.85], 2-way 73 ANOVA with Sidak posthoc test. N=6 mice, n.s. = not significant, *p<0.05, **p<0.01, ***p<.001, ****p<0.0001. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

76 

**==> picture [309 x 327] intentionally omitted <==**

- 77 **Figure 3 Experimental design and optic cannula for ACC silencing experiments** 

- 78 **A** ) Bilateral ACC was injected with virus expressing an inhibitory opsin (stGtCAR2) or control (mCherry), and 79 implanted with fiberoptic cannulae. **B** ) Histology showing representative virus + cannula targeting (one cannula 

- 80 was implanted at a 15 degree angle). **C** ) High magnification image showing membrane expression of stGtCAR2 

- 81 under optic fiber. **D** ) Overview of training and testing protocol for optogenetic silencing; optogenetic testing 82 followed no barrier and/or barrier training phases, and during an open field (OF) and tail suspension test (TST). 83 **E** ) Targeting of optic cannulae. **F** ) Example of a typical test day with 2 forced and 16 choice trials with light 84 delivered in a pseudorandom pattern. 

84 85 86 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

87 88 

**==> picture [541 x 264] intentionally omitted <==**

## **Figure 4  Optogenetic silencing of bilateral ACC reversibly disrupts high effort choices** 

89 **A** ) Schematic representing trial cycle on which light OFF/ON epochs are overlaid. **B** ) Example of light ON overlaid 90 for choice only, light ON during trial itself extends spatially from start through choice point. **C** ) Quantification of 91 %HR choices for light OFF vs. ON, end of ITI through choice point, mCherry and stGtACR2;  (blue shading is 92 light ON) [ _FInteraction_ (1,10)=7.13, _P_ =0.024, _FLaser_ (1,10)=6.20, _P_ =0.032, _FVirus_ (1,10)=6.14, _P_ =0.033], 2-way ANOVA 93 with Sidak posthoc test. **D** ) Quantification %HR for light OFF vs. ON, ITI + start only [ _FInteraction_ (1,20)=13.6, 94 _P_ =0.002, _FLaser_ (1,20)=11.2, _P_ =0.003, _FVirus_ (1,20)=14.0, _P_ =0.001], 2-way ANOVA with Sidak posthoc test. **E** ) 95 Quantification %HR for light OFF vs. ON, ITI only [ _FInteraction_ (1,20)=0.054, _P_ =0.82, _FLaser_ (1,20)=0.048, _P_ =0.83, 96 _FVirus_ (1,20)=3.98, _P_ =0.06], 2-way ANOVA with Sidak posthoc test. **F** ) Quantification %HR for light OFF vs. ON, 97 choice only [ _FInteraction_ (1,20)=20.8, _P_ =0.0002, _FLaser_ (1,20)=25.8, _P_ =0.0001, _FVirus_ (1,20)=20.6, _P_ =0.0002], 2-way 98 ANOVA with Sidak posthoc test. **G** ) 2 Barrier control continuation for stGtACR2 choice only condition. **H** ) %HR 99 for 2 Barrier control, consecutive trials quantified in blocks of 5 for light OFF vs. ON. For ( **C** ), mCherry (n=3), 00 stGtACR2 (n=4). For ( **D-H** ), mCherry (n=5), stGtACR2 (n=6); *p<0.05, **p<0.01, ***p<.001, ****p<0.0001. 

- 01 

- 02 

- 03 

- 04 

- 05 

06 07 08 09 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

**==> picture [335 x 206] intentionally omitted <==**

10 

**Figure 5  Optogenetic silencing of bilateral ACC reversibly disrupts high effort choices across days** 

11 

12 **A-B** ) Schematic for light ON vs. OFF during choice trials delivered across sequential 3 day blocks. **C** ) 13 Quantification of %HR choices for light OFF vs. ON, 3:1 differential no barrier condition [ _FInteraction_ (2,24)=0.10, 14 _P_ =0.904, _FDays_ (2,24)=1.53, _P_ =0.24, _FLaser_ (1,24)=4.30, _P_ =0.049], 2-way ANOVA with Sidak posthoc test (n=5). **D** ) 15 Quantification %HR for light OFF vs. ON, 3:1 one barrier condition [ _FInteraction_ (2,42)=0.11, _P_ =0.89, 16 _FDays_ (2,42)=0.76, _P_ =0.47, _FLaser_ (1,42)=91.99, _P_ <0.0001], 2-way ANOVA with Sidak posthoc test (n=8). **E** ) 17 Quantification %HR for light OFF vs. ON, 3:1 two barriers condition [ _FInteraction_ (3,38)=9.40, _P<0.0001,_ 18 _FDays_ (3,38)=8.96, _P_ =0.0001, _FLaser_ (1,38)=11.34, _P_ =0.002], 2-way ANOVA with Sidak posthoc test (n=7). **F** ) 19 Quantification %HR for light OFF vs. ON, mCherry control condition 3:1 one barrier condition 20 [ _FInteraction_ (2,26)=1.20, _P=0.32, FDays_ (2,26)=2.10, _P_ =0.14, _FLaser_ (1,26)=0.33, _P_ =0.57], 2-way ANOVA with Sidak 21 posthoc test (n=6). *p<0.05, **p<0.01, ***p<.001, ****p<0.0001. 

- 21 22 

- 23 

- 24 

- 25 

- 26 

- 27 

28 

29 

30 31 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

33 

32 

**==> picture [541 x 290] intentionally omitted <==**

## **Figure 6  ACC silencing alters choice trajectories during effort-based action selection** 

34 **A** ) Schematic representation of T-maze video processing: keypoint tracking with DeepLabCut (DLC) and 35 analysis of tracking data using custom BehaviorDEPOT code. **B** ) Behavior videos with silencing during action 36 selection used for tracking analysis. **C** ) Schematic representation of T-Maze zones assigned for subsequent 37 analysis (‘approach’ + ‘choice’). **D** ) DLC tracking for a mouse in the choice zone of the maze (head mounted 38 implant used as tracking point (green dot)). **E** ) Example trajectory plot for a mouse showing light OFF trials, and 39 **F** ) light ON trials with overlaid approach and choice zones. **G** ) Quantification of time in approach and choice 40 zones for light OFF vs. ON trials, one barrier condition - all choices [ _FInteraction_ (1,28)=4.41, _P_ =0.045, 41 _FZone_ (1,28)=2.47, _P_ =0.13, _FLaser_ (1,28)=14.35, _P_ =0.0007], 2-way ANOVA with Sidak posthoc test. **H** ) 42 Quantification for HR choices only [ _FInteraction_ (1,16)=1.16, _P_ =0.30, _FZone_ (1,16)=0.011, _P_ =0.92, _FLaser_ (1,16)=20.9, 43 _P_ =0.0003], 2-way ANOVA with Sidak posthoc test. **I** ) Quantification for LR choices only [ _FInteraction_ (1,20)=0.47, 44 _P_ =0.50, _FZone_ (1,20)=3.58, _P_ =0.07, _FLaser_ (1,20)=6.05, _P_ =0.02], 2-way ANOVA with Sidak posthoc test. **J** ) 45 Example, single trial trajectory plots for light ON condition (blue: low effort = ‘LR-ON’ and chrimson: high effort = 46 ‘HR-ON’) with locations of micropauses marked (arrowhead). **K** ) Locations of all pauses for example mouse. **L** ) 47 Quantification of pauses per trial for ALL choices, light OFF vs. ON [ _FInteraction_ (1,40)=8.30, _P_ =0.006, 48 _FLaser_ (1,40)=11.35, _P_ =0.0017, _FZone_ (1,40)=0.56, _P_ =0.46], 2-way ANOVA with Sidak posthoc test, and **M** ) broken 49 down by choice type [ _FLaser_ (1,20)=35.12, _P<0.0001_ , _FChoice_ (3,40)=1.47, _P_ =0.24, _FLaserXChoice_ (3,20)=6.27, _P_ =0.004], 50 Mixed-effects analysis with Sidak posthoc test. **N** ) Quantification of pause duration, ALL choices, light OFF vs. 51 ON [ _FInteraction_ (1,27)=0.176, _P_ =0.68, _FLaser_ (1,27)=0.357, _P_ =0.56, _FZone_ (1,27)=0.774, _P_ =0.39], 2-way ANOVA with 52 Sidak posthoc test, and **O** ) broken down by choice type [ _FLaser_ (1,35)=0.803, _P=0.38_ , _FChoice_ (3,35)=0.318, _P_ =0.81, 53 _FLaserXChoice_ (3,35)=0.168, _P_ =0.92], Mixed-effects analysis with Sidak posthoc test. *p<0.05, **p<0.01, ***p<.001, 54 ****p<0.0001. 

- 55 

bioRxiv preprint doi: https://doi.org/10.1101/2022.03.22.485350; this version posted January 3, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. 

- 56 

**==> picture [541 x 216] intentionally omitted <==**

## 57 **Figure 7  Optogenetic silencing of ACC has no effect on tail suspension test or open field tests.** 

- 58 **A** ) Quantification of mean struggling time calculated for each minute of the tail suspension test with optogenetic 

- 59 silencing of ACC (blue shading = light ON). **B** ) Summary data for light OFF vs. ON for mCherry (n=9) and 

- 60 stGtACR2 (n=12) conditions [ _FInteraction_ (1,38)=1.96, _P_ =0.17, _FVirus_ (1,38)=0.0021, _P_ =0.96, _FLaser_ (1,38)=0.0028, 

- 61 _P_ =0.96], 2-way ANOVA with Sidak posthoc test. **C** ) Quantification of mean velocity for open field test with 

- 62 optogenetic silencing of the ACC, data for light OFF vs. ON for mCherry (n=9) and stGtACR2 (n=8) conditions 63 [ _FInteraction_ (1,30)=0.0033, _P_ =0.95, _FVirus_ (1,30)=0.076, _P_ =0.78, _FLaser_ (1,30)=0.68, _P_ =0.42], 2-way ANOVA with Sidak 64 posthoc test. n.s. = not significant. 

