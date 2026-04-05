Biological Psychiatry 

## Archival Report 

# Computational Modeling of Electroencephalography and Functional Magnetic Resonance Imaging Paradigms Indicates a Consistent Loss of Pyramidal Cell Synaptic Gain in Schizophrenia 

Rick A. Adams, Dimitris Pinotsis, Konstantinos Tsirlis, Leonhardt Unruh, Aashna Mahajan, Ana Montero Horas, Laura Convertino, Ann Summerfelt, Hemalatha Sampath, Xiaoming Michael Du, Peter Kochunov, Jie Lisa Ji, Grega Repovs, John D. Murray, Karl J. Friston, L. Elliot Hong, and Alan Anticevic 

## ABSTRACT 

BACKGROUND: Diminished synaptic gain—the sensitivity of postsynaptic responses to neural inputs—may be a fundamental synaptic pathology in schizophrenia. Evidence for this is indirect, however. Furthermore, it is unclear whether pyramidal cells or interneurons (or both) are affected, or how these deficits relate to symptoms. METHODS: People with schizophrenia diagnoses (PScz) (n = 108), their relatives (n = 57), and control subjects (n = 107) underwent 3 electroencephalography (EEG) paradigms—resting, mismatch negativity, and 40-Hz auditory steady-state response—and resting functional magnetic resonance imaging. Dynamic causal modeling was used to quantify synaptic connectivity in cortical microcircuits. 

RESULTS: Classic group differences in EEG features between PScz and control subjects were replicated, including increased theta and other spectral changes (resting EEG), reduced mismatch negativity, and reduced 40-Hz power. Across all 4 paradigms, characteristic PScz data features were all best explained by models with greater selfinhibition (decreased synaptic gain) in pyramidal cells. Furthermore, disinhibition in auditory areas predicted abnormal auditory perception (and positive symptoms) in PScz in 3 paradigms. 

CONCLUSIONS: First, characteristic EEG changes in PScz in 3 classic paradigms are all attributable to the same underlying parameter change: greater self-inhibition in pyramidal cells. Second, psychotic symptoms in PScz relate to disinhibition in neural circuits. These findings are more commensurate with the hypothesis that in PScz, a primary loss of synaptic gain on pyramidal cells is then compensated by interneuron downregulation (rather than the converse). They further suggest that psychotic symptoms relate to this secondary downregulation. 

https://doi.org/10.1016/j.biopsych.2021.07.024 

Reduced excitatory synaptic gain (i.e., decreased slope of the presynaptic input–postsynaptic response relationship) is believed to be a primary deficit in schizophrenia (1,2). This reduction may primarily affect pyramidal cells (1) or inhibitory interneurons (3). For example, loss of cortical interneuron markers (in postmortem studies of people with schizophrenia diagnoses [PScz]) was originally thought to indicate a primary interneuron pathology, but recent work suggests that these markers are activity dependent, so their loss may reflect weaker pyramidal inputs (4). Decreased interneuron function in the disorder may thus be primary or a compensatory response to try to rebalance excitatory and inhibitory transmission in cortical circuits (5). These hypotheses are difficult to test in vivo, however. 

Various mechanisms may reduce synaptic gain in schizophrenia: the most important is probably hypofunction of NMDA receptors (NMDARs) and their postsynaptic signaling cascade (1,2). Evidence for this comes from psychiatric genetics (6), magnetic resonance spectroscopy imaging (7), neuropathological studies (4), and animal models (8), but of these, only magnetic resonance spectroscopy is performed in humans in vivo, and its glutamatergic measures are difficult to interpret. Other neuromodulatory dysfunctions in schizophrenia [e.g., reduced cortical dopamine (9) or muscarinic receptors (10)] can be assessed more directly using positron emission tomography, but magnetic resonance spectroscopy and positron emission tomography are very indirect measures of synaptic gain. 

## SEE COMMENTARY ON PAGE 167 

202 ª 2021 Society of Biological Psychiatry. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

ISSN: 0006-3223 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [81 x 71] intentionally omitted <==**

**==> picture [121 x 54] intentionally omitted <==**

**==> picture [209 x 107] intentionally omitted <==**

**==> picture [22 x 32] intentionally omitted <==**

**==> picture [14 x 20] intentionally omitted <==**

**==> picture [13 x 20] intentionally omitted <==**

**==> picture [13 x 20] intentionally omitted <==**

**==> picture [106 x 34] intentionally omitted <==**

**==> picture [223 x 61] intentionally omitted <==**

**==> picture [87 x 52] intentionally omitted <==**

**==> picture [106 x 34] intentionally omitted <==**

**==> picture [210 x 34] intentionally omitted <==**

**==> picture [109 x 196] intentionally omitted <==**

**==> picture [158 x 90] intentionally omitted <==**

Figure 1. An overview of the analysis. This schematic illustrates the key steps in the preprocessing of the electroencephalography (EEG) (resting state [rs], mismatch negativity [MMN], and 40-Hz auditory steady-state response [ASSR]) and resting-state functional magnetic resonance imaging (rsfMRI) paradigms and their subsequent analysis using dynamic causal modeling (DCM) and parametric empirical Bayes. Simplified depictions of the paradigms are shown in the first column (see the Supplement for details), with group differences in EEG data features in the second column (first 3 rows) and DCM in the third column. The EEG data control group (Con) versus people with schizophrenia diagnoses (PScz) group differences are (from first to third rows) in rsEEG q, b, and g frequency band power (Figure 2A), MMN responses (Figure 3A), and 40-Hz ASSR power (Figure 4C). The second column of the final row (rsfMRI) shows the Glasser parcellation areas primary auditory cortex (A1) (middle), A4 (left), and 44 (right) containing the MMN sources A1, superior temporal gyrus (STG), and inferior frontal gyrus (IFG), respectively; these were used as nodes in the rsfMRI analysis, so that results could be compared across data modalities. Key preprocessing and analysis steps are described below the illustrations. DCM for EEG uses a cortical microcircuit model, shown on the left in the third column 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

203 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

An alternative way to investigate synaptic gain is by using electroencephalography (EEG) paradigms such as the mismatch negativity (MMN), an auditory oddball paradigm (11), and auditory steady-state response at 40 Hz (40-Hz ASSR); a paradigm inducing neural oscillations using a click train (12); or in the “resting state,” measuring with EEG (rsEEG) or functional magnetic resonance imaging (rsfMRI). PScz show robust reductions in 40-Hz ASSR (12) (d z 0.6) and MMN (11) (d z 1) responses, which may relate to diminished synaptic gain and decreased gain modulation (13), respectively, but these paradigms are not direct indices of synaptic gain. 

Neural mass models of noninvasive data can be parameterized in terms of synaptic gain and these parameters estimated, for example, using dynamic causal modeling (DCM) (14), furnishing model-based biomarkers (15,16). This has several advantages: it can estimate subject-specific parameters and can fit evoked (e.g., MMN) and induced (e.g., 40-Hz ASSR or resting) EEG responses and rsfMRI, and thus explain responses to different paradigms in terms of common synaptic parameters, such as gain or self-inhibition on pyramidal cells or interneurons. Although fMRI models cannot incorporate detailed microcircuit parameters, due to fMRI’s coarse temporal resolution, they can assess local changes in excitability. Third, one can employ hierarchical modeling, e.g., using group-level parameters recursively to inform singlesubject fits, for example, using parametric empirical Bayes (PEB) (17). 

To date, DCM studies of PScz have used modest sample sizes and single paradigms but have found reasonably consistent results, e.g., cortical disinhibition in EEG (13,18–20) and rsfMRI (21) and diminished contextual gain modulation (13,19,22). Nevertheless, foundational questions remain, including the following: are well-replicated group differences between PScz and control subjects (Con) across paradigms all ascribable to the same model parameter(s)? How do symptoms in PScz relate to these parameters? Here, we address these questions using DCM across multiple EEG and fMRI paradigms, in PScz, Con, and first-degree relatives (Rel). 

## METHODS AND MATERIALS 

Data were collected from PScz (n = 107) recruited from outpatient clinics, first-degree relatives (n = 57), and control subjects (n = 108) recruited from media advertisements, who each underwent rsEEG, MMN, 40-Hz ASSR, and rsfMRI paradigms and recorded symptoms and other measures. PScz and Con were well matched in terms of age (mean 6 SD = 39.4 6 14.3 years and 39.4 6 13.9 years, respectively), sex (59% and 68% male, respectively) and smoking status (33% and 39% smokers, respectively). PScz had mean Brief Psychiatric Rating Scale scores of 14.4 out of 49 for positive symptoms and 7.3 out of 28 for negative symptoms (Table S1). We first performed conventional analyses of group differences in data 

features for each paradigm. We then inferred the best explanations for these differences in terms of DCM parameters. Figure 1 summarizes the analysis (excluding results). 

We used the DCM canonical microcircuit neural mass model (Figure S1) to analyze the EEG paradigms; more details are given in the Results, with a full description in the Supplement. Model parameters include connectivity strengths between populations, self-inhibition (synaptic gain) in these populations, and membrane time constants and transmission delays. For the rsEEG, MMN, and 40-Hz ASSR paradigms, we analyzed group differences using conventional data features (event-related potentials or power spectra). We then modeled either group-averaged data (rsEEG) or estimated subjectspecific DCM parameters (MMN and 40-Hz ASSR). For rsfMRI, we only modeled the network generating MMN (and 40-Hz ASSR, in part) for comparative purposes. 

We used PEB to analyze group and individual differences in synaptic (model) parameters, with the exception of rsEEG, where characteristic group responses were modeled. We interpret greater self-inhibition of pyramidal cells as an effective loss of pyramidal synaptic gain. Given known pathophysiology in PScz, NMDAR hypofunction seems the most likely explanation for loss of pyramidal gain, but other explanations are possible (see Supplement for further discussion). 

Age, sex, smoking, and chlorpromazine dose equivalent covariates did not significantly affect the results, unless otherwise stated. All t tests were two-tailed, and rank sum tests were used if distributions were skewed; none are Bonferroni-corrected unless stated. 

## RESULTS 

## In rsEEG, PScz Have Altered Power in q, b, and g Frequency Bands 

We first examined rsEEG power spectra by subtracting the 1/f gradient, noting that gradients did not differ between groups with eyes open or closed (p . .2). The mean adjusted power spectra within the Con (n = 98) and PScz (n = 95) groups are shown in Figure 2A, for eyes closed (left) and open (right) conditions, with q/a/b/g frequency bands demarcated. A repeated-measures analysis of variance (between-subjects factor, group; within-subjects factors, eyes open/closed and frequency band) demonstrated a significant interaction of frequency 3 group (F3,573 = 6.59, p , .001) but not of eyes 3 group (F1,191 = 0.05, p = .8) or of frequency 3 eyes 3 group (F3,573 = 0.4, p = .8). We therefore averaged the power in each frequency band across eyes open and closed conditions and performed Wilcoxon rank sum tests (as some distributions were skewed), Bonferroni-corrected for 4 frequency bands (Figure 2B). PScz had increased q (Z = 2.63, pCorr = .035), decreased b (Z = 22.77, pCorr = .022), and increased 

= (also see Figure 2C). It contains superficial and deep pyramidal cells (blue triangles), inhibitory interneurons (red circles), and spiny stellate cells (green stars). The lower three DCM illustrations include macroscopic model structures, i.e., the cortical areas involved: A1, STG, and IFG (58). In the rsEEG analysis (top row), a single-area DCM was used to reproduce power spectra characteristic of each group. In the remaining paradigms, models were fitted to the data and parametric empirical Bayes was used to analyze group and individual differences. The final column depicts an example analysis (from Figure 3F) of group differences in DCM parameters between Con and PScz in the MMN. ICA, independent component analysis; MEG, magnetoencephalography; Rel, first-degree relative. 

204 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [481 x 526] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>rsEEG: eyes closed rsEEG: eyes open All rsEEG<br>8 ↑θ p=0.035 α p=0.75 ↓β p=0.022 ↑γ p=0.040<br>Con Con<br>Scz Scz 6 Con<br>Scz<br>4<br>2 ↑↓ Scz change<br>0<br>- - -2<br>- - -4<br>- - -6<br>θ α β γ<br>C left right<br>IFG IFG<br>sp<br>forward  STG STG<br>connection<br>STG<br>ii ss IFG backward<br>connection<br>A1 A1<br>self-inhibitory<br>dp connection  drive (not used in<br>(EEG: sp cell  resting state)<br>self-inhibition)<br>Canonical microcircuit model  2 area model (example) 3 area MMN model schematic<br>(EEG only): all connections<br>D<br>rsEEG microcircuit model simulations<br>↑θ ↓β ↓γ ↑θ ↓β ↔γ ↓θ ↓β ↔γ ↑θ ↑β ↔γ ↑θ ↓β ↑γ<br>0.4 0.4 0.4 0.4 0.4<br>0.3 0.3 0.3 0.3 0.3<br>0.2 0.2 0.2 0.2 0.2<br>0.1 0.1 0.1 0.1 0.1<br>0 0 0 0 0<br>-0.1 -0.1 -0.1 -0.1 -0.1<br>Modle 1 Modle 2 Modle 3 Modle 4 Modle 5<br>-0.2 -0.2 -0.2 -0.2 -0.2<br>0 20 40 60 80 0 20 40 60 80 0 20 40 60 80 0 20 40 60 80 0 20 40 60 80<br>Frequency (Hz) Frequency (Hz) Frequency (Hz) Frequency (Hz) Frequency (Hz)<br>Con simulations<br>Scz simulations (<30%<br>change in parameters) Model 1: Model 2: Model 3: Model 4: Model 5:<br>↑θ [Simulation matches ] Scz rsEEG All (except  ii inputs ↓ ii self- ii ‘gain’ ↓ sp ‘gain’ ↓<br>self-inhibition) (or outputs ↓)  inhibition ↓ (↑self-inhib.) (↑self-inhib.)<br>↑θ [Simulation doesn’t ] match Scz rsEEG<br>Normalized p ower (AU) Normalised p ed power (AU) NormalisNormaliz Normalized power (AU)Normalised power (AU)<br>Normalized power (AU)Normalised power (AU)<br>**----- End of picture text -----**<br>


Figure 2. Resting-state electroencephalography (rsEEG) results, dynamic causal modeling (DCM) model structure, and rsEEG simulations. (A) Mean normalized eyes closed and eyes open rsEEG power spectra (6 SEM) across all channels for control subjects (Con) (n = 98; blue) and people with schizophrenia diagnoses (PScz) (n = 95; red) groups, divided into 4 frequency bands (dotted lines): q (3–7 Hz), a (8–14 Hz), b (15–30 Hz), and g (.31 Hz). (B) Group comparisons in mean power across both eyes closed and eyes open conditions in the q, a, b, and g bands are shown. The box plots show the mean, SEM, and SD. p values are Bonferroni-corrected for 4 comparisons. (C) EEG DCMs used the current version of the canonical microcircuit model (59) (also see Figure S1A). This microcircuit (left) consists of superficial pyramidal (sp) and deep pyramidal (dp) cells, inhibitory interneuron (ii), and spiny stellate (ss) cells. They are interconnected with excitatory (arrowheads) and inhibitory (beads) connections; their self-inhibitory connections parameterize their responsiveness to their inputs, i.e., synaptic gain. In EEG DCM, each modeled cortical area contains a microcircuit (middle); functional magnetic resonance imaging DCM uses a much simpler neuronal model. Both DCMs have self-inhibition parameters (round gray beads), which—in EEG—inhibit superficial pyramidal cells specifically. A schematic DCM diagram is explained on the right. (D) The top row shows the results of 5 sets (models 1–5) of simulations of microcircuit parameter changes 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 205 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

g (Z = 2.58, pCorr = .040), but unchanged a (Z = 21.32, pCorr = .75). 

## Increased Pyramidal Self-inhibition Explains q, b, and g Changes in PScz 

We used DCM’s canonical microcircuit model—a biophysical model of interacting pyramidal, interneuron, and spiny stellate populations (Figure 2C, left)—to identify the most likely synaptic pathology. To model power spectrum changes in PScz, we treated cortex as a single microcircuit in which specific parameters were changed in 5 plausible ways (Figure 2D, bottom): a loss of all microcircuit connectivity (model 1), a loss of pyramidal connections to or from interneurons (model 2), interneuron disinhibition (model 3), increased interneuron selfinhibition (model 4), and increased pyramidal cell self-inhibition (model 5). Note that this model does not fit the large a peak. 

Only model 5 could explain the q, b, and g changes seen in PScz (Figure 2D, upper row). Models 1 and 2 only reproduced the q and b changes. Model 3 showed decreased b peak frequency, which was quantitatively lower in PScz but not statistically significant (Figure S2A). 

## MMN and P100 Are Reduced in Both PScz and Rel 

The MMN paradigm consisted of standard and durationdeviant tones. The mismatch amplitude is the deviant– standard response in electrode Fz (11), which was reduced in both PScz and Rel around 200 ms (Figure 3A). There were no significant group differences in MMN latency between Con (mean 6 SD latency = 194 6 34 ms) and Rel (196 6 45 ms, p = .8) or PScz (202 6 44 ms, p = .18). In the averaged deviant and standard waveforms (Figure S2B), PScz showed reduced response amplitudes around 50 to 100 ms in both, and an exaggerated mismatch-like response around 175 ms in the standard condition. 

Smoothed sensor-level data were analyzed using clusterbased statistics. Across Con and PScz, there was a strong mismatch effect, peaking at 198 ms (peak familywise errorcorrected p [pFWE] , .001, t376 = 11.23) (Figure 3B), which was reduced in PScz (peak at 186 ms, punc , .001, cluster pFWE = .010, t376 = 3.46) and in Rel (peak at 198 ms, punc , .001, cluster pFWE = .011, t268 = 3.83) (Figure 3C). Likewise, PScz had a reduced P100 response (peak at 82 ms, pFWE = .003, cluster pFWE , .001, t376 = 4.83), as did Rel, although this was only significant at an uncorrected peak threshold (peak at 94 ms, punc = .001, cluster pFWE = .8, t268 = 3.02) (Figure S2C). 

## DCM of MMN Indicates Increased Frontal Selfinhibition in PScz, but Disinhibition in Broca Area Relates to Abnormal Auditory Percepts 

We first used model comparison to establish whether it was best to fix or estimate various microcircuit parameters in the MMN analysis (see Supplement). We compared 6 models 

(Figure 3D): model 6G estimates 6 connectivity (G) parameters, models 4Ga-d consider subsets of these six, and model 6G,D,T also estimates delays and time constants. Bayesian model selection preferred model 6G (also in Con and PScz separately), with a protected exceedance probability of p = .89 (Figure 3E, left). This model fitted most participants’ data accurately (e.g., Figure S3A). A histogram of R[2] values is shown in Figure 3E (right); the group mean R[2] was 0.73. R[2] were slightly higher in Con (mean 6 SD = 0.76 6 0.13) than in PScz (0.70 6 0.14; rank sum Z = 3.12, p = .0018) and Rel (0.71 6 0.15; rank sum Z = 2.14, p = .033) (Figure S3C). 

We then used PEB to ask which parameters best explained group differences in MMN: self-inhibition within areas or connections between areas. The reduced mismatch amplitude in PScz was best explained by increased self-inhibition in deviant—relative to standard—trials in left (L) inferior frontal gyrus (IFG) (p . .95) and right (R) IFG (p . .99) (Figure 3F). Including chlorpromazine dose equivalent covariates reduced the posterior probability to p . .75, but age, sex, and smoking had no effect. Conversely, there was no overall group effect (across both standards and deviants) of PScz on the microcircuit parameters (all p , .95) (Figure S4C, left) unless chlorpromazine dose equivalents were included as covariates; here, PScz showed greater superficial pyramidal self-inhibition in L and R IFG (both p . .99) (Figure S4C, middle and right) and reduced interneuron self-inhibition throughout (p . .95). Rel did not show effects of p . .95 in either analysis. 

In PScz, the auditory perceptual abnormalities state measure was associated with disinhibition in L IFG (p . .99)— within the Broca area—but increased self-inhibition in R IFG (p . .95) in the mismatch contrast (Figure 3G). Historical auditory perceptual abnormalities (the trait measure) showed similar effects but at lower posterior probability (p . .75, not shown). 

## PScz Had Reduced g Power and Peak Frequency in 40-Hz ASSR, and Rel Had Reduced g Power 

We next considered induced responses during auditory steady-state stimulation. Group-averaged 40-Hz ASSR are shown in Figure 4A and the distributions of participants’ peak g – (35 45 Hz) frequencies in Figure 4B. PScz had slightly reduced g peak frequency: mean peak frequencies (following subtraction of the 1/f gradient) (Figure S2E) were Con = 40.2 Hz (SD, 1.7), PScz = 39.5 Hz (SD, 1.7; t184 = 2.67, pCorr = .016), and Rel = 39.9 Hz (SD, 2.1; t132 = 1.03, p = .3). Adjusted timefrequency plots are shown in Figure 4C (and raw timefrequency data in Figure S2F): Con showed a robust increase in w40 Hz power around 100 ms, which is diminished in PScz and Rel (p , .05; t tests at each frequency and time point are circled on the middle and right plots, for Con vs. PScz and Con vs. Rel in black and PScz vs. Rel in white; this many differences are unlikely due to chance—Con vs. PScz and Con 

= and their similarity to the rsEEG changes in q, b, and g bands in PScz (the model does not produce an a peak). The parameters changed in each model are illustrated in the microcircuit schematics for models 1–5 (bottom row); parameter increases are denoted by whole lines and decreases by dotted lines. Each model is used to produce 10 simulations, starting with standard parameter values (to simulate Con) plotted in dark blue, and then reducing or increasing the parameters illustrated below in increments of 3% to simulate PScz (up to the most extreme change, plotted in dark red). Only model 5, an increase in superficial pyramidal self-inhibition, i.e., a loss of synaptic gain, reproduces the changes seen in all 3 frequency bands. IFG, inferior frontal gyrus; MMN, mismatch negativity; STG, superior temporal gyrus. 

206 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [481 x 560] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>Mismatch effect: Fz Sensor-level  Con > Scz  Con > Rel<br>(deviants – standards)  mismatch effect mismatch effect mismatch effect<br>C<br>Con<br>Scz<br>Rel<br>0 100 200 300 0 100 200 300 0 100 200 300<br>Time (ms) Time (ms) Time (ms)<br>D Microcircuit models’ free parameters<br>Peak p<0.001 (FWE) Peak p<0.001 (unc) Peak p<0.001 (unc)<br>11 3.4 3.8<br>10 3.6<br>9 3.2 3.4<br>8<br>3 3.2<br>4Ga 4Gc 6G 7<br>3<br>6 2.8<br>& delays Fz 5 Fz Fz 2.8<br>& time  2.6 2.6<br>constants Right Left t Right Left t Right Left t<br>4Gb 4Gd 6G,D,T Sensors Sensors Sensors<br>E F<br>Model comparison and fit Connectivity parameters, deviants–standards: Scz > Con<br>0.4 * ** IFG IFG<br>1 50<br>Mean R2=0.73 0.3<br>0.8 40<br>0.2<br>0.6 30 STG STG<br>0.1<br>0.4 20<br>0.2 10 0 A1 A1<br>0 0 -0.1<br>0 0.2 0.4 0.6 0.8 1<br>R2<br>Free parameters ** p>0.95<br>PEB Parameter ** p>0.99<br>G<br>Deviant–standard effects vs Auditory Perceptual State: Scz only<br>0.2 ** * IFG IFG<br>0.1<br>0 STG STG<br>-0.1<br>-0.2 A1 A1<br>** p>0.95<br>PEB Parameter ** p>0.99<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>4Ga 4Gb 4Gc 4Gd 6GD,T,6G L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>Posterior Posterior Posterior<br>Anterior Anterior Anterior<br>Posterior Posterior Posterior<br>Anterior Anterior Anterior<br>Posterior<br>Frequency<br>Protected exceedance prob Number of participants Effect size (log scaling)<br>Posterior<br>Effect size (log scaling)<br>**----- End of picture text -----**<br>


Figure 3. Mismatch negativity data and modeling analysis. (A) Mismatch difference waves (i.e., deviant–standard, mean 6 SEM) for control subjects (Con) (n = 94; blue), people with schizophrenia diagnoses (PScz) (n = 96; red), and first-degree relatives (Rel) (n = 42; green) at electrode Fz. Group differences are computed using t tests (uncorrected [unc]) at each time point and are marked with red (PScz vs. Con) and green (Rel vs. Con) bars above the difference waves. There were no significant PScz vs. Rel differences. (B) The lower plot shows the location of the mismatch effect (i.e., deviants—standard) at sensor level across all Con and PScz, displayed at p , .05 (familywise error [FWE]). Fz is shown in white. The peak effect is shown in green (p , .001 [FWE], t376 = 11.23). The upper plot shows sensors vs. time; the peak effect occurs at 198 ms. (C) These plots show the interaction of condition and group for the Con . PScz contrast 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 207 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

vs. Rel both p , .001, PScz vs. Rel p = .006, permutation tests). Maximum ASSR g power correlated with MMN amplitude in PScz (r = 0.28, pCorr = .029) but not in Con (r = 0.04, p = .7) or Rel (r = 0.14, p = .4). 

## 40-Hz ASSR DCM Suggests a Loss of Pyramidal Input to Interneurons in PScz and Rel and Greater Self-inhibition in PScz 

The peak cortical source—closest to primary auditory cortex (A1)—was (50 212 4), hence bilateral sources at (650 212 4) were used as priors for reconstruction of virtual electrode data: the DCM comprised these bilateral sources and their thalamic drive (Figure 4D). Empirical priors for several parameters were used to optimize model fit (Figure S1A). Bayesian model comparison between the full model (containing empirical priors for the contribution of spiny stellate cells to measured signals, the neural activation function, and synaptic time constants) and models with standard priors for these parameters showed that the full model was superior (Figure 4E, left). The 40-Hz thalamic drive was modeled using a Gaussian bump function of width w # 4 Hz (see Supplement); this width performed better than a narrower bump of 1 Hz (model -w) (Figure 4E). Model fits for the winning model were reasonable (mean R[2] = 0.53) (Figure S3B). Group differences in R[2] were not detected (rank sum tests: all p . .1) (Figure S3C). 

We performed group comparisons with PEB using schizophrenia genetic risk (PScz 1 Rel . Con) and diagnosis (PScz . Rel) as explanatory variables (13,19), instead of PScz . Con and Rel . Con comparisons (as in the MMN analysis). This was because the group differences in data features were less marked in the 40-Hz ASSR, and there were substantial differences between Rel and Con parameters, only some of which were shared by PScz (Figure S6B). The genetic risk effect was an increased conduction delay in L A1 (p . .95) (Figure 4F), and reduced superficial pyramidal (sp) to inhibitory interneuron (ii) connectivity (p . .99) (Figure 4G, left). The schizophrenia diagnosis effect was increased superficial pyramidal selfinhibition in bilateral A1 in PScz (both p . .99) (Figure 4G, right). 

## 40-Hz ASSR DCM Links Abnormal Auditory Percepts to A1 Disinhibition in PScz 

In PScz, the auditory perceptual abnormalities trait measure related to a disinhibited sp-ii-sp circuit, i.e., increased sp-ii (p . .99) and reduced ii-sp connectivity (p . .99), and greater selfinhibition in L A1 (p . .99) (Figure 4H). The auditory state measure had similar associations but at lower posterior probability (p . .95 for sp-ii, p . .75 for ii-sp and sp-sp: not shown). 

## rsfMRI DCM of the MMN Circuit Finds Increased Self-inhibition in IFG in PScz and Rel 

We then analyzed effective connectivity within the MMN network during rsfMRI, i.e., the Glasser parcellation areas (in the rsfMRI data) based on MMN source locations (see Supplement): bilateral A1, A4, and 44 (Figure 1). The microcircuit model for fMRI data is simpler than the neural mass models used for EEG; however, they retain inhibitory selfconnections. Model fits were accurate: R[2] s were .0.7 in all groups, with no group differences (rank sum tests: all p . .05) (Figure S3C). 

In PEB analysis, PScz showed increased self-inhibition in L and R IFG (p . .99 and p . .95, respectively) (Figure 5A). These effects were robust to age, sex, and smoking covariates (and to the removal of the 10 participants with the lowest rsfMRI signal-to-noise ratio: 8 PScz and 2 Con; both p . .95). These effects did not survive addition of chlorpromazine dose equivalents (L IFG self-inhibition fell to p . .75). However, Rel . Con showed the same increase in self-inhibition in bilateral IFG (both p . .95) (Figure 5B). This group difference did not survive addition of the age covariate: Rel were older than Con (Rel mean age = 45.4 6 16.6 years, Con mean age = 39.4 6 14.3 years; t162 = 2.4, p = .02). These differences were not detected using conventional functional connectivity analyses, which cannot assess self-inhibition, or analyses of regional variance (Figure S6B–E and Supplement for further discussion). 

= (left) and Con . Rel contrast (right) in the same format as Figure 2B, at the lower threshold of p , .005 (unc) for display purposes. Both groups demonstrate similar differences from Con in the mismatch contrast in frontocentral sensors just before 200 ms. (D) Microcircuit models were compared, differing only in which parameters were allowed to change from their priors (estimated G connectivity parameters are shown, as in Figure 2C). These models’ free G parameters included various combinations of superficial pyramidal and/or deep pyramidal cell (blue) connections to or from inhibitory interneurons (red) and self-inhibition of superficial pyramidal and inhibitory interneuron cells. Note that each parameter within each microcircuit could differ between subjects but was constrained to be the same in every cortical area within subjects, except for superficial pyramidal self-inhibition, which could differ throughout. The final model also estimated delay (D) and time constant (T) parameters (these were fixed in the other five models). (E) Model comparison and evaluation. Left: the protected exceedance probability is the probability a particular model is more likely than any other tested model, above and beyond chance, given the group data. The model with most free parameters is at the far right; it comes second to the 6G model with fixed delays and time constants and 6 microcircuit connectivity parameters estimated. Right: a histogram of R[2] values for all participants for the winning model; it fits most participants well. (F) A parametric empirical Bayes (PEB) analysis of mismatch negativity model parameters (i.e., connections) that contribute to the PScz . Con mismatch effect. The results are plotted on the left (with 95% Bayesian confidence intervals) and shown in schematic form on the right; parameters with posterior probabilities of p . .95 or p . .99 of contributing to the group difference effect are indicated with 1 (*) or 2 asterisks (**), respectively. On the plot, self-inhibitory connections are shaded gray, forward (fwd) connections shaded yellow, and backward (bkwd) connections shaded purple (matching the colors in the schematic). The y-axis denotes logscaling of the effect size; changes of exp (60.2) are of roughly 620%. Some parameters have been eliminated during Bayesian model reduction (see Supplement). The analysis indicates that PScz showed greater self-inhibition (or reduction in synaptic gain) in bilateral inferior frontal gyrus (IFG) in the mismatch contrast. The Rel . Con contrast did not show significant effects. (G) PEB analysis of mismatch negativity mismatch effect model parameters that correlate with current (state) abnormal auditory percepts within PScz only, plotted in the same format as Figure 3F. Within PScz, abnormal auditory percepts relate to reduced self-inhibition in right (R) IFG but disinhibition in left (L) IFG (in Broca area). All effects shown in (F) and (G) are also present without the addition of age, sex, and smoking covariates (p . .95). Inclusion of a chlorpromazine dose equivalent covariate renders the analysis in (F) nonsignificant (p . .75), but it makes the overall effect of PScz on L and R IFG self-inhibition become significant (Figure S4C). STG, superior temporal gyrus. 

208 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [481 x 569] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>40 Hz Auditory steady state response: Fz Peak γ frequency<br>0.5<br>p<0.05 Con vs Scz p=0.016; Con<br>0.4 Con vs Rel p=0.3 Scz<br>Rel<br>0.3<br>0.2<br>Con<br>Scz 0.1<br>Rel<br>0<br>35 36 37 38 39 40 41 42 43 44 45<br>Peak γ frequency (Hz)<br>C Con Scz        Rel<br>D E 1 40 F 4 * Scz+Rel<br>Mean R2=0.53<br>0.8 > Con<br>30<br>2<br>0.6<br>20<br>0.4<br>0<br>10<br>0.2<br>A1 A1 ** p>0.95<br>0 0 -2<br>0 0.2 0.4 0.6 0.8 1 L R<br>Models with alternative priors R2 Delays<br>G<br>40 Hz ASSR microcircuit parameters: Scz+Rel > Con 40 Hz ASSR microcircuit parameters: Scz > Rel<br>** ** ** L & R<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0 0<br>-0.2 -0.2<br>-0.4 -0.4<br>** p>0.99 ** p>0.99<br>PEB Parameter PEB Parameter<br>H<br>40 Hz ASSR parameters vs Auditory Perceptual Trait: Scz only<br>** ** ** L<br>0.6<br>0.4<br>0.2<br>0<br>-0.2<br>-0.4<br>** p>0.99<br>PEB Parameter<br>-J(1) -S -T -w Full<br>L sp-spR sp-sp ii-ii ii-spii-dp sp-ii dp-ii<br>L sp-spR sp-sp ii-ii ii-spii-dp sp-ii dp-ii<br>L sp-spR sp-sp ii-ii ii-spii-dp sp-ii dp-ii<br>Proportion of participants<br>Number of participants<br>Protected exceedence prob Effect size (log scaling)<br>Effect size (log scaling) Effect size (log scaling)<br>Effect size (log scaling)<br>**----- End of picture text -----**<br>


Figure 4. 40-Hz auditory steady-state response (ASSR) data and modeling analysis. (A) 40-Hz ASSR time courses at electrode Fz for control subjects (Con) (n = 92; blue), people with schizophrenia diagnoses (PScz) (n = 94; red), and first-degree relatives (Rel) (n = 42; green). Sixteen clicks were played at 40 Hz, starting at 0 ms. Group differences in the baseline deflection (not modeled subsequently) emerge after around 250 ms, shown with red bars (Con vs. PScz) and green bars (Con vs. Rel), both p , .05 (t tests per time point, uncorrected). (B) g (35–45 Hz) frequencies with the strongest power (in the normalized spectrum) in each participant are shown in a histogram. (C) These normalized time frequency plots show the w40 Hz responses around 100 to 400 ms. The PScz and Rel 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 209 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

## rsfMRI DCM Reveals Relationships of Positive Symptoms to Cortical Disinhibition in PScz 

PEB analysis within PScz found that trait auditory perceptual abnormalities were associated with increased self-inhibition in L and R IFG (both p . .99) (Figure 5C, left). Conversely, state auditory perceptual abnormalities were associated with disinhibition in R A1 (p . .95) and L A1 and superior temporal gyrus (STG) (both p . .99) and STG-A1 backward connectivity bilaterally (both p . .99) (Figure 5C, right). 

Similarly, Brief Psychiatric Rating Scale positive symptoms (including age, sex, smoking, and negative symptoms covariates) were associated with decreased self-inhibition everywhere except R STG (all p . .99 except L IFG and R A1, both p . .95) and stronger forward connections everywhere except R Al-STG (all p . .99) (Figure 5D, left). Brief Psychiatric Rating Scale negative symptoms (including age, sex, smoking, and positive symptom covariates) were associated with decreased self-inhibition in all temporal—but not frontal—nodes (all p . .99) (Figure 5D, right). 

Note that many rsfMRI results were lost if global signal regression was not performed (Supplemental Results, Figure S7). 

## Self-inhibition Findings in PScz Across 

## Electroencephalography and rsfMRI Paradigms Are Similar 

In summary, we found clear evidence for increased selfinhibition (evidence of reduced synaptic gain) in PScz (Figure 6A) in all data modalities and paradigms. However, auditory perceptual abnormalities within PScz were associated with the opposite change: disinhibition (Figure 6B). A sensitivity analysis (see Supplement) confirmed that increased superficial pyramidal self-inhibition best reproduced the key data features of MMN (i.e., decreased MMN amplitude but unchanged latency) (Figure S8A) and, along with loss of sp-ii connectivity, decreased 40-Hz ASSR (Figure S8B). Evidence for withinsubject correlations in self-inhibition parameters across paradigms was weak, however (see Supplemental Results, Figure S9). 

## DISCUSSION 

DCM of EEG and fMRI produced two key cross-paradigm findings. First, well-established effects in rsEEG (23), MMN (11), and 40-Hz ASSR (12) paradigms in PScz were replicated, and all could be explained by increased self-inhibition in 

(superficial) pyramidal cells. Likewise, PScz also showed an increase in prefrontal self-inhibition—similar to MMN—in rsfMRI (Figure 6A). This strongly favors the hypothesis that there is diminished synaptic gain on pyramidal cells (1,2,5) over the hypothesis of diminished synaptic gain on interneurons (3) in this sample of PScz with established illness. 

Second, abnormal auditory percepts in PScz were associated with decreased self-inhibition in auditory areas selectively across 3 paradigms (Figure 6B). This is consistent with 40-Hz ASSR g power (24) [and phase locking of auditory g (25)] correlating positively with auditory symptoms, despite being reduced in PScz overall [as in the visual domain (26)], and with hallucinations and psychotic-like experiences relating to decreased self-inhibition in IFG across the psychosis spectrum (27). Positive symptoms were also associated with disinhibition in the rsfMRI analysis (Figure 5D). These opposing effects of group and symptoms on self-inhibition (28)—and also on cortical glutamate (29)—support the hypothesis (1,5) that decreased synaptic gain (NMDAR hypofunction in particular) is compensated by allostatic disinhibition of pyramidal cells (i.e., interneuron downregulation) and, furthermore, indicate that psychotic symptoms result from this disinhibitory rebalancing of excitatory and inhibitory transmission. 

In rsEEG, increased q power in PScz is a well-established finding (23,30). A U-shaped change in spectral power (here, increased q, decreased b, increased g) has been seen several times across q, a, and b frequencies (23). Increases (not decreases) in a and b in PScz have been seen in eyes open rsEEG (30,31), but in unnormalized data; before subtracting the 1/f gradient, b power was numerically higher in our sample of PScz as well. This speaks to the importance of distinguishing band-specific changes from changes in 1/f slope, which itself is increased by lower excitation:inhibition ratio (32,33). Of note, low g (30–45 Hz) power is typically reduced in PScz with longstanding diagnoses (34), but we lacked illness duration information. 

Decreased mismatch amplitude in PScz [and especially in chronic PScz (35)] is well documented (11), and we found an effect of similar size in Rel, larger than is typical (35). Underlying this effect, we found that deviant stimuli decrease self-inhibition in IFG in Con but not in PScz, recapitulating other DCM studies (13,22). The mismatch amplitude rarely correlates with hallucinations in PScz [e.g., in only 3 of 22 studies (11)], but we found abnormal auditory percepts related to (condition-specific) disinhibition in L IFG—Broca’s area. Traditional MMN analysis (using electrode Fz) might miss this lateralized effect. Nevertheless, there are reports of 

= plots have areas of difference from Con encircled in black; the Rel plot has areas of difference from PScz encircled in white (p , .05, t tests at each time and frequency). (D) The left plots show the bilateral primary auditory cortex (A1) (transverse temporal gyrus) sources chosen following source localization [650 -12 4]. The 40-Hz ASSR model structure is on the right: bilateral sources in A1. (E) Left: to improve the dynamic causal modeling fit of the cross spectral densities in bilateral A1 in this nonstandard paradigm, we used empirical priors (also see Figure S1A) for J(1), the contribution spiny stellate cells make to the electroencephalography (EEG) signal; S, the gain of the neuronal activation function; T, population time constants; and w, the width of the w40 Hz Gaussian bump. The plot shows that the full model (with all the empirical priors) is superior to other models that used standard values for their respective priors (or for -w, 1 Hz instead of 4 Hz). Right: a histogram of R[2] s for all participants for the winning model. (F) Parametric empirical Bayes (PEB) analysis indicated that PScz 1 Rel . Con showed increased neural transmission delays in left (L) A1. (G) Left: PEB analysis (in the same format as Figure 3H) indicated that PScz 1 Rel . Con (a psychosis genetic risk effect) had decreased superficial pyramidal (sp)–inhibitory interneuron (ii) connectivity. Right: PScz . Rel (a psychosis diagnosis effect) shows decreased sp self-inhibition in bilateral A1. (H) PEB analysis in PScz, showing that abnormal auditory percepts are associated with disinhibition of the sp-ii circuit (and increased sp self-inhibition in L A1). All effects shown in (F), (G), and (H) are also present without the addition of age, sex, and smoking covariates (p . .95) and with inclusion of chlorpromazine dose equivalents as a covariate. dp, deep pyramidal; Freq, frequency; Pow, power; R, right. 

210 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [481 x 533] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>rsfMRI connectivity parameters: Scz > Con rsfMRI connectivity parameters: Rel > Con<br>(without age covariate)<br>** * * *<br>0.15 IFG IFG 0.15 IFG IFG<br>0.1 0.1<br>0.05 0.05<br>STG STG STG STG<br>0 0<br>-0.05 -0.05<br>-0.1 A1 A1 -0.1 A1 A1<br>-0.15 -0.15<br>** p>0.95 ** p>0.95<br>** p>0.99<br>PEB Parameter<br>PEB Parameter<br>C<br>rsfMRI connectivity parameters vs  rsfMRI connectivity parameters vs<br>Auditory Perceptual Trait Score: Scz only Auditory Perceptual State Score: Scz only<br>** ** ** * ** ** **<br>0.15 IFG IFG 0.15 IFG IFG<br>0.1 0.1<br>0.05 0.05<br>STG STG STG STG<br>0 0<br>-0.05 -0.05<br>-0.1 A1 A1 -0.1 A1 A1<br>-0.15 -0.15<br>** p>0.99 ** p>0.95<br>** p>0.99<br>PEB Parameter PEB Parameter<br>D<br>rsfMRI connectivity parameters vs positive symptoms: rsfMRI connectivity parameters vs negative symptoms:<br>Scz only Scz only<br>0.15 ** * ** * ** ** ** ** IFG IFG 0.15 ** ** ** ** IFG IFG<br>0.1 0.1<br>0.05 0.05<br>STG STG STG STG<br>0 0<br>-0.05 -0.05<br>-0.1 A1 A1 -0.1 A1 A1<br>-0.15 -0.15<br>** p>0.95 ** p>0.99<br>** p>0.99<br>PEB Parameter PEB Parameter<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd L A1 selfR A1 selfL STG selfR STG selfL IFG selfR IFG selfL A1 fwdR A1 fwdL STG fwdR STG fwdL STG bkwdR STG bkwdL IFG bkwdR IFG bkwd<br>Posterior Posterior<br>Effect size (log scaling) Effect size (log scaling)<br>Posterior Posterior<br>Effect size (log scaling) Effect size (log scaling)<br>Posterior Posterior<br>Effect size (log scaling)<br>**----- End of picture text -----**<br>


Figure 5. Resting-state functional magnetic resonance imaging (rsfMRI) modeling analysis. (A) For comparative purposes, the rsfMRI connectivity analysis was conducted on the same network as the mismatch negativity (MMN) analysis. Results for control subjects (Con) (n = 85) and people with schizophrenia diagnoses (PScz) (n = 72) are shown in the same format as Figure 3F. As in the MMN, PScz showed increased self-inhibition in the bilateral inferior frontal gyrus (IFG). Inclusion of chlorpromazine equivalent dose as a covariate still showed increased self-inhibition in left (L) IFG but only at p . .75. (B) rsfMRI connectivity analysis without covariates for Con (n = 85) and first-degree relatives (Rel) (n = 45) is shown. Similar to PScz, Rel show increased self-inhibition in the bilateral IFG, but this effect disappeared with addition of the age covariate (p , .75). (C) Left: within PScz, abnormal auditory percepts (trait measure) related to increased self-inhibition in the bilateral IFG. Right: conversely, abnormal auditory percepts (state score, i.e., experiences within the last week only) relate to disinhibition in temporal areas and also a loss of top-down connections within the auditory cortex. The right (R) primary auditory cortex (A1) effect was attenuated if age, sex, and smoking covariates were not included and if a chlorpromazine dose equivalent covariate was added. (D) Left: within PScz, Brief 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 211 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

**==> picture [10 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [313 x 272] intentionally omitted <==**

**----- Start of picture text -----**<br>
Scz show increased self-inhibition – indicating loss of (pyramidal) synaptic gain – vs other groups<br>Scz simulations, rsEEG Scz > Con, MMN<br>L & R<br>A1<br>sp<br>ii ss<br>Scz > Rel, 40 Hz ASSR Scz > Con, rsfMRI<br>B dp<br>Abnormal auditory perception (AP) in Scz linked to disinhibition in auditory/speech areas<br>L A1<br>Canonical microcircuit model<br>(EEG only): all connections<br>Scz & AP Trait, 40 Hz ASSR Scz & AP State, MMN Scz & AP State, rsfMRI<br>**----- End of picture text -----**<br>


Figure 6. Summary of key findings across paradigms. This figure illustrates similar dynamic causal modeling findings across paradigms using the schematic illustrations from previous analyses. The inset at bottom right shows the canonical microcircuit model for electroencephalography (EEG) (below), which exists in each modeled cortical area (above). The microcircuit consists of superficial pyramidal (sp) and deep pyramidal (dp) cells (blue), inhibitory interneuron (ii) (red), and spiny stellate (ss) cells (green), interconnected with excitatory (arrowheads) and inhibitory (beads) connections. (A) Crucially, the people with schizophrenia diagnoses (Scz) group consistently exhibited increased selfinhibition (as expected from a loss of synaptic gain) in superficial pyramidal cells in particular (i.e., in the EEG paradigms). This was the case (from left to right) in primary auditory cortex (A1) in the 40-Hz auditory steady-state response (ASSR) (when compared with first-degree relatives [Rel]), in the bilateral inferior frontal gyrus (IFG) in both the mismatch negativity (MMN) (deviant–standard contrast) and the restingstate functional magnetic resonance imaging (rsfMRI), and in the rsEEG simulations. (B) Within the PScz group, abnormal auditory percepts were linked with disinhibition in A1 in both the 40-Hz ASSR paradigm and the rsfMRI and with disinhibition in left (L) IFG—i.e., Broca area—in the MMN (deviant– standard contrast). Con, control subjects; R, right; STG, superior temporal gyrus. 

left-lateralized (including IFG) associations of hallucinations with auditory oddball responses in PScz (36). 

In the 40-Hz ASSR, PScz showed decreased g power and peak frequency, and Rel showed decreased power [as elsewhere (12,20,37)]. DCM indicated that diminished pyramidal connectivity to interneurons (and greater transmission delay) was common to both PScz and Rel, but loss of pyramidal gain was unique to PScz (Figure 4G). Others have modeled 40-Hz ASSR in PScz by increasing interneuron time constants (38); this reproduced a concurrent increase in 20-Hz power in PScz (38), which was not observed in our data. We assumed time constants did not differ in PScz in the ASSR or MMN, and estimated connectivity parameters—and delays, in the ASSR—instead (these can be regarded as synaptic rate constants). 

A previous rsfMRI DCM analysis in PScz found disinhibition in the anterior cingulate cortex (21), rather than increased selfinhibition in bilateral IFG (Figure 5A). This recalls a pattern of altered intraprefrontal functional connectivity in early PScz (39): increased connectivity of medial areas and more modest decreases in connectivity in lateral areas. Prefrontal 

hyperconnectivity correlated positively with positive symptoms (39). We similarly found that positive symptoms were associated with disinhibition in bilateral IFG and A1 (Figure 5D, left). This relationship echoes findings that increased functional connectivity of primary sensory areas (to the thalamus) correlates with Positive and Negative Syndrome Scale scores (40), and that increased A1 rsfMRI autocorrelation (a result of reduced self-inhibition) in PScz relates to auditory hallucinations (28) (Figure 5C, right). Our results have commonalities with a spectroscopy mega-analysis that correlated positive symptoms to frontal and negative symptoms to temporal glutamate concentrations (29) (Figure 5D). Thus, symptoms may depend not just on connectivity between nodes but on synaptic gain within nodes; modeling is key to disambiguating these possibilities. 

More data are required to draw firm conclusions about the Rel group. In MMN, no effects exceeded p . .95 despite Rel’s similar data features to PScz. In 40-Hz ASSR, pyramidal selfinhibition was reduced in Rel (Figure S5B), not increased. In rsfMRI, however, Rel showed comparable IFG self-inhibition increases to PScz (Figure 5B). 

= Psychiatric Rating Scale positive symptom score related to disinhibition throughout the MMN network and increased forward (fwd) connectivity in 3 of 4 connections. Most effects were robust to addition of chlorpromazine dose equivalents as a covariate (all p . .99 except L IFG self-inhibition, p . .75), removal of the hallucinations score from the Brief Psychiatric Rating Scale positive symptom total (all p . .95 except L IFG and R A1 self-inhibition, p . .75), and analysis without covariates (all p . .99 except L IFG self-inhibition, p . .75). Right: within PScz, Brief Psychiatric Rating Scale negative symptom score related to disinhibition in temporal nodes of the MMN network. All effects shown (except Rel . Con) are also present without the addition of age, sex, and smoking covariates and if participants (2 Con, 8 PScz) with rsfMRI signal-to-noise ratio ,25 are excluded (all p . .95). Some rsfMRI results are no longer significant without global signal regression (Figure S7). No results change substantially with inclusion of chlorpromazine dose equivalent as a covariate unless stated. bkwd, backward; PEB, parametric empirical Bayes; STG, superior temporal gyrus. 

212 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

## Loss of Pyramidal Synaptic Gain in Schizophrenia 

A crucial question is what changes in self-inhibition mean: changes in synaptic gain or reciprocal coupling with interneurons? Our interpretation of self-inhibition changes is guided by known pathophysiology in PScz, i.e., given that cortical synaptic gain is decreased [e.g., reduced function of NMDA (1,2,6), dopamine D1 (9), and muscarinic (10) receptors] and inhibitory interneurons downregulated (4,5), then the most logical interpretation of increases and decreases in pyramidal self-inhibition is diminished pyramidal synaptic gain (41,42) and decreased interneuron function, respectively (gain in the neural mass model is discussed in detail in the Supplement.) If the fundamental pathology in PScz was a loss of synaptic gain on interneurons, one would expect to see consistent group effects of increased interneuron self-inhibition and/or decreased pyramidal self-inhibition, neither of which were found. 

Regarding potential causes of reduced synaptic gain, some PScz data features imply NMDAR hypofunction. In rsEEG, increased g follows NMDAR antagonism (43), e.g., using ketamine (which also suppresses b) (44), or in NMDAR encephalitis (which also increases q) (15,45). In contrast, LSD and psilocybin do not increase q (46), and D2 antagonists potentiate a and b (47,48). The 40-Hz ASSR is sensitive to NMDAR function (49) but also cholinergic (50), dopaminergic (51) and serotonergic (52) manipulations; the latter do not affect MMN, however, which is quite specific to NMDAR function (11). Ketamine also reduces rsfMRI functional connectivity of IFG and auditory cortices (53). Antipsychotic dose covariates weakened the PScz MMN condition-specific effects (Figure 3F) but strengthened the overall MMN effects (Figure S4C); they also weakened the PScz rsfMRI effects, but similar rsfMRI effects emerged in unmedicated Rel (Figure 5). Overall, these findings resemble NMDAR hypofunction and seem unlikely to be medication induced. 

Several limitations are addressable. Given that pathophysiology is dynamic in PScz (1) and that subgroups may exist (54), larger datasets should be analyzed, containing more early-course (and preferably unmedicated) PScz. Notably, even the latter show reductions (d . 1) in cortical glutamate (55), consistent with the idea that pyramidal cell hypofunction—rather than disinhibition—is primary in PScz. DCM models with explicitly parameterized NMDA (and other) receptor conductances (15) can explore self-inhibition in more detail and across more cortical areas. 

In conclusion, we found consistently increased selfinhibition (i.e., diminished synaptic gain) in PScz, especially in frontal areas, but disinhibition—in auditory areas in particular—correlated with auditory perceptual abnormalities. Psychotic symptoms may therefore be caused by interneuronal downregulation that restores cortical excitation/inhibition balance in PScz. These complex processes may explain why successful glutamatergic treatments for PScz are elusive, and why such treatments may have narrow therapeutic windows (56) or depend on illness stage (57). 

## ACKNOWLEDGMENTS AND DISCLOSURES 

This work was supported by a Medical Research Council Skills Development Fellow (Grant No. MR/S007806/1 [to RAA]), a University College London Bogue Research Fellowship, the Academy of Medical Sciences 

(Grant No. AMS-SGCL13-Adams [to RAA]), the National Institute of Health Research (Grant No. CL-2013-18-003 [to RAA]), the National Institute for Health Research University College London Hospital Biomedical Research Centre (to RAA), Slovenian Research Agency (Grant Nos. J7-8275 and P30338 [to GR]), National Institutes of Health (Grant No. MH112746 [to JDM]), and the Wellcome Trust (Grant No. 088130/Z/09/Z [to KJF]). 

RAA conceived the project, conducted or supervised all analyses, and wrote the paper. DP and KT developed analysis code and conducted some analyses. LU, AM, AMH, LC, and JLJ assisted with analysis. AS, XMD, HS, and PK collected and curated the data. GR developed analysis code, assisted with analysis, and contributed to the paper. JDM contributed to the paper. KJF developed analysis code, assisted with analysis, and contributed to the paper. LEH collected the data and contributed to the paper. AA supervised the project and contributed to the paper. 

We are very grateful to numerous colleagues who provided guidance in dynamic causal modeling and statistics, including Vladimir Litvak, Peter Zeidman, Rosalyn Moran, Adeel Razi, Amirhossein Jafarian, Marta Garrido, and Jon Roiser. 

A previous version of this article was published as a preprint on medRxiv: https://doi.org/10.1101/2021.01.07.21249389. 

GR consults for and holds equity in RBNC Therapeutics. JLJ, JDM, and AA consult for RBNC (formerly BlackThorn Therapeutics) and are listed as coinventors on the following pending patent: Anticevic A, Murray JD, Ji JL: Systems and Methods for Neuro-Behavioral Relationships in Dimensional Geometric Embedding (N-BRIDGE), PCT International Application No. PCT/ US2119/022110, filed March 13, 2019. JDM holds stock in BlackThorn Therapeutics. LEH has received or plans to receive research funding or consulting fees on research projects from Mitsubishi, Your Energy Systems LLC, Neuralstem, Taisho, Heptares, Pfizer, Luye Pharma, Sound Pharma, Takeda, and Regeneron. AA is also a Scientific Advisory Board member for BlackThorn Therapeutics. All other authors report no biomedical financial interests or potential conflicts of interest. 

## ARTICLE INFORMATION 

From the Centre for Medical Image Computing and Artificial Intelligence (RAA, KT, AM, AMH), Institute of Cognitive Neuroscience (RAA, LU, LC), and Wellcome Centre for Human Neuroimaging (KJF), University College London; Centre for Mathematical Neuroscience and Psychology and Department of Psychology (DP), City University of London; Max Planck-UCL Centre for Computational Psychiatry and Ageing Research (RAA), London, United Kingdom; Department of Psychiatry (RAA, JLJ, JDM, AA), Yale University School of Medicine, New Haven, Connecticut; Picower Institute for Learning & Memory and Department of Brain and Cognitive Sciences (DP), Massachusetts Institute of Technology, Cambridge, Massachusetts; Department of Psychiatry (AS, HS, XMD, PK, LEH), Maryland Psychiatric Research Center, University of Maryland School of Medicine, Baltimore, Maryland; and Department of Psychology (GR), University of Ljubljana, Ljubljana, Slovenia. 

Address correspondence to Rick A. Adams, Ph.D., M.R.C.P., M.R.C.Psych., at rick.adams@ucl.ac.uk. 

Received Mar 31, 2021; revised and accepted Jul 29, 2021. Supplementary material cited in this article is available online at https:// doi.org/10.1016/j.biopsych.2021.07.024. 

## REFERENCES 

1. Krystal JH, Anticevic A, Yang GJ, Dragoi G, Driesen NR, Wang XJ, Murray JD (2017): Impaired tuning of neural ensembles and the pathophysiology of schizophrenia: A translational and computational neuroscience perspective. Biol Psychiatry 81:874–885. 

2. Stephan KE, Friston KJ, Frith CD (2009): Dysconnection in schizophrenia: From abnormal synaptic plasticity to failures of self-monitoring. Schizophr Bull 35:509–527. 

3. Lewis DA, Hashimoto T, Volk DW (2005): Cortical inhibitory neurons and schizophrenia. Nat Rev Neurosci 6:312–324. 

4. Chung DW, Fish KN, Lewis DA (2016): Pathological basis for deficient excitatory drive to cortical parvalbumin interneurons in schizophrenia. Am J Psychiatry 173:1131–1139. 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 213 

Biological Psychiatry 

Loss of Pyramidal Synaptic Gain in Schizophrenia 

5. Dienel SJ, Lewis DA (2019): Alterations in cortical interneurons and cognitive function in schizophrenia. Neurobiol Dis 131:104208. 

6. Hall J, Trent S, Thomas KL, O’Donovan MC, Owen MJ (2015): Genetic risk for schizophrenia: Convergence on synaptic pathways involved in plasticity. Biol Psychiatry 77:52–58. 

7. Poels EMP, Kegeles LS, Kantrowitz JT, Javitt DC, Lieberman JA, Abi-Dargham A, Girgis RR (2014): Glutamatergic abnormalities in schizophrenia: A review of proton MRS findings. Schizophr Res 152:325–332. 

8. Neill JC, Barnes S, Cook S, Grayson B, Idris NF, McLean SL, et al. (2010): Animal models of cognitive dysfunction and negative symptoms of schizophrenia: Focus on NMDA receptor antagonism. Pharmacol Ther 128:419–432. 

9. Slifstein M, van de Giessen E, Van Snellenberg J, Thompson JL, Narendran R, Gil R, et al. (2015): Deficits in prefrontal cortical and extrastriatal dopamine release in schizophrenia: A positron emission tomographic functional magnetic resonance imaging study. JAMA Psychiatry 72:316–324. 

10. Scarr E, Cowie TF, Kanellakis S, Sundram S, Pantelis C, Dean B (2009): Decreased cortical muscarinic receptors define a subgroup of subjects with schizophrenia. Mol Psychiatry 14:1017–1023. 

11. Umbricht D, Krljes S (2005): Mismatch negativity in schizophrenia: A meta-analysis. Schizophr Res 76:1–23. 

12. Thuné H, Recasens M, Uhlhaas PJ (2016): The 40-Hz auditory steadystate response in patients with schizophrenia: A meta-analysis. JAMA Psychiatry 73:1145–1153. 

13. Ranlund S, Adams RA, Díez Á, Constante M, Dutt A, Hall MH, et al. (2016): Impaired prefrontal synaptic gain in people with psychosis and their relatives during the mismatch negativity. Hum Brain Mapp 37:351–365. 

14. Stephan KE, Schlagenhauf F, Huys QJM, Raman S, Aponte EA, Brodersen KH, et al. (2017): Computational neuroimaging strategies for single patient predictions. Neuroimage 145:180–199. 

15. Symmonds M, Moran CH, Leite MI, Buckley C, Irani SR, Stephan KE, et al. (2018): Ion channels in EEG: Isolating channel dysfunction in NMDA receptor antibody encephalitis. Brain 141:1691–1702. 

16. Shaw AD, Hughes LE, Moran R, Coyle-Gilchrist I, Rittman T, Rowe JB (2021): In vivo assay of cortical microcircuitry in frontotemporal dementia: A platform for experimental medicine studies. Cereb Cortex 31:1837–1847. 

17. Friston KJ, Litvak V, Oswal A, Razi A, Stephan KE, van Wijk BCM, et al. (2016): Bayesian model reduction and empirical Bayes for group (DCM) studies. Neuroimage 128:413–431. 

18. Dima D, Frangou S, Burge L, Braeutigam S, James AC (2012): Abnormal intrinsic and extrinsic connectivity within the magnetic mismatch negativity brain network in schizophrenia: A preliminary study. Schizophr Res 135:23–27. 

19. Díez Á, Ranlund S, Pinotsis D, Calafato S, Shaikh M, Hall MH, et al. (2017): Abnormal frontoparietal synaptic gain mediating the P300 in patients with psychotic disorder and their unaffected relatives. Hum Brain Mapp 38:3262–3276. 

20. Shaw AD, Knight L, Freeman TCA, Williams GM, Moran RJ, Friston KJ, et al. (2020): Oscillatory, computational, and behavioral evidence for impaired GABAergic inhibition in schizophrenia. Schizophr Bull 46:345–353. 

21. Bastos-Leite AJ, Ridgway GR, Silveira C, Norton A, Reis S, Friston KJ (2015): Dysconnectivity within the default mode in firstepisode schizophrenia: A stochastic dynamic causal modeling study with functional magnetic resonance imaging. Schizophr Bull 41:144–153. 

22. Fogelson N, Litvak V, Peled A, Fernandez-del-Olmo M, Friston K (2014): The functional anatomy of schizophrenia: A dynamic causal modeling study of predictive coding. Schizophr Res 158:204–212. 

23. Boutros NN, Arfken C, Galderisi S, Warrick J, Pratt G, Iacono W (2008): The status of spectral EEG abnormality as a diagnostic test for schizophrenia. Schizophr Res 99:225–237. 

24. Puvvada KC, Summerfelt A, Du X, Krishna N, Kochunov P, Rowland LM, et al. (2018): Delta vs gamma auditory steady state synchrony in schizophrenia. Schizophr Bull 44:378–387. 

25. Spencer KM, Niznikiewicz MA, Nestor PG, Shenton ME, McCarley RW (2009): Left auditory cortex gamma synchronization and auditory hallucination symptoms in schizophrenia. BMC Neurosci 10:85. 

26. Spencer KM, Nestor PG, Perlmutter R, Niznikiewicz MA, Klump MC, Frumin M, et al. (2004): Neural synchrony indexes disordered perception and cognition in schizophrenia. Proc Natl Acad Sci U S A 101:17288–17293. 

27. Dzafic I, Larsen KM, Darke H, Pertile H, Carter O, Sundram S, Garrido MI (2021): Stronger top-down and weaker bottom-up frontotemporal connections during sensory learning are associated with severity of psychotic phenomena. Schizophr Bull 47:1039–1047. 

28. Wengler K, Goldberg AT, Chahine G, Horga G (2020): Distinct hierarchical alterations of intrinsic neural timescales account for different manifestations of psychosis. Elife 9:e56151. 

29. Merritt K, McGuire PK, Egerton A, 1H-MRS in Schizophrenia Investigators, Aleman A, Block W, et al. (2021): Association of age, antipsychotic medication, and symptom severity in schizophrenia with proton magnetic resonance spectroscopy brain glutamate level: A mega-analysis of individual participant-level data. JAMA Psychiatry 78:667–681. 

30. Narayanan B, O’Neil K, Berwise C, Stevens MC, Calhoun VD, Clementz BA, et al. (2014): Resting state electroencephalogram oscillatory abnormalities in schizophrenia and psychotic bipolar patients and their relatives from the bipolar and schizophrenia network on intermediate phenotypes study. Biol Psychiatry 76:456–465. 

31. Newson JJ, Thiagarajan TC (2018): EEG frequency bands in psychiatric disorders: A review of resting state studies. Front Hum Neurosci 12:521. 

32. Gao R, Peterson EJ, Voytek B (2017): Inferring synaptic excitation/inhibition balance from field potentials. Neuroimage 158:70–78. 

33. Peterson EJ, Rosen BQ, Campbell AM, Belger A, Voytek B (2017): 1/f neural noise is a better predictor of schizophrenia than neural oscillations. bioRxiv. https://doi.org/10.1101/113449. 

34. Grent-’t-Jong T, Gross J, Goense J, Wibral M, Gajwani R, Gumley AI, et al. (2018): Resting-state gamma-band power alterations in schizophrenia reveal E/I-balance abnormalities across illness-stages. Elife 7: e37799. 

35. Erickson MA, Ruffle A, Gold JM (2016): A meta-analysis of mismatch negativity in schizophrenia: From clinical risk to disease specificity and progression. Biol Psychiatry 79:980–987. 

36. Taylor JA, Larsen KM, Garrido MI (2020): Multi-dimensional predictions of psychotic symptoms via machine learning. Hum Brain Mapp 41:5151–5163. 

37. Hong LE, Summerfelt A, McMahon R, Adami H, Francis G, Elliott A, et al. (2004): Evoked gamma band synchronization and the liability for schizophrenia. Schizophr Res 70:293–302. 

38. Vierling-Claassen D, Siekmeier P, Stufflebeam S, Kopell N (2008): Modeling GABA alterations in schizophrenia: A link between impaired inhibition and altered gamma and beta range auditory entrainment. J Neurophysiol 99:2656–2671. 

39. Anticevic A, Hu X, Xiao Y, Hu J, Li F, Bi F, et al. (2015): Early-course unmedicated schizophrenia patients exhibit elevated prefrontal connectivity associated with longitudinal change. J Neurosci 35:267–286. 

40. Anticevic A, Cole MW, Repovs G, Murray JD, Brumbaugh MS, Winkler AM, et al. (2014): Characterizing thalamo-cortical disturbances in schizophrenia and bipolar illness. Cereb Cortex 24:3116–3130. 

41. Bygrave AM, Kilonzo K, Kullmann DM, Bannerman DM, Kätzel D (2019): Can N-methyl-D-aspartate receptor hypofunction in schizophrenia be localized to an individual cell type? Front Psychiatry 10:835. 

42. Stein H, Barbosa J, Rosa-Justicia M, Prades L, Morató A, GalanGadea A, et al. (2020): Reduced serial dependence suggests deficits in synaptic potentiation in anti-NMDAR encephalitis and schizophrenia. Nat Commun 11:4250. 

43. Lemercier CE, Holman C, Gerevich Z (2017): Aberrant alpha and gamma oscillations ex vivo after single application of the NMDA receptor antagonist MK-801. Schizophr Res 188:118–124. 

44. Rivolta D, Heidegger T, Scheller B, Sauer A, Schaum M, Birkner K, et al. (2015): Ketamine dysregulates the amplitude and connectivity of 

214 Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 

Biological Psychiatry 

## Loss of Pyramidal Synaptic Gain in Schizophrenia 

   - high-frequency oscillations in cortical-subcortical networks in humans: Evidence from resting-state magnetoencephalography-recordings. Schizophr Bull 41:1105–1114. 

45. Gitiaux C, Simonnet H, Eisermann M, Leunen D, Dulac O, Nabbout R, et al. (2013): Early electro-clinical features may contribute to diagnosis of the anti-NMDA receptor encephalitis in children. Clin Neurophysiol 124:2354–2361. 

46. Pallavicini C, Vilas MG, Villarreal M, Zamberlan F, Muthukumaraswamy S, Nutt D, et al. (2019): Spectral signatures of serotonergic psychedelics and glutamatergic dissociatives. Neuroimage 200:281–291. 

47. Ongini E, Bo P, Dionisotti S, Trampus M, Savoldi F (1992): Effects of remoxipride, a dopamine D-2 antagonist antipsychotic, on sleepwaking patterns and EEG activity in rats and rabbits. Psychopharmacology (Berl) 107:236–242. 

48. Sebban C, Zhang XQ, Tesolin-Decros B, Millan MJ, Spedding M (1999): Changes in EEG spectral power in the prefrontal cortex of conscious rats elicited by drugs interacting with dopaminergic and noradrenergic transmission. Br J Pharmacol 128:1045–1054. 

49. Sivarao DV (2015): The 40-Hz auditory steady-state response: A selective biomarker for cortical NMDA function. Ann N Y Acad Sci 1344:27–36. 

50. Sivarao DV, Frenkel M, Chen P, Healy FL, Lodge NJ, Zaczek R (2013): MK-801 disrupts and nicotine augments 40 Hz auditory steady state responses in the auditory cortex of the urethane-anesthetized rat. Neuropharmacology 73:1–9. 

51. Albrecht MA, Price G, Lee J, Iyyalol R, Martin-Iverson MT (2013): Dexamphetamine selectively increases 40 Hz auditory steady state response power to target and nontarget stimuli in healthy humans. J Psychiatry Neurosci 38:24–32. 

52. Nissen TD, Laursen B, Viardot G, l’Hostis P, Danjou P, Sluth LB, et al. (2020): Effects of vortioxetine and escitalopram on electroencephalographic recordings - A randomized, crossover trial in healthy males. Neuroscience 424:172–181. 

53. Adhikari BM, Dukart J, Hipp JF, Forsyth A, McMillan R, Muthukumaraswamy SD, et al. (2020): Effects of ketamine and midazolam on resting state connectivity and comparison with ENIGMA connectivity deficit patterns in schizophrenia. Hum Brain Mapp 41:767–778. 

54. Clementz BA, Sweeney JA, Hamm JP, Ivleva EI, Ethridge LE, Pearlson GD, et al. (2016): Identification of distinct psychosis biotypes using brain-based biomarkers. Am J Psychiatry 173:373– 384. 

55. Jeon P, Limongi R, Ford SD, Mackinley M, Dempster K, Théberge J, Palaniyappan L (2021): Progressive changes in glutamate concentration in early stages of schizophrenia: A longitudinal 7-tesla MRS study. Schizophr Bull Open 2:sgaa072. 

56. Javitt DC (2016): Bitopertin in schizophrenia: Glass half full? Lancet Psychiatry 3:1092–1093. 

57. Kinon BJ, Millen BA, Zhang L, McKinzie DL (2015): Exploratory analysis for a targeted patient population responsive to the metabotropic glutamate 2/3 receptor agonist pomaglumetad methionil in schizophrenia. Biol Psychiatry 78:754–762. 

58. Garrido MI, Kilner JM, Stephan KE, Friston KJ (2009): The mismatch negativity: A review of underlying mechanisms. Clin Neurophysiol 120:453–463. 

59. Shaw AD, Moran RJ, Muthukumaraswamy SD, Brealy J, Linden DE, Friston KJ, Singh KD (2017): Neurophysiologically informed markers of individual variability and pharmacological manipulation of human cortical gamma. Neuroimage 161:19–31. 

Biological Psychiatry January 15, 2022; 91:202–215 www.sobp.org/journal 215 

