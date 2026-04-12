---
source_file: "onodera2021_epilepsy_astrocyte.md"
paper_id: "onodera2021_epilepsy_astrocyte"
title: "Exacerbation of Epilepsy by Astrocyte Alkalization and Gap Junction Uncoupling"
authors: "Mariko Onodera, Jan Meyer, Kota Furukawa, Yuichi Hiraoka, Tomomi Aida, Kohichi Tanaka, Kenji F. Tanaka, Christine R. Rose, Ko Matsui"
year: 2021
journal: "The Journal of Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "hippocampus_ca1"]
keywords: ["exacerbation", "epilepsy", "astrocyte", "alkalization", "gap", "junction", "uncoupling"]
key_citations: ["wang2020_alternating_theta_sequences"]
---

### One-line summary

Brief epileptiform activity triggers astrocyte alkalization via Na+/HCO3- cotransporter (NBC) activation, causing gap junction uncoupling that impairs extracellular K+ clearance and exacerbates epilepsy — a process preventable by NBC blockade with S0859.

---

### Background & motivation

Epilepsy is characterised by seizures that intensify with each episode, but the mechanisms underlying this early exacerbation are poorly understood. Astrocytes regulate neuronal excitability by buffering extracellular K+ through a process that depends on intercellular diffusion via gap junctions. Disruption of this K+ clearance mechanism could leave neurons in a hyperexcitable state, but whether astrocyte gap junction coupling changes acutely in response to the first seizure events — and what drives this change — had not been established. The study therefore sought to identify the chain of cellular events linking initial epileptiform activity to rapid plasticity in astrocyte function.

---

### Methods

- **Preparation**: Acute parasagittal hippocampal slices (250 µm) from C57BL/6J or BALB/c mice (P16–P30).
- **Epileptiform activity induction**: 15-minute perfusion with Mg2+-free ACSF + 100 µM picrotoxin (GABAA antagonist; "0Mg2+-Pic").
- **Extracellular K+ recording**: Double-barrelled K+-selective microelectrodes in CA1 stratum radiatum; glutamate bath application (1 mM, 10 s) in TTX to generate K+ transients isolated from synaptic activity.
- **Na+ imaging**: SBFI-AM fluorescent dye loaded into slices; astrocytes identified by SR101; electrical stimulation of single "starter" astrocyte to measure intercellular Na+ spread (proxy for gap junction coupling).
- **pH imaging**: Transgenic mice (Mlc1-tTA × tetO-Lck-E2GFP) expressing a ratiometric pH sensor (Lck-E2GFP) specifically in astrocytes; confocal ratiometric imaging before and after epileptiform activity.
- **Pharmacology**: S0859 (50 µM) NBC blocker applied during epileptiform induction to test sufficiency of the NBC-alkalization pathway.
- **In vitro neuronal excitability**: LFP recordings in CA1; neuronal excitability evaluating stimuli (NEES; 100 Hz for 100 ms) before and after an epi-stimulation protocol; power spectrum analysis.
- **In vivo rapid kindling**: Implanted bipolar electrode and microdialysis probe in right dorsal hippocampus of adult C57BL/6J mice; 12 stimulations/day for 3 days; continuous intrahippocampal delivery of ACSF ± S0859 (300 µM feed concentration, ~10–30 µM effective); EEG recorded from cortical screw electrodes.
- **Statistical tests**: Student's t-test, Welch's t-test with Holm correction, two-way repeated-measures ANOVA with Tukey's post hoc, chi-squared test, Mann–Whitney U test.

---

### Key findings

- Short-term epileptiform activity (15 min, 0Mg2+-Pic) significantly prolonged the half-decay time of glutamate-evoked K+ transients in CA1 (p < 0.05), indicating impaired extracellular K+ clearance, without significantly altering peak K+ amplitude or resting K+ levels.
- Na+ imaging showed that intercellular spread of Na+ from electrically stimulated astrocytes was significantly reduced at multiple distances (10–40 µm and 50–70 µm) in post-epileptic slices (p < 0.05, Welch's t-test), consistent with acute gap junction uncoupling.
- Astrocytes in transgenic pH-reporter mice showed significant intracellular alkalization at 5 min and 10 min after 0Mg2+-Pic exposure relative to controls (p < 0.01, two-way RM ANOVA).
- Direct induction of astrocyte alkalization with NH4Cl (20 mM) mimicked gap junction uncoupling, with significantly reduced Na+ diffusion at all measured distances (p < 0.05 to p < 0.0001).
- S0859 (NBC blocker) significantly attenuated astrocyte alkalization (p < 0.01) and, importantly, almost completely prevented gap junction uncoupling in post-epileptic slices (p < 0.001 at 50–70 µm).
- S0859 prevented the increase in LFP power spectrum density across 4–30 Hz frequency bands following epileptiform stimulation in vitro (control n = 9, S0859 n = 4; p < 0.05–0.01).
- In vivo, S0859 significantly reduced the ratio of second-to-first afterdischarge (AD) peak integrated amplitude (p < 0.05, n = 6 animals each), demonstrating prevention of acute kindling.
- Continuous S0859 administration over 3 days dramatically reduced AD occurrence rates (chi-squared = 27.4, 24.5, 91 for days 1, 2, 3; p < 0.0001) and total AD durations (p < 0.001 to p < 0.0001, Mann–Whitney U test).
- Resting-state EEG power was not significantly different between S0859 and control at any frequency band, suggesting no adverse baseline effects of NBC blockade.
- Delta-band EEG power (1–4 Hz) increased from day 1 to day 3 in control animals (p < 0.05) but not in S0859-treated animals, consistent with prevention of pathological epileptogenesis.

---

### Computational framework

Not applicable in a formal sense. The paper proposes a mechanistic cascade rather than a mathematical computational model: epileptiform activity → neuronal K+ efflux → astrocyte depolarisation → NBC activation → HCO3- influx → intracellular alkalization → connexin pH sensitivity → gap junction uncoupling → impaired K+ spatial buffering → prolonged neuronal hyperexcitability. There is no formal model (ODEs, network model, etc.) developed. The results constrain biophysical models of K+ homeostasis and connexin gating, and may inform computational models of seizure propagation and termination that incorporate astrocyte dynamics.

---

### Prevailing model of the system under study

The paper's introduction frames the field's prevailing understanding as follows: astrocytes form a syncytium via gap junctions (connexins Cx30, Cx43) that enables K+ spatial buffering — neurons discharge K+ into the extracellular space, astrocytes take it up, and it diffuses intercellularly through the gap-junction network away from the active region ("spatial buffering"). Disruption of gap junctions was known to impair K+ clearance. Gap junction uncoupling had been reported in the advanced (chronic) stages of epilepsy and in sclerotic tissue, but was not established as an acute event occurring after first-time exposure to brief seizure activity. The prevailing view also held that astrocyte alkalization occurs during seizure-like activity (established in earlier work by Chesler, Kraig, and Raimondo), and pH sensitivity of connexins was known from non-neuronal cell types. However, the causal link from initial seizure activity → NBC activation → alkalization → gap junction uncoupling → K+ clearance failure → seizure exacerbation had not been assembled as a unified mechanism, nor had a pharmacological intervention targeting this chain been tested.

---

### What this paper contributes

This paper demonstrates for the first time that even brief (15-minute) exposure to epileptiform activity is sufficient to acutely uncouple astrocyte gap junctions via an NBC-dependent alkalization mechanism. Specifically, the paper:

1. Establishes a temporal link between first-time epileptiform activity and acute K+ clearance impairment — a mechanism previously only described in chronic epilepsy.
2. Provides direct evidence that this uncoupling is driven by intracellular astrocyte alkalization, using a transgenic pH sensor to confirm alkalization in vivo in astrocytes.
3. Demonstrates that artificially alkalized astrocytes (NH4Cl) recapitulate gap junction uncoupling, causally implicating pH as the upstream trigger.
4. Shows that NBC blockade (S0859) prevents alkalization, prevents gap junction uncoupling, suppresses the development of post-epileptic neuronal hyperexcitability in vitro, and substantially inhibits kindling progression in vivo — without perturbing baseline neural activity.
5. Identifies NBC as a potential therapeutic target for anti-epileptogenic (rather than purely anti-seizure) intervention, targeting astrocyte plasticity rather than neuronal firing directly.

---

### Brain regions & systems

- **Hippocampus (CA1 stratum radiatum)** — primary site of all slice electrophysiology, K+ recording, and astrocyte imaging; locus of epileptiform activity induction and K+ clearance measurements.
- **Hippocampus (Schaffer collaterals / CA1 pyramidal layer)** — stimulated to induce epileptiform activity; used for LFP and NEES recordings.
- **Dorsal hippocampus (in vivo)** — implantation site for kindling electrode and microdialysis probe; site of NBC blocker delivery.
- **Cortex (bilateral screw electrodes)** — used for EEG recording in in vivo kindling model.
- **Astrocytic syncytium** — the distributed network of gap-junction-coupled astrocytes is the primary system under study, proposed as the locus of acute epileptic plasticity.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Brief epileptiform activity acutely exacerbates seizure susceptibility by impairing extracellular K+ clearance.

**Computational level**: The brain must efficiently buffer activity-evoked K+ accumulation to prevent runaway neuronal depolarisation and subsequent seizure propagation. The astrocytic syncytium performs spatial buffering of K+ as a distributed computation, routing K+ from high-concentration regions via diffusion through the network.

**Algorithmic level**: The algorithm proposed is: (1) neuronal activity → K+ efflux → astrocyte depolarisation; (2) depolarisation activates the electrogenic NBC in the inward direction, importing Na+ and HCO3-; (3) HCO3- influx raises intracellular pH (alkalization); (4) alkaline pH reduces gap junction open probability (connexin closure); (5) reduced gap junction coupling restricts spatial K+ diffusion via the syncytium; (6) extracellular K+ remains elevated for longer, keeping neurons hyperexcitable. Pharmacological closure of the NBC (S0859) breaks the chain at step (2), preventing steps (3)–(6).

**Implementational level**: The paper provides direct implementation evidence at the level of specific cellular and molecular machinery: the NBC transporter (NBCe1/SLC4A4, expressed preferentially in astrocytes), connexin proteins (Cx30, Cx43) with their known pH-sensitivity, and the spatial geometry of the astrocytic syncytium in hippocampal CA1. Neural data supporting the algorithm include: K+-selective electrode recordings showing impaired clearance kinetics; Na+ fluorescence imaging showing reduced intercellular diffusion across specific distance intervals; transgenic pH sensor imaging showing astrocyte-specific alkalization; NH4Cl alkalization recapitulating uncoupling; and S0859 prevention of each step in the chain both in slices and in vivo. The paper does not resolve the precise molecular mechanism linking pH to connexin gating (phosphorylation, protein-binding, or direct pH effect on connexin pore) but discusses these as candidate sub-mechanisms.

---

### Limitations & open questions

- The precise molecular mechanism by which intracellular pH changes close connexins is not established — candidate pathways include direct pH effects on pore gating, connexin phosphorylation via MAPK/Src pathways, and cytoskeletal interactions with Cx43.
- The slice preparation uses young mice (P16–P30), and it is unclear whether the same acute mechanism operates identically in adult or aged animals.
- S0859 is not entirely astrocyte-specific; NBC is also expressed in neurons (particularly NBCn1 in excitatory postsynaptic membranes), and chronic NBC blockade may have additional neuronal effects (e.g., reducing NMDAR surface expression) that contribute to its anti-epileptogenic effects independently of astrocyte alkalization.
- In vivo, the microdialysis delivery of S0859 produces a concentration gradient of uncertain spatial extent; the effective drug concentration at the recording site is estimated but not directly measured.
- When ADs did occur in S0859-treated animals, their duration still increased with repeated stimulation (similar to controls), suggesting that multiple additional mechanisms contribute to kindling that are not prevented by NBC blockade alone.
- The relative contribution of K+ clearance impairment (studied here) versus other early epileptogenesis mechanisms (increased excitatory synaptic transmission, loss of interneurons, Kir4.1 and Na+/K+-ATPase dysfunction) is not quantified.
- Chronic NBC blockade may affect astrocytic energy metabolism through effects on glycogenesis (NBC's reported relationship to metabolic pathways), which could have secondary effects on network excitability.
- The paper does not examine whether the gap junction uncoupling is reversible and on what timescale, or whether repeated brief seizures have cumulative or ceiling effects on alkalization/uncoupling.

---

### Connections & keywords

**Key citations**:
- Raimondo et al. (2016) — established tight coupling of astrocyte pH dynamics to epileptiform activity using genetically encoded sensors
- Chesler & Kraig (1987, 1989) — original observations of astrocyte alkalization during cortical stimulation
- González-Nieto et al. (2008) — pH regulation of neuronal connexin-36 channels
- Bedner et al. (2015) — astrocyte uncoupling in human temporal lobe epilepsy
- Bazzigaluppi et al. (2017) — astrocyte gap junction blockade and extracellular K+ in neocortex
- Langer et al. (2012) — Na+ imaging of intercellular spread in hippocampal astrocytes
- Wang et al. (2020) — short-term epileptiform activity weakens gap junction coupling and K+ distribution
- Du et al. (2018) — computational model showing gap junction uncoupling and K+ transients
- Pannasch et al. (2012) — astroglial gap junctions shape neuronal network activity

**Named models or frameworks**:
- Rapid hippocampal kindling model (in vivo)
- 0Mg2+-Pic (zero-magnesium plus picrotoxin) acute epileptiform activity model (in vitro)
- KENGE-tetO-Lck-E2GFP transgenic pH reporter mouse
- Mlc1-tTA astrocyte-specific driver mouse

**Brain regions**:
- Hippocampus (CA1, stratum radiatum)
- Dorsal hippocampus
- Cortex (EEG recording)

**Keywords**:
- astrocyte gap junction uncoupling
- connexin pH sensitivity
- extracellular potassium clearance
- Na+/HCO3- cotransporter (NBC, NBCe1)
- epileptogenesis
- spatial buffering
- hippocampal astrocyte syncytium
- intracellular alkalization
- rapid kindling
- S0859 NBC blocker
- astrocyte plasticity
- SBFI sodium imaging
