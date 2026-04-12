---
source_file: "solan2020_src_regulation_gap_junction.md"
paper_id: "solan2020_src_regulation_gap_junction"
title: "Src Regulation of Cx43 Phosphorylation and Gap Junction Turnover"
authors: "Joell L. Solan, Paul D. Lampe"
year: 2020
journal: "Biomolecules"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
keywords: ["lin_et_al_2001_v_src_phosphorylation_of_cx43", "lampe_et_al_2006_mapk_phosphorylation_sites", "dunn_and_lampe_2012", "2014_akt_phosphorylation_of_cx43", "solan_and_lampe_2007", "2008_cx43_phosphorylation_by_src_and_pkc", "lauf_et_al_2002", "gaietta_et_al_2002_connexin_trafficking_dynamics", "totland_et_al_2017_nedd4_ubiquitin_ligase", "girao_et_al_2007_proteasome_regulation_of_cx43_zo_1_interaction", "named_models_or_frameworks", "cx43_kinome_concept", "gap_junction_life_cycle_model_figure_8", "connexisome_annular_junction_formation_pathway", "gap_junction_scaffold_function_model_channel_dependent_vs_channel_independent_functions", "phospho_specific_subdomain_organization", "brain_regions", "not_applicable_cell_culture_study", "keywords", "connexin43"]
---

### One-line summary

Src activation promotes connexisome formation through ERK-mediated phosphorylation of Cx43 at S279/282, with proteasome inhibition counteracting Src-mediated gap junction downregulation and preserving phospho-specific subdomains.

---

### Background & motivation

Gap junctions are dynamic intercellular channels composed of connexin proteins that enable direct cell-to-cell communication. Connexin43 (Cx43), the most widely expressed gap junction protein, has a short half-life (1–3 hours) and is regulated by phosphorylation at over a dozen sites by multiple kinases. While the "Cx43 kinome" is known to regulate gap junction assembly and turnover, the spatiotemporal relationship between phosphorylation events and disassembly pathways remained poorly understood. This study aimed to elucidate how Src activation and phosphorylation events coordinate gap junction turnover mechanisms.

---

### Methods

- **Cell lines**: Normal rat kidney (NRK) epithelial cells, LA-25 cells (NRK cells with temperature-sensitive v-Src), and BWEM cells (fetal rat myocyte line expressing endogenous Cx43)
- **Live cell imaging**: Lattice light sheet microscopy (LLSM) at Janelia Research Center for high-resolution timelapse imaging of Cx43-mEmerald and Cx43-HaloTag fusion proteins
- **Pulse-chase labeling**: HaloTag system with Alexa488 (green, old Cx43) and TMR (red, new Cx43) ligands combined with immunofluorescence
- **Super-resolution microscopy**: Airyscan microscopy for phospho-specific subdomain visualization
- **Pharmacological inhibitors**: MG132 (proteasome), NH4Cl (lysosome), sodium orthovanadate (tyrosine phosphatase), cycloheximide (protein synthesis), Brefeldin A (trafficking), ALLN
- **Immunoblotting**: Quantitative analysis using phospho-specific antibodies against Cx43 phosphorylated at Y247, S262, Y265, S279/282, S325/328/330, S365, S368, and S373

---

### Key findings

- **Multiple disassembly pathways coexist**: Live cell imaging revealed at least two distinct gap junction turnover mechanisms within single cells: (1) vesicle trains leaving the plaque center followed by collapse/reorganization, and (2) shrinkage via loss of single-color vesicles (0.1–0.5 μm) without large-scale endocytic events
- **Phospho-specific subdomains exist**: Super-resolution microscopy revealed phosphorylation at S365 and Y247 (Src site) forms distinct subdomains within gap junction plaques, while pS373 appears homogenously distributed
- **Src promotes connexisome formation**: Src activation in LA25 cells doubled connexisome abundance compared to control BWEM cells; connexisomes showed high levels of both pY247 (Src site) and pS279/282 (MAPK sites)
- **Proteasome inhibition counteracts Src**: MG132 treatment restored gap junction size and number in Src-active cells to levels comparable to Src-inactive cells; pY247 levels increased 4.4-fold while pY265 decreased, suggesting pY247 is specifically preserved within gap junctions
- **Inhibitors produce distinct phospho-profiles**: Each inhibitor (proteasome, lysosomal, phosphatase, protein synthesis, trafficking) produced a unique Cx43 phosphorylation signature, consistent with spatiotemporal regulation:
  - Proteasome inhibition: increased pY247, pY265, pS279/282, pS365, pS373
  - Lysosomal inhibition: eliminated pY247/pY265, reduced pS368/pS373, increased pS279/282
  - MAPK phosphorylation (pS279/282) increased under all conditions except trafficking inhibition
  - Akt phosphorylation (pS373) was diminished in all conditions except proteasome inhibition

---

### Computational framework

Not applicable. This is an empirical study using cell biology and imaging techniques. However, the authors present a conceptual model (Figure 8) of the Cx43 life cycle that could be formalized computationally, involving:
- State transitions between homeostatic scaffold, growth-promoting scaffold, and disassembly-prone scaffold
- Phosphorylation state vectors determining transition probabilities
- Compartmental models of Cx43 trafficking (Golgi → plasma membrane → gap junction → internalization/degradation)

---

### Prevailing model of the system under study

The field understood that Cx43 gap junctions are highly dynamic structures with short protein half-lives (1–3 hours), undergoing constant assembly, remodeling, and turnover. Multiple kinases (PKC, PKA, CK1, MAPK, Src, Akt) were known to phosphorylate Cx43 at various sites, regulating assembly, channel gating, and degradation. Src activation was associated with gap junction downregulation and intercellular communication inhibition. The proteasome and lysosome were both implicated in Cx43 degradation. ZO-1 was known as a negative regulator of gap junction size. Akt phosphorylation at S373 was known to eliminate ZO-1 binding and increase gap junction size. However, the spatiotemporal organization of phosphorylation events within plaques and how different kinase activities coordinate distinct internalization pathways remained unclear.

---

### What this paper contributes

This paper establishes that multiple gap junction disassembly pathways can coexist within single cells and that kinase-mediated phosphorylation events create phospho-specific subdomains that regulate which pathway is engaged. Specifically:

1. **Phospho-specific subdomain organization**: Demonstrated that phosphorylation at S365 and Y247 (Src sites) forms distinct subdomains within gap junction plaques, while pS373 is distributed homogenously. This subdomain organization provides potential signaling nodes for cytoskeletal interaction and kinase organization.

2. **Src-driven connexisome formation**: Showed that Src activation promotes connexisome (annular junction) formation through ERK-mediated phosphorylation of S279/282, with connexisomes containing high levels of both pY247 and pS279/282. This represents a specific pathway where scaffold function is maintained while channel function is lost.

3. **Proteasome-sensitive regulation**: Discovered that proteasome inhibition rapidly counteracts Src-mediated gap junction downregulation, restoring gap junction size and number. This implicates a proteasome-sensitive factor in Src-mediated gap junction regulation and reveals that pY247 is specifically preserved within gap junctions during this process.

4. **Multiple disassembly modes**: Provided live-cell evidence that gap junctions can be disassembled through at least two distinct mechanisms: (1) connexisome formation maintaining scaffold function, and (2) disaggregation with internalization of individual connexons eliminating both channel and scaffold function. The choice between these pathways appears regulated by phosphorylation state.

5. **Conceptual model**: Proposed an integrated model where differential phosphorylation creates distinct scaffold states with different signaling properties, allowing cells to dynamically regulate both channel-dependent communication and channel-independent scaffold functions through kinase programs.

---

### Brain regions & systems

Not applicable. This study uses cell culture models (NRK epithelial cells, LA-25 cells with temperature-sensitive v-Src, BWEM fetal rat myocytes). The findings are relevant to general cell biology of gap junctions in various tissues including heart, skin, and epithelial tissues, but no specific brain regions or neural systems are studied.

---

### Mechanistic insight

This paper provides mechanistic insight at multiple levels, though it does not fully meet the high bar for Marr's three levels as it lacks a formal computational model fitted to behavior. However, it provides substantial mechanistic insight into the molecular regulation of gap junction turnover:

**Algorithmic level (partial)**: The authors propose a conceptual algorithm where phosphorylation state vectors determine gap junction fate:
- Specific phosphorylation events (Y247, S365) create subdomains within plaques
- These subdomains serve as organizational hubs for kinase interactions and cytoskeletal tethering
- The combination of phosphorylation states determines which disassembly pathway is engaged (connexisome formation vs. disaggregation)

**Implementational level**: The paper provides detailed molecular mechanisms:
- Src directly phosphorylates Cx43 at Y247, Y265, and Y313
- Src activation increases MAPK activity, leading to phosphorylation at S279/282
- These phosphorylation events regulate binding to ZO-1, NEDD4, and clathrin adaptor proteins
- Proteasome inhibition stabilizes gap junctions by preventing degradation of a factor required for gap junction maintenance
- Different phosphorylation states differentially affect proteasome vs. lysosomal degradation pathways

The paper does not meet the full Marr's levels bar because it lacks behavioral data tied to a computational model, but it provides substantial mechanistic insight into the molecular control of gap junction turnover.

---

### Limitations & open questions

- **Cell line limitations**: All experiments were conducted in cultured cell lines (NRK, LA-25, BWEM); findings need validation in primary cells and in vivo tissues
- **Temperature-sensitive Src system**: LA-25 cells use temperature-sensitive v-Src, which may not perfectly replicate physiological Src activation dynamics
- **Inhibitor specificity**: Pharmacological inhibitors (MG132, NH4Cl, etc.) have pleiotropic effects; interpretation requires caution as noted by the authors
- **Temporal resolution**: The pulse-chase experiments used 1-hour labeling intervals, which may miss rapid trafficking events
- **Cannot distinguish new vs. resident connexons**: The authors note that their system cannot distinguish between newly arriving Cx43 and connexons already in the gap junction
- **Mechanism of proteasome effect**: While proteasome inhibition restores gap junctions, the specific proteasome-sensitive factor involved remains unidentified
- **Kinase network complexity**: The interactions between Src, MAPK, Akt, and other kinases in regulating Cx43 are complex and not fully mapped
- **Functional consequences**: The impact of different disassembly pathways (connexisome vs. disaggregation) on cell signaling and behavior requires further investigation

---

### Connections & keywords

**Key citations:**
- Lin et al. 2001 (v-Src phosphorylation of Cx43)
- Lampe et al. 2006 (MAPK phosphorylation sites)
- Dunn & Lampe 2012, 2014 (Akt phosphorylation of Cx43)
- Solan & Lampe 2007, 2008 (Cx43 phosphorylation by Src and PKC)
- Lauf et al. 2002; Gaietta et al. 2002 (connexin trafficking dynamics)
- Totland et al. 2017 (NEDD4 ubiquitin ligase)
- Girao et al. 2007 (proteasome regulation of Cx43-ZO-1 interaction)

**Named models or frameworks:**
- Cx43 "kinome" concept
- Gap junction life cycle model (Figure 8)
- Connexisome (annular junction) formation pathway
- Gap junction scaffold function model (channel-dependent vs. channel-independent functions)
- Phospho-specific subdomain organization

**Brain regions:**
Not applicable (cell culture study)

**Keywords:**
connexin43, gap junction, src kinase, phosphorylation, proteasome, connexisome, annular junction, gap junction turnover, ZO-1, MAPK, live cell imaging, lattice light sheet microscopy, pulse-chase labeling, subdomain organization, NEDD4, ubiquitin, lysosome, intercellular communication
