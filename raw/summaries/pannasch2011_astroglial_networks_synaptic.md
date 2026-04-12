---
source_file: pannasch2011_astroglial_networks_synaptic.md
paper_id: pannasch2011_astroglial_networks_synaptic
title: "Astroglial networks scale synaptic activity and plasticity"
authors:
  - "Ulrike Pannasch"
  - "Lydia Vargová"
  - "Jürgen Reingruber"
  - "Pascal Ezan"
  - "David Holcman"
  - "Christian Giaume"
  - "Eva Syková"
  - "Nathalie Rouach"
year: 2011
journal: "Proceedings of the National Academy of Sciences"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
keywords:
  - astrocytes
  - gap_junctions
  - connexin_30
  - connexin_43
  - synaptic_transmission
  - glutamate_transporters
  - potassium_buffering
  - extracellular_space
  - long_term_potentiation
  - long_term_depression
  - silent_synapses
  - hippocampus
  - tripartite_synapse
  - neuroglial_interactions
  - synaptic_scaling
  - astroglial
  - networks
  - scale
  - synaptic
  - activity
key_citations:
  - rouach2008_astrocyte_metabolism
---

### One-line summary

Astroglial gap junction networks, mediated by connexin 30 and connexin 43, tonically suppress hippocampal synaptic transmission by facilitating extracellular glutamate and potassium clearance, thereby controlling synaptic strength and plasticity.

### Background & motivation

Astrocytes dynamically interact with neurons to regulate synaptic transmission, but their role has primarily been considered at the level of individual cells. A distinctive feature of astrocytes is their network organization via gap junction channels formed by connexin 30 (Cx30) and connexin 43 (Cx43), which enable intercellular exchange of ions and small signaling molecules. While previous studies showed behavioral impairments and pathological alterations in connexin knockout mice, the specific role of astroglial networks in basal synaptic transmission and plasticity remained unknown.

### Methods

- **Animal model**: Double-knockout mice lacking both Cx30 and astroglial Cx43 (Cx30−/− Cx43−/−), with conditional deletion of Cx43 in astrocytes and total deletion of Cx30; wild-type littermate controls (P16–P25)
- **Electrophysiology**: 
  - Field EPSP recordings from CA1 Schaffer collateral synapses
  - Whole-cell voltage clamp recordings of EPSCs and IPSCs in CA1 pyramidal neurons
  - Paired-pulse facilitation measurements
  - Minimal stimulation to assess silent synapses
  - LTP induction (two 1-s trains of 100 Hz, 20 s apart)
  - LTD induction (1-Hz stimulation for 15 min)
- **Astrocyte recordings**: Simultaneous recording of glutamate transporter (GLT) currents and potassium currents in astrocytes during synaptic stimulation
- **Pharmacology**: Local AMPA application, D-AP5, CNQX, cyclothiazide, D-serine, DPCPX, RS-CPP, D-AA
- **Morphological analysis**: NeuN and S100 immunostaining, GFAP immunoreactivity, vimentin staining, sulforhodamine 101 labeling
- **Extracellular space measurements**: Tetramethylammonium (TMA+) ion-selective microelectrodes during synaptic stimulation

### Key findings

- **Disruption of astroglial gap junctions increases synaptic transmission**: Cx30−/− Cx43−/− mice showed ~100% increase in basal excitatory transmission (fEPSP slope/fiber volley ratio, P < 0.05), with EPSC amplitude increased from −51 ± 5 pA (WT) to −114 ± 5 pA (double-knockout, P < 0.001)
- **Enhanced inhibitory transmission**: IPSCs were also increased in double-knockout mice (241 ± 19 pA vs. 83 ± 13 pA in WT, P < 0.001), indicating general augmentation of synaptic transmission
- **Increased release probability**: Paired-pulse facilitation was decreased in double-knockout mice (1.5 ± 0.05 vs. 1.7 ± 0.06 in WT, P < 0.05), indicating increased presynaptic release probability
- **Enhanced postsynaptic AMPAR density**: The AMPA/NMDA ratio was increased by ~80% in double-knockout mice (4.1 ± 0.5 vs. 2.3 ± 0.2 in WT, P < 0.001). Local AMPA application revealed ~40% increase in whole-cell current amplitude (−705 ± 64 pA vs. −493 ± 46 pA in WT, P < 0.05)
- **Reduced silent synapses**: Minimal stimulation revealed reduced failure rate and increased EPSC amplitude in double-knockout mice, indicating conversion of silent synapses to functional ones
- **Impaired LTP and enhanced LTD**: LTP was nearly absent in double-knockout mice (~80% decrease compared to WT, P < 0.005), while LTD magnitude was increased by ~100% (P < 0.05). LTP could be restored by prior depotentiation
- **Impaired glutamate clearance**: Astroglial glutamate transporter (GLT) currents showed ~86% increased amplitude but slower decay kinetics. Deconvolution-derived glutamate clearance was nearly two times slower in double-knockout mice (10 ± 1.4 ms vs. 5.2 ± 0.9 ms in WT, P < 0.05)
- **Impaired potassium buffering**: Astrocytic potassium currents showed ~79% increased amplitude, but extracellular potassium rise was ~110% higher during comparable neuronal activity. Potassium clearance showed ~3-fold increased decay time and half-width
- **Reduced extracellular space volume**: During 10 Hz/10 s stimulation, relative decrease in ECS volume was doubled in double-knockout mice (P < 0.0001), with increased half-decay time of TMA+ responses
- **Astrocyte hypertrophy and reactivity**: Cx30−/− Cx43−/− astrocytes showed hypertrophy, larger domain areas (1900 ± 10 μm² vs. 1200 ± 5 μm² in WT), elongated processes, enhanced GFAP immunoreactivity, and vimentin expression (indicating reactive gliosis)
- **No developmental defects**: Normal hippocampal architecture, comparable densities of CA1 pyramidal neurons and astrocytes, similar levels of synaptophysin and PSD-95, and unchanged intrinsic membrane properties of neurons and astrocytes indicated that effects were not due to major developmental abnormalities

### Computational framework

Not applicable. This is an empirical study investigating the role of astroglial gap junction networks in synaptic physiology. However, the findings constrain models of tripartite synapse function and extracellular homeostasis, suggesting that biophysical models of synaptic transmission should incorporate astroglial network-mediated clearance of glutamate and potassium, as well as activity-dependent changes in extracellular space volume.

### Prevailing model of the system under study

Prior to this study, the field understood that astrocytes modulate synaptic transmission and plasticity primarily through the activity of individual astrocytes. While gap junction-mediated astroglial networks were known to enable intercellular communication and exchange of ions and small molecules, their specific role in regulating basal synaptic transmission and plasticity under physiological conditions was unknown. The prevailing view held that individual astrocyte functions (glutamate uptake, potassium buffering, gliotransmitter release) were the primary mechanisms of neuroglial interaction, without considering the network-level organization as a critical factor in extracellular homeostasis and synaptic scaling.

### What this paper contributes

This paper establishes that astroglial gap junction networks, mediated by connexin 30 and connexin 43, are essential for maintaining extracellular homeostasis and scaling synaptic activity in the hippocampus. Specifically:

1. **Network-level function**: The study demonstrates that astroglial network connectivity is required for efficient clearance of extracellular glutamate and potassium during synaptic activity. Disconnected astrocytes can take up these substances but cannot redistribute them via the network, leading to accumulation, cellular swelling, and reduced clearance rates.

2. **Bidirectional synaptic control**: Astroglial networks limit both excitatory and inhibitory transmission by controlling presynaptic release probability and postsynaptic AMPA receptor density. The increased extracellular potassium and glutamate levels in network-deficient mice enhance neuronal excitability and transmitter release.

3. **Synaptic plasticity regulation**: The study reveals that astroglial network dysfunction occludes LTP and enhances LTD by converting silent synapses to functional ones during development. This shift in the LTP/LTD balance has implications for learning and memory, consistent with behavioral impairments previously observed in these mice.

4. **Extracellular space dynamics**: The work demonstrates that astroglial network-mediated clearance and volume regulation are critical for maintaining extracellular space volume during neuronal activity. Network disruption causes astrocyte swelling and ECS shrinkage, further concentrating extracellular neuroactive substances.

### Brain regions & systems

- **Hippocampus CA1** — primary site of investigation; site of altered synaptic transmission, plasticity, and astrocyte function in Cx30/Cx43 double-knockout mice
- **Hippocampus CA3** — source of Schaffer collateral inputs to CA1; location of presynaptic terminals with increased release probability
- **Stratum radiatum** — region of CA1 where electrophysiological recordings and astrocyte morphological analyses were performed
- **Dentate gyrus** — mentioned as having reduced radial glia-like cells and granule neurons in double-knockout mice (though not a focus of this study)

### Mechanistic insight

This paper provides substantial mechanistic insight into how astroglial networks regulate synaptic transmission, meeting the criteria of presenting a process that explains the phenomenon with supporting neural data.

**Computational level**: The brain must solve the problem of maintaining extracellular homeostasis during synaptic activity to prevent excessive neuronal excitation and ensure proper synaptic communication. Astroglial networks address this by providing a distributed system for glutamate and potassium clearance that scales with network activity.

**Algorithmic level**: The proposed mechanism involves:
1. **Intercellular redistribution**: Gap junction-coupled astrocytes form a functional syncytium that redistributes accumulated potassium and glutamate from active regions to distal astrocytes
2. **Enhanced clearance capacity**: Network connectivity enables more efficient removal of extracellular glutamate through GLTs and potassium through spatial buffering
3. **Volume regulation**: Proper clearance prevents astrocyte swelling and maintains extracellular space volume, facilitating diffusion of neuroactive substances
4. **Activity-dependent scaling**: The system dynamically adjusts to synaptic activity levels, limiting both excitatory and inhibitory transmission proportionally

**Implementational level**: The physical implementation involves:
- **Connexin 30 and 43**: Gap junction proteins forming hemichannels and intercellular channels between astrocytes, with Cx43 present from embryonic stages and Cx30 expressed later in development
- **Glutamate transporters (GLT/EAAT2)**: Located on astrocyte membranes, these show ~86% increased current amplitude but slower decay kinetics when networks are disrupted
- **Potassium channels**: Including Kir4.1, mediating spatial buffering, with ~79% increased current amplitude but prolonged clearance in disconnected astrocytes
- **Cellular morphology**: Network disruption causes astrocyte hypertrophy (50% larger domain areas), process elongation, and reactive gliosis (vimentin expression)
- **Extracellular space dynamics**: Disruption causes ~100% greater reduction in ECS volume during activity and ~3-fold slower recovery

The paper provides direct neural evidence linking these implementational mechanisms to synaptic and network outcomes through comprehensive electrophysiological recordings from both neurons and astrocytes, combined with morphological and extracellular measurements.

### Limitations & open questions

- **Developmental compensation**: While the authors note no major developmental defects, subtle developmental alterations cannot be completely ruled out as contributing factors
- **Cell-autonomous vs. network effects**: The study cannot fully dissociate cell-autonomous effects of connexin deletion from network-level effects, as both are disrupted simultaneously
- **Regional specificity**: The study focuses on hippocampal CA1; whether similar mechanisms operate in other brain regions with different connexin expression patterns remains to be determined
- **Behavioral correlates**: While the authors cite previous behavioral impairments in these mice, direct correlation between the synaptic changes observed and specific behavioral deficits was not examined
- **Therapeutic implications**: The potential for targeting connexin function or astroglial networks in neurological conditions involving excitotoxicity or epilepsy remains unexplored
- **Molecular mechanisms of swelling**: The precise molecular pathways linking connexin deletion to astrocyte hypertrophy and reactive gliosis are not identified

### Connections & keywords

- **Key citations**: Perea & Navarrete & Araque 2009 (tripartite synapses), Giaume et al. 2010 (astroglial networks), Theis et al. 2003 (Cx43 knockout behavior), Lutz et al. 2009 (dysmyelinating phenotype), Rouach et al. 2008 (metabolic networks), Wallraff et al. 2006 (potassium buffering), Kerchner & Nicoll 2008 (silent synapses and LTP), Diamond 2005 (glutamate clearance), Turrigiano 2008 (synaptic scaling)
- **Named models or frameworks**: Tripartite synapse, astroglial metabolic networks, silent synapse hypothesis, synaptic scaling, spatial potassium buffering
- **Brain regions**: Hippocampus CA1, hippocampus CA3, stratum radiatum, dentate gyrus
- **Keywords**: astrocytes, gap junctions, connexin 30, connexin 43, synaptic transmission, glutamate transporters, potassium buffering, extracellular space, long-term potentiation, long-term depression, silent synapses, hippocampus, tripartite synapse, neuroglial interactions, synaptic scaling
