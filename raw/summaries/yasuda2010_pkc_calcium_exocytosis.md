---
source_file: yasuda2010_pkc_calcium_exocytosis.md
title: PKC-Dependent Inhibition of Ca2+-Dependent Exocytosis from Astrocytes
authors: Keiichi Yasuda, Makoto Itakura, Kyota Aoyagi, Tsukiko Sugaya, Etsuko Nagata, Hideshi Ihara, Masami Takahashi
year: 2010
journal: GLIA
paper_type: empirical
contribution_type: empirical
---

### One-line summary

PKC activation inhibits Ca2+-dependent exocytosis in astrocytes by phosphorylating SNAP-23 on specific serine residues, representing the opposite effect of PKC in neurons and endocrine cells.

---

### Background & motivation

Astrocytes release neurotransmitters and bioactive substances via Ca2+-dependent exocytosis, but the regulatory mechanisms of glial exocytosis remain poorly understood. While PKC positively regulates exocytosis in neurons and endocrine cells, its role in astrocyte exocytosis was unknown. This study aimed to investigate whether PKC regulates exocytosis in glial cells and identify the molecular mechanisms involved.

---

### Methods

- **Cell culture**: Primary cultured rat brain astrocytes isolated from postnatal day 2 Wistar rats; clonal rat glioma C6 cells; PC12 cells for comparison
- **Pharmacological treatments**: Phorbol 12-myristate 13-acetate (PMA) to activate PKC; bisindolylmaleimide I (BIS) to inhibit PKC; BAPTA-AM to chelate intracellular Ca2+; ATP or ionomycin to stimulate Ca2+-dependent exocytosis
- **Antibody generation**: Custom phospho-specific antibodies against SNAP-23 phosphorylated at Ser95, Ser110, Ser120, and Ser160
- **Mass spectrometry**: LC-MS/MS analysis of tryptic peptides from immunoaffinity-purified SNAP-23 to identify phosphorylation sites
- **Western blot analysis**: Detection of SNAP-23 phosphorylation and protein levels
- **hGH release assay**: Human growth hormone (hGH) expressed in astrocytes as a reporter for Ca2+- and SNARE-dependent exocytosis; hGH release measured by ELISA after ATP or ionomycin stimulation
- **Tetanus toxin (TeTX) assay**: Co-expression of TeTX light chain to cleave VAMP-2 and assess SNARE dependence of hGH release

---

### Key findings

- PMA treatment induced phosphorylation of SNAP-23 on Ser95, Ser120, and Ser160 in astrocytes and C6 cells, as identified by mass spectrometry and confirmed by phospho-specific antibodies
- Phosphorylation at Ser95, Ser120, and Ser160 was suppressed by the PKC inhibitor BIS, demonstrating PKC-dependent phosphorylation
- Ser110 of SNAP-23 was constitutively phosphorylated under basal conditions and was dephosphorylated in a PKC-dependent manner (phosphorylation decreased with PMA treatment, blocked by BIS)
- Exogenously expressed hGH accumulated in cytoplasmic granular structures in astrocytes and was released by ATP stimulation in a Ca2+- and SNARE-dependent manner (suppressed by BAPTA-AM and tetanus toxin)
- PMA treatment markedly suppressed ATP-induced hGH release from astrocytes, and this inhibition was reversed by BIS co-treatment
- Similar PKC-dependent suppression of hGH release was observed in C6 cells stimulated with ionomycin
- PKC negatively regulates Ca2+-dependent exocytosis in astrocytes, opposite to its positive regulatory role in neurons and endocrine cells

---

### Computational framework

Not applicable. This is a molecular and cellular biology study using biochemical and pharmacological approaches. The results provide empirical constraints on molecular mechanisms of vesicle trafficking but do not employ explicit computational modeling.

---

### Prevailing model of the system under study

The field understood that astrocytes release neurotransmitters and bioactive substances via Ca2+-dependent exocytosis involving SNARE proteins, with SNAP-23 (rather than SNAP-25) serving as the primary plasma membrane SNARE in astrocytes. In neurons and endocrine cells, PKC was known to positively regulate exocytosis, primarily through phosphorylation of SNAP-25 at Ser187, which enhances vesicle recruitment and neurotransmitter release. However, the regulation of glial exocytosis by protein kinases, particularly PKC, was largely unexplored, and it was unknown whether PKC would have similar or different effects in astrocytes compared to neurons.

---

### What this paper contributes

This paper establishes that PKC negatively regulates Ca2+-dependent exocytosis in astrocytes, representing the opposite functional effect from neurons and endocrine cells where PKC enhances exocytosis. The study identifies the molecular mechanism: PKC phosphorylates SNAP-23 (the astrocyte homolog of SNAP-25) at multiple serine residues (Ser95, Ser120, Ser160), while simultaneously promoting dephosphorylation of the constitutively phosphorylated Ser110. This reveals a novel inhibitory signaling pathway in glial cells and highlights that the same protein kinase can have opposite effects on exocytosis depending on cell type and the specific SNARE protein substrates available (SNAP-23 vs. SNAP-25). The findings suggest that astrocytes have evolved distinct regulatory mechanisms for vesicle trafficking compared to neurons.

---

### Brain regions & systems

Not applicable. This study uses primary cultured rat brain astrocytes (from cerebral cortex) and clonal rat glioma C6 cells. No specific anatomical circuits or intact brain systems were studied. The findings are relevant to understanding astrocyte biology in cortical and potentially other brain regions.

---

### Mechanistic insight

This paper provides mechanistic insight at the molecular level but does not fully meet the high bar for Marr's three levels because it does not present an explicit algorithm that could explain the phenomenon or provide neural data linking specific model variables to measured activity.

**What the paper does establish:**
- **Implementational level**: The study identifies specific molecular substrates (SNAP-23 serine residues: Ser95, Ser110, Ser120, Ser160) that are phosphorylated or dephosphorylated by PKC activation. It demonstrates that this phosphorylation state is coupled to the functional output (exocytosis suppression).

**Why it doesn't fully meet the bar:**
The paper does not provide an algorithmic-level account of how PKC-dependent phosphorylation of SNAP-23 mechanistically inhibits vesicle fusion. It does not distinguish between possible mechanisms (e.g., blocking SNARE complex formation, promoting SNARE complex disassembly, altering vesicle docking, or affecting vesicle priming). The correlation between phosphorylation state and exocytosis suppression is established, but the causal mechanism linking phosphorylation to the inhibition of membrane fusion remains to be elucidated.

---

### Limitations & open questions

- The study does not determine which specific PKC isoform(s) are responsible for the observed effects on SNAP-23 phosphorylation and exocytosis inhibition
- The mechanism by which PKC promotes dephosphorylation of Ser110 remains unclear—whether this involves activation of a specific phosphatase or inhibition of the kinase that maintains basal phosphorylation
- The causal relationship between specific phosphorylation sites and exocytosis inhibition is not fully established; it remains unclear whether phosphorylation at Ser95, Ser120, and/or Ser160 directly inhibits SNARE complex formation or function
- The physiological significance of PKC-dependent inhibition of astrocyte exocytosis in brain function remains unexplored—whether this serves to dampen gliotransmission under certain conditions or regulate synaptic modulation by astrocytes
- The study uses cultured cells and C6 glioma cells; whether the same PKC-dependent inhibition occurs in intact astrocytes in brain tissue is unknown

---

### Connections & keywords

**Key citations:**
- Hepp et al., 1999 - SNAP-23 expression in glial cells
- Nagy et al., 2002 - PKC-dependent phosphorylation of SNAP-25 at Ser187 in neurons
- Suzuki & Verma, 2008 - Phosphorylation of SNAP-23 Ser95 and Ser120 in mast cell degranulation
- Wick et al., 1993 - hGH assay system for evaluating exocytosis
- Li et al., 2008 - Lysosomal exocytosis in astrocytes

**Named models or frameworks:**
- SNARE complex-mediated vesicle fusion
- hGH (human growth hormone) reporter assay for exocytosis
- Phorbol ester (PMA) activation of PKC signaling

**Brain regions:**
- Cerebral cortex (source of primary astrocyte cultures)

**Keywords:**
- astrocyte exocytosis
- protein kinase C (PKC)
- SNAP-23 phosphorylation
- SNARE proteins
- gliotransmission
- calcium-dependent vesicle release
- human growth hormone (hGH) assay
- phorbol 12-myristate 13-acetate (PMA)
- vesicle trafficking
- glial cell signaling
