---
source_file: delcorsso2012_cx36_camkii.md
paper_id: delcorsso2012_cx36_camkii
title: "Calmodulin dependent protein kinase increases conductance at gap junctions formed by the neuronal gap junction protein Connexin36"
authors:
  - "Cristiane del Corsso"
  - "Rodolfo Iglesias"
  - "Georg Zoidl"
  - "Rolf Dermietzel"
  - "David C. Spray"
year: 2012
journal: "Brain Research"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
  - rat
methods:
  - electrophysiology
brain_regions:
  - thalamus
keywords:
  - connexin36
  - cx36
  - electrical_synapse
  - gap_junction
  - camkii
  - calmodulin_dependent_protein_kinase_ii
  - synaptic_plasticity
  - phosphorylation
  - run_up
  - junctional_conductance
  - neuroblastoma
  - patch_clamp
  - channel_open_probability
  - calmodulin
  - dependent
  - protein
  - kinase
  - increases
  - conductance
  - gap
---

### One-line summary

CaMKII phosphorylation of Connexin36 at specific binding and phosphorylation sites is required for the "run-up" phenomenon, a 10-fold increase in junctional conductance that confers functional plasticity on electrical synapses.

### Background & motivation

Electrical synapses formed by gap junctions were historically believed to be passive intercellular conduits with little dynamic control, unlike chemical synapses which exhibit use-dependent plasticity. However, the neuronal gap junction protein Connexin36 (Cx36) exhibits a unique "run-up" phenomenon where junctional conductance increases 10-fold within 5–10 minutes after patch-clamp recording begins. This study investigates whether calmodulin-dependent protein kinase II (CaMKII) activation underlies this plasticity, given prior evidence that CaMKII binds and phosphorylates Cx36.

### Methods

- **Cell system**: Mouse neuroblastoma (Neuro2A) cells transiently transfected with rat Cx36 (either C-terminally EGFP-tagged or co-transfected with separate Cx36 and EGFP plasmids)
- **Electrophysiology**: Dual whole-cell patch clamp recording to measure junctional currents (Ij) and calculate junctional conductance (Gj = Ij/Vj)
- **Perforated patch recordings**: Using amphotericin B (100 μg/ml) to limit intracellular dialysis and test whether run-up requires diffusible cytoplasmic factors
- **Pharmacological manipulations**:
  - Intracellular Ca²⁺ chelation: BAPTA-AM (25 μM)
  - CaMKII inhibition: KN-93 (50–100 μM) and membrane-permeable TAT-CN21 peptide (50 μM)
  - Phosphatase treatment: alkaline phosphatase (1 U/ml) in pipette
  - Phosphatase inhibition: okadaic acid (6 μM) pretreatment
- **Peptide competition assays**: Synthetic peptides (200 μM in pipette) corresponding to CaMKII binding sites (CLB: aa 175–195; CTB: aa 272–292) and phosphorylation sites (CLP: aa 99–119; CTP: aa 300–321)
- **Site-directed mutagenesis**: Deletion mutants lacking CLB (Δ175–185), CTB (Δ272–292), or both; also CLP deletion

### Key findings

- Cx36 exhibits robust "run-up": junctional conductance increases ~10-fold over 5–10 minutes with a halftime of ~6.35 minutes and maximal slope of 0.45 fold/min (corresponding to ~30 channels/min accrual)
- Run-up is unique to Cx36; not observed in other connexins
- Run-up requires intracellular dialysis: perforated patch conditions showed minimal run-up, whereas subsequent break-in to whole-cell mode triggered immediate run-up
- Intracellular Ca²⁺ is necessary for run-up: Ca²⁺ ionophore (ionomycin) enhanced run-up; Ca²⁺ chelation with BAPTA-AM blocked run-up
- CaMKII is essential for run-up: KN-93 (CaMKII inhibitor) blocked run-up when applied during recording and substantially reduced it with pretreatment; membrane-permeable TAT-CN21 peptide also strongly reduced run-up
- Specific CaMKII binding sites are required: peptides corresponding to CLB and CTB binding sites strongly inhibited run-up; CTB deletion mutant and double CLB/CTB deletion mutant showed substantially reduced run-up
- Specific phosphorylation site is required: CTP peptide (corresponding to phosphorylation site S315) inhibited run-up; CTB deletion (which removes this region) blocked run-up; CLP peptide had minimal effect
- Phosphorylation state controls run-up: alkaline phosphatase in the pipette reduced junctional conductance and blocked run-up; okadaic acid (phosphatase inhibitor) did not prevent run-up, indicating that dephosphorylation prevents but ongoing phosphorylation maintains the process

### Computational framework

Not applicable. This is an empirical biophysical study investigating the molecular mechanisms of gap junction plasticity. However, the findings constrain models of electrical synapse dynamics by demonstrating that: (1) junctional conductance is not static but dynamically regulated by kinase activity, (2) CaMKII-mediated phosphorylation increases channel open probability rather than unitary conductance or channel number, and (3) the time course of plasticity follows predictable kinetics (Boltzmann-like with ~6 min halftime).

### Prevailing model of the system under study

Prior to this work, electrical synapses were widely believed to be passive, static intercellular conduits lacking the dynamic plasticity characteristic of chemical synapses. While long-term changes in electrical coupling had been observed in fish and mammalian brain (e.g., LTP at mixed synapses on Mauthner cells, long-term modulation in thalamus), the molecular mechanisms underlying such plasticity were unknown. Recent evidence had implicated CaMKII and PKA in long-term functional plasticity of gap junctions in goldfish Mauthner cells and retina, and it was known that CaMKII could bind and phosphorylate Cx36, but whether this interaction was functionally relevant for electrical synapse plasticity remained unestablished.

### What this paper contributes

This paper establishes that CaMKII phosphorylation of Cx36 is the molecular mechanism underlying the "run-up" phenomenon and confers functional plasticity on electrical synapses. Specifically: (1) It demonstrates that CaMKII activation is necessary for run-up, using pharmacological inhibitors (KN-93, TAT-CN21), (2) It identifies the specific molecular determinants—CaMKII binding sites (CLB, CTB) and phosphorylation site (CTP/S315) in Cx36's cytoplasmic domains that are required for this plasticity, (3) It shows that phosphorylation/dephosphorylation balance controls the phenomenon, and (4) It establishes that the mechanism involves increased channel open probability rather than altered unitary conductance or channel trafficking. This positions electrical synapses as possessing activity-dependent plasticity comparable to chemical synapses, with CaMKII serving as a shared molecular mechanism for synaptic plasticity at both synapse types.

### Brain regions & systems

Not applicable. This study uses transfected neuroblastoma cells (Neuro2A) as an in vitro model system. However, the paper discusses functional relevance for: (1) Retina — AII amacrine cells which express Cx36 and show similar conductance run-up (Veruki et al., 2008), (2) Goldfish Mauthner cells — where CaMKII-mediated potentiation of electrical transmission has been described, (3) Mammalian thalamus — where long-term modulation of electrical synapses occurs, and (4) Cortical pyramidal cells — potentially relevant to pre-ictal oscillatory activity.

### Mechanistic insight

This paper provides mechanistic insight into electrical synapse plasticity, though it does not fully meet the highest bar for Marr's three levels as it lacks behavioral data linking the mechanism to neural computation. However, it substantially advances understanding:

**Computational level**: The paper addresses how electrical synapses can solve the problem of activity-dependent modulation of intercellular communication. Unlike chemical synapses where plasticity modulates quantal transmission, electrical synapses must regulate continuous ionic current flow. The run-up phenomenon provides a mechanism for rapidly increasing coupling strength in response to elevated intracellular Ca²⁺, which may occur during high neuronal activity.

**Algorithmic level**: The mechanism involves CaMKII activation → binding to Cx36 at CLB and CTB sites → phosphorylation at S315 (CTP site) → increased channel open probability. The kinetics follow a Boltzmann-like function with ~6.35 min halftime and 0.45 fold/min maximal slope. This represents a positive feedback loop where Ca²⁺ influx activates CaMKII, which then strengthens electrical coupling.

**Implementational level**: The physical implementation involves specific amino acid residues in Cx36's cytoplasmic domains: the CLB site (aa 175–195) and CTB site (aa 272–292) serve as CaMKII binding regions, while the CTP site (aa 300–321, specifically S315) is the phosphorylation target. These domains show structural similarity to CaMKII regulatory subunit pseudosubstrate and pseudotarget sites, analogous to the NR2B-CaMKII interaction at NMDA receptors.

### Limitations & open questions

- The study was conducted entirely in transfected neuroblastoma cells (Neuro2A), not in native neurons or brain tissue
- Whether the mechanism involves increased channel open probability versus channel trafficking (insertion/internalization) cannot be fully distinguished, though the authors favor open probability based on rapid kinetics
- The relationship between run-up and long-term plasticity (LTP/LTD) at electrical synapses in vivo remains to be established
- Whether similar mechanisms operate at electrical synapses formed by other connexins (Cx45, Cx50, Cx57, Cx30.2) is unknown
- The physiological conditions that trigger CaMKII-mediated potentiation in native neurons (activity patterns, Ca²⁺ levels) are not defined
- Whether Mg²⁺-dependent blockade of gap junctions (analogous to NMDA receptor blockade) contributes to electrical synapse plasticity remains speculative

### Connections & keywords

- **Key citations**: Alev et al. 2008 (CaMKII binding to Cx36); Zoidl et al. 2002 (original run-up observation); Veruki et al. 2008 (similar phenomenon in retinal AII amacrine cells); Pereda et al. 1998, 2003 (CaMKII in Mauthner cell plasticity); Srinivas et al. 1999 (Cx36 unitary conductance); Bennett 1977; Connors and Long 2004 (electrical synapse reviews)
- **Named models or frameworks**: Run-up phenomenon; Long-term increase in coupling (LINC); Boltzmann kinetics of conductance increase
- **Brain regions**: Retina (AII amacrine cells); Mauthner cells (goldfish); thalamus; cortex
- **Keywords**: Connexin36, Cx36, electrical synapse, gap junction, CaMKII, calmodulin-dependent protein kinase II, synaptic plasticity, phosphorylation, run-up, junctional conductance, neuroblastoma, patch clamp, channel open probability
