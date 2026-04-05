Biophysical Journal Volume 87 August 2004 958–973 

958 

## The Permeability of Gap Junction Channels to Probes of Different Size Is Dependent on Connexin Composition and Permeant-Pore Affinities 

Paul A. Weber,* Hou-Chien Chang,[y] Kris E. Spaeth,[z] Johannes M. Nitsche,[y] and Bruce J. Nicholson* 

*Department of Biological Sciences and[y] Department of Chemical Engineering, State University of New York at Buffalo, Buffalo, New York 14260; and[z] Washington University School of Medicine, St. Louis, Missouri 

ABSTRACT Gap junctions have traditionally been characterized as nonspecific pores between cells passing molecules up to 1 kDa in molecular mass. Nonetheless, it has become increasingly evident that different members of the connexin (Cx) family mediate quite distinct physiological processes and are often not interchangeable. Consistent with this observation, differences in permeability to natural metabolites have been reported for different connexins, although the physical basis for selectivity has not been established. Comparative studies of different members of the connexin family have provided evidence for ionic charge selectivity, but surprisingly little is known about how connexin composition affects the size of the pore. We have employed a series of Alexa dyes, which share similar structural characteristics but range in size from molecular weight 350 to 760, to probe the permeabilities and size limits of different connexin channels expressed in Xenopus oocytes. Correlated dye transfer and electrical measurements on each cell pair, in conjunction with a three-dimensional mathematical model of dye diffusion in the oocyte system, allowed us to obtain single channel permeabilities for all three dyes in six homotypic and four heterotypic channels. Cx43 and Cx32 channels passed all three dyes with similar efficiency, whereas Cx26, Cx40, and Cx45 channels showed a significant drop-off in permeability with the largest dye. Cx37 channels only showed significant permeability for the smaller two dyes, but at two- to sixfold lower levels than other connexins tested. In the heterotypic cases studied (Cx26/Cx32 and Cx43/Cx37), permeability characteristics were found to resemble the more restrictive parental homotypic channel. The most surprising finding of the study was that the absolute permeabilities calculated for all gap junctional channels in this study are, with one exception, at least 2 orders of magnitude greater than predicted purely on the basis of hindered pore diffusion. Consequently, affinity between the probes and the pore creating an energetically favorable in-pore environment, which would elevate permeant concentration within the pore and hence the flux, is strongly implicated. 

## INTRODUCTION 

Gap junctions (GJ) are the only known intercellular channels that allow the direct exchange of molecules up to ;1 kDa in molecular mass between cells (reviewed in Yeager and Nicholson, 1996; Harris, 2001). Each gap junction channel is formed by two hemichannels (connexons), representing hexamers of connexin (Cx) subunits, contributed by each of the coupled cells. To date, over 20 different Cxs have been identified in the mouse and human genomes (Eiberger et al., 2001). This diversity is further increased by the expression of multiple connexins in most cells, allowing for heterologous interactions among members of the connexin family (Bruzzone et al., 1996). These heterologous Cx interactions can be classified as either heterotypic, when two homogeneous connexons (hemichannels) of different Cx composition form a functional channel (Barrio et al., 1991; White et al., 1995), or heteromeric, when two different Cxs mix within one connexon (Stauffer 1995; Jiang and Goodenough, 1996; Brink et al., 1997; Bevans et al., 1998; He et al., 1999). 

Traditionally, gap junctions have been characterized as inert, nonspecific pores. However, the tissue and temporally 

> Submitted October 23, 2003, and accepted for publication March 8, 2004. Address reprint requests to Bruce J. Nicholson, Dept. of Biochemistry, University of Texas Health Science Center at San Antonio, San Antonio, TX 78229. E-mail: bjn@uthscsa.edu. 

specific expression patterns, and the variety of defects induced by genetic ablation of different connexins, suggest that the intercellular signaling of specific molecules may be unique for each isoform (Paul, 1995). Supporting this theory are genetic mutations of different connexins in humans that result in varied developmental and/or physiological defects (summarized in Nicholson, 2003). More direct demonstrations of the distinct properties of Cx isoforms include the failure of one (Cx46) to replace the loss of the other (Cx50) in eye development (White, 2002) and the differential efficacy of connexins in tumor suppression (e.g., Mesnil et al., 1995). 

Previous studies have documented that gap junctions are permeable to some of the more important secondary messengers involved in cell signaling, such as cAMP (Lawrence et al., 1978), Ca[2][1] (Saez et al., 1989), and IP3 (Saez et al., 1989; Sanderson, 1995). More recently, it has been demonstrated that the connexin isoform can influence gap junctional permeability to such natural metabolites. A novel capture technique, used to identify the physiological metabolites that traverse gap junction channels, demonstrated that homotypic channels of Cx43 have 100–300-fold higher selectivity for ATP over those of Cx32. Other metabolites (glutamate, glutathione, ADP, and AMP) show 10–20-fold preferential permeability through Cx43 channels, whereas adenosine is 10-fold more permeable through Cx32 

� 2004 by the Biophysical Society 0006-3495/04/08/958/16 $2.00 

doi: 10.1529/biophysj.103.036350 

Selective Permeability of Gap Junctions 

959 

(Goldberg et al., 1999, 2002). It has also been documented in transfected HeLa cells, loaded with the Ca[2][1] -sensitive fluorescent dye Fura-2, that IP3 permeates homotypic Cx32 gap junctions approximately four times more efficiently than Cx26 and ;2.5 times more efficiently than Cx43 gap junctions (Niessen et al., 2000). The stoichiometry of isoforms within heteromeric Cx26 1 Cx32 connexons, solubilized from rat or mouse liver and reconstituted into liposomes, has been further shown to govern hemichannel selectivity between cAMP and cGMP (Bevans et al., 1998). These studies demonstrate that connexins differentially regulate the intercellular transfer of natural permeants. However, the physical basis of this selectivity remains obscure, as there are no evident correlations between metabolite properties and their permeability through different connexin channels. It is clearly not a simple property like size or charge. 

Efforts to define the basis of connexin selectivity using ion and dye permeabilities of selected connexins expressed in HeLa cells (Elfgang et al., 1995; Cao et al., 1998) and Xenopus oocytes (Cao et al., 1998), or reconstituted into liposomes (Bevans et al., 1998), have been inconclusive. Elfgang et al (1995) investigated a variety of different homotypic and heterotypic gap junctions using a range of molecules of differing charge, shape, and size. Although selectivity was clearly demonstrated, the experiments did not allow clear conclusions to be drawn as to the underlying mechanisms. Cao et al. (1998) provided more quantitative estimates of permeability for an anionic and cationic dye (i.e., Lucifer Yellow and 4#,6-diamidino-2-phenylindole (DAPI), respectively) that suggested charge contributes to the selectivity (Cx45 and Cx26 being more cation selective and Cx32 more anion selective), consistent with results from ion substitution (Veenstra et al., 1995; Veenstra, 1996; Suchyna et al., 1999). In a very different approach employing reconstituted hemichannels of mixed connexin composition in liposomes, Bevans et al. (1998) used a homologous series of polymaltose probes to demonstrate that the presence of Cx26 reduces the size exclusion limit of Cx32 channels. 

Examination of electrophysiological properties of different connexins reveals a broad range of single channel conductances (gj), varying from main states from ;30 pS (Cx57, Manthey et al., 1999; Cx45, Moreno et al., 1995; Veenstra et al., 1994b) to ;300 pS (Cx37, Veenstra et al., 1994a; Traub et al., 1998). This suggests gap junctional pores range in size from 11 (gj ; 30 pS) to 24 A[˚] (gj ; 300 pS) in diameter, if they are modeled as simple aqueous pores in the form of right circular cylinders (Hille, 1992; Veenstra et al., 1995; Veenstra, 1996; Beblo and Veenstra, 1997). However, it has previously been documented that ionic selectivity does not correlate with ionic conductance, suggesting that channels with small gj values do not necessarily possess greater selectivities (Veenstra et al., 1995; Veenstra, 1996) and by inference may not have smaller pore diameters. Consistent with this, Bevans et al. 

(1998) report that Cx26 (gj ; 135 pS) reduces the ability of larger molecules to traverse Cx32 (gj ; 55 pS) channels. 

The effective pore diameter of connexins has been estimated in several ways. Structural measurements from atomic force microscopy (AFM) (Perkins et al., 1997) and electron diffraction (Unger et al., 1999) suggest a narrowest pore diameter of 15 A[˚ ] , with a wider cytoplasmic opening of 25–45 A[˚] in diameter. However, the open or closed state of these channels could not be verified. Estimates based on size cutoffs for permeants suggest that the effective pore diameter varies over a range of 8–16 A[˚ ] , depending on the connexin isoform (Beblo and Veenstra, 1997; Oh et al., 1997; Wang and Veenstra, 1997; Veenstra, 2000; Gong and Nicholson, 2001). Some studies employed a highly uniform series of neutral probes (polyethylene glycols, PEGs), but could only measure block and not flux rates. Others utilized hydrodynamic equations to extrapolate a limiting diameter from fluxes of tertiary amines of increasing size. 

This study focuses on a quantitative investigation of size selectivity in gap junction pores composed of six different connexins, each expressed in Xenopus oocytes. A series of three fluorescent Alexa probes (Molecular Probes, Eugene, OR) that vary in size from 350 to 760 mol wt (MW), but possess similar charge and chemical structure, were employed as probes. We have chosen connexin channels that represent the complete range of homotypic gj values within the connexin family of proteins. Quantitative numbers describing the permeability of single gap junction channels are calculated using a three-dimensional diffusion model (Nitsche et al., 2004; cf. Nitsche, 1999) to deconvolute junction derived intercellular permeability from other simultaneously operating factors within each cell. This allowed the calculation of the absolute permeability of several gap junction channels for this series of dyes, a determination that has only been made once previously for two connexins with one dye (Valiunas et al., 2002). 

## MATERIALS AND METHODS 

## Three-dimensional modeling of probes 

Three-dimensional modeling of Alexa dyes was performed using the molecular modeling software InsightII version 98.0 (Molecular Simulations, San Diego, CA). Dyes were assembled from individual aromatic rings and common functional groups using the Builder module and energy minimized with the esff force field in the Discover3 module. Measurements, in angstrom units, of nonhydrated Alexa fluors were performed across each three-dimensional face of the probes using the Discover3 module. 

## Oocyte preparation 

Adult female Xenopus frogs were anesthetized on ice, and ovarian lobes containing stage V and VI oocytes were removed and stored at 19�C in Leibovitz-15 medium (L-15, 1:2 dilution), (Gibco Laboratories, Grand Island, NY) buffered with 12.5 mM Hepes, pH 7.6. Three antibiotics (penicillin, streptomycin, and gentamycin) were each added at a concentration of 10 mg/ml. To remove the follicle layer, ovarian lobes were dissected 

Biophysical Journal 87(2) 958–973 

Weber et al. 

960 

into clumps containing ;50 oocytes and incubated in Ca[2][1] -free OR-2 solution (83 mM NaCl, 2 mM KCl, 1 mM MgCl2, 5 mM Tris buffer, pH 7.5) containing 2 mg/ml collagenase (Sigma Chemical, St. Louis, MO) for 1 h (Dasckal et al., 1985). Oocytes were then washed with OR-2 and placed back in L-15. After selection of stage VI oocytes, the follicle layer was then stripped manually with forceps. 

Defolliculated Xenopus laevis oocytes were pressure injected using an electric microinjector (Nanoject Variable Microinjection Apparatus, model 3-000-203-XV, Drummond Scientific, Broomall, PA), and micropipettes pulled from glass capillaries (3-00-203-G/XL, Drummond Scientific) with a horizontal micropipette puller (model P-87, Sutter Instrument, Novato, CA). A total of 41.4 nl 0.1 ng/nl Cx cRNA was injected, along with 0.1 ng/nl of antisense DNA oligo, to endogenously expressed Cx38 (XeCx38; nucleotides 327–353, numbering beginning at the start of translation). In the case of connexins that form functional channels with XeCx38, oocytes were also preinjected with antisense oligo 96 h before injection of Cx cRNA to allow time for complete degradation of the endogenous protein. Connexin cRNAs were synthesized from pSP64 or pBluescript vectors using either mMessage mMachine (Ambion, Austin, TX) or AmpliScripe (Epicentre Technologies, Madison, WI) in vitro transcription kits. cRNA injected oocytes were incubated at 19�C for 24 h before manual devitellinization and pairing. Oocytes were manipulated into pairs, with vegetal poles opposed and facing downwards, for 24–48 h in 35-mm petri dishes coated with 1 mm agar in which uniform depressions were formed for each oocyte pair. 

## Oocyte intercellular conductance measurements 

The dual cell voltage clamp technique (as described by Spray et al., 1981) was used to measure the conductance between oocyte pairs. A 5-s voltage pulse was applied to one of the cells, whereas the other cell was held at a constant voltage (Gene Clamp 500B, Axon Instruments, Foster City, CA), and the junctional currents to the nonpulsed cell were recorded digitally (pClamp6 or pClamp8 Data Acquisition and Analysis software, Axon Instruments). Clamping electrodes were prepared from capillary glass (1B150F-4, World Precision Instruments, Sarasota, FL) using a horizontal micropipette puller (model P-87, Sutter Instrument). The input resistance of all electrodes was ;1 MV. Conductances were measured before (initial) and after (final) each dye transfer experiment. Initial conductances were required to be between 5 and 50 mS so as to ensure a significant signal above background, whereas avoiding the possibility that cytoplasmic bridges could have formed between the oocytes. If the conductance of an oocyte pair changed significantly during the experiment, the initial and final conductances were averaged. However, if the change exceeded the initial value by twofold, data from the oocyte pair was not included in our analysis. 

## Fluorescent imaging 

After recording initial junctional conductances between an oocyte pair, one of the oocytes was injected, as described above, with 41.4 nl 10-mM solution (in H2O) of a hydrazide sodium salt of either Alexa Fluor 350 (Alexa 350 MW), Alexa Fluor 488 (Alexa 570 MW), or Alexa Fluor 594 (Alexa 760 MW) (A-10439, A-10436, and A-10438, respectively; Molecular Probes). Time courses of fluorescent dye diffusion between oocytes were collected by mounting the oocytes on a Zeiss Axiovert 10 microscope (Jena, Germany) and using a digital camera (model RTE/CCD-1300-Y, Princeton Instruments, Trenton, NJ) operated by imaging software (Metamorph 4.0, Universal Imaging, West Chester, PA) to acquire images at 30-min intervals over a 6-h period. The following excitation (x), emission (m) filter sets were used for each dye: Alexa 350, (x) D360/40 and (m) D460/50; Alexa 570, (x) 450–490 and (m) LP520; and Alexa 760, (x) 530–585 and (m) LP615; Chroma Technology, Brattleboro, VT). To quantify Alexa dye diffusion between oocytes, the average fluorescence intensity was calculated within boxes of uniform area, centered in each oocyte and placed 50 pixels from the intercellular interface. The ratio of acceptor/donor (A/D) cell intensities 

plotted as a function of time contributed the key input to the mathematical model (Nitsche et al., 2004) that was applied to extract the unitary channel permeability from these macroscopic data. 

Color assignment of digitized fluorescent images was based on pixel intensity over a range of 0–4095. In this scale an intensity of zero is assigned a color of black and an intensity of 4095 is assigned a color of white. Presented in Fig. 2 D is the color table used to assign a color range to varying pixel intensities. Color assignment was linear over the range of pixel intensities observed as demonstrated in Fig. 2 E, where color assignment was normalized to the length of the color table image. 

## Mathematical modeling 

The mathematical model employed is described in Nitsche et al. (2004) and accounts for diffusion of dyes within the cytoplasm of each cell in addition to permeation through the membrane interface between the cells. Cytoplasmic diffusion, slowed by a very significant degree of dye binding to the cytoplasm, represents a significant mass transfer resistance in the oocyte system. If this physical phenomenon were not accounted for (e.g., in a simpler model assuming well mixed cells), then much of the slowness of intercellular dye transfer would be erroneously attributed to a low apparent gap junctional permeability, underrepresenting the actual permeability. The model was applied in two steps. A single-cell specialization of it (with the intercellular junctional membrane permeability set to zero) was used to first analyze diffusion of dye across a single cell of a nonjunctionally coupled cell pair, yielding values of the diffusion and binding coefficients characterizing the cytoplasm. Subsequently, the intercellular junction permeability appearing in a full two-cell version of the model was adjusted by trial and error to fit the time evolution of the measured acceptor/donor fluorescence intensity ratio. The intercellular junction permeability so obtained was converted to unitary gap junctional permeability via division by the total number of functionally coupled gap junction channels (as explained in Results). 

## RESULTS 

## Three-dimensional modeling of the Alexa series of fluorescent probes 

A rigorous investigation of the size selectivity of gap junctional pores requires a graded series of permeants of increasing size that do not vary in other parameters (i.e., charge, substituent groups, etc.). The commercially available Alexa series of fluorescent probes were ideally suited to this purpose. These probes are all structurally based on similar aromatic conjugations and functional groups. All three Alexa dyes are anionic, with net charges of �2 (Alexa 488, MW 570; Alexa 594, MW 760) and �1 (Alexa 350, MW 350) distributed similarly over their surfaces. Calculated spacefilling models of each probe, rotated from its orientation in (A) by 90� about its y (B) or x axis (C) are shown in Fig. 1, along with the structural formula of each (Fig. 1 D). Given their structural homologies, differences in single channel permeability of the Alexa dye series between different gap junctions should be predominantly based on size. 

Using InsightII/Discover3 software modeling (see Materials and Methods), the unhydrated dimensions of each Alexa probe can be approximated (Fig. 1 E). The probes are clearly nonspherical, but a reasonable approximation of the minimal pore diameter required to allow their transit would be the 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

961 

**==> picture [336 x 376] intentionally omitted <==**

FIGURE 1 Structure and molecular dimensions of Alexa series of fluorescent probes. Space-filling models showing each axial face (separated by 90� rotations) of the three Alexa dyes used in this study (A–C). Atoms are represented by color: carbon (green), hydrogen (white), nitrogen (blue), oxygen (red), and sulfur (yellow). Bar in image, 5 A[˚ ] . Structural formulas of each probe are shown in D. The maximal dimensions of each axial face are displayed in the table (E). The limiting dimensions for passage through a pore, assuming the longest dimension would align axially with the pore in cases of tight fit, are bolded. 

median axial diameter of the probe (Fig. 1 E, bold), assuming alignment of the longest molecular axis with the pore axis to be the orientation in which a molecule traverses a pore in cases of tight fit. Given these assumptions, and the nonhydrated state of the models, it is likely that this value, which ranges from 5 to 14 A[˚] for these fluorophores, underestimates effective probe size within the pore. 

## Differential diffusion of Alexa dyes through homotypic gap junction channels 

Use of the Xenopus oocyte expression system provided the significant advantage of being able to measure functional gap junction expression levels (electrophysiologically) and diffusion of fluorescent dyes (optically) within the same cell pair. Dye transfer from donor to acceptor oocyte was measured digitally over 6 h with junctional conductance being assessed immediately before and after the time course. 

Pseudocolor images (see legend of Fig. 2) of sample time courses with each Alexa dye for several homotypic connexin combinations are shown in Fig. 2, A–C. Pairs were chosen 

with similar intercellular conductances, although the Cx45 pairs consistently developed lower conductances than the other connexins (see Table 1). Taking conductances into account, all connexins tested allowed intercellular diffusion of Alexa 350 (MW 350), although the Cx37 channels seemed less efficient (Fig. 2 A). Similar rates of transfer of Alexa 488 (MW 570) were seen with Cx26, Cx32, and Cx40, whereas Cx37 and Cx45 pairs showed a decrease compared to Alexa 350, and Cx43 appeared to show enhanced transfer (Fig. 2 B). Increasing the size of the probe to Alexa 594 (MW 760) only caused a slight drop in transfer across Cx32 and Cx43 junctions, but greatly reduced transfer in Cx26, Cx40, and Cx45 pairs and eliminated detectable transfer in Cx37 pairs. The sensitivity of detection for the three dyes varied, with Alexa 350 having approximately twofold lower quantum yield in our detection system than the other two dyes. However, detectability of dye transfer between oocyte pairs was in practice limited by the background levels of fluorescence seen in oligonucleotide injected pairs (our standard negative control). Again, Alexa 350 was the only one of the three dyes that consistently 

Biophysical Journal 87(2) 958–973 

Weber et al. 

962 

**==> picture [241 x 449] intentionally omitted <==**

FIGURE 2 Representative time courses for transfer of the three Alexa dyes through different homotypic gap junction channels in Xenopus oocyte pairs. Images were taken using Metafluor (West Chester, PA) software at the indicated times (far left) after Alexa 350 (A), Alexa 488 (B), or Alexa 594 (C) microinjection into the left oocyte (donor) of each pair. Oocytes were injected 16–24 h earlier with antisense oligo to XeCx38 without (left column) or with the indicated connexin cRNA. Although gap junctions composed of all connexins allowed some passage of the smallest dye (Alexa 350), as the size of the dyes increased, greater selectivity was evident, so that only Cx32 and Cx43 channels passed Alexa 594 efficiently. Color assignment of digitized fluorescent images is based on pixel intensity, proportional to fluorescent probe concentration, as indicated in D. The range of colors varied linearly with pixel intensity along the color table (E). 

showed transfer in these negative controls, producing a 5–10-fold higher background than seen with Alexa 488 and Alexa 594. The combination of these two factors placed differential limits on detectability that are discussed in the following section. 

TABLE 1 Macroscopic, single channel conductances (gj), and calculated channel numbers for each homotypic and heterotypic connexin combination tested in Xenopus oocyte pairs 

|||||No. of channels|
|---|---|---|---|---|
|Cx|gobserved (mS)*|gj (pS)|gcorrected (mS)y|(3105)z|
|mCx45|4.05|32§{|4.27|1.3|
|rCx32|45.2|55k**|107|20.0|
|rCx43|48.8|90yy|130|14.8|
|rCx26|42.6|135k**|94|7.1|
|mCx40|54.9|198zz|185|9.5|
|mCx37|31.7|315§§|53|2.3|
|Cx26/Cx32|44.8|90k**|105|12.8|
|Cx37/Cx43|35.8|140{{|66|5.6|



*gobserved equals the conductance calculated from the voltage difference between the electrodes, and compensation current in the voltage clamp of the cell where the membrane potential is held constant. ygcorrected equals the junctional conductance corrected for cytoplasmic access resistance as estimated in Fig. 5. zN ¼ gcorrected/gj. §Moreno et al. (1995). {Veenstra et al. (1994b). kBukauskas et al. (1995a). **Suchyna et al. (1999). yyVeenstra et al. (1995). zzBukauskas et al. (1995b). §§Traub et al. (1998). {{Cx43/Cx37 single channel conductances were obtained by the sum of the respective homotypic hemichannel resistances estimated from Traub et al. (1998), Veenstra et al. (1995), and Moreno et al. (1994). 

The Alexa dyes also showed minimal leakage across nonjunctional membranes, with the notable exception of Alexa 350 (Fig. 2 A). However, leak of this dye seemed to correlate with connexin expression, as it was minimal in oocyte pairs that were uninjected, or in pairs expressing connexins that were less permeable to this dye (Cx37), or where levels of expression were lower (Cx45). This raises the intriguing possibility that the extracellular leak of Alexa 350, rather than occurring nonspecifically across membranes, may arise from patent connexin hemichannels in the unopposed membranes. However, even in the case of Alexa 350, leakage represented a relatively small fraction of the total dye present in the system and could be neglected in the subsequent modeling analysis. 

## Calculation of single channel permeabilities of the Alexa dyes through different connexins 

The observations presented in Fig. 2 provide a qualitative view of how different connexins determine transfer rates and impart distinct size cutoffs for the family of anionic dyes studied. However, the experimental system allowed us to not only quantify these differences, but also to calculate absolute permeabilities of the dyes through channels of each connexin type, rather than simply present comparative numbers. Despite the recent growth in dye transfer studies addressing relative permeabilities of connexins channels, absolute estimates have been difficult to obtain for gap junction 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

963 

channels and are important in that they place constraints on the underlying physical features of permeability of these relatively large pores. 

As a first step, macroscopic diffusion in an uncoupled oocyte was analyzed in order that contributions from the intercellular channels could be deconvoluted from the other factors influencing dye movement, in particular slower diffusion within the cytoplasm than in bulk water, reversible binding to the cytoplasm, and premixing of the dye that occurs immediately after injection. These factors were included in an intracellular diffusion model (described in full in Nitsche et al., 2004), and the parameters characterizing them were obtained from fits to the diffusion of each dye across the uncoupled cell (sample fits are shown in Fig. 3). 

This model was then run in its more general mode, in which cytoplasmic diffusion occurs in series with passive diffusion of dye across the intercellular interface. The only remaining variables in this model were the number (Npore) of channels and the unique area 3 permeability ((AP)pore) factor that characterizes the unitary permeability of each channel with respect to each permeant (see Fig. 4 and Nitsche et al., 2004). The product of these two variables was obtained as a measure of macroscopic membrane permeability (Pjunc ¼ Npore(AP)pore/Amem) from fits of the transfer of each dye from donor to acceptor cell for each connexin (examples for Cx32 shown in Fig. 4). The Pjunc values derived from these fits were largely influenced by the longer time points, although most curves also showed a more rapid rise in the first 30 min. The fits to these initial increases were influenced by the different background levels in each experiment but were also predicted by the model, since at early time points more dye was available for transfer, resulting in faster transfer than at later time points where much of the dye was unavailable for transfer as it had reached equilibrium binding to the cytoplasm (Kcyt ¼ (bound dye)/(free dye) ¼ 2–10, depending on the dye (Fig. 3)). The area of the opposed membranes (Amem) was estimated to be ;0.41 mm[2] from optical measurements of paired oocytes fitted to an idealized geometrical representation (see Nitsche et al., 2004), allowing the calculation of Npore(AP)pore. 

Within this scheme, the calculation of absolute values for single channel permeabilities (i.e., (AP)pore) would only require an estimate of the number of channels (Npore). This could, in principle, be obtained from the measured junctional conductance (Gobs) of each cell pair and the known single channel conductances (gj values) of each of the connexins tested (Table 1). In the case of Cx45, single channel conductances have been determined only for rat and human (a mouse clone was used here). However, given the interspecies similarity in gj values for other connexins, it seemed reasonable to assume the same value for mouse Cx45. In the absence of any contrary reports, it is assumed that all gap junctions involved in this study exist predominantly in their respective main conductive states in 

Xenopus oocytes, despite one report in N2A cells that Cx37 may reside in a 70-pS subconductance state (Veenstra et al., 1994a). 

One complication to this analysis was introduced by the high conductances (typically 25–50 mS; Table 1) between oocytes that were needed to measure dye transfer. This required a correction for access resistance to the channels that included the cytoplasmic or any other operative resistance within each cell, which could account for a significant fraction of the voltage drop between the clamping electrodes in each cell (Fig. 5 A). This is empirically manifested as an apparent loss of voltage sensitivity of gap junction channels as conductances increase, such that higher applied voltages are required for the same gating response (Fig. 5, B–D). From such data, the value DVj/DVtotal can be estimated for each oocyte pair, where DVtotal is the recorded voltage between the clamping electrodes, and DVj is the actual voltage drop across the gap junction channels. A simple cell pair conductance model (see Appendix B in Nitsche et al., 2004) then yields the linear relation DVj/DVtotal ¼ 1 � bGobs., in which b is a parameter representing all nonjunctional series resistances, and Gobs would be the junctional conductance if DVj ¼ DVtotal. A plot of DVj/DVtotal versus Gj for Cx32 coupled oocyte pairs (Fig. 5 E) yielded a value for b of 12,800 V from a best fit to the data. At conductances below 7 mS, this correction factor has a small effect, but at high conductances it can be significant (e.g., 0.23 for Gobs ¼ 60 mS). For values of Gobs greater than this, the correction factor becomes increasingly inaccurate. 

A second complication to this analysis is introduced by the length of the experiment, leading to potentially significant changes in the junctional conductance during the experiment. To control for this, conductances were measured immediately before and after the dye transfer time course, and an average value was used. Any oocyte pairs in which the conductance changed by greater than twofold during the 6-h experiment were not included in our analyses due to the potential for errors in the estimate of channel number. 

A comparison of the final average numbers of channels for each connexin in these experiments (Table 1) shows Cx32 to be expressed at about twice the levels of most connexins (i.e., Cx26, Cx40, and Cx43), whereas Cx37 and Cx45 are expressed at significantly lower levels (;1/9th and 1/15th of Cx32 levels, respectively). It appears that ;10[5] channels are needed to detect dye transfer in the oocyte system. Applying this method of estimating channel number to our model, (AP)pore values could be calculated for each connexin pair. The average values of (AP)pore for each connexin isotype with each dye is summarized in Table 2 and graphically on a log scale in Fig. 6. 

Overall, unitary permeabilities of gap junction channels composed of different connexins for a particular dye vary by factors of 6 and 8 for Alexa 350 and Alexa 488, respectively, and ;20 for Alexa 594, where size exclusion appears to play a role. The six isotypes studied can be grouped into two 

Biophysical Journal 87(2) 958–973 

Weber et al. 

964 

**==> picture [217 x 566] intentionally omitted <==**

FIGURE 3 Fits of the single cell diffusion model to transfer data for each of the three Alexa dyes within a single, uncoupled oocyte. Fluorescence intensities were determined from two boxes of identical size, a donor (containing the site of dye injection) and an acceptor box within one oocyte of an uncoupled pair. The ratio of the pixel intensities in the acceptor/donor boxes (A/D) was plotted against time and fitted with the single cell diffusion model that includes terms for cytoplasmic diffusion (Dcyt) and reversible binding to the yolk (kcyt, forward rate constant; Kcyt, equilibrium constant) 

different classes based on their relative decreases in permeability as Alexa probe size increases. The single channel permeabilities for both Cx32 and Cx43 (Fig. 6, green) show only small decreases in permeability (two- to fourfold) across the range of dyes used. Surprisingly, Cx43 channels actually show a twofold increase in permeability as the permeant size increases from Alexa 350 to Alexa 488, before showing a fourfold drop in permeability for the largest Alexa dye. 

In contrast, Cx26, Cx37, Cx40, and Cx45 (Fig. 6, red) channel permeabilities all decreased by 20- (Cx26) to 45-fold (Cx40 and Cx45) between the smallest and largest Alexa probes, although the difference in permeability between smallest and middle dye was relatively small (negligible for Cx26 and Cx40, and twofold for Cx37 and Cx45). Cx37 was the least permeable of all of the connexins to the Alexa probes in general, and its permeability to Alexa 594 was reduced to the limits of detection in this system (hence, no value is presented in Table 2). This limit of detection varied from dye to dye, due to differences in detectability of the dyes in our system (lowest for Alexa 350) and differing levels of background transfer of dye between oocytes in our oligo-injected negative control pairs that was also worst in the case of Alexa 350 (as described above). In the worst-case scenario of Alexa 350, background levels correspond to an effective Pjunc of 2.7 3 10[�][6] cm[2] /s. If one assumes 10[6] channels between cell pairs (the average of all the connexins tested; see Table 1), this would correspond to a detection limit for single channel permeability of 0.1 3 10[�][10] mm[3] /s. This is an order of magnitude below the permeabilities of any of the connexins tested here (see Table 2). The detectability limits for Alexa 488 and Alexa 594 were even lower by a factor of at least 10 (approximately twofold better detectability and 5–10-fold lower background transfer) For Cx37, with an average of 2 3 10[5] channels between cells, this corresponded to a limit of detection of ;0.05 3 10[�][10] mm[3] /s for Alexa 594. This is half that measured for the next least permeable connexin for this dye (Cx40) and over 10fold lower than the permeability of Cx37 to Alexa 488 (24fold less than the permeability to Alexa 350). 

## Heterotypic gap junctional permeabilities are similar to permeabilities possessed by the more restrictive parental homotypic channel 

In addition to comparisons of homotypic gap junction channels, the Xenopus oocyte system is ideally suited to an examination of heterotypic combinations of connexins (different connexins expressed in opposing cells). For this 

(equations in A are fully derived in Nitsche et al., 2004). Representative fits for each Alexa dye are shown (B). The initial rapid rise is dominated by free diffusion in the cytoplasm, whereas the slower transfer after 10 min is dominated by binding to the cytoplasm. Parameter values determined by fitting the model (solid curves) to the data (s) are indicated on each graph. 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

965 

**==> picture [217 x 473] intentionally omitted <==**

FIGURE 4 Fits of the dual cell hindered diffusion model to intercellular transfer of the three Alexa dyes through Cx32 gap junctions. Data was collected and plotted as in Fig. 4, but in this case the donor and acceptor boxes were in two separate cells coupled with Cx32 gap junction channels. The macroscopic model, incorporating cytoplasmic diffusion and binding parameters determined as in Fig. 3, is fitted to the data by adjusting the permeability Pjunc of the junctional membrane separating the oocytes (A). Solutions are obtained using a finite difference methodology (see Nitsche et al., 2004). Fits of the model to experimental data for each of the Alexa dyes and one sample connexin are shown in B. 

purpose, we chose two examples for analysis: Cx32/Cx26 and Cx37/Cx43 heterotypic channels. On initial inspection, the permeability of heterotypic channels seems dominated by the more restrictive of the parental channels (Fig. 7, A and B). Estimates of single channel permeabilities of these hetero- 

typic channels, however, require an estimate of their single channel conductances (gj). This has been measured for Cx26/Cx32 heterotypic channels as 90 pS at Vj ¼ 0, although this does vary with Vj (Barrio et al., 1991; Suchyna et al., 1999). The gj for heterotypic Cx37/Cx43 channels has not been measured, but can be estimated by assuming that the two-homomeric connexons behave independently and can be modeled as two resistors in series. This has proven to be a valid assumption for other heterotypic channels, including 32/26 (Suchyna et al., 1999), 43/40 (Cottrell and Burt, 2001), and 43/45 (Moreno et al., 1994). Hence, based on the known gj values for Cx37 (315 pS, Traub et al., 1998) and Cx43 (;90 pS, Veenstra et al., 1995; Moreno et al., 1994), a gj of 140 pS was assumed for Cx37/Cx43 heterotypic gap junction channels in these studies. 

Estimates of single channel permeabilities to the Alexa series of probes for Cx26/Cx32 and Cx37/Cx43 heterotypic channels, summarized in Table 2 and Fig. 7, C and D, confirmed the original subjective assessment that the permeability of heterotypic channels is similar to the permeability of the more restrictive parental homotypic channel. For each dye, flux through the asymmetric heterotypic channels was tested in both directions. In the case of Cx32 and Cx26, there were no statistical differences between the Alexa 350 (significance level p . 0.3, based on a Student’s t-test) or Alexa 488 (p . 0.6) permeabilities of either homotypic channel and heterotypic Cx26/Cx32 (dye injected into Cx26 cell) or Cx32/Cx26 (dye injected into Cx32 cell) channels. However, Cx32 channels possessed significantly higher permeabilities to Alexa 594 than did Cx26 or either configuration of the Cx32/Cx26 heterotypic channel (p , 0.004). By comparison, no significant differences (at p , 0.05) were evident between the Alexa 594 permeabilities of Cx26 and Cx32/Cx26 (p ¼ 0.3) or Cx26/ Cx32 channels (p ¼ 0.07). 

In comparisons of Cx37/Cx43 heterotypic channels, although Cx37 showed significantly lower permeability to Alexa 350 than Cx43 (p ¼ 0.03), no statistically significant differences in permeability to this dye could be demonstrated between either homotypic channel or Cx37/Cx43 heterotypic channels (p . 0.1). However, for both Alexa 488 (p , 0.002) and Alexa 594 (p ¼ 0.0008), the permeability of homotypic Cx43 channels was significantly greater than either configuration of the Cx37/Cx43 heterotypic channel. Homotypic Cx37 permeabilities to Alexa 594 are not reported due to their extremely low values, but permeability for Alexa 488 was essentially identical for Cx37 and Cx43/ Cx37 heterotypic channels. 

As would have been predicted based on known physical principles, no asymmetry in dye transfer was seen in either of the heterotypic combinations tested with any of the three dyes (i.e., rates of steady-state flux were indistinguishable, no matter which side of the heterotypic channel faced the donor cell). This was true, even though pairings of channels included connexins with very different homotypic channel 

Biophysical Journal 87(2) 958–973 

Weber et al. 

966 

**==> picture [337 x 337] intentionally omitted <==**

FIGURE 5 Method for estimation of junctional conductance (and channel number) in highly coupled oocyte pairs. Diagram of the dual cell voltage clamp of Xenopus oocyte pairs illustrates that the current path between the two clamps includes both cytoplasmic (Rcyt) and junctional (Rj) resistances in series (A). At low junctional conductances (,10 mS), effectively the entire voltage drop occurs across Rj (i.e., Vj ¼ Vtotal where Vtotal ¼ Va � Vb), and accurate junctional conductances are provided by DIa/Vtotal. Junctional current recorded from such a pair of oocytes exhibit a time dependent, voltage-induced decay for voltage steps of either polarity that is characteristic of each connexin (Cx40 trace shown in B). As conductance increases (i.e., Rj decreases), the voltage drop across Rcyt becomes significant, so that greater voltage steps are needed to achieve the same gating response of the channels (cf. C and D). Actual Vj can be estimated from the relative response of the channels. A plot of these estimated Vj/Vtotal values against junctional conductance is shown in E, with a linear regression best fit (see Appendix to Nitsche et al., 2004). This plot was then used to correct observed conductance values to obtain more accurate estimates of actual intercellular conductances when cells were well coupled. Numbers of channels connecting cells could then be obtained from the published unitary conductance for each connexin. 

properties (i.e., Cx37 and Cx43) and heterotypic channels that have been demonstrated to rectify electrically (i.e., Cx26/Cx32, Suchyna et al., 1999). 

## DISCUSSION 

The work presented here represents only the second determination of the absolute values of unitary permeability 

TABLE 2 Single channel permeabilities (310[2][10] mm[3] /s) for Alexa dyes through homotypic and heterotypic gap junction channels 

|Cx||350*|488*|594*|
|---|---|---|---|---|
|26|2.5|6 0.5 (8)|2.8 6 1.5 (6)|0.13 6 0.05 (10)|
|32|3.1|6 0.8 (15)|3.3 6 0.8 (15)|1.6 6 0.4 (10)|
|37|1.2|6 0.3 (3)|0.6 6 0.1 (4)|ND (6)|
|40|4.4|6 1.2 (8)|3.6 6 0.9 (4)|0.10 6 0.01 (4)|
|43|2.4|6 0.3 (6)|4.8 6 1.0 (7)|1.2 6 0.2 (8)|
|45|7.3|6 1.5 (6)|3.3 6 0.0 (2)|0.16 6 0.05 (13)|
|26/32|2.4|6 0.8 (4)|3.4 6 1.0 (8)|0.31 6 0.08 (13)|
|32/26|2.3|6 0.2 (2)|3.9 6 0.7 (4)|0.27 6 0.10 (3)|
|37/43|2.0|6 0.4 (3)|NT|0.07 (1)|
|43/37|2.0|6 0.1 (4)|0.9 6 0.3 (3)|0.09 6 0.03 (3)|



ND, not detected; NT, not tested. Number of data sets used in calculating permeability shown in parentheses. *Mean 6 SE of (AP)pore (units of 10[�][10] mm[3] /s). 

of gap junction channels for larger solutes (cf. Valiunas et al., 2002), and the first to perform a comparative study of multiple connexins using a range of dyes. Estimation of absolute values, rather than the relative comparisons in previous studies, was made possible by the capability, in the Xenopus oocyte expression system, to record electrically (conductance) and optically (dye spread) from the same cell pair, and the development of models that allowed the junctional properties to be extracted from the other variables that influence measurements in the system. Both the relative and absolute permeabilities determined here for six different connexins channels reveal several novel insights that influence our thinking about the way in which these structures are likely to impose selectivity on the exchange of information between cells. 

## Connexin composition imposes distinct size exclusion limits on intercellular permeability 

Two distinct patterns of permeability were observed among the connexins examined here. Cx43 and Cx32 showed only a twofold drop in permeability as the probes increased in size from Alexa 350 to Alexa 594. In fact, no change (Cx32) or even an increase (Cx43) in permeability was seen in going from Alexa 350 to Alexa 488. All other connexins 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

967 

**==> picture [217 x 127] intentionally omitted <==**

FIGURE 6 Calculated unitary channel permeabilities for the three different Alexa dyes for six different connexins plotted against the MW of the dyes. The logarithm of homotypic gap junctional permeability (APpore calculated from the three-dimensional model; Nitsche et al., 2004) for each connexin is plotted against the molecular weight of each Alexa probe (Alexa 350 ¼ 350 MW; Alexa 488 ¼ 590 MW; Alexa 594 ¼ 760 MW). The homotypic channels present in this study can be grouped into three different classes (as noted by color). Cx32 and Cx43 (green) show minimal decreases in permeability for all three Alexa dyes. All other connexins (red) show dramatic decreases in permeability to the largest dye, Alexa 594, but Cx37 channels (purple) are significantly less permeable to the Alexa dyes in general, and permeability to Alexa 594 was close to detectable limits (;10[�][11.5] , indicated by a dashed line). 

tested showed no change (Cx26 and Cx40) or a twofold drop (Cx37 and Cx45) in permeability as the probe size increased form Alexa 350 to Alexa 488. However, in contrast to Cx43 and Cx32, these connexins displayed a large decrease of 20- (Cx26) to 45-fold (Cx40 and Cx45) in permeability to Alexa 594 (compared to Alexa 350). In the case of Cx37, this reduced permeability to at or below detectable limits, corresponding to a drop of $25-fold from the measured permeability of these channels to Alexa 350. This suggested that the largest Alexa dye must be close to the exclusion limit of these channels such that steric constraints and hydrodynamic hindrance within the channel, possibly at a point of constriction (see below), significantly hinders diffusion. Based on these overall comparisons, we would suggest that the effective exclusion limits of the connexin channels studied here can be ranked in decreasing order as: Cx32 $ Cx43 � Cx26 $ Cx40 � Cx45 $ Cx37. 

Similar conclusions were reached in a previous study (Gong and Nicholson, 2001) that estimated the cutoff limits for entry of PEG into the channels to be greatest for Cx32 (PEG 300) and progressively smaller for Cx26 (PEG 200) and Cx37 (PEG 157). Generally, the size-exclusion limits for the Alexa dyes seemed larger than for PEG, at least when measured by MW. Even comparisons of the unhydrated dimensions of the Alexa fluorophores (see Fig. 1) to the estimated Stokes-Einstein radius of the PEGs showed a consistent discrepancy in size, suggesting that the nature of the probe and its interaction with the pore could influence permeability limits. However, differences in both the methods used to establish the dimensions of these two 

molecular series, and the means to measure their passage through the channel, could have influenced absolute estimates of limiting pore diameter, although keeping the relative order of connexin permeability consistent. 

It is of interest to note that, whereas all of the Alexa dyes are anionic, most connexins have been reported to be at least modestly selective for cations (Veenstra et al., 1995). The relative importance of charge in determining permeability could not be directly assessed here, as cationic dyes show too high a binding constant for the oocyte cytoplasm to be useful in dye transfer experiments. However, it is unlikely to be a dominant property, as connexins with very different cation and anion selectivities have quite similar permeabilities to Alexa 350 and Alexa 488 (e.g., Cx32 and Cx40, with cation/ anion ratios of ;0.9 and 3.4, respectively, vary in permeability to either dye by #25%). Conversely, channels with similar cation/anion selectivity (e.g., Cx37 and Cx40 at 3.4 and 3.6, respectively) can differ significantly in terms of their absolute permeability to the Alexa probes (four- to sixfold for Alexa 350 and Alexa 488). 

Comparisons of the exclusion limits for the Alexa dyes or PEG with the single channel conductance of the corresponding gap junction channels revealed a surprising lack of, or even an inverse, correlation. The least restrictive connexins, Cx43 and Cx32, had among the lowest channel conductances (90pS (Veenstra et al., 1995) and 55pS (Bukauskas et al., 1995a; Suchyna et al., 1999), respectively). By contrast, Cx26 and Cx40 have intermediate conductances (135 pS (Bukauskas et al., 1995a; Suchyna et al., 1999) and 198 pS (Bukauskas et al., 1995b), respectively) and permeabilities, whereas Cx37 has the largest recorded conductance of 315 pS (Traub et al., 1998) but is the most restrictive to passage of the largest Alexa dye and PEG. The notable exception is Cx45, which shows both a low channel conductance of 32pS (Moreno et al., 1995; Veenstra et al., 1994b) and a highly restrictive passage of the largest Alexa dye. 

In these comparisons, we have used published values for the main conductance states of each of the connexin channels. Although most of these connexin channels can also exist in at least one main substate, the assumption of a single main state is valid in this study, as these substates are typically only observed at high DVj, and all dye transfer experiments were done in the absence of any transjunctional voltage gradient. Only Cx37 channels show a significant frequency of subconductance states at low DVj. If one were to assume that a significant number of channels were in the lower conductance state, which would further increase the estimate of channel number, this would in turn decrease the estimate of the single channel permeability of these channel, making the differences in permeability of Cx37 channels and those of most other connexins even larger. 

The significance of these generally inverse relationships between size exclusion limits and conductances is not immediately evident. However, in estimating the effective 

Biophysical Journal 87(2) 958–973 

Weber et al. 

968 

**==> picture [331 x 421] intentionally omitted <==**

FIGURE 7 Permeabilities of the heterotypic gap junction channels Cx32/Cx26 and Cx37/ Cx43 to the Alexa dye series. Representative images of intercellular diffusion of the three Alexa dyes are shown for two different heterotypic gap junction channels, Cx26/Cx32 (A) and Cx37/Cx43 (B) and their homotypic counterparts, along with a negative control injected with antisense oligonucleotides to XeCx38 (–). All images represent data collected 360 min after initial dye injection. Calculated unitary permeabilities for each of the three Alexa dyes for homotypic Cx32 (green) and Cx26 (red) channels and for both orientations of heterotypic Cx26/Cx32 channels (dotted blue, dye injected cell is written first) are plotted against the MWs of the dyes in C. Analogous plots for Cx37 (pink), Cx43 (green) and both Cx37/Cx43 heterotypic orientations (dashed blue) are shown in D. Cx37 permeability to Alexa 594 was at the limit of detection (;10[�][11.5] , indicated by dotted line), and permeability of Cx37Cx43 to Alexa 488 was not determined (indicated by ?). As might be expected from physical principles, neither heterotypic channel showed any rectification in their permeabilities. In both cases, the behavior of the heterotypic channels most closely resembles the more restrictive of the parental homotypic channels in showing markedly reduced permeability for the largest Alexa probe. 

pore diameter of a large channel like the gap junction, one might expect that ions would diffuse more independently of interactions with the pore wall than larger charged solutes. Hence, ion flux, or conductance, should represent a better reflection of average pore diameter if modeled simply as electromigration though a cylindrical channel. This would suggest, then, that some gap junction channels (e.g., Cx37) have very large diameters when averaged over the whole length of the channel, but that at some point within the pore there must be a constriction that imposes a stringent size limit on larger permeants but has little effect on overall conductance. This would also be true to a lesser degree with Cx26 and Cx40 channels. By this argument, Cx32 and Cx43 channels would be predicted to be more uniform in diameter along their length, producing relatively low conductance but high permeability gap junction channels. A prediction arising from these models is that the shape, in 

profile, of gap junction channels composed of distinct connexins would vary significantly. 

## Gap junction pores show large enhancements of dye flux over hindered diffusion, indicating a dye-pore affinity 

A comparison of the permeabilities of all connexins for each of the smaller two dyes in the Alexa series revealed differences in permeation of a factor of 6 (Table 2). This seemed likely to reflect differential affinities between the fluorescent probes and the various connexins that make up the pores. However, the most compelling indication that permeant-pore affinities are likely to play a role comes from the overall magnitudes of the channel permeabilities themselves. Based on hindered diffusion models of spherical permeants through circular right cylinders, described in 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

969 

**==> picture [235 x 512] intentionally omitted <==**

FIGURE 8 Addition of dye-pore affinity into the three-dimensional hindered diffusion model is required for reasonable fits to the empirical data. The logarithm of single channel permeability (AP)pore is plotted against the molecular weight of each Alexa probe for Cx43 (A), Cx26 (B), and Cx37 (C) homotypic gap junction channels. Solid lines representing classical pore diffusion theory in the absence of any affinity (i.e., dye-pore attraction) clearly underestimate actual permeabilities by 1–2 orders of magnitude. Dashed and dotted lines represent pore theory in which van der Waals affinities between the dyes and the pore have been incorporated as an example of permeant-pore affinity, with access resistance terms being either included (dashed) or excluded (dotted) (Nitsche et al., 2004). Clearly, inclusion of an affinity term produces a much better overall representation of the data. As described in the text, van der Waals interactions were chosen as 

detail in Nitsche et al. (2004), the permeabilities of the Alexa dyes reported here would require pores 36–80 A[˚] in diameter. This clearly exceeds all reasonable estimates of the pore diameter of gap junction channels (typically 10–20 A[˚ ] ), based on either structural studies, inferences from unitary conductances, or size exclusion limits for permeants as reported here. Stated another way, the estimated permeabilities were 1–2 orders of magnitude greater than would have been expected from hindered diffusion alone (Fig. 8). 

Inclusion of a significant affinity between the pore wall and the Alexa probes in the microscopic diffusion model, however, would effectively increase the pore partition coefficients of the dyes. The term ‘‘affinities’’ does not imply the extreme limit of attraction that causes binding and immobilization of the permeant, but rather attractions that make the pore an energetically favorable environment, elevating the in pore concentration of the permeant and leading to a marked enhancement of flux through the pore. As a test of this principle, we incorporated van der Waals interactions between the fluorescent probes and the wall of the channel into our model (described in detail in Appendix D of Nitsche et al., 2004). The inclusion of a simple representation of short-range repulsion near the pore wall in our model prevents the phenomenon of tight binding. Clearly there can be multiple potential sources of affinity between probe and pore, including electrostatic interactions that can exert a relatively strong influence. However, they are not readily incorporated into a pore model in the absence of any structural information about the precise location of charges. Furthermore, the mapping of pore lining residues in the membrane spanning portions of Cx32 channels indicate that this part of the pore is almost exclusively hydrophobic, with no exposed charges (Skerrett et al., 2002). Hence, van der Waals interactions are likely to be ubiquitous throughout the channel, and can be readily estimated without detailed pore structure. Incorporation of this factor into the microscopic model, using reasonable values for the Hamaker constant for the dyes (see Nitsche et al., 2004), led to predicted permeabilities, depending on the diameter of the pore, that were much closer to the experimentally observed values and 1–2 orders of magnitude larger than predictions based on passive diffusion alone (Fig. 8). Given some contribution from pore access resistance, this model is consistent with pore diameters for the junctional channels of 10–20 A[˚ ] , well within empirically established values (see Fig. 8 in Nitsche et al., 2004). 

This model is also consistent with the assumption that the channel conductances of different connexins reflect the average diameters of their pores. Cx37, the channel with 

an illustrative model that did not require assumptions about charge locations in the pore and were consistent with the hydrophobic nature of the residues identified as lining the pore (Skerrett et al., 2002), but similar corrections could be made by incorporating electrostatic interactions. 

Biophysical Journal 87(2) 958–973 

Weber et al. 

970 

the largest conductance (and by inference, the largest average diameter), requires the least correction to the data, as presumably the interactions of the probe with the pore are minimal for most of the channel length. Conversely, the correction factors for Cx32 and Cx43, the channels with two of the smaller conductances, had the greatest effect because of the close interaction between the permeant and the pore. Hence, this affinity model predicts that smaller pores can show higher permeability to solutes than larger pores, where interactions with the channel wall would be minimal. This might also explain why some channels (e.g., Cx43) showed a modest increase in permeability when probe size increased (e.g., from Alexa 350 to Alexa 488), as this would allow closer interactions with the pore wall. However, as the permeant approaches the size limit of the pore, steric constraints (especially at the constriction postulated above) and hydrodynamic drag play a major role, resulting in the large drop in permeability for the largest Alexa probe in Cx26, Cx37, Cx40, and Cx45 channels. 

In the one previous study estimating absolute flux rates for permeants through gap junctions expressed in HeLa cells, Valiunas et al. (2002) found much lower permeabilities for Lucifer Yellow (MW 427) through Cx43 and Cx40 channels (1560 and 300 molecules per second per channel, respectively) than we report here for even the largest of the Alexa probes (MW 790) (70,000 and 6,000 molecules per second per channel, respectively) (values are normalized for a concentration gradient of 1 mM across the channels). The intermediate sized Alexa 488 (MW 590) had even higher permeabilities for these two connexins (300,000 and 200,000 molecules per second per channel at 1 mM). (Note: If the relative differences in permeability between Cx43 and Cx40 relate in part to the relative size exclusion limits of these pores, then the effective diameter of LY (5.3-fold difference between Cx43 and Cx40) would appear to lie between Alexa 488 (1.5-fold difference between Cx43 and Cx40) and Alexa 590 (12-fold difference between Cx43 and Cx40)). 

Although there are clear differences in the two experimental situations and in the models applied to analyze the respective sets of data (discussed extensively in Nitsche et al., 2004), the different physical circumstances and assumptions used are unlikely to account for the 1–2 orders of magnitude differences in the estimated flux rates. For example, although cytoplasmic binding was not considered in the model of Valiunas et al., in such small cells and with short time constants for transfer, this would be unlikely to significantly change their numbers. Certainly, differences in the structures of Lucifer Yellow and the Alexa dyes used here could contribute significantly, particularly in light of the interactions between the probes and pore wall deduced above. Preliminary comparisons in oocytes suggest that Lucifer Yellow may be less permeable than Alexa 488, although only by a factor of ;2 (A. Verma, unpublished results). It is also possible that differences in the state of the channels expressed in different systems could also contribute significantly. In this 

context, Cx43 is typically phosphorylated at multiple sites in most mammalian expression systems (Musil et al., 1990), whereas it appears that there is minimal phosphorylation in oocytes (Zhou et al., 1999). As discussed in Nitsche et al. (2004) in terms of a possible electrostatic effect, given that phosphorylation has been shown to reduce unitary channel conductance, it would likely have a significant effect on the passage of larger anionic dyes. 

Interestingly, Valiunas et al. (2002) note that the rates of flux that they measure would make the gap junction channels minimally effective at transmitting low abundance signals between cells. However, the study here paints a different picture, with affinities between permeants and the pore wall contributing to much higher flux rates that would certainly allow for efficient transfer of even low abundance species with relatively short half-lives. For example, assuming similar flux rates for metabolites as reported here for the middle-sized Alexa dye, even with concentration gradients of 1 mM, transfer rates would be 40–300 molecules per second per channel, depending on the connexin. Given the thousands of channels that connect most cells, even for molecules with quite short half-lives, this should allow for efficient transfer of signals between cells, at least in the case of the connexins that are most permeable for the particular metabolite. 

The affinities of gap junction channels for second messengers and metabolites is likely to have been fine tuned through evolution to optimize each connexin to the function(s) it fills in a given tissue or cell type. Already substantial evidence exists that the selectivity of different connexins for specific natural permeants may significantly exceed that seen here for the Alexa dyes. The passage of ATP through Cx43 channels is favored by between 100- and 300-fold over that through Cx32 (Goldberg et al., 1999, 2002), whereas other metabolites like ADP, AMP, glutathione, and glutamate show lower degrees of preference for Cx43 channels, and adenosine passes 10-fold more readily through Cx32 channels (Goldberg et al., 2002). Reconstituted hemichannels with differing Cx32/Cx26 composition have also been shown to have remarkable selectivity between cAMP and cGMP (Bevans et al., 1998). There are no obvious rules based on size or charge that can explain the results for natural permeants. This is where the use of a series of artificial probes where one property at a time can be altered is likely to be of great use in unraveling the physical basis of gap junction selectivity. 

## Permeability determinants: in the pore or other parts of the connexin structure? 

In terms of determinants for the size selectivity of the pores, an examination of the main pore-lining residues in M2 and M3 mapped in Cx32 by Skerrett et al. (2002) does not reveal any consistent pattern of side-chain conservation among the more restrictive connexins (i.e., Cx26, Cx37, Cx40, and Cx45), compared to the more permeable ones (i.e., Cx32 and 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

971 

Cx43). This is probably not surprising, as differences in the exclusion limits between connexins is likely to arise more from changes in the overall profile of the pore than from changes in individual side chains. Hence, indirect effects induced by changes in nonpore lining residues may well contribute to the general shape of, and localized restrictions within, the pore. Previously, Oh et al. (1997) presented evidence that an X-linked Charcot-Marie-Tooth (CMTX) related mutation in M1, at S26, could affect the size exclusion limits of Cx32. A mutation at this site has also been associated with changes in single channel conductance (Moreno et al., 1994, 1995). Sequence alignments of the connexins from the study here indicated that this same residue was consistently larger (T) in the more restrictive pores, and smaller (S) in the pores that were permeable to Alexa 594. However, preliminary mutagenic studies on this site revealed only modest effects on the permeability to Alexa 594 (data not shown), suggesting that this was not a major determinant of size cutoff for these channels. Clearly, more extensive molecular analyses, including systematic changes within the pore lining regions will be needed to define the basis for size selectivity and affinity of different connexins. 

## Heterotypic channel permeability is dominated by the more restrictive connexin 

In selecting heterotypic channels to examine for permeability, we chose combinations in which the homotypic parental channels showed large differences in permeant size cutoff, and also ones that are known, or likely, to form in situ. Both Cx32/Cx26 and Cx43/Cx37 pairings showed size-exclusion characteristics most similar to the more restrictive parental connexin. Thus, in Cx32/Cx26 channels, there was, if anything, an increase in permeability in going from Alexa 350 to Alexa 488, but a 10-fold drop in permeability with the largest Alexa dye. Although this drop is less than half the drop seen with Cx26 alone, it is much greater than seen with Cx32 channels. Furthermore, the heterotypic channels would be expected to show somewhat less influence of size on permeability than Cx26 homotypic channels, as there would only be a barrier to transit in one of the two hemichannels. A similar pattern was observed for the Cx43/Cx37 channels, in that permeability to Alexa 594 did not drop to near undetectable levels as for Cx37 homotypic channels but was reduced 10-fold compared to Alexa 488 and over 20-fold compared to Alexa 350. These reductions in permeability as size of the probe increased were much larger than seen with Cx43 channels (Table 2; Fig. 7). 

In terms of general affinity for the pore, as opposed to sizeexclusion limits, simplified models of heterotypic channels as resistances-in-series indicate that the hemichannel with highest affinity for the probes has the most influence on permeability. This prediction is consistent with the observation in Table 1 that the permeability values for heterotypic Cx43/Cx37 channels for Alexa 350 were not significantly 

different to those of Cx43 channels but almost double those of Cx37 channels. This would be consistent with the higher affinity of the Cx43 hemichannel for this class of probes exerting a positive influence on the permeability of the heterotypic channel. Although the same was not true for permeability to the Alexa 488 probe, it is likely that steric hindrance to diffusion was already having an influence on permeability through the heterotypic channels. 

Overall, the properties of heterotypic channels seem relatively well predicted by the properties of the homotypic channels of the contributing connexins. In addition, since it is straightforward to assess permeability through these heterotypic channels in either direction, we confirmed here that these channels show no rectification for steady-state diffusion, despite the fact that Cx32/Cx26 channels had been shown to be electrically rectifying (Barrio et al., 1991; Suchyna et al., 1999). Based on physical principles, this result is expected. However, claims of rectifying passive dye flux have been published previously (e.g., Robinson et al., 1993). In all of these cases, the cell systems between which the communication occurred were asymmetric, and differences in the size or coupling levels of the donor and acceptor pools could account for the findings. In this study, this variable was controlled, as both cells were the same size, and as a result no found. 

## FUTURE PROSPECTS 

The observations presented here clearly establish a significant range of size exclusion limits for gap junction channels composed of different connexins and, more importantly, demonstrate that the pore lining can apparently have a significant affinity for permeants as they approach the pore exclusion limit. This results in fluxes that can exceed those that would arise by passive diffusion in a nonattractive (i.e., nonenergetically favorable) pore by several orders of magnitude. The next major challenge lies in identifying the properties of both the permeants and the pore lining residues that contribute to this affinity and defining how it affects the permeation of natural metabolites through these pores. Given that each connexin is likely to have evolved for specific functions associated with the tissue in which it is expressed, it is quite possible that the amount of, and variation in, affinity arising for endogenous molecules may significantly exceed that seen with the dyes used here. The basis for this selectivity is likely to arise from a complex combination of charge, size, shape, and aromaticity of the permeant species. Finally, although heterotypic combinations of connexins were shown to have channel properties that were relatively well predicted from the properties of the component connexins, it is not clear that the same will hold with heteromeric mixes of connexin subunits within a hemichannel. Such mixes of connexins are likely to be common in situ and may even be the predominant form. Understanding the added dimension that they introduce to the permeability 

Biophysical Journal 87(2) 958–973 

Weber et al. 

972 

of gap junction channels will be another major challenge for the future. 

We thank Mary Merritt for the continuous supply of good quality dissected Xenopus oocytes. 

This work has been supported by a grant from the Whitaker Foundation to J.M.N. and B.J.N. and National Institutes of Health grants to B.J.N. 

- He, D. S., J. X. Jiang, S. M. Taffet, and J. M. Burt. 1999. Formation of heteromeric gap junction channels by connexins 40 and 43 in vascular smooth muscle cells. Proc. Natl. Acad. Sci. USA. 96:6495–6500. 

- Hille, B. 1992. Ionic Channels of Excitable Membranes, 2nd ed. Sinauer Asssociates, Sunderland, MA. 

- Jiang, J. X., and D. A. Goodenough. 1996. Heteromeric connexons in lens gap junction channels. Proc. Natl. Acad. Sci. USA. 93:1287–1291. 

- Lawrence, T. S., W. H. Beers, and N. B. Gilula. 1978. Transmission of hormonal stimulation by cell-to-cell communication. Nature. 272:501– 506. 

## REFERENCES 

- Barrio, L. C., T. Suchyna, T. Bargiello, L. X. Xu, R. Roginski, M. V. L. Bennett, and B. J. Nicholson. 1991. Gap junctions formed by connexin 26 and 32 along and in combination are differently affected by applied voltage. Proc. Natl. Acad. Sci. USA. 88:8410–8414. 

- Beblo, D. A., and R. D. Veenstra. 1997. Monovalent cation permeation through the connexin40 gap junction channel: Cs, Rb, K, Na, Li, TEA, TMS, TBA, and effects of anions Br, Cl, F, acetate, aspartate, glutamate, NO3. J. Gen. Physiol. 109:509–522. 

- Bevans, C. G., M. Kordel, S. K. Rhee, and A. L. Harris. 1998. Isoform composition of connexin channels determines selectivity among second messengers and uncharged molecules. J. Biol. Chem. 273:2808–2816. 

- Brink, P. R., K. Cronin, K. Banach, E. Peterson, E. M. Westphale, K. H. Seul, S. V. Ramanan, and E. C. Beyer. 1997. Evidence for heteromeric gap junction channels formed from rat connexin43 and human connexin37. Am. J. Physiol. 42:C1386–C1396. 

- Bruzzone, R., T. W. White, and D. L. Paul. 1996. Connections with connexins: the molecular basis of direct intercellular signaling. Eur. J. Biochem. 238:1–27. 

- Bukauskas, F. F., C. Elfgang, K. Willecke, and R. Weingart. 1995a. Heterotypic gap junction channels (connexin 26 or connexin 32) violate the paradigm of unitary conductance. Pflugers Arch. 429:870–872. 

- Bukauskas, F. F., C. Elfgang, K. Willecke, and R. Weingart. 1995b. Biophysical properties of gap junction channels formed by mouse connexin 40 in induced pairs of transfected human HeLa cells. Biophys. J. 68:2289–2298. 

- Cao, F., R. Eckert, C. Elfgang, J. M. Nitsche, S. A. Snyder, D. F. Hulser, K. Willecke, and B. J. Nicholson. 1998. A quantitative analysis of connexin-specific permeability differences of gap junctions expressed in HeLa transfectants and Xenopus oocytes. J. Cell Sci. 111:31–43. 

- Cottrell, G. T., and J. M. Burt. 2001. Heterotypic gap junction channel formation between heteromeric and homomeric Cx40 and Cx43 connexons. Am. J. Physiol: Cell Physiol. 281:C1559–1567. 

- Dasckal, N., B. Gillo, and Y. Lass. 1985. Role of calcium mobilization in mediation of acetylcholine-evoked chloride currents in Xenopus laevis oocytes. J. Physiol. (Lond.). 366:299–313. 

- Elfgang, C., R. Eckert, H. Lichtenberg-Frate, A. Butterweck, O. Traub, R. A. Klein, D. F. Hulser, and K. Willecke. 1995. Specific permeability and selective formation of gap junction channels in connexintransfected HeLa cells. J. Cell Biol. 129:805–817. 

- Eiberger, J., J. Degen, A. Romualdi, U. Deutsch, K. Willecke, and G. Sohl. 2001. Connexin genes in the mouse and human genome. Cell Commun. Adhes. 8:163–165. 

- Goldberg, G. S., P. D. Lampe, and B. J. Nicholson. 1999. Selective transfer of endogenous metabolites through gap junctions composed of different connexins. Nat. Cell Biol. 1:457–459. 

- Goldberg, G. S., A. M. Moreno, and P. D. Lampe. 2002. Gap junctions between cells expressing connexin 43 or 32 show inverse permselectivity to adenosine and ATP. J. Biol. Chem. 277:36725–36730. 

- Gong, X. Q., and B. J. Nicholson. 2001. Size selectivity between gap junction channels composed of different connexins. Cell Commun. Adhes. 8:187–192. 

- Harris, A. L. 2001. Emerging issues of connexin channels: biophysics fills the gap. Q. Rev. Biophys. 34:325–472. 

- Manthey, D., F. Bukauskas, C. G. Lee, C. A. Kozak, and K. Willedcke. 1999. Molecular cloning and functional expression of the mouse gap junction gene encoding connexin-57 in human HeLa cells. J. Biol. Chem. 274:14716–14723. 

- Mesnil, M., V. Krutoviskikh, C. Piccoli, C. Elfgang, O. Traub, K. Willecke, and H. Yamasaki. 1995. Negative growth control of HeLa cells by connexin genes: connexin species specificity. Cancer Res. 55: 629–639. 

- Moreno, A. P., J. G. Laing, E. C. Beyer, and D. C. Spray. 1995. Properties of gap junction channels formed of connexin 45 endogenously expressed in human hepatoma (SKHep1) cells. Am. J. Physiol. 268:C356–C365. 

- Moreno, A. P., J. C. Saez, G. I. Fishman, and D. C. Spray. 1994. Human connexin 43 gap junction channels. Regulation of unitary conductances by phosphorylation. Circ. Res. 74:1050–1057. 

- Musil, L. S., B. A. Cunningham, G. M. Edelman, D. A. Goodenough. 1990. Differential phosphorylation of the gap junction protein connexin43 in junctional communication-competent and -deficient cell lines. J. Cell. Biol. 111:2077–2088. 

- Nicholson, B. J. 2003. Gap junctions: from cell to molecule. J. Cell Sci. 116:4479–4481. 

- Niessen, H., H. Harz, P. Bednew, K. Kramer, and K. Willecke. 2000. Selective permeability of different connexin channels to the second messenger inositol 1,4,5-triphosphate. J. Cell Sci. 113:1365–1372. 

- Nitsche, J. M. 1999. Cellular microtransport processes: intercellular, intracellular, and aggregate behavior. Annu. Rev. Biomed. Eng. 1:463– 503. 

- Nitsche, J. M., H. C. Chang, P. A. Weber, and B. J. Nicholson. 2004. A transient diffusion model yields unitary gap junctional permeabilities from images of cell-to-cell fluorescent dye transfer between Xenopus oocytes. Biophys. J. 86:2058–2077. 

- Oh, S., Y. Ri, M. V. L. Bennett, E. B. Trexler, V. K. Verselis, and T. A. Bargiello. 1997. Changes in permeability caused by connexin 32 mutations underlie X-linked Charcot-Marie-Tooth disease. Neuron. 19:927–938. 

- Paul, D. L. 1995. New functions for gap junctions. Curr. Opin. Cell Biol. 7:665–672. 

- Perkins, G. A., D. A. Goodenough, and G. E. Sosinsky. 1997. Threedimensional structure of the gap junction connexon. Biophys. J. 72:533– 544. 

- Robinson, S. R., E. C. Hampson, M. N. Munro, and D. I. Vaney. 1993. Unidirectional coupling of gap junctions between neuroglia. Science. 262:1072–1074. 

- Saez, J. C., J. A. Connor, D. C. Spray, and M. V. Bennett. 1989. Hepatocyte gap junctions are permeable to the second messenger, inositol 1,4,5-trisphosphate, and to calcium ions. Proc. Natl. Acad. Sci. USA. 86:2708–2712. 

- Sanderson, M. J. 1995. Intercellular calcium waves mediated by inositol triphosphate. Ciba Found. Symp. 188:175–194. 

- Skerrett, I. M., J. Aronowitz, J. H. Shin, G. Cymes, E. Kasperek, F. L. Cao, and B. J. Nicholson. 2002. Identification of amino acid residues lining the pore of a gap junction channel. J. Cell Biol. 159:349–359. 

- Spray, D. C., A. L. Harris, and M. V. L. Bennett. 1981. Equilibrium properties of a voltage-dependent junctional conductance. J. Gen. Physiol. 77:77–93. 

Biophysical Journal 87(2) 958–973 

Selective Permeability of Gap Junctions 

973 

- Stauffer, K. A. 1995. The gap junction proteins b1-connexin (connexin-32) and b2-connexin (connexin-26) can form heteromeric hemichannels. J. Biol. Chem. 270:6768–6772. 

- Suchyna, T. M., M. Chiton, J. Nitsche, A. L. Harris, R. D. Veenstra, and B. J. Nicholson. 1999. Different ionic permeabilities for connexin 26 and 32 produce rectifying gap junction channels. Biophys. J. 77:2968–2987. 

- Traub, O., B. Hertlein, M. Kasper, R. Eckert, A. Krisciukaitis, D. Hulser, and K. Willecke. 1998. Characterization of the gap junction protein connexin37 in murine endothelium, respiratory epithelium, and after transfection in human HeLa cells. Eur. J. Cell Biol. 77:313–322. 

- Unger, V. M., N. M. Kumar, N. B. Gilula, and M. Yeager. 1999. Threedimensional structure of a recombinant gap junction membrane channel. Science. 283:1176–1180. 

- Valiunas,V.,E.C.Beyer,andP.R.Brink.2002.Cardiacgapjunctionchannels show quantitative differences in selectivity. Circ. Res. 91:104–111. 

- Veenstra, R. D. 1996. Size and selectivity of gap junction channels formed from different connexins. J. Bioenerg. Biomembr. 28:327–337. 

- Veenstra, R. D. 2000. Ion permeation through connexin gap junction channels: effects on conductance and selectivity. In Gap junctions: Molecular Basis of Cellular Communication in Health and Disease. Current Topics in Membranes, Vol. 49. C. Peracchia, editor. Academic Press, New York. 95–129. 

- Veenstra, R. D., H. Z. Wang, D. A. Beblo, M. G. Chilton, A. L. Harris, E. C. Beyer, and P. R. Brink. 1995. Selectivity of connexin-specific 

gap junctions does not correlate with channel conductance. Circ. Res. 77:1156–1165. 

- Veenstra, R. D., H. Z. Wang, E. C. Beyer, S. V. Ramanan, and P. R. Brink. 1994a. Connexin37 forms high conductance gap junctions channels with subconductance state activity and selective dye and ionic permeabilities. Biophys. J. 66:1915–1928. 

- Veenstra, R. D., H. Z. Wang, E. Beyer, and P. R. Brink. 1994b. Selective dye and ionic permeability of gap junction channels formed by connexin45. Circ. Res. 75:483–490. 

- Wang, H. Z., and R. D. Veenstra. 1997. Monovalent ion selectivity sequences of the rat connexin43 gap junction channel. J. Gen. Physiol. 109:491–507. 

- White, T. W. 2002. Unique and redundant connexin contributions to lens development. Science. 295:319–320. 

- White, T. W., D. L. Paul, D. A. Goodenough, and R. Bruzzone. 1995. Functional analysis of selective interactions among rodent connexins. Mol. Biol. Cell. 6:459–470. 

- Yeager, M., and B. J. Nicholson. 1996. Structure of gap junction intercellular channels. Curr. Opin. Struct. Biol. 6:183–192. 

- Zhou, L., E. M. Kasperek, and B. J. Nicholson. 1999. Dissection of the molecular basis of pp60[v-src] induced gating of connexin43 gap junctions. J. Cell Biol. 144:1033–1045. 

Biophysical Journal 87(2) 958–973 

