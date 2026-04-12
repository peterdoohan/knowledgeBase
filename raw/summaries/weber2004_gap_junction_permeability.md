---
source_file: weber2004_gap_junction_permeability.md
paper_id: weber2004_gap_junction_permeability
title: "The Permeability of Gap Junction Channels to Probes of Different Size Is Dependent on Connexin Composition and Permeant-Pore Affinities"
authors:
  - "Paul A. Weber"
  - "Hou-Chien Chang"
  - "Kris E. Spaeth"
  - "Johannes M. Nitsche"
  - "Bruce J. Nicholson"
year: 2004
journal: "Biophysical Journal"
paper_type: empirical
contribution_type: empirical
methods:
  - calcium_imaging
keywords:
  - gap_junctions
  - connexins_cx26
  - cx32
  - cx37
  - cx40
  - cx43
  - cx45
  - size_selectivity
  - dye_permeability
  - alexa_fluorophores
  - single_channel_permeability
  - permeant_pore_affinity
  - heterotypic_channels
  - hindered_diffusion
  - xenopus_oocytes
  - permeability
  - gap
  - junction
  - channels
  - probes
---

### One-line summary

Gap junction channels composed of different connexin isoforms exhibit distinct size exclusion limits and permeant-pore affinities that can enhance dye flux by 1-2 orders of magnitude above hindered diffusion predictions.

### Background & motivation

Gap junctions have traditionally been viewed as nonspecific pores allowing passage of molecules up to ~1 kDa, but accumulating evidence indicates different connexin family members mediate distinct physiological processes and are not functionally interchangeable. While ionic charge selectivity has been documented, surprisingly little was known about how connexin composition affects pore size and permeability to larger molecules. This study aimed to systematically characterize size selectivity across multiple connexin isoforms using a graded series of fluorescent probes.

### Methods

- **Expression system**: Xenopus oocytes injected with connexin cRNA (Cx26, Cx32, Cx37, Cx40, Cx43, Cx45) and antisense oligonucleotide to endogenous Cx38
- **Dye probes**: Three Alexa Fluor dyes (Alexa 350: MW 350, charge -1; Alexa 488: MW 570, charge -2; Alexa 594: MW 760, charge -2) with similar chemical structures but varying sizes
- **Measurements**: Dual-cell voltage clamp to measure junctional conductance combined with time-lapse fluorescence imaging (30-min intervals over 6 hours) to track dye transfer
- **Modeling**: Three-dimensional mathematical diffusion model accounting for cytoplasmic diffusion, dye binding, and intercellular permeation to extract single-channel permeabilities
- **Correction for access resistance**: Voltage clamp measurements corrected for cytoplasmic series resistance at high conductances (>10 mS)

### Key findings

- **Two distinct permeability classes identified**: Cx43 and Cx32 showed minimal size-dependent permeability decreases (2-4 fold across dye sizes), while Cx26, Cx37, Cx40, and Cx45 showed dramatic 20-45 fold decreases in permeability to the largest dye (Alexa 594)
- **Cx37 was least permeable**: Cx37 showed 2-6 fold lower absolute permeability to all dyes compared to other connexins, and Alexa 594 permeability was below detection limits
- **Size exclusion ranking**: Effective pore exclusion limits ranked in decreasing order: Cx32 ≈ Cx43 > Cx26 ≈ Cx40 ≥ Cx45 > Cx37
- **Heterotypic channel behavior**: Heterotypic channels (Cx26/Cx32 and Cx37/Cx43) showed permeability characteristics resembling the more restrictive parental homotypic channel; no directional asymmetry in dye flux was observed
- **Permeability magnitudes 1-2 orders of magnitude above hindered diffusion predictions**: Classical hindered diffusion theory would require pore diameters of 36-80 Å to explain observed permeabilities, far exceeding structural estimates (10-20 Å); this indicates significant permeant-pore affinity effects enhancing flux
- **Inverse correlation between conductance and size exclusion**: Counterintuitively, Cx37 had the largest single-channel conductance (315 pS) but smallest pore for large permeants; Cx32 and Cx43 had smaller conductances (55 and 90 pS) but larger effective pore sizes

### Computational framework

The study employs a **three-dimensional hindered diffusion model with permeant-pore affinity corrections** to extract single-channel permeabilities from macroscopic dye transfer measurements. The core mathematical framework accounts for:

1. **Cytoplasmic diffusion**: Modeled with effective diffusion coefficients (Dcyt) slower than free diffusion due to reversible binding to yolk (equilibrium constant Kcyt = 2-10, depending on dye)
2. **Intercellular permeation**: Treated as passive diffusion across the junctional membrane with permeability Pjunc
3. **Unitary channel permeability**: Calculated as (AP)pore = Pjunc × Amem / Npore, where Amem is membrane area and Npore is number of channels estimated from conductance measurements
4. **Affinity corrections**: Van der Waals interactions between dye and pore wall incorporated to explain permeabilities 1-2 orders of magnitude above hindered diffusion predictions; access resistance terms included/excluded for comparison

The model assumes right cylindrical pore geometry for hindered diffusion calculations, with the recognition that actual pore shape varies among connexins (constrictions postulated for Cx37, Cx26, Cx40 vs. more uniform diameter for Cx32, Cx43).

### Prevailing model of the system under study

Prior to this study, gap junctions were conceptualized as simple aqueous pores with limited selectivity, passing molecules up to ~1 kDa based primarily on size. The field acknowledged that different connexin isoforms had different single-channel conductances (ranging from ~30-300 pS), which were assumed to reflect average pore diameter. However, several observations challenged this simple model:

1. Connexins with similar conductances showed different permeability to natural metabolites (e.g., Cx43 vs. Cx32 for ATP)
2. Ionic selectivity did not correlate with conductance (Cx45 and Cx26 being more cation selective despite different conductances)
3. Previous size-exclusion studies with PEGs showed different cutoff limits for different connexins, but these measured block rather than flux rates
4. Heterotypic channels showed electrical rectification, suggesting asymmetric properties

The physical basis for selectivity remained obscure—there were no evident correlations between metabolite properties (size, charge) and their permeability through different connexin channels.

### What this paper contributes

This paper fundamentally reframes understanding of gap junction permeability by establishing three key principles:

1. **Connexin-specific size exclusion limits**: The paper demonstrates that different connexins impose distinct size cutoffs on permeants, with two classes emerging—permissive (Cx32, Cx43) and restrictive (Cx26, Cx37, Cx40, Cx45). This provides a physical basis for why different connexins cannot functionally substitute for one another in different tissues.

2. **Permeant-pore affinity as a major determinant of flux**: The most surprising finding is that absolute permeabilities are 1-2 orders of magnitude greater than predicted by hindered diffusion alone. This requires invoking significant attractive interactions (affinity) between permeants and pore walls that enhance flux—a phenomenon not previously appreciated for gap junctions. The paper demonstrates this using van der Waals corrections to the diffusion model.

3. **Inverse relationship between conductance and pore size for large permeants**: The paper reveals a counterintuitive dissociation between ionic conductance (which reflects average pore diameter) and permeability to larger molecules. Cx37 has the highest conductance (315 pS) but is most restrictive to large dyes, suggesting a pore with a large average diameter but a stringent constriction. This implies pore shape varies significantly among connexins, with some having narrow constrictions that limit large permeants while allowing ion flux.

The paper also establishes that heterotypic channels behave like the more restrictive parental homotypic channel, providing predictive rules for complex channel compositions, and shows no rectification of passive dye flux despite electrical rectification in some heterotypic channels.

### Brain regions & systems

Not applicable. This study investigates gap junction channels expressed in Xenopus oocytes, focusing on biophysical properties of connexin proteins rather than specific neural or anatomical systems. The connexins studied (Cx26, Cx32, Cx37, Cx40, Cx43, Cx45) are expressed in various tissues including heart, liver, brain, and vascular endothelium, but the study characterizes their intrinsic permeability properties in a heterologous expression system.

### Mechanistic insight

This paper provides mechanistic insight at Marr's three levels:

**Computational**: The brain (and tissues generally) needs to solve the problem of selective intercellular communication—allowing specific signals to pass between cells while excluding others. Different connexin isoforms provide a combinatorial solution, where channel composition determines which metabolites can pass, enabling tissue-specific communication patterns.

**Algorithmic**: The mechanism involves hindered diffusion through aqueous pores modified by permeant-pore affinity interactions. The key variables are: 1) pore diameter (particularly at constrictions), 2) attractive interactions between permeant and pore wall (van der Waals forces), and 3) hydrodynamic drag at narrow pore segments. The paper formalizes this through a 3D diffusion model with affinity corrections.

**Implementational**: At the neural hardware level, the mechanism is implemented by different connexin protein isoforms (Cx26, Cx32, Cx37, Cx40, Cx43, Cx45) that form hexameric hemichannels. The specific amino acid sequences determine pore structure—particularly the presence or absence of constrictions that limit large permeant passage. The paper notes that pore-lining residues in Cx32 M2 and M3 domains are predominantly hydrophobic, supporting van der Waals interactions as a mechanism for affinity enhancement.

The paper meets the high bar for mechanistic insight: it presents a formal algorithm (the 3D diffusion model with affinity corrections) and provides neural data (dye transfer measurements through expressed connexin channels) that specifically support this algorithm over simpler hindered diffusion models.

### Limitations & open questions

1. **Detection limits for low permeability**: Cx37 permeability to Alexa 594 was below detection limits, preventing full characterization of the most restrictive connexin to the largest dye.

2. **Background transfer issues**: Alexa 350 showed significant background transfer in negative controls (oligo-injected pairs), possibly from patent hemichannels in unopposed membranes, complicating quantification.

3. **Limited connexin structural information**: The study lacks detailed structural data on pore-lining residues for most connexins (only Cx32 had been mapped at the time), limiting mechanistic understanding of size selectivity determinants.

4. **Single permeant series**: Only size was varied (using Alexa dyes); systematic examination of how charge, shape, and chemical properties contribute to selectivity was not performed.

5. **Heteromeric channels not examined**: The study examined homotypic and heterotypic (different connexins in each cell) channels, but not heteromeric channels (mixed connexins within single hemichannels), which are likely common in situ.

6. **Natural metabolite permeability not directly measured**: The study used artificial fluorescent probes; whether the same permeability rankings apply to natural metabolites like ATP, IP3, cAMP remains to be verified.

### Connections & keywords

**Key citations**:
- Valiunas et al., 2002 (previous absolute permeability study with Lucifer Yellow in HeLa cells)
- Nitsche et al., 2004 (companion paper on 3D diffusion model)
- Gong and Nicholson, 2001 (PEG size exclusion study)
- Bevans et al., 1998 (cAMP/cGMP selectivity in heteromeric hemichannels)
- Goldberg et al., 1999, 2002 (ATP and metabolite selectivity in Cx43 vs Cx32)
- Veenstra et al., 1994a, 1994b, 1995 (single channel conductances and ionic selectivity)
- Skerrett et al., 2002 (pore-lining residues in Cx32)
- Barrio et al., 1991; Suchyna et al., 1999 (heterotypic Cx26/Cx32 properties)

**Named models or frameworks**:
- Three-dimensional hindered diffusion model with permeant-pore affinity corrections
- Resistances-in-series model for heterotypic channels
- van der Waals affinity corrections to pore diffusion theory

**Brain regions**: Not applicable (Xenopus oocyte expression system used; connexins studied are expressed in various tissues including heart, liver, vascular endothelium, and brain but studied heterologously)

**Keywords**:
- gap junctions
- connexins (Cx26, Cx32, Cx37, Cx40, Cx43, Cx45)
- size selectivity
- dye permeability
- Alexa fluorophores
- single channel permeability
- permeant-pore affinity
- heterotypic channels
- hindered diffusion
- Xenopus oocytes
