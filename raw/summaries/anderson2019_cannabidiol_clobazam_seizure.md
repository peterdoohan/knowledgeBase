---
source_file: anderson2019_cannabidiol_clobazam_seizure.md
title: "Coadministered cannabidiol and clobazam: Preclinical evidence for both pharmacodynamic and pharmacokinetic interactions"
authors: Lyndsey L. Anderson, Nathan L. Absalom, Sarah V. Abelev, Ivan K. Low, Peter T. Doohan, Lewis J. Martin, Mary Chebib, Iain S. McGregor, Jonathon C. Arnold
year: 2019
journal: Epilepsia
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Using a Dravet syndrome mouse model and in vitro assays, this study demonstrates that the enhanced anticonvulsant efficacy of combined cannabidiol (CBD) and clobazam involves both a pharmacokinetic interaction (CBD inhibiting CYP-mediated clobazam metabolism) and a novel pharmacodynamic interaction (cooperative potentiation of GABAA receptor currents), and that CBD's intrinsic anticonvulsant activity is required for the combination to produce greater efficacy than clobazam alone.

---

### Background & motivation

CBD was FDA-approved as an adjunct treatment for Dravet syndrome and Lennox-Gastaut syndrome, but critics questioned whether its clinical efficacy is merely a pharmacokinetic artefact: CBD inhibits CYP3A4 and CYP2C19, thereby increasing plasma concentrations of co-administered clobazam and its active metabolite N-desmethylclobazam (N-CLB). Clinical trials could not resolve this because they lacked a CBD-without-clobazam control group, and subgroup analyses were confounded by other AED co-medications. This study used a controlled preclinical approach — combining in vitro enzyme assays, mouse pharmacokinetics, a genetic Dravet syndrome mouse model (Scn1a+/−), and Xenopus oocyte electrophysiology — to disentangle pharmacokinetic from pharmacodynamic contributions.

---

### Methods

- **In vitro pharmacokinetics**: CBD inhibition of CYP3A4-mediated clobazam metabolism and CYP2C19-mediated N-CLB metabolism characterised using Supersomes expressing human CYP isoforms; Ki values determined from substrate-velocity curves.
- **In vivo pharmacokinetics**: Wildtype mice administered clobazam ± CBD (12 mg/kg, i.p.); plasma and brain concentration-time profiles for clobazam and N-CLB generated using a two-compartment model.
- **Hyperthermia-induced seizure model**: Scn1a+/− mice challenged with graduated thermal stimulus to elicit GTCS; temperature threshold for seizure used as outcome. Two CBD dose conditions tested: sub-anticonvulsant (12 mg/kg) and anticonvulsant (100 mg/kg), each combined with a range of clobazam doses (0.1–10 mg/kg, i.p.).
- **Spontaneous seizure and survival model**: Scn1a+/− mice primed with a single hyperthermia-induced seizure at P18, then treated with clobazam, CBD, or combination via chow for 60 h; spontaneous GTCS frequency and survival tracked.
- **GABAA receptor electrophysiology**: Two-electrode voltage-clamp in Xenopus oocytes expressing concatenated α1β2γ2 GABAA receptors; concentration-response curves and paired drug applications for CBD, clobazam, and N-CLB, individually and in combination.

---

### Key findings

- CBD potently inhibited CYP3A4-mediated clobazam metabolism (Ki = 139 nmol/L) and less potently inhibited CYP2C19-mediated N-CLB metabolism (Ki = 2.6 μmol/L); Ki values are within the range of plasma CBD concentrations seen in epilepsy patients (318–2544 nmol/L).
- CBD (12 mg/kg) prolonged clobazam plasma half-life ~5-fold (15 → 78 min) and increased brain AUC ~6.5-fold; N-CLB brain AUC increased ~2.7-fold. Brain-to-plasma ratio of N-CLB rose from 2.2 to 3.6, suggesting CBD also inhibits N-CLB efflux from the brain.
- A sub-anticonvulsant dose of CBD (12 mg/kg) did not augment clobazam's anticonvulsant effect against hyperthermia-induced seizures in Scn1a+/− mice despite producing a significant pharmacokinetic interaction — demonstrating that the pharmacokinetic interaction alone is not sufficient to enhance anticonvulsant efficacy.
- An anticonvulsant dose of CBD (100 mg/kg) combined with clobazam (1 mg/kg) significantly raised the thermal seizure threshold above either drug alone (p = 0.0036 vs clobazam; p < 0.0001 vs CBD or vehicle).
- In the spontaneous seizure/survival experiment, neither CBD nor clobazam monotherapy significantly improved survival vs controls (p = 0.053 and p = 0.075 respectively), but CBD + clobazam co-treatment significantly improved survival (p = 0.0033).
- At GABAA receptors, CBD (max modulation: +106%, EC50 = 2.4 μmol/L) and clobazam (max: +369%, EC50 = 662 nmol/L) each individually potentiated GABA-evoked currents; co-application of CBD (10 μmol/L) + clobazam (10 μmol/L) produced significantly greater potentiation than either alone (289 ± 54% vs 204 ± 33% for clobazam, p = 0.049; vs 82 ± 11% for CBD, p = 0.016). Similarly, CBD + N-CLB exceeded either alone. The interaction was additive, not synergistic.

---

### Computational framework

Not applicable. The paper is a pharmacological study with no explicit computational or mathematical framework. The results are mechanistically relevant to quantitative pharmacology (pharmacokinetic modelling, enzyme kinetics) but no formal computational model is developed. The Ki values and pharmacokinetic parameters quantify drug interactions but do not constitute a computational model of the system.

---

### Prevailing model of the system under study

The paper's introduction presents two competing views: (1) CBD has genuine intrinsic anticonvulsant activity, supported by preclinical data and Phase III trials; (2) CBD's apparent clinical efficacy is a pharmacokinetic epiphenomenon — CBD raises clobazam and N-CLB plasma levels, and it is this increase in benzodiazepine exposure that accounts for seizure reduction. The prevailing mechanistic model for Dravet syndrome is that loss-of-function SCN1A mutations preferentially impair NaV1.1-dependent firing of GABAergic interneurons, leading to net disinhibition and hyperexcitability — which is why positive allosteric modulators of GABAA receptors (including benzodiazepines such as clobazam) are therapeutically effective. The introduction also flags a prior finding from the same group that CBD itself is a weak positive allosteric modulator of GABAA receptors, suggesting a possible pharmacodynamic interaction with clobazam at the receptor level.

---

### What this paper contributes

The study establishes that pharmacokinetic interaction alone — although real and quantitatively substantial — does not account for the enhanced anticonvulsant effect of CBD + clobazam co-treatment: a sub-anticonvulsant dose of CBD that still elevated clobazam plasma levels failed to augment anticonvulsant efficacy, whereas an intrinsically anticonvulsant dose did. This rules out the pure pharmacokinetic confound explanation and demands a pharmacodynamic account. The paper provides the first direct electrophysiological evidence for that pharmacodynamic interaction: CBD and clobazam co-applied to GABAA receptors produce greater inhibitory current potentiation than either drug alone, acting via distinct binding sites (CBD at a non-benzodiazepine site). Beyond seizure suppression, the combination also significantly improved survival in Scn1a+/− mice — a clinically important finding for SUDEP risk — that neither monotherapy achieved. The overall picture is that both pharmacokinetic and pharmacodynamic mechanisms contribute to CBD + clobazam efficacy in Dravet syndrome.

---

### Brain regions & systems

Not the central focus of this paper. The study operates at the level of systemic pharmacology (plasma/brain PK), whole-animal seizure phenotypes, and isolated receptor preparations. The following are relevant at the mechanistic level implied by the Dravet syndrome model:

- **GABAergic interneurons (cortex/hippocampus)** — the functional target of NaV1.1 loss in Scn1a+/− mice; impaired interneuron excitability underlies seizure susceptibility and is the proposed site of therapeutic benefit from GABAA PAMs.
- **GABAA receptors (α1β2γ2 subunit composition)** — characterised in vitro as the pharmacodynamic locus of CBD-clobazam interaction; expressed throughout cortical and subcortical circuits.

---

### Mechanistic insight

The paper partially meets the bar. It proposes a specific algorithm (cooperative positive allosteric modulation of GABAA receptors by CBD and clobazam at distinct binding sites) and provides direct electrophysiological evidence (two-electrode voltage clamp in oocytes) supporting that mechanism at the receptor level. However, the evidence is from a heterologous expression system (Xenopus oocytes), not from native neural tissue, recordings, or imaging in the Scn1a+/− mouse. The in vivo anticonvulsant experiments establish that intrinsic CBD efficacy is required for combination benefit, but cannot isolate whether the GABAA pharmacodynamic interaction, CBD's GPR55 antagonism, or other multimodal mechanisms drive the in vivo effect. There is no neural recording or imaging linking the GABAA interaction to specific activity patterns in the mouse brain.

Mapping what the paper does establish:
- **Computational**: The brain must maintain inhibitory tone in circuits where GABAergic interneurons are compromised by NaV1.1 loss; increasing GABAA receptor-mediated inhibition compensates for reduced interneuron firing.
- **Algorithmic**: CBD and clobazam each independently increase the gain of GABA-mediated inhibitory currents via distinct allosteric sites on GABAA receptors; their co-application produces additive (not synergistic) current enhancement, consistent with independent site occupancy.
- **Implementational**: Partly addressed — the paper identifies CBD's binding site as distinct from the classical benzodiazepine site on GABAA receptors, and notes that clobazam/N-CLB have higher affinity for α2- than α1-containing GABAA complexes, but specific cell types, circuit connectivity, or biophysical implementation in native brain tissue are not characterised here.

---

### Limitations & open questions

- The in vivo experiments cannot formally test synergy (isobolographic analysis requires ED50 determination for both drugs, which was unattainable because CBD does not produce a classical dose-response in Scn1a+/− mice).
- The anticonvulsant dose of CBD used in mice (100 mg/kg, i.p.; plasma ~1800 ng/mL) exceeds the plasma concentrations typically seen in human patients (100–800 ng/mL), raising translational questions about whether pharmacodynamic interactions occur at clinically relevant CBD concentrations.
- The GABAA electrophysiology used a single concatenated receptor subunit combination (α1β2γ2) in a heterologous system; results may differ across GABAA subunit compositions expressed in native brain.
- The study cannot exclude other CBD mechanisms (GPR55 antagonism, TRPV1 activation, Nav1.6 modulation) as major contributors to the in vivo interaction with clobazam.
- Effects on spontaneous seizure frequency for the CBD + clobazam combination vs clobazam alone were non-significant (16% vs 28%), likely due to a floor effect; a larger study would be needed to resolve this.
- The survival benefit of combination therapy in Dravet syndrome has no direct clinical analogue because SUDEP endpoints in trials require years of follow-up.

---

### Connections & keywords

**Key citations**:
- Devinsky et al. (2017) — Phase III CBD trial in Dravet syndrome (N Engl J Med)
- Geffrey et al. (2015) — clinical CBD-clobazam pharmacokinetic interaction in children with refractory epilepsy
- Gaston et al. (2017) — CBD interactions with antiepileptic drugs
- Kaplan et al. (2017) — CBD attenuates seizures in Scn1a+/− mice via GPR55 antagonism (PNAS)
- Bakas et al. (2017) — CBD as positive allosteric modulator of GABAA receptors
- Hawkins et al. (2017) — Scn1a+/− mouse model used as experimental platform

**Named models or frameworks**:
- Scn1a+/− mouse model of Dravet syndrome
- CYP3A4 / CYP2C19 enzyme inhibition kinetics (Ki determination)
- Xenopus oocyte two-electrode voltage-clamp assay
- Two-compartment pharmacokinetic model

**Brain regions**:
- GABAergic interneurons (cortex, hippocampus — implied by Dravet pathophysiology)
- GABAA receptor (α1β2γ2 subunit composition)

**Keywords**:
- cannabidiol, clobazam, Dravet syndrome, SCN1A, GABAA receptor positive allosteric modulation, CYP3A4 inhibition, CYP2C19 inhibition, pharmacokinetic drug interaction, pharmacodynamic interaction, N-desmethylclobazam, hyperthermia-induced seizure, SUDEP
