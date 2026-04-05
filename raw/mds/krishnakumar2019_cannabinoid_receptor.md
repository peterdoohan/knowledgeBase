Article 

## Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex 

## Graphical Abstract 

**==> picture [286 x 287] intentionally omitted <==**

## Authors 

Kaavya Krishna Kumar, Moran Shalev-Benami, Michael J. Robertson, ..., Sanjay V. Malhotra, Brian K. Kobilka, Georgios Skiniotis 

## Correspondence 

kobilka@stanford.edu (B.K.K.), yiorgo@stanford.edu (G.S.) 

## In Brief 

Looking at how a toxic, synthetic ligand locks cannabinoid receptor 1 into a signaling conformation points to ways to understand and modulate receptor activity. 

## Highlights 

- d 3 A[˚] cryo-EM structure of the CB1-Gi complex bound to potent agonist MDMB-Fubinaca 

- d MDMB-Fubinaca locks ‘‘toggle switch’’ residues F200[3.36] / W356[6.48] in active conformation 

- d Quantum mechanics calculations reveal the mechanism for the high affinity of Fubinaca 

- d Molecular dynamic simulations reveal a path for ligand entry between TM1 and TM7 

Krishna Kumar et al., 2019, Cell 176, 1–11 January 24, 2019 ª 2018 Elsevier Inc. https://doi.org/10.1016/j.cell.2018.11.040 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

## Article 

**==> picture [60 x 60] intentionally omitted <==**

## Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex 

Kaavya Krishna Kumar,[1,8] Moran Shalev-Benami,[1,2,8] Michael J. Robertson,[1,2] Hongli Hu,[1,2] Samuel D. Banister,[3] Scott A. Hollingsworth,[1,4,5] Naomi R. Latorraca,[1,4,5] Hideaki E. Kato,[1] Daniel Hilger,[1] Shoji Maeda,[1] William I. Weis,[2,6] David L. Farrens,[7] Ron O. Dror,[1,4,5] Sanjay V. Malhotra,[3] Brian K. Kobilka,[1,] * and Georgios Skiniotis[1,2,6,9,] * 

1Department of Molecular and Cellular Physiology, Stanford University School of Medicine, 279 Campus Drive, Stanford, CA 94305, USA 

2Department of Structural Biology, Stanford University School of Medicine, 279 Campus Drive, Stanford, CA 94305, USA 

3Department of Radiation Oncology, Division of Radiation and Cancer Biology, Stanford University School of Medicine, Stanford, CA 94304, USA 

4Department of Computer Science, Stanford University, Stanford, CA 94305, USA 

5Biophysics Program, Stanford University, Stanford, CA 94305, USA 

6Department of Photon Science, SLAC National Accelerator Laboratory, Stanford University, Menlo Park, CA 94025, USA 

7Departments of Biochemistry and Molecular Biology, Oregon Health Sciences University, Portland, OR 97201, USA 

8These authors contributed equally 

9Lead Contact 

*Correspondence: kobilka@stanford.edu (B.K.K.), yiorgo@stanford.edu (G.S.) https://doi.org/10.1016/j.cell.2018.11.040 

## SUMMARY 

Cannabis elicits its mood-enhancing and analgesic effects through the cannabinoid receptor 1 (CB1), a G protein-coupled receptor (GPCR) that signals primarily through the adenylyl cyclase-inhibiting heterotrimeric G protein Gi. Activation of CB1-Gi signaling pathways holds potential for treating a number of neurological disorders and is thus crucial to understand the mechanism of Gi activation by CB1. Here, we present the structure of the CB1-Gi signaling complex bound to the highly potent agonist MDMB-Fubinaca (FUB), a recently emerged illicit synthetic cannabinoid infused in street drugs that have been associated with numerous overdoses and fatalities. The structure illustrates how FUB stabilizes the receptor in an active state to facilitate nucleotide exchange in Gi. The results compose the structural framework to explain CB1 activation by different classes of ligands and provide insights into the G protein coupling and selectivity mechanisms adopted by the receptor. 

## INTRODUCTION 

The cannabinoid receptor 1 (CB1) is the most abundantly expressed G protein-coupled receptor (GPCR) in the brain (Marsicano and Lutz, 1999) and the target for D[9] -tetrahydrocannabinol (D[9] -THC), the major psychoactive component of Cannabis that has been used for recreational and therapeutic purposes for millennia. Recently, CB1 has been targeted by designed synthetic cannabinoids which, like their plant-based counterparts, piggyback their pharmacology on a collection of endogenous molecules known as the endocannabinoids. Endocannabinoid signaling has proven to play important roles in memory, mood, 

sleep, appetite, inflammation, and pain sensation (Mackie, 2006), thereby rendering CB1 an attractive target for the development of novel therapeutics toward a variety of conditions. 

CB1 elicits its physiological responses by coupling primarily to Gi/o proteins to inhibit adenylate cyclase and cyclic AMP signaling, although coupling with Gs or Gq/11 has also been reported (Glass and Felder, 1997; Lauckner et al., 2005). Activation of CB1 has been shown to have anxiolytic, analgesic, neuroprotective, and anti-nausea effects (Campos et al., 2012; Izzo et al., 2009; Micale et al., 2013), while preclinical data indicate that D[9] -THC and synthetic cannabinoid agonists are effective antinociceptive agents in laboratory animal models of neurodegenerative, neuroinflammatory, and pain-related disease states (Fagan and Campbell, 2014; Guindon and Hohmann, 2009; Pryce and Baker, 2012). However, D[9] -THC and, to a much greater extent, synthetic cannabinoids can induce side effects that include dependence, memory impairment, hallucinations, panic attacks, seizures, convulsions, and psychoses (Cooper, 2016). Fubinacas, a class of potent synthetic agonists infused in illicit herbal mixes such as ‘‘K2’’ or ‘‘Spice,’’ have been named ‘‘zombie drugs’’ due to their association with users in semi-comatose state (Adams et al., 2017). Although side effects and potential lethality limit their direct therapeutic use, such compounds represent important tools to dissect mechanistic questions regarding the extent of CB1 activation and potency of distinct classes of ligands in order to design drugs with improved pharmaceutical properties. 

MDMB-Fubinaca (FUB), a derivatization of the AB-Fubinaca originally developed by Pfizer, has been designated as the deadliest cannabino-mimetic sold to date (Adams et al., 2017). A recent study on 43 synthetic cannabinoids found FUB to have the highest affinity to CB1 in a radioligand binding assay with Ki values of 98 pM (Schoeder et al., 2018). In GTPgS binding assay FUB was found to be 20-fold more potent compared to D[9] -THC (Gamage et al., 2018). Although toxicity of FUB consumption has not been determined directly, Fubinacas have been linked to thousands of hospitalizations and numerous 

Cell 176, 1–11, January 24, 2019 ª 2018 Elsevier Inc. 1 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 399] intentionally omitted <==**

Figure 1. GTP Turnover Assay for the CB1 Ligands (A) Chemical structures of CB1 agonists used in this study and of PAM ZCZ. 

(B) GTP turnover assay for the 10 ligands tested. 

(C) The addition of ZCZ further increases GTP turnover indicating PAM activity (p < 0.0001). Data are normalized to FUB in (B) and (C) and are represented as mean ± SD. See also Figure S1. 

fatalities (Adams et al., 2017; Peace et al., 2017). While synthetic cannabinoids have been shown to have multiple targets, they predominantly signal through CB1. To gain structural insights into the binding and activation of CB1 by FUB, we determined a 3 A[˚] cryo-EM structure of FUB-activated full-length CB1 in complex with its down-stream heterotrimeric Gi protein. The structure, complemented by molecular dynamics (MD) and ligand docking calculations, provides a snapshot into the FUB binding properties, its activation of CB1, and the structural basis of G protein coupling. This work sets the framework to integrate a large body of structure-activity relationship (SAR) studies toward understanding cannabinoid receptor activation by different classes of ligands and also provides insights into the promiscuous coupling of CB1 to both Gs and Gi. 

## RESULTS AND DISCUSSION 

## Cryo-EM of the CB1-FUB-Gi Complex 

In our preliminary studies, we evaluated 10 synthetic cannabinoids for their ability to activate Gi signaling (Figure 1A). Through GTP turnover and fluorescence-detection size exclusion chromatography (F-SEC) assays (Figures 1B and S1A) we observed a direct correlation between complex stability and ligand ability to induce signaling. In these assays, FUB demonstrated high efficacy and complex stability (Figure 1B). 

In addition, we prepared the CB1-FUB-Gi complex in the presence of ZCZ-011 (ZCZ), a positive allosteric modulator (PAM) that was shown to mediate analgesia with no psychoactive effect (Ignatowska-Jankowska et al., 2015). ZCZ further increased the 

2 Cell 176, 1–11, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 310] intentionally omitted <==**

Figure 2. Cryo-EM Structure of the CB1-Gi Complex (A) Representative reference-free two-dimensional (2D) cryo-EM average of CB1-FUB-Gi-scFv16 shows high resolution features including the helical pitch of TM a helices. The labels indicate complex components. The diameter of the circular mask is 18 nm. (B–E) Three-dimensional map (B) rotated 180[�] along the x axis (D) and 90[�] along the y axis (E), and the model (C) obtained from cryo-EM of the CB1-Gi complex. Blue, CB1; orange, FUB; yellow, Gai; cyan, Gb; dark magenta, Gg; pink, scFv16. 

(F) Snapshot of model versus map density in the region where the scFv16 is engaging Gai and Gb. The zoomed in region corresponds to the area highlighted by a dashed black box in (E). See also Figures S1 and S2 and Tables S1 and S3. 

rate of GTP turnover of FUB-bound CB1 confirming positive allosteric modulation (Figure 1C). However, while negative stain EM analysis (Peisley and Skiniotis, 2015) showed an intact CB1-Gi complex, inspection of cryo-EM samples indicated sample dissociation, presumably due to adverse effects during cryogrid preparation (Noble et al., 2018). To further enhance complex stability, we utilized scFv16, a single-chain variable fragment that we recently employed to obtain the cryo-EM structure of the m-opioid receptor (mOR)-Gi complex (Koehl et al., 2018). ScFv16 is derived from a monoclonal antibody that was raised against a rhodopsin:Gi1 complex. It confers GTPgS resistance to receptor-Gi/o complexes, thus enhancing their stability (Maeda et al., 2018). We thus obtained cryo-EM images of the CB1-FUB-Gi-scFv16 complex and used �177,000 projections to calculate a 3D reconstruction with a global nominal resolution of 3 A[˚] (Figures 2, S1B, S1C, and S2). Local resolution calculations indicate a range of 2.7–3.6 A[˚] in most map regions, with the highest resolution observed at the core of the Gi protein (Figure S2C). This map enabled the building of a model for the fully activated CB1 signaling complex (Figures 2 and S2; Table S1). 

The cryo-EM map shows well-defined density for FUB in the orthosteric binding pocket (Figures 3A and S2D) but no observable density to accommodate ZCZ. This might suggest that the PAM engages a flexible site of the receptor, although we cannot exclude the possibility that it may have dissociated from the complex during cryo-EM specimen preparation. The FUB binding pocket is composed of residues in TM2–TM3 and TM5– TM7, overlapping with the orthosteric site observed in previously reported crystal structures of active CB1 (Hua et al., 2017) (Figures 3B and 4). Compared to other GPCRs (with the exception of rhodopsin), the FUB pocket is further buried in the TM region and is capped by ECL2, which folds into the pocket with F268[ECL2] making direct hydrophobic contacts with the ligand. FUB fits well in the map density where the indazole ring is well-identified, and the p-fluoro-benzyl and tert-butyl-ester moieties fit into the remaining density (Figure S2D). Furthermore, molecular dynamics (MD) simulations of several computationally docked poses converged to nearly identical ensembles that agreed well with the EM density (Figure S2E). The polar ester group often formed water-mediated interactions with residues on TM2 and 

Cell 176, 1–11, January 24, 2019 3 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

Figure 3. The FUB Binding Pocket (A) Cut-through view of CB1 cryo-EM map with FUB bound in the orthosteric pocket. Orange, density corresponding to FUB; purple, density corresponding to CB1. 

(B) FUB interactions in the CB1 binding site. See also Figure S2. 

TM7, and the tert-butyl group remained more proximal to TM2 and TM3. 

## CB1 Activation by FUB 

Compared to the inverse agonist (taranabant)- and antagonist (AM-6538)-bound structures of CB1 (Hua et al., 2016; Shao et al., 2016), the ligand binding pocket in FUB-bound CB1 undergoes an extensive structural rearrangement that agrees well with that observed in the agonist-bound CB1 structures (Hua et al., 2017). This structural rearrangement involves the inward displacement of TM1 and TM2, along with the displacement of the N terminus out of the transmembrane core (Figure 4). Such large differences in the binding pocket between active and inactive states have not been observed in other GPCRs; rootmean-square deviation (RMSD) values between binding pocket residues in the active and inactive states range between 2.7 A[˚] in the b2-adrenergic receptor (b2AR) and 5.1 A[˚] in the mOR compared to 8.5 A[˚] in CB1. The TM2 movement is accompanied by the repositioning of residues F170[2.5] , F174[2.61] , F177[2.64] , and H178[2.65] (superscripts indicate Ballesteros-Weinstein numbering for GPCRs) (Ballesteros and Weinstein, 1995), that turn toward the pocket in the active conformation and contribute to interactions with the agonist (Figure 4A). Notably, F200[3.36] , which in the inactive receptor state is stabilized by interactions with W356[6.48] , rotates away to interact with the indazole ring of FUB (Figures 4A and 4B). The role of the interaction between F200[3.36] and W356[6.48] , also known as the ‘‘toggle twin switch,’’ in stabilizing the inactive conformation of CB1 was previously demonstrated by mutation of F[3.36] A, which resulted in high basal activity in a GTPgS binding assay (McAllister et al., 2004). In our structure, the F200[3.36] repositioning allows W356[6.48] to rotate inward, resulting in the relaxation of the kink at the highly conserved P358[6.50] , with a consequent straightening and an outward movement of the cytoplasmic end of TM6 that serves to create a cavity for G protein binding (Figure 4B). 

Furthermore, the structural rearrangements to accommodate the agonist involve the displacement of the receptor N terminus, a region which along the proceeding TM1 helix has limited resolution in our map (�4 A[˚ ] ). These observations suggest that these elements are relatively mobile, consistent with their dynamics observed in MD simulations (Figure S3A). It is clear, however, 

that the N-terminal displacement is necessary to accommodate the agonist, due to steric clash with the tert-butyl moiety in FUB or the terpenoid scaffold in the previously reported CB1 agonists AM-11542 and AM-841 (Figure 4C). This steric clash is not present in the CB1 structures bound to antagonists or inverse agonists reported to date (Hua et al., 2016; Shao et al., 2016), raising the possibility that the N-terminal displacement may be part of the activation mechanism. Indeed, in all MD simulations performed here, the N terminus regularly fluctuated between contacting the extracellular surface of the receptor and residing in the bulk solvent (Figure S3A). 

The MD simulations further hint at a possible mechanism for ligand entry at the CB1 receptor. In four out of six simulations, TM1 moves outward to create a gap between TM1 and TM7 (Figure S3A). This small opening is similar to one observed in the lipid bilayer between TM1 and TM7 in an inactive-state structure (Figure S3B) and has been proposed to facilitate ligand entry and dissociation in CB1 and all lipid-activated receptors (Shao et al., 2016). Intriguingly, the simulations also show that the opening of the TM1–TM7 gap coincides with both the binding of a lipid molecule (POPC) and the stabilization of the upward position of the N terminus relative to the extracellular surface of the receptor (Figures S3C–S3F). 

## FUB Binding and Comparison with Other CB1 Agonists 

Crystal structures of CB1 constructs truncated at N and C termini have been previously determined in complex with agonists AM-11542 and AM-841 that possess a THC-like scaffold and are structurally distinct from FUB (Hua et al., 2017). Despite the differences in chemical composition, FUB assumes the same overall C-shape geometry as AM-11542 and AM-841, with overlapping ligand binding pockets (Figures 4B and S4). The p-fluorobenzyl that p-p stacks with W279[5.43] , and the indazole group of FUB engage in hydrophobic interactions with aromatic residues in TM5 and TM6 (Figure 4A). Notably, the C3 alkyl chain of the AM-derivatives and the p-fluorobenzyl of FUB occupy the same position in a narrow side pocket comprised of residues in TM3, TM5, TM6, and ECL2 (Figures 4B and 4C). This pocket has been observed to be occupied by the aliphatic chain of CB1 antagonist AM-6538 (Hua et al., 2016) (Figure 4C) and is also present in the sphingosine 1-phosphate receptor (S1P1) where it was shown to be occupied by the aliphatic moiety of a selective antagonist (Hanson et al., 2012). It thus appears that the side pocket is a conserved docking region for aliphatic chains in lipid binding receptors, where it seems to be important for ligand affinity regardless of its ability to activate the receptor. 

4 Cell 176, 1–11, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [421 x 145] intentionally omitted <==**

Figure 4. CB1 Activation by FUB (A) Superposition of the FUB-activated complex (blue) with an inverse agonist bound receptor (AM-6358, PDB: 5TGZ, gray). (B) FUB and AM-11542 (PDB: 5XRA) bound at the CB1 orthosteric pocket make direct contacts with residues F200[3.36] and W356[6.48] . The rotation of F200[3.36] to interact with the indazole ring of FUB allows W356[6.48] to rotate outward, with a consequent outward movement of the cytoplasmic end of TM6 that serves to create a cavity for G protein binding. The groups interacting with the ‘‘toggle twin switch’’ of CB1 (indazole ring of FUB and GDH moiety of AM-11542) are marked in orange. The inactive receptor structure is shown in gray (PDB: 5TGZ). (C) A comparison of binding pockets of AM-6538 (antagonist, gray, PDB: 5TGZ), AM-11542 (agonist, cyan, PDB: 5XRA), and FUB (orange). The receptor is presented as cartoon with the active conformation in blue (present cryo-EM structure) and the inactive conformation in gray (PDB: 5TGZ). See also Figures S3, S4, and S5. 

This might explain the similar affinities observed for the AMderivatives and FUB (indicated Ki values are 0.098 and 0.11 nM for FUB and AM-11542, respectively) (Schoeder et al., 2018) as also supported by SAR studies showing that the replacement of the FUB p-fluorobenzyl with an alkyl chain yields a ligand with similar affinity (Schoeder et al., 2018) and EC50 (Adams et al., 2017). In agreement with this interpretation, our ligand docking calculations show that the aliphatic moiety of a Fubinaca derivative (5F-MDMB-Pinaca) overlaps with the p-fluorobenzyl group of FUB (Figure S4B). 

D[9] -THC has a much greater safety profile compared to synthetic cannabinoids (Fantegrossi et al., 2014). One reason that could attribute to this toxicity difference is that D[9] -THC is a partial agonist whereas synthetic cannabinoids like FUB are full agonists (Atwood et al., 2010). Although structurally similar to D[9] -THC, AM-11542 shows enhanced potency and efficacy for CB1 due to the addition of a 1[0] ,1[0] -gem-dimethylheptyl (GDH) chain at the C3 position. The GDH group in AM-11542 mediates hydrophobic interactions with the ‘‘toggle twin switch,’’ which undergoes concerted conformational changes upon agonistbinding and activation (Figure 4B). In FUB instead, strong aromatic interactions with both F200[3.36] and W356[6.48] are maintained by the indazole ring, thereby explaining the high efficacy of this ligand (Figure 4B). The lack of the toggle switch interaction has been suggested as the explanation of the partial agonist activity observed for D[9] -THC compared to the full agonist activity of the AM compounds. In support of this notion, our docking calculations of D[9] -THC in the CB1 cryo-EM structure yields several poses where the terpenoid ring aligns well with that of AM-11542 in the CB1 crystal structure (PDB: 5XRA) (Hua et al., 2017), but the aliphatic moiety of D[9] -THC fluctuates between penetrating the hydrophobic cavity occupied by the p-fluorobenzyl group in FUB and a downward conformation that points toward the toggle switch to activate the receptor (Figures S4C–S4E). Hence, 

it appears that the conformational variability of D[9] -THC likely compromises both its affinity and potency for CB1, a characteristic that presumably makes it safer compared to more rigid and potent synthetic cannabinoids. 

In contrast, the high efficacy of FUB is partly due to its structural rigidity in the characteristic C-shape configuration that stereotypically recognizes the CB1 binding site and stabilizes the active receptor conformation (Figures 4 and S4A). FUB analogs demonstrate that intramolecular interactions between the heterocyclic core and the linker of the tert-butyl can significantly stabilize the bound conformation, with a marked loss of potency when the indazole core is replaced with an indole or when the amide is replaced by a ketone (Schoeder et al., 2018). Accordingly, our quantum mechanics (QM) calculations show that the bound conformation in FUB is much lower in energy compared to the alternate conformation with a flipped dihedral angle between the amide and the indazole (Figure S5). Because this intramolecular interaction is absent in less potent analogs, the energy difference between the bound and flipped pose is significantly lower, and thus these compounds display a mix of conformations compromising their activity. 

The tert-butyl position in FUB, which overlaps with the terpenoid scaffold of the AM agonists, greatly diversifies in various derivatives of the Fubinaca family (Figure 1A). In the CB1-FUB-Gi-scFv16 structure, the ester moiety of FUB is in position to form polar interactions with H178[2.65] (Figure S4F). In addition, molecular mechanics calculations using JAWS (Michel et al., 2009) consistently showed the presence of a strongly bound (>3.5 kcal/mol) water molecule in between the amide linker, H178[2.65] and S383[7.39] (Figures S4F–S4H). MD simulations further support the presence of a polar network involving the ligand’s ester moiety, H178[2.65] and S383[7.39] , but the precise arrangement and behavior of waters tends to differ slightly from the JAWS-predicted network. Both ligand docking and 

Cell 176, 1–11, January 24, 2019 5 

**==> picture [60 x 60] intentionally omitted <==**

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

Figure 5. Structural Changes in CB1 on Nucleotide-free Gi Binding 

(A) Structural rearrangement of P-I-F motif in CB1, mOR (inactive—PDB: 4DKL, yellow; PDB: 6DDE, magenta), and b2AR (inactive—PDB: 2RH1, gray; active—PDB: 3SN6, green) upon activation. (B) The local unwinding of TM5 due to P[5.50] in active and inactive b2AR (green) and mOR (magenta) is not seen in CB1. See also Figure S6. 

comparison to an agonist bound-crystal structure (PDB: 5XRA) reveal that AM analogs and D[9] -THC have a hydrogen bonding group able to interact with this water molecule and/or S383[7.39] . In agreement with these findings, mutagenesis of S383[7.39] decreases agonist binding (Hua et al., 2017; Kapur et al., 2007), while SAR data with the hydrogen bonding moiety removed (-OH in terpenoid or cannabidiol scaffolds and amino-group in the FUB linker) reveal lower compound potency (Bow and Rimoldi, 2016). 

## Propagation of Agonist-Stabilized Structural Changes 

Excluding differences in regions that are stabilized by Gi binding to the receptor, the structures of FUB-Gi-bound and agonist-bound CB1 are remarkably similar (RMSD of Ca is 1.2) (Figure S6) despite the fact that the modified receptor construct used for determining the agonist-bound structure cannot signal (Hua et al., 2017). This finding is in contrast to the b2AR and mOR (Rosenbaum et al., 2011); (Nygaard et al., 2013), where agonist-binding alone, in the absence of G protein, cannot stabilize the fully extended active-state conformation of TM6. The higher propensity of CB1 to transition to an active conformation likely explains its inherently high basal activity (Seifert and Wenzel-Seifert, 2002), a feature that has been shown to be important for modulating neuronal development (Njoo et al., 2015). 

A striking difference between CB1, as well as a number of lipid-activated receptors with most other family A GPCRs, is the absence of the conserved P[5.50] , whose insertion creates a bulge in TM5 and local unwinding between residues 5.45 and 

5.48 to relieve geometric constraints and orient ligand-interacting residues to the binding pocket (Sansuk et al., 2011) (Figure 5A). In the b2AR and mOR, P[5.50] is involved in packing interactions with I[3.40] (found in 42% of class A GPCRs) and F[6.44] (found in 82% of class A GPCRs), which rearrange upon receptor activation (Figures 5A and 5B) (Huang et al., 2015). Although in activated CB1 we observe relatively small rearrangements in the homologous corresponding residues L[5.50] , V[3.40] , and L[6.44] , the discussed structural changes in TM6 drive L[6.44] to move away from V[3.40] and L[5.50] (Figure 5A). Crucially, the lack of unwinding in CB1 due to the absence of a proline at position 5.50, makes TM5 a more rigid helix connecting the binding pocket to the G protein coupling domain. While this highly conserved P[5.50] has been proposed to play a key role in the activation of many family A receptors (Deupi, 2014), the L[5.50] P mutation in the CB2 receptor disrupts signaling, indicating that a non-kinked TM5 is a prerequisite for cannabinoid receptor function (Zhou and Song, 2002). 

## Structure of the CB1-Gi Interface 

Globally, the structure of the CB1-Gi complex reveals a similar mode of interaction when compared to other Gi bound receptors. However, the N terminus of a5 in the CB1-Gi complex deviates from that of the G-protein in the mOR-Gi and b2AR-Gs complexes, resulting in a different relative orientation of the G protein. When aligned on the receptors, the Gi in complex with CB1 is rotated along the membrane by 18[�] when compared to mOR-Gi (Figure 6A). The difference is attributed to the more extensive interactions between the N terminus of the a5 helix and the extended TM5 of CB1 (Figures 6B and 6C), resulting in a relative configuration that is similar to a recently reported cryo-EM structure of a Rho-Gi complex (Kang et al., 2018). Although TM5 is also extended in the b2AR-Gs complex, it does not form strong interactions with the N terminus of the a5 helix due to the difference in G protein orientation (Figure 6D). Thus, the relative orientational differences between G protein and its respective receptors, as exemplified in the structures of CB1, mOR and b2AR complexes, is underlined by a change of interaction profiles. Gi interactions with CB1 are primarily between the a5 helix of Gi and ICL2, TM5, TM6, and H8 of CB1 

6 Cell 176, 1–11, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

Figure 6. Relative Orientation of CB1 and Gi and the Role of ICL2 in Coupling Selectivity (A) Comparison of the relative orientation of Gi bound to CB1 (blue), mOR (PDB: 6DDE, magenta), and b2AR (PDB: 3SN6, green) when aligned on the receptor. A magnified view is provided of the position of the a5 helices in CB1-Gai (yellow), mOR-Gai (wheat), and b2AR-Gas (orange). 

(B–D) Residues in the TM5–TM6 helices of CB1 (B), mOR (C), and b2AR (D) interacting with the a5 helix of Gai (yellow, bound to CB1; wheat, bound to mOR) and Gas (orange). 

(E–G) Interactions between ICL2 of CB1 (blue) and Gai (yellow) (E), mOR (magenta) and Gai (wheat) (F), and b2AR (green) and Gas (orange) (G). See also Figure S7 and Table S2. 

(Figures 6B and 6E), while only a weak hydrophobic contact is observed between the b2-b3 loop of Gi and ICL. In contrast, more extensive interactions are maintained between the ICL2 of the mOR and the aN-b1 loop of Gi and between ICL2 of the b2AR and the aN-b1 loop of Gs (Figures 6C, 6D, 6F, and 6G). A complete list of contacts is shown in Table S2. 

The C terminus of the a5 helix of Gi is in a similar position when bound to CB1 or mOR (Figure 6A), while the Gi complexes overlay well with the structures of rhodopsin, adenosine receptor, A1 (A1A) (Draper-Joyce et al., 2018), and the serotonin receptor, 5HT1B (Garcı´a-Nafrı´a et al., 2018), in complex with Gi. On the other hand, the C terminus of the a5 helix of Gs coupled to receptors (e.g., the b2AR) is displaced by �6.5 A[˚ ] , requiring a larger outward movement of TM6 compared to Gi coupled receptors. Accordingly, TM6 repositions by 12 A[˚] and 11.3 A[˚] in CB1-Gi and mOR-Gi, respectively, compared to �14 A[˚] in b2AR-Gs (Figure 6A), while an even larger outward displacement of TM6 is observed in the family B receptors in complex with Gs. Given 

these findings, we postulate that the ability to accommodate the C terminus of Gas is one of the determinants of Gs coupling specificity. For CB1 to couple to Gs, its TM6 would have to be able to move outward to a greater extent than that found in the CB1-Gi complex. In the b2AR, the larger displacement of TM6 can be attributed to G[6.38] and G[6.42] . Although there are no glycine residues at similar positions of CB1, G357[6.49] in the conserved C[6.47] W[6.48] X[6.49] P[6.50] motif may add extra flexibility to TM6. It is also worth noting that the homologous amino acid at position 6.49 in CB2 is phenylalanine and in mOR is threonine, and both of these receptors couple very poorly to Gs (Connor and Christie, 1999; Mnpotra et al., 2014). Conformational memory calculations showed that the flexibility of TM6 around positions 6.49 and 6.50 was significantly greater for CB1 compared to CB2, but the flexibility was greater for CB2 with the F[6.49] G mutation compared to CB1 with the G[6.49] F mutation (Barnett-Norris et al., 2002). 

## Role of CB1 ICL2 in Coupling Gi/s Coupling Promiscuity 

CB1 signals primarily through the Gi/Go family of G proteins but several studies indicate that the receptor can also couple to Gs (Felder and Glass, 1998; Glass and Felder, 1997). Multiple GPCRs have been shown to couple to different G protein subtypes, such as b2AR that couples to Gs and Gi, while some receptors couple almost exclusively to one G protein subtype (e.g., the mOR) (Connor and Christie, 1999), which couples predominantly to the Gi/Go family. While several studies have provided evidence that the mOR may couple to Gs in GTPgS binding and cyclic AMP (cAMP) accumulation assays (Chakrabarti et al., 2010; Szu¨ cs et al., 2004), the coupling is very weak, requiring much higher concentrations of agonist than is needed for Gi activation. Earlier work has shown that Gs- and Gi-coupled receptors appear to have different amino acid 

Cell 176, 1–11, January 24, 2019 7 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

Figure 7. Structural Changes in Gi on CB1 Binding 

**==> picture [324 x 338] intentionally omitted <==**

(A) Comparison of GDP-bound Gai (PDB: 1GP2, green) and nucleotide-free Gai from the CB1-Gi complex (yellow). The structures are aligned on the b-subunit (CB1-Gi, cyan and GDP-bound Gai, gray). GDP is shown as sticks. The alpha helical domain (AHD) seen in the GDP-bound structure is not resolved in the nucleotide-free Gai bound to CB1. 

(B) The a5 helix of Gai moves upward by 6 A[˚] and rotates �60[�] to engage the receptor core. The TCAT motif that coordinates the guanosine base of GDP in the GDP-bound structure (green) has shifted upward in the nucleotide-free Gai bound to mOR (wheat). In CB1-bound Gai (yellow), the TCAT motif is in a similar position as that seen in A2Abound mini-Gas (with GDP) (PDB: 5G53, purple). (C) The conformation of the P loop in CB1-bound Gi (yellow) will allow nucleotide binding as seen when overlaid with GDP-bound Gi (1GP2, smudge). However, in the nucleotide-free G protein bound to mOR (mOR-Gi, sand), there is a clash of the P loop with the GDP. 

## Structural Changes in Gi upon Binding CB1 

Upon coupling to CB1, the a5 helix of Gi undergoes a 6 A[˚] translation and a 60[�] rotation to engage the core of the receptor (Figures 7A and 7B). This is in good agreement with other complex structures where the translation of a5 has been shown to influence the position of the b6-a5 loop containing the conserved TCAT motif that directly contacts the guanosine base of GDP. The TCAT motif in Gi bound to CB1 has moved �2.0 A[˚] closer to the nucleotide-binding site compared to the recently published mOR-Gi structure (Figure 7C). Movement of the a5 helix disrupts interactions between its N terminus and the a1 helix, leading to displacement of the P loop (Figure 7B) and the destabilization of its contacts GDP, with eventual release of the nucleotide. The P loop in the CB1-Gi complex deviates from mOR-Gi by 3.5 A[˚] (at E43) but overlays well with the structures of GDP-bound Gai subunit (Figure 7C). Interestingly, the observed P loop conformation in the CB1-Gi complex may accommodate nucleotide binding, in contrast to the mOR-Gi complexwherethisis precluded due to potential steric clashes (Figure 7C). Thus, while both mOR-Gi and CB1-Gi complexes are nucleotide-free, the CB1-Gi complex may represent a conformation that is poised for GTP binding and activation (Figure 7C). 

preferences at the ICL2 position, with L222[ICL2] , in particular, reported to determine Gs protein coupling (Chen et al., 2010). A L222[ICL2] F mutation in CB1 increased basal signaling through Gs, whereas a L222[ICL2] A/L222[ICL2] P mutation led to a loss of Gs coupling but retained coupling to Gi. In the CB1-Gi structure, the ICL2 of the receptor interacts primarily with the a5 helix of Gi, but not with the aN-b1 loop as observed in the mOR-Gi and b2AR-Gs complexes. 

Notably, L222[ICL2] is only weakly interacting with L194 in the b2-b3 loop of Gi (Figure 6E). The homologous F139[ICL2] in the b2AR is buried in a hydrophobic pocket formed by the a5 helix, the aN-b2 loop, and the b2-b3 loop of Gs (Figure 6G), whereas the corresponding smaller residue V173[ICL2] in the mOR-Gi complex is surrounded by a similar hydrophobic pocket formed by I343, F336, and T340 of Gi (Figure 6B). In contrast, L222[ICL2] of CB1 points toward, but does not engage, the Gi hydrophobic pocket (Figure 6E). Although alanine substitution of F139[ICL2] in the b2AR and other Gs coupled receptors impairs their ability to activate G proteins (Moro et al., 1993), the L222[ICL2] A mutation in CB1 does not alter Gi coupling, suggesting that interactions between ICL2 and the hydrophobic pocket are less important for Gi coupling of this receptor. On the other hand, the bulkier phenylalanine in the CB1 L222[ICL2] F mutation would be expected to engage the hydrophobic pocket in Gs, which has been shown to be required for promoting GDP release. 

## Conclusions 

Delineating the structural basis for ligand efficacy and G protein recruitment at CB1 will aid in the design of drugs with high specificity and optimal therapeutic effects. Here, we report a cryo-EM structure of CB1-Gi complex revealing the binding mode of the highly potent synthetic cannabinoid FUB and the molecular characteristics of Gi protein coupling and activation. FUB 

8 Cell 176, 1–11, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

binding stabilizes the receptor in an active conformation through interference with the CB1 ‘‘toggle twin switch’’ residues F200[3.36] and W356[6.48] . The W356[6.48] repositioning results in the relaxation of the kink at P358[6.50] , thereby allowing the cytoplasmic part of TM6 to straighten and open up to accommodate the C-terminal a5 helix of Gi. The rigid C-shape geometry of FUB along with the strong aromatic interactions of its indazole ring with CB1 residues F200[3.36] and W356[6.48] might distinguish this full agonist from partial agonists like D[9] -THC, which has a better safety profile. 

Comparison of the CB1-Gi complex with the previously determined nucleotide-free structures of mOR-Gi, A1A-Gi, 5HT1B-Go, rhodopsin-Gi, and b2AR-Gs reveal largely similar overall interaction profiles for receptor-G protein binding. However, compared to the previously determined complex structures, the relative orientation of the CB1 and Gi is different, with a weaker interaction between the Ras domain of Gi and ICL2 of CB1. Determining G protein coupling specificity has been a major unanswered question in the field of GPCR biology. Although, the CB1-Gi complex provides insights into the promiscuous coupling of CB1 relative to CB2, it does not provide a universal molecular basis of G protein coupling specificity across all receptors. It is entirely possible that coupling specificity is determined at the initial stages of complex formation wherein a GDP-bound G protein engages the agonist-activated receptor. However, due to their highly dynamic and transient nature, such pre-equilibrium complexes are currently challenging for structure determination. 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d CONTACT FOR REAGENT AND RESOURCE SHARING d METHOD DETAILS 

   - B Purification of CB1 

   - B Expression and purification of Gi heterotrimer 

B Fluorescence - size exclusion chromatography 

   - B Purification of scFv16 

   - B CB1-Gi complex formation and purification 

   - B Cryo-EM data acquisition 

   - B Image processing and 3D reconstructions 

   - B Model building and refinement 

   - B GTP turnover assay 

   - B Docking and pose refinement 

   - B System setup for MD simulations 

   - B MD simulation force field parameters 

   - B MD simulation protocol 

   - B Quantum Chemical Calculations 

   - B Molecular Mechanics JAWS Simulations 

   - B Figure preparation 

- d DATA AND SOFTWARE AVAILABILITY 

## SUPPLEMENTAL INFORMATION 

Supplemental Information includes seven figures and three tables and can be found with this article online at https://doi.org/10.1016/j.cell.2018.11.040. 

## ACKNOWLEDGMENTS 

K.K. was supported by the NHMRC, Australia CJ Martin Fellowship. The work is supported by the NIH (R37DA036246 to B.K.K. and G.S. and R01GM083118 to B.K.K.). B.K.K. is a Chan Zuckerberg Biohub investigator. 

## AUTHOR CONTRIBUTIONS 

K.K. developed the procedure for and prepared the CB1-Gi complex, performed the GTP-turnover assay with assistance from D.H., and together with M.S.-B. modeled the structure in the cryo-EM map. M.S.-B. and H.H. obtained cryo-EM data, and M.S.-B processed data and obtained the cryo-EM map under supervision of G.S. S.D.B. synthesized ligands supervised by S.V.M. H.E.K. assisted in G protein and scFv16 purification. M.J.R. performed QM, docking, and JAWS calculations under the supervision of G.S. S.A.H. and N.R.L. generated docked poses and performed and analyzed molecular dynamics simulations under supervision of R.O.D. S.M. provided P2 virus for scFv16 production. W.I.W. provided advice on model refinement. D.L.F. provided advice on CB1 purification. K.K., M.S.-B., B.K.K., and G.S. wrote the manuscript with input from all the authors. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

Received: September 10, 2018 Revised: October 16, 2018 Accepted: November 26, 2018 Published: January 10, 2019 

## REFERENCES 

Adams, P.D., Afonine, P.V., Bunko´ czi, G., Chen, V.B., Echols, N., Headd, J.J., Hung, L.-W., Jain, S., Kapral, G.J., Grosse Kunstleve, R.W., et al. (2011). The Phenix software for automated determination of macromolecular structures. Methods 55, 94–106. 

Adams, A.J., Banister, S.D., Irizarry, L., Trecki, J., Schwartz, M., and Gerona, R. (2017). ‘‘Zombie’’ outbreak caused by the synthetic cannabinoid AMBFUBINACA in New York. N. Engl. J. Med. 376, 235–242. 

Afonine, P.V., Klaholz, B.P., Moriarty, N.W., Poon, B.K., Sobolev, O.V., Terwilliger, T.C., Adams, P.D., and Urzhumtsev, A. (2018). New tools for the analysis and validation of Cryo-EM maps and atomic models. Acta Crystallogr. D Struct. Biol. 74, 814–840. 

Atwood, B.K., Huffman, J., Straiker, A., and Mackie, K. (2010). JWH018, a common constituent of ‘Spice’ herbal blends, is a potent and efficacious cannabinoid CB receptor agonist. Br. J. Pharmacol. 160, 585–593. 

Ballesteros, J.A., and Weinstein, H. (1995). Integrated methods for the construction of three-dimensional models and computational probing of structure-function relations in G protein-coupled receptors. Meth. Neurosci. 25, 366–428. 

Barnett-Norris, J., Hurst, D.P., Buehner, K., Ballesteros, J.A., Guarnieri, F., and Reggio, P.H. (2002). Agonist alkyl tail interaction with cannabinoid CB1 receptor V6.43/I6.46 groove induces a helix 6 active conformation. Int. J. Quantum Chem. 88, 76–86. 

Betz, R.M. (2017). Dabble. Membrane protein builder and parameterizer. http://dabble.robinbetz.com. 

Bow,E.W.,andRimoldi, J.M.(2016).The structure-functionrelationships ofclassical cannabinoids: CB1/CB2 modulation. Perspect. Medicin. Chem. 8, 17–39. 

Campos, A.C., Moreira, F.A., Gomes, F.V., Del Bel, E.A., and Guimara˜ es, F.S. (2012). Multiple mechanisms involved in the large-spectrum therapeutic potential of cannabidiol in psychiatric disorders. Philos. Trans. R. Soc. Lond. B Biol. Sci. 367, 3364–3378. 

Case, D.A., Darden, T.A., Cheatham, T.E., Simmerling, C.L., Wang, J., Duke, R.E., Luo, R., Crowley, M., Walker, R.C., Zhang, W., et al. (2008). AMBER 10 (San Francisco: University of California). 

Cell 176, 1–11, January 24, 2019 9 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

Chai, J.-D., and Head-Gordon, M. (2008). Long-range corrected hybrid density functionals with damped atom-atom dispersion corrections. Phys. Chem. Chem. Phys. 10, 6615–6620. 

Chakrabarti, S., Liu, N.-J., and Gintzler, A.R. (2010). Formation of mu-/kappaopioid receptor heterodimer is sex-dependent and mediates female-specific opioid analgesia. Proc. Natl. Acad. Sci. USA 107, 20115–20119. 

Chen, X.P., Yang, W., Fan, Y., Luo, J.S., Hong, K., Wang, Z., Yan, J.F., Chen, X., Lu, J.X., Benovic, J.L., and Zhou, N.M. (2010). Structural determinants in the second intracellular loop of the human cannabinoid CB1 receptor mediate selective coupling to G(s) and G(i). Br. J. Pharmacol. 161, 1817–1834. 

Connor, M., and Christie, M.D. (1999). Opioid receptor signalling mechanisms. Clin. Exp. Pharmacol. Physiol. 26, 493–499. 

Cooper, Z.D. (2016). Adverse effects of synthetic cannabinoids: management of acute toxicity and withdrawal. Curr. Psychiatry Rep. 18, 52. 

Deupi, X. (2014). Relevance of rhodopsin studies for GPCR activation. Biochim. Biophys. Acta 1837, 674–682. 

Draper-Joyce, C.J., Khoshouei, M., Thal, D.M., Liang, Y.L., Nguyen, A.T.N., Furness, S.G.B., Venugopal, H., Baltos, J.A., Plitzko, J.M., Danev, R., et al. (2018). Structure of the adenosine-bound human adenosine A1 receptor-Gi complex. Nature 558, 559–563. 

Dror, R.O., Mildorf, T.J., Hilger, D., Manglik, A., Borhani, D.W., Arlow, D.H., Philippsen, A., Villanueva, N., Yang, Z., Lerch, M.T., et al. (2015). SIGNAL TRANSDUCTION. Structural basis for nucleotide exchange in heterotrimeric G proteins. Science 348, 1361–1365. 

Emsley, P., and Cowtan, K. (2004). Coot: model-building tools for molecular graphics. Acta Crystallogr. D Biol. Crystallogr. 60, 2126–2132. 

Fagan, S.G., and Campbell, V.A. (2014). The influence of cannabinoids on generic traits of neurodegeneration. Br. J. Pharmacol. 171, 1347–1360. 

Fantegrossi, W.E., Moran, J.H., Radominska-Pandya, A., and Prather, P.L. (2014). Distinct pharmacology and metabolism of K2 synthetic cannabinoids compared to D(9)-THC: mechanism underlying greater toxicity? Life Sci. 97, 45–54. 

Felder, C.C., and Glass, M. (1998). Cannabinoid receptors and their endogenous agonists. Annu. Rev. Pharmacol. Toxicol. 38, 179–200. 

Fernandez-Leiro, R., and Scheres, S.H.W. (2017). A pipeline approach to single-particle processing in RELION. Acta Crystallogr. D Struct. Biol. 73, 496–502. 

Frisch, M.J., Trucks, G.W., Schlegel, H.B., Scuseria, G.E., Robb, M.A., Cheeseman, J.R., Scalmani, G., Barone, V., Mennucci, B., and Petersson, G.A. (2009). Gaussian 09 Revision D. 01, 2009 (Wallingford, CT: Gaussian Inc.). 

Gamage, T.F., Farquhar, C.E., Lefever, T.W., Marusich, J.A., Kevin, R.C., McGregor, I.S., Wiley, J.L., and Thomas, B.F. (2018). Molecular and behavioral pharmacological characterization of abused synthetic cannabinoids MMBand MDMB-FUBINACA, MN-18, NNEI, CUMYL-PICA, and 5-fluoro-CUMYLPICA. J. Pharmacol. Exp. Ther. 365, 437–446. 

Garcı´a-Nafrı´a, J., Nehme´ , R., Edwards, P.C., and Tate, C.G. (2018). Cryo-EM structure of the serotonin 5-HT1B receptor coupled to heterotrimeric Go. Nature 558, 620–623. 

Ghanouni, P., Schambye, H., Seifert, R., Lee, T.W., Rasmussen, S.G., Gether, U., and Kobilka, B.K. (2000). The effect of pH on beta(2) adrenoceptor function. Evidence for protonation-dependent activation. J. Biol. Chem. 275, 3121– 3127. 

Glass, M., and Felder, C.C. (1997). Concurrent stimulation of cannabinoid CB1 and dopamine D2 receptors augments cAMP accumulation in striatal neurons: evidence for a Gs linkage to the CB1 receptor. J. Neurosci. 17, 5327–5333. 

Goddard, T.D., Huang, C.C., Meng, E.C., Pettersen, E.F., Couch, G.S., Morris, J.H., and Ferrin, T.E. (2018). UCSF ChimeraX: Meeting modern challenges in visualization and analysis. Protein Sci. 27, 14–25. 

Grant, T., Rohou, A., and Grigorieff, N. (2018). cisTEM, user-friendly software for single-particle image processing. eLife 7, e14874. 

Gregorio, G.G., Masureel, M., Hilger, D., Terry, D.S., Juette, M., Zhao, H., Zhou, Z., Perez-Aguilar, J.M., Hauge, M., Mathiasen, S., et al. (2017). Single- 

molecule analysis of ligand efficacy in b2AR-G-protein activation. Nature 547, 68–73. 

Guindon, J., and Hohmann, A.G. (2009). The endocannabinoid system and pain. CNS Neurol. Disord. Drug Targets 8, 403–421. 

Hanson, M.A., Roth, C.B., Jo, E., Griffith, M.T., Scott, F.L., Reinhart, G., Desale, H., Clemons, B., Cahalan, S.M., Schuerer, S.C., et al. (2012). Crystal structure of a lipid G protein-coupled receptor. Science 335, 851–855. 

Heymann, J.B. (2018). Guidelines for using Bsoft for high resolution reconstruction and validation of biomolecular structures from electron micrographs. Protein Sci. 27, 159–171. 

Hopkins, C.W., Le Grand, S., Walker, R.C., and Roitberg, A.E. (2015). Long-time-step molecular dynamics through hydrogen mass repartitioning. J. Chem. Theory Comput. 11, 1864–1874. 

Hua, T., Vemuri, K., Pu, M., Qu, L., Han, G.W., Wu, Y., Zhao, S., Shui, W., Li, S., Korde, A., et al. (2016). Crystal structure of the human cannabinoid receptor CB1. Cell 167, 750–762. 

Hua, T., Vemuri, K., Nikas, S.P., Laprairie, R.B., Wu, Y., Qu, L., Pu, M., Korde, A., Jiang, S., Ho, J.-H., et al. (2017). Crystal structures of agonist-bound human cannabinoid receptor CB1. Nature 547, 468–471. 

Huang, W., Manglik, A., Venkatakrishnan, A.J., Laeremans, T., Feinberg, E.N., Sanborn, A.L., Kato, H.E., Livingston, K.E., Thorsen, T.S., Kling, R.C., et al. (2015). Structural insights into m-opioid receptor activation. Nature 524, 315–321. 

Huang, J., Rauscher, S., Nawrocki, G., Ran, T., Feig, M., de Groot, B.L., Grubmu¨ ller, H., and MacKerell, A.D., Jr. (2017). CHARMM36m: an improved force field for folded and intrinsically disordered proteins. Nat. Methods 14, 71–73. 

Humphrey, W., Dalke, A., and Schulten, K. (1996). VMD: visual molecular dynamics. J. Mol. Graph. 14, 33–38, 27–28. 

Ignatowska-Jankowska, B.M., Baillie, G.L., Kinsey, S., Crowe, M., Ghosh, S., Owens, R.A., Damaj, I.M., Poklis, J., Wiley, J.L., Zanda, M., et al. (2015). A cannabinoid CB1 receptor-positive allosteric modulator reduces neuropathic pain in the mouse with no psychoactive effects. Neuropsychopharmacology 40, 2948–2959. 

Izzo, A.A., Borrelli, F., Capasso, R., Di Marzo, V., and Mechoulam, R. (2009). Non-psychotropic plant cannabinoids: new therapeutic opportunities from an ancient herb. Trends Pharmacol. Sci. 30, 515–527. 

Jorgensen, W.L., and Tirado-Rives, J. (2005). Molecular modeling of organic and biomolecular systems using BOSS and MCPRO. J. Comput. Chem. 26, 1689–1700. 

Jorgensen, W.L., Maxwell, D.S., and Tirado-Rives, J. (1996). Development and testing of the OPLS all-atom force field on conformational energetics and properties of organic liquids. J. Am. Chem. Soc. 118, 11225–11236. 

Kang, Y., Kuybeda, O., de Waal, P.W., Mukherjee, S., Van Eps, N., Dutka, P., Zhou, X.E., Bartesaghi, A., Erramilli, S., Morizumi, T., et al. (2018). Cryo-EM structure of human rhodopsin bound to an inhibitory G protein. Nature 558, 553–558. 

Kapur, A., Hurst, D.P., Fleischer, D., Whitnell, R., Thakur, G.A., Makriyannis, A., Reggio, P.H., and Abood, M.E. (2007). Mutation studies of Ser7.39 and Ser2.60 in the human CB1 cannabinoid receptor: evidence for a serineinduced bend in CB1 transmembrane helix 7. Mol. Pharmacol. 71, 1512–1524. 

Klauda, J.B., Venable, R.M., Freites, J.A., O’Connor, J.W., Tobias, D.J., Mondragon-Ramirez, C., Vorobyov, I., MacKerell, A.D., Jr., and Pastor, R.W. (2010). Update of the CHARMM all-atom additive force field for lipids: validation on six lipid types. J. Phys. Chem. B 114, 7830–7843. 

Koehl, A., Hu, H., Maeda, S., Zhang, Y., Qu, Q., Paggi, J.M., Latorraca, N.R., Hilger, D., Dawson, R., Matile, H., et al. (2018). Structure of the m-opioid receptor-Gi protein complex. Nature 558, 547–552. 

Lauckner, J.E., Hille, B., and Mackie, K. (2005). The cannabinoid agonist WIN55,212-2 increases intracellular calcium via CB1 receptor coupling to Gq/11 G proteins. Proc. Natl. Acad. Sci. USA 102, 19144–19149. 

Mackie, K. (2006). Cannabinoid receptors as therapeutic targets. Annu. Rev. Pharmacol. Toxicol. 46, 101–122. 

10 Cell 176, 1–11, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

Maeda, S., Koehl, A., Matile, H., Hu, H., Hilger, D., Schertler, G.F.X., Manglik, A., Skiniotis, G., Dawson, R.J.P., and Kobilka, B.K. (2018). Development of an antibody fragment that stabilizes GPCR/G-protein complexes. Nat. Commun. 9, 3712. 

Marsicano, G., and Lutz, B. (1999). Expression of the cannabinoid receptor CB1 in distinct neuronal subpopulations in the adult mouse forebrain. Eur. J. Neurosci. 11, 4213–4225. 

Mastronarde, D.N. (2005). Automated electron microscope tomography using robust prediction of specimen movements. J. Struct. Biol. 152, 36–51. McAllister, S.D., Hurst, D.P., Barnett-Norris, J., Lynch, D., Reggio, P.H., and Abood, M.E. (2004). Structural mimicry in class A G protein-coupled receptor rotamer toggle switches: the importance of the F3.36(201)/W6.48(357) interaction in cannabinoid CB1 receptor activation. J. Biol. Chem. 279, 48024–48037. 

Micale, V., Di Marzo, V., Sulcova, A., Wotjak, C.T., and Drago, F. (2013). Endocannabinoid system and mood disorders: priming a target for new therapies. Pharmacol. Ther. 138, 18–37. 

Michel, J., Tirado-Rives, J., and Jorgensen, W.L. (2009). Prediction of the water content in protein binding sites. J. Phys. Chem. B 113, 13337–13346. 

Mnpotra, J.S., Qiao, Z., Cai, J., Lynch, D.L., Grossfield, A., Leioatts, N., Hurst, D.P., Pitman, M.C., Song, Z.H., and Reggio, P.H. (2014). Structural basis of G protein-coupled receptor-Gi protein interaction: formation of the cannabinoid CB2 receptor-Gi protein complex. J. Biol. Chem. 289, 20259–20272. 

Moriarty, N.W., Grosse-Kunstleve, R.W., and Adams, P.D. (2009). Electronic ligand builder and optimization workbench (eLBOW): a tool for ligand coordinate and restraint generation. Acta Crystallogr. D Biol. Crystallogr. 65, 1074–1080. 

Moro, O., Lameh, J., Ho¨ gger, P., and Sade´ e, W. (1993). Hydrophobic amino acid in the i2 loop plays a key role in receptor-G protein coupling. J. Biol. Chem. 268, 22273–22276. 

Njoo, C., Agarwal, N., Lutz, B., and Kuner, R. (2015). The cannabinoid receptor CB1 interacts with the WAVE1 complex and plays a role in actin dynamics and structural plasticity in neurons. PLoS Biol. 13, e1002286. 

Noble, A.J., Dandey, V.P., Wei, H., Brasch, J., Chase, J., Acharya, P., Tan, Y.Z., Zhang, Z., Kim, L.Y., Scapin, G., et al. (2018). Routine single particle CryoEM sample and grid characterization by tomography. eLife 7, 32. 

Nygaard, R., Zou, Y., Dror, R.O., Mildorf, T.J., Arlow, D.H., Manglik, A., Pan, A.C., Liu, C.W., Fung, J.J., Bokoch, M.P., et al. (2013). The dynamic process of b(2)-adrenergic receptor activation. Cell 152, 532–542. 

Peace, M.R., Krakowiak, R.I., Wolf, C.E., Poklis, A., and Poklis, J.L. (2017). Identification of MDMB-FUBINACA in commercially available e-liquid formulations sold for use in electronic cigarettes. Forensic Sci. Int. 271, 92–97. 

Peisley, A., and Skiniotis, G. (2015). 2D projection analysis of GPCR complexes by negative stain electron microscopy. Methods Mol. Biol. 1335, 29–38. 

Pettersen, E.F., Goddard, T.D., Huang, C.C., Couch, G.S., Greenblatt, D.M., Meng, E.C., and Ferrin, T.E. (2004). UCSF Chimera–a visualization system for exploratory research and analysis. J. Comput. Chem. 25, 1605–1612. 

Pryce, G., and Baker, D. (2012). Potential control of multiple sclerosis by cannabis and the endocannabinoid system. CNS Neurol. Disord. Drug Targets 11, 624–641. 

Ranganathan, A., Dror, R.O., and Carlsson, J. (2014). Insights into the role of Asp79(2.50) in b2 adrenergic receptor activation from molecular dynamics simulations. Biochemistry 53, 7283–7296. 

Robertson, M.J., Tirado-Rives, J., and Jorgensen, W.L. (2015). Improved peptide and protein torsional energetics with the OPLSAA force field. J. Chem. Theory Comput. 11, 3499–3509. 

Rohou, A., and Grigorieff, N. (2015). CTFFIND4: fast and accurate defocus estimation from electron micrographs. J. Struct. Biol. 192, 216–221. 

Rosenbaum, D.M., Zhang, C., Lyons, J.A., Holl, R., Aragao, D., Arlow, D.H., Rasmussen, S.G.F., Choi, H.-J., Devree, B.T., Sunahara, R.K., et al. (2011). Structure and function of an irreversible agonist-b(2) adrenoceptor complex. Nature 469, 236–240. 

Ryckaert, J.-P., Ciccotti, G., and Berendsen, H.J.C. (1977). Numerical integration of the cartesian equations of motion of a system with constraints: molecular dynamics of n-alkanes. J. Comput. Phys. 23, 327–341. 

Salomon-Ferrer, R., Go¨ tz, A.W., Poole, D., Le Grand, S., and Walker, R.C. (2013). Routine microsecond molecular dynamics simulations with AMBER on GPUs. 2. Explicit solvent particle mesh Ewald. J. Chem. Theory Comput. 9, 3878–3888. 

Sansuk, K., Deupi, X., Torrecillas, I.R., Jongejan, A., Nijmeijer, S., Bakker, R.A., Pardo, L., and Leurs, R. (2011). A structural insight into the reorientation of transmembrane domains 3 and 5 during family A G protein-coupled receptor activation. Mol. Pharmacol. 79, 262–269. 

Schoeder, C.T., Hess, C., Madea, B., Meiler, J., and Mu¨ ller, C.E. (2018). Pharmacological evaluation of new constituents of ‘‘Spice’’: synthetic cannabinoids based on indole, indazole, benzimidazole and carbazole scaffolds. Forensic Toxicol. 36, 385–403. 

Seifert, R., and Wenzel-Seifert, K. (2002). Constitutive activity of G-proteincoupled receptors: cause of disease and common property of wild-type receptors. Naunyn Schmiedebergs Arch. Pharmacol. 366, 381–416. 

Shao, Z., Yin, J., Chapman, K., Grzemska, M., Clark, L., Wang, J., and Rosenbaum, D.M. (2016). High-resolution crystal structure of the human CB1 cannabinoid receptor. Nature 540, 602–606. 

Szu¨ cs, M., Boda, K., and Gintzler, A.R. (2004). Dual effects of DAMGO [D-Ala2,N-Me-Phe4,Gly5-ol]-enkephalin and CTAP (D-Phe-Cys-Tyr-D-TrpArg-Thr-Pen-Thr-NH2) on adenylyl cyclase activity: implications for mu-opioid receptor Gs coupling. J. Pharmacol. Exp. Ther. 310, 256–262. 

Udier-Blagovic,� M., Morales De Tirado, P., Pearlman, S.A., and Jorgensen, W.L. (2004). Accuracy of free energies of hydration using CM1 and CM3 atomic charges. J. Comput. Chem. 25, 1322–1332. 

Vanommeslaeghe, K., and MacKerell, A.D., Jr. (2012). Automation of the CHARMM general force field (CGenFF) I: bond perception and atom typing. J. Chem. Inf. Model. 52, 3144–3154. 

Vanommeslaeghe, K., Raman, E.P., and MacKerell, A.D., Jr. (2012). Automation of the CHARMM General Force Field (CGenFF) II: assignment of bonded parameters and partial atomic charges. J. Chem. Inf. Model. 52, 3155–3168. 

Westfield, G.H., Rasmussen, S.G.F., Su, M., Dutta, S., DeVree, B.T., Chung, K.Y., Calinski, D., Velez-Ruiz, G., Oleskie, A.N., Pardon, E., et al. (2011). Structural flexibility of the G alpha s alpha-helical domain in the beta2-adrenoceptor Gs complex. Proc. Natl. Acad. Sci. USA 108, 16086–16091. 

Williams, C.J., Headd, J.J., Moriarty, N.W., Prisant, M.G., Videau, L.L., Deis, L.N., Verma, V., Keedy, D.A., Hintze, B.J., Chen, V.B., et al. (2018). MolProbity: more and better reference data for improved all-atom structure validation. Protein Sci. 27, 293–315. 

Zheng, S.Q., Palovcak, E., Armache, J.-P., Verba, K.A., Cheng, Y., and Agard, D.A. (2017). MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron microscopy. Nat. Methods 14, 331–332. 

Zhou, D., and Song, Z.H. (2002). CB1 cannabinoid receptor-mediated tyrosine phosphorylation of focal adhesion kinase-related non-kinase. FEBS Lett. 525, 164–168. 

Cell 176, 1–11, January 24, 2019 11 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE|SOURCE|SOURCE|IDENTIFIER|IDENTIFIER|
|---|---|---|---|---|
||||||
|Chemicals, Peptides, and Recombinant|Proteins||||
|Uranyl formate|VWR||Cat# 101410-83||
|SR-141716|~~N~~IDA||~~N~~OCD-082||
|CP 55,490|~~N~~IDA||~~N~~OCD-091||
|MDMB-Fubinaca|This paper||N/A||
|ADB-Fubinaca|This paper||N/A||
|Cumyl-Fubinaca|This paper||N/A||
|FAB-144|~~T~~his paper||~~N~~/A||
|5F-SDB-006|~~T~~his paper||~~N~~/A||
|(C8)-CP 47,497|This paper||N/A||
|5F-AB-Fuppyca|This paper||N/A||
|Lauryl maltose neopentyl glycol (L-MNG)<br>Anatrace|||Cat# NG310||
|n-dodecyl-b-D-maltoside (DDM)|Anatrace||Cat# D310||
|Cholesteryl Hemisuccinate|Steraloids||Cat# C6823||
|PNGase F|~~N~~ew England Biolabs||Cat# P0704S||
|Benzamidine hydrochloride hydrate|Sigma Aldrich||Cat# B6506-100G||
|Leupeptin|~~S~~igma Aldrich||~~C~~at# 50-568-49||
|Lambda Protein Phosphatase|New England Biolabs||Cat# P0753L||
|TCEP|~~T~~hermo Fisher Scientifc||Cat# 77720||
|FLAG peptide|~~S~~tanford Pan Facility||N/A||
|GDP|~~S~~igma Aldrich||~~C~~at# G7127||
|GDN (glyco-diosgenin): Synthetic<br>Digitonin Substitute|Anatrace||Cat# GDN101||
|EDTA|~~S~~igma Aldrich||~~C~~at# E5134-500G||
|ESF921 culture medium|Expression Systems||Cat# 96-001||
|2-Mercaptoethanol|Sigma Aldrich||Cat# M6250-100ML||
|Apyrase|New England Biolabs||Cat# M0398S||
||||||
|Critical Commercial Assays|||||
|GTPase-Glo assay|Promega||Cat# V7682||
|Deposited Data|||||
|CB1-Gicoordinates|~~T~~his paper||~~P~~DB: 6N4B||
|CB1-GiEM map|This paper||EMDB: EMD-0339||
||||||
|Experimental Models: Cell Lines|||||
|~~Spodoptera frugiperda Sf9 cells~~|~~E~~xpression Systems||N/A||
|Trichuplusia ni Hi5cells|Expression Systems||N/A||
||||||
|Oligonucleotides|||||
|CB1 fwd primer- aaatttGGATCCATGA<br>AGACGATCATCGCCCTGAGC|Stanford Pan Facility||N/A||
|CB1 rev primer- TAGTGATGGTGATGAT<br>GGTGCAGAGCCTCGGCAGACGTGTC<br>Stanford Pan Facility|||N/A||
||||||
|Recombinant DNA|||||
|pFastbac-CB1|This paper||N/A||
|pVL1392-Ga|~~T~~his paper||~~N~~/A||
||||||



(Continued on next page) 

e1 Cell 176, 1–11.e1–e5, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

|Continued|||||
|---|---|---|---|---|
|REAGENT or RESOURCE|SOURCE||IDENTIFIER||
|pVL1392duet-Gbg|This paper||N/A||
|pVL1392-GP67-scFv16|This paper||N/A||
||||||
|Software and Algorithms|||||
|SerialEM|~~M~~astronarde, 2005||http://bio3d.colorado.edu/SerialEM/||
|MotionCor2|~~Z~~heng et al., 2017||~~h~~ttp://msg.ucsf.edu/em/software/motioncor2.html||
|CTFFIND4|~~R~~ohou and Grigorieff, 2015||http://grigorieffab.janelia.org/ctffnd4||
|Relion 2.1.0|Fernandez-Leiro and Scheres, 2017<br>https://www2.mrc-lmb.cam.ac.uk/relion/<br>~~i~~ndex.php?title=Download_&_install||||
|CisTEM|~~G~~rant et al., 2018||~~h~~ttps://cistem.org/||
|Phenix|~~A~~dams et al., 2011||~~h~~ttps://www.phenix-online.org/||
|B-soft|~~H~~eymann, 2018||~~h~~ttps://lsbr.niams.nih.gov/bsoft/||
|UCSF Chimera|~~P~~ettersen et al., 2004||~~h~~ttps://www.cgl.ucsf.edu/chimera/||
|PyMol|~~S~~chro¨dinger||~~h~~ttps://pymol.org/2/||
|Chimera X|~~G~~oddard et al., 2018||https://www.rbvi.ucsf.edu/chimerax/||
|COOT|~~E~~msley and Cowtan, 2004||https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/||
|~~Molprobity~~|~~W~~illiams et al., 2018||http://molprobity.biochem.duke.edu/||
|Glide|Schro¨dinger||~~h~~ttps://www.schrodinger.com/glide||
|Maestro|Schro¨dinger||https://www.schrodinger.com/maestro||
|Prime|Schro¨dinger||https://www.schrodinger.com/prime||
|Dabble|Betz, 2017||http://dabble.robinbetz.com/||
|ParamChem|Vanommeslaeghe et al., 2012||N/A||
|GAUSSIAN|Frisch et al., 2009||http://gaussian.com||
|MCPRO|Jorgensen and Tirado-Rives, 2005||http://zarbi.chem.yale.edu/software.html||
|PMEMD|Case et al., 2008; Salomon-Ferrer<br>et al., 2013||N/A||
|VMD|Humphrey et al., 1996||N/A||
|Prism (v6)|GraphPad||https://www.graphpad.com||



## CONTACT FOR REAGENT AND RESOURCE SHARING 

Further information and requests for reasorces and reagents should be directed to and will be fulfilled by the Lead Contact, Georgios Skiniotis (yiorgo@stanford.com). 

## METHOD DETAILS 

## Purification of CB1 

Human full-length CB1 with N-terminal FLAG and C-terminal hexahistadine tag was expressed in Spodoptera frugiperda Sf9 insect cells using the baculovirus method (Expression Systems). The same construct with an eGFP (CB1-eGFP) at the C terminus was used for small-scale coupling and FSEC studies. The receptor was extracted from insect cell membranes with 1% lauryl maltose neopentyl glycol (L-MNG) and purified by nickel-chelating Sepharose chromatography. The Ni-NTA pure eluate was applied to a M1 anti-FLAG immunoaffinity resin and washed with progressively decreasing concentration of inverse agonist, SR and increasing concentration of agonist FUB. The receptor was eluted in a buffer consisting of 20 mM HEPES pH 7.5, 150 mM NaCl, 0.05% L-MNG, 0.005% cholesterol hemisuccinate (CHS), 2 mM FUB, FLAG peptide and 5 mM EDTA. The final step of purification was size exclusion chromatography on Superdex 200 10/300 gel filtration column (GE) in 20 mM HEPES pH 7.5, 150 mM NaCl, 0.02% L-MNG, 0.002% CHS, and 2 mM FUB. Finally, agonist-bound CB1 was concentrated to �500 mM and flash frozen and stored in �80[�] C. 

## Expression and purification of Gi heterotrimer 

Heterotrimeric Gi was expressed and purified as previously described (Dror et al., 2015). Briefly, Trichuplusia ni Hi5 insect cells were infected with two viruses, one encoding the wild-type human Gai subunit and another encoding the wild-type human b1g2 subunits with an histidine tag inserted at the amino terminus of the b subunit. Cells expressing the heterotrimetric G-protein were harvested 48 hours post infection. After cells were lysed in hypotonic buffer, heterotrimeric Gib1g2 was extracted in a buffer containing 1% 

Cell 176, 1–11.e1–e5, January 24, 2019 e2 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

sodium cholate and 0.05% n-dodecyl-b-D-maltoside (DDM, Anatrace). The heterotrimer containing soluble fraction was purified using Ni-NTA chromatography, and the detergent was exchanged from cholate/DDM to DDM on column. Human rhinovirus 3C protease (3C protease) was added and the histidine tag was cleaved on-column overnight at 4[�] C. The flow through was collected and was further purified by size exclusion chromatography on Superdex 200 10/300 gel filtration column (GE) into 20 mM HEPES pH 7.5, 100 mM NaCl, 0.02% DDM, 100 mM TCEP, 10 mM GDP, and concentrated to �20 mg/mL for further complexing with the CB1. 

## Fluorescence - size exclusion chromatography 

Purified CB1-eGFP (1.25 M excess) was incubated with Gi (that has been incubated with 1% L-MNG for 1 hour), in the presence of the tested ligands at room temperature for 1 hour, after which apyrase was added and further incubated on ice for 1 hour. The sample was applied to a Superdex 200 10/300 column (equilibrated in 20mM HEPES pH 7.5, 100mM NaCl, 0.01% L-MNG/0.001% CHS) inline with a Jasco FP 2020 Plus fluorescence detector set to an excitation of 480 nm and an emission of 512 nm. Complex formation and complex stability was monitored for each ligand by analyzing the extent of free receptor and complex peaks. 

## Purification of scFv16 

scFv16 was purified as previously described (Koehl et al., 2018). Briefly, hexahistidine-tagged scFv was expressed in secreted form from Trichuplusia ni Hi5 insect cells using the baculoviral method, and purified by Ni-NTA chromatography. After balancing the pH and quenching chelating agents, the supernatant from baculoviral infected cells was loaded onto Ni-NTA resin. The protein was eluted in 20 mM HEPES pH 7.5, 500 mM NaCl, and 250 mM imidazole and incubated with 3C protease to cleave the carboxy-terminal hexahistidine tag. Following dialysis into a buffer consisting of 20mM HEPES pH 7.5 and 100 mM NaCl, cleaved scFv16 was further purified by reloading over Ni-NTA resin. The flow-through was collected and applied over a Superdex 200 16/60 column. scFv16 fractions were pooled, concentrated, and flash frozen. 

## CB1-Gi complex formation and purification 

Purified Gi1 heterotrimer in DDM was incubated with 1% L-MNG for 1 hour at 4[�] C to exchange the detergent and simultaneously, FUB-bound CB1 was incubated with ZCZ at 24[�] C. The FUB- and ZCZ-bound CB1 was incubated with a 1.25 molar excess of detergent exchanged Gi heterotrimer. The reaction tube was incubated at 24[�] C for 3 hours and was followed by the addition of apyrase, to stabilize a nucleotide-free complex (Westfield et al., 2011), for an additional 1.5 hour at 4[�] C. A 4-fold volume of 20 mM HEPES pH 7.5, 100 mM NaCl, 0.8% L-MNG/0.08% CHS, 0.27% GDN/0.027% CHS, 1 mM MgCl2, 10 mM FUB, 1 mM ZCZ and 2 mM CaCl2 was added to the complexing reaction and purified by M1 anti-FLAG affinity chromatography to remove excess G protein. The complex was eluted in 20mM HEPES pH 7.5, 100mM NaCl, 0.01% L-MNG/0.001% CHS, 0.0033% GDN/0.00033% CHS 10 mM FUB, 1 mM ZCZ, 5 mM EDTA, and FLAG peptide. The eluted complex was supplemented with 100 mM TCEP to provide a reducing environment. A 2 molar excess of scFv16 was added to the preparation and incubated overnight at 4[�] C. The CB1-Gi-scFv16 complex was purified by size exclusion chromatography on a Superdex 200 10/300 Increase column in 20mM HEPES pH 7.5, 100mM NaCl, 10 mM FUB, 1 mM ZCZ, 0.00075% L-MNG/0.000075% CHS and 0.00025% GDN/0.000025% CHS. Peak fractions were concentrated to �16 mg/mL for electron microscopy studies. 

## Cryo-EM data acquisition 

For cryo-EM 3.5 mL of purified CB1-Gi complex at 5 mg/ml concentration were applied on glow-discharged holey carbon gold grids (Quantifoil R1.2/1.3, 200 mesh). The grids were blotted using a Vitrobot Mark IV (FEI) with 1 s blotting time at 100% humidity and plunge-frozen in liquid ethane. A total of 2,759 movies were recorded on a Titan Krios electron microscope (Thermo Fisher Scientific - FEI) operating at 300 kV at a calibrated magnification of x29,000 and corresponding to a magnified pixel size of 0.86 A[˚ ] . Micrographs were recorded using a K2 Summit direct electron camera (Gatan) with a dose rate of �5.0 electrons/A[˚][ 2] /s and defocus values ranging from �0.7 mm to �2.5 mm. The total exposure time was 10.0 s and intermediate frames were recorded in 0.2 s intervals resulting in an accumulated dose of �58 electrons per A[˚][ 2] and a total of 50 frames per micrograph. Automatic data acquisition was done using SerialEM (Mastronarde, 2005). 

## Image processing and 3D reconstructions 

Micrographs were subjected to beam-induced motion correction using MotionCor2 (Zheng et al., 2017). CTF parameters for each micrograph were determined by CTFFIND4 (Rohou and Grigorieff, 2015). An initial set of 1,178,914 particle projections were extracted using semi-automated procedures and subjected to reference-free two-dimensional classification in RELION 2.1.0 (Fernandez-Leiro and Scheres, 2017). From this step, 562,312 particle projections were selected for further processing. The map of m-opioid receptor (EMDB- 7868) low passed filtered to 60 A[˚] was used as an initial reference model for maximum-likelihood-based threedimensional classifications. Conformationally homogeneous groups accounting for 177,787 particles, forming class averages with well resolved features for all subunits, were subjected to 3D masked refinement in Frealign (CisTEM) (Grant et al., 2018) followed by map sharpening applying temperature-factors of �90 A[˚ ] 2 and �60 A[˚ ] 2 for the low- and high- resolution ends of the amplitude spectrum, respectively. The final map has an indicated global nominal resolution of 3.0 A[˚] (Figures S1 and S2). Reported resolution is based 

e3 Cell 176, 1–11.e1–e5, January 24, 2019 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

on the gold-standard Fourier shell correlation (FSC) using the 0.143 criterion and is in agreement with both Relion 2.1.0 and M-triage as implemented in Phenix (Afonine et al., 2018). Local resolution was determined using B-soft (Heymann, 2018) with half map reconstructions as input maps (Figure S2C). 

## Model building and refinement 

The initial template of CB1 was derived from the crystal structure of agonist-bound CB1 (PDB 5XRA). The m-opioid receptor coordinates (PDB 6DDE) were used as initial models for the Gi and scFv16. Agonist coordinates and geometry restrains were generated using phenix.elbow (Moriarty et al., 2009). Models were docked into the EM density map using UCSF Chimera (Pettersen et al., 2004), followed by iterative manual building in Coot (Emsley and Cowtan, 2004). The final model was subjected to global refinement and minimization in real space using phenix.real_space_refine in Phenix (Adams et al., 2011). Residues in regions of weak density were stubbed to their Cb position, while preserving sequence information (Stubbed CB1 residues shown in Table S2). Molprobity (Williams et al., 2018) was used to evaluate model geometry. FSC curves were calculated between the resulting model and the half map used for refinement as well as between the resulting model and the other half map for cross-validation (Figure S2). The final refinement parameters are provided in Table S1. 

## GTP turnover assay 

Analysis of GTP turnover was performed by using a modified protocol of the GTPase-Glo assay (Promega) described previously (Gregorio et al., 2017). This assay detects the amount of GTP remaining after GTP hydrolysis, which is enhanced upon activation of the G protein by the ligand-bound receptor. After the GTPase reaction, addition of GTPase-Glo-reagent converts the remaining GTP to ATP that is converted to a luminescent signal by the detection reagent. CB1 was incubated with and without ligands for 30 minutes at room temperature. The reaction was started by mixing the unliganded or liganded-CB1 and Gi in an assay buffer containing 20 mM HEPES, pH 7.5, 50 mM NaCl, 0.01% L-MNG, 100 mM TCEP, 10 mM mM GDP and 5 mM GTP. After incubation for 60 minutes (agonists assay) and 30 minutes (for PAM assay), reconstituted GTPase-Glo-reagent was added to the sample and incubated for 30 min at room temperature. Luminescence was measured after the addition of detection reagent and incubation for 10 min at room temperature using a SpectraMax Paradigm plate reader. 

## Docking and pose refinement 

To select ligand poses for simulation, we performed docking with Glide SP (Schro¨ dinger) against an earlier refinement of the cryo-EM structure (model available upon request). We used the enhanced sampling option to improve conformer generation (set to four times the usual amount of sampling) and requested at most 100 output poses. Subsequent poses were aligned within the electron density map, and two distinct poses that fit within the density were selected for simulation, along with a pose obtained through manual modeling whose orientation also differed from the two Glide-generated poses. In order to compare docking poses for other CB1 agonists, Glide XP docking was performed with CP55,940, D[9] -THC, and the fluoroalkyl analog of FUB. 

## System setup for MD simulations 

Prior to running MD simulations of CB1, we performed several steps of refinement and modeling of the cryo-EM structure. The CB1 model was treated in isolation after removing the Gi atoms form the cryo-EM structure. The Advanced Homology Modeling tool in Maestro (Schro¨ dinger) was used to remodel ECL2 to match the conformation observed in 5XRA. Prime (Schro¨ dinger) was used to insert missing side chains, hydrogens and cap the termini of the protein while D163 and D213 were manually protonated, in accordance with evidence that these residues become protonated upon GPCR activation (Ghanouni et al., 2000; Ranganathan et al., 2014). For each of the final candidate ligand poses, the ligand was added to the prepared protein resulting in three unique protein-ligand complexes. Each prepared protein-ligand complex was inserted into a pre-equilibrated palmitoyl oleoylphosphatidylcholine (POPC) bilayer using Dabble (Betz, 2017). The final system dimensions were 74.1 3 76.8 3 94.3 A[˚ ] , including 121 lipids, �10,600 water molecules, 13 sodium ions and 29 chloride ions. 

## MD simulation force field parameters 

The CHARMM36m parameters were used to model protein molecules, CHARMM36 parameters for lipids and salt and the CHARMM36 TIP3P model for water (Huang et al., 2017; Klauda et al., 2010). Parameters for the ligand were generated using the ParamChem webserver and CGenFF parameterset (Vanommeslaeghe and MacKerell, 2012; Vanommeslaeghe et al., 2012) 

## MD simulation protocol 

MD simulations were performed on GPUs with the CUDA enabled version of PMEMD in AMBER16 (Case et al., 2008; Salomon-Ferrer et al., 2013). Each simulation underwent a similar equilibration procedure. Following an initial minimization, each system underwent a heating using the Langevin thermostat from 0K to 100K in the NVT ensemble over 12.5 picoseconds (ps) with 10 kcal mol[-1] A[˚][ -2] harmonic restraints on all non-hydrogen atoms in the protein, ligand and lipid. The heated then continued in the NPT ensemble with semi-isotropic coupling for 125 ps and a pressure of 1 bar to a final temperature of 310K with 5.0 kcal mol[-1] A[˚][ -2] harmonic restraints. Further equilibration was then carried out at 310K with harmonic restraints applied to the protein starting at 5.0 kcal mol[-1] A[˚][ -2] and reduced in a stepwise fashion every 2 ns (ns) for 10 ns, followed by 0.1 kcal mol[-1] A[˚][ -2] restraints for 20 ns for a total of 30 ns 

Cell 176, 1–11.e1–e5, January 24, 2019 e4 

Please cite this article in press as: Krishna Kumar et al., Structure of a Signaling Cannabinoid Receptor 1-G Protein Complex, Cell (2019), https://doi.org/10.1016/j.cell.2018.11.040 

**==> picture [60 x 60] intentionally omitted <==**

of equilibration. Production simulations were run at 310K and 1 bar in the NPT ensemble using the Langevin thermostat and Monte Carlo barostat. Throughout the final stages of equilibration and production, 5.0 kcal mol[-1] A[˚][ -2] harmonic restraints were placed on all residues of CB1 that were within 5A[˚] of Gi in the CB1- Gi complex to ensure that the receptor remained in the active state in the absence of the G-protein. 

Each simulation used periodic boundaries and employed a time step of 4.0 fs using hydrogen mass repartitioning (Hopkins et al., 2015). All bond lengths to hydrogens were constrained by SHAKE (Ryckaert et al., 1977). Short range electrostatic and van der Waals interactions were cut off at 9.0 A[˚ ] , while long range electrostatic interactions were computed using the particle mesh Ewald method. The FFT grid size was chosen such that the width of a single grid cell was approximately 1 A[˚ ] . For each of the three simulated poses, we performed three independent simulations, each of 2.0 ms in length. 

Snapshots from each trajectory were saved every 200 ps during the production phase of each simulation and visualized using VMD (Humphrey et al., 1996). Analysis was carried out using a combination of VMD and locally developed analysis tools. 

## Quantum Chemical Calculations 

Quantum chemical dihedral scans were prepared using the GAUSSIAN software (Frisch et al., 2009) for each of the indazole-amide derivatives. All calculations were performed with the uB97-xd functional (Chai and Head-Gordon, 2008) and the 6-311++(2d,2p) basis set. The annotated dihedral was scanned in increments of 15 degrees with other degrees of freedom optimized. All compounds had minima at �0 and �180 degrees, the relative energies of which are given in Figure S5. 

## Molecular Mechanics JAWS Simulations 

JAWS simulations (Michel et al., 2009) were prepared from the cryo-EM structure of the CB1 receptor with the MCPRO software package (Jorgensen and Tirado-Rives, 2005). A 15A[˚] sphere around FUB was solvated with theta waters to be sampled in the simulation and treated as flexible. The protein was simulated with the OPLS-AA/M force field (Robertson et al., 2015), the ligand used the OPLS-AA/CM1A force field (Udier-Blagovic et al., 2004� ) and the TIP4P model was used for the water (Jorgensen et al., 1996). Simulations used 5 million Monte Carlo steps for solvent equilibration, 10 million Monte Carlo steps in identifying hydration sites, and 50 million Monte Carlo steps in the production phase. Free energies of binding were then calculated from the percentage of the simulation where a given water molecule was predicted to exist, with water molecules sufficiently energetically favorable to always be existent given an energy of > 3.5 kcal/mol. 

## Figure preparation 

Figures were created using PyMol (https://pymol.org/2), and the UCSF Chimera X package (Goddard et al., 2018). 

## DATA AND SOFTWARE AVAILABILITY 

The cryo-EM density map has been deposited in the Electron Microscopy Data Bank (EMDB) under accession code EMD-0339 and model coordinates have been deposited in the Protein Data Bank (PDB) under accession number 6N4B. 

e5 Cell 176, 1–11.e1–e5, January 24, 2019 

## Supplemental Figures 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [324 x 469] intentionally omitted <==**

Figure S1. Complex Formation and Cryo-EM Data Processing, Related to Figures 1 and 2 (A) Fluorescence-detection size exclusion chromatography (FSEC) traces showing complex peak and free receptor peak with the different ligands. (B) Representative reference-free 2D cryo-EM averages of CB1-Gi. The diameter of the circular mask is 18 nm. (C) Cryo-EM data processing flow chart of CB1, including particle selection, classifications and density map reconstruction. Details are provided in the STAR Methods. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [324 x 468] intentionally omitted <==**

Figure S2. Map and Model Quality and Local Resolution, Related to Figures 2 and 3 (A) Gold standard Fourier shell correlation (FSC) curves of two individual half maps indicating an average resolution of 3 A[˚] at 0.143 FSC. (B) FSC curves of the model versus the final EM map (blue) and the two independent half maps (gold and green). FSC plots were calculated with Phenix_M-triage. (C) Density map colored by local resolution indicating a range of 2.7-3.6 A[˚] resolution in most map regions. Highest resolution is observed at the core of the Gi-protein complex with indicated local resolution better than 2.8 A[˚] for most residues. Color scheme for resolution values is presented in the bottom. (D) FUB in density. Density is contoured at s = 3.0 around the ligand. (E) Ensemble of FUB poses observed in MD simulations sampled every 150 ns fitted in the cryo-EM map density. (F) CB1 helixes 1-8 in density. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [324 x 358] intentionally omitted <==**

Figure S3. Ligand Binding Pocket and Entry Pathway, Related to Figure 4 (A) A snapshot from MD simulation (yellow) with the N terminus in the most outward position and TM1-TM7 farthest apart compared to the CB1-Gi structure (blue). (B-C) The presence and absence of lipid access channel between TM1 and TM7 in taranabant- and FUB-bound structures respectively. (D) Surface representation of a snapshot from MD simulation showing the ligand access channel between TM1 and TM7. (E) A graph showing the CB1 N terminus (in black) outward movement as measured by the distance observed between the N terminus (Ca F108[N-ter] ) and ICL2 (Ca P269[ICL2] ). This N terminus movement coincides with the increase in TM1-TM7 distance (shown in red) distance as measured by (Ca Q116[1.32] ) and ICL2 (Ca T377[7.32] ). The yellow background colors indicate the presence of lipid binding during the simulation. (F) An example of lipid binding the TM1-TM7 gap during MD simulation and the lipid molecule overlaid on the taranabant-bound structure. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 431] intentionally omitted <==**

Figure S4. Interaction of Agonists with the CB1, Related to Figure 4 (A) FUB assumes a C-shape configuration that occupies most of the binding pocket volume. (B) Docking of FUB analog 5F-MDMB-PINACA (PIN) with a fluoroalkyl moiety to the CB1 binding pocket, with alkyl chain overlapping with the p-fluorobenzyl group in FUB. (C) Docking results of one pose of D[9] -THC (green) superimposed with the structure of FUB (orange) and the crystal structure of AM-11542 (cyan, PDB 5XRA) indicating that the alkyl chain in D[9] -THC overlaps with the p-Fluorobenzyl group and the alkyl chains in FUB and AM-11542, respectively. (D) The docking pose from (C) (light green) superimposed with an alternative docked pose for D[9] -THC (dark green), indicating that the alkyl chain in D[9] -THC fluctuates between two main poses. (E) Chemical structures of FUB, AM-11542 and D[9] -THC, with suggested mechanism for D[9] -THC partial agonism as implemented from the docking experiments. Moieties that interfere with toggle switch activation are highlighted in orange. (F-H) JAWS calculation demonstrating a tightly bound water molecule mediating interactions between FUB (F), H178[2.65] , and S383[7.39] . Both AM-11542 (PDB 5XRA, (G) and CP-55,940 (docked, (H) have hydrogen bonding groups in this region. Chemical structures are showed on bottom, hydrogen bonding group highlighted in light yellow. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 224] intentionally omitted <==**

Figure S5. QM Calculations, Related to Figure 4 (A) Diagram of the dihedral being flipped in the full FUB molecule. (B) Comparison of the relative QM energies for the cis/trans flip in derivatives of FUB (orange) and other analogs with the same scaffold. The compounds are: Orange (FUB) with both an indazole and an amide (X = N, Y = NH); cyan with an indazole but no amide (X = N, Y = CH2); green an amide and an indole (X = CH, Y = NH2); and yellow with an indole and no amide (X = CH, Y = CH2). Positions X and Y are denoted with red circles. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [324 x 167] intentionally omitted <==**

Figure S6. Structural Changes in CB1 on Nucleotide-free Gi Binding, Related to Figure 5 (A) Comparison of R[3.50] and the NPXXY motif conformations in agonist-bound (PDB 5XRA, cyan) and Gi-bound CB1 (blue). (B) The TM6 outward movement on agonist binding (cyan) is further enhanced upon Gi binding (blue) in comparison to antagonist-bound CB1 (PDB 5U09, orange). 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [322 x 222] intentionally omitted <==**

Figure S7. Coupling Selectivity, Related to Figure 6 Comparison of the position of residues at 6.33 and 6.34 in CB1-Gi (blue and yellow) and b2AR-Gs (green and orange) structures. 

