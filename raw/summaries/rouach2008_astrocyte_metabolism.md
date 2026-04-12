---
source_file: rouach2008_astrocyte_metabolism.md
paper_id: rouach2008_astrocyte_metabolism
title: "Astroglial Metabolic Networks Sustain Hippocampal Synaptic Transmission"
authors:
  - "Nathalie Rouach"
  - "Annette Koulakoff"
  - "Veronica Abudara"
  - "Klaus Willecke"
  - "Christian Giaume"
year: 2008
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - mouse
brain_regions:
  - hippocampus
  - hippocampus_ca1
keywords:
  - astrocytes
  - gap_junctions
  - connexin_43
  - connexin_30
  - glucose_metabolism
  - lactate
  - metabolic_coupling
  - hippocampus
  - synaptic_transmission
  - energy_metabolism
  - neuroglial_interaction
  - glut1
  - ampa_receptors
  - glutamate
  - epilepsy
  - hemichannels
  - perivascular_endfeet
  - neuron_astrocyte_metabolic_network
  - 2_nbdg
  - astroglial
---

### One-line summary

Gap junctions formed by connexin 43 and 30 enable activity-dependent intercellular trafficking of glucose and its metabolites through astroglial networks to sustain glutamatergic synaptic transmission during glucose deprivation.

### Background & motivation

Astrocytes provide metabolic substrates to neurons in an activity-dependent manner, but the molecular mechanisms and role in synaptic transmission remain unclear. Astrocytes take up glucose from blood via perivascular endfeet and provide physical links between vasculature and synaptic terminals. Additionally, astrocytes form extensive networks through gap junctions. This study investigated whether gap junction connectivity contributes to metabolic support of neurons.

### Methods

- **Immunohistochemistry**: Cx43 and Cx30 staining in mouse hippocampus (P16) combined with GFAP labeling to visualize perivascular endfeet
- **Whole-cell patch clamp recordings**: Of perivascular astrocytes in hippocampal slices from wild-type and knockout mice
- **Dye diffusion assays**: Sulforhodamine-B, Lucifer yellow, biocytin to measure gap-junction coupling; 2-NBDG and 6-NBDG (fluorescent glucose derivatives) to measure glucose trafficking
- **Pharmacological manipulations**: Carbenoxolone (gap-junction blocker), TTX (activity blocker), CNQX (AMPAR antagonist), CPP (NMDAR antagonist), 4-CIN (lactate transport inhibitor)
- **Extracellular recordings**: fEPSPs evoked by Schaffer collateral stimulation to measure synaptic transmission
- **Genetic models**: Cx30−/−, Cx43(fl/fl):GFAP-cre, and double-knockout Cx30−/−Cx43(fl/fl):GFAP-cre mice

### Key findings

- Cx43 and Cx30 are enriched in perivascular astrocyte endfeet, forming honeycomb patterns around blood vessels (Fig. 1A)
- Functional gap-junction coupling between perivascular astrocytes is extensive (58±10 cells after 20 min) and blocked by carbenoxolone (Fig. 1B-D, H)
- 2-NBDG (fluorescent glucose) traffics through astroglial networks when dialyzed into perivascular astrocytes (52±5 cells, n=19) (Fig. 1E, H)
- Glucose trafficking is mediated by Cx30 and Cx43: reduced ~35% in Cx30−/−, ~50% in Cx43(fl/fl):GFAP-cre, and completely abolished in double-knockout mice (Fig. 1H)
- 2-NBDG-6P (phosphorylated metabolite) trafficking is decreased ~70% compared to 2-NBDG, suggesting gap-junction selectivity for non-phosphorylated glucose (Fig. 1H)
- TTX (blocking spontaneous activity) decreases 2-NBDG diffusion by ~35%; CNQX (AMPAR antagonist) reduces coupling by ~25% (Fig. 2E)
- Epileptiform activity (0 Mg2+ + picrotoxin) increases 2-NBDG diffusion by ~40%, an effect blocked by AMPA and NMDA receptor antagonists (Fig. 2E)
- Evoked activity (Schaffer collateral stimulation, 1 Hz, 15 min) increases 2-NBDG trafficking by ~50%, mediated by AMPA receptors (Fig. 2E)
- Activity-dependent regulation is specific to glucose: sulforhodamine-B and biocytin trafficking are not regulated by neuronal activity (Fig. 2F)
- Local energetic demand shapes metabolic networks: when 2-NBDG is delivered to stratum oriens astrocytes and Schaffer collaterals are stimulated in stratum radiatum, glucose diffusion extends to stratum radiatum (almost doubled compared to control) (Fig. 3)
- During exogenous glucose deprivation (EGD), intracellular glucose delivery to astrocytic networks prevents fEPSP depression in wild-type mice (~50% depression without glucose, no depression with glucose) (Fig. 4C, E, G)
- Glucose delivery does not prevent fEPSP depression in Cx30−/−Cx43−/− double-knockout mice (Fig. 4D, F, G)
- Lactate transport inhibitor 4-CIN blocks the protective effect of glucose, indicating glucose is metabolized to lactate for neuronal use (Fig. 4G)
- Direct lactate delivery to astrocytic networks also prevents fEPSP depression during EGD (Fig. 4G)
- Astroglial glycogen stores and metabolic capacity are comparable between wild-type and double-knockout mice (Fig. 4E, F)
- Hemichannel involvement was ruled out: ethidium bromide uptake showed no difference between control and EGD conditions (fig. S5)
- Glucose trafficking through astroglial networks can partially sustain epileptiform activity during EGD (31% of bursts maintained vs. almost total abolition without glucose) (fig. S6)

### Computational framework

Not applicable. This is an empirical study characterizing the biophysical and molecular mechanisms of metabolic coupling between astrocytes and neurons. The findings provide constraints for future computational models of neuron-glia metabolic coupling and astrocytic network function.

### Prevailing model of the system under study

The classical model of astroglial energy metabolism viewed astrocytes as single entities that take up glucose from blood vessels and provide metabolic support to neurons. This paper identifies that astrocytes are extensively coupled through gap junctions formed by connexin 43 and 30, forming functional metabolic networks that enable intercellular trafficking of glucose and its metabolites. The prevailing understanding did not include the role of gap-junction-mediated networks in activity-dependent metabolic support.

### What this paper contributes

This paper establishes that connexin 43 and 30 gap junctions form the molecular basis for perivascular astroglial metabolic networks that enable activity-dependent intercellular trafficking of glucose and lactate. The findings demonstrate that: (1) glucose trafficking is selective for non-phosphorylated glucose, (2) trafficking is regulated by glutamatergic synaptic activity via AMPA receptors, (3) local energetic demands reshape the spatial extent of metabolic networks, and (4) this pathway is essential for sustaining synaptic transmission and epileptiform activity during glucose deprivation. The work extends the classical model by showing that astrocytes function as coordinated networks rather than isolated cells, providing a more efficient pathway for delivering energetic metabolites from blood vessels to distal active neurons.

### Brain regions & systems

- **Hippocampus** — primary brain region studied; CA1 area specifically for synaptic transmission and fEPSP recordings
- **Stratum radiatum** — hippocampal layer where Schaffer collateral stimulation was performed and where astrocytic glucose diffusion was measured
- **Stratum oriens** — hippocampal layer where perivascular astrocytes were recorded and where glucose delivery was initiated
- **Stratum pyramidale** — hippocampal layer containing pyramidal cell bodies, used as a reference for positioning recordings
- **Perivascular astrocytes** — specifically studied for their role in glucose uptake from blood vessels and distribution through gap junctions

### Mechanistic insight

This paper meets the bar for mechanistic insight by providing both an algorithmic process (gap-junction-mediated metabolic trafficking) and extensive neural data supporting it.

**Computational**: The brain solves the problem of efficiently delivering energetic metabolites from blood vessels to sites of high neuronal demand. The computational goal is to maintain synaptic transmission during periods of high activity or glucose deprivation.

**Algorithmic**: The process involves: (1) glucose uptake by perivascular astrocytes via GLUT1 transporters in endfeet, (2) intercellular trafficking through gap junctions formed by Cx43 and Cx30, (3) activity-dependent regulation via glutamate-activated AMPA receptors that increase glucose diffusion gradients toward active synapses, (4) glycolytic conversion of glucose to lactate in astrocytes, and (5) lactate release via monocarboxylate transporters for neuronal uptake and utilization.

**Implementational**: The physical implementation uses: (1) connexin 43 and 30 proteins forming gap junctions between astrocytes, enriched in perivascular endfeet, (2) glucose transporter-1 (GLUT1) in perivascular endfeet for glucose uptake from blood, (3) AMPA receptors on neurons (not astrocytes) that respond to glutamate release, (4) monocarboxylate transporters for lactate release, and (5) selective permeability of gap junctions preferring non-phosphorylated glucose over glucose-6-phosphate.

### Limitations & open questions

- The study focuses on hippocampal CA1; whether similar mechanisms operate in other brain regions remains to be determined
- The exact molecular mechanism by which neuronal activity (via AMPA receptors) regulates glucose trafficking is not fully elucidated—whether it involves direct signaling or metabolic demand gradients is unclear
- The relative contribution of lactate versus glucose as the final energetic substrate delivered to neurons was not quantitatively determined
- Whether hemichannels (as opposed to full gap junctions) contribute to metabolite release under pathological conditions remains uncertain
- The long-term consequences of disrupting astroglial metabolic networks for neuronal survival and circuit function were not investigated
- Potential therapeutic targeting of astroglial metabolic networks for epilepsy treatment requires further validation

### Connections & keywords

**Key citations**:
- Tsacopoulos & Magistretti 1996 — foundational work on metabolic coupling between glia and neurons
- Pellerin & Magistretti 1994 — lactate shuttle hypothesis
- Giaume & McCarthy 1996 — astroglial gap junctions and intercellular communication
- Nagy & Rash 2000 — connexin distribution in brain
- Simard et al. 2003 — perivascular astrocyte endfeet and connexin 43

**Named models or frameworks**:
- Astrocyte-neuron lactate shuttle (ANLS) — extended by this work to include gap-junction-mediated networks
- Metabolic coupling — the concept of functional metabolic interaction between glia and neurons
- Gap-junction-mediated metabolic networks — the novel framework proposed in this paper

**Brain regions**:
- Hippocampus, CA1, stratum radiatum, stratum oriens, stratum pyramidale, perivascular astrocytes

**Keywords**:
- astrocytes, gap junctions, connexin 43, connexin 30, glucose metabolism, lactate, metabolic coupling, hippocampus, synaptic transmission, energy metabolism, neuroglial interaction, GLUT1, AMPA receptors, glutamate, epilepsy, hemichannels, perivascular endfeet, neuron-astrocyte metabolic network, 2-NBDG
