---
source_file: lampe2000_connexin43_phosphorylation.md
title: "Phosphorylation of Connexin43 on Serine368 by Protein Kinase C Regulates Gap Junctional Communication"
authors: Paul D. Lampe, Erica M. TenBroek, Janis M. Burt, Wendy E. Kurata, Ross G. Johnson, Alan F. Lau
year: 2000
journal: The Journal of Cell Biology
paper_type: empirical
contribution_type: empirical
---

### One-line summary

PKC directly phosphorylates connexin43 (Cx43) at serine 368 in vivo, and this single phosphorylation event is necessary and sufficient to shift gap junction channel conductance from ~100 pS to ~50 pS and reduce intercellular communication.

---

### Background & motivation

Gap junctions, composed of connexin proteins, mediate direct cell-to-cell exchange of small molecules and ions, and are thought to suppress tumorigenesis by enabling growth-control signals to pass between cells. Phorbol esters such as TPA activate protein kinase C (PKC), increase Cx43 phosphorylation, and decrease gap junctional communication — an effect linked to tumor promotion. However, whether PKC acts directly on Cx43 in vivo, and precisely which phosphorylation site(s) mediate the functional change at the level of individual channels, had not been established. This paper addresses that mechanistic gap by identifying the specific PKC target residue and demonstrating its causal role in channel behavior.

---

### Methods

- Metabolic labeling of rat liver epithelial T51B cells with ³²Pi, with or without TPA treatment (100 ng/ml for 30 min), followed by Cx43 immunoprecipitation and phosphoamino acid analysis.
- Two-dimensional phosphotryptic peptide mapping of Cx43 from TPA-treated cells and from immunoaffinity-purified Cx43 phosphorylated in vitro by PKC (purified from bovine brain; mixture of α, β, γ isozymes).
- HPLC purification of tryptic phosphopeptides and Edman degradation sequencing (with ³²P release tracking cycle by cycle) to identify the phosphorylated residue — both from synthetic peptide D360-I382 phosphorylated by PKC in vitro and from in vivo-labeled TPA-treated cells.
- Site-directed mutagenesis converting S368 to alanine (Cx43-S368A); stable transfection into Cx43⁻/⁻ mouse fibroblasts alongside wild-type Cx43 (Cx43wt).
- Lucifer yellow dye-transfer assays to quantify incidence and extent of intercellular coupling after TPA treatment (0–120 min, 50 ng/ml TPA).
- Dual whole-cell voltage-clamp single channel electrophysiology (transjunctional voltage 40 mV; halothane used to reduce junctional conductance); event amplitude-relative frequency histograms compiled from >600 events per condition across multiple clones.

---

### Key findings

- TPA treatment increased overall Cx43 phosphorylation approximately fivefold in T51B cells; phosphoamino acid analysis showed phosphorylation exclusively on serine.
- The major TPA-induced phosphotryptic peptide comigrated with the dominant in vitro PKC phosphorylation product, strongly implicating direct PKC action.
- Edman degradation of the purified phosphopeptide identified S368 (cycle 9 of the COOH-terminal peptide A367-R370) as the primary PKC phosphorylation site, with a secondary site at S364 at ~20% of the S368 signal.
- In vivo sequencing of the 8-min HPLC peak from TPA-treated T51B cells confirmed S368 as the dominant phosphorylated residue (cycle 2, 208 cpm vs. cycle 1, 54 cpm and cycle 3, 105 cpm).
- In Cx43wt-transfected fibroblasts, TPA reduced dye-coupling extent to 54% and 12% of baseline at 60 and 120 min, respectively. In Cx43-S368A clone pI8, coupling extent was 97% and 87% of baseline at the same time points, with no reduction in incidence of coupling.
- Single channel electrophysiology: in Cx43wt cells (and T51B cells), TPA shifted the dominant channel population from ~100 pS (76% of events under control) to ~50 pS (63% of events under TPA). In Cx43-S368A cells, ~100 pS channels remained dominant (69% of events) under both control and TPA conditions; the 50-pS population was unchanged (9–10%) regardless of TPA.
- The S368A mutation did not prevent TPA-induced inhibition of gap junction assembly, implying a separate PKC-mediated pathway targeting assembly.

---

### Computational framework

Not applicable. This is a biochemical and electrophysiological study with no explicit computational model. The results constrain mechanistic models of connexin channel gating: they provide a defined molecular switch (phosphorylation state of a single serine) that controls which conductance sub-state predominates, which is relevant to ion channel gating models and kinetic schemes for gap junction channels.

---

### Prevailing model of the system under study

The introduction establishes that, prior to this paper, it was known that: (1) Cx43 is phosphorylated at multiple serine residues in vivo; (2) TPA/PKC activation increases Cx43 phosphorylation and decreases gap junctional communication in many cell types; (3) phosphorylation affects channel assembly, turnover, and gating rather than being required for channel formation per se. However, the field had not established which specific residue(s) PKC phosphorylates directly in vivo, and had only indirect evidence (from Moreno et al., 1994 and Kwak et al., 1995) that phosphorylation shifts Cx43 toward a lower conductance state. The prevailing model was that PKC "somehow" phosphorylated Cx43 to reduce communication, but the responsible site and mechanism linking a specific phosphorylation event to a defined change in single-channel behavior were unknown.

---

### What this paper contributes

This paper resolves the identity of the primary PKC site (S368) in the COOH-terminal tail of Cx43 and provides causal evidence — through the S368A phosphorylation-deficient mutant — that this single residue is both necessary and responsible for the TPA-induced shift from the ~100-pS to the ~50-pS conductance state, and for the consequent reduction in dye-coupling permeability. Before this paper, it could only be speculated that PKC acted directly on Cx43 and that phosphorylation at a specific site altered single-channel behaviour. This work now establishes S368 as a molecular switch: phosphorylation of one residue per connexin subunit is sufficient to alter channel gating and decrease intercellular communication, providing a concrete molecular mechanism linking PKC activation and tumor promotion to gap junction suppression.

---

### Brain regions & systems

Not applicable. This paper studies gap junction channels in non-neural cell types (rat liver epithelial T51B cells and mouse fibroblasts). The level of analysis is molecular and cellular: connexin protein biochemistry and membrane electrophysiology of gap junction channels.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight at the molecular (implementational) level, though not in a neural context.

- **Computational**: The problem being "solved" by PKC-mediated phosphorylation is the transient or sustained downregulation of intercellular communication in response to mitogenic signaling (e.g., during cell cycling or in response to tumor-promoting stimuli).
- **Algorithmic**: The mechanism is a binary post-translational switch: phosphorylation of S368 by PKC changes the preferred conductance state of the Cx43 channel from ~100 pS (high-conductance, full-open) to ~50 pS (reduced conductance), decreasing the effective permeability of gap junctions. The S368A mutation data demonstrate that this single site is necessary for the conductance shift; the shift is not explained by changes in channel number or assembly at this timescale.
- **Implementational**: S368 is located in the COOH-terminal cytoplasmic tail of Cx43 (within the tryptic peptide A367-R370). PKC (α/β/γ isozymes) directly phosphorylates this site in vitro, and TPA drives phosphorylation at this site in intact cells. The data do not fully discriminate between a unitary conductance change (the 100-pS channel converts to a 50-pS channel upon phosphorylation) and a change in open probability of two distinct stable conductance states, but several observations (absence of 50-pS events in some control records; absence of 100-pS events in some TPA records; both states opening from zero current) favour a true conductance-state switch rather than a subconductance gating change.

---

### Limitations & open questions

- The data cannot rigorously distinguish between a phosphorylation-induced change in unitary conductance versus a change in open probability between two pre-existing conductance states, due to the use of halothane in all single-channel experiments, which precluded long, stable single-channel records.
- The pI9 Cx43-S368A clone showed a TPA-induced reduction in the incidence of coupling despite no change in single-channel behaviour, indicating an additional PKC-sensitive mechanism (likely gap junction assembly inhibition) that is independent of S368.
- The kinetics and subcellular location of S368 phosphorylation are unknown; preliminary data suggest some phosphorylation may occur before gap junction assembly, but this is not established.
- S364 is phosphorylated at ~20% of the S368 level in vitro; its functional role is not addressed.
- The paper does not specify which PKC isozyme(s) are responsible in vivo.
- Discrepant results in rat cardiomyocytes (Saez et al., 1997) — where S368 and S372 were phosphorylated by PKC in vitro but not in vivo under staurosporine conditions — are noted but not reconciled.
- Whether the ~50-pS population in Cx43-S368A cells reflects phosphorylation at an alternative site by another kinase is not determined.

---

### Connections & keywords

**Key citations**:
- Moreno et al. (1994) — Cx43 unitary conductance regulated by phosphorylation
- Kwak et al. (1995a, b, c) — PKC/PKG effects on Cx43 conductance and permeability
- Lampe (1994) — TPA/PKC inhibition of gap junction assembly
- Saez et al. (1997) — PKC phosphorylation of Cx43 at S368 and S372 in vitro
- Martyn et al. (1997) — Cx43 knockout cell line used as transfection host
- Goodenough et al. (1996) — Connexins, connexons, and intercellular communication (review)
- Britz-Cunningham et al. (1995) — Cx43 mutations and heart malformations

**Named models or frameworks**:
- Two-dimensional phosphotryptic peptide mapping
- Edman degradation with ³²P release tracking
- Dual whole-cell voltage clamp for gap junction single-channel analysis
- Site-directed mutagenesis (Chameleon kit, Stratagene)

**Brain regions**: Not applicable.

**Keywords**: connexin43, gap junction, protein kinase C, serine phosphorylation, S368, TPA, phorbol ester, single channel conductance, intercellular communication, tumor promotion, phosphotryptic mapping, Cx43 gating
