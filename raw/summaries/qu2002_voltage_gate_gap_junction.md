---
source_file: qu2002_voltage_gate_gap_junction.md
paper_id: qu2002_voltage_gate_gap_junction
title: "Function of the voltage gate of gap junction channels: Selective exclusion of molecules"
authors:
  - "Yang Qu"
  - "Gerhard Dahl"
year: 2002
journal: "Proceedings of the National Academy of Sciences"
paper_type: empirical
contribution_type: empirical
methods:
  - electrophysiology
keywords:
  - gap_junctions
  - connexin
  - cx46
  - cx43
  - voltage_gating
  - subconductance_states
  - permeability_selectivity
  - hemichannels
  - camp
  - fluorescent_tracers
  - second_messengers
  - cell_cell_communication
  - electrophysiology
  - xenopus_oocytes
  - function
  - voltage
  - gate
  - gap
  - junction
  - channels
---

### One-line summary

The voltage gate of gap junction channels selectively restricts the passage of larger molecules (fluorescent tracers, cAMP) while preserving electrical coupling via small ions, suggesting a physiological role in regulating metabolic versus electrical cell-cell communication.

---

### Background & motivation

Gap junction channels allow direct cell-cell communication by passing ions and small molecules (up to ~1 kDa). Most vertebrate gap junctions are regulated by transjunctional voltage (Vj), but this regulation is incomplete—channels enter subconductance states rather than fully closing, leaving electrical coupling intact. This raised a fundamental question: what is the physiological function of the voltage gate if it does not break electrical continuity? The authors hypothesized that subconductance states might have different permeability selectivity, potentially restricting larger molecules while allowing small ions to pass.

---

### Methods

- **Preparation**: Xenopus oocytes injected with connexin 46 (cx46), connexin 43 (cx43), or CFTR mRNA; incubated 18–24 hours
- **Electrophysiology**: Two-microelectrode voltage clamp to measure membrane conductance and junctional conductance
- **Fluorescent tracer studies**: Oocytes held at -20 mV or +20 mV, exposed to 1 mM fluorescent tracers (calcein, lucifer yellow, cascade blue) for 10–20 min, then cryosectioned and imaged
- **cAMP flux assay**: Coexpression of cx46 hemichannels with CFTR chloride channels as a cAMP reporter; cAMP influx through cx46 activates CFTR, producing measurable chloride current
- **Heterotypic gap junction assay**: cx46/cx43 heterotypic channels with cAMP flux monitored via CFTR in the postjunctional cell

---

### Key findings

- **Voltage-dependent tracer flux**: At +20 mV (subconductance state), influx of fluorescent tracers (calcein, lucifer yellow, cascade blue) through cx46 hemichannels was reduced to near detection threshold, while at -20 mV (full conductance), tracer uptake was robust (~4-fold higher)
- **No size/charge selectivity effect**: All three tracers (different sizes and charges) showed similar voltage-dependent reduction, suggesting the voltage gate acts as a general size-selective barrier rather than discriminating by specific chemical properties
- **cAMP flux through hemichannels**: At +20 mV, cAMP-induced membrane conductance was 21 μS versus 80 μS at -20 mV, indicating ~4-fold reduction in cAMP permeability at positive potentials
- **Preserved electrical coupling**: Macroscopic membrane conductance was actually higher at +20 mV than at -20 mV due to increased open probability, demonstrating that electrical coupling persists while molecular flux is restricted
- **Heterotypic gap junction results**: Similar voltage-dependent reduction of cAMP flux observed in complete cx46/cx43 gap junction channels, confirming the phenomenon applies to full channels not just hemichannels

---

### Computational framework

Not applicable. This is a purely empirical study using electrophysiology and fluorescence microscopy. However, the results constrain biophysical models of gap junction permeation, suggesting that subconductance states involve a physical constriction of the channel pore that differentially affects larger molecules while maintaining permeability to small ions.

---

### Prevailing model of the system under study

The prevailing model held that gap junction voltage gating serves to regulate electrical coupling between cells, with channels entering subconductance states under voltage gradient. The function of these subconductance states was unclear—whether they represented a partially closed state with reduced permeability for all molecules, or whether they had different selectivity properties. Some studies suggested subconductance states might present a slightly higher permeation barrier, while others argued that their brief duration made them physiologically irrelevant for selectivity. The prevailing assumption was that conductance and permeability were correlated—channels with different conductance states would proportionally affect all permeant molecules.

---

### What this paper contributes

This paper demonstrates that the voltage gate of gap junction channels selectively restricts the passage of larger molecules (fluorescent tracers, second messengers like cAMP) while allowing small ions to pass, thereby preserving electrical coupling. This reveals a previously unrecognized function of the voltage gate: to regulate metabolic/second messenger communication independently of electrical synchronization. The subconductance state acts as a size-selective filter rather than simply a partially closed state. This finding suggests that cells can dynamically regulate the flow of signaling molecules between them without losing electrical continuity, potentially preventing electrophoretic accumulation of charged molecules in tissues under electrical fields or blocking loss of metabolites from healthy cells into injured neighbors.

---

### Brain regions & systems

Not applicable. This study uses Xenopus oocytes as an expression system to study connexin channels. The findings are relevant to understanding gap junction function broadly across tissues including heart, nervous system, and lens (where cx46 is endogenously expressed), but no specific brain regions were studied.

---

### Mechanistic insight

This paper provides mechanistic insight at the biophysical level but does not meet the full algorithmic/mechanistic bar (no algorithmic-level model with neural data). The paper establishes:

**Biophysical mechanism**: The voltage gate of gap junction channels creates a size-selective permeability barrier in the subconductance state. The physical basis is likely a constriction of the channel pore that:
- Allows small ions (maintaining electrical conductance)
- Restricts larger molecules (~620 Da fluorescent tracers, cAMP)

**Marr's levels analysis**:
- **Computational**: The problem is regulating molecular flow between cells while maintaining electrical coupling—decoupling metabolic from electrical communication
- **Algorithmic**: The mechanism involves voltage-dependent gating transitions between full conductance and subconductance states with differential permeability
- **Implementational**: The physical implementation involves connexin channel structure, likely at the extracellular end of the pore where the voltage gate operates

---

### Limitations & open questions

- The study does not distinguish whether the reduced molecular flux is due to the subconductance state itself or to the rectification process that also occurs at positive potentials
- Mechanism at the structural level remains unresolved—how exactly does the voltage gate constrict the pore?
- Findings are based on cx46 and cx43 expressed in oocytes; whether similar selectivity properties apply to other connexins and in native tissue contexts needs further validation
- The physiological scenarios proposed (electrophoretic accumulation prevention, injury response) remain hypothetical and have not been tested in vivo
- Duration of subconductance states and their physiological relevance under dynamic conditions in native tissues is unclear

---

### Connections & keywords

**Key citations**:
- Trexler et al. 1996 (single channel properties of cx46)
- Pfahnl & Dahl 1998 (hemichannel gating mechanisms)
- Valiunas et al. 1997 (conductance ratios in different salts)
- Christ & Brink 1999 (dwell time analysis of subconductance states)
- Paul et al. 1991 (cx46 cloning and expression)
- Veenstra et al. 1994, 1995 (connexin channel conductance and permeability)

**Named models or frameworks**:
- Gap junction voltage gating (Vj gate)
- Subconductance states as permeability barriers
- CFTR reporter assay for cAMP flux

**Brain regions**: Not applicable (Xenopus oocyte expression system)

**Keywords**:
- gap junctions
- connexin
- cx46
- cx43
- voltage gating
- subconductance states
- permeability selectivity
- hemichannels
- cAMP
- fluorescent tracers
- second messengers
- cell-cell communication
- electrophysiology
- Xenopus oocytes
