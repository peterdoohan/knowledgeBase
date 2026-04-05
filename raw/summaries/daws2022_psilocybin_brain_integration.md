---
source_file: daws2022_psilocybin_brain_integration.md
title: "Increased global integration in the brain after psilocybin therapy for depression"
authors: Richard E. Daws, Christopher Timmermann, Bruna Giribaldi, James D. Sexton, Matthew B. Wall, David Erritzoe, Leor Roseman, David Nutt, Robin Carhart-Harris
year: 2022
journal: Nature Medicine
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Psilocybin therapy for depression produces a subacute decrease in whole-brain network modularity that is absent after escitalopram and correlates with long-term antidepressant response across two independent clinical trials.

---

### Background & motivation

Depression is associated with abnormally rigid and segregated brain network organisation — elevated functional connectivity within the default mode network (DMN) and reduced connectivity between the DMN and higher-order cognitive networks (executive network, EN; salience network, SN) — reflecting the characteristically narrow, ruminative quality of depressive cognition. While psilocybin therapy shows substantial antidepressant efficacy in multiple clinical trials, its neural mechanism is poorly understood. One hypothesis is that psilocybin's acute action on 5-HT2A receptors in transmodal cortex (which densely overlaps with the DMN/EN/SN) causes a lasting increase in global brain network integration that underlies therapeutic benefit. This paper tests that hypothesis directly using resting-state fMRI from two clinical trials, and asks whether the same mechanism is present after the conventional SSRI antidepressant escitalopram.

---

### Methods

- **Study design**: Two clinical trials with pre- and post-treatment resting-state fMRI.
  - *Open-label trial (TRD)*: 16 patients with treatment-resistant depression (TRD); baseline fMRI and clinical assessment, then 10 mg + 25 mg psilocybin therapy (1 week apart); post-treatment fMRI 1 day after second dose.
  - *Double-blind randomised controlled trial (DB-RCT, MDD)*: 59 patients with major depressive disorder randomly assigned to psilocybin arm (2 × 25 mg psilocybin + daily placebo; n = 22 in imaging sample) or escitalopram arm (2 × 1 mg psilocybin + 6 weeks escitalopram 10–20 mg/day; n = 21 in imaging sample); post-treatment fMRI 3 weeks after second dose.
- **Primary outcome (imaging)**: Normalised brain network modularity (Q) derived from Pearson correlation functional connectivity matrices of 100 cortical ROIs (Schaefer atlas), using a Louvain community detection algorithm.
- **Secondary analyses**: Functional cartography (network recruitment and between-network integration for DMN, EN, SN); dynamic network flexibility from multilayer modularity (DB-RCT only, leveraging higher temporal resolution).
- **Clinical outcome**: Beck Depression Inventory (BDI-1A) at multiple post-treatment time points.
- **fMRI preprocessing**: Standard pipeline (FSL, AFNI, FreeSurfer, ANTs); strict head motion exclusion criteria (>20% volumes with framewise displacement >0.5 mm).

---

### Key findings

- **Open-label trial**: Brain network modularity significantly decreased 1 day after psilocybin therapy (mean difference −0.29; t15 = 2.87, P = 0.012, d = 0.72), indicating global increase in functional connectivity between networks.
- **Modularity-outcome correlation (open-label)**: Post-treatment modularity correlated with BDI at 6-month primary endpoint (r14 = 0.64, P = 0.023, FDR-corrected); change in modularity correlated with BDI change at 6 months (r14 = 0.54, P = 0.033).
- **Cartography (open-label)**: DMN within-network recruitment decreased (d = 0.75); DMN–EN between-network integration increased (d = 0.75); DMN–SN between-network integration increased (d = 0.72); all FDR-corrected.
- **DB-RCT replication**: Brain network modularity significantly reduced in the psilocybin arm 3 weeks post-treatment (mean difference −0.39; t21 = −2.20, P = 0.039, d = 0.47); modularity change correlated with BDI improvement at primary endpoint (r20 = 0.42, P = 0.025, one-tailed).
- **Escitalopram comparison**: No significant change in modularity in the escitalopram arm (mean difference 0.01, P = 0.95, d = 0.02); no significant correlation between modularity change and BDI improvement.
- **Dynamic flexibility (DB-RCT)**: Increased executive network dynamic flexibility strongly correlated with greater depression improvement after psilocybin (r20 = −0.76, 95% CI −0.90 to −0.50, P = 0.001, FDR-corrected); no significant correlations in the escitalopram arm.
- Baseline modularity did not predict treatment response; early-phase modularity change after treatment did.

---

### Computational framework

The paper uses **brain network modularity (graph theory / complex network analysis)** as its primary analytical framework. Network modularity (Q) quantifies how strongly the brain's functional connectivity can be partitioned into segregated communities (modules), relative to a null model. High Q reflects strong within-network and weak between-network coupling; low Q reflects global integration. The Louvain community detection algorithm iteratively assigns nodes (cortical ROIs) to communities to maximise Q. Normalised Q (relative to randomly rewired null networks) is used to allow comparisons across patients and sessions. Dynamic flexibility extends this by tracking how often each region switches community allegiance across time windows using multilayer modularity.

The framework frames brain function as lying on a spectrum from modular/segregated to globally integrated, and connects this to the energy landscape metaphor: high modularity = constrained state space; low modularity = broader, more flexible repertoire of network configurations.

---

### Prevailing model of the system under study

Prior to this paper, the field understood depression as associated with abnormally rigid brain network organisation: excessive DMN self-referential activity, hyperconnectivity within the DMN (linked to rumination), and hypoconnectivity between the DMN and task-positive networks (EN, SN) involved in cognitive flexibility, attention switching, and goal-directed behaviour. This abnormal modularity was thought to create a constricted functional state space — an "attractor state" of negative cognition with limited ability to flexibly engage with alternative cognitive modes. The acute action of psilocybin was known to produce network disintegration and increased global functional connectivity, but whether this acute mechanism persisted subacutely and whether it was specifically linked to therapeutic outcome was unclear. The introduction also notes that prior fMRI work on psilocybin in TRD had shown increased DMN connectivity 1 day post-treatment, in apparent contrast to the acute disintegration, and that the mechanism linking psilocybin's neural action to its antidepressant effect remained unresolved.

---

### What this paper contributes

This paper provides the first replicated, mechanistically specific neuroimaging evidence that psilocybin's antidepressant effect is mediated by a subacute increase in global brain network integration (decreased modularity). Key advances:

1. The effect is robustly replicated across two trials with different populations (TRD vs. MDD), dose regimens, scan timing (1 day vs. 3 weeks post-treatment), and fMRI acquisition parameters — substantially strengthening causal inference.
2. Modularity change after treatment prospectively predicts long-term (6-month) antidepressant response, establishing it as a biomarker of therapeutic mechanism, not just a correlate.
3. The mechanism appears specific to psilocybin: escitalopram produces no change in modularity despite achieving some antidepressant effect, suggesting the two drugs work via distinct neural pathways.
4. Network cartography and dynamic flexibility analyses converge on higher-order transmodal networks (DMN, EN, SN) as the locus of psilocybin's action — these are also the networks with the highest 5-HT2A receptor density, linking pharmacology to network-level change.
5. The results reframe psilocybin's subacute effect as a "carryover" of the acute disintegration/integration dynamic, now shown to be clinically meaningful.

---

### Brain regions & systems

- **Default mode network (DMN)** — identified as hyperactive/overrecruited in depression; shows reduced within-network recruitment and increased between-network integration with EN and SN after psilocybin therapy.
- **Executive network (EN)** — impaired in depression and other disorders of cognitive inflexibility; shows increased between-network integration with DMN and increased dynamic flexibility after psilocybin, with flexibility strongly predicting treatment response (r ~ −0.76).
- **Salience network (SN)** — implicated in internal/external attention switching, impaired in depression; shows increased between-network integration with DMN after psilocybin.
- **Dorsal attention network (DA)** — included in secondary cartography analyses; shows trend toward increased flexibility with psilocybin.
- **Transmodal cortex broadly** — highest density of 5-HT2A receptors; proposed pharmacological substrate linking psilocybin's binding profile to the observed network changes.

---

### Mechanistic insight

The paper provides partial but not complete evidence for mechanistic insight at Marr's levels.

**Computational**: The brain in depression is solving the problem of regulating self-referential cognition and attentional flexibility, but is stuck in an overly modular (rigid, constricted) functional state that biases toward rumination and away from flexible updating. Psilocybin's therapeutic action is modelled as resetting this to a broader, more integrated state space.

**Algorithmic**: Decreased network modularity — specifically reduced DMN self-recruitment and increased DMN–EN and DMN–SN communication — is proposed as the mechanism. Dynamic flexibility of the EN is particularly linked to outcome. However, this is a descriptive account derived from fMRI connectivity metrics; the paper does not specify an algorithmic process or computation (e.g., no model of how information is processed differently under lower modularity).

**Implementational**: The paper implicates 5-HT2A receptor agonism in transmodal cortex as the physical substrate, pointing to the known overlap between 5-HT2A receptor density maps and the DMN/EN/SN topology. The hypothesised contrast with escitalopram (which acts predominantly on 5-HT1A in limbic circuitry) provides a receptor-level mechanistic account. However, the paper does not provide receptor-level, cellular, or direct pharmacological data in the imaging sample — this remains inference from the literature.

The paper does not fully meet the mechanistic bar: it provides fMRI data supporting a network-level account but does not formalise an algorithm or link network changes to specific neural computations. The strongest contribution is a robust empirical biomarker with a plausible (but not directly tested) pharmacological substrate account.

---

### Limitations & open questions

- **No active placebo control in open-label trial**: psychological expectancy effects cannot be ruled out; the DB-RCT mitigates but does not eliminate this given the perceptual unblinding of psilocybin.
- **Eyes-closed fMRI**: higher risk of in-scanner sleep; authors partially address this with self-report data and head motion analyses, but cannot fully rule out sleep confound.
- **Cartography findings did not fully replicate across trials**: DMN-specific changes in network recruitment and between-network integration seen at 1 day post-treatment in the open-label trial were not significant at 3 weeks in the DB-RCT — may reflect timing differences or severity differences between populations.
- **Baseline modularity does not predict response**: limits prospective use as a treatment selection biomarker.
- **Small samples**: open-label n = 16, DB-RCT psilocybin n = 22, limiting power for subgroup analyses.
- **Correlation does not establish causality**: psychological processes independent of drug action may have contributed to both clinical and neuroimaging outcomes.
- **Temporal dynamics unclear**: scans at 1 day vs. 3 weeks post-treatment differ, making it unclear how long the modularity effect persists and when it is maximal.
- **Dynamic flexibility analysis only in DB-RCT**: due to TR differences; limits direct comparison across trials.
- **Key open question**: What are the parameters of psilocybin dose, preparation, timing, and psychotherapeutic context that optimise the modularity change and therapeutic response? Are these effects generalisable beyond MDD/TRD to other disorders characterised by cognitive inflexibility?

---

### Connections & keywords

**Key citations**:
- Carhart-Harris et al. (2017), Sci Rep — open-label TRD psilocybin fMRI trial (trial 1 in this paper)
- Carhart-Harris et al. (2021), NEJM — DB-RCT psilocybin vs. escitalopram (trial 2 in this paper)
- Carhart-Harris & Friston (2019), Pharmacol Rev — REBUS model of psychedelic brain action
- Lord et al. (2019), NeuroImage — dynamical exploration of brain network repertoire under psilocybin
- Luppi et al. (2021), NeuroImage — LSD and dynamic integration/segregation
- Hamilton et al. (2011), Biol Psychiatry — DMN and task-positive network activity in MDD
- Goodman et al. (2021), Cereb Cortex — whole-brain functional dynamics and depressive symptom severity
- Mattar et al. (2015), PLoS Comput Biol — functional cartography of cognitive systems
- Rolls (2016), Neurosci Biobehav Rev — non-reward attractor theory of depression

**Named models or frameworks**:
- REBUS (Relaxed Beliefs Under Psychedelics) model
- Brain network modularity (Louvain community detection; Newman & Girvan Q metric)
- Functional cartography (network recruitment and between-network integration)
- Dynamic flexibility / multilayer modularity
- Attractor state model of depression
- Energy landscape framework for brain states

**Brain regions**:
- Default mode network (DMN)
- Executive network (EN)
- Salience network (SN)
- Dorsal attention network
- Transmodal cortex

**Keywords**:
- psilocybin therapy
- treatment-resistant depression
- brain network modularity
- resting-state fMRI
- functional connectivity
- network integration
- 5-HT2A receptor
- dynamic network flexibility
- escitalopram comparison
- antidepressant mechanism
- graph-theoretic neuroimaging
- psychedelic neuroscience
