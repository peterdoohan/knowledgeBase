Article 

## **A cortico-collicular circuit for orienting to shelter during escape** 

|https://doi.org/10.1038/s41586-022-05553-9<br>Received: 25 May 2020<br>Accepted: 10 November 2022<br>Published online: 21 December 2022<br>Check for updates|**Dario Campagner1,2,5, Ruben Vale1,3,5, Yu Lin Tan1, Panagiota Iordanidou1, Oriol Pavón Arocas1, **<br>**Federico Claudi1, A. Vanessa Stempel1, Sepiedeh Keshavarzi1, Rasmus S. Petersen4, **<br>**Troy W. Margrie1 & Tiago Branco1**✉|
|---|---|
||When faced with predatory threats, escape towards shelter is an adaptive action that<br>ofers long-term protection against the attacker. Animals rely on knowledge of safe<br>locations in the environment to instinctively execute rapid shelter-directed escape<br>actions1,2. Although previous work has identifed neural mechanisms of escape<br>initiation3,4, it is not known how the escape circuit incorporates spatial information<br>to execute rapid fights along the most efcient route to shelter. Here we show that<br>the mouse retrosplenial cortex (RSP) and superior colliculus (SC) form a circuit<br>that encodes the shelter-direction vector and is specifcally required for accurately<br>orienting to shelter during escape. Shelter direction is encoded in RSP and SC neurons<br>in egocentric coordinates and SC shelter-direction tuning depends on RSP activity.<br>Inactivation of the RSP–SC pathway disrupts the orientation to shelter and causes<br>escapes away from the optimal shelter-directed route, but does not lead to generic<br>defcits in orientation or spatial navigation. We fnd that the RSP and SC are<br>monosynaptically connected and form a feedforward lateral inhibition microcircuit<br>that strongly drives the inhibitory collicular network because of higher RSP input<br>convergence and synaptic integration efciency in inhibitory SC neurons. This results<br>in broad shelter-direction tuning in inhibitory SC neurons and sharply tuned excitatory<br>SC neurons. These fndings are recapitulated by a biologically constrained spiking<br>network model in which RSP input to the local SC recurrent ring architecture<br>generates a circular shelter-direction map. We propose that this RSP–SC circuit might<br>be specialized for generating collicular representations of memorized spatial goals<br>that are readily accessible to the motor system during escape, or more broadly, during<br>navigation when the goal must be reached as fast as possible.|



Escaping to shelter has higher survival value than simply moving away from the source of threat[1] . Refuges are places where predators are usually impeded from entering and where predation risk is thus very low. To minimize exposure to the predator, navigating to the destination should in principle be as fast as possible, and animals rely on knowledge of the spatial environment to deploy accurate shelter-directed flights with very short reaction times[1,2] . Mice in new environments can learn the location of a shelter within minutes and when exposed to imminent threat, they orient their head and body in the shelter direction before running towards it along a straight vector[2] . Previous work has shown that shelter-directed escapes do not depend on sensory cues from the shelter and instead, mice use memory of the shelter location to reach safety[1,2] . Rodents therefore rely on continuously tracking the shelter direction during exploration to execute fast escape actions when exposed to threat[2,5] . Despite extensive knowledge about the neurobiology of spatial navigation[6–9] , it is not known how the escape circuit accesses information about safe locations to generate accurate shelterdirected actions during escape. 

## **Neural encoding of shelter direction** 

To investigate navigation to shelter, we allowed mice to explore a circular arena with a shelter and presented innately threatening sound stimuli[10] . These threat stimuli reliably elicited shelter-directed escapes initiated with a head rotation movement that oriented the mouse in the shelter direction[2] (Fig. 1a and Supplementary Video 1). To understand the neural basis of this orienting action we focused on two brain regions: RSP, which has been shown to encode the direction and angular velocity of the head as well as the spatial locations of goals and rewards[11,12] ; and SC, which can generate orienting motor commands[13,14] as well as escape initiation[10,15] , and receives projections from the RSP[16,17] . By simultaneously recording single-unit activity in these two regions while the animal explored the arena (Extended Data Fig. 1a and Supplementary Video 2; 836 RSP units and 683 SC units from 4 mice) we found that the firing rate of a subset of neurons in both the RSP and SC (centro- and latero-medial regions) is tuned to shelter direction (Fig. 1b,c, Extended Data Fig. 1b,c and Supplementary Video 3). This information is encoded 

> 1UCL Sainsbury Wellcome Centre for Neural Circuits and Behaviour, London, UK. 2UCL Gatsby Computational Neuroscience Unit, London, UK. 3MRC Laboratory of Molecular Biology, Cambridge, UK.[4] Division of Neuroscience, University of Manchester, Manchester, UK.[5] These authors contributed equally: Dario Campagner, Ruben Vale.[✉] e-mail: t.branco@ucl.ac.uk 

Nature | Vol 613 | 5 January 2023 | **111** 

## Article 

**==> picture [519 x 460] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>Shelter position 1 –90º<br>Auditory threat 180 ms<br>2 Hz<br>270 ms LED<br>±180º<br>Position 1<br>360 ms 5 Hz<br>450 ms 10 min 90º Visual cue<br>Memory-guidedorientation Shelter position 2 Shelter<br>Shelter<br>540 ms<br>LED Position 2<br>Head–shelter angle measurement 630 ms –90º 90º<br>5 Hz<br>Headdirection 135º angle directionHead 45º anglee 720 ms 55 min ±180º Visual cue –180 Head–shelter angle (º)–90 0 +90 +180<br>c d e<br>RSP SC<br>Position 2 tuning shift<br>1 1 RSP 4 9 SC<br>1 1<br>90 [o]<br>Per cent tuned<br>2 × 10 [–5]<br>neurons<br>30% Shelter<br>180º 0 [o]<br>RSP 1<br>1<br>90 [o]<br>0 0 Closed<br>29 63 30% shelter 0<br>–180 0 180 –180 0 180 180 [o] 0 [o] 4 2<br>Head–shelter angle (º) Head–shelter angle (º) SC<br>f g<br>Real data Full GLM GLM without HSO<br>Accuracy RSP 1 SC 1<br>change (%) –180<br>30 Hz 0<br>–30<br>RSP SC<br>5 s Tuning curve<br>180º<br>0º  180 0 0<br>Head–shelter angle –180 Predicted head–  180 –180 Predicted head–  180<br>–180º<br>Min Max shelter angle ( [o] ) shelter angle ( [o] )<br>Shelter Shelter<br>Shelter<br>Shelter<br>Shelter<br>Shelter<br>–2)<br>Neuron no. Neuron no.<br>LED<br>Normalized firing rate Normalized firing rate<br>Flight probability (mm<br>)(angle o<br>Real head–shelter P(predicted|real) P(predicted|real)<br>**----- End of picture text -----**<br>


**Fig. 1 | RSP and SC neurons encode egocentric shelter direction. a** , Left, superimposed video frames showing orientation to shelter after a threat stimulus and subsequent shelter-directed escape (the yellow line shows flight trajectory). The inset illustrates the measurement of egocentric shelter direction (defined as the head–shelter angle). Right, video frame sequence detailing the decrease in head–shelter angle at escape initiation (yellow arrows show head direction and white shade indicates head–shelter angle). **b** , Left, video frames with escape trajectories (yellow lines) to initial shelter position (top, position 1) and after rotation (bottom, position 2). Middle, tuning curves for a single SC unit, showing a rotation of the firing field that follows the rotation of the shelter position. Other explicit landmarks remain in place (LED and visual cue). Right, sample raster plot and tuning curve for the same neuron. **c** , Tuning 

curves for shelter-direction RSP and SC units for the shelter in position 1. Curves are sorted by tuning peak. **d** , Distribution of change in the Rayleigh vector direction after rotating the shelter by 90° (position 1 to position 2). **e** , Schematic of flight termination probability across the arena and percentage of units tuned to each of the shelters and the LED landmarks (circle area is proportional to percentage). **f** , Example generalized linear model data for a SC neuron showing the evolution of recorded firing rate (top left) and head– shelter angle (bottom left), together with the full model fit (cross-validated prediction accuracy: 50 ± 3%) and the same model without the head–shelter angle variable. Bottom right, the tuning curve recovered from the full model fit (yellow symbols) and the recorded curve (grey). **g** , Cross-validated confusion matrices for LDA population decoding of head–shelter angle. 

in an egocentric frame of reference and represents the angle between the current heading and the shelter (head–shelter angle; Supplementary Video 3). The preferred tuning of these shelter-direction neurons covers the entire egocentric angular space (Fig. 1c and Extended Data Fig. 1c,d) and their firing rate is independent of the allocentric head direction (Extended Data Fig. 1e and Extended Data Fig. 2). To confirm that the firing fields of shelter-direction neurons are anchored to the shelter, we rotated its position by 90° while keeping all other 

landmarks in place, which resulted in escapes to the new location after a brief exploration period[2] (Fig. 1b and Supplementary Video 4). The firing fields rotated with the shelter location and therefore maintained their angular tuning profile with respect to the shelter position (RSP median rotation = 113°, interquartile range (IQR) = [83°, 134°]; SC median rotation = 99°, IQR=[83°, 127°]; _P_ > 0.9 versus 90° and _P_ = 0 versus 0°, non-uniformity _v_ -test; Fig. 1e), indicating that neurons in RSP and SC specifically and dynamically encode the shelter direction. 

**112** | Nature | Vol 613 | 5 January 2023 

The tuning of shelter-direction neurons could in principle reflect either a behaviourally relevant or perceptually salient location in the environment. To distinguish between these two possibilities, we added to the arena a second, identical shelter but with the entrance closed, as well as a bright LED. Mice preferentially explored the open and closed shelters’ locations (Extended Data Fig. 1f), and threat presentation resulted in 79% of escapes to the open shelter, 14% to the closed shelter and none to the LED ( _n_ = 29 trials; Fig. 1e), indicating the relative behavioural relevance of each location for escaping from imminent threat. We then computed the egocentric direction tuning to these two locations, as well as to the location of one landmark in the arena, a bright LED. Whereas the fraction of RSP neurons tuned to the open and closed shelter was similar (open shelter: 3.5%, closed shelter: 3.5%; _P_ = 0.721, two-proportions _z_ -test), SC neurons were preferentially tuned to the open shelter (open shelter: 9.2%, closed shelter: 1.6%; _P_ = 0.000638, two-proportions _z_ -test), with both regions being significantly less sensitive to LED location (RSP: 0.8%, _P_ = 0.0277; SC: 1.1%, _P_ = 0.00254; two-proportions _z_ -test vs open shelter; Fig. 1e). This suggests that in this behavioural context, whereas the RSP contains a broader representation of familiar places in the arena, neurons in the SC preferentially encode the direction of the most behaviourally salient location for escape. 

Neurons in the SC and RSP have been shown to encode a range of different behavioural variables[11,18] , so we next quantified the contribution of shelter tuning to the firing rate of shelter-direction neurons in both areas. We built a generalized linear model that included several variables, including head direction and angular head movements (Methods), and measured the difference in firing rate prediction accuracy between the full model and one without shelter direction (Fig. 1f). Removing the shelter-direction predictor caused a drop of roughly 30% in the prediction accuracy, confirming that this variable is a key determinant of firing rate in single RSP and SC neurons (relative accuracy drop: RSP: −24 ± 3.67%, _P_ = 1.2511 × 10[−6] ; SC, −31 ± 3.6%, _P_ = 8.8599 × 10[−12] , one-tailed _t_ -test). Furthermore, at the population level, a linear discriminant analysis-based decoder (LDA) could use the neuronal firing rates to predict the shelter direction significantly above chance (prediction accuracy: SC, 0.73; RSP, 0.83; chance, 0.19; Fig. 1g). Together these results show that there are neurons in the RSP and SC that represent the ongoing shelter direction in an egocentric reference frame, which is the information needed to generate orienting movements towards the shelter during escape. 

## **Dependence on RSP activity** 

As the RSP is proposed to act as a hub for integrating spatial information[11] , we hypothesized that the representation of shelter direction in the SC might depend on RSP input. To test this, we assessed the effect of inactivating RSP neurons on SC shelter-direction tuning. We used a chemogenetic approach where we targeted the inhibitory designer receptor hM4Di selectively to SC-projecting RSP neurons by injecting AAVretro-cre in the SC and Cre-dependent hM4Di in the RSP (Fig. 2a and Extended Data Fig. 3). We then recorded single-unit activity in the RSP and SC during activation of hM4Di with systemic delivery (by intraperitoneal injection) of clozapine _N_ -oxide (CNO). This manipulation significantly decreased the in vivo firing rate of RSP neurons, confirming the chemogenetic inhibition ( _P_ = 0.0029, one-tailed Kolmogorov–Smirnov test; _n_ = 340 units, 2 mice; Fig. 2b,c). In the SC, whereas the overall firing rate of the population was not affected (Extended Data Fig. 4), RSP loss of function caused a 33% decrease in the fraction of SC shelter-direction neurons ( _P_ = 0.01, Chi-squared test; Fig. 2d). Accordingly, the ability to decode shelter direction at the SC population level was also compromised (Fig. 2e; median change in accuracy = −18.76%; IQR = [−15.7%, −19.7%], _P_ = 0.0020, signed rank test). These data show that the representation of egocentric shelter direction in the SC depends on RSP input. They further suggest that the 

RSP–SC pathway might be a critical neural circuit element for navigating to shelter during escape. 

To investigate the relevance of RSP neurons and their SC projections for shelter-directed escape behaviour, we used the same retrograde AAV strategy to inactivate SC-projecting RSP neurons (Extended Data Fig. 3) while monitoring behavioural responses to imminent threat. Loss of function of these RSP neurons caused mice to make larger errors in the orientation phase of escape (Fig. 2f,g and Supplementary Video 5; median escape error: CNO: 23°, 105 trials, 11 mice; saline: 5°, 51 trials, 6 mice; _P_ = 0.0153, permutation test) without affecting escape vigour (Extended Data Fig. 6g). This phenotype was observed for escapes elicited in both light and dark conditions, indicating that the errors were not caused by impaired visual processing (Extended Data Fig. 5). The orientation deficits resulted in flight trajectories that were not directed towards the shelter location and consequently, the probability of terminating the flight outside the shelter was 7.4 times higher than for the control ( _P_ = 0.0001, two-proportions _z_ -test; Fig. 2h). Although these escapes after RSP–SC inactivation were often resumed and the shelter was eventually found, the time to shelter was 50% longer than for the control (CNO: median = 2.1 s, IQR = [1.8 s, 2.8 s]; saline: median = 1.4s, IQR = [1.1 s, 1.7 s]; _P_ = 0.0439, permutation test; Extended Data Fig. 6h). Furthermore, flights were aborted earlier when orientation errors were larger (Extended Data Fig. 6i), suggesting that mice might retain awareness of shelter direction but are unable to select the appropriate direction of travel, similar to topographic disorientation in humans with RSP lesions[19] . We observed the same orientation impairment after global inactivation of RSP with chemogenetics (Extended Data Fig. 7a and Supplementary Video 6) and muscimol (Extended Data Fig. 7d and Supplementary Video 7). However, chemogenetic loss of function of the posterior parietal cortex (PPC) and anterior motor areas (AMA), two other SC-projecting cortical areas involved in goal-directed navigation, did not perturb shelter-directed escapes (Fig. 2k and Extended Data Figs. 7b,c and  8). This confirms that orienting to shelter is particularly dependent on RSP function. Since systemic CNO injection may inactivate SC-projecting RSP neurons that have collaterals to other regions, we next tested whether the orientation deficits were specifically due to loss of activity in RSP–SC synapses. We again targeted hM4Di to SC-projecting RSP neurons with the retrograde viral strategy, but locally infused CNO over the SC to specifically inactivate the RSP–SC projection (Fig. 2i, Extended Data Fig. 9a and Supplementary Video 8), which recapitulated the escape orientation errors of global RSP loss of function (Fig. 2j). By contrast, placing the cannula over a prominent secondary projection of SC-projecting RSP neurons, the anterior cingulate cortex (Extended Data Fig. 9b), did not affect escape behaviour (Fig. 2j and Supplementary Video 9), further supporting a unique role of RSP–SC inputs in orienting to shelter during imminent threat. 

## **Escape specificity of the RSP–SC circuit** 

Since previous studies have shown that the SC commands orienting to sensory stimuli[13,18,20] and that the RSP contains representations of space[7,11,21] , the behavioural phenotype we observe after inactivation of the RSP–SC pathway could, in principle, be a trivial result from perturbing these known functions. To evaluate this possibility, we first tested whether RSP–SC inactivation impaired the classic role of the SC in sensory-guided orienting. We started by considering that RSP input to the SC might be necessary for SC control of head movement, and analysed whether RSP inactivation affected the relationship between the firing rate of SC neurons and head movements. As previously reported[22] , we found SC neurons tuned to egocentric head displacements (Fig. 3a), from which upcoming angular head movements could be decoded at the population level (Extended Data Fig. 10a). Chemogenetic inactivation of SC-projecting RSP neurons with intraperitoneal CNO injection did not affect motor tuning of SC neurons (Fig. 3a) and the LDA prediction accuracy was not different between CNO and saline conditions (Fig. 3c; 

Nature | Vol 613 | 5 January 2023 | **113** 

## Article 

**==> picture [517 x 547] intentionally omitted <==**

**----- Start of picture text -----**<br>
a c d<br>0<br>Before RSP inactivation After RSP inactivation<br>RSP RSP Saline<br>Shelter Shelter<br>5%<br>Flexed-hM4Di RSP AAVretro-cre CNO –90º 90º –90º 90º<br>–0.55<br>30 Hz 30 Hz<br>SC<br>Cortex 500 μm Δ Firing rate index ±180º ±180º<br>b e 5 Hz<br>RSP SC<br>1<br>Baseline –180<br>RSP inactivation<br>CNO<br> 180<br>0 –180 –90 0 90 180 –180 –90 0 90 180<br>–180 –90 0 90 180 –180 180<br>Predicted head–  Head–shelter angle (º) Head–shelter angle (º)<br>Head–shelter angle (º) shelter angle (º)<br>f g h<br>Auditory threat<br>Shelter orientation error Flight termination error<br>Wrong orientation 120 ms<br>movement 90º 10 [–7]<br>240 ms 23º<br>CNO<br>180º 0<br>360 ms Saline 5º<br>480 ms<br>90º 10 [–7]<br>RSP inactivation 600 ms<br>i j k<br>500 μm 90º Area inactivation Projection<br>inactivation<br>RSP Cortex<br>SC SC control<br>30º<br>20<br>CNO<br>180º<br>Saline<br>15º 10<br>hM4Di RSP<br>CNO<br>SC 90º 1<br>Inactivation of RSP–SC axon terminals<br>angle (º)<br>Real head-shelter P(predicted|real)<br>–2)<br>Shelter Shelter Shelter Shelter<br>Flight probability (mm<br> SC<br>Shelter →<br>SC-projecting Muscimol<br> ACC<br>RSP  →<br>Global<br>Normalized orientation error PPC AMA RSP<br>**----- End of picture text -----**<br>


**Fig. 2 | Shelter-direction tuning in SC and orientation to shelter during escape depend on RSP input. a** , Schematic of retrograde adeno-associated virus (AAV) strategy for inactivating SC-projecting RSP neurons, and coronal image of targeted RSP neurons. **b** , Sample raster plot of a RSP shelter-direction cell before and after intraperitoneal CNO administration. **c** , Population histograms showing a decrease in firing rate in RSP neurons after intraperitoneal CNO. **d** , Example tuning curves and sample raster plots showing loss of tuning in an SC shelter-direction neuron after intraperitoneal CNO. **e** , Cross-validated confusion matrix for LDA population decoding of head–shelter angle in SC after RSP inactivation. **f** , Example video frames as in Fig. 1a, showing escape initiation in the wrong direction owing to incorrect orientation. **g** , Summary plot of orientation errors at escape initiation after intraperitoneal CNO. The light shaded area covers the 5th to 95th percentile range; the dark bar is the 

IQR and the white line shows the median. **h** , Summary plot for location of flights terminated outside the shelter (CNO: 29.5%, saline: 3.9%). **i** , Example coronal image of RSP axon terminals in the SC and schematic for local inactivation of these terminals. **j** , Orientation errors as in **g** , for local CNO infusion over SC (54 CNO trials and 37 saline trials from 6 mice; _P_ = 0.0032, permutation test). **k** , Summary of activity manipulation effects on orientation errors. Global RSP: 57 CNO trials and 32 saline trials from 5 mice; _P_ = 0.004; Muscimol: 21 drug trials from 6 mice and 25 saline trials from 3 mice; _P_ = 0.0061; PPC: 31 CNO trials and 22 saline trials from 3 mice; _P_ = 0.6514; AMA: 31 CNO trials from 4 mice and 28 saline trials from 3 mice; _P_ = 0.1003; RSP to ACC: 21 CNO trials and 21 saline trials from 5 mice; _P_ = 0.8282 _,_ permutation test. Data are normalized by dividing each inactivation trial error by the median of the orientation error of the respective control dataset. 

**114** | Nature | Vol 613 | 5 January 2023 

**==> picture [339 x 329] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>2 Hz directionHead 45° angle Prediction accuracy change (%)–4 –2 0 2 4 6<br>60 ms<br>d<br>Baseline Tone 120 ms 20 RSP inactivationSC-projecting<br>Sensory-guided<br>After CNO orientation 180 ms<br>10<br>240 ms<br>–20 0 20<br>1<br>Head displacement (°) 300 ms<br>e f<br>* NS * NS<br>1 9<br>Food available<br>0 s 7 s 9 s<br>Mouse in Sound on<br>trigger area<br>75%<br>directionHead 45° angle<br>0 ms 0 0<br>Sound Sound Escape Food-<br>Distance OFF ON seeking<br>travelled 133 ms * NS * NS<br>2.5 180<br>Shortest path 266 ms<br>Lick port<br>400 ms<br>533 ms<br>1 0<br>Escape Food- Escape Food-<br>666 ms seeking seeking<br>Sound trigger area<br>Speaker<br>Speaker Speaker Speaker<br>Shelter<br>ound<br>S<br>Normalized orientation error<br>Lick port<br>Saline CNO<br>Saline<br>Lick probability Saline Time to goal (s)<br>Saline CNO<br>Lick port<br>Lick port<br>Tortuosity Saline Saline CNO Saline CNO Saline CNO<br>Orientation error (º)<br>**----- End of picture text -----**<br>


**Fig. 3 | Orientation and navigation errors after RSP–SC inactivation are specific to escape behaviour. a** , Tuning curve and sample raster plot for an SC neuron tuned to egocentric head displacement. **b** , Example video frames showing instinctive orientation to a sound source, an SC-dependent behaviour. **c** , Change in LDA prediction accuracy of head displacement from SC firing rates (percentage change in CNO − percentage change in saline). **d** , Summary data showing no effect of inactivation of SC-projecting RSP neurons in the soundorienting assay but increased shelter orientation errors for the same mice ( _P_ = 0.0143, permutation test; 32 CNO trials and 42 saline trials). Data are normalized by dividing each CNO trial error by the median orientation error of 

the respective control dataset. **e** , Task schematic (top) and example video frames showing curved trajectory and slow orientation towards lick port during a learned, non-urgent goal navigation task. **f** , Summary data showing that mice learned the task rules (top left) and that the behaviour is not affected by inactivation of SC-projecting RSP neurons. Lick probability, time to lick port, trajectory tortuosity and errors in orientation to lick port are not different between saline control and CNO trials, in contrast to the increased shelter orientation errors during escape measured in the same mice. Note that time to goal and path tortuosity are different between navigation during escape and food-seeking. * _P_ < 0.05. 

median change = 2.1%, IQR = [0.2%, 3.2%]; _P_ = 0.11, signed rank test). This suggests that SC motor function was not affected by RSP–SC inactivation, therefore predicting that simple orientation movements to acute sensory stimuli should be preserved after RSP loss of function[13,18,20] . To test this prediction, we developed a sound-orienting assay to probe sensory-guided SC motor function. One of two speakers placed opposite each other emitted a brief tone while the animal explored the arena. Mice innately oriented to the sound emitting speaker as quickly and accurately as they orient to the shelter (Fig. 3b, Extended Data Fig. 10b–e and Supplementary Video 10). However, in contrast to the shelter orientation errors during escape, inactivation of SC-projecting RSP neurons (Extended Data Fig. 3) did not increase the error in orienting to the sound, confirming that RSP activity is not required for sensory stimulus-guided orientation ( _P_ = 0.9290, permutation test; _n_ = 23 CNO trials and 26 saline trials, 4 mice; Fig. 3d and Supplementary Video 11). These experiments demonstrate that the escape errors after RSP–SC inactivation do not result from disrupting the general ability of the SC to command orientation movements. Instead they indicate that the RSP–SC pathway is specific for memory driven goal orientation, suggesting that the SC contains parallel streams for processing direct sensory orienting and orienting to high-order memory-based targets. 

We next addressed whether escape errors after RSP inactivation arise because of a generic disruption of the ability of mice to navigate 

in space. First, we analysed navigation during exploratory behaviour and found no differences between control and RSP–SC inactivated animals (Extended Data Fig. 6e,f). Second, we probed the effect of RSP–SC inactivation on goal-directed navigation in an alternative task. To test this, we placed mice in the same arena, but instead of a shelter we provided a lick port to which the mice were trained to go to in response to a long sound cue (7 s). Although both navigation to the lick port and navigation to the shelter during escape are directed towards a learned, rewarding spatial goal, a key difference in the navigation strategies in these two tasks was the efficiency with which the mice reach the goal: mice arrived at the lick port approximately 1 s later than at the shelter during escape, and the path taken to the lick port was curved, unlike the direct path taken during escape, as the mice did not orient immediately to the target but instead slowly oriented throughout the trajectory (Fig. 3e,f). In contrast to escape, inactivation of RSP–SC did not increase orientation errors to lick port (Fig. 3f and Supplementary Video 12). These data show that the escape errors following RSP–SC inactivation do not simply reflect a generic deficit in spatial navigation. Instead, they suggest that the RSP–SC pathway might have a specialized role for either escape or navigation when the goal must be reached as quickly as possible, and similar to the SC, suggest that there are parallel pathways in the RSP network for different types of goal-directed navigation[11,23] . 

Nature | Vol 613 | 5 January 2023 | **115** 

Article 

**==> picture [339 x 383] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b 20 Hz RSP activation vGATvGluT2 [+]  SC [+]  SC<br>500 μm 0.4<br>RSP RSP<br>SC<br>ChrimsonR Neuropixels<br>Opticfibre SC 0<br>SC<br>RSP 1 mm 200 ms<br>vGAT-ChR2 or vGluT2-ChR –0.2<br>c vGluT2 [+]  SC vGAT [+]  SC d 180<br>vGAT [+]  SC<br>20 mV 20 mV<br>200 ms<br>Membrane potential<br>100<br>20 Hz RSP activation 79 vGluT2 [+]  SC<br>50 pA<br>Current steps Synaptic currents 100 ms 1 Light pulse no. 5<br>e f<br>vGluT2 [+] vGAT [+] vGluT2 [+ ] projecting vGAT [+ ] projecting vGAT [+ ] projecting<br>360 vGluT2 [+ ] projecting<br>SC SC RSP RSP<br>100 μm 250 μm 200 μm 500 μm 0 0 600<br>No. of SC starter cells<br>1.1<br>*<br>AMA All<br>Starter cells vGAT [+ ] projecting<br>(rabies + helpers) vGluT2 [+ ] projecting<br>PPC<br>NS<br>NS<br>RSP<br>0<br>RSP AMA PPC<br>Population firing rate  (normalized)<br>Peak voltage (%)<br>No. of RSP presynaptic cells<br>RSPa<br>Convergence index<br>RSPd<br>RSPv<br>**----- End of picture text -----**<br>


**Fig. 4 | RSP synaptic input has a diverging effect on SC vGAT[+] and vGluT2[+] neurons. a** , Schematic of dual-opsin strategy for recording dynamics of the SC network following RSP input in head-fixed mice (inset) and coronal image of the targeted RSP and SC neurons with trajectories of acutely inserted Neuropixels probes (left). Right, 3D rendering of probe trajectories in all mice. **b** , Normalized firing rate of vGluT2[+] (32 neurons) and vGAT[+] (68 neurons) SC populations during 20 Hz activation of RSP axons in SC in vivo. Both SC populations are initially activated but diverge in firing profile over the course of stimulation. **c** , Example synaptic potential and currents evoked by 20 Hz optogenetic stimulation of RSP inputs onto excitatory and inhibitory SC neurons in vitro (blue circles indicate stimulation times). Left insets show voltage response to step current injections. **d** , Summary plot of summation during 20 Hz optogenetic activation of RSP inputs (vGAT[+] : slope = 17.6%, _P_ = 5.2 × 10[−13] ; vGluT2[+] : slope = −2.9%, P = 0.16; linear regression). **e** , Left, coronal images (top) and 3D reconstruction (bottom) of vGluT2[+] or vGAT[+] starter cells in SC. Cells 

expressing helper AAVs are shown in yellow, rabies-infected cells are shown in blue and starter cells are shown in white (inset). White arrows point to example starter cells. Right, coronal image (top) and 3D reconstruction (bottom) showing labelled input areas to excitatory and inhibitory SC neurons, including the RSP (inset). **f** , Top, number of RSP-labelled cells as a function of the number of SC starter cells, showing higher convergence of RSP input onto inhibitory SC cells for any given number of starter cells (each dot is data from one mouse). Logarithmic fit _P_ -values: vGluT2[+] : 0.0017; vGAT[+] : 1.7 × 10[−5] . The shaded area represents the 95% confidence interval. Note that the confidence intervals for vGluT2[+] and vGAT[+] never overlap. Bottom, cell type-specific convergence index for RSP, AMA and PPC, showing that the higher convergence onto SC inhibitory neurons is specific to RSP inputs and that AMA and PPC have lower convergence onto SC neurons overall. Starter cells were observed in all the three RSP subdivisions: RSP ventral part (RSPv), RSP dorsal part (RSPd) and RSP lateral agranular part (RSPa). 

## **Mechanisms for shelter direction mapping** 

To understand the cellular and circuit mechanisms supporting the transfer of shelter direction information between the RSP and the SC we next measured the dynamics of the SC network in response to RSP input using single-unit recordings in head-fixed animals and optical stimulation via a fibre placed over the SC (Fig. 4a and Extended Data Fig. 14). We expressed ChrimsonR, a red-shifted opsin, in SC-projecting RSP cells to activate RSP input, and channelrhodopsin-2 in either vGluT2[+] or vGAT[+] cells in the SC to determine the response profile of excitatory and inhibitory SC neurons, respectively, using an opto-tagging approach[24] (Fig. 4a). Activation of RSP input to SC with 20 Hz pulses 

caused a short-latency increase in the firing rate of both excitatory and inhibitory SC neurons (vGAT[+] latency = 9 ms, vGluT2[+] latency = 4 ms; Fig. 4b). Over the course of 1 s of stimulation, however, the firing profiles of these two cell populations diverged markedly: whereas the firing rate of vGAT[+] neurons increased progressively, the activity of vGluT2[+] neurons started to decrease after about 100 ms and became inhibited, falling below the baseline firing rate. This low-dimensional activity profile captures most of the variance across SC neurons responses to cortical activation (Extended Data Fig. 11). Although this stimulation paradigm is artificial, it indicates that the RSP engages both excitatory and inhibitory cells in SC. In addition, the divergent firing profiles between the two SC populations suggested that there might be a feedforward lateral 

**116** | Nature | Vol 613 | 5 January 2023 

inhibition circuit, whereby inhibitory cells activated by RSP inhibit excitatory cells that also receive RSP input. We therefore investigated in more detail the functional organization of the RSP–SC microcircuit. 

First, we characterized the anatomy of the RSP–SC projection[16,17] with cell type-specific monosynaptic retrograde rabies virus tracing from vGluT2[+] or vGAT[+] starter cells (Fig. 4e; _n_ = 6 mice each). Rabies infection of either SC population resulted in prominent labelling of layer 5 RSP neurons, showing that both excitatory and inhibitory SC cells indeed receive RSP input (Fig. 4e). There was, however, 1.8 times more convergence of RSP input onto inhibitory than excitatory cells (Fig. 4f; convergence index vGAT[+] = 0.83 ± 0.14, vGluT2[+] = 0.47 ± 0.08, _P_ = 0.035, _t_ -test). The magnitude of RSP convergence into the SC was also higher than two other cortical areas involved in navigation (PPC and AMA), which projected in a sparser and symmetrical manner to excitatory and inhibitory SC neurons (AMA: convergence index vGAT[+] = 0.29 ± 0.05, vGluT2[+] = 0.32 ± 0.05; PPC: convergence index vGAT[+] = 0.19 ± 0.04, vGluT2[+] = 0.18 ± 0.04; Fig. 4f). Next, we measured the physiological properties of RSP–SC connections using whole-cell recordings in vitro and channelrhodopsin-2 expressed in the RSP. Optogenetic activation of RSP axons over the centromedial and centrolateral SC confirmed a high connectivity rate for both excitatory and inhibitory SC neurons (vGluT2[+] : 37.1%, _n_ = 70 cells, 4 mice; vGAT[+] : 43.8%, _n_ = 73 cells, 4 mice). RSP input elicited excitatory monosynaptic potentials in both cell populations, and we found that temporal summation was more efficient in vGAT[+] neurons because of differences in intrinsic excitability and short-term synaptic plasticity (Fig. 4c,d and Extended Data Fig. 12; fifth pulse peak voltage: 154 ± 14% for vGAT[+] , 79 ± 12% for vGluT2[+] ; _P_ = 2.53 × 10[−4] , _t_ -test). Together, these data show that both excitatory and inhibitory SC neurons receive monosynaptic input from the RSP and suggest that RSP activity should generate a stronger drive in the inhibitory network because of higher anatomical convergence and more efficient synaptic integration in vGAT[+] neurons. 

Next, we looked for the existence of the feedforward lateral inhibition motif suggested by the RSP stimulation experiments, using a dual-opsin, dual-recombinase anterograde strategy and slice electrophysiology. In brief, to express an opsin specifically in the SC vGAT[+] cells that receive RSP input, we injected an anterograde virus carrying a Cre-dependent flippase[25] into the RSP of vGAT::cre mice. This anterograde virus jumps one synapse into the SC, resulting in SC vGAT[+] cells expressing flippase. Injection of a flippase-dependent channelrhodopsin-2 into the SC then induced opsin expression in this cell population (Fig. 5a,b). In addition, we also expressed a Cre-off fluorescent marker to label putative excitatory SC cells (that is, vGAT[−] ), as well as ChrimsonR in the RSP to activate RSP axons. We then obtained whole-cell recordings from SC excitatory cells, activated ChrimsonR to identify vGAT[-] neurons that directly receive RSP input, and stimulated channelrhodopsin-2 to elicit inhibition. This experiment revealed that 26.3% of excitatory neurons in the SC receive both monosynaptic input from the RSP and are directly inhibited by the local vGAT[+] neurons that also receive RSP input (Fig. 5c). The RSP–SC circuit therefore contains a feedforward lateral inhibition motif. 

To further explore how the RSP–SC circuit maps shelter direction between RSP and SC, we measured the electrophysiological properties of additional local SC connections (Extended Data Fig. 13a) and built a spiking network model constrained by our anatomical and electrophysiological data. In brief, the model consisted of conductance-based leaky integrate-and-fire RSP neurons organized as a ring-like network, with neighbouring neurons tuned to similar angles and providing inputs to vGluT2[+] and vGAT[+] SC neurons with diagonal and inverted diagonal connectivity kernels, respectively (Fig. 5d; see Methods for details). vGAT[+] SC neurons inhibited vGluT2[+] SC neurons to replicate the measured feedforward lateral inhibition architecture, and the model also included the remaining local SC connections, all with diagonal connectivity matrices (Fig. 5d and Extended Data Fig. 13b). This model successfully fitted the SC firing dynamics elicited by RSP stimulation (average sum 

of squared errors of 30 best fitting models = 1.6770 ± 0.0066; Fig. 5e), whereas a standard ring attractor model without feedforward lateral inhibition[8,26–28] achieved a poorer fit (4.1891 ± 0.0743; _P_ = 8.97 × 10[−40] , _t_ -test; Extended Data Fig. 13c). In the feedforward lateral inhibition model, when the mouse is at a particular angular distance from the shelter, RSP neurons tuned to this distance create an activity bump in a small fraction of excitatory SC neurons, which inherit the respective cortical tuning (Fig. 5d). In parallel, the active RSP neurons also excite SC inhibitory neurons that project to an orthogonal population of excitatory SC cells, and consequently silence the excitatory neurons surrounding the activity bump because of the high efficiency of the RSP synaptic connection onto inhibitory SC neurons (Fig. 5e). The net result is a clean mapping of shelter direction between the RSP and SC networks. A prediction from this model is that the tuning of SC excitatory cells should be narrow, whereas the tuning of inhibitory cells should be broad because they pool from RSP neurons with diverse tuning. To test this prediction, we recorded SC shelter-direction cells in vivo while opto-tagging excitatory or inhibitory cells (Extended Data Figs. 1a and 14). We found that the tuning curves of inhibitory SC neurons were indeed broader than for excitatory cells, with Rayleigh vectors 2.4 times higher (vGAT[+] : 0.09 ± 0.002, vGluT2[+] : 0.22 ± 0.04; _P_ = 0.0054, _t_ -test; Fig. 5f). 

## **Discussion** 

Our results show that the RSP and SC continuously encode the escape goal direction vector in an egocentric reference frame. RSP neurons project to both excitatory and inhibitory SC neurons but generate a stronger drive of the inhibitory network because of higher convergence and more efficient synaptic integration. By dissecting the RSP–SC pathway with projection and cell-type specificity, we find a feedforward lateral inhibition circuit architecture, whereby inhibitory neurons that receive RSP input directly inhibit excitatory neurons that also integrate RSP synaptic input. Since the representation of shelter direction in the SC depends on RSP activity, a plausible model is that the RSP generates an egocentric representation of shelter direction that the SC inherits. Although it is possible that the RSP broadcasts spatial and self-motion signals that are used locally by the SC to assemble shelter direction de novo, we show that the RSP–SC synaptic connection is necessary for accurate orientation to shelter during escape. We therefore favour a model in which shelter direction is directly mapped from the RSP to the SC. Through simulating a biologically constrained spiking network we propose that this mapping is done by exploiting the feedforward lateral inhibition motif to generate shelter tuning in a subset of excitatory SC neurons while inhibiting the network of excitatory cells with orthogonal tuning. The finding that shelter tuning curves in excitatory SC neurons are sharper than in inhibitory neurons is in support of this model. Similar models have been previously applied to explain tuning specificity in sensory pathways, including visual[29] , somatosensory[30] and auditory[31] ; as well as to the representation of saccadic vectors between the frontal eye field and the SC[32] . Our model is also closely related to models of heading direction in a variety of circuits and animals species[26,33,34] , perhaps suggesting a conserved circuit architecture for mapping circular variables. 

The firing fields of shelter-direction cells are similar to goal-vector cells found in the hippocampus of bats[35] and the lateral entorhinal cortex of rats navigating to learned reward locations, and to egocentric centre-bearing cells in the postrhinal cortex; though distinct from egocentric boundary vector cells[21,36,37] . The finding of an egocentric representation of shelter direction vector in the RSP agrees with previous work showing that RSP neurons encode behaviourally important locations, such as landmarks, reward locations and a variety of spatial features of the environment[21,38,39] . In particular, the RSP integrates information from multiple streams to form representations of head-direction and angular velocity[40] , place and conjunctives of 

Nature | Vol 613 | 5 January 2023 | **117** 

## Article 

**==> picture [513 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>Anterograde transynaptic DIO-Flp Excitatory SC neuron<br>Syn-ChrimsonR<br>FRT-ChR2 RSP activation vGAT [+]  activation<br>cre-off-FP<br>SC<br>vGAT-cre 100 ms<br>mouse  10 pA<br>50 μm<br>ChrimsonR [+]  cells RSP-receiving vGAT [+] Input from  Input from RSP-receiving<br>RSP-receiving vGAT [+] ChR2 [+]  cells  ChR2 [+]  cells  RSP neurons SC vGAT [+]  neurons<br>vGAT [–]  labelled cells<br>d<br>RSP shelter direction tuning  RSP to SC vGluT2 [+] RSP to SC vGAT [+] Recurrent excitation Lateral inhibition<br>–90º<br>±180º<br>90º<br>Illustrative shelter tuning curves<br>Firing rate or<br>–90º –90º –90º projection strength<br>RSP neuron<br>High<br>SC vGAT [+]  neuron<br>±180º ±180º ±180º SC vGluT2 [+]  neuron<br>SC vGAT [+]<br>Excitatory synapse<br>Inhibitory synapse Low<br>90º 90º 90º<br>e f<br>20 Hz RSP activation<br>Fitted model tuning curves Tuning curves in freely behaving mice<br>Predicted –90º –90º –90 [o] –90 [o]<br>Real<br>SC vGluT2 [+] SC vGAT [+] SC vGluT2 [+] SC vGAT [+]<br>0.05 AU ±180º ±180 [o]<br>SC vGat [+]<br>SC vGluT2 [+] 90º 90º 90 [o] 90 [o]<br>100 ms Model Rayleighvector length SC vGAT [+] * Real Rayleighvector length SC vGAT [+] *<br>0.1 0.1<br>RSP SC vGluT2+<br>SC vGluT2+ SC vGluT2+<br>Shelter<br>+ +<br>Shelter Shelter Shelter SC vGluT2 SC vGAT RSP<br>Shelter Shelter<br>**----- End of picture text -----**<br>


**Fig. 5 | A feedforward lateral inhibition model for mapping shelter** 

**direction from RSP to SC. a** , Schematic of the anterograde dual-opsin strategy used to test for feedforward lateral inhibition in vitro. **b** , Coronal image of RSPreceiving vGAT[+] cells expressing ChR2. **c** , Activation of RSP-receiving vGAT[+] SC cells generates inhibitory synaptic currents in vGAT[−] SC cells (right) that also receive monosynaptic RSP input (left). **d** , Top, schematic illustrating the ring architecture and connectivity profiles for the different components of the feedforward lateral inhibition model (RSP, vGluT2[+] SC and vGAT[+] SC networks). Neurons are shown organized in a circular manner with respect to their shelter tuning preference. Colour intensity of circles indicates neuronal firing rate, colour intensity of lines indicates projection strength. From left to right: RSP population firing when the mouse faces −90° from the shelter, RSP projections to vGluT2[+] SC and vGAT[+] SC (only projections from the RSP neuron tuned to −90° are shown), local recurrent excitation and lateral inhibition within SC. RSP neurons excite a small number of recurrently connected SC vGluT2[+] neurons, 

which inherit the same tuning, while exciting all other SC vGAT[+] neurons that then project to orthogonal vGluT2[+] SC neurons. Activity in a given RSP neuron results in feedforward lateral inhibition of all SC vGluT2[+] neurons with a different shelter direction preference. Additional circuit elements are shown in Extended Data Fig. 13. Bottom, tuning curve schematics for an RSP neuron tuned to −90° and for the vGluT2[+] and vGAT[+] SC neurons most strongly excited by the RSP neuron shown. **e** , Left, mean and 95% confidence interval of predicted firing rate of vGluT2[+] and vGAT[+] SC populations following 20 Hz activation of RSP neurons in the best 30 models fitted to the data, compared with the dynamics recorded in vivo (dashed lines, data from Fig. 4b). Right, example predicted tuning curves for vGluT2[+] and vGAT[+] SC neurons (top). The model predicts that vGluT2[+] SC neurons are more sharply tuned to shelter direction than vGAT[+] SC neurons (bottom). **f** , Experimentally measured tuning curves of opto-tagged vGluT2[+] and vGAT[+] SC neurons and Rayleigh vector lengths for the population of recorded neurons. 

**118** | Nature | Vol 613 | 5 January 2023 

these variables[21] , and it is thus well-positioned to compute spatial representations in egocentric coordinates[11,36,37,41,42] . An important finding of our study is that although the escape orientation errors after RSP–SC inactivation could in principle be explained by a perturbation of these known RSP functions and a general loss of navigation ability, we show that loss-of-function in the RSP–SC pathway does not perturb navigation during exploration or to a food reward goal. This suggests that there are parallel circuits for different types of navigation, and that the RSP–SC pathway might be dedicated for escape behaviour or navigation when the goal needs to be reached as fast as possible. Our recordings with two shelters in the arena further suggest that the RSP may form egocentric maps of behaviourally important locations in general. By contrast, the SC specifically encoded the open shelter direction. Together with the known role of the SC in establishing saliency and priority maps[43,44] , these findings raise the possibility that the SC selects the most relevant target from a pool of RSP-encoded locations. 

- Previous work has demonstrated a role for cortico-collicular path ways mediating learned actions in highly trained animals in a variety of tasks and species[45,46] . Here we demonstrate that a cortico-collicular circuit is essential for an instinctive, survival behaviour. A key finding is that SC motor function and sensory-guided orientation were not affected by RSP loss-of-function, and thus escape orientation errors cannot be explained by generic orientation deficits. Instead, our data suggest a selective role for the RSP–SC circuit in the memory-guided orienting movements required to orient to shelter[2] . Future work will be needed to understand how the shelter orienting action is generated upon the detection of threat, which requires integrating additional information from areas such as the medial SC[3] . A possible advantage of this cortico-collicular organization is to use cortical circuits to perform complex computations and distill the result to variables that can be easily converted into actions—here, the shelter direction continuously mapped already in egocentric coordinates. This could potentially decrease the time to execute the accurate action, which in the case of escaping from imminent threat is of great survival value. The model that emerges from our results may therefore represent a generic brain strategy for using cortical output to generate fast and accurate goal-directed actions. 

## **Online content** 

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-022-05553-9. 

1. Domenici, P., Blagburn, J. M. & Bacon, J. P. Animal escapology I: Theoretical issues and emerging trends in escape trajectories. _J. Exp. Biol._ **214** , 2463–2473 (2011). 

2. Vale, R., Evans, D. A. & Branco, T. Rapid spatial learning controls instinctive defensive behavior in mice. _Curr. Biol._ **27** , 1342–1349 (2017). 

3. Branco, T. & Redgrave, P. The neural basis of escape behavior in vertebrates. _Annu. Rev. Neurosci._ **43** , 417–439 (2020). 

4. Tovote, P., Fadok, J. P. & Lüthi, A. Neuronal circuits for fear and anxiety. _Nat. Rev. Neurosci._ **16** , 317–331 (2015). 

5. van der Meer, M. A. A., Richmond, Z., Braga, R. M., Wood, E. R. & Dudchenko, P. A. Evidence for the use of an internal sense of direction in homing. _Behav. Neurosci._ **124** , 164–169 (2010). 

6. Hartley, T., Lever, C., Burgess, N. & O’Keefe, J. Space in the brain: how the hippocampal formation supports spatial cognition. _Phil. Trans. R. Soc. B_ **369** , 20120510 (2014). 

7. Taube, J. S. The head direction signal: origins and sensory-motor integration. _Annu. Rev. Neurosci._ **30** , 181–207 (2007). 

8. Laurens, J. & Angelaki, D. E. The brain compass: a perspective on how self-motion updates the head direction cell attractor. _Neuron_ **97** , 275–289 (2018). 

9. Rowland, D. C., Roudi, Y., Moser, M.-B. & Moser, E. I. Ten years of grid cells. _Annu. Rev. Neurosci._ **39** , 19–40 (2016). 

10. Evans, D. A. et al. A synaptic threshold mechanism for computing escape decisions. _Nature_ **558** , 590–594 (2018). 

11. Mitchell, A. S., Czajkowski, R., Zhang, N., Jeffery, K. & Nelson, A. J. D. Retrosplenial cortex and its role in spatial cognition. _Brain Neurosci. Adv._ **2** , 239821281875709 (2018). 

12. Miller, A. M. P., Mau, W. & Smith, D. M. Retrosplenial cortical representations of space and future goal locations develop with learning. _Curr. Biol._ **29** , 2083–2090.e4 (2019). 

13. Sparks, D. L. & Jay, M. F. The functional organization of the primate superior colliculus: A motor perspective. _Progr. Brain Res._ **64** , 235–241 (1986). 

14. Masullo, L. et al. Genetically defined functional modules for spatial orienting in the mouse superior colliculus. _Curr. Biol._ **29** , 2892–2904.e8 (2019). 

15. Sahibzada, N., Dean, P. & Redgrave, P. Movements resembling orientation or avoidance elicited by electrical stimulation of the superior colliculus in rats. _J. Neurosci._ **6** , 723–733 (1986). 

16. Benavidez, N. L. et al. The mouse cortico-tectal projectome. Preprint at _bioRxiv_ https:// doi.org/10.1101/2020.03.24.006775 (2020). 

17. García Del Caño, G., Gerrikagoitia, I. & Martínez‐Millán, L. Morphology and topographical organization of the retrospleniocollicular connection: a pathway to relay contextual information from the environment to the superior colliculus. _J. Comp. Neurol._ **425** , 393–408 (2000). 

18. Basso, M. A. & May, P. J. Circuits for action and cognition: a view from the superior colliculus. _Annu. Rev. Vis. Sci._ **3** , 197–226 (2017). 

19. Maguire, E. A. The retrosplenial contribution to human navigation: A review of lesion and neuroimaging findings. _Scand. J. Psychol._ **42** , 225–238 (2001). 

20. Jay, M. F. & Sparks, D. L. Sensorimotor integration in the primate superior colliculus. II. Coordinates of auditory signals. _J. Neurophysiol._ **57** , 35–55 (1987). 

21. Laurens, J. et al. Multiplexed code of navigation variables in anterior limbic areas. Preprint at _bioRxiv_ https://doi.org/10.1101/684464 (2019). 

22. Wilson, J. J., Alexandre, N., Trentin, C. & Tripodi, M. Three-dimensional representation of motor space in the mouse superior colliculus. _Curr. Biol._ **28** , 1744–1755.e12 (2018). 

23. Vann, S. D. & Aggleton, J. P. Extensive cytotoxic lesions of the rat retrosplenial cortex reveal consistent deficits on tasks that tax allocentric spatial memory. _Behav. Neurosci._ **116** , 85–94 (2002). 

24. Lima, S. Q., Hromádka, T., Znamenskiy, P. & Zador, A. M. PINP: a new method of tagging neuronal populations for identification during in vivo electrophysiological recording. _PLoS ONE_ **4** , e6099 (2009). 

25. Zingg, B. et al. AAV-mediated anterograde transsynaptic tagging: mapping corticocollicular input-defined neural pathways for defense behaviors. _Neuron_ **93** , 33–47 (2017). 

26. Pisokas, I., Heinze, S. & Webb, B. The head direction circuit of two insect species. _eLife_ **9** , e53985 (2020). 

27. Ben-Yishai, R., Bar-Or, R. L. & Sompolinsky, H. Theory of orientation tuning in visual cortex. _Proc. Natl Acad. Sci. USA_ **92** , 3844–3848 (1995). 

28. Zhang, K. Representation of spatial orientation by the intrinsic dynamics of the headdirection cell ensemble: a theory. _J. Neurosci._ **16** , 2112–2126 (1996). 

29. Rodieck, R. W. & Stone, J. Analysis of receptive fields of cat retinal ganglion cells. _J. Neurophysiol._ **28** , 833–849 (1965). 

30. Gutnisky, D. A. et al. Mechanisms underlying a thalamocortical transformation during active tactile sensation. _PLoS Comput. Biol._ **13** , e1005576 (2017). 

31. Li, L. et al. A feedforward inhibitory circuit mediates lateral refinement of sensory representation in upper layer 2/3 of mouse primary auditory cortex. _J. Neurosci._ **34** , 13670–13683 (2014). 

32. Hanes, D. P. & Wurtz, R. H. Interaction of the frontal eye field and superior colliculus for saccade generation. _J. Neurophysiol._ **85** , 804–815 (2001). 

33. Petrucco, L. et al. Neural dynamics and architecture of the heading direction circuit in a vertebrate brain. Preprint at _biorXiv_ https://doi.org/10.1101/2022.04.27.489672 (2022). 

34. Seelig, J. D. & Jayaraman, V. Neural dynamics for landmark orientation and angular path integration. _Nature_ **521** , 186–191 (2015). 

35. Sarel, A., Finkelstein, A., Las, L. & Ulanovsky, N. Vectorial representation of spatial goals in the hippocampus of bats. _Science_ **355** , 176–180 (2017). _(1979)_ . 

36. Wang, C., Chen, X. & Knierim, J. J. Egocentric and allocentric representations of space in the rodent brain. _Curr. Opin. Neurobiol._ **60** , 12–20 (2020). 

37. Alexander, A. S. et al. Egocentric boundary vector tuning of the retrosplenial cortex. _Sci. Adv._ **6** , eaaz2322 (2020). 

38. Jacob, P. Y. et al. An independent, landmark-dominated head-direction signal in dysgranular retrosplenial cortex. _Nat. Neurosci._ **20** , 173–175 (2017). 

39. Vedder, L. C., Miller, A. M. P., Harrison, M. B. & Smith, D. M. Retrosplenial cortical neurons encode navigational cues, trajectories and reward locations during goal directed navigation. _Cerebr. Cortex_ **27** , 3713–3723 (2017). 

40. Keshavarzi, S. et al. Multisensory coding of angular head velocity in the retrosplenial cortex. _Neuron_ **110** , 532–543.e9 (2022). 

41. Burgess, N. Spatial cognition and the brain. _Ann. NY Acad. Sci._ https://doi.org/10.1196/ annals.1440.002 (2008). 

42. Alexander, A. S. & Nitz, D. A. Retrosplenial cortex maps the conjunction of internal and external spaces. _Nat. Neurosci._ **18** , 1143–1151 (2015). 

43. Fecteau, J. H. & Munoz, D. Salience, relevance, and firing: a priority map for target selection. _Trends Cogn. Sci._ **10** , 382–390 (2006). 

44. Krauzlis, R. J., Lovejoy, L. P. & Zénon, A. Superior colliculus and visual spatial attention. _Annu. Rev. Neurosci._ **36** , 165–182 (2013). 

45. Duan, C. A., Erlich, J. C. & Brody, C. D. Requirement of prefrontal and midbrain regions for rapid executive control of behavior in the rat. _Neuron_ **86** , 1491–1503 (2015). 

46. Inoue, K. I., Takada, M. & Matsumoto, M. Neuronal and behavioural modulations by pathway-selective optogenetic stimulation of the primate oculomotor system. _Nat. Commun._ **6** , 8378 (2015). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

© The Author(s), under exclusive licence to Springer Nature Limited 2022 

Nature | Vol 613 | 5 January 2023 | **119** 

Article 

## **Methods** 

## **Mice** 

All experiments were performed under the UK Animals (Scientific Procedures) Act of 1986 (PPL 70/7652 and PFE9BCE39) following local ethical approval (Sainsbury Wellcome Centre, University College London). Male adult C57BL/6J wild-type (Charles Rivers, 6–24 weeks old) were used for all behavioural experiments. Mice were single housed after surgery and at least 3 days before starting behavioural protocols. Mice had free access to food and water on a 12:12 h light:dark cycle (ambient temperature 24 °C, humidity 47 relative humidity) and were tested during the light phase (unless stated otherwise). VGluT2::eYFP (resulting from in-house cross of VGluT2-ires-cre with R26-stop-eYFP, Jackson Laboratory Stock 016963 and 006148, respectively) or VGAT::eYFP (resulting from in-house cross of VGAT-cre with R26-stop-eYFP, Jackson Laboratory Stock 016962 and 006148, respectively) mice (5–8 weeks old) were used for ChR2-assisted circuit mapping (CRACM). VGluT2-ires-cre (Jackson Laboratory Stock 016963) or VGAT-cre (Jackson Laboratory Stock 016962) mice (9–20 weeks old) were used for retrograde rabies tracing and dual-opsin-assisted circuit mapping and opto-tagging experiments. 

2 × 10[12] GC ml[−1] ); AAV2/1-Ef1a–fDIO-hChR2(H134R)-EYFP (made in house; 9.2 × 10[14] GC ml[−1] ); AAV2/1-CamKIIa-cre-OFF-GCaMP7f (made in house; 1.0 × 10[14] GC ml[−1] ). 

## **Behavioural procedures** 

**Experimental setup.** All behavioural experiments were performed in an elevated circular Perpex arena (92 cm diameter), located in an opaque, sound-deadening 140 × 140 × 160 cm enclosure[2] . The shelter was an overground red translucent Perspex box (20 × 10 × 10 cm) placed at the edge of the arena, with a 4.2 cm wide entrance facing the centre of the arena. The enclosure held six infrared light-emitting diodes (LED) illuminators (Abus) and experiments were recorded with an overhead near-IR GigE camera (Basler), at 30 or 40 frames per second. Unless stated otherwise, experiments were conducted at a background luminance of 2.7 lux, generated by a projector (BenQ) pointed at a translucent overhead screen (Xerox). Video recording and sensory stimulation (see below) were controlled with custom software written in LabVIEW (2015 64-bit, National Instruments) and Mantis software (mantis64.com). All signals and stimuli, including each camera frame, were triggered and synchronised using hardware-time signals controlled with a PCIe-6351 and USB-6343 board (National Instruments). 

## **Surgical procedures** 

Mice were anaesthetized with an intraperitoneal injection of ketamine (95 mg kg[−1] ) and xylazine (15.2 mg kg[−1] ) or with isoflurane (2.5–5%) and secured on a stereotaxic frame (Kopf Instruments). Isoflurane (0.5–2.5% in oxygen) was used to maintain anaesthesia. Carprofen (5 mg kg[−1] ) was administered subcutaneously for analgesia. Craniotomies were made using a 0.5 mm burr and coordinates were measured from bregma or lambda (see Supplementary Tables 1 and 3 for implant affixation, and 2 for virus injection coordinates). Viral vectors were delivered using pulled glass pipettes (10 μl Wiretrol II pulled with a Sutter-97) and an injection system coupled to a hydraulic micromanipulator (Narishige), at approximately 50 nl min[−1] . Implants were affixed using light-cured dental cement (3M) and the surgical wound was sutured (Vicryl Rapide) or glued (Vetbond). 

## **Viruses** 

The following viruses were used in this study and are referred to by contractions in the text. Chemogenetic projection-specific inhibition experiments: rAAV2-retro-CMV-bGlo-iCre-GFP[47] (made in house; 1.07 × 10[12] genome copies (GC) ml[−1] ) and AAV2-hSyn-DIO-hM4D(G i)-mCherry[48] (Addgene #44362; 4.6 × 10[12] GC ml[−1] ); chemogenetic non-projection-specific inhibition experiments AAV8-hSyn-hM4D (Gi)-mCherry (Addgene #50475; 4.8 × 10[12] GC ml[−1] ). Retrograde rabies tracing[49] : EnvA pseudotyped SAD-B19 rabies virus (SAD-B19[ΔG] -mCherry; made in house; 2 × 10[8] GC ml[−1] ) used in combination with AAV2/1 encoding the EnvA receptor TVA and rabies virus glycoprotein (AAV2/1-Flex-N2cGnucGFP; made in house; 7 × 10[12] GC ml[−1] and AAV2/1-EF1a-Flex-GT-GFP; made in house; 2 × 10[12] GC ml[−1] ); Retrograde rabies tracing for automated cell counting (see ‘Anatomical tracing’): EnvA pseudotyped N2c (N2c[ΔG] -mCherry; made in house; 10[9] GC ml[−1] ) used in combination with a single AAV2/2 helper virus encoding both the EnvA receptor TVA and rabies virus glycoprotein (AAV2/2-EF1a-(ATG-out)Flex-EBFP-T2a-TVA-E2A-N2cG, made in house; 1.13 × 10[13] GC ml[−1] ); ChR2-assisted circuit mapping: AAV2/1-CAG-hCh R2(H134R)-mCherry-WPRE-SV40 (Penn Vector Core; 2 × 10[14] GC ml[−1] ) or AAV2/2-EF1a-DIO-hChR2(H134R)-mCherry (UNC Gene Therapy Vector Core; 5.1 × 10[12] GC ml[−1] ) . Dual-opsin-assisted circuit mapping and opto-tagging in head-fixed and freely moving mice: AAV2/-E F1a-DIO-hChR2(H134R)-EYFP-WPRE-pA (UNC Gene Therapy VectorCore; 4.2 × 10[12] GC ml[−1] ); AAV2/-Syn-ChrimsonR-tdT[50] (Addgene plasmid 59171, 1.3 × 10[13] GC ml[−1] ). Dual-opsin-assisted circuit mapping and opto-tagging in brain slices: AAV2/-Syn-ChrimsonR-tdT (Addgene plasmid 59171, 1.3 × 10[13] GC ml[−1] ); AAV2/1-CAG-Flex-FlpO (made in house; 

**Sensory stimuli. Escape behaviour assay.** The stimulus was a frequency-modulated auditory upsweep[51] from 17 to 20 kHz over 2 s. In a small fraction of experiments, additional stimuli were used to minimize habituation of escape responses. Waveform files were created in MATLAB (Mathworks), and the sound was generated in LabVIEW, amplified and delivered via an ultrasound speaker (Pettersson) positioned 50 cm above the arena centre. Sound pressure level at the arena floor was 73–82 dB. Food-seeking assay: same as above, but the stimulus was a 7-s tone at a frequency of 5 kHz. Orientation to sound assay: the stimulus was a 300-ms tone at a frequency of 2.5 kHz. Sound pressure measured at the centre of the arena was 75–80 dB. 

**Behavioural protocols. Escape behaviour assay.** The procedure was conducted as described[2] . Before the experiment, bedding from the animal’s home cage was placed inside the shelter. After a 7 min habituation period, during which the mouse had to enter the shelter at least once, sound stimuli were delivered. During a single session, multiple stimuli were delivered with an inter-stimulus interval of at least 90 s. Typically, half of the trials were presented in the dark (0.01–0.03 lux); escape error was not different between dark and light conditions and therefore the results were pooled ( _P_ > 0.05 for all datasets permutation test). Experiments had a typical duration of 90 min. 

**Orientation to sound assay.** Experiments were conducted in the dark using the same arena as the escape behaviour assay. The stimulus was delivered by one of two speakers at the height of arena floor, 10 cm away from the edge and positioned at diametrically opposite sides. After a 7 min habituation period, 7 stimuli were presented with an inter-stimulus interval of at least 90 s from a randomly selected speaker. Stimuli were typically presented when mice subtended an angle smaller than 120° towards the speaker because sound location in azimuthal plane has been shown to be unreliable above this range[52] . Experiments had a typical duration of 40 min. 

**Food-seeking assay.** Experiments were conducted using the same arena as the escape behaviour assay. Food-restricted mice were trained for 21 days in navigating to a lick port dispensing condensed-milk, upon the presentation of a sound cue signalling reward availability. Reward delivery was triggered by licks. The sound cue was trigger only when the mouse was exploring a specific region of the arena floor (sound trigger area, Fig. 3e). The lick port was positioned opposite from the trigger area, in a shallow hole near the edge of the arena, which the 

mouse could access via a step. During training, the temporal duration of the sound cue and the trigger zone were progressively decreased. On the experiment day, reward was available during the presentation of the 7 s long sound cue, which was automatically triggered with a probability of 0.75, after the mouse entered the trigger zone. Reward remained accessible for 2 s after stimulus offset. Licking was detected as previously described[53] . 

**Analysis.** Behavioural video and tracking data were sorted into peri-stimulus trials and manually annotated. Detection of the stimulus was assessed as previously described[10] . Escape behaviour assay: onset of escape was determined by visual inspection of the video recordings and considered as either the onset of a head-rotation movement or an acceleration (whichever occurred first) after the mouse detected the stimulus[10] . Flight termination was defined as the first time the mouse stopped outside the shelter, re-oriented or arrived to shelter, after having initiated an escape. Escape error was computed as the shelter direction at the end of the orientation phase of escape (see Fig. 1a for example of an accurate orientation phase where escape error is close to 0°). Shelter direction was measured manually using a custom-designed Python-based graphic interface and varied between 0° (mouse heading perfectly aligned to the centre of the shelter entrance) and ± 180° (positive angles are measured in the clockwise direction from the shelter, negative angles are measured in the anti-clockwise direction). Flight distance was computed as the ratio of the Euclidean distance between the mouse position at escape onset and at the flight termination, over the Euclidean distance between the mouse position at escape onset and the shelter entrance. Food-seeking assay: lick probability was computed as the fraction of trials in which the mouse licked at least once while reward was available. Time to goal is the time it took the mouse to reach the lick port hole, starting from stimulus onset. Orientation to sound assay: orientation error was computed as the head–speaker angle at the end of the first orientation movement after the auditory stimulus presentation. 

## **Pharmacological inactivation** 

Mice were bilaterally implanted with guide and dummy cannulae (Plastics One) over RSP and given at least 96 h for recovery. On experiment day, the animals were infused with 1.0–1.2 μl Muscimol-BODIPY-TMR-X (0.5 mg ml[−1] , ThermoFisher) or vehicle per hemisphere and tested in the escape behaviour assay. Mice were anaesthetized and internal cannulae projecting 0.5 mm below guide cannulae were inserted and sealed with Kwik-Sil. Muscimol or vehicle were then infused at a rate of 150–200 nl min[−1] using a microinjection unit (Hamilton, 10-μl syringe; in Kopf Instruments Model 5000) connected to the internal canulae through tubing (Plastics One) and plastic disposable adapters (Plastics One). Mice were given 35 min to recover before starting the escape behaviour assay. 

To confirm infusion site, immediately upon termination of the behavioural assay, mice were anaesthetized with isoflurane (5%, 2 l min[−1] ) and decapitated. The brain was sectioned coronally (100 μm) with a vibratome (Campden Instruments) in ice-cold PBS (0.1 M), directly transferred to 4% paraformaldehyde (PFA) solution, and kept for 20 min at 4 °C. The slices were then rinsed in PBS, counter-stained with 4′,6-diamidino-2-phenylindole (DAPI; 3 μM in PBS), and mounted on slides in SlowFade Gold (Thermo Fisher) before imaging (Zeiss Axio Imager 2) on the same day. 

## **Chemogenetic inactivation** 

Mice were injected with a retro-AAV (rAAV2-retro-CMV-bGlo-iCre-GFP) into the SC and AAV2/2-hSyn-DIO-hM4D(Gi)-mCherry into the RSP for projection-specific inactivation, or with AAV2/8-hSynhM4D(Gi)-mCherry into the target locations for global inactivation. After at least 4 weeks mice were intraperitoneally injected with CNO (final concentration of 10 mg kg[−1] ; Hellobio CNO freebase) or 

saline, during brief (<2 min) isoflurane anaesthesia (2–4% in oxygen, 1 l min[−1] ). Mice were given 35 min to recover before starting behavioural experiments. Saline and CNO sessions for a given mouse were spaced in time at least 3 days. In a subset of the above mice, cannulae were implanted either in the SC or in the ACC to inactivate specifically the respective RSP projection[48] . Guide and dummy cannulae (Plastics One) were implanted into the target location at least 4 weeks after viral injection, and at least 4 days before behavioural experiments. Cannulae implantation and infusion were performed as described in ‘Pharmacological inactivation’ section. CNO was diluted in buffered saline containing (in mM): 150 NaCl, 10 d-glucose, 10 HEPES, 2.5 KCl, 1 MgCl2 and to a final concentration of 10 μM. A volume of 0.8–1.2 μl CNO was infused. 

## **Anatomical tracing** 

Injections for monosynaptic rabies tracing[49] from unilateral vGluT2[+] or vGAT[+] SC cells were performed with an angled approach to avoid infection of the ipsilateral RSP. In the first surgery, a mix of AAV1-Flex-N2cGnucGFP24 and AAV2/1-EF1a-Flex-GT-GFP25, or AAV2/2-EF1a-(ATG-out) Flex-EBFP-T2a-TVA-E2A-N2cG only, was injected in the left SC (10° ML angle; AP: − 0.40 mm from lambda; ML: −1.00 mm; DV: −1.75 mm; injection volume = 20–25 nl). SAD-B19DG-mCherry rabies virus, or N2c-mcherry, was injected vertically 5 days after the first procedure (same target location; injection volume 25–30 nl). Mice were perfused 10 days after the second procedure. Brains were imaged by serial micro-optical sectioning two-photon tomography[54] (40 μm thick coronal sections; voxel size ML 2 μm, DV 2 μm, AP 5 μm). For cell counting, images were first registered to the Allen Mouse Brain Atlas (Allen Brain Atlas API available from https://brain-map.org/api/index.html). mCherry-expressing and EBFP-expressing cells in SC, AMA, RSP and PPC were automatically counted using the deep learning algorithm CellFinder[55] , manually curated and visualized using brainrender[56] . Starter cells were defined as cells co-expressing helper EBFP and rabies mCherry. Convergence index for a given presynaptic brain region was computed as the ratio between the number of mCherry-labelled cells and the total number of SC starter cells. One sample brain was sectioned using a cryostat (Leica 3050 S) and imaged with an epifluorescence microscope (Zeiss Axio Imager 2) . Images were visualized using ImageJ 1.53q (FIJI). 

## **In vitro whole-cell recordings** 

**Preparation of acute midbrain slices.** For CRACM experiments, male and female VGluT2::EYFP or VGAT::EYFP mice were injected with AAV2/ 1-CAG-hChR2(H134R)-mCherry-WPRE-SV40 in RSP or AAV2/2-EF1a-DIOhChR2(H134R)-mCherry in SC. For dual-opsin-assisted circuit mapping and and opto-tagging experiments, VGAT::cre mice were injected with AAV2/-Syn-ChrimsonR-tdT and AAV2/1-CAG-Flex-FlpO in RSP, and AAV2/1-Ef1a–fDIO-hChR2(H134R)-EYFP and AAV2/1-CamKIIacre-OFF-GCaMP7f in SC. 

After 2 weeks (or 4 weeks for dual-opsin-assisted circuit mapping and opto-tagging experiments) mice were killed by decapitation following isoflurane anaesthesia. Brains were quickly removed and immediately immersed in ice-cold slicing solution containing (in mM): 87 NaCl, 2.5 KCl, 26 NaHCO3, 1.25 NaH2PO4, 10 glucose, 50 sucrose, 0.5 CaCl2, and 3 MgCl2, with an osmolarity of 281-282 mOsm, and constantly bubbled with carbogen (95% O2 and 5% CO2) for a final pH of 7.3. Acute coronal slices of 250 μm thickness were prepared at the level of the SC (−0.8 to 0.2 mm from lambda) using a vibratome (Leica VT1200 S). Slices were collected and transferred to a recovery chamber containing slicing solution and stored under submerged conditions at near-physiological temperature (35 °C) for 30 min, constantly bubbled with carbogen (95% O2 and 5% CO2). Slices were then transferred to a different recovery chamber and submerged in artificial cerebrospinal fluid (aCSF) solution containing (in mM): 125 NaCl, 2.5 KCl, 26 NaHCO3, 1 NaH2PO4, 10 glucose, 2 CaCl2, and 1 MgCl2, 

## Article 

with an osmolarity of 293–298 mOsm and constantly bubbled with carbogen (95% O2 and 5% CO2) for a final pH of 7.3. Slices were further incubated at room temperature (19–23 °C) for at least 30 more minutes prior to electrophysiological recordings. 

**Recording electrodes.** Pipettes were pulled from standard-walled filament-containing borosilicate glass capillaries (Harvard Apparatus, 1.5 mm outer diameter, 0.85 mm internal diameter) using a vertical micropipette puller (PC-10 or PC-100, Narishige) to a final resistance of 4–6 MΩ. Pipettes were backfilled with potassium methane sulfonate based solution containing (in mM): 130 potassium methanesulfonate, 10 KCl, 10 HEPES, 4 NaCl, 4 Mg-ATP, 0.5 Na2-GTP, 5 sodium phosphocreatine, 1 EGTA, biocytin (1 mg ml[−1] ), with an osmolarity of 294 mOsm, filtered (0.22 μm, Millex) and adjusted to pH 7.4 with KOH. 

**Data acquisition.** Whole-cell patch-clamp recordings were performed with an EPC 800 amplifier (HEKA). Data were sampled at 25 kHz, low-pass Bessel filtered at 5 kHz, digitised with 16 bit resolution using a PCIe-6353 board (National Instruments) and recorded in LabVIEW using custom software. For recordings, slices were transferred to a submerged chamber and perfused with aCSF constantly bubbled with carbogen (95% O2 and 5% CO2). The solution was perfused at a flow rate of 2-3 ml min[−1] with a peristaltic pump (PPS2, MultiChannel Systems or Minipuls 3, Gilson) and temperature was kept at 32–34 °C. Cells were visualized with oblique illumination on an upright SliceScope Pro 1000 (Scientifica) using a 60× water-immersion objective (Olympus) or with DIC illumination on an upright SliceScope Pro 6000 (Scientifica) using a 40× water-immersion objective (Olympus). 

For CRACM experiments, expression of ChR2-mCherry was assessed based on fluorescence from mCherry expression using LED illumination (pE-100, CoolLED) at a wavelength of 565 nm. Target cells were identified based on fluorescence from EYFP expression using LED illumination (pE-100, CoolLED) at a wavelength of 490 nm. ChR2 was activated with wide-field 490-nm LED illumination (pE-100, CoolLED) using a train of five 1-ms long pulses at 20 Hz (maximum light intensity = 6 mW). The resting membrane potential was determined immediately after establishing the whole-cell configuration and experiments were continued only if cells had a resting membrane potential more hyperpolarized than −45 mV. For dual-opsin-assisted circuit mapping and opto-tagging experiments, target putative vGluT2[+] cells were identified based on the fluorescence from GCaMP7f expression using 470 nm wide-field LED illumination (pE-800, CoolLED) filtered by a 466/40 nm bandpass filter (FF01-466/40-25, Semrock). ChR2 was activated with wide-field 435-nm LED illumination (pE-800, CoolLED) filtered by a 430/40 nm bandpass filter (86349, Edmund Optics) using a train of five 1-ms long pulses (maximum light intensity = 13.5 mW), that was preceded by a 250 ms long pulse of 635-nm wide-field LED illumination[50] (pE-800, CoolLED) filtered by a 624/40 nm bandpass filter (67035, Edmund Optics), maximum light intensity = 13 mW. ChrimsonR was activated with wide-field 635-nm LED illumination (pE-800, CoolLED) filtered by a 624/40 nm bandpass filter (67035, Edmund Optics) using a train of five 1-ms long pulses (maximum light intensity = 13 mW). 

Input resistance ( _R_ in) and series resistance ( _R_ s) were monitored continuously throughout the experiment, and _R_ s was compensated in current-clamp recordings. Only cells with a stable _R_ s < 40 MΩ were analysed. Upon termination of the recording, the anatomical location of the recorded neuron within the slice was recorded using a 5× objective (Olympus) for future reference. After the experiment, slices were fixed with 4% PFA for 2 h, kept in 4 °C PBS overnight, and imaged using an epifluorescence microscope (Zeiss Axio Imager 2). 

**Analysis.** Analysis was performed in python 3.7. Normalized peak voltages of EPSPs in a train were calculated by dividing the peak amplitude of each evoked EPSP to the first evoked EPSP. Membrane potential values stated in the text are not corrected for liquid junction potentials. 

## **Histological procedures** 

For general histology, mice were anaesthetized with Euthatal (0.15– 0.2 ml) and transcardially perfused with 10 ml of ice-cold PBS with heparin (0.02 mg ml[−1] ) followed by 4% PFA in PBS solution. Brains were post-fixed overnight at 4 °C then transferred to PBS solution. Sections (50 μm) were cut with a cryostat (Leica CM3050S) and stained. Unless otherwise stated, sections were imaged with an epifluorescence microscope (Zeiss Axio Imager using ZEN 3.5 Blue Edition software). Immunohistochemistry was performed to enhance the signal of hM4D-mCherry-expressing RSP neurons. Sections were initially blocked using a 5% normal donkey serum (NDS) in PBS solution. Subsequently, they were incubated overnight at 4 °C with anti-RFP primary antibody (1:1,000, rabbit; 600-401-379, Rockland), followed by a 2-h incubation with Alexa-568 donkey anti-rabbit (1:1,000, Life Technologies). Antibodies were diluted in 0.5% NDS and 0.05% Triton X-100. DAPI was used for counterstaining. Sections were mounted in SlowFade Gold (Thermo Fisher, S36936) onto slides before imaging. 

## **Single-unit recordings in freely moving animals** 

**Data acquisition.** Mice were singly housed after probe implantation in a reversed 12 h light cycle and tested during the dark phase of the day light cycle. A single Neuropixels probe[57] (phase3A, option1, 384 channels) was chronically implanted in the RSP and SC. Before insertion, the probe shank was coated with DiI (1 mM in ethanol, Invitrogen) for track identification (Extended Data Fig. 1a). At the end of the experiment the mouse was perfused and the brain was imaged with an epifluorescence microscope (Zeiss AxioImager 2) or by serial micro-optical sectioning 2-photon tomography to confirm the location of probe implantation (see ‘Anatomical tracing’). For single-unit recording experiments paired with chemogenetic inactivation, probes were implanted in mice previously injected (4 weeks) with viruses as described in ‘Chemogenetic inactivation’. 

Extracellular recordings in freely moving animals were performed in a similar behavioural apparatus as described in ‘Behavioural procedure’, with an overground shelter (20 × 10 × 10 cm; 12 cm wide entrance) positioned by the edge and facing the centre of the platform. Two explicit visual cues were positioned in the environment: a yellow LED, always positioned on the ‘west wall’ of the behavioural cabinet, and an A2 white cardboard sheet, always positioned in the ‘south wall’ of the cabinet, both distal to the arena. A custom-made rotary joint (adapted from Doric AHRJ-OE_PT_AH_12_HDMI) was used to prevent the cables from twisting. Each mouse was tested multiple times with a minimum time interval between consecutive experiments of 3 days. During each session, the mouse explored the shelter in two locations (east pole of the arena: shelter position one; north pole of the arena: shelter position 2) for at least 30 min each. In a fraction of the experiments, after the mouse was tested in the protocol described above, the LED was moved to the east pole of the arena or a closed shelter was introduced at the south pole of the arena and then moved to the east pole. For Neuropixels recording experiments paired with chemogenetic inactivation, the intraperitoneal injection of CNO (or saline) was done during the behavioural experiment, after the mouse explored the shelter in the second position for at least 30 min. The mouse was not removed from the arena and was not anesthetised for the injection. Although the recording was never interrupted, the first 35 min following the injection were excluded from further analysis. Extracellular potentials were recorded with SpikeGLX (Release_ v20170901-phase3A, https://github.com/ billkarsh/SpikeGLX, Janelia Research Campus) and were amplified (500×), high-pass filtered (300 Hz) and sampled at 30 kHz. 

**Analysis.** Data analysis was performed in MATLAB. Spike sorting was done using Janelia Rocket Cluster 3.0[58] or Kilosort 2.0[59] and manually curated. Only units that had an absolute refractory period of at least 

1 ms were included in subsequent analysis. Behavioural variables were extracted from video recordings using DeepLabCut (DLC[60] ; training set 1,000 frames, 1 million training iterations). All timepoints during which the mouse was either inside the shelter or leaning down the behavioural platform where excluded from further analysis. Head-direction and shelter direction were calculated using DLC tracked ear-positions: head-direction was defined as the angle between the direction perpendicular to a line that joins both ears and the horizontal axis; shelter direction was defined as the angle between the same direction as above and a line connecting the centre point between the ears and the shelter entrance (Fig. 1a, Extended Data Fig. 2b and Supplementary Video 3). 

**Criteria for classification of shelter-direction and head-direction cells in single-cell tuning analysis.** We used Rayleigh vector length[61] in head-direction and shelter direction spaces, as previously described in head-direction tuning testing in rodents[62] , to quantify the tuning of each cell to each of these variables. A neuron was considered to be significantly tuned to a variable when the length of its Rayleigh vector exceeded the 95th percentile of the distribution of Rayleigh vectors lengths computed for 1,000 shuffled-datasets, generated by shifting recorded spike trains from all cells coherently by a uniform amount chosen randomly between 1 and 100 s. To ensure the tuning estimation was not influenced by potential behavioural biases, we binned the variable space into 16 bins and sampled them equally. Single units from RSP or SC were classified as shelter-direction cells if all the following criteria were met: (1) for each epoch the neuron has to display a significant shelter direction Rayleigh vector; (2) for each epoch the neuron tuning to shelter direction must de decoupled from tuning to head-direction (using tuning entanglement decoupling (TunED) analysis); (3) shelter direction tuning has to be stable across all epochs (above chance receiver operating characteristic (ROC) decoding[63] along the direction in which Rayleigh vector points during the shelter position 1 epoch, in shelter position 2 epoch); (4) shelter direction tuning must rotate with the shelter (after rotation of the shelter, the tuning to shelter position 2 must not be significantly explained by the tuning to shelter position 1, using TunED analysis). Single units from RSP or SC were classified as head-direction cells if all the following criteria were met: (1) for each epoch (including the no shelter epoch) the neuron had to display a significant head-direction Rayleigh vector; (2) for each epoch the neuron tuning to head-direction had to be decoupled from tuning to shelter direction (using the TunED method); (3) head-direction tuning has to be stable across all epochs (above chance ROC decoding along the direction in which Rayleigh vector points during the first epoch of the experiment, in the subsequent periods). 

**TunED analysis.** To determine whether a neuron that is statistically tuned to two correlated variables is driven by just one of the variables ( _v_ 1 (driver)) while the tuning to the second variable ( _v_ 2 (passenger)) is an artefact of the correlation, we performed tuning entanglement decoupling analysis (TunED). The method takes a list of spike-counts _r_ along with simultaneously measured stimulus variables _v_ 1 and _v_ 2. Let 

**==> picture [33 x 9] intentionally omitted <==**

be the probability that the neuron’s spike count _r_ takes a given value, given a discrete value for the variable _v_ , the tuning curve of the neuron to stimulus variable _v_ (observed tuning to _v_ 1 or _v_ 2, Extended Data Fig. 2a, right, dark yellow and dark blue) is then the conditional mean spike count 

**==> picture [71 x 18] intentionally omitted <==**

To determine whether a neuron is only tuned to the driver variable _v_ 1 or indeed significantly tuned to both _v_ 1 and _v_ 2, the method formulates 

the null hypothesis that the neuron’s activity is purely driven by the _v_ 1. In this case it can be shown that the tuning curve to _v_ 2 ( _μ_ ( _v_ 2); expected tuning of _v_ 2 given tuning to _v_ 1; Extended Data Fig. 2a, right, light yellow and light blue) can be expressed as 

**==> picture [104 x 16] intentionally omitted <==**

Where the suffix NH denotes this is not the actual tuning curve to _v_ 2 but instead it is derived by the above null hypothesis. 

TunED analysis was used to classify cells as head direction or shelter direction cells. Recorded spike and head direction and shelter direction time series were bootstrapped 1,000 times, generating 1,000 observed tuning curves to each variable (Extended Data Fig. 2c, left, dark yellow and dark blue) as well as 1,000 expected tuning curves of the same variable using the null hypothesis equation above (Extended Data Fig. 2c, left, light yellow and light blue). For each variable, the Euclidean distance ( _dHSA_ and _dHD_ ) between the observed ( _OTHSA_ and _OTHD_ ) and the expected ( _ETHSA_ and _ETHD_ ) tuning curves was calculated for each bootstrap iteration (Extended Data Fig. 2c, right, yellow and blue histograms). Finally, we computed the distribution of the differences between each variable _d_ HSA and _d_ HD for each bootstrap iteration (Extended Data Fig. 2c, right, dark grey histograms). If the distribution of _dHSA_ − _dHD_ was significantly smaller than zero (both 2.5th and 97.5th percentile < 0, vertical dotted lines in Extended Data Fig. 2c, right) the cell was considered a head direction cell (Extended Data Fig. 2c, top); if the distribution of _dHSA_ − _dHD_ was significantly larger than zero (both 2.5th and 97.5th percentile > 0) the cell was considered a shelter direction cell (Extended Data Fig. 2c, bottom); otherwise the cell was not considered a shelter direction nor head direction cell. 

**Generalized linear model.** Generalized linear models[64] were used to predict the probability of spiking at certain time _t_ during shelter position 1 and shelter position 2 epochs, given the values of a set of simultaneously recorded variables at time _t_ (head direction, shelter direction, locomotion velocity, head angular velocity, change in head direction within the next 100 ms and 200 ms; see ref.[22] ). For each of these variables we defined a set of equally spaced bins (locomotion speed, 11; head direction, 27; shelter direction, 27; head angular velocity, 23; change in head direction within the next 100ms, 13; change in head direction within the next 200  ms, 13). A time varying binary predictor was then defined for each bin (excluding one) of each variable. At a given _t_ , each binary predictor could be 1, if the value of the respective behavioural variable fell in that bin at _t_ and zero otherwise. The generalized linear model was fitted with the glmfit MATLAB function assuming logistic link function and Bernulli probability distribution. Model prediction accuracy was assessed by performing ten-fold cross-validation and computing Pearson correlation coefficient between predicted and real spike trains (smoothed over 100 ms). The analysis above was also performed after excluding shelter direction from the model. 

**Population decoding analysis.** We employed multiclass LDA[65] to decode shelter direction from spike trains of RSP and SC neural populations, and change in head direction within the next 100 ms from spike trains of SC neural population. Shelter direction was binned into 16 equally populated classes (bin range: −180° to 180°, bin amplitude: 22.5°), and change in head direction into 9 classes (bin range: −27° to 27°, bin amplitude: 6°). Population data was constructed by grouping all recorded neurons and aligning their activity according to the value of shelter direction (or change in head direction) in which it was measured. Both shelter positions 1 and shelter positions 2 epochs were divided into 6 interleaved time periods of equal duration; for each epoch periods 1, 3 and 5 were used to train the classifier, while periods 2, 4 and 6 were used to test its accuracy. Prediction accuracy was computed as the fraction of observations of the testing set classified in the main diagonal of the 

## Article 

classifier confusion matrix and in the adjacent ones (±1), over the total number of observations in the testing set. Predictions accuracy was also compared to the one obtained for a shuffled dataset. 

## **Single-unit recordings paired with chemogenetic loss-offunction analysis** 

**Firing rate change.** The effect of inactivation was assessed separately in RSP and SC neurons. Change in firing rate index (Δ firing rate index) for each neuron in the period before (shelter position 2 epoch) and after the administration of CNO (or saline) was computed as 

**==> picture [246 x 25] intentionally omitted <==**

**Single-cell analysis.** To test for changes in the percentage of neurons classified as shelter-direction neurons we first identified shelter-direction as described above in the periods before and after the injection. 

We then computed 

**==> picture [96 x 24] intentionally omitted <==**

where fraction is the fraction of shelter-direction cells after the injection. 

**Population analysis.** We computed the change in prediction accuracy of multiclass LDA classifiers (see ‘Population decoding analysis’), following injection of CNO or saline in respect to baseline. The period before injection (including shelter positions 1 and 2 epochs) was divided into 12 bins of equal duration. Odd bins were used to train the classifier and even bins used to cross-validate it, producing the baseline prediction accuracy result. The same classifier was used to predict the behavioural variable, given spike trains, after injection of CNO or saline. This was repeated 10 times, by randomly choosing the samples of data for each class. To probe the effect of inactivation of RSP, we tested the statistical significance of the difference between the change the classifier’s prediction accuracy after CNO and after saline injection, using sign rank test. The first 35 min after injection were discarded from these analyses. Single-unit recordings paired with chemogenetic loss-of-function experiments were performed with two mice (see ref.[66] ). The statistical power supporting the conclusion was reached because of the high number of recorded neurons. 

## **Single-unit recordings in head-fixed mice paired with dual-opsinassisted circuit mapping and opto-tagging** 

Neuropixels silicon probes (phase3A, option3, 384 channels) were used to record extracellular spikes from SC neurons of 3 adult VgluT2::cre and 4 adult VGAT::cre mice, previously injected (6–8 weeks) as described in ‘Viruses’. A metal custom-made head-plate and optic fibre (Newdoon, see Supplementary Table 3) were attached to the skull using dental cement. A craniotomy was made over the SC and sealed with Kwik-Cast on the day of the first recording session. During each recording session, mice were placed on a plastic wheel and head fixed. We performed up to four recording sessions per mouse. Before insertion, the probe was coated with one of the four following dyes, to identify and distinguish probe tracks: DiI (1 mM in ethanol, Invitrogen), DiO (1 mM in ethanol, Invitrogen), Vybrant DiD (1 mM in ethanol, Invitrogen), Cellbrite blue (Cytoplasmic Membrane-Labeling Kit, Biotium). Craniotomy and skull surface were submerged with aCSF (see ‘In vitro whole-cell recordings’) and a coated (AgCl) silver wire (0.35 mm diameter, Goodfellow) was held in the aCSF bath for external referencing and grounding. For recording, the probe was slowly inserted into the SC (see Fig. 4a) to a depth of 2.8–3.0 mm and left in place for at least 45 min before the 

beginning of the recording session. Data were acquired as described in ‘Single-unit recordings in freely moving animals’. 

Dual-opsin-assisted circuit mapping and opto-tagging was performed analogously to that described in ‘In vitro whole-cell recordings’ using a Vortran Stradus VersaLase as light source (wavelengths: 472 nm and 639 nm), except that for ChR activation light pulse was 5 ms long (power at fibre tip ~10mW) and for ChrimsonR activation we used a 20 Hz train of 10 ms–long pulses (1 s duration, power at fibre tip ~10 mW). These stimuli were repeated interleaved 50 times with an interstimulus interval of 35 s. A neuron was classified as putative vGluT2[+] or a vGAT[+] if it spiked in at least 75% of the 472nm pulses. Population dynamics shown in Fig. 4b were robust to the additional constraints of the first spike latency having small jitter across trials (IQR 1 ms and 2.5 ms). 

## **Single-unit recordings in freely moving mice paired with dualopsin-assisted circuit mapping and opto-tagging** 

Recordings and analysis in freely moving mice were performed as described in ‘Single-unit recording in freely moving mice’ in 2 adult VgluT2::cre and 2 adult VGAT::cre mice, previously injected (6–8 weeks) as described in ‘Viruses’. An optic fibre (Newdoon, see Supplementary Table 3) were attached to the skull on the same day of the Neuropixels chronic implant. At the end of each recording session, dual-opsin-assisted circuit mapping and opto-tagging was performed as described in ‘Single-unit recordings in head-fixed mice paired with dual-opsinassisted circuit mapping and opto-tagging’. 

## **Spiking recurrent neural network modelling** 

An artificial spiking neural network with biologically constrained synaptic properties and connectivity was used to model the shelter direction RSP to SC circuit neural dynamics. The model was implemented in custom Python code and used the Brian2 neural network simulator package[67] . The simulated network was composed of three distinct populations (representing RSP, SC excitatory and SC inhibitory units) of 512 conductance-based leaky integrate and fire (LIF) neurons adapted from previous models of spiking neural networks with ring-attractor dynamics[68] . The neuronal network model was designed to implement a ring-like-neural network, with neurons in each population numbered (1–512) and ordered such that nearby neurons corresponded to similar angles in the ring[68] . A connectivity kernel was used to determine which neurons in the source population projected to which neurons in the target one and the strength of the connection between each pair ( _w_ ), based on their position in the ring. Two kernel types were used. _Diagonal_ created connections with a kernel shaped as a Gaussian distribution (of standard deviation equal to kernel width; see Supplementary Table 4), such that entries in the main diagonal had the strongest connection, the first super- and sub-diagonals weaker connections etc. with weights approaching zeros for entries further away from the main diagonal. _Inverted diagonal_ was analogous to the diagonal except that synaptic weight was highest for off-diagonal elements and approached zero for elements on the main diagonal with a Gaussian kernel[26] . Within the constraints of the connectivity kernel, synaptic connections between neurons in the three populations were randomly created with a probability _pconnection_ (see below). 

The membrane potential ( _V_ m) dynamics of each neuron was modelled by the following ordinary differential equation: 

**==> picture [143 x 22] intentionally omitted <==**

> where _Ileak_ = _gleak_ × ( _Vm_ − _Eleak_ )[ is the leakage current, ] _[I][spontaneous inputs]_[ is the ] spontaneous synaptic current and _Isynapses_ is the sum of synaptic currents ( _Isynapse_ ) from each presynaptic population: RSP inputs ( _Irsp_ ), excitatory SC inputs ( _Ivglut sc_ ) and inhibitory SC inputs ( _Ivgat sc_ ). 

**==> picture [114 x 12] intentionally omitted <==**

In order to better fit experimental data, each _Isynapse_ was modelled with a slow ( _Islow_ ) and a fast ( _Ifast_ ) component: 

**==> picture [68 x 11] intentionally omitted <==**

For each component, the dynamics in synaptic conductance ( _g_ ) is governed by the time constants _τrise_ and _τdecay_ 

**==> picture [106 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
I = g × ( Vm − Ereversal )<br>τrise<br>dg = ( ττdecayrise ) τdecay − τrise × s − g<br>dt τrise<br>d s − s<br>=<br>dt τdecay<br>**----- End of picture text -----**<br>


Following a presynaptic spike, the value of _s_ at the synapse between the presynaptic neuron _i_ and the postsynaptic neuron _j_ is incremented by _gmax_ ( _i,j_ ). 

**==> picture [87 x 37] intentionally omitted <==**

Such that _g_ at any time _t_ after a presynaptic spike is given by 

**==> picture [161 x 23] intentionally omitted <==**

_P_ models the short-term plasticity dynamics ( _P_ = _u_ × _x_ ), where _x_ is the proportion of available synaptic resources at time of presynaptic spike (initialized to 1) and _u_ the release probability, following the equations described in ref.[69] . _P_ was set to 1 for the slow component, such that only the fast component shows short-term plasticity. The following variables obtained from either our own experimental data (directly or after compartmental modelling in NEURON[70] ) or from published data[10,71] where necessary: synaptic properties – maximum connection probability of the synapse type, slow components[3,64] ; cellular properties: membrane resistance ( _gmax_ , _τrise_[ and ] _[τ][decay]_[ of the fast and ] _g_ leak−1 ) and capacitance ( _C_ m), resting membrane potential, and spike threshold and spike reset potential. 

To mimic the effect of optogenetic stimulation of RSP neurons on neural dynamics in SC, a randomly selected subset of RSP neurons received an external input in the form of a train of positive current. Stimulation patterns were the same as the ones described in ‘Single-unit recordings in head-fixed mice paired with dual-opsin-assisted circuit mapping and opto-tagging’. An exhaustive grid search was used to estimate parameters yielding neural dynamics similar to those measured experimentally. In brief, for each combination of parameters a neural network model was simulated as above and the normalized average activity of vGluT2[+] and vGAT[+] neurons was measured and compared to the experimentally recorded neurons calculating the sum of squared error. To generate shelter direction tuning curves, 10 non-overlapping subgroups of nearby RSP neurons were defined, each spanning a 36° angle. Each RSP subgroup was stimulated individually by increasing the strength of the spontaneous inputs to its neurons for 1 s, and the 

simulated spike trains of SC vGAT[+] and vGluT2[+] neurons were used to compute tuning curves and Rayleigh vectors as described in ‘Single-unit recordings in freely moving animals’. 

## **General data analysis** 

Data analysis was performed using custom-written routines in Python 2.7, or 3.7, and MATLAB (version 2018 and 2020) and custom code will be made available on request. Data are reported as median ± IQR or mean ± s.e.m unless otherwise indicated. Statistical comparisons using the significance tests stated in the main text were made in GraphPad Prism 7, MATLAB, R 3.6 and statistical significance was considered when _P_ < 0.05. Data were tested for normality with the Shapiro–Wilk test, and a parametric tests were used if the data were normally distributed, and a non-parametric otherwise, as detailed in the text next to each comparison. To test whether a population of angular measures was distributed non-uniformly around the circle we used a _v_ -test for non-uniformity of circular data. The _z_ -test for equality of proportion was used to compare proportions. Unless otherwise stated, statistical difference between behavioural metrics in CNO and control experiments was computed using the following permutation test (developed in collaboration with J. Rapela). Two groups of mice M and N, each of numerosity _m_ and _n_ , were tested under a different experimental condition (for example, control or CNO). The test statistic computed is the difference between the mean of all trials pooled in CNO group and the mean of the trials in the control group. For the permutation, at every iteration each mouse is randomly re-assigned to CNO or control group, while keeping the total number of mice per condition the same. The _n_ number in this statistical comparison is therefore the number of mice in each group. The procedure was repeated 100,000 times and the test statistics was computed after each iteration, obtaining the null distribution of the test. The _P_ -value of the test is one minus the percentile of the null distribution corresponding to the value of the test statistic of the non-shuffled data. Source data for brain silhouettes and 3D renderings are from the Allen Mouse Brain Atlas (https://atlas. brain-map.org). 

## **Reporting summary** 

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article. 

## **Data availability** 

The data and code that support the findings of this study are available from the corresponding authors upon request. 

47. Tervo, D. G. R. et al. A designer AAV variant permits efficient retrograde access to projection neurons. _Neuron_ **92** , 372–382 (2016). 

48. Stachniak, T. J., Ghosh, A. & Sternson, S. M. Chemogenetic synaptic silencing of neural circuits localizes a hypothalamus→midbrain pathway for feeding behavior. _Neuron_ **82** , 797–808 (2014). 

49. Wickersham, I. R. et al. Monosynaptic restriction of transsynaptic tracing from single, genetically targeted neurons. _Neuron_ **53** , 639–647 (2007). 

50. Klapoetke, N. C. et al. Independent optical excitation of distinct neural populations. _Nat. Methods_ **11** , 338–346 (2014). 

51. Mongeau, R., Miller, G. A., Chiang, E. & Anderson, D. J. Neural correlates of competing fear behaviors evoked by an innately aversive stimulus. _J. Neurosci._ **23** , 3855–3868 (2003). 

52. Sterbing, S. J., Hartung, K. & Hoffmann, K. P. Representation of sound source direction in the superior colliculus of the guinea pig in a virtual auditory environment. _Exp. Brain Res._ **142** , 570–577 (2002). 

53. Campagner, D. et al. Prediction of choice from competing mechanosensory and choice-memory cues during active tactile decision making. _J. Neurosci._ **39** , 3921–3933 (2019). 

54. Ragan, T. et al. Serial two-photon tomography for automated ex vivo mouse brain imaging. _Nat. Methods_ **9** , 255–258 (2012). 

55. Tyson, A. L. et al. A deep learning algorithm for 3D cell detection in whole mouse brain image datasets. _PLoS Comput. Biol._ **17** , e1009074 (2021). 

56. Claudi, F. et al. Visualizing anatomically registered data with brainrender. _eLife_ **10** , e65751 (2021). 

57. Jun, J. J. et al. Fully integrated silicon probes for high-density recording of neural activity. _Nature_ **551** , 232–236 (2017). 

## Article 

58. Jun, J. J. et al. Real-time spike sorting platform for high-density extracellular probes with ground-truth validation and drift correction. Preprint at _bioRxiv_ https://doi.org/10.1101/ 101030 (2017). 

59. Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M. & Harris, K. D. Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels. Preprint at _bioRxiv_ https://doi.org/10.1101/061481 (2016). 

60. Mathis, A. et al. DeepLabCut: markerless pose estimation of user-defined body parts with deep learning. _Nat. Neurosci._ **21** , 1281–1289 (2018). 

61. Batschelet, E. _Circular Statistics in Biology_ (Academic Press, 1981). 

62. Taube, J. S., Muller, R. U. & Ranck, J. B. Head-direction cells recorded from the postsubiculum in freely moving rats. I. Description and quantitative analysis. _J. Neurosci._ **10** , 420–435 (1990). 

63. Gu, Y., Fetsch, C. R., Adeyemo, B., DeAngelis, G. C. & Angelaki, D. E. Decoding of MSTd population activity accounts for variations in the precision of heading perception. _Neuron_ **66** , 596–609 (2010). 

64. Campagner, D., Evans, M. H., Bale, M. R., Erskine, A. & Petersen, R. S. Prediction of primary somatosensory neuron activity during active tactile exploration. _eLife_ **5** , e10696 (2016). 

65. Nicolelis, M. A. L. et al. Simultaneous encoding of tactile information by three primate cortical areas. _Nat. Neurosci._ **1** , 621–630 (1998). 

66. Laurens, J. The statistical power of three monkeys. Preprint at _bioRxiv_ https://doi.org/ 10.1101/2022.05.10.491373 (2022). 

67. Stimberg, M., Brette, R. & Goodman, D. F. Brian 2, an intuitive and efficient neural simulator. _eLife_ **8** , e47314 (2019). 

68. Compte, A. Synaptic mechanisms and network dynamics underlying spatial working memory in a cortical network model. _Cerebr. Cortex_ **10** , 910–923 (2000). 

69. Tsodyks, M. V. & Markram, H. The neural code between neocortical pyramidal neurons depends on neurotransmitter release probability. _Proc. Natl Acad. Sci. USA_ **94** , 719–723 (1997). 

70. Hines, M. L. & Carnevale, N. T. Neuron: a tool for neuroscientists. _Neuroscientist_ **7** , 123–135 (2001). 

71. Zhu, J. J. & Lo, F. Recurrent inhibitory circuitry in the deep layers of the rabbit superior colliculus. _J. Physiol._ **523** , 731–740 (2000). 

**Acknowledgements** This work was funded by a Wellcome Senior Research Fellowship (214352/Z/18/Z), by the Sainsbury Wellcome Centre Core Grant from the Gatsby Charitable Foundation and Wellcome (GAT3755 and 219627/Z/19/Z) and by a European Research Council grant (Consolidator no. 864912) (T.B.), MRC PhD Studentship (R.V.), Boehringer Ingelheim Fonds PhD fellowship (R.V.), Gatsby Unit/SWC Joint Research Fellowship in Neuroscience (D.C.), UCL Wellcome 4-year PhD Programme in Neuroscience (O.P.A.), A*STAR National Science Scholarship (PhD) (Y.L.T.), the SWC PhD Programme (Y.L.T.), Weizmann UK Making Connections Grant (R.S.P.) and BBSRC grant BB/V009680/1 (R.S.P.). We thank members of the Branco laboratory and T. Mrsic-Flogel for discussions; J. Rapela and P. Shamash for advice on statistical analysis; A. Murray, I. Duguid, C. Schmidt-Hieber, N. Burgess, M. Tripodi and the I. Bianco laboratory for comments on the manuscript; M. Strom, T. Okbinoglu, R. Campbell, the SWC Neurobiological Research Facility and FabLabs for technical support; K. Betsios for programming the data acquisition software; T. R. Stones for inspiration; and G. T. Gray for viral constructs. Source of mouse silhouettes: https://scidraw.io/. 

**Author contributions** D.C. and R.V.: behavioural experiments. D.C., F.C. and Y. L.T.: theoretical modelling. D.C.: single-unit recordings. O.P.A., A.V.S. and Y.L.T.: in vitro electrophysiology. D.C., P. I., S.K. and R.V.: surgeries. D.C., O.P.A., R.S.P., Y.L.T. and R.V. data analysis. D.C., P. I., Y.L.T. and R.V.: histological preparations and imaging. T.B., D.C., Y.L.T. and R.V.: experimental design. T.B. and R.V. conceived the project. T.B. wrote the manuscript, with critical input from D.C., T.W.M., Y.L.T. and R.V. 

**Competing interests** The authors declare no competing interests. 

## **Additional information** 

**Supplementary information** The online version contains supplementary material available at https://doi.org/10.1038/s41586-022-05553-9. 

**Correspondence and requests for materials** should be addressed to Tiago Branco. **Peer review information** _Nature_ thanks Ivan de Araujo, Marisela Morales and Larry Zweifel for their contribution to the peer review of this work. 

**Reprints and permissions information** is available at http://www.nature.com/reprints. 

**==> picture [347 x 544] intentionally omitted <==**

**Extended Data Fig. 1 | Single unit recordings of shelter-direction and headdirection cells.** ( **A** ) Left: Coronal image of post-recording histology showing the track of the neuropixels probe (red). Right: 3D rendering of probe tracks in all chronically implanted mice ( **B** ) Example tuning curves for a shelter-direction neuron in the RSP before and after shelter rotation. ( **C** ) Tuning curves for nonoverlapping subsets of data generated by random sampling. For RSP and SC, the plot on the left is sorted by tuning peak, and the sorting indexes have been 

used to sort the plot on the right. ( **D** ) Summary plot of preferred tuning angle for RSP and SC shelter-direction neurons. ( **E** ) Example tuning curves for allocentric head-direction neurons in the SC and RSP. We recorded 2% headdirection cells in the SC, and 6% in the RSP. ( **F** ) Summary plot showing the occupancy of the arena during exploratory behaviour in the presence of a second, closed shelter. 

## Article 

**==> picture [335 x 598] intentionally omitted <==**

**Extended Data Fig. 2 |** See next page for caption. 

**Extended Data Fig. 2 | Tuning entanglement decoupling analysis.** ( **A** ) Left, plot illustrating a driver variable ( _v1_ ) and a correlated passenger variable ( _v2_ ; Pearson’s correlation coefficient = 0.45). _v1_ samples are drawn from a normal distribution of mean 0 and standard deviation 1. The _j[th]_ sample of _v2_ is computed as _v2, j_ = _0.5_ × _v1,j_ + _ε_ j, where each _εj_ is drawn from a second normal distribution with mean 0 and standard deviation 1. Right, _v1_ is used to simulate the spiking of a neuron such that the probability of firing is equal to _0.1_ × _v1_ if _v1_ > 1 and 0 if _v1_ ≤ 1. TunED analysis was then applied to _v1_ , _v2_ and simulated spiking data as described in Methods to compute observed and expected tuning curves to _v1_ and _v2_ . The method correctly identifies _v1_ as the driver variable. The observed tuning curve to the passenger variable _v2_ (dark yellow) can be fully explained by the tuning to the driver variable (brown). In contrast, the observed tuning to driver variable (dark blue), cannot be explained by the tuning to the passenger variable (light blue). ( **B** ) Left, schematic of head–shelter angle and head direction 

variables during the experiment. Right, correlation between head–shelter angle and head direction in our experimental setting plotted for eight values of head direction for each grid location. ( **C** ) Left, tuning curves of neurons for which the driver variable was head direction (top) or head–shelter angle (bottom). Right, illustration of the statistical method used to determine whether the driver variable of the neuron was head shelter offset, head direction or none of them (see Methods for details). Briefly, the distribution of _dHSA_ - _dHD_ (dark grey histogram) indicates whether the expected and observed tuning curves are more similar for head–shelter angle or for head direction. If the _dHSA_ - _dHD_ distribution is significantly smaller than zero (both 2.5[th] and 97.5[th] percentile <0, vertical dotted lines) the cell is classified as a head direction cell; if the distribution of _dHSA_ - _dHD_ is significantly larger than zero (both 2.5[th] and 97.5[th] percentile > 0) the cell is classified as a head-shelter angle cell; otherwise the cell is not considered a shelter-direction nor head direction cell. 

## Article 

**==> picture [353 x 275] intentionally omitted <==**

**Extended Data Fig. 3 | Histology for loss-of-function of SC-projecting RSP neurons.** 3D rendering of the location of SC-projecting RSP neurons expressing hM4Di for the mice in the following datasets: escape behaviour 

assay, orientation to sound assay, food-seeking assay, single unit recordings during chemogenetic inactivation. For an example coronal section see Fig. 2a. 

**==> picture [198 x 83] intentionally omitted <==**

**Extended Data Fig. 4 | RSP loss-of-function does not affect average SC firing rates.** (A) Population histograms for firing rate of SC single units after saline and CNO i.p. injection in animals expressing hM4Di in SC-projecting RSP neurons (P = 0.75 one-tailed Kolmogorov-Smirnov test; N = 264 units, 2 mice). 

## Article 

**==> picture [139 x 170] intentionally omitted <==**

**Extended Data Fig. 5 | Shelter orientation error does not depend on the environment luminance level.** Shelter orientation error increases both during light and dark conditions upon inactivation of SC-projecting RSP neurons, in comparison to saline control (Dark: P = 0.0302 permutation test; saline: 5 mice, 24 trials; CNO: 11 mice, 58 trials. Light: P = 0.038 permutation test; saline: 6 mice, 27 trials; CNO: 9 mice, 47 trials). No significant differences were observed between saline in light and dark condition (P = 0.46 permutation test) or CNO in light and dark condition (P = 0.26 permutation test). 

**==> picture [503 x 528] intentionally omitted <==**

**Extended Data Fig. 6 | Additional analysis of the effect of RSP-SC loss-offunction on behaviour.** ( **A** – **F** ) Navigation during exploratory behaviour is not affected by inactivation of SC-projecting RSP neurons. Panels show quantification of exploratory behaviour during the time period preceding the presentation of the first threatening stimulus for saline control (black, N = 6) and CNO (blue, N = 11) mice, expressing hM4Di in SC-projecting RSP neurons. None of the metrics differs between the two groups (P > 0.15 for all metrics, 2-tailed Mann-Whitney test). ( **A** ) Latency between the beginning of the experiment and the first time the mouse entered the shelter. ( **B** ) Number of times the mouse entered the shelter. ( **C** ) Percentage of time the mouse spent outside the shelter. ( **D** ) Total length of the path travelled while outside the shelter. ( **E** ) Percentage of the arena surface explored while outside the shelter. 

( **F** ) Average and 95th percentile of mouse locomotion speed while outside the shelter. The duration of the time period preceding the presentation of the first threatening stimulus did not differ between saline control and CNO groups (P = 0.51, 2 tailed Mann-Whitney test). ( **G** ) Average change in speed after threat presentation for saline control (black) and CNO (blue) showing that both groups of mice initiate escape with similar vigour. ( **H** ) Summary data for time to reach the shelter after escape initiation. ( **I** ) Length of flight after escape initiation as a function of orientation error, showing that larger errors are associated with shorter flights. (Fitted function: Boltzmann sigmoidal equation; slope −5.5, P = 0.02; F-statistic goodness of fit test against constant model, P < 0.0001). Shaded area: 95% confidence interval. Distance is normalized to the distance to shelter at escape onset. 

Article 

**==> picture [417 x 557] intentionally omitted <==**

**Extended Data Fig. 7 | Histology for cortical loss-of-function.** Coronal sections and 3D renderings showing neurons targeted with hM4Di expression in the entire RSP ( **A** ), posterior parietal cortex ( **B** ) and anterior motor areas ( **C** ). 

**D** shows fluorescently-labelled muscimol targeted to the RSP. White circles represent infusion cannulae location. 

**==> picture [511 x 126] intentionally omitted <==**

**Extended Data Fig. 8 | Additional cortical inputs onto SC neurons.** Coronal images of monosynaptic rabies tracing from starter SC cells in excitatory (vGluT2[+] ) and inhibitory (vGAT[+] ) neuron populations, showing prominent inputs from the posterior parietal cortex ( **A** ), M2 ( **B** ) and anterior cingulate cortex ( **C** ). 

## Article 

**==> picture [396 x 277] intentionally omitted <==**

**Extended Data Fig. 9 | Histology for projection-specific RSP-SC loss-offunction.** Coronal sections and 3D renderings showing guides and internal cannulae locations (white dotted lines and white circles) implanted in the superior colliculus (SC; A) and anterior cingulate cortex (ACC; B). Insets and 

blue shades in the right panels show SC-projecting RSP neurons of the respective mouse, expressing hM4Di. Inset in B (top-right) shows the axon collaterals to ACC of SC-projecting RSP neurons. 

**==> picture [407 x 401] intentionally omitted <==**

**Extended Data Fig. 10 | Quantification of head-displacement prediction and orientation to sound performance.** ( **A** ) Cross validated confusion matrix for LDA population decoding of the angle of future head displacement (100 ms ahead) from SC firing rates (prediction accuracy: 0.78). ( **B** ) Summary data showing that mice orient accurately to sound (with no biases for left nor right speaker neither for left nor right turns; P = 0.27 and P = 0.33 respectively, 

_permutation test_ ; N = 36, 6 mice), with short latencies ( **C** , left) and fast movements ( **C** , right). ( **D** ) Summary data showing that mice are equally accurate when orienting to sound or to shelter (P = 0.82 _permutation test_ ; orientation to sound N = 36, 6 mice; orientation to shelter N = 32, 5 mice). ( **E** ) Orientation to sound accuracy does not depend on the distance at sound onset between the mouse and the speaker (slope = −0.012, P = 0.48, _linear regression_ ). 

## Article 

**==> picture [161 x 155] intentionally omitted <==**

**Extended Data Fig. 11 | Principal components of SC population dynamics during RSP activation.** Principal component 1 and 2 of SC vGAT[+] and SC vGluT2[+] neurons during cortical activation (same data as Fig. 4b). The first two principal components are sufficient to explain most of the variance present in the data (84%) and closely resemble the temporal dynamics observed for SC vGAT[+] and SC VGluT2[+] neurons. 

**==> picture [323 x 137] intentionally omitted <==**

**Extended Data Fig. 12 | Biophysical properties of SC neurons receiving RSP input.** ( **A** ) Summary curves for action potential firing from somatic current injection. ( **B** ) Summary data for short-term plasticity of RSP inputs onto SC neurons. 

## Article 

**==> picture [493 x 537] intentionally omitted <==**

**Extended Data Fig. 13 | Elements of the lateral feedforward inhibition and ring attractor models.** ( **A** ) Real and simulated synaptic currents or potentials for all synaptic connections in the model. ( **B** ) Additional circuit elements of the feedforward lateral inhibition model (c.f. Fig. 5d). ( **C** ) Left: Circuit elements of 

the standard ring attractor model. Right: predicted firing rate of vGluT2+ and vGAT+ SC populations following 20 Hz activation of RSP neurons in the model, compared to observed dynamics (dashed lines, see also in Fig. 4b). 

**==> picture [281 x 273] intentionally omitted <==**

**Extended Data Fig. 14 | 3D reconstruction of viral injection and fiber placement of dual-opsin-assisted circuit mapping and optotagging.** 3D rendering of the location of ChrimsonR-expressing neurons in the entire 

RSP (blue), ChR2-expressing SC vGluT2[+] and vGAT[+] neurons (yellow), and optic fibers (white cylinders) used in the freely moving and head-fixed dual-opsin and optotagging experiments. For an example coronal section see Fig. 4a. 

**==> picture [228 x 36] intentionally omitted <==**

**==> picture [365 x 47] intentionally omitted <==**

**==> picture [519 x 365] intentionally omitted <==**

**==> picture [76 x 71] intentionally omitted <==**

**==> picture [171 x 133] intentionally omitted <==**

**==> picture [191 x 52] intentionally omitted <==**

**==> picture [384 x 152] intentionally omitted <==**

**==> picture [463 x 167] intentionally omitted <==**

**==> picture [569 x 792] intentionally omitted <==**

