https://doi.org/10.1038/s41592-022-01742-6 

## **nature methods** 

## **Brief Communication** 

## **A modular architecture for organizing, processing and sharing neurophysiology data** 

Received: 27 January 2020 **The International Brain Laboratory*, Niccolò Bonacchi[1] , Gaelle A. Chapuis[2,3] , Anne K. Churchland[4] , Eric E. J. DeWitt[1] , Mayo Faulkner[2] , Kenneth D. Harris[2] ,** Accepted: 21 November 2022 **Julia M. Huntenburg[5] , Max Hunter[2] , Inês C. Laranjeira[1] , Cyrille Rossant[2] ,** Published online: 2 March 2023 **Maho Sasaki[6] , Michael M. Schartner[1] , Shan Shen[6] , Nicholas A. Steinmetz[7] , Edgar Y. Walker[6] , Steven J. West[8] , Olivier Winter[1] & Miles J. Wells[2]** Check for updates 

We describe an architecture for organizing, integrating and sharing neurophysiology data within a single laboratory or across a group of collaborators. It comprises a database linking data files to metadata and electronic laboratory notes; a module collecting data from multiple laboratories into one location; a protocol for searching and sharing data and a module for automatic analyses that populates a website. These modules can be used together or individually, by single laboratories or worldwide collaborations. 

Improving technology allows neurophysiologists to record ever larger datasets. The need for technologies to organize and share these data is growing as scientists begin to assemble into large, international teams. The International Brain Laboratory (IBL) is a collaboration studying the computations supporting decision-making in the mouse[1] . We have developed modular data-management tools that enable individual laboratories and collaborations to manage experimental subject colonies and track subject- and experiment-level metadata; integrate data from multiple laboratories in a central store for sharing inside or outside the collaboration; access shared data through a programmatic interface; and process incoming data through pipelines that automatically populate a website. 

Current neurophysiological datasets comprise multiple recordings from multiple subjects, recorded using diverse devices. These data must be preprocessed, time-aligned and integrated with data such as locations of recording electrodes before they can be used to draw scientific conclusions[2][–][8] . Distributed collaborations pose distinct challenges: while public data release must wait for careful quality control, scientists within the collaboration require immediate access to specific data. This store must be searchable and allow downloading 

and also revision of individual items, because preprocessing and quality control methods are still evolving[9][–][11] . 

We addressed these problems with an architecture consisting of four modules (Fig. 1). The first module is a web interface for colony management and electronic laboratory notebook that links files arising from each experiment to relevant metadata. The second module integrates data from multiple laboratories into a central database and bulk data store, providing immediate access while allowing updates of individual items. The third automatically runs analyses on newly arrived data, providing results via a web interface. The fourth allows standardization, access and sharing of the data. Full documentation can be found at https://docs.internationalbrainlab.org/ and through links at https://www.internationalbrainlab.com/tools. 

To manage data within each laboratory, we developed Alyx, a relational database that links colony management, metadata and laboratory notes to experimental data files. A web graphical user interface allows users to enter metadata as it arrives (such as birth, weaning, genotyping, surgeries or experiments), and a REST application programming interface (API) allows experiment control software to automatically enter metadata. Bulk data files are stored on a 

> 1Champalimaud Center for the Unknown, Lisboa, Portugal. 2Institute of Neurology, University College London, London, UK. 3Department of Basic Neuroscience, University of Geneva, Geneva, Switzerland.[4] Department of Neurobiology, University of California, Los Angeles, Los Angeles, CA, USA. 5Max Planck Institute for Biological Cybernetics, Tübingen, Germany. 6DataJoint, Houston, TX, USA. 7Department of Biological Structure, University of Washington, Seattle, WA, USA.[8] Sainsbury-Wellcome Centre, University College London, London, UK. *A list of authors and their affiliations appears at the end of the paper. e-mail: kenneth.harris@ucl.ac.uk 

Nature Methods | Volume 20 | March 2023 | 403–407 

**403** 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

**==> picture [381 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
Central data server<br>Within-laboratory data management<br>Multi-laboratory integration<br>Alyx<br>Pipelined analysis<br>Contributor Data access<br>Globus<br>Experiment<br>control<br>computer<br>ONE<br>protocol<br>Laboratory data<br>server<br>Web metadata<br>entry<br>Automated metadata<br>entry<br>Bulk data transfer<br>Distributed job management<br>Preprocessing<br>**----- End of picture text -----**<br>


**Fig. 1 | IBL data architecture.** The Alyx database links colony management and electronic laboratory notebook metadata to experimental data files on a laboratory data server. Data from several laboratories are integrated on a central server, and a distributed job management system coordinates preprocessing 

on laboratory servers. Data are accessed via the ONE protocol, with adapters for Neurodata Without Borders[12][,][14] and DataJoint[13] , which also performs pipelined analyses for automatic display on a website. Globus, DataJoint and Neurodata Without Borders logos used with permission. 

laboratory server and linked to experiment and subject metadata in the Alyx database. This tool can be used by single laboratories as well as collaborations: it was developed in one member laboratory before IBL’s founding, and is now used by several laboratories worldwide for non-IBL work. A link to an Alyx user guide can be found via our main documentation page (https://docs.internationalbrainlab.org). 

Integrating data between laboratories raises challenges of size and complexity. Large-scale electrophysiology produces hundreds of gigabytes per experiment, for which we have designed a threefold lossless compression algorithm (https://github.com/int-brain-lab/ mtscomp) (Supplementary Note 1). A single IBL experiment generates over 150 raw and processed data files. We have devised conventions for organizing and naming these files, termed the Open Neurophysiology Environment (ONE) (Supplementary Note 2; https://one.internationalbrainlab.org), which formalizes how to encode cross-references between files, time synchronization and versioning, and allows local and remote access via an API. ONE provides a way to standardize and share data from individual laboratories, by specifying standard filenames for common data types (Supplementary Note 3) and defining conventions for naming laboratory-specific data files (https://github. com/int-brain-lab/ONE/blob/main/docs/Open_Neurophysiology_Environment_Filename_Convention.pdf). Files from several laboratories are integrated by uploading nightly from laboratory servers to a central server using Globus Online[12] , coordinated by a central Alyx database that also stores metadata from all laboratories. 

Neurophysiology data require preprocessing, such as spike sorting and video analysis. We developed a task management system that uses computers in member laboratories as a processing pool. Computers query the Alyx database for a list of outstanding preprocessing tasks, determined by a dependency graph. Because Alyx is accessed through http, this works despite different universities’ diverse firewall policies, and allows monitoring, logging and restarting all preprocessing tasks. Higher-level analyses are automatically run on newly preprocessed data using DataJoint[13] , which runs automated analyses and places the results on a website, including summaries of behavioral performance, allowing scientists to monitor training progress, and basic analyses of spike trains. While manual curation of the full dataset will be required before public release, an illustrative curated 

subset of these data is available on a public website (https://data. internationalbrainlab.org). 

To access data, an API allows users to search experiments and load data from the ONE files directly into Python (Supplementary Note 3). This API allows both collaborations and individual laboratories to share data using the same standard. A large collaboration can host files on a server such as Amazon Web Services, and run an Alyx server that allows users to rapidly search and selectively download the data. Individual - laboratories can release data compatible with the same API by ‘upload ing and forgetting’ a zip of ONE files to a site such as FigShare, for users to download (instructions at https://github.com/int-brain-lab/ONE/ blob/main/docs/Open_Neurophysiology_Environment_Filename_ Convention.pdf). Users can also access data via Neurodata Without Borders[13][,][14] using software that translates from the ONE standard (https://github.com/catalystneuro/IBL-to-nwb; Supplementary Table 1), or through DataJoint[15] . A comparison of these and other sharing systems is in Supplementary Note 4. The analyses in a recently published paper[1] were made using this system, and an additional example is provided below for evaluating training time. 

The IBL architecture was designed for our large-scale collaboration, but its modular design allows components to be used by individual laboratories and smaller-scale collaborations. The Alyx system provides easy-to-use colony management and electronic laboratory notebook features for laboratories or collaborations, linking experimental files to this metadata. The ONE conventions allow data to be organized within a laboratory and shared externally, using standards that scale to large collaborations. Larger collaborations can also benefit from other features such as the automated analyses for web display. We hope that these tools, and additional software we have provided (Supplementary Table 1), will help pave the way forward to an era in which data from neurophysiology laboratories are integrated and shared on a routine basis. 

To demonstrate how this system can manage data and metadata, integrate them across laboratories and analyze the results, we evaluated the importance of multiple variables for predicting the time required for mice to complete behavioral training. 

Mice were on a visual discrimination task using the standard IBL training pipeline[1] . Training was considered complete when 

Nature Methods | Volume 20 | March 2023 | 403–407 

**404** 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

**==> picture [437 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>Q1 Q2 Q3 1.0 1.0<br>35 Original<br>30 1 0.55 0.34 0.069 0.034 0.8 0.8 Shuffled<br>25<br>2 0.21 0.34 0.24 0.21 0.6 0.6<br>20<br>15 3 0.2 0.17 0.37 0.27 0.4 0.4<br>10<br>0.2 0.2<br>5 4 0.036 0.14 0.21 0.61<br>0 0 0<br>0 10 20 30 40 50 60 1 2 3 4 Full Task performance<br>Time until ‘trained’ (sessions) Predicted quartile change<br>Classifier<br>d<br>0.10 Task performance (first five sessions)<br>Subject features<br>0.08<br>Rig ambient<br>0.06 Institute-specific features<br>0.04<br>0.02<br>0<br>Permuted feature<br>Task performance changeWheel displacement biasAgeAir pressureVariance in daily performance changeWeekend water regimeWeight loss Trial count changeTotal trial countTemperatureStarting weightStarting trial countStarting task performanceStarting RTRelative humiditySex RT changeFood protein contentLight cycleWheel moves per time<br>True quartile<br>Number of mice<br>Accuracy score (F1)<br>Decrease in model score (F1)<br>**----- End of picture text -----**<br>


**Fig. 2 | Predicting time taken to complete training from diverse data and metadata. a** , Histogram of the number of training sessions taken to reach the IBL ‘trained’ criterion ( _n_ = 116 mice). Vertical dashed lines represent the split of the data in quartiles. **b** , Cross-validated confusion matrix of a random forest classifier, trained to predict training-time quantile from multiple behavioral features. Rows represent the true quartile and columns represent the predicted quartile; results were normalized over the number of mice of the corresponding true quartile (row). **c** , Prediction accuracy for a classifier that uses all features 

(full classifier), and a classifier that uses only task performance change across the first five training sessions (task performance change classifier). Horizontal lines show classifier performance; boxplots show distribution of performance scores over random shuffles of the training-time labels ( _n_ = 100 shuffles). **d** , Importance of each feature in predicting training time. Boxplots show the distribution of importance scores obtained across multiple permutations ( _n_ = 10 permutations). In all boxplots, the box shows median and interquartile range, whiskers show range and points show individual observations. RT denotes median reaction time. 

performance met criteria for the fraction of correct responses, number of completed trials and fitted psychometric parameters, for three consecutive sessions. Behavior on reaching this criterion was similar across mice, but the training time required for mice to meet these criteria was variable, ranging from 5 to 57 training sessions (Fig. 2a). We used the data architecture described above to investigate which factors might predict this variability. Because comprehensive data and metadata from all laboratories were integrated in a centralized and standardized manner, we could quickly perform these analyses. 

We investigated whether training time could be predicted from several classes of variables. The first class was subject features: the sex of the animal, the age, weight and weight loss (relative to prewater-restriction weight) on training start. The second was rig ambient measures: temperature, relative humidity and air pressure, averaged across all training sessions. Third, some institute-specific experimental conditions such as the type of light cycle mice were housed in, the protein content of the homecage food and the weekend water regime in place (water restriction versus 2% free homecage citric acid water[16] ). Fourth, metrics assessed from early training sessions including: task performance; median reaction time; total number of trials on the first training session; the changes in those values over the 

first five training sessions; the total sum of trials performed over the first five training sessions; the variance in the sign of the daily performance change across the first five training sessions; the number of wheel movements per second and the average wheel displacement bias (averaged across the first five training sessions). 

A random forest classifier accurately predicted time to reach the performance criterion for each mouse from this feature set (Fig. 2a). Time to criterion was grouped into quartiles and classification accuracy was evaluated by tenfold cross-validation, producing a confusion matrix comparing the predicted and actual quartile for each mouse (Fig. 2b), summarized by an F1 score (Fig. 2c). When trained with all available features, the classifier predicted the true quartile more often than any other (Fig. 2b), with accuracy around two times higher than when trained after randomly shuffling quartile labels (Fig. 2c). 

To investigate the importance of each feature, we performed a permutation test on each of the features. The importance of each feature was assessed by the decrease in the classifier’s accuracy after randomly shuffling that feature’s values across all mice. This revealed that one predictor variable was more important than all others: the task performance change across the first five training sessions (Fig. 2d): that is, the percentage correct achieved on session five minus the 

Nature Methods | Volume 20 | March 2023 | 403–407 

**405** 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

percentage correctly achieved on session 1. Site-specific features that are hard to standardize across locations, such as food protein content and humidity, were not important to the classifier’s accuracy. The only predictive feature not related to task performance in early days was age. 

Given the importance of the 5-day performance change feature compared to the remaining ones, we further evaluated the accuracy of a classifier trained only with this one feature (Fig. 2c). Prediction using only this feature was nearly as accurate as the full classifier, although including other predictor variables resulted in a 14% increase in accuracy. 

This large-scale analysis was made possible by the ease and speed of accessing large amounts of behavioral data saved in a standard manner. The obtained results showed that tracking changes in performance during the first few training days was enough to predict training time above chance level, with even better accuracy achieved when also considering other behavioral metrics. The ability to predict final training time after only five training sessions could allow automated decisions about when to drop a subject from the training pipeline. 

## **Online content** 

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41592-022-01742-6. 

## **References** 

1. The International Brain Laboratory. et al. Standardized and reproducible measurement of decision-making in mice. _eLife_ **10** , e63711 (2021). 

2. Pachitariu, M. et al. Suite2p: beyond 10,000 neurons with standard two-photon microscopy. Preprint at _bioRxiv_ https://doi. org/10.1101/061507 (2016). 

3. Mathis, A. et al. DeepLabCut: markerless pose estimation of user-defined body parts with deep learning. _Nat. Neurosci._ **21** , 1281–1289 (2018). 

4. Giovannucci, A. et al. CaImAn an open source tool for scalable calcium imaging data analysis. _eLife_ **8** , e38173 (2019). 

5. Vogelstein, J. T. et al. Fast nonnegative deconvolution for spike train inference from population calcium imaging. _J. Neurophysiol._ **104** , 3691–704 (2010). 

6. Pachitariu, M., Steinmetz, N. A., Kadir, S. N., Carandini, M. & Harris, K. D. in _Advances in Neural Information Processing Systems_ 29 (eds. Lee, D. D. et al.) 4448–4456 (Curran Associates, Inc., 2016). 

7. Wiltschko, A. B. et al. Revealing the structure of pharmacobehavioral space through motion sequencing. _Nat. Neurosci._ **23** , 1433–1443 (2020). 

8. Vogelstein, J. T. et al. Discovery of brainwide neural-behavioral maps via multiscale unsupervised structure learning. _Science_ **344** , 386–392 (2014). 

9. Siegle, J. H. et al. Survey of spiking in the mouse visual system reveals functional hierarchy. _Nature_ **592** , 86–92 (2021). 

10. Hill, D. N., Mehta, S. B. & Kleinfeld, D. Quality metrics to accompany spike sorting of extracellular signals. _J. Neurosci._ **31** , 8699–705 (2011). 

11. Harris, K. D., Quiroga, R. Q., Freeman, J. & Smith, S. L. Improving data quality in neuronal population recordings. _Nat. Neurosci._ **19** , 1165–1174 (2016). 

12. Foster, I. Globus Online: accelerating and democratizing science through cloud-based services. _IEEE Internet Comput._ **15** , 70–73 (2011). 

13. Rübel, O. et al. The Neurodata Without Borders ecosystem for neurophysiological data science. _eLife_ **11** , e78362 (2022). 

14. Teeters, J. L. et al. Neurodata Without Borders: creating a common data format for neurophysiology. _Neuron_ **88** , 629–634 (2015). 

15. Yatsenko, D. et al. DataJoint: managing big scientific data using MATLAB or Python. Preprint at _bioRxiv_ https://doi. org/10.1101/031658 (2015). 

16. Urai, A. E. et al. Citric acid water as an alternative to water restriction for high-yield mouse behavior. _eNeuro_ **8** , ENEURO.0230-20.2020 (2021). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

- © The Author(s), under exclusive licence to Springer Nature America, Inc. 2023 

## **The International Brain Laboratory** 

**Luigi Acerbi[3] , Valeria Aguillon-Rodriguez[9] , Mandana Ahmadi[10] , Jaweria Amjad[10] , Dora Angelaki[11] , Jaime Arlandis[1] , Zoe C. Ashwood[12] , Kush Banga[2] , Hailey Barrell[7] , Hannah M. Bayer[13] , Julius Benson[11] , Brandon Benson[14] , Jai Bhagat[15] , Daniel Birman[7] , Niccolò Bonacchi[1] , Kcenia Bougrova[1] , Julien Boussard[13] , Sebastian A. Bruijns[5] , Matteo Carandini[15] , Joana Catarino[1] , Fanny Cazettes[1] , Gaelle A. Chapuis[2,3] , Anne K. Churchland[4] , Yang Dan[16] , Felicia Davatolagh[4] , Peter Dayan[5] , Sophie Denève[17] , Eric E. J. DeWitt[1] , Ling Liang Dong[18] , Tatiana Engel[9] , Michele Fabbri[13] , Mayo Faulkner[2] , Ila Fiete[18] , Charles Findling[3] , Laura Freitas-Silva[1] , Surya Ganguli[14] , Berk Gercek[3] , Naureen Ghani[8] , Ivan Gordeliy[17] , Laura M. Haetzel[12] , Kenneth D. Harris[2] , Michael Hausser[19] , Naoki Hiratani[10] , Sonja Hofer[8] , Fei Hu[16] , Felix Huber[3] , Julia M. Huntenburg[5] , Cole Hurwitz[13] , Anup Khanal[4] , Christopher S. Krasniak[9,20] , Sanjukta Krishnagopal[10] , Michael Krumin[2] , Christopher Langdon[9] , Inês C. Laranjeira[1] , Peter Latham[10] , Petrina Lau[19] , Hyun Lee[13] , Ari Liu[18] , Zachary F. Mainen[1] , Hernando Martinez Vergara[8] , Conor Mcgrory[9] , Brenna McMannon[12] , Guido T. Meijer[1] , Maxwell Melin[4] , Leenoy Meshulam[7] , Nathaniel J. Miska[8] , Catalin Mitelut[13] , Zeinab Mohammadi[12] , Thomas Mrsic-Flogel[8] , Masayoshi Murakami[1,22] , Jean-Paul Noel[11] , Kai Nylund[7] , Alex Pan Vazquez[12] , Liam Paninski[13] , Alberto Pezzotta[10] , Samuel Picard[2] , Jonathan W. Pillow[12] , Alexandre Pouget[3] , Cyrille Rossant[2] , Noam Roth[7] , Nicholas A. Roy[12] , Kamron Saniee[13] , Rylan Schaeffer[18,23] , Michael M. Schartner[1] , Yanliang Shi[9] , Karolina Z. Socha[15] , Cristian Soitu[9] , Nicholas A. Steinmetz[7] , Karel Svoboda[21] , Marsa Taheri[4] , Charline Tessereau[5] , Anne E. Urai[9,24] , Erdem. Varol[13] , Miles J. Wells[2] , Steven J. West[8] , Matthew R. Whiteway[13] , Charles Windolf[13] , Olivier Winter[1] , Ilana Witten[12] , Lauren E. Wool[2] & Anthony M. Zador[9]** 

Nature Methods | Volume 20 | March 2023 | 403–407 

**406** 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

9Cold Spring Harbor Laboratory, Cold Spring Harbor, NY, USA. 10Gatsby Computational Neuroscience Unity, University College London, London, UK. 11Center for Neural Science, New York University, New York, NY, USA. 12Princeton Neuroscience Institute, Princeton University, Princeton, NJ, USA. 13Zuckerman Institute, Columbia University, New York, NY, USA. 14Department of Applied Physics, Stanford University, Stanford, CA, USA. 15Institute of Opthalmology, University College London, London, UK.[16] Department of Molecular and Cell Biology, University of California, Berkeley, Berkeley, CA, USA. 17Département D’études Cognitives, École Normale Supérieure, Paris, France. 18Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge, MA, USA.[19] Wolfson Institute of Biomedical Research, University College London, London, UK.[20] Watson School of Biological Science, Cold Spring Harbor, NY, USA.[21] The Allen Institute for Neural Dynamics, Seattle, WA, USA.[22] Present address: Department of Physiology, University of Yamanashi, Kofu, Japan.[23] Present address: Department of Computer Science, Stanford University, Stanford, CA, USA.[24] Present address: Cognitive Psychology Unit, Institute of Psychology and Leiden Institute for Brain and Cognition, Leiden University, Leiden, the Netherlands. 

Nature Methods | Volume 20 | March 2023 | 403–407 

**407** 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

## **Methods** 

The experimental methods used to collect the data analyzed in this paper are described in ref.[1] . 

For the analysis described in this paper, we accessed the behavioral data using the public DataJoint protocol. Mice selected for the analysis consisted of all mice trained according to the standard IBL training pipeline, up until 23 March 2020. Mice were excluded from the analyses if they were dropped from the pipeline before reaching the end of training. Training was considered complete when performance met criteria for the fraction of correct responses, number of completed trials and fitted psychometric parameters, for three consecutive sessions[1] . 

A random forest classifier was used to assess whether training time could be predicted from several classes of variables: subject features, rig ambient measures, institute-specific experimental conditions and performance metrics from early training sessions. For that, data were processed and organized as a design matrix with shape number of mice × number of variables. For each mouse, we included the following variables: (1) sex; (2) age at the start of training; (3) weight at the start of training; (4) weight loss at the start of training, calculated as the weight fraction relative to the prewater-restriction weight; (5) whether the mouse was housed on an inverted or noninverted light cycle scheme; (6) the percentage of protein content of the homecage food; (7) weekend water regime in place: whether mice were on a traditional water restriction regime or on had free access to 2% free homecage citric acid water[16] ; (8) the training rig temperature, averaged across the first five training sessions; (9) the training rig relative humidity, averaged across the first five training sessions; (10) the training rig air pressure, averaged across the first five training sessions; (11) the fraction of correct responses on the first training session; (12) median reaction time on the first training session; (13) total number of trials on the first training session; (14) difference in fraction of correct responses between first and fifth training sessions; (15) difference in the median reaction time between the first and fifth training sessions; (16) difference in the total number of trials between the first and fifth training sessions; (17) total number of trials performed over the first five training sessions; (18) the variance in the sign of the daily performance change across the first five training sessions (daily performance change was computed as the difference in the fraction of correct responses across consecutive sessions); (19) the amount of wheel movement per second averaged across the first five training sessions and (20) the wheel displacement bias averaged across the first five training sessions (wheel displacement bias was calculated as the amount of wheel displacement divided by the total amount of wheel movement). Missing data that prevented the calculation of any of the above metrics led to the exclusion of the corresponding mouse from the analyses. The predicted variable was the training-time quartile of the mouse. Training time was calculated as the number of training sessions until training completion. The quartiles of the distribution were calculated after exclusion of mice with missing data. 

To assess whether training time could be predicted from the listed variables, a random forest classifier was trained on the data, using tenfold cross-validation. For that, scikit-learn functions RanfomForestClassifier and KFold were used. Prediction accuracy of the classifier was computed using the F1-score function. The F1 score reaches 1 for the highest accuracy value and 0 for the worst. It is calculated according to the following formula: 

- _F_ 1 = 2 × true positives2 + × false positives true positives + false negatives 

Classifier performance was compared with that of a classifier trained on a control dataset in which quartile labels were randomly shuffled ( _n_ = 100 shuffles). 

To investigate the importance of each feature to the classifier’s performance, we performed a permutation test on each of the features. The importance of each feature was assessed by the decrease in the 

classifier’s accuracy (F1 score) after randomly shuffling that feature’s values across mice ( _n_ = 10 repetitions). 

Finally, we further evaluated the accuracy of a classifier trained only on the most important feature, as concluded from the permutation test: the difference in fraction of correct responses between first and fifth training sessions. 

## **Reporting summary** 

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article. 

## **Data availability** 

All IBL data are available online using the access protocols described in this manuscript. For further information see https://www.internationalbrainlab.com/data. The specific data used to create Fig. 2 can be accessed by the code that created this figure, available at https:// github.com/int-brain-lab/paper-data-architecture. 

## **Code availability** 

All code described in this paper is freely available and is listed in Supplementary Table 1 along with links to their respective repositories. The behavior data were collected using Bonsai and pyBpod, available at https://github.com/int-brain-lab/iblrig. Metadata were stored in a custom database available at https://github.com/cortex-lab/alyx. The data were processed using the custom data pipelines ibllib (https:// github.com/int-brain-lab/ibllib) and DataJoint (https://datajoint.io/). The data were accessed using ONE (https://one.internationalbrainlab. org) and DataJoint (https://github.com/int-brain-lab/IBL-pipeline). 

## **Acknowledgements** 

This work was supported by the Wellcome Trust (grant no. 209558 to IBL, 216324 to IBL) and Simons Foundation (to IBL). 

## **Author contributions** 

N.B. supported the conceptualization and worked on data curation of data, metadata and the pipeline; funding acquisition, project administration (meeting coordination and attendance), resources (computing and data storage), software, validation (pipeline, core, quality control, database and analysis libraries), writing the original draft and review and editing. G.A.C. was responsible for data curation and helped with writing user guides detailing how to enter metadata in Alyx, as well as software, validation (acted as naive user tester for ONE and DataJoint) and project administration (gathered and reported users’ requirements). A.K.C. contributed to project administration, funding acquisition, writing and revising. E.E.J.D.W. was responsible for the investigation and contributed to analyses for example use of data as well as writing and creating the figures and draft text. M.F. worked on the software and contributed to implementation of backend data infrastructure and analysis libraries, the data curation and contributed to curating datasets and assuring quality assurance. K.D.H. contributed to design of overall data architecture, and to Alyx and ONE systems, as well as to project administration, funding acquisition, writing and revising. J.M.H. worked on the software and contributed to implementation of backend data infrastructure, analysis libraries and continuous integration, as well as data curation and contributed to dataset curation and quality assurance. M.M.S. worked on the conceptualization and contributed to the development of dataset types related to video and their quality control metrics. M.H. contributed to the design and development of Alyx. I.C.L. worked on the investigation and performed analyses for the example use case of the data architecture as well as helping to write the original draft. C.R. contributed to design and implementation of overall data architecture, and to Alyx and ONE systems. M.S. contributed to the design and implementation of the IBL Data Portal website. S.S. contributed to the design and implementation of the DataJoint 

Nature Methods 

**Brief Communication** 

https://doi.org/10.1038/s41592-022-01742-6 

pipeline and the IBL JupyterHub. N.A.S. contributed to the design, testing, and development of Alyx, of dataset types, and of software tools for working with them. E.Y.W. contributed to the design and implementation of the DataJoint pipeline and the IBL Data Portal. S.J.W. contributed to the design of data structures for histological alignment. O.W. worked on the software and implemented the backend data infrastructure, the validation/methodology, designed the full loop integration tests to allow maintenance of the codebase, data curation and fixed and updated erroneous datasets. M.J.W. worked on the software and contributed to the design, testing and implementation of Alyx, its dataset types and of software tools that work with them, the validation, contributed to the design and implementation of continuous integration and quality assurance systems and contributed to writing, reviewing and editing the text and Supplementary Notes. 

## **Competing interests** 

The authors declare the following competing interests: E.Y.W. holds equity ownership in Vathes LLC, which provides development and consulting for the framework (DataJoint) described in this work. 

E.Y.W., M.S. and S.S were employees of Vathes LLC at the time the work in this paper was done. The remaining authors declare no competing interests. 

## **Additional information** 

**Supplementary information** The online version contains supplementary material available at https://doi.org/10.1038/s41592-022-01742-6. 

**Correspondence and requests for materials** should be addressed to Kenneth D. Harris. 

**Peer review information** _Nature Methods_ thanks Joshua Vogelstein and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Primary Handling Editor: Nina Vogt, in collaboration with the _Nature Methods_ team. 

## **Reprints and permissions information** is available at 

www.nature.com/reprints. 

Nature Methods 

Corresponding author(s): Kenneth Harris Last updated by author(s): 11/18/2022 

**==> picture [220 x 40] intentionally omitted <==**

## Reporting Summary 

Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Research policies, see our Editorial Policies and the Editorial Policy Checklist. 

## Statistics 

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section. 

## n/a Confirmed 

The exact sample size ( _n_ ) for each experimental group/condition, given as a discrete number and unit of measurement 

A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly 

The statistical test(s) used AND whether they are one- or two-sided 

_Only common tests should be described solely by name; describe more complex techniques in the Methods section._ 

A description of all covariates tested 

A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons 

A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals) 

For null hypothesis testing, the test statistic (e.g. _F_ , _t_ , _r_ ) with confidence intervals, effect sizes, degrees of freedom and _P_ value noted _Give P values as exact values whenever suitable._ 

For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings 

For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes 

Estimates of effect sizes (e.g. Cohen's _d_ , Pearson's _r_ ), indicating how they were calculated 

_Our web collection on statistics for biologists contains articles on many of the points above._ 

## Software and code 

## Policy information about availability of computer code 

Data collection The behaviour data were collected using Bonsai v2.6 and pyBpod v1.8, available at https://github.com/int-brain-lab/iblrig. Metadata were stored in a custom database (Alyx v1.4) available at https://github.com/cortex-lab/alyx. 

Data analysis The data were processed using the custom data pipelines ibllib v2.17 (https://github.com/int-brain-lab/ibllib) and DataJoint for Python v0.13 (https://datajoint.io/). The data were accessed using ONE v1.16 (https://github.com/int-brain-lab/ONE) and DataJoint IBL Pipeline v0.2 (https://github.com/int-brain-lab/IBL-pipeline). Additional data analysis code described in the paper is available at https://github.com/cortex-lab/alyx (v1.4); https://github.com/int-brain-lab/ mtscomp (v1.0); https://github.com/int-brain-lab/ibllib; https://github.com/datoviz/datoviz (v0.1); https://github.com/int-brain-lab/iblenv (unversioned); https://github.com/cortex-lab/LabCI (v3.1); and https://github.com/catalystneuro/IBL-to-nwb (v0.1). Supplementary figure 1 was generated with code available here: https://github.com/int-brain-lab/paper-data-architecture (unversioned). 

All Python packages were used with Python version 3.7 and 3.8. 

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information. 

Data 

## Policy information about availability of data 

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable: 

- Accession codes, unique identifiers, or web links for publicly available datasets 

- A list of figures that have associated raw data 

- A description of any restrictions on data availability 

Data for Figure 2 is freely available at https://data.internationalbrainlab.org 

## - Field specific reporting 

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection. Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences 

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf 

## Life sciences study design 

All studies must disclose on these points even when the disclosure is negative. 

||lose on these points even when the disclosure is negative.|
|---|---|
|||
|Sample size<br>Data exclusions<br>Replication<br>Randomization<br>Blinding|The sample size of 105 mice was used as this was the total number of mice from a previously published dataset (International brain lab et al,<br>eLife 2021). The sample size statement from that paper is "This study exceeds the numbers of animals and lab that would be required strictly<br>to test our hypotheses. This is because the main aim of our research is to acquire neural data from those animals in those labs. The demands<br>for the present study are therefore amply exceeded."|
||Mice that did not reach 'trained' status were excluded as the aim was to evaluate candidate variables for predicting the number of sessions<br>required for mice to complete behavioral training.|
||The data set analyzed contains experiments replicated in multiple labs, and consistent results were found across labs (International brain lab<br>et al, eLife 2021).|
|||
||Randomization of subjects was not necessary as only a single experimental group was used in the analysis.  This group was split into quartiles<br>based solely on the time it took to reach 'trained' status.|
|||
||Investigator blinding was not necessary as the goal was to determine which, if any, variables available in early training were predictive of<br>overall training time after the data had been collected.  A random forest classifier was used and performance was cross-validated.|



## Reporting for specific materials, systems and methods 

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response. 

|Materials & experimental systems|Materials & experimental systems|Materials & experimental systems|Materials & experimental systems|Methods|Methods|Methods|
|---|---|---|---|---|---|---|
|n/a||Involved in the study||n/a||Involved in the study<br>ChIP-seq<br>Flow cytometry<br>MRI-based neuroimaging|
||||Antibodies||||
||||||||
||||Eukaryotic cell lines||||
||||||||
||||Palaeontology and archaeology||||
|||Animals and other organisms<br>Human research participants<br>Clinical data<br>Dual use research of concern|||||
||||||||



## Animals and other organisms 

Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research 

Laboratory animals This paper includes a re-analysis of data previously published in (International Brain lab et al, eLife 2021). For details of species, strain, sex, number and age of animals, and ethical approval, please see the original paper. 

Wild animals 

This study did not use wild animals 

Field-collected samples This study did not use field-collected samples Ethics oversight 

Ethics approval is described in the paper describing the experiments whose data was re-analyzed here(International brain lab et al, eLife 2021). 

Note that full information on the approval of the study protocol must also be provided in the manuscript. 

