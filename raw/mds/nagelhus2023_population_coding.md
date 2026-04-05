Article 

## Object-centered population coding in CA1 of the hippocampus 

## Highlights 

- d Up to 620 CA1 cells were recorded simultaneously during foraging in rats 

- d The majority of cells changed their firing pattern when an object was introduced 

- d Population activity reorganized around the object in a distance-dependent manner 

- d The response to the object was distributed and did not depend on specific cells 

## Authors 

Anne Nagelhus, Sebastian O. Andersson, Soledad Gonzalo Cogno, Edvard I. Moser, May-Britt Moser 

## Correspondence 

soledad.g.cogno@ntnu.no (S.G.C.), edvard.moser@ntnu.no (E.I.M.), may-britt.moser@ntnu.no (M.-B.M.) 

## In brief 

Objects are crucial for guiding navigation. Nagelhus, Andersson, et al. show that CA1 cells change their spatial firing pattern in response to salient objects in the environment. At the population level, these changes are widely distributed and smoothly organized according to the animal’s distance from the object. 

**==> picture [17 x 17] intentionally omitted <==**

Nagelhus et al., 2023, Neuron 111, 2091–2104 July 5, 2023 ª 2023 The Author(s). Published by Elsevier Inc. https://doi.org/10.1016/j.neuron.2023.04.008 

**ll** 

**ll** OPEN ACCESS 

**==> picture [46 x 35] intentionally omitted <==**

## Article 

## Object-centered population coding in CA1 of the hippocampus 

Anne Nagelhus,[1][,][3] Sebastian O. Andersson,[1][,][2][,][3] Soledad Gonzalo Cogno,[1][,][4][,][5][,] * Edvard I. Moser,[1][,][4][,][5][,] * and May-Britt Moser[1][,][4][,][5][,][6][,] * 

1Kavli Institute for Systems Neuroscience and Centre for Algorithms in the Cortex, Norwegian University of Science and Technology (NTNU), Trondheim, Norway 

2Present address: Max Planck Institute for Brain Research, Frankfurt, Germany 

3These authors contributed equally 

4These authors contributed equally 

5Senior author 

6Lead contact 

*Correspondence: soledad.g.cogno@ntnu.no (S.G.C.), edvard.moser@ntnu.no (E.I.M.), may-britt.moser@ntnu.no (M.-B.M.) https://doi.org/10.1016/j.neuron.2023.04.008 

## SUMMARY 

Objects and landmarks are crucial for guiding navigation and must be integrated into the cognitive map of space. Studies of object coding in the hippocampus have primarily focused on activity of single cells. Here, we record simultaneously from large numbers of hippocampal CA1 neurons to determine how the presence of a salient object in the environment alters single-neuron and neural-population activity of the area. The majority of the cells showed some change in their spatial firing patterns when the object was introduced. At the neural-population level, these changes were systematically organized according to the animal’s distance from the object. This organization was widely distributed across the cell sample, suggesting that some features of cognitive maps—including object representation—are best understood as emergent properties of neural populations. 

## INTRODUCTION 

Objects and landmarks are crucial for guiding navigation and must be part of the brain’s cognitive map of space.[1] A long history of work has shown that objects influence spatial firing in the hippocampus in a variety of ways. In place cells,[2][,][3] the number, size, position, and directionality of firing fields may be changed when a salient object is introduced in the environment.[4–9] The hippocampus has also been reported to have cells with specific firing at the location of the object.[5][,][10] These ‘‘object cells’’ consistently move their firing fields along with the object when the object is moved. 

One synapse upstream of the hippocampus, in the medial entorhinal cortex (MEC), specialized cells fire whenever the animal is at a fixed distance from the object in a given direction (i.e., the cell’s firing location is given by a vector between the animal and the object).[11][,][12] These ‘‘object-vector cells’’ fire independently of the object’s shape, size, and identity. A similar set of cells, ‘‘landmark-vector cells,’’ has been reported in the hippocampus[13][,][14] but these cells only began to fire at fixed distances and directions from objects after the animal gained experience with the object.[13] However, limited amounts of data made it difficult to characterize the nature of these cells in a systematic manner. 

Despite numerous studies on object coding in the hippocampus, the exact nature of object representation remains unclear. Early studies used limited quantitative criteria to identify object 

cells and landmark-vector cells. Moreover, cells in the hippocampus often show complex responses that lack a simple relationship with the object location.[7][,][15] In the present study, we considered the possibility that information about the presence and location of the object is expressed in the collective activity of the hippocampal population in ways that cannot be extracted from the firing of individual neurons.[16–18] Thus, with access to spike activity from almost 1,200 unique principal neurons and more than 600 neurons recorded simultaneously, we set out to determine how the presence of objects influences population activity in the CA1 area of the hippocampus in freely moving rats. We report that population activity shows a strikingly smooth organization according to the animal’s distance from the object. 

## RESULTS 

Object cells and object-vector cells in the hippocampus To investigate single-cell and population coding of objects in the hippocampus, we implanted tetrodes or Neuropixels probes in the CA1 of rats (7 and 2 rats, respectively; Figure S1) and recorded activity daily for four trials as the rats foraged in a 150 cm 3 150 cm open field arena (Figure 1A). Each session began with an empty box trial (no object [NO]). Then, on the second trial (object [O]), a multi-colored Duplo tower 52 cm 3 10 cm 3 10 cm (height 3 width 3 length) was placed in the arena. On the third trial (object moved [OM]), the object was 

**==> picture [17 x 17] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 ª 2023 The Author(s). Published by Elsevier Inc. 2091 This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

Article 

## **ll** 

OPEN ACCESS 

**==> picture [323 x 555] intentionally omitted <==**

Figure 1. Object-tuned cells in CA1 

(A) Schematic of experimental protocol. Each recording session consisted of four consecutive trials where rats foraged freely in the same 150 cm 3 150 cm open field arena. In the two middle trials (object [O] and object moved [OM]), a Duplo tower was placed into the environment (red squares). 

(B) Schematic of iterative template matching procedure that we used to identify cells that fired at the object (object cells; top row) or at fixed distances and directions from it (object-vector cells; bottom row). (Left) In each iteration, we placed a Gaussian template at a specific location in the O trial, moved it to the same location relative to the object in the OM trial, and then calculated the Pearson correlation between rate map and template in the two trials separately. (Right) We repeated this procedure with the template offset from the object location in different directions (8 offsets from 10 to 60 cm and 8 cardinal directions) and for 8 different variances of the Gaussian firing field (not shown). For each repetition, the minimum of the two Pearson correlations was taken as an ‘‘object-tuning score’’. 

(C) Distribution of object-tuning scores (n = 1,189 unique CA1 cells). Blue bars, cells classified as object-tuned cells; gray bars, cells not classified as object-tuned. 

(D) Polar scatter plot showing orientation (polar axis, in degrees) and distance (radial axis, in cm, red) of object-tuned cells (one dot per cell). 

(E) Color-coded firing rate maps from example object cell (top) and example object-vector cell (bottom). Object locations are indicated by the white square. Object-tuning score is indicated at the left and peak firing rate at the bottom of each rate map. 

(F) Orientation coverage of firing fields of objecttuned cells as a function of distance to object. The nearer the cell’s firing field is to the object, the larger is the orientation coverage. 

(G) Object-tuning score as a function of the number of days the animal had been exposed to the object (day #) for all cells recorded across different days and that were identified as object-tuned at least in 1 day (n = 62). Each dot indicates a cell. 

(H) Color-coded matrix showing object-tuning scores as a function of recording day in two different rooms for 35 object-tuned cells that were recorded on 2 days or more. Left column, objecttuning scores the 1st day the cells were recorded (‘‘day 0’’). Middle and right column, object-tuning scores for the same cells on additional days in the same room (room A) or in a different room (room B). Only 11 of the 35 cells (31.4%) passed the criteria for object-tuned cells on more than 1 day (cells indicated by blue asterisks). Gray regions indicate that the cell was not recorded on the specific day. Bar, range of object-tuning scores (lighter colors, high score; darker colors, low score). 

moved to a new, semi-random location, before it was taken out from the box for the last trial (no object[0] [NO[0] ]). 

We first set out to identify individual cells with activity related to the presence of the object. We developed an iterative template 

matching procedure (Figure 1B) that identified cells with objectrelated activity (‘‘object-tuned cells’’) regardless of whether they fired at the location of the object (object cells)[5][,][10] or at fixed distances and directions from the object (object-vector or 

2092 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

landmark-vector cells).[11–14] In this procedure, a Gaussian template was placed successively at 65 locations and at 8 different widths in each location in the O and OM trials (Figure 1B; STAR Methods). For each iteration, the correlation between rate map and template was determined for each trial. The smallest of the two correlations was then taken as the iteration’s object-tuning score. We classified a cell as object-tuned cell if at least one of the 65 3 8 scores was larger than the 99[th] percentile of a shuffled distribution created by randomly choosing the template location in both trials. 

Using the template matching procedure, 19.9% of CA1 cells were classified as object-tuned (237/1,189 cells) (Figures 1C, S2A, and S2B). This fraction was significantly higher than a chance level determined by running the same template matching procedure on control trials without objects (11/219 cells, 5.03%; 19.9% compared to chance level of 5.03%, p < 5.73 3 10[�][141] , binomial test). The firing fields of the object-tuned cells covered a wide range of distances from the object (range: 4.8–80.7 cm; mean ± SD: 37.7 ± 16.0 cm) and the entire azimuthal range (Figure 1D). We did not observe a correlation between the proximodistal recording location and the percentage of cells classified as object-tuned (Figures S1 and S2C). Object-related activity was present also in CA3[13][,][19] (Figures S1 and S3). 

To enable a rough comparison between the present dataset and previous literature, we estimated that 4.1% of all recorded cells were object cells (49/1,189 cells, object-tuned cells with firing fields <15 cm from the object, Figure 1E top) and 13.3% were object-vector cells (158/1,189 cells, object-tuned cells with firing fields R15 cm distance from the object, Figure 1E bottom) (note that in 30 object-tuned cells, firing fields could not be detected because the object-related activity was not confined to contiguous regions—these 30 cells were therefore not classified as object cells or object-vector cells; see STAR Methods for details). While object cells have fields covering all orientations around the object (Figure 1F),[5][,][10] the data suggest a continuum between object cells and object-vector cells (Figures 1E and 1F). We observed no significant effect of day of exposure to the object on the object-tuning score (Figure 1G) (r = �0.080, p = 0.57369, Pearson correlation). 

We next asked if the object responses were stable across time and environments. A total of 35 object-tuned cells were recorded on more than 1 day (in room A and room B) (Figure 1H). Only 13 of these cells (31.4%) had significant object-tuning scores on more than 1 day (Figure 1H). However, object-tuned cells were more stable than expected by chance, with higher probability of passing the classification on later days compared to other cells (13/35 object-tuned cells vs. 36/370 other cells, p = 3.35 3 10[�][4] , binomial test). In addition, during the course of a single trial, cells with larger object-tuning scores tended to be more stable than cells with lower scores (Figure S2E) (Pearson correlation between within-trial stability and object-tuning score, r = 0.45, p = 3.65 3 10[�][13] ), pointing to the existence of a discrete cell class with transient object-tuning. 

## The majority of hippocampal cells change spatial firing patterns in the presence of objects 

Many CA1 cells that did not pass criteria for object-tuned cells still responded in some way or other to the object (Figure 2A). In 

the cell sample as a whole, introducing the object led to larger changes in spatial firing patterns (i.e., smaller Pearson correlations of rate maps) than in pairs of control trials with no object (Figures 2B, 2C, and 2D, top left; NO-O vs. CON1-CON2: z = 12.17, p = 4.75 3 10[�][34] , Wilcoxon rank-sum test). While firing locations changed, the overall rate change, estimated as the mean firing rate in the less active trial divided by mean firing rate in the more active trial (rate overlap), was not different between trial pairs with objects (NO-O) and control trials (CON1-CON2) (Figure 2D, top right; z = 0.57, p = 0.57, Wilcoxon rank-sum test). Using a shuffling procedure to determine chance levels (see STAR Methods), we estimated that 67.5% of the cells (n = 803/1,189 cells) expressed either spatial change, rate change, or both between NO and O. Considerable change was also observed between the O and OM trials (Figure 2D, second row; O-OM vs. CON2-CON3; spatial correlation: z = 13.23, p = 5.87 3 10[�][40] ; rate overlap: z = 3.43, p = 0.001, Wilcoxon rank-sum tests). In these trials, 69.7% of the cells changed their spatial firing pattern, firing rate, or both when the object was moved (n = 829/1,189 cells). Major changes were evoked also when we removed the object (Figure 2D, third row; OM-NO[0] vs. CON3-CON4; spatial correlation: z = 11.85, p = 2.11 3 10[�][32] ; rate overlap: z = 1.79, p = 0.074, Wilcoxon rank-sum tests). Upon removal of the object, many cells retained firing fields from the preceding trial, consistent with previous observations of hysteresis in CA1 place cells[13][,][20][,][21] (Figures 2A and S4). In line with this observation, major changes in spatial firing were also observed between NO and NO[0] (Figure 2D, fourth row; NO-NO[0] vs. CON1CON4; spatial correlation: z = 11.85, p = 2.11 3 10[�][32] , Wilcoxon rank-sum test). 

We observed extensive changes in firing locations and rates also in CA3 (Figures S3D–S3F). 

## Decoding the presence of an object from neuralpopulation activity 

To determine the extent to which information about object location is present in the collective firing of hippocampal neurons, we first reasoned that if hippocampal population activity contains object-related information, we would be able to use population activity to decode whether an object is present in the environment. For all decoding analyses, we used recordings from 15 tetrode sessions with 25–39 cells in each recording and 2 Neuropixels sessions with 620 and 135 cells, respectively, unless otherwise indicated (total of 4 rats). Building upon an existing Bayesian decoding algorithm,[22] we developed an approach where we fed data from the NO trial and the O trial into a decoder, which classified testing data into either of these two types of trial (Figure 3A). The decoding accuracy was above chance (50%) in all experimental sessions (Figure 3B), showing that we can infer the presence of the object using population activity. The decoder’s performance increased approximately logarithmically with the bin size of the testing data vector (Figure 3C) and the success of decoding increased with the number of cells included (Figure 3D). We chose 1 s bins for the main analyses because performance saturated around this level (Figure 3C). As expected from the trace analysis, we were also able to decode the NO trial from the NO[0] trial using population activity (Figure S5A). 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 2093 

**==> picture [76 x 35] intentionally omitted <==**

**==> picture [63 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>OPEN ACCESS<br>**----- End of picture text -----**<br>


**==> picture [47 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [237 x 275] intentionally omitted <==**

**----- Start of picture text -----**<br>
A D<br>B<br>C<br>**----- End of picture text -----**<br>


**==> picture [198 x 65] intentionally omitted <==**

Figure 2. CA1 cells change spatial firing patterns in response to objects 

(A) Color-coded firing rate maps of 4 example cells recorded in CA1 (experimental protocol as in Figure 1A). The red square indicates the object. The first cell changes its spatial firing pattern only upon introduction of the object (top row). The second cell changes its spatial firing pattern when the object is introduced but it preserves the firing pattern during the next trials, leaving a trace of the original firing field (second row). The third cell changes its firing pattern when the object is moved and maintains a trace on the last trial (third row). The fourth cell changes its firing pattern when the object is moved, but the spatial firing pattern is more diffuse than in the other cells (last row). Rat ID and cell ID are indicated to the left of the firing rate maps, and peak firing rate in each trial is indicated at the top of each rate map. Bars, color-coded firing rate. 

(B) Control experiments used to compare object-induced changes to changes that occur due to passage of time. Four consecutive trials were run with rats foraging freely in the same 150 cm 3 150 cm empty open field arena. 

(C) Color-coded firing rate map from an example CA1 cell in the control experiment. 

(D) Cumulative normalized frequency distributions showing spatial correlation (left column) and rate overlap (right column) between pairs of trials. Each row shows a given pair of trials in sessions with objects (as in Figure 1A; dark purple lines; n = 1,189 principal cells recorded from 9 rats) and the corresponding pair of control trials (as in Figure 2B; brown lines; n = 219 principal cells recorded from 3 rats). NO, no object; O, object; OM, object moved; NO[0] , no object[0] ; CON 1–4, control 1–4. 

Having established as a proof-of-concept that we can use population activity to decode the presence of the object, we next asked if decoding accuracy differed as a function of the animal’s spatial relationship with the object. We divided the environment into 5 distance bins, consisting of concentric rings radiating out from the object (Figure 4A). By feeding data from each distance bin into the decoder, we found that decoding performance decreased gradually with increasing distance from the object (Figure 4B) (H = 44.559, p = 4.91 3 10[�][9] , Kruskal-Wallis test, n = 16 experimental sessions; significantly different decoding accuracies for distance bins 1 vs. 2; 2 vs. 3; and 4 vs. 5, W R 111, p % 0.0049, Wilcoxon signed-rank tests). Such a decrease 

was also seen in the individual experiments (Figure 4C). In the main analyses, we optimized distance bins for each experiment so that we had an equal number of samples in each bin. We found the same decrease in decoding accuracy using fixed distance bins rather than optimized bins (Figure S5B) (fixed bins of 0–20, 20–40, 40–60, 60–80, and 80–100 cm). 

To test if the reorganization was equally large in all directions relative to the object, we divided the environment into 5 angular bins, with each bin covering a different set of allocentric angles relative to the object (Figure 4D). The decoding accuracy was the same in different angular bins (Figures 4E and 4F) (H = 3.75, p = 0.4416, Kruskal-Wallis test, n = 16 experimental 

2094 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [141 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C D<br>**----- End of picture text -----**<br>


**==> picture [98 x 104] intentionally omitted <==**

**==> picture [91 x 108] intentionally omitted <==**

**==> picture [87 x 88] intentionally omitted <==**

Figure 3. Decoding the presence of an object in the animal’s environment (A) Schematic of the conceptual framework. A Bayesian decoder infers whether a 1 s sample of population data (highlighted in gray) occurred in the absence or presence of an object (bottom left and right, respectively). (B) Decoding accuracy in all sessions (n = 16). The decoding accuracy is given by the fraction of samples that the decoder classified correctly. (C) Decoding accuracy as a function of bin size (ms), expressed on a logarithmic scale. The bin size was 10[1] , 5 3 10[1] , 10[2] , 5 3 10[2] , 10[3] , 5 3 10[3] , and 10[4] ms. Each color shows a different experimental session. (D) Decoding accuracy as a function of number of cells used to perform the decoding. Cells were randomly subsampled 100 times for each specific n and dataset. Data points show means and error bars show standard deviations (calculated on decoding accuracies pooled from all datasets). Stippled lines indicate the chance level (0.5). Color scale shows how many datasets (i.e., rats) contribute to each datapoint. 2 datasets are from tetrode rats (between 25 and 39 cells) and 2 datasets are from Neuropixels rats (135 and 620 cells, respectively). 

sessions). This shows that the distance-dependent reorganization of population activity is general and not specific for certain compass directions. 

To ensure that the result reflects a genuine phenomenon in the population activity we performed several controls. First, we observed no decrease in decoding accuracy across the same distance bins when attempting to decode the first half of the NO trial from the second half of the NO trial (Figure S5C) or when performing decoding in NO control trials (Figures 2B and S5D). Second, we randomly shuffled the trial labels of the spike count vectors (labels being ‘‘NO’’ and ‘‘O’’), destroying the association between spike count vectors and trials. On the shuffled data, the decoder performed with a mean accuracy of 50% in all distance bins (Figure S5E). Third, we partitioned the data into training and testing in a random manner (in the standard decoder the first half of the session was used for training and the second half for testing and then vice versa). The results 

from this decoder showed the same decline in decoding accuracy as a function of distance from the object (Figure S5F). Finally, across all cells, firing fields were widely distributed across the environment and not concentrated at the object location (Figures S5G and S5H), whereas firing rates were similar between trials, being largest at middle distances from the object (peaking in distance bin 3; Figure S5I). These observations indicate that firing field locations and firing rates cannot trivially explain our findings. 

To further visualize the hippocampal object representation, we took the entire stack of rate maps from the NO trial and O trial and computed the pairwise Pearson correlation between the two stacks. This gives a correlation value (from �1 to 1) for each spatial bin (size: 3 cm 3 3 cm). The correlation maps had low correlations in the central regions near the object, but high correlations in peripheral regions further away from the object (Figure 4G). Next, we binned the environment into 5 distance bins and collected the correlation values in each bin (number of correlation values for each bin: 489 ± 27; mean ± SEM; n = 16 experimental sessions). This showed a stepwise linear increase in correlation values as a function of distance from object, with saturation at larger distances (Figure 4H) (H = 30.1, p = 4.67 3 10[�][6] , Kruskal-Wallis test; significantly different correlation values for distance bins 1 vs. 2; 2 vs. 3; and 3 vs. 4, W % 19, p % 0.0113, Wilcoxon signed-rank tests). Altogether, these findings suggest that the object acts as a pivot around which the hippocampal population activity reorganizes in a distancedependent manner. The internal walls of the recording environment did not play a similar role as the free-standing object, since position decoding accuracy and population vector correlations were comparable near and far away from the walls (Figures S5J and S5K). 

## Behavioral analyses 

We next reasoned that if the animals’ behavior is different between the NO and O trials, and increasingly different near the object, this could also produce decoding accuracy that falls with object distance (Figure 4B). To ask if such a behavioral confound was present in the previous analyses, we developed decoders that attempted to infer the trial (NO vs. O) based on the animal’s behavior (see STAR Methods). Decoders for speed, head direction, and occupancy performed only slightly above 50% correct, with accuracies independent of object distance (Figures S6A, S6C, and S6E). We verified that all behavioral decoders worked: when simulating speed, head direction, or occupancy that was clearly different between the NO and O trials in all distance bins, the decoders performed with virtually 100% accuracy (Figures S6B, S6D, and S6F, left). Similarly, when simulating speed, head direction, or occupancy that was increasingly different near the object, the decoders had distance-dependent accuracies (Figures S6B, S6D, and S6F, right). That the behavioral decoders show flat accuracies in the experimental data (Figures S6A, S6C, and S6E) is therefore a strong indication that variations in behavior are not sufficient to explain our findings (Figures 4B and 4C). 

We further reasoned that we could test for any role of behavior by artificially removing any behavioral differences between the trials prior to running the decoder on the neural data (example 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 2095 

**==> picture [76 x 35] intentionally omitted <==**

**ll** OPEN ACCESS 

## Article 

**==> picture [230 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D E F<br>G H<br>**----- End of picture text -----**<br>


**==> picture [92 x 99] intentionally omitted <==**

**==> picture [92 x 101] intentionally omitted <==**

**==> picture [100 x 100] intentionally omitted <==**

**==> picture [9 x 83] intentionally omitted <==**

**==> picture [83 x 83] intentionally omitted <==**

Figure 4. Graded reorganization of hippocampal population activity 

(A) Schematic of partitioning of the environment for the main analysis. We divided the recording arena (150 cm 3 150 cm) into 5 distance bins, forming circles around the object. We then applied the decoder to data from each distance bin to assess how decoding accuracy scales with distance from object. (B) Boxplot of decoding accuracy as a function of distance from object. The central dashed line indicates the median, and the top and bottom lines indicate upper and lower and quartiles, respectively. The length of the whiskers indicates 1.5 times the interquartile range. Distance bin 1 is nearest the object; distance bin 5 furthest away. Each distance bin had an equal number of samples. (C) Decoding accuracy as a function of distance from object for each individual experiment (n = 16). Data are the same as in the previous panel, but each color shows a different experimental session. Note that all experimental sessions have decreasing curves. (D) Schematic of the partitioning of the environment for angular binning. We divided the arena into 5 angular bins, each bin spanning 72[�] and applied a decoder to each bin. (E) Boxplot of decoding accuracy as a function of angle relative to object. Outliers exceeding 1.5 times the interquartile range are shown as crosses. (F) Similar to (C) but for angle relative to object. All experimental sessions have flat curves. (G) Correlation map showing similarity of timeaveraged population firing on trials with and without the object (rat 27207). The correlations are closer to zero (near 0.3) in the vicinity of the object (white square) and more positive (beyond 0.8) in the periphery. (H) Correlation between stacks of rate maps (NO trial vs. O trial) as a function of distance from the object. For each experimental session, we calculated a correlation map as in the previous panel. Then, we binned all values in the correlation map into 5 distance bins (based on distance to object) and calculated the mean correlation inside each distance bin. Plot shows mean ± SEM for all experimental sessions (n = 16) from all animals. 

for speed distributions before and after removing behavioral differences in Figure S6G). We still observed a graded decrease in decoding accuracy for the neural activity decoder after matching distributions for speed (Figure S6H), head direction (Figure S6I) and occupancy (Figure S6J), confirming that behavioral differences between the trials were not necessary to obtain our results. The standard decoder used a prior that included information about the animal’s occupancy (see STAR Methods for details). As expected from the behavioral analyses, removal of this prior had no effect on our results (Figure S6K). 

Finally, in the presence of the object there will be some regions that the animal cannot explore, preventing certain neural activity patterns from occurring in the O trial, which might lead to high decoding success near the object. To test that possibility, we included only spatial bins in which the animal had spent a mini- 

mum amount of time (either 100, 500, 1,000, or 2,000 ms) in both the NO and O trials (i.e., excluding all spatial bins that the animal had not occupied for that duration in both trials). Regardless of the threshold value, the result was the same as before, with accuracy declining along with object distance (Figure S6L; note that to perform this analysis, the rate map bin size had to be increased from 3 to 10 cm[2] ). 

## Objects are encoded by distinct patterns of joint activity in CA1 cells 

We next asked if specific features of the population activity become different when the object is introduced. To parametrize the population activity, we introduced the concepts of ‘‘words’’ and ‘‘counts’’ as used previously to study population coding.[23–25] We defined words as unique patterns of spiking and 

2096 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

Article 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [302 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>**----- End of picture text -----**<br>


**==> picture [136 x 128] intentionally omitted <==**

**==> picture [117 x 112] intentionally omitted <==**

**==> picture [117 x 114] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
D<br>**----- End of picture text -----**<br>


**==> picture [7 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
E<br>**----- End of picture text -----**<br>


**==> picture [113 x 134] intentionally omitted <==**

Figure 5. Objects are represented by distinct patterns of joint activity in the CA1 cell population (A) Framework for analyzing population activity. We represent neural data in an N 3 T spike matrix, where N is the number of recorded cells and T is the number of time points in the trial sampled at 10 ms. We define a specific pattern of spiking across the neural population as a word. In the schematic, each unique word is 

(legend continued on next page) 

Neuron 111, 2091–2104, July 5, 2023 2097 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

silence across neurons in the population in a single time bin (Figure 5A, time bins of 10 ms) and counts as the total sum of spikes across the population in a single time bin (Figure 5A, bottom row). We then calculated the mutual information (MI) between words and trial, and between counts and trial (see STAR Methods). Words were much more informative than counts (Figure 5B) (U R 439, p % 1.19 3 10[�][6] , Wilcoxon rank-sum tests). Importantly, the amount of information gained from words decreased as a function of distance from the object (Figures 5B and 5C) (H = 24.29, p = 6.98 3 10[�][5] , KruskalWallis test), reproducing the pattern of the decoder. In contrast, the amount of information from counts did not depend on object distance (H = 4.08, p = 0.3947, Kruskal-Wallis test) and was not significantly above zero (t % 1.46, p R 0.1636 for all comparisons, t tests). 

To visualize the word representation, we calculated how many times each word occurred in each trial and sorted the words by frequency in the NO trial (Figure 5D, top). By applying the same sorting in the O trial (Figure 5D, bottom) we could see which words were up- and down-regulated with objects present. Many low-frequency words in the NO trial were high-frequency words in the O trial, standing out as spikes (Figure 5D, bottom). No such spikes were present in shuffled versions of data (Figure S7A), suggesting that the NO and O trials recruit different patterns of neural activity. 

Word frequency distributions appeared different near the object (Figure 5D, distance bin 1) but more similar further away from the object (Figure 5D, distance bins 2–5; note that the same pattern was obtained when we sorted both histograms according to word frequencies in the O trial rather than the NO trial; Figure S7B). Consistent with this, the KullbackLeibler (KL) divergence between the NO and O distributions became smaller with increasing object distance (Figure 5E, blue curve) (H = 16.22, p = 0.0027, Kruskal-Wallis test; KL divergences in 1st distance bin vs. 5th distance bin: W = 102, p = 6.10 3 10[�][4] , Wilcoxon signed-rank test). No decrease in the KL divergence was present in shuffled data (Figure 5E, green curve). In contrast to the identity of words, the number of words was independent of trial type and distance from the object (Figures S7C and S7D). 

Because the number of observed states is much larger for words than counts, the entropy was higher for words than counts 

(entropy of words: 1.65 bits ± 0.06; entropy of counts: 0.84 bits ± 0.02; mean ± SEM). However, the difference in entropy could not trivially explain why words were more informative than counts, because after downsampling the number of states to be equal for words and counts, words were still much more informative (Figure S7E). 

## Distance-specific reorganization of the hippocampal map is widely distributed across the CA1 population 

We next wondered to what extent the distance-based reorganization of the hippocampal map is distributed across the cell population. The reorganization may be driven by a dedicated subpopulation of cells with ‘‘strong tuning’’ to distance from the object, or it could be distributed across most of the cells, as an emergent property of the network, independently of the responses at the single-cell level. 

To understand how many cells are necessary to see the reorganization, we first asked if it is present already at the level of single cells. To estimate the distance modulation of individual cells, we first ran the decoder (Figure 3A) with one cell at a time (n = 1,189 cells and runs of the decoder). Individual cells showed no obvious decrease in decoding accuracy as a function of distance, with medians just slightly above 0.5 (Figure 6A, compare to Figure 4B). We then calculated 

distance tuning = decoding accuracy bin #1 � decoding accuracy bin #5 (Equation 1) 

as a proxy for distance modulation of individual cells, where a more positive value implies stronger distance modulation. CA1 cells had a slight positive bias in distance tuning (mean: 0.02; for reference, the same mean calculated from populations is 0.19; Figure 4C) and nearly all cells were contained between the bounds �0.2 and 0.2 (98.7% of cells). By shuffling data (circularly shifting spike trains) and re-calculating the distance tuning, we observed that some cells had significant positive distance tuning (12.2%, n = 145/1,189 cells) (Figure 6B, red bars) and some cells had significant negative distance tuning (3.8%, n = 45/1,189 cells) (Figure 6B, yellow bars). However, while these cells were individually informative, they were dispensable: after removing cells with significant positive distance tuning (12.2%), we still observed a gradual drop in decoding accuracy 

labeled by a different color. We define counts as the total number of spikes in the neural population in any given time bin. The total count is illustrated in the bottom row. (B) Mutual information between trial type (NO or O) and population response (either words, in blue, or counts, in orange) as a function of distance from object. Distance bins were constructed to contain the same number of samples, as in Figures 4B and 4C. Data points show mean ± SEM (n = 16 experimental sessions, 14 from tetrodes data, 2 from Neuropixels data where the number of cells was subsampled to 30, see STAR Methods for further details). Distance bin 1 is nearest the object; distance bin 5 furthest away. Words but not counts are informative about trial type, and they are more informative if activity is sampled near the object. (C) Mutual information from words (blue) or counts (orange) for each individual experiment. Data and analysis are as in the previous panel. Each curve shows a different experimental session. Notice that all orange curves overlap. 

(D) Histograms of word frequencies from the NO trial (top) and the O trial (bottom) of an example session with 26 simultaneously recorded cells. Each histogram shows how many times each unique word appeared during each trial, in each distance bin. The words are indexed from 1 to 100 (only the 100 most frequent words in the NO trial are plotted). All distributions are sorted according to how frequently each word occurred in the NO trial. For this reason, distributions from the NO trial are decreasing (top) while distributions from the O trial have more arbitrary shapes (bottom). This also means that indices of words match between top and bottom (word #1 at the top is the same as word #1 at the bottom). 

(E) Kullback-Leibler (KL) divergence between word distributions in the O (D, bottom) and NO (D, top) trial as a function of distance to object. Real data use the true trial labels of the words (blue curve); in shuffled data, trial labels were randomly assigned to each word (green curve). Word distributions were sorted by word frequencies in the NO trial (as described in the previous, D). 

2098 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

Figure 6. The distance-specific reorganization is widely distributed 

**==> picture [300 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A<br>C D<br>E F<br>**----- End of picture text -----**<br>


(A) Decoding accuracy as a function of distance from object for individual cells (15 tetrode sessions and 2 Neuropixels sessions, n = 1,189 cells). Individual cells have mostly flat decoding accuracy. Boxplot conventions are as in Figures 4B. (B) Distance tuning of individual cells (n = 1,189 cells). Some cells had significant positive distance tuning (red bars) and other cells had significant negative distance tuning (yellow bars), compared to shuffled data. Note the slight positive bias of distance tuning values in the entire population. (C) Decoding accuracy as a function of distance from object, based on different subsets of cells of size n (n = 1, 5, 20, 30, 50, 100, 200, 300, 400, and 500). Cells were randomly selected from a total population of N = 620 cells simultaneously recorded. Data points show means over 20 random realizations; error bars show SEM. When error bars cannot be seen it is because they are too small. Stippled line indicates chance level. (D) Distance reorganization as a function of number of cells used in the decoding. The left y axis (blue curve) shows the distance difference (decoding accuracy in bin #1—decoding accuracy in bin #5) and the right y axis (orange curve) shows the slope of the least-square line (fitted to decoding accuracy vs. distance curves in the previous panel). These two measures are proxies for the amount of distance reorganization. Data points show means; error bars show SEM. Note the increasing distance difference, as well as the decreasing slope, as a function of the number of cells. 

**==> picture [324 x 125] intentionally omitted <==**

(E) Decoding accuracy as a function of distance from object, depending on the fraction of cells with lowest distance tuning retained. We ran the decoder using the k% of cells with lowest tuning, with k being 100, 80, 60, 40, and 20. Keeping 20% of cells with the least tuning is sufficient to see reorganization of neural-population activity according to distance from the object. Data are from the same Neuropixels rat as in (C) and (D). (F) Distance reorganization as a function of the percentage of cells with the lowest distance tuning retained. Conventions are as in (D). 

obtained with population data as a function of object distance (Figure S5L). This is consistent with the idea that many cells contribute to the smooth change in population activity according to object distance (Figures 4B and 4C). 

W = 2.48, p = 0.6489; all other curves: W R 11.89, p % 0.0182, Wilcoxon signed-rank tests). The difference between bins #1 and #5 grew systematically with the number of cells (Figure 6D; left y axis, blue) (H = 174.57, p = 3.14 3 10[�][32] , Kruskal-Wallis test) and reached its maximum at n = 500 cells. In parallel, the slope of the least-square line (fitted to the curves in Figure 6C) became increasingly negative (Figure 6D, right y axis, orange) (H = 157.6, p = 1.011 3 10[�][28] , Kruskal-Wallis test) and reached its minimum at n = 500 cells, creating the appearance of two curves that were mirror-images of one another. First, this implies that even a small number of cells picked randomly is sufficient to see the distance modulation, independently of the individual cell properties (Figure 6C, blue and green curves). Second, the more cells we include, the stronger the distance-modulated reorganization of the map is (Figure 6D). This suggests that the factors 

We next asked how the reorganization scales with the number of cells used in the decoder. For this, we first used Neuropixels data from a rat implanted with two probes in the left hippocampus, yielding 620 CA1 cells with a wide variety of properties, including place cells, object cells, and object-vector cells. To simulate different population sizes, we picked random subsets of cells (subsets of size n = 1, 5, 10, 30, 50, 100, 200, 300, 400, and 500) from the 620 cells. For each n we ran the decoder on 20 different randomly chosen subsets of cells. All curves showed reduced decoding accuracy as a function of distance, except the curve constructed using only a single cell (Figure 6C) (n = 1 curve: 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 2099 

Article 

**==> picture [76 x 35] intentionally omitted <==**

**ll** OPEN ACCESS 

Figure 7. Single-cell properties are not predictive of distance tuning 

**==> picture [182 x 43] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>**----- End of picture text -----**<br>


**==> picture [134 x 157] intentionally omitted <==**

(A) Relationship between each cell’s object-tuning score and its distance tuning. Due to the large number of cells, we bin the data to aid visualization (10 bins, ranging from minimum object-tuning score to maximum object-tuning score). Data points show mean ± SD for each bin. Inset shows scatterplot of original data before binning (n = 1,189 cells). Note lack of a strong correlation between object-tuning score and the distance tuning. 

**==> picture [123 x 116] intentionally omitted <==**

(B) Relationship between each cell’s spatial information (bits/spike) (in the O trial) and its distance tuning (n = 1,189 cells). 

(C) Relationship between each cell’s spatial correlation (between rate maps from the NO and O trials) and its distance tuning (n = 1,189 cells). 

(D) Relationship between each cell’s rate overlap (between the NO and O trials) and its distance tuning (n = 1,189 cells). In all panels, note absence of relationships between single-cell properties and tuning to distance from the object. 

**C D** 

**==> picture [61 x 41] intentionally omitted <==**

score, spatial information, spatial correlation, or rate overlap (Figures 7A–7D, insets). Distance tuning did not appear to depend strongly on any single-cell property. The object-tuning score had a significant positive correlation with distance tuning, but very weakly so (r = 0.12, p = 1.95 3 10[�][5] ). Spatial information had a significant negative correlation, but also this was very weak (r = �0.13, p = 3.70 3 10[�][7] ). Similarly, spatial correlation and rate overlap were also negatively but weakly correlated with distance tuning (spatial correlation: r = �0.08, p = 7.61 3 10[�][4] ; rate overlap: r = �0.18, p = 1.57 3 10[�][9] ). We obtained similar results when, instead of distance tuning, we used the slope of the regression line fitted to decoding accuracy vs. distance as a measure of reorganization (object-tuning score: r = �0.12, p = 3.05 3 10[�][5] ; spatial information: r = 0.10, p = 3.58 3 10[�][5] ; spatial correlation: r = �0.08, p = 7.98 3 10[�][4] ; rate overlap: r = 0.19, p = 1.13 3 10[�][12] ). After removing all object-tuned cells (19.9%) from the data and re-running the decoder, we observed the same gradual fall in decoding accuracy as a function of distance (Figure S5M). Collectively the observations suggest that cells can contribute to the distance fall-off independently of whether they are objecttuned cells (Figure 7A), place cells (Figure 7B), or exhibit small or large changes in spatial selectivity (Figure 7C) or firing rate (Figure 7D). The dissociation of our findings from single-cell properties (Figures 7 and S5M) is supportive of the notion that distancedependence is widespread throughout CA1 cells and manifests at the neural-population level (Figure 6). 

underlying the reorganization are distributed across the entire population of hippocampal cells. The finding was upheld in data from animals with smaller numbers of cells (135 cells in a Neuropixels recording; 25–39 cells in tetrode recordings) (Figures S8A–S8D). 

We next asked whether we can visualize the distance reorganization even when using cells that show the least ‘‘distance tuning.’’ After calculating the distance tuning of single cells (Figures 6A and 6B; Equation 1), we sorted the cells according to this variable, starting with the lowest value. We then subsampled the same Neuropixels data (Figures 6C and 6D), keeping either 100%, 80%, 60%, 40%, or 20% of cells with the lowest distance tuning. As expected, curves gradually became flatter when using smaller populations of cells (Figure 6E). However, even the 20% of cells with lowest tuning was sufficient to demonstrate the distance modulation, in the form of positive distance tuning as well as a negative slope (Figures 6E and 6F; rightmost point on blue curve: 0.121; on orange curve: �0.0267). Thus even the ‘‘worst’’ cells (with lowest distance tuning) contribute to a distance-specific reorganization of the hippocampal map. As before, the finding also held in smaller-sized tetrode and Neuropixels data (Figures S8E–S8H). 

## DISCUSSION 

By simultaneously recording up to 620 principal neurons in the hippocampal area CA1 of freely moving rats, we could evaluate single-cell and population-level perspectives on how local objects influence representations of space. Some cells fired at the 

Finally, we asked if any properties of single cells were predictive of distance tuning. We correlated the distance tuning of individual cells (Figure 6B; Equation 1) against their object-tuning 

2100 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

object (object cells), others at fixed distances and directions from it (object-vector cells, reminiscent of landmark-vector cells[13] ). In addition, the majority of the CA1 cells changed their spatial firing patterns when the object was introduced, moved, or taken out from the environment. At the level of neural populations, the heterogeneous responses were coherently organized across cells so that the amount of reorganization of the hippocampal map depended ondistance from the object in a graded manner. The reorganization of the hippocampal map in the presence of objects was widely distributed and did not require specific subsets of cells or the presence of object cells and object-vector cells. Although past studies have already raised the possibility that the hippocampal representation of objects may be non-factorized,[15] we here demonstrate how by describing (1) a strikingly smooth change in population activity according to object distance, and (2) an emergent property of the code, where the distance-based representation becomes more evident as sample sizes are increased. Our findings hint that some aspects of hippocampal cognitive maps may not be understood through properties of dedicated functional cell types—such as object cells, object-vector cells, or place cells—but through emergent properties of cell populations whose activities appear random and disorganized when viewed individually. 

We first set out to estimate how many object cells and objectvector cells are present in CA1 when animals explore twodimensional spaces, in a dataset where the number of cells is an order of magnitude larger than in previous studies of such cells.[5][,][10][,][13][,][14] We found both object cells and object-vector cells (4.1% and 13.3%, respectively, if using an arbitrary 15 cm distance cut-off between the two groups). Object-tuned cells had variable tuning across time and environments, unlike their MEC counterparts,[11] which are stable over weeks and across different tasks.[11][,][26] A different type of ‘‘instability’’ across time was reported in hippocampal landmark-vector cells, which only began to fire at fixed distances and directions from objects once the rat had gained experience with the objects.[13] In the present study we did not observe such experience-dependence. Other studies have reported stable object tuning at the level of individual cells,[5] whereas we only find hints of stability during the course of a single trial (30 min). While this may reflect differences in training procedures (B. Rivard, personal communication), a broader lesson from our work may be that even if a stimulus (for example, an object and its location) is not represented via stable activities of individual cells, it may still be represented stably at the level of the network. 

How exactly did objects influence the spatial firing patterns? Our findings are consistent with studies that report remarkable heterogeneity of object responses in the hippocampus.[7][,][15] We observed appearance and disappearance of firing fields, movement of firing fields, object cells, object-vector cells, and firing fields that persisted after objects were removed. This heterogeneity points to a transformation of the object-centered spatial codes within the entorhinal-hippocampal circuit, where the representation of space is changed from a low-dimensional code in MEC with coherence between cells’ responses across environments[27–29] to a higher-dimensional code in the hippocampus that orthogonalizes distinct representations of space.[20][,][30][,][31] The higher dimensionality of hippocampal responses is closely 

linked to the phenomenon of global remapping, where distinct place-field codes are created for distinct environments.[4][,][32][,][33] 

In parallel with the large variability of responses at the level of single hippocampal cells, we observed a striking organization of the cells’ collective activity. The object acted as a pivot for reorganizing hippocampal population activity: in the object’s neighborhood, the reorganization was large, leading to high decoding accuracy, whereas further away from the object, the reorganization became increasingly smaller, leading to low decoding accuracy. Thus, the highly variable activity of the CA1 cells was brought together into a unified population code, where activity was largely determined by the state of a single variable: the animal’s distance from the object. In that sense, the population response had a simple and predictable structure, in comparison with the disorganized activities of individual cells. The graded reorganization of the population response between NO and O trials could not be explained by differences in the animal’s behavior: (1) we were unable to decode the trial type based on behavior and (2) downsampling data to match behavior between the trials had no effect on the main result. 

Remapping restricted to subsets of place cells has been shown in many contexts.[10][,][34–37] However, the reorganization of population activity described here does not correspond to forms of place-cell remapping described in the literature,[4][,][32][,][33][,][35][,][38] one key difference being the smoothness of the change in the population representation. Remapping in place cells often appears in one of two forms: global remapping or rate remapping.[32] During global remapping, place cells collectively reorganize their spatial firing patterns, providing an entirely new and orthogonal representation of space. This form of remapping is thought of as discrete,[33][,][39–41] and during periods of ambiguity, there may even be flickering between distinct maps.[40][,][42][,][43] Such discreteness is clearly different from the smooth reorganization seen in the present study. Rate remapping[44] can also be smooth during gradual changes of the environment.[21] However, these smooth changes, expressed in the firing rates of individual cells, took place all over the environment. Those changes were clearly different from the smooth reorganization across space seen in the present study, where the amount of reorganization of the hippocampal map was a continuous function of the animal’s distance from an object. The presence of this smooth reorganization, combined with the simultaneous presence of place cells and object-tuned cells, suggests that population-level representations co-exist with single-cell representations in CA1. Future work will have to determine if such co-existence arises de novo in the hippocampus or already at input stages such as the MEC. While responses of individual MEC cells may show less heterogeneity than their hippocampal counterparts (MEC cells fractionate into discrete functional cell types[11][,][45–48] ), we cannot exclude the possibility that similar population-level representations exist on top of the cells’ individual firing profiles in MEC. This possibility would be consistent with topological analyses demonstrating population structure in grid cells not apparent in individual neurons.[27] 

A critical element of our findings is how widely distributed the object-centered population coding is across the recorded cells. The more cells we put into the decoder, the larger the improvement in decoding accuracy near the object (relative to far from 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 2101 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

the object). In addition, we could still visualize some degree of distance-based reorganization when only the cells with the weakest distance tuning were retained in the analysis. While distance tuning is generally weak in individual cells, at the population level the responses transform into a smooth distancedependent code. The transformation has parallels to classic work in the vertebrate retina, where weak pairwise correlations are transformed into strong correlations in population activity,[23] and supports recent work in the hippocampus showing that place cells and non-place cells encode information in a collective and distributed fashion.[16][,][17] Taken together, the findings suggest that some neural representations may be best described as emergent properties of large numbers of cells.[18] 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d RESOURCE AVAILABILITY 

   - B Lead contact 

   - B Materials availability 

   - B Data and code availability 

- d EXPERIMENTAL MODEL AND SUBJECT DETAILS 

- d METHOD DETAILS 

   - B Surgery and electrode implantation 

## SUPPLEMENTAL INFORMATION 

Supplemental information can be found online at https://doi.org/10.1016/j. neuron.2023.04.008. 

## ACKNOWLEDGMENTS 

We thank Ø. Høydal and E. Ranheim Skytøen for discussions and R. Gardner for developing the Neuropixels data acquisition and analysis pipeline. We thank A.M. Amundsga˚ rd, S. Ball, K. Haugen, K. Jenssen, E. Kra˚ kvik, I. Ulsaker-Janke, and H. Waade for technical assistance. The study was supported by funding from the Research Council of Norway (FRIPRO grant number 300394 to M.-B.M., Centre of Excellence grant number 223262 to M.-B.M. and E.I.M., and National Infrastructure grant number 295721 to E.I.M. and M.-B.M.); a grant from the K.G. Jebsen Foundation (grant number SKGJMED-022); a Synergy grant to E.I.M. from the European Research Council (‘‘KILONEURONS,’’ grant agreement no. 951319); the Kavli Foundation (M.-B.M. and E.I.M.); and a direct contribution to M.-B.M. and E.I.M. from the Ministry of Education and Research of Norway. 

## AUTHOR CONTRIBUTIONS 

A.N. and S.O.A. have equal right to list themselves first in bibliographic documents. A.N., E.I.M., and M.-B.M. designed and planned experiments; A.N. performed the experiments (surgeries, recordings, spike sorting); A.N. and S.O.A. performed single-cell analyses; S.O.A. performed neural-population analyses; S.O.A. and A.N. wrote the paper with inputs and edits from all authors; S.G.C., E.I.M., and M.-B.M. supervised the project; E.I.M. and M.-B.M. obtained funding. 

## DECLARATION OF INTERESTS 

- B Behavioral procedures 

- B Recording procedures 

E.I.M. is on the Advisory Board of Neuron. 

   - B Histology and reconstruction of electrode placement 

   - B Spike sorting and cell-inclusion criteria 

- d QUANTIFICATION AND STATISTICAL ANALYSIS 

## INCLUSION AND DIVERSITY 

We support inclusive, diverse, and equitable conduct of research. 

- B Firing rate maps and identification of firing fields 

- B Spatial information content 

- B Shuffling of spike data 

- B Template matching procedure to identify objecttuned cells 

- B Object-vector score and object-vector cell criteria 

- B Spatial correlation and rate overlap 

- B Region-of-interest analysis for object traces 

- B Bayesian decoding algorithm 

- B Calculation of decoding accuracy as a function of distance and allocentric angle 

- B Performance of decoder 

- B Controls for results of decoder 

- B Behavioral analyses I: Decoding 

- B Behavioral analyses II: Subsampling 

- B Subsampling for decoder 

- B Measuring strength of distance-specific reorganization 

- B Significance of distance tuning in individual cells 

- B Population vector correlation 

- B Definition of words and counts 

- B Mutual information 

- B Word distributions 

- B Downsampling words 

- B Kullback-Leibler divergence between word distributions 

- B Statistical tests 

Received: July 7, 2022 Revised: December 22, 2022 Accepted: April 7, 2023 Published: May 5, 2023 

## REFERENCES 

1. O’Keefe, J., and Nadel, L. (1978). The Hippocampus as a Cognitive Map (Clarendon Press; Oxford University Press). 

2. O’Keefe, J., and Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res. 34, 171–175. 

3. O’Keefe, J. (1976). Place units in the hippocampus of the freely moving rat. Exp. Neurol. 51, 78–109. https://doi.org/10.1016/0014-4886(76)90055-8. 

4. Muller, R.U., and Kubie, J.L. (1987). The effects of changes in the environment on the spatial firing of hippocampal complex-spike cells. J. Neurosci. 7, 1951–1968. 

5. Rivard, B., Li, Y., Lenck-Santini, P.-P., Poucet, B., and Muller, R.U. (2004). Representation of objects in space by two classes of hippocampal pyramidal cells. J. Gen. Physiol. 124, 9–25. https://doi.org/10.1085/jgp. 200409015. 

6. Battaglia, F.P., Sutherland, G.R., and McNaughton, B.L. (2004). Local sensory cues and place cell directionality: additional evidence of prospective coding in the hippocampus. J. Neurosci. 24, 4541–4550. https://doi.org/ 10.1523/JNEUROSCI.4896-03.2004. 

7. Lenck-Santini, P.P., Rivard, B., Muller, R.U., and Poucet, B. (2005). Study of CA1 place cell activity and exploratory behavior following spatial and 

2102 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

nonspatial changes in the environment. Hippocampus 15, 356–369. https://doi.org/10.1002/hipo.20060. 

8. Burke, S.N., Maurer, A.P., Nematollahi, S., Uprety, A.R., Wallace, J.L., and Barnes, C.A. (2011). The influence of objects on place field expression and size in distal hippocampal CA1. Hippocampus 21, 783–801. https://doi. org/10.1002/hipo.20929. 

9. Hollup, S.A., Molden, S., Donnett, J.G., Moser, M.-B., and Moser, E.I. (2001). Accumulation of hippocampal place fields at the goal location in an annular watermaze task. J. Neurosci. 21, 1635–1644. https://doi.org/ 10.1523/JNEUROSCI.21-05-01635.2001. 

10. Gothard, K.M., Skaggs, W.E., Moore, K.M., and McNaughton, B.L. (1996). Binding of hippocampal CA1 neural activity to multiple reference frames in a landmark-based navigation task. J. Neurosci. 16, 823–835. https://doi. org/10.1523/JNEUROSCI.16-02-00823.1996. 

11. Høydal, Ø.A., Skytøen, E.R., Andersson, S.O., Moser, M.B., and Moser, E.I. (2019). Object-vector coding in the medial entorhinal cortex. Nature 568, 400–404. https://doi.org/10.1038/s41586-019-1077-7. 

12. Andersson, S.O., Moser, E.I., and Moser, M.-B. (2021). Visual stimulus features that elicit activity in object-vector cells. Commun. Biol. 4, 1219. https://doi.org/10.1038/s42003-021-02727-5. 

13. Deshmukh, S.S., and Knierim, J.J. (2013). Influence of local objects on hippocampal representations: landmark vectors and memory. Hippocampus 23, 253–267. https://doi.org/10.1002/hipo.22101. 

14. Geiller, T., Fattahi, M., Choi, J.S., and Royer, S. (2017). Place cells are more strongly tied to landmarks in deep than in superficial CA1. Nat. Commun. 8, 14531. https://doi.org/10.1038/ncomms14531. 

15. GoodSmith, D., Kim, S.H., Puliyadi, V., Ming, G.L., Song, H., Knierim, J.J., and Christian, K.M. (2022). Flexible encoding of objects and space in single cells of the dentate gyrus. Curr. Biol. 32, 1088–1101.e5. https://doi.org/ 10.1016/j.cub.2022.01.023. 

16. Meshulam, L., Gauthier, J.L., Brody, C.D., Tank, D.W., and Bialek, W. (2017). Collective behavior of place and non-place neurons in the hippocampal network. Neuron 96, 1178–1191.e4. https://doi.org/10.1016/j. neuron.2017.10.027. 

17. Stefanini, F., Kushnir, L., Jimenez, J.C., Jennings, J.H., Woods, N.I., Stuber, G.D., Kheirbek, M.A., Hen, R., and Fusi, S. (2020). A distributed neural code in the dentate gyrus and in CA1. Neuron 107, 703– 716.e704. https://doi.org/10.1016/j.neuron.2020.05.022. 

18. Yuste, R. (2015). From the neuron doctrine to neural networks. Nat. Rev. Neurosci. 16, 487–497. https://doi.org/10.1038/nrn3962. 

19. Manns, J.R., and Eichenbaum, H. (2009). A cognitive map for object memory in the hippocampus. Learn. Mem. 16, 616–624. https://doi.org/10. 1101/lm.1484509. 

20. Leutgeb, S., Leutgeb, J.K., Treves, A., Moser, M.B., and Moser, E.I. (2004). Distinct ensemble codes in hippocampal areas CA3 and CA1. Science 305, 1295–1298. https://doi.org/10.1126/science.1100265. 

21. Leutgeb, J.K., Leutgeb, S., Treves, A., Meyer, R., Barnes, C.A., McNaughton, B.L., Moser, M.B., and Moser, E.I. (2005). Progressive transformation of hippocampal neuronal representations in "morphed" environments. Neuron 48, 345–358. https://doi.org/10.1016/j.neuron.2005. 09.007. 

22. Posani, L.A.-O., Cocco, S., Je�zek, K., and Monasson, R. (2017). Functional connectivity models for decoding of spatial representations from hippocampal CA1 recordings. J. Comput. Neurosci. 43, 17–33. 

23. Schneidman, E., Berry, M.J., Segev, R., and Bialek, W. (2006). Weak pairwise correlations imply strongly correlated network states in a neural population. Nature 440, 1007–1012. https://doi.org/10.1038/nature04701. 

24. Osborne, L.C., Palmer, S.E., Lisberger, S.G., and Bialek, W. (2008). The neural basis for combinatorial coding in a cortical population response. J. Neurosci. 28, 13522–13531. https://doi.org/10.1523/JNEUROSCI. 4390-08.2008. 

25. Schneidman, E., Puchalla, J.L., Segev, R., Harris, R.A., Bialek, W., and Berry, M.J. (2011). Synergy from silence in a combinatorial neural code. 

J. Neurosci. 31, 15732–15741. https://doi.org/10.1523/JNEUROSCI. 0301-09.2011. 

26. Obenhaus, H.A., Zong, W., Jacobsen, R.I., Rose, T., Donato, F., Chen, L., Cheng, H., Bonhoeffer, T., Moser, M.B., and Moser, E.I. (2022). Functional network topography of the medial entorhinal cortex. Proc. Natl. Acad. Sci. USA 119, e2121655119. https://doi.org/10.1073/pnas.2121655119. 

27. Gardner, R.J., Hermansen, E., Pachitariu, M., Burak, Y., Baas, N.A., Dunn, B.A., Moser, M.B., and Moser, E.I. (2022). Toroidal topology of population activity in grid cells. Nature 602, 123–128. https://doi.org/10.1038/ s41586-021-04268-7. 

28. Fyhn, M., Hafting, T., Treves, A., Moser, M.B., and Moser, E.I. (2007). Hippocampal remapping and grid realignment in entorhinal cortex. Nature 446, 190–194. https://doi.org/10.1038/nature05601. 

29. Yoon, K., Buice, M.A., Barry, C., Hayman, R., Burgess, N., and Fiete, I.R. (2013). Specific evidence of low-dimensional continuous attractor dynamics in grid cells. Nat. Neurosci. 16, 1077–1084. https://doi.org/10. 1038/nn.3450. 

30. Alme, C.B., Miao, C., Jezek, K., Treves, A., Moser, E.I., and Moser, M.B. (2014). Place cells in the hippocampus: eleven maps for eleven rooms. Proc. Natl. Acad. Sci. USA 111, 18428–18435. https://doi.org/10.1073/ pnas.1421056111. 

31. McNaughton, B.L., and Morris, R.G.M. (1987). Hippocampal synaptic enhancement and information storage within a distributed memory system. Trends Neurosci. 10, 408–415. https://doi.org/10.1016/01662236(87)90011-7. 

32. Leutgeb, S., Leutgeb, J.K., Barnes, C.A., Moser, E.I., McNaughton, B.L., and Moser, M.B. (2005). Independent codes for spatial and episodic memory in hippocampal neuronal ensembles. Science 309, 619–623. https:// doi.org/10.1126/science.1114037. 

33. Colgin, L.L., Moser, E.I., and Moser, M.-B. (2008). Understanding memory through hippocampal remapping. Trends Neurosci. 31, 469–477. https:// doi.org/10.1016/j.tins.2008.06.008. 

34. Tanila, H., Shapiro, M.L., and Eichenbaum, H. (1997). Discordance of spatial representation in ensembles of hippocampal place cells. Hippocampus 7, 613–623. 

35. Anderson, M.I., and Jeffery, K.J. (2003). Heterogeneous modulation of place cell firing by changes in context. J. Neurosci. 23, 8827–8835. https://doi.org/10.1523/JNEUROSCI.23-26-08827.2003. 

36. Knierim, J.J. (2002). Dynamic interactions between local surface cues, distal landmarks, and intrinsic circuitry in hippocampal place cells. J. Neurosci. 22, 6254–6264. https://doi.org/10.1523/JNEUROSCI.22-1406254.2002. 

37. Chen, G., King, J.A., Burgess, N., and O’Keefe, J. (2013). How vision and movement combine in the hippocampal place code. Proc. Natl. Acad. Sci. USA 110, 378–383. https://doi.org/10.1073/pnas.1215834110. 

38. Latuske, P., Kornienko, O., Kohler, L., and Allen, K. (2017). Hippocampal remapping and its entorhinal origin. Front. Behav. Neurosci. 11, 253. https://doi.org/10.3389/fnbeh.2017.00253. 

39. Wills, T.J., Lever, C., Cacucci, F., Burgess, N., and O’Keefe, J. (2005). Attractor dynamics in the hippocampal representation of the local environment. Science 308, 873–876. https://doi.org/10.1126/science.1108905. 

40. Jezek, K., Henriksen, E.J., Treves, A., Moser, E.I., and Moser, M.-B. (2011). Theta-paced flickering between place-cell maps in the hippocampus. Nature 478, 246–249. https://doi.org/10.1038/nature10439. 

41. Kubie, J.L., Levy, E.R.J., and Fenton, A.A. (2020). Is hippocampal remapping the physiological basis for context? Hippocampus 30, 851–864. https://doi.org/10.1002/hipo.23160. 

42. Kelemen, E., and Fenton, A.A. (2010). Dynamic grouping of hippocampal neural activity during cognitive control of two spatial frames. PLoS Biol. 8, e1000403. https://doi.org/10.1371/journal.pbio.1000403. 

43. Renaudineau, S., Poucet, B., and Save, E. (2007). Flexible use of proximal objects and distal cues by hippocampal place cells. Hippocampus 17, 381–395. https://doi.org/10.1002/hipo.20277. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, 2091–2104, July 5, 2023 2103 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

44. Markus, E.J., Qin, Y.L., Leonard, B., Skaggs, W.E., McNaughton, B.L., and Barnes, C.A. (1995). Interactions between location and task affect the spatial and directional firing of hippocampal neurons. J. Neurosci. 15, 7079–7094. https://doi.org/10.1523/JNEUROSCI.15-11-07079.1995. 

45. Hafting, T., Fyhn, M., Molden, S., Moser, M.B., and Moser, E.I. (2005). Microstructure of a spatial map in the entorhinal cortex. Nature 436, 801–806. https://doi.org/10.1038/nature03721. 

46. Sargolini, F., Fyhn, M., Hafting, T., McNaughton, B.L., Witter, M.P., Moser, M.B., and Moser, E.I. (2006). Conjunctive representation of position, direction, and velocity in entorhinal cortex. Science 312, 758–762. https://doi. org/10.1126/science.1125572. 

47. Solstad, T., Boccara, C.N., Kropff, E., Moser, M.B., and Moser, E.I. (2008). Representation of geometric borders in the entorhinal cortex. Science 322, 1865–1868. https://doi.org/10.1126/science.1166466. 

48. Kropff, E., Carmichael, J.E., Moser, M.B., and Moser, E.I. (2015). Speed cells in the medial entorhinal cortex. Nature 523, 419–424. https://doi. org/10.1038/nature14622. 

49. Jun, J.J., Steinmetz, N.A., Siegle, J.H., Denman, D.J., Bauza, M., Barbarits, B., Lee, A.K., Anastassiou, C.A., Andrei, A., Aydın, C¸ ., et al. (2017). Fully integrated silicon probes for high-density recording of neural activity. Nature 551, 232–236. https://doi.org/10.1038/nature24636. 

50. Steinmetz, N.A., Aydin, C., Lebedeva, A., Okun, M., Pachitariu, M., Bauza, M., Beau, M., Bhagat, J., Bo¨ hm, C., Broux, M., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. Science 372, eabf4588. https://doi.org/10.1126/science.abf4588. 

51. Mankin, E.A., Sparks, F.T., Slayyeh, B., Sutherland, R.J., Leutgeb, S., and Leutgeb, J.K. (2012). Neuronal code for extended time in the hippocam- 

pus. Proc. Natl. Acad. Sci. USA 109, 19462–19467. https://doi.org/10. 1073/pnas.1214107109. 

52. Mankin, E.A., Diehl, G.W., Sparks, F.T., Leutgeb, S., and Leutgeb, J.K. (2015). Hippocampal CA2 activity patterns change over time to a larger extent than between spatial contexts. Neuron 85, 190–201. https://doi. org/10.1016/j.neuron.2014.12.001. 

53. Kentros, C.G., Agnihotri, N.T., Streater, S., Hawkins, R.D., and Kandel, E.R. (2004). Increased attention to spatial context increases both place field stability and spatial memory. Neuron 42, 283–295. https://doi.org/ 10.1016/s0896-6273(04)00192-8. 

54. Skaggs, W.E., McNaughton, B.L., and Gothard, K.M. (1993). An information-theoretic approach to deciphering the hippocampal code. In Advances in Neural Information Processing Systems 5, [NIPS Conference] (Morgan Kaufmann Publishers Inc.), pp. 1030–1037. 

55. Agresti, A. (2015). Foundations of Linear and Generalized Linear Models (John Wiley & Sons Inc). 

56. Cover, T.M., and Thomas, J.A. (2006). Elements of Information Theory (John Wiley & Sons, Inc). https://doi.org/10.1002/047174882X.ch2. 

57. Shannon, C.E. (1948). A mathematical theory of communication. Bell Syst. Tech. J. 27, 379–423. https://doi.org/10.1002/j.1538-7305.1948. tb01338.x. 

58. Panzeri, S., Senatore, R., Montemurro, M.A., and Petersen, R.S. (2007). Correcting for the sampling bias problem in spike train information measures. J. Neurophysiol. 98, 1064–1072. https://doi.org/10.1152/jn. 00559.2007. 

59. Kullback, S., and Leibler, R.A. (1951). On information and sufficiency. Ann. Math. Statist. 22, 79–86. https://doi.org/10.1214/aoms/1177729694. 

2104 Neuron 111, 2091–2104, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|
|---|---|---|---|---|
||||||
|Experimental models: Organisms/strains|||||
||||||
|Rat: Long-Evans|Bred inhouse at KISN<br>Kavli Institute for Systems Neuroscience||||
||||||
|Software and algorithms|||||
|Matlab 2020a|MathWorks<br>https://mathworks.com/products/matlab.<br>htmlRRID: SCR_001622||||
|Cheetah 6.3.1|Neuralynx<br>https://neuralynx.com/||||
|MClust|A.D. Redish<br>https://redishlab.umn.edu/mclust||||
|SpikeGLX|Jun et al.49<br>https://billkarsh.github.io/SpikeGLX/||||
|Kilosort|Steinmetz et al.50<br>https://github.com/MouseLand/Kilosort||||
|Phy|Jun et al.49<br>https://github.com/cortex-lab/phy||||
|OptiTrack Motive|OptiTrack<br>https://optitrack.com/software/motive/||||
|Custom software|This paper<br>https://doi.org/10.5281/zenodo.7797252||||
|Other|||||
||||||
|Axona Microdrives|Axona<br>https://www.axona.com||||
|Neuralynx Acquisition System|Neuralynx<br>https://neuralynx.com/||||
|Neuropixels Probes|Neuropixels<br>https://www.neuropixels.org/||||
|Neuropixels Control System|Neuropixels<br>https://www.neuropixels.org/control-<br>system||||
|Optitrack Flex 13 USB cameras|<br>OptiTrack<br>https://optitrack.com/cameras/||||
|Zeiss AxioImager|Zeiss<br>N/A||||
|Deposited data|||||
||||||
|Datasets|This paper<br>https://doi.org/10.25493/Q0FG-1X8||||
||||||



## RESOURCE AVAILABILITY 

## Lead contact 

Further information and requests for resources should be directed to and will be fulfilled by the lead contact, May-Britt Moser (may-britt.moser@ntnu.no). 

## Materials availability 

This study did not generate new unique reagents. 

## Data and code availability 

- d Data are publicly available as of the date of publication (https://doi.org/10.25493/Q0FG-1X8). 

- d Code has been deposited on Zenodo (https://doi.org/10.5281/zenodo.7797252). 

- d All information is provided in the key resources table. Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request. 

## EXPERIMENTAL MODEL AND SUBJECT DETAILS 

Data were obtained from 10 male Long-Evans rats aged 2-3.5 months (320-470 grams) at the time of implantation. The rats were housed with 2-4 littermates prior to surgery. After implantation, the rats were housed individually on a single floor in large, dual-floor metal cages (95 x 63 x 61 cm) with access to food and water ad libitum throughout the entire experiment. The cages contained nesting material and were enriched with cardboard and plastic houses and contained a heightened platform. The rats were kept in a temperature and humidity controlled environment and kept on a 12 hour light/12 hour dark schedule. All testing occurred during 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e1 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

the dark phase. All experiments were performed in accordance with the Norwegian Animal Welfare Act and the European Convention for the Protection of Vertebrate Animals used for Experimental and Other Scientific Purposes and were approved by the Norwegian Food Safety Authority (permit numbers 7163 and 18011). 

## METHOD DETAILS 

## Surgery and electrode implantation 

## Tetrode experiments 

Seven rats were implanted with one or two "microdrives," each containing a single bundle of four or eight tetrodes. Five of these rats were implanted with a single eight-tetrode microdrive targeting the CA1 and CA3 areas of the hippocampus, whereas two rats were implanted with one four-tetrode microdrive targeting CA1/CA3 in one hemisphere and one eight-tetrode microdrive targeting the medial entorhinal cortex (MEC) of the opposite hemisphere. Few cells were recorded on the MEC tetrodes and the data from these tetrodes was not used. Choice of hemisphere varied across rats. Tetrodes were constructed from four twisted 17-mm polyimidecoated platinum-iridium (90–10%) wires (California Fine Wire). The electrode tips were plated with platinum to reduce electrode impedances to between 120 and 220 kU at 1 kHz. 

Anaesthesia was induced by placing the rat in a closed glass induction chamber filled with 5 % isoflurane (air flow: 0.4 l/min; oxygen flow: 0.4 l/min). The rat was given subcutaneous injections of buprenorphine (Temgesic, 0.03 mg/kg), meloxicam (Metacam, 1 mg/kg), and atropine (0.05 mg/kg). The local anaesthetic bupivacaine (Marcain, 1 mg/kg) was injected subcutaneously before the incision was made. After injections the rat was moved to a raised platform with a mask and a stereotactic frame and the head was secured in place with a set of ear bars. The rat’s body was resting on a heating pad (38[�] C) to ensure that the body temperature was maintained throughout the surgery. Isoflurane levels were gradually reduced to 0.5-1.5 % depending on the physiological condition of the rat, which was evaluated by reflex responses and breathing patterns. 

After the incision had been made, the periost was removed and the craniotomies were drilled. Tetrodes targeting CA1/CA3 were implanted without an angle at 3.2 mm lateral to the midline and 3.8-4 mm posterior to bregma. Tetrodes targeting MEC were implanted at 4.5 mm lateral to the midline and 0.1 mm anterior to the transverse sinus edge, with an anterior angle of 25[�] relative to the bregma/lambda horizontal reference. The initial depth of the tetrode tips varied between 1500 and 2000 mm relative to the dura mater. The microdrives were secured to the skull using an adhesive (OptiBond, Kerr), dental cement (Meliodent), and 2-5 Jeweller screws (M1.4) that were placed in vertically drilled holes in the parietal bones. One or two screws were placed in the occipital bone over the cerebellum and were connected to the drive grounds. 

After the surgery, the rat was left in a heated chamber (30[�] C) for 30-60 minutes for the immediate recovery phase, after which it was transferred back to the home cage. Additional doses of buprenorphine were administered 8-12 and 24 hours after the first injection. Meloxicam was administered once every 24 hours for as long as was assessed necessary (usually 3-4 days). The rat was left to recover for 3-5 days before the experiments began. 

## Neuropixels experiments 

Three rats were implanted bilaterally with four-shank Neuropixels 2.0 silicone probes[49][,][50] targeting the CA1/CA3 in one hemisphere, and the MEC in the opposite hemisphere. The MEC data were not used in the present study due to the small number of cells and experimental sessions. Two rats were implanted with one probe in each hemisphere, whereas one rat was implanted with two probes in the left hippocampus and one probe in the right MEC. In this case, the two hippocampal-targeting probes were glued together at the probe base prior to surgery and the in total eight probe shanks were implanted in the same craniotomy. The hippocampal probe tips were lowered to 7000-7500 mm relative to the dura mater. The stereotactic coordinates and the surgical procedure were the same as described above for tetrode experiments and have been described in detail elsewhere.[27] The probes were secured to the skull using Optibond and Venus (Kulzer) and protected by fitting a modified falcon tube. After surgery and the initial recovery in the heating chamber, the rat was kept in the home cage for approximately 3 hours before experiments began. Post-operative analgesia was administered as described above. 

## Behavioral procedures 

Before surgery, the rats were habituated to being handled by the experimenter and familiarised with the experimental task and environment during training sessions. Each rat underwent 7-15 training sessions, lasting at least 20 minutes each on separate days. During each training session, the rat foraged for randomly scattered corn puff crumbs in a 150 cm x 150 cm square arena with 50 cm tall black walls. The floor mat was either matt black or dark blue/green. Tetrode rats were not familiarised with the object prior to surgery, whereas Neuropixels rats had six or seven extra training sessions before surgery where the object was placed into the arena in order to avoid novelty effects of the object during recordings. 

Tetrode sessions were performed in one of two different rooms. In one room, the arena was encircled by a set of lightproof blue curtains. A large white paper sheet was attached to the curtain on one side as a distal cue. The arena in the second room had curtains hanging on only one side of the arena and various distal cues were visible to the rat on the remaining sides. Neuropixels sessions were performed in a single room, where the arena was surrounded by a set of lightproof blue curtains on three sides. On the fourth side, the curtains were open towards a white wall on which a shelf containing the recording apparatus was placed. 

e2 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

During experimental testing, each recording session consisted of either three or four trials. In all trials, the rat was freely foraging for randomly scattered corn puff crumbs. Each trial typically lasted 20-30 minutes, depending on how long it took the rat to fully cover the extent of the arena. The first trial was always an empty arena (No Object). This was followed by a trial in which a colourful Duplo tower (52 cm x 10 cm x 10 cm) was placed at or close to the middle of the arena (Object). In the third trial, the Duplo tower was moved to another, semi-random location in the arena, usually towards one of the four corners (Object Moved; approximate range of distance from the corner: 35-55 cm). A fourth trial in which the object was removed was used to check for carry-over (hysteresis) of firing at the former object location (No Object’). In the few cases where the rat would stop exploring the arena, the fourth trial was omitted from the experiment (this happened to 8.5% of the cells). Between each trial, the rat was placed on a towel in a flowerpot on a pedestal next to the arena for 1-3 minutes and given a cookie with vanilla cream and access to a water bottle. 

It has previously been shown that the activity of CA cells can change dynamically over time without changes in context[51–53] To control for this, a separate set of experiments was performed, where cells were recorded as the rat foraged freely in the same open field arena during four consecutive trials without an object (Control sessions; Figure 2B). All other parameters were the same as for sessions with the object. 

In the tetrode experiments, recordings typically started 3-5 days after implantation. The tetrodes were turned down in steps of 50 mm per day. To determine if the tetrodes were in the CA1 pyramidal cell layer, cells were recorded as the rat explored the empty open field arena and the presence of theta modulation together with the presence of at least 5-10 place cells was used as criteria. When the criteria were met for the first time, the full experimental protocol was started. The tetrodes were subsequently moved down in steps of 50 mm per day at the most, and the experiment was repeated several times over the course of 1-2 months (up to 25 recording sessions per animal). In two of the rats, the tetrodes were subsequently lowered to the CA3 and experiments were repeated as for the CA1 recordings. 

The Neuropixels data were obtained from a total of four recording sessions from the three rats. Two of the rats were only recorded once, whereas the third was recorded two times (first in CA1 and then in CA3) with a 3-day interval between the two recording sessions. All recording sessions were performed within 72 hours after recovery from surgery. 

## Recording procedures 

## Tetrode experiments 

During electrophysiological recordings, the microdrives (with tetrodes) were connected to a Neuralynx data acquisition system (Neuralynx, Tucson, AZ; Neuralynx Digital Lynx SX) through a multichannel, impedance matching unity gain head stage. The output of the head stage was conducted via a lightweight multi wire tether cable and a slip-ring commutator. Unit activity was amplified by a factor of 3000-5000 and band-pass filtered from 600 to 6000 Hz. Spike waveforms above a threshold of 30 or 40 mV were timestamped and digitized at 32 kHz for 1 ms. Local field potential (LFP) signals were recorded from each tetrode, amplified by a factor of 250-1000, low-pass filtered at 300-475 Hz and sampled at 1800-2500 Hz. An overhead camera recorded the position of two lightemitting diodes (LEDs) on the head stage in order to track the rat’s movements at a sampling rate of 25 Hz. The diodes were separated by 4 cm. 

## Neuropixels experiments 

Signals were recorded using a Neuropixels acquisition system as described previously.[27][,][49][,][50] Briefly, the spike band signal was amplified at a gain of 80, low-pass-filtered at 0.5 Hz, high-pass-filtered at 10 kHz, and digitalised at 30 kHz on the probe circuit board. The signal was then multiplexed and transmitted to a Neuropixels PXIe acquisition module via a 5 m tether cable made using twisted pair wiring. A 3D motion capture system consisting of six OptiTrack Flex 13 cameras and Motive software was used to track the rat’s movement at a sampling rate of �120 Hz. Five reflective markers glued to a rigid body was attached to the rat’s implant during recording. Randomised sequences of digital pulses were generated by an Arduino microcontroller. In order to synchronise the timestamps of the two recording systems, the pulses were sent to the Neuropixels acquisition system as direct TTL input and to the OptiTrack system via infrared LEDs that were placed on the edge of the arena. 

## Histology and reconstruction of electrode placement 

The rat was placed in a closed glass induction chamber filled with 5% isoflurane (air flow 1.2 l/min) to induce anaesthesia. It was then given an overdose of pentobarbital injected intraperitoneally and perfused intracardially with saline followed by 4% formaldehyde. The brain was removed and stored in formaldehyde. Frozen 30 mm sagittal sections were cut, mounted on glass, and stained with Cresyl violet (Nissl). 

The final position of the tip of each tetrode or the placement of the probe shank was identified on photomicrographs obtained with an Axio Scan.Z1 microscope and ZEN software (Zen 2.6; Carl Zeiss). The tip of the tetrode was used to determine the anatomical location of the recorded cell. For the Neuropixels experiments, the depths of the probe shank tips were measured in ZEN software. The known position of active recording sites relative to the tip was then used to determine the location of the recorded cells. CA1 and CA3 recording locations were distinguished based on depth and activity profiles along the probe shanks. Recorded cells that were judged to be in the cortex overlying the CA1 or in the dentate gyrus were excluded from all analyses. 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e3 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

## Spike sorting and cell-inclusion criteria 

Spike sorting of tetrode data was performed offline using the graphical cluster-cutting software MClust (A.D. Redish, https:// redishlab.umn.edu/mclust). Spikes were clustered manually in 2D projections of the multidimensional parameter space (consisting of waveform amplitudes and waveform energies), using autocorrelation and crosscorrelation functions as additional separation tools and separation criteria. To follow cells across recording sessions, clusters of successive sessions were compared and identified to be the same unit if the locations of the spike clusters in the multidimensional parameter space were stable. Spike sorting of Neuropixels data was performed using a version of KiloSort 2.5[50] with customisations as described previously.[27] 

For both types of experiments, all trials in a session were clustered together. Single units were discarded if more than 1% of their inter-spike intervals were less than 2 ms. Further, cells were excluded if they had a mean spike rate of less than 0.05 Hz or greater than 10 Hz across the full recording session. 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

Data analyses were performed with custom-written scripts in MATLAB (Version 2020a). The study did not involve any experimental subject groups; therefore, random allocation and experimenter blinding did not apply and were not performed. 

## Firing rate maps and identification of firing fields 

2D rate maps that displayed the firing rate as a function of the position of the animal in the arena were calculated for each trial separately. First, position estimates were binned into a square grid of 2.5 cm x 2.5 cm bins. Next, the firing rate in each position bin was calculated as the number of spikes recorded in the bin, divided by the time the rat spent in the bin. The 2D rate map was smoothed with a Gaussian kernel with standard deviation of 2 bins in both the x and the y direction. Only time epochs in which the animal was moving at a speed above 2.5 cm/s were used for constructing the rate maps and for spatial analyses. 

Firing fields in the rate map were detected by iteratively applying the Matlab "contour" function (Mathworks), starting from the cell’s peak firing rate until it reached 3 3 median absolute deviation (MAD) of the firing rates of all bins in the rate map. Firing fields were defined as contiguous areas within a contour with a size of at least 225 cm[2] and with a minimum firing rate of at least 1 Hz. 

## Spatial information content 

To calculate the spatial information content in each cell’s firing, the rate map was used. First, the spatial information rate[54] was computed as 

**==> picture [64 x 24] intentionally omitted <==**

where N is the total number of bins (3200 bins in total), li is the firing rate in the i-th bin of the rate map, l is the mean firing rate in the trial, and Pi is the probability of the rat being in the i-th bin, calculated as the occupancy in the i-th bin (time spent in the bin) divided by the total duration of the trial. Spatial information content (in bits per spike) was then obtained for each trial by dividing the spatial information rate by the mean firing rate of the cell in that trial. 

## Shuffling of spike data 

To determine significance for spatial information content, a per-trial shuffling procedure was implemented for each cell separately. For each trial, the sequence of spike timestamps was circularly shifted (with the end of the trial wrapped to the beginning of the trial) by a displacement that took random values between 20 seconds and 20 seconds less than the duration of the trial. Time shifts varied randomly between trials and between cells. The shuffling procedure was repeated 1000 times per trial per cell. For each shuffle iteration, the rate maps were recalculated and the spatial information content was computed using the position of the rat, which remained unchanged, and a shuffled distribution of spatial information content values was built. A cell was judged to be spatially modulated in the trial if the spatial information content calculated on the experimental data was above the 99[th] percentile of the shuffled distribution. 

## Template matching procedure to identify object-tuned cells 

We developed a template matching procedure to identify cells firing at the location of objects ("object cells") and cells firing in fixed distances and directions from objects ("object-vector cells"). Throughout the paper, we refer to such cells as "object-tuned cells." 

First, we placed a Gaussian template at a specific location in the Object trial. The template was then transferred to the same location in the Object Moved trial, relative to the object. For example, the template’s location (i.e. the mean of the Gaussian) could be 15 cm North from the object, or directly at the object (as in Figure 1B, left). The template location (relative to the object) was always the same in both trials. 

Second, we calculated the Pearson correlation between the template and the cell’s actual firing rate map in both the Object and Object Moved trials. This gave a measure of how strongly the cell’s firing pattern resembled the template in each of the trials. Because an object-tuned cell should fire relative to the object consistently in both trials, we took the minimum of these two Pearson 

e4 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

correlations as an "object-tuning score." Taking the minimum ensures that we only classify cells as object-tuned cells if their firing patterns move along when the object moves. 

object tuning score = minðcorrobject; corrobject movedÞ 

## Parametric variations 

Since cells can fire at a variety of distances and directions from the object, we repeated the calculation of object-tuning score with the template in different locations (9 offsets, including the template located at the object, and 8 directions, Figure 1B, right). Similarly, we repeated the calculation with 8 different variances (s[2] ) of the Gaussian template. Each combination of offsets, angles and variances gives one object-tuning score and constitutes a specific hypothesis about how the cell’s firing could be related to the object. 

The offsets between the object and the template’s center were 0, 5, 10, 15, 20, 30, 40, 50 and 60 cm. The angles between the object and template varied between 0 and 2p, in steps of p/4. That is, the template could be shifted in 8 cardinal directions. The variances of the Gaussian template were 5, 10, 25, 75, 50, 100, 150 and 200 cm. 

This meant that, for each cell, we calculated 520 object-tuning scores: 8 variances 3 (8 angles 3 8 offsets + 1 offset at the object) = 520. In other words, we evaluated 520 different hypotheses of how the cell’s firing could be related to the object. 

To determine whether the obtained scores were statistically significant, we compared the actual object-tuning scores to scores calculated on shuffled data. We created shuffled data by choosing the template location randomly in both the Object and Object Moved trials, and then re-calculated the object-tuning score. We repeated this procedure 500 times. 8 shuffling distributions were created for each cell (1 for each variance of the Gaussian template), because we only compared actual scores to shuffled scores using the same variance of the Gaussian template. For example, if the template’s variance was s[2] = 50 when calculating the actual object-tuning score, the template’s variance was also s[2] = 50 for the shuffled scores. We therefore had a total of 8 3 1189 shuffling distributions, where 8 is the number of variances and 1189 is the number of cells. If the cell had one or more object-tuning scores larger than the 99[th] percentile of the shuffled distribution, we considered the cell object-tuned. 

Most object-tuned cells (88.6%) had more than one significant object-tuning score, while only a small fraction (11.4%) had one significant score (Figure S2B). Since object-tuned cells typically fitted more than one template (with slight variations in template parameters), this means that an approximate fit between the template and the cell’s actual firing pattern is sufficient for detection. The result also suggests that step sizes in our parameters were small enough. 

To roughly estimate the number of object-tuned cells that were object cells and object-vector cells, we used the distance between the cell’s firing field and the object. Cells with firing fields less than 15 cm from the object were considered object cells; cells with firing fields more than 15 cm from the object were considered object-vector cells. In a small number of object-tuned cells, the firing field detection algorithm did not identify any firing fields, either because the activity was too low or scattered to form firing fields (see Firing rate maps and identification of firing fields for details about the algorithm). These cells were therefore not separated into object cells or object-vector cells (30/1189 cells). 

## Chance level 

To estimate the chance level in classification of object-tuned cells (5.03%), we repeated the same template matching procedure for cells recorded in control trials without objects (Figure 2B) (n = 219 CA1 cells). For this, we used the middle of the arena as the object location in the Object trial (x = 75 cm, y = 75 cm) and the upper-left corner of the arena as the object location in the Object Moved trial (x = 35 cm, y = 120 cm) (the most common object location in Object Moved trials). 

## Object-vector score and object-vector cell criteria 

To confirm that the general template matching procedure (see above) identified object-vector cells, we applied the methods used in previous publications to identify object-vector cells.[11][,][12] For this, we constructed "vector maps" that expressed each cell’s firing as a function of the animal’s distance and direction from the object. After constructing vector maps from the Object and Object Moved trials, we used the Pearson correlation between the two maps as an "object-vector score." To create shuffled data, we circularly shifted each cell’s spike train 500 times (as described under Shuffling of spike data) and re-calculated the object-vector score. Object-vector scores from cells that were above the 99th percentile of the shuffled distribution were considered significant. 

Before applying the criteria, we excluded cells with firing fields that would fall outside of the arena in the Object Moved trial (for example, when the object was moved to the south-east corner, when the cell fired at a south-east angle from the object) (28.8% of CA1 cells were excluded). 

Cells were considered object-vector cells if the following criteria were met: 

- 1) The spatial information content was above the 99[th] percentile of the shuffled distribution in both the Object and the Object Moved trials. 

- 2) The object-vector score was above the 99[th] percentile of the shuffled distribution. 

- 3) One or more firing fields were present in the Object and the Object Moved trials. 

- 4) The firing field had to be at least 15 cm distance from the object (to select object-vector cells rather than object cells). 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e5 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

40 out of 1189 cells (3.4%) were classified by this method but not by the template matching procedure. Manual inspection showed that these cells were mostly false positives, confirming that the template matching procedure correctly classified object-vector cells. 

## Spatial correlation and rate overlap 

In order to determine whether the firing activity of single cells changed or remained stable when the object was introduced, moved, or removed from the environment, two measures were considered: 

- 1) Spatial correlation 

## 2) Rate overlap 

The spatial correlation between two trials was defined as the Pearson correlation between the overlapping parts of the two firing rate maps (excluding bins that contained no value in either rate map). The rate overlap between two trials was calculated by dividing the mean firing rate in the less active trial by the mean firing rate in the more active trial. 

To classify a cell’s response as changing or stable, a baseline stability of the cell’s firing within a trial ("within-trial") was first assessed. The position data and the corresponding spike timestamps from the first trial (No Object) were binned into n sections of 1-second duration, where n is the full duration of the No Object trial in seconds. The bins were randomly assigned to two groups of size n/2. New rate maps for the two groups were then constructed, and the spatial correlation and the firing rate overlap between them was calculated. The procedure was repeated 500 times for each cell, with different bins randomly assigned to the two groups for each permutation. 

For each between-trial comparison (e.g., No Object – Object), the same procedure as for the within-trial comparison was used. Position data and corresponding spiking data were randomly assigned to two groups of n/2 bins of 1 second duration for each of the two trials separately. Only one of the two groups (i.e., half of the data) from each trial was used and spatial correlation and rate overlap between the two trials were calculated as described above. The procedure was again repeated 500 times per between-trial comparison. A cell’s response was classified as changing if the mean of the between-trial distribution fell below the 1[st] percentile of the within-trial distribution from the No Object trial, and if the mean ranks of the two distributions were judged to significantly different (assessed using a Wilcoxon signed-rank test). 

## Region-of-interest analysis for object traces 

To investigate the presence of object-trace fields, we first pre-selected for cells that changed their spatial firing patterns or firing rates between No Object and No Object’ (quantified with spatial correlation and rate overlap, using criteria defined in the previous section). For these pre-selected cells (n = 919), we identified firing fields in No Object’. Then, a circular ROI was defined in the same way as described in section Region-of-interest analysis for object responses. The ROI was transferred to the same location in the other three trials (No Object, Object, and Object Moved). The firing rate overlap was calculated between the No Object’ ROI and the other three ROIs. We used rate overlaps from all trials to test which trial combinations produced the largest rate overlap (and therefore the strongest object traces) (Figure S4B). 

To determine the presence of object traces, we used the rate overlap with the Object Moved trial. For this, a shuffling procedure where the ROI identified in No Object’ was placed at random locations in the Object Moved rate map ("Shuffled ROI") was applied. Bins of the Shuffled ROI that fell outside the boundaries of the rate map were wrapped around to the opposite site of the rate map. This was repeated 1000 times, and for each shuffle iteration, the rate overlap between the actual ROI in the No Object’ trial and a Shuffled ROI in the Object Moved trial was calculated. All 1000 values of rate overlap were then used to build a shuffled distribution. If the rate overlap between the ROI in No Object’ and Object Moved was greater than the 99[th] percentile of the shuffled distribution, the cell was classified as having an object-trace field (Figures S4C and S4D). 

## Bayesian decoding algorithm 

For this and all other sections using population activity, we used n = 15 tetrode sessions with a minimum of 25 and a maximum of 39 cells recorded simultaneously (the threshold for including a tetrode session being that it had a minimum of 25 cells) and n = 2 Neuropixels sessions with 620 cells (from two probes) and 135 cells (from a single probe), respectively. 

To assess whether population activity in the hippocampus contains information about objects in the environment, we used a decoding approach. Building upon an existing Bayesian decoder,[22] we used rate maps to infer whether samples of neural activity occurred in the absence or presence of an object (No Object or Object trial). We divided the data into two groups, for training and testing (first half of data used for training and second half for testing; then vice versa in a separate iteration). While the training data was used to create rate maps, the testing data consisted of samples that the decoder classified as coming from the ‘‘No Object’’ or ‘‘Object’’ trial. Specifically, one sample of the testing data was a vector of spike counts from all hippocampal cells in a 1 second time window: 

d1 Data = 0B d2 1C B « C @ dN A 

e6 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

where di is the number of spikes produced by each hippocampal cell in the 1 second time window and N is the total number of recorded cells in a session. Overall, our goal is to compare the likelihood that the ‘‘Data’’ are from the ‘‘No Object’’ trial against the likelihood that they are from the ‘‘Object’’ trial. This is given by the likelihood ratio: 

**==> picture [141 x 13] intentionally omitted <==**

**==> picture [60 x 9] intentionally omitted <==**

To calculate PðDataj No ObjectÞ, because ‘‘Data’’ could have occurred when the animal was in any spatial bin, we started by introducing another term x on the right-hand side of the probability and asking how likely it is that the ‘‘Data’’ are from a specific spatial bin x (50 3 50 spatial bins, x = 1, 2., 2500) in the No Object trial: PðDataj x; No ObjectÞ. 

To calculate the likelihood PðDataj x;No ObjectÞ, we assume that each cell fires according to a Poisson distribution with mean firing rate riðxÞ, where i is the cell index and x is the spatial location of the animal. Each riðxÞ is obtained by going to the rate map for cell i and extracting the firing rate in spatial bin x. In that sense, rate maps constructed from training data are used as a look-up table. The likelihood was calculated by: 

**==> picture [150 x 24] intentionally omitted <==**

where di is the number of spikes produced by cell i and where the multiplication over Poisson distributions from N cells indicates the assumption of independence between firing of different cells. Note that the more consistent the set of spike counts fdig are with the set of firing rates friðxÞg, the larger the value of the likelihood. 

The likelihood was next multiplied by a prior, 

**==> picture [60 x 9] intentionally omitted <==**

given by the fraction of time the animal spent in spatial bin x during the No Object trial. This accounts for the intuition that the ‘‘Data’’ are more likely to come from a given spatial bin if the animal spent a lot of time in that bin. We then marginalised over all spatial bins x (50 3 50 bins), 

**==> picture [236 x 18] intentionally omitted <==**

to obtain the overall likelihood of the No Object trial. The same calculation is performed for the Object trial to obtain the overall likelihood of the Object trial, PðDataj ObjectÞ. The ratio of these terms determines the decoder’s output. That is, if PPðDataðDatajNoj ObjectObjectÞ Þ[>][ 1, the] decoder infers the ‘‘Data’’ as being from the No Object trial; otherwise, from the Object trial. 

Since the length of an experimental trial was 1800 seconds, 1800/2 = 900 seconds could be used as testing data. With a bin size of 1 second, this gave us 900 testing samples. Given the two iterations described above (using either the first or second half of the trial as testing data), we had 90032 = 1800 testing samples. The decoding accuracy was the fraction of 1800 samples classified correctly. The chance level of the decoder was calculated through a shuffling procedure (see Shuffling trial labels). 

## Calculation of decoding accuracy as a function of distance and allocentric angle 

To understand how decoding performance depended on the animal’s spatial relationship with the object, we asked how decoding accuracy changed as a function of the animal’s distance and allocentric angle relative to the object (Figures 4A–4C and 4D–4F, respectively). To examine the role of distance, we divided spike and position data into 5 distance bins, forming concentric rings around the object (Figure 4A). By creating training data and testing data for each specific distance bin and feeding these separately into the decoder, we could assess how decoding accuracy differed as a function of distance from object. For each experimental session, we optimized distance bins so that we had an equal number of testing samples within each bin. For example, if the animal spent little time near the object, distance bin 1 was made larger to obtain more samples. This helped to account for differences in the animal’s behavior in different experimental sessions. Specifically, the length of an experimental session was 1800 seconds, allowing 1800/2 = 900 seconds to be used for testing data. This gave 900/5 = 180 seconds of testing data per distance bin. Because the bin size was 1 second, we had 180 testing samples per distance bin. The decoding accuracy in each distance bin was the fraction of 180 testing samples classified correctly. To examine the role of allocentric angle, we used an analogous procedure. In this case, we divided spike and position data into 5 angular bins, forming sectors of a circle (Figure 4D), and created training and testing data separately for each angular bin. 

## Performance of decoder 

## Effect of bin size 

To assess the performance of the decoder, we first asked how decoding performance depended on the bin size of testing data. For this analysis, we ran the decoder separately using bin sizes of 10, 50, 100, 500, 1000, 5000 and 10000 ms and calculated the decoding accuracy. Larger bin size corresponds to observing more spike counts from each hippocampal cell, which will lead to spike counts fdig that are more similar to the mean firing rates friðxÞg. Consistent with this idea, performance increased with increasing 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e7 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

bin size. Specifically, performance increased rapidly up to 1000 ms, after which it saturated and gains of increasing bin size were lower (Figure 3C). Based on these results, we chose 1000 ms as bin size for all main analyses. Effect of number of cells 

To assess how decoding performance depended on the number of cells fed into the decoder (Figure 3E), we used a subsampling approach. We randomly selected a subset of k cells from a Neuropixels dataset with a total of N = 620 cells, iterating over k = f1; 5; 10; 20; 30; 50; 100; 200; 300; 400; 500g cells. For each k, we ran the decoder 100 times, using different subsets of cells each time. 

## Controls for results of decoder 

## Fixed distance bins 

To ensure that our findings did not depend on using distance bins with an equal number of samples (described in Calculation of decoding accuracy as a function of distance and allocentric angle), we repeated the main analysis with fixed distance bins. In this case, we divided spike and position data into distance bins with fixed values of 0-20 cm, 20-40 cm, 40-60 cm, 60-80 cm and 80-100 cm for all experimental sessions, ignoring differences in the animal’s behavior. 

## Decoding 1st half vs. 2nd half of No Object trial 

To ensure that our findings could not arise without the presence of an object, we attempted to classify data samples belonging to either the 1st and 2nd half of the No Object trial, as a negative control. For this, we divided the No Object trial at its midpoint. For example, a 1800 seconds long trial would be split at 900 seconds, with 450 seconds for training data and 450 seconds for testing data for each one of the halves. The two halves were then used as input to the decoder (rather than the No Object and Object trials). Decoding in control experiments without objects 

To further test whether our findings could arise without objects, we performed the decoding in control experiments without objects present (Figure 2B). For this, the trials Control 1 and Control 2 were used as input to the decoder (rather than the No Object and Object trials). 

## Shuffling trial labels 

To ensure that our findings reflected a real relationship between population activity and trial type, we shuffled the trial labels of all testing data samples. That is, after shuffling, a spike count vector labelled ‘‘No Object’’ had 50% chance of being labelled ‘‘Object.’’ To perform the shuffling, we first concatenated testing data from the ‘‘No Object’’ and ‘‘Object’’ trials into an N3T spike matrix, where N is the number of cells and T the total number of timepoints. To shuffle the trial labels, we first randomly permuted the set of integers f1; 2; 3.Tg using the MATLAB function randperm. For example, consider the simple case of T = 10. The original arrangement of the N31 spike count vectors in the matrix would be f1; 2; 3; 4; 5; 6; 7; 8; 9; 10g, where timepoints 1-5 would come from ‘‘No Object’’ and timepoints 6-10 would come from ‘‘Object.’’ The permuted rearrangement might be f7;1;2;6;10;4;8;3;9;5g. After permutation, the first T/2 spike count vectors were labelled ‘‘No Object’’ and the last T/2 spike count vectors were labelled ‘‘Object.’’ This shuffling procedure destroys any real relationship between population activity and trial type. 

## Random partitioning into training and testing data 

In the main analysis, we used the first half of the session as training data and the second half as testing data (and vice versa in a separate iteration). To confirm that our findings did not depend on such a partitioning, we used an alternative partitioning method where we randomly chose which set of timepoints would constitute training data. The random partitioning was analogous to the shuffling procedure above, but without concatenating spike matrices from the ‘‘No Object’’ and ‘‘Object’’ trials. For example, if data from ‘‘No Object’’ consisted of T timepoints, we generated a random permutation of the set of integers f1; 2; 3.Tg and used the first T/2 integers as timepoints for training data and the last T/2 integers for testing data (and vice versa in a separate iteration). Removing object-tuned cells 

To test whether object-tuned cells (object cells and object-vector cells) were necessary for the distance-dependent decrease in decoding accuracy (Figures 4B and 4C), we removed all object-tuned cells (237/1189 cells, 19.9%) (Figure 1C) and re-ran the decoder. Removing effects of prior 

The standard decoder used a prior that included information about the animal’s occupancy (see above). To ensure that our findings (Figures 4B and 4C) did not depend on using this prior, we replaced it with a uniform probability distribution (a prior that assumes that the animal spent an equal amount of time in each bin) and re-ran the decoder. Sampling analysis 

In the Object trial, the object constitutes a physical barrier preventing the animal from exploring some places. This may prevent neural activity patterns associated with that place from occurring, possibly providing a trivial explanation for high decoding success near the object. In general, parts of the environment never or rarely explored in one trial (but explored in the other trial) could potentially lead to high decoding accuracy. To ensure that lack of sampling of some parts of the environment did not influence our results (Figures 4B and 4C), we identified spatial bins in which the animal had spent less time than a threshold value (100 ms, 500 ms, 1000 ms or 2000 ms) in either trial and excluded those spatial bins from both trials. That is, only spatial bins explored longer than the threshold value in both trials were included. After excluding spatial bins with low sampling, we re-ran the decoder. Note that for this analysis, we increased the rate map bin size from 3 cm[2] to 10 cm[2] , since otherwise almost no bins would be explored longer than the sampling threshold. 

e8 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

Article 

**==> picture [46 x 35] intentionally omitted <==**

## Behavioral analyses I: Decoding 

To test whether behavioural confounds could explain the distance-dependent decrease in decoding accuracy (Figures 4B and 4C) (which could happen, for example, if the animal behaves differently between trials, and more different near the object), we developed decoders that tried to infer the trial of data samples based on the animal’s behaviour. We focused on three key and independent behavioural features: speed, head direction and spatial occupancy. The behavioural decoders were based on the same framework as the standard decoder applied to neural data (see Bayesian decoding algorithm), used the same number of spatial bins (50 3 50 bins) and divided data into training and testing data the same way. However, there are three differences between the behavioural decoders and the standard decoder: 

- The sample of testing data is now a scalar (speed and head direction) or 2-dimensional vector (occupancy), rather than a vector of spike counts. 

- The likelihood no longer uses a Poisson distribution, but other distributions that are more appropriate models of each behaviour. 

- The training data are constructed by calculating ‘‘behaviour maps’’ rather than firing rate maps. 

## Speed decoder 

For the speed decoder, each sample of testing data was now a scalar representing the animal’s instantaneous speed (cm/s) (sampled at 25 Hz). We estimated the animal’s speed (in this section denoted by s) as the norm of the vector that has as components the speed in the x and y directions. These were calculated as the change in position of the animal in the x and y directions in consecutive time bins, divided by the size of the time bin and smoothed with a Lowess filter. All speed values were included, including zero speed (immobility). Probability distributions for speed typically had a large peak at low speed values, followed by rapid decay at larger speed values (see Figure S6G for examples). We therefore used a gamma distribution for the likelihood, which provides good fits for unimodal and exponentially decaying distributions (the exponential distribution being a special case of the gamma distribution). The gamma distribution was a reasonable model for speed: after having learnt model parameters in training data, we could accurately predict the animal’s speed in testing data (statistics in Table S1). The model parameters (aðxÞ and bðxÞ, see below) were estimated by maximum likelihood. The likelihoods of parameters had well-defined peaks and covered small intervals of the parameter space (size of interval covering 95% of the likelihood’s area under the curve: for aðxÞ, 1.22 ± 0.85; for bðxÞ, 4.98 ± 1.07; median interval size ± SD), compared to the range of inferred parameter values (aðxÞ: from 0.011 to 42.40; bðxÞ: from 2.69310⁻⁴ to 36.38), suggesting that we were able to infer model parameters with reasonable precision. Using the gamma distribution, we calculated the likelihood as: 

**==> picture [244 x 23] intentionally omitted <==**

where s is the animal’s instantaneous speed, x indexes the spatial bins (50 3 50 bins in total), GðÞ is the gamma function, and aðxÞ and bðxÞ are shape and scale parameters that are functions of x because they describe the animal’s speed within every spatial bin (analogous to how the mean parameter of the Poisson distribution described the cell’s firing within every spatial bin). 

To construct training data (using the animal’s speed from half the trial), we divided speed observations in the No Object trial into spatial bins (based on the animal’s location at the time of the speed measurement), so that each spatial bin contained a vector of speed values. For every spatial bin x we then fitted a gamma distribution to the observed speed values and estimated the parameters aðxÞ and bðxÞ via maximum likelihood. This way we obtained ‘‘maps’’ for aðxÞ and bðxÞ (analogous to firing rate maps). We repeated this procedure using data from the Object trial. Finally, the obtained parameters aðxÞ and bðxÞ could then be used to calculate the likelihood. As in the standard decoder, for every testing sample we then marginalise over spatial bins to obtain the overall likelihood of the No Object and Object trials, and finally classify the sample based on the ratio of likelihoods of the No Object and Object trials (see Bayesian decoding algorithm for details). 

We verified that the speed decoder accurately identified speed differences between trials present in simulated data. For this, we either simulated (1) speed distributions that were different between the No Object and Object trials, or (2) speed distributions that became more and more different near the object. For (1), each speed measurement was drawn randomly from a gamma distribution with parameters a = 2, b = 2 for all x (No Object trial) or a = 2, b = 10 for all x (Object trial). For (2), speed measurements were drawn randomly from a gamma distribution with parameters a = 2, b = 2 (No Object trial, distance bins 1-5) or a = 2, b = 10 (Object trial, distance bin 1), a = 2, b = 8 (Object trial, distance bin 2), a = 2, b = 6 (Object trial, distance bin 3), a = 2, b = 4 (Object trial, distance bin 4) and a = 2, b = 2 (Object trial, distance bin 5). That is, in the Object trial, the b parameter approached the value of b in the No Object trial with further distance from the object, while the a parameter remained the same. Simulated speed values were sampled at 25 Hz (once per position sample). The animal’s true position at the time of sampling determined the distance bin of the speed measurement (and therefore the parameters of the gamma distribution in simulation 2). Position data were taken from the 16 experimental sessions. 

## Head direction decoder 

For the head direction (HD) decoder, each sample of testing data was a scalar representing the animal’s instantaneous HD (radians) (sampled at 25 Hz). The animal’s HD was determined from the relative positions of LEDs or reflective markers on the implant. Because HD distributions were bimodal or unimodal, we used a mixture of two Gaussians to calculate the likelihood. As before, after having learnt model parameters in training data (means, standard deviations and weights of the Gaussians, see below), the model could 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e9 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

accurately predict the animal’s HD in testing data (statistics in Table S1). The model parameters (means, standard deviations and weights, see below) were estimated by maximum likelihood. The likelihood of model parameters had well-defined peaks and covered small intervals of the parameter space (size of interval covering 95% of the likelihood’s area under the curve: for means of Gaussians, 0.20 ± 0.096; for standard deviations of Gaussians, 0.27 ± 0.23; for weights of Gaussians, 0.18 ± 0.037; median interval size ± SD) compared to the range of inferred parameter values (means: from 0 to 2p; standard deviations: from 6.06310⁷ to 6.18; weights: from 0.013 to 1), suggesting that we were able to infer model parameters with reasonable precision. 

Using a mixture of two Gaussians, we calculated the likelihood as: 

**==> picture [460 x 37] intentionally omitted <==**

where h is the animal’s head direction, x indexes the spatial bin, m1ðxÞ is the mean of the first Gaussian, s1ðxÞ is the standard deviation of the first Gaussian and w1ðxÞ is the weight of the first Gaussian, and similarly for the second Gaussian. Again, the mean, standard deviation and weight of each Gaussian are functions of x, describing the animal’s HD within every spatial bin. Note that the model is appropriate also when HD is unimodally distributed, because a mixture of two Gaussians includes one Gaussian as a special case (for example, the weight of one Gaussian can be set to zero, or the two Gaussians can be assigned the same mean and standard deviation). Finally, the model is also appropriate when the HD distribution is uniform, because the Gaussians can be assigned very large standard deviations. 

To construct training data (using the animal’s HD from half the trial), we divided HD observations in the No Object trial into spatial bins (based on the animal’s location at the time of measurement), so that each spatial bin contained a vector of HD values. For every spatial bin x we then fitted a mixture of two Gaussians to the observed HD values and estimated the means, standard deviations and weights via maximum likelihood. This way we obtained ‘‘maps’’ for all 6 parameters (analogous to firing rate maps). We repeated this procedure using data from the Object trial. Finally, the obtained parameters could be used to calculate the likelihood. As in the standard decoder, we then marginalise over spatial bins to obtain the overall likelihood of the No Object and Object trials, and finally classify the trial based on the ratio of likelihoods of the No Object and Object trials (see Bayesian decoding algorithm for details). 

We verified that the HD decoder accurately detected differences in HD between two trials in simulated data. For this verification, we simulated HD distributions from a single Gaussian since this is a special case of a mixture of two Gaussians. We either simulated (1) HD distributions that were different between the No Object and Object trials, or (2) HD distributions that became more and more different near the object. For (1), each HD sample was drawn randomly from a Gaussian distribution with parameters m = 2 and s = 0:5 for all x (No Object trial) or m = 5 and s = 0:5 for all x (Object trial). For (2), HD samples were drawn randomly from a Gaussian distribution with parameters m = 2 and s = 0:5 (No Object trial, distance bin 1), m = 2 and s = 1 (No Object trial, distance bin 2), m = 2 and s = 1:5 (No Object trial, distance bin 3), m = 2 and s = 2 (No Object trial, distance bin 4) and m = 2 and s = 10 (No Object trial, distance bin 5). In the Object trial, the parameters were the same except that m = 5 for all distance bins. That is, the standard deviations of HD distributions from the No Object and Object trials increased further away from the object, so that they both approached uniform distributions (and could no longer be distinguished). Simulated HD values were sampled at 25 Hz (once per position sample). The animal’s true position at the time of sampling determined the distance bin of the HD measurement (and therefore the standard deviation of the Gaussian in simulation 2). Position data were taken from the 16 experimental sessions. Occupancy decoder 

For the occupancy decoder, each sample of testing data represented the animal’s instantaneous position in space (sampled at 25 Hz). Because the decoder itself calculates the likelihood of different spatial bins, and then marginalises over spatial bins (see Bayesian decoding algorithm), position will now appear on both sides of the probability expressions, with different roles. On the left-hand side is the animal’s continuous location in space, as part of the testing data; on the right-hand side is the binned location in space, as part of the training data. 

**==> picture [330 x 20] intentionally omitted <==**

where pos is the continuous location of the animal (a 2-dimensional vector of real numbers), as part of testing data; xi is the i[th] spatial bin for the x coordinate and yj is the j[th] spatial bin for the y coordinate (i and j are integers between 1 and 50), and both xi and yj are part of training data. 

The occupancy decoder can now be simplified analytically, because each sample of testing data could only have occurred within a specific spatial bin (for example, the observation pos = ð149:2 cm; 148:0 cmÞ could only have occurred when the animal was in the northeast corner of the environment ðx50;y50Þ – that is, when the animal was in the ‘‘last’’ bin of an environment with 50 bins in the x coordinate and 50 bins in the y coordinate. In general, this means that: 

Pðposj xk; yl; No ObjectÞ = 1 

e10 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

Article 

**==> picture [46 x 35] intentionally omitted <==**

whenever k and l are the indices of the spatial bins that the observed position sample falls into. Also, 

P�pos�� xi; yj; No Object� = 0 

whenever isk or jsl. Plugging these equations into the likelihood gives: 

**==> picture [257 x 19] intentionally omitted <==**

**==> picture [172 x 9] intentionally omitted <==**

**==> picture [180 x 10] intentionally omitted <==**

That is, the probability that the sample of testing data comes from the No Object trial is proportional to the time that the animal spent in the relevant spatial bin. Therefore, the likelihood ratio becomes a ratio of occupancies in the relevant spatial bin: 

**==> picture [156 x 21] intentionally omitted <==**

so that we assign ‘‘No Object’’ if the animal spent more time in the spatial bin ðxkylÞ in the No Object trial than the Object trial (and vice versa). 

Given the simplification above, we constructed training data for the decoder by calculating occupancy maps (amount of time animal spent in every spatial bin, divided by total trial duration). 

We verified that the occupancy decoder could accurately identify differences in occupancy between trials in simulated data. For this, we either simulated (1) occupancies that were different between the No Object and Object trials, or (2) occupancies that became more and more different near the object. We simulated occupancies by drawing random position samples either from a uniform distribution with edges from 0 to 150 cm (for both the x and y coordinates) or from a uniform distribution with edges that covered only half the environment (y edges from 0 to 75 cm in the No Object trial and y edges from 75 to 150 cm in the Object trial; x edges from 0 to 150 cm in both trials). That is, each position sample could either be drawn from the whole environment or from half the environment. To change how strongly occupancy differed between the trials, we varied the probability of drawing position samples from the whole or half environment. For (1), the probability of drawing from half the environment was 1. That is, all position samples were drawn from the lower (No Object trial) or upper (Object trial) half of the environment. For (2), in both trials, the probability of drawing from (half the environment, whole environment) was either (1, 0) (distance bin 1), (0.75, 0.25) (distance bin 2), (0.5, 0.5) (distance bin 3), (0.25, 0.75) (distance bin 4) or (0,1) (distance bin 5). That is, in distance bin 5 position samples were drawn only from the whole environment (generating similar occupancy between the trials), while in distance bin 1 position samples were drawn only from half the environment (generating different occupancy between the trials). Also, for (2), edges of uniform distributions were adjusted so that (a) drawing from the whole environment was replaced by drawing from the whole distance bin; and (b) drawing from half the environment was replaced by drawing from half the distance bin. The number of position samples drawn was the same as the total number of position samples in real data. 

## Behavioral analyses II: Subsampling 

To test whether the decoder applied to neural data (Figures 4B and 4C) made use of behavioural differences between the trials, we reran the decoder after matching distributions of behaviour. We specifically matched behaviour between trials in every distance bin to account for any distance-dependent behavioural effects (for example, if the animal ran had biased head direction near the object). To do this, we first calculated distributions of each behaviour (speed, head direction and occupancy) in every distance bin. 

The distributions for speed had bins from 0 cm/s to 100 cm/s in steps of 5 cm/s. The distributions for head direction had bins from 0 to 2p radians in steps of p/10. The distributions for occupancy were two-dimensional and had both x and y bins from 0 cm to 150 cm in steps of 30 cm. 

For each speed, HD or occupancy bin, we compared the number of observations from the No Object trial (nNO) and the number of observations from the Object trial (nO). If we found that: 

## nNO > nO 

we threw away nNO � nO random samples from the No Object trial, so that the number of samples matched between the trials. Conversely, if we found that, 

## nO > nNO 

we threw away nO � nNO random samples from the Object trial. This process was repeated for all bins, until distributions were completely matched (see example for speed in Figure S6G). After matching distributions within every distance bin, we ran the standard decoder (Bayesian decoding algorithm) on the subsampled neural data. The process was done separately for speed, head direction and occupancy. 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e11 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

## Subsampling for decoder 

To understand how widely distributed the object-centered population coding was across the recorded cells, we asked how many cells we needed to see the distance-based decrease in decoding accuracy (Figure 6). To answer this, we used a subsampling procedure before feeding data into the decoder. We used Neuropixels data from a rat implanted with two probes in left hippocampus (N = 620 cells). The subsampling was analogous to the shuffling described under Shuffling trial labels. We took the set of all cells f1; 2; 3; .; Ng, where each integer corresponds to a different cell identity, and randomly permuted the set using the MATLAB function randperm. We then took the first k integers of the permuted set, corresponding to k cells, and used them to create the subset. The number of subsampled cells, k, took the values 1, 5, 10, 30, 100, 200, 300, 400 and 500. For each k, we ran the decoder 20 times, (20 times being sufficient to get negligible error bars), so that the results were independent of cell identities and cell properties. In this way, we could determine how the number of cells influenced the decoding results (Figure 5A) and show the distribution of distance coding across the entire hippocampal population. 

## Measuring strength of distance-specific reorganization 

To estimate the strength of the distance-specific reorganization in populations of cells (and in individual neurons), we calculated two separate measures (Figures 6B, 6D, and 6F). Firstly, after having run the decoder and having obtained the curve showing decoding accuracy as a function of distance, we calculated 

distance tuning = decoding accuracy bin #1 � decoding accuracy bin #5 

A strong distance-specific reorganization should be associated with large distance tuning. Secondly, we fitted a line to the same curve via least squares[55] , 

**==> picture [64 x 13] intentionally omitted <==**

where A was the design matrix: 

**==> picture [56 x 51] intentionally omitted <==**

b was a vector containing the decoding accuracy of the cell in each distance bin i, 

**==> picture [46 x 52] intentionally omitted <==**

and xb was a 2-element vector containing the intercept (xb1) and slope (xb2) of the fitted line. A strong distance-specific organization should be associated with a more negative slope (xb2). The results obtained using the two measures (distance tuning and slope) were consistent. 

We also re-calculated these measures using distance bin #4 as the last distance bin (Table S1). 

## Significance of distance tuning in individual cells 

To test whether distance tuning values in individual cells were significant (Figure 6B), we compared the actual values to shuffled data. To create shuffled data, we circularly shifted spike trains (as described under shuffling of spike data) and re-calculated distance tuning (100 repetitions per cell). Cells with actual values above the 99[th] percentile of the shuffled distribution were considered to have significant positive tuning (Figure 6B, red bars) while cells with actual values below the 1[st] percentile were considered to have significant negative tuning (Figure 6B, yellow bars). 

## Population vector correlation 

To assess the similarity between populations of rate maps from the No Object and Object trials, we calculated the correlation between stacks of rate maps from each trial. For each experimental session, we stacked the rate maps from the No Object trial and Object trial separately, while preserving the cell ordering. This procedure generated two N3m3n matrices, where N is the number of cells recorded in the session, m is the number of y-bins and n is the number of x-bins of the rate maps (m = n = 50 bins). We then calculated the Pearson correlation rðx; yÞ between two N-dimensional vectors of firing rates, one from each trial, for every spatial bin. After computing the Pearson correlations, we obtained an m3n map showing Pearson correlations as a function of space (Figure 4G). After computing the correlation map, we allocated correlation values rðx; yÞ to distance bins and calculated the mean correlation in every distance bin (5 bins in total, bin size = 20 cm). Repeating this analysis for all experimental sessions (n = 16 from both tetrode and Neuropixels data), we were able to determine how correlations between the stacks changed as a function of distance from object (Figure 4H). 

e12 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

## Definition of words and counts 

To understand which specific features of population activity explained the decrease in decoding accuracy as a function of distance from object, we considered two descriptions of population activity that we refer to as words and counts. These concepts have previously been used to study neural coding at the population level.[23–25] First, we expressed population activity in an N3T matrix, where N is the number of cells and T the number of timepoints in one trial. Each entry of the matrix corresponds to the number of spikes generated by each cell in specific time bin. To obtain mostly ones and zeroes (in rare cases, 2 or 3) we used 10 ms bins. We defined a specific pattern of activity and silence across the population as a ‘‘word.’’ We had as many words as timepoints sampled at 10 ms. The length of each word was the number of cells in the population (tetrode data: 25–39 cells; Neuropixels data: subsampled to contain 30 cells). In contrast, we defined the total number of spikes generated by the population in a time bin as the ‘‘count.’’ Words are a detailed description of population activity that preserves the cell identity, while counts are a coarse description of population activity. To illustrate, in a population of 4 neurons, the word [1, 0, 0, 1] would mean that the 1st and 4th neuron fired one spike in that time bin, while the 2nd and 3rd neurons remained silent. The total count would be 2 = 1 + 1. The word [0, 0, 0, 1] would mean that the 4th neuron fired one spike, while all others remained silent. The total count would be 1. 

## Mutual information 

To quantify how much information words and counts provided about the presence of an object in the animal’s environment, we calculated the mutual information (MI)[56][,][57] between the population response and the trial type (No Object and Object). The MI tells us how much information one variable (e.g., the words) provide about another variable (e.g., the trial type) independent of assuming any specific relationship between the two variables (e.g., the relationship could be completely non-linear). For words, the calculation was given by 

**==> picture [196 x 24] intentionally omitted <==**

where PðwordÞ and PðtrialÞ are the marginal probabilities of the words and trial type and Pðtrial; wordÞ is the joint probability. Similarly, for counts the calculations was given by 

**==> picture [201 x 24] intentionally omitted <==**

where PðcountÞ and PðtrialÞ are the marginal probabilities of the counts and trial type and Pðcount; wordÞ is the joint probability. All probabilities were estimated from the frequency distributions. When calculating the MI of words, the number of bins was the same as the number of words in both trials (No Object and Object). For counts, the number of bins was determined by the maximum counts observed in both trials. For example, if the maximum number of spikes in a single time bin was 14, bins would range from 1 to 14 (in steps of 1). Being highly frequent and uninformative, the all-zero vector was excluded from our analyses. For the same reason, the zero count was also excluded. 

## Bias-subtraction 

Calculation of MI on datasets with small numbers of samples is well-known to lead to a bias where one overestimates the amount of information.[58] To ensure that our findings were not caused by sampling problems, we used a shuffling procedure to calculate the bias and subtract it from the mutual information. For this, we first shuffled trial labels as described for the decoder under Shuffling trial labels. After shuffling, a vector originally labelled ‘‘No Object’’ now had a 50% chance of being labelled ‘‘Object.’’ In other words, the shuffling destroys any relationship between the two variables (response and trial type) and shows the amount of ‘‘information’’ we should expect without such a relationship. The shuffling was performed 50 times, after which we calculated the mean MI across all 50 shuffles. This value (the "bias") was subtracted from the MI calculated on real data. 

## Entropy 

To estimate the entropy of words, we calculated 

**==> picture [95 x 24] intentionally omitted <==**

where H is the entropy function, p = fpig is the entire probability distribution of words, pi is the probability of word i occurring during the trial, and W is the total number of words. The calculation for the entropy of counts was done similarly, but with probabilities of words replaced by probabilities of counts. 

## Word distributions 

To directly visualize the change of words between No Object and Object, we calculated frequency distributions of words. For this, we first created a spike matrix based on activity from both trials (as in Figure 5A, bin size = 10 ms, n = 25-39 cells). We then calculated the occurrences of each word, plotting the result in a histogram (Figure 5D). To facilitate comparison between No Object and Object (for example, word #8 in No Object is the same as word #8 in Object), we applied the same sorting to the words in both trials. Specifically, we sorted words from No Object in order of descending frequency (Figure 5D, top) and applied the same sorting to the Object trial (Figure 5D, bottom). 

Neuron 111, 2091–2104.e1–e14, July 5, 2023 e13 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

To ensure that any differences in words between No Object and Object could not arise by chance, we randomly shuffled the trial labels (as described under ‘‘shuffling trial labels’’) and calculated word distributions on the shuffled data (Figure S7A). 

## Downsampling words 

Because the total number of words and counts differ by an order of magnitude (in a given trial, we usually observe a few hundred different words and approximately ten different counts), we wanted to assess how this difference influences the mutual information. For this, we downsampled the number of words to be equivalent to the number of counts (Figure S7E). In a given trial, we identified how many unique counts were present, c, and then kept the c words with the largest frequencies. The frequency distribution was then normalized, creating a downsampled probability distribution for words. Note that because we keep the most probable words, the total number of samples of words and counts are roughly the same even after downsampling (so that any difference in the number of samples should not have a large effect on the mutual information). 

## Kullback-Leibler divergence between word distributions 

To quantify how strongly word distributions (as in Figure 5D) differed between the No Object and Object trials, we calculated the Kullback-Leibler (KL) divergence,[56][,][59] which is given by, 

**==> picture [107 x 23] intentionally omitted <==**

where pi is the probability of word i occurring in the No Object trial, qi is the probability of word i occurring in the Object trial, W is the total number of words from the No Object and Object trials, p = fpig is the entire probability distribution of words from the No Object trial while q = fqig is the entire probability distribution from the Object trial. Probabilities of the words were estimated in each trial as the normalized frequency distribution (number of times each word occurred/total number of timepoints). For visualization purposes, we plotted histograms of only the most 100 frequent words in each trial (Figure 5D). However, the KL divergence was calculated using all words. 

## Statistical tests 

All statistical analyses were performed in MATLAB (version 2020a). P-values are indicated in figures and legends. Wilcoxon signedrank tests were used for paired data and Wilcoxon rank sum tests for unpaired data. Kruskal-Wallis tests were used for comparing differences between multiple groups. Binomial tests were used to compare fractions of observed cells (for example, object cells) to chance levels. Correlations were determined using Pearson’s product-moment correlation coefficients (r). The significance level was set to p = 0.05. All statistical tests were two-sided. 

e14 Neuron 111, 2091–2104.e1–e14, July 5, 2023 

Neuron, Volume 111 

## Supplemental information 

## Object-centered population coding 

## in CA1 of the hippocampus 

Anne Nagelhus, Sebastian O. Andersson, Soledad Gonzalo Cogno, Edvard I. Moser, and May-Britt Moser 

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 132] intentionally omitted <==**

**==> picture [612 x 9] intentionally omitted <==**

**Supplementary Figure 1. Anatomical location of recording sites** Micrographs of Cresyl violet stationed sagittal brain sections from 7 rats implanted with microdrives with a single bundle of 4 or 8 tetrodes, and 3 rats implanted with one or two four shank Neuropixels 2.0 silicone probes. Rat ID, hemisphere (L = left; R = right), and number of tetrodes or shanks is indicated on top of each micrograph. Sections from rats with tetrode implants are organised from most medial (top left) to most lateral (bottom right) implant. Sections from the Neuropixels rats are organised for each rat from the most medially placed shank(s) (left) to the most lateral shank(s) (right). The arrows indicate final recording locations (tetrodes) or top and bottom locations of active recording sites (Neuropixels). Purple arrows indicate CA1 and green arrows indicate CA3/hilus. One brain (rat 25371) was damaged during sectioning, and parts of the hippocampal formation are therefore missing from the micrograph. Scale bars = 1000 µm. D = dorsal; V = ventral; A = anterior; P = posterior. 

**Supplementary Figure 2** 

**a** 

**==> picture [40 x 526] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [6 x 43] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [6 x 42] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [97 x 34] intentionally omitted <==**

**==> picture [5 x 42] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [39 x 526] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [43 x 42] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 42] intentionally omitted <==**

**==> picture [42 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [5 x 42] intentionally omitted <==**

**==> picture [5 x 42] intentionally omitted <==**

**==> picture [5 x 42] intentionally omitted <==**

**==> picture [5 x 43] intentionally omitted <==**

**==> picture [106 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
b c<br>**----- End of picture text -----**<br>


**==> picture [114 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
d e<br>**----- End of picture text -----**<br>


**==> picture [314 x 125] intentionally omitted <==**

**==> picture [83 x 84] intentionally omitted <==**

**Supplementary Figure 2. Examples of object tuned cells and object tuning properties of individual cells a,** Rate maps from example object tuned cells recorded in CA1. Conventions as in Fig. 1e. Cells are ordered according to their object tuning score, starting with the highest. The score is indicated to the left of each cell. Peak firing rate is indicated at the bottom of each rate map. Scale bar, colour coded firing rate. Rate maps on the left are from tetrode data; rate maps on the right are from Neuropixels data. **b** , Cumulative fraction of object tuned cells as a function of the number of tests (out of 520) that passed significance (compared to shuffled data) in the template matching procedure. Few cells passed a single test (11.4%); the majority of cells passed multiple tests (88.6%). **c,** Percentage of object tuned cells in different animals. Animals are ordered according to the proximodistal implantation site. There was no significant linear correlation between the proximodistal site and the percentage of object related cells ( _r_ = 0.42, _p_ = 0.2216, Pearson correlation). The superscript for rat 27207 refers to two different Neuropixels probes. Note that the total number of cells varied widely between different animals (from left to right, _n_ = 39, 129, 43, 13, 242, 151, 26, 135, 378, 33). **d,** Distribution of object tuning scores after having removed object traces from the Object Moved trial, testing for any possible interference from object traces on the classification. The number object tuned cells was not significantly different after removing traces (using expected percentage 19.9% from Fig. 1c and observed count of 256/1189 object tuned cells after removing traces, _p_ = 0.0905, binomial test). **e,** Within trial stability as a function of object tuning score (n = 237 cells with significant object tuning). To calculate within trial stability, we created firing rate maps from the first and second halves of the trial (using the Object trial) and computed their Pearson correlation. 

**Supplementary Figure 3** 

**==> picture [285 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>d e<br>**----- End of picture text -----**<br>


**==> picture [131 x 128] intentionally omitted <==**

**==> picture [418 x 190] intentionally omitted <==**

## **f** 

**==> picture [182 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
p  = 5.13 x 10 [-8] p  = 0.154 NO - O<br>z  = 1.43 CON1 - CON2<br>p  = 6.64 x 10 [-7] p  = 0.159 OM - NO<br>CON3 - CON4<br>**----- End of picture text -----**<br>


**==> picture [182 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
p  = 2.87 x 10 [-8] p = 0.727 O - OM<br>CON2 - CON3<br>p  = 1.52 x 10 [-6] p  = 0.325 NO - NO<br>CON1 - CON4<br>**----- End of picture text -----**<br>


**Supplementary Figure 3. CA3 data to Figure 1 and 2. a,** Consistent with previous reports[10,16] , object related activity was present also in CA3. Distribution of object tuning scores ( _n_ = 313 CA3 cells). Blue bars, cells classified as object tuned cells; grey bars, cells not classified as object tuned. In CA3, 23% of the cells were object tuned (72/313 cells; 7 object cells and 58 object vector cells). **b,** Polar scatter plot showing orientation (polar axis, in degrees) and distance (radial axis, in cm, red) of firing fields of object tuned cells with respect to the object location (one dot per cell). **c,** Orientation coverage of firing fields of object tuned cells as a function of distance to object. The orientation coverage is expressed as the fraction of the azimuthal range around the object (0 360°) covered by the firing fields of each cell. The nearer the cell�s firing field is to the object, the larger the orientation coverage is. **d,** Colour coded firing rate maps for 4 example cells. The top row shows a cell that changed its spatial firing pattern when introducing the object. The second row shows a cell that had a diffuse spatial firing pattern. The third row shows a cell that changed its spatial firing pattern both when introducing and moving the object. The bottom row shows a place cell that was unaffected by the presence of the object. Object locations in the Object and Object Moved trials are shown as red squares. Rat ID and cell ID are indicated to the left of the firing rate maps, and peak firing rate in each trial is indicated at the top of each rate map. Bars, colour coded firing rate. **e,** We also recorded 59 unique principal cells in 2 rats during control sessions without the object. Colour coded firing rate maps for 2 example cells. The top row shows a place cell whose peak firing rate remains approximately the same throughout the session, and the bottom row shows a cell where the peak firing rate changes. Symbols as in panel d. **f,** Cumulative normalized frequency distributions of spatial correlation (left plots in each pair) and rate overlap (right plot in each pair). Each plot compares pairs of experimental trials from Object sessions (dark green lines) to the corresponding control trials (pink lines). The spatial correlation is defined as the Pearson correlation between the firing rate maps in two trials, and the rate overlap is calculated by dividing the mean firing rate in the less active trial by the mean firing rate in the more active trial. We calculated differences between the distributions for each panel (dark green lines and pink lines; Wilcoxon rank sum tests; _p_ values are indicated at the top left corner of each plot). As for CA1, we found that spatial correlation values between pairs of trials was always significantly different between Object sessions and control sessions, whereas rate overlap was not significantly different between the two types of sessions. NO = No Object; O = Object; OM = Object Moved; NO�= No Object�; CON1 4 = Control 1 4. 

**Supplementary Figure 4** 

**==> picture [398 x 232] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Changing b p  = 1.53 x 10 [-69]<br>p  = 2.59 x 10 [-32]<br>1<br>No Object Object  Object Moved No Object’<br>= Field<br>= ROI 0.5<br>= Shuffled ROI<br>0<br>OM O NO<br>- - -<br>NO’ NO’ NO’<br>c d<br>x 10 [4]<br>12 50<br>1<br>0.8<br>0.6<br>6 25<br>0.4<br>0.2<br>0<br>0 500 1000 0 0<br>Field index 0 0.2 0.4 0.6 0.8 1<br>Rate overlap<br>**----- End of picture text -----**<br>


## **Supplementary Figure 4. Object trace responses** 

**a.** Schematic of procedure to quantify object trace responses (responses in locations where objects had been presented on the preceding trial). First, we identified cells where the spatial firing pattern changed between the first and last trials (No Object and No Object�; _n_ = 919 cells, red line labelled �Changing�). In these cells, we identified firing fields in No Object�as a circular region of interest (ROI; �Field�, blue). We then transferred the ROI to the same location in the preceding No Object, Object and Object Moved trials. To quantify traces, we calculated the rate overlap between the actual ROI in No Object�and the ROI transferred to Object Moved (the other trials are used in panel b). To create shuffled data, we moved the ROI to random locations in the Object Moved trial (�Shuffled ROI�, orange) and calculated the rate overlap between the actual ROI in No Object�and the Shuffled ROI. This shuffling procedure was repeated 1000 times. If the cell had more than one field, we repeated the analysis for each field. **b** . Box plot of rate overlap between ROIs for the following pairs of trials: Object Moved and No Object�, Object and No Object�, and No Object and No Object�. Data are from _n_ = 1,252 fields in _n_ = 919 cells. The large rate overlap between Object Moved and No Object�compared to the other trials suggests carry over (hysteresis) of firing fields from the most recent trial[18] . We found that 18.3% of CA1 cells had trace responses, with larger values of ROI rate overlap between Object Moved and No Object�than the 99[th] percentile of shuffled data (Supplementary Fig. 4 c and d) ( _n_ = 218/1189 cells in total, significantly above chance level of 1%, _p_ < 5.73×10 141, binomial test). Control analyses showed that the trace activity did not interfere with the classification of object tuned cells (Supplementary Fig. 2d). **c.** ROI rate overlap between the Object Moved and No Object�trials for all fields as a function of the field index. The red dashed line indicates the 99[th] percentile of the shuffled distribution for each field. The fields above the red line passed the 99[th] percentile of the shuffled distribution and are considered trace fields ( _n_ = 312/1252 trace fields in _n_ = 218/919 cells). **d** . ROI rate overlap values from shuffled data (left y axis, gray) and real data (right y axis, blue). Distribution for real data is shifted to the right compared to shuffled data, showing that in many CA1 cells firing fields persist after the object is removed. 

**Supplementary Figure 5** 

**b** 

**Fixed distance bins** 

**==> picture [7 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>**----- End of picture text -----**<br>


**==> picture [89 x 103] intentionally omitted <==**

**==> picture [194 x 92] intentionally omitted <==**

**==> picture [217 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
c d<br>Decoding 1st half of No Object vs.<br>2nd half of No Object<br>e f<br>Shuffled trial labels<br>**----- End of picture text -----**<br>


**==> picture [132 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
Decoding in control experiments<br>Control 1 vs. Control 2<br>**----- End of picture text -----**<br>


**==> picture [194 x 88] intentionally omitted <==**

**==> picture [185 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
f<br>Testing/training data randomly selected<br>**----- End of picture text -----**<br>


**==> picture [90 x 89] intentionally omitted <==**

**==> picture [196 x 89] intentionally omitted <==**

**==> picture [90 x 89] intentionally omitted <==**

**==> picture [216 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
g h<br>i<br>l Cells with significant<br>positive distance tuning removed<br>**----- End of picture text -----**<br>


**==> picture [196 x 96] intentionally omitted <==**

**==> picture [214 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
j Position decoding error  k Population vector correlations<br>near vs. away from walls near vs. away from walls<br>**----- End of picture text -----**<br>


**==> picture [199 x 83] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
m<br>**----- End of picture text -----**<br>


**==> picture [109 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Object-tuned cells removed<br>**----- End of picture text -----**<br>


**==> picture [185 x 88] intentionally omitted <==**

**==> picture [186 x 88] intentionally omitted <==**

**Supplementary Figure 5. Controls for the results of the decoder a,** Decoding accuracy in all sessions (n = 16) when attempting to decode No Object from No Object�. Each circle corresponds to one session. Consistent with the demonstration of trace fields, the decoding accuracy is above chance. **b,** (Left panel) Decoding accuracy as a function of distance from object when using fixed distance bins. In the main analysis (Fig. 4), we used optimized distance bins to ensure the same number of samples in each bin, avoiding potential biases due to uneven exploration of the animal. The fixed distance bins were 0 20 cm, 20 40 cm, 40 60 cm, 60 80 cm and 80 100 cm. Decoding accuracy decreases as a function of distance from object ( _H_ = 39.69, _p_ = 5.02×10[8] , Kruskal Wallis test), showing that the result is independent of our choice of binning. (Right panel) Same data, but each colour shows a different experimental session. **c,** (Left panel) Decoding accuracy as a function of distance from object when attempting to decode 1st vs. 2nd half of No Object trial (instead of No Object vs. Object). We observed no decrease in accuracy as a function of distance ( _H_ = 1.46, _p_ = 0.834, Kruskal Wallis test), which is expected given that no object was present in the trial. (Right panel) Same data, but each colour shows a different experimental session. **d** , (Left panel) Decoding accuracy as a function of distance from object when attempting to perform the decoding in control experiments without the object (Control trial 1 vs. Control trial 2). We observed no decrease in accuracy as a function of distance ( _H_ = 6.32, _p_ = 0.1768, Kruskal Wallis test), consistent with no object being present in these experiments. (Right panel) Same data, but each colour shows a different experimental session. **e,** (Left panel) To ensure that the results were not an artefact of the decoder, we shuffled the trial labels of testing data. The mean decoding accuracy is 50% in all distance bins (mean ± SD in distance bins 1 5: 0.498 ± 0.010; 0.501 ± 0.008; 0.501 ± 0.006; 0.504 ± 0.008; 0.502 ± 0.010; none of the groups significantly different from 0.5: _t_ 2.1254, _p_ 

0.0518 for all comparisons, t tests), confirming that the decoder does not generate distance tuning unless such structure is present in the data. We performed 50 shuffling iterations for each experimental session. Data are means over the 50 shuffling iterations. (Right panel) Same data as in the previous panel, but each colour shows a different experimental session. **f,** (Left panel) In the main analysis (Fig. 4), we used the first half of the session as training data and the second half as testing data (and vice versa in a separate iteration). Here, we randomly selected half the timepoints to constitute training data. Hence, training data were distributed across the entire session. We observed the same decrease in decoding accuracy as a function of distance from the object ( _H_ = 39.71, _p_ = 4.98×10[8] , Kruskal Wallis test), confirming that our results did not depend on the choice of partitioning. (Right panel) Same data, but each colour shows a different experimental session. **g** , Firing field positions in the No Object trial (left) and Object trial (right). Data consist of 1884 fields (No Object trial) and 1989 fields (Object trial) from 1189 cells. Each dot corresponds to the centroid of the firing field of one cell. Coordinates of firing fields are expressed relative to the object, using (0,0) as the 

object centre. **h** , (Left) Histogram of distances between firing fields and object location in the No Object trial and Object trial. (Right) Proportion of firing fields as a function of object distance. Data were normalised by total number of firing fields per session because of large differences in number of cells between tetrode and Neuropixels datasets. Data are from n = 16 sessions. Error bars show SEM. **i** , Mean firing rates (left) and median firing rates (right) as a function of distance bins for all cells. Data are from n = 16 sessions. Error bars show SEM. **j** , Error of the position decoder near (�Wall�) and far away (�Box�) from walls, in the No Object trial (near walls defined as less than 15 cm from walls; far defined as more than 15 cm from walls). The error was calculated as the Euclidian distance between the actual position of the animal and the decoder�s predicted position. **k** , Population vector correlations near (�Wall�) and far away (�Box�) from walls (correlations calculated between stacks of rate maps from the 1st and 2nd halves of the No Object trial). **l** , (Left panel) Decoding accuracy as a function of distance from object after removing all cells with significant positive distance tuning (12.3%, Fig. 6b) from the data. We still observed a decrease in decoding accuracy as a function of distance ( _H_ = 28.88, _p_ = 8.27×10[6] , Kruskal Wallis test). (Right panel) Same data, but each colour shows a different experimental session. **m** , (Left panel) Decoding accuracy as a function of distance from object after having removed all object tuned cells (237/1189 cells, 19.9%) from the data. We still observed a decrease in decoding accuracy as a function of distance ( _H_ = 38.89, _p_ = 7.34×10[8] , Kruskal Wallis test). (Right panel) Same data, but each colour shows a different experimental session. 

**Supplementary Figure 6** 

**Decoding based on speed a (actual data)** 

**Decoding based on speed (simulated data)** 

**b** 

**==> picture [194 x 88] intentionally omitted <==**

**==> picture [167 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
Decoding based on head direction<br>c (actual data)<br>**----- End of picture text -----**<br>


**==> picture [194 x 88] intentionally omitted <==**

**==> picture [221 x 384] intentionally omitted <==**

**----- Start of picture text -----**<br>
e Decoding based on occupancy<br>(actual data)<br>g<br>i<br>HD distributions matched<br>k<br>Prior removed (uniform prior)<br>**----- End of picture text -----**<br>


**==> picture [194 x 89] intentionally omitted <==**

**==> picture [203 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
Speed different entire environment Speed increasingly different near object<br>Decoding based on head direction<br>d (simulated data)<br>HD different entire environment HD increasingly different near object<br>f Decoding based on occupancy<br>(simulated data)<br>**----- End of picture text -----**<br>


**==> picture [201 x 366] intentionally omitted <==**

**----- Start of picture text -----**<br>
Occupancy different entire environment Occupancy increasingly different near<br>object<br>h<br>Speed distributions matched<br>j Occupancy distributions matched<br>l<br>Change of occupancy threshold<br>for rate map bins<br>**----- End of picture text -----**<br>


**==> picture [90 x 88] intentionally omitted <==**

**Supplementary Figure 6. Controls for the animal�s behaviour** To test whether behavioural differences between the No Object and Object trials could explain our main result, we developed decoders that tried to infer the trial (No Object vs. Object) based on the animal�s behaviour ( **a f** ). The decoders were based on the same framework as the standard decoder, but used alternative models (likelihoods) that were more appropriate for each behaviour. We also subsampled data from the No Object and Object trials so that, after subsampling, distributions of behaviour were the same across trials in each distance bin ( **g j** ). **a,** (Left panel) Decoding accuracy as a function of distance from object for the speed decoder. There was no significant change in decoding accuracy as a function of distance ( _H_ = 6.85, _p_ = 0.1441, Kruskal Wallis test). (Right panel) Same data, but each colour shows a different experimental session. **b** , When we simulated different animal speeds between the two trials across the entire environment (left) or increasingly different speeds near the object (right), the decoder performed with nearly perfect accuracy (left) or had distance dependent accuracy (right). **c** , (Left panel) Decoding accuracy as a function of distance from object for the head direction (HD) decoder. There was no significant change in decoding accuracy as a function of distance ( _H_ = 2.13, _p_ = 0.711, Kruskal Wallis test). (Right panel) Same data, but each colour shows a different experimental session. **d** , When we simulated different HD between the two trials across the entire environment (left) or increasingly different HD near the object (right), the decoder performs with nearly perfect accuracy (left) or has distance dependent accuracy (right). **e,** (Left panel) Decoding accuracy as a function of distance from object for the occupancy decoder. There was no significant change in decoding accuracy as a function of distance ( _H_ = 3.53, _p_ = 0.4735, Kruskal Wallis test). (Right panel) Same data, but each colour shows a different experimental session. **f** , When we simulated different occupancies of the animal across the entire environment (left) or increasingly different occupancy near the object (right), the decoder performs with nearly perfect accuracy (left) or has distance dependent accuracy (right). **g** , To further control for the role of behaviour, we implemented a procedure where we matched distributions of behaviour between the No Object and Object trials within every distance bin, and then re ran the decoder on the remaining neural data. Top, example of speed distributions (distance bins 1 5) before matching. Bottom, example of speed distributions (distance bins 1 5) after matching. We obtained matched distributions by finding which speed bins (in distributions from distance bins 1 5) had more observations in one of the trials than the other. Then, we randomly removed samples from those speed bins until the number of observations was the same between the trials. **h** , After matching speed distributions in every distance bin between the No Object and Object trials, decoding accuracy calculated on neural data still decreased as a function of distance from object ( _H_ = 45.4, _p_ = 3.28×10 9 , Kruskal Wallis test). **i** , After matching HD distributions in every distance bin between the No Object and Object trials, decoding accuracy still decreased as a function of distance from object ( _H_ = 38.23, _p_ 

= 1.01×10 7, Kruskal Wallis test). **j** , After matching occupancy distributions in every distance bin between the No Object and Object trials, decoding accuracy still decreased as a function of object distance ( _H_ = 45.8, _p_ = 2.71×10 9, Kruskal Wallis test). **k** , After removing the prior in the standard decoder that contains information about the animal�s occupancy, decoding accuracy still declined as a function of distance from object ( _H_ = 42.92, _p_ = 1.07×10 8, Kruskal Wallis test). **l** , When including only spatial bins in which the animal had spent a minimum amount of time (either 100 ms, 500 ms, 1000 ms or 2000 ms) in both the No Object and Object trials, decoding accuracy still declined as a function of distance from object (for all curves, _H_ 34.08, _p_ 7.18×10 7, Kruskal Wallis test). For this control analysis, we had to increase the rate map bin size from 3 cm² to 10 cm², since otherwise almost no bins would be explored for 500 ms or more. Note that the physical blockade from the object would be only be relevant in distance bin 1, and all the main statistics hold even after excluding distance bin 1 (Supplementary Table 1). 

**Supplementary Figure 7** 

**==> picture [258 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Rat 26186 No Object trial (shuffled)<br>**----- End of picture text -----**<br>


**==> picture [427 x 102] intentionally omitted <==**

**==> picture [92 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
Object trial (shuffled)<br>**----- End of picture text -----**<br>


**==> picture [427 x 95] intentionally omitted <==**

**==> picture [430 x 298] intentionally omitted <==**

**----- Start of picture text -----**<br>
b Rat 26186 No Object trial<br>Object trial<br>c d e<br>Total number of words and<br>counts equivalent<br>**----- End of picture text -----**<br>


**==> picture [428 x 130] intentionally omitted <==**

**==> picture [423 x 420] intentionally omitted <==**

**Supplementary Figure 8** 

**a** 

## **b** 

**==> picture [206 x 142] intentionally omitted <==**

## **c** 

**==> picture [206 x 152] intentionally omitted <==**

## **e** 

**==> picture [206 x 142] intentionally omitted <==**

**==> picture [8 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
g<br>**----- End of picture text -----**<br>


**==> picture [206 x 152] intentionally omitted <==**

## **d** 

## **f** 

**==> picture [8 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
h<br>**----- End of picture text -----**<br>


**==> picture [168 x 141] intentionally omitted <==**

**==> picture [165 x 151] intentionally omitted <==**

**==> picture [171 x 153] intentionally omitted <==**

**==> picture [168 x 163] intentionally omitted <==**

**Supplementary Figure 8. Additional data emergence of distance specific reorganisation** 

**a** , Decoding accuracy as a function of distance from object, based on the number of cells used in the decoder. Conventions as in Figure 6c. Data are from 14 experimental sessions from tetrode data (2 animals). The number of data points for each dot is 280 (14 sessions × 20 draws of random subsets). Error bars for this and other panels show SEM. The number of cells for n = max was from 29 to 35 cells, depending on the session. **b** , Distance reorganisation as a function of number of cells used in the decoding. The left y axis (blue curve) shows the distance difference (decoding accuracy in bin #1 �decoding accuracy in bin #5) and the right y axis (orange curve) shows the slope of the least square line (fitted to decoding accuracy vs. distance curves in the previous panel). Conventions as in Figure 6d. The distance difference became increasingly positive ( _H_ = 74 349.13, _p_ = 2.70×10 , Kruskal Wallis test) and the slope increasing negative ( _H_ = 352.35, _p_ = 5.46×10 75, Kruskal Wallis test) **c** , Same plot as in panel a for a Neuropixels dataset with 135 cells (1 experimental session, 1 animal). The number of data points for each dot is 20 (20 draws of random subsets). **d** , Same plot as in panel b for a Neuropixels dataset (different rat than the one shown in Fig. 6c f). The distance difference became increasingly positive ( _H_ = 62.87, _p_ = 4.03×10 11, Kruskal Wallis test) and the slope increasing negative ( _H_ = 55.76, _p_ = 1.06×10 9, Kruskal Wallis test). **e** , Decoding accuracy as a function of distance from object, depending on the fraction of cells with lowest distance tuning retained. Conventions as in Fig. 6e. Data are from 14 experimental sessions with tetrodes. **f** , Distance reorganisation as a function of the percentage of cells with the lowest distance tuning retained. Note that the slope reaches zero when the fraction of least tuned cells kept is 0.6. **g** , Same plot as in panel e for a Neuropixels dataset (1 experimental session). **h** , Same plot as in panel f above for a Neuropixels dataset. Note that the slope approach zero when the fraction of least tuned cells kept is 0.5. 

**==> picture [426 x 597] intentionally omitted <==**

**----- Start of picture text -----**<br>
Main results when distance bin 1 (nearest object) is excluded<br>Analysis  Statistics  Relevant figure or<br>section<br>Effect of object distance on decoding  H  = 25.06,  p  = 1.50×10 , Kruskal-Wallis test Fig. 4b<br>accuracy<br>Fixed distance bins rather than  H  = 29.87,  p  = 1.47×10 , Kruskal-Wallis test Supplementary Fig.<br>optimized distance bins  6a<br>1st half of No Object vs. 2nd half of  H  = 2.69,  p  = 0.4426, Kruskal-Wallis test  Supplementary Fig.<br>No Object  6c<br>Random partitioning of  H  = 15.26,  p  = 0.0016, Kruskal-Wallis test  Supplementary Fig.<br>training/testing data  6g<br>Effect of object distance on  H  = 13.28,  p  = 0.0041, Kruskal-Wallis test  Fig. 4h<br>population vector correlations<br>Effect of object distance on MI from  H  = 7.76,  p  = 0.0513, Kruskal-Wallis test  Fig. 5b<br>words<br>Effect of object distance on MI from  H  = 4.84,  p  = 0.1835, Kruskal-Wallis test Fig. 5b<br>counts<br>Analyses of  using distance bin 4 rather than 5<br>Distance difference increasing with  H  = 44.72,  p  = 2.45×10 6, Kruskal-Wallis test Fig. 6d<br>number of cells (Neuropixels data, n =<br>620 cells)<br>Slope decreasing with number of cells  H  = 38.91,  p  = 2.64×10 5, Kruskal-Wallis test Fig. 6f<br>(Neuropixels data, n = 620 cells)<br>Distance difference increasing with  H  = 220.66,  p  = 1.35×10 46, Kruskal-Wallis test Supplementary Fig.<br>number of cells (tetrode data) 7b<br>Slope decreasing with number of cells  H  = 245.32,  p  = 6.64×10 52, Kruskal-Wallis test Supplementary Fig.<br>(tetrode data) 7b<br>Distance difference increasing with  H  = 62.87,  p  = 4.03×10 11, Kruskal-Wallis test Supplementary Fig.<br>number of cells (Neuropixels data, n =  7d<br>135)<br>Slope decreasing with number of cells  H  = 52.45,  p  = 4.77×10 9, Kruskal-Wallis test Supplementary Fig.<br>(Neuropixels data, n = 135) 7d<br>Correlations in Figure 7 for individual datasets<br>Tetrode dataset, correlations  r  = 0.18,  p  = 1.45×10 4 (object-tuning score)  Fig. 7<br>between distance tuning and single- r  = -0.086,  p  = 0.0062 (spatial information)<br>cell properties  r  = -0.09,  p  = 0.0026 (spatial correlation)<br>r  = -0.16, p  = 3.97×10 7, (rate overlap)<br>Neuropixels dataset (n = 620 cells), as  r  = 0.069,  p  = 0.0856 (object-tuning score)  Fig. 7<br>above  r  = -0.18,  p  = 4.75×10 6 (spatial information)<br>r  = -0.040,  p  = 0.3234 (spatial correlation)<br>r  = -0.26, p = 8.92×10 7 (rate overlap)<br>Neuropixels dataset (n = 135 cells), as  r  = 0.10,  p  = 0.2523 (object-tuning score)  Fig. 7<br>above  r  = 0.17,  p  = 0.0500 (spatial information)<br>r  = -0.30,  p  = 3.51×10 4 (spatial correlation)<br>r  = -0.34, p = 5.08×10 5 (rate overlap)<br>Error in training data (No Object) 0.0033 ± 0.0012 (mean absolute error ± SD)*  Speed decoder<br>Error in testing data (No Object 0.0039 ± 0.0012 (mean absolute error ± SD) (Method)<br>Error in training data (Object) 0.0034 ± 0.0011 (mean absolute error ± SD)<br>Error in testing data (Object  0.0042 ± 0.0013 (mean absolute error ± SD)<br>HD with mixture of two Gaussians<br>Error in training data (No Object) 0.047 ± 0.013 (mean absolute error ± SD)* HD decoder<br>Error in testing data (No Object  0.066 ± 0.017 (mean absolute error ± SD) (Method)<br>Error in training data (Object) 0.049 ± 0.015 (mean absolute error ± SD)<br>Error in testing data (Object  0.069 ± 0.019 (mean absolute error ± SD)<br>**----- End of picture text -----**<br>


## **Supplementary Table 1.** 

*Units for these statistics are given in terms of probability distributions. For example, an error of 0.047 corresponds to a 4.7% error between the HD HD. 

