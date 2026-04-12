---
source_file: krishnakumar2019_cannabinoid_receptor.md
paper_id: krishnakumar2019_cannabinoid_receptor
title: "Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex"
authors:
  - "Kaavya Krishna Kumar"
  - "Moran Shalev-Benami"
  - "Michael J. Robertson"
  - "Hongli Hu"
  - "Samuel D. Banister"
  - "Scott A. Hollingsworth"
  - "Naomi R. Latorraca"
  - "Hideaki E. Kato"
  - "Daniel Hilger"
  - "Shoji Maeda"
  - "William I. Weis"
  - "David L. Farrens"
  - "Ron O. Dror"
  - "Sanjay V. Malhotra"
  - "Brian K. Kobilka"
  - "Georgios Skiniotis"
year: 2019
journal: Cell
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - optogenetics
brain_regions:
  - mediodorsal_thalamus
keywords:
  - cannabinoid_receptor_1_cb1
  - cryo_em
  - gpcr_g_protein_complex
  - gi_protein_coupling
  - mdmb_fubinaca
  - toggle_twin_switch
  - synthetic_cannabinoids
  - receptor_activation_mechanism
  - g_protein_selectivity
  - transmembrane_helix_6
  - molecular_dynamics
  - quantum_mechanics
  - orthosteric_binding_pocket
  - partial_vs_full_agonism
  - structure
  - signaling
  - cannabinoid
  - receptor
  - protein
  - complex
---

### One-line summary

A 3 Å cryo-EM structure of the CB1-Gi signaling complex bound to the potent synthetic cannabinoid MDMB-Fubinaca (FUB) reveals the molecular basis of receptor activation, ligand efficacy, and G protein coupling selectivity.

---

### Background & motivation

CB1 is the most abundantly expressed GPCR in the brain and mediates the psychoactive and analgesic effects of cannabis primarily through Gi protein coupling. Synthetic cannabinoids such as FUB (MDMB-Fubinaca) are far more potent than natural cannabinoids and have caused numerous overdoses and fatalities, yet the structural basis for their extreme efficacy relative to partial agonists like THC was unknown. Prior CB1 crystal structures existed in inactive states or in agonist-bound forms lacking G protein, leaving the full activation mechanism and G protein coupling interface unresolved. A structure of the fully activated, Gi-coupled CB1 complex was needed to explain how different ligand classes vary in efficacy and to guide the design of safer therapeutics.

---

### Methods

- Purified full-length human CB1 from Sf9 insect cells using baculovirus expression, with FLAG and His-tags; performed ligand exchange to FUB during purification.
- Expressed and purified heterotrimeric human Gi (Gαi/Gβ1γ2) from Hi5 insect cells.
- Screened 10 synthetic cannabinoids for Gi activation using a GTP turnover (GTPase-Glo) assay and fluorescence-size exclusion chromatography (F-SEC) to assess complex stability.
- Assembled the CB1-FUB-Gi complex stabilised with scFv16, a single-chain antibody fragment conferring GTPase resistance, to enhance cryo-EM sample stability.
- Collected ~2,759 cryo-EM movies on a Titan Krios (300 kV) with a K2 Summit detector; processed ~177,000 particle projections to yield a 3D reconstruction at 3.0 Å global resolution (range 2.7–3.6 Å locally).
- Built an atomic model using CB1 crystal structure (PDB: 5XRA) and mOR-Gi (PDB: 6DDE) as templates; refined in Phenix and COOT.
- Performed molecular dynamics (MD) simulations to characterise ligand binding poses, N-terminal dynamics, and a proposed TM1–TM7 ligand entry pathway.
- Conducted quantum mechanics (QM) calculations to explain FUB's conformational rigidity and high-affinity binding.
- Used JAWS molecular mechanics calculations to predict water molecule positions in the binding pocket.
- Compared CB1-Gi with published mOR-Gi, b2AR-Gs, A1A-Gi, 5HT1B-Go, and rhodopsin-Gi structures to assess commonalities and differences in G protein coupling.

---

### Key findings

- FUB binds in the deep orthosteric pocket of CB1 (formed by TM2–TM3 and TM5–TM7), adopting a characteristic C-shape geometry shared with other CB1 agonists despite distinct chemical scaffolds.
- FUB stabilises the active conformation by engaging the CB1 "toggle twin switch": its indazole ring displaces F200^3.36 from its interaction with W356^6.48, allowing TM6 to swing outward by 12 Å and open a cavity for the Gi α5 helix.
- The binding pocket RMSD between active and inactive CB1 is 8.5 Å, far larger than in β2AR (2.7 Å) or mOR (5.1 Å), indicating an unusually large activation-related structural rearrangement.
- QM calculations show that FUB's intramolecular interactions constrain it in a low-energy bound conformation, explaining its exceptional potency (Ki ~98 pM); less potent analogs lack this geometric pre-organisation.
- MD simulations reveal a potential lateral ligand entry pathway between TM1 and TM7, coinciding with N-terminal displacement and POPC lipid binding.
- Unlike β2AR and mOR, agonist-bound CB1 alone (without G protein) can largely stabilise the active TM6 conformation, consistent with high basal CB1 activity; the absence of P^5.50 makes TM5 a rigid helix less dependent on G protein for conformational stabilisation.
- The Gi orientation relative to CB1 is rotated ~18° compared to mOR-Gi, attributable to more extensive contacts between the Gi α5 helix N-terminus and CB1's extended TM5; this is similar to the rhodopsin-Gi orientation.
- ICL2 of CB1 interacts weakly with Gi (primarily the α5 helix), not with the aN-β1 loop as seen in mOR-Gi or b2AR-Gs; the L222^ICL2 residue does not engage the Gi hydrophobic pocket, but a bulkier phenylalanine substitution promotes Gs coupling, explaining CB1's promiscuous G protein selectivity.
- The P-loop conformation in CB1-Gi is compatible with nucleotide re-binding, suggesting this complex may represent a conformation poised for GTP loading rather than a strictly nucleotide-free dead-end state, in contrast to mOR-Gi where steric clashes preclude nucleotide binding.

---

### Computational framework

The paper combines structural biology with complementary computational methods rather than a single formalised computational framework:

- **Molecular dynamics (MD) simulations** (AMBER/PMEMD, CHARMM36m force field): modelled CB1 in a lipid bilayer (POPC) to characterise FUB binding pose ensembles, N-terminal flexibility, and a proposed TM1–TM7 ligand entry corridor. Key variables: atomic coordinates, lipid interactions, RMSD from cryo-EM density.
- **Quantum mechanics calculations** (Gaussian 09, ωB97X-D functional): computed the energy difference between FUB's bound conformation and a flipped dihedral pose to explain its conformational rigidity and high affinity. Key finding: the bound pose is substantially lower in energy than alternate conformations, a feature absent in less potent Fubinaca analogs.
- **Molecular mechanics / JAWS calculations** (MCPRO/OPLS): predicted the location and binding free energy of water molecules at the CB1 binding site (>3.5 kcal/mol binding predicted for a water bridging the FUB ester, H178^2.65, and S383^7.39).
- **Ligand docking** (Glide/Schrodinger): generated and refined docked poses of FUB, THC, and Fubinaca derivatives; confirmed consistency with cryo-EM density.

---

### Prevailing model of the system under study

The paper's introduction frames CB1 as the brain's most abundant GPCR, primarily coupled to Gi/o proteins to inhibit adenylyl cyclase and cAMP signalling. The endocannabinoid system was understood to regulate memory, mood, sleep, appetite, inflammation, and pain, making CB1 a therapeutic target. Existing structural knowledge was limited to inactive-state CB1 crystal structures (bound to antagonist AM-6538 or inverse agonist taranabant) and agonist-bound crystal structures of N/C-terminally truncated CB1 constructs that cannot signal. The active-state conformation of TM6 had not been fully resolved in a signalling competent complex, and the molecular basis of the toggle twin switch mechanism (F200^3.36 / W356^6.48) had been inferred from mutagenesis rather than direct structural observation. How different ligand chemical scaffolds achieved variable efficacy (partial vs. full agonism) was speculative. The structural basis of CB1's ability to couple promiscuously to both Gi and Gs, in contrast to more selective receptors like mOR, was also unresolved. The broader GPCR field understood activation in terms of TM6 outward displacement creating a G protein cavity, a mechanism mediated in many receptors by rearrangement of the conserved P-I-F motif and P^5.50-mediated TM5 flexibility.

---

### What this paper contributes

The structure directly visualises, for the first time, the full signalling-competent CB1-Gi complex and provides several concrete advances:

1. **Mechanism of toggle switch activation**: the structure confirms that FUB's indazole ring physically displaces F200^3.36 from W356^6.48, enabling TM6 outward movement — previously inferred from mutagenesis alone.
2. **Structural basis of FUB's extreme potency**: QM calculations reveal that FUB's intramolecular conformational rigidity locks it in the optimal bound geometry, directly explaining why it outperforms THC (which lacks this constraint and shows conformational variability in docking).
3. **CB1-specific activation features**: unlike most class A GPCRs, CB1 lacks P^5.50, making TM5 a rigid conduit that does not require G protein binding to adopt an active-like conformation — consistent with CB1's known high basal activity.
4. **G protein coupling interface**: the CB1-Gi interface is structurally distinct from mOR-Gi (18° rotational difference), driven by CB1's extended TM5. ICL2 of CB1 does not engage the canonical Gi hydrophobic pocket, explaining why ICL2 mutations that impair Gs coupling (L222F) do not affect Gi coupling.
5. **Partial vs. full agonism**: the structure clarifies why THC is a partial agonist — its conformational flexibility prevents consistent engagement of the toggle switch, while FUB's rigidity ensures full switch engagement.

---

### Brain regions & systems

Not applicable as a direct anatomical focus — this is a structural/biochemical study at the molecular level. CB1 is the most abundantly expressed GPCR in the brain and is expressed broadly in neuronal populations throughout the forebrain (cited from Marsicano and Lutz, 1999). The physiological role of CB1 in memory, mood, sleep, appetite, inflammation, pain, and neuroprotection is noted as motivation, but the paper's analysis operates at the molecular/structural level of analysis rather than the circuit or systems level.

---

### Mechanistic insight

This paper meets a high bar for structural mechanistic insight, though it does not involve neural recording data.

The paper formalises an **algorithm** — the toggle twin switch activation cascade — and provides direct **structural evidence** (cryo-EM) supporting that specific mechanism over alternatives. It additionally provides quantum mechanical and molecular dynamics evidence that constrains how different ligand chemistries engage this mechanism.

Mapping to Marr's levels:

- **Computational**: CB1 must transduce an extracellular ligand-binding event into intracellular Gi activation (nucleotide exchange), thereby inhibiting adenylyl cyclase and modulating cAMP-dependent signalling. The receptor must distinguish full from partial agonists and must preferentially couple to Gi over Gs.
- **Algorithmic**: FUB binding induces displacement of F200^3.36 away from W356^6.48 (the toggle twin switch); this allows W356^6.48 to rotate inward, relaxing the P358^6.50 kink, straightening TM6 and opening a cytoplasmic cavity; the Gi α5 helix inserts into this cavity and undergoes 6 Å translation + 60° rotation, destabilising the GDP P-loop and triggering nucleotide release. ICL2 geometry and the specific ICL2 residue determine whether Gs or Gi hydrophobic pockets are engaged.
- **Implementational**: the physical mechanism involves specific side-chain rotamer rearrangements (F200^3.36, W356^6.48, P358^6.50), water-mediated polar contacts (H178^2.65, S383^7.39, FUB ester), the absence of P^5.50 making TM5 a rigid helix, and lipid bilayer interactions (POPC at the TM1–TM7 entry corridor). The scFv16 antibody stabilises the nucleotide-free intermediate for structural capture.

**Note**: the paper does not provide neural recordings or in vivo electrophysiology — the mechanistic evidence is entirely structural and biochemical. The paper does not address implementational differences across cell types or brain regions.

---

### Limitations & open questions

- ZCZ-011 (PAM) was present during complex formation but showed no density in the cryo-EM map, possibly due to dissociation during vitrification; its allosteric binding site and mechanism remain unresolved structurally.
- The structure represents a stabilised, nucleotide-free intermediate; the pre-equilibrium state where GDP-bound Gi first engages activated CB1 is transient and not captured, leaving the initial coupling geometry unknown.
- The N-terminus and TM1 of CB1 were at lower resolution (~4 Å) and showed mobility in MD simulations; the precise role of N-terminal displacement in the activation mechanism is inferred but not fully resolved.
- How CB1 couples to Gs under specific conditions (e.g., at high agonist concentration) is not fully explained; the authors propose ICL2 L222^ICL2 as a determinant but the structural basis of Gs selectivity in a complex is not directly demonstrated.
- No in vivo or in cellulo validation of the ligand entry pathway (TM1–TM7 gap) is provided; it is inferred from MD simulations.
- The study used a synthetic, highly potent full agonist; structural data for partial agonists (e.g., THC) bound to the Gi-coupled receptor are absent, meaning the structural basis of partial agonism is supported by docking rather than direct cryo-EM evidence.
- G protein coupling specificity across the broader GPCR family is not resolved; the authors acknowledge this remains a major open question.

---

### Connections & keywords

**Key citations**:
- Hua et al. (2016, 2017) — CB1 crystal structures in inactive and agonist-bound states (PDB: 5TGZ, 5XRA)
- Shao et al. (2016) — High-resolution crystal structure of CB1 (PDB: 5U09)
- Koehl et al. (2018) — mOR-Gi complex structure (PDB: 6DDE)
- Maeda et al. (2018) — scFv16 development for GPCR-Gi stabilisation
- McAllister et al. (2004) — Mutagenesis establishing the toggle twin switch (F3.36/W6.48)
- Adams et al. (2017) — "Zombie" outbreak caused by AMB-FUBINACA; clinical context for FUB toxicity
- Schoeder et al. (2018) — SAR data on synthetic cannabinoids including FUB Ki (~98 pM)
- Gamage et al. (2018) — FUB 20-fold more potent than THC in GTPgS assay
- Ballesteros and Weinstein (1995) — Ballesteros-Weinstein GPCR residue numbering scheme
- Dror et al. (2015) — Structural basis for nucleotide exchange in heterotrimeric G proteins

**Named models or frameworks**:
- Toggle twin switch (F200^3.36 / W356^6.48 rotamer mechanism)
- Ballesteros-Weinstein residue numbering
- P-I-F motif (conserved GPCR activation motif; CB1 has L-V-L variant)
- TCAT motif (Gi nucleotide-coordinating sequence)
- GTPase-Glo assay (Promega)
- Cryo-EM single-particle analysis (RELION 2.1.0, cisTEM, Phenix)

**Brain regions**:
Not applicable (molecular structural study). CB1 is the most abundant GPCR in the brain, broadly expressed in forebrain neuronal populations.

**Keywords**:
cannabinoid receptor 1 (CB1), cryo-EM, GPCR-G protein complex, Gi protein coupling, MDMB-Fubinaca, toggle twin switch, synthetic cannabinoids, receptor activation mechanism, G protein selectivity, transmembrane helix 6, molecular dynamics, quantum mechanics, orthosteric binding pocket, partial vs. full agonism
