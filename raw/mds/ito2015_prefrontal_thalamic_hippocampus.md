doi:10.1038/nature14396 

## ARTICLE 

## A prefrontal–thalamo–hippocampal circuitforgoal-directedspatialnavigation 

Hiroshi T. Ito[1] , Sheng-Jia Zhang[1] , Menno P. Witter[1] , Edvard I. Moser[1] & May-Britt Moser[1] 

Spatial navigation requires information about the relationship between current and future positions. The activity of hippocampal neurons appears to reflect such a relationship, representing not only instantaneous position but also the path towards a goal location. However, how the hippocampus obtains information about goal direction is poorly understood. Here we report a prefrontal–thalamic neural circuit that is required for hippocampal representation of routes or trajectories through the environment. Trajectory-dependent firing was observed in medial prefrontal cortex, the nucleus reuniens of the thalamus, and the CA1 region of the hippocampus in rats. Lesioning or optogenetic silencing of the nucleus reuniens substantially reduced trajectory-dependent CA1 firing. Trajectory-dependent activity was almost absent in CA3, which does not receive nucleus reuniens input. The data suggest that projections from medial prefrontal cortex, via the nucleus reuniens, are crucial for representation of the future path during goal-directed behaviour and point to the thalamus as a key node in networks for long-range communication between cortical regions involved in navigation. 

Hippocampal place cells are part of an allocentric representation of local space that allows animals to navigate to desired locations[1,2] . Place cells provide accurate information about current location, but it has remained unclear how the place-cell map is used for animals to navigate from their current position to a goal position elsewhere in the environment. To implement goal-directed navigation, previous studies have proposed the need for a separate representation of future positions that is somehow brought together with the representation of current location to point the network to the goal[3–5] . Such pointers may be expressed in the activity of hippocampal place cells. When rats are engaged in a T-maze-based alternation task, in which they take left or right trajectories on alternating laps, place cells with fields on the stem of the maze fire at different rates on left- and right-turn trajectories, without changes in the position of the firing field[6,7] . The dependence on trajectory has both retrospective and prospective components, reflecting both where the animal comes from and where it is going[8] . However, as the animal approaches the decision point at the junction of the maze, the representation becomes more forward-oriented[9] , often with trajectories to upcoming locations embedded into the representation[10,11] , in addition to mere changes in firing rate. 

The source of trajectory information in place cells has not been identified. Here we used a continuous version of the T-maze alternation task[6] to determine how information about succeeding choices is introduced in hippocampal place-cell activity. We hypothesized that the selection of future trajectories depends on a wider circuit including not only the hippocampus but also structures involved in the evaluation and selection of actions, such as the prefrontal cortex[12–14] . Neurons in medial prefrontal cortex (mPFC) do not project directly to the hippocampus[15,16] but the midline thalamic nucleus reuniens (NR), which has reciprocal anatomical connections with the mPFC, may serve as a functional bridge to the hippocampal region, since NR has strong terminal fields in the CA1 subfield[15,17–19] . To address this possibility, we recorded and manipulated activity at various nodes of the prefrontal–reuniens–CA1 circuit and determined whether this circuit is necessary for place cells to represent upcoming trajectories. 

Trajectory-dependent firing is stronger in CA1 than CA3 We first asked whether NR is the source of trajectory information in CA1. If it is, we should observe a difference in trajectory-dependent firing between CA1 and CA3, because NR has major excitatory projections to CA1 but not CA3 (refs 15, 17–19). We thus recorded place cells in rat CA1 and CA3 in a continuous alternation task on a modified T-maze (Fig. 1a, b and Extended Data Fig. 1). A total of 363 CA1 cells and 180 CA3 cells exhibited location-specific complex spiking (12 and 5 rats, respectively). Within this sample, 98 CA1 cells and 34 CA3 cells had place fields on the central stem. All subsequent analysis of these cells was restricted to parts of the stem where there was no significant difference in the animal’s head direction, lateral position, or running speed between left-turn and right-turn trajectories. 

Many place cells in CA1 expressed several-fold changes in peak firing rate between left- and right-turn trajectories on the stem, without changes in the position of the firing field (Fig. 1c, d and Extended Data Fig. 2a). 54 CA1 cells (55.1%) showed significant rate changes that depended on trajectory (left or right) (P , 0.05 for main effect of trial type (left/right) in a two-way analysis of variance (ANOVA) with trial type and stem position as factors, and P , 0.05 post-hoc analysis of covariance (ANCOVA) with running speed, head direction and lateral position as covariates[6] ). By contrast, only six cells (17.7%) met the criteria for trajectory-dependent rate change in CA3 (Fig. 1e, f). The proportion of trajectory-dependent cells relative to total place cells was significantly smaller in CA3 than in CA1 (Z 5 3.78, P , 0.001, binomial test). Distributions of rate changes were significantly different (CA1, 32.8 6 2.6%; CA3, 19.8 6 3.1%; means 6 s.e.m.; D 5 0.338, P 5 0.005, Kolmogorov–Smirnov test; Fig. 1d, f and Extended Data Fig. 2b). Place-fields position did not change across trajectories (D 5 0.125, P 5 0.812). 

## Trajectory-dependent firing in NR 

The fact that trajectory dependence is expressed more strongly in CA1 than in CA3 points to NR as a possible source of modulation. To examine whether trajectory information is represented in NR, we 

> 1Kavli Institute for Systems Neuroscience and Centre for Neural Computation, Norwegian University of Science and Technology, Olav Kyrres gate 9, MTFS, 7491 Trondheim, Norway. 

5 0 | N A T U R E | V O L 5 2 2 | 4 J U N E 2 0 1 5 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [386 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
CA1 CA3<br>a b<br>c CA1 e CA3<br>#16755  TT11_1.t Right turn Left turn #18553 T7_1.t Right turn Left turn<br>40<br>60<br>30<br>40<br>20<br>31.6 10 53.9 20<br>Hz 00 20 40 60 80 Hz 00 20 40 60<br>0 Stem position (cm) 0 Stem position (cm)<br>d High-rate trajectories Low-rate trajectories 0.4 f High-rate trajectories Low-rate trajectories 0.4<br>0.3 0.3<br>10 0.2 5 0.2<br>20<br>30 0.1 10 0.1<br>4050 0 0 Peak rate change (%)20 40 60 80 100 15 00 Peak rate change (%)20 40 60 80 100<br>60 0.8 20 0.8<br>70 0.6 0.6<br>80 0.4 25 0.4<br>90 0.2 30 0.2<br>0 0<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 0 10 20 30 40 50 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 0 10 20 30 40 50<br>Normalized stem position Field position shift (cm) Normalized stem position Field position shift (cm)<br>Right Right<br>Left Left<br>Spike rate (Hz) Spike rate (Hz)<br>Cell number Frequency Cell number Frequency<br>**----- End of picture text -----**<br>


Figure 1 | Trajectory-dependent firing in CA1 but not CA3. a, Modified T-mazes used for the continuous alternation task. Red disk, food reward; arrows, running directions. b, Nissl-stained coronal sections through dorsal hippocampus. Red circles, tetrode tracks in CA1 and CA3. Original magnification, 32.5. c, Trajectory-dependent firing in CA1. Left panel, rate maps for a representative CA1 place cell in the continuous alternation task (left to right: all laps, right-turn laps, left-turn laps). Identification number of animal (#16755) and unit number (TT11_1.t) are indicated on top. Right panel, means (solid lines) and 95% confidence intervals (shaded) for spike rates of a single cell across the stem of the maze. Raster plots above. Left-heading runs in blue, right-heading runs in red. d, Left panels, difference in mean rates 

recorded spike activity in NR, simultaneously with CA1, while animals performed the continuous alternation task. Activity was also recorded in a square enclosure. Tetrodes were placed centrally in the rostral half of NR, where many CA1-projecting neurons are located[18] (Fig. 2a and Extended Data Fig. 1). We recorded activity in 64 NR cells from six animals. NR neurons were active across the entire box, with a mean firing rate of 7.8 6 1.3 Hz (mean 6 s.e.m.). Spatial information in bits per spike was negligible and substantially lower than in CA1 (NR, 0.048 6 0.009; CA1, 1.46 6 0.09; Extended Data Fig. 2c). Nonetheless, in the continuous alternation task, NR neurons exhibited differential firing on left- versus right-turn trajectories (Fig. 2b, c). Of the NR cells 42.2% (27 out of 64) showed a significant rate change across alternating trajectories (Fig. 2d; P , 0.05 for trial type and trial type 3 stem position in a two-way ANOVA). The proportion of trajectory-modulated cells was not significantly lower than in simultaneously recorded CA1 cells (59.1%; 13/22 cells; Z 5 1.37, P 5 0.17, binomial test) or in the entire sample of CA1 cells from the animals with hippocampal tetrodes (54/98 cells; Z 5 1.61, P 5 0.11). The mean change in peak firing rate on the stem was 22.5 6 2.5% (left versus right; Fig. 2e). The difference between left- and right-turn trajectories could not be explained by differences in other behavioural variables (P , 0.05, ANCOVA with running speed, head direction and lateral position as covariates). The recordings thus support the idea that NR is a major source of trajectory information to CA1. 

## Trajectory-dependent firing in mPFC 

NR receives strong projections from mPFC[19] , suggesting that it serves as a relay between mPFC and CA1[15,19] . If it does, trajectory information in NR and CA1 may also be expressed in mPFC. To test this, we 

between left and right trajectories for all CA1 cells with firing fields on the stem. Left- and right-turn trajectories were classified as high rate or low rate depending on which direction had the highest mean peak rate on the stem. Spike rates were normalized to the peak firing rate of each cell and sorted according to field position on high-rate trajectories. Each line shows one cell. Normalized spike rate is colour-coded (red for higher and blue for lower rates). Right top panel, distribution of normalized change in peak firing rate on the stem between high and low-rate trajectories high{low . Right bottom � high � panel, distribution of shift of field position between high- and low-rate trajectories. e, f, As in c, d but for CA3 place cells. 

recorded the activity of mPFC cells in the continuous alternation task (338 cells, 3 animals). The cells were also recorded during free foraging in the square box. The recordings started with tetrodes in the dorsal anterior cingulate cortex and continued as the tetrodes were advanced 

**==> picture [253 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b #17340 TT5_1.t  Right turn Left turn<br>9.3<br>Hz<br>0<br>NR<br>c d High-rate trajectories Low-rate trajectories e<br>10<br>20 0.3<br>8 30<br>0.2<br>6<br>40<br>4<br>50 0.1<br>2<br>60<br>00 10 20 30 40 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 00 20 40 60 80 100<br>Stem position (cm) Normalized stem position Peak rate change (%)<br>Right<br>Left<br>Cell number Frequency<br>Spike rate (Hz)<br>**----- End of picture text -----**<br>


Figure 2 | Trajectory-dependent firing in NR. a, Nissl-stained coronal section showing tetrode track (red circle) in NR (outline). Original magnification, 32.5. b, Rate maps of a representative NR cell in the continuous alternation task (left to right: all laps, right-turn laps, left-turn laps). Animal and unit identification as in Fig. 1b.Top, colour-codedrate maps; bottom, spike locations (red) on trajectory (blue). c, Mean rate, 95% confidence intervals and raster plots for the cell in b. d, Normalized spike rate on the stem for all cells recorded in NR, plotted as in Fig. 1d. e, Change in spike rate between highand low-rate trajectories, as in Fig. 1d but for NR cells. 

4 J U N E 2 0 1 5 | V O L 5 2 2 | N A T U R E | 5 1 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

to the dorsal prelimbic cortex (Fig. 3a and Extended Data Fig. 3a). Neurons in mPFC had firing properties similar to those of NR neurons in that, while they were non-selectively active throughout the square box, with a mean firing rate of 4.9 6 0.4 Hz (mean 6 s.e.m.) and minimal location-selective activity (mean spatial information: 0.134 6 0.012 bits per Hz; Extended Data Fig. 2c), these neurons fired differentially on left and right-turntrajectories onthe centralstem of the alternation task (Fig. 3b, c). One-third of the cells (129/338 cells or 38.2%) exhibited trajectory-dependent rate changes, in agreement with previous reports[14,20] (Fig. 3d and Extended Data Fig. 3b, c; P , 0.05 for trial type and trial type 3 stem position in a two-way ANOVA). The mean change in peak firing rate between left and right-turn trajectories (6 s.e.m.) was 29.6 6 1.2% (Fig. 3e). The rate change was not caused by differences in observed behaviour (P , 0.05 in ANCOVA with running speed, headdirectionandlateral position as covariates).Taken together, these observations suggest that NR shares information about past and present trajectory with the mPFC. 

## NR inactivation reduces trajectory-dependent CA1 firing 

It is not clear from the recording experiments whether trajectorydependent firing in NR is necessary for trajectory-dependent firing in the hippocampus, or whether these patterns of activity are expressed independently and in parallel across multiple brain regions. We addressed this question using two approaches that each interrupted the mPFC–NR–CA1 loop at the level of NR. 

First we made lesions in NR using local injections of ibotenic acid (Fig. 4a and Extended Data Fig. 4). Animals with NR lesions did not exhibit detectable deficits in learning or performance on the continuous alternation task (Extended Data Fig. 5a), in agreement with previous work showing that continuous alternation persists after large hippocampal lesions[21] . We were also not able to identify changes in running speed or in the spectral power of local field potentials in CA1 (Extended Data Fig. 5b, c). However, trajectory coding in CA1 was clearly impaired. We recorded 176 CA1 place cells from 4 animals with NR lesions. Neurons in CA1 from lesioned animals expressed little rate change between left- and right-turn trajectories (Fig. 4b, c). Among the 44 cells that had place fields on the stem, we found only 7 (15.9%) that passed the criteria for trajectory-dependent rate change, a significant reduction compared to the proportion in CA1 cells of control animals (55.1%; Z 5 4.36, P , 0.001, binomial test). The mean rate change (6s.e.m.) between left- and right-turn trajectories for 

**==> picture [253 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b #17914 TT7_2.t  Right turn Left turn<br>12.8<br>Hz<br>0<br>c d High-rate trajectories Low-rate trajectories e<br>0.25<br>50<br>100 0.2<br>15 150 0.15<br>10 200 0.1<br>250<br>5 0.05<br>300<br>00 10 20 30 40 50 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 00 20 40 60 80 100<br>Stem position (cm) Normalized stem position Peak rate change (%)<br>htRig<br>Left<br>Cell number Frequency<br>Spike rate (Hz)<br>**----- End of picture text -----**<br>


Figure 3 | Trajectory-dependent firing in mPFC. a, Nissl-stained coronal section showing tetrode positions (red circles) in the dorsal prelimbic area of mPFC. Original magnification, 32.5. b, Rate maps for a representative mPFC cell (recorded at location in a, plotted as in Fig. 2b). c, Mean rate, 95% confidence intervals and raster plots for the cell in b. d, Normalized rate on the stem for all mPFC cells, as in Fig. 1d. e, Change in spike rate of mPFC cells between trajectories, as in Fig. 1d. 

place cells was 18.7 6 2.7%, significantly lower than in CA1 control animals (32.8 6 2.6%; D 5 0.346, P , 0.001, Kolmogorov–Smirnov test; Fig. 4d, e and Extended Data Fig. 5d) and comparable to CA3 control animals (19.8 6 3.1%; D 5 0.152, P 5 0.744). The position shift of place fields between trajectories was not significantly different from those of control animals (D 5 0.083, P 5 0.982). Thus the NR lesion caused a selective reduction of trajectory-dependent rate differences in CA1 cells. 

The lesion experiment does not exclude the possibility that NR plays only a temporary role in the development of trajectory coding in CA1 and so may not be required after initial learning. To assess the need for ongoing NR activity, we used local infusion of adeno-associated virus to express selectively the enhanced halorhodopsin eNpHR3.1 in NR neurons. Neurons expressing eNpHR3.1 could then be inactivated optogenetically with laser application using a wavelength of 532 nm restricted to the time when the animals were engaged in the alternation task. NR spikes, recorded with tetrodes attached to the optic fibre, were significantly suppressed during light application, on average by 63.1 6 7.0% (mean reduction 6 s.e.m., 5 to 0 s interval before silencing versus 2.5 to 5 s interval after onset 

**==> picture [253 x 331] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b CA1 with NR lesion<br>#16249 TT7_2.t Right turn Left turn<br>31.8<br>Hz<br>0<br>c d High-rate trajectories Low-rate trajectories e 0.3<br>CA1<br>5 0.2<br>10<br>0.1<br>15<br>40 20 0<br>30 25 0.3 CA1 with<br>20 30 0.2 NR lesion<br>35<br>10 40 0.1<br>00 20 40 60 80 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 0 0 20 40 60 80 100<br>Stem position (cm) Normalized stem position Peak rate change (%)<br>f #18516 TT3_2.t Right turn Left turn<br>0.2<br>12 0.15<br>8 0.1<br>13.5 4 0.05<br>Hz 0 0<br>0 0 20 40 60 0 20 40 60 80 100<br>0.2<br>0.15<br>15 0.1<br>17.6Hz 105 0.05<br>0 00 20 40 60 0 0 20 40 60 80 100<br>0.2<br>0.15<br>20 0.1<br>19.0 1510 0.05<br>Hz 5<br>0 0<br>0 0 20 40 60 0 20 40 60 80 100<br>Stem position (cm) Peak rate change (%)<br>Right<br>Left<br>Cell number Frequency<br>Spike rate (Hz)<br>Right<br>Left<br>Before<br>Right<br>Left<br>Laser on Spike rate (Hz) Frequency<br>Right<br>Left<br>After<br>**----- End of picture text -----**<br>


Figure 4 | Loss of trajectory-dependent firing in CA1 after NR inactivation. a, Nissl-stained coronal brain section showing bilateral NR lesion. Outline shows NR. Original magnification, 32.5. b, Colour-coded rate maps for a representative CA1 place cell in a NR-lesioned animal, plotted as in Fig. 1c. c, Mean rate, 95% confidence intervals and raster plots for the cell in b. d, Normalized firing rate on the stem for all CA1 place cells from animals with NR lesions, as in Fig. 1d. e, Change in peak rate on the stem between leftand right-turn trajectories, as in Fig. 1d. f, Left, colour-coded rate maps for a representative CA1 place cell before, during, and after optogenetic silencing of NR, with separate plots for left- and right-turn trajectories, as in Fig. 1c. Middle, means, 95% confidence intervals and raster plots for left- and rightturn trajectories (blue and red, respectively). Same cell as in the left plot. Right, change in peak rate between left- and right-turn trajectories for CA1 place cells with trajectory-dependent firing (as in Fig. 1d). 

5 2 | N A T U R E | V O L 5 2 2 | 4 J U N E 2 0 1 5 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

of silencing; Extended Data Fig. 6). In six NR-implanted animals, we recorded simultaneously the activity of 50 CA1 cells with place fields on the stem. Before the laser application, 72% of the recorded CA1 place cells (36/50) exhibited significant trajectory-dependent rate changes. During the laser application, the percentage of trajectorydependent cells, in the same sample, was reduced to 44 (22/50, Z 5 2.837, P 5 0.005, binomial test). When the illumination was terminated, the percentage recovered to baseline (72%; 36/50 cells). We did not observe any difference in the position of place fields between trajectories on laser-on and laser-off trials (F2,98 5 0.02, P 5 0.983, repeated-measures ANOVA; Extended Data Fig. 5i). Silencing of NR cells did not affect the animal’s behaviour, the mean firing rates of the place cells, or the spectral power of the local field potential in CA1 (Extended Data Fig. 5e–h).Taken together, these findings demonstrate that NR activity modulates firing rates of CA1 cells in a trajectory-dependent manner during spatial navigation. 

## Prospective trajectory representation 

While we found significant correlation between trajectory choices and activity of neurons in mPFC, NR and CA1 (Extended Data Fig. 7), it remains unclear whether this information is a determinant of the next trajectory choice or merely a reflection of events associated with the preceding lap on the maze. We addressed this distinction in three ways. 

First, we investigated trajectory-dependent firing on error trials, or runs succeeded by an incorrect choice. On these runs, the representation of the next correct destination is likely to be compromised, unlike influences from the preceding trajectory, which may be preserved. Differences between correct trials and error trials are likely to be most evident near the end of the stem, just before the animal makes the next trajectory choice. Thus, we divided the stem into equal-size bins and assessed decoding accuracy using mean firing rates in each bin as inputs to a classifier. We found that the activity of neurons in mPFC, NR and CA1 consistently represented the correct next trajectory across stem positions on correct trials (Fig. 5a). By contrast, on error trials, the activity of the neuronal ensemble initially represented the correct succeeding trajectory but then gradually decreased to chance level as the animals approached the junction. A significant reduction of trajectory representation on error trials was observed in all three regions—mPFC, NR and CA1—providing further support for the idea that these areas are functionally coupled (main effect of task performance (correct versus error) in a logistic regression analysis, with task performance and stem position as coefficients: mPFC, Z 5 5.98, P , 0.001; NR, Z 5 3.59, P , 0.001; CA1, Z 5 3.43, P , 0.001). The disruption of trajectory representation on error trials indicates that the information transferred through the mPFC–NR– CA1 circuit is an important determinant of the animal’s succeeding choice of trajectory. 

In a second approach, we introduced a delay of 10–15 s each time the animal reached the base of the stem. During this delay, access to the central stem was blocked. The delay was added to reduce the influence of working memory, or memory of the preceding lap, on trajectory-dependent firing when the rat subsequently ran down the stem of the maze. Prospective components should not be disrupted by this procedure. Animals learned the delayed alternation task to nearperfect levels (89% correct on average across 56 sessions). We recorded 133 cells from mPFC, 57 cells from NR, and 45 cells from CA1 in this task. All CA1 cells had firing fields on the stem. The decoding approach was then used to assess whether the firing rates on the stem represented the correct succeeding trajectory. During the delay period, the classifier was not able to decode any trajectory representation after the first half of the delay (Fig. 5b). After the delay, significant differences emerged between correct and incorrect trials, with decoding performance increasing towards the end of the stem (task performance 3 stem position, logistic regression analysis; mPFC, 

**==> picture [248 x 539] intentionally omitted <==**

**----- Start of picture text -----**<br>
mPFC<br>a P  < 0.05<br>90<br>80<br>70<br>60<br>50<br>Chance level<br>40 Correct<br>Error<br>30<br>Stem position<br>NR CA1<br>P  < 0.05<br>90 90<br>80 80<br>70 70<br>60 60<br>50 50<br>40 Correct  40 Correct<br>Error Error<br>30 30<br>Stem position Stem position<br>b mPFC P  < 0.05<br>80 Correct<br>70 Error<br>60<br>Chance level<br>50<br>40<br>Delay Run<br>30 Delay Run<br>20<br>Firsthalf Lasthalf Stem position<br>80 NR 80 CA1 P  < 0.05<br>Correct  Correct<br>70 70<br>Error Error<br>60 60<br>50 50<br>40 40<br>30 Delay Run 30 Delay Run<br>20 20<br>Firsthalf Lasthalf Stem position Firsthalf Lasthalf Stem position<br>c Retrospective Prospective<br>90 70 P  < 0.05<br>mPFC<br>80 NR<br>CA1 60<br>70<br>60<br>50<br>mPFC Chance level<br>50 NR<br>CA1<br>40 40<br>Stem position Stem position<br>d Retrospective Prospective P  < 0.05<br>70 Delay Run 70 Delay Run<br>mPFC mPFC<br>NR NR<br>60 CA1 60 CA1<br>50 50<br>Chance level<br>40 Firsthalf Lasthalf Stem position 40 Firsthalf Lasthalf Stem position<br>Decoding of correct choice (%)<br>Decoding of correct choice (%) Decoding of correct choice (%)<br>Decoding of correct choice (%)<br>Decoding of correct choice (%) Decoding of correct choice (%)<br>Decoding performance (%) Decoding performance (%)<br>Decoding performance (%) Decoding performance (%)<br>**----- End of picture text -----**<br>


Figure 5 | Prospective coding. a, Decoding of correct subsequent trajectory using mean firing rates on the stem as inputs to a linear classifier. The stem was divided into six equally sized bins (upper left panel) and decoding performance was compared bin by bin for trials when animals subsequently made correct versus incorrect choices (three remaining panels: mPFC, NR, CA1; means 6 s.e.m.). Decodingperformance was estimatedagainst thenext correct trajectory direction on both correct trials and error trials. Dashed lines at the top indicate bins with decoding performance significantly better than chance (P , 0.05, binomial test). b, Decoding of correct subsequent trajectory on trials with a 10–15 s delay at the start of the stem. Symbols as in a. c, Retrospective and prospective components were extracted from spike rates using a subsampling procedure that cancelled out the contributions from one of the two components. Symbols as in a, but P values were estimated from the bootstrap distributions. d, Retrospective and prospective components in the delayed alternation task. Symbols as in c. 

4 J U N E 2 0 1 5 | V O L 5 2 2 | N A T U R E | 5 3 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Z 5 3.01, P 5 0.002; NR, Z 5 3.30, P , 0.001; CA1, Z 5 3.14, P 5 0.002). The gradual emergence of a trajectory representation relevant to the succeeding behavioural outcome suggests that activity in the mPFC–NR–CA1 loop represents prospective trajectory choices and not, in the first place, memories of the preceding path. 

Finally, we tried to extract analytically the prospective and retrospective components of the trajectory representation in the decoding analysis. To this end, we used a subsampled data set with the same number of correct trials and error trials such that the contributions of prospective or retrospective components were cancelled out (see Methods). In mPFC, the percentage of successfully decoded prospective paths was 62.7 6 3.6% on the continuous task and 65.6 6 4.1% on the delay task (mean 6 s.e.m. for last half of the stem). The prospective component correlated strongly with position segment, suggesting that it built up towards the end of the stem (continuous task, r 5 0.73 6 0.26; delay task, r 5 0.79 6 0.14; Fig. 5c, d). Neurons in NR and CA1 expressed a similar increase of the prospective component (correlation between stem segment and prospective component: NR, r 5 0.88 6 0.12; CA1, r 5 0.58 6 0.29 in the continuous task; NR, r 5 0.73 6 0.13; CA1, r 5 0.67 6 0.14 in the delay task). The prospective component in CA1 was abolished by lesions of NR (Extended Data Fig. 7b). We were also able to extract a retrospective component on the initial part of the stem in the continuous task (Fig. 5c), but not in the delayed task (Fig. 5d). Thus, whereas the representation of the preceding trajectory was largely disrupted by increasing the demands on working memory, the prospective component was maintained and expressed consistently across the mPFC–NR–CA1 circuit. 

source for goal-directed trajectory sequences in CA1 place cells, observed as sweeps of prospective spatial firing both during theta activity at junctions in a complex T-maze[10] or during brief periods of immobility when animals navigate to fixed locations in an open space[11] . 

The fact that alternation performance was not impaired by NR lesions, and remains intact after hippocampal lesions[21] , raises questions about the function of trajectory-dependent firing. We have shown that trajectory-dependent firing exists in multiple brain circuits. Trajectory information from mPFC may reach systems involved in motor planning and decision making directly, without passing through the hippocampus. This may be sufficient to enable choice behaviour in a simple alternation task. The copy of the trajectory signal that is sent to the hippocampus, via the NR, may become critical only when navigational decisions require combinatorial representation of trajectory and location (Extended Data Fig. 10). Such combinatorial representations were observed only in CA1. Nonlinear combination of information modalities has been described in individual neurons in a number of brain systems[31–34] and is thought to increase the discrimination capacity of downstream neurons during encoding of high-dimensional information[35] . In the hippocampus, combinatorial coding in trajectory-dependent place cells may form the basis for complex navigational operations in efferent regions such as the subiculum or the entorhinal cortex. High-dimensional representations in trajectorydependent place cells may be necessary for networks in these regions to classify complex position–trajectory combinations. 

Online Content Methods, along with any additional Extended Data display items andSource Data, are available in the onlineversion of the paper; references unique to these sections appear only in the online paper. 

## Discussion 

When animals plan a route to a desired location, they must estimate how spatial position is changed following particular movements. Our study points to mPFC, NR and CA1 as part of the neural circuit for representation of goal-directed routes or trajectories. The data suggest that while distinct sets of CA1 cells are activated at each spatial position, the distribution of firing rates among these cells collectively represents the animal’s intended direction of movement, and that this information is carried from the prefrontal cortex to CA1 through the midline thalamic NR. At each node of this loop, cells have firing rates that reflect the animal’s subsequent trajectory. Disrupting the loop at the level of NR substantially reduces the trajectory dependence of the representation in CA1. CA3 cells, which do not receive direct input from NR, exhibit little trajectory-dependent activity, despite the strong remapping seen in this subfield during changes in the sensory environment[22–24] . Taken together, the results point to the mPFC–NR– CA1 circuit, and possibly indirect projections from mPFC and NR via the entorhinal cortex[25] , as a key element of the circuit for map-based route planning. The data provide functional support for the idea that communication between cortical regions is mediated not only by direct connections but also through the thalamus[26–29] . 

The findings offer some clues as to what kind of information is imposed on CA1 cells by signals from mPFC and NR. Previous work has pointed to a role for NR inputs in expression of hippocampal memory. Lesions of NR disrupt spatial working memory[30] and inactivation of mPFC inputs to NR or NR inputs to the CA1 impair discrimination between contexts in a fear conditioning task[28] . The present results speak against a role for mPFC and NR in sensory context discrimination per se, because cells in these areas do not fire differentially unless the task involves differences in the route taken by the animal (Extended Data Figs 8 and 9). The trajectory-dependent nature of the firing was also not dependent on working memory, or memory of the preceding trajectory, because differential firing was resumed on the stem after it was blocked during the delay at the start of the stem. Instead the gradual increase in trajectory dependence as the animal approached the choice point on correct trials but not on error trials points to mPFC and NR as sources for information about the animal’s intended movement. The findings provide a possible 

## Received 30 August 2014; accepted 6 March 2015. 

## Published online 27 May 2015. 

1. O’Keefe, J. & Nadel, L. The Hippocampus as a Cognitive Map (Oxford Univ. Press, 1978). 

2. Moser, E. I., Kropff, E. & Moser, M. B. Place cells, grid cells, and the brain’s spatial representation system. Annu. Rev. Neurosci. 31, 69–89 (2008). 

3. Burgess, J., Recce, M. & O’Keefe, J. A model of hippocampal function. Neural Netw. 7, 1065–1081 (1994). 

4. Redish, A. D. Beyond the Cognitive Map (The MIT Press, 1999). 

5. Foster, D. J., Morris, R. G. & Dayan, P. A model of hippocampally dependent navigation, using the temporal difference learning rule. Hippocampus 10, 1–16 (2000). 

6. Wood, E. R., Dudchenko, P. A., Robitsek, R. J. & Eichenbaum, H. Hippocampal neurons encode information about different types of memory episodes occurring in the same location. Neuron 27, 623–633 (2000). 

7. Frank, L. M., Brown, E.N. & Wilson, M. Trajectory encodingin the hippocampus and entorhinal cortex. Neuron 27, 169–178 (2000). 

8. Ferbinteanu, J. & Shapiro, M. L. Prospective and retrospective memory coding in the hippocampus. Neuron 40, 1227–1239 (2003). 

9. Catanese, J., Viggiano, A., Cerasti, E., Zugaro, M. B. & Wiener, S. I. Retrospectively and prospectively modulated hippocampal place responses are differentially distributed along a common path in a continuous T-maze. J. Neurosci. 34, 13163–13169 (2014). 

10. Johnson, A. & Redish, A. D. Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. J. Neurosci. 27, 12176–12189 (2007). 

11. Pfeiffer, B. E. & Foster, D. J. Hippocampal place-cell sequences depict future paths to remembered goals. Nature 497, 74–79 (2013). 

12. Kim, J. N. & Shadlen, M. N. Neural correlates of a decision in the dorsolateral prefrontal cortex of the macaque. Nature Neurosci. 2, 176–185 (1999). 

13. Hok, V., Save, E., Lenck-Santini, P. P. & Poucet, B. Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex. Proc. Natl Acad. Sci. USA 102, 4602–4607 (2005). 

14. Fujisawa, S., Amarasingham, A., Harrison, M. T. & Buzsaki, G. Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. Nature Neurosci. 11, 823–833 (2008). 

15. Vertes, R. P., Hoover, W. B., Szigeti-Buck, K. & Leranth, C. Nucleus reuniens of the midline thalamus: link between the medial prefrontal cortex and the hippocampus. Brain Res. Bull. 71, 601–609 (2007). 

16. Jones, B. F. & Witter, M. P. Cingulate cortex projections to the parahippocampal region and hippocampal formation in the rat. Hippocampus 17, 957–976 (2007). 

17. Herkenham, M. The connections of the nucleus reuniens thalami: evidence for a direct thalamo-hippocampal pathway in the rat. J. Comp. Neurol. 177, 589–609 (1978). 

18. Dolleman-van Der Weel, M. J. & Witter, M. P. Projections from the nucleus reuniens thalami to the entorhinal cortex, hippocampal field CA1, and the subiculum in the rat arise from different populations of neurons. J. Comp. Neurol. 364, 637–650 (1996). 

5 4 | N A T U R E | V O L 5 2 2 | 4 J U N E 2 0 1 5 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

19. Cassel, J.C. et al. Thereuniens andrhomboid nuclei:neuroanatomy, electrophysiological characteristics and behavioral implications. Prog. Neurobiol. 111, 34–52 (2013). 

20. Baeg,E.H. etal. Dynamics ofpopulation codefor workingmemoryintheprefrontal cortex. Neuron 40, 177–188 (2003). 

21. Ainge, J. A., van der Meer, M. A., Langston, R. F. & Wood, E. R. Exploring the role of context-dependent hippocampal activity in spatial alternation behavior. Hippocampus 17, 988–1002 (2007). 

22. Anderson, M. I. & Jeffery, K. J. Heterogeneous modulation of place cell firing by changes in context. J. Neurosci. 23, 8827–8835 (2003). 

23. Leutgeb, S., Leutgeb, J. K., Treves, A., Moser, M. B. & Moser, E. I. Distinct ensemble codes in hippocampal areas CA3 and CA1. Science 305, 1295–1298 (2004). 

24. Leutgeb, S. et al. Independent codes for spatial and episodic memory in hippocampal neuronal ensembles. Science 309, 619–623 (2005). 

25. Wouterlood, F. G., Saldana, E. & Witter, M. P. Projection from the nucleus reuniens thalamitothe hippocampal region: light and electron microscopic tracingstudyin the rat with the anterograde tracer Phaseolus vulgaris-leucoagglutinin. J. Comp. Neurol. 296, 179–203 (1990). 

26. Sommer, M.A.& Wurtz, R.H. Influence ofthethalamus onspatial visualprocessing in frontal cortex. Nature 444, 374–377 (2006). 

27. Sherman, S. M. & Guillery, R. W. Exploring the Thalamus and its Role in Cortical Function. (MIT Press, 2006). 

28. Xu, W. & Sudhof, T. C. A neural circuit for memory specificity and generalization. Science 339, 1290–1295 (2013). 

29. Vertes, R. P., Linley, S. B., Groenewegen, H. J. & Witter, M. P. in The Rat Nervous System 4th edn (ed. G. Paxinos) Ch. 16 (Elsevier Academic Press, 2014). 

30. Hembrook, J. R. & Mair, R. G. Lesions of reuniens and rhomboid thalamic nuclei impair radial maze win-shift performance. Hippocampus 21, 815–826 (2011). 

31. Andersen, R. A. & Mountcastle, V. B. The influence of the angle of gaze upon the excitability of the light-sensitive neurons of the posterior parietal cortex. J. Neurosci. 3, 532–548 (1983). 

32. Sargolini, F. et al. Conjunctive representation of position, direction, and velocity in entorhinal cortex. Science 312, 758–762 (2006). 

33. Komorowski, R. W., Manns, J. R. & Eichenbaum, H. Robust conjunctive item-place coding by hippocampal neurons parallels learning what happens where. J. Neurosci. 29, 9918–9929 (2009). 

34. Warden, M. R. & Miller, E. K. Task-dependent changes in short-term memory in the prefrontal cortex. J. Neurosci. 30, 15801–15810 (2010). 

35. Rigotti, M. et al. The importance of mixed selectivity in complex cognitive tasks. Nature 497, 585–590 (2013). 

Supplementary Information is available in the online version of the paper. 

Acknowledgements Wethank A.M.Amundsga˚rd,K.Haugen,K.Jenssen,E.Kra˚kvik and H. Waade for technical assistance, M. Andresen, E. Ha˚rstad and G. Jakobsen for taking care of animals, J. Ye and J. Wu for help with immunostaining of brain sections, K. Deisseroth for providing eNpHR3.0 plasmids, and A. Treves and A. Tsao and other members of the Moser laboratory for discussion. This work was supported by two Advanced Investigator grants from the European Research Council (‘CIRCUIT’, Grant Agreement no. 232608; ‘ENSEMBLE’, Grant Agreement no. 268598), the Kavli Foundation, the Centre of Excellence scheme of the Research Council of Norway (Centre for the Biology of Memory and Centre for Neural Computation). 

Author Contributions H.T.I.,E.I.M.and M.-B.M. designedthe experiment. S.-J.Z. madeall viralconstructs.M.P.W.advised onlocationofelectrodesandlesions,H.T.I.performedall experiments and analyses. H.T.I., E.I.M. and M.-B.M. wrote the manuscript after discussion among all authors. M.-B.M. and E.I.M. supervised and coordinated the project. 

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to H.T.I. (hiroshi.ito@ntnu.no) or M.-B.M. (may-britt.moser@ntnu.no). 

4 J U N E 2 0 1 5 | V O L 5 2 2 | N A T U R E | 5 5 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

## METHODS 

Subjects. Thirty-six male Long Evans rats (400–600 g at implantation) were housed individually in transparent Plexiglass cages (45 cm 3 30 cm 3 35 cm). Six of the rats were implanted with tetrodes in CA1 only. Two rats were implanted with tetrodes in both CA1 and CA3. Three rats had tetrodes in CA3. Four rats received neurotoxic lesions of NR and had tetrodes in CA1. Twelve rats had tetrodes in NR and CA1/CA3. Three rats had tetrodes in mPFC. Six rats received adeno-associated virus (AAV) injections in NR; all of these animals had tetrodes in CA1. All rats were kept at 85–90% of free-feeding body weight and maintained on a 12-h light/12-h dark schedule. All behavioural training and recordings were performed in the dark phase. 

The experiments were performed in accordance with the Norwegian Animal Welfare Act and the European Convention for the Protection of Vertebrate Animals used for Experimental and Other Scientific Purposes. The study contained no randomization to experimental treatments and no blinding. Sample size (number of animals) was set a priori to three or more, considered as the minimum required to obtain the number of cells required for statistical power in the present type of data. No statistical method was used to predetermine sample size. 

Construction, preparation and titration of recombinant AAV (rAAV) expressing eNpHR3.1. The proviral plasmid used for packaging rAAV was flanked by AAV serotype-2 inverted terminal repeats (ITR). The rAAV vector contained both a woodchuck hepatitis virus post-transcriptional regulatory element and a bovine growth hormone polyadenylation signal for enhancing transgene transcription and expression. Transcription was regulated by a calcium– calmodulin-dependent protein kinase II a (CaMKIIa) promoter, and the viral vector, pAAV-CaMKIIa-eNpHR3.0-eYFP (a gift from K. Deisseroth), was used as a PCR template to generate a trafficking-enhanced opsin. A Flag tag was placed at the C-terminus of the opsin gene between the 20-amino-acid trafficking signal DYKDHDGDYKDHDIDYKDDDDK and the endoplasmic reticulum exporting motif FCYENEV, both derived from the inward-rectifier potassium ion channel Kir2.1 and introduced to improve membrane trafficking[36] . The 17-amino acid N-terminal signal peptide from the b subunit of the nicotinic acetylcholine receptor, originally used for membrane insertion in eNpHR2.0, was removed as previously described[37,38] . 

The rAAV vector was pseudo-typed with AAV1 capsid proteins. rAAV2/1 was prepared by co-transfection of human embryonic kidney cell line HEK293 using the calcium phosphate method along with the adenoviral helper plasmid pHelper (Strategene). Twelve hours after transfection, the DNA/CaCl2 mixture was replaced with normal growth medium. After an additional 60 h in culture, the transfected cells were collected and subjected to three freeze/thaw cycles. The clear supernatant was then purified using heparin affinity columns (HiTrap Heparin HP, GE Healthcare). The purified rAAV2/1 was concentrated with an Amicon Ultra-4 centrifugal filter 100K device (Millipore), and the viral titre was determined by real-time quantitative PCR using StepOnePlus Real-Time PCR Systems and TaqMan Universal Master Mix (Applied Biosystems). The titred virus was diluted and matched to 1.0 3 10[12] viral genomic particles per ml by 13 PBS. 

Surgery, virus injection, lesions and drive implantation. The rats were anaesthetized with isoflurane. Initial concentration in the induction chamber was 5.0% (vol/vol). Air flow was set to 1.0–1.5 l min[2][1] . For analgesia, Temgesic (buprenorphine, 15 mg/300 g; RB Pharmaceuticals Limited) was administered by subcutaneous injection. Following induction of anaesthesia, the animal was fixed in a Kopf stereotaxic frame for electrode implantation and virus injection at 0.5–2% isoflurane (vol/vol), adjusted according to physiological monitoring. Holes for tetrode implantation were drilled on the skull. 

For tetrode recording from CA1 or CA3, animals were implanted with a ‘hyperdrive’ with 14 independently movable tetrodes constructed from 17-mm polyimide-coated platinum–iridium (90–10%) wire (California Fine Wire). The tetrode bundle was circular. The tetrodes were implanted at anterior–posterior (AP): 23.8 mm from bregma, medial–lateral (ML): 3.5 mm from midline, and dorsal–ventral (DV): 1.0 mm below dura. Electrode tips were plated with platinum to reduce electrode impedances to 100–200 kV at 1 kHz. In seven animals, implanted for simultaneous recording from NR and CA1 and/or CA3, we used a split bundle of tetrodes, in order to independently target seven tetrodes (three independently movable double tetrodes and one reference) to NR (AP: 22.25, ML: 0.6) and seven tetrodes (six independently movable tetrodes and one reference) to the hippocampus (AP: 23.25, ML: 2.5). The tetrodes were implanted with a 5u lateral-to-medial angle in the coronal plane. For tetrode recording in mPFC, a hyperdrive with a circular bundle of 14 independently movable tetrodes was implanted on the surface of the prefrontal cortex (AP: 13.25, ML: 0.6, DV: 1.0, with a 5u lateral-to-medial angle in the coronal plane). The hyperdrives were secured to the skull with jeweller’s screws and dental cement. Two screws in the 

skull behind the lambda (above the cerebellum) were connected to hyperdrive ground. Following closure of the wound, the electrodes were turned into the cortex while signals were monitored on the recording system. The animals received an oral dose of the analgesic Metacam (Meloxicam, 0.1 mg per 300 g; Boehringer Ingelheim) during the first few days after the surgery. 

In two animals aimed for simultaneous recording from NR and CA1, we first implanted a ‘microdrive’ with four tetrodes targeting NR (AP: 22.0, ML: 0.6, DV: 5.5, with a 5u lateral-to-medial angle in the coronal plane). This was followed by the implantation of a second microdrive above CA1 (AP: 24.0, ML: 3.2, DV: 1.5). One skull screw behind lambda (above the cerebellum) served as ground for each drive. 

For the optogenetics experiments, solution of rAAV virus was injected using a 10-ml NanoFil syringe and a 33-gauge bevelled metal needle (World Precision Instruments) at four sites in NR (AP: 22.0 and 22.5, ML 0.8 mm from midline, DV: 6.75 and 6.25). The injection was made at an 8u lateral-to-medial angle in the coronal plane) in order to target the central portion of NR in the coronal plane, on both sides of the midline. Injection volume (0.25 ml at each site) and flow rate (0.05 ml min[2][1] ) were controlled with a Micro4 Microsyringe Pump Controller (World Precision Instruments). After the injection, the needle was left in place for ten additional minutes before it was withdrawn slowly. After retraction of the needle, an optic fibre (FT400UMT: 0.39 NA, core size Ø 400 mm; Thorlabs) with two tetrodes attached was inserted so that the tip of the fibre was approximately 0.25 mm above NR (AP: 2.25, ML: 0.8, DV: 6, with an 8u lateral-to-medial angle in the coronal plane). The two tetrodes were advanced 0.75 mm beyond the tip of the optic fibre, targeting NR. The tetrodes were wired to the headstage connector for the recording system (Axona Ltd). After the optic fibre insertion, a hyperdrive with 14 independently movable tetrodes was implanted above CA1 in the left hemisphere (AP 4.0, ML 3.5 with a 10u lateral-to-medial angle in the coronal plane). 

For NR lesion experiments, ibotenic acid (Sigma-Aldrich) was dissolved in phosphate-buffered saline (pH 7.4, 10 mg ml[2][1] ) and injected using a 10-ml NanoFil syringe and a 33-gauge bevelled metal needle (World Precision Instruments) mounted to the stereotaxic frame. Volumes of 0.1 ml of ibotenic acid were infused over 10 min at three stereotaxic positions in the NR of the left hemisphere (AP: 21.75, ML: 0.6, DV: 6.75; AP: 2.25 and 2.75, ML: 0.6, DV: 7.0), targeting the central portion of NR in the coronal plane. The angle of the injection needle was 5u in the coronal plane with the tip pointing towards the midline. The flow rate was 0.01 ml min[2][1] . Flow was controlled with a Micro4 Microsyringe Pump Controller. After the injection, the needle was left in place for 10 min. When the infusions were completed, the rats were immediately implanted with a hyperdrive aimed at CA1 in the same hemisphere (AP: 3.8, ML: 3.0) or with two microdrives aimed at CA1 in each hemisphere (AP: 4.0, ML: 3.2). 

Electrode turning and recording procedures. The hyperdrive was connected to a multichannel unity gain headstage (HS-54; Neuralynx). The output of the headstage was connected via a lightweight multi-wire tether and a Neuralynx PSR-36 commutator to a data acquisition system with 64-channel digital amplifiers (Digital Lynx; Neuralynx). Unit activity was filtered at 600 (64 taps)–6,000 (32 taps) Hz with a FIR band-pass filter. Spike waveforms above a threshold of ,40 mV or more (noise r.m.s. ,20 mV) were time-stamped and digitized at 32,556 Hz at 24-bit resolution for 1 ms. Light-emitting diodes on the headstage were tracked to obtain the animal’s position and head direction. The local field potential (LFP) was filtered at 1–500 Hz with a running average filter (DCO) and a low-pass FIR filter (64 taps). The LFP signal was digitized at 2,034 Hz. 

After surgery, the tetrodes were moved in small daily increments towards the target area while the rat was resting on a pedestal. One electrode was used to record a reference signal from the superficial layers of the cortex (DV: ,1 mm). Another electrode was used to monitor LFP, in the stratum lacunosum-moleculare for the recordings from the hippocampus, and in the dorsal thalamus (DV: ,5 mm) for recordings from NR. The pyramidal cell layer of CA1 or CA3 was identified during recording by the presence of sharp waves and large-amplitude complex-spike activity. On the day of recording, the electrodes were not moved at all to maintain stable recordings. 

Microdrives for simultaneous NR and CA1 recording were connected to a multi-channel unity gain headstage, which in turn was connected via a counterbalanced cable to an Axona recording system (Axona Ltd). Unit activity was band-pass filtered at 600–6,000 Hz with third-order Bessel filters and amplified by a factor of 5,000–12,500. Spike waveforms above a threshold of ,40 mV or more (noise r.m.s. ,25 mV) were time-stamped and digitized at 48,000 Hz at 24-bit resolution for 1 ms. Tetrodes were lowered in 50-mm steps while the rat rested on the pedestal. The LFP was low-pass filtered at 500 Hz with a sixth-order Bessel filter. The signal was digitized at 4,800 Hz. 

For tetrode recordings with optogenetic manipulations, a 532-nm light pulse was generated from a DPSS laser unit (Shanghai Laser & Optics Century) with a 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

patch cable (FT400UMT; Thorlabs) connected to the animal. Power density was 20–30 mW mm[2][2] at the tip of the fibre. The laser application was controlled with a custom made program in MATLAB (MathWorks) through a NI-DAQ system (USB-6211; National Instruments). Pulse delivery depended on the animal’s position on the maze, which was monitored through a NetCom connection between MATLAB and Cheetah recording software (Neuralynx). Three to four weeks after the virus injection, silencing of cells with laser application was confirmed with tetrodes attached to the optic fibre. Unit activity from the tetrodes on the optic fibre was monitored using an Axona recording system (Axona Ltd). In all animals tested, at least two units in NR showed a significant reduction of spike rate by the laser application (Extended Data Fig. 6). After the animals were sufficiently familiarized with the continuous alternation task, the first recording session (,10 min) started with an optic-fibre patch cable connected to the animal without laser application. After the first session, the animal was at rest for 5 min before the next session, when light was applied for ,10 min. To avoid unnecessary photodamage to the tissue, the laser application was turned off intermittently. The laser application was always on when the animal was running on the central stem and the side arms, but it was turned off when the animal reached the bottom arm. Five seconds after the animal reached the food port, the laser application was restarted, which was approximately 5–10 s before the next run. The laser then continued to be on for the next trajectory. After the session with laser application, the animal was at rest on the pedestal for at least 10 min or in the Plexiglass home cage for ,30 min before a new session was started. The final session (,10 min) was conducted with the optic fibre patch cable connected without laser application. 

Behavioural task on the modified T-maze. Two versions of modified T-mazes are shown in Fig. 1a (110 cm 3 110 cm square-shaped maze and 130 cm 3 130 cm diamond-shaped maze). The mazes were constructed of 12 cm wide wooden runways covered by rubber sheet and with 2 cm high plastic side walls. The central runway (stem) was 100 cm for the square-shaped maze and 120 cm for the diamond-shape maze. Additional wall strips (10 cm length, 2 cm high, 1 cm thickness) were added on both sides at the end portion of the stem to reduce the width of the runway. This helped minimizing the lateral deviation of the animals’ trajectories. Chocolate-taste cereals or cookies were provided on a small dish located at the centre of the bottom arm (Fig. 1a). In contrast to previous studies using this task[6,21] , reward was always given at the same spatial position, irrespective of whether the animals chose left or right trajectories, such that effects of intended movement could be dissociated from effects of the goal location itself. The maze was elevated 50 cm above the ground. It was surrounded by black circular curtains (180 cm diameter) without any visual cues on three sides. The bottom side of the maze was partially open to the recoding room. 

Behavioural training and recordings were performed on one of the mazes. The maze was randomly chosen for each animal. After finishing the recordings on the first maze, some animals with tetrodes in NR or in the hippocampus were further trained and recorded on the other maze. For NR recordings, the same units were typically active across mazes. In those cases, cells were only included into one of the data sets. For recordings from CA1 or CA3, we often observed global remapping of place cells after changing the shape of the maze, and sometimes new units were recruited on the stem. 

Behavioural training started after recovery from surgery. Training started with 1 or 2 days of accommodation where each rat was placed on the maze to freely explore and find food at the food port. In the next stage of training, the animals were instructed to follow a specific direction on the maze—from the stem through a side arm to the food port—by blocking reverse movement with the experimenter’s hands when necessary. Food was available at the food port irrespective of which trajectory the animal chose at this stage. After the animal was familiar with the movement direction rule on the maze, the final stage was to acquire the alternation rule. Reward was provided only when the animal chose the opposite trajectory of the previous trial, irrespective of whether choices were correct or incorrect on the preceding trial. For each day, three to five 10-min sessions were performed. Criterion was reached when choices were correct on 90% of the trials. Trajectory-dependent firing continued to be expressed long after the animals reached the behavioural criterion (for up to 2–3 months). Trajectory dependence emerged without the use of a barrier to instruct correct alternation during the training stage[39] . 

The number of left- and right-preferring neurons (neurons with higher firing rate on trajectories that led to left versus right turns) was balanced (CA1: 48 versus 50 cells; CA3: 16 versus 18 cells; CA1 with NR lesions: 24 versus 20 cells; NR: 34 versus 30 cells; mPFC: 176 versus 162 cells). There was no difference in the number of left- and right-preferring cells within trials (binomial tests with Bonferroni correction, P . 0.05). 

For the delayed alternation task in Fig. 5b, a delay period of either 10 or 15 s was introduced before the animals started running on the stem. The maze was 

equipped with a manually controlled plastic door (25 3 25 cm) on the central stem approximately 25 cm from the start of the stem. In addition, plastic walls (25 cm high) were inserted on both sides of the delay zone to minimize lateral movement (Extended Data Fig. 7c). The animal’s movement was continuously monitored with a custom made program in MATLAB with a NetCom connection to the recording system. When the animal entered the delay zone, a counter was started by the program. Criterion was reached when choices were correct on 80% of the trials. 

Spike sorting and cell classification. All main analyses were performed using MATLAB (MathWorks). Spike sorting was performed offline using MATLABbased graphical cluster-cutting software, MClust (A.D. Redish). Clustering was performed manually in two-dimensional projections of the multidimensional parameter space (consisting of waveform energies and peak–trough amplitude differences). Autocorrelation and cross-correlation functions were used as additional separation tools. For recordings in CA1 or CA3, putative pyramidal cells were distinguished from putative interneurons by spike width and average rate and the presence of bursts. In the continuous alternation task, only cells with a peak firing rate more than 1 Hz on the central stem of the maze on either trajectory were analysed. In the open field, all units with an average firing rate above 0.2 Hz in at least one of the sessions were used for the further analysis. 

To ensure the same cell was not counted multiple times, for recordings in CA1 and CA3, the estimated number of cells recorded on each tetrode was generally based on a single recording session (with tetrodes placed optimally in the cell layer). For a few exceptional animals, a second recording session was conducted in the other shape of the T-maze, but in these cases, only new clusters at the same tetrode position were included. For recordings from NR and mPFC, discrete units were sampled from recording sessions with at least 40 mm separation from the preceding and succeeding recording locations. 

Trajectory-dependent firing on the modified T-maze. For analysis of trajectory-dependent firing on the stem, we first extracted a portion of the stem where the animal’s running speed, head direction and lateral position were not significantly different between left and right trajectories. 95% confidence intervals for multiple comparisons of six bins (with Bonferroni correction) were determined for lateral position on left- and right-turn trajectories and the portion of the central stem with overlapping confidence intervals was extracted for analysis. A segment of 5 cm was further excluded from the top end of the extracted stem portion to guarantee minimal trajectory deviation. For the remaining portion of the stem, we examined the 95% confidence intervals for running speed on leftand right-turn trajectories. If necessary, the trial with the largest deviation of running speed was excluded iteratively until the confidence intervals between trajectories overlapped across the entire selected portion of the stem. The same procedure was applied for head direction. 

To analyse trajectory-dependent firing on the central stem of the T-maze, we divided it into six equally sized bins. The length of individual bins was 8–13 cm, depending on the selected portion of the stem. The following parameters were calculated for each bin of each trial: (1) firing rate: the number of spikes divided by the amount of time spent in the bin; (2) running speed: the averaged position shift per time in the bin; (3) head direction: the averaged angle of two coloured LEDs on the headstage; and (4) lateral position: averaged position perpendicular to the long axis of the central stem. 

For each cell, a two-way ANOVA was conducted with trial type (correct leftand right-turn run) and six bins as independent variables and firing rate as the dependent measure. In the hippocampus, cells with a significant main effect of trial type were identified as potential trajectory-dependent cells. For these cells, a second analysis was performed to examine whether variations in speed, heading, or lateral position might account for the differences in firing rate between trial types. This was examined with a two-way ANCOVA with trial type and bins as the independent variables, firing rate as the dependent measure, and speed, head direction, and lateral position as covariates. Cells that continued to show a significant difference in firing rate between left- and right-turn trials, when the covariates were included in the ANCOVA model, were classified as trajectory dependent[6] . In NR or mPFC, any cell which showed either a significant main effect of trial type or a significant trial type 3 bin interaction with both ANOVA and ANCOCA, was considered a trajectory-dependent cell. 

To create spatial rate maps, spatial positions in the maze were divided into 10 3 10 pixel bins (3 pixels per cm) and the firing rate for each bin was calculated. This was performed only for periods when the animal’s running speed exceeded 10 cm s[2][1] . Instantaneous spike rates were estimated using a Gaussian kernel on the spike data for temporal smoothing. Instantaneous rate was calculated as 

**==> picture [63 x 23] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

where g is a 1D Gaussian kernel, h is a bandwidth, N is the total number of spikes, and ti is the time of the i-th spike. An optimal bandwidth between 50 and 250 ms was determined for each cell by minimizing the mean integrated square error between the estimated rate and the unknown underlying rate[40] . The rate map was smoothed using a 2D Gaussian filter with a bandwidth of one bin (3.3 cm 3 3.3 cm). Bins visited less than 40 ms were excluded. Spike rate at each stem position was estimated using a linear interpolation method applied to temporally smoothed spike rates by the 1D Gaussian kernel. Mean values and 95% confidence intervals of the spike rates were calculated for left- and right- turn trajectories. Peak firing rate and peak firing position were determined. Decoding analysis. A linear decoder, expressed by the following equation, was used to predict the next trajectory from the spike rates on the stem: 

**==> picture [159 x 10] intentionally omitted <==**

**==> picture [128 x 10] intentionally omitted <==**

F is a vector of firing rates for each cell, w is a vector of respective weights, b is a scalar offset, and y is an output value of the classifier (1, 21). Optimal weights of the decoder were determined by a support vector machine algorithm to maximize the separation margin for better generalization performance on any data set by avoiding over-fitting to the training data used for the weight optimization[41,42] . In brief, for a given number N of trials of rate-trajectory pairs, (Fi, yi), i 5 1,2,3,…N, we searched for w that satisfies the following condition, 

**==> picture [69 x 22] intentionally omitted <==**

**==> picture [124 x 10] intentionally omitted <==**

C is a penalty parameter for misclassification. We set C at 1 throughout the decoding analysis but changing the C value to (0.1, 10, 100) did not significantly affect any conclusion. The mean firing rates on each bin were used as for the inputs of the classifier. 

Decoding performance was estimated using a leave-one-out cross-validation, performed as follows. From a given set of trials in a recording session, one trial was randomly chosen as a test data set and the rest of the trials were used as a training data set. The weights of the linear classifier were optimized based on a training data set, and the same weights were applied to the test data for classification. This procedure was repeated for all trials to be tested, and the classification accuracy on the test data sets was considered an estimate of the decoding performance. The decoding performance on error trials was calculated using the weights optimized for all correct trials in the same recording session. 

For decoding analysis in the delayed alternation task in Fig. 5b, the delay period was divided into two temporal bins, corresponding to the first and last halves, and the stem part was divided into four equally sized spatial bins. Decoding performance was estimated using the mean spike rate at each bin. 

To isolate prospective and retrospective components in the alternation task, we analysed a subset of trials with an equal number of correct and error trials, so that we could focus on only one of the components, either prospective or retrospective, while the influence from the other component was cancelled out due to an equal number of left- and right-directed trajectories. The details of this procedure are as follows. 

Suppose that we want to estimate the probability that the animal took a left trajectory on the previous trial using the spike rates on the stem. The probability for correct trials can then be expressed as: 

P(last Ljrate, correct)~P(LRjrate, correct)~1{P(RLjrate, correct) 

where ‘last L’ indicates a left trajectory choice on the previous trial, ‘LR’ indicates the trajectory from the previous left arm to the next right arm, and ‘RL’ indicates the trajectory from the previous right arm to the next left arm. The first term indicates the probability that the animal took a left trajectory on the previous trial, given the spike rates on the stem on correct trials. Note that, if the direction of the last trajectory is given, the next trajectory choice is automatically determined, depending on whether the trial is correct or incorrect. Similarly, the probability for error trials is expressed as: 

P(last Ljrate, error)~P(LLjrate, error)~1{P(RRjrate, error) 

Now the retrospective component of the trajectory representation can be estimated using the following equation: 

P(last Ljrate)~P(correct)|P(LRjrate, correct)zP(error)|P(LLjrate, error) 

P(correct) and P(error) are the probabilities of correct trials and error trials, respectively. Evaluating this equation with all data sets, however, gives a bias 

towards the next right turn, because P(correct) ? P(error). In other words, this equation gives P(last L, next biased to R j rate) when all trials are considered. To cancel out the influence of the next trajectory on the decoding performance, we used a subset of trials with an equal number of correct and error trials. This gives: 

**==> picture [91 x 9] intentionally omitted <==**

**==> picture [201 x 52] intentionally omitted <==**

Here the probabilities P(LR j rate, correct) and P(LL j rate, error) can be obtained using the same decoding procedure as in Fig. 5a, b. A statistical distribution for decoding performance was estimated from 1,000 randomly sampled subsets with an equal number of correct and error trials (a bootstrap resampling method). Similarly, the prospective component of the trajectory representation was estimated as: 

**==> picture [93 x 9] intentionally omitted <==**

**==> picture [203 x 9] intentionally omitted <==**

**==> picture [173 x 38] intentionally omitted <==**

To compare overall firing rates on correct trials and error trials we normalized firing rate on the stem on error trials to firing rates on the stem on correct trials. Normalized firing rates ranged from 0.90 for CA1 to 1.04 for mPFC. Only the CA1 group was significantly different from 1. To test the influence of the lower rate on error trials, the overall firing rates on error trials in the CA1 group were multiplicatively increased by the factor of 1/0.9 in order to match the rates on correct trials. This adjustment did not change the magnitude of the prospective and retrospective components of the firing. 

The number of trials used for decoding analysis on continuous trials (Fig. 5a) was, for mPFC, 1,035 correct trials and 27 error trials; for NR, 1,199 correct trials and 34 error trials; and for CA1, 1,145 correct trials and 25 error trials. The number of cells per session was, for mPFC, 14.9 6 0.9; for NR, 4.5 6 0.2; and for CA1, 6.3 6 0.6. The number of trials for trials with a delay (Fig. 5b) was, for mPFC, 319 correct trials and 29 error trials; for NR, 637 correct trials and 83 error trials; and for CA1, 439 correct trials and 54 error trials. The number of cells per session was, for mPFC, 8.8 6 0.8; for NR, 5.2 6 0.3; and for CA1, 7.0 6 0.6. 

Open-field tests. Animals were tested also in a square box with individually exchangeable walls (black on one side, white on the other side; 100 cm 3 100 cm; 50 cm high). Distal background cues were masked by black curtains encircling the recording box (180 cm diameter). A pedestal, where the rat slept and rested, was placed between the test box and the experimenter outside the curtains. 

Rate remapping was induced in the hippocampus by changing the colour configuration of the recording box while the box was kept at a constant location. The rat was first placed into the black/white box for 10 min, then into the box with opposite colour for two consecutive 10-min sessions, and then back into the original black/white box for a final 10-min session. The rats were allowed to rest for 5 min on the pedestal between the sessions. While the animal was resting, the four walls of the box were flipped and the floor was washed with water. Animals with tetrodes in NR and CA1 were tested in a black–white–white–black sequence of four sessions, using the same box. Animals with tetrodes in mPFC were recorded in a black–white–black sequence of three sessions. 

For all recordings in the open field, spatial rate distributions for each wellisolated unit were constructed by summing the total number of spikes that occurred in a given location bin (5 cm 3 5 cm) and dividing by the amount of time spent in that bin. An adaptive smoothing method was applied for colourcoded rate plots and for the calculation of spatial correlation and peak firing rate to optimize the trade-off between blurring error and sampling error[43] . The firing rate at each bin in the environment was estimated by expanding a circle around the point until 

**==> picture [26 x 18] intentionally omitted <==**

where r is the radius of the circle in bins, n is the number of occupancy samples within the circle, s is the total number of spikes in those occupancy samples and 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

the constant a is set to 10,000. With a position sampling rate of 50 Hz, the firing rate at that point was then set to 50 sn ~~.~~ The maximum value in the smoothed rate map was taken as the peak firing rate of the cell. Spatial information for individual cells was calculated from spike rate maps, using the following equation: 

**==> picture [48 x 20] intentionally omitted <==**

where li is the mean firing rate in the i-th bin, l is the overall mean firing rate and pi is the probability of the animal being in the i-th bin (occupancy in the i-th bin/ total recording time). 

Firing patterns were compared across trials with a spatial correlation procedure. Pearson correlation was measured between the firing rates in common pixels of the two maps for each cell. For comparison of peak rate, the difference of peak rates between boxes divided by the peak rate across the sessions was calculated for each cell. The average value obtained from all possible combinations of sessions with either the same or different colour boxes was considered as representative for each cell. For example, for the sessions with a black 1, white 2, white 3, black 4 sequence, the average value of correlation or rate change between similar session pairs (black 1/black 4 and white 2/white 3) was used as a representative value for the same colour comparison, while the average among different session pairs (black 1/white 2, black 1/white 3, white 2/black 4, white 3/black 4) was used for the different colour comparison. 

Histological procedures and electrode positions. The rats received an overdose of pentobarbital and were perfused intracardially with saline followed by either 4% formaldehyde (vol/vol). The brains were extracted and stored in formaldehyde, and frozen coronal sections (30 mm or 40 mm) were cut and stained with cresyl violet. Each section through the relevant brain region was collected for analysis. All tetrode and optic fibre traces were identified and the tip of each electrode was found by comparison across adjacent sections. The position and extent of the neurotoxic lesions in NR were outlined in Nissl-stained sections throughout the anteroposterior extent of NR. Lesioned tissue was defined by either absence of tissue or stained neurons, and included areas showing picnotic neurons. 

Statistical tests. All statistical tests were two-sided. Data met assumptions about normality when parametric statistics were used. 

Code availability. Code for decoding of subsequent trajectories can be obtained from the authors. 

36. Gradinaru, V., Thompson, K. R. & Deisseroth, K. eNpHR: a Natronomonas halorhodopsin enhanced for optogenetic applications. Brain Cell Biol. 36, 129–139(2008). 

37. Gradinaru, V. et al. Molecular and cellular approaches for diversifying and extending optogenetics. Cell 141, 154–165 (2010). 

38. Zhang, S. J. et al. Optogenetic dissection of entorhinal-hippocampal functional connectivity. Science 340, 1232627 (2013). 

39. Bower, M. R., Euston, D. R. & McNaughton, B. L. Sequential-context-dependent hippocampal activity is not necessary to learn sequences with repeated elements. J. Neurosci. 25, 1313–1323 (2005). 

40. Shimazaki, H. & Shinomoto, S. Kernel bandwidth optimization in spike rate estimation. J. Comput. Neurosci. 29, 171–182 (2010). 

41. Boser, B. E., Guyon, I. M. & Vapnik, V. N. A training algorithm for optimal margin classifiers. Proceedingsofthe fifth annualworkshoponComputationallearning theory 144–152 (1992). 

42. Chang, C. C. & Lin, C. J. LIBSVM: a library for support vector machines. ACM Trans. Intell. Syst. Technol. 2, 3, Article 27, (2011). 

43. Skaggs, W. E., McNaughton, B. L., Wilson, M. A. & Barnes, C. A. Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. Hippocampus 6, 149–172 (1996). 

44. Dolleman-Van der Weel, M. J. & Witter, M. P. Nucleus reuniens thalami innervates gamma aminobutyric acid positive cells in hippocampal field CA1 of the rat. Neurosci. Lett. 278, 145–148 (2000). 

45. Euston, D. R. & McNaughton, B. L. Apparent encoding of sequential context in rat medial prefrontal cortex is accounted for by behavioral variability. J. Neurosci. 26, 13143–13155 (2006). 

46. Lu, L. et al. Impaired hippocampal rate coding after lesions of the lateral entorhinal cortex. Nature Neurosci. 16, 1085–1093 (2013). 

47. Hyman, J. M., Ma, L., Balaguer-Ballester, E., Durstewitz, D. & Seamans, J. K. Contextual encoding by ensembles of medial prefrontal cortex neurons. Proc. Natl Acad. Sci. USA 109, 5086–5091 (2012). 

48. Whitlock, J. R., Pfuhl, G., Dagslott, N., Moser, M. B. & Moser, E. I. Functional split between parietal and entorhinal cortices in the rat. Neuron 73, 789–802 (2012). 

49. Salinas, E. & Abbott, L. F. Coordinate transformations in the visual system: how to generate gain fields and what to compute with them. Prog. Brain Res. 130, 175–190 (2001). 

50. Salinas, E. & Sejnowski, T. J. Gain modulation in the central nervous system: where behavior,neurophysiology,andcomputationmeet. Neuroscientist 7, 430–440(2001). 

51. Cohen, Y. E. & Andersen, R. A. A common reference frame for movement plans in the posterior parietal cortex. Nature Rev. Neurosci. 3, 553–562 (2002). 

52. Moser, E. I. et al. Grid cells and cortical representation. Nature Rev. Neurosci. 15, 466–481 (2014). 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

**==> picture [473 x 648] intentionally omitted <==**

Extended Data Figure 1 | Nissl-stained coronal sections showing tetrode positions in each animal with recordings in CA1, CA3 or NR. Positions of tetrode tracks are indicated by red circles. Rat number, recording region and type of electrode assembly are indicated above each section. 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [455 x 372] intentionally omitted <==**

Extended Data Figure 2 | The influence of rate variability on sorting of high-rate and low-rate trajectories, trajectory coding in CA1 and CA3, and spatial properties of neurons in mPFC, NR and CA1. a, Demonstration of the influence of rate variability on sorting of high-rate and low-rate trajectories in Figs 1d, f, 2d, 3d and 4d. For each cell, the rate variability (s.d.) within the trajectory in which the cell exhibited a higher peak firing rate was estimated. Gaussian noise with the estimated s.d. was then added to the original rate data. The figure shows two sets of data with the addition of independent Gaussian random noise, sorted into high-rate and low-rate trajectories as in Fig. 1d. The colour-code difference between high-rate and low-rate trajectories reflects the rate variability within the same trajectory. These plots are substantially different from the original plots for CA1 (Fig. 1d), NR (Fig. 2d) and mPFC (Fig. 3d) but are similar to the plots for CA3 (Fig. 1f) and CA1 with NR lesions (Fig. 4d), indicating that colour-code differences on the latter plots can be largely accounted by the rate variability within the same trajectory. b, Box 

plot showing CA1–CA3 difference in change of peak rate (left) but not field position (right) in the continuous alternation task. *P , 0.05. c, Distribution of spatial information across cells in CA1, NR, and mPFC (frequency histogram and box plot; *P , 0.05). Spatial information per spike was significantly higher in CA1 neurons than in NR or mPFC neurons (CA1, 1.46 6 0.09; NR, 0.048 6 0.009; mPFC, 0.134 6 0.012 bits per spike (mean 6 s.e.m.); CA1 versus NR, P , 0.001, D 5 0.98; CA1 versus mPFC, P , 0.001, D 5 0.93, Kolmogorov–Smirnov test). Spatial information per spike was also higher in mPFC than in NR (D 5 0.36, P , 0.001, Kolmogorov– Smirnov test) but this difference was not significant when measured in bits per second (D 5 0.07, P 5 0.19), indicating that the difference per spike is largely due to higher firing rates in NR (NR, 7.83 6 1.27 Hz, mPFC, 4.86 6 0.39 Hz (mean 6 s.e.m.)). The total number of neurons analysed was 71 in CA1, 61 in NR, and 164 in mPFC. 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

**==> picture [491 x 543] intentionally omitted <==**

Extended Data Figure 3 | Tetrode positions and localization of trajectorydependent cells in mPFC. a, Positions of tetrode tracks are indicated with red circles. Rat numbers are indicated. b, Spike waveform widths (peak-to-trough time) and mean spike rates on the stem (both trajectories combined) were plotted for each cell in mPFC. Trajectory-dependent cells are indicated in red and trajectory-independent cells in blue. No significant difference was observed in spike widths of the two cell types (D 5 0.071, P 5 0.802, Kolmogorov– Smirnov test) but the mean spike rates of trajectory-dependent cells were weakly—but significantly—higher than those of trajectory-independent cells 

(trajectory-dependent cells, 8.10 Hz; trajectory-independent cells, 5.87 Hz; D 5 0.172 P 5 0.016, Kolmogorov–Smirnov test). c, Percentage of trajectorydependent cells in superficial versus deep layers of mPFC and in prelimbic versus dorsal anterior cingulate areas. The percentage of trajectory-dependent neurons was slightly larger in the dorsal anterior cingulate area than in the prelimbic area (45.3% versus 33.2%, z 5 2.26, P 5 0.024, binomial test). There was no significant difference between superficial and deep layers (32.0% versus 41.0%, z 5 1.54, P 5 0.125). 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [505 x 332] intentionally omitted <==**

Extended Data Figure 4 | Nissl-stained coronal sections showing tetrode positions in CA1 of animals and the extent of their NR lesions. Positions of tetrode tracks in CA1 are indicated by red circles. Right sections show outlines of the lesioned areas (orange) and NR (black dashed line) at different anterior–posterior levels. Note that all lesions are bilateral. Percentage of NR 

lesions (lesioned NR area/total NR area): #15465, 73%; #16214, 68%; #16249, 85%; #16337, 70%. Percentage of lesioned areas specific to NR (lesioned NR area/total lesioned area): #15465, 71%; #16214, 80%; #16249, 73%; #16337, 80%. 

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

**==> picture [454 x 372] intentionally omitted <==**

Extended Data Figure 5 | Effect of removal of NR input on behaviour, spike rates and local field potentials in CA1. a, Left, behavioural performance (percentage of correct trials) on the continuous alternation task in control animals and animals with NR lesions. No significant difference was observed (x1[2][5][ 1.76,][ P][ 5][ 0.184; Kruskal–Wallis test). Right, number of days required for] animals to reach behavioural criterion (correct trials .90%; t14 5 0.236, P 5 0.817). b, No significant difference was observed between control and NRlesioned animals in mean running speed on the stem (t19 5 0.403, P 5 0.692). c, The mean spectral power of the local field potentials recorded in the CA1 pyramidal layer was not different between control and lesioned animals. The plots show mean values (solid lines) with 95% confidence intervals (shaded areas). d, Left, change in field position across alternating trajectories for CA1 place cells recorded in control animals and animals with NR lesions. Right, box plots showing difference in changeof peak rate between CA1 in control animals and CA1 in animals with NR lesions (top; D 5 0.346 P , 0.001, Kolmogorov– Smirnov test). There was no corresponding change in field position (bottom; D 5 0.083, P 5 0.982 Kolmogorov–Smirnov test). *P , 0.05. e, Behavioural performance did not change during laser stimulation in NR in eNpHRexpressing animals (x2[2][5][ 2.77,][ P][ 5][ 0.250; Friedman test).][ f][, Running speed] on the stem did not change significantly during laser application (F2,28 5 0.89, P 5 0.423, repeated-measures ANOVA). g, Mean firing rates of place cells on the stem (both trajectories combined) did not change significantly during 

laser application but were significantly reduced after termination of the stimulation (F2,28 5 6.52, P 5 0.002, repeated-measures ANOVA; before versus during: t49 5 1.651, P 5 0.105, during versus after: t49 5 2.137, P 5 0.038, post hoc paired t-test). The lack of a consistent reduction in CA1 mean firing rate during light application probably reflects the fact that excitatory inputs from NR to CA1 terminate not only on pyramidal cells but also on local inhibitory neurons[44] . h, Spectral power of local field potentials in the CA1 pyramidal layer was not significantly changed by laser application in NR (before/during laser application, mean 6 s.e.m. mV[2] Hz[2][1] in a decibel scale): delta (1–4 Hz): 37.3 6 0.92/37.6 6 0.99; theta (6–11 Hz): 41.8 6 1.08/41.4 6 1.18: slow gamma (25–50 Hz) 31.6 6 0.41/31.7 6 0.42; fast gamma (60–90 Hz): 26.1 6 0.53/26.2 6 0.53). The plot shows mean values (solid lines) and 95% confidence intervals (shaded areas). i, Left, field position shift between alternating trajectories (frequency histograms and box plots). Right, box plots showing difference in change of peak rate (top; F2,98 5 12.02, P , 0.001, repeated-measures ANOVA), but not field position (bottom; F2,98 5 0.02, P 5 0.983). Before laser stimulation, the rate change between left and right laps among place cells that expressed significant trajectory-dependent firing was 52.0 6 5.1% (mean 6 s.e.m.). During stimulation, the rate change dropped to 38.6 6 4.4% (t33 5 4.04 P , 0.001; paired t-test, two-tailed). The effect recovered to baseline levels after the laser application was terminated (55.0 6 3.9%; t33 5 4.81, P , 0.001; paired t-test). 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [508 x 612] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Extended Data Figure 6 | Nissl-stained coronal sections showing positions of tetrodes and optic fibres in optogenetic experiments. The figure is organized into six blocks, one for each of six animals. Five-digit animal numbers are indicated above each block. Top two rows of each block, positions of tetrode tracks (red circles) in CA1 of each animal. Bottom left, position of optic fibre above NR (red rectangular outline). NR is indicated by a black dashed triangle. The tip of the fibre was placed near the midline to silence cells at both sides of the midline. The bottom right panels of each block show spike rates for two representative units on the tetrodes attached to the optic fibre (.,750 mm from the tip of the fibre). The two panels show mean values (solid line) and 95% confidence intervals (shaded areas) of spike rate, with spike rasters at the top. The 532 nm laser was applied for 5 s (0–5 s on the x axis). A significant reduction of spike rate was observed during laser application for all units in this figure (P , 0.05, t-test). Unlike the ibotenic-acid lesion, which destroyed 68–85% of the NR, the laser light probably reached only a small 

portion of the nucleus. The total volume of NR is roughly 2 mm[3] (1 mm of width, 1 mm of height, and 2 mm of length). Supposing that the tip of the optic fibre was located 250 mm above NR, that the laser light suppressed activity up to 1 mm below the fibre tip (optic fibre 0.39 NA, core size Ø 400 mm), and that all cells within this region were inactivated, the estimated proportion of NR affected by the laser light would be ,36% at the most. The tetrodes attached to the optic fibre were positioned approximately 750 mm below the fibre tip, near the distance limit of laser light for activation of halorhodopsin. At this depth, the intensity of the laser was probably not sufficient to activate halorhodopsin maximally. The sub-maximal activation probably accounts for the relatively slow time course of NR silencing (sometimes . 1 s). Another contributing factor may be that thalamic neurons express T-type calcium channels, which are de-inactivated by hyperpolarization, making the neurons more excitable[27] . This excitation may retard the suppression of NR activity. 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [509 x 621] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Extended Data Figure 7 | Trajectory coding in CA1, CA3 and CA1 of NRlesioned animals, and influence of behavioural variables on the decoding analysis. a, Decoding of succeeding trajectory using peak firing rates of CA1 or CA3 place cells with firing fields on the stem as inputs to a linear classifier. Only trials with correct choices are included. Decoding performance was estimated from randomly selected cell groups in the entire data set across animals and plotted as a function of number of neurons in the sample. The plot shows mean (solid lines) 6 s.e.m. (shaded areas). Significant differences between CA1 versus CA3 or CA1 versus CA1 with NR lesions are indicated by dashed lines at the top (P , 0.05). To estimate the decoding performance for a specific number of cells, the desired number of cells was randomly selected from the entire data set across all animals. As the total trial number of runs on left- or right-run trajectories was often different across the recording sessions from which the cell group was taken, we randomly subsampled the trials to equalize the total trial number across sessions. This subsampling procedure was performed ten times, decoding performance was acquired for each, and the average was taken as an estimate of the decoding performance of the cell group. Then, a different cell group with the same number of cells was randomly selected and the same procedure was performed. The procedure was repeated 1,000 times to acquire a statistical distribution of decoding performance for the given number of cells (bootstrap resampling method). P values were estimated from the bootstrap distributions. The peak firing rates of approximately 15 CA1 place cells on the stem provided sufficient information to indicate a correct succeeding trajectory with over 90% accuracy (96.6 6 4.3% with a total of 30 cells, mean 6 s.e.m.). The decoding accuracy was significantly lower when CA3 cells or CA1 cells from NR-lesioned animals were used as inputs to the classifier (decoding performance with 30 cells: CA3, 69.9 6 7.0%; NR-lesioned, 76.9 6 7.6%). These results suggest that, for correct choices, the subsequent trajectory can be read out reliably from the collective firing of place cell ensembles in CA1 of animals with intact NR–CA1 connections. b, Left, decoding of correct subsequent trajectory using firing rates of CA1 place cells from NR-lesioned animals as inputs to the classifier. Trials with correct choices and error trials are shown separately (number of trials analysed for animals with NR lesions: correct, 467; error, 23; cell number per session, 7.5 6 0.9 (mean 6 s.e.m.)). Symbols as in Fig. 5a. We also estimated the decoding performance using peak firing rates on the stem (without binning). In the CA1 of lesioned animals, the decoding performance was not significantly different 

between correct trials and error trials (67.2 6 2.2% versus 69.6 6 9.8%; mean 6 s.e.m.). In CA1 of control animals, performance was 80.5 6 1.2% on correct trials and 56.0 6 10.1% on error trials (interaction term in a logistic regression analysis with task performance (correct versus incorrect) and manipulation (control versus NR lesion) as coefficients, Z 5 2.08, P 5 0.038; post hoc binomial test for correct versus incorrect trials: NR lesion, Z 5 0.232, P 5 0.816; control, Z 5 3.03, P 5 0.002). Right, retrospective and prospective components estimated from spike rates of CA1 cells in animals with NR lesions. Symbols as in Fig. 5c. NR lesions specifically disrupted the prospective component of the trajectory representation (50.6 6 4.9% successful decoding of succeeding path on the last half of the stem, compared to 59.5 6 4.7% in intact animals; chance level 50%), supporting the idea that the mPFC–NR–CA1 circuit is necessary for the hippocampus to access to the information about intended actions. The retrospective component was still decodable (60.1 6 4.9% successful decoding of retrospective paths on the last half of the stem, compared to 63.5 6 4.8% in intact animals), suggesting that CA1 cells with residual trajectory dependence after NR lesions exclusively represent the animal’s trajectory on the preceding trial. c, d, Differences in decoding performance are not caused by differences in running speed, head direction or lateral position. c, Differences in running speed, head direction, and lateral position between left- and right-turn trajectories were assessed across all recording sessions used for the decoding analysis. No significant differences in any of these behavioural variables were observed (P . 0.05, t-test with Bonferroni correction for multiple comparisons of six bins). The plot shows mean 6 s.e.m. Standard errors were estimated for each recording session. d, While we did not observe any significant difference in any of the above behavioural variables, we still observed small systematic trends, as shown in c. To exclude the possibility that these small trends have an influence on the decoding performance[45] we generated, for each variable, a subsampled data set by excluding iteratively the trial with the largest deviation until we obtained nearly the same mean value for the respective behavioural variable on left- andright-turn trajectories. The decoding performance wascalculated from this subsampled data set and the result was compared to the one from the original data set. No significant difference in decoding performance was observed between the groups, suggesting that the small and non-significant differences of behavioural variables do not account for the differences in firing on left and right trials and the decoding that results from these differences. 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [469 x 688] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Extended Data Figure 8 | Firing rates in NR and mPFC fail to distinguish between discrete environments. We have shown that CA1 cells encode intended trajectories by differences in firing rate rather than firing position. A similar rate-based coding scheme has been observed in place cells of freely foraging animals trained to distinguish between open-field environments differing in colour or shape but not location (with similar rate differences following changes in colour or shape)[22,24] . Based on this similarity, we asked whether activity in mPFC and NR accounts for rate differences also between discontinuous environments. We recorded simultaneously 51 place cells from CA1 and 49 cells from NR during free running in a pair of differently coloured square boxes located at the same place in the room (three rats). A total of 176 cells were recorded from mPFC in a different set of animals (two rats). a, Colour-coded rate maps for a representative sample of simultaneously recorded cells in CA1 andNRon consecutivetrialsof free foraging in thesquare enclosure. Cartoons on top indicate the sequence of trials with different box colours (black–white–white–black). Boxes were always in the same location. Note strong rate remapping (change in firing rate but not firing location) in CA1 but no rate code in NR. b, Colour-coded rate maps for cells in mPFC. 

Symbols as in a. Note lack of change in firing rate. c, Top, change in peak firing rate between trials with similar (blue) or different (red) colour configuration. Bottom, spatial correlation between trials. The rate change between the two environments was significant in CA1 (same versus different colour, peak rate change t100 5 6.40, P , 0.001) but not in NR (t96 5 0.875, P 5 0.38) or mPFC (t350 5 0.924, P 5 0.36). Taken together, these results suggest that changes in the distribution of firing rate in CA1 can have multiple sources. While mPFC–NR inputs may be necessary for trajectory selection, the change in rate distribution between discrete environments may depend on other hippocampal inputs, such as those from the lateral entorhinal cortex[46] . In the foraging task, the firing rates of the mPFC and NR neurons are modulated by subsequent direction of movement, mirroring their trajectory-dependent firing in the alternation task (Extended Data Fig. 9), but because trajectory directions are variable in this task, trajectory-dependent activity is likely to be cancelled out in time-averaged rate maps. The colour-reversal task should be sufficiently sensitive to detect influences of discrete stimuli, considering that mPFC cells do respond to such changes under other conditions[47] . 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [497 x 689] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Extended Data Figure 9 | Activity of neurons in mPFC and NR correlates significantly with movement direction in the continuous alternation task and the open field environment. a, Spike-rate maps based on the animal’s selfmovementweregeneratedbypreviouslypublishedprocedures[48] .Inbrief,position and head direction data were smoothed with a 25-sample quadratic local regression (loess) fit. Changes in the animal’s position and heading were calculated between the start and end of a sliding 100 ms time window to generate movement vectors. Movement vectors in each map were binned at 4 cm s[2][1] 3 4 cm s[2][1] . The self-motion rate map was generated by dividing the sum of spiketriggeredmovement vectors by the total number of movement vectors at each bin, which was smoothed by a 2D Gaussian filter with a bandwidth at 1.5 bin. To understand the temporal relationship between spike timing and the animal’s prospective or retrospective motion, spike-triggered movement vectors were generated from movement vectors that were systematically time-shifted relative to spike time, from one second before to one second after the spike event. Top, colour-coded rate maps for a representative mPFC cell which was tuned to left forward movement in the open field environment. Bottom, colour-coded rate maps for a representative NR cell that was tuned to right forward movement. b, Self-movement information inspikes was estimated using the following equation: 

**==> picture [50 x 21] intentionally omitted <==**

where li is the mean firing rate in the i-th bin, l is the overall mean firing rate and pi is the probability of the animal being in the i-th bin (occupancy in the i-th bin/total recording time). Shaded areas indicate the range of the values (mean 6 s.e.m.) obtained from a shuffled data set generated by shifting spike timings either 12 s or 22 s across the session, which will disrupt spiketriggered movement information but maintain spike number and spike patterns. The time periods when spikes provide significant information about self-centred movement direction compared to the results from the shuffled data set are indicated by dashed lines at the top (P , 0.05, t-test). c, Selfmovement rate-map stability within a recording session. The behavioural session (10 min) was divided into first and last halves and Spearman’s correlation between self-movement maps generated from each half was calculated. Significant map stability was observed around the spike time both in mPFC and NR (compared to the shuffled data set, P , 0.05, t-test), indicating that spikes provide reliable information about self-movement. d, Two representative examples of mPFC cells recorded both in the alternation task and in the open field. While these cells expressed a similar trend of preferred self-movement direction across the tasks, they exhibited stronger self-movement tuning in the alternation task than in the open field exploration. 

> G2015 Macmillan Publishers Limited. All rights reserved 

ARTICLE RESEARCH 

**==> picture [405 x 426] intentionally omitted <==**

> G2015 Macmillan Publishers Limited. All rights reserved 

RESEARCH ARTICLE 

Extended Data Figure 10 | Conjunctive coding of position and trajectory increases representational dimensionality in CA1. Trajectory-dependent coding is not necessary for performance in the continuous version of the alternation task because animals with complete hippocampal lesions are unimpaired in this task[21] , as were theanimals with lesions oftheNR input to the hippocampus in thepresent study.The continuous alternation task may thus be too simple for decision behaviour to be affected by lesions of the NR–CA1 system. To examine how trajectory-dependent firing might contribute to navigation behaviour, we estimated the representational advantage of encoding space with trajectory-dependent place cells instead of separate cell populations for trajectory and location. It has been suggested that nonlinear integration of multimodal information in individual neurons enhances the capacity of downstream neurons to classify combinations of features of high-dimensional information[35] . Similarly, we hypothesized here that a key advantage of trajectory-dependent place cells in CA1 is the enhancement of the classification capacity for position–trajectory combinations in efferent neurons, an advantage that may not be evident in an alternation task with only a single choice point. a, Example of a task that requires discrimination of multiple position–trajectory combinations. For successful performance, animals choose a right-turn path at the first choice point in A and then a left-turn path at the next choice point in B. b, To perform the task in a, the brain might use cells that represent correct combinations of movement direction and position on the trajectory.An examplecell mightbeactivewhen theanimalplans a rightpath at position A as well as a left path at position B, but not otherwise. c, Suppose that cells with activity on the stem can be categorized into three classes: trajectorydependent non-place cells, trajectory-independent place cells, and trajectorydependent place cells. The neural activity in b cannot be generated from any linear combination of the two former classes (trajectory-dependent non-place cells and trajectory-independent place cells), as shown in the following argument. Suppose that the activity patterns of trajectory-dependent non-place cells, either right turn or left turn, can be expressed by the following activity matrices, with each row representing future trajectory, right or left, and each column showing position, that is, A or B: 

**==> picture [94 x 21] intentionally omitted <==**

Similarly, activity of trajectory-independent place cells, with firing fields on either position A or B, can be expressed as follows: 

**==> picture [94 x 21] intentionally omitted <==**

The activity matrix of a downstream neuron driven by a linear combination of the above four types of neurons can be expressed as follows: 

**==> picture [198 x 21] intentionally omitted <==**

For the downstream neuron to express the desired activity in b, the following conditions are required: 

**==> picture [76 x 21] intentionally omitted <==**

**==> picture [146 x 69] intentionally omitted <==**

where h is the threshold of activity. However, summation of (1) and (4) gives wazwbzwczwdw2h, whereas summation of (2) and (3) gives wazwbzwczwdƒ 2h, resulting in a contradiction. Thus, neurons with pure selectivity alone cannot generate the desired activity. To achieve the activity in b, neurons with nonlinear mixed selectivity, namely trajectorydependent place cells, are required (also see ref. 35). d, To estimate the number of implementable patterns in the recorded CA1 neurons, firing rates of neurons at each of 12 behavioural states (six stem positions with two future trajectory directions) were analysed. In addition to the recorded activity, we extended the data using a resampling procedure[35] . Resampling was performed by cyclic permutation of firing rates across stem positions. Supposing that the original activity of the recorded neurons is represented by sequential numbers of six stem positions as (1 2 3 4 5 6), five sets of new activity were generated by exchanging activity across stem positions, resulting in (2 3 4 5 6 1), (3 4 5 6 1 2), (4 5 6 1 2 3), (5 6 1 2 3 4) and (6 1 2 3 4 5). Resampling not only increased the number of neurons for analysis, but also minimized spatial bias of ensemble representations across stem positions. Following resampling, decoding performance was calculated for all binary combinations of 12 states (2[12] 5 4,096 patterns), using a linear classifier with firing rates in each behavioural state as inputs, as in Fig. 5. e, The number of implementable patterns was determined for neurons in CA1, CA3, and CA1 from animals with NR lesions, and from CA1 of NR-lesioned animals combined with NR cells from intact animals. For the latter group, the total number of cells was doubled after combining the same number of cells from two populations, as indicated on the x axis with a different colour. A binary pattern was considered as implementable if the decoding performance was better than 99%. For each sample size, cells were randomly selected five times to estimate the standard deviation of the decoding performance. Plots indicate mean 6 s.d. Regardless of the size of the cell sample, the analysis showed a significantly larger number of implementable patterns for CA1 than for the other groups, including the combination of trajectory-dependent cells in NR and nontrajectory-dependent place cells in CA1, suggesting that integration of NR inputs in CA1 place cells is a key step to achieve high-dimensional representations. The results point to trajectory-dependent place cells and the mPFC–NR–CA1 circuit as possible elements of the neural circuit for discrimination of complex position–trajectory combinations, such as the one illustrated in a. Combinatorial coding provides a computational basis for efferent neurons to perform addition or subtraction among vectors in different coordinate systems[49–51] , such as the allocentric reference frame imposed by spatial cells in the entorhinal cortex[52] and the egocentric trajectory frame dependent on projections from mPFC through NR. Such vector operations may be essential for the network to estimate a future allocentric position, which is one of the key steps of route planning during goal-directed navigation. 

> G2015 Macmillan Publishers Limited. All rights reserved 

