Article 

## Widespread coding of navigational variables in prefrontal cortex 

## Highlights 

- d Prefrontal regions encode navigational variables 

- d Neurons encoding navigational variables exhibit random, mixed selectivity 

- d Strength of navigational encoding increases along a ventralto-dorsal gradient 

## Authors 

David J.-N. Maisson, Roberto Lopez Cervera, Benjamin Voloh, Indirah Conover, Mrunal Zambre, Jan Zimmermann, Benjamin Y. Hayden 

Correspondence benhayden@gmail.com 

## In brief 

Maisson et al. show that prefrontal brain areas in freely moving rhesus macaques encode navigational variables with random, mixed selectivity. The strength of encoding increases along a ventral-todorsal gradient. 

**==> picture [17 x 17] intentionally omitted <==**

Maisson et al., 2023, Current Biology 33, 3478–3488 August 21, 2023 ª 2023 Elsevier Inc. https://doi.org/10.1016/j.cub.2023.07.024 

**ll** 

**ll** 

## Article 

## Widespread coding of navigational variables in prefrontal cortex 

David J.-N. Maisson,[1][,][2] Roberto Lopez Cervera,[1][,][2] Benjamin Voloh,[1] Indirah Conover,[1] Mrunal Zambre,[1] Jan Zimmermann,[1][,][3][,][4] and Benjamin Y. Hayden[1][,][3][,][4][,][5][,] * 

1Department of Neuroscience, Center for Magnetic Resonance Research, Center for Neuroengineering, Department of Biomedical Engineering, University of Minnesota, Minneapolis, MN 55455, USA 

2These authors contributed equally 

3These authors contributed equally 

4Senior author 

5Lead contact *Correspondence: benhayden@gmail.com https://doi.org/10.1016/j.cub.2023.07.024 

## SUMMARY 

To navigate effectively, we must represent information about our location in the environment. Traditional research highlights the role of the hippocampal complex in this process. Spurred by recent research highlighting the widespread cortical encoding of cognitive and motor variables previously thought to have localized function, we hypothesized that navigational variables would be likewise encoded widely, especially in the prefrontal cortex, which is associated with volitional behavior. We recorded neural activity from six prefrontal regions while macaques performed a foraging task in an open enclosure. In all regions, we found strong encoding of allocentric position, allocentric head direction, boundary distance, and linear and angular velocity. These encodings were not accounted for by distance, time to reward, or motor factors. The strength of coding of all variables increased along a ventral-to-dorsal gradient. Together, these results argue that encoding of navigational variables is not localized to the hippocampus and support the hypothesis that navigation is continuous with other forms of flexible cognition in the service of action. 

## INTRODUCTION 

To move in the world, organisms must represent where they are, where they are going, and where important features in the world are. In other words, they must navigate. The majority of research highlights the role of the hippocampus and adjacent structures in navigation.[1–6] This work supports a modular view of navigation— that is, that navigation results from computations in anatomically circumscribed circuits.[7][,][8] An alternative view is that navigation relies on a suite of more general cognitive abilities, including generalized mapping functions, such as the encoding of task structure and latent environmental variables. 

The modular approach to understanding functional neuroanatomy has been challenged by a growing set of studies that highlight the broad distribution of variables. These include motor signals[9–12] and reward signals.[13–15] Such findings raise the possibility that navigation may also be distributed.[16–19] Thus, evidence of widespread distribution of navigational codes would support their posited role in anchoring elements of cognition to maps of embodied space. In this view, navigation is a special case of the more general problem of representing conceptual linkages.[5–7][,][20][,][21] 

A growing body of research suggests that, at least in rodents, navigational functions exist outside the hippocampal complex, including within prefrontal areas.[22][,][23] For example, neurons in somatosensory cortex, orbitofrontal cortex (OFC), and piriform cortex encode current and future spatial positions, as well as 

the location of targets in the environment.[24–27] However, the distinct navigational strategies and preferred sensory modalities in rodents may not generalize to primates. Moreover, the extent to which rodent prefrontal areas serve as functional homologies to those of primates remains unclear.[28] 

Theories about the function of the prefrontal cortex (PFC) seldom involve a navigational role. Instead, they typically involve functionsthatindirectlysupportnavigation,including control ofaction, planning, resolving conflict, and comparing values.[17][,][18][,][29][,][30] Often, however, these areas support more abstract mapping functions that augment space by anchoring to it an executive-controltype function. For example, the roles for space typically assigned to the PFC include the encoding of goal location, navigational action planning and landmark vector representations, and spatial working memory.[19][,][20][,][31–34] Yet, the direct involvement of PFC in navigational encoding remains unclear. 

We developed a novel naturalistic paradigm for recording neural and behavioral data from freely navigating macaques.[35] As macaques performed a freely moving foraging task, we recorded neuronal activity in six regions: OFC, dorsal anterior cingulate cortex (dACC), supplementary motor area (SMA), ventrolateral PFC (vlPFC), dorsolateral PFC (dlPFC), and dorsal premotor cortex (PMd). In all six, we found selectivity for navigational variables: allocentric position, allocentric head orientation, egocentric boundary distance, angular velocity, and linear velocity. Notably, this navigational tuning is not place-cell-like. Instead, it has a more unstructured pattern, even as it contains 

**==> picture [16 x 17] intentionally omitted <==**

3478 Current Biology 33, 3478–3488, August 21, 2023 ª 2023 Elsevier Inc. 

**ll** 

## Article 

navigational information. Proportions of neurons responding were roughly the same as those encoding non-navigational variables, such as reward number and feeder identity. Neurons encoding navigational variables did not form functionally specialized subpopulations and these encodings were not accounted for by distance, time to reward, or motor factors. Finally, we found that distributed encoding of both navigational and nonnavigational task variables followed functional gradients in which stronger coding was found in more dorsal areas. Together these results support the idea that navigational functions are supported by widespread activity of neurons, including those in several prefrontal structures. 

## RESULTS 

## Behavioral and neural recordings 

Rhesus macaques performed a novel freely moving foraging task in a large (245 cm 3 245 cm 3 275 cm) enclosure with four barrels and up to four reward stations (Figures 1A and 1B; STAR Methods). If the subject approached a station (or ‘‘patch’’) and pressed the lever, a juice tube provided preferred liquid reward (1.5 mL) and the display changed from blue to white with a green cross (Figure 1C). After 2 s, the screen returned to blue and the subject could repeat the process. After the fifth lever press, the patch deactivated for 3 min. We used OpenMonkeyStudio[35] to track subjects in space. We recorded neural activity from 128 independently moveable electrodes (Figure 1D; STAR Methods). We recorded 8,276 neurons over 196 sessions from six structures in the PFC (Figure 1E). 

## Activity of prefrontal neurons can be fitted by a linearnonlinear encoding model 

We used a linear-nonlinear Poisson-distributed generalized additivemodel (LN-GAM)toestimate tuningfunctions for 8 distinct variables developed by Hardcastle et al.[36] and used by Laurens etal.,[37] Vinepinskyetal.,[38] Mao etal.,[39] and Yoo etal.,[40][,][41] :(1)lever pressing (versus not pressing, equivalent to reward); (2) position of thebodyonthegroundplane;(3)headelevation;(4)compass-wise head direction; (5) head tilt; (6) distance to enclosure boundaries; (7) angular velocity (speed of change in subjects’ compass-wise orientation); and (8) linear velocity ofthe subject’s body. These variables were used in previous studies of navigational tuning in the macaque hippocampus and were defined the same way.[37][,][39] Note that this procedure includes a cross-validation procedure that controls for false positives by dividing each session into 10 partitions and performing 5-fold cross-validation within each partition. To characterize the encoding of basic navigational variables, we considered the prevalence of tuning to each variable in turn across neurons in each structure (see Figure S1 and Table S1 for a summary). 

## Neurons in all six regions encode position 

To quantify occupancy, we segmented the surface area of the arena into 36–50 cm[2] bins. During each session, we computed the amount of time when head position was within each bin (Figure 2A). Subjects visited the full range of the arena height, though they tended to favor an elevation between 100 and 200 cm. 

We defined tuning to 3D position as the simultaneous selectivity to the head’s 2D position (x and y axes) (Figure 1A) and 

elevation (z axis).[39] Neurons in all six regions encode 3D position. For example, neuron OFC.143 showed increased firing when the subject entered the northeast corner (Figure 2B); neuron dACC.70 showed increased firing when the subject entered the southeast corner (Figure 2C). Responses of six neurons are shown in Figures 2B–2G and S2. 

Spatial selectivity is common in all regions recorded. In OFC, 42.87% of neurons showed selectivity to position (Y: 50.13%; W: 39.59%). Overall, 21.35% (n = 259/1,213) carry information about 3D position (p < 0.0001, binomial test). This pattern was observed in both subjects (subjects Y and W) individually (Y: 24.93%; W: 19.74%). An additional 9.65% of OFC neurons were tuned to 2D position, but not to head elevation (Y: 12.22%; W: 8.49%; p < 0.0001); 11.87% of OFC neurons were tuned to head elevation only (Y: 12.99%; W: 11.36%). Indeed, a statistically significant proportion of neurons showed selectivity for 3D position in all regions (Figure 2H). Note that in reporting the percent of neurons modulated by this variable, we do not mean to imply that this is the only variable that the neurons encode. Indeed, we later show that this is not true. To confirm tuning stability, we computed the correlation between encoding magnitudes for each neuron during the first and second halves of the session. We found high correlations in all six structures (OFC: r = 0.903; dACC: r = 0.865; SMA: r = 0.504; vlPFC: r = 0.757; dlPFC: r = 0.608; PMd: r = 0.563; p < 0.0001 in all cases). 

## Neurons in all six regions encode allocentric head direction 

Head direction tuning has been observed in hippocampal formation and associated thalamic nuclei, including in macaques.[39][,][42][,][43] To confirm that subjects’ head positions varied, we segmented the allocentric yaw angles into 6[�] bins (n = 60 bins, from 0[�] to 360[�] , 0[�] representing east). For each bin, during each session, we computed the amount of time during which head direction (yaw) was within each bin (Figure 3A). We did the same with pitch. Subjects favored (an average of 63.61% ± 0.59% of the session) angles between 72[�] and 132[�] (Figure 3A). Subjects overwhelmingly favored (an average of 69.51% ± 0.09% of the session) orienting their heads at an angle between 60[�] and 120[�] (Figure 3A). We found that individual neurons in the PFC encode head direction. For example, neuron OFC.276 showed increased firing rates for northeast head direction (Figure 3B). Responses of six example neurons are shown in Figures 3D–3G. 

Head direction selectivity was common. In OFC, 43.53% of neurons showed selectivity to 3D orientation (Y: 47.48%; W: 41.75%). Overall, 21.12% (n = 256/1,213) carry information about 3D orientation (p < 0.0001; Y: 26.52%; W: 18.66%); 11.05% of OFC neurons were tuned to head direction but not to head tilt (Y: 9.55%; W: 11.72%) and 11.38% were tuned to head tilt (Y: 11.41%; W: 11.36%). We found similar results across all five other structures (Figure 3H). To confirm stability, we computed correlation between encoding magnitudes during the first and second halves of the session. We found positive correlations in all structures (OFC: r = 0.922; dACC: r = 0.846; SMA: r = 0.504; vlPFC: r = 0.774; dlPFC: r = 0.624; PMd: r = 0.548; p < 0.0001 in all cases). These findings suggest that allocentric head direction is encoded in all six prefrontal regions and this encoding is stable within sessions. 

**==> picture [46 x 35] intentionally omitted <==**

Current Biology 33, 3478–3488, August 21, 2023 3479 

**ll** 

Article 

**==> picture [418 x 549] intentionally omitted <==**

Figure 1. Behavior and neural recordings (A) Schematic of the arena. Checkerboard patterns indicate floor. Black rectangles denote cameras. Blue rectangles indicate the approximate locations of the feeding stations. The lower panel shows a cartoon depiction of the feeding station, with the display monitor at the center showing solid blue. (B) Photograph of the arena. 

- (C) Schematic of the available, novel freely moving foraging task. 

- (D) 3D model of the recording system superimposed on a subject’s cranium. 

- (E) 3D rendering of the prefrontal areas from which neural data were recorded. Bars: number of neurons recorded from each region. 

3480 Current Biology 33, 3478–3488, August 21, 2023 

**ll** 

Article 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [418 x 510] intentionally omitted <==**

Figure 2. Allocentric position encoding (A) Occupancy heat maps depicting the average proportion of time spent in each 50 cm[2] bin across sessions. X: E-W axis of the arena; Y: N-S axis. Color: proportion of the session time in each bin; left: rectangular screens represent the approximate location of each patch feeder and white asterisks denote which ones were on top of barrels. Right, occupancy plot for elevation axis. (B–G) Rate maps of a sample neuron from each structure that was determined to be significantly tuned to 3D allocentric position (2D position and tracked height, simultaneously). Color: neural activity, computed as the occupancy-normalized firing rate (spikes/s); size, occupancy, computed as the time spent (s) in a bin. (H) The proportion of total recorded neurons in each structure (collapsed across subjects) tuned to 3D position (XYZ), 2D position (XY only), tracked height (Z only), single selectivity to 2D position alone, and single selectivity to height alone. Red line: chance. Bars indicate SEM. See also Figure S2. 

Current Biology 33, 3478–3488, August 21, 2023 3481 

Article 

## **ll** 

**==> picture [418 x 481] intentionally omitted <==**

Figure 3. Allocentric head orientation coding in volumetric space 

(A) Occupancy histograms depicting the distribution across sessions of the proportion of the total orientations recorded. R, proportion orientation bins occupied at least once during a session; theta: orientation. 

(B–G) Polar rate maps of a sample neuron with significant tuning. R, occupancy-normalized firing rate (spikes/s). 

(H) Proportion of total recorded neurons in each structure (collapsed across subjects) tuned to 3D orientation (Y, yaw; P, pitch; and R, roll), head direction (yaw only), head tilt (pitch and roll), single selectivity to head direction, and single selectivity to head tilt. Red line: chance. 

## Encoding of boundary distance, linear velocity, and angular velocity 

We found neural encoding of egocentric boundary distance, linear velocity, and angular velocity in all six regions[39] (Figure 4). Egocentric boundary distance is a subject’s current distance to the nearest boundary of the environment.[39] A significant proportion of neurons in all six regions show this encoding (Figures 4C, 

4D, and 5A); tuning in the first and second halves of the session were correlated (OFC: r = 0.94; dACC: r = 0.93; SMA: r = 0.73; vlPFC: r = 0.86; dlPFC: r = 0.78; PMd: r = 0.74; p < 0.0001 in all cases). 

Linear velocity is the derivative of position (converted to cm/s). Significant portions of neurons encoded linear velocity in all areas (Figures 4E and 5A); first/second half coding was 

3482 Current Biology 33, 3478–3488, August 21, 2023 

Article 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [490 x 372] intentionally omitted <==**

Figure 4. Example tuning curves for neurons encoding angular velocity, egocentric boundary distance, and linear velocity (A and B) The within-session distribution of angular velocities (A) and the corresponding rate maps of a sample neuron from each brain area with significant tuning (B). (C and D) The within-session distribution of egocentric boundary distance (C) and the corresponding rate maps of a sample neuron with significant tuning (D). (E) The tuning curve of a sample neuron with significant tuning to linear velocity. See also Figure S3. 

correlated (OFC: r = 0.865; dACC: r = 0.865; SMA: r = 0.518; vlPFC: r = 0.757; dlPFC: r = 0.624; PMd: r = 0.548; p < 0.0001 in all cases). 

We defined angular velocity as the change in orientation along yaw and pitch angles. We found a significant encoding proportion in all structures (p < 0.0001 in all cases) (Figures 4A, 4B, and 5A), and positive first/second half correlations (OFC: r = 0.884; dACC: r = 0.865; SMA: r = 0.518; vlPFC: r = 0.774; dlPFC: r = 0.608; PMd: r = 0.563; p < 0.0001 in all cases). Figure S3 offers a visualization of the overlap between encoding of different navigational variables across all brain areas. 

## Relationship between encoding of navigational variables and task variables 

Neurons in the PFC carry information related to key behavioral variables, such as reward and choice.[44–46] We wondered how robust encoding of navigational variables relates to the more 

familiar non-navigational task-variable encoding methodology. We computed neural encoding for five task variables: (1) lever pressing (versus not pressing—note that this is confounded with reward receipt); (2) number of rewards remaining throughout the environment; (3) number of rewards remaining at the current patch; (4) stay/leave choice after the previous trial; and (5) the predicted probability of stay/leave at each press given the number of presses remaining through the environment. 

We found in OFC that 21.19% (n = 257/1,213 neurons) showed selectivity to lever pressing. This proportion is significantly greater than chance (p < 0.0001, binomial test). We found similar and significant proportions in both subjects individually (Y: 22.55%, W: 20.69%). These proportions are roughly in line with the proportion observed in this region in other tasks.[47] We found similar results in all structures (Figure 5B; Tables S2 and S3). 

To measure variables 2–5, we segmented each lever press into individual trials, computed the average firing rates for each 

Current Biology 33, 3478–3488, August 21, 2023 3483 

Article 

## **ll** 

**==> picture [239 x 268] intentionally omitted <==**

Figure 5. Prefrontal encoding of other navigational and non-navigational variables (A) A summary of the proportion of total recorded neurons tuned to egocentric boundary distance, angular velocity, and linear velocity collapsed across subjects. 

(B) The proportion of neurons significantly tuned to task-related variables. Each bar indicates the proportion of tuned neurons in one of the six structures. Red lines in (A) and (B) show chance levels for ɑ = 0.05. nSMA = 280, nPMd = 2,017, ndlPFC = 1,591, nvlPFC = 1,756, ndACC = 1,419, nOFC = 1,213. See also Tables S2 and S3. 

neuron per lever press and regressed the averages on the four other task variables (comparable with the approach expected from a chaired-task paradigm). We found that a significant proportion of neurons in each region encoded the number of rewards remaining across the environment (Figure 5B). We found similar results for stay/leave choice (Figure 5B). 

To measure the probability of leaving a given patch, we fitted a sigmoid function to choice by regressing the total number of presses remaining across all patches in the environment against the stay/leave decision (see STAR Methods). We then used the fitted function to estimate the probability of staying/leaving, based on the total number of presses available in the arena. We found a significant proportion of neurons encoded the probability of leaving the current patch, controlling for the rewards remaining at the current patch (Figure 5B). 

Finally, we found that a significant proportion of neurons encoded the probability of leaving the current patch, while controlling for the number of rewards remaining at the current patch in OFC, dACC, vlPFC, and dlPFC (Figure 5B). The proportion of neurons encoding the number of remaining rewards at the current patch failed to reach significance in the SMA (6.64%, p = 0.07, binomial test) and PMd (5.33%, p = 0.25, binomial test). 

## Variable encoding is distributed randomly among neurons within structures 

To determine whether navigational and task variables are encoded in distinct subpopulations, we used elliptical projection angle index of response similarity (ePAIRS).[48] We used the LNGAM-generated variable weights to calculate estimated marginal means (EMMs), reduced the dimensionality, and computed a cluster index (Cidx) from the 10 best explanatory principal components (see STAR Methods and Raposo et al.[49] ). The cluster index uses the angles between neural response vectors to compute similarities in tuning properties, so neurons that respond along the same dimensions will be categorized as more similar (even if their tuning curves are different) than neurons that respond along orthogonal dimensions. Given perfect clustering (Cidx = 1), the angle of each point is identical to its nearest neighbors. Conversely, given a perfectly random distribution of variables, Cidx = 0. A Cidx < 0 would indicate a smoother distribution in variable encoding than would be generated by the data-derived null distribution.[49] We found significantly negative ePAIRS score in all structures (Figure 6A). This result provides evidence against the hypothesis that neurons are clustered into functional subtypes. 

One advantage of multiplexing is that it allows the same population of neurons to meet distinct behavioral demands, while continuing to support simple linear combinations for downstream decoding.[49][,][50] In one study, the authors demonstrated that, despite the category-free coding they observed in the posterior parietal cortex, it was possible to nonetheless perform a linear readout of firing to estimate task variables, demonstrating that category-free coding does not result in a sacrifice in fidelity.[49] To confirm that the same applies to our own data, we performed the same control analysis described in that study. To do so, we asked whether we could use a linear decoder to accurately predict the position of the animal, based on the firing rates across the population (see STAR Methods). We segmented the arena into 9 zones, so chance-level decoding accuracy was 11.11% (i.e., 1/9). We compared the decoding accuracy from population activity in each structure with chance (correcting for multiple comparisons, a = 0.0083). Position was decodable from population neural activity in all structures (Figure 6B). These analyses were confirmed for both subjects individually (data not shown). 

## Coding of all measured variables grows along a ventralto-dorsal gradient 

We previously found a ventral-to-dorsal gradient in encoding of economic variables along the medial wall of the PFC.[46] We asked if a similar gradient is observed for navigational variables. We identified two distinct potential ventral-to-dorsal anatomical gradients in our data: a medial (OFC / dACC / SMA / PMd) and a lateral series (OFC / vlPFC / dlPFC / PMd). We found that position encoding increases along both gradients. Formally, the regression weight of response strength, computed for each neuron, increased with structure’s hierarchical position (medial: Spearman r[2] = 0.067; lateral: r[2] = 0.051; p < 0.0001 in both cases). We observed the same pattern using depth of electrode instead of brain areas (Figure 7, medial: Pearson r[2] = 0.055; lateral: r[2] = 0.065; p < 0.0001 in both cases). 

We found a similar gradient for head direction with brain area (medial: r[2] = 0.099; lateral: r[2] = 0.078; p < 0.0001) and with 

3484 Current Biology 33, 3478–3488, August 21, 2023 

## **ll** 

## Article 

Figure 6. Prefrontal encoding of navigational and task variables is distributed randomly among regional neurons (A) Weights for the first and second principal components from both subjects combined, which was produced by reducing the dimensionality of the LN-GAM-derived navigational variable encoding. The roughly uniform circular distributions indicate a lack of encoding-based clustering in N-dimensional principal component space. The inlaid score indicated the clustering index from the ePAIRS analysis and an asterisk denotes significance at p < 0.05. 

**==> picture [322 x 230] intentionally omitted <==**

(B) Accuracy of a linear decoder, a regressionbased support-vector machine, in using population neural activity to decode the 2D position of the subject. Each bar indicates the accuracy for decoding subject position based on neural activity in each structure. Gray: shuffled values. Bars: standard error across bootstrapped iterations. Red line, chance. 

electrode depth (medial: r[2] = 0.081; lateral: r[2] = 0.095; p < 0.0001). We found similar results for egocentric boundary distance (medial: r[2] = 0.125; lateral: r[2] = 0.099; p < 0.0001) and electrode depth (medial series: r[2] = 0.098; lateral: r[2] = 0.076; p < 0.0001). Likewise for angular velocity (medial: r[2] = 0.125; lateral: r[2] = 0.099; p < 0.0001) and electrode depth (medial: r[2] = 0.098; lateral: r[2] = 0.076; p < 0.0001); likewise for linear velocity (medial: r[2] = 0.118; lateral: r[2] = 0.099; p < 0.0001) and electrode depth (medial: r[2] = 0.097; lateral: r[2] = 0.071; p < 0.0001). 

be inevitable that information like this is observed broadly. Unfortunately, we cannot ascertain whether these navigational variables are either endogenously or exogenously generated (or some combination). However, we do not believe it is logically necessary that the information will be observed everywhere. There are plentiful examples of cases in which information is generated in one region, but not shared in others. As such, it seems unlikely that different parts of the PFC achieve a balance of encoding due to sharing of information. Having said that, we must also be careful about functional interpretations—the fact that we observe widespread correlates of navigational information in these regions does not prove they play a causal role in navigation. 

We found similar patterns for our non-navigational variables. Encoding of stay/leave choice probability significantly increased along both gradients (medial: r[2] = 0.071; lateral: r[2] = 0.069; p < 0.0001). Unsigned weight of reward encoding, from the LN-GAM, increased along both (medial: r[2] = 0.081; lateral: r[2] = 0.067; p < 0.0001). These patterns were significant with electrode depth (p < 0.0001 in all cases). These results extend our previous findings of a ventral-to-dorsal gradient of encoding for economic variables to navigational variables. 

Several reports in rodents have identified encoding of navigational variables beyond the hippocampal complex.[24–27] Likewise, a small literature in humans emphasizes the potential roles of nonhippocampal regions, especially prefrontal ones, in navigation.[22] Our report adds to this literature. Some of these results have proposed that navigational information outside of the hippocampus may play a distinct role, such as linking space to value or changing plans; however, existing data are also consistent with the hypothesis that hippocampal and prefrontal regions play largely overlapping roles. Our results imply that navigational information can be found in the PFC, just as it can be found in the hippocampal complex. It is worth emphasizing that the tuning for place that we find is not place-cell-like. In particular, it is not generally localized to a single position in space, nor does it have other hallmarks of place cells. On the other hand, it does clearly contain information about place, and it does resemble responses of nongrid cells in medial entorhinal cortex. It is likely, in our view, that these differences reflect differences in the way space is encoded in prefrontal regions and in hippocampus. It is worth noting, however, that the spread-out responses we observe do qualitatively resemble those measured in two recent studies of primate hippocampus,[39][,][52] suggestingthatthedifferencemaybe,atleastinpart,aspeciesdifference, rather than a purely real one. 

## DISCUSSION 

In freely moving macaques, single neurons in six prefrontal areas encode several navigational variables. Navigational and nonnavigational variables are encoded in the same set of neurons, using mixed selectivity.[49–51] The widespread encoding of navigational variables outside of the hippocampus suggests that processing of navigational information may not be localized. These results tie into emerging theories that see navigation as a special case of associative mapping.[5–7][,][20][,][21] Indeed navigational information may be found in prefrontal regions because of their more general role as flexible encoders of associative information. 

It is not clear whether these signals are generated within the regions we recorded, or whether they are generated elsewhere. Given the broad interconnections with prefrontal regions, it may 

**==> picture [46 x 35] intentionally omitted <==**

Current Biology 33, 3478–3488, August 21, 2023 3485 

Article 

## **ll** 

**==> picture [239 x 181] intentionally omitted <==**

Figure 7. Ventral-dorsal gradient of navigational tuning Average encoding strength as a function of electrode position for both subjects combined. Bubbles correspond to position bins. Color, strength of encoding. Size, number of neurons in bin. 

We observe no evidence for separate populations encoding navigational and non-navigational information. These results are important because they indicate that navigational encoding is not part of specialized patches or neural subregions, nor of distinct neurons that were inaccessible in prior studies. This result is consistent with the growing body of research indicating that mixed selectivity is widespread and robust.[49][,][51][,][53] This mixed selectivity may allow for flexible yet robust coding and may allow for rapid recombination of information.[50] 

The ventral-to-dorsal gradient in coding strength we report here resembles one we have found for the medial wall.[46] Why would we see stronger encoding more dorsally? We propose that information encoded in a format that is more accessible to the motor system (and likewise to our decoding analyses) in more ventral structures. In other words, more dorsal structures show information in a more untangled manner.[54] Conversely, these data argue against a functionally modular arrangement, in which each area has a specific nameable function, such as ‘‘evaluate,’’ ‘‘compare,’’ and ‘‘control.’’ At the same time, these data argue against a purely distributed view, in which all information is present in the same form across the PFC. Instead, they support a hierarchical view.[17][,][18][,][45][,][55–57] 

One interesting feature of our data is that firing rates are much lower than those typically observed in standard primate physiology experiments, and lower than those often reported in rodent studies of the navigational system. We suspect that the discrepancy is likely to reflect genuine differences in how neurons fire and differences in firing rate for neurons selected online and offline. Specifically, we have noticed that as we move toward more naturalistic tasks, firing rates tend to decrease. Indeed, in our informal observations of these same subjects performing chaired tasks with the same recording system, firing rates are lower in our open-field paradigm. Moreover, we believe that when selecting neurons for recording, physiologists (including ourselves) tend to select higher tonically active neurons, simply because these are the ones we are more likely to notice. It 

remains an open question which of these two factors is more important, and whether other factors contribute as well. 

One limitation of the present study is that we did not measure gaze direction. As such, we could not perform a disambiguation between tuning to facing location (where in the room the subject’s head is facing) and spatial view (where in the room the subject’s eyes are looking). In a recent, important paper, Mao et al.[39] characterized navigational tuning in the hippocampus of freely moving primates. They showed the results of both a traditional tuning curve and the LN-GAM approach used here. The traditional tuning curve approach, using a single fitted variable at a time, yielded tuned proportions analogous to those commonly reported in the rodent hippocampus. Critically, however, the LN-GAM approach included a variable for ‘‘facing location’’ and ‘‘spatial view’’ within the large, simultaneously fitted model. They demonstrated that hippocampal tuning was predominantly driven by facing location rather than spatial view, which underscores the importance of performing this disambiguation (see also Killian et al.[58] and Jacobs et al.[59] ). In future studies we hope to investigate the relationship between facing location and spatial view. 

Another limitation is that we could not include 4 of the 5 nonnavigational variables in the LN-GAM (rewards remaining at the current patch, rewards remaining in the environment, stay/leave choice, and stay/leave probability); therefore, we could not perform any direct analyses to relate navigational encoding to the broader non-navigational encoding strengths beyond the one included in the LN-GAM (lever pressing). One further limitation is that the lack of a rigid trial structure restricted our ability to compare navigational variable encoding when subjects were task-engaged versus not engaged. We conservatively defined a trial as the 2-s epoch after a lever press, a period in which subjects exhibited limited range of motion and which was highly confounded with reward receipt. 

Ultimately, we believe that these results provide a strong argument for the use of naturalistic tasks. It is well known that natural behavior is continuous, complex (multieffector), embedded (in an environment), and seldom isolated from other competing demands on attention and planning.[60–65] Nonetheless, most laboratory tasks, including the great bulk of our own past work, does not hew to these principles. Instead, they use overly simplified laboratory tasks. Simple laboratory tasks have great benefits, especially in tractability, but they have disadvantages. One is that they often do not manipulate variables that may, if manipulated, be found to be major drivers of neural activity. Ignoring that tuning may in turn obscure the broader and more general functions of neurons in regions of interest. 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d RESOURCE AVAILABILITY 

   - B Lead contact 

   - B Materials availability 

   - B Data and code availability 

- d EXPERIMENTAL MODEL AND SUBJECT DETAILS 

3486 Current Biology 33, 3478–3488, August 21, 2023 

**ll** 

## Article 

   - B Animal model 

- d METHOD DETAILS 

   - B Surgical procedures 

   - B Recording sites 

   - B Behavioral task 

- d QUANTIFICATION AND STATISTICAL ANALYSIS 

   - B Behavioral analysis 

   - B Linear-Nonlinear Poisson-distributed Generalized Additive Model 

   - B Stay/leave choice probability and neural encoding 

   - B Distribution of variable encoding 

   - B Linear decoder 

## SUPPLEMENTAL INFORMATION 

Supplemental information can be found online at https://doi.org/10.1016/j. cub.2023.07.024. 

## ACKNOWLEDGMENTS 

We thank the Hayden/Zimmermann lab for valuable discussions as well as Brenna Knaebe for help with animal care and preparation. This work was supported by NIH grants R01 MH128177 (J.Z.), P30 DA048742 (J.Z. and B.Y.H.), R01 MH125377 (B.Y.H.), T32 GM008244 (R.L.C.), T32 MH115886 (R.L.C. and D.J.-N.M.), T32 NS105604 (R.L.C. and D.J.-N.M.), NSF 2024581 (J.Z. and B.Y.H.), and MH125377 and a UMN AIRP award (J.Z. and B.Y.H.) from the Digital Technologies Initiative (J.Z.), from the Minnesota Institute of Robotics (J.Z.). 

## AUTHOR CONTRIBUTIONS 

Formal analysis, D.J.-N.M. and R.L.C.; investigation, D.J.-N.M., R.L.C., B.V., I.C., and M.Z.; data curation, D.J.-N.M., R.L.C., and B.V.; writing, D.J.-N.M. and R.L.C.; supervision, J.Z. and B.Y.H. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

Received: January 9, 2023 Revised: June 1, 2023 Accepted: July 13, 2023 Published: August 3, 2023 

## REFERENCES 

1. Hartley, T., Lever, C., Burgess, N., and O’Keefe, J. (2014). Space in the brain: how the hippocampal formation supports spatial cognition. Philos. Trans. R. Soc. Lond. B Biol. Sci. 369, 20120510. 

2. Rolls, E.T., and Wirth, S. (2018). Spatial representations in the primate hippocampus, and their functions in memory and navigation. Prog. Neurobiol. 171, 90–113. 

3. Moser, E.I., Kropff, E., and Moser, M.B. (2008). Place cells, grid cells, and the brain’s spatial representation system. Annu. Rev. Neurosci. 31, 69–89. 

4. McNaughton, B.L., Battaglia, F.P., Jensen, O., Moser, E.I., and Moser, M.B. (2006). Path integration and the neural basis of the ‘cognitive map’. Nat. Rev. Neurosci. 7, 663–678. 

5. Stachenfeld, K.L., Botvinick, M.M., and Gershman, S.J. (2017). The hippocampus as a predictive map. Nat. Neurosci. 20, 1643–1653. 

6. Schuck, N.W., and Niv, Y. (2019). Sequential replay of nonspatial task states in the human hippocampus. Science 364, eaaw5181. 

7. Epstein, R.A., Patai, E.Z., Julian, J.B., and Spiers, H.J. (2017). The cognitive map in humans: spatial navigation and beyond. Nat. Neurosci. 20, 11. 

8. Poulter, S., Hartley, T., and Lever, C. (2018). The neurobiology of mammalian navigation. Curr. Biol. 28, R1023–R1042. 

9. Musall, S., Kaufman, M.T., Juavinett, A.L., Gluf, S., and Churchland, A.K. (2019a). Single-trial neural dynamics are dominated by richly varied movements. Nat. Neurosci. 22, 10. 

10. Musall, S., Urai, A.E., Sussillo, D., and Churchland, A.K. (2019b). Harnessing behavioral diversity to understand neural computations for cognition. Curr. Opin. Neurobiol. 58, 229–238. 

11. Stringer, C., Pachitariu, M., Steinmetz, N., Reddy, C.B., Carandini, M., and Harris, K.D. (2019). Spontaneous behaviors drive multidimensional, brainwide activity. Science 364, 255. 

12. Steinmetz, N.A., Zatka-Haas, P., Carandini, M., and Harris, K.D. (2019). Distributed coding of choice, action and engagement across the mouse brain. Nature 576, 7786. 

13. Vickery, T.J., Chun, M.M., and Lee, D. (2011). Ubiquity and specificity of reinforcement signals throughout the human brain. Neuron 72, 166–177. 

14. Shin, E.J., Jang, Y., Kim, S., Kim, H., Cai, X., Lee, H., Sul, J.H., Lee, S.-H., Chung, Y., Lee, D., et al. (2021). Robust and distributed neural representation of action values. eLife 10, e53045. 

15. Ottenheimer, D.J., Hjort, M.M., Bowen, A.J., Steinmetz, N.A., and Stuber, G.D. (2022). A stable, distributed code for cue value in mouse cortex during reward learning. eLife 12, RP84604. 

16. Fine, J.M., and Hayden, B.Y. (2022). The whole prefrontal cortex is premotor cortex. Philos. Trans. R. Soc. Lond. B Biol. Sci. 377, 20200524. 

17. Fuster, J.M. (2000). Executive frontal functions. Exp. Brain Res. 133, 66–70. 

18. Fuster, J.M. (2001). The prefrontal cortex—an update: time is of the essence. Neuron 30, 319–333. 

19. Yoo, S.B.M., Sleezer, B.J., and Hayden, B.Y. (2018). Robust encoding of spatial information in orbitofrontal cortex and striatum. J. Cogn. Neurosci. 30, 898–913. 

20. Behrens, T.E.J., Muller, T.H., Whittington, J.C.R., Mark, S., Baram, A.B., Stachenfeld, K.L., and Kurth-Nelson, Z. (2018). What is a cognitive map? Organizing knowledge for flexible behavior. Neuron 100, 490–509. 

21. Whittington, J.C.R., Muller, T.H., Mark, S., Chen, G., Barry, C., Burgess, N., and Behrens, T.E.J. (2020). The Tolman-Eichenbaum machine: unifying space and relational memory through generalization in the hippocampal formation. Cell 183, 1249–1263.e23. 

22. Patai, E.Z., and Spiers, H.J. (2021). The versatile wayfinder: prefrontal contributions to spatial navigation. Trends Cogn. Sci. 25, 520–533. 

23. Maisson, D.J.-N., Wikenheiser, A., Noel, J.-P.G., and Keinath, A.T. (2022). Making sense of the multiplicity and dynamics of navigational codes in the brain. J. Neurosci. 42, 8450–8459. 

24. Basu, R., Gebauer, R., Herfurth, T., Kolb, S., Golipour, Z., Tchumatchenko, T., and Ito, H.T. (2021). The orbitofrontal cortex maps future navigational goals. Nature 599, 449–452. 

25. Long, X., and Zhang, S.-J. (2021). A novel somatosensory spatial navigation system outside the hippocampal formation. Cell Res. 31, 6. 

26. Poo, C., Agarwal, G., Bonacchi, N., and Mainen, Z.F. (2022). Spatial maps in piriform cortex during olfactory navigation. Nature 601, 7894. 

27. Wikenheiser, A.M., Gardner, M.P.H., Mueller, L.E., and Schoenbaum, G. (2021). Spatial representations in rat orbitofrontal cortex. J. Neurosci. 41, 6933–6945. 

28. Heilbronner, S.R., Rodriguez-Romaguera, J., Quirk, G.J., Groenewegen, H.J., and Haber, S.N. (2016). Circuit-based corticostriatal homologies between rat and primate. Biol. Psychiatry 80, 509–521. 

29. Miller, E.K., and Cohen, J.D. (2001). An integrative theory of prefrontal cortex function. Annu. Rev. Neurosci. 24, 167–202. 

30. Knight, R.T., and Stuss, D.T. (2002). Prefrontal cortex: the present and the future. Princ. Frontal Lobe Funct. 573–597. 

31. Martinet, L.-E., Sheynikhovich, D., Benchenane, K., and Arleo, A. (2011). Spatial learning and action planning in a prefrontal cortical network model. PLoS Comp. Biol. 7, e1002045. 

**==> picture [46 x 35] intentionally omitted <==**

Current Biology 33, 3478–3488, August 21, 2023 3487 

Article 

## **ll** 

32. Strait, C.E., Sleezer, B.J., Blanchard, T.C., Azab, H., Castagno, M.D., and Hayden, B.Y. (2016). Neuronal selectivity for spatial positions of offers and choices in five reward regions. J. Neurophysiol. 115, 1098–1111. 

33. Bicanski, A., and Burgess, N. (2020). Neuronal vector coding in spatial cognition. Nat. Rev. Neurosci. 21, 453–470. 

34. Ikkai, A., and Curtis, C.E. (2011). Common neural mechanisms supporting spatial working memory, attention and motor intention. Neuropsychologia 49, 1428–1434. 

35. Bala, P.C., Eisenreich, B.R., Yoo, S.B.M., Hayden, B.Y., Park, H.S., and Zimmermann, J. (2020). Automated markerless pose estimation in freely moving macaques with OpenMonkeyStudio. Nat. Commun. 11, 4560. 

36. Hardcastle, K., Maheswaranathan, N., Ganguli, S., and Giocomo, L.M. (2017). A multiplexed, heterogeneous, and adaptive code for navigation in medial entorhinal cortex. Neuron 94, 375–387.e7. 

37. Laurens, J., Abrego, A., Cham, H., Popeney, B., Yu, Y., Rotem, N., Aarse, J., Asprodini, E.K., Dickman, J.D., and Angelaki, D.E. (2019). Multiplexed code of navigation variables in anterior limbic areas. https://doi.org/10. 1101/684464. 

38. Vinepinsky, E., Perchik, S., and Segev, R. (2020). A generalized linear model of a navigation network. Front. Neural Circuits 14, 56. 

39. Mao, D., Avila, E., Caziot, B., Laurens, J., Dickman, J.D., and Angelaki, D.E. (2021). Spatial modulation of hippocampal activity in freely moving macaques. Neuron 109, 3521–3534.e6. 

40. Yoo, S.B.M., Tu, J.C., Piantadosi, S.T., and Hayden, B.Y. (2020). The neural basis of predictive pursuit. Nat. Neurosci. 23, 252–259. 

41. Yoo, S.B.M., Tu, J.C., and Hayden, B.Y. (2021). Multicentric tracking of multiple agents by anterior cingulate cortex during pursuit and evasion. Nat. Commun. 12, 1985. 

42. Taube, J.S., Muller, R.U., and Ranck, J.B. (1990). Head-direction cells recorded from the postsubiculum in freely moving rats. I. Description and quantitative analysis. J. Neurosci. 10, 420–435. 

43. Taube, J.S. (1998). Head direction cells and the neurophysiological basis for a sense of direction. Prog. Neurobiol. 55, 225–256. 

44. Kennerley, S.W., and Wallis, J.D. (2009). Reward-dependent modulation of working memory in lateral prefrontal cortex. J. Neurosci. 29, 3259–3270. 

45. Rushworth, M.F.S., Noonan, M.P., Boorman, E.D., Walton, M.E., and Behrens, T.E. (2011). Frontal cortex and reward-guided learning and decision-making. Neuron 70, 1054–1069. 

46. Maisson, D.J.-N., Cash-Padgett, T.V., Wang, M.Z., Hayden, B.Y., Heilbronner, S.R., and Zimmermann, J. (2021). Choice-relevant information transformation along a ventrodorsal axis in the medial prefrontal cortex. Nat. Commun. 12, 4830. 

47. Padoa-Schioppa, C. (2011). Neurobiology of economic choice: A goodbased model. Annu. Rev. Neurosci. 34, 333–359. 

48. Hirokawa, J., Vaughan, A., Masset, P., Ott, T., and Kepecs, A. (2019). Frontal cortex neuron types categorically encode single decision variables. Nature 576, 446–451. 

49. Raposo, D., Kaufman, M.T., and Churchland, A.K. (2014). A category-free neural population supports evolving demands during decision-making. Nat. Neurosci. 17, 1784–1792. 

50. Fusi, S., Miller, E.K., and Rigotti, M. (2016). Why neurons mix: high dimensionality for higher cognition. Curr. Opin. Neurobiol. 37, 66–74. 

51. Blanchard, T.C., Piantadosi, S.T., and Hayden, B.Y. (2018). Robust mixture modeling reveals category-free selectivity in reward region neuronal ensembles. J. Neurophysiol. 119, 1305–1318. 

52. Courellis, H.S., Nummela, S.U., Metke, M., Diehl, G.W., Bussell, R., Cauwenberghs, G., and Miller, C.T. (2019). Spatial encoding in primate hippocampus during free navigation. PLoS Biol. 17, e3000546. 

53. Kaufman, M.T., Benna, M.K., Rigotti, M., Stefanini, F., Fusi, S., and Churchland, A.K. (2022). The implications of categorical and categoryfree mixed selectivity on representational geometries. Curr. Opin. Neurobiol. 77, 102644. 

54. Yoo, S.B.M., and Hayden, B.Y. (2018). Economic choice as an untangling of options into actions. Neuron 99, 434–447. 

55. Hunt, L.T., Dolan, R.J., and Behrens, T.E. (2014). Hierarchical competitions subserving multi-attribute choice. Nat. Neurosci. 17, 1613–1622. 

56. Hunt, L.T., Malalasekera, W.M.N., de Berker, A.O., Miranda, B., Farmer, S.F., Behrens, T.E.J., and Kennerley, S.W. (2018). Triple dissociation of attention and decision computations across prefrontal cortex. Nat. Neurosci. 21, 1471–1481. 

57. Hunt, L.T., and Hayden, B.Y. (2017). A distributed, hierarchical and recurrent framework for reward-based choice. Nat. Rev. Neurosci. 18, 172–182. 

58. Killian, N.J., Jutras, M.J., and Buffalo, E.A. (2012). A map of visual space in the primate entorhinal cortex. Nature 491, 761–764. 

59. Jacobs, J., Weidemann, C.T., Miller, J.F., Solway, A., Burke, J.F., Wei, X.X., Suthana, N., Sperling, M.R., Sharan, A.D., Fried, I., et al. (2013). Direct recordings of grid-like neuronal activity in human spatial navigation. Nat. Neurosci. 16, 1188–1190. 

60. Brown, A.E.X., and De Bivort, B. (2018). Ethology as a physical science. Nat. Phys. 14, 653–657. 

61. Datta, S.R., Anderson, D.J., Branson, K., Perona, P., and Leifer, A. (2019). Computational neuroethology: a call to action. Neuron 104, 11–24. 

62. Krakauer, J.W., Ghazanfar, A.A., Gomez-Marin, A., MacIver, M.A., and Poeppel, D. (2017). Neuroscience needs behavior: correcting a reductionist bias. Neuron 93, 480–490. 

63. Matusz, P.J., Dikker, S., Huth, A.G., and Perrodin, C. (2019). Are we ready for real-world neuroscience? J. Cogn. Neurosci. 31, 327–338. 

64. Pearson, J.M., Watson, K.K., and Platt, M.L. (2014). Decision making: the neuroethological turn. Neuron 82, 950–965. 

65. Yoo, S.B.M., Hayden, B.Y., and Pearson, J.M. (2021). Continuous decisions. Philos. Trans. R. Soc. Lond. B Biol. Sci. 376, 20190664. 

66. Azab, H., and Hayden, B.Y. (2018). Correlates of economic decisions in the dorsal and subgenual anterior cingulate cortices. Eur. J. Neurosci. 47, 979–993. 

67. Farashahi, S., Donahue, C.H., Hayden, B.Y., Lee, D., and Soltani, A. (2019). Flexible combination of reward information across primates. Nat. Hum. Behav. 3, 1215–1224. 

68. Yoo, S.B.M., and Hayden, B.Y. (2020). The transition from evaluation to selection involves neural subspace reorganization in core reward regions. Neuron 105, 712–724.e4. 

69. Wang, M.Z., and Hayden, B.Y. (2019). Monkeys are curious about counterfactual outcomes. Cognition 189, 1–10. 

70. Wang, M.Z., Hayden, B.Y., and Heilbronner, S.R. (2022). A structural and functional subdivision in central orbitofrontal cortex. Nat. Commun. 13, 3623. 

71. Blanchard, T.C., Wolfe, L.S., Vlaev, I., Winston, J.S., and Hayden, B.Y. (2014). Biases in preferences for sequences of outcomes in monkeys. Cognition 130, 289–299. 

72. Ebitz, R.B., Sleezer, B.J., Jedema, H.P., Bradberry, C.W., and Hayden, B.Y. (2019). Tonic exploration governs both flexibility and lapses. PLoS Comp. Biol. 15, e1007475. 

73. Balzani, E., Lakshminarasimhan, K., Angelaki, D., and Savin, C. (2020). Efficient estimation of neural tuning during naturalistic behavior. Adv. Neural Inf. Process. Syst. 33, 12604–12614. 

74. Ledergerber, D., Battistin, C., Blackstad, J.S., Gardner, R.J., Witter, M.P., Moser, M.B., Roudi, Y., and Moser, E.I. (2021). Task-dependent mixed selectivity in the subiculum. Cell Rep. 35, 109175. 

75. Saxena, S., and Cunningham, J.P. (2019). Towards the neural population doctrine. Curr. Opin. Neurobiol. 55, 103–111. 

76. Ebitz, R.B., and Hayden, B.Y. (2021). The population doctrine in cognitive neuroscience. Neuron 109, 3055–3068. 

3488 Current Biology 33, 3478–3488, August 21, 2023 

**ll** 

Article 

**==> picture [46 x 35] intentionally omitted <==**

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|
|---|---|---|---|---|
||||||
|Deposited data|||||
||||||
|Preprocessed data<br>Zenodo<br>https://doi.org/10.5281/zenodo.8067596|||||
||||||
|Software and algorithms|||||
|MATLAB analysis code<br>Zenodo<br>https://doi.org/10.5281/zenodo.8067596|||||
||||||



## RESOURCE AVAILABILITY 

## Lead contact 

Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, Benjamin Hayden (benhayden@gmail.com). 

## Materials availability 

The study did not generate new unique reagents. 

## Data and code availability 

- d The processed data reported in this paper have been deposited on Zenodo and are publicly available as of the date of publication. The DOI is listed in the key resources table. 

- d All original code has been deposited on Zenodo and is publicly available as of the date of publication. The DOI is listed in the key resources table. 

- d Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request. 

## EXPERIMENTAL MODEL AND SUBJECT DETAILS 

## Animal model 

Two male rhesus macaques (Macaca mulatta) served as subjects. Animals were habituated to laboratory conditions, trained to enter and exit an open arena, and then trained to operate water dispensers. The University Committee on Animal Resources at the University of Minnesota approved all animal procedures. Animal procedures were designed and conducted in compliance with the Public Health Service’s Guide for the Care and Use of Animals and approved by the institutional animal care and use committee (IACUC) of the University of Minnesota. 

## METHOD DETAILS 

## Surgical procedures 

We placed a cranium adherent form-fitted Gray Matter (Gray Matter Research) recording chamber and a 128-channel microdrive recording system over the area of interest. We used the same approach as Mao et al.[39] to verify sites. Specifically, we used CT scans which were compared to corresponding CT studies performed following surgical implantation and placement of the electrodes. The hyperdense appearance of electrodes using the post-recording CT allowed us to verify that electrodes followed the trajectory of the pre-operative plan. In both cases (that is, for both subjects), the results of the CT show that this was the case. Specifically, these results indicate that our procedures provided co-registration with an error of less than 0.5 mm. Since electrodes were advanced incrementally not all locations are verified using this approach, but positions could be validly inferred using interpolation. In addition, we performed a second complementary method that also confirmed placement of the electrodes. Specifically, as we have done in many past studies, as we moved the electrodes down into the brain, we made note of the auditorily detectable change from gray to white matter, and reconciled this information with our preoperative CT scans. In all cases, the two matched. Animals received analgesics and antibiotics after all procedures. Procedures were designed and conducted in compliance with the Public Health Service’s Guide for the Care and Use of Animals and approved by the institutional animal care and use committee (IACUC) of the University of Minnesota. 

## Recording sites 

We approached our brain regions by controlled and monitored advancement of individual electrodes, through reconciliation of measured thread-count against postoperative CT images. The implanted microdrive was connected through jumper cables and a 

Current Biology 33, 3478–3488.e1–e3, August 21, 2023 e1 

Article 

## **ll** 

head stage to a removable data logger (SpikeGadgets). The data logger was wirelessly triggered to store neural recordings onto a removable memory card from which it was then extracted at the end of each session. 

We defined OFC as lying within the coronal planes situated between 39.6 and 23.9 mm rostral to the central sulcus, the horizontal planes situated between 23.3 and 45.7 mm from the brain’s dorsal surface, and the sagittal planes between 1.3 and 22.1 mm from the medial wall. 

We defined dACC as lying within the coronal planes situated between 33.5 and 7.4 mm rostral to the central sulcus, the horizontal planes situated between 11.1 and 38.5 mm from the brain’s dorsal surface, and the sagittal planes between 0.4 and 6.7 mm from the medial wall. 

We defined SMA as lying within the coronal planes situated between 30.4 and 13.1 mm rostral to the central sulcus, the horizontal planes situated between 16.2 and 34.3 mm from the brain’s dorsal surface, and the sagittal planes between 0.4 and 6.7 mm from the medial wall. 

We defined vlPFC as lying within the coronal planes situated between 46.8 and 16.8 mm rostral to the central sulcus, the horizontal planes situated between 16.2 and 47.2 mm from the brain’s dorsal surface, and the sagittal planes between 1.1 and 19.4 mm from the medial wall. 

We defined dlPFC as lying within the coronal planes situated between 36.4 and 12.3 mm rostral to the central sulcus, the horizontal planes situated between 17.4 and 48.9 mm from the brain’s dorsal surface, and the sagittal planes between 1.1 and 19.4 mm from the medial wall. 

We defined PMd as lying within the coronal planes situated between 26.7 and 2.9 mm rostral to the central sulcus, the horizontal planes situated between 6.8 and 37.9 mm from the brain’s dorsal surface, and the sagittal planes between 1.9 and 23.7 mm from the medial wall. 

## Behavioral task 

Each patch delivered a fixed amount of 1.5 mL. The first four presses were rewarded with fluid delivery. The fifth was unrewarded and led to a 3-min deactivation. No reset or deactivation was applied if the animal left the patch. A patch was only reset if the subject pressed the lever a fifth time and waited 3 min. A trial consisted of a lever press at time 0, which changed the display to white with a green plus-sign in the center (0-2 seconds), an auditory cue was played (0-2 seconds), and a solenoid opened to dispense reward (0-1 second). After dispensing reward, the solenoid closed, the auditory cue ended, and the green plus-sign disappeared. The screen remained white for 2 additional seconds (2-4 seconds) before the screen turned blue again (total trial time = 4 seconds). The fifth lever press was followed by a white screen. Prior and concurrent chaired task training of these subjects included two risky choice tasks[66–70] and a simpler choice task.[71][,][72] 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

## Behavioral analysis 

There were 5-7 patch events recorded for each patch engagement: lever press, screen off (set to white), screen/auditory reward cue (rewarded presses only), solenoid open (rewarded presses only), solenoid close (rewarded presses only), screen off (set to white), timeout (deactivation press only), and screen reset. Lever press events that led to a reward were used to analyze the reward encoding. The final (unrewarded) press in the series was behaviorally special, so it was not suitable for use in comparison with the rewarded presses. We verified the accuracy of our system to subtle head movements in a previous manuscript.[35] 

To measure the 3 angular axes of the head, we first centered the extracted nose and neck coordinates, placing the estimated head position at the volumetric axis-origin. For each frame, we applied Euler angle transformations on the head-fixed coplanar points to determine the yaw, pitch and roll angles between the origin and the current head orientation. We defined the head direction variable as a 1D vector for the yaw angle of the head. We defined the head tilt variable as a 2D vector consisting of the pitch and roll angles. We measured egocentric boundary in polar coordinates, defined as a 2D variable consisting of the radial distance between the subject and the nearest wall on the azimuthal plane and the angle of the subject relative to the center of the room. To measure angular velocity, we computed a two-dimensional variable, where the first dimension reflects the rotation speed of the head (degrees/second) along the yaw angle and the second dimension reflects the rotation along the pitch angle. To measure linear velocity, we computed the distance traveled (centimeters/second) in any direction. 

## Linear-Nonlinear Poisson-distributed Generalized Additive Model 

We adapted a previously developed approach.[36][,][37][,][39–41][,][73][,][74] Briefly, recordings and variables were binned into 100-ms time bins. Neural data were fitted to multiple, nested linear-nonlinear-Poisson distributed generalized additive models. Data were divided into 10 tranches across the session. Within each, model estimates were computed using 5-fold cross-validation, by dividing each into 5 more subtranches. The process was repeated for each one. The estimated log-likelihood quantified the model performance, and the distribution of log-likelihood estimates was compared to a null distribution (one-sided Wilcoxon signed rank test, alpha = 0.05). 

The best-fitting model was selected using an optimized forward search. Models containing only one variable (1[st] order models) were fitted first. If these models performed better than the null, models containing two variables (2[nd] order models) were fitted. The process was repeated until the performance of the newly fitted model no longer improved over the previous. A neuron was categorized as tuned to a given variable if that variable was included within the best-fitting model. We use the proportion of neurons tuned 

e2 Current Biology 33, 3478–3488.e1–e3, August 21, 2023 

## Article 

## **ll** 

**==> picture [46 x 35] intentionally omitted <==**

as a population level analysis because it suggests that a variable may be a particularly important feature of the neural code and that the population activity may be important for decoding that variable (as we show in the decoding analysis for Figure 6).[75][,][76] Since our significance threshold, alpha, was set at 0.05 for a one-sided Wilcoxon signed rank test, we consider any proportion of neurons above 5% to be significant (see Figure S1 and Table S1 for a summary of variable tuning). Importantly, the additive process for multiple terms was incorporated within the exponentiation used to compute the estimated firing, thus making selectivity to multiple variables a conjunctive (nonlinear) estimate. To assess tuning stability across a session, we computed Pearson’s correlation between encoding magnitudes for each neuron to a given variable during the first and second half of the session. 

We validated the model on our data through a series of controls. After fitting the LN-GAM models, we randomly selected a neuron that was not significantly tuned to any combination of variables. We modified the spike train for that neuron to include a single spurious high firing event, once in each of 3 time periods. We also selected both 10 and 100 bins from each of 3 time periods to insert spurious high firing. Finally, we time-locked the insertion of 1, 10, and 100 simulated spurious events to consistent instances of the tracked position. We repeated this process across 20 randomly selected, untuned neurons from each structure, generating a set of 1200 synthetic datasets. We fitted each of these simulated time series against the original variables. We then determined the proportion of fitting processes that resulted in significant tuning. Only 8.08% (n = 97/1200) of control sets generated a statistically significant fit. These controls confirmed that the best-fitting models were not being influenced by random or spurious events, and instead reflected reliable tuning to the selected variables. 

## Stay/leave choice probability and neural encoding 

We adapted an approach commonly used in traditional neuroeconomics paradigms.[23][,][46][,][73] We leveraged the strictly timed structure of the foraging task to isolate the 2-second epoch during which subjects were rewarded for pressing a lever. Each lever press is necessarily separated from the next by a minimum of 4 seconds; 2 seconds of a reward period and 2 seconds of an intertrial interval. Therefore, each rewarded lever press was treated as a separate trial. We aggregated all trials for each feeder across the session. For each trial, we determined the number of rewarded presses remaining at both the current patch and all distal patches. We also determined whether the current trial occurred at the same or different patch from the previous trial. If it was the same as the previous patch, the subject was said to have made a ‘‘stay’’ choice on the previous trial. Conversely, if it was at a different patch, the subject was said to have made a ‘‘leave’’ choice on the previous trial. This binary choice variable was fitted to the total number of rewarded presses available across the distal patches, using a logistic regression. The resulting sigmoidal function was then used to estimate the stay/leave probability for each trial, based on how many rewarded presses were available elsewhere in the arena. Finally, for each neuron and each trial, an average firing rate was computed from the same post-press epoch. The trial-length vector of stay/leave probability was used to predict this trial-length vector of firing rates, using a linear regression that simultaneously controlled for the number of rewarded presses remaining at the current patch. 

## Distribution of variable encoding 

We adapted an approach previously developed for estimating clustering in n-dimensions, the elliptical Projection Angle Index of Response Similarity (ePAIRS).[48][,][49] If neurons form specialized subpopulations, they should form clusters along a shared axis. Thus, reducing the dimensionality of the tuning conditions across the population code should elucidate a functional cluster. To define a tuning condition, we compute the estimated marginal means (EMMs) from the fully-fitted LN-GAM model. Estimates were computed using the minimum and maximum values for each variable in the design matrix. We used the fully-fitted model estimates because it reduces sparsity in the population matrix. The dimensions of the EMM matrix were n x c, where n is the number of neurons in a brain area and c are the EMMs for each condition (1022 conditions total). We then performed principal component analysis (PCA) on this matrix to generate an n x d matrix of scores for each neuron, where d is the 10 most explanatory PC scores. We then computed the relative angles of each point in 10-D PC space and compared the angular distance between all pairs of nearest neighbors. A functional cluster, therefore, should have relatively tight angles between nearest neighbors when compared to a random distribution. Statistical significance was computed using a rank sum test. 

In each session, a given neuron might be more heavily tuned to one variable than another. That is, the EMMs reflect the distribution of preferred variables. We would expect these estimates to show clustering along the dimensions of the preferred variables. Therefore, as a positive control we performed the ePAIRS analysis on the EMMs and found significant clustering in all areas (p < 0.001, in all areas; two-tailed rank sum test). 

## Linear decoder 

To determine if randomly distributed variable encoding continues to support downstream decodability, we implemented a regressionbased SVM. Tracking data from each session was spatially binned into 9 continuous zones. We define a trial as an entry into the zone, followed by continuous zone occupancy until exiting the zone. We constructed a pseudo-population of pseudo-trials, 495-trials X n-neurons, by randomly selecting 55 trials from each zone for each neuron. We repeated the bootstrapping procedure to constitute one training set and one test set. We created two more matrices by shuffling the zone labels. A regression-based SVM model was trained on the training set and predictions were calculated by fitting the model to the test set. Accuracy was measured as the overall rate of successfully predicting the zone from the population neural activity in the test set. We repeated this process 500 times and averaged the classification accuracy across iterations. We then compared this average accuracy to that from the shuffled data. 

Current Biology 33, 3478–3488.e1–e3, August 21, 2023 e3 

