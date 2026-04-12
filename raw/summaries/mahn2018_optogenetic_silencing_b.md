---
source_file: mahn2018_optogenetic_silencing_b.md
paper_id: mahn2018_optogenetic_silencing_b
title: "High-efficiency optogenetic silencing with soma-targeted anion-conducting channelrhodopsins"
authors:
  - "Mathias Mahn"
  - "Lihi Gibor"
  - "Pritish Patil"
  - "Katayun Cohen-Kashi Malina"
  - "Shir Oring"
  - "Yoav Printz"
  - "Rivka Levy"
  - "Ilan Lampl"
  - "Ofer Yizhar"
year: 2018
journal: "Nature Communications"
paper_type: empirical
contribution_type: methodological
species:
  - mouse
  - rat
methods:
  - optogenetics
  - electrophysiology
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - nucleus_accumbens
  - amygdala
  - basolateral_amygdala
keywords:
  - optogenetic_inhibition
  - anion_conducting_channelrhodopsin_acr
  - gtacr2_soma_targeting
  - antidromic_spiking
  - axonal_chloride_reversal_potential
  - kcc2_co_transporter
  - kv2_1_subcellular_targeting
  - aav_mediated_opsin_expression
  - in_vivo_neuronal_silencing
  - fear_extinction
  - channelrhodopsin_membrane_trafficking
  - photocurrent_amplitude
  - high
  - efficiency
  - optogenetic
  - silencing
  - soma
  - targeted
  - anion
  - conducting
wiki_pages:
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

### One-line summary

Soma-targeting of Guillardia theta anion-conducting channelrhodopsins (stGtACR2) improves membrane expression, increases photocurrents, and eliminates most axonal excitation artifacts, enabling highly efficient optogenetic silencing of neuronal populations in the mammalian brain.

---

### Background & motivation

Optogenetic silencing of neurons has relied primarily on light-driven ion pumps (halorhodopsin, archaerhodopsin), which require high light power, show photocurrent rundown over sustained illumination, and perturb intracellular ion homeostasis. Naturally-occurring anion-conducting channelrhodopsins from Guillardia theta (GtACRs) have large single-channel conductance and better photon-ion stoichiometry, making them potentially superior tools, but their adoption in mammalian neuroscience has been limited by poor membrane targeting and an unexpected problem: axonal chloride reversal potential is depolarised relative to the soma, causing ACR activation in axons to trigger antidromic action potentials rather than inhibition. This paper addresses both limitations through subcellular targeting engineering.

---

### Methods

- **Constructs tested:** Native GtACR2, engineered GtACR2 with ER export/trafficking signals (eGtACR2), soma-targeted GtACR2 fused to the Kv2.1 somatodendritic targeting motif (stGtACR2), and a further destabilised variant (stGtACR2-PEST); compared against engineered ACRs iC++ and iChloC and ion-pump opsins eArch3.0 and eNpHR3.0.
- **In vitro characterisation:** Whole-cell patch-clamp recordings from cultured rat hippocampal neurons (AAV or calcium phosphate transfection); voltage-clamp and current-clamp to quantify photocurrents and antidromic spike generation; spatially restricted laser illumination to isolate soma vs. neurite contributions.
- **KCC2 overexpression experiment:** Co-transfection of GtACR2 with KCC2 in cultured neurons; immunostaining for KCC2 and MAP2 to verify axonal KCC2 localisation; patch-clamp to assess changes in chloride reversal potential and antidromic spiking rates.
- **Acute brain slice:** AAV injection into mouse medial prefrontal cortex (mPFC); whole-cell recordings to quantify stationary photocurrents; contralateral EPSC recordings to assay light-evoked axonal neurotransmitter release.
- **In vivo electrophysiology (awake mice):** Extracellular multi-unit recordings from mPFC using movable optrode drives; 5 s silencing pulses (460 nm, 4 light powers: 0.125–1 mW/mm²); short 5 ms pulses to mPFC and nucleus accumbens (NAc) to detect antidromic spiking.
- **c-Fos immunohistology:** Sustained silencing during enriched environment exploration (75 min, 6 mW); comparison of c-Fos-positive nuclei in expressing vs. non-expressing hemispheres across stGtACR1, stGtACR2, eNpHR3.0, and TagRFP controls.
- **Fear extinction behaviour:** Bilateral BLA injection of stGtACR2 or eYFP control; auditory fear conditioning followed by CS-paired continuous light during extinction training; freezing measured during extinction recall.

---

### Key findings

- GtACR2 produced stationary photocurrents of ~629 pA (at Vhold = −35 mV), significantly larger than iC++ (~330 pA) and iChloC (~136 pA), but showed poor somatic membrane targeting.
- Antidromic (escaped) action potentials were observed in 6/12 GtACR2-expressing neurons in response to 1 ms full-field pulses; neurite-targeted illumination (not soma) was the trigger, confirming a depolarised chloride reversal potential in the axon.
- KCC2 overexpression significantly reduced GtACR2-evoked antidromic spiking (76% → 50% of neurons spiking; Mann–Whitney p = 0.04), without shifting somatic chloride reversal potential, confirming the axon-specific chloride gradient hypothesis.
- eGtACR2 (improved membrane targeting alone) paradoxically increased antidromic spiking, while stGtACR2 (soma-targeted) both increased photocurrents and decreased antidromic spiking, without reducing peak photocurrents in matched cultures.
- stGtACR2 showed a 2.6-fold increase in stationary photocurrents compared to GtACR2 in acute brain slice (~2 nA vs. ~800 pA; ANOVA, F(2,23) = 11.84, p = 2.9×10⁻⁴), exceeding the photocurrents reported for eArch3.0 and eNpHR3.0.
- Soma-targeted variants dramatically reduced light-evoked EPSCs in contralateral axon terminals compared to GtACR2 (ANOVA, F(2,22) = 5.54, p = 0.011), confirming reduced axonal channel presence.
- In vivo: stGtACR2 silenced 52–61% of mPFC units at all light powers tested, versus 21–43% for GtACR2; stGtACR2 was superior at the two lowest powers (0.125 mW/mm²: p = 3.2×10⁻⁵; 0.25 mW/mm²: p = 2.1×10⁻⁴).
- Antidromic spiking from distal NAc axons occurred in 19% of GtACR2 units vs. only 3% of stGtACR2 units in vivo (Chi-square, p = 1.97×10⁻³).
- c-Fos labelling confirmed widespread cortical silencing with stGtACR1 (p = 0.018) and stGtACR2 (p = 0.023) but not eNpHR3.0 (p = 0.84) or TagRFP controls (p = 0.96); no DAPI-count reduction indicated no toxicity.
- BLA inhibition with stGtACR2 during CS presentation impaired fear extinction recall (higher freezing in stGtACR2 mice: p = 0.038), without affecting contextual fear or open field behaviour.

---

### Computational framework

Not applicable. The paper is an optogenetic tool development and validation study; it does not apply a formal computational framework. Findings are relevant to experiments testing causal circuit hypotheses and could be used to constrain circuit-level computational models of mPFC, BLA, and fear extinction. The underlying biophysics of chloride reversal potential differences between axonal and somatodendritic compartments (governed by KCC2 distribution) is a central mechanistic concept, but is not formalised computationally.

---

### Prevailing model of the system under study

The paper addresses the field of optogenetic tool development rather than a specific brain system model. The prevailing understanding at the time was that ACRs from Guillardia theta are powerful inhibitory tools in invertebrates (Drosophila, zebrafish) but problematic in mammals because: (1) GtACRs showed poor membrane trafficking and intracellular aggregation in mammalian neurons; and (2) chloride in the axon is at a higher concentration than in the soma — due to the absence of the KCC2 co-transporter from the axonal compartment — meaning an anion-conducting channel opened in the axon could depolarise rather than hyperpolarise the membrane, generating antidromic spikes. The introduction also frames the limitations of the incumbent tools (ion-pump rhodopsins): 1 ion per photocycle, photocurrent rundown of up to 90% after 1 min, tissue heating, and unintended effects on ion homeostasis (halorhodopsin: chloride accumulation; archaerhodopsin: pH-driven Ca²⁺ influx and vesicle release).

---

### What this paper contributes

The paper demonstrates that both main obstacles to GtACR use in mammals are addressable through protein engineering: adding the Kv2.1 somatodendritic targeting motif restricts GtACR2 to the soma and proximal dendrites, simultaneously improving membrane expression (yielding larger photocurrents) and removing channel from the axon (eliminating most antidromic spiking). The result is a tool that outperforms all previous inhibitory opsins in terms of light sensitivity and silencing efficiency in vivo, and that can be used to achieve behaviorally relevant, temporally precise inhibition (e.g., BLA silencing during CS presentation interferes with fear extinction). The paper also clarifies a general phenomenon — ACR-mediated axonal excitation via a depolarised chloride reversal potential — demonstrating it in three preparation types (cultured neurons, acute slice, behaving mice) and providing a mechanistic explanation (absence of KCC2 from the axon). This legitimises soma-targeting as the standard approach for ACR-based inhibition in mammalian neurons.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary site for in vivo AAV injection, optrode recordings, and assessment of silencing efficiency; used as a cortical test bed for tool characterisation.
- **Nucleus accumbens (NAc)** — target of optogenetic stimulation to assess antidromic spiking in distal cortico-striatal axons of mPFC-projecting neurons.
- **Basolateral amygdala (BLA)** — site of bilateral stGtACR2 expression for the fear extinction experiment; used to demonstrate behaviorally relevant inhibition.
- **Hippocampus (CA1/CA3 culture)** — primary model system for in vitro patch-clamp characterisation of GtACR2 variants and the KCC2 rescue experiment.

---

### Mechanistic insight

The paper meets both criteria for this section.

**Phenomenon:** Chloride-conducting channels (ACRs) in the axon can excite rather than inhibit neurons, generating antidromic action potentials, because the axonal chloride reversal potential is depolarised relative to the resting membrane potential.

**Computational level:** The problem the nervous system "solves" here is not directly addressed; the paper focuses on an undesired tool artifact. However, the underlying biology reveals that the brain maintains spatially heterogeneous chloride gradients as part of the normal organisation of inhibitory signalling — the axon is not subject to the same KCC2-mediated chloride extrusion as the somatodendritic compartment, which may relate to how axo-axonic cells (chandelier cells) modulate spike initiation excitatorily under some conditions.

**Algorithmic level:** KCC2 is the key regulator: its expression in the somatodendritic compartment (but absence from the axon) creates a lower intracellular chloride concentration in the soma/dendrites and a higher concentration in the axon, resulting in different reversal potentials across compartments. Opening a chloride channel in the soma leads to hyperpolarisation (chloride inflow), while opening it in the axon leads to depolarisation (chloride outflow).

**Implementational level:** The paper provides evidence at the implementational level: KCC2 immunostaining confirms its somatodendritic-only localisation; overexpression of KCC2 in axons (confirmed by MAP2-negative co-localisation) significantly reduces antidromic spiking (from 76% to 50% of neurons), directly linking KCC2-mediated chloride extrusion to the axonal excitation phenotype. Bonus: the Kv2.1 targeting motif localises stGtACR2 to soma and proximal dendrites via a specific trafficking mechanism (distinct from the ion channel's own trafficking), providing an implementational tool for restricting channel activity to specific subcellular compartments.

---

### Limitations & open questions

- stGtACR2 does not entirely eliminate antidromic spiking from proximal axon segments; short 5 ms pulses at higher light power still evoke spiking at the mPFC soma/proximal axon level, requiring longer pulses at lower power to circumvent this.
- Rebound excitation (increased firing after light offset) was observed for both GtACR2 and stGtACR2, a general caveat of sustained optogenetic silencing likely due to synaptic depression rebound, which must be accounted for in experimental design.
- The direct measurement of axonal chloride concentration during ACR-mediated conductance was not performed (suggested as future work using red-shifted chloride indicators).
- The construct drives expression under CaMKIIα, restricting use to excitatory neurons; generalisation to other cell types requires testing.
- The high-expression levels of soma-targeted GtACR variants reported by a contemporaneous study (Mardinly et al., 2018) caused cell death; this study did not observe toxicity, but did not systematically compare expression levels.
- Recordings were from relatively small numbers of animals (n = 2 mice per group for in vivo electrophysiology), and blinding/randomisation were not performed.

---

### Connections & keywords

**Key citations:**
- Govorunova et al. (2015) Science — original description of GtACR1 and GtACR2
- Mahn et al. (2016) Nat Neurosci — prior work showing GtACR1-mediated excitatory release at thalamocortical axons
- Malyshev et al. (2017) Neurosci Lett — concurrent report of antidromic spiking in GtACR2-expressing cortical neurons
- Gradinaru et al. (2010) Cell — source of ER export/trafficking signal for enhanced membrane targeting (eNpHR3.0 strategy)
- Baker et al. (2016) eLife — soma-targeting of ChR2 using Kv2.1 motif
- Mattis et al. (2011) Nat Methods — comparative analysis of microbial opsins, reference photocurrents for eArch3.0 and eNpHR3.0
- Mardinly et al. (2018) Nat Neurosci — contemporaneous soma-targeted GtACR1 variant
- Sierra-Mercado et al. — BLA muscimol/extinction precedent (reference 43)

**Named models or frameworks:**
- stGtACR2 (soma-targeted GtACR2) — the principal tool developed
- stGtACR1 — red-shifted soma-targeted variant
- eGtACR2 — ER export/trafficking signal variant
- stGtACR2-PEST — destabilised variant with PEST degradation sequence
- Kv2.1 somatodendritic targeting motif
- KCC2 (potassium-chloride co-transporter 2) — chloride extruder used mechanistically
- Auditory fear conditioning / extinction paradigm (context A/B, CS-US, extinction recall)

**Brain regions:**
- Medial prefrontal cortex (mPFC)
- Basolateral amygdala (BLA)
- Nucleus accumbens (NAc)
- Hippocampus (CA1/CA3, cultured neurons)

**Keywords:**
- optogenetic inhibition
- anion-conducting channelrhodopsin (ACR)
- GtACR2 soma-targeting
- antidromic spiking
- axonal chloride reversal potential
- KCC2 co-transporter
- Kv2.1 subcellular targeting
- AAV-mediated opsin expression
- in vivo neuronal silencing
- fear extinction
- channelrhodopsin membrane trafficking
- photocurrent amplitude

### Related wiki pages
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]
