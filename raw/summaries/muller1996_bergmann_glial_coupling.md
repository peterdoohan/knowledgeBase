---
source_file: muller1996_bergmann_glial_coupling.md
title: Electrical Coupling Among Bergmann Glial Cells and Its Modulation by Glutamate Receptor Activation
authors: Thomas Müller, Thomas Möller, Jochen Neuhaus, Helmut Kettenmann
year: 1996
journal: GLIA
paper_type: empirical
contribution_type: empirical
---

### One-line summary

This study characterizes the development and modulation of gap junctional coupling between Bergmann glial cells in mouse cerebellar slices, demonstrating that coupling is developmentally regulated and modulated by pH, halothane, and glutamate receptor activation through a calcium-dependent mechanism.

### Background & motivation

Bergmann glial cells are specialized radial astrocytes in the cerebellum that play crucial roles in cerebellar development and adult brain function. While gap junctions between astrocytes are well known, the functional properties and modulation of electrical coupling in Bergmann glial cells remained poorly understood. This study addresses how gap junctional communication develops and is regulated by physiological stimuli, providing insights into glial network function and neuron-glia interactions.

### Methods

- Acute cerebellar slices from postnatal day 5-7 (young) and 20-24 (adult) mice
- Dual patch-clamp recordings from pairs of Bergmann glial cells with inter-soma distances <50 μm
- Lucifer Yellow dye injection via patch pipette to visualize coupling
- Confocal microscopy for 3D reconstruction of coupled cell arrays
- Electron microscopy of Lucifer Yellow-filled cells to localize gap junctions
- Pharmacological manipulations: NH4Cl (pH modulation), halothane, ionomycin (Ca2+ ionophore), kainate (AMPA/kainate receptor agonist)
- Voltage-clamp protocols to measure junctional conductance and coupling ratios

### Key findings

- **Developmental regulation**: No dye coupling observed at postnatal days 5-7 (n=10), but abundant coupling at days 20-24, indicating gap junction formation is developmentally regulated
- **Time-dependent coupling increase**: Dye coupling increased with time in vitro: 15% at 1 hour, 65% at 2 hours, and 82% at 4 hours after slice preparation
- **Spatial organization**: Coupled cells formed a "string of pearls" arrangement perpendicular to parallel fibers in parasagittal sections, extending across ~7 Purkinje cells
- **Gap junction distribution**: Electron microscopy revealed gap junctions were abundant in distal processes (10-30 μm from soma), rare on somata or initial processes; 11 gap junctions found on a single 35 μm process
- **Voltage independence**: Junctional conductance showed linear current-voltage relationship, indicating voltage-independent gating (consistent with connexin 43)
- **pH modulation**: Alkalinization (NH4+) increased junctional conductance to 150% of control; acidification decreased it to 70%
- **Halothane sensitivity**: Application reduced junctional conductance to 26% of control (n=8), with mostly irreversible effects
- **Calcium dependence**: Ionomycin (Ca2+ ionophore) reduced conductance to 10% of control, indicating Ca2+-dependent modulation
- **Glutamate receptor modulation**: Kainate (1 mM) reduced junctional conductance to 26% of control (n=13) within 2 seconds; this effect was abolished in Ca2+-free solution (85% of control) and enhanced with elevated extracellular Ca2+ (12 mM), indicating Ca2+ entry through AMPA/kainate receptors mediates gap junction closure
- **Passive current mediation**: Halothane reduced passive K+ currents in adult cells to 70% of control, but had no effect on voltage-gated currents in young cells, confirming that passive currents are at least partially mediated via gap junctions

### Computational framework

Not applicable. This is an empirical electrophysiology study without formal computational modeling. The results could inform models of glial network dynamics and spatial buffering of potassium in the cerebellar cortex.

### Prevailing model of the system under study

The paper builds on the established understanding that: (1) Bergmann glial cells are specialized radial astrocytes essential for cerebellar development and adult function; (2) Astrocytes throughout the brain form gap junction-coupled syncytia for ionic and metabolic homeostasis; (3) Connexin 43 is the primary gap junction protein in astrocytes; (4) Bergmann glial cells express AMPA/kainate receptors that are Ca2+-permeable; and (5) Spatial buffering of K+ by glial cells is important for maintaining neuronal excitability.

### What this paper contributes

This paper provides the first systematic characterization of gap junctional coupling in Bergmann glial cells, establishing that: (1) Coupling is developmentally regulated, emerging between postnatal days 7-20; (2) Coupled cells form a specific spatial pattern ("string of pearls") perpendicular to parallel fibers; (3) Gap junctions are predominantly located on distal processes rather than somata; (4) Junctional conductance is voltage-independent but modulated by pH, Ca2+, and neurotransmitter receptor activation; and (5) Glutamate receptor activation specifically blocks coupling through a Ca2+-dependent mechanism, revealing a novel form of neuron-glia communication that links synaptic activity to glial network function.

### Brain regions & systems

- **Cerebellum** — primary brain region studied; focus on cerebellar cortex
- **Molecular layer** — where gap junctions are abundant on distal Bergmann glial processes; contains parallel fiber-Purkinje cell synapses
- **Purkinje cell layer** — location of Bergmann glial cell somata
- **Bergmann glial cells** — specialized radial astrocytes forming the glial syncytium; express connexin 43 and AMPA/kainate receptors
- **Gap junctions** — primarily located on distal processes (10-30 μm from soma); mediate electrical and dye coupling

### Mechanistic insight

This paper provides mechanistic insight at the biophysical level, mapping evidence onto Marr's three levels:

**Computational level**: The brain maintains ionic homeostasis in the cerebellar cortex through spatial buffering networks that extend across multiple glial cells. The "string of pearls" organization of coupled Bergmann glial cells perpendicular to parallel fibers creates anisotropic spatial buffering domains aligned with Purkinje cell dendritic trees.

**Algorithmic level**: Bergmann glial cells form a functionally anisotropic syncytium through gap junctions primarily located on distal processes. The coupling strength is dynamically regulated by intracellular Ca2+ and pH, providing a mechanism for activity-dependent modulation. The specific spatial arrangement creates preferential pathways for ion flow that match the dendritic organization of Purkinje cells.

**Implementational level**: Connexin 43 forms gap junctions between Bergmann glial cell processes. These junctions are voltage-independent but modulated by pH (alkalinization increases, acidification decreases conductance), halothane (blocks), and intracellular Ca2+ (elevated Ca2+ reduces conductance). Glutamate receptor activation (specifically Ca2+-permeable AMPA/kainate receptors) triggers Ca2+ influx that closes gap junctions, linking synaptic activity to glial network function.

### Limitations & open questions

- The low measured coupling ratios (mean 0.032) may underestimate actual process-to-process coupling strength due to the spatial distribution of gap junctions distant from recorded somata
- The study focused on parasagittal slices; different coupling patterns might exist in other orientations
- The irreversibility of kainate effects in some experiments suggests possible additional mechanisms beyond simple Ca2+-dependent closure
- The functional consequences of coupling modulation for synaptic transmission and Purkinje cell excitability remain to be determined through direct experimentation
- Whether other neurotransmitters or neuromodulators affect Bergmann glial coupling was not tested
- The specific molecular mechanism linking Ca2+ influx to gap junction closure was not elucidated

### Connections & keywords

- **Key citations**: Hatten et al., 1990; Rakic, 1981; Shiga et al., 1983a,b; Palay and Chan-Palay, 1974; Müller et al., 1992, 1994; Dermietzel et al., 1989, 1991; Yamamoto et al., 1990; Connors et al., 1983; Cornell-Bell et al., 1990; Giaume et al., 1991; Hampson et al., 1992; Dowling, 1991; De Vries and Schwartz, 1989; Bennett et al., 1991; Boron and de Weer, 1976; Peinado et al., 1993; Yuste et al., 1992; Lowel et al., 1988; Innocenti and Caminiti, 1980; Scheich, 1983; Kirischuk et al., 1995; Kim et al., 1994; Enkvist and McCarthy, 1994; Jonas et al., 1994; Belliveau et al., 1991; De Blas, 1984; Fischer and Kettenmann, 1985; Sontheimer et al., 1990; Moreno et al., 1992
- **Named models or frameworks**: Spatial buffering hypothesis, Glial syncytium, Connexin 43 gap junctions, Activity-dependent modulation of gap junctions
- **Brain regions**: Cerebellum, molecular layer, Purkinje cell layer, Bergmann glial cells
- **Keywords**: Bergmann glial cells, gap junctions, electrical coupling, connexin 43, glutamate receptors, AMPA receptors, kainate, calcium signaling, cerebellum, patch clamp, Lucifer Yellow, developmental regulation, pH modulation, spatial buffering, astrocyte syncytium, neuron-glia interactions, passive conductance, voltage-independent coupling
