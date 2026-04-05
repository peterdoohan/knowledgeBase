---
source_file: mccartney2022_cannabidiol_driving.md
title: "Effects of cannabidiol on simulated driving and cognitive performance: A dose-ranging randomised controlled trial"
authors: Danielle McCartney, Anastasia S Suraev, Peter T Doohan, Christopher Irwin, Richard C Kevin, Ronald R Grunstein, Camilla M Hoyos, Iain S McGregor
year: 2022
journal: Journal of Psychopharmacology
paper_type: empirical
contribution_type: empirical
---

### One-line summary

A dose-ranging RCT (15, 300, and 1500 mg oral CBD) found that acute oral cannabidiol does not impair simulated driving performance or cognitive function, and does not induce feelings of intoxication, in healthy adults.

---

### Background & motivation

Cannabidiol (CBD) is increasingly consumed via prescription and over-the-counter products for conditions including anxiety, epilepsy, and chronic pain. Unlike THC, CBD is widely considered non-intoxicating, but its effects on safety-sensitive tasks such as driving had not been systematically tested across a clinically relevant dose range via oral administration — the most common route for prescribed and nutraceutical products. Only one prior study had examined CBD's effects on driving (Arkell et al., 2020), using a low dose of vaporised CBD; the pharmacokinetics of oral CBD differ substantially from vaporised CBD (later, lower peak concentrations), and therapeutic doses can be much higher (up to ~1500 mg/day). This trial aimed to fill that gap using a rigorous, non-inferiority design.

---

### Methods

- **Design**: Randomised, double-blind, placebo-controlled, four-way crossover trial. Sessions separated by ≥7-day washout.
- **Participants**: n = 17 healthy adults (10M/7F; median age ~28 years), licensed drivers who had not used cannabis in ≥3 months.
- **Treatments**: Oral synthetic CBD at 15, 300, or 1500 mg, or placebo (MCT oil), co-administered with a high-fat supplement to enhance bioavailability.
- **Driving assessment**: Fixed-base driving simulator with a two-part scenario: (1) a ~7-min car-following (CF) component and (2) a ~25-min standard highway/rural component. Drives completed at ~45–75 min (Drive 1) and ~210–240 min (Drive 2) post-treatment.
- **Primary outcome**: Standard deviation of lateral position (SDLP) — a well-validated index of vehicular control — analysed via non-inferiority testing (non-inferiority margin Δ = Cohen's d_z = 0.50, equivalent to impairment at 0.05% BAC).
- **Cognitive battery**: DSST, Divided Attention Task (DAT), PSAT, DRUID app, Psychomotor Vigilance Task (PVT).
- **Other measures**: Subjective experiences (VAS: stoned, sedated, alert, anxious, sleepy; STAI-S; driving self-efficacy); plasma CBD and metabolite concentrations (LC-MS/MS); cardiovascular parameters.

---

### Key findings

- **Driving (primary outcome)**: Non-inferiority to placebo was established on all three CBD doses during the standard component of Drive 1 and the CF component of Drive 2. CBD-15 and CBD-1500 were also non-inferior during the standard component of Drive 2. Remaining comparisons (CF at Drive 1; CBD-300 on standard Drive 2) were inconclusive (95% CIs included both 0 and 0.50), likely reflecting insufficient power rather than impairment — average SDLP changes (+1.0–1.4 cm) were well below those typically seen with intoxicating drugs (~2.5 cm) or THC (~3.9 cm in the same simulator).
- **Cognition**: No dose impaired performance on DSST, DAT hits/response time, PSAT, PVT, or DRUID. A treatment effect on DAT tracking error showed less error on CBD-300 and CBD-1500 than CBD-15, with no significant difference from placebo for any dose; authors attribute this to chance (Type II error or noise across 10 outcome measures).
- **Subjective experiences**: No dose induced feelings of being stoned, sedated, or intoxicated. Anxiousness ratings were marginally lower on CBD-300 and CBD-1500 than on placebo and CBD-15 (~5 mm VAS), consistent with anxiolytic effects at higher doses.
- **Treatment blinding**: Participants correctly identified their treatment on only 16% of occasions, confirming successful blinding.
- **Plasma pharmacokinetics**: CBD and metabolites (7-COOH-CBD, 7-OH-CBD, 6-OH-CBD) were detected in plasma up to ≥29 days after a 1500 mg dose in 12/17 participants during their placebo session, demonstrating unexpectedly prolonged persistence — a novel and unreported pharmacokinetic finding. Residual concentrations were low (mean ~4.7 ng/mL) and comparable to peak concentrations on the 15 mg dose; no substantial impact on driving outcomes was detected.
- **No THC detected**: Δ9-THC and metabolites were absent in all included participants.

---

### Computational framework

Not applicable. The paper uses a statistical non-inferiority framework rather than a computational model of cognition or behaviour. The primary analysis computes Cohen's d_z effect sizes with 95% CIs and evaluates whether the upper CI falls below a pre-specified margin (Δ = 0.50). Secondary outcomes use linear mixed-effects models. These methods constrain dose–response models of CBD's effects on psychomotor function and could inform pharmacokinetic–pharmacodynamic (PK-PD) modelling of CBD's CNS effects, but no such model is developed here.

---

### Prevailing model of the system under study

The paper's introduction frames CBD as a "non-intoxicating" cannabinoid whose CNS effects are minimal compared to THC. The prevailing working model is that CBD does not act on the CB1 receptors responsible for THC-induced impairment, and therefore should not degrade performance on safety-sensitive tasks even at high doses. However, as the authors note, this assumption was empirically underdeveloped for the oral route and across the broad dose range used therapeutically. The existing evidence base at the time consisted primarily of cognitive battery studies and a single on-road driving study using low-dose vaporised CBD. The paper situates itself as providing the first test of oral, dose-ranging CBD against a driving benchmark calibrated to a legal impairment standard.

---

### What this paper contributes

The results largely confirm and extend the prevailing view that CBD is non-impairing: the majority of non-inferiority comparisons were established, and no dose produced subjective intoxication or cognitive impairment. The contribution is twofold. First, it provides the first dose-ranging evidence (15–1500 mg oral) that CBD is unlikely to impair simulated driving even at doses used in psychiatric and neurological treatment — substantially strengthening the evidence base for the safety of therapeutic CBD use by drivers. Second, it documents a novel pharmacokinetic observation: that a single 1500 mg oral dose can produce detectable residual plasma CBD concentrations for at least 4 weeks, raising questions about appropriate washout periods in future trials and the long-term accumulation of CBD with chronic dosing.

---

### Brain regions & systems

Not applicable. The paper is a behavioural pharmacology trial with no neuroimaging, electrophysiology, or direct anatomical focus. The level of analysis is at the systems/behavioural level: whole-organism psychomotor performance, cognitive function, and subjective state as proxies for CNS drug action.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight. It provides no neural data (no imaging, no recordings, no pharmacological dissection of mechanism) and does not formalise an algorithm for how CBD acts on the CNS to produce (or fail to produce) impairment. It establishes behavioural and pharmacokinetic facts consistent with CBD's non-impairing profile but does not distinguish between competing mechanistic accounts (e.g., CB1 receptor non-engagement, serotonergic modulation, anxiety reduction without psychomotor effect). The results constrain the space of plausible mechanisms — particularly ruling out a direct psychomotor-depressant action of CBD at therapeutic doses — but do not resolve the mechanism itself.

---

### Limitations & open questions

- **Underpowered**: Target sample of n = 27 was not reached (final n = 17) due to COVID-19 research suspension; this inflated CI widths, leaving several comparisons inconclusive rather than confirmed non-inferior.
- **Residual CBD at baseline**: 12/17 participants had detectable CBD and metabolites during their placebo session following prior high-dose CBD administration; though impact on outcomes appeared negligible, it complicates interpretation of the placebo condition.
- **High-fat supplement**: Co-administration with a high-fat supplement to boost bioavailability did not appear to elevate plasma CBD concentrations above expected fasted levels; the PK profile was highly variable and Cmax could not be reliably estimated.
- **Simulated (not on-road) driving**: External validity to real road conditions remains to be established, though the simulator has demonstrated sensitivity to THC.
- **Single acute dose**: Chronic CBD use and its longer-term accumulation in adipose tissue are unstudied — the pharmacokinetic finding of prolonged persistence signals this as a priority for future research.
- **Inconclusive CF Drive 1 results**: The car-following component at ~45–75 min post-treatment was inconclusive for all doses; it is unknown whether CBD has phasic early effects that a larger sample might detect.
- **Pharmacological activity of CBD metabolites** (7-COOH-CBD, 7-OH-CBD) in humans is not established.
- **Population**: Healthy adults with no current cannabis use; generalisability to patient populations chronically using CBD for medical conditions is uncertain.

---

### Connections & keywords

**Key citations**:
- Arkell et al. (2020) — JAMA RCT of vaporised CBD and THC on on-road driving (single prior driving study, key comparator)
- McCartney et al. (2020) — Published protocol for this trial
- Millar et al. (2019) — Systematic review of CBD dosing in clinical populations
- Taylor et al. (2018) — Phase I PK study of high-dose oral CBD
- Verster & Roth (2011) — Standard operating procedures for SDLP measurement

**Named models or frameworks**:
- Non-inferiority trial design
- SDLP (standard deviation of lateral position) as impairment metric
- Cohen's d_z effect size framework
- BAC-equivalent non-inferiority margin (Δ = 0.05% BAC equivalent)
- DRUID app (Drug Impairment smartphone assessment)

**Brain regions**: Not applicable (behavioural/pharmacological study)

**Keywords**: cannabidiol, CBD, simulated driving, SDLP, non-inferiority trial, driving impairment, oral cannabinoid pharmacokinetics, psychomotor performance, dose-ranging RCT, medicinal cannabis, drug-impaired driving, CBD pharmacokinetics
