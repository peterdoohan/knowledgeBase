---
source_file: adams2021_pyramidal_synaptic_gain.md
paper_id: adams2021_pyramidal_synaptic_gain
title: "Computational Modeling of Electroencephalography and Functional Magnetic Resonance Imaging Paradigms Indicates a Consistent Loss of Pyramidal Cell Synaptic Gain in Schizophrenia"
authors:
  - "Rick A. Adams"
  - "Dimitris Pinotsis"
  - "Konstantinos Tsirlis"
  - "Leonhardt Unruh"
  - "Aashna Mahajan"
  - "Ana Montero Horas"
  - "Laura Convertino"
  - "Ann Summerfelt"
  - "Hemalatha Sampath"
  - "Xiaoming Michael Du"
  - "Peter Kochunov"
  - "Jie Lisa Ji"
  - "Grega Repovs"
  - "John D. Murray"
  - "Karl J. Friston"
  - "L. Elliot Hong"
  - "Alan Anticevic"
year: 2022
journal: "Biological Psychiatry"
paper_type: computational
contribution_type: empirical
species:
  - human
methods:
  - fmri
  - dynamic_causal_modelling
  - parametric_empirical_bayes
  - computational_modeling
brain_regions:
  - superior_temporal_gyrus
  - inferior_frontal_gyrus
  - primary_auditory_cortex
frameworks:
  - bayesian_inference
keywords:
  - schizophrenia_synaptic_gain
  - pyramidal_cell_self_inhibition
  - dynamic_causal_modelling
  - nmda_receptor_hypofunction
  - mismatch_negativity
  - auditory_steady_state_response
  - resting_state_eeg_spectral_abnormalities
  - excitation_inhibition_balance
  - cortical_microcircuit
  - interneuron_disinhibition
  - parametric_empirical_bayes
  - computational_psychiatry_biomarkers
  - computational
  - modeling
  - electroencephalography
  - functional
  - magnetic
  - resonance
  - imaging
  - paradigms
---

### One-line summary

Across four independent neuroimaging paradigms (resting EEG, MMN, 40-Hz ASSR, rsfMRI), dynamic causal modelling consistently identifies increased self-inhibition of pyramidal cells — reflecting diminished synaptic gain — as the core circuit abnormality in schizophrenia, while psychotic symptoms specifically relate to secondary disinhibition in auditory and frontal areas.

---

### Background & motivation

Reduced synaptic gain is hypothesised to be a fundamental pathophysiology of schizophrenia, most likely mediated by NMDA receptor hypofunction, but it has been difficult to measure in vivo. A critical unresolved question is whether the primary deficit lies on pyramidal cells or on inhibitory interneurons, since loss of cortical interneuron markers in postmortem tissue could reflect either primary interneuron pathology or a compensatory response to weakened pyramidal drive. Indirect measures (MRS, PET) provide limited mechanistic resolution, and prior DCM studies have used single paradigms with modest samples, leaving the across-paradigm generality of any parameter change uncertain. This paper addresses both the locus question (pyramidal vs. interneuron) and the symptoms question by applying DCM to four paradigms simultaneously in a well-powered sample.

---

### Methods

- **Participants**: People with schizophrenia diagnoses (PScz, n = 108), first-degree relatives (Rel, n = 57), and healthy controls (Con, n = 107); groups well matched for age, sex, and smoking.
- **Neuroimaging paradigms**: Resting-state EEG (rsEEG), auditory mismatch negativity (MMN; duration-deviant oddball), 40-Hz auditory steady-state response (ASSR; 40-Hz click train), and resting-state fMRI (rsfMRI).
- **DCM model**: The canonical microcircuit model (neural mass model) containing superficial pyramidal (sp), deep pyramidal (dp), inhibitory interneuron (ii), and spiny stellate (ss) populations was used for EEG paradigms. A simpler neuronal model retaining inhibitory self-connections was used for rsfMRI.
- **Model inversion and selection**: For rsEEG, five plausible parameter-change models were simulated and compared against observed group spectral differences. For MMN and ASSR, subject-specific DCM parameters were estimated and Bayesian model comparison identified the best model structure. For rsfMRI, DCM was fitted to the MMN source network (bilateral A1, STG/A4, IFG/area 44).
- **Group and individual-difference analysis**: Parametric Empirical Bayes (PEB) was used to assess group effects (PScz vs. Con, Rel vs. Con, PScz vs. Rel) and symptom correlations (BPRS positive/negative symptoms, auditory perceptual abnormality state and trait scores).
- **Covariates**: Age, sex, smoking, and chlorpromazine-equivalent dose were tested as covariates throughout.

---

### Key findings

- **rsEEG**: PScz showed increased theta (Z = 2.63, p_corr = .035), decreased beta (Z = −2.77, p_corr = .022), and increased gamma (Z = 2.58, p_corr = .040) power. Of five candidate models, only increased superficial pyramidal self-inhibition (Model 5) reproduced all three band changes simultaneously.
- **MMN**: MMN amplitude was reduced in both PScz (cluster p_FWE = .010) and Rel (cluster p_FWE = .011). PEB indicated that the deviant–standard contrast difference in PScz was best explained by increased self-inhibition in bilateral IFG (p > .99 right IFG, p > .95 left IFG).
- **40-Hz ASSR**: PScz showed reduced gamma power and reduced peak frequency (mean 39.5 vs. 40.2 Hz; p_corr = .016). A genetic-risk effect (PScz+Rel > Con) was reduced sp-to-ii connectivity (p > .99); a diagnosis-specific effect (PScz > Rel) was increased sp self-inhibition in bilateral A1 (both p > .99).
- **rsfMRI**: PScz showed increased self-inhibition in left (p > .99) and right (p > .95) IFG. Relatives showed a similar pattern in bilateral IFG (both p > .95), though this was confounded by age.
- **Symptom correlations**: Across three paradigms (40-Hz ASSR, MMN, rsfMRI), auditory perceptual abnormalities within PScz were consistently associated with disinhibition (decreased self-inhibition) in auditory areas (A1, STG) and left IFG (Broca area). BPRS positive symptoms in rsfMRI related to disinhibition throughout the auditory-frontal network; negative symptoms related to temporal disinhibition specifically.
- **Cross-paradigm pattern**: Increased self-inhibition (reduced pyramidal gain) was the dominant group effect across all four modalities; disinhibition was the dominant symptom correlate within PScz — opposing effects in the same parameters.

---

### Computational framework

The paper uses **dynamic causal modelling (DCM)** with a canonical cortical microcircuit neural mass model. The core formalism represents each cortical area as a set of interacting neural mass populations (superficial pyramidal, deep pyramidal, inhibitory interneuron, spiny stellate), connected by excitatory and inhibitory synaptic coupling parameters. Self-inhibitory parameters within each population encode **synaptic gain** — the sensitivity of postsynaptic population responses to inputs. Greater self-inhibition corresponds to reduced gain, operationalising NMDA receptor hypofunction as a loss of pyramidal cell responsiveness.

Group and individual differences in DCM parameters are estimated via **Parametric Empirical Bayes (PEB)**, a hierarchical Bayesian framework that uses group-level posteriors to regularise subject-level fits and supports Bayesian model comparison across nested hypotheses. The framework can explain both evoked (MMN, ASSR) and induced/spontaneous (rsEEG, rsfMRI) responses in terms of the same biophysical parameters, enabling cross-paradigm inference.

---

### Prevailing model of the system under study

Before this paper, two competing hypotheses about the primary synaptic locus in schizophrenia were active in the field. The dominant view (Krystal et al. 2017; Stephan et al. 2009) held that NMDA receptor hypofunction reduces synaptic gain primarily on pyramidal cells. A competing account (Lewis et al. 2005) attributed cortical circuit disruption to primary pathology of GABAergic interneurons, supported by postmortem evidence of lost interneuron markers. The paper notes that recent work suggests interneuron marker loss may be activity-dependent — a consequence of weaker pyramidal drive — rather than a primary pathology. Electrophysiological biomarkers (MMN reduction, 40-Hz ASSR reduction) were known to be robust group differences in schizophrenia and were linked to reduced synaptic gain and diminished contextual modulation, but these were not direct indices of gain and had not been reconciled under a single mechanistic model. Prior DCM studies had found "cortical disinhibition" in EEG and fMRI, consistent with interneuron downregulation, but with small samples and single paradigms, and without resolving whether disinhibition was primary or secondary.

---

### What this paper contributes

The paper provides the first multi-paradigm, large-sample DCM demonstration that a single parameter change — increased self-inhibition (reduced gain) of superficial pyramidal cells — accounts for the canonical EEG and fMRI group differences in schizophrenia across four independent experimental contexts. This strongly favours the hypothesis of primary pyramidal cell synaptic gain loss over primary interneuron pathology. The paper also resolves the apparent contradiction between group-level cortical inhibition and the observation of disinhibition in hallucinating patients: these represent opposing processes in the same circuit, consistent with allostatic interneuron downregulation compensating for reduced pyramidal gain. The finding that psychotic symptoms (especially positive symptoms and auditory perceptual abnormalities) track with disinhibition specifically suggests that symptom generation depends on this secondary compensatory rebalancing, not on the primary gain deficit itself. This has implications for glutamatergic treatment strategies, potentially explaining why they have narrow therapeutic windows and stage-dependent efficacy.

---

### Brain regions & systems

- **Primary auditory cortex (A1)** — shows increased pyramidal self-inhibition in the 40-Hz ASSR (PScz vs. Rel); also the site of disinhibition correlating with auditory perceptual abnormalities and positive symptoms in rsfMRI and ASSR.
- **Superior temporal gyrus (STG)** — a node in the MMN network; disinhibition here correlates with auditory perceptual state scores and positive symptoms in rsfMRI.
- **Inferior frontal gyrus (IFG) / Broca area (left IFG)** — shows increased pyramidal self-inhibition in PScz across MMN (bilateral) and rsfMRI (bilateral); left IFG disinhibition specifically correlates with auditory perceptual abnormalities in both MMN and rsfMRI. Broca area disinhibition is flagged as particularly relevant to hallucinations.
- **Cortical microcircuit (generic)** — the biophysical model applies across all areas; the superficial pyramidal cell population is the primary locus of the schizophrenia effect in EEG paradigms.

---

### Mechanistic insight

The paper meets both criteria for this section. It formalises an algorithm (reduced pyramidal self-inhibitory gain leading to allostatic interneuron downregulation and consequent disinhibition) and provides multi-modal neural data (EEG/fMRI across four paradigms) that specifically support this account over the alternative of primary interneuron pathology.

**Computational level**: The brain maintains excitation/inhibition balance in cortical circuits. In schizophrenia, a primary loss of synaptic gain on pyramidal cells (likely via NMDA receptor hypofunction) disrupts this balance, triggering a compensatory reduction in interneuron activity to restore the ratio — at the cost of destabilised circuit dynamics that manifest as psychotic symptoms.

**Algorithmic level**: Self-inhibitory connections on superficial pyramidal cells parameterise their gain — how strongly they respond to inputs. Increased self-inhibition reduces this gain, attenuating prediction-error signals (MMN) and gamma oscillations (ASSR) globally. Separately, decreased interneuron-mediated inhibition (disinhibition) constitutes a distinct circuit state that co-varies with psychotic symptoms within the PScz group. PEB analyses dissociate these two effects statistically across multiple paradigms.

**Implementational level**: The paper links the pyramidal self-inhibition parameter specifically to superficial pyramidal cells in the canonical microcircuit, and infers that NMDA receptor hypofunction is the most likely biological substrate, based on convergence of the EEG spectral signature with known effects of NMDAR antagonists (ketamine, MK-801) and NMDAR encephalitis. The disinhibition effect is linked to interneuron downregulation, consistent with postmortem evidence of activity-dependent loss of interneuron markers driven by weaker pyramidal input.

**Bonus**: The implementational account is grounded in specific cell types (superficial vs. deep pyramidal cells, inhibitory interneurons, spiny stellate cells) and specific receptor systems (NMDA, D1 dopamine, muscarinic), providing a cell-type-resolved mechanistic picture.

---

### Limitations & open questions

- The sample predominantly comprised chronically ill, medicated PScz; antipsychotic dose covariates attenuated some effects (notably MMN condition-specific effects and rsfMRI IFG self-inhibition). Early-course and unmedicated samples are needed.
- Within-subject correlations of self-inhibition parameters across paradigms were weak, suggesting paradigm-specific variance not fully captured by the cross-paradigm narrative.
- The self-inhibition parameter in the neural mass model is not uniquely attributable to a single biophysical mechanism; it could reflect NMDA receptor hypofunction, reduced dopaminergic/muscarinic modulation, or other factors reducing gain.
- The rsfMRI DCM uses a simpler model lacking full microcircuit resolution, limiting direct comparability with EEG microcircuit parameters.
- Results for first-degree relatives were inconsistent across paradigms (no effects in MMN PEB, reduced self-inhibition in ASSR, increased IFG self-inhibition in rsfMRI confounded by age), preventing firm conclusions about familial transmission of the circuit phenotype.
- Global signal regression was required for some rsfMRI results, introducing dependency on a contested preprocessing choice.
- Open question: Why do glutamatergic treatments for schizophrenia have narrow therapeutic windows and stage-dependent efficacy? The allostatic compensation model predicts that restoring pyramidal gain without addressing interneuron downregulation (or vice versa) may not suffice.

---

### Connections & keywords

**Key citations**:
- Krystal et al. (2017) — pyramidal gain loss hypothesis
- Stephan, Friston & Frith (2009) — dysconnection in schizophrenia
- Lewis, Hashimoto & Volk (2005) — cortical inhibitory neuron hypothesis
- Umbricht & Krljes (2005) — MMN meta-analysis in schizophrenia
- Thuné, Recasens & Uhlhaas (2016) — 40-Hz ASSR meta-analysis in schizophrenia
- Friston et al. (2016) — parametric empirical Bayes for group DCM
- Ranlund et al. (2016) — impaired prefrontal synaptic gain in psychosis (MMN DCM)
- Dienel & Lewis (2019) — interneuron alterations in schizophrenia
- Wengler et al. (2020) — intrinsic neural timescales and psychosis (A1 rsfMRI)

**Named models or frameworks**:
- Dynamic Causal Modelling (DCM)
- Canonical cortical microcircuit (neural mass model)
- Parametric Empirical Bayes (PEB)
- Mismatch negativity (MMN) paradigm
- 40-Hz auditory steady-state response (ASSR) paradigm
- Glasser parcellation (for rsfMRI ROI definition)

**Brain regions**:
- Primary auditory cortex (A1)
- Superior temporal gyrus (STG)
- Inferior frontal gyrus (IFG) / Broca area

**Keywords**:
- schizophrenia synaptic gain
- pyramidal cell self-inhibition
- dynamic causal modelling
- NMDA receptor hypofunction
- mismatch negativity
- auditory steady-state response
- resting-state EEG spectral abnormalities
- excitation-inhibition balance
- cortical microcircuit
- interneuron disinhibition
- parametric empirical Bayes
- computational psychiatry biomarkers
