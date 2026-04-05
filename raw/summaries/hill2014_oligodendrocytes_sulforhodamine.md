---
source_file: hill2014_oligodendrocytes_sulforhodamine.md
title: In vivo imaging of oligodendrocytes with sulforhodamine 101
authors: Robert A. Hill, Jaime Grutzendler
year: 2014
journal: Nature Methods
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Sulforhodamine 101 (SR101), long assumed to be an astrocyte-specific dye, also labels mature myelinating oligodendrocytes in vivo via gap-junction transfer from astrocytes.

---

### Background & motivation

SR101 has been widely used as an astrocyte-specific marker in in vivo brain imaging, often in combination with calcium-sensitive dyes to separate neuronal and astrocytic signals. Despite a caveat in the original publication, its assumed specificity for astrocytes was not rigorously challenged. The existence of gap junctions between astrocytes and oligodendrocytes raised the theoretical possibility that the dye could spread beyond astrocytes, yet this had not been directly tested. This paper fills that gap by systematically characterising which cell types are labelled by SR101 in vivo.

---

### Methods

- Three transgenic mouse lines used to identify cell types in vivo:
  - Aldh1L1-GFP (GFP exclusively in astrocytes)
  - NG2cre:ZEG (GFP in all cortical oligodendrocyte-lineage cells and vascular pericytes)
  - PLPcreER:mT/mG (membrane-bound GFP in a subset of mature myelinating oligodendrocytes after Cre induction)
- SR101 applied both topically to the cortex and via intravenous injection
- In vivo two-photon microscopy and combined confocal / spectral confocal reflectance (SCoRe) microscopy used to identify and characterise labelled cells
- Time-lapse imaging at 40 min and 140 min post-application to assess temporal dynamics of labelling
- Pharmacological gap-junction blockade with carbenoxolone to test mechanism
- Cell counts and proportions quantified by cortical depth at postnatal days 30, 90, and 210

---

### Key findings

- A substantial proportion of SR101-labelled cells in Aldh1L1-GFP mice did not express GFP (i.e. were not astrocytes), with morphology consistent with mature oligodendrocytes.
- 100% of mGFP-labelled myelinating oligodendrocytes in PLPcreER:mT/mG mice were co-labelled with SR101 (91/91 cells, 3 mice).
- SR101 labelled myelin sheaths as well as oligodendrocyte cell bodies.
- Oligodendrocyte labelling was not route-dependent: it occurred with both topical cortical application and intravenous injection.
- Time-lapse imaging showed oligodendrocyte labelling emerging between 40 and 140 min post-application, with SR101 fluorescence increasing more strongly in oligodendrocytes than in initially labelled astrocytes, consistent with transfer from astrocytes.
- Carbenoxolone (gap-junction blocker) inhibited SR101 labelling of both astrocytes and oligodendrocytes, confirming a gap-junction-dependent mechanism.
- Density of dually labelled cells varied by cortical depth and increased with age (P30, P90, P210), reflecting developmental addition of oligodendrocytes.
- Practical workaround proposed: acquiring an initial image within ~45 min of dye application captures astrocytes before oligodendrocytes are labelled, allowing the two cell types to be distinguished by timing and morphology.

---

### Computational framework

Not applicable. This is a purely experimental cell-biology/imaging study with no computational or mathematical framework. The results constrain models of glial gap-junction coupling and the design of in vivo imaging experiments that rely on cell-type-specific markers.

---

### Prevailing model of the system under study

The field assumed SR101 was a highly specific astrocyte marker suitable for in vivo two-photon imaging. Its widespread diffusion through the astrocyte syncytium via gap junctions was understood, but the dye was believed not to enter oligodendrocytes to any meaningful degree. This assumption underpinned a large body of work using SR101 to define astrocytic calcium signals and to distinguish astrocytic from neuronal activity in vivo. The existence of astrocyte-oligodendrocyte gap junctions was known, but it had not been operationally incorporated into protocols using SR101.

---

### What this paper contributes

The paper demonstrates that the foundational assumption of SR101 astrocyte specificity is incorrect: the dye reliably and substantially labels mature myelinating oligodendrocytes. This means that any past study using SR101 as a sole astrocyte identifier may have confounded astrocytic signals with oligodendrocytic ones. The paper identifies the mechanism (gap-junction transfer) and provides a practical mitigation strategy (early time-point imaging). It also opens SR101 as a tool for in vivo oligodendrocyte imaging, with the added benefit of labelling myelin sheaths.

---

### Brain regions & systems

- Cerebral cortex — primary site of SR101 application and imaging; cortical depth-dependent distribution of labelled oligodendrocytes characterised.

No specific subcortical regions are investigated. The study is focused on glial cell identity within cortical tissue rather than on circuit-level or systems-level neuroscience.

---

### Mechanistic insight

The paper meets criterion 1 (it proposes and tests a specific mechanism — gap-junction transfer from astrocytes to oligodendrocytes) and criterion 2 (it provides in vivo imaging data and pharmacological evidence directly supporting that mechanism). However, it does not address the algorithmic or computational level in any meaningful sense, as this is a cell biology finding rather than a neural computation finding.

Mapping onto Marr's levels is not the appropriate frame here; the paper instead provides a mechanistic account of a dye-labelling artefact:

- **Phenomenon**: SR101 labels mature myelinating oligodendrocytes in addition to astrocytes.
- **Mechanism**: SR101 transfers from astrocytes to oligodendrocytes via gap junctions (supported by temporal dynamics of labelling and carbenoxolone blockade).
- **Implementation**: The gap junctions between astrocytes and oligodendrocytes (previously documented by Massa & Mugnaini 1982 and Dermietzel & Spray 1993) provide the physical substrate.

No specific cell types beyond the glial classes, or molecular details of the gap junctions involved, are identified in this paper.

---

### Limitations & open questions

- The study is confined to cortex; SR101 labelling specificity in other brain regions (e.g. white matter tracts, cerebellum) is not assessed.
- The practical workaround (early time-point imaging) is proposed but not extensively validated — the 45-minute window is approximate.
- The paper does not characterise which specific connexin isoforms mediate astrocyte-oligodendrocyte SR101 transfer.
- Whether SR101 labelling of oligodendrocytes affects their function or viability is not examined.
- Past studies using SR101 are flagged as potentially compromised, but no systematic reanalysis is performed.
- The developmental trajectory (increasing oligodendrocyte labelling at P30, P90, P210) is noted but not deeply characterised.

---

### Connections & keywords

**Key citations**:
- Nimmerjahn et al., Nat. Methods, 2004 (original SR101 astrocyte-labelling report)
- Wang et al., Nat. Neurosci., 2006 (SR101 combined with calcium imaging)
- Kuchibhotla et al., Science, 2009 (SR101 combined with calcium imaging)
- Massa & Mugnaini, Neuroscience, 1982 (astrocyte-oligodendrocyte gap junctions)
- Dermietzel & Spray, Trends Neurosci., 1993 (gap junctions in brain)
- Schain, Hill & Grutzendler, Nat. Med., 2014 (SCoRe microscopy)

**Named models or frameworks**:
- Spectral confocal reflectance (SCoRe) microscopy
- Aldh1L1-GFP transgenic mouse line
- NG2cre:ZEG transgenic mouse line
- PLPcreER:mT/mG transgenic mouse line

**Brain regions**:
- Cerebral cortex

**Keywords**:
- sulforhodamine 101 (SR101)
- oligodendrocyte labelling
- astrocyte specificity
- gap junctions
- in vivo two-photon microscopy
- glial imaging
- myelin sheath labelling
- carbenoxolone
- spectral confocal reflectance microscopy
- cell-type identification
- astrocyte-oligodendrocyte coupling
- in vivo brain imaging
