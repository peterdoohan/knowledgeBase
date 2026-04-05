Resource 

## The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas 

## Graphical Abstract 

**==> picture [288 x 288] intentionally omitted <==**

## Authors 

Quanxin Wang, Song-Lin Ding, Yang Li, ..., Hongkui Zeng, Julie A. Harris, Lydia Ng 

## Correspondence 

julieha@alleninstitute.org (J.A.H.), lydian@alleninstitute.org (L.N.) 

## In Brief 

The Allen Mouse Brain CCF is an openly accessible, cellular level resolution 3D reference atlas for analysis, visualization, and integration of multimodal and multiscale datasets. 

## Highlights 

- d Created a 3D average template brain from 1,675 mice at 10mm voxel resolution 

- d Delineated 43 isocortical areas from multiple surface views using curved coordinates 

- d Delineated 329 subcortical areas, 8 ventricle structures, and 

- d The Allen CCF is open access and available with related tools at https://atlas.brain-map.org/ 

**==> picture [17 x 17] intentionally omitted <==**

Wang et al., 2020, Cell 181, 936–953 May 14, 2020 ª 2020 Elsevier Inc. https://doi.org/10.1016/j.cell.2020.04.007 

**ll** 

**ll** 

## Resource 

## The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas 

Quanxin Wang,[1,2] Song-Lin Ding,[1,2] Yang Li,[1,2] Josh Royall,[1] David Feng,[1,4] Phil Lesnar,[1] Nile Graddis,[1] Maitham Naeemi,[1] Benjamin Facer,[1] Anh Ho,[1] Tim Dolbeare,[1] Brandon Blanchard,[1,5] Nick Dee,[1] Wayne Wakeman,[1] Karla E. Hirokawa,[1] Aaron Szafer,[1,6] Susan M. Sunkin,[1] Seung Wook Oh,[1,7] Amy Bernard,[1] John W. Phillips,[1] Michael Hawrylycz,[1] Christof Koch,[1] Hongkui Zeng,[1] Julie A. Harris,[1,3,] * and Lydia Ng[1,3,8,] * 

1Allen Institute for Brain Science, Seattle, WA 98109, USA 

2These authors contributed equally 

3Senior author 

4Present address: Tableau Software, Seattle, WA 98103, USA 

5Present address: 343 Industries, Redmond, WA 98052, USA 

6Present address: Microsoft Corporation, Redmond, WA 98052, USA 

7Present address: MDimune, Seoul 04790, Korea 

8Lead Contact 

*Correspondence: julieha@alleninstitute.org (J.A.H.), lydian@alleninstitute.org (L.N.) https://doi.org/10.1016/j.cell.2020.04.007 

## SUMMARY 

Recent large-scale collaborations are generating major surveys of cell types and connections in the mouse brain, collecting large amounts of data across modalities, spatial scales, and brain areas. Successful integration of these data requires a standard 3D reference atlas. Here, we present the Allen Mouse Brain Common Coordinate Framework (CCFv3) as such a resource. We constructed an average template brain at 10 mm voxel resolution by interpolating high resolution in-plane serial two-photon tomography images with 100 mm z-sampling from 1,675 young adult C57BL/6J mice. Then, using multimodal reference data, we parcellated the entire brain directly in 3D, labeling every voxel with a brain structure spanning 43 isocortical areas and their layers, 329 subcortical gray matter structures, 81 fiber tracts, and 8 ventricular structures. CCFv3 can be used to analyze, visualize, and integrate multimodal and multiscale datasets in 3D and is openly accessible (https://atlas.brain-map.org/). 

## INTRODUCTION 

Modern advances in whole brain imaging techniques have made it essential that brain atlases keep pace with large-scale data collection. Digital three-dimensional (3D) atlases are in demand, having significant advantages over classic 2D plate-based atlases as anatomical frameworks for whole brain datasets. Both 2D and 3D reference atlases consist of two key separable and complementary components: (1) the reference brain and its image, and (2) the structural annotations that show how the brain is parcellated. A standard reference atlas should include additional critical features: a spatial coordinate system, ordered structure ontologies, and easy, interactive access to the atlas at multiple resolutions. 

The current standard 2D atlas annotations were drawn on images of a single reference brain sectioned in one plane, stained, and imaged with cellular resolution light microscopy (Ding et al., 2016; Dong, 2008; Paxinos and Franklin, 2012; Swanson, 2004). Conventionally, parcellation is based on cellular architecture revealed with histological stains (e.g., Nissl, AChE) and/or myelin architecture (e.g., Gallyas silver stain, myelin basic protein). 

Brain parcellation efforts also utilize differential gene expression, connectivity patterns, or functional properties between brain areas. Because each of these modalities may reveal unique characteristics of certain brain regions, when used together, they are expected to greatly improve structural delineations. However, no mammalian brain atlas has systematically combined modalities in a single integrated atlas. In the last decade, brain mapping projects have provided substantial new data revealing highly detailed cellular architecture, including gene expression (Lein et al., 2007; Ng et al., 2009), mesoscale connectivity (Oh et al., 2014; Zingg et al., 2014), and transgenic expression in Cre driver mice (Gong et al., 2007; Harris et al., 2014; Kim et al., 2017; Shima et al., 2016). To stay current, reference atlases should allow for modifications to parcellation schemes based on current knowledge. 

Standard 2D mouse brain reference atlases, e.g., the Allen Reference Atlas (ARA) (Dong, 2008) and the Mouse Brain in Stereotaxic Coordinates (MBSC) (Paxinos and Franklin, 2001, 2012), continue to serve important roles, but a digital 3D reference atlas is preferred for informatics-based workflows, data visualization, and integration across brains, labs, and data types. 

**==> picture [16 x 17] intentionally omitted <==**

936 Cell 181, 936–953, May 14, 2020 ª 2020 Elsevier Inc. 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [482 x 579] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Iteration<br>H<br>1mm<br>(a)<br>B C D<br>Dorsal  Anterior  F Lateral<br>E F G<br>J<br>K<br>I<br>Coronal  Sagittal  Horizontal<br>1mm<br>K K<br>H  Single Brain  I J K<br>400 m  300 m  800 m  600 m<br>Average Template<br>barrels in  barrelettes<br>SSp layer 4 in SPVI<br>barreloids<br>in VPM<br>**----- End of picture text -----**<br>


Figure 1. The 3D Average Mouse Brain Template (A) Evolution of the average template in a coronal plane in the building process. From left to right are the results from the 1[st] , 3[rd] , 5[th] , and 7[th] iteration, respectively. (B–D) Volume rendering (max intensity projection) of the average template in horizontal (B), coronal (C), and sagittal (D) views. Dotted red lines show the position of the virtual section views below in (E)–(G). 

(legend continued on next page) 

Cell 181, 936–953, May 14, 2020 937 

Resource 

## **ll** 

The Allen Mouse Brain Common Coordinate Framework (CCF) is a 3D reference atlas that has already undergone several revisions. The first version, CCFv1, was created to support whole brain gene expression mapping and searches (Lein et al., 2007). We converted a subset (n = �200) of the Nissl-based ARA 2D structure annotations to 3D, in one hemisphere, at low resolution (200 mm voxels). CCFv2 was introduced to support mapping and visualization of brain-wide mesoscale connectivity (Oh et al., 2014). It included many more structure annotations (n = 860) converted from the ARA, both hemispheres, and higher resolution voxels (100 mm). Despite these improvements, at least two major issues remained: (1) conversion of the coronally annotated 2D structures to 3D volumes resulted in irregular, non-biological borders and shapes when viewed in non-coronal planes, and (2) current large-scale data generation efforts, such as the BRAIN Initiative Cell Census Network (https://www.biccn.org), require a higher, cellular level resolution atlas (10–20 mm) (Ecker et al., 2017). 

To overcome these limitations, we created CCFv3. First, we generated a new 3D reference brain: a volumetric average template at 10 mm isotropic voxel resolution. Second, we comprehensively parcellated and annotated the entire average template brain directly in 3D space. To assist with accurate areal delineations, we compiled and curated multimodal reference datasets deformably registered to the average template brain. Reference data included histology stains, immunohistochemistry, transgene expression, in situ hybridization (ISH), and anterograde tracer connectivity experiments. CCFv3 is parcellated into 43 isocortical areas and their layers, 329 subcortical gray matter structures, 81 fiber tracts, and 8 ventricular structures (per hemisphere). Data and tools are accessible through our web portal (http://atlas.brain-map.org). 

## RESULTS 

## The Average Template 

The CCFv3 reference brain is a 3D spatial template constructed as a population average of 1,675 young adult mouse brains imaged using serial two photon tomography (STPT) for the Allen Mouse Brain Connectivity Atlas (Kuan et al., 2015; Oh et al., 2014; Ragan et al., 2012). The average was created from tissue autofluorescence detected in the red channel. Different formulations of an ‘‘average brain’’ could exist depending on the feature being averaged. For future leverage and integration with human atlases, we followed methods developed for a human MRIbased population average template (Fonov et al., 2011). To maximize input data and create a symmetrical atlas, each hemisphere was reflected across the midline, for a total of 3,350 image series (= 2 3 1,675 brains). STPT images were acquired at high resolution (x, y = 0.35 mm/pixel) every 100 mm through the anterior-posterior axis of the brain, then downsampled to 50, 25, and 10 mm in x-y axes. Slight offsets in the position where imaging starts for each brain provide sufficient coverage to allow 

interpolation along the z axis to obtain isotropic voxel resolution to 10 mm. Assuming uniform sampling along the z axis, each 10 mm is spanned by data from 335 hemispheres, a number comparable to Fonov et al. (2011). We started with a previous template (Kuan et al., 2015; Oh et al., 2014), adding more registered brains to create the new CCFv3 initial template. An iterative process (1) deformably registered each specimen to the template and averaged all specimens, and (2) computed the average deformation field over all specimens, then inverted and applied it to the average image created in (1). This resulted in a volume with an average unbiased shape and intensity used as the template in the next iteration. The algorithm continued until the difference between the mean magnitude of the average deformation field between iterations fell below a certain threshold and stabilized. Figure 1A illustrates the convergence to a sharp average image with evident anatomical details. For computational efficiency, the method was first applied at 50 mm resolution until convergence was attained, followed by processing at 25 mm, then 10 mm for the final 3D volume (Figures 1B–1G). The average template was matched in size and anterior-posterior extent to the ARA Nissl-stained specimen to retain integrity with the original coordinates and dependent informatic tools. The most rostral part of the main olfactory bulb and the most caudal parts of the medulla and cerebellum are excluded. At 10 mm voxel resolution, the average template contains �506 million voxels. Its dimensions are 1,320 (anterior to posterior, 13.2 mm) 3 1,140 (left to right, 11.4 mm) 3 800 voxels (dorsal to ventral, 8.0 mm). 

The final template contains many distinguishable, detailed, anatomical features (Figures 1H–1K). Intensity (contrast) levels appear to reflect differences in cell densities (see STAR Methods for details), with white and gray matter appearing at opposite ends of the intensity scale (dark, fiber tracts; light, gray matter). The whisker barrel fields in layer 4 of the primary somatosensory cortex (SSp-bfd) are much more evident in the template compared to a single specimen (Figure 1H). In the medullary spinal nucleus of the trigeminal, interpolar part (SPVI), the first brain location targeted by axons carrying sensory information from each whisker, it is difficult to identify the whisker barrelette formations using only background fluorescence in a single STPT coronal image, but, this structure also becomes clearly visible in the average template (Figure 1I, top versus bottom). Similarly, the related barreloids in the ventral posteromedial nucleus (VPM) of the thalamus (Figure 1J), cortical layers (Figures 1H and 1J), and other thalamic nuclei (Figures 1J and 1K) exemplify how the averaging process revealed anatomical structures. The average template provides resolution at cellular scale and is a suitable 3D reference brain for parcellation and annotation. 

## Structure Ontology 

Two major rodent brain ontologies are used today: (1) Rat Brain in Stereotaxic Coordinates (Paxinos and Watson, 2013), also used in the MBSC (Paxinos and Franklin, 2001, 2012), and (2) Brain Maps: Structure of the Rat Brain (Swanson, 2004, 2018). 

> (E–G) One virtual section of the average template volume in 3 planes: coronal (E), sagittal (F), and horizontal (G). 

(H–K) Zoom-in views of the boxed areas area in (A) and (E)–(G), respectively. Top panels are examples from a single STPT imaged specimen. Bottom panels show the average template. Many anatomical features are more salient in the average template than in any individual specimen. Scale bars, 1 mm (A–G), 0.4 mm (H), 0.3 mm (I), 0.8 mm (J), and 0.6 mm (K). 

938 Cell 181, 936–953, May 14, 2020 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [420 x 523] intentionally omitted <==**

Figure 2. Annotation Workflow for Building 3D Structures (A) For every brain structure, anatomists started by reviewing relevant data from multiple sources (see Table S3). Structures visible in the average template were drawn first. Dashed arrow indicates that the ISH data from the Allen Brain Atlas were consulted side by side with the template, unlike the other datasets that were registered and could be viewed as direct overlays of the average template for annotation. 

(B) Using a curated set of reference data, neuroanatomists labeled voxels that they determined belonged to each brain structure in coronal, sagittal, and horizontal plates at regularly spaced intervals, according to the size of the structure, directly on the average template using ITK-SNAP. Two neighboring structures are shown in magenta and green. 

(C) At the end of step (B), a 3D ‘‘weave’’ was produced (right) that was not yet smooth or filled in across all planes (sagittal view, middle). Structures were completed in 3D by skilled illustrators to produce a smooth final 3D volume (left). 

(legend continued on next page) 

Cell 181, 936–953, May 14, 2020 939 

Resource 

## **ll** 

While full structure names show major overlap between ontologies, abbreviations are quite different (e.g., primary visual cortex is ‘‘V1’’ in MBSC and ‘‘VISp’’ in the Swanson ontology). For CCFv3, we use the ARA ontology that followed Brain Maps, but adopt terms from the MBSC, or other publications, when structures were not present in the ARA ontology. Given these differences, users should carefully assess regions with respect to their own purposes (Table S1 compares ARA and MBSC terms). The ARA ontology is hierarchical (see also Figure S6A). At the top level (‘‘root’’), the brain is divided into gray matter (including cell groups and regions), fiber tracts (myelinated structures), and ventricular systems (spaces filled with brain fluid). Gray matter is sub-divided into 3 large regions (‘‘cerebrum,’’ ‘‘brain stem,’’ and ‘‘cerebellum’’), which are themselves organized into subregions with differing numbers of ‘‘leaves’’ in the hierarchical tree (Table S2). Similar structures are not always at the same hierarchical level. We also refer to 12 ‘‘major divisions’’ of the gray matter: isocortex, olfactory areas, hippocampal formation, cortical subplate, striatum, pallidum, thalamus, hypothalamus, midbrain, pons, medulla, and cerebellum, and 316 ‘‘summary structures’’: non-overlapping, finer divisions, independent of their exact depth in the tree (Table S2). 

The exact criteria used for determining boundaries varied depending on the specific structure, so we provide examples in the following sections to illustrate our approach. With the selected reference data registered and overlaid, structures were reconstructed directly in the average template using the 3D annotation software ITK-SNAP (http://www.itksnap.org/pmwiki/pmwiki.php) (Yushkevich et al., 2006). Neuroanatomists delineated each structure across coronal, sagittal, and horizontal planes at regular intervals, depending on the size and shape of the structure (Figure 2B). This ‘‘weaved’’ structure was filled in, refined, and smoothed by illustration specialists (Figure 2C) and then validated by the neuroanatomists. Once a critical number of 3D reconstructions were reached, individual and local structure groups were merged. After merging, minor overlaps and gaps were fixed, so that all voxels were assigned to a single brain structure (Figure 2D). A final evaluation was then performed by the neuroanatomists. This procedure was followed for delineation of cortical layers, subcortical gray matter structures, white matter fiber tracts, and ventricular structures, but not isocortical areas, which used a variant described next. We fully annotated the entire average template volume (i.e., no voxel is left unlabeled). 

## Parcellation: Isocortical Areas 

## Annotation Workflow and Reference Datasets 

Annotation of the average template brain was accomplished using a coordinated, iterative workflow (Figure 2). The first step for a given structure was review of previously published atlases and literature, visual analyses of the average template and the five types of multimodal reference datasets (Figures 2A and S1). Reference data were selected based on existing knowledge and new analyses for those that best revealed boundaries and layers of isocortical areas, subcortical structures, and fiber tracts. Data types included: (1) transgenic mouse data imaged with STPT (Madisen et al., 2010; Daigle et al., 2018; Gerfen et al., 2013; Gong et al., 2007; Harris et al., 2014, 2019; Shima et al., 2016); (2) axonal projection data from the Allen Mouse Connectivity Atlas (Harris et al., 2019; Martersteck et al., 2017; Oh et al., 2014); (3) immunohistochemical and (4) cytoarchitectural stains, including antibodies against NeuN, NF-160, SMI32, parvalbumin, SMI-99, and calbindin, as well as stains for DAPI, Nissl, and AChE; and (5) in situ hybridization (ISH) data from the Allen Mouse Brain Atlas (Ng et al., 2009, 2010). Datasets curated for each structure revealed highly coincident shapes, sizes, and borders. Occasionally, we encountered conflicting evidence that suggested small differences in border locations for a given structure. To deal with this rare situation, we re-assessed the multimodal datasets for quality (including registration results) and consulted additional mouse and rat atlases and literature to best integrate all the information into our final annotation. In no case did we see data that suggested orthogonal or perpendicular borders due to different datasets. Specific datasets used for the delineation of brain structures are listed in Table S3, which is searchable and contains links or file locations where images can be accessed and/or downloaded. 

The isocortex is a 3D sheet organized into layers where connections between the layers are typically perpendicular to the surface, suggesting a hypothetical columnar organization. Even though the mouse cortex is lissencephalic, its curvature makes it difficult to visualize along this theoretical dimension, as one ‘‘column’’ cuts through a variable number of coronal planes. So, we developed a curved cortical coordinate system to approximate the ‘‘vertical’’ direction of the sheet based on the geometry of the cortex. These curved coordinates enable the integration and aggregation of information in a columnar manner across datasets, facilitating analyses and parcellation of the cortex. 

The first step to create the curved coordinates was to draw the outside border of the entire isocortex. Although the boundaries between isocortex and its neighbors are mostly recognizable in the average template, manual delineation was facilitated by overlaying STPT images obtained from transgenic Cre driver mice (e.g., Calb1-T2A-dgCre and Fezf2-CreER) (Figures 3A– 3C). Calb1-T2A-dgCre shows enriched gene expression in the superficial layers of the entire isocortex, except for the ventral part of the retrosplenial area. Fezf2-CreER shows complementary expression in deep layers. In a coronal view, the isocortex is separable ventrally and laterally from the piriform area (PIR), where expression of both transgenes is absent (Figure 3A). In a sagittal view, it is separable from the postsubiculum (POST) and area prostriata (Apr) posteriorly, and anteroventrally from the PIR (Figure 3B). Horizontally, isocortex can be separated anteriorly from the main and accessory olfactory bulb (MOB and AOB), and posteriorly from the lateral entorhinal cortex (ENTl), which contains strong Fezf2-CreER and weak Calb1T2A-Cre expression (Figure 3C). 

(D) As more individual structures were completed, the next step was to ‘‘fit’’ them together, to not have unlabeled voxels (‘‘gaps’’) or voxels with multiple labels (‘‘overlaps’’). This was done by manual proof-reading. It was sometimes necessary to go back and review reference datasets to resolve discrepancies. 

(E) The voxel labels were finalized in one hemisphere and flipped to generate the symmetric CCFv3. 

940 Cell 181, 936–953, May 14, 2020 

## Resource 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [376 x 601] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Calb1-T2A-dgCre B C<br>Isocortex Fezf2-CreER MOB AOB Isocortex<br>Isocortex<br>APr<br>POST<br>PIR PIR<br>ENTl<br>D E F<br>D<br>M P<br>A L<br>V<br>1mm<br>G Chrna2-Cre_OE25Rorb-IRES2-Cre H 1 M 1 N 1 O<br>2/3 2/3 2/3<br>SSp-m 4 4 4<br>SSp-ul<br>SSp-ll SSp-n 5 5 5<br>6a<br>SSp-bfd 6a 6a<br>RSPd,v 6b 200�m 6b 6b<br>Average Template Calb1-T2A-dgCre Nr5a1-Cre<br>A VISp 1 P 1 Q 1 R<br>M 2/3 2/3 2/3<br>I Slc17a8-IRES2-CreAM projections J 4 4 4<br>5 5 5<br>6a 6a<br>6a<br>6b 6b<br>6b<br>Rbp4-Cre_KL100 Ntsr1-Cre_GN220 Ctgf-2A-dgCre<br>VISa VISa<br>RSPd<br>S<br>D<br>VISp M P<br>A L<br>V<br>Grp-Cre_KH288 K PL FRP L<br>VAL projections<br>MOs MOs<br>MOp SSp-m MOp SSp-m<br>SSp-ul SSp-ul<br>SSp-n<br>SSp-ll SSp-ll<br>SSp-bfd SSs<br>VISa<br>RSPd RSPd<br>VISp TEa<br>1mm<br>VISal<br>VISal<br>SSp-tr SSp-tr<br>SSp-tr<br>SSp-tr<br>VISpl<br>VISpl<br>VISrl<br>VISrl<br>VISam VISam<br>VISam<br>VISpor<br>VISpor<br>AUDpo<br>VISpm VISpm<br>VISpm<br>AUDd<br>SSp-un<br>SSp-un<br>RSPagl<br>RSPagl RSPagl<br>AUDp<br>AUDv<br>AUDp<br>VISli<br>VISli<br>VISl<br>VISl<br>RSPv<br>RSPv<br>ACAd<br>**----- End of picture text -----**<br>


(legend on next page) 

Cell 181, 936–953, May 14, 2020 941 

Resource 

## **ll** 

After delineating the entire isocortex in 3D, the outer surfaces of layer (L) 6b (bordering white matter) and L1 (bordering pial surface) were designated. Laplace’s equation was solved between these surfaces, resulting in intermediate equidistance fields (Figure 3D). Steepest descent paths, called streamlines, were computed through the equidistance fields from the pial surface to the white matter (Figures 3E and 3F) (Jones et al., 2000; Lee et al., 2011; Lerch et al., 2008). Analyses of the streamlines provides data on cortical geometry (e.g., radial orientation may reflect putative column orientation) (Figure S2A), and variation in thickness can be mapped across the cortical sheet (Figure S2B). 

We confirmed the streamlines reflect the true curvature of a vertical axis by comparing them with the topology of thick-tufted dendrites of L5 pyramidal neurons that extend to L1 (Figures S2E–S2V). L5 neurons were selectively labeled with Cre-dependent viral tracer injections into the Sim1-Cre_KJ18 driver line (Harris et al., 2019). In the nose region of primary somatosensory cortex (SSp-n), L5 apical dendrites cross several coronal planes in the anterior direction from the labeled cell bodies (Figures S2E–S2K), and, similarly, streamlines are slightly tilted anteriorly (Figures S2L–S2N). In the rostrolateral visual cortex (VISrl), streamlines are closer to upright (Figure S2A, green star), and L5 apical dendrites cross fewer coronal planes (Figure S2S, inset). In more anterior locations where the isocortical sheet curves ventrally, such as the secondary motor cortex (MOs) (Figure S2C, orange star), streamlines become almost orthogonal to the coronal plane, looking very like the apical dendrites of Sim1Cre[+] neurons in MOs when sectioned coronally (Figure S2U, inset). In fact, it can be hard to visualize L5 apical tufts in single coronal sections but reorienting these data by ‘‘unbending’’ the curved cortical sheet, so streamlines point up, reveals the stereotypical profile of the Sim1-Cre[+] apical dendrites reaching to L1 (Figures S2O–S2V). 

Using the computed streamlines, information at different cortical depths can be aggregated and projected to the pial surface. Various 2D views can then be created from 3D, and information can also be translated back to 3D. For example, streamlines enable visualization of the entire cortical sheet in 2D (i.e., a virtual ‘‘flatmap’’) (Figures S2A–S2D) (Fischl et al., 1999; Harris 

et al., 2019). We used multiple 2D surface views of the 3D average template overlaid with registered reference datasets for parcellation. Surface views were generated by projecting the highest intensity voxel along a streamline to its surface voxel counterpart. Given that various views can provide additional information across a rounded surface, we used seven angles (top, bottom, medial, side, rotated, front, and back). Example datasets mapped onto the top and lateral views are shown in Figures 3G–3L and S3, because these two angles contain most isocortical areas in a single image, but all surface views generated for the transgenic and connectivity data used to delineate isocortex regions are available for download. We drew borders directly on these 2D views, integrating data as described next, and then transformed the surface drawings into 3D volumes by extrapolating from the surface along the streamlines. 

In the top view of the average template (Figure 3G), distinct bright domains are obvious (e.g., barrel fields) that are unambiguously anatomical structures. Based on the location and shape of these structures, we putatively assigned them as primary visual, primary auditory, primary somatosensory, and retrosplenial areas. Boundaries were confirmed by overlaying registered reference datasets on the average template. Rorb-IRES2-Cre, a marker of layer 4 neurons densest in primary sensory areas, affirmed the putative borders of the three primary sensory regions (Figure 3H, red). Transgene expression in the Chrna2-Cre_OE25 line is enriched in retrosplenial areas (Figure 3H, green), and the registered spatial pattern aligned well with the putative border drawn from the average template. Additional datasets helped finalize the borders and subdivisions within them (Figure S3). These four major cortical regions then served as landmarks for the remaining isocortex. 

Unlike the intrinsically bright areas, regions between landmarks are not visible using only contrast in the average template. For higher order (secondary) visual areas, we generated visuotopic connectivity maps and a virtual callosal connectivity map (Figure 3I). By overlaying these on the average template, we identified nine higher visual areas based on their complete visual field maps and fixed spatial relationships with callosal labeling patterns (Wang and Burkhalter, 2007). Five of these areas (anterolateral, rostrolateral, anterior, anteromedial, and 

Figure 3. Delineating the Isocortex 

(A–C) The isocortex was defined in part by overlaying registered STPT images from the transgenic lines Calb1-T2A-dgCre (red) and Fezf2-CreER (false-colored green) shown here in coronal (A), sagittal (B), and horizontal (C) planes. 

(D) Equidistance fields solved with Laplace’s equation are shown in jet color map. 

(E) Subsampled and randomly colored streamlines descend from the cortical surface to layer 6 in a single coronal section. (F) A 3D projection shows the curved cortical streamlines in a dorsolateral view. 

(G) A (top) cortical surface view of the average template constructed using the maximum intensity projection of voxels along the streamlines to the surface. (H) Top surface view showing reporter expression from transgenic lines Rorb-IRES2-Cre (red) and Chrna2-Cre_OE25 (false-colored green) overlaid on the average template. These lines reveal the shape and size of primary sensory and retrosplenial areas, marked with solid white lines. 

(I) Higher visual areas were delineated by overlaying visuotopic projection maps (cyan, pink, and blue representing nasal, temporal, and lower visual fields, respectively) and virtual callosal labeling (green) to the average template. 

(J) Transgenic line data (Slc17a8-IRES-Cre, red) and cortical projections from the thalamic nucleus AM (green) assisted delineation of RSPagl. (K) Transgenic line data (Grp-Cre_KH288, red) and cortical projections from the thalamic nucleus VAL (green) assisted delineation of MOp and MOs. (L) 31 isocortical areas are visible and were delineated in the top surface view. Solid white lines represent areal borders. 

(M) Contrast features inherent to the average template were useful for identifying individual cortical layers. A single coronal plane is shown at the level of SSp-bfd. (N–R) STPT images of Ai14 reporter expression in layer-selective transgenic mouse lines; Calb1-T2A-dgCre for L2/3 (N), Nr5a1-Cre for L4 (O), Rbp4-Cre_KL100 for L5 (P), Ntsr1-Cre_GN220 for L6a (Q), and Ctgf-2A-dgCre for L6b (R). 

(S) Dorsolateral 3D view of the parcellated isocortex intersected with the cortical layers (white solid lines in cut-away). Structure abbreviations in Table S2. A, anterior; P, posterior; M, medial; L, lateral; D, dorsal; V, ventral. Scale bars, 1 mm (A–E) and (G–L), 200 mm (M–R). 

942 Cell 181, 936–953, May 14, 2020 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [456 x 600] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>I P A<br>CB<br>ISOCORTEX HPF MB IPR IPDM<br>IPDL<br>STR IPRL<br>TH<br>MY<br>P<br>PAL IPL<br>OLF<br>HY<br>IPN IPI<br>IPC<br>C midline G K L M IPR<br>IPDM IPRL<br>IPDM<br>IPDM IPDM IPR<br>IPDL IPDL IPDL<br>IPA IPA IPA IPA IPDL<br>*<br>IPI * IPI* * *<br>IPL IPL<br>IPL IPL<br>Nissl IPC [IPI] Slc17a8-iCre IPC IPC PG IPC PG IPC IPI<br>D H N O P<br>IPR<br>IPDM IPDM IPDM IPDM IPRL<br>IPR<br>IPDL<br>IPDL IPDL<br>IPA IPA IPA<br>IPA IPDL<br>IPI IPI<br>IPL IPL<br>Calb1SMI-99 IPC  [IPI] IPL Kcng4-Cre IPC Slc17a8Kcng4 IPC IPL IPC IPC IPI<br>E I Q R S<br>IPR<br>IPDM IPRL<br>IPDM<br>IPDM IPDM IPR<br>IPDL<br>IPA IPDL IPA IPDL IPA IPA IPDL<br>IPI IPI IPI<br>IPL IPL IPL<br>PvalbSMI-32 IPC CS projections IPC MHCS IPC IPL IPC IPC IPI<br>F J T U V<br>IPRL<br>IPDM IPDM IPDM<br>IPDL IPR<br>IPA IPA IPDL IPA IPA<br>IPDL IPR<br>IPL<br>IPI IPI<br>IPC IPI IPL IPC IPI<br>IPC<br>IPL IPL<br>NF-160NeuN IPC MH projections IPC 200 �m<br>IPDM<br>IPDL<br>**----- End of picture text -----**<br>


(legend on next page) 

Cell 181, 936–953, May 14, 2020 943 

Resource 

## **ll** 

posteromedial), were also recognizable for having enriched expression in line Glt25d2-Cre_NF107 (Figure S3C, in red) and axonal projections from the lateral dorsal nucleus of thalamus (Figure S3D, in green). 

To parcellate the remaining isocortical areas, we continued to use both transgenic and connectivity datasets registered to the average template, as well as consulting histological reference stains, published atlases, and literature. In the top view, we further delineated dorsal (Figures S3D and S3E), agranular (Figures 3J and S3F), and ventral retrosplenial areas (Figures S3F and S3G), primary and secondary motor areas (Figure 3K), the dorsal part of the anterior cingulate area (Figure S3H, in green), and the prelimbic area (Figure S3F, in green). Like the top view, the lateral view of the template also showed the primary sensory areas as inherently brighter than surrounding structures (Figure S3I). Their shapes, sizes, and locations were similarly confirmed through registration and visualization of transgenic expression data. In addition to reconstructing areas that were at least in part visible in the top view, the lateral view enabled additional areas to be parcellated (details and examples in the Figure S3 legend). We reconstructed 31 isocortical areas in the top view (Figure 3L) and 33 in the lateral view (Figure S3T). Using all surface views, the mouse isocortex was parcellated into 43 total areas. 

## Parcellation: Isocortical Layers 

Next, we delineated the borders between isocortical layers primarily using differential contrast features in the average template itself and Cre driver lines with layer-selective reporter expression (Figures 3M–3S) (Gerfen et al., 2013; Harris et al., 2014, 2019), as well as consulting histology data and publications. In the average template (Figure 3M), L1 is brighter at the cortical surface, getting 

darker near the transition to L2/3. L4 is generally brighter than L2/ L3 and L5, while L6 is generally darker than L5, but brighter than the fiber tracts beneath the isocortex. L6a and 6b are not readily distinguishable in the average template. L6b, located directly above the white matter, is very thin (�20–30 mm, 2–3 voxels), so we relied on the Ctgf-2A-dgCre line with enriched expression in L6b neurons (Figure 3R). L1, 2/3, 5, 6a, and 6b were delineated for all isocortical areas using multiple Cre lines for each layer, registered and overlaid on the average template. L4 is not present (or very thin) in the prelimbic, infralimbic, orbital, agranular insular, motor, anterior cingulate, retrosplenial, perirhinal, and ectorhinal areas. Delineated layers were intersected with the 43 cortical areas, resulting in a total of 242 structure volumes (Figure 3S). 

## Parcellation: Subcortical Gray Matter Structures 

We delineated an additional 329 gray matter structures outside the isocortex, covering the other 11 major brain divisions. For each structure, we curated a unique combination of experiments extracted from the complete set of histological, immunohistochemical, in situ hybridization, transgenic driver line, and connectivity datasets that were most consistent with each other to define putative borders (Table S3). Contrast features inherent in the average template were always used when present and informative. Each subcortical structure was concurrently delineated through coronal, sagittal, and horizontal planes of the average template at 10 mm voxel resolution to create smooth 3D volumes. We present only one example out of 329, the interpeduncular nucleus in the midbrain (IPN) (Figure 4A). First, we comprehensively reviewed previous parcellations in other atlases and the literature on IPN anatomy. IPN was previously delineated into seven (Paxinos and Franklin, 2012) or eight 

Figure 4. Delineating a Subcortical Gray Matter Structure, the Interpeduncular Nucleus (IPN) (A) A parasagittal view of the whole parcellated CCFv3 shows the location of IPN in the midbrain. Visible major divisions are labeled. 

(B) The final smooth 3D volume shows eight IPN subdivisions (R, rostral; C, caudal; A, apical; L, lateral; I, intermediate; DM, dorsomedial; DL, dorsolateral; RL, rostrolateral). (C) Coronal section image from a Nissl-stained brain at the approximate center of the IPN. Nissl reveals putative IPN subdivisions as regions containing neurons of different sizes and densities. 

(D–F) Coronal section images of the IPN from three brains immunohistochemically stained with a pair of antibodies as indicated. (D) Antibody labeling for calbindin D28K (Calb1, green) reveals very dense terminal fibers in IPL. Myelin basic protein is labeled with the SMI-99 antibody (red). There are relatively more myelinated axons visible in IPC and IPI, compared to the other subdivisions. (E) Antibody labeling for parvalbumin (Pvalb, green) shows spatial restriction of Pvalb[+] neurons to putative IPL and IPR (not shown). Neurofilament-H is labeled with the SMI-32 antibody (red) and is notably strongest in IPL. (F) Antibody labeling for NeuN (in red) also reveals sub-regional differences in neuronal densities; dense nuclei in IPA, IPDM, and IPR (not shown), moderate in IPC and IPL, sparse in IPI and IPDL. (G and H) Coronal STPT images of tdTomato reporter expression in two Cre driver transgenic lines. Slc7a8-iCre (G) is expressed at high levels in putative IPL and IPC. Kcng4-Cre (H) is similarly expressed at high levels in IPL. (I and J) Coronal STPT images of axonal projections labeled following tracer injections into afferent source areas to the IPN. (I) Projections from the superior central nucleus of the raphe (CS) terminate most densely in IPC and IPI. (J) Projections from the medial habenula (MH) to the IPN terminate with high density in putative IPL and moderate density in IPA, IPDL, and IPDM. (K–M) Virtual single plane sections in coronal (K), sagittal (L), and horizontal(M) slices of the average template through the IPN. Differential contrast features also reveal many putative IPN subdivisions. White matter and cell sparse regions appear dark and the gray matter bright. IPC is visible in all panels as a very bright region ventral to IPA and IPR, and just dorsal to the pontine gray (PG). IPR is also visible as a bright distinctive shape anterior to IPA (see sagittal section in L). IPA is clearly separated from IPC by a darker, cell sparse, region (* in L). IPL is also a relatively brighter shape, located lateral to IPI (K,M) and ventral to IPDL (K). IPI is a thin bright strip between IPC and IPL, separated from these two subdivisions via darker regions (* in K and M). IPDM (seen in K and L) is dorsal and medial to IPDL, dorsal and lateral to IPA, and posterior to IPR. IPDL (seen in K and M) is also lateral to IPA and IPR and above IPI and IPC. (N–P) STPT image series from the transgenic Cre line experiments in (G) and (H) registered to and overlaid on the average template provided critical assistance in border delineations, shown here in virtual coronal (N), sagittal (O), and horizontal (P) slicing planes. (Q–S) STPT image series from the two anterograde tracer datasets registered to and visualized in the average template volume provided critical assistance in border delineations, shown here in virtual coronal (Q), sagittal (R), and horizontal (S) slicing planes. (T–V) Integrating the information from the above multimodal reference data, the IPN was divided into eight sub-regions, shown here in coronal (T), sagittal (U), and horizontal (V) planes. Structure abbreviations in Table S2. Scale bar, 200 mm (C–V). 

944 Cell 181, 936–953, May 14, 2020 

**ll** 

## Resource 

(Quina et al., 2017) subdivisions based on cytoarchitecture, transgenic, and connectivity data. It was not sub-divided in the ARA (Dong, 2008). We also delineated eight IPN subdivisions in CCFv3 (Figure 4B) using a combination of cytoarchitecture (Nissl) (Figure 4C), antibody staining (Figures 4D-4F), transgene expression (Figures 4G–4H), axonal projections to IPN labeled via anterograde tracing (Figures 4I–4J), and the average template itself (Figures 4K–4M). We reviewed all the high resolution 2D image data to assist in discovering and determining the locations, shapes, and contours of regions in coronal planes, and we overlaid the registered image data (downsampled to 10 mm) on the average template for viewing and drawing in the three orthogonal planes (Figures 4N–4S). Details are provided in the Figure 4 legend. 

Each structure was pursued in this way, with data analyses, drawing, and merging of structure groups as described above (Figure 2). Most voxels in the average template volume were labeled after parcellating the 329 subcortical gray matter structures. However, some gaps in the gray matter (i.e., unlabeled voxels) remained. Based on the specific location within the brain, these voxels were assigned to one of the 11 major brain regions (as part of a ‘‘parent’’ structure). For example, after delineating the more than 40 hypothalamic nuclei, there were gaps between regions that did not clearly belong to any of the neighboring annotations (e.g., see light pink color around DMH, VMH, TU, and LHA in Figure S7B). We labeled such voxels that were located between other regions with the appropriate parent structure (e.g., ‘‘hypothalamus’’). 

## Parcellation: Fiber Tracts 

We delineated white matter fiber tracts throughout the entire brain volume (Figures 5A and 5B) primarily using inherent contrast features in the average template supported by two types of reference data: anterograde tracing and antibody staining. Some white matter bundles are obviously distinguishable from surrounding gray matter structures, because the axons contained within them are highly fasciculated, traveling in the same direction at these locations. In these types of tracts, contours and trajectories were readily defined by comparing the average template with corresponding anterograde tracing data that directly labels the axons making up these tracts. As an example, we show a set of three related tracts all originating from the medial mammillary nucleus (MM) (Figures 5C and 5D): the principal mammillary tract (pm), most proximal to MM, which splits to form the mammillotegmental tract (mtg) and the mammillothalamic tract (mtt). Axonal tracing data from the Allen Mouse Connectivity Atlas shows the mtt travels anteriorly to innervate thalamic regions, e.g., anteroventral (AV) and anteromedial (AM) nuclei (Figures 5F and 5G), whereas the mtg travels posteriorly to innervate the midbrain ventral tegmental nucleus (VTN) (Figures 5H and 5I). The location, shape, size, and trajectories of these three tracts can thus be accurately delineated by comparing the STPT images of labeled axons originating from MM in the coronal plane with the average template (where the tracts are dark in appearance, Figures 5J–5O). Contours of these fiber tracts were drawn, then adjusted and smoothed iteratively on the average template in coronal, sagittal, and horizontal planes to build coherent 3D volumes. Other examples of ‘‘simple’’ fiber tracts include the anterior commissure (ac), 

fornix (fx), and fasciculus retroflexus (fr, see labels in Figure 5N). Most fiber tracts were more complicated. More commonly, fiber tracts adjoin, merge, or intersect other bundles and/or portions of gray matter structures at different locations, leading to different intensities along their complete paths. For these structures, we used additional reference data to more accurately delineate boundaries and trajectories, e.g., antibody staining for parvalbumin (Pvalb) which reveals clear fiber orientation patterns for tracts such as the medial lemniscus, as described for rat (Celio, 1990; Endo et al., 1986), see also CCF technical documentation (http://atlas.brain-map.org/). Applying these methods and processes for simple and complicated white matter, we reconstructed 81 fiber tracts throughout the mouse brain in 3D (Table S2). 

## Parcellation: Ventricular Structures 

The ventricular system includes the lateral ventricle, third ventricle, cerebral aqueduct, fourth ventricle, and central canal of the lower medulla, as well as associated ventricular recesses and choroid plexuses. We delineated these structures in 3D based mainly on inherent contrast in the average template, paired with corresponding Nissl-stained sections (Figure S4). In the template, ventricles, like many white matter tracts, have a very dark appearance (Figures S4D–S4H). In Nissl-stained sections, however, the shape and size of ventricular structures and choroid plexuses are readily distinguishable from fiber tracts (Figures S4I–S4M). The contours of these structures were also delineated using specific transgenic lines that label the ependymal epithelia (e.g., Slc17a8-IRES2-Cre) (Figures S4N-S4R) and/ or choroid plexuses (e.g., Foxp2-IRES-Cre, not shown). One notable observation is that the cerebral aqueduct, at the level of the inferior colliculus, appears more ventricle- than aqueduct-like (Figure S4C). As described for fiber tracts and subcortical gray matter structures, the adjustment and smoothing of these structures were done iteratively in coronal, sagittal, and horizontal planes to build a 3D volume. We reconstructed 8 ventricles and associated structures. 

## Structures Added to CCFv3 

While manually inspecting and curating the multimodal reference data, we found evidence to support the addition of 36 subcortical gray matter structures to the ARA/CCFv3 ontology. Most (n = 27) already exist in the MBSC ontology and atlas, and we were able to identify enough reference data to support adding these delineations in CCFv3. However, several structures are unique to CCFv3 over other reference atlases (Table S1), although all were previously described in the literature. For example, the IPRL subdivision of the IPN (Figure 4) described above is a new CCFv3 structure. We also further parcellated the dorsal part of the lateral geniculate complex (LGd) into three subdivisions not previously annotated in ARA or MBSC ontologies, based on anatomical features in the template, anterograde tracing data from retinal ganglion cell types, and previous publications: shell (LGd-sh), core (LG-co), and ipsilateral zone (LG-ip) (Figure S5) (Grubb and Thompson, 2004; Huberman et al., 2009; Kay et al., 2011; Kerschensteiner and Guido, 2017; Martersteck et al., 2017; Rivlin-Etzion et al., 2011). Other newly delineated gray matter structures include the hippocampoamygdalar 

**==> picture [46 x 35] intentionally omitted <==**

Cell 181, 936–953, May 14, 2020 945 

**ll** 

Resource 

**==> picture [481 x 368] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>scwm<br>cing AM mtg VTN<br>cc mtt<br>onl<br>mcp<br>icp<br>pm<br>lotg arb D opt MM<br>cst<br>A P A<br>D F G E I H E J M<br>VTN<br>AM mtg mtg mtg<br>pm pm<br>mtt<br>pm pm<br>MM<br>F G K N<br>fr<br>AV<br>fx mtt<br>AM mtt mtt ac<br>H I L O<br>mtg<br>VTN<br>mtg<br>mtg<br>800 �m<br>**----- End of picture text -----**<br>


Figure 5. Delineating Mammillary-Related Fiber Tracts 

(A and B) Dorsal (A) and sagittal (B) views of all white matter tracts reconstructed in 3D. Some major tracts visible in these views are labeled (onl, olfactory nerve layer; lotg, lateral olfactory tract; cc, corpus callosum; cing, cingulum bundle; scwm, supracallosal cerebral white matter; arb, arbor vitae; opt, optic tract; mcp, middle cerebellar peduncle; icp, inferior cerebellar peduncle; cst, corticospinal tract). (C) The final 3D structure of three mammillary related fiber tracts near the midline are shown after removing overlying structures (pm, principal mammillary tract; mtt, mammillothalamic tract; mtg, mammillotegmental tract). 

(D) Sagittal view of the maximum intensity projection of fluorescently labeled MM axons. 

(E–I) STPT images show the locations of fiber tracts and their targets at the five coronal levels indicated by the dashed lines in (D). (J–O) Virtual coronal (J–L) and sagittal (M–O) sections of the average template. Coronal sections are matched to STPT images on the left (E, G, and I). Differential contrast features reveal other putative fiber tracts (dark), e.g., the anterior commissure (ac), fornix (fx), and fasciculus retroflexus (fr), indicated in (N). Integration of these data enabled the 3D reconstruction of tracts directly on the template volume. Scale bar, 800 mm (D–O). 

transition area, prosubiculum, and area prostriata (Ding, 2013; Ding et al., 2019; Lu et al., 2020). 

We also identified and added four fiber tracts not in the previous ARA and MBSC: the optic and auditory radiations, the body of the corpus callosum (ccb), and the supra-callosal cerebral white matter (scwm) (Figures 6A–6C). Cortical callosal projections make up a fiber bundle that is generally labeled as a single tract, the corpus callosum (cc) (Dong, 2008; Paxinos and Franklin, 2012). However, visual inspection of contralateral axonal projections labeled from a comprehensive set of cortical areas revealed that these cortical axons do not occupy the entire white matter region beneath the isocortex. Labeled callosal 

axons are instead concentrated in the mid-to-deep portion of the white matter, in both hemispheres, leaving a clear gap between this callosal bundle and the overlying isocortex (Figures 6D–6F). In contrast, we observed that thalamocortical axons appear to be layered above the callosal bundles, just beneath overlying isocortex (Figures 6G–6I). Based on this striking lamination in the white matter (i.e., separate callosal and thalamocortical axon paths), we delineated these as two separate structures, the cc and scwm. Interestingly, corticothalamic projection fibers appear to first travel in the scwm and then penetrate the callosal bundle before they innervate subcortical targets (not shown). Therefore, the cc is mainly composed of the cortical 

946 Cell 181, 936–953, May 14, 2020 

**ll** 

## Resource 

**==> picture [159 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
A P<br>A<br>ccb<br>fp<br>ccg<br>fa fa<br>ee<br>ccs<br>**----- End of picture text -----**<br>


**==> picture [159 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
B P<br>A<br>cing<br>cing scwm<br>**----- End of picture text -----**<br>


**==> picture [161 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
C<br>cing<br>scwm<br>ccb<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [476 x 479] intentionally omitted <==**

**----- Start of picture text -----**<br>
D SSp-n projections G AM projections D’ G’<br>scwm<br>scwm<br>cc<br>cc<br>cc<br>E SSp-bfd projections H AV projections E’ H’<br>cing<br>cing<br>cc<br>cc<br>cc<br>F VISp projections I LD projections F’ I’<br>scwm<br>scwm<br>cc<br>cc<br>cc<br>500 �m 50 �m<br>**----- End of picture text -----**<br>


(legend on next page) 

Cell 181, 936–953, May 14, 2020 947 

Resource 

## **ll** 

commissural fibers that run between the two hemispheres and part of the cortico-subcortical fibers. The scwm mostly consists of ipsilateral thalamocortical projection fibers, including the optic radiation (or) and cingulum bundle (cing) (Figures 6B and 6C), as well as the auditory radiation and part of the cortico-subcor- 

## CCF Applications and Resources 

We developed web applications for exploring CCFv3 in 2D and 3D (http://atlas.brain-map.org). Our interactive Atlas Viewer (http://atlas.brain-map.org/atlas?atlas=602630314) provides 2D visualization and linked browsing of coronal average template sections overlaid with corresponding structure annotations, like a conventional 2D reference atlas (Figures S6A– S6C). Notably, the Atlas Viewer can also be used to compare our anatomists’ delineations of the average template side-byside with most of the multimodal reference datasets. Exceptions include the Allen Brain Atlas (ABA) ISH data, because these datasets were not registered directly to CCFv3, and a few transgenic line experiments currently available only via download. Using Table S3, users can identify experiments of interest for a given structure and follow the links provided to navigate to these datasets individually. For example, clicking on the link for a connectivity experiment will open a Mouse Connectivity Atlas experiment page. There, one can open the high resolution image viewer (a box with arrow icon) and click on the key icon to show the reference atlas. Turning on this functionality changes the display into a side-by-side split window with the atlas image on the left and the data image on the right. The two views can be aligned using the ‘‘sync’’ feature (Figure S6D). The Experiment Image Viewer also provides the ability to view and navigate multiple datasets in a single window to compare different expression or connectivity patterns from multiple experiments. For example, one can view the histological reference stains by selecting and viewing all experiments at this link (http://connectivity. brain-map.org/static/referencedata), then adding and ‘‘syncing’’ with the 3D coronal atlas (Figures S6E–S6I). The Allen Brain Explorer (beta) application enables 3D visualization of CCFv3 structures (http://connectivity.brain-map.org/3d-viewer?v=1). It supports linked browsing and visualization of structures of interest in the CCFv3 ontology tree or loading of 3D models for different sets of structures (e.g., ‘‘major divisions’’ or ‘‘fine divisions’’). 

The Allen Brain Map portal hosts downloads through our web Application Programming Interface (API; http://help.brain-map. org/display/mouseconnectivity/API) and the Allen Software Development Kit (AllenSDK; https://allensdk.readthedocs.io/en/ 

latest/reference_space.html). The AllenSDK provides, in addition to data access and caching, a thoroughly documented and actively maintained open source library of tools for using CCFv3 annotations in concert with registered data. The API and AllenSDK together support cross-platform, public access to the CCFv3 ontology, template, and annotation volumes (at 10, 25, 50, and 100 mm isotropic resolution) along with the code and documentation required to use the CCFv3 in research projects. 

To demonstrate potential uses of the CCF and Allen SDK, we developed two applications using image series already registered to the CCF: reverse mapping and volume estimation. Above, we described that data used to assist with parcellations were warped and downsampled to fit into the average template volume (Figures 7A–7C). However, the reverse mapping (i.e., visualizing atlas annotations in the original image space) is also possible. We used the AllenSDK to access CCFv3, our STPT image data, and original transform parameters following deformable registration to the CCF and applied the inverted deformation field output from the registration process to warp the CCF to the images (Figures 7D–7J). Using the deformation fields also enabled us to compute brain structure volumes for the population of mice used to create the average template. Note that deformably mapping data to a template does not preserve distance relationships, and so measurements like distance and volume need to be done on the original specimen space. The population used to create the average template consists of 1,675 brains (n = 1,051 males: 621 females), with a mean age and SD of P77 ± 10.7 days. First, to calculate whole brain volumes for each brain, we generated a voxel mask for the entire average template volume. Then, we applied a marching cubes algorithm to find the corresponding surface mesh of this mask. Deformation fields were again applied in reverse to map the whole brain surface mesh back to each individual brain’s original shape and size (Figure 7K). Volumes ranged from 359–545 mm[3] , with a mean and SD of 435 ± 23.5 mm[3] (Figure 7L). Thus, most individual whole brain volumes are within �11% of the mean, with a coefficient of variation (CoV) = 5.4%. We did not observe a significant difference between males and females (434.24 ± 22.94 versus 437.07 ± 24.41mm[3] ,respectively). Note themean volume is �15% smaller than the CCFv3 average template (435 versus 506 mm[3] ). This is due to our first version template (Kuan et al., 2015) that intentionally matched the size and orientation of the ARA Nissl-stained brain specimen. Because this template initialized the CCFv3 average, the size and shape were also inherited. Notably, the unfixed fresh-frozen ARA specimen is closer in size to brains imaged in vivo (e.g., 506.9 ± 11.5 mm[3] ) (Ma et al., 2008) compared 

Figure 6. Delineating the Supracallosal White Matter (scwm) 

(A and B) Angled lateral views of the reconstructed white matter tracts located just below the isocortex. (A) The corpus callosum (cc) consists of six substructures (ccg, genu; ccb, body; ccs, splenium; fa, anterior forceps; ee, extreme capsule; fp, posterior forceps). (B) White matter tracts layered above the cc, but below the isocortex, are colored (scwm, cing, cingulum bundle). 

(C) A virtual coronal section of the average template (at the approximate anterior-posterior midpoint of the white matter shown in B). (D–F) Coronal STPT images at three locations along the anterior-posterior axis show axonal projections labeled following tracer injections into three cortical areas (SSp-n, primary somatosensory area, nose [D]; SSp-bfd, primary somatosensory area, barrel field [E]; VISp, primary visual area [F]). Callosal projection fibers are identified as those in the white matter below isocortex traveling toward the midline. 

(G–I) Coronal STPT images at three locations along the anterior-posterior axis show axonal projections labeled following tracer injections into three thalamic source areas (AM, anteromedial nucleus [G]; AV, anteroventral nucleus [H]; LD, laterodorsal nucleus [I]). Thalamocortical projection fibers are localized above the callosal fibers, in the gap between cc and isocortex. (D[0] –I[0] ) Enlarged view of the areas within the dashed line boxes (D–I). The white dashed lines in (D[0] )–(I[0] ) indicate white matter borders. Scale bars, 500 mm (D–I), 50 mm (D[0] –I[0] ). 

948 Cell 181, 936–953, May 14, 2020 

## Resource 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [420 x 392] intentionally omitted <==**

**----- Start of picture text -----**<br>
Image Series Registration  to  CCF CCF Annotations Mapped Back  to  Image Series<br>A B C G F E<br>D Deformation Field Output<br>� x � y � z<br>- 400 �m 0 + 400 �m<br>Original Section Image Atlas Mapped to Section Image Structure Boundaries<br>H I J<br>LGd<br>APN<br>LGv<br>Axons labeled from VISp<br>K 3D renderings  L Whole Brain<br>140<br>120<br>100<br>80<br>60<br>40 CCFv3<br>20<br>0<br>350 375 400 425 450 475 500 525 550<br>CCFv3 Individual 1 Individual 2 Volume, mm [3]<br>Count<br>**----- End of picture text -----**<br>


Figure 7. Registration to CCFv3 Enables Downstream Applications 

(A–G) For many data analyses and visualizations, individual image series are registered to the CCF. Imaged brain sections (A) are registered to the average template (B), resulting in a field of deformation vectors (‘‘deformation field’’) (D) that map points from the raw image space to our reference space (C). For other analyses, the reverse mapping (CCF annotations pushed onto individual brains) may be appropriate (E–G). Here, using the deformation fields (D), annotations from our atlas (E) can be mapped back to the raw image space (F) to produce annotated image sections in the original image space (G). (H–J) An example of the reverse mapping is shown for a viral tracing experiment from the Allen Mouse Brain Connectivity Atlas acquired using STPT imaging. The original image section (H) is annotated by warping the atlas onto the image (I) using the deformation field output from registration. In this image (I), all structure annotations are overlaid onto the STPT image. However, individual structure boundaries can also be selectively viewed/mapped on the images using code we developed (J). 

(K) 3D renderings of the CCFv3 average template and two individual brains after applying their deformation fields in reverse to a whole brain surface mask. CCFv3 is shown on the left; two examples of individual brains are shown on the right, without (top) and with (bottom) cortical area parcellations. (L) Whole brain volumes were measured using the individual deformation fields for each of the 1,675 mice (gray line) used to create the average template, shown in the frequency histogram. The volume of the CCFv3 average template is indicated with the black line (511 mm[3] ). 

to the perfusion-fixed brains imaged by STPT. We also calculated structure volumes and descriptive statistics across the entire CCFv3 ontology using the approach described for the whole brain (Table S4). Major division volumes were not any more variable than the whole brain (CoVs = 5.4% to 7%), whereas variation was larger (10.7%) for the finest divisions. The largest variations (87%) were noted in structures with very high surface area to volume ratios (i.e., long thin structures like layer 6b). These measure- 

ments rely on the specimen deformation fields, so variations in individual volumes are a function of both underlying biological variability and variability in the registration process. 

## DISCUSSION 

The CCFv3 reference brain offers several improvements over previous volumetric templates. First, we averaged substantially more 

Cell 181, 936–953, May 14, 2020 949 

Resource 

## **ll** 

individuals than MRI-based templates (n = 1,675 versus 4 to 40 brains) (Ali et al., 2005; Bock et al., 2006; Chen et al., 2006; Dorr et al., 2008; Kovacevic� et al., 2005; Ma et al., 2005; Sharief et al., 2008). Acquiring whole brain high resolution images for so many specimens combined with iterations of registration and averaging resulted in very good signal-to-noise, revealing anatomical details not readily discernable in any single specimen. Second, CCFv3 has the highest spatial resolution of any available 3D reference brain (10 versus 17–50 mm voxels or more) and is 1,000 times higher resolution than CCFv2 (100 mm voxels). Of course, limitations still exist. For example, the reference brain is �15% larger than the average of the individual STPT imaged brains used in its creation, and, the relationship of the template to fiducial landmarks of the skull (e.g., Bregma) are unknown. So, at present, CCFv3 is not suitable for determining stereotaxic coordinates. This limitation could be overcome by registering the average template to brains imaged in the skull with high resolution MRI or X-ray microCT or validating mapped coordinates following alignment of the CCFv3 to the MBSC atlas (Chon et al., 2019). 

We labeled all the voxels in the average template to produce a fully annotated 3D reference atlas using an approach that differs notably from previous atlases (including CCFv2). Here, we delineated structures directly in 3D to build smooth volumes as opposed to drawing in only one imaging plane, which produced noticeable improvement in the ‘‘smoothness’’ of borders when viewed in all planes (Figure S7). This result is not just aesthetic. The isocortex is a thin sheet of gray matter that has a concave inner surface and a convex outer surface, thus, it follows that areal borders that extend from the brain surface down to the white matter should be curved. However, in conventional 2D atlases, borders between cortical areas are always drawn as straight lines from the pial surface down to the white matter in all planes (coronal, horizontal, and sagittal) (Paxinos and Franklin, 2012). Straight border lines seem very unlikely to represent the true curvature of the isocortical sheet in 3D space. 

Conventional 2D mouse brain atlases are drawn on reference brains stained with Nissl (Dong, 2008), or Nissl and AChE (Paxinos and Franklin, 2012). We also used Nissl staining to corroborate and assist in drawing borders, but it was not the primary reference space (i.e., the average template). Other reference data types commonly consulted for parcellating mouse brain structures include myeloarchitecture, chemoarchitecture, genoarchitecture, connectivity, and functional mapping (Bienkowski et al., 2018; Gam� anut‚� et al., 2018; Garrett et al., 2014; Thompson et al., 2008; Wang and Burkhalter, 2007; Watson et al., 2012; Zhuang et al., 2017). Given that each dataset reveals a unique labeling pattern for certain regions, combining data types should provide a tremendous methodological advantage for accurately defining brain structures. Our neuroanatomists carefully selected datasets across these modalities, and, like atlases drawn by other experts, subjectively integrated these data to draw borders (albeit this time in 3D). Incorporating additional structures and using these annotation methods likely enhanced the accuracy of areal delineations, but we did not systematically validate all the parcellations by mapping them back onto individual image series containing appropriately labeled data for validation. 

We annotated 658 individual structures in total for CCFv3. It contains far more 3D reconstructions than any existing MRIbased atlas (Ali et al., 2005; Badea et al., 2007; Dorr et al., 2008; Ma et al., 2005; MacKenzie-Graham et al., 2004; Ullmann et al., 2013), but fewer annotated structures compared to standard 2D atlases, i.e., MBSC (4[th] edition, n = 946) and ARA (n = 860). Reasons included a lack of available data from which borders could be confidently drawn, but, in large part came down to resources, because the process of manually annotating so many structures in 3D was time- and labor-intensive. Given major advances in machine learning approaches to image feature detection and leveraging large multimodal whole brain datasets, we expect future atlases will be built in more automated, unbiased ways (Van Essen and Glasser, 2018). Several groups have already applied automatic delineation methods to mouse brain images but so far extracted only major brain regions (Johnson et al., 2010; Ma et al., 2005, 2008) or focused on a small number of brain areas in reasonable detail (Chen et al., 2019). Supervised machine learning methods could be applied to learn image features predictive of known brain regions using manual parcellation results. Comparison of atlases built from unimodal and multimodal data types will undoubtedly shed new light on fundamentals of brain organization. To achieve this goal, it is important that data and delineations are in a common spatial coordinate framework. 

Registration of image data into the CCF enables direct comparison and integration across multiple datasets in the same space. Specifically, registration enables a voxel-level description of features of interest in any given image series. As each 10 mm voxel is labeled with a structure from the ARA ontology, one can simply add up all the voxels with the same label to get descriptions at the brain region level, enabling multi-scale analyses ranging from single voxel (cellular resolution) to whole brain. Voxel-based data summaries are demonstrably useful for quantitative analyses (Kim et al., 2017; Knox et al., 2018; Oh et al., 2014; Whitesell et al., 2019) and data visualizations across multiple resolutions (Winnubst et al., 2019). Working with voxels also provides flexibility in structure annotation (i.e., voxels can be relabeled) and the ability to ignore parcellation completely for purely spatialbased analyses. 

Registration precision may always be best for image series collected using the same modality (i.e., STPT), but other image types can also be registered to this template. We did not develop registration software tools for users, but because the CCF was made available online, many recent publications already describe registration solutions and informatics pipelines for different imaging modalities, including MRI, light sheet imaging of cleared brains, other high-resolution fluorescent whole-brain imaging platforms, and traditional histological-stained brain sections (Allan Johnson et al., 2019; Chon et al., 2019; Eastwood et al., 2019; Fu¨ rth et al., 2018; Han et al., 2018; Jin et al., 2019; Li et al., 2018; Ni et al., 2020; Pallast et al., 2019; Puchades et al., 2019; Renier et al., 2016; Salinas et al., 2018; Tappan et al., 2019; Tward and Miller, 2019; Winnubst et al., 2019; Xiong et al., 2018). CCFv3 has also been used to provide anatomical context for large-scale electrophysiology experiments distributed across the brain (Steinmetz et al., 2019) and for widefield 

950 Cell 181, 936–953, May 14, 2020 

**ll** 

## Resource 

calcium imaging maps in cortex of behaving mice (Musall et al., 2019). Alignment of neural activity data opens up the possibility of incorporating functional evidence into the mostly anatomicalbased parcellation schemes used for the mouse brain. 

CCFv3 is a fully annotated anatomical reference space provided as a digital open access interactive atlas. The average template, annotations, and reference datasets are available through our web portal (http://atlas.brain-map.org/). All CCF users are encouraged to contribute back to the resources, tools, and discussions through our community forum (https://community. brain-map.org/t/allen-mouse-ccf-accessing-and-using-relateddata-and-tools/359). 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d RESOURCE AVAILABILITY 

   - B Lead Contact 

   - B Materials Availability 

   - B Data and Code Availability 

- d EXPERIMENTAL MODEL AND SUBJECT DETAILS 

   - B Animal care and use 

- d METHOD DETAILS 

   - B Overall strategy for anatomical delineations in the CCF B Reference Datasets 

- d QUANTIFICATION AND STATISTICAL ANALYSIS 

- d ADDITIONAL RESOURCES 

## SUPPLEMENTAL INFORMATION 

Supplemental Information can be found online at https://doi.org/10.1016/j. cell.2020.04.007. 

## ACKNOWLEDGMENTS 

We thank Dr. Josh Huang from CSHL for providing the Fezf2-CreER mouse line and Dr. Sacha Nelson from Brandeis University for providing PB-mCitrine_p170 and PB-mCitrine_P038 mice. We also thank Dr. John Hohmann for early supervision and the Animal Care, Laboratory Animal Services, Transgenic Colony Management, Imaging, and Technology teams at the Allen Institute for their technical support. We are grateful for the leadership of Allan Jones. The authors wish to thank the Allen Institute founder, Paul G. Allen, for his vision, encouragement, and support. This work was funded by the Allen Institute for Brain Science and in part by NIH (1U24MH114827-01 to M.H. and L.N.). 

## AUTHOR CONTRIBUTIONS 

Conceptualization, L.N., J.A.H., and H.Z.; Transgenic Mice, K.E.H., J.A.H., and H.Z.; Acquisition of Data, A.H., N.D., and A.B.; Software, Y.L., N.G., and L.N.; Project Administration, A.S., S.M.S., S.W.O., and J.W.P.; Data Investigation, Q.W., S.L.-D., J.J.R., P.L., N.G., M.N., B.A.F., L.N., and J.A.H.; Anatomical Boundary Delineation, Q.W. and S.L.-D.; Web Visualization, T.D., B.B., N.G., D.F., W.W., and L.N.; Manuscript Preparation, Q.W., S.L.-D., Y.L., M.N., K.E.H., N.G., M.H., J.J.R., P.L., H.Z., L.N, and J.A.H.; Supervision, C.K. and H.Z. All authors discussed and commented on the manuscript. 

## DECLARATION OF INTERESTS 

D.F. is an employee Tableau Software. B.B. is an employee of 343 Industries. A.S. is an employee of Microsoft Corporation. S.W.O. is an employee of MDimune (Korea). 

Received: May 2, 2019 Revised: December 12, 2019 Accepted: April 3, 2020 Published: May 7, 2020 

## REFERENCES 

Ali, A.A., Dale, A.M., Badea, A., and Johnson, G.A. (2005). Automated segmentation of neuroanatomical structures in multispectral MR microscopy of the mouse brain. Neuroimage 27, 425–435. 

Allan Johnson, G., Wang, N., Anderson, R.J., Chen, M., Cofer, G.P., Gee, J.C., Pratson, F., Tustison, N., and White, L.E. (2019). Whole mouse brain connectomics. J. Comp. Neurol. 527, 2146–2157. 

Avants, B.B., Epstein, C.L., Grossman, M., and Gee, J.C. (2008). Symmetric diffeomorphic image registration with cross-correlation: evaluating automated labeling of elderly and neurodegenerative brain. Med. Image Anal. 12, 26–41. Badea, A., Ali-Sharief, A.A., and Johnson, G.A. (2007). Morphometric analysis of the C57BL/6J mouse brain. Neuroimage 37, 683–693. 

Bienkowski, M.S., Bowman, I., Song, M.Y., Gou, L., Ard, T., Cotter, K., Zhu, M., Benavidez, N.L., Yamashita, S., Abu-Jaber, J., et al. (2018). Integration of gene expression and brain-wide connectivity reveals the multiscale organization of mouse hippocampal networks. Nat. Neurosci. 21, 1628–1643. 

Bock, N.A., Kovacevic, N., Lipina, T.V., Roder, J.C., Ackerman, S.L., and Henkelman, R.M. (2006). In vivo magnetic resonance imaging and semiautomated image analysis extend the brain phenotype for cdf/cdf mice. J. Neurosci. 26, 4455–4459. 

Celio, M.R. (1990). Calbindin D-28k and parvalbumin in the rat nervous system. Neuroscience 35, 375–475. 

Chen, X.J., Kovacevic, N., Lobaugh, N.J., Sled, J.G., Henkelman, R.M., and Henderson, J.T. (2006). Neuroanatomical differences between mouse strains as shown by high-resolution 3D MRI. Neuroimage 29, 99–105. 

Chen, Y., McElvain, L.E., Tolpygo, A.S., Ferrante, D., Friedman, B., Mitra, P.P., Karten, H.J., Freund, Y., and Kleinfeld, D. (2019). An active texture-based digital atlas enables automated mapping of structures and markers across brains. Nat. Methods 16, 341–350. 

Chon, U., Vanselow, D.J., Cheng, K.C., and Kim, Y. (2019). Enhanced and unified anatomical labeling for a common mouse brain atlas. Nat. Commun. 10, 5067. 

Daigle, T.L., Madisen, L., Hage, T.A., Valley, M.T., Knoblich, U., Larsen, R.S., Takeno, M.M., Huang, L., Gu, H., Larsen, R., et al. (2018). A Suite of Transgenic Driver and Reporter Mouse Lines with Enhanced Brain-Cell-Type Targeting and Functionality. Cell 174, 465–480. 

Ding, S.-L. (2013). Comparative anatomy of the prosubiculum, subiculum, presubiculum, postsubiculum, and parasubiculum in human, monkey, and rodent. J. Comp. Neurol. 521, 4145–4162. 

Ding, S.-L., Royall, J.J., Sunkin, S.M., Ng, L., Facer, B.A.C., Lesnar, P., Guillozet-Bongaarts, A., McMurray, B., Szafer, A., Dolbeare, T.A., et al. (2016). Comprehensive cellular-resolution atlas of the adult human brain. J. Comp. Neurol. 524, 3127–3481. 

Ding, S.-L., Yao, Z., Hirokawa, K.E., Nghi Nguyen, T., Graybuck, L.T., Bohn, P., Ngo, K., Smith, K.A., Koch, C., Phillips, J.W., et al. (2019). Distinct transcriptomic cell types and neural circuits of the subiculum and prosubiculum along the dorsal-ventral axis. bioRxiv. https://doi.org/10.1101/2019.12.14.876516. 

Dong, H.W. (2008). The Allen Reference Atlas: a Digital Color Brain Atlas of the C57BL/6J Male Mouse (Wiley). 

Dorr, A.E., Lerch, J.P., Spring, S., Kabani, N., and Henkelman, R.M. (2008). High resolution three-dimensional brain atlas using an average magnetic resonance image of 40 adult C57Bl/6J mice. Neuroimage 42, 60–69. 

**==> picture [46 x 35] intentionally omitted <==**

Cell 181, 936–953, May 14, 2020 951 

## **ll** 

## Resource 

Eastwood, B.S., Hooks, B.M., Paletzki, R.F., O’Connor, N.J., Glaser, J.R., and Gerfen, C.R. (2019). Whole mouse brain reconstruction and registration to a reference atlas with standard histochemical processing of coronal sections. J. Comp. Neurol. 527, 2170–2178. 

Ecker, J.R., Geschwind, D.H., Kriegstein, A.R., Ngai, J., Osten, P., Polioudakis, D., Regev, A., Sestan, N., Wickersham, I.R., and Zeng, H. (2017). The BRAIN Initiative Cell Census Consortium: Lessons Learned toward Generating a Comprehensive Brain Cell Atlas. Neuron 96, 542–557. 

Endo, T., Takazawa, K., Kobayashi, S., and Onaya, T. (1986). Immunochemical and immunohistochemical localization of parvalbumin in rat nervous tissues. J. Neurochem. 46, 892–898. 

Fischl, B., Sereno, M.I., and Dale, A.M. (1999). Cortical surface-based analysis. II: Inflation, flattening, and a surface-based coordinate system. Neuroimage 9, 195–207. 

Fonov, V., Evans, A.C., Botteron, K., Almli, C.R., McKinstry, R.C., and Collins, D.L.; Brain Development Cooperative Group (2011). Unbiased average ageappropriate atlases for pediatric studies. Neuroimage 54, 313–327. 

Fu¨ rth, D., Vaissie` re, T., Tzortzi, O., Xuan, Y., Ma¨ rtin, A., Lazaridis, I., Spigolon, G., Fisone, G., Tomer, R., Deisseroth, K., et al. (2018). An interactive framework for whole-brain maps at cellular resolution. Nat. Neurosci. 21, 139–149. 

Gam� anut‚, R., Kennedy, H., Toroczkai, Z., Ercsey-Ravasz, M., Van Essen, D.C.,� Knoblauch, K., and Burkhalter, A. (2018). The Mouse Cortical Connectome, Characterized by an Ultra-Dense Cortical Graph, Maintains Specificity by Distinct Connectivity Profiles. Neuron 97, 698–715. 

Garrett, M.E., Nauhaus, I., Marshel, J.H., and Callaway, E.M. (2014). Topography and areal organization of mouse visual cortex. J. Neurosci. 34, 12587–12600. 

Gerfen, C.R., Paletzki, R., and Heintz, N. (2013). GENSAT BAC cre-recombinase driver lines to study the functional organization of cerebral cortical and basal ganglia circuits. Neuron 80, 1368–1383. 

Glocker, B., Komodakis, N., Tziritas, G., Navab, N., and Paragios, N. (2008). Dense image registration through MRFs and efficient linear programming. Med. Image Anal. 12, 731–741. 

Gong, S., Doughty, M., Harbaugh, C.R., Cummins, A., Hatten, M.E., Heintz, N., and Gerfen, C.R. (2007). Targeting Cre recombinase to specific neuron populations with bacterial artificial chromosome constructs. J. Neurosci. 27, 9817–9823. 

Grubb, M.S., and Thompson, I.D. (2004). Biochemical and anatomical subdivision of the dorsal lateral geniculate nucleus in normal mice and in mice lacking the beta2 subunit of the nicotinic acetylcholine receptor. Vision Res. 44, 3365–3376. 

Han, Y., Kebschull, J.M., Campbell, R.A.A., Cowan, D., Imhof, F., Zador, A.M., and Mrsic-Flogel, T.D. (2018). The logic of single-cell projections from visual cortex. Nature 556, 51–56. 

Harris, J.A., Oh, S.W., and Zeng, H. (2012). Adeno-associated viral vectors for anterograde axonal tracing with fluorescent proteins in nontransgenic and cre driver mice. Curr. Protoc. Neurosci. Chapter 1, 1–18. 

Harris, J.A., Hirokawa, K.E., Sorensen, S.A., Gu, H., Mills, M., Ng, L.L., Bohn, P., Mortrud, M., Ouellette, B., Kidney, J., et al. (2014). Anatomical characterization of Cre driver mice for neural circuit mapping and manipulation. Front. Neural Circuits 8, 76. 

Harris, J.A., Mihalas, S., Hirokawa, K.E., Whitesell, J.D., Choi, H., Bernard, A., Bohn, P., Caldejon, S., Casal, L., Cho, A., et al. (2019). Hierarchical organization of cortical and thalamic connectivity. Nature 575, 195–202. 

Huberman, A.D., Wei, W., Elstrott, J., Stafford, B.K., Feller, M.B., and Barres, B.A. (2009). Genetic identification of an On-Off direction-selective retinal ganglion cell subtype reveals a layer-specific subcortical map of posterior motion. Neuron 62, 327–334. 

Jin, M., Nguyen, J.D., Weber, S.J., Mejias-Aponte, C.A., Madangopal, R., and Golden, S.A. (2019). SMART: An open source extension of WholeBrain for iDros. Inf. Serv.CO+ LSFM intact mouse brain registration and segmentation. bioRxiv. https://doi.org/10.1101/727529. 

Johnson, G.A., Badea, A., Brandenburg, J., Cofer, G., Fubara, B., Liu, S., and Nissanov, J. (2010). Waxholm space: an image-based reference for coordinating mouse brain research. Neuroimage 53, 365–372. 

Jones, S.E., Buchbinder, B.R., and Aharon, I. (2000). Three-dimensional mapping of cortical thickness using Laplace’s equation. Hum. Brain Mapp. 11, 12–32. 

Kay, J.N., De la Huerta, I., Kim, I.J., Zhang, Y., Yamagata, M., Chu, M.W., Meister, M., and Sanes, J.R. (2011). Retinal ganglion cells with distinct directional preferences differ in molecular identity, structure, and central projections. J. Neurosci. 31, 7753–7762. 

Kerschensteiner, D., and Guido, W. (2017). Organization of the dorsal lateral geniculate nucleus in the mouse. Vis. Neurosci. 34, E008. 

Kim, Y., Yang, G.R., Pradhan, K., Venkataraju, K.U., Bota, M., Garcı´a Del Molino, L.C., Fitzgerald, G., Ram, K., He, M., Levine, J.M., et al. (2017). Brain-wide Maps Reveal Stereotyped Cell-Type-Based Cortical Architecture and Subcortical Sexual Dimorphism. Cell 171, 456–469. 

Knox, J.E., Harris, K.D., Graddis, N., Whitesell, J.D., Zeng, H., Harris, J.A., Shea-Brown, E., and Mihalas, S. (2018). High-resolution data-driven model of the mouse connectome. Netw. Neurosci. 3, 217–236. 

Kovacevic, N., Henderson, J.T., Chan, E., Lifshitz, N., Bishop, J., Evans, A.C.,� Henkelman, R.M., and Chen, X.J. (2005). A three-dimensional MRI atlas of the mouse brain with estimates of the average and variability. Cereb. Cortex 15, 639–645. 

Kuan, L., Li, Y., Lau, C., Feng, D., Bernard, A., Sunkin, S.M., Zeng, H., Dang, C., Hawrylycz, M., and Ng, L. (2015). Neuroinformatics of the allen mouse brain connectivity atlas. Methods 73, 4–17. 

Lee, J., Ehlers, C., Crews, F., Niethammer, M., Budin, F., Paniagua, B., Sulik, K., Johns, J., Styner, M., and Oguz, I. (2011). Automatic cortical thickness analysis on rodent brain. Proc. SPIE Int. Soc. Opt. Eng. 7962, 7962481– 79624811. 

Lein, E.S., Hawrylycz, M.J., Ao, N., Ayres, M., Bensinger, A., Bernard, A., Boe, A.F., Boguski, M.S., Brockway, K.S., Byrnes, E.J., et al. (2007). Genome-wide atlas of gene expression in the adult mouse brain. Nature 445, 168–176. 

Lerch, J.P., Carroll, J.B., Dorr, A., Spring, S., Evans, A.C., Hayden, M.R., Sled, J.G., and Henkelman, R.M. (2008). Cortical thickness measured from MRI in the YAC128 mouse model of Huntington’s disease. Neuroimage 41, 243–251. 

Li, X., Yu, B., Sun, Q., Zhang, Y., Ren, M., Zhang, X., Li, A., Yuan, J., Madisen, L., Luo, Q., et al. (2018). Generation of a whole-brain atlas for the cholinergic system and mesoscopic projectome analysis of basal forebrain cholinergic neurons. Proc. Natl. Acad. Sci. USA 115, 415–420. 

Lu, W., Chen, S., Chen, X., Hu, J., Xuan, A., and Ding, S.-L. (2020). Localization of area prostriata and its connections with primary visual cortex in rodent. J. Comp. Neurol. 528, 389–406. 

Ma, Y., Hof, P.R., Grant, S.C., Blackband, S.J., Bennett, R., Slatest, L., McGuigan, M.D., and Benveniste, H. (2005). A three-dimensional digital atlas database of the adult C57BL/6J mouse brain by magnetic resonance microscopy. Neuroscience 135, 1203–1215. 

Ma, Y., Smith, D., Hof, P.R., Foerster, B., Hamilton, S., Blackband, S.J., Yu, M., and Benveniste, H. (2008). In Vivo 3D Digital Atlas Database of the Adult C57BL/6J Mouse Brain by Magnetic Resonance Microscopy. Front. Neuroanat. 2, 1. 

MacKenzie-Graham, A., Lee, E.-F., Dinov, I.D., Bota, M., Shattuck, D.W., Ruffins, S., Yuan, H., Konstantinidis, F., Pitiot, A., Ding, Y., et al. (2004). A multimodal, multidimensional atlas of the C57BL/6J mouse brain. J. Anat. 204, 93–102. 

Madisen, L., Zwingman, T.A., Sunkin, S.M., Oh, S.W., Zariwala, H.A., Gu, H., Ng, L.L., Palmiter, R.D., Hawrylycz, M.J., Jones, A.R., et al. (2010). A robust and high-throughput Cre reporting and characterization system for the whole mouse brain. Nat. Neurosci. 13, 133–140. 

Martersteck, E.M., Hirokawa, K.E., Evarts, M., Bernard, A., Duan, X., Li, Y., Ng, L., Oh, S.W., Ouellette, B., Royall, J.J., et al. (2017). Diverse Central Projection Patterns of Retinal Ganglion Cells. Cell Rep. 18, 2058–2072. 

952 Cell 181, 936–953, May 14, 2020 

**ll** 

## Resource 

Musall, S., Kaufman, M.T., Juavinett, A.L., Gluf, S., and Churchland, A.K. (2019). Single-trial neural dynamics are dominated by richly varied movements. Nat. Neurosci. 22, 1677–1686. 

Ng, L., Bernard, A., Lau, C., Overly, C.C., Dong, H.-W., Kuan, C., Pathak, S., Sunkin, S.M., Dang, C., Bohland, J.W., et al. (2009). An anatomic gene expression atlas of the adult mouse brain. Nat. Neurosci. 12, 356–362. Ng, L., Lau, C., Sunkin, S.M., Bernard, A., Chakravarty, M.M., Lein, E.S., Jones, A.R., and Hawrylycz, M. (2010). Surface-based mapping of gene expression and probabilistic expression maps in the mouse cortex. Methods 50, 55–62. Ni, H., Tan, C., Feng, Z., Chen, S., Zhang, Z., Li, W., Guan, Y., Gong, H., Luo, Q., and Li, A. (2020). A robust image registration interface for large volume brain atlas. Sci. Rep. 10, 2139. Oh, S.W., Harris, J.A., Ng, L., Winslow, B., Cain, N., Mihalas, S., Wang, Q., Lau, C., Kuan, L., Henry, A.M., et al. (2014). A mesoscale connectome of the mouse brain. Nature 508, 207–214. Pallast, N., Diedenhofen, M., Blaschke, S., Wieters, F., Wiedermann, D., Hoehn, M., Fink, G.R., and Aswendt, M. (2019). Processing pipeline for atlas-based imaging data analysis of structural and functional mouse brain MRI (AIDAmri). Front. Neuroinform. 13, 42. Paxinos, G., and Franklin, K.B.J. (2001). The Mouse Brain in Stereotaxic Coordinates, Second Edition (Elsevier Academic Press). Paxinos, G., and Franklin, K.B.J. (2012). The Mouse Brain in Stereotaxic Coordinates, Fourth Edition (Elsevier Academic Press). Paxinos, G., and Watson, C. (2013). The Rat Brain in Stereotaxic Coordinates (Elsevier Academic Press). Puchades, M.A., Csucs, G., Ledergerber, D., Leergaard, T.B., and Bjaalie, J.G. (2019). Spatial registration of serial microscopic brain images to three-dimensional reference atlases with the QuickNII tool. PLoS ONE 14, e0216796. 

Quina, L.A., Harris, J., Zeng, H., and Turner, E.E. (2017). Specific connections of the interpeduncular subnuclei reveal distinct components of the habenulopeduncular pathway. J. Comp. Neurol. 525, 2632–2656. 

Ragan, T., Kadiri, L.R., Venkataraju, K.U., Bahlmann, K., Sutin, J., Taranda, J., Arganda-Carreras, I., Kim, Y., Seung, H.S., and Osten, P. (2012). Serial twophoton tomography for automated ex vivo mouse brain imaging. Nat. Methods 9, 255–258. 

Renier, N., Adams, E.L., Kirst, C., Wu, Z., Azevedo, R., Kohl, J., Autry, A.E., Kadiri, L., Umadevi Venkataraju, K., Zhou, Y., et al. (2016). Mapping of Brain Activity by Automated Volume Analysis of Immediate Early Genes. Cell 165, 1789–1802. 

Rivlin-Etzion, M., Zhou, K., Wei, W., Elstrott, J., Nguyen, P.L., Barres, B.A., Huberman, A.D., and Feller, M.B. (2011). Transgenic mice reveal unexpected diversity of on-off direction-selective retinal ganglion cell subtypes and brain structures involved in motion processing. J. Neurosci. 31, 8760–8769. 

Salinas, C.B.G., Lu, T.T.H., Gabery, S., Marstal, K., Alanentalo, T., Mercer, A.J., Cornea, A., Conradsen, K., Hecksher-Sørensen, J., Dahl, A.B., et al. (2018). Integrated Brain Atlas for Unbiased Mapping of Nervous System Effects Following Liraglutide Treatment. Sci. Rep. 8, 10310. 

Sharief, A.A., Badea, A., Dale, A.M., and Johnson, G.A. (2008). Automated segmentation of the actively stained mouse brain using multi-spectral MR microscopy. Neuroimage 39, 136–145. 

Shima, Y., Sugino, K., Hempel, C.M., Shima, M., Taneja, P., Bullis, J.B., Mehta, S., Lois, C., and Nelson, S.B. (2016). A Mammalian enhancer trap resource for discovering and manipulating neuronal cell types. eLife 5, e13503. 

Steinmetz, N.A., Zatka-Haas, P., Carandini, M., and Harris, K.D. (2019). Distributed coding of choice, action and engagement across the mouse brain. Nature 576, 266–273. 

Swanson, L.W. (2004). Brain Maps III: Structure of the Rat Brain: an Atlas with Printed and Electronic Templates for Data, Models, and Schematics (Academic Press). 

Swanson, L.W. (2018). Brain maps 4.0-Structure of the rat brain: An open access atlas with global nervous system nomenclature ontology and flatmaps. J. Comp. Neurol. 526, 935–943. 

Tang, T.W.H., and Chung, A.C.S. (2007). Non-rigid image registration using graph-cuts. Med. Image. Comput. Comput. Assist. Interv. 10, 916–924. 

Tappan, S.J., Eastwood, B.S., O’Connor, N., Wang, Q., Ng, L., Feng, D., Hooks, B.M., Gerfen, C.R., Hof, P.R., Schmitz, C., and Glaser, J.R. (2019). Automatic navigation system for the mouse brain. J. Comp. Neurol. 527, 2200–2211. 

Thompson, C.L., Pathak, S.D., Jeromin, A., Ng, L.L., MacPherson, C.R., Mortrud, M.T., Cusick, A., Riley, Z.L., Sunkin, S.M., Bernard, A., et al. (2008). Genomic anatomy of the hippocampus. Neuron 60, 1010–1021. 

Tward, D., and Miller, M. (2019). EM-LDDMM for 3D to 2D registration. bioRxiv. https://doi.org/10.1101/604405. 

Ullmann, J.F.P., Watson, C., Janke, A.L., Kurniawan, N.D., and Reutens, D.C. (2013). A segmentation protocol and MRI atlas of the C57BL/6J mouse neocortex. Neuroimage 78, 196–203. 

Van Essen, D.C., and Glasser, M.F. (2018). Parcellating Cerebral Cortex: How Invasive Animal Studies Inform Noninvasive Mapmaking in Humans. Neuron 99, 640–663. 

Wang, Q., and Burkhalter, A. (2007). Area map of mouse visual cortex. J. Comp. Neurol. 502, 339–357. 

Wang, Q., Sporns, O., and Burkhalter, A. (2012). Network analysis of corticocortical connections reveals ventral and dorsal processing streams in mouse visual cortex. J. Neurosci. 32, 4386–4399. 

Wang, Q., Henry, A.M., Harris, J.A., Oh, S.W., Joines, K.M., Nyhus, J., Hirokawa, K.E., Dee, N., Mortrud, M., Parry, S., et al. (2014). Systematic comparison of adeno-associated virus and biotinylated dextran amine reveals equivalent sensitivity between tracers and novel projection targets in the mouse brain. J. Comp. Neurol. 522, 1989–2012. 

Wang, Q., Ng, L., Harris, J.A., Feng, D., Li, Y., Royall, J.J., Oh, S.W., Bernard, A., Sunkin, S.M., Koch, C., and Zeng, H. (2017). Organization of the connections between claustrum and cortex in the mouse. J. Comp. Neurol. 525, 1317–1346. 

Watson, C., Paxinos, G., and Puelles, L. (2012). The Mouse Nervous System (Elsevier Academic Press). 

Whitesell, J.D., Buckley, A.R., Knox, J.E., Kuan, L., Graddis, N., Pelos, A., Mukora, A., Wakeman, W., Bohn, P., Ho, A., et al. (2019). Whole brain imaging reveals distinct spatial patterns of amyloid beta deposition in three mouse models of Alzheimer’s disease. J. Comp. Neurol. 527, 2122–2145. 

Winnubst, J., Bas, E., Ferreira, T.A., Wu, Z., Economo, M.N., Edson, P., Arthur, B.J., Bruns, C., Rokicki, K., Schauder, D., et al. (2019). Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long-Range Connectivity in the Mouse Brain. Cell 179, 268–281. 

Xiong, J., Ren, J., Luo, L., and Horowitz, M. (2018). Mapping histological slice sequences to the allen mouse brain atlas without 3D reconstruction. Front. Neuroinform. 12, 93. 

Yushkevich, P.A., Piven, J., Hazlett, H.C., Smith, R.G., Ho, S., Gee, J.C., and Gerig, G. (2006). User-guided 3D active contour segmentation of anatomical structures: significantly improved efficiency and reliability. Neuroimage 31, 1116–1128. 

Zhuang, J., Ng, L., Williams, D., Valley, M., Li, Y., Garrett, M., and Waters, J. (2017). An extended retinotopic map of mouse cortex. eLife 6, e18372. 

Zingg, B., Hintiryan, H., Gou, L., Song, M.Y., Bay, M., Bienkowski, M.S., Foster, N.N., Yamashita, S., Bowman, I., Toga, A.W., and Dong, H.W. (2014). Neural networks of the mouse neocortex. Cell 156, 1096–1111. 

**==> picture [46 x 35] intentionally omitted <==**

Cell 181, 936–953, May 14, 2020 953 

**ll** 

Resource 

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE|SOURCE|SOURCE|IDENTIFIER|IDENTIFIER|
|---|---|---|---|---|
||||||
|Antibodies|||||
|Rabbit polyclonal anti-Calbindin D-<br>28k (Calb1)|Swant||Cat#CB38; RRID: AB_2721225||
|Mouse monoclonal anti-NeuN|Millipore Sigma||Cat#MAB377; RRID: AB_2298772||
|Rabbit polyclonal anti-Neuroflament,<br>Medium, 160 kD (NF-160)|Abcam||Cat#AB9034; RRID: AB_306956||
|Rabbit polyclonal anti-Parvalbumin|Swant||Cat#PV 25; RRID: AB_10000344||
|Mouse monoclonal anti-Neuroflament H<br>(SMI-32)|Covance||Cat#SMI-32R-100; RRID: AB_509997||
|Mouse monoclonal anti-Myelin Basic<br>Protein (SMI-99)|Covance||Cat#SMI-99P; RRID: AB_2564742||
|Alexa Fluor 488 goat anti-rabbit|Thermo Fisher Scientifc||Cat#A-11008; RRID: AB_10563748||
|Alexa Fluor 594 goat anti-mouse|Thermo Fisher Scientifc||Cat#A-11005; RRID: AB_2534073||
|Bacterial and Virus Strains|||||
|AAV2/1.hSynapsin.EGFP.WPRE.bGH|UPenn Vector Core||Addgene AAV1; 105539;<br>~~R~~RID:Addgene_105539||
|AAV2/1.CAG.FLEX.EGFP.WPRE.bGH|UPenn Vector Core||Addgene AAV1; 51502; RRID:<br>Addgene51502||
|||||_|
|Chemicals, Peptides, and Recombinant Proteins|||||
|Trimethoprim (TMP)|Sigma-Aldrich||T7883-5G||
|Tamoxifen (TAM)|Sigma-Aldrich||T5648-5G||
|Experimental Models: Organisms/Strains|||||
|Mouse: C57BL/6J|The Jackson Laboratory||JAX: 000664||
|Mouse: B6.Cg-Tg(A930038C07Rik-cre)<br>1Aibs/J, A930038C07Rik-Tg1-Cre|The Jackson Laboratory||JAX: 017346||
|Mouse: Adcyap1-2A-Cre|Allen Institute for Brain Science||N/A||
|Mouse: B6;129S-Calb1tm2.1(cre)Hze/J,Calb1-<br>IRES2-Cre<br>The Jackson Laboratory|||JAX: 028532||
|Mouse: B6.Cg-Calb1tm1.1(folA/EGFP/cre)Hze/<br>J,Calb1-T2A-dgCre|The Jackson Laboratory||JAX: 023531||
|Mouse: B6(Cg)-Calb2tm1(cre)Zjh/J,Calb2-<br>IRES-Cre|The Jackson Laboratory||JAX: 010774||
|Mouse: B6;129S-Cartpttm1.1(cre)Hze/J, Cart-<br>IRES2-Cre<br>The Jackson Laboratory|||JAX: 028533||
|Mouse: STOCK Tg(Cartpt-cre)1Aibs/J,<br>Cart-Tg1-Cre|The Jackson Laboratory||JAX: 009615||
|Mouse: B6(Cg)-Ccktm2.1(cre/ERT2)Zjh/J, Cck-<br>IRES-Cre|The Jackson Laboratory||JAX: 012706||
|Mouse: B6;129S6-Chattm1(cre)Lowl/J,Chat-<br>IRES-Cre-neo|The Jackson Laboratory||JAX: 006410||
|Mouse: STOCK Tg(Chrna2-cre)OE25Gsat/<br>Mmucd, Chrna2-Cre_OE25|MMRRC||MMRRC: 036502||
|Mouse: STOCK Tg(Cnnm2-cre)KD18Gsat/<br>Mmucd, Cnnm2-Cre_KD18|MMRRC||MMRRC: 030951||
|Mouse: Crh-IRES-Cre_BL|Bradford Lowell||N/A||
|Mouse: B6(Cg)-Crhtm1(cre)Zjh/J, Crh-IRES-<br>Cre_ZJH|The Jackson Laboratory||JAX: 012704||



(Continued on next page) 

e1 Cell 181, 936–953.e1–e9, May 14, 2020 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

|Continued|||
|---|---|---|
|REAGENT or RESOURCE|SOURCE|IDENTIFIER|
|Mouse: B6.Cg-Ctgftm1.1(folA/cre)Hze/J, Ctgf-<br>2A-dgCre|The Jackson Laboratory|JAX: 028535|
|Mouse: B6(Cg)-Cux2tm3.1(cre/ERT2)Mull/<br>Mmmh, Cux2-CreERT2|MMRRC|MMRRC: 032779|
|Mouse: B6(Cg)-Cux2tm1.1(cre)Mull/Mmmh,<br>Cux2-IRES-Cre|MMRRC|MMRRC: 031778|
|Mouse: STOCK Tg(Dbh-cre)KH212Gsat/<br>Mmcd, Dbh-Cre_KH212|MMRRC|MMRRC: 032081|
|Mouse: STOCK Tg(Dlg3-cre)KG118Gsat/<br>Mmucd, Dlg3-Cre_KG118|MMRRC|MMRRC: 032809|
|Mouse: Drd1a-Cre|Richard Palmiter|N/A|
|Mouse: STOCK Tg(Drd3-cre)KI196Gsat,<br>Drd3-Cre_KI196|MMRRC|MMRRC: 034610|
|Mouse: STOCK Tg(Drd3-cre)KI198Gsat/<br>Mmucd, Drd3-Cre_KI198|MMRRC|MMRRC: 031741|
|Mouse: STOCK Tg(Efr3a-cre)NO108Gsat/<br>Mmucd, Efr3a-Cre_NO108|MMRRC|MMRRC: 036660|
|Mouse: B6.129S2-Emx1tm1(cre)Krj/J, Emx1-<br>IRES-Cre|The Jackson Laboratory|JAX: 005628|
|Mouse: B6.Cg-Erbb4tm1.1(cre/ERT2)Aibs/J,<br>Erbb4-2A-CreERT2|The Jackson Laboratory|JAX: 012360|
|Mouse: Esr1-2A-Cre|David Anderson|N/A|
|Mouse: B6;129S-Esr2tm1.1(cre)Hze/J, Esr2-<br>IRES2-Cre|The Jackson Laboratory|JAX: 030158|
|Mouse: B6(Cg)-Etv1tm1.1(cre/ERT2)Zjh/J, Etv1-<br>CreERT2<br>The Jackson Laboratory||JAX: 013048|
|Mouse: B6;129S-Fezf1tm1.1(cre/folA)Hze/J,<br>Fezf1-2A-dCre|The Jackson Laboratory|JAX: 013048|
|Mouse: Fezf2-CreER|Z. Josh Huang|N/A|
|Mouse: B6.Cg-Foxp2tm1.1(cre/GFP)Rpa/J,<br>Foxp2-IRES-Cre|The Jackson Laboratory|JAX: 030541|
|Mouse: STOCKGad2tm2(cre)Zjh/J, Gad2-<br>~~IRES-Cre~~|The Jackson Laboratory|JAX: 010802|
|Mouse: STOCK Tg(Gal-cre)KI87Gsat/<br>Mmcd, Gal-Cre_KI87|MMRRC|MMRRC: 031060|
|Mouse: STOCK Tg(Colgalt2-cre)<br>NF107Gsat/Mmucd, Glt25d2-Cre_NF107|MMRRC|MMRRC: 036504|
|Mouse: B6.Cg-Gnb4tm1.1(cre)Hze/J, Gnb4-<br>IRES2-Cre|The Jackson Laboratory|JAX: 029587|
|Mouse: B6.Cg-Gnb4tm1.1(cre/ERT2)Hze/J,<br>Gnb4-IRES2-CreERT2|The Jackson Laboratory|JAX: 030159|
|Mouse: STOCK Tg(Gpr26-cre)KO250Gsat/<br>Mmucd, Gpr26-Cre_KO250<br>MMRRC||MMRRC: 033032|
|Mouse: C57BL/6-Tg(Grik4-cre)G32-4Stl/J,<br>Grik4-Cre|The Jackson Laboratory|JAX: 006474|
|Mouse: STOCK Tg(Grm2-cre)MR90Gsat/<br>Mmcd, Grm2-Cre_MR90|MMRRC|MMRRC: 034611|
|Mouse: STOCK Tg(Grp-cre)KH288Gsat/<br>Mmucd, Grp-Cre_KH288|MMRRC|MMRRC: 031183|
|Mouse: B6;129S-Htr1atm1.1(cre)Hze/J, Htr1a-<br>IRES2-Cre<br>The Jackson Laboratory||JAX: 030160|
|Mouse: STOCK Tg(Htr2a-cre)KM207Gsat/<br>Mmucd Htr2a-CreKM207|MMRRC|MMRRC: 031150|
|, _|||



(Continued on next page) 

Cell 181, 936–953.e1–e9, May 14, 2020 e2 

Resource 

## **ll** 

|Continued|||
|---|---|---|
|REAGENT or RESOURCE|SOURCE|IDENTIFIER|
|Mouse: STOCK Tg(Htr3a-cre)NO152Gsat/<br>Mmucd, Htr3a-Cre_NO152|MMRRC|MMRRC: 036680|
|Mouse: STOCK Jam2tm1.1(cre)Jrs/J,<br>Jam2-Cre|The Jackson Laboratory|JAX: 031612|
|Mouse: STOCK Tg(Kcnc2-Cre)K128Stl/<br>LetJ, Kcnc2-Cre|The Jackson Laboratory|JAX: 008582|
|Mouse: B6.129(SJL)-Kcng4tm1.1(cre)Jrs/J,<br>Kcng4-Cre|The Jackson Laboratory|JAX: 029414|
|Mouse: B6.129-Leprtm2(cre)Rck/J, Lepr-<br>IRES-Cre|The Jackson Laboratory|JAX: 008320|
|Mouse: Lypd6-Cre_KL156|Nathaniel Heintz and Charles Gerfen|N/A|
|Mouse: B6.Cg-Ndnftm1.1(folA/cre)Hze/J, Ndnf-<br>IRES2-dgCre<br>The Jackson Laboratory||JAX: 028536|
|Mouse: B6;129S-Nos1tm1.1(cre/ERT2)Zjh/J,<br>Nos1-CreERT2|The Jackson Laboratory|JAX: 014541|
|Mouse: FVB-Tg(Nr5a1-cre)2Lowl/J,<br>Nr5a1-Cre|The Jackson Laboratory|JAX: 006364|
|Mouse: B6.Cg-Ntng2tm1.1(cre)Hze/J, Ntng2-<br>IRES2-Cre|The Jackson Laboratory|JAX: 029588|
|Mouse: B6;129S4-Ntrk1tm1(cre)Lfr/Mmucd,<br>Ntrk1-IRES-Cre|MMRRC|MMRRC: 015500|
|Mouse: B6.FVB(Cg)-Tg(Ntsr1-cre)<br>GN220Gsat/Mmucd, Ntsr1-Cre_GN220|MMRRC|MMRRC: 030648|
|Mouse: B6.Cg-Nxph4tm1.1(cre/ERT2)Hze/J,<br>Nxph4-2A-CreERT2|The Jackson Laboratory|JAX: 022861|
|Mouse: STOCK Tg(Oxtr-cre)ON66Gsat/<br>Mmucd, Oxtr-Cre_ON66|MMRRC|MMRRC: 036545|
|Mouse: PB-mCitrine P038|~~S~~hima et al., 2016|~~N~~/A|
|Mouse: PB-mCitrine P170|~~S~~hima et al., 2016|~~N~~/A|
|Mouse: B6.Cg-Tg(Pcp2-cre)GN135Gsat/<br>Mmucd, Pcp2-Cre_GN135|MMRRC|MMRRC: 030868|
|Mouse: B6;129S-Pdyntm1.1(cre/ERT2)Hze/J,<br>~~Pdyn-T2A-CreERT2~~|The Jackson Laboratory|JAX: 030197|
|Mouse: STOCK Tg(Pdzk1ip1-cre)<br>KD31Gsat/Mmucd, Pdzk1ip1-Cre_KD31|MMRRC|MMRRC: 030851|
|Mouse: B6;129S-Penktm2(cre)Hze/J, Penk-<br>IRES2-Cre|The Jackson Laboratory|JAX: 025112|
|Mouse: STOCK Tg(Plxnd1-cre)OG1Gsat/<br>Mmucd, Plxnd1-Cre_OG1|MMRRC|MMRRC: 036631|
|Mouse: Plxnd1-CreER|Z. Josh Huang|N/A|
|Mouse: STOCK Tg(Pomc1-cre)16Lowl/J,<br>Pomc-Cre_BL|The Jackson Laboratory|JAX: 005965|
|Mouse: STOCK Tg(Ppp1r17-cre)<br>NL146Gsat/Mmucd, Ppp1r17-Cre_NL146|MMRRC|MMRRC: 036205|
|Mouse: STOCK Tg(Prkcd-glc-1/CFP,-cre)<br>EH124Gsat/Mmucd, Prkcd-GluCla-CFP-<br>IRES-Cre_EH124|MMRRC|MMRRC: 011559|
|Mouse: B6;129P2-Pvalbtm1(cre)Arbr/J, Pvalb-<br>IRES-Cre<br>The Jackson Laboratory||JAX: 008069|
|Mouse: B6;129S-Rasgrf2tm1.1(cre/folA)Hze/J,<br>Rasgrf2-T2A-dCre|The Jackson Laboratory|JAX: 022864|
|Mouse: STOCK Tg(Rbp4-cre)KL100Gsat/<br>Mmucd Rbp4-CreKL100|MMRRC|MMRRC: 031125|
|, _|||



(Continued on next page) 

e3 Cell 181, 936–953.e1–e9, May 14, 2020 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

|Continued|||
|---|---|---|
|REAGENT or RESOURCE|SOURCE|IDENTIFIER|
|Mouse: Rorb-IRES2-Cre-neo|Allen Institute for Brain Science|N/A|
|Mouse: B6;129S-Rorbtm1.1(cre)Hze/J, Rorb-<br>IRES2-Cre|The Jackson Laboratory|JAX: 023526|
|Mouse: B6;C3-Tg(Scnn1a-cre)2Aibs/J,<br>Scnn1a-Tg2-Cre|The Jackson Laboratory|JAX: 009112|
|Mouse: B6;C3-Tg(Scnn1a-cre)3Aibs/J,<br>Scnn1a-Tg3-Cre|The Jackson Laboratory|JAX: 009613|
|Mouse: Sdk2-CreER|Joshua Sanes|N/A|
|Mouse: STOCK Tg(Sim1-cre)KJ18Gsat/<br>Mmucd, Sim1-Cre_KJ18|MMRRC|MMRRC: 031742|
|Mouse: STOCKSlc17a6tm2(cre)Lowl/J,<br>Slc17a6-IRES-Cre|The Jackson Laboratory|JAX: 016963|
|Mouse: B6;129S-Slc17a7tm1.1(cre)Hze/J,<br>Slc17a7-IRES2-Cre|The Jackson Laboratory|JAX: 023527|
|Mouse: Tg(Slc17a8-icre)1Edw/SealJ,<br>Slc17a8-iCre|The Jackson Laboratory|JAX: 018147|
|Mouse: B6;129S-Slc17a8tm1.1(cre)Hze/J,<br>Slc17a8-IRES2-Cre|The Jackson Laboratory|JAX: 028534|
|Mouse: STOCK Tg(Slc18a2-cre)OZ14Gsat/<br>Mmcd, Slc18a2-Cre_OZ14<br>MMRRC||MMRRC: 034814|
|Mouse: STOCKSlc32a1tm2(cre)Lowl/J,<br>Slc32a1-IRES-Cre|The Jackson Laboratory|JAX: 016962|
|Mouse: STOCKSlc6a3tm1(cre)Xz/J,<br>Slc6a3-Cre|The Jackson Laboratory|JAX: 020080|
|Mouse: B6.Cg-Tg(Slc6a4-cre)ET33Gsat/<br>Mmcd, Slc6a4-Cre_ET33|MMRRC|MMRRC: 031028|
|Mouse: STOCK Tg(Slc6a4-cre/ERT2)<br>EZ13Gsat/Mmcd, Slc6a4-CreERT2_EZ13|MMRRC|MMRRC: 030071|
|Mouse: STOCK Tg(Slc6a5-cre)KF109Gsat/<br>Mmucd, Slc6a5-Cre_KF109<br>MMRRC||MMRRC: 030730|
|Mouse: STOCKSsttm2.1(cre)Zjh/J, Sst-<br>IRES-Cre|The Jackson Laboratory|JAX: 013044|
|Mouse: STOCK Tg(Syt17-cre)NO14Gsat/<br>~~Mmucd, Syt17-Cre_NO14~~|MMRRC|MMRRC: 034355|
|Mouse: STOCK Tg(Syt6-cre)KI148Gsat/<br>Mmucd, Syt6-Cre_KI148|MMRRC|MMRRC: 032012|
|Mouse: B6;129S-Tac1tm1.1(cre)Hze/J, Tac1-<br>IRES2-Cre|The Jackson Laboratory|JAX: 021877|
|Mouse: B6;129S-Tac2tm1.1(cre)Hze/J, Tac2-<br>IRES2-Cre|The Jackson Laboratory|JAX: 021878|
|Mouse: Tacr1-T2A-Cre|~~D~~aigle et al., 2018|~~N~~/A|
|Mouse: B6;129S-Tac2tm1.1(cre)Hze/J, Tac2-<br>IRES2-Cre|The Jackson Laboratory|JAX: 021878|
|Mouse: B6.FVB(Cg)-Tg(Th-cre)FI172Gsat/<br>Mmucd, Th-Cre_FI172|MMRRC|MMRRC: 031029|
|Mouse: FVB/N-Tg(Thy1-cre)1Vln/J,<br>Thy1-Cre|The Jackson Laboratory|JAX: 006143|
|Mouse: STOCK Tg(Tlx3-cre)PL56Gsat/<br>Mmucd, Tlx3-Cre_PL56|MMRRC|MMRRC: 041158|
|Mouse: B6.Cg-Trib2tm1.1(cre/ERT2)Hze/J,<br>Trib2-F2A-CreERT2|The Jackson Laboratory|JAX: 022865|
|Mouse: STOCKViptm1(cre)Zjh/J, Vip-<br>IRES-Cre|The Jackson Laboratory|JAX: 010908|
||||



(Continued on next page) 

Cell 181, 936–953.e1–e9, May 14, 2020 e4 

**ll** 

Resource 

|Continued|||||
|---|---|---|---|---|
|REAGENT or RESOURCE|SOURCE||IDENTIFIER||
|Mouse: STOCK Tg(Vipr2-cre)KE2Gsat/<br>Mmucd, Vipr2-Cre_KE2|MMRRC||MMRRC: 034281||
|Mouse: STOCK Tg(Vipr2-cre)KE2Gsat/<br>Mmucd, Vipr2-IRES2-Cre|The Jackson Laboratory||JAX: 031332||
|Mouse: Vipr2-IRES2-Cre-neo|Allen Institute for Brain Science||N/A||
|Mouse: B6.Cg-Gt(ROSA)26Sortm14(CAG-<br>tdTomato)Hze/J, Ai14(RCL-tdT)|The Jackson Laboratory||JAX: 007914||
|Mouse: B6.Cg-Igs7tm140.1(tetO-EGFP,CAG-tTA2)<br>Hze/J Ai140(TIT2L-GFP-ICL-tTA2)<br>The Jackson Laboratory|||JAX: 030220||
|,|||||
|Software and Algorithms|||||
|ITK-SNAP (http://itksnap.org)|Penn Image Computing and Science<br>Laboratory (PICSL), Scientifc Computing<br>~~a~~nd Imaging Institute (SCI)||RRID:SCR_002010||
|Insight Toolkit (ITK), SimpleITK (itk.org)|~~K~~itware||~~R~~RID:SCR_001149||
|Python 3.x (python.org)|~~P~~ython Software Foundation||RRID:SCR_008394||
|Anaconda|Anaconda||~~h~~ttps://www.anaconda.com/||
|NumPy (http://numpy.org)|~~N~~umPy Developers||~~R~~RID:SCR_008633||
|pynrrd|~~M~~aarten H. Everts and contributors||~~h~~ttps://github.com/mhe/pynrrd||
|pandas|~~N~~umFOCUS||~~h~~ttps://pandas.pydata.org/||
|h5py|~~T~~he HDF Group (THG)||~~h~~ttp://www.h5py.org/||
|SciPy (http://scipy.org)|~~S~~ciPy developers||~~R~~RID:SCR_008058||
|pg8000|~~M~~athieu Fenniak||~~h~~ttps://github.com/tlocke/pg8000||
|~~Kakadu~~|~~K~~akadu Software Pty Ltd||~~h~~ttps://kakadusoftware.com/||
|tinyXML|Lee Thomason||http://grinninglizard.com/tinyxml/||
|Other|||||
|Allen Brain Reference Atlases|This paper||~~h~~ttp://atlas.brain-map.org/||
|Allen Mouse Brain Atlas|~~L~~ein et al., 2007||~~h~~ttp://mouse.brain-map.org||
|Allen Mouse Brain Connectivity Atlas|~~O~~h et al., 2014; Harris et al., 2019||~~h~~ttp://connectivity.brain-map.org||
|Anatomic Reference Data|Allen Institute for Brain Science||http://connectivity.brain-map.org/static/<br>referencedata||



## RESOURCE AVAILABILITY 

## Lead Contact 

Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Lydia Ng (lydian@alleninstitute.org). 

## Materials Availability 

This study did not generate new unique reagents. 

## Data and Code Availability 

The Allen Brain Map is an open access resource with publicly available data at http://portal.brain-map.org/. CCFv3, as well as older versions of the reference atlas, are available at the Allen Brain Reference Atlases portal (http://atlas.brain-map.org/). Individual average template and associated annotation images can be manually downloaded using the Atlas Viewer, while images can be downloaded en masse using the AllenSDK (https://allensdk.readthedocs.io/en/latest/_static/examples/nb/image_download.html). 

The AllenSDK is hosted on Github (https://github.com/alleninstitute/allensdk) and its documentation on Read The Docs (https:// allensdk.readthedocs.io/). Registration code is available at (https://github.com/AllenInstitute/stpt_registration); see critical documentation at (https://github.com/AllenInstitute/stpt_registration/blob/master/README.md). Code for estimating structure volumes (https://github.com/AllenInstitute/CCFv3_Volumetric_Analysis/) and mapping the atlas annotations onto a specimen’s image space are available as described above (https://github.com/AllenInstitute/3D-atlas-reverse-mapping/). 

Our web API is documented at http://help.brain-map.org/ and http://help.brain-map.org/display/mouseconnectivity/ API#API-DownloadAtlas3-DReferenceModels. 

e5 Cell 181, 936–953.e1–e9, May 14, 2020 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

Other data files, including the transgenic lines registered and downsampled to 25 mm resolution, 2D cortical surface maps, and the average deformation field derived from the 1,675 specimens used to create the average template are here: http://download. alleninstitute.org/publications/allen_mouse_brain_common_coordinate_framework/. 

## EXPERIMENTAL MODEL AND SUBJECT DETAILS 

## Animal care and use 

All experimental procedures were approved by the Allen Institute Institutional Animal Care and Use Committee (IACUC) and conform to NIH guidelines. Both male and female wild-type (C57BL/6J) and transgenic mice R P56 were used in these studies. All animals were housed 3-5 per cage, under constant temperature, humidity, and light conditions (12 hr light/dark cycles) and given food and water ad libitum. 

## METHOD DETAILS 

## Overall strategy for anatomical delineations in the CCF 

Unlike the 2D ARA atlas drawn on a single Nissl-stained specimen (Dong, 2008), or Nissl- and AchE-stained specimen (Paxinos and Franklin, 2012), the mouse brain atlas built in this study was manually drawn in 3D space on the average template using multimodal reference datasets (described below). In the average template, we identified many structures with distinct inherent contrast features that directly guided border delineations (e.g., primary sensory cortices and dentate gyrus). However, the borders of many other structures, such as higher visual cortical areas, are not visible in the template alone. These ‘‘invisible’’ (as well as the ‘‘visible’’) structures were delineated with the aid of multimodal reference data: transgenic and connectivity datasets, cytoarchitecture, chemoarchitecture, and in situ hybridization data. We additionally consulted the MBSC and ARA atlases and relevant literature for each brain structure. When conflicts between these two atlases occurred, or when delineation schemes did not exist in either atlas, additional literature was consulted prior to determining borders using our own reference data in the average template. 

## Reference Datasets 

## The Average Template 

The average template was generated from autofluorescence background signal in the red channel acquired during STPT imaging from 1,675 mouse brains with a final voxel resolution of 10 mm. This volume was annotated to assign every voxel to an anatomical structure. The average template has lower x-y spatial resolution compared to the ARA Nissl-stained specimen images, where one can see size, shape, and density of cells more clearly. Notably, the original STPT images do have high (0.35 mm) x-y resolution, and, in these images, cell nuclei appear darker than the cytoplasm. Thus, in the average template, ‘‘dark’’ and ‘‘light’’ areas often reflect cell density, but not necessarily shape or size as in Nissl-stained specimens. Specifically, we see that structures with relatively densely packed cells are light, such as layer 4 of the primary sensory cortical areas. By contrast, structures with sparse cells are relatively dark, such as fiber tracts which are even darker than gray matter structures (Figures 1A and 1E–1K). There are a few notable exceptions, including the pyramidal layer of the hippocampus. The pyramidal layer is composed of very densely packed cells. Since individual cell nuclei are dark, the many dark nuclei merge together in the averaging and downsampling in x-y to 10 mm voxels, and so form the dark band-like appearance of the pyramidal layer. Also, since cell cytoplasm appears ‘‘light’’ in the STPT autofluorescence background, and the gray matter contains more cell bodies than fiber tracts, the gray matter itself is lighter than fiber tracts (which are very dark) in the average template. 

## Transgenic Mice 

Transgenic lines were generated at the Allen Institute (Madisen et al., 2010) or imported from external sources including the GENSAT project (Gerfen et al., 2013; Gong et al., 2007) and are listed in the Key Resources Table. Cre driver lines were crossed with the Credependent tdTomato expressing reporter line Ai14, Ai110 or Ai140 (Madisen et al., 2010; Daigle et al., 2018). Regulatable Cre lines were induced with TAM or TMP 1-2 weeks before perfusion. Brains were perfused at an average age of P56 (min – max: P50 – P131), imaged by STPT, and registered to the 3D average template brain. Experiments were curated for those with (1) enriched gene expression in the structures that we wanted to delineate and (2) successful registration to the average template determined by visual inspection of alignment results. High resolution images are available through links in Table S3. Registered grid files, cortical surface views, and instructions for using ITK-SNAP to view them are also available here: (http://download.alleninstitute.org/publications/ allen_mouse_brain_common_coordinate_framework/). 

## Mouse Connectivity Atlas Data 

All anterograde viral tracing experiments were performed with our standardized imaging and informatics pipeline (Harris et al., 2012, 2019; Martersteck et al., 2017; Oh et al., 2014). Viruses are listed in the Key Resources Table. Brains were perfused and collected 3 weeks post-injection at P56 (or post-TAM or TMP induction for regulatable lines). Experiments were curated for those that provided useful information on regions or their borders. In brief, we chose datasets which (1) contained strong (dense) projections to target structure(s) that we wanted to delineate. (2) injections were mostly restricted to a single brain region (little secondary infection in neighboring structures), and (3) registration precision to the average template was considered good following expert visual inspection. We did not use a specific quantitative threshold for injection size as the appropriate volume varies by brain structure volume, but 

Cell 181, 936–953.e1–e9, May 14, 2020 e6 

**ll** 

Resource 

we selected those that came closest to filling up a single region, because this shows the largest innervated territories in the target structure. Data can be found in the Allen Mouse Brain Connectivity Atlas database (http://connectivity.brain-map.org) using experiment IDs or links provided in Table S3. 

## Histology and immunohistochemistry 

Histological staining (Nissl and Acetylcholinesterase) and fluorescent double-immunohistochemistry were described previously (Wang et al., 2014). Antibodies used are listed in the Key Resources Table. Perfused P56 C57BL/6J brains were cryostat sectioned at 25 mm with a final sampling density of 50 mm. Colorometric stained slides were imaged with a 10x objective on a ScanScope (Aperio Technologies). Fluorescent immunohistochemistry slides were imaged on a VS series multichannel fluorescence microscope (Olympus) with a 10x objective. Image series were registered to the 3D average template brain. Data can be found in the Allen Reference Data database (http://connectivity.brain-map.org/static/referencedata). 

## In Situ Hybridization 

All in situ hybridization (ISH) was performed via a standardized production platform that was previously described (Lein et al., 2007). Fresh frozen brains from male P56 C57BL/6J mice were cryostat sectioned at 25 mm with a final sampling density of 200 mm. The colorometric stained slides were imaged with a 10x objective on a ScanScope (Aperio Technologies). Due to the sampling density, images were not registered to the 3D average template brain, but plane matched sections were analyzed side-by-side. Data were selected using AGEA, Fine Structure Search, Gene Search and Differential Search tools in the Allen Mouse Brain Atlas database (http://mouse.brain-map.org), and the specific data selected can be viewed using experiment IDs or links provided in Table S3. Administration of tamoxifen or trimethoprim 

Some Cre driver lines contain regulatable versions of Cre recombinase. Induction of CreERT2 driver lines was done by administration of 0.2 mg/g body weight of tamoxifen (TAM) solution (50 mg/ml in corn oil) via oral gavage once per day for 5 consecutive days. Induction of DHFR-domain containing (dCre or dgCre) driver lines was done by administration of 0.3 mg/g body weight of trimethoprim (TMP) solution (20mg/ml in DMSO/methylcellulose) via oral gavage once per day for 3 consecutive days. 

## Serial two-photon tomography (STPT) imaging 

STPT imaging of mouse brains was performed via a standardized production platform using the TissueCyte 1000 system (TissueVision) coupled with a Mai Tai HP DeepSee laser (Spectra Physics) that was previously described (Oh et al., 2014; Ragan et al., 2012). Single optical plane images 75 mm below the tissue surface were acquired using 925 nm wavelength light through a Zeiss 320 water immersion objective (NA = 1.0), with 250 mW light power at objective. To scan a full tissue section, individual tile images were acquired at a resolution of 2080x2080 pixels, and the entire stage was moved between each tile. Following scanning of a full tissue section, a 100 mm section was cut by vibratome and the imaging process repeated. A total of 140 coronal sections covering the rostralto-caudal extent of the brain, are scanned in red, green, and blue channels using a 20x objective, at an x,y resolution of 0.35 mm per pixel. 

## Average template construction and image registration 

The CCFv3 spatial template is constructed as a population average of 1,675 young adult mouse brains imaged using STPT as part of the Allen Mouse Brain Connectivity Atlas pipeline, following procedures described in detail previously (Kuan et al., 2015). For hemispheric symmetry and to maximize input data used in the averaging process, each hemisphere was reflected across the midline, resulting in a total of 3,350 image series ( = 2 3 1,675 brains). Each image series were first globally registered to the template created for the Allen Mouse Brain Connectivity Atlas data processing pipeline (Kuan et al., 2015; Oh et al., 2014). The process for global registration consists of three steps: (1) coarse registration initialized by matching the image moments of the specimen and the template brain; (2) subsequent rigid (in terms of rotation and translation) registration; and (3) a 12-parameter affine (linear) registration. Each registration step aims to maximize and normalize mutual information of the intensity between the specimen and the template. A multi-resolution scheme was used to first register on smoothed and downsampled versions of the images in order to smooth out details to drive the algorithm to match large-scale shape features. The results from one resolution initializes the next resolution and so on allowing finer details to be matched. After global alignment, the specimens were averaged to create the first iteration of the CCFv3 template which effectively provide initial orientation and scale. An iterative process then (1) registers each specimen deformably to the template and subsequently averages all specimens, (2) computes the average deformation field over all specimens and subtracts this result from the average image created in step (1). This shape and intensity normalized average is then used as the anatomical template in the next iteration. This algorithm continued until the mean magnitude of the average deformation field fell below a certain threshold and stabilized. 

Deformable registration can easily become trapped in a local minimum especially when there is specimen damage and hence a coarse-to-fine approach is essential. In this process, deformations between specimen and template was parameterized as 3D B- splines (order of 3) where the knots are placed on a regularly spaced 3D grid. A coarse grid implicitly only allows smooth/stiff deformations while a finer grid allows more elastic transformations allowing local neighborhoods to be more accurately matched in later stages. The optimization problem (optimal position of the knots) was formulated and solved as a graph labeling problem (Glocker et al., 2008; Tang and Chung, 2007). Instead of considering all the possible continuous moves of each knot, the searching space is discretized into a number of grids represented by labels. This implementation has higher probability to find the global minimum as compared to gradient-based methods. Like in Avants et al. (2008), the registration was performed in both directions and then composed to form the final transform, resulting in a symmetric and invertible deformation field. Cross-correlation is used as the image similarity metric and to speed up computation; it was only evaluated on a small portion of randomly selected voxels. 

e7 Cell 181, 936–953.e1–e9, May 14, 2020 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

All datasets, except for ISH data, were registered and mapped to the 3D average template through global and local alignment as previously described (Kuan et al., 2015; Oh et al., 2014). 

## Generation of the curved cortical coordinate system with Laplace’s Equation 

To delineate isocortical areas, we first drew the outside borders of the isocortex, then marked its inner and outer surface. We applied Laplace’s Equation to the isocortex volume to generate the equidistance fields. The steepest lines perpendicular to the equidistance fields are called streamlines. Streamlines can be used to project data at various locations through the cortical depth, e.g., the maximum density of the average template, transgenic lines or connectivity data labeling, to counterparts on the isocortical surface. The curved cortical coordinate system based on these streamlines was used to delineate isocortical areas. 

## Generation of visuotopic map and virtual callosal labeling 

Visuotopic maps and callosal labeling patterns have been used to define visual cortical areas in mammalian brains. We utilized projection data from the Allen Mouse Brain Connectivity Atlas to generate a visuotopic map and virtual callosal labeling. First, we selected viral tracer injections covering different visual fields in VISp (n = 26, experiment IDs in Table S3). 3D volumes of registered and downsampled projection densities from each experiment were combined to create a color-coded, weighted, source location map. This visuotopic map was used for delineation of higher visual areas in surface views. Second, because callosal labeling has a unique spatial relationship with the higher visual areas (Wang and Burkhalter, 2007), a virtual callosal projection pattern was generated with a set of injections in the isocortex in one hemisphere (n = 107, experiment IDs in Table S3). A projection density map was created by finding, at each voxel, the maximum density value over all injections. A surface view was then generated by considering only signal within 0.1 to 0.5 mm normalized cortical depths and projecting the largest maximum value to the surface. The virtual callosal labeling pattern further restricts boundaries of the higher visual areas, although to a lesser extent than in previous studies likely due to the density of injections (Wang and Burkhalter, 2007; Wang et al., 2012). 

## Annotation of brain structures in 3D 

Brain structures were reconstructed on the average template (at 10 mm isotropic voxel resolution) using the multi-plane and 3D viewers in the annotation software ITK-SNAP (http://www.itksnap.org/pmwiki/pmwiki.php) (Yushkevich et al., 2006). As multiple structures were reconstructed, custom macros for merging and splitting individual files were utilized to facilitate group delineations and adjustments at local and global levels. In the last step, right hemisphere 3D reconstructions were mirrored to the left hemisphere to render a symmetrically complete 3D brain atlas. Additional detailed information on the process implemented for 3D reconstruction of brain structures can be found at the Allen Mouse Brain Connectivity Atlas documentation page (http://help.brain-map.org/display/ mouseconnectivity/Documentation, Mouse CCF, Reference Atlas, Version 3 [2017]) and in Wang et al., (2017). 

## Use of registration deformation fields to estimate structure volumes and to map CCFv3 annotations on individual brains 

The AllenSDK can be used to implement analyses and visualizations not available through the interactive atlas viewer web application. We described two examples of the kinds of tools that one can develop using the CCFv3 and the AllenSDK. First, we provide an example to map and visualize CCFv3 annotations onto the original image space from an individual specimen. This example is demonstrated in a Jupyter Notebook provided at: https://github.com/AllenInstitute/3D-atlas-reverse-mapping. In brief, using the registration parameters obtained for any Allen Mouse Brain Connectivity Atlas specimen through the AllenSDK, a mask of the whole brain in the reference space is mapped back to a specimen’s image space. This is used to identify the sections of the coronal atlas that map to the original coronal imaged section of interest. Next, these sections of the atlas and their corresponding deformation vectors are used to map each annotated voxel from the atlas onto the corresponding imaged section. The atlas and deformation fields have a resolution of 25x25x25 microns, while the imaged sections have a resolution of 0.35x0.35x100 microns. Thus, it is also necessary to convert the scales so that voxels map to the correct pixels in the imaged sections. Since the value of each voxel corresponds to a structure ID in our ontology, individual structures present in the imaged section can be analyzed and visualized. Second, we provide the scripts used to estimate structure volumes in individual brain specimens at: https://github.com/AllenInstitute/CCFv3_Volumetric_Analysis/. The script ‘‘find_structure_surface_mesh.py’’ uses the marching cubes algorithm to produce vertices and faces of a structure’s surface mesh, given its CCFv3 ID. These vertices and faces have already been calculated and stored under the ‘‘/data/’’ directory in the linked repository. Next, the scripts ‘‘find_structure_ volume.py’’ and ‘‘find_structure_surface_area.py’’ take a structure ID and experiment ID and generate the respective volume or surface area. This is achieved by loading the deformation field for an individual experiment from the AllenSDK and applying it to a given structure’s surface mesh. Once a structure is mapped to the specimen’s image space, the volume or surface area is calculated. 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

The CCFv3 average template was constructed from the brains of n = 1,675 mice. Using the Python NumPy package, we calculated descriptive statistics for the estimates of brain and structure volumes across this population, including: mean, standard deviation, and coefficient of variation, as well as mean, median, and lower and upper bounds of the interquartile range relative to the average template volume. Values are provided in Table S4. Most multimodal imaging experiments were n = 1 animal per transgenic line, viral tracer injection into a given source, histology stain or ISH gene probe. All individual animal IDs are provided in Table S3. 

Cell 181, 936–953.e1–e9, May 14, 2020 e8 

Resource 

## **ll** 

## ADDITIONAL RESOURCES 

Detailed protocol descriptions for all procedures can be found at the Allen Mouse Brain Connectivity Atlas documentation page (http://help.brain-map.org//display/mouseconnectivity/Documentation). Additional protocol descriptions for ISH procedures can be found at the Allen Mouse Brain Atlas documentation page (http://help.brain-map.org/display/mousebrain/Documentation). 

e9 Cell 181, 936–953.e1–e9, May 14, 2020 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

## Supplemental Figures 

**==> picture [479 x 417] intentionally omitted <==**

Figure S1. Multimodal Reference Data for Delineation of Isocortical and Subcortical Structures, Related to Figure 2 (A-E) STPT images from five transgenic mouse lines crossed to the Ai14 reporter (red), and used to assist delineation of isocortex and subcortical structures; Rbp4-Cre_KL100 (A), Calb1-T2A-dgCre (B), Scnn1a-Tg3-Cre (C), Glt25d2-Cre_NF107 (D) and Fezf2-CreER. (F-J) STPT images for five examples of connectivity data acquired following injections of viral tracers expressing EGFP injected into thalamic nuclei: LD (F), PO (G), MG (H), VPM (I) and LP (J) and used for delineation of cortical areas. (K-M) Immunohistochemistry with three paired antibody staining: NeuN (in red) and NF-160 (in green) (K), SMI-32 (in red) and Pvalb (in green) (L), and SMI-99 (in red) and Calb1 (in green) (M), reveals cortical and subcortical structures. DAPI (in blue) was used in counterstaining in (K-M). (N) Nissl-staining (in blue) reveals characteristic cytoarchitectures of isocortex and subcortical structures. (O) AChE-staining shows unique labeling in cortical and subcortical structures (in brown). (P-T) Images following in situ hybridization for five example genes with enriched gene expressions in cortical and subcortical structures; Mef2c (P), Wfs1 (Q), Rorb (R), Etv1 (S) and Rprm (T). Scale bar: 1 mm. 

Resource 

## **ll** 

**==> picture [380 x 601] intentionally omitted <==**

**----- Start of picture text -----**<br>
A A B THIC K C DORSAL D<br>M L<br>P THI N VENTRAL<br>MOs<br>SSp<br>VISrl<br>E Z = -100 F SSp Z = 0 G Z = +100<br>500 �m<br>H Z’ =  -100 I Z’ = 0 J Z’ =  +100 K Y’ = 0<br>D<br>A<br>L Z’ = -100 M Z’ = 0 N Z’ = +100<br>500 �m<br>O P<br>Medial Lateral Anterior Posterior<br>Q SSp R<br>S VISrl T<br>U MOs V<br>**----- End of picture text -----**<br>


(legend on next page) 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

Figure S2. Visualization of Isocortical Anatomical Features Using Curved Streamlines, Related to Figure 3 (A-D) Virtual flatmap views summarize and visualize variability of different features across the entire isocortical sheet in 2D. (A) rotational angles of the streamlines, (B) cortical thickness, (C) tilt, and (D) the average template with final parcellations. The flatmap is generated by first constructing a 3D-to-2D mapping, such that the 2D Euclidean distance of every point on the flatmap to a pair of anchor points are the same as their 3D geodesic distance (shortest path along the surface). This process is repeated for another pair of anchor points, with each pair forming an axis of the flattened cortical coordinate space. Stars in (D) show the location of the injection centroids for tracing experiments shown in E-V. (E-G) Three serial coronal STPT images, spaced 100 mm apart, are shown around the approximate center of a viral tracer injection into SSp-n (z = 0, panel F) in the Sim1-Cre_KJ18 line, which labels L5 thick-tufted excitatory neurons. (H-J) These original image data were segmented, downsampled, and registered to the CCF to generate a whole brain voxel-level projection density volume. Images show virtual 100 mm coronal sections from the registered images. (K) shows a sagittal view of the maximum projection density in the registered dataset near the injection site, revealing how the apical dendrites of the infected cells in this location curve in an angle non-orthogonal to the coronal plane (anteriorly). (L-N) shows the path for a subset of computed streamlines in three consecutive 100 mm coronal sections of the average template. Note that these are not complete lines extending from pia to white matter in any single section at this cortical location. (O,P) A 2D image of the cortical sheet can be formed by re-sampling the cortex with the streamlines to normalize for cortical thickness, tilt, and rotation, for the medial-lateral (O) and anterior-posterior (P) axes. Dashed lines are used to indicate a sample of the streamlines in this view, which are now perpendicular to the isocortical sheet (as opposed to curved). (Q-V) Spatially normalized views of the registered dendrite and projection data from tracer injections into SSp-n, VISrl, and MOs in the Sim1-Cre_KJ18 line. 

**ll** 

Resource 

**==> picture [94 x 139] intentionally omitted <==**

**==> picture [94 x 139] intentionally omitted <==**

**==> picture [95 x 139] intentionally omitted <==**

**==> picture [94 x 138] intentionally omitted <==**

**==> picture [94 x 139] intentionally omitted <==**

**==> picture [94 x 138] intentionally omitted <==**

**==> picture [94 x 138] intentionally omitted <==**

**==> picture [94 x 138] intentionally omitted <==**

**==> picture [126 x 81] intentionally omitted <==**

**==> picture [126 x 81] intentionally omitted <==**

**==> picture [125 x 80] intentionally omitted <==**

**==> picture [126 x 80] intentionally omitted <==**

**==> picture [126 x 80] intentionally omitted <==**

**==> picture [125 x 80] intentionally omitted <==**

**==> picture [126 x 81] intentionally omitted <==**

**==> picture [126 x 81] intentionally omitted <==**

**==> picture [125 x 81] intentionally omitted <==**

**==> picture [125 x 80] intentionally omitted <==**

**==> picture [126 x 80] intentionally omitted <==**

**==> picture [126 x 80] intentionally omitted <==**

(legend on next page) 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

Figure S3. Surface Views of Transgenic and Connectivity Data Used for Delineation of Isocortical Areas, Related to Figure 3 (A) Top view of reporter expression from the predominantly layer (L)4 line, Nr5a1-Cre, shows enriched gene expression in subdivisions of SSp, with weaker signal in SSs, VISp and AUDp. (B) Top view from the superficial layer neuron-selective Cux2-CreERT2 line shows more widespread reporter expression compared to Nr5a1, with enriched labeling in VISp and SSp. No labeling was seen in RSPd,v. (C) Top view of reporter expression from the Glt25d2-Cre_NF107 line (in red) shows strong signal in MOs, in the mouth region of MOp and SSp, and in VISpm, VISam, VISa, VISrl and VISal. An MD thalamic tracer injection (in green) shows strong axon terminal labeling in FRP, ACAd, and MOs, and moderate labeling in RSPagl, RSPd, VISa and VISam. (D) Top view of reporter expression in the Tacr1T2A-Cre line (in red) shows strong expression in PL, ACAd, FRP, MOs, and the mouth region of MOp. Labeled projections following tracer injection into LD of thalamus shows strong to moderate inputs to RSPd, VISpm, VISam, VISa, VISrl, VISal, and parts of SSp. (E) Top view of reporter labeling from the Penk-IRES2Cre line shows enriched gene expression in RSPd, but not in RSPv and RSPagl. (F) Top view of reporter expression from the Calb2-IRES-Cre line in red, shows strong labeling in RSPv, RSPagl, SSp-ll and SSp-tr, but weaker signal in neighbors RSPd, SSp-ul, SSp-bfd and VIS. Another MD tracer injection (in green) shows dense axonal projections to PL. (G) Top view of reporter expression from the predominantly L6 line, Syt6-Cre_KI148 in red, shows denser expression in retrosplenial and motor areas. A cortical surface view of axons labeled via tracer injection into the thalamic nucleus PO is also overlaid (in green). These projections show SSs which receives more dense terminals compared to neighboring SSp-bfd. (H) Top view of reporter expression from the L5 line, Tlx3-Cre_PL56 in red, shows enriched gene expression in higher visual areas, compared to neighboring primary visual and somatosensory areas. In green, tracer data from an MD thalamic nucleus injection reveals anterior cingulate as it receives denser projections compared to retrosplenial areas. (I) The lateral surface view also reveals primary sensory areas as inherently brighter regions compared to other cortical areas in the average template. ‘‘D’’ is dorsal, ‘‘A’’ is anterior. (J) Lateral view of reporter expression in the L5 line Rbp4-Cre_KL100 shows strongest signal in frontal cortex; MOs, AId and AIv, with moderate signal in other areas including SSs, AUD, Alp, PERl, VISpor and VISpl. (K) Lateral view of reporter expression in line Grp-Cre_KH288 (in red) shows strong signal in MOs, Ald and Alv. Cortical projections labeled following viral tracer injection into thalamic nucleus RE (in green) shows densest terminations in Alv, Alp, PERl, ECT, VISpor and VISpl. (L) Lateral view of reporter expression in line Pvalb-IRES-Cre shows strong signal in VISp, SSp and AUDp, with weaker labeling in neighboring higher visual and auditory areas, SSs, MOp and MOs. Cortical projections labeled following viral tracer injection into thalamic nucleus MD (in green) shows dense input to Ald, and weaker projections to Alp and MOs. (M) Lateral view of reporter expression in line Calb2-IRES-Cre shows strong signal in VISC, TEa and ECT, with moderate signal in Al, AUDv, subdivisions of SSp and VISp. (N) Lateral view of reporter expression in line Crh-IRES-Cre reveals VISp, AUDp, and SSp. (O) Lateral view of reporter expression in line Glt25d2-Cre_NF107 (in red) shows strong signal in VISC, MOs and the mouth region of MOp, and moderate signal in VISpm, VISam, VISa, VISrl and VISal. Cortical projections labeled following viral tracer injection into thalamic nucleus CM (with minor infection in VPLpc) shows strong input (in green) to VISC and Ald, and moderate input to PERl. (P) Lateral view of reporter expression in transgenic line Esr2-IRES2-Cre (in red) shows strongest signal in SSs and Alp, with moderate labeling in Alv, AUDd, VISpor and VISpl. Cortical projections labeled following viral tracer injection into thalamic nucleus VM (with minor infection in VAL) show strong input to MOp and VISC, and moderate input to MOs, Ald and GU. (Q) Lateral view of reporter expression in transgenic line Slc17a8-IRES2-Cre shows strong signal in GU, SSp-ll, and moderate signal in SSs, Ald, Alv, AUDd, VISpor, VISl, VISpl and VISli. (R) Lateral view of reporter expression in the L5 transgenic line Sim1-Cre_KJ18 (in red) shows strongest signal in Alv, and moderate signal in Ald, Alp and PERl. Cortical projections labeled following viral tracer injection into thalamic nucleus VPMpc (in green) shows dense axon terminals in GU. (S) Lateral view of reporter expression in transgenic line Tacr1-T2A-Cre (in red) shows strong signal in Alv, Ald and Alp, and moderate signal in GU, MOs, MOp and PERl. Cortical projections labeled following viral tracer injection into VISp show densely labeled axons in VISpor, VISl, VISli, VISpl, VISal and VISrl, and sparser axons in SSp-bfd, TEa, ECT and AUD areas. (T) All 33 isocortical areas delineated in the lateral surface view. Solid white lines represent areal borders. For abbreviations see Table S2. Scale Bar:1mm. 

**ll** 

Resource 

**==> picture [481 x 400] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Dorsal view B Lateral view C<br>D E F G H IC<br>AQ<br>VL AQ<br>V4<br>V4 c<br>V3 AQ<br>c<br>VL V4<br>D V3 D<br>chp<br>A P A A<br>D E H<br>VL<br>AQ<br>VL<br>V3<br>int V4 icp<br>mlf VIIn<br>ac<br>ac c sptV<br>V3 sptV<br>ac sV<br>J K L M<br>VL<br>AQ<br>VL<br>V3 V4 icp<br>int VIIn<br>ac<br>sptV<br>ac V3 ac sV sptV<br>mlf<br>**----- End of picture text -----**<br>


**==> picture [93 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
N<br>VL<br>**----- End of picture text -----**<br>


**==> picture [92 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
O<br>VL<br>V3<br>V3<br>**----- End of picture text -----**<br>


**==> picture [92 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
P<br>AQ<br>**----- End of picture text -----**<br>


**==> picture [92 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Q<br>V4<br>**----- End of picture text -----**<br>


**==> picture [92 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
R<br>c<br>800 �m<br>**----- End of picture text -----**<br>


Figure S4. Delineation of Ventricles and Related Structures, Related to Figure 5 (A) Dorsal and (B) lateral views of the whole brain ventricular system reconstructed in 3D. Ventricles are labeled (VL: lateral ventricle, V3: third ventricle, AQ: cerebral aqueduct, V4: fourth ventricle, c: central canal). Dashed lines indicate level of coronal section shown in D-R. (C) Nissl-stained sagittal section near the midline showing the AQ, 4V, and choroid plexus (chpl). Note the ventricle-like AQ just below the inferior colliculus (IC). (D-H) Virtual coronal sections of the average template. Differential contrast features reveal ventricles (dark/black), although they are similar in intensity to many putative fiber tracts (lower case abbreviations; ac: anterior commissure, int: internal capsule, mlf: medial longitudinal fascicle, sV: sensory root of the trigeminal nerve, VIIn: facial nerve, icp: inferior cerebellar 

(legend continued on next page) 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

peduncle, sptV: spinal tract of the trigeminal nerve). (I-M) Coronal Nissl-stained sections at corresponding locations to above template images show each ventricle location and shape and contains features that more easily distinguish white matter tracts. (N-R) Coronal STPT images of tdTomato reporter expression from the Slc17a8-IRES2-Cre line, which labels the ependymal cells lining the ventricles and central canal. Integration of these data types enabled the 3D reconstruction of ventricles and associated structures directly on the template volume. For all abbreviations see Table S2. Scale Bar: 800 mm from D-R. 

**ll** 

Resource 

**==> picture [481 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>contra to injected eye<br>shell<br>shell<br>ip<br>core core<br>ipsi to injected eye<br>RGC axons  Lateral view of LGd Lateral view of LGd<br>E I J K<br>sh sh co<br>ip ip<br>ip ip sh<br>co co<br>Thy1 ipsi RGC axons<br>F L M N<br>sh sh co<br>sh ip<br>ip ip sh<br>co<br>co<br>Calb2-IRES-Cre;Ai14<br>Calb2-IRES-Cre;Ai14 Thy1 ipsi RGC axons<br>G O P Q<br>sh sh co<br>ip ip<br>co ip ip sh<br>co co<br>Cart1 RGC axons<br>Kcng4 RGC axons Kcng4 RGC axons<br>H R S T<br>co<br>sh sh LGd<br>ip ip sh<br>co LGd ip ip sh<br>co LGd co<br>300 �m<br>Cart1 RGC axons<br>**----- End of picture text -----**<br>


## Figure S5. Delineation of Three LGd Subdivisions, Related to Figure 4 

(A,B) Maximum intensity projection (lateral and dorsal view) of retinal ganglion cell (RGC) axons labeled with viral tracer into the left eye of a Thy1-Cre driver mouse to reveal central projections brain-wide. Dashed lines indicate coronal, sagittal, and horizontal levels in E-T. (C,D) Lateral views of the final reconstruction of LGd into 3 subdivisions; shell, core, and ipsilateral projection zone (ip). The ip, located medial and ventral to the shell, and dorsal to the core is shown in (D) after making the shell partially transparent. (E-H) Coronal STPT images through the LGd, showing tdTomato reporter expression in a Calb2-IRESCre mouse (F) or RGC axonal projections labeled from different Cre driver transgenic lines as indicated. Ipsilaterally-projecting Thy1-Cre+ RGCs terminate in a discrete location within LGd (ip; E, section was flipped to match hemisphere shown in F-H). The ip is also visible as the area with sparse to no input from the contralateral retina in the Kcng4-Cre and Cart-Tg1-Cre lines (G,H). Calb2-IRES-Cre reporter expression is enriched in the shell region at the dorsolateral surface (F). The shell region also contains direction-selective RGC axons labeling in the Cart1-Tg1-Cre line (H), whereas the relatively denser labeling of Kcng4-Cre+ alpha-RGC axons in ventromedial LGd defines the core (G). (I-K) Virtual single plane sections (coronal, sagittal, horizontal) of the average template through the LGd. The dorsolateral edge of the LGd is the brightest part in the template, but subdivisions are not otherwise recognizable. (L-N) The transgenic and anterograde tracing Cre line experiments in E and F were registered and overlaid with the average template. 3D views of the reference data provided critical assistance in the non-coronal planes, in this case, further supporting the delineations of borders between LGd-sh and LGd-ip. (O-Q) The two anterograde tracer datasets in G and H were registered to and visualized in the average template volume, which helped to further define the LGd-sh and LGdco. (R-T) Integrating information from the above multimodal reference data, the LGd was divided into three sub-regions shown here in coronal, sagittal, and horizontal planes. For all abbreviations see Table S2. Scale Bar: 300 mm from E-T. 

**ll** 

## Resource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [420 x 554] intentionally omitted <==**

**----- Start of picture text -----**<br>
A  B<br>C<br>D  E  F<br>G  H  I<br>**----- End of picture text -----**<br>


Figure S6. The Interactive Ontology and Viewer for the Coronal Mouse Brain Atlas, Related to Figure 7 (A) An interactive hierarchal tree shows the complete ARA ontology. Acronyms and full structure names in the ontology are in black text for the structures annotated in CCFv3; structure names shown in light gray italics indicate structures that exist in the ARA ontology, but were not delineated for CCFv3. Clicking on any acronym in the side bar of the ontology tree highlights the corresponding structure in the interactive 2D atlas (and vice versa). For example, ‘‘PO’’ is highlighted in (A), and this structure is visible in B and C (purple). (B) One of 132 2D atlas coronal plates. (C) The coronal image of the average template corresponding to the atlas plate and annotations in B. (D-I) Images of an anterograde viral tracing experiment with projections to PO (D), Nissl (E), AChE (F), antibodies against NeuN and NF160 (G), Calb1 and SMI-99 (H), and Pvalb and SMI-32 (I) are shown synced with the interactive 2D atlas plate and the average template image shown in B,C. To 

(legend continued on next page) 

Resource 

## **ll** 

sync images, the user defines the alignment position on the data image by placing it in the center the viewing window. The ‘‘sync’’ service translates this image location into a CCFv3 coordinate using databased transforms. The service then determines the best matched image position within the atlas sections. The atlas view is updated such that the best match location is in the center of view and at a zoom level similar to the data view. Annotations in the 2D atlas can thus be compared side-by-side with these registered multimodal reference datasets. 

**ll** 

Resource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [324 x 408] intentionally omitted <==**

Figure S7. CCFv3 Compared with CCFv2, Related to Figure 7 (A-B) In coronal sections, borders between regions are smooth in both CCFv2 and CCFv3, as regions were delineated in coronal planes for CCFv2. (C-D) Improvements based on 3D reconstructions are obvious in sagittal planes. (E-F) An angled dorsolateral view shows the borders of cortical areas in CCFv2 (E) compared with those in CCFv3 (F). In addition to the ‘‘jaggedness’’ of borders, there are also notable differences in shape, size, and number of annotated structures between CCFv2 and CCFv3. For example, we added three higher visual areas in the isocortex for CCFv3. Because of the different delineation approaches and number of structures, we strongly recommend users compare areas of interest between atlases carefully. Dashed lines in E and F indicate the approximate coronal and sagittal levels shown in A-D. (G-H) For public facing data products (i.e., the Allen Brain Explorer), the structure volume meshes derived from annotation tools in ITK-SNAP in E,F were rendered and used for interactive 3D display purposes. For abbreviations see Table S2. Scale bar: 1 mm from A-D. 

