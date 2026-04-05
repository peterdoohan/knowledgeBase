**==> picture [523 x 31] intentionally omitted <==**

Article 

https://doi.org/10.1038/s41467-024-55248-0 

## INSIHGT: an accessible multi-scale, multimodal 3D spatial biology platform 

Received: 28 June 2024 Chun Ngo Yau 1,2,8, Jacky Tin Shing Hung 1,2,8, Robert A. A. Campbell 3, 1,2,4 1,2 Thomas Chun Yip Wong[1,2] , Bei Huang , Ben Tin Yan Wong , Accepted: 6 December 2024 Nick King Ngai Chow[1,2] , Lichun Zhang[1,2] , Eldric Pui Lam Tsoi[1,2] , Yuqi Tan 5, Joshua Jing Xi Li 6, Yun Kwok Wing 1,2,4 & Hei Ming Lai 1,2,7 Check for updates 

Biological systems are complex, encompassing intertwined spatial, molecular and functional features. However, methodological constraints limit the completeness of information that can be extracted. Here, we report the development of INSIHGT, a non-destructive, accessible three-dimensional (3D) spatial biology method utilizing superchaotropes and host-guest chemistry to achieve homogeneous, deep penetration of macromolecular probes up to centimeter scales, providing reliable semi-quantitative signals throughout the tissue volume. Diverse antigens, mRNAs, neurotransmitters, and posttranslational modifications are well-preserved and simultaneously visualized. INSIHGT also allows multi-round, highly multiplexed 3D molecular probing and is compatible with downstream traditional histology and nucleic acid sequencing. With INSIHGT, we map undescribed podocyte-to-parietal epithelial cell microfilaments in mouse glomeruli and neurofilament-intensive inclusion bodies in the human cerebellum, and identify NPY-proximal cell types defined by spatial morpho-proteomics in mouse hypothalamus. We anticipate that INSIHGT can form the foundations for 3D spatial multi-omics technology development and holistic systems biology studies. 

The complexity of biological systems mandates high-dimensional measurements to obtain an integrative understanding. However, measurements are inevitably perturbative, affecting the authenticity of the retrieved information. Spatially resolved transcriptomics[1] and highly multiplexed immunohistochemistry (IHC)[2] have proven to be powerful approaches to extract spatial molecular insights from tissue slices, but the two-dimensional (2D) readout limits the representativeness of the information extracted. Meanwhile, three-dimensional (3D) multiplexed visualization of tissue structural and molecular features can reveal previously unknown organization principles[3][,][4] . Optical 

tissue clearing technologies promises to reveal the authentic 3D nature of tissue architecture and molecular distributions[5] . Despite its significant advancements, the achievable depths of probe penetration limits the depth of analysis[6] . The limited penetration of antibodies in 3D IHC represents one of the most significant barrier to 3D spatial biology[6] . 

In recent years, multiple creative solutions have been proposed for deep immunohistochemistry[7][–][10] . However, an accessible technology that balances the authenticity and volume of data extracted is still lacking. For example, signal homogeneity across penetration depth is 

1Department of Psychiatry, Faculty of Medicine, The Chinese University of Hong Kong, Hong Kong SAR, China. 2Li KaShing Institute of Health Sciences, Faculty of Medicine, The Chinese University of Hong Kong, Hong Kong SAR, China.[3] Sainsbury Wellcome Centre for Neural Circuits and Behaviour, University College London, London, UK.[4] Li Chiu Kong Family Sleep Assessment Unit, Department of Psychiatry, The Chinese University of Hong Kong, Hong Kong SAR, China. 5Department of Microbiology and Immunology, Stanford University, Stanford, CA, USA. 6Department of Pathology, School of Clinical Medicine, The University of Hong Kong, Queen Mary Hospital, Hong Kong SAR, China.[7] Department of Chemical Pathology, Faculty of Medicine, The Chinese University of Hong Kong, Hong Kong SAR, China.[8] These authors contributed equally: Chun Ngo Yau, Jacky Tin Shing Hung. e-mail: hmlai@cuhk.edu.hk 

Nature Communications | (2024) 15:10888 

1 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

suboptimal with most methods, where probes preferentially deposit near the tissue surface and complicates downstream quantitative protein expression determination[6][,][11] . The homogeneous penetration can only be attained either through complicated operations or equipment[11][–][13] , or extensive tissue permeabilization[14][,][15] or incubation times measuring in weeks[8] . These shortcomings hinder the wide adoption of 3D tissue analysis in research and renders them unsatisfactory for clinical translation. 

Here, we report the development of In situ Host-Guest Chemistry for Three-dimensional Histology (INSIHGT). INSIHGT is a userfriendly 3D histochemistry method, featuring (1) homogeneous probe penetration up to centimeter depths, (2) producing quantitative, highly specific immunostaining signals, (3) a fast and affordable workflow to accommodate different tissue sizes and shapes, (4) simple immersion-based staining at room temperature, thus easily adopted in any laboratory and ready for scaling and automate, and (5) uses off-the-shelf antibodies or probes and is directly applicable to otherwise unlabeled mouse and human tissues fixed with paraformaldehyde only. INSIHGT was developed based on the manipulation of macromoleular diffusiophoresis using closododecahydrododecaborate [B12H12][2-][16] and a γ-cyclodextrin derivative. If tissue clearing is required, INSIHGT works best with solventbased clearing methods[17][–][19] . 

## Results 

## Modulation of antibody-antigen binding for enhanced probe penetration 

The limited penetration of macromolecular probes in complex biological systems belongs to the broader subject of transport phenomena, where diffusion and advections respectively drive the dissipation and directional drift of mass, energy and momentum. When biomolecules such as proteins are involved, the (bio)molecular fluxes are additionally determined by binding reactions, which can significantly deplete biomolecules due to their high binding affinities and low concentrations employed - a “reaction barrier” to deep antibody penetration. This is first described and postulated by Renier et al.[17] (as in immunolabeling-enabled three-dimensional imaging of solventcleared organs, iDISCO) and Murray et al.[14] (as in system-wide control of interaction time and kinetics of chemicals, SWITCH), and the latter further showed that the modulation of antibody-antigen (Ab-Ag) binding affinity (SWITCH labeling) can lead to homogeneous penetration of up to 1 mm for an anti-Histone H3 antibody using low concentrations of sodium dodecyl sulfate (SDS). Other techniques similarly utilizes urea[8] , sodium deoxycholate[12] , and heat[9] to modulate antibody-antigen binding. 

However, others and we observed a general compromise between antibody labelling quality, penetration depth and uniformity, and duration of incubation. Deep penetration invariably requires long incubation times with inhomogeneous signal across depth, while faster methods leads to weak or nonspecific staining, as well as non-uniform penetration[8][,][9][,][17] . Specifically, the use of SDS for deep labelling with SWITCH labelling has only been demonstrated for a handful of antigens (e.g., Histone H3[14] , NeuN[20] , ColIV, αSMA, and TubIII[21] ). It was found that deep staining with SDS was not universally applicable[20] , - resulting in weak calbindin staining[22] , insufficient staining depth for β amyloid plaques[23] , and often required tailored refinement of buffer concentration[24] . In our validation data, we similarly observed the variable performance when SDS is co-applied with antibodies (Supplementary Fig. 1). Furthermore, although adding antibodies or probes theoretically improves penetration via steep concentration gradients, either the cost becomes prohibitive or it produces a biased representation of rimmed surface staining pattern[6][,][8] , especially for densely expressed binding targets. In the most extreme cases, the superficial staining signal would saturate microscope detectors while the core remains unstained (Supplementary Fig. 2). 

Nonetheless, the conception of modulating antibody-antigen binding kinetics as a means to control probe flux through tissues is highly attractive[12][,][14] , given the simplicity, scalability, and affordability should the method be robust and generalizable. We postulated that the reason for the highly variable performance of SDS-assisted deep immunostaining is two-fold: the denaturation of antibodies beyond reparability, and the ineffective reinstatement of binding reactions. This prompted us to search for alternative approaches that can tune biomolecular binding affinities while preserving both macromolecular probe mobility and stability. In addition, the negation of the modulatory effect should be efficient and robust to reinstate biomolecular reactions within the complex tissue environment. Therefore, here we aim to develop a fast, equipment-free, deep and uniform multiplexed immunostaining method, which will help bring 3D histology to any basic laboratories. 

## Boron cluster host–guest chemistry for in situ macromolecular probe mobility control 

Our initial attempts by using heat and the GroEL-GroES system to denature and refold antibodies in situ respectively have proved unsuccessful (Supplementary Fig. 1). We thus switched from the natural molecular chaperones to artificial ones using milder detergents (e.g., sodium deoxycholate (SDC) and 3-([3-Cholamidopropyl]dimethylammonio)- 2-hydroxy-1-propanesulfonate i.e., CHAPSO) and their charge-complementary, size-matched hostcomplexing agents (e.g., β-cyclodextrins and their derivatives such as heptakis-(6-amino-6-deoxy)-beta-cyclodextrin, i.e., 6NβCD), which improved antibody penetration and staining success rate (Supplementary Fig. 3). However, despite extensive optimization on the structure and derivatization on the detergents and their size- and charge-complementary cyclodextrins, they still have limited generality for a panel of antibodies tested (Supplementary Fig. 3), producing nonspecific vascular precipitates or nuclear stainings. We then explored the use of chaotropes, which are known to solubilize proteins with enhanced antibody penetration[8] . However, these approaches require long incubation times with extensive tissue preprocessing. Furthermore, higher concentrations of chaotropes often denature proteins as they directly interact with various protein residues and backbone[25][,][26] (Fig. 1a, b). 

We hence focus on testing weakly coordinating superchaotropes (WCS), a class of chemicals that we hypothesized to inhibit antibody-antigen interactions while preserving their structure and hence functions (Fig. 1a, b). We searched for weakly coordinating ions based on their utility in isolating extremely electrophilic species for X-ray crystallography, or as conjugate bases of superacids. We can then select a subset of these coordinatively inert ionic species that possess high chaotropicity as candidates for our deep immunostaining purpose. After antibodies and WCS have been homogeneously distributed throughout the tissue matrix, measures must be taken to negate the superchaotropicity to reinstate inter-biomolecular interactions in a bio-orthogonal and system-wide manner. To do so, we took advantage of the enthalpydriven chaotropic assembly reaction, where the activities of superchaotropes can be effectively negated with supramolecular hosts in situ, reactivating interactions between the macromolecular probes and their tissue targets. 

Based on the above analysis, we designed a scalable deep molecular phenotyping method, performed in two stages: a first infiltrative stage where macromolecular probes co-diffuse homogeneously with WCS with minimized reaction barriers, followed by the addition of macrocyclic compounds for in situ host-guest reactions to reinstate antibody-antigen binding. With a much-narrowed list of chemicals to screen, we first benchmarked the performances of several putative WCS host-guest systems using a standard protocol as previously 

Nature Communications | (2024) 15:10888 

2 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

published[6][,][8][,][9] (Supplementary Fig. 4). These include perrhenate/αcyclodextrin (ReO4−/αCD), ferrocenium/βCD ([Fe(C5H5)2]+/βCD), closododecaborate ions ([B12X12][2][−] /γCD (where X = H, Cl, Br, or I)), metallacarborane ([Co(7,8-C2B9H11)2][−] /γCD), and polyoxometalates ([PM12O40][3][−] /γCD (where M = Mo, or W)) (Fig. 1c, d). Group 5 and 6 halide clusters and rhenium chalcogenide clusters such as [Ta6Br12][2+] , [Mo6Cl14][2-] and {Re6Se8}[2+] derivatives were excluded due to instability in aqueous environments. Only ReO4-, [B12H12]2−, and [Co(7,8C2B9H11)2][−] proved compatible with immunostaining conditions without causing tissue destruction or precipitation. [B12H12][2][−] /γCD produced the best staining sensitivity, specificity and signal homogeneity across depth (Supplementary Fig. 5), while the effect of derivatizing γCD was negligible (Supplementary Fig. 5). Finally, we chose the more soluble 2-hydroxypropylated derivative (2HPγCD) for its higher water solubility in our applications. We term our method INSIHGT, for In situ host-guest chemistry for three-dimensional histology. 

## In situ host–guest chemistry for three-dimensional histology (INSIHGT) 

INSIHGT was designed to be a minimally perturbative, deeply and homogeneously penetrating staining method for 3D histology. Designed for affordability and scalability, INSIHGT involves simply incubating the conventional formaldehyde-fixed tissues in [B12H12][2-] / PBS with antibodies, then in 2HPγCD/PBS (Fig. 2a) - both at room temperature with no specialized equipment. We compared INSIHGT with other 3D IHC techniques using a stringent benchmarking experiment as previously published (see “Methods”, Supplementary Fig. 4) to compare their penetration depths and homogeneity[6][,][9] . Briefly, a mouse hemibrain was first stained in bulk for an antigen using various deep immunostaining methods (“bulk-staining”), followed by cutting the tissue coronally in the middle (thickest dimension) and restained for the same marker with a different fluorophore using a standardized control method (“cut-staining”), which serves as the 

**==> picture [476 x 423] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>native detergents ΔG < 0<br>E<br>Ab + Ag<br>[Ab-Ag]<br>H2Oprotein<br>H2Obulk<br>Reaction Coordinate<br>chaotropes weakly coordinating  ΔG ≥ 0<br>superchaotropes E<br>H2Obulk<br>Ab + Ag<br>[Ab-Ag]<br>H2Oprotein<br>Reaction Coordinate<br>c d<br>H P 3- d<br>B CD<br>Fe<br>CO Co -<br>Re W<br>2-<br>+<br>-<br>x n = dCD (Å) n<br>[ReO4] [-] [Fe(C5H5)2] [+] [B12H12] [2-]   (     ) [Co(7,8-C2B9H11)2] [-] [PW12O40] [3-] βα 12 14.615.4 x -Cyclodextrin (     )<br>di  = 5.2Å di  = 6.9Å di  = 8.0Å di  = 8.0Å di  = 13.1Å γ 3 17.5<br>**----- End of picture text -----**<br>


Fig. 1 | INSIHGT conceptualization and key components. a, b Reconceptualization of the biomolecular binding phenomena. a Microscopic view. Native antibody-antigen binding (left upper, in an aqueous medium) requires the desolvation of their solvation shells (∇μH2O < 0). Detergents (right upper) and chaotropes (left lower) solubilize proteins by masking binding sites (and displacing the solvent shell), but they may lead to protein denaturation in high concentrations (black arm of the antibody). Weakly coordinating superchaotropes (right lower, 

WCS, e.g., [B12H12][2-] ) instead solubilizes proteins by favoring solvent-protein interactions (∇μH2O ≥ 0), striking a balance between protein solubilization and stabilization. Created with Biorender.com. b Energetic view. Antibody-antigen binding without WCS (upper panel), occurs spontaneously with ΔGtot < 0, while with WCA (bottom panel), is unfavorable with ΔGtot ≥ 0. Created with Biorender.com. c Structures and ionic diameters (di) of weakly coordinating ions tested. d General structure of cyclodextrins and their cavity opening diameter (dCD). 

Nature Communications | (2024) 15:10888 

3 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [481 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>d<br>Parvalbumin<br>1<br>1 [st]  staining  2 [nd]  staining  r  = 0.512<br>solution solution<br>Tissue Stained tissue<br>γCD<br>Antibody +<br>antigensTissue  [B12H12] [2-] ↓ Ag-Ab interactions,↑ Ab penetration [B12↑ Ag-Ab interactionH12] [2-]     γCD formed,  Deep, homogeneous immunostaining pen. dist.(μm) INSIHGT  18040<br>b INSIHGT CUBIC-HV c 1.0 INSIHGTCUBIC-HV 0 0 cut-stain intensity (normalized) Segmented cell 1<br>iDISCO<br>SHANEL<br>c-Fos<br>1<br>r  = 0.752<br>500μm 0.5<br>iDISCO SHANEL<br>Ideal 1421<br>INSIHGT<br>pen. dist.(μm)<br>0<br>0<br>0 0 Segmented cell 1<br>0 500 1000 1500 cut-stain intensity (normalized)<br>Bulk-stain penetration distance (μm)<br>e INSIHGT 6h 1d 6h 4d 3h Fixation<br>1d 3d 7d Permeabilize<br>CUBIC-HVeFLASH 4d 1d 3d 1d 1d Deep immunostainingWashing<br>iDISCO* 6h 3.5d 3.5d 7d 1d 7d 1d Other steps<br>SHANEL* 1d 3d 7d 2d 7d 1d 7d 1d<br>SWITCH-pumping  of  4d 2d 7d 2d 4d 6h 2d 18h 1d 1d 12h 18h 3h<br>mELAST tissue-hydrogel 2d 2d 1d 1d 1d 6h 7d 2d 7d 1d<br>SWITCH<br>0 1 2 3 4 5 6 7 14 21 28 days<br>Time from tissue to image for a whole mouse brain<br>depth Segmented cell<br>U INSIGHT intensity (normalized)<br>staining Bulk-stain intensity Cut-stain intensity<br>PVALB<br>Cut-<br>then<br>Segmented cell  Segmented cell<br>Bulk-<br>INSIGHT intensity (normalized)<br>**----- End of picture text -----**<br>


Fig. 2 | Homogeneous and deep staining with INSIHGT. a Experimental steps and principle of INSIHGT for immunostaining. Top row: Tissue is infiltrated with antibodies and a weakly coordinating superchaotrope ([B12H12][2-] , purple dodecahedron) in the 1st staining solution and then transferred into the 2nd solution containing a complexation agent (CD, red ring). Bottom row: The molecular principles of INSIHGT. Weakly coordinating superchaotropes prevents antibodyantigen interactions, removing penetration obstacles. After homogeneous infiltration, subsequent γCD infiltration complexes the [B12H12][2-] ions, allowing deep tissue immunostaining. Reproduced with permission from Illumos Limited. b Benchmark results of four buffers used in deep immunostaining. Enlarged views of smaller areas are shown in insets. Parvalbumin (PVALB) immunostaining signals 

on cut surface: magenta, bulk-staining signal; green: cut-staining PVALB signal (refer to Supplementary Fig. 1). c Quantification of bulk:cut-staining signal ratio against penetration distance for segmented cells. Each dot represents a cell. Lines are single-term exponential decay regression curves. The signal decay distance constants (τ) are shown in Supplementary Table 1. Hypothetical ideal method performance is shown as a gray line (τ→0+). d Correlation of INSIHGT signal with reference (cut-staining intensity) signal, illustrating 3D quantitative immunostaining. r: Pearson correlation coefficient. e Timeline illustration for a whole mouse brain processing experiment with the different benchmarked methods (drawn to scale). *indicates methods where in principle the use of secondary antibody Fab fragments can lead to halved immunostaining times. 

reference signal without penetration limitations. The tissue was then imaged on the cut face to compare the bulk-staining intensity (deep staining method signal) and cut-staining intensity (reference signal) as a function of the bulk-staining penetration depth. We found that INSIHGT achieved the deepest immunolabeling penetration with the best signal homogeneity throughout the penetration depth (Fig. 2b). To quantitatively compare the signal, we segmented the labeled cells and compared the ratio between the deep immunolabelling signal and the reference signal against their penetration depths. Exponential decay curve fitting showed that the signal homogeneity was near-ideal (Fig. 2c, Supplementary Table 1)—where there was negligible decay in deep immunolabelling signals across the penetration depth. We repeated our benchmarking experiment with different markers, and by correlating INSIHGT signal with the reference signal, we found INSIHGT provides reliable relative quantification of cellular marker expression levels throughout an entire mouse hemi-brain stained for 1 day (Fig. 2d). We supplemented our comparison with the binding kinetics modulating buffers employed in eFLASH and SWITCH- 

pumping of mELAST tissue-hydrogel, as we lacked the specialized equipment to provide the external force fields and mechanical compressions, respectively (Supplementary Fig. 6). For SWITCH-pumping of mELAST tissue-hydrogel, we utilized the latest protocol and buffer recipe[13] . Our results also showed the use of binding kinetics modulating buffers alone from eFLASH and SWITCH-pumping of mELAST tissue-hydrogel lead to shallower staining penetration than INSIHGT, confirming the deep penetration of these methods is mainly contributed by the added external force fields and mechanical compressions, respectively. Hence, with excellent penetration homogeneity with a simple operating protocol, INSIHGT can be the ideal method for mapping whole organs with cellular resolution. It is also the fastest deep immunolabelling from tissue harvesting to image (Fig. 2e). Due to its compatibility with solvent-based delipidation methods, we recommend the use of solvent-based clearing[17][–][19] for an overall fastest INSIHGT protocol, although aqueous-based clearing techniques are also compatible (see “INSIHGT protocol in Supplementary Materials” for further discussions). However, protocols involving the use of 

Nature Communications | (2024) 15:10888 

4 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Triton X-100[8][,][15] and triethylamine[19] must be replaced with alternatives as they form precipitates with [B12H12][2][−] . 

Notably, after washing, only a negligible effect of [B12H12][2-] -treatment will remain within the tissue. This is evident as the cut-staining intensity profile of INSIHGT showed very steep exponential decay with increasing cut-staining penetration depth, and became similar to that of iDISCO (Supplementary Fig. 7) which has identical tissue preprocessing steps. Upon the addition of 2HPγCD and washing off the soformed complexes, the penetration enhancement effect was completely abolished. This suggests that [B12H12][2-] and cyclodextrins do not further permeabilize or disrupt the delipidated tissue. 

## High-throughput, multiplexed, dense whole organ mapping 

After confirming INSIHGT can achieve uniform, deeply penetrating immunostaining, we next applied INSIHGT to address the challenges in whole organ multiplexed immunostaining, where the limited penetration of macromolecular probes hinders the scale, speed, or choice of antigens that can be reliably mapped. Due to the operational simplicity, scaling up the sample size in organ mapping experiments with INSIHGT is straightforward and can be done using multiwell cell culture plates (Fig. 3a). For example, we demonstrated our case by mapping 14 mouse kidneys in parallel (Fig. 3b) within 6 days of tissue harvesting using a standard 24-well cell culture plate. 

We then exemplify the capability of INSIHGT to simultaneously map densely expressed targets in whole organs (Fig. 3c-i, Supplementary Fig. 8-9). We first performed multiplexed staining on mouse kidney with 3 days of incubation for Lycopersicon esculentum lectin (LEL), Peanut agglutinin (PNA), Griffonia simplicifolia lectin (GSL), and AQP-1, which are targets associated with poor probe penetration due to their binding targets’ dense expression (Fig. 3c-d, Supplementary Fig. 2, Supplementary Fig. 9a, b). With the use of INSIHGT, the dense tubules and vascular structures can be reliably visualized and traced (Supplementary Fig. 8). 

We then proceeded to map the whole brain of a 3-year-old mouse at the time of euthanasia. We utilized INSIHGT with 3 days of staining for Calbindin (CALB1), NeuN, and c-Fos, providing cell type and activity information across the aged organ (Fig. 3e-i, Supplementary Fig. 9c). With whole organ sampling, we identified regions where aging-related changes were prominent, these include cavitations in the bilateral thalamus and striatum (Fig. 3g, h), as well as calbindin-positive deposits in the stratum radiatum of hippocampus (Fig. 3i). Interestingly, there seems to be an increased c-Fos expression level among the neurons surrounding thalamic cavitations (Fig. 3g) which are located deep within the brain tissue and thus cannot be explained by preferential antibody penetration, suggesting these cavitations may affect baseline neuronal activities. Similar 1-step multiplexed mapping of calcium-binding proteins across a whole adult mouse brain can also be performed with 3 days of staining (with a fixed tissue-to-image time of 6 days) (Fig. 3j–l, Supplementary Movie 1). Similarly, whole adult mouse brain mapping and statistics can be obtained for ~35 million NeuN+ cells, their GABA quantities and c-Fos expression levels using the same protocol (Supplementary Fig. 10), allowing structure, neurotransmitter, and activity markers to be analyzed simultaneously. 

Overall, INSIHGT overcomes technical, operational, and cost bottlenecks towards accessible organ mapping for every basic molecular biology laboratory, providing rapid workflows to qualitatively evaluate organ-wide structural, molecular, and functional changes in health and disease, regardless of the spatial density of the visualization target. 

## Boron cluster-based supramolecular histochemistry as a foundation for spatial multi-omics 

With the maturation of single-cell omics technologies, integrating these high-dimensional datasets becomes problematic. Embedding 

these data in their native 3D spatial contexts is the most biologically informative approach. Hence, we next tested whether our boron cluster supramolecular chemistry allows the retention and detection of multiple classes of biomolecules and their features, based on which 3D spatial multi-omics technologies can be developed. 

With identical tissue processing steps and INSIHGT conditions, we tested 357 antibodies and found 323 of them (90.5%) produced the expected immunostaining patterns as manually validated with reference to the human protein atlas and/ or existing literature (Fig. 4a, Supplementary Figs. 11–15, Supplementary Table 2). This was at least six times the number of compatible antibodies demonstrated by any other deep immunostaining method (Fig. 4a), demonstrating the robustness and scalability of INSIHGT. Antigens ranging from small molecules (e.g., neurotransmitters), epigenetic modifications, peptides to proteins and their phosphorylated forms were detectable using INSIHGT (Fig. 4b, c). The specificity of immunostaining even allowed the degree of lysine methylations (i.e., mono-, di- and trimethylation) and the symmetricity of arginine dimethylations to be distinguished from one another (Fig. 4b). We further tested 21 lectins to detect complex glycosylations, proving that [B12H12][2][−] do not sequester divalent metal ions essential for their carbohydrate recognition (Fig. 4d, Supplementary Fig. 16). 

Small molecule dyes such as nucleic acid probes, which are mostly positively charged, present a separate challenge as they precipitate with closo-dodecaborates, forming [probe][n+] /[B12H12][2][−] precipitates when co-applied with INSIHGT. We found size-matched and chargecomplementing cyclodextrin derivatives as cost-effective supramolecular host agents for non-destructive deep tissue penetration and preventing precipitation. For example, sulfobutylether-βCD (SBEβCD) (Fig. 4e) can react with nucleic acid probes to form [probe⊂SBEβCD], which exhibits penetration enhancement during INSIHGT (Fig. 4f, g) without precipitation problems. The so-formed [probe⊂SBEβCD] complex can thus be co-incubated with antibodies in the presence of [B12H12][2][−] for a simpler protocol. 

We also performed RNA integrity number (RIN) and whole genome DNA extraction analyses on INSIHGT-treated samples (Supplementary Fig. 17). We found each step of the INSIHGT protocol did not result in a significant decrease in RNA integrity number (RIN) (Supplementary Fig. 17a). The total RNA extracted after undergoing the whole INSIHGT protocol has an RIN of 7.2, compared with a RIN of 9 from a treatment-naive control sample. For whole genome DNA, both control versus INSIHGT-protocoltreated samples have similar sample integrity and total DNA yield per mm[3] sample (14.6 μg versus 10.12 μg), as well as subsequent whole genome sequencing quality (total clean base 114.5 Gb versus 125.2 Gb) with both having a mapping rate of 99.96% (Supplementary Fig. 17b see also “Methods” on the quality control descriptions). With RNA sequencing whole transcriptomic comparing an INSIHGT-treated sample and a paired control sample (the opposite mouse hemibrain), the results showed essentially no differentially expressed genes profiles (Supplementary Fig. 17c). The Pearson correlation coefficient of the expression of all genes was 0.967. Hence, unsurprisingly, we found singlemolecule fluorescent in situ hybridization (FISH) is also applicable for co-detection of protein antigens and RNAs with INSIHGT. Combining all the above probes, simultaneous 3D visualization of protein antigens, RNA transcripts, protein glycosylations, epigenetic modifications, and nuclear DNA is possible using a mixed supramolecular system in conventionally formalin-fixed intact tissue (Fig. 4h, Table 1). Taken together, our results suggest in situ boron cluster supramolecular histochemistry can form the foundation for volumetric spatial multi-omics method development. The implication of well-preserved RNAs suggests the possibility of post-INSIHGT section-based spatial transcriptomics. 

Nature Communications | (2024) 15:10888 

5 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [9 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>c<br>**----- End of picture text -----**<br>


**==> picture [379 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
e CalbindinNeuN f g Calbindinc-Fos<br>c-Fos Thalamus<br>Anterior<br>200μm Lateral<br>h<br>Cortex<br>Striatum<br>200μm<br>i<br>Cortex<br>Hippocampus<br>Dentate<br>1.5mm 1.5mm gyrus<br>200μm<br>CALB1CALB2 Single slice 2000 μ m x-y projection<br>PVALB [l]<br>**----- End of picture text -----**<br>


## Centimeter-scale 3D histochemistry by isolated diffusional propagation 

Since antibody penetration remains the most challenging obstacle, we focus the remainder of our investigation on larger-scale 3D immunophenotyping. We thus applied INSIHGT to visualize centimeter-scale human brain samples, without using any external force fields to drive the penetration of macromolecular probes. 

These large, pigmented samples were sliced in the middle of the tissues’ smallest dimensions to allow imaging of the deepest areas with tiling confocal microscopy. We show that INSIHGT can process a 1.5 cm × 1.5 cm × 3 cm human cortex block for parvalbumin (PV) (Fig. 5a–c), with excellent homogeneity and demonstration of parvalbumin neurons predominantly in layer 4 of the human cortex. 

Nature Communications | (2024) 15:10888 

6 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Fig. 3 | High-throughput whole-organ deep immunostaining with dense mapping using INSIHGT. a Parallelized sample processing with INSIHGT, exemplified with whole mouse kidneys. b Whole organ imaging results with parallelized INSIHGT for the samples shown in (a), showing vimentin INSIHGT signals colorcoded by z-depth. One sample was dropped due to manual errors. c,d Whole mouse kidney densely multiplexed visualization with Lycopersicon esculentum lectin (red), Peanut agglutinin (gray), Griffonia simplicifolia lectin I (blue), and AQP1 (green). d Enlarged 2D view of the white boxed area in (c). e, f Rendered view of whole mouse brain multiplexed Calbindin, NeuN, and c-Fos mapping of a 3-year-old 

We then scaled INSIHGT to a 1.75 cm × 2.0 cm × 2.2 cm human cerebellum block for blood vessels (using Griffonia simplicifolia lectin I, GSL-I) (Fig. 5d–f). As light-sheet microscopy is suboptimal due to the large human sample, we assessed the INSIHGT staining penetration on the cut face along the thickest dimension using confocal microscopy (Fig. 5e, Supplementary Fig. 18). This again reveals excellent homogeneity with no decay of signal across the centimeter of penetration depth. This shows that the use of boron cluster-based host-guest chemistry remains applicable for highly complex environments at the centimeter scale. The results further show that macromolecular transport within a dense biological matrix can remain unrestricted in a non-denaturing manner by globally adjusting inter-biomolecular interactions. 

We further applied INSIHGT to a 1.0 cm × 1.4 cm × 1.4 cm human brainstem with dementia with Lewy bodies (DLB) for phosphorylated alpha-synuclein at serine 129 (αSyn-pS129) (Fig. 5g-i, Supplementary Fig. 19). The large scale of imaging enabled registration and hence correlation with mesoscale imaging modalities such as magnetic resonance imaging (MRI) (Fig. 5g, Supplementary Movie 2). With this, we confirmed the localization of Lewy body pathologies to the locus ceruleus complex–subcerulean nuclei[27] and substantia nigra, in keeping with the prominent rapid eye movement sleep behavior disorder (RBD) symptoms of this patient. Such a radio-histopathology approach would allow for correlative structural-molecular studies for neurodegenerative diseases. Overall, the capability of INSIHGT in achieving centimeter-sized tissue staining bridges the microscopic and mesoscopic imaging modalities, providing a general approach to correlative magnetic resonance-molecular imaging. 

## Volumetric spatial morpho-proteomic cartography for cell type identification and neuropeptide proximity analysis 

We next extended along the molecular dimension on conventionally fixed tissues, where highly multiplexed immunostaining-based molecular profiling in 3D had not been accomplished previously. A single round of INSIHGT-based indirect immunofluorescence plus lectin histochemistry can simultaneously map up to 6 antigens (Supplementary Fig. 20), tolerating a total protein concentration at >0.5 μg/μl in the staining buffer, and is limited only by spectral overlap and species compatibility. To achieve higher multiplexing, antibodies can be stripped off with 0.1 M sodium sulfite in the [B12H12][2-] -containing buffer after overnight incubation at 37 °C (Fig. 6a, Supplementary Fig. 21). Since [B12H12][2][−] does not significantly disrupt intramolecular and intermolecular noncovalent protein interactions, the approach can be directly applied to routine formaldehyde-fixed tissues, we observed no tissue damage and little distortion, obviating the need for additional or specialist fixation methods. 

We exemplified this approach by mapping 28 marker expression levels in a 2 mm-thick mouse hypothalamus slice over 7 imaging rounds (Fig. 6a–c, Supplementary Figs. 22, 23). With each iterative round taking 48 h (including imaging, retrieval and elution), the whole manual process from tissue preparation to the 28-plex image took 16 days. After registration and segmentation using Cellpose 2.0[28] (Fig. 6d, e, see “Methods”), we obtained 192,075 cells and their differentially expressed proteins (DEPs) based on immunostaining signals. Note that other user-friendly approaches such as StarDist[29] and 

mouse. g–i Age-related structural and molecular changes in the thalamus (g) and striatum (h) with cavitations (indicated by yellow arrowheads), and the hippocampus (i) with CALB1-positive deposits (indicated by yellow arrows). j Whole brain multiplexed staining of the calcium-binding proteins calbindin (CALB1), calretinin (CALB2), and parvalbumin (PVALB) with 3 days of INSIHGT staining. k Zoomed in 3D rendering view on the hippocampus (Hp), reticular nucleus of thalamus (Ret. Nuc.), and amygdala (Amyg.). l A single coronal slice view (left) and a 2 mm-thick anteroposterior projection (right) of the same sample. 

BCFind[30] can also be used. Omitting 3 blood vessel channels, we then obtained the normalized mean intensities of the remaining 25 markers, their standard deviations (S.D.s) of signal intensities of the same 25 markers, as well as their distance to the nearest vessels for dimensionality reduction analysis and clustering. The S.D.s of signal intensities for each cell served as a measure of heterogeneous expression of a certain marker within the cell (e.g., strictly cytoplasmic or nuclear expression will have a higher S.D. than a marker expressing in both the cytoplasms and nuclei, as illustrated in Fig. 6e). Uniform manifold approximation and projection (UMAP) analysis of a subset of 84,139 cells based on these 51 markers (Fig. 6f, Supplementary Figs. 24, 25) plus their distance to the nearest vessels revealed 42 cell type clusters, allowing their 3D spatial interrelationships to be determined (Supplementary Fig. 26). 

INSIHGT allows both 3D morphology and molecular information to be well-visualized via immunostaining, which is more difficult to access via current section-based spatial transcriptomics or single-cell multi-omics despite ongoing efforts[31] . Recent characterizations of neuronal network activities based on the diffusional spread of neuropeptides highlight the need for 3D spatial mapping of protein antigens. To obtain these morphological-molecular relationships using INSIHGT, we segmented the neuropeptide Y (NPY)-positive fibers and computed the 3D distance to each UMAP-clustered cell types’ somatic membrane (Fig. 6g–j). While most clusters have a similar distance from NPY fibers, certain clustered cells (notably right tile clusters1 and 2) are more proximally associated with NPY fibers, suggesting these cell clusters aredifferentially modulated by NPY when isotropicdiffusion is assumed in the local brain parenchyma. Nonetheless, our dataset and analysis demonstrated it is possible to estimate the likely modulatory influence for a given cell-neuropeptide pair, providing an alternative approach to discovering neuronal dynamics paradigms. 

## Fine-scale 3D imaging reveals unsuspected intercellular contacts traversing the Bowman space in mouse kidneys 

We found that the process of INSIHGT from fixation to completion preserves delicate structures such as free-hanging filaments and podia, enabling fine-scale analysis of compact structures such as the renal glomeruli. We found unsuspected intercellular contacts traversing the Bowman space, which was not known to be present in normal glomeruli even with serial sectioning electron microscopy studies[32][–][36] (Fig. 7a, b). These filaments are mostly originated from the podocytic surface, although some were also seen to emerge from PECs. They were numerous and found around the glomerular globe (Fig. 7c), with varied in their length, distance from each other, and morphologies (Fig. 7d, Supplementary Fig. 27). 

We classified these podocyte-to-PEC microfilaments into “reachers” and “stayers”, depending on whether they reached the PEC surface or not (Fig. 7e). Microfilaments of the reachers-type were more numerous than the stayers-type per glomerulus (Fig. 7f). Visually, we noted the emergence of these filaments tended to cluster together, especially for the reachers-type. To quantify such spatial clustering, we calculated the glomerular surface geodesic distances between the podocytic attachment points for each microfilament, which showed an inverse relationship with their path lengths (Fig. 7g), and reachers-type filament are geodesically located 

Nature Communications | (2024) 15:10888 

7 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [481 x 487] intentionally omitted <==**

**----- Start of picture text -----**<br>
a 300 323 c Mouse brain neurotransmitters INSIHGT e g 0 Nuclei Intensity (a.u.)<br>GABA Cortex R =  or    H<br>200<br>100<br>44 26 33 17 36 7<br>0 Cationic probe<br>Sulfobutylether-βCD DAPI<br>50μm 10μm f 120 DAPI SBE-βCD<br>bH2A.V DAPIMouse testis epigenetics INSIHGTH2A.Z H2AX L-Glutamate Cortex [NcAP] [n] [+] (aq) fast +[B , K 12 eq H ≫12] 0 [2-] [NcAP]2[B12H12] n  (s)<br>+ SBE-βCD [-]<br>+ [B12H12] [2-]<br>10μm (spontaneous)<br>macro-H2A.1 H2AX-S139p H3.3 [NcAP]4[SBEβCD] n (s) slow, Keq  ≫ 0 [NcAP ⸦ SBEβCD] [(4-] [n] [)] [-] (aq)<br>h<br>DAPI SBE-βCD [Glc N Ac]1-3<br>Serotonin Pons<br>H3K9ac H3T11p H3K27ac<br>50μm<br>H3K27me1 H3K27me2 H3K27me3 H3K27 acetylation car8  mRNA<br>Histamine Hypothalamus<br>H3R8me1 H3R8me2 [asym] H3R8me2 [sym]<br>CNP1 Merged<br>d Mouse kidney structures INSIHGT<br>GSL-I-BODIPY TMR WGA-AF488 PO-PRO1 S BEβCD<br>L-Noradrenaline LC<br>10μm<br>PHA-E-AF647 Rb-Vim-Atto490LS Ms-αSMA-AF594 DAPI SBE-βCD<br>H3K27 acetylation[Glc N Ac]1-3<br>car8  mRNA<br>CNP1<br>2D 3D Dopamine Hypothalamus<br>10μm 10μm<br>INSIHGTCUBIC-HVeFLASHiDISCOSWITCH-ELASTSHANEL<br>No. of validated Ab<br>Penetration depth (μm)<br>∩<br>4- 0, K  ≫ eq 2-H]1212<br>+[SBEβCD] fast +[B<br>U<br>∩<br>U<br>**----- End of picture text -----**<br>


Fig. 4 | Multi-modality INSIHGT for generality. a Number of validated antibodies f Thermodynamic scheme of NAP’s complexation reaction with SBEβCD. SBEβCD compatible with each benchmarked method. b–d INSIHGT’s compatibility in neither redissolves DAPI/[B12H12][2-] precipitates nor precipitates DAPI out from the revealing the 3D location of various features. b Epigenetic markers based on his[DAPI⊂SBEβCD] complex, suggesting kinetic stabilization. g Quantification of tone post-translational modifications and isoforms. c Neurotransmitters. LC: locus penetration depths of [DAPI⊂SBEβCD] compared to traditional DAPI staining. ceruleus. d Structural features, using one-step multiplexed supramolecular hish Multimodal 3D molecular phenotyping in a 1 mm-thick mouse cerebellum slice tochemistry, multiplexed supramolecular lectin histochemistry, and the suprafor proteins (CNP1), nucleic acids (car8, DAPI), epigenetic modifications (H3K27 molecular dye complex [PO-PRO1⊂SBEβCD]. e Nucleic acid probe (NAP, DAPI acetylation), and glycosylations ([GlcNAc]1-3) with INSIHGT. Imaging was limited to structure shown) complexation by SBEβCD for improved tissue penetration. 200 μm due to working distance constraints. 

## Table 1 | Sequences of FISH HCR probes applied 

car8 (with B3 Hairpin initiator) 

GTCCCTGCCTCTATATCTCCACTCAACTTTAACCCG TACAA GCTTCTCTGGAGTTTAGGTTGATAGG TAAAA AAAGTCTAATCCGTCCCTGCCTCTATATCTCCACTC GTCCCTGCCTCTATATCTCCACTCAACTTTAACCCG TACAA CTTCATACAGCTCAAACTCCTGTCC TAAAA AAAGTCTAATCCGTCCCTGCCTCTATATCTCCACTC GTCCCTGCCTCTATATCTCCACTCAACTTTAACCCG TACAA GCTTTGAAATTGACCGTGTGCTCAGA TAAAA AAAGTCTAATCCGTCCCTGCCTCTATATCTCCACTC 

Nature Communications | (2024) 15:10888 

8 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [481 x 467] intentionally omitted <==**

**----- Start of picture text -----**<br>
a g T2 MRI<br>b G. simplicifolia DAPI   SBE lectin IβCD c<br>PVALB<br>6390<br>0 xy Penetration distance (μm) 2cm<br>h αSyn-pS129<br>1cm<br>SN<br>Z-depth ~15mm 1mm 200μm SC RN<br>INS A (7d) INS B (1d)<br>d e IC<br>9520<br>LC<br>z-depth<br>(μm)<br>7755 1.75 cm-thick 5mm 0<br>xy Penetration<br>0 distance (μm) i<br>f<br>200<br>Z-depth ~8.75mm<br>G. simplicifolia NF-H  lectin I 1mm 500μm 20μm<br>0<br>∩<br>z-depth (μm)<br>**----- End of picture text -----**<br>


Fig. 5 | Centimeter-scale INSIHGT. a A human cortex block (1.5 cm × 1.5 cm × 3 cm), processed with INSIHGT and cut in the middle for confocal imaging to confirm penetration depth. b Confocal tiled image of the cut face from (a), stained with [DAPI⊂SBEβCD], G. simplicifolia lectin I (GSL-I), and for parvalbumin (PVALB). Inset: penetration depth over the imaging surface. c Enlarged view of the yellow boxed area in (b). d A human cerebellum tissue block (1.75 cm × 2.0 cm × 2.3 cm) processed with INSIHGT, stained with GSL-I lectin and NF-H. Inset: penetration depth over the imaging surface. e Illustrated tissue processing steps: tissue is stained for 7 days in INSIHGT buffer A (with [B12H12][2][−] ), washed in INSIHGT buffer B (with 

2HPγCD), and sliced perpendicular to the thinnest dimension at the midpoint. f Enlarged view of the yellow boxed area in (d). g T2-weighted magnetic resonance imaging (MRI) of a patient’s brain with dementia with Lewy bodies (DLB). A hemibrainstem region spanning the pons to substantia nigra was stained for phosphorylated α-synuclein at serine 129 (αSyn-pS129). h αSyn-pS129 staining intensity color-coded in z-depth. Inset shows the specimen photograph. LC: locus ceruleus complex, IC inferior colliculus, RN red nucleus, SC superior colliculus, SN substantia nigra. i Zoomed-in view of the yellow boxed area showing Lewy neurites (arrow) and Lewy bodies (triangle). 

nearer to each other than the stayers type (Supplementary Fig. 28). This suggests that the emergence of long, projecting microfilaments that reach across the Bowman space is localized on a few hotspots of the glomerular surface. Whether these hotspots of long-reaching microfilaments are driven by signals originated from the podocyte, the glomerular environment underneath, or the nearest PECs across the Bowmann space remains to be investigated and may reveal previously unsuspected podocyte physiological responses within their microenvironments. Notably, similar structures have been observed in the pathological state of cresenteric 

glomerulonephritis, in conjunction with whole cells traversing the Bowman space. As cresenteric glmoerulonephiritis is a final common pathway of glomerulonephropathies, it would be interesting to investigate whether there is a continuum of progressive changes from microfilaments physiologically to larger trans-Bowman space connections pathologically. In addition, morphologically similar structures have been observed in the microglia[37] , pericytes[38] , between tumor and immune cells[39] , and between normal and apoptotic cells in cell culture[40] . The podocyte-PEC connections described here thus add another organ to the growing list of 

Nature Communications | (2024) 15:10888 

9 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [397 x 599] intentionally omitted <==**

**----- Start of picture text -----**<br>
a BABB clearing 28-plex image d<br>½ day Segmented<br>Delipidation Multiplexed IHC by INSIHGT 7 Rounds Imaging registrationNon-rigid  Summed image vessel mask<br>1 day 1 day (21 days) 1 day<br>Elution<br>½ day<br>b HTR3AVIP Cell masks by  25-plex image<br>CALB2 Cellpose (omitted vessels)<br>NPY<br>CALB1<br>Orexin A<br>GFAP<br>NRF2-pS40<br>Tomato lectin<br>Cluster by:<br>1. Intensity Mean<br>2. Intensity S.D.<br>3. Distance from Vessel<br>e<br>Original Image Segmented cells<br>255 75<br>100μm 0 1<br>Intensity Mean Intensity S.D.<br>c<br>1 1<br>0 0<br>Distance Transform Distance fr. Vessel<br>40 1<br>50μm 0 0<br>f Left tile UMAP Right tile UMAP Spatial re-embedded UMAP clusters UMAP clustered masks with morphology<br>1st UMAP 1st UMAP<br>g h<br>Neurons<br>Varicosities<br>626<br>10μm<br>100μm 0<br>2<br>i NPY NPYGFAP j<br>CALB1<br>NRF-pS40<br>VIPCALB2 0 Left tile clusters 1-17 non-clustered cells<br>2<br>20μm 0<br>Right tile clusters 1-21<br>Intensity Cell ID<br>Norm. Value Norm. Value<br>Distance fr.  Vessel (μm) Norm. Value<br>Distance from<br>z-depth  (μm)<br>**----- End of picture text -----**<br>


nanostructural connections mediating information and matter exchange between different cell types in their physiological states. 

## Sparsely distributed neurofilament inclusions unique to the human cerebellum 

We next completely mapped a 3 mm-thick (post-dehydration dimensions) human cerebellar folium for NF-H, GFAP, and blood vessels 

(Fig 8a, Supplementary Figs. 29, 30, Supplementary Movie 3), with preserved details down to the Bergmann glia fibers, perivascular astrocytic endfeet, and Purkinje cell axons that make the amenable to 3D orientation analysis and visualization (Fig. 8b-d, Supplementary Figs. 29, 30). The detailed visualization of filamentous structures throughout the 3 mm-thickness is in stark contrast to our previous attempts with similar specimens employing various methods, which 

Nature Communications | (2024) 15:10888 

10 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Fig. 6 | Multi-round multiplexed INSIHGT. a Schematics of the processing steps for a 1mm-thick mouse hypothalamus sample. b A selection of multi-round immunostaining signals (for nine targets) displayed for the multi-round multiplexed INSIHGT-processed sample. c Enlarged view of the yellow boxed area in (b) with a complementary panel of markers. d Schematics of the image analysis process. e Illustrated results of a segmented image subset. The images below show corresponding cell segmentation and quantification results. f Left panel: Nested UMAP embedding of all segmented cells from both tiles of the image stack. Middle panel: The spatial locations of the different color-coded clusters. Right panel: 

showed weak NF-H signal in cerebellar sulci and barely visible GFAP signal in cerebellar white matter due to poor antibody penetration. 

We discovered sparsely distributed NF-H-intense inclusions that are easily missed in 2D sectioning and thus remain poorly characterized. We manually traced and identified 1078 inclusions throughout the entire imaged volume (Fig. 8e, f), where they were found in all of the three basic layers of the cerebellar cortex. A typical morphology of one type of these inclusion is a single bright globular inclusion at the sub-Purkinje layer radial location, with an elongated thick fiber extension that coils back and project to the adjacent molecular layer (Fig. 8e). However, much more protean morphologies also exist (Fig. 8e, f, Supplementary Fig. 30). To capture the morphological and spatial diversities of these inclusions, we obtained their spatialmorphometric statistics (Supplementary Fig. 31a), followed by principal component analysis of the compiled morphometrics such as Sholl analysis and Horton-Strahler number. The results reveal most of these inclusions to be morphologically homogeneous with variations explained largely by their path lengths, with a small subset characterized by much higher branching of the NF-H-intense filaments (Supplementary Fig. 31b). However, further understanding of these inclusions awaits broader investigations in normal and various disease states other than in DLB. Preliminarily, we have also observed these inclusions in normal human cerebellum tissues (Supplementary Fig. 31c). With the advancements in technologies, correlated mulitpronged approaches using superresolution microscopy, electron microscopy and spatially resolved proteomics are expected to help greatly clarify the pathobiology of these inclusions. 

## INSIHGT bridges the gap between 3D histology and traditional 2D pathology in current clinical practice 

The bio-orthogonal nature of the INSIHGT chemical system underlies its non-destructiveness. To highlight the clinical impact of INSIHGT in addition to 3D imaging of human samples, we found that INSIHGTprocessed samples can be retrieved and processed as naïve tissues for traditional 2D histology via paraffin wax embedding and sectioning. Notably, staining qualities of routine hematoxylin and eosin (H&E) and various special stains on the post-INSIHGT processed slides were indistinguishable from the pre-INSIHGT processed slides even by a senior pathologist (Fig. 8g, h). In addition to not interfering with downstream clinical processes, the preserved quality of special staining allows for multi-modal cross-validation of 3D fluorescent imaging findings, making INSIHGT the ideal platform choice for nextgeneration histopathology (Fig. 8i). Together with the possibility for post-INSIHGT DNA and RNA sequencing, we envision (Supplementary Fig. 17) quantitative 3D information within clinical specimens can be maximally extracted and preserved with high authenticity in a nonconsumptive manner using INSIHGT, and its fast speed promises compatibility with current clinical workflows and constraints, allowing digital pathology and precision medicine to benefit from 3D analysis. 

## Discussion 

The convergence of multiple technological advances has paved the way for the acquisition of large-scale molecular phenotyping datasets at single-cell resolution, most notably single-cell transcriptomics[36] . With a large number of previously undiscovered cell states, the quest 

Similar to the middle panel but with cellular morphology. g Color-coded z-projection of neuropeptide Y (NPY) staining signals. A higher magnification view for the left white boxed area is shown in the inset. h Schematic representation of distance measurement from NPY fibers to cell bodies via distance transformation. Created with Biorender.com. i NPY signal in a periventricular region (right white boxed area in g) is shown in the left panel, and with selected markers staining in the right panel. j Quantification of distance from NPY-expressing fibers for each cell type shown in violin plots, based on the 3D spatial locations of somas and NPY fibers. 

to extend towards spatially resolved cell phenotyping based on translated and post-translationally expressed biomolecular signatures is paramount to understanding their structural and functional properties in biology[41] . 

Scalable, high-resolution 3D tissue mapping provides a powerful approach to further our understanding of these previously unidentified cell types. Clinically, 3D histology has been shown to improve diagnosis in bladder cancer[42] , predict biochemical recurrence in prostate cancer[43] , and evaluate response to chemotherapy in ovarian carcinoma[42] , By sampling across whole intact samples, 3D histology can deliver unbiased, quantitative, ground-truth data on the spatial distributions of molecules and cell types in their native tissue contexts[44] . However, 3D tissue imaging is yet to be widely adopted despite the increasing accessibility of tissue clearing, optical sectioning microscopy, and coding-free image processing software. This is in large part due to the limited penetration of probes that plague the field regardless of the combinations of these technologies employed[6][,][10] , yielding variable, surface-biased data with questionable representativeness. Creative approaches have provided solutions to the penetration problem but are limited in their scalability and accessibility[6] . 

Constrained by the requirements of non-advective approaches and compatibility with off-the-shelf reagents, the development of INSIHGT involved re-examining biomolecular transport and protein stability from the first principles, which led us to identify weakly coordinating superchaotrope and its chemical activity modulation by in situ host–guest reactions to implement our theoretical formulation. With the use of closo-dodecaborate and cyclodextrin as an additive in PBS, we solved the bottleneck of 3D histology by providing a costefficient, scalable, and affordable approach to quantitatively map multiple molecules in centimeter-sized tissues. With an equivalent tissue processing pipeline to iDISCO[17] , INSIHGT shares the same affordability and scalability while providing much faster processing and greatly improved image quality, due to enhanced antibody penetration depth and homogeneity. Mapping tissue blocks simultaneously in multi-well dishes is easily accomplished in any basic molecular biology laboratory. Such simplicity in operation makes it highly accessible and automatable, as it requires no specialized equipment or skills. Furthermore, cocktails of off-the-shelf antibodies can be directly added to PBS supplemented with [B12H12][2][−] . Finally, we note that both [B12H12][2][−] salts and cyclodextrins are non-hazardous and stable indefinitely at ambient temperatures[16] . 

With the affordability and accessibility of INSIHGT, we anticipate its diverse applications in 2D and 3D histology applications. Meanwhile, boron cluster-based supramolecular histochemistry can form the backbone for 3D spatial molecular-structural-functional profiling methods and studies, as well as atlas mapping efforts. The high-depth, quantitative readout of well-preserved tissue biomolecules offered by INSIHGT forms the foundation for multiplexed, multi-modal, and multi-scale 3D spatial biology. By making non-destructive 3D tissue molecular probing accessible, INSIHGT can empower researchers to bridge molecular-structural inferences from subcellular to the organwide level, even up to clinical radiological imaging scales for radiohistopathological correlations. Finally, the compatibility of INSIHGT with downstream traditional 2D histology methods indicates its noninterference with subsequent clinical decision-making. This paves the 

Nature Communications | (2024) 15:10888 

11 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [234 x 40] intentionally omitted <==**

**----- Start of picture text -----**<br>
a DAPI SBE-βCD b c<br>WGA<br>PHA-E<br>GSL-I<br>U<br>**----- End of picture text -----**<br>


**==> picture [417 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
e f g 30 colors:<br>150 25 glomeruli IDs<br>20<br>100<br>15<br>“Reachers” 50 10<br>0 5<br>Podocyte surface “Stayers” PEC surface 0 0 10 20 30 40<br>Path length (μm)<br>“Stayers”“Reachers”<br>per glomerulus<br>Geodesic dist. from<br> nearest neighbor (μm)<br>**----- End of picture text -----**<br>


Fig. 7 | INSIHGT reveals previously undescribed intercellular filaments traversing the Bowman space in mouse kidneys. a Original image of multiplexed image of whole mouse glomerulus with full Bowman capsule. WGA Wheat germ agglutinin, PHA-E Phaseolus vulgaris hemagglutinin, GSL-I Griffonia simplicifolia lectin I. b Segmentation of microfilaments with en bloc preservation of native morphologies and spatial relationships in 3D Euclidean space. c Global representation of the 3D spatial distribution of microfilaments across the entire Bowman space. d Distinct and protean morphologies of the podocyte-to-parietal epithelial cell (PEC) microfilaments. e Schematic representation of reachers (contacting PEC 

surface) and stayers (remaining in the Bowman space) originating from podocyte surfaces with the related physical parameters. f Descriptive statistics of microfilament subtypes per analyzed glomeruli. N = 14 glomeruli analyzed across four mice (where three mice has four glomeruli imaged, one mouse has two glomeruli imaged, and the results were plotted together). g Correlation between the path length of each microfilament and the geodesic distance between its podocytic attachment point and its nearest neighbor. The data points were color-coded based on their glomerulus of origin in the dataset. Source data are provided as a Source Data file. 

way for the translation and development of 3D histology-based tissue diagnostics, promising rapid and accurate generation of groundtruth data across entire tissue specimens. 

We recognize that INSIHGT still has room for further improvements. Immunostaining penetration homogeneities for larger tissues and denser antigens can be further enhanced, Practically, this is limited to a maximum of ~2 cm[3] sized tissues, and extremely dense antigens such as GAPDH, type I collagen, actin, and myosin remain difficult for whole organ staining with homogeneous penetration. Nonetheless, for 

any antigens stained using the iDISCO+ protocol[45] with 7 days of primary antibody staining, INSIHGT with 3 days of antibody staining will at least provide 10–20× penetration enhancement, along with a noticeable enhancement in penetration homogeneity. Penetration can be further enhanced by prolonging the incubation times and ensuring an adequate amount probes has been added relative to the tissue expression level (see “Supplementary Note and INSIHGT protocol therein”). If available, the use of primary nanobodies with fluorescently-labeled secondary whole IgGs will further increase the penetration by about 5–10 times. In 

Nature Communications | (2024) 15:10888 

12 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

**==> picture [209 x 47] intentionally omitted <==**

**----- Start of picture text -----**<br>
z NF-H<br>x GFAP<br>1000μm Lectin<br>d e<br>**----- End of picture text -----**<br>


**==> picture [465 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
g Pre-INSIHGT H&E Post-INSIHGT H&E h Periodic Acid- Masson’s<br>Alcian Blue Trichrome<br>50μm<br>100μm<br>i Next-Generation 3D Histopathology Pathway<br>INSIHGT- Light-sheet  Cut & trim for  Confocal  Retrieve for FFPE Traditional Histology<br>processed tissue microscopy selected region microscopy + Sequencing<br>Pre-INSIHGT<br>Post-INSIHGT<br>**----- End of picture text -----**<br>


addition, the penetration homogeneity of small molecule dyes and lectins were still suboptimal for millimeter-scale tissues and remains to be further enhanced. In multi-round immunostaining, we noticed that the staining specificity and sensitivity deteriorated with each round of antibody elution with sulfite or β-mercaptoethanol, calling for a better 3D immunostaining elution method. Alternatively, hyperspectral imaging[46] , nonlinear optics[47] , time-resolved fluorescence techniques[48] , 

and same-species antibody multiplexing[49] could be explored to extend the multiplexing capabilities of INSIHGT. Finally, although theoretically applicable, we have yet to apply the INSIHGT-based multi-round staining in tissues from other species. 

Our discovery of boron clusters’ capabilities to solubilize proteins globally in a titratable manner, combined with their bio-orthogonal removal with supramolecular click chemistry, can reach beyond 

Nature Communications | (2024) 15:10888 

13 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Fig. 8 | INSIHGT enables non-destructive characterization and analysis of human clinical samples. a A 3.5mm-thick human cerebellum triplex-stained for glial filaments (GFAP), neurofilament (NF-H) and blood vessels (G. simplicifolia lectin I). Orientation and coherence (or fractional anisotropy) visualization of neurofilament (b, NF-H) and glial filament (c, GFAP) via structure tensor analysis. d Enlarged view of the boxed area in a via post-hoc confocal microscopy. e Prototypical morphology of human cerebellar neurofilament inclusions, where their extensions may loop back to the Purkinje layer and occasionally to another inclusion body (lowest image). f Overview of the 1078 manually traced 

histology applications. Given the surprisingly robust performance of INSIHGT in complex tissue environments, we envision they can be applied in simpler in vitro settings to control intermolecular interactions —particularly when involving proteins—in a spatiotemporally precise manner. 

## Methods 

## Ethical statement 

For animal tissues, all experimental procedures were approved by the Animal Research Ethics Committee of the Chinese University of Hong Kong (CUHK) and were performed in accordance with the Guide for the Care and Use of Laboratory Animals (AEEC number 20-287-MIS). The housing of animals was provided by the Laboratory Animal Service Center of CUHK. For human tissues donated post-mortem, prior ethics approvals have been obtained and approved by the Joint Chinese University of Hong Kong-New Territories East Cluster Clinical Research Ethics Committee (approval number 2022.137), with consent obtained from the donor and his family. 

## Chemicals and reagents 

The antibodies utilized in this study were listed in Supplementary Table 2. All protein-conjugating fluorophores tested and their compatibility with INSIHGT were listed in Supplementary Table 3. Secondary Fab fragments or nanobodies were acquired from Jackson ImmunoResearch or Synaptic Systems, and all lectins were sourced from VectorLabs. Conjugation of secondary antibodies and lectins with fluorophores was achieved through N-hydroxysuccinimidyl (NHS) chemistry. The process was conducted at room temperature for a duration exceeding 16 h at antibody concentrations >3 mg/ml, using a tenfold molar excess of the reactive dye-NHS ester. Dodecahydrocloso-dodecaborate salts and other boron cluster compounds were procured from Katchem, while cyclodextrin derivatives were obtained from Cyclolab, Cyclodextrin Shop, or Sigma Aldrich. 

We noticed occasionally the chemicals involved in the INSIHGT process require purification. Specifically, for Na2[B12H12], if insoluble flakes were noticed after dissolution in PBS, the solution was then acidified to pH 1 with concentrated hydrochloric acid, extracted with diethyl ether (Sigma Aldrich), and the organic solvent was removed and distilled off with a warm water bath. The residual H2B12H12 was then dissolved in minimal amount of water, and neutralized with 1 M Na2CO3 solution until pH 7 is reached with no further evanescence. The solution was then concentrated by distillation under vacuum and dried in an oven. 

For 2-hydroxypropyl-γ-cyclodextrin and sulfobutylether-β-cyclodextrin, if insoluble specks or dusts were noticed after dissolution in PBS, the solution was vacuum filtered through 0.22μm hydrophilic cellulose membrane filters (GSWP14250) using a Buchner funnel before use. A slight brownish-yellow discoloration of the resulting solution would not interfere with the INSIHGT results. 

For benzyl benzoate, if the solution is yellowish (possibly due to the impurities of fluorenone present), the solvent is poured into a metal bowl or glass crystallization dish and refrigerated to 4[०] C until crystallization begins. If no crystallization occurs, a small crystal seed of benzyl benzoate obtained by freezing the solvent at −20[०] C in a microcentrifuge tube can be put into the cooled solvent to kick-start 

neurofilament inclusions across the cerebellar sample, color-coded by z-depth. Traditional 2D histology with special stains on pre-INSIHGT and post-INSIHGT processed samples. g H&E staining of human brain, h Left to right: Periodic acidSchiff (PAS), Alcian blue, and Masson’s trichrome staining of human kidney, mouse colon, and mouse kidney sections respectively. i The Next-Generation Histopathology Pathway. INSIHGT is compatible with traditional histological pipelines, empowering a multi-pronged approach to maximizing the information extracted from clinical samples. 

the process. The crystals were then collected by vacuum filtration with air continuously drawn at room temperature until the crystals are white, which were warmed to 37[०] C to result in clear, colorless benzyl benzoate. If the resulting colorless benzyl benzoate is cloudy, 3 Å molecular sieves were added to the solvent to absorb the admixed water from condensation, before filtering off to result in a clear colorless benzyl benzoate. This purified benzyl benzoate is ready to constitute BABB clearing solution for imaging. 

## Human and animal tissues 

Adult male C57BL/6 were utilized. These mice were housed in a controlled environment (22–23 °C) with a 12-h light-dark cycle, provided by the Laboratory Animal Service Center of CUHK. Unrestricted access to a standard mouse diet and water was ensured, and the environment was maintained at <70% relative humidity. Tissues were perfusion formaldehyde-fixed and collected by post-mortem dissection. In the case of immunostaining for neurotransmitters where Immusmol antibodies were used, the tissues were perfusion-fixed with the STAINperfect™ immunostaining kit A (Immusmol) with the antibody staining steps replaced with those in our INSIHGT method. 

For human tissues, brain and kidney tissues donated post-mortem by a patient (aged 77 at the time of passing) were used in this study. Prior ethics approvals have been obtained and approved by the Joint Chinese University of Hong Kong-New Territories East Cluster Clinical Research Ethics Committee (approval number 2022.137), with consent from the donor and his family. Human dissection was performed by an anatomist (HML) after perfusion fixation with 4% paraformaldehyde via the femoral artery. The post-mortem delay to fixation and tissue harvesting was 4 weeks at −18 °C refrigeration, and the fixation duration was 1 week at room temperature. The corresponding organs were then harvested and stored in 1x PBS at room temperature until use. 

## Screening deep staining approaches with in situ antibody recovery 

4% PFA-fixed, 1mm-thick mouse cerebellum slices, 0.5 μg antiparvalbumin antibody (Invitrogen, PA1-933), and 0.5 μg AlexaFluor 647-labeled Fab fragments of Donkey anti-Rabbit antibody (Jackson Immunoresearch 711-607-003) were used in this experiment to develop our method. Co-incubation of the secondary Fab fragment and primary antibody was utilized for 1-step immunostaining. All stainings were performed with an overnight immunostaining first stage at room temperature (unless specified otherwise) in various buffers, with subsequent recovery secondary stage at room temperature (unless specified otherwise) in various buffers, as detailed for each strategy below. The tissues were then washed in 1x PBSN, dehydrated with graded methanol, and cleared in BABB, before proceeding to imaging with confocal microscopy. 

For the SDS/αCD system, immunostaining was performed in a solution consisting of 10 mM sodium dodecylsulphate (SDS) in 1xPBS, while recovery was performed with a solution consisting of 10 mM αCD in 1x PBS. 

For the GnCl/GroEL+GroES system, immunostaining was performed in solution consisting of 6 M guanidinium chloride in 1x PBS, while recovery was performed with GroEL+GroES refolding buffer, consisting of 0.5 μM GroEL (MCLabs GEL-100), 1 μM GroES (MCLabs 

Nature Communications | (2024) 15:10888 

14 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

GES-100), 2.5 mM adenosine triphosphate, 20 mM Tris base, 300 mM NaCl, 10 mM MgSO4, 10 mM KCl, 1 mM tris(2-carboxylethyl)phosphine hydrochloride, 10% glycerol, with pH adjusted to 7.9[50] . 

For the sodium deoxycholate (SDC)/βCD system, immunostaining was performed in a solution consisting of 15 mM sodium deoxycholate (SDC) with 240 mM Tris base, 360 mM CAPS (N-cyclohexyl-3-aminopropanesulfonic acid), with pH adjusted to 8, while recovery was performed with a solution consisting of 15 mM βCD with 240 mM Tris base, 360 mM CAPS, with pH adjusted to 8. 

For the Na2[B12H12]/γCD system, immunostaining was performed in a solution consisting of 0.1 M Na2[B12H12] in 1x PBS, while recovery was performed in a solution consisting of 0.1 M γCD in 1x PBS. 

## Benchmarking experiments 

We designed a stringent benchmarking scheme for quantitative evaluation of antibody penetration depth and signal homogeneity across depth for comparison across existing deep immunostaining methods, based on our previously described principles (Supplementary Fig. 1a)[6] The benchmarking experiment is carried out in two parts, the first part using a whole mouse hemisphere stained in bulk with anti-Parvalbumin (PV) antibodies with excess AlexaFluor 647-conjugated secondary Fab — — fragments termed bulk-staining after which the tissue is cut coronally at defined locations using a brain matrix and re-stained with anti-PV — antibodies and AlexaFluor 488-conjugated secondary Fab fragments termed cut-staining (Supplementary Fig. 1a). Hence, signals from bulkstaining can be distinguished easily from cut-staining and reveal different penetration depths of the two-staged immunostaining. We tested different deep immunostaining methods in the bulk-staining stage of the experiments, while the cut-staining was performed in 1× PBS with 0.1% Tween-20 as a conventional immunostaining buffer. The bulkstaining duration for INSIHGT was 24 h in benchmarking. 

All benchmarking samples were perfusion-fixed with 4% paraformaldehyde (PFA) in 1× PBS followed by post-fixation in 4% PFA overnight at 4 °C, except for SHIELD and mELAST samples where the SHIELD protocol was used. In addition, the final RI matching where the benzyl alcohol/benzyl benzoate (BABB) clearing method was universally employed to standardize the changes in tissue volumes and hence penetration distance adjustments. The standardized optical clearing avoids the variability in fluorescent quenching and tissue shrinkage/expansion introduced by different RI matching agents. For bulk-staining during our benchmarking experiment, we followed the published protocols except for eFLASH and mELAST due to the lack of specialized in-house equipment. 

For eFLASH[12] , we stained the SHIELDed and SDS-delipidated tissue in the alkaline sodium deoxycholate buffer (240 mM Tris, 160 mM CAPS, 20% w/v D-sorbitol, 0.9% w/v sodium deoxycholate) and titrated-in acidadjusting booster buffer (20% w/v D-sorbitol and 60 mM boric acid) hourly over 24 h to achieve a −0.1 ± 0.1 pH/h adjustment rate, using primary IgGs with secondary fluorophore-labeled Fab fragments. The tissue was then washed with 1× PBSTN (1× PBS, 1% v/v Triton X-100, and 0.02% w/v NaN3) two times 3 h each before imaging. 

For mELAST[7][,][13][,][14] , we stained the SHIELDed and SDS-delipidated tissue with the antibody and Fab fragments in 0.2 × PBSNaCh (0.2× PBS, 5% w/v NaCh and 0.02% w/v NaN3, 5% v/v normal donkey serum) first for 1 day at 37 °C without embedding the SHIELDed tissue in elastic gel nor compression/stretching, followed by adding Triton X-100 to a final concentration of ~5% and incubated for 1 more day. The tissue was then washed with 1× PBSTN 2 times 3 h each before imaging. 

For CUBIC HistoVision[8] and iDISCO[17] , the tissue was processed and stained as previously described[9] . The staining durations were 14 days for CUBIC HistoVision and 7 days for iDISCO (both using primary IgGs with secondary fluorophore-labeled Fab fragments). 

For SHANEL[51] , the tissue was first delipidated with CHAPS/NMDEA solution (10% w/v CHAPS detergent and 25% w/v N-methyldiethanolamine in water) for 1 week, then further delipidated with 

dichloromethane/methanol as in iDISCO, then treated with 0.5 M acetic acid for 2 days, washed in water for 6 h repeated 2 times, and then treated with guanidinium solution (PBS with 4 M guanidinium chloride, 0.05 sodium acetate, 2% w/v Triton X-100) for 2 days, blocked in blocking buffer (1× PBS, 0.2% v/v Triton X-100, 10% v/v DMSO, 10% goat serum) for 1 day, and finally stained in antibody incubation buffer (1× PBS, 0.2% v/v Tween-20, 3% v/v DMSO, 3% v/v goat serum, 10 mg/L heparin sodium) using primary IgGs with secondary fluorophorelabeled Fab fragments for 7 days. 

For quantification, PV-positive cells were identified using a Laplacian of Gaussian filter, followed by intensity-based segmentation. These segmented masks allow the quantification of bulk- and cutstaining channel intensities, in addition to the distance transformation intensity, performed in MATLAB R2023a (MathWorks, US). For an ideal deep immunostaining, the bulk-immunostaining signals should be independent of the bulk-staining penetration distances computed with distance transform of the segmented tissue boundaries, and perfectly correlate with that of cut-immunostaining. This is often not the case, as “rimming” of bulk-staining signals inevitably occurs as a “shell” around the tissue due to more easily accessible antigens on the bulk-staining tissue surface. The rimming effect can be quantified by fitting a singleterm exponential decay curve 

**==> picture [231 x 21] intentionally omitted <==**

and evaluating the decay constant, tau (τ), across penetration depths, with τ → 0[+] as we approach the ideal case. 

## Screening chemicals for INSIHGT 

We first pre-screened the WCS by immunostaining for parvalbumin in 1 mm[3] of mouse cortex tissue cubes in the presence of WCS at 0.1 M, after 1 day of incubation at room temperature the staining solution was aspirated and 0.1 M corresponding cyclodextrin was added and incubated overnight. The tissue was then washed in PBSN for 15 min two times and cleared with the BABB method, and imaged. This procedure eliminated [B12Br12][2][−] , [B12I12][2][−] , and [PW12O40][3][−] (as cesium or sodium salts) as they do not give the correct immunostaining pattern or lead to tissue destruction. We tested [Fe(C5H5)2][+] (as the hexafluorophosphate salt) for the sake of completion as a low-charge large-sized cation. 

To benchmark the ability in achieving deep and homogeneous immunostaining, the above benchmarking procedure was used. Mouse hemibrains were fixed, washed, and stained with 1 μg rabbit anti-parvalbumin antibody with 1 μg AlexaFluor 647-labeled donkey anti-rabbit secondary antibody Fab fragments in 0.1 M of the WCS. The staining proceeded for 1 day after which the solution was replaced with 0.1 M corresponding cyclodextrin (or its derivatives) and incubated overnight. The hemibrains were then washed in PBSN for 1 h two times, cut in the middle coronally and re-stained for parvalbumin using AlexaFluor 488-labeled secondary Fab fragments. The tissue was then washed, cleared with the BABB method, and imaged on the cut face using a confocal microscope. 

## INSIHGT 

A detailed step-by-step protocol used in this study has been given below. As a general overview, tissues were typically fixed using formalin or 4% paraformaldehyde, thoroughly washed in PBSN, and preincubated overnight at 37 °C in INSIHGT buffer A. The tissues were then stained with a solution containing the desired antibodies, Fab fragments, lectins, and SBEβCD-complexed nucleic acid probes in INSIHGT buffer A, ensuring a final [B12H12][2][−] concentration of 0.25 M. Staining duration varied from 6 h to 10 days based on tissue size, antigen, and required homogeneity (please see the calculation of time t in the step-by-step protocol). Post-staining, the solution was aspirated and replaced with INSIHGT buffer B (0.25 M 2-hydroxypropyl-γ- 

Nature Communications | (2024) 15:10888 

15 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

cyclodextrin in PBS) without prior washing, followed by a minimum 6-h incubation with adequate shaking of the viscous buffer. After sufficient PBSN washing, tissues were ready for imaging or clearing. Over incubation for any steps up to 60 days was tolerable. After imaging, the antibodies can be eluted with 0.1 M sodium sulphite in INSIHGT buffer A at 37 °C overnight. 

## Screening antibodies compatible with INSIHGT 

To test antibodies in a high-throughput manner, we compiled a list of antibodies, reviewed their tissue expression and staining patterns in the literature, and then obtained the respective tissues known to have positive staining. These tissue blocks or entire organs were then washed, dehydrated, delipidated, rehydrated, washed, and infiltrated with INSIHGT solution A as described in the INSIHGT protocol. These INSIHGT-infiltrated tissues were then cut into ~1 mm[3] tissue cubes and placed in a 96-well plate as indicated in the list, with each well containing 70 μl of 1x INSIHGT solution A. About 0.5 μg of the primary antibody to be tested was then added and 0.5 μg of the corresponding AlexaFluor 647 or AlexaFluor 594-conjugated secondary antibody Fab fragment. The AlexaFluor 647 and 594 fluorophores were chosen for to minimize interference from any tissue autofluorescence on the result interpretation. For a total volume and antibodies added two each well, an equal volume of 2x INSIHGT solution A was then added to ensure the final concentration of 1x INSIHGT solution A. The plate was then sealed and the staining was allowed to proceed in the dark overnight at room temperature. The tissues were then washed in INSIHGT solution B for 2 h, PBSN for 1 h for two times, and then dehydrated with through 15 min-incubation of 50% methanol, 100% methanol, and 100% methanol. The tissues were then cleared in BABB for 15 min and proceeded to imaging. The total fixed tissue-to-image time for the antibody compatibility test is <36 h. 

## Comparison between 2D histological staining of post-INSIHGT and control tissues 

Mouse and human samples were pre-processed as described above. Tissues were divided into the post-INSIHGT treated group which underwent the INSIHGT protocol with 3 days of INSIHGT A incubation without the application of antibodies and 6 h of INSIHGT B incubation, plus BABB clearing, and the control group which was immersed in PBSN for an equivalent period of time. Both groups were immersed in 70% ethanol, preceded by the immersion in 100% ethanol for the postINSIHGT group (which were in BABB), and in 50% ethanol for the control group (which were in PBSN). Tissues were then immersed in 100% ethanol, xylene, and paraffin as in the standard paraffin embedding process. The embedded tissues were cut into 5 μm (human) or 10 μm (mouse) sections followed 2D histological staining with special stains. Following standard protocols, H&E staining was performed on human brain and kidney, PAS staining was performed on human kidney, Alcian blue staining was performed on mouse colon, and Masson trichrome staining was performed on mouse kidney samples. 

## Microscopy 

Confocal microscopy was performed using a Leica SP8 confocal microscope equipped with excitation lasers at 405 nm, 488 nm, 514 nm, 561 nm, 649 nm, with detection using a 10× (NA 0.4, Leica HC PL APO ×10/0.40 CS2) or a 40× oil-immersion (NA 1.30, Leica HC PL APO 40×/1.30 Oil CS2) objective and a tunable emission filter. A custom-built MesoSPIM v5.1[52] was used for light-sheet microscopy equipped with lasers at 405 nm, 488 nm, 514 nm, 561 nm, 633 nm, and 675 nm, with detection using an Olympus MVX-ZB10 zoom body with a magnification range from 0.63×–6.3×. The equipped emission filters were from AHF, including QuadLine Rejectionband ZET405/488/561/ 640, 440/50 ET Bandpass, 509/22 Brightline HC, 515/LP Brightline HC Longpass Filter, 542/27 BrightLine HC, 585/40 ET Bandpass, 594 LP Edge Basic Longpass Filter, 660/13 BrightLine HC, 633 LP Edge Basic 

Longpass Filter, and a 685/LP BrightLine HC Longpass Filter. Twophoton tomography was performed at 780 nm excitation[9] using a 16× objective (NA 0.8, Nikon CFI75 LWD 16X W), equipped with four emission filters (ThorLabs 460-60, Semrock 525/50, Semrock 607/70, and Chroma ET 670/50). Basic image acquisition parameters for all microscopy images in this study were listed in Supplementary Table 4. 

## RNA and DNA quality control 

Control and INSIHGT-treated samples following the 1 mm[3] treatment timeline were re-embedded in paraffin wax and sent for nucleic acid integrity, sequencing, and bioinformatics analysis services provided by the BGI Hongkong Tech Solution NGS Lab. RNA integrity number analysis was performed using the Qubit Fluorometer. Whole genome DNA quality analysis was performed using the Agilent 2100 Bioanalyzer system. Sequencing was performed using the DNBSEQ[TM] sequencing technology platform. 

For transcriptomic comparison, the total clean bases were 11.2 Gb and 10.97 Gb for the control and INSIHGT-treated samples, respectively. The clean reads ratio after filtering was 90.64% and 89.96%, respectively. For whole genome sequencing, The total clean bases were 114.5 Gb and 125.2 Gb for the control and INSIHGT-treated samples, respectively, with both samples having a clean data rate of 100% and a mapping rate of 99.96%. 

## RNA FISH HCR with INSIHGT 

Our RNA FISH HCR protocol is largely adapted from Choi et al.[53] . The post-INSIHGT samples were first fixed in 4% PFA for 1 day. The samples were then pre-incubated in pre-hybridization buffer until the tissue sank to the bottom, and hybridized in hybridization buffer at 37 °C overnight. The next day, the tissue was washed in probe wash buffer for 1 h two times at room temperature, pre-incubated in amplification buffer for 30 min, followed by HCR amplification by incubating in amplification buffer with the addition of 30 pmol of fluorescentlylabeled HCR hairpins and incubated overnight at RT. Note that the HCR hairpins were snap-cooled (heated at 95 °C for 2 min and cooled to RT for 30 min) in 10 μL 5× SSC buffer before application to ensure hairpin structures are formed[54] . The samples were then washed thoroughly in 500 μL probe wash buffer for 30 min × 3 times to mitigate non-specific binding and later subjected to confocal imaging. 

The HCR probes which hybridize on the mRNA targets were custom-designed following the approach by Choi et al.[53] , as shown in Table 1, and were purchased from Integrated DNA Technologies. 

## Image processing 

No penetration-related attenuation intensity adjustments were performed for all displayed images except for the 3D renderings (but not 2D cross-sectional views) in Fig. 3 and Supplementary Movie 1 to provide the best visualization of an internal signal. For samples imaged with two-photon tomography, we noticed a thin rim attributed to the heat produced during the gelatin embedding process (which we verified by repeating the staining and confirming its absence with light sheet microscopy). We employed an intensity transformation mask based on the exponent of the distance from the whole organ mask surface. Image segmentation was performed with Cellpose 2.0[28] for cells implemented in MATLAB R2023b or Python, or with simple intensity thresholding. Affine and non-linear image registration was performed in MATLAB R2023a or manually in Adobe After Effects 2020 using the mesh warp effect and time remapping for z-plane adjustment. Image stitching was performed either with ImageJ BigStitcher plugin[55] or assisted manually with Adobe After Effects 2020 followed by tile allocation using customwritten scripts in MATLAB R2023a. 

3D image visualization and Movie rendering were performed with Bitplane Imaris 9.1, which were done as raw data with brightness and contrast adjustments, except for the whole mouse brain imaged with 

Nature Communications | (2024) 15:10888 

16 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

two-photon tomography. To remove their slicing artifacts, we resliced the volume into x-z slices, performed a z-direction Gaussian blur, followed by a 2D Fourier transformand filtered out non-central frequency peaks before inverting the transform. Finally, a Richardson-Lucy deconvolution was performed with a point-spread function elongated in the x-z direction, and resliced back into x-y slices. 

## Segmentation and analysis of podocyte-to-PEC microfilaments in mouse kidneys 

Podocyte-to-PEC microfilaments of 14 mouse kidneys were manually traced via the SNT plugin in ImageJ[56] . Path properties of the tracings were then exported for further analysis using custom codes in MATLAB R2023a. Distance transforms were performed under manually curated glomerulus and Bowman space masks, such that each voxel value corresponds to the distance between that voxel and the nearest nonzero voxel of the Bowman space mask. Path displacement df il was computed via Pythagoras theorem using the start and end coordinates of the filament. Minimal distance dmin is defined as the voxel value difference between the start and end coordinates. Path length dpath is directly measured via SNT. Tortuosity is defined as dpath=df il, skewness is defined as df il=dmin, and the angle of take-off is defined as the angle between the unit gradient vector of the distance transform and the unit path displacement vector. The geodesic distance dAðp, qÞ between voxels p, q 2 A is defined as the minimal of length L of path(s) P = (p1, p2, …, pl) connecting p, q, where A is the set of all voxels constituting the surface of the glomerular mask[57] : 

**==> picture [204 x 52] intentionally omitted <==**

where �h iN represents the Gaussian-weighted smoothing over N[58][,][59] . Eigendecomposition of T[�] is then performed to define the shape (eigenvalues, λ) and the orientation (eigenvectors, ve) of the diffusion ellipsoid. The fractional anisotropy (FA) is then computed from λ: 

**==> picture [203 x 42] intentionally omitted <==**

where FA ranges from 0 (complete isotropic diffusion) to 1 (complete anisotropic diffusion)[60] . 

The tertiary (least) eigenvalue-associated eigenvectors were then extracted for the 3-dimensional image volume, with the 4th dimension encoding the corresponding vector basis magnitudes. To visualize the orientation of fibers in the context of the image, the eigenvectors were intensity-modulated with both the fractional anisotropy and the original image voxel values, and represented as a 3D RGB stack for visualization in Imaris. 

**==> picture [201 x 10] intentionally omitted <==**

## Multi-round multiplexed 3D image processing and analysis 

Correlation statistics were then performed via GraphPad Prism version 8 for Windows, GraphPad Software, Boston, Massachusetts USA, www.graphpad.com. Tracing and statistical analysis for the human cerebellar neurofilament inclusions were performed analogously. 

## Spatial orientation and fractional anisotropy visualization of human cerebellum neural and glial filaments 

To visualize cerebellar neural and glial fibers in their preferred orientations, we performed structure tensor analysis with orientation-based color-coding in 3D. 

In detail, let G : R[3] × R + !R be a 3D Gaussian kernel with standard deviation σ: 

**==> picture [204 x 25] intentionally omitted <==**

Define a 3D image as a function I : R[3] !R which outputs the spatial voxel values. The gradient ∇I : R[3] ! R[3] of I at each voxel is obtained by convolving I with the spatial derivatives of G: 

**==> picture [183 x 21] intentionally omitted <==**

**==> picture [148 x 9] intentionally omitted <==**

where * denotes the convolution operation. 

Compute the structure tensor T : R[3] ! R[3 × 3] as the outer product of ∇I with itself: 

**==> picture [161 x 9] intentionally omitted <==**

T is then smoothed over a neighborhood N via convolution with G to give T[�] : 

**==> picture [170 x 10] intentionally omitted <==**

As the images were acquired across multiple rounds on a confocal microscope, we encountered the issues of misalignment and z-step glitching due to piezoelectric motor errors. Hence, the tiles of images can neither be directly stitched nor registered across multiple rounds. A custom MATLAB code was written to manually remove all the z-step glitching, followed by matching the z-steps across multiple rounds aiding by using the time-remapping function in Adobe After Effects, with linear interpolation for the transformed z-substacks.The resulting glitch-removed, z-matched tiles were then rigid registered using the image registration application in MATLAB, followed by non-rigid registration for local matching. Finally, the registrated tiles were stitched for downstream processing. 

Before segmentation, all non-vessel channels underwent background subtraction. They were then summed to capture the full morphology of stained cells, followed by segmentation using Cellpose 2.0[28] . A custom model was trained and used based on 2D excerpts of the images until adequate segmentation accuracy was achieved by manual inspection. The final test image segmentation has a Dice Coefficient (or F1-score) of 0.9354 ± 0.0596 and Jaccard Index of 0.8824 ± 0.1023, provided as mean ± S.D. on six excerpted test images. Vessels were segmented based on their staining intensity, and a distance transform was used to obtain the distance from vessels for all voxels. The cell masks subsequently facilitated the acquisition of the statistics for all stained channels. 

UMAP was performed in MATLAB R2023a using the UMAP 4.4[55][,][61] package in a nested manner, incorporating the means and standard deviations ofall immunostaining intensities, as well as the distance to the nearest blood vessel. An initial UMAP (with “min_dist” = 0.05, “metric” = “euclidean”, and “n_neighbors” = 15) was applied to each image stack tile, followed by DBSCAN clustering (using the default value ε = 0.6) to eliminate the largest cluster based on cell count. The remaining cells were subjected to a second UMAP (with the same parameters), where another round of DBSCAN clustering (with the same parameters) yielded the final cell clusters for analysis. The choice of UMAP parameters was based on an online guide (https://umap-learn.readthedocs.io/en/latest/ api.html) and visual inspection on the reasonable clustering results. 

Nature Communications | (2024) 15:10888 

17 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Violin plots for each clustered cell type’s distance from neuropeptide Y-positive fibers were obtained by creating a distance transformation field from the segmented fibers. Segmented cell masks were used to compute the mean intensity value of the distance transformation field. The pairwise distances of the clustered cell types were obtained for the 30 nearest neighbors, followed by calculating the mean and SD for the coefficient of variation. The gramm package in MATLAB R2023a was used for plotting some of the graphs[62] . 

## Statistics and reproducibility 

For Fig. 2c, Supplementary Figs. 6, 7, one-component exponential regression was applied for curve fitting, and Pearson’s correlation coefficient was computed for the scattered plot in Fig. 2d. Two-sample unpaired t-test was employed for Supp. Fig. 28 The staining and imaging experiments in Fig. 2–8, were repeated with at least two independent samples in the same or similar condition with slight modifications, such as using similarly sized tissues of similar characteristics (especially for human samples), using different staining antibodies and marker choice, or staining durations. All the results were reliably reproduced in accordance with the expected outcome of the methods. No method was used to predetermine sample size. 

## Reporting summary 

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article. 

## Data availability 

The raw imaging data in this paper are too large for public deposit. They will be made available upon request to the corresponding author (H.M.L). The benchmarking experiment dataset has been deposited and made available for analysis at Code Ocean (capsule link: https://doi.org/ 10.24433/CO.4249201.v1). The data associated with Fig. 7f, g were provided in the Source Data File. Source data are provided with this paper. 

## Code availability 

The code for benchmarking experiment analysis along with sample data has been deposited and made available at Code Ocean (capsule link: https://doi.org/10.24433/CO.4249201.v1). 

## References 

1. Moses, L. & Pachter, L. Museum of spatial transcriptomics. Nat. Methods 19, 534–546 (2022). 

2. Hickey, J. W. et al. Spatial mapping of protein composition and tissue organization: a primer for multiplexed antibody-based imaging. Nat. Methods 19, 284–295 (2021). 

3. Cho, W., Kim, S. & Park, Y.-G. Towards multiplexed immunofluorescence of 3D tissues. Mol. Brain 16, 37 (2023). 

4. Liu, J. T. C., Glaser, A. K., Poudel, C. & Vaughan, J. C. Nondestructive 3D pathology with light-sheet fluorescence microscopy for translational research and clinical assays. Annu. Rev. Anal. Chem. 16, 231–252 (2023). 

5. Richardson, D. S. et al. Tissue clearing. Nat. Rev. Methods Prim. 1, 1–24 (2021). 

6. Yau, C. N. et al. Principles of deep immunohistochemistry for 3D histology. Cell Rep. Methods 3, 100458 (2023). 

7. Ku, T.et al. Elasticizing tissuesforreversibleshapetransformationand accelerated molecular labeling. Nat. Methods 17, 609–613 (2020). 

8. Susaki, E. A. et al. Versatile whole-organ/body staining and imaging based on electrolyte-gel properties of biological tissues. Nat. Commun. 11, 1982 (2020). 

9. Lai, H. M. et al. Antibody stabilization for thermally accelerated deep immunostaining. Nat. Methods 19, 1137–1146 (2022). 

10. Mai, H. et al. Whole-body cellular mapping in mouse using standard IgG antibodies. Nat. Biotechnol. https://doi.org/10.1038/s41587023-01846-0 (2023). 

11. Kim, S.-Y. et al. Stochastic electrotransport selectively enhances the transport of highly electromobile molecules. Proc. Natl Acad. Sci. 112, E6274–E6283 (2015). 

12. Yun, D. H. et al. Ultrafast immunostaining of organ-scale tissues for scalable proteomic phenotyping. bioRxiv 660373 https://doi.org/ 10.1101/660373 (2019). 

13. Park, J. et al. Integrated platform for multi-scale molecular imaging and phenotyping of the human brain. bioRxiv 2022.03.13.484171 https://doi.org/10.1101/2022.03.13.484171 (2023). 

14. Murray, E. et al. Simple, scalable proteomic imaging for highdimensional profiling of intact systems. Cell 163, 1500–1514 (2015). 

15. Park, Y.-G. et al. Protection of tissue physicochemical properties using polyfunctional crosslinkers. Nat. Biotechnol. 37, 73–83 (2018). 

16. Pitochelli, A. R. & Hawthorne, F. M. The isolation of the icosahedral B12H12-2 ION. J. Am. Chem. Soc. 82, 3228–3229 (1960). 

17. Renier, N. et al. iDISCO: a simple, rapid method to immunolabel large tissue samples for volume imaging. Cell 159, 896–910 (2014). 

18. Dent, J. A., Polson, A. G. & Klymkowsky, M. W. A whole-mount immunocytochemical analysis of the expression of the intermediate filament protein vimentin in Xenopus. Development 105, 61–74 (1989). 

19. Masselink, W. et al. Broad applicability of a streamlined ethyl cinnamate-based clearing procedure. Development 146, dev166884 (2019). 

20. Scardigli, M. et al. Comparison of different tissue clearing methods for three-dimensional reconstruction of human brain cellular anatomy using advanced imaging techniques. Front. Neuroanat. 15, 752234 (2021). 

21. Darche, M. et al. Light sheet fluorescence microscopy of cleared human eyes. Commun. Biol. 6, 1–7 (2023). 

22. Cartmell, S. C. et al. Multimodal characterization of the human nucleus accumbens. Neuroimage 198, 137–149 (2019). 

23. Lichtenegger, A. et al. Assessment of pathological features in Alzheimer’s disease brain tissue with a large field-of-view visible-light optical coherence microscope. Neurophotonics 5, 035002 (2018). 

24. Gail Canter, R. et al. 3D mapping reveals network-specific amyloid progression and subcortical susceptibility in mice. Commun. Biol. 2, 360 (2019). 

25. Salvi, G., De Los Rios, P. & Vendruscolo, M. Effective interactions between chaotropic agents and proteins. Proteins 61, 492–499 (2005). 

26. Proc, J. L. et al. A quantitative study of the effects of chaotropic agents,surfactants,andsolventsonthedigestion efficiencyofhuman plasma proteins by trypsin. J. Proteome Res. 9, 5422–5437 (2010). 

27. Dugger, B. N. et al. Neuropathological analysis of brainstem cholinergic and catecholaminergic nuclei in relation to rapid eye movement (REM) sleep behaviour disorder. Neuropathol. Appl. Neurobiol. 38, 142–152 (2012). 

28. Pachitariu, M. & Stringer, C. Cellpose 2.0: how to train your own model. Nat. Methods 19, 1634–1641 (2022). 

29. Weigert, M., Schmidt, U., Haase, R., Sugawara, K. & Myers, E. Starconvex polyhedra for 3D object detection and segmentation in microscopy. In Proc. IEEE Workshop on Applications of Computer Vision 3655–3662 (IEEE, 2019). 

30. Frasconi, P. et al. Large-scale automated identification of mouse brain cells in confocal light sheet microscopy images. Bioinformatics 30, i587–i593 (2014). 

31. Bao, F. et al. Integrative spatial analysis of cell morphologies and transcriptional states with MUSE. Nat. Biotechnol. 40, 1200–1209 (2022). 

32. Shankland, S. J., Smeets, B., Pippin, J. W. & Moeller, M. J. The emergence of the glomerular parietal epithelial cell. Nat. Rev. Nephrol. 10, 158–173 (2014). 

33. Li, Z.-H. et al. The role of parietal epithelial cells in the pathogenesis of podocytopathy. Front. Physiol. 13, 832772 (2022). 

Nature Communications | (2024) 15:10888 

18 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

34. Neal, C. R. et al. Novel hemodynamic structures in the human glomerulus. Am. J. Physiol. Ren. Physiol. 315, F1370–F1384 (2018). 

35. Ohse, T. et al. The enigmatic parietal epithelial cell is finally getting noticed: a review. Kidney Int. 76, 1225–1238 (2009). 

36. Potter, S. S. Single-cell RNA sequencing for the study of development, physiology and disease. Nat. Rev. Nephrol. 14, 479–492 (2018). 

37. Chakraborty, R., Nonaka, T., Hasegawa, M. & Zurzolo, C. Tunnelling nanotubes between neuronal and microglial cells allow bidirectional transfer of α-Synuclein and mitochondria. Cell Death Dis. 14, 329 (2023). 

38. Alarcon-Martinez, L. et al. Interpericyte tunnelling nanotubes regulate neurovascular coupling. Nature 585, 91–95 (2020). 

39. Saha, T. et al. Intercellular nanotubes mediate mitochondrial trafficking between cancer and immune cells. Nat. Nanotechnol. 17, 98–106 (2022). 

40. Wang, X. & Gerdes, H.-H. Transfer of mitochondria via tunneling nanotubes rescues apoptotic PC12 cells. Cell Death Differ. 22, 1181–1191 (2015). 

41. Piwecka, M., Rajewsky, N. & Rybak-Wolf, A. Single-cell and spatial transcriptomics: deciphering brain complexity in health and disease. Nat. Rev. Neurol. 19, 346–362 (2023). 

42. Tanaka, N. et al. Whole-tissue biopsy phenotyping of threedimensional tumours reveals patterns of cancer heterogeneity. Nat. Biomed. Eng. 1, 796–806 (2017). 

43. Xie, W. et al. Prostate cancer risk stratification via nondestructive 3d pathology with deep learning-assisted gland analysis. Cancer Res. 82, 334–345 (2022). 

44. Liu, J. T. C. et al. Harnessing non-destructive 3D pathology. Nat. Biomed. Eng. 5, 203–218 (2021). 

45. iDISCO+ protocol. https://idisco.info/wp-content/uploads/2015/04/ whole-mount-staining-bench-protocol-methanol-dec-2016.pdf. 

46. Seo, J. et al. PICASSO allows ultra-multiplexed fluorescence imaging of spatially overlapping proteins without reference spectra measurements. Nat. Commun. 13, 1–17 (2022). 

47. Bai, B. et al. Deep learning-enabled virtual histological staining of biological samples. Light Sci. Appl 12, 57 (2023). 

48. Suhling, K., French, P. M. W. & Phillips, D. Time-resolved fluorescence microscopy. Photochem. Photobiol. Sci. 4, 13–22 (2005). 

49. Buchwalow, I., Samoilova, V., Boecker, W. & Tiemann, M. Multiple immunolabeling with antibodies from the same host species in combination with tyramide signal amplification. Acta Histochem. 120, 405–411 (2018). 

50. Dahiya, V. & Chaudhuri, T. K. Chaperones GroEL/GroES accelerate the refolding of a multidomain protein through modulating onpathway intermediates. J. Biol. Chem. 289, 286–298 (2014). 

51. Mai, H. et al. Scalable tissue labeling and clearing of intact human organs. Nat. Protoc. 17, 2188–2215 (2022). 

52. Voigt, F. F. et al. The mesoSPIM initiative: open-source light-sheet microscopes for imaging cleared tissue. Nat. Methods 16, 1105–1108 (2019). 

53. Choi, H. M. T., Beck, V. A. & Pierce, N. A. Next-generation in situ hybridization chain reaction: higher gain, lower cost, greater durability. ACS Nano 8, 4284–4294 (2014). 

54. Tsuneoka, Y. & Funato, H. Modified in situ hybridization chain reaction using short hairpin DNAs. Front. Mol. Neurosci. 13, 75 (2020). 

55. Hörl, D. et al. BigStitcher: reconstructing high-resolution image datasets of cleared and expanded samples. Nat. Methods 16, 870–874 (2019). 

56. Arshadi, C., Günther, U., Eddison, M., Harrington, K. I. S. & Ferreira, T. A. SNT: a unifying toolbox for quantification of neuronal anatomy. Nat. Methods 18, 374–377 (2021). 

57. Soille, P. Morphological Image Analysis (Springer Berlin Heidelberg, 2004). 

58. Bigun, J. Optimal orientation detection of linear symmetry. In Proc. IEEE-First International Conference on Computer Vision. 433–438 (IEEE, London, 1987). 

59. Khan, A. R. et al. 3D structure tensor analysis of light microscopy data for validating diffusion MRI. Neuroimage 111, 192–203 (2015). 

60. Bigun, J., Bigun, T. & Nilsson, K. Recognition by symmetry derivatives and the generalized structure tensor. IEEE Trans. Pattern Anal. Mach. Intell. 26, 1590–1605 (2004). 

61. Website. Connor Meehan, Jonathan Ebrahimian, Wayne Moore, and Stephen Meehan (2022). Uniform Manifold Approximation and Projection (UMAP) (https://www.mathworks.com/matlabcentral/ fileexchange/71902), MATLAB Central File Exchange. 

62. Morel, P. Gramm: grammar of graphics plotting in Matlab. J. Open Source Softw. 3, 568 (2018). 

## Acknowledgements 

We would like to express our deepest gratitude to the tissue donor and his family for their generosity and wisdom in supporting scientific studies. We thank William Wu for access to confocal microscopy; Cathy Shuk Ling Chan for manual data annotation and analysis; Ka Wai Chan for administrative support to the project. Figures 1and 6h were partly created with BioRender.com. The project was supported by the Midstream Research Program for Universities (MRP/048/20, H.M.L.) of the Innovation and Technology Council of Hong Kong, a Direct Grant for Research 2022/23 (2022.072, H.M.L.) of the Chinese University of Hong Kong, and the Chinese University of Hong Kong Research – Committee Group Research Scheme (GRS) 2021 22 (granted to Y.K.W.). 

## Author contributions 

Conceptualization: H.M.L. Methodology: C.N.Y., J.T.S.H., R.A.A.C., T.C.Y.W., B.T.Y.W., N.K.N.C., L.Z., E.P.L.T., H.M.L. Investigation: C.N.Y., J.T.S.H., R.A.A.C., T.C.Y.W., B.H., B.T.Y.W., N.K.N.C., L.Z., E.P.L.T., Y.T., J.J.X.L., Y.K.W., H.M.L. Visualization: C.N.Y., J.T.S.H., R.A.A.C., H.M.L. Funding acquisition: Y.K.W., H.M.L. Project administration: H.M.L. Supervision: H.M.L. Writing: C.N.Y., H.M.L. 

## Competing interests 

C.U.H.K. filed a patent application in part based on the invention described in this paper with H.M.L. and C.N.Y. as the inventors. The associated patent, owned by C.U.H.K., was exclusively licensed to Illumos Limited, of which H.M.L. is a co-founder. The remaining authors declare no competing interests. 

## Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-024-55248-0. 

Correspondence and requests for materials should be addressed to Hei Ming Lai. 

Peer review information Nature Communications thanks Ying Hu, who co-reviewed with Hirushi GunasekaraAngela Sirigu, who co-reviewed with Guillaume Lio; Irene Costantini; and Masaharu Yoshihara for their contribution to the peer review of this work. A peer review file is available. 

Reprints and permissions information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Nature Communications | (2024) 15:10888 

19 

Article 

https://doi.org/10.1038/s41467-024-55248-0 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/. 

© The Author(s) 2024 

Nature Communications | (2024) 15:10888 

20 

