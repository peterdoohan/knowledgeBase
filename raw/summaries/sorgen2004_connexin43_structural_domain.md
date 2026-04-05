---
source_file: sorgen2004_connexin43_structural_domain.md
title: Structural Changes in the Carboxyl Terminus of the Gap Junction Protein Connexin43 Indicates Signaling between Binding Domains for c-Src and Zonula Occludens-1
authors: Paul L. Sorgen, Heather S. Duffy, Prangya Sahoo, Wanda Coombs, Mario Delmar, David C. Spray
year: 2004
journal: Journal of Biological Chemistry
paper_type: empirical
contribution_type: empirical
---

### One-line summary

NMR structural analysis reveals that the connexin43 carboxyl-terminal domain (Cx43CT) is primarily an elongated random coil with two alpha-helical regions, and that binding of c-Src SH3 domain induces long-range structural changes that can displace the ZO-1 PDZ-2 complex, demonstrating signaling between distal binding domains.

### Background & motivation

Gap junction protein connexin43 (Cx43) is regulated by multiple binding partners including c-Src and zonula occludens-1 (ZO-1). While c-Src can disrupt the Cx43-ZO-1 interaction leading to down-regulation of gap junction communication, the binding sites for ZO-1 and c-Src are ~100 residues apart on the Cx43CT. The structural mechanisms enabling communication between these distal domains were unknown, as was the overall structure of the Cx43 cytoplasmic domains.

### Methods

- Recombinant expression and purification of Cx43CT (residues 255–382), [15N]Cx43CT, [15N,13C]Cx43CT, c-Src SH3 domain, and ZO-1 PDZ-2 domain
- NMR spectroscopy at 7°C using Bruker DRX-300, DRX-600, and Varian INOVA 600 MHz spectrometers
- 15N-NOESY-HSQC and 13C-NOESY-HSQC for distance constraints
- Temperature dependence studies (7–37°C) to identify hydrogen bonds
- Structure calculation using simulated annealing with torsion angle dynamics (CNS software)
- NMR titration experiments with unlabeled binding partners to identify interaction-induced structural changes
- Peptide competition experiments to verify specificity of interactions

### Key findings

- Cx43CT exists primarily as an elongated random coil with two regions of alpha-helical structure (residues Ala-315–Thr-326 and Asp-340–Ala-348), determined by NMR at pH 5.8, 7°C
- Root mean square deviations for helical alignments were 0.27 Å and 0.34 Å for backbone atoms
- ZO-1 PDZ-2 domain binding affected the last 19 Cx43CT residues (Ser-364–Ile-382), a region larger than the previously reported PDZ binding motif (final 4 amino acids)
- c-Src SH3 domain binding affected multiple distal regions: Lys-264–Lys-287 (contains canonical SH3 binding PXXP motif), Ser-306–Glu-316, His-331–Phe-337, Leu-356–Val-359, and Ala-367–Ser-372
- Only region Lys-264–Lys-287 contains the previously reported SH3 binding domain; the other four affected regions represent long-range conformational changes
- Region Ala-367–Ser-372 overlaps with the ZO-1 PDZ-2 binding region, suggesting a mechanism for c-Src-mediated displacement of ZO-1
- SH3 domain could partially displace the Cx43CT-PDZ-2 complex, as evidenced by reappearance of NMR resonance peaks upon SH3 addition
- Peptide competition experiments confirmed specificity of interactions

### Computational framework

Not applicable. This is a structural biology study using NMR spectroscopy and simulated annealing for structure determination. The results provide empirical constraints that could inform future computational models of gap junction regulation and intrinsically disordered protein interactions.

### Prevailing model of the system under study

Prior to this study, the field understood that: (1) Cx43 gap junction channels are regulated by multiple binding partners including ZO-1 and c-Src; (2) c-Src can disrupt the Cx43-ZO-1 interaction, leading to down-regulation of gap junction intercellular communication; (3) binding sites for ZO-1 and c-Src on Cx43CT were mapped to different regions via site-directed mutagenesis (ZO-1 binds near the C-terminus, c-Src SH3 binds near residue 280); (4) the cytoplasmic domains of Cx43 were structurally uncharacterized. The prevailing assumption was that protein-protein interactions could be understood primarily through mapping binding motifs in the primary sequence.

### What this paper contributes

This paper provides the first structural characterization of a connexin domain and demonstrates that signaling between distal binding domains occurs through long-range conformational changes in an intrinsically disordered protein. Specifically: (1) Cx43CT is primarily an elongated random coil with two alpha-helical regions, characteristic of intrinsically disordered proteins; (2) ZO-1 PDZ-2 binding affects a larger region than the minimal PDZ binding motif; (3) c-Src SH3 binding induces structural changes spanning the entire Cx43CT, including regions distal to the canonical binding site; (4) the structural overlap between SH3-affected regions and the PDZ-2 binding site provides a mechanism for c-Src-mediated displacement of ZO-1 without requiring direct SH3-PDZ-2 interaction; (5) the disordered nature of Cx43CT enables high specificity with low affinity interactions, facilitating rapid switching between binding partners. This establishes a new paradigm for understanding how intrinsically disordered domains can mediate allosteric signaling between spatially separated binding sites.

### Brain regions & systems

Not applicable. This study uses recombinant protein biochemistry and NMR spectroscopy with purified Cx43CT domains and binding partners. Cx43 is expressed in various tissues including heart and brain, but no specific neural circuits or brain regions are investigated in this paper.

### Mechanistic insight

This paper provides mechanistic insight at the molecular level but does not meet the dual criteria of presenting a formal algorithm AND providing neural data supporting that algorithm over alternatives. The paper does provide:

**Computational level**: The problem being solved is how to regulate gap junction intercellular communication in response to pathophysiological stimuli. The paper proposes that this requires rapid switching between binding partners (ZO-1 for stabilization, c-Src for down-regulation).

**Algorithmic level**: The mechanism involves an intrinsically disordered domain (Cx43CT) that undergoes disorder-to-order transitions upon binding. The conformational ensemble enables long-range allosteric communication between distal binding sites through: (1) overlapping binding regions (residues 367–372 affected by both SH3 and PDZ-2), and (2) propagated structural changes throughout the disordered domain.

**Implementational level**: The implementation involves specific protein domains (SH3 domain of c-Src, PDZ-2 domain of ZO-1) binding to the Cx43CT (residues 255–382). The two alpha-helical regions in Cx43CT (315–326 and 340–348) may form a coiled-coil in the dimerized state, contributing to the "ball-and-chain" mechanism of chemical gating.

The paper does not provide neural recordings or behavioral data that would constrain the algorithmic model against alternatives.

### Limitations & open questions

- The NMR structure was determined for a soluble recombinant Cx43CT domain (residues 255–382), not the full-length membrane-bound protein; the N-terminal region of Cx43CT (near the membrane) may have different structure when attached to transmembrane domains
- The structure was determined at pH 5.8 and 7°C to match acidic conditions that induce dimerization, but this may not reflect physiological pH conditions
- The structure represents a monomer; dimerization (relevant for the "ball-and-chain" model) was observed but insufficient intermolecular NOEs prevented modeling of the dimer interface
- The mechanism of long-range structural changes induced by SH3 binding (allostery in a disordered domain) is hypothesized but not fully explained
- Whether phosphorylation of residues in the 364–371 region affects binding affinities to intracellular ligands remains to be determined
- The functional significance of the helical domains in channel gating is speculative; direct evidence for a coiled-coil in the physiological context is lacking

### Connections & keywords

- **Key citations**: Toyofuku et al. 2001 (Cx43-ZO-1 interaction), Duffy et al. 2004 (pH-dependent cross-talk), Kanemitsu et al. 1997 (Src SH3 binding), Calero et al. 1998 (Src interaction), Unger et al. 1999 (Cx43 membrane structure), Morley et al. 1996 (ball-and-chain model), Ek-Vitorin et al. 1996 (pH gating)
- **Named models or frameworks**: ball-and-chain model (chemical gating), disorder-to-order transition, intrinsic disorder, PDZ domain binding, SH3 domain binding, multimolecular complex
- **Brain regions**: Not applicable (recombinant protein study; Cx43 expressed in heart and brain)
- **Keywords**: connexin43, gap junction, NMR spectroscopy, protein structure, intrinsic disorder, ZO-1, c-Src, SH3 domain, PDZ domain, protein-protein interaction, allosteric signaling, ball-and-chain model, chemical gating, cytoplasmic tail, intercellular communication
