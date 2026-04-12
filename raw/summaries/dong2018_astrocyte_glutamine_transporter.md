---
source_file: dong2018_astrocyte_glutamine_transporter.md
paper_id: dong2018_astrocyte_glutamine_transporter
title: "PKC-Mediated Modulation of Astrocyte SNAT3 Glutamine Transporter Function at Synapses in Situ"
authors:
  - "Wuxing Dong"
  - "Alison C. Todd"
  - "Angelika Bröer"
  - "Sarah R. Hulme"
  - "Stefan Bröer"
  - "Brian Billups"
year: 2018
journal: "International Journal of Molecular Sciences"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
  - rat
keywords:
  - snat3_sn1
  - slc38a3
  - glutamine_transporter
  - astrocyte_perisynaptic
  - protein_kinase_c_pkc
  - transporter_internalisation_endocytosis
  - glutamateglutamine_cycle
  - calyx_of_held
  - surface_biotinylation
  - fluorescence_ph_imaging
  - nedd4_2_ubiquitination
  - phorbol_ester_pma
  - neurotransmitter_recycling
  - pkc
  - mediated
  - modulation
  - astrocyte
  - snat3
  - glutamine
  - transporter
---

### One-line summary

Activation of conventional PKC isoforms rapidly reduces glutamine release from perisynaptic astrocytes by internalising the SNAT3 transporter from the plasma membrane, demonstrating a fast feedback mechanism for regulating neurotransmitter supply at synapses in situ.

---

### Background & motivation

The glutamate–glutamine cycle is essential for sustaining excitatory and inhibitory neurotransmission: astrocytes adjacent to synapses sequester glutamate and release glutamine via the transporter SNAT3 (SN1/Slc38a3), which neurons then use to regenerate glutamate and GABA. Previous work in Xenopus oocytes and cultured cell lines suggested that protein kinase C (PKC) could internalise SNAT3, but results from cultured astrocytes were inconsistent, partly because the PKC isoform profile and SNAT3 expression levels differ markedly between cultures and acutely isolated tissue. This study investigates PKC-mediated regulation of SNAT3 directly in astrocytes in situ, using acute brain slices that preserve the native perisynaptic environment.

---

### Methods

- **Preparation**: Acute brainstem slices (100–140 µm) from postnatal day 10–15 Wistar rats and C57BL/6 mice, containing the medial nucleus of the trapezoid body (MNTB) and the calyx of Held synapse.
- **SNAT3 functional assay**: Whole-cell patch-clamp of individual perisynaptic astrocytes loaded with the pH indicator HPTS; SNAT3 activity was measured as intracellular alkalinisation (ΔpHi) triggered by 5 s puff-application of 10 mM glutamine. A cocktail of receptor and channel blockers was used to isolate SNAT3-specific responses.
- **PKC activation**: Bath application of phorbol 12-myristate 13-acetate (PMA, 100–400 nM); inactive analogue 4α-PMA served as negative control. PKC inhibitors bisindolylmaleimide I (Bis I, broad) and UCN-01 (selective for conventional isoforms) were used to identify the isoform class responsible.
- **Surface biotinylation**: Sulfo-NHS-LC-biotin labelling of whole brain slices followed by streptavidin pull-down and western blotting with a custom SNAT3 antibody (55 kDa band); loading control: Na⁺/K⁺-ATPase. Quantification by ImageJ.
- **Statistics**: Linear mixed-effects ANOVA; data reported as mean ± SEM; n = individual brain slices.

---

### Key findings

- PKC activation with PMA reduced SNAT3-mediated alkalinisation to 77 ± 6% of baseline within ~20 min in live recording experiments (n = 5 rat cells; p = 0.005); controls without PMA showed no time-dependent rundown.
- Pre-incubation with 100 nM PMA for 1 h replicated the effect: alkalinisation fell to 75.0 ± 8.6% of control in rats (n = 7; p = 0.021) and 73.4 ± 6.3% in mice (n = 13; p = 0.017), confirming the result across species.
- The PKC inhibitor Bis I and the conventional-isoform-selective inhibitor UCN-01 each fully blocked the PMA effect, indicating that PKCα, PKCβI, PKCβII, or PKCγ mediates SNAT3 downregulation.
- Cell-surface biotinylation showed that PMA reduced plasma membrane SNAT3 to 67.8 ± 4.6% of control (n = 6; p = 0.014); 4α-PMA had no effect (116 ± 10%; n = 4; p = 0.30).
- The magnitude of functional reduction (~25%) closely matched the magnitude of surface protein reduction (~32%), consistent with the entire functional effect being explained by transporter internalisation rather than altered transport kinetics.
- Because mouse SNAT3 lacks the serine at position 52 (replaced by proline) that is the candidate PKC phosphorylation site in rat, direct phosphorylation of S52 is insufficient to explain internalisation; phosphorylation of an accessory trafficking protein (e.g. via Nedd4-2) is implicated.

---

### Computational framework

Not applicable. The paper is a cellular/molecular physiology study with no explicit computational framework. The results constrain models of activity-dependent regulation of synaptic glutamate supply: any quantitative model of the glutamate–glutamine cycle must incorporate a PKC-dependent trafficking term that reduces astrocytic glutamine efflux on a timescale of minutes in response to Gq-coupled receptor activation.

---

### Prevailing model of the system under study

The introduction frames the glutamate–glutamine cycle as a constitutively operating shuttle: astrocytes passively maintain SNAT3 at the plasma membrane and continuously release glutamine to replenish presynaptic glutamate and GABA pools. Dynamic regulation of SNAT3 surface expression in the native perisynaptic context was not established; prior evidence for PKC-mediated internalisation came only from heterologous expression systems and gave conflicting results in cultured astrocytes, whose PKC isoform profiles and SNAT3 expression levels differ from the in vivo situation. The implicit working model was therefore that the cycle is relatively stable, subject at most to slow transcriptional regulation.

---

### What this paper contributes

The paper establishes that SNAT3 surface expression and glutamine release are under rapid, dynamic PKC control in native perisynaptic astrocytes, not just in artificial cell systems. This shifts the prevailing model from a static shuttle to an activity-regulated one: Gq-coupled receptor activation in astrocytes (triggered by synaptic release of glutamate, ACh, noradrenaline, ATP, etc.) can reduce glutamine efflux by ~25–30% within minutes via transporter internalisation. Because GLT-1 is known to be similarly downregulated by PKC in the same perisynaptic microdomain, astrocytic PKC signalling emerges as a coordinated control point for both glutamate removal and glutamine supply, potentially forming a negative-feedback loop that suppresses further synaptic activity when the excitatory drive is high.

---

### Brain regions & systems

- **Medial nucleus of the trapezoid body (MNTB), auditory brainstem** — primary experimental site; contains the calyx of Held glutamatergic synapse used as the model synapse.
- **Calyx of Held synapse** — a large, identifiable excitatory terminal with high neurotransmitter turnover, serving as the model system for studying the glutamate–glutamine cycle at an identified synapse.
- **Perisynaptic astrocytes (MNTB)** — the cell type under study; express high levels of SNAT3 and are in intimate physical contact with the calyx.

---

### Mechanistic insight

The paper meets one of the two criteria: it identifies an algorithm (PKC-driven endocytosis that removes SNAT3 from the plasma membrane) and provides pharmacological and biochemical data (PKC inhibitors rescue function; biotinylation quantifies surface loss). It does not, however, provide neural data that distinguishes this specific trafficking algorithm from alternatives at the algorithmic level (e.g., it does not resolve whether the internalised transporters are degraded or recycled, or how quickly surface expression recovers). Accordingly the bar for full mechanistic insight is partially met:

- **Computational**: The brain (astrocyte) solves the problem of calibrating glutamine supply to match synaptic demand; PKC provides a signal for demand reduction.
- **Algorithmic**: Conventional PKC isoforms are activated (possibly by Gq-coupled receptor stimulation), leading to endocytosis of SNAT3 via a caveolin-dependent, dynamin-independent pathway likely involving Nedd4-2 ubiquitin ligase; the target of PKC phosphorylation is not SNAT3 itself (the S52 story is ruled out by the mouse data) but an upstream trafficking regulator.
- **Implementational**: Specific conventional PKC isoforms (PKCα/β/γ) expressed in astrocytes in situ; SNAT3 surface reduction measured at 55 kDa band by western blot in acute slices; timescale of ~20–30 min for full effect.

The paper does not resolve the recycling vs. degradation question, nor does it identify the precise phosphorylation target, leaving the implementational level incomplete.

---

### Limitations & open questions

- The study uses PMA as a pharmacological PKC activator; the physiological Gq-coupled receptor pathways that would activate PKC endogenously in response to synaptic activity are not directly tested.
- It is unknown whether internalised SNAT3 is degraded or recycled back to the surface, and if so, on what timescale — this matters for understanding whether the effect is transient or sustained.
- The specific conventional PKC isoform responsible is not identified beyond the class level (PKCα, β, or γ); the downstream phosphorylation target (SNAT3 itself vs. Nedd4-2 or another trafficking protein) is unresolved.
- Experiments are confined to postnatal day 10–15 animals; PKC isoform expression changes with development, so applicability to adult tissue is not established.
- Whole-tissue lysates used for biotinylation contain multiple cell types; although SNAT3 is predominantly astrocytic, minor contamination cannot be excluded.
- The functional consequence for neurotransmitter release at the adjacent calyx of Held (i.e., whether reduced glutamine supply measurably affects presynaptic glutamate or GABA levels and synaptic strength) is proposed but not directly tested here.

---

### Connections & keywords

**Key citations**:
- Todd et al. (2017, Glia) — previous characterisation of SNAT3 function in perisynaptic astrocytes at the calyx of Held, regulated by intracellular sodium.
- Balkrishna et al. (2010, Am J Physiol Cell Physiol) — PKC-induced caveolin-dependent internalisation of SNAT3 in Xenopus oocytes.
- Nissen-Meyer et al. (2011, J Neurosci) — PKC phosphorylation of S52 on rat SNAT3 and its role in membrane trafficking.
- Sidoryk-Wegrzynowicz et al. (2011, Glia) — PKCδ-mediated, slower SNAT3 internalisation in astrocyte cultures under manganese exposure.
- Billups et al. (2013, J Neurosci) — inducible presynaptic glutamine transport at the calyx of Held.

**Named models or frameworks**:
- Glutamate–GABA–glutamine cycle
- Calyx of Held synapse (model glutamatergic synapse)

**Brain regions**:
- Medial nucleus of the trapezoid body (MNTB)
- Auditory brainstem
- Calyx of Held synapse

**Keywords**:
- SNAT3 (SN1, Slc38a3)
- glutamine transporter
- astrocyte perisynaptic
- protein kinase C (PKC)
- transporter internalisation / endocytosis
- glutamate–glutamine cycle
- calyx of Held
- surface biotinylation
- fluorescence pH imaging
- Nedd4-2 ubiquitination
- phorbol ester (PMA)
- neurotransmitter recycling
