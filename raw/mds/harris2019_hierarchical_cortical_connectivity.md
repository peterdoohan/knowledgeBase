Article 

## **Hierarchical organization of cortical and thalamic connectivity** 

|https://doi.org/10.1038/s41586-019-1716-z<br>Received: 16 April 2018<br>Accepted: 24 September 2019<br>Published online: 30 October 2019|**Julie A. Harris1,5*, Stefan Mihalas1,5, Karla E. Hirokawa1, Jennifer D. Whitesell1, Hannah Choi1,2, **<br>**Amy Bernard1, Phillip Bohn1, Shiella Caldejon1, Linzy Casal1, Andrew Cho1, Aaron Feiner1, **<br>**David Feng1, Nathalie Gaudreault1, Charles R. Gerfen3, Nile Graddis1, Peter A. Groblewski1, **<br>**Alex M. Henry1, Anh Ho1, Robert Howard1, Joseph E. Knox1, Leonard Kuan1, Xiuli Kuang4, **<br>**Jerome Lecoq1, Phil Lesnar1, Yaoyao Li4, Jennifer Luviano1, Stephen McConoughey1,**<br>**Marty T. Mortrud1, Maitham Naeemi1, Lydia Ng1, Seung Wook Oh1, Benjamin Ouellette1,**<br>**Elise Shen1, Staci A. Sorensen1, Wayne Wakeman1, Quanxin Wang1, Yun Wang1, Ali Williford1, **<br>**John W. Phillips1, Allan R. Jones1, Christof Koch1 & Hongkui Zeng1**|
|---|---|
||The mammalian cortex is a laminar structure containing many areas and cell types<br>that are densely interconnected in complex ways, and for which generalizable<br>principles of organization remain mostly unknown. Here we describe a major<br>expansion of the Allen Mouse Brain Connectivity Atlas resource1, involving around a<br>thousand new tracer experiments in the cortex and its main satellite structure, the<br>thalamus. We used Cre driver lines (mice expressing Cre recombinase) to<br>comprehensively and selectively label brain-wide connections by layer and class of<br>projection neuron. Through observations of axon termination patterns, we have<br>derived a set of generalized anatomical rules to describe corticocortical,<br>thalamocortical and corticothalamic projections. We have built a model to assign<br>connection patterns between areas as either feedforward or feedback, and generated<br>testable predictions of hierarchical positions for individual cortical and thalamic<br>areas and for cortical network modules. Our results show that cell-class-specifc<br>connections are organized in a shallow hierarchy within the mouse corticothalamic<br>network.|



Cognitive processes and voluntary control of behaviour originate in the cortex. To understand how incoming sensory information is processed and integrated with past experiences and current states in order to generate appropriate behaviour requires knowledge of the anatomical patterns and rules of connectivity between cortical areas. Connectomes—complete descriptions of brain wiring[2] —exist at different levels of spatial granularity, from single cells to populations of cells and entire areas (micro-, meso-, and macro-scale). Common organizational features of macro- and meso-scale cortical connectivity have been distilled across data sets[1,3–7] , often using graph theory approaches to describe network architecture[8] . For example, cortical areas have unique patterns of connections (‘fingerprints’), connection strengths follow a log-normal distribution spanning more than four orders of magnitude[1,4] , and the organization of cortical areas is modular, with distinct modules corresponding to specific functions[3,9–11] . 

The concept of hierarchical organization[12,13] is important for understanding the cortex, and has inspired the development of neural network methods in deep machine learning[14] . A hierarchy of cortical areas was first derived by mapping anatomical patterns of corticocortical (CC) connections onto feedforward and feedback directions. In primate, - feedforward connections were characterized by dense axon termina tions in layer (L)4 of the target area, and feedback connections as dense terminals in superficial and deep layers (avoiding L4)[12,15] . Differences in 

the layers of origin are also associated with feedforward and feedback connections[12,16] . It is still unclear whether the concept of a cortical hierarchy, which has been derived largely from sensory systems, can be applied globally across the entire cortex, and how it arises from connections made by different classes of neurons. Each cortical region comprises distinct types of excitatory neurons that are largely organized by layers, but also by long-distance projection patterns: intratelencephalic (IT) in L2–L6, pyramidal tract (PT) in L5, and corticothalamic (CT) in L6[17,18] . 

Thalamic nuclei make important contributions to cortical function. They serve as a ‘relay’ for primary sensory information, and are well positioned to influence cortical information processing through reciprocal or transthalamic loops[19,20] . Thalamocortical (TC) projection neurons are classified into three major classes[21–23] : core, intralaminar, and matrix. Like CC projections, feedforward and feedback rules have been proposed for TC and CT projections. Core projections (to L4) are described as ‘driver’ (feedforward) and matrix projections (to L1) as ‘modulator’ (feedback)[19] . For CT connections, input from L6 is considered feedback, and from L5 feedforward[20] . 

We hypothesize that a unifying hierarchical organization across the entire cortex and its major input structure, the thalamus, is governed by a set of anatomical rules for CC, CT and TC connections. By using diverse Cre driver mouse lines to selectively label cells from different cortical layers and classes[24–27] , we have substantially expanded the 

1Allen Institute for Brain Science, Seattle, WA, USA. 2University of Washington, Department of Applied Mathematics, Seattle, WA, USA. 3Laboratory of Systems Neuroscience, National Institute of Mental Health, Bethesda, MD, USA.[4] Wenzhou Medical University, Wenzhou, P. R. China.[5] These authors contributed equally: Julie A. Harris, Stefan Mihalas. *e-mail: julieha@alleninstitute.org 

Nature | Vol 575 | 7 November 2019 | **195** 

**==> picture [47 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [475 x 308] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Cortical map:top-down  b vlORB l Cortical map:flat c Injections d Mouse line Layer  [Projection] class<br>m FRP d [v] C57BL/6J L2–L6 IT PT CT<br>AI Emx1 L2–L6 IT PT CT<br>MOs PL Cux2 L2/3 IT<br>MOp m MOs MOp m p Sepw1 L2/3 IT<br>ul Nr5a1 L4 IT<br>ll n ACA ul n SSs Scnn1a-Tg3 L4/5 IT<br>vRSPd pmamtraVISSSpp rlbfdplallporliAUDpod v vd RSPd llamtra SSpVISprlbfd all podliplAUDpporv RorbRbTlx3Chrna2Efr3aSim1A93p-4Tg1 L4/5L5L5L5L5L5L5 ITIT PTITPTPTPTPT<br>Ntsr1 L6 CT<br>e Target Syt6 L6 CT<br>1.00.80.60.4 QQ shuffled1.3 Prefrontal Lateral Somatomotor Visual Medial Aud. f g<br>0.2<br>� :0 1.0 2.0FRP -2 AId SSp - m<br>ACAd<br>ORBmACAvORBlILAPL Somatomotor FRP AIv MOp GUSSp - n<br>ORBvlVISCAIdAIpGUAIv -3 Medial VisualAud PL ORBl MOs SSp - ul VISC<br>SSp-bfdPERIECTSSsTEa ILA ORBmORBvl SSp - ll SSp - unSSs AIp<br>SSp-tr<br>SSp-unSSp-mSSp-ulSSp-nSSp-ll -4 ACAv ACAd SSp - tr SSp - bfd<br>VISalMOpMOsVISpVISl RSPagl VISamVISa AUDd ECT PERI<br>VISporVISamVISplVISrlVISaVISli -5 RSPvRSPdVISpm VISrlVISliVISalAUDpoAUDpTEa AUDv<br>VISpm VISl<br>RSPaglRSPd VISpor<br>AUDdRSPv VISp VISpl<br>AUDp<br>AUDpo<br>AUDv -6<br>TEa<br>TEa<br>GU<br>pm<br>Prefrontal<br>Lateral<br>PL<br>agl<br>un<br>un<br>VISC<br>SSs PERl<br>ECT<br>agl<br>) Q<br>FRP ACAd ACAvPL ILA ORBl ORBm ORBvl AId AIv AIpGU VISC TEa PERI ECT SSs SSp-bfdSSp-trSSp-llSSp-ulSSp-unSSp-nSSp-mMOpMOs VISal VISl VISpVISplVISli VISporVISrl VISa VISam VISpmRSPaglRSPd RSPv AUDd AUDpAUDpoAUDv<br>Modularity (<br>Source<br> normalized connection density<br>10<br>log<br>**----- End of picture text -----**<br>


**Fig. 1 | Cortical tracer experiments and network modularity. a** , Top-down view of the right cortical hemisphere in CCFv3. **b** , A virtual cortical flat map shows all 43 annotated areas. The white dotted line indicates the boundaries of what is visible in **a** . **c** , Cortical injection locations plotted on the flat map. **d** , Key summarizes layer and projection class selectively for 15 mouse lines. The colour code is also used in **c** ; experiments in lines not listed are coloured dark grey. **e** , Matrix shows ipsilateral normalized connection densities between 43 cortical areas. Top left corner: the modularity metric ( _Q_ ) and _Q_ shuffled are plotted for each _γ_ level. Colours to the left of each row indicate community structure at 

_γ_ = 0–2.5. Community structure was determined independently for each value of _γ_ , but colours were matched to show how communities split as _γ_ increases. Columns are coloured by the six modules identified at _γ_ = 1.3. **f** , Cortical regions on the flat map colour-coded by module affiliation at _γ_ = 1.3. **g** , Network diagram shows ipsilateral CC connections using a force-directed layout algorithm. Nodes are colour-coded by module. Edge thickness shows relative normalized connection density. Edges between modules are coloured as a blend of the connected node colours. For all abbreviations of structure names, see Supplementary Table 3. 

Allen Mouse Brain Connectivity Atlas resource (http://connectivity. brain-map.org[1] ), adding 1,256 new tracing experiments. Our findings follow analyses of projection patterns spanning nearly the entire mouse cortex and thalamus, and show how these patterns relate to layer and cell class. We test the above hypothesis by building a computational hierarchical model using anatomical rules derived from observations of axon termination patterns. Our results show that the mouse cortex and thalamus form an integrated hierarchical organization. 

## **Cre drivers for cortical projection mapping** 

Our goal for expanding the Allen Mouse Brain Connectivity Atlas[1] was to create a map of all interareal projections that originate from neurons of different cell classes within a given source. Here, we used 50 mouse lines (wild-type C57BL/6J mice and 49 Cre driver lines) for cortical projection mapping. We injected Cre-dependent enhanced green fluorescent protein (EGFP) or synaptophysin–EGFP viral tracers to selectively trace axons from Cre[+] neurons (see Extended Data Fig. 1a–c for virus comparison). Using our high-throughput imaging and informatics pipeline approach, we produced 1,081 cortical tracer experiments suitable for analyses (see Methods and Supplementary Tables 1, 2). To visualize coverage, we plotted injection locations for all experiments on a cortical surface flat map of the 3D Allen Common Coordinate Framework reference atlas (CCFv3, Fig. 1a–c). High-resolution image series, visualization tools, and quantification of injection sites and brain-wide targets are accessible through our data portal (http://connectivity.brain-map.org). 

We inspected brain-wide axonal projection patterns to manually classify each experiment into one of six layer and projection classes: (1) IT PT CT: labelled axons originate from all source layers and terminate in all target regions (ipsilateral and contralateral cortex and striatum, thalamus, and midbrain, pons and/or medulla); (2) IT PT: labelled axons observed in all target regions, but the injection site did not include L6 neurons; (3) IT: labelled axons restricted to ipsilateral and contralateral cortex and striatum; (4) PT: labelled axons projected ipsilaterally and subcortically; (5) CT: labelled axons project almost exclusively to thalamus from L6; and (6) local: no (or few) long-distance axons present (Extended Data Fig. 2a, Supplementary Table 1). Manual assignment to projection class was consistent with the results of unsupervised clustering (Extended Data Fig. 2b–d) and previous characterizations[25] . We also characterized layer selectivity in the source for each Cre line on the basis of injection sites (Extended Data Fig. 2e). 

From these data, we chose a core set of 15 lines that we used to comprehensively map connectivity from different projection neuron classes across cortical layers (Fig. 1d), resulting in 849 experiments used for subsequent analyses of CC and CT projections. We did not identify a suitable Cre line for L6 IT[28] . 

## **Corticocortical connectivity modules** 

Previous network analyses revealed a modular community structure in the mouse brain, including in the isocortex[9] . To determine whether our data set demonstrated a similar network architecture, we constructed 

**196** | Nature | Vol 575 | 7 November 2019 

an ipsilateral cortical connectivity matrix (Fig. 1e) using a data-driven model based on wild-type mice[29] . We analysed the network structure of this matrix using the Louvain algorithm[30] , which maximizes a modularity metric ( _Q_ ) to identify groups of nodes (cortical areas) that are most densely connected to each other compared to a randomized network. To identify stable modules, we systematically varied the spatial resolution parameter, _γ_ , from 0 to 2.5, measured _Q_ at each value, and compared the results to a shuffled network. The mouse cortex was modular ( _Q_ > _Q_ shuffled) for every value of _γ_ above 0.3. We chose to focus on the six modules identified at _γ_ = 1.3 ( _Q_ = 0.36), where the difference between _Q_ and _Q_ shuffled was maximal (0.22 ± 0.017, mean ± s.d.). We named these six modules for the areas assigned to each: prefrontal, lateral, somatomotor, visual, medial, and auditory. Even with substantial community structure, intracortical connections are dense between modules (Fig. 1f). The Louvain algorithm parameterizes edge strength only, with no constraint for spatial arrangement of nodes, but there is a clear spatial component, in that neighbouring areas usually belong to the same module (Fig. 1g). We directly tested the degree to which spatial proximity affects modularity by fitting a power-law to the distance component of the ipsilateral connectivity matrix, and then analysing the resulting residual matrix using the Louvain algorithm (Extended Data Fig. 3). Although fewer modules were present after accounting for distance, regions within them were generally still anatomically adjacent. 

## **Corticocortical projections by layer or class** 

To investigate the contributions of distinct cell classes within each area to CC projections, we compiled 43 groups of spatially matched experiments, each having a ‘complete’ membership roster representing all layer classes (L2/3 IT, L4 IT, L5 IT PT, L5 IT, L5 PT and L6 CT) plus a wildtype or _Emx1_ IT PT CT data set (note that Cre mouse lines are referred to by gene symbol; for example, _Emx1_ is _Emx1-IRES_ -Cre). Projection class was confirmed for each experiment. These 43 anchor groups, composed of 364 experiments, represent 25 out of 43 CCFv3 cortical areas (Fig. 2a–d, Supplementary Table 4). From any given source, CC projections labelled from these Cre lines had similar overall patterns, but _Rbp4_ (L5 IT PT) consistently appeared to show the most extensive projections (Fig. 2e). Intracortical projections were labelled from all layers (L2/3–L6). The identification of interareal projections from L4 was unexpected, given canonical circuit descriptions, but is not without recent precedent[28,31] . To confirm that IT projections could truly be attributed to L4 neurons, we reconstructed the complete dendritic and axonal morphology of 25 sparsely labelled neurons following wholebrain fluorescence micro-optical sectioning tomography (fMOST) imaging[32] . We identified three classes of L4 neuron using morphological criteria[33] , and confirmed that many, but not all, individual L4 cells sent axons to other cortical areas (Extended Data Fig. 4). 

To make quantitative comparisons across Cre lines, we first manually identified true positive and negative connections for each experiment in the anchor groups (43 ipsilateral and 43 contralateral targets in 364 experiments, giving 31,304 connections checked; Supplementary Table 4). We noted when a target contained only fibres of passage, and considered it a true negative. Using automated segmentation and registration to CCFv3, we generated a weighted connectivity matrix (using normalized projection volume (NPV); see Methods) for each Cre line (wild-type and _Emx1_ were merged; Extended Data Fig. 1e–g), and applied the true positive mask to remove true negative connections (Fig. 2f). We selected only one anchor group per cortical region for visualization if there was a significant, positive correlation between _Rbp4_ replicates (Spearman _r_ > 0.8), resulting in 27 groups; 25 unique areas and two locations in the secondary motor area and supplemental somatosensory area. 

Overall, the CC matrices revealed several features of layer- or class-specific connectivity in terms of the number and specificity of 

connections. The average ‘out-degree’ (number of targets; Fig. 2g) from _Rbp4_ was larger in both hemispheres than from any other Cre line, except for _Tlx3_ on the contralateral side. L5 PT and L6 CT lines had the fewest targets in both hemispheres, followed by the L2/3, L4, and L5 IT lines. For every line, there were fewer (or no) contralateral compared to ipsilateral connections. 

We measured the amount of overlap between the specific set of cortical targets contacted in each experiment and its _Rbp4_ anchor (Fig. 2h). Wild-type/ _Emx1_ projections went to about 80% of the same targets as _Rbp4_ axons. A roughly equal number of targets was unique to either wild-type or _Emx1_ (12.7 and 7%, respectively), perhaps owing to injection variability or differences in viral tracers. For every other Cre line, essentially all projections went to a subset of L5 _Rbp4_ targets (Fig. 2h, fewer than 5% of targets unique to any line). Within L5, IT cells had the most overlap with _Rbp4_ targets, whereas PT cells had the least (Fig. 2e, f). Most of the differences between L2/3 and L5 resulted from the presence of fewer projections to the contralateral hemisphere from L2/3 (Fig. 2g). 

## **Thalamocortical projections by source or class** 

To investigate TC connections, we selected 81 out of 254 injection experiments in wild-type and Cre driver lines on the basis of the extent of anatomical restriction to a single region. These experiments covered 29 out of 44 thalamic nuclei in CCFv3 (Supplementary Tables 1, 2, Extended Data Fig. 5a). Most thalamic nuclei that are known to contain cortically projecting neurons were included, except for the posterior triangular thalamic nucleus (PoT), suprageniculate nucleus (SGN), anterodorsal nucleus (AD), and interanteromedial nucleus of the thalamus (IAM)[23] . 

We visually inspected the brain-wide axonal projection patterns and classified these 81 experiments using previous definitions for core, matrix and intralaminar TC projection classes[18,23] . Each experiment was manually assigned to one of four groups, or ‘none’ if no TC axons were observed (Fig. 3a): (1) core: labelled axons were observed in a small number of cortical targets with axons predominantly ramifying in L4; (2) intralaminar: labelled axons were predominantly observed in the striatum, with weak or diffuse cortical axons present; (3) matrix (focal): labelled axons targeted L1 in a small number of nearby targets; and (4) matrix (multiareal): labelled axons targeted L1 in a more distributed set of targets. Most thalamic nuclei could be assigned to one class, although this does not preclude regions having mixed classes (Fig. 3b, Supplementary Table 1). Only three regions (all primary sensory thalamic nuclei) were assigned core-type projections—the ventral posterolateral nucleus (VPL), ventral posteromedial nucleus (VPM), and dorsal part of the lateral geniculate complex (LGd)[19,21] . Most thalamic sources were matrix or intralaminar. 

Unlike the cortex, which is organized into distinct projection classes within layers of a single region, thalamic nuclei contain relatively homogenous populations of cortically projecting neurons[34] . As we used multiple Cre lines and wild-type mice for thalamic injections (Supplementary Table 1), we generated a TC connectivity matrix to compare the patterns of individual experiments (Fig. 3f). We manually identified true positive and true negative (including fibres of passage) connections for cortical targets (43 ipsilateral and 43 contralateral targets in 81 experiments, giving 6,966 connections manually checked; Supplementary Table 5), and performed hierarchical clustering on the masked weights (Fig. 3c). Most sources with multiple injections clustered together, even those from different lines. Exceptions included the mediodorsal nucleus (MD), where further analyses showed that precise location mattered more than Cre line (MD-1 experiments are in mid-to-caudal MD, MD-2 experiments are in the rostral portion). The specific patterns of cortical areas targeted by each cluster of thalamic nuclei were remarkably like the cortical modules defined by CC connections (Extended Data Fig. 5b). 

Nature | Vol 575 | 7 November 2019 | **197** 

## Article 

**==> picture [377 x 386] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b MOs  c SSp-m d VISp f Ipsilateral targets Contralateral targets<br>L1 L1 L1 PFC Lateral SoM Vis Med Aud PFC Lateral SoM Vis MedTemAudp<br>MOs SSp - m L2/3 L2/3L4 L2/3L4<br>L5 L5<br>L5<br>VISp L6 L6 L6<br>e<br>Cux2 -IRES-Cre MOs<br>L2/3 IT SSp - m<br>VISp<br>Scnn1a- Tg3-Cre<br>L4 IT<br>Nr5a1 - Cre<br>Tlx3 -Cre_PL56<br>L5 IT<br>Rbp4 -Cre_KL100<br>L5 IT PT<br>A93 -Tg1-Cre<br>L5 PT<br>Ntsr1 -Cre_GN220<br>L6 CT<br>Shared Rbp4 -Cre only Other line only<br>g 40 h 1.0<br>35 0.5<br>0.8<br>30<br>25 0.6<br>20 –1.5<br>15 0.4<br>10<br>0.2<br>5<br>–3.5<br>0 Ipsi Contra 0.0<br>Hemisphere Mouse line<br>Emx1<br>C57BL/6J/<br>L2/3 IT<br>L4 IT<br>L5 IT<br>L5 IT PT<br>L5 PT<br>Avg.out-degree (CC)<br>Fraction of postive targets  normalized projection volume L6 CT<br>10<br>Log<br>**----- End of picture text -----**<br>


**Fig. 2 | Corticocortical projection patterns by layer and class. a** , Forty-three groups of experiments, spatially matched to one _Rbp4_ anchor (green dots). Most group members were less than 500 μm from the anchor (median, 296 μm). Green circles indicate the variance in distance to _Rbp4_ for each group. **b** – **e** , Data from three groups. **b** – **d** , Serial two-photon tomography (STPT) images at the centre of each injection site per Cre line were manually overlaid by finding the best match between the pial surface (top) and white matter boundary (bottom), then pseudocoloured by line. Scale bar, 250 μm. **e** , Topdown views of CC projections for spatially matched experiments. **f** , Directed, weighted connectivity matrices (27 × 86) for seven mouse lines: wild-type and the six Cre lines in **e** . Each row contains the log10-transformed NPVs from a single experiment in one of 27 source areas. Columns show cortical target 

regions. Rows and columns follow the same order in each matrix. White boxes highlight regions in the same module. True negatives and passing fibres were masked out (dark grey). Rows for which an experiment was missing (often because of low Cre expression) are light grey. The colour map ranges from 10[−3.5] to 10[0.5] log NPV. It is truncated at both ends. **g** , Mean out-degrees (± s.e.m.) across all sources for each Cre line plotted for ipsilateral and contralateral cortex. **h** , The fraction of true positive targets shared by each line with its _Rbp4_ anchor is shown in the box plot (grey). The fraction of positive targets unique to _Rbp4_ (green) or to the line indicated (white) are also shown. Box plots show median and interquartile range (IQR). Whiskers show minimum and maximum values. 

## **Corticothalamic projections by layer or class** 

We also used the _Rbp4_ anchored cortical experiments to generate weighted CT connectivity matrices. We again identified true positive and true negative connections, this time for all thalamic targets (44 ipsilateral and 44 contralateral targets in 256 experiments, giving 22,528 CT connections manually checked; Supplementary Table 6). As expected from previous publications, most cortical projections to the thalamus were observed in L5 PT and L6 CT Cre lines (and wild-type mice), with minimal to no true positive connections from L2/3, L4, and L5 IT lines (Supplementary Table 6). We focused our subsequent analyses on _Rbp4_ to represent L5 PT, given its more comprehensive coverage. Connection strengths were significantly correlated between the L6 CT lines _Ntsr1_ and _Syt6_ ( _P_ < 0.0001, Fig. 4d), so we averaged or merged these data (Fig. 4b). 

The L5 and L6 CT matrices appear similar, but have quantitative differences (Fig. 4a, b). Many thalamic targets receive inputs from both 

layers (Fig. 4c), and the connection weights for shared targets is significantly correlated ( _P_ < 0.0001, Fig. 4f). However, this coefficient (0.65) is smaller than that between replicate experiments (0.84, Fig. 4e) and between the L6 lines (0.77, Fig. 4d). We calculated and visualized relative differences in input strength from L5 and L6 for every source–target pair in the anchor group matrix (Fig. 4g). Some targets are contacted more, or less, by L5 or L6 depending on source region, but other targets have stronger L5 or L6 input regardless of source (bands of a single colour down a column in Fig. 4g). 

Notably, some CT projections clearly travel through thalamic regions before reaching their final targets, but also form synapses in those areas. Although entire regions containing only passing fibres were masked out, the remaining connections can contain a mix of fibres and terminals. To determine the effect of this kind of axonal trajectory on quantification of CT connection strengths, we compared a subset of spatially matched data sets in L5 and L6 Cre lines using 

**198** | Nature | Vol 575 | 7 November 2019 

**==> picture [255 x 341] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Core c Prefrontal Lateral Somatomotor Visual Medial Aud<br>From LGd<br>VPM<br>VPL<br>* VISp VPMVPM<br>Intralaminar VPMPO<br>From PF POPO<br>MG<br>MG<br>MG<br>PIL<br>* LD<br>AV<br>VISam AV<br>Matrix-focal LDAV<br>LD<br>From AV LD<br>LP<br>LP<br>AV<br>VAL<br>* PFPF<br>RSPv CL<br>Matrix-multiareal CLLGd<br>LGd<br>From VM * LGdLGd<br>LGd<br>LGd<br>LGd<br>LGd<br>LGd<br>MOs LP<br>POL<br>b Source Class MD-1<br>VPL Core MD-1<br>VPM Core MD-1<br>LGd Core MD-1<br>PF IL MD-1<br>IMD IL MD-1<br>CLPVTMGCMIAD ILILILILMatrix(f) IMDCMSMTVMVMPCN<br>AV Matrix(f) VAL<br>LD Matrix(f) MD-2<br>VAL Matrix PT<br>PT Matrix PVT<br>MD Matrix PVT<br>PO Matrix(m) PVT<br>POLPCNVMRESMTPILAMLPLGv Matrix(m)Matrix(m)Matrix(m)Matrix(m)Matrix(m)Matrix(m)Matrix(m)Matrix(m)None MD-2MD-2MD-2PTPTPTPTREREAV<br>SPFm None AM<br>LH None AM<br>MH None AM<br>RT None IAD<br>FRP ACAd ACAv PL ILA ORBl ORBm ORBvl AId AIv AIpGU VISC TEa PERI ECT SSs SSp-bfdSSp-trSSp-llSSp-ulSSp-unSSp-nSSp-mMOpMOs VISal VISl VISpVISplVISli VISporVISrl VISa VISam VISpmRSPaglRSPd RSPv AUDd AUDpAUDpoAUDv<br>**----- End of picture text -----**<br>


**Fig. 3 | Thalamocortical projection patterns by region and class. a** , Left, flat map views show TC projections labelled from the region indicated. Right, STPT images from the centre of a cortical target (asterisk on left) show example axon lamination patterns associated with each projection class. **b** , Key summarizes projection class assigned for 29 thalamic nuclei. **c** , The TC connectivity matrix (70 × 43) for individual viral tracer injection experiments with verified cortical projections. Each row shows log10-transformed NPVs from one experiment to the 43 ipsilateral cortical targets (columns). Cre line names for each row are in Supplementary Table 5). Unsupervised hierarchical clustering, using Spearman correlation and average linkages, revealed seven clusters containing thalamic regions with cortical projection patterns resembling the cortical modules. Matrix colour map as in Fig. 2. 

synaptophysin–EGFP to preferentially label terminals over fibres (Extended Data Fig. 6; see Methods). We found a strong linear relationship between measured connection strengths, and between relative differences between L5 and L6, with these two tracers, showing that EGFP tracer results can be used confidently for quantitative estimates of CT strengths. Nevertheless, this is an important consideration, as across the entire brain connection strengths from synaptophysin–EGFP experiments are on average lower than when using EGFP (Extended Data Fig. 1c), specifically by about 0.5 log units for _Rbp4_ CT targets (Extended Data Fig. 6k). 

## **Laminar termination patterns in cortex** 

Using automated image registration to CCFv3, we quantified projection strengths by layer within each cortical target (registration precision in Extended Data Fig. 7a–c, Supplementary Table 7; see Methods). Then, to identify common laminar termination patterns across all sources and lines, we performed unsupervised hierarchical clustering with the complete data set (849 cortical and 81 thalamic experiments). Data had to pass three filters, as follows. (1) Target connection strength (log10 

**==> picture [253 x 362] intentionally omitted <==**

**----- Start of picture text -----**<br>
–3.5 –1.5 0.5<br>a Rbp4 -Cre_KL100: L5 log10 normalized projection volume<br>ACAdACAv c Shared<br>PLILAORBl 1.0 L5Other<br>ORBvl<br>AIdSSs-1 0.8<br>SSs-2<br>SSp-bfd<br>SSp-llSSp-ul 0.6<br>SSp-n<br>SSp-m<br>MOs-1MOp 0.4<br>MOs-2<br>VISal<br>VISl 0.2<br>VISp<br>VISpor<br>VISrl<br>VISam 0.0<br>VISpm<br>RSPdRSPv Mouse line<br>AUDp<br>b Avg Ntsr1  +  Syt6  L6  d<br>ACAdACAv 1<br>PL 0<br>ILA<br>ORBl –1<br>ORBvlAId –2<br>SSs-1SSs-2 –3<br>SSp-bfd –4<br>MOs-1MOs-2SSp-llSSp-ulSSp-nSSp-mMOp –5–6–6 –5 Ntsr1 –4 Ntsr1 only–3-Cre_GN220–2 –1 0 1<br>VISalVISl e<br>VISpVISpor 1<br>VISrlVISam 0<br>VISpm –1<br>RSPd<br>RSPv –2<br>AUDp –3<br>g Relative diff matrix L6 Equal L5 –4<br>ACAdACAv –5<br>PLILA –6–6 –5 –4 –3 –2 –1 0 1<br>ORBlORBvl Replicate 1<br>AId<br>SSs-1<br>SSs-2SSp-bfd f<br>SSp-llSSp-ul 1<br>SSp-nSSp-m 0 L6<br>MOs-1MOp –1<br>MOs-2 –2<br>VISalVISl –3<br>VISpVISporVISrl –4–5 L5<br>VISamVISpmRSPd –6–6 –5 –4 –3 –2 –1 0 1<br>RSPvAUDp Rbp4 -Cre_KL100<br>VPL VPM PO PoT VPMpcVPLpcSPFpMG PIL PP SGN AD AV LD LP VAL PF CL LGd SubG LGv IGL IntG POL MD IMD CM SMT SPA VM PCN PVT PT RE SPFm Xi RH IAM PR LH MH AM IAD RT<br>Fraction of positive targets<br>Syt6<br>Syt6<br> only<br> NPV<br>10<br>log<br> NPV_replicate 2<br>10<br>log<br> NPV_Avg L6 line<br>10<br>log<br>**----- End of picture text -----**<br>


**Fig. 4 | Corticothalamic projections from layers 5 and 6. a** , **b** , CT connectivity matrices (27 × 44) for L5 ( **a** , _Rbp4_ ) and L6 ( **b** , average of _Ntsr1_ and _Syt6_ ). Each row shows log10-transformed NPVs from one of the 27 cortical source areas in Fig. 2 to the 44 ipsilateral thalamic target regions (columns). **c** , The fraction of true positive CT targets shared by wild-type (black circle) and each L6 line (yellow) with its _Rbp4_ anchor is plotted in the box plot (grey). The fraction of positive targets unique to _Rbp4_ (green) or unique to the L6 line (white) are also shown. Box plots show median and IQR. Whiskers show minimum and maximum values. **d** , log NPVs for thalamic targets shared by _Ntsr1_ and _Syt6_ were significantly correlated (Spearman _r_ = 0.77, _P_ < 0.0001). **e** , log NPVs for thalamic targets shared by replicate experiments in the same Cre line less than 500 μm apart were significantly correlated (Spearman _r_ = 0.84, _P_ < 0.0001). **f** , The average log NPVs originating from L6 are plotted against L5 for all spatially matched experiments (Spearman _r_ = 0.65, _P_ < 0.0001). **g** , The matrix shows the relative difference for each source × target connection originating from L5 versus L6 (L5 − L6/L5 + L6). 

transformed NPV) was above −1.5. This threshold was chosen after analysing NPV frequency distributions for a set of manually verified true positive and true negative connections (Extended Data Fig. 7d). (2) Percentage of infection volume in the primary source was more than 50%. (3) Self-to-self (within area) projections were removed. Following these steps, if present, multiple experiments were averaged, resulting in a total of 7,063 (660 thalamus, 6,403 cortex) unique source–line–target connections (Supplementary Table 8). We identified nine clusters (Fig. 5a). The median relative density values for each layer and the overall frequencies of these clusters are shown in Fig. 5b–d. Representative images from specific connections (a given source–line–target) assigned to each cluster from a cortical and thalamic source are shown in Fig. 5e. 

A summary of cluster representation shows that each cortical Cre line and TC projection class is associated with more than one type of 

Nature | Vol 575 | 7 November 2019 | **199** 

## Article 

**==> picture [516 x 387] intentionally omitted <==**

**----- Start of picture text -----**<br>
a 1 2 3 4 5 6 7 8 9<br>3<br>L1<br>L2/3<br>L4<br>L5 1<br>L6a 0<br>b 1 2 3 4 5 6 7 8 9 e<br>L1<br>L2/3<br>L4<br>L5<br>L6a<br>c 2,000 CTX TH 250<br>1,600 200<br>1,200 150<br>800 100<br>400 50<br>0 0<br>d 100<br>75<br>50<br>25 1 2 3 4 5 6 7 8 9 1 2 3 4 *cc 5 6 7 8 *cc 9 *cc<br>0<br>f g Cortical sources Thalamic sources<br>L1<br>3<br>1<br>2 L2/3<br>3<br>4 L4<br>5<br>L5<br>6<br>1<br>7<br>L6a<br>8<br>9<br>0<br>All L2/3 L4 L5 L6 C IL F M<br>WT Cux2Sepw1Nr5a1RorbScnn1aRbp4Tlx3 A93Chrna2Sim1Efr3aNtsr1Syt6 CoreIL Matrix (f)Matrix (m)<br>Relative density<br>Median value<br>Cortical sources<br>Number<br>: TH  freq<br>Thalamic sources<br>CTX<br>Relative frequency<br>**----- End of picture text -----**<br>


**Fig. 5 | Corticocortical and thalamocortical target lamination patterns. a** , Unsupervised hierarchical clustering on relative projection density per layer. Each column is a unique combination of mouse line, cortical or thalamic source area, and cortical target. Connections to agranular (no L4) regions are coloured grey for L4. The dotted line indicates where the dendrogram was cut into nine clusters. **b** , Median relative density by layer for each cluster. **c** , Number of cortical or thalamic connections in each cluster, plotted on the left and right _y_ - axis, respectively. **d** , The frequency of cortical and thalamic targets assigned to each cluster. The dotted line indicates the overall frequency of CC targets in the entire data set (90.53%). **e** , Representative STPT images show axonal lamination patterns from a connection assigned to each cluster from cortex or thalamus. In columns 4, 8, and 9, thalamic axons passing through the 

superficial corpus callosum are indicated (*cc). **f** , The relative frequency with which each cortical Cre line and TC projection class appears in the clusters. The fraction of experiments in a cluster belonging to each Cre line or class was divided by the overall frequency of experiments from that Cre line or class. A relative frequency value of 1 (white) indicates that the Cre line appeared in that cluster with the same frequency as in the entire data set. Values below 1 (green) indicate lower and above 1 (pink) indicate higher than expected frequency in a cluster. Dots indicate significant positive enrichment in that cluster (Fisher’s exact test, _P_ < 0.0001). **g** , Schematic diagram shows significantly enriched axon lamination patterns associated with each layer and/or class of origin in the source area. 

target layer pattern (Fig. 5f). The most common, and significantly enriched, laminar patterns from each are schematized in Fig. 5g (Fisher’s exact test, _P_ < 0.0001). L2/3 and L4 ( _Nr5a1_ ) neurons project predominantly to middle layers (L2/3, L4, and L5), avoiding L1. Other L4 neurons project to L1 and either L2/3 or L5, avoiding L4 and L6. In L5, when both IT and PT classes are labelled, as in the _Rbp4_ line, projections target L6 and either L1 or L2/3. L5 IT neurons predominantly target superficial layers (L1 and L2/3). L5 PT neurons target either deep layers only (L5 and L6) or deep layers and L1, consistent with the L5 _Rbp4_ patterns representing both IT and PT patterns. L6 CT neurons project predominantly to deep layers. From thalamic sources, core neurons project to L4 and either L5 or L6, intralaminar and matrixfocal neurons preferentially project to L5 and L6, and connections coming from matrix-multiareal sources all project to L1, with differing proportions in other layers. 

## **Hierarchy of cortical and thalamic areas** 

We hypothesized that the above anatomical rules could be used across all cortical and thalamic regions to build a testable hierarchical model to predict the direction of information flow. We used cortical Cre line experiments (Fig. 6) because they allow incorporation of the specific layer termination patterns related to cell class, but results are also provided using wild-type data (Extended Data Fig. 10). 

We used an unbiased approach to identify the most optimal label for each of the nine clusters; feedforward (FF) or feedback (FB). We defined an initial hierarchical position for each cortical area (as both a source and target) using the averaged difference between FB and FF connections, normalized by a confidence measure for each cortical Cre line (Eqs. (2–4) in Methods; see also results without this confidence term in Extended Data Fig. 10). We searched over all possible mappings between the nine layer patterns and directional assignments, and 

**200** | Nature | Vol 575 | 7 November 2019 

**==> picture [250 x 366] intentionally omitted <==**

**----- Start of picture text -----**<br>
a L1 2 FB6 CC mapping9 1 3 4FF5 7 8 3 b 10 FBCT mappingCC + TC c 4540353025 ShuffledCCCC + TCCC + TC + CT Observed<br>L2/3 FF 20<br>L4 –1 FB 15<br>L5 1 10<br>L6a 0 –2 FF 50<br>FB FF –2 –1 0 1<br>TC mapping L5 line log10 NPV Global hierarchy score<br>d e CC + TC + CT<br>POLVMPILREPF PrefrontalLateralSomatomotorVisual 0.25Top VISpor VISamVISa<br>ORBvl<br>ACAd Medial<br>MOsTEaAIv ThalamusAuditory VISpm<br>VISa VISpl<br>VISam 0 VISal<br>ACAv<br>VISpor VISli<br>FRP<br>ORBmILAPL VISl VISrl<br>AUDpo<br>ORBl<br>LP –0.25<br>SMT<br>VAL<br>AV<br>SSp-tr<br>AId<br>VISpm<br>RSPaglRSPvVISalPVTCM –0.5Bottom Out VISp In<br>VISplVISliPO f Top CC + TC + CTPrefrontal<br>MOpLD 0.3<br>RSPd<br>VISrl<br>VISl<br>SSsAIp 0.2 Lateral<br>SSp-bfd<br>PT<br>SSp-m<br>SSp-ulMD Medial<br>SSp-llAUDd 0.1<br>SSp-n<br>AUDp<br>IMD<br>MGAM Somatomotor<br>VISp 0<br>IAD<br>CL CC<br>LGd<br>VPMPCNVPL CC + TCCC + TC + CT –0.1 Visual<br>–1.0 Hierarchy score (all areas)–0.5 0 0.5 1.0 Bottom Auditory<br>–0.005 0.015 0.035 0.055 0.075 0.095 0.115 0.135<br>Avg L6 line No. of values<br>Relative density<br>Hierarchy score (all areas)<br>Cortical and thalamic areas<br>Hierarchy score (all areas)<br>**----- End of picture text -----**<br>


**Fig. 6 | A hierarchical organization of areas and modules. a** , Direction mapping results for CC and TC terminal layer patterns. Median relative density by layer for each cluster shown from Fig. 5b. **b** , Direction mapping for CT connections. Scatterplot shows the log10-transformed NPVs for every CT connection from L5 and L6. Points are colour-coded by the mapping (FF or FB) predicted from the CC + TC hierarchy. Red line, linear discriminant analysisassigned connections (below, FF; above, FB). **c** , Global hierarchy scores (Eq. (17)) for CC connections only (green), compared to the scores when TC and CT connections are included sequentially (pink, blue). Scores for the original, observed, data are shown as single outlined bars. Distributions of hierarchy scores were obtained from shuffled data sets ( _n_ = 100). The medians of the shuffled distributions estimate the lower bound (0.001, 0.044 and −0.002 for CC, CC + TC and CC + TC + CT, respectively). **d** , Thirty-seven cortical areas and twenty-four thalamic nuclei rank-ordered by their CC + TC + CT hierarchy scores. Scores for each area using only CC or CC + TC connections are also plotted. _y_ -axis labels are colour-coded by module assignment for cortical areas. **e** , Network diagram showing interconnections of all cortical visual areas (light blue, visual module; dark blue, medial module). Edge width represents relative connection density from Fig. 1e. The curved lines show outputs (left) and inputs (right) to each node. Nodes are positioned along a single axis based on hierarchical score. **f** , Intermodule network diagram. Edge width represents sum of connection densities from Fig. 1e. 

determined which mapping resulted in the most self-consistent initial hierarchy (maximized the CC global hierarchy score, which measures how consistent the obtained hierarchy is with directions of individual connections; Eq. (5) in Methods). For CC connections, clusters 2, 6, and 9 were assigned to one direction, and 1, 3, 4, 5, 7 and 8 to the other (Fig. 6a). For TC projections, clusters 2 and 6 were assigned to the same direction and the rest to the other (Eqs. (8–10) in Methods). Cluster 9 switched directions for CC and TC. We confidently labelled these 

two directions as either FF or FB on the basis of extensive anatomical analyses relating our observed layer patterns to known hierarchical order and rules between reciprocally connected regions[35–38] (Extended Data Figs. 8, 9). After obtaining initial hierarchy positions with the most optimal mappings, scores were iterated to further refine the hierarchy (Eqs. (6, 7, 11, 12) in Methods). 

To label CT connections, we used the Cre-defined L5 and L6 projection strengths (thresholded by log10-transformed NPV > −2.5; Extended Data Fig. 7e; Eq. (13) in Methods). Linear discriminant analysis was applied to assign CT connections into the FF or FB class that was most self-consistent with the direction predicted from a CT hierarchy constructed first from CC and TC projections (Fig. 6b, Supplementary Table 9; Eq. (14) in Methods). 

Using these rules, we obtained three versions of hierarchy based on (1) CC connections only, (2) CC and TC connections, and (3) CC, TC, and CT connections. We demonstrate that there is significant hierarchical organization by comparing global hierarchy scores with corresponding distributions of scores from shuffled connections (Fig. 6c, see _z_ -scores in Extended Data Fig. 10f). Adding thalamus connections essentially doubled the hierarchy scores (0.069, 0.120, and 0.128 for CC, CC + TC, and CC + TC + CT, respectively). Nonetheless, by comparing the global hierarchy scores with their maxima (0.679, 0.636, and 0.683; see Methods), it appears to be a rather shallow hierarchy. 

The final hierarchical positions for 37 cortical areas and 24 thalamic nuclei are presented in Fig. 6d (scores in Supplementary Table 9). Most thalamic regions are located at the bottom or top, suggesting that they have pure driver or modulator effects on the cortical areas with which they are connected. Several thalamic nuclei appear mid-hierarchy, indicating more balanced numbers of FF and FB connections. For cortical regions, primary visual cortex is at the bottom and the prefrontal area ORBvl (ventrolateral part of the orbital area) is at the top. Predicted hierarchical positions were broadly similar across the three versions (CC, CC + TC, or CC + TC + CT). Most regions had only minor shifts in position. The largest shifts occurred in thalamic regions when adding CT connections. Hierarchies were also exceedingly robust to contributions from any single Cre line, or layer or projection class (Extended Data Fig. 10h). 

We used similar methods to predict hierarchy for subsets of areas (visual cortex, Fig. 6e) and between modules (Fig. 6f). The intermodule hierarchy had a relatively low global score (0.07) compared to the allarea hierarchy (0.13), but it was more obviously organized into distinct levels; primary sensory modules at the bottom, lateral and medial modules in the middle, and prefrontal at the top. 

## **Discussion** 

We used a genetic viral tracing approach, building on our previously established whole-brain imaging and informatics pipeline, to map projections originating from unique cell populations in the same cortical area, and from distinct projection classes in the thalamus. Our study represents a big step towards a true mesoscale connectome[39] . It will be informative for future connectome studies with more refined cell types and single cells[40–42] , which will no doubt reveal additional principles of cell-type-specific brain connectivity[43] . With these mesoscale data, we derived several generalizable anatomical rules of cortical and thalamic connections, and tested whether the organizing principle of a hierarchy applies to mouse cortex and thalamus. 

The cortex is organized as a modular network[3,9,11] , which provides a structural view of possible paths of information flow, but does not impose direction or order onto that flow. By contrast, a hierarchy implies that interareal connections belong to at least two general types: feedforward or feedback. Specific anatomical projection patterns were previously associated with information transmission in these directions in primate and rodent visual cortex[12,13,36,38] . In our data, we observed many similar patterns. Two patterns that differed were the superficial 

Nature | Vol 575 | 7 November 2019 | **201** 

## Article 

layer projections (cluster 1) and the deep layer projections (cluster 9). Felleman and van Essen[12] noted the occasional superficial-only pattern, but they called it feedback because it did not involve L4. Our results suggest this pattern is associated with feedforward. The strength and presence of projections between areas from the predominantly L4 Cre lines was also unexpected, given canonical circuit diagrams[44] , and might be explained by varying degrees of layer selectivity. However, by reconstructing the complete dendritic and axonal morphology of single cells, we directly show that L4 neurons, even spiny stellate cells, can in fact have long-range projections. 

The hierarchy that we find is shallower than might have been expected, even with inclusion of thalamic regions. The difference between the lowest and the highest areas is less than two full levels, and the all-area hierarchy global score is at 19% between random and perfectly hierarchical. This might be characteristic of the mouse cortex, given its high connection density, particularly when considering all non-zero connection strengths[45] . We did not explicitly include strengths in computing hierarchy, except that weak connections were removed. Notably, hierarchical position alone does not explain all of the connections of a given area. This complexity may be why some have argued that the concept of a hierarchy is overly simplistic for describing functional properties[46] . Given the number of different connection types that arise from a single area, future computational models that incorporate more than feedforward and feedback labels will enable further insights into the organization of brain networks. 

- Cortical hierarchies were previously derived from classic antero grade or retrograde tracing without cell-class resolution. Using Cre lines, we have mapped both layer of origin and target lamination pattern in the same experiment. We found that L2/3 and L4 neurons have predominantly feedforward layer projection patterns, whereas L5 and L6 neurons have both feedforward and feedback patterns. However, these general relationships depend on the specific source–target connection and Cre line. The Cre data set, with all this detail, produced the most robust hierarchy (Extended Data Fig. 10f). However, our results from wild-type mice provide a solid benchmark for others interested in applying these hierarchical model algorithms to classic tracing data. The calculation of global hierarchy scores for other data sets will enable direct comparisons between species and quantitative assessments of how development or disease might affect hierarchical organization. 

## **Online content** 

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-019-1716-z. 

1. Oh, S. W. et al. A mesoscale connectome of the mouse brain. _Nature_ **508** , 207–214 (2014). 

2. Sporns, O., Tononi, G. & Kötter, R. The human connectome: a structural description of the human brain. _PLOS Comput. Biol_ . **1** , e42 (2005). 

3. Zingg, B. et al. Neural networks of the mouse neocortex. _Cell_ **156** , 1096–1111 (2014). 4. Markov, N. T. et al. A weighted and directed interareal connectivity matrix for macaque cerebral cortex. _Cereb. Cortex_ **24** , 17–36 (2014). 

5. Bota, M., Sporns, O. & Swanson, L. W. Architecture of the cerebral cortical association connectome underlying cognition. _Proc. Natl Acad. Sci. USA_ **112** , E2093–E2101 (2015). 

6. Scannell, J. W., Blakemore, C. & Young, M. P. Analysis of connectivity in the cat cerebral cortex. _J. Neurosci_ . **15** , 1463–1483 (1995). 

7. Swanson, L. W., Hahn, J. D. & Sporns, O. Organizing principles for the cerebral cortex network of commissural and association connections. _Proc. Natl Acad. Sci. USA_ **114** , E9692–E9701 (2017). 

8. Bullmore, E. & Sporns, O. Complex brain networks: graph theoretical analysis of structural and functional systems. _Nat. Rev. Neurosci_ . **10** , 186–198 (2009). 

9. Rubinov, M., Ypma, R. J. F., Watson, C. & Bullmore, E. T. Wiring cost and topological participation of the mouse brain connectome. _Proc. Natl Acad. Sci. USA_ **112** , 10032–10037 (2015). 

10. Wang, Q., Sporns, O. & Burkhalter, A. Network analysis of corticocortical connections reveals ventral and dorsal processing streams in mouse visual cortex. _J. Neurosci_ . **32** , 4386–4399 (2012). 

11. Swanson, L. W., Hahn, J. D., Jeub, L. G. S., Fortunato, S. & Sporns, O. Subsystem organization of axonal connections within and between the right and left cerebral cortex and cerebral nuclei (endbrain). _Proc. Natl Acad. Sci. USA_ **115** , E6910–E6919 (2018). 

12. Felleman, D. J. & Van Essen, D. C. Distributed hierarchical processing in the primate cerebral cortex. _Cereb. Cortex_ **1** , 1–47 (1991). 

13. Rockland, K. S. & Pandya, D. N. Laminar origins and terminations of cortical connections of the occipital lobe in the rhesus monkey. _Brain Res_ . **179** , 3–20 (1979). 

14. Riesenhuber, M. & Poggio, T. Hierarchical models of object recognition in cortex. _Nat. Neurosci_ . **2** , 1019–1025 (1999). 

15. Rockland, K. S. What do we know about laminar connectivity? _Neuroimage_ **197** , 772–784 (2019). 

16. Markov, N. T. et al. Anatomy of hierarchy: feedforward and feedback pathways in macaque visual cortex. _J. Comp. Neurol_ . **522** , 225–259 (2014). 

17. Shepherd, G. M. G. Corticostriatal connectivity and its role in disease. _Nat. Rev. Neurosci_ . **14** , 278–291 (2013). 

18. Harris, K. D. & Shepherd, G. M. G. The neocortical circuit: themes and variations. _Nat. Neurosci_ . **18** , 170–181 (2015). 

19. Sherman, S. M. Thalamus plays a central role in ongoing cortical functioning. _Nat. Neurosci_ . **19** , 533–541 (2016). 

20. Usrey, W. M. & Sherman, S. M. Corticofugal circuits: communication lines from the cortex to the rest of the brain. _J. Comp. Neurol_ . **527** , 640–650 (2019). 

21. Jones, E. G. _The Thalamus_ (Cambridge Univ. Press, 2007). 22. Jones, E. G. Viewpoint: the core and matrix of thalamic organization. _Neuroscience_ **85** , 331–345 (1998). 

23. Clascá, F., Rubio-Garrido, P. & Jabaudon, D. Unveiling the diversity of thalamocortical neuron subtypes. _Eur. J. Neurosci_ . **35** , 1524–1532 (2012). 

24. Gong, S. et al. Targeting Cre recombinase to specific neuron populations with bacterial artificial chromosome constructs. _J. Neurosci_ . **27** , 9817–9823 (2007). 

25. Gerfen, C. R., Paletzki, R. & Heintz, N. GENSAT BAC cre-recombinase driver lines to study the functional organization of cerebral cortical and basal ganglia circuits. _Neuron_ **80** , 1368–1383 (2013). 

26. Harris, J. A. et al. Anatomical characterization of Cre driver mice for neural circuit mapping and manipulation. _Front. Neural Circuits_ **8** , 76 (2014). 

27. Daigle, T. L. et al. A suite of transgenic driver and reporter mouse lines with enhanced brain-cell-type targeting and functionality. _Cell_ **174** , 465–480.e22 (2018). 

28. Tasic, B. et al. Shared and distinct transcriptomic cell types across neocortical areas. _Nature_ **563** , 72–78 (2018). 

29. Knox, J. E. et al. High-resolution data-driven model of the mouse connectome. _Netw. Neurosci_ . **3** , 217–236 (2018). 

30. Rubinov, M. & Sporns, O. Complex network measures of brain connectivity: uses and interpretations. _Neuroimage_ **52** , 1059–1069 (2010). 

31. Minamisawa, G., Kwon, S. E., Chevée, M., Brown, S. P. & O’Connor, D. H. A Non-canonical feedback circuit for rapid interactions between somatosensory cortices. _Cell Rep_ . **23** , 2718–2731.e6 (2018). 

32. Li, A. et al. Micro-optical sectioning tomography to obtain a high-resolution atlas of the mouse brain. _Science_ **330** , 1404–1408 (2010). 

33. Wang, Y., Ye, M., Kuang, X., Li, Y. & Hu, S. A simplified morphological classification scheme for pyramidal cells in six layers of primary somatosensory cortex of juvenile rats. _IBRO Rep_ . **5** , 74–90 (2018). 

34. Phillips, J. W. et al. A repeated molecular architecture across thalamic pathways. _Nat. Neurosci_ . https://doi.org/10.1038/s41593-019-0483-3 (2019). 

35. Huh, C. Y. L., Peach, J. P., Bennett, C., Vega, R. M. & Hestrin, S. Feature-specific organization of feedback pathways in mouse visual cortex. _Curr. Biol_ . **28** , 114–120.e5 (2018). 

||organization of feedback pathways in mouse visual cortex._Curr. Biol_.**28**, 114–120.e5<br>(2018).|
|---|---|
|36.|Coogan, T. A. & Burkhalter, A. Hierarchical organization of areas in rat visual cortex.|
|37.|_J. Neurosci_.**13**, 3749–3772 (1993).<br>Crick, F. & Koch, C. Constraints on cortical and thalamic projections: the no-strong-loops<br>hypothesis._Nature_ **391**, 245–250 (1998).|



38. D’Souza, R. D., Meier, A. M., Bista, P., Wang, Q. & Burkhalter, A. Recruitment of inhibition and excitation across mouse visual cortex depends on the hierarchy of interconnecting areas. _eLife_ **5** , e19332 (2016). 

39. Bohland, J. W. et al. A proposal for a coordinated effort for the determination of brainwide neuroanatomical connectivity in model organisms at a mesoscopic scale. _PLOS Comput. Biol_ . **5** , e1000334 (2009). 

40. Han, Y. et al. The logic of single-cell projections from visual cortex. _Nature_ **556** , 51–56 (2018). 

41. Economo, M. N. et al. A platform for brain-wide imaging and reconstruction of individual neurons. _eLife_ **5** , e10566 (2016). 

42. Winnubst, J. et al. Reconstruction of 1,000 projection neurons reveals new cell types and organization of long-range connectivity in the mouse brain. _Cell_ **179** , 268–281.e13 (2019). 

43. Halassa, M. M. & Sherman, S. M. Thalamocortical circuit motifs: a general framework. _Neuron_ **103** , 762–770 (2019). 

44. Douglas, R. J. & Martin, K. A. C. Neuronal circuits of the neocortex. _Annu. Rev. Neurosci_ . **27** , 419–451 (2004). 

45. Gămănuţ, R. et al. The mouse cortical connectome, characterized by an ultra-dense cortical graph, maintains specificity by distinct connectivity profiles. _Neuron_ **97** , 698–715. e10 (2018). 

46. Hegdé, J. & Felleman, D. J. Reappraising the functional implications of the primate visual anatomical hierarchy. _Neuroscientist_ **13** , 416–421 (2007). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

- © The Author(s), under exclusive licence to Springer Nature Limited 2019 

**202** | Nature | Vol 575 | 7 November 2019 

## **Methods** 

## **Mice** 

Experiments involving mice were approved by the Institutional Animal Care and Use Committees of the Allen Institute for Brain Science in accordance with NIH guidelines. Sources of mouse lines are listed in Supplementary Table 1. Transgene expression patterns in many Cre driver lines used in this study have been previously characterized[26] and are available through the Transgenic Characterization data portal (http://connectivity.brain-map.org/transgenic). Cre lines were originally derived on various backgrounds, but the majority were crossed to C57BL/6J mice for more than ten generations and maintained as heterozygous lines upon arrival. Tracer injections were performed in male and female mice at an average age of P56 + 10 days. Mice were grouphoused with a 12-h light–dark cycle. Food and water were provided ad libitum. No statistical methods were used to predetermine sample size. The experiments were not randomized and investigators were not blinded to allocation during experiments and outcome assessment. 

## **Tracers and injection methods** 

rAAV was used as an anterograde tracer. For most regions, stereotaxic coordinates were used to identify the appropriate location for a tracer injection. Atlas-derived stereotaxic coordinates were chosen for each target area based on _The Mouse Brain in Stereotaxic Coordinates_[47] . Anterior–posterior (AP) coordinates are referenced from bregma, medial–lateral (ML) coordinates are distance from midline at bregma, and dorsal–ventral (DV) depth is measured from the pial surface of the brain. Stereotaxic coordinates used for each experiment can be found through the data portal. For a subset of experiments in the left hemisphere, we first functionally mapped the visual cortex using intrinsic signal imaging (ISI) through the skull, described below to assist in targeting injections. A pan-neuronal AAV expressing EGFP (rAAV2/1. hSynapsin.EGFP.WPRE.bGH, Penn Vector Core, AV-1-PV1696, Addgene ID 105539) was used for injections into wild-type C57BL/6J mice (stock no. 00064, The Jackson Laboratory). To label genetically defined populations of neurons, we used either a Cre-dependent AAV vector that robustly expresses EGFP within the cytoplasm of Cre-expressing infected neurons (AAV2/1.pCAG.FLEX.EGFP.WPRE.bGH, Penn Vector Core, AV-1-ALL854, Addgene ID 51502) or, a Cre-dependent AAV virus expressing a synaptophysin–EGFP fusion protein to more specifically label presynaptic terminals (AAV2/1.pCAG.FLEX.sypEGFP.WPRE.bGH, Penn Vector Core). 

Functional mapping of visual field space by ISI was used in some cases to guide injection placement. Additional details of this procedure can be found at http://help.brain-map.org/display/mouseconnectivity/Documentation?preview=/2818171/10813533/Connectivity_Overview.pdf). In brief, a custom 3D-printed headframe was attached to the skull, centred at 3.1 mm lateral and 1.3 mm anterior to lambda on the left hemisphere. A transcranial window was made by securing a 7-mm glass coverslip onto the skull in the centre of the headframe well. Mice were allowed to recover for at least seven days before ISI mapping. ISI was then used to measure the haemodynamic response to visual stimulation across the entire field of view of a lightly anaesthetized, head-fixed, mouse. The visual stimulus consisted of sweeping a bar containing a flickering black-and-white checkerboard pattern across a grey background[48] . To generate a map, the bar was swept across the screen ten times in each of the four cardinal directions, moving at 9° per second. Processing of sign maps followed methods previously described[49] , with minor modifications. Phase maps were generated by calculating the phase angle of the pre-processed discrete Fourier transform at the stimulus frequency. The phase maps were used to translate the location of a visual stimulus displayed on the retina to a spatial location on the cortex. A sign map was produced from the phase maps by taking the sign of the angle between the altitude and azimuth map gradients. Averaged sign maps were produced from a 

minimum of three time series images, for a combined minimum average of 30 stimulus sweeps in each direction. Visual area segmentation and identification was obtained by converting the visual field map into a binary image using a manually defined threshold and further processing the initial visual areas with a split/merge routine[49] . Sign maps were curated and the experiment repeated if (1) fewer than six visual areas were positively identified; (2) retinotopic metrics of VISp were out of bounds (azimuth coverage within 60–100° and altitude coverage within 35–60°); or (3) auto-segmented maps needed to be annotated with more than three adjustments. Each animal had three attempts to get a passing map. 

ISI images were acquired using a pair of Nikon lenses (Nikkor 135 mm f/2.8 lens and 50 mm f/1.8), providing a magnification of 2.7×. Illumination was from a ring of sequential and independent LED lights, with green (peak wavelength of 527 nm and full width half maximum (FWHM) of 50 nm; Cree, C503B-GCN-CY0CO791) and red spectra (peak wavelength of 635 nm and FWHM of 20 nm; Avago Technologies, HLMP-EG08-Y2000), via a bandpass filter (630/92 nm, Semrock, FF01), and acquired with a sCMOS camera (Andor, Zyla 5.5 10-tap). Illumination and image acquisition were controlled with in-house GUI software written in Python. An image of the surface vasculature was acquired with green LED illumination to provide fiduciary marker references on the surface of the brain. 

All mice received one unilateral injection into a single target region. For injections using stereotaxic coordinates from bregma as a registration point, procedures were followed as previously described[1] . For ISI-guided injections, the glass coverslip of the transcranial window was removed by drilling around the edges and a small burr hole drilled, first through the Metabond and then through the skull using surface vasculature fiducials obtained from the ISI session as a guide. An overlay of the sign map over the vasculature fiducials was used to identify the target injection site. rAAV was delivered by iontophoresis with current settings of 3 μA at 7 s ‘on’ and 7 s ‘off’ cycles for 5 min total, using glass pipettes (inner tip diameters of 10–20 μm). 

Some injections were done into lines with regulatable versions of Cre. Tamoxifen-inducible Cre line (CreER) mice were treated with 0.2 mg/g body weight of tamoxifen solution in corn oil via oral gavage once per day for 5 consecutive days starting the week after virus injection. Trimethoprim-inducible Cre line (dCre) mice were treated with 0.3 mg/g body weight of trimethoprim solution in 10% DMSO via oral gavage once per day for 3 consecutive days starting the week after virus injection. For these Cre lines, brains were removed 4 weeks after the rAAV injection date as opposed to 3 weeks. All mice were deeply anaesthetized before intracardial perfusion, brain dissection, and tissue preparation for serial imaging as previously described[1] . 

## **Serial two-photon tomography and image data processing** 

Imaging by STPT (TissueCyte 1000, TissueVision Inc. Somerville, MA) has been described[1,50] , and here we used the exact same procedures as in our earlier published studies[1,51] . In brief, following tracer injections, brains were imaged using STPT at high _x_ – _y_ resolution (0.35 μm × 0.35 μm) every 100 μm along the rostrocaudal _z_ -axis, after which the images underwent quality control and manual annotation of injection sites, followed by signal detection and registration to the Allen Mouse Brain Common Coordinate Framework, version 3 (CCFv3) through our informatics data pipeline (IDP). 

The IDP manages the processing and organization of the image and quantified data for analysis and display in the web application, as previously described[1,52] . The two key algorithms are signal detection and image registration. Previous methods were implemented, except that two variations of the segmentation algorithm were employed, depending on the virus used for that experiment; one was tuned for EGFP detection and one for SypEGFP detection. High-threshold edge information was combined with spatial distance-conditioned low-threshold edge results to form candidate signal object sets. The candidate objects 

## Article 

were then filtered on the basis of morphological attributes such as length and area using connected component labelling. For the SypEGFP data, filters were tuned to detect smaller objects (punctate terminal boutons versus long fibres). In addition, high-intensity pixels near the detected objects were included in the signal pixel set. Detected objects near hyper-intense artefacts that occurred in multiple channels were removed. We developed an additional filtering step using a supervised decision tree classifier to filter out surface segmentation artefacts, based on morphological measurements, location context and the normalized intensities of all three channels. 

The output is a full resolution mask that classifies each 0.35 μm × 0.35 μm pixel as either signal or background. An isotropic 3D summary of each brain is constructed by dividing each image series into 10 μm × 10 μm × 10 μm grid voxels. Total signal is computed for each voxel by summing the number of signal-positive pixels in that voxel. Each image stack is registered in a multi-step process using both global affine and local deformable registration to the 3D Allen mouse brain reference atlas as previously described[52] . Segmentation and registration results are combined to quantify signal for each voxel in the reference space and for each structure in the reference atlas ontology by combining voxels from the same structure. 

Once an image series had passed quality control steps, injection site polygons overlaying the cell bodies of infected neurons were manually drawn. These polygons were informatically warped into the CCFv3 atlas space. Green channel signal intensity within the polygons was used to identify which structures have been injected, and to quantify the relative magnitude of their infections. The structure that received the largest proportion of signal intensity was identified as the primary injection site structure, and all other structures were considered secondary structures containing infected cells. A quantified injection summary is provided for each image series through the data portal that shows the relative amount of signal detected within each infected structure. 

## **Quantification of projection strengths using segmentation and registration** 

Projection signals can be quantified in several ways using our informatics pipeline (see SDK help: https://allensdk.readthedocs.io/en/latest/ connectivity.html#structure-level-projection-data). Here, we most frequently report ‘normalized projection volume’, which is the volume of detected projection signals in all voxels in a structure (in mm[3] ), divided by the total volume of detected signal in the manually annotated injection site. We also use the ‘normalized connection densities’ output from the voxel-level interpolation model for modularity analyses in Fig. 1e. Connection density is the sum of detected projection pixels divided by the sum of all pixels in that voxel or structure. Normalized connection density is this value divided by the injection site density. 

It is important to note that even after undergoing our quality control procedures, these informatically derived measures of connection strength can include artefacts (false positives), and, particularly for the EGFP tracer, report total signal from labelled axons, including passing fibres and synaptic terminals. For this reason, we performed extensive manual checking of all CC, CT, and TC targets to remove any signals from regions in which we could not identify any true positive axons or terminals (see main text). 

## **Morphological reconstruction of single L4 neurons** 

The Cux2-IRES-CreERT2 driver line was crossed with a TIGRE2.0 reporter line[27] , Ai166, also known as TIGRE-MORF[53] . In brief, Ai166 expresses a Cre-dependent MORF transgene, composed of a farnesylated EGFP preceded by a stretch of 22 guanidine nucleotides (22G-GFPf), which puts the transgene out of frame. Rare DNA replication errors lead to the deletion of one G, correcting the frameshift, and leading to GFPf expression. Combining Ai166 with a CreERT2 line and giving mice a low dose of tamoxifen produces sparse cellular 

labelling that is well suited for 3D morphological reconstruction[53] . High-resolution whole-brain imaging by fMOST has been described previously[54] ; similar protocols were used here to image the Cux2IRES-CreERT2;Ai166 brain. Specifically, high-resolution block-face fluorescence imaging was done in coronal planes. Using a diamond knife, 1.0-μm sections were removed before we imaged subsequent planes. The process was repeated through the entire rostral–caudal extent of the mouse brain, producing more than 10,000 images with a resolution of 0.3 × 0.3 × 1 μm ( _x_ × _y_ × _z_ ). Following acquisition of the complete fMOST image stack, it was converted into a multi-level navigable data set using the Vaa3D-TeraFly program[55] , and then reconstructions were performed using Vaa3D-TeraVR software tools built to facilitate semi-automated and manual reconstructions[56] . 

## **Creation of the cortical top-down and flattened views of the CCFv3 for data visualization** 

A standard _z_ -projection of signal in a top-down view of the cortex mixes signal from multiple areas. Visualizations of fluorescence in Figs. 1–3 instead project signal along a curved cortical coordinate system that more closely matches the columnar structure of the cortex. This coordinate system was created by first solving Laplace’s equation between pia and white matter surfaces, resulting in intermediate equi-potential surfaces. Streamlines were computed by finding orthogonal (steepest descent) paths through the equi-potential field. Cortical signal can then be projected along these streamlines for visualization. 

A cortical flatmap was also constructed to enable visualization of anatomical and projection information while preserving spatial context for the entire cortex. The flatmap was created by computing the geodesic distance (the shortest path between two points on a curve surface) between every point on the cortical surface and two pairs of selected anchor points. Each pair of anchor points forms one axis of the 2D embedding of the cortex into a flatmap. The 2D coordinate - for each point on the cortical surface is obtained by finding the loca tion such that the radial (circular) distance from the anchor points (in 2D) equals the geodesic distance that was computed in 3D. This procedure produces smooth mapping of the cortical surface onto a 2D plane for visualization. This embedding does not preserve area and the frontal pole and medial-posterior region is highly distorted. As such, all numerical computation is done in 3D space. Similar techniques are used for texture mapping on geometric models in the field of computer graphics[57] . 

## **Network modularity analysis** 

The matrix of connection weights between cortical areas (Fig. 1e) was obtained from a model of voxel-level connectivity[29] . We analysed the network structure of this graph using the Louvain Community Detection algorithm from the Brain Connectivity Toolbox (https://sites. google.com/site/bctnet/)[30,58] . We determined the modularity metric ( _Q_ ) at various levels of granularity by varying the resolution parameter, _γ_ , from 0 to 2.5 in steps of 0.1. _Q_ quantifies the fraction of connections inside modules minus the fraction of connections expected inside the same modules if the network was connected randomly; that is, _Q_ = 0 has no more intramodule connections than expected by chance, while _Q_ > 0 indicates a network with some community structure. 

For each value of _γ_ , the modularity was computed 1,000× and each - pair of regions received an affinity score between 0 and 1. The affin ity score is the probability of two regions being assigned to the same module weighted by the modularity score ( _Q_ ) for that iteration, thereby assigning higher weights to partitions with a higher modularity score. Each region was assigned to the module with which it had the highest affinity, with the caveat that all structures within a module had an affinity score ≥0.5 with all other members of the module. For each value of _γ_ , we also generated a shuffled matrix containing the same weights but with the source and target regions randomized. The modularity for the cortical matrix ( _Q_ ) and the shuffled matrix ( _Q_ shuffled) were evaluated at 

each value of _γ_ . As stated in the results, we chose to focus on the modules identified at _γ_ = 1.3 ( _Q_ = 0.36) where the difference between _Q_ and _Q_ shuffled was at its peak (0.22 ± 0.017, mean ± s.d.), although it should be noted that it was relatively stable between _γ_ = 1 and _γ_ = 1.8 (0.21 ± 0.019 at _γ_ = 1, 0.20 ± 0.012 at _γ_ = 1.8). Modules were identical from _γ_ = 1.3 to _γ_ = 1.5 and showed only minor differences for _γ_ between 1 and 2. 

## **Statistics and reproducibility** 

We used the software program GraphPad Prism for statistical tests and generation of graphs, and the software program Gephi for visualization and layout of network diagrams[59,60] . The exact numbers of tracer injection experiments per mouse line and source area are shown in Supplementary Table 1, and range from _n_ = 1 to 31. Not all experiments were independently repeated because we sought to balance the need for broad coverage across Cre lines and source areas with excessive animal use. Previously, we demonstrated that _n_ = 1 is a good predictor of connectivity strengths across multiple animals[1] . In this study, we also show that the correlations between brain-wide projection strengths from experiments at matched locations within the same mouse line are consistent, positive, and significant (Spearman _r_ > 0.8, _P_ < 0.0001, Extended Data Fig. 1). Sample sizes for analyses presented in all figures are mostly noted in the main text, and can also be found in associated Supplementary Tables. Specifics include: for Fig. 2g, h: _n_ = number of mice per line, for wild-type, _Cux2_ , _Rbp4_ : _n_ = 27, _Syt6_ : _n_ = 23, _A93_ : _n_ = 22, _Tlx3_ , _Ntsr1_ : _n_ = 21, _Scnn1a_ -Tg3: _n_ = 19, _Chrna2_ , _Efr3a_ : _n_ = 15, _Nr5a1_ : _n_ = 10, _Sim1_ : _n_ = 9, _Rorb_ : _n_ = 6, _Sepw1_ : _n_ = 5; for Fig. 4c: _n_ = number of mice per line, for wild-type, _Rbp4_ : _n_ = 27, _Syt6_ : _n_ = 23, and _Ntsr1_ : _n_ = 21; for Fig. 4d: _n_ = 1,158 total CT connections, 462 are shared above threshold, for Fig. 4e: _n_ = 1,892 total CT connections, 628 are shared above threshold, for Fig. 4f: _n_ = 1,158 total CT connections, 495 are shared above threshold; for Fig. 5a: _n_ = 7,063 unique connections (columns). Numbers of replicate experiments per each of the 7,063 connections ranged from 1 to 53, and are listed in Supplementary Table 8; for Fig. 5f: the number of connections assigned to each cluster is plotted in Fig. 5c, and can also be found in Supplementary Table 8 (cluster 1: _n_ = 1,740, cluster 2: _n_ = 366, cluster 3: _n_ = 375, cluster 4: _n_ = 228, cluster 5: _n_ = 602, cluster 6: _n_ = 2,224, cluster 7: _n_ = 102, cluster 8: _n_ = 129, cluster 9: _n_ = 1,297). The number of connections per cortical Cre line can also be found in Supplementary Table 8, for _A93_ : _n_ = 375, C57Bl6/J/ _Emx1_ : _n_ = 1,431, _Chrna2_ : _n_ = 136, _Cux2_ : _n_ = 703, _Efr3a_ : _n_ = 223, _Nr5a1_ : _n_ = 251, _Ntsr1_ : _n_ = 246, _Rbp4_ : _n_ = 1,149, _Rorb_ : _n_ = 185; _Scnn1a_ -Tg3: _n_ = 263, _Sepw1_ : _n_ = 140, _Sim1_ : _n_ = 108, _Syt6_ : _n_ = 150, _Tlx3_ : _n_ = 1,043), and per thalamic projection class was, for core: _n_ = 62, matrix-focal: _n_ = 136, intralaminar: _n_ = 160, matrix-multiareal: _n_ = 302. Figure 6b: _n_ = 385 total CT connections. 

We first defined hierarchy scores of cortical regions based on layertermination patterns of CC connections. First consider a mapping function _M_ CC for CC connections: 

**==> picture [176 x 9] intentionally omitted <==**

which maps a type of connection cluster ( _CTi_ , _j_ ∈{1, …, 9} , where _CTi_ , _j_ denotes the layer termination pattern of the connection from area _j_ to area _i_ for Cre line _T_ ) to either feedforward ( _M_ CC = 1) or feedback ( _M_ CC = −1) type. We search over the space of possible maps to see which map produces the most self-consistent hierarchy. As some transgenic lines have different numbers of connections in different clusters, some maps will lead to particular transgenic lines having very biased feedforward or feedback calls. Thus, we add a confidence measure (conf( _T_ )) for each Cre line _T_ , which decreases the importance of the information provided by a transgenic line to the CC global hierarchy if the calls from that transgenic line are biased. This allows us to reduce the bias in the regions where experiments used more Cre lines that predominantly mark feedforward or feedback connections. The Cre-dependent confidence measure is defined as: 

**==> picture [184 x 11] intentionally omitted <==**

with a global confidence as an average over all the inter-areal connections above the threshold (10[−1.5] ) 

**==> picture [170 x 11] intentionally omitted <==**

We define the initial hierarchical position of an area as: 

**==> picture [241 x 26] intentionally omitted <==**

> The first term, 〈 _M_ CC( _CTi_ , _j_ ) × conf( _T_ )〉 _j_ , describes the average direction of connections to area _i_ , and thus represents the hierarchical position of 

> the area as a target. The second term, −〈 _M_ CC( _CT j_ , _i_ ) × conf( _T_ )〉 _j_ , on the other hand, represents the average direction of connections from area _i_ , depicting the hierarchical position of the area as a source. The hierarchical position of a cortical area is the average between its hierarchical position as source and target. To test how self-consistent a hierarchy is we define the CC global hierarchy score: 

**==> picture [222 x 22] intentionally omitted <==**

## **Clustering analyses** 

Unsupervised hierarchical clustering was conducted with the online software, Morpheus (https://software.broadinstitute.org/morpheus/). log-transforms were calculated on all values after adding a small value (0.5 minimum of the true positive array elements) to avoid log (0). Proximity between clusters was computed using average linkages with Spearman rank correlations as the distance metric. Relative layer density is the fraction of the total projection signal in each layer, scaled by the relative layer volumes in that target. The clustering algorithm works agglomeratively: initially assigning each sample to its own cluster and iteratively merging the most proximal pair of clusters until finally all the clusters have been merged. To compare distances between granular and agranular samples (those that lack L4), we used the median of the other present layers for L4. 

## **Unsupervised discovery of hierarchy position** 

Following the classification of the laminar patterns into nine clusters of CC and TC connections, we used an unsupervised method to simultaneously assign a direction to a cluster type and to construct a hierarchy. 

We performed an exhaustive search over all the maps _M_ CC for the entire set of CC connections, and the most self-consistent hierarchy that maximizes the CC global hierarchy score is obtained when connections of clusters 2, 6 and 9 are of one direction and 1, 3, 4, 5, 7 and 8 are of the opposite direction. As described in the main text, we conclude that clusters 2, 6 and 9 are feedback connection patterns, and the other group of clusters corresponds to feedforward. 

The initial hierarchy score ( _Hi_ 0) of each area _i_ is thus obtained by computing the average direction of connections to and from the area (Eq. (4)) while concurrently searching for the optimal mapping of each lamination pattern to either the feedforward or feedback direction, and is bounded by −1 and 1. After we obtain the initial positions in the hierarchy, the hierarchy scores of all cortical regions are iterated until the fixed points are reached, to refine the cortical hierarchy. Without iterations, the hierarchy scores account only for the number of feedforward and feedback connections each area receives or sends out. Therefore, the initial hierarchy obtained by Eq. (4) alone does not account for the hierarchy positions of the target and source areas that each cortical area makes connections to, and places any two areas with 

## Article 

the same number of feedforward and feedback connections at the same level in the hierarchy. To address this issue, we implement a twostep iterative scheme: 

until the fixed points are reached (20 iterations), using a full mapping function _M_ CC+TC that combines _M_ CC and _M_ TC for CC and TC connections, respectively: 

**==> picture [496 x 62] intentionally omitted <==**

where _n_ refers to iterative steps. The first part (Eq. (6)) refines the hierarchy score of area _i_ on the basis of the current hierarchy scores of its target and source areas. The next part (Eq. (7)) subtracts the hierarchy scores averaged over all areas to remove possible drifts. At every iteration step we also check to see whether the mapping of connection clusters to feedforward or feedback connection needs to change; however, it remained constant through the iterations. We found that the hierarchy scores reach the fixed points after just a few (<5) iterations, and used 20 iterations to find the final hierarchy scores of all areas. These final hierarchy scores are denoted as the hierarchy obtained by CC connections. 

Next, we examined whether and how the TC connections affect the cortical hierarchy, by incorporating layer termination patterns of TC connections in addition to the CC connections. As in CC connections, TC connections are clustered into nine types on the basis of their layer termination patterns. The mapping of the lamination patterns is based on the hierarchy scores of cortical regions obtained by CC connections, while the hierarchical positions of thalamic areas relative to the cortical areas are found concurrently. The mapping of the TC layer termination types to directions is defined as: 

**==> picture [176 x 9] intentionally omitted <==**

similar to the mapping of CC connections in Eq. (1). Because thalamic areas are always the source in TC connections, the initial hierarchy score of each thalamic area _i_ is defined by the average direction of connections from the area: 

**==> picture [199 x 26] intentionally omitted <==**

where the mapping of the lamination patterns, _M_ TC is obtained by searching for the most self-consistent assignment that maximizes the TC global hierarchy score _h_ TC: 

**==> picture [221 x 26] intentionally omitted <==**

The parameters _N_ ff and _N_ fb refer to the numbers of feedforward and feedback TC connections, respectively. The multiplier min( _N_ ff _N_ +ff _N_ , _N_ fbfb )biases the optimization method to preferentially search for mappings that result in roughly equal numbers of feedforward and feedback connections. Without such a weight on equal divide of the connections, the search algorithm decides TC connections to be always feedforward, placing all thalamic areas below cortical areas. 

As with CC connections, we performed an exhaustive search over all the maps _M_ TC for the entire set of TC connections to find the most self-consistent hierarchy that maximizes the TC global hierarchy score. For TC connections, we found that connections of cluster 2 and 6 are of one direction and the rest of the clusters are of the opposite direction. Again, as described in the main text, we conclude that clusters 2 and 6 are feedback, and the rest correspond to feedforward patterns. 

Once the initial positions of the thalamic areas in the hierarchy are obtained, hierarchy scores of thalamic and cortical areas are iterated 

Finally, the effect of CT connections on the hierarchy is considered. Either feedforward or feedback direction is assigned to CT connections depending on the cortical layer from which the connections originate. Specifically, we classified CT connections based on the log10-transformed NPV from layers 5 and 6 of the source areas. Therefore, the mapping of CT connections is described by: 

**==> picture [214 x 11] intentionally omitted <==**

We first determined the predicted direction (feedforward or feedback) of each CT connection based on the hierarchy constructed from CC and TC projection patterns. These directions of CT connections show mixed L5 and L6 source expressions. To classify the CT connections to either L5 or L6 dominance and, subsequently, to feedforward or feedback, we used linear discriminant analysis on log10-transformed NPV values of L5 and L6 lines with a prior that biases the method to yield about equal numbers of L5 and L6-dominant connections. The classifier assigns feedforward direction to connections with stronger L5 source NPV, and feedback direction to L6 dominant connections, using the linear separator. Once directions of CT connections have been obtained, the mappings _M_ CC, _M_ TC and _M_ CT are combined to construct a comprehensive mapping _M_ CC+TC+CT of all connections among cortical and thalamic areas to directions. The initial positions of thalamic regions in the hierarchy are computed by: 

**==> picture [211 x 18] intentionally omitted <==**

where _M_ TC+CT is the mapping of all TC and CT connections. Note that the multiplier min( _N_ ff _N_ +ff _N_ , _N_ fbfb)[used for initial thalamic hierarchy with TC connec-] tions only (which biases thalamus to be towards the centre of the hierarchy) is not needed here, owing to the presence of the CT connections in the computations. However, the bias is not fully eliminated as it influenced the initial assignment of CT and TC connections types to be feedforward or feedback. The initial hierarchy scores are iterated together with hierarchy scores of cortical areas obtained from Eqs. (6, 7): 

_Hin_ −1/2 = 2[1][{⟨] _H nj_ −1 + _M_ CC+TC+CT( _CTi_ , _j_ )⟩−⟨− _j H nj_ −1 + _M_ CC+TC+CT( _CT j_ , _i_ )⟩} _j_ (15) 

**==> picture [177 x 28] intentionally omitted <==**

In this way, we obtained three different versions of cortical hierarchy constructed from: (1) CC connections only, (2) CC connections and thalamocortical connections, and (3) CC, TC, and CT connections. 

We examined how the additional information provided by TC and CT connections affects the self-consistency of the hierarchy by comparing the global hierarchy scores of the three different versions of hierarchy. For this purpose, we compared the global hierarchy scores without any confidence or weight multiplier: 

**==> picture [184 x 21] intentionally omitted <==**

In addition to the hierarchy of all areas, we also constructed the intermodule hierarchy of cortical areas. We used the same mappings obtained from construction of the all-area hierarchy to classify the lamination patterns. For intermodule hierarchy, all the connections to and from each module were used to build the hierarchy among the modules. 

## **Global hierarchy score of shuffled connectomes and ‘perfectly hierarchical’ connectome** 

To evaluate ‘how hierarchical’ the mouse brain is, we generated shuffled connectivity data for the connection patterns, computed the global hierarchy scores, and compared the global hierarchy scores of the shuffled connectomes to that of the mouse brain connectome. The shuffled connectivity is constructed by randomly rearranging sources and targets, while preserving the projection layer patterns and the distributions of source and target areas, within each Cre line. We generated 100 versions of shuffled connectivity data, and calculated their global hierarchy scores as was done with the original connectivity data, described in the previous section. The medians of the shuffled distributions provide an estimate of the lower bound of this score (0.001, 0.044, −0.002, for CC, CC + TC, CC + TC + CT, respectively; Fig. 6c). 

We also generated connectivity data with perfectly self-consistent hierarchy, which provides the upper bound of the global hierarchy score. To do this, we assigned a direction (feedforward or feedback) for each connection in the mouse brain connectivity data, based on the final hierarchy positions of the cortical and thalamic regions. With this ‘true’ mapping of each connection to a direction, the global hierarchy score is computed using Eq. (17), producing values of 0.679, 0.636, and 0.683, respectively, for CC, CC + TC, and CC + TC + CT connections. 

Therefore, comparison of global hierarchy scores allows us to evaluate how hierarchical the mouse brain is compared to the hierarchy by chance (shuffled) and the perfect hierarchy (upper bound). The global hierarchy scores with the shuffled mean subtracted and normalized by the strictly hierarchical data provides a single measure that quantifies the steepness of hierarchy across arbitrarily different connectivity data. 

## **Reporting summary** 

Further information on research design is available in the Nature Research Reporting Summary linked to this paper. 

## **Data availability** 

Data (including high-resolution images, segmentation, registration to CCFv3, and automated quantification of injection size, location, and distribution across brain structures) are available through the Allen Mouse Brain Connectivity Atlas portal (http://connectivity.brain-map.org/). Individual experiment summaries can be viewed using this link: http:// connectivity.brain-map.org/projection/experiment/[insert experimental id]. Experimental ids are listed in Supplementary Table 2. In addition to visualization and search tools available at this site, users can download data using the Allen Brain Atlas API (http://help.brain-map. org/display/mouseconnectivity/API) and the Allen Brain Atlas Software - Development Kit (SDK: http://alleninstitute.github.io/AllenSDK/con nectivity.html). Through the SDK, structure and voxel-level projection data are available for download. Examples of code for common 

data requests are provided as part of the Mouse Connectivity Jupyter notebook to help users get started with their own analyses. Source data generated for this study are provided as Supplementary Tables as indicated throughout. Code and data files for hierarchical analyses are available through the Allen SDK and Github (https://github.com/ AllenInstitute/MouseBrainHierarchy). 

47. Franklin, K. B. J. & Paxinos, G. _The Mouse Brain in Stereotaxic Coordinates_ (Elsevier Academic, 2012). 

48. Kalatsky, V. A. & Stryker, M. P. New paradigm for optical imaging: temporally encoded maps of intrinsic signal. _Neuron_ **38** , 529–545 (2003). 

49. Garrett, M. E., Nauhaus, I., Marshel, J. H. & Callaway, E. M. Topography and areal organization of mouse visual cortex. _J. Neurosci_ . **34** , 12587–12600 (2014). 

50. Ragan, T. et al. Serial two-photon tomography for automated ex vivo mouse brain imaging. _Nat. Methods_ **9** , 255–258 (2012). 

51. Martersteck, E. M. et al. Diverse central projection patterns of retinal ganglion cells. _Cell Rep_ . **18** , 2058–2072 (2017). 

52. Kuan, L. et al. Neuroinformatics of the Allen mouse brain connectivity atlas. _Methods_ **73** , 4–17 (2015). 

53. Wang, Y. et al. Complete single neuron reconstruction reveals morphological diversity in molecularly defined claustral and cortical neuron types. Preprint at https://www.biorxiv. org/content/10.1101/675280v1 (2019).If ref. 53 (preprint) has now been published in final peer-reviewed form, please update the reference details if appropriate. 

54. Gong, H. et al. Continuously tracing brain-wide long-distance axonal projections in mice at a one-micron voxel resolution. _Neuroimage_ **74** , 87–98 (2013). 

55. Bria, A., Iannello, G., Onofri, L. & Peng, H. TeraFly: real-time three-dimensional visualization and annotation of terabytes of multidimensional volumetric images. _Nat. Methods_ **13** , 192–194 (2016). 

56. Wang, Y. et al. TeraVR empowers precise reconstruction of complete 3-D neuronal morphology in the whole brain. _Nat. Commun_ . **10** , 3474 (2019). 

57. Oliveira, G. N., Torchelsen, R. P., Comba, J. L. D., Walter, M. & Bastos, R. Geotextures: a multi-source geodesic distance field approach for procedural texturing of complex meshes. _2010 23rd SIBGRAPI Conf. Graphics, Patterns and Images_ 126–133 (IEEE, 2010). 

58. Blondel, V. D., Guillaume, J.-L., Lambiotte, R. & Lefebvre, E. Fast unfolding of communities in large networks. _J. Stat. Mech. Theory Exp_ . **2008** , P10008 (2008). 

59. Bastian, M., Heymann, S. & Jacomy, M. Gephi: an open source software for exploring and manipulating networks. _Intl AAAI Conf. Weblogs and Social Media_ **3** , 361–362 (2009). 

60. Jacomy, M., Venturini, T., Heymann, S. & Bastian, M. ForceAtlas2, a continuous graph layout algorithm for handy network visualization designed for the Gephi software. _PLoS One_ **9** , e98679 (2014). 

**Acknowledgements** We thank the Animal Care, Transgenic Colony Management and Laboratory Animal Services teams for mouse husbandry and tissue preparation; all the members of the Neurosurgery and Behavior team for viral injections, including those not listed as authors: N. Berbesque, N. Bowles, S. Cross, M. Edwards, S. Lambert, W. Liu, K. Mace, N. Mastan, C. Nayan, B. Rogers, J. Swapp, C. White and N. Wong; H. Gu for cloning of the synaptophysin–EGFP viral vector; E. Lee, F. Griffin and T. Nguyen for intrinsic signal imaging; and J. Royall and P. Lesnar for schematic figure preparation. This work was supported by the Allen Institute for Brain Science and, in part, by National Institutes of Health grants R01AG047589 to J.A.H and U01MH105982 and U19MH114830 to H.Z. We thank the Allen Institute founder, Paul G. Allen, for his vision, encouragement, and support. 

**Author contributions** Conceptualization: H.Z., J.A.H. and S. Mihalas. Supervision: H.Z., J.A.H., S. Mihalas, A.B., L.N., N. Gaudreault, P.A.G., J. Lecoq, S.A.S., J.W.P., A.R.J. and C.K. Project administration: S. McConoughey, S.W.O. and W.W. Investigation, validation, methodology and formal analyses: J.A.H., S. Mihalas, K.E.H., H.C., J.D.W, J.E.K., P.B., S.C., L.C., A.C., A.F., N. Gaudreault, N. Graddis, C.R.G., P.A.G., A.M.H., A.H., R.H., L.K., X.K., J. Lecoq, J. Luviano, P.L., Y.L., M.T.M., M.N., L.N., B.O., E.S., S.A.S., Q.W., A.W. and Y.W. Data curation: J.A.H., K.E.H., J.D.W., P.B., S.C., A.M.H., B.O. and W.W. Visualization: J.A.H., K.E.H., J.D.W., H.C., L.N., D.F., S. Mihalas, M.N. and Y.W. The original draft was written by J.A.H. with input from K.E.H., J.D.W, S. Mihalas, H.C., Q.W., C.K. and H.Z. All co-authors reviewed the manuscript. 

**Competing interests** The authors declare no competing interests. 

## **Additional information** 

**Supplementary information** is available for this paper at https://doi.org/10.1038/s41586-0191716-z. 

**Correspondence and requests for materials** should be addressed to J.A.H. **Peer review information** _Nature_ thanks Claus Hilgetag, Moritz Helmstaedter and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. 

**Reprints and permissions information** is available at http://www.nature.com/reprints. 

## Article 

**==> picture [511 x 330] intentionally omitted <==**

**Extended Data Fig. 1 | Similarity of connection strengths by distance, virus, hemisphere, and** _**Emx1**_ **-IRES-Cre or C57BL/6J mice. a** – **d** , Most experiments were done with the Cre-dependent rAAV tracer, rAAV2/1.pCAG.FLEX.EGFP. WPRE. A subset of left hemisphere injections had a duplicate injection of rAAV with a synaptophysin–EGFP fusion transgene in place of the cytoplasmic EGFP (rAAV2/1.pCAG.FLEX.SypEGFP.WPRE). This tracer allowed us to address whether labelling presynaptic terminals would improve the accuracy with which we could quantify target connection strength, particularly in brain regions that contain mostly fibres of passage. Data consisted of _n_ = 275 experiments (137 EGFP, 138 SypEGFP). These were matched across Cre lines and areas, and represent _n_ = 8 Cre lines and _n_ = 26 cortical areas. For pairs of spatially matched experiments, the average projection strength (log10transformed NPV) measured across the entire brain was lower in SypEGFP than in EGFP experiments (~0.8 log unit when <500 μm apart). However, brain-wide projection values were still highly and significantly correlated. Thus, we included the SypEGFP data sets when indicated for analyses of connectivity patterns from given source areas (but only in comparison with other SypEGFP data sets). **a** , Spearman correlation coefficients ( _r_ ) of normalized projection volumes for all possible pairs of injections (different and same tracer, all in the same Cre line) plotted against the distance between the injection centroids. Linear regressions showed a significant negative slope ( _P_ < 0.0001) with _r_ decreasing as distance between injections increased. **b** , _r_ plotted for injections within 500 μm of each other; slopes were not significantly different from zero and means were not significantly different from each other. Average and s.d. 

for each group is shown by the large symbols on the left (EGFP vs EGFP: 0.81 ± 0.056, SypEGFP vs SypEGFP: 0.79 ± 0.064, SypEGFP vs EGFP: 0.79 ± 0.071). **c** , Quantitative differences in projection strengths measured between replicates with the same virus and between SypEGFP and EGFP (logNPV(EGFP) − logNPV(SypEGFP) injections, all <500 μm apart in the same Cre line ( _n_ = 133 within virus and 222 between virus comparisons). Boxplots show median, IQR, minimum and maximum values; + indicates mean. **d** , Maximum intensity projections from four experiments within 500 μm of each other illustrate overall similarities between replicate injections and tracers ( _r_ shown for each pair). Injections targeted primary visual cortex (VISp) in _Emx1_ -IRES-Cre mice using either EGFP or SypEGFP tracers as indicated. **e** – **g** , Injections into _Emx1_ -IRES-Cre mice were made into visual areas on the left hemisphere, whereas all C57BL/6J mice received injections into the right hemisphere. Following registration to the CCF, which is a symmetric atlas, we identified three pairs of experiments in which the injection centroids were <500 μm apart after we flipped injection site coordinates from the left to the right. Cortical projections were visually similar across both lines and hemispheres, and cortical connectivity strengths (to the 86 cortical targets) from these individual experiments (normalized projection volumes) were positively and strongly correlated as indicated. Thus, in Fig. 2 we merged the _Emx1_ and C57BL/6J data to represent connection strengths from all layers and classes, and in some of the ‘anchor’ groups we used data from both left and right hemisphere injections. 

**==> picture [511 x 348] intentionally omitted <==**

**Extended Data Fig. 2 | Characterization of cortical projection neuron classes and layer selectivity across mouse lines. a** , Brain-wide projection patterns were visually inspected for every experiment and manually classified into one of six categories on the basis of projections to ipsilateral and contralateral cortex, striatum, thalamus, and midbrain, pons or medulla structures as described for IT, PT, and CT classes. **b** – **d** , Unsupervised hierarchical clustering (using Euclidean distance and average linkage) of projection weights validates and reveals major classes of cortical projection neurons. **b** , Each column of the heat map shows one of the 1,081 injection experiments. Colours in the ‘manual PN’ class are coded as in **c** for projection class. Rows show selected major brain regions that distinguish known classes of projection neurons. Values in each cell are the fractions of total brain projection volume in the given region. The dendrogram was split into nine clusters, with two subclusters identified posthoc for cluster 5. The numbers of experiments per cluster were: 1, _n_ = 24; 2, _n_ = 4; 3, _n_ = 204; 4, _n_ = 158; 5a, _n_ = 148; 5b, _n_ = 230; 6, _n_ = 174; 7, _n_ = 12; 8, _n_ = 16; 9, _n_ = 111. The numbers of experiments per projection class were: CT, _n_ = 119; IT, _n_ = 342; IT PT, _n_ = 158; IT PT CT, _n_ = 189; local, _n_ = 100; PT, _n_ = 173. **c** , The relative frequency of experiments from manually assigned projection classes within each cluster is shown. There was significant enrichment of 1, or 2 related, classes in each 

cluster (dots; Fisher’s exact _t_ -test, _P_ < 0.01). **d** , Maximum intensity projections of GFP-labelled axons across the brain from one example per cluster. **e** , Characterization of layer selectivity in wild-type mice and 14 Cre lines derived from injection experiments. Number of experiments per line is listed in Supplementary Table 1. For every injection and line, we assessed layer selectivity on the basis of the manually annotated injection sites. Polygons were drawn around every injection site so that, after registration to the CCF, injection volume in each layer could be informatically derived. A layerselectivity index was calculated for each experiment (the fraction of the total injection volume contained in each layer, scaled by the relative volume of each layer in the injection source region, because layer volumes differ by area). Plots show individual data points and the average layer selectivity index ± 95% confidence intervals (in black) for the set of 15 mouse lines. Red lines in each Cre graph show average values from C57BL/6J experiments. Red lines in the C57BL/6J graph are averages from the _Emx1_ -IRES-Cre experiments, which also labels cells across all layers. There is a bias towards L5 neuron infection in both C57BL/6J and _Emx1_ -IRES-Cre mice, highlighting the importance of using layerselective Cre lines for better coverage of cortical outputs. 

## Article 

**==> picture [511 x 339] intentionally omitted <==**

## **Extended Data Fig. 3 | Computationally removing the distance dependence** 

**of connection weights alters the modular structure of the cortex.** To test the degree to which the spatial proximity of regions affects modularity analysis, we used a power law to fit the distance component of our ipsilateral CC connectivity matrix[29] . Then, we repeated our modularity analysis on the ‘distance-subtracted’ matrix built from these residuals. **a** , Weighted connectivity matrix for 43 cortical areas showing the value of the residuals from a power law to fit the distance component. Rows are sources, columns are targets. Colours on the rows indicate distance-subtracted community structure with varying levels of resolution ( _γ_ = 0.5–1.5 on the _y_ -axis, _γ_ = 0.8 only on the top portion of the _x_ -axis). Columns are coloured by their module affiliation in the distance-subtracted matrix above their module affiliation in the original matrix (Fig. 1e). The inset in the top left corner shows the modularity metric ( _Q_ ) for each level of _γ_ , along with the _Q_ value for a shuffled network containing the same weights. The _Q_ values for modularity in the distance-subtracted matrix were smaller than for the original cortical matrix (for example, 0.2754 versus 0.4638 at _γ_ = 0.8) and the range of values for which 

_Q_ was greater than _Q_ shuffled was narrower (0.7 ≤ _γ_ ≤ 1.7), but some modules were still present in the distance-subtracted cortical connectivity matrix. The difference between _Q_ and _Q_ shuffled was greatest for _γ_ = 0.8. The first distancesubtracted module was comprised of the entire somatomotor module, most of the lateral module, and two regions from the prefrontal module. The second distance-subtracted module contained the visual, auditory, and medial modules, plus most of the prefrontal module and one region from the lateral module (temporal association area). Notably, these modules were like those reported by Rubinov et al.[9] . As _γ_ increased past 1.0, regions began to split from the two large modules in small groups that generally did not reflect the original divisions, except for the auditory areas. **b** , Ipsilateral cortical network in 2D using a force-directed layout algorithm. Nodes are colour coded by module. Edge thickness shows residual values and edges between modules are coloured as a blend of the module colours. **c** , Cortical regions colour-coded by their distance-subtracted community affiliation at _γ_ = 0.8 show spatial relationships. 

**==> picture [483 x 606] intentionally omitted <==**

**Extended Data Fig. 4 |** See next page for caption. 

## Article 

**Extended Data Fig. 4 | Whole-brain single-neuron reconstructions reveal L4** 

**IT projections. a** , L4 neurons are classified into at least three morphological types as shown. **b** , Image shows sparse labelling of L2/3 and L4 neurons in the tamoxifen-inducible _Cux2_ -IRES-CreERT2 driver crossed with the _Ai166_ reporter and using a low dose of tamoxifen via oral gavage for 1 day. L4 neurons were identified on the basis of their apical dendrite and local axons, using additional anatomical context when possible. Reconstruction was performed using Vaa3D-TeraVR on the high-resolution whole-brain image stack (composed of more than 10,000 images, resolution _x_ × _y_ × _z_ : 0.3 × 0.3 × 1 μm) acquired with a two-photon fMOST system. **c** , We identified 25 L4 neurons for complete morphological reconstruction of dendrites and axons for three cell types and three cortical areas. In this Cre line at least, spiny stellate cells (SSCs) were most frequently identified. **d** , Dorsal surface view shows the CC projection patterns from three anterograde tracer experiments into the 

predominantly L4 Cre lines for somatosensory cortex (SSp-m), visual cortex (VISp) and auditory cortex (AUD). **e** – **k** , Each panel shows two examples of reconstructed cells of the same L4 type in somatosensory, visual or auditory cortex. Local morphology for each cell is shown in the inset. Arrowheads indicate axon clusters outside local region. Red, axon; blue, basal dendrite; black, apical dendrite. Consistent with canonical descriptions, we found SSCs in the somatosensory cortex that had only local axon clusters ( **e** ). However, even in these cases, we frequently observed what appeared to be an aborted axon branch (no terminal cluster found; long arrow). We also found SSCs in somatosensory cortex that did have clear axon clusters in nearby areas ( **g** ), and, in auditory cortex, SSCs projected even to the opposite hemisphere ( **f** ). **h** – **k** , Although we identified fewer tufted pyramidal (TPC) and untufted pyramidal (UPC) cell types in this experiment, for both types we still found cells with near and long-range projections. 

**==> picture [511 x 265] intentionally omitted <==**

**Extended Data Fig. 5 | Locations and cortical projection patterns from thalamic tracer experiments. a** , Locations of the thalamic tracer injection centroids (blue dots) mapped onto virtual 2D coronal planes from the Allen CCFv3. To minimize the number of sections shown, all centroids are mapped within 200 μm of their original location. See Supplementary Table 1 (thalamus tab) for more details on Cre lines and coverage. **b** , Example TC projections are shown in a flat map view of the ipsilateral cortical hemisphere for different thalamic nuclei arranged by the clusters identified in Fig. 3 and related to 

cortical modules. Most thalamic clusters projected primarily to a single module (Fig. 3c), but some thalamic regions projected across multiple modules (for example, anteroventral nucleus (AV), ventral anterior-lateral complex (VAL), parafascicular nucleus (PF), and central lateral nucleus (CL)), or projected strongly to both prefrontal and another module; for example, somatomotor (mediodorsal nucleus (MD)-1, ventral medial nucleus (VM)), lateral (paraventricular nucleus (PVT), MD-2, parataenial nucleus (PT)) or medial regions (nucleus of reuniens (RE), anteromedial nucleus (AM)). 

**==> picture [47 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [511 x 563] intentionally omitted <==**

**==> picture [158 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Extended Data Fig. 6 |  See next page for caption.<br>**----- End of picture text -----**<br>


## **Extended Data Fig. 6 | Comparison of corticothalamic projection strengths** 

**derived from EGFP and SypEGFP tracer experiments. a** – **d** , Maximum intensity projections from four experiments within 500 μm of each other targeting VISp (same experiment labelled VISp-3 below) using either EGFP or SypEGFP tracers in the _Rbp4_ -Cre_KL100 (L5) or _Ntsr1_ _Cre_GN220 (L6) line as indicated. **a′** – **d′** , Coronal STPT images near the centre of the densest terminal zone in LGd show axon and presynaptic terminal labelling in LGd and other thalamic targets, including the ventral lateral geniculate (LGd, LGv), the intergeniculate leaflet (IGL) and the lateral posterior nucleus (LP). The anterior pretectal nucleus (APN) in the midbrain is also indicated. SypEGFP labelling is more punctate and has less fluorescence in axons and fibre tracts. **a′′** – **d′′** , Coronal STPT images near the centre of one of the densest terminal zones in the middle of LP. **a′′′** – **d′′′** , Coronal STPT images near the centre of the second densest terminal zone in the anterior part of LP. This image also contains a portion of the terminal zone in the lateral dorsal nucleus (LD). **e** – **h** , Directed, weighted, connectivity matrices (11 × 44) showing log10-transformed normalized projection volumes for the Cre lines representing CT projections labelled from layers 5 ( **e** , **f** ) or 6 ( **g** , **h** ) with EGFP or SypEGFP tracer as indicated. True negatives (including passing fibres) at the regional level were masked and coloured dark grey. The colour map is the same as in Fig. 4. The matrix shows 

relative differences for connections originating from L5 versus L6 (L5 − L6/ L5 + L6) for EGFP-based measures ( **i** ) and SypEGFP-based measures ( **j** ). **k** , Normalized projection strengths for CT targets ( _n_ = 484) were significantly correlated from matched cortical locations between EGFP and SypEGFP tracers for both Cre lines (Spearman _r_ = 0.71, 0.73; _P_ < 0.0001). On average, EGFP CT NPVs were ~0.5 log unit larger than SypEGFP for _Rbp4_ experiments, but were not different for the _Ntsr1_ line. **l** , Normalized projection strengths for CT targets ( _n_ = 484) contacted by L5 or L6 cortical neurons in matched injection locations were also significantly correlated for both EGFP and SypEGFP tracers (Spearman _r_ = 0.51, 0.60; _P_ < 0.0001), although more weakly than for the same line between viruses. Specific connections with different fibre to terminal ratios are coloured by source module (light blue, from VISp; orange, from SSp; dark blue, from RSPagl). **m** , Relative differences in projection strength to LP and LGd are plotted from _n_ = 6 VISp injection experiments (VISp-1 to VISp-6 in matrix rows above) for each Cre line and viral tracer. **n** , Relative difference ratios calculated for L5 to L6 using EGFP are plotted against those obtained using SypEGFP ( _n_ = 484 CT connections, _n_ = 278 above threshold). There is a significant correlation (Spearman _r_ = 0.68, _P_ < 0.0001). Specific connections are coloured by source module (from **l** ) and labelled with the target. 

## Article 

**==> picture [511 x 373] intentionally omitted <==**

**Extended Data Fig. 7 | Validation of informatics-processing steps: CCF registration and quantification from segmentation. a** – **c** , To determine the precision of the registration process on which we rely here for quantification of signal by layer in the cortex, we manually delineated layers 1 to 6b, using background fluorescence in coronal STPT images, for _n_ = 9 cortical areas (ACAd, ORBvl, AId, PERI, SSp-bfd, MOp, VISp, RSPd, and AUDp; see Supplementary Table 3) in _n_ = 4 mice per region. We then quantified the percentage of voxels within each manually annotated layer that were assigned to all cortical layers following automated registration to the CCFv3. **a** , A confusion matrix show the mean percentage of overlapping voxel labels averaged across these areas (individual region data in Supplementary Table 7). **b** , **c** , Boxplots show the median and mean (indicated with +); whiskers show the minimum–maximum range for the percentage overlap for individual experiments ( **b** ) or cortical areas ( **c** , coloured dots). Across these cortical areas, the average percentage overlap ranged from 86 to 96% of voxels appropriately registered for all layers, except for L6b, which was not included in subsequent layer quantifications. For some areas and layers, the precision was worse than others; for example, while 66% of voxels were appropriately assigned to L2/3 in 

ACAd, the remaining 34% were assigned to neighbouring L5. In ORBvl, only 51% of voxels were appropriately labelled for L6a. Note, however, that delineating layer 5 from L6a in ORBvl in coronal sections using just background fluorescence was very difficult even for experienced anatomists, so some of the imprecision may in fact come from the manual drawing. Even with these exceptions noted, in all cases a large majority of voxels were registered and assigned correctly. **d** , **e** , Frequency distributions of informatically derived quantification for manually verified true negative and positive targets. **d** , The numbers of log10-transformed normalized projection values are plotted for all CC and TC targets manually verified as true negative ( _n_ = 24,272) or true positive ( _n_ = 12,921). Most true positive values were between log10 = −4 and log10 = 1. At log10 = −1.5 (red arrow), 639 true negatives remained (2.6%), while 7,100 true positives were still included (54.9%), resulting in a false positive rate of 8.3% at this threshold level. **e** , Numbers of log10-transformed normalized projection values plotted for all CC and TC targets manually verified as true negative ( _n_ = 15,789) or true positive ( _n_ = 4,503). At log10 = −2.5 (red arrow), 362 true negatives remained (2.3%), while 3,335 true positives were still included (74.1%), resulting in a false positive rate of 9.8% at this threshold level. 

**==> picture [493 x 606] intentionally omitted <==**

**Extended Data Fig. 8 |** See next page for caption. 

## Article 

## **Extended Data Fig. 8 | CC projection patterns by layer and class between** 

**reciprocally connected areas with known hierarchy. a** , In the visual module, VISp and VISal (see Supplementary Table 3) are reciprocally connected (black line). VISp is the de facto bottom of visual cortex hierarchy. The output to VISal from VISp is feedforward (FF). The reciprocal connection (VISal to VISp) is feedback (FB). In the FF direction (top), VISp projections from L2/3, L4, and L5 IT projections were densest in L2/3–L5 of VISal, and relatively sparse in L1 and L6 (cluster 4). _Rbp4_ projections from VISp to VISal were densest in L4 and L6, with moderate levels in L2/3 (cluster 8). L5 PT and L6 CT cells projected, albeit sparsely, to L1 and L5 (cluster 2). In the FB direction (bottom), L2/3 IT axons were broadly distributed across layers, with a sparser region in L5 (cluster 6). VISal L4 IT cells projected noticeably more weakly to VISp (as opposed to the panel above), and terminated with a different pattern (L1 and L5/6, cluster 6). L5 IT cells projected densely to superficial layers in VISp (cluster 1). _Rbp4_ axons were dense in L1 and deep layers (cluster 6). Projections from L5 PT and L6 CT cells were also sparse, but present in L1 and L6 (cluster 6). **b** , In the somatomotor module, SSp-bfd and SSs cortex are reciprocally connected. SSpbfd to SSs is FF; the reverse is FB. In the FF direction (top), L2/3 and L4 IT cells preferentially innervate L2/3–L5, with relatively fewer terminals in L1 and L6 (clusters 3 and 4). L5 IT projections densely innervate L1 and L2/3 (cluster 1). _Rbp4_ projections were densest in L4 and L6, with moderate levels in L2/3 

(cluster 8). L5 PT and L6 CT cell projections were sparse, and to L1 and/or deep layers (cluster 2 and 6). In the FB direction (bottom), the patterns looked remarkably like FB projections from VISal to VISp. Note again the strong connection originating from L4 cells only in the FF direction. **c** , VISp (in the visual module) and ACAd (in the prefrontal module) are reciprocally connected. ACAd exerts top-down control of VISp activity (FB); the reverse (VISp to ACAd) is considered FF. In the FF direction (top), L2/3, L4, and L5 cells all preferentially innervate L1 (cluster 1). In the FB direction (bottom), L2/3 cells also predominantly terminate in L1, but L5 cells project to both L1 and deep layers (L5 and L6, cluster 6). Note also there is a potentially significant sub-layer distinction; axons from VISp to ACAd are relatively deeper in L1 (or at the border of L1 and L2/3) of ACAd, compared to the more superficial termination of ACAd axons in L1 of VISp. All panels: overall, FF projections are more often in clusters 1, 4, and 8, and FB projections in cluster 6. Cluster assignments are indicated in each panel; n/a indicates that the connection was either absent or below threshold for clustering. Areas in each module are shown in a top down cortex view and the network as a force-directed layout (edges denote normalized connection density from Fig. 1e). STPT images in the approximate centre of each target region show the laminar distribution of axons arising from labelled neurons in the different Cre lines. Images are rotated so that the pial surface is always at the top of each panel. 

**==> picture [481 x 606] intentionally omitted <==**

**Extended Data Fig. 9 |** See next page for caption. 

## Article 

## **Extended Data Fig. 9 | TC and CT projection patterns and rules between** 

**reciprocally connected areas. a** , Schematic summarizes observed projection patterns between core thalamic nuclei (blue circle) and their reciprocally connected cortical targets (L1–L6 colour coded). Laminar patterns are from Fig. 5g. STPT images of labelled axon terminals between three pairs of core nuclei and primary sensory cortex that perfectly follow rules in both directions. In the FF direction (LGd to VISp, VPL to SSp-ll, VPM to SSp-n), projections are dense in L4 or L4 and L6 (clusters 4, 8). In the FB direction, CT projections predominantly arise from L6. **b** , Schematic summarizes observed projection patterns between matrix-focal thalamic nuclei (orange circle) and their reciprocally connected cortical targets. STPT images of reciprocal connections between PT and ILA, MD and ORBl, and MD and AId illustrate the schematized rules. Projections from these thalamic nuclei belong to clusters with relatively fewer L1 axons (FF-like, clusters 3, 7, 9). The reciprocal CT input is also stronger from L6 (FB), like the core nuclei above. **c** , Three schematics are shown to summarize observed projection patterns between matrix-multiareal thalamic nuclei (red circles) and their reciprocally connected cortical targets. The top schematic shows dense TC projections to L1 (FB) with CT projections originating from L5 (FF). The middle schematic (with relevant example images boxed) shows reciprocal connection patterns in which TC projections target mid-layers (FF-like) and the reciprocal CT input is stronger from L6 (FB). The bottom schematic shows the same TC projection pattern as the top schematic, 

but with CT projections originating approximately equally from L5 and L6. STPT images show reciprocal connections between multiarea-matrix thalamic regions LP, PO, RE, and VM to three cortical targets each. Some regions have target-specific projections that are either FF or FB. For example, different from the LP-to-VISp projection (FB), axons from LP to VISam and ACAd target midlayers as opposed to L1 (clusters 8 and 5, FF), and the reciprocal connection arises more from L6 (typical for FB). Projections from PO, RE, and VM to all three cortical targets are consistent with a FB projection (denser terminations in L1 and either L5 or L6 (clusters 2 and 6). Reciprocal CT projections originate from L5 or, both L5 and L6. We did not see CT input arising equally from both layers or more from L5 when the reciprocal TC projection was considered FF, consistent with the ‘no-strong-loops’ hypothesis[37] . All panels: overall, FF projections from core thalamic regions are in clusters 4 and 8. FB projections from matrix-multiareal thalamic regions are in clusters 2 and 6, like CC FB. The matrix-focal results support the notion that patterns with relatively less L1 involvement (3, 5, 7, 9) are FF, particularly given the strong reciprocal input observed from L6. STPT images are from the approximate centre of the axon termination field for each target region. Cortex images were rotated so that the pial surface is at the top. Cluster assignments (for TC) are indicated in each panel. Text labels above image show FF and FB direction based on relative position in Fig. 6. Dashed lines indicate region borders. 

**==> picture [511 x 375] intentionally omitted <==**

**Extended Data Fig. 10 | Robustness of the hierarchical organization results.** We constructed multiple hierarchies using only C57BL6/J and _Emx1_ -IRES-Cre experiments (WT) or Cre data without the Cre line confidence measure to compare with results in Fig. 6. The hierarchical position of each area _H_ 0 _i_ and the CC global hierarchy score _h_ CC are defined as in Eqs. (4, 5) in Methods, but with the same confidence for all lines, that is, conf( _T_ ) = 1 for all Cre lines ( _T_ ). **a** , **b** , In both cases, connection types 2 and 6 are assigned to one direction (feedback), while other clusters are grouped to the opposite direction (feedforward). Cluster 7 was not identified in the WT data set. **c** , CT connections were also classified as in Fig. 6b for the Cre data. CT connections were not included for WT as these are exclusively defined by Cre lines. **d** , **e** , Global hierarchy scores from the original, observed data, and the distributions of hierarchy scores obtained from shuffled data sets ( _n_ = 100) are shown for CC connections only (green), compared to scores obtained when TC and CT connections are sequentially included (pink, blue). The upper bound scores for an artificially perfect hierarchy using the WT data sets ( **e** ) are 0.630 for CC and 0.601 for CC + TC connections. **f** , _z_ -scores were calculated for the global hierarchy scores compared to shuffled data for each of the three versions of cortical hierarchy (CC, CC + TC, CC + TC + CT). The highest _z_ -scores were observed when using Cre 

line confidence weighting (compared to those with no confidence weighting or wild type data only). **g** , Predicted hierarchical positions of 37 cortical and 24 thalamic areas based on CC, CC + TC, or CC + TC + CT connections. Areas are ordered in each panel by the scores obtained using Cre line data with confidence weighting (Cre conf, black circles). Scores from Cre line data without confidence weighting (grey circles) and scores from wild type/ _Emx1_ - IRES-Cre data (open circles) are plotted for direct comparison. _y_ -axis labels are colour coded by module assignment (for cortical areas). **h** , Robustness of the cortical hierarchy (w/ Cre conf) against individual Cre lines and projection classes. Left, Spearman rank correlation coefficients between the CC and CC + TC hierarchy with _n_ = 13 layer- or class-specific Cre lines included versus each of the Cre lines removed. Right, results when data from Cre lines with the same layer and class were removed together. Removal of these lines and classes produced relatively minor deviations from the overall hierarchy determined with all data. Note that in both panels the _y_ -axis starts at _r_ = 0.85. For all lines and classes, the correlation with the hierarchy using the complete data set is very high. The lowest correlations occurred following removal of _Cux2_ -IRESCre, _Rbp4_ -Cre_KL100, and _Tlx3_ -Cre_PL56. 

Corresponding author(s): Julie Harris 

**==> picture [227 x 33] intentionally omitted <==**

## Reporting Summary 

Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Research policies, see Authors & Referees and the Editorial Policy Checklist. 

## Statistical parameters 

When statistical analyses are reported, confirm that the following items are present in the relevant location (e.g. figure legend, table legend, main text, or Methods section). 

## n/a Confirmed 

The exact sample size ( _n_ ) for each experimental group/condition, given as a discrete number and unit of measurement 

An indication of whether measurements were taken from distinct samples or whether the same sample was measured repeatedly 

The statistical test(s) used AND whether they are one- or two-sided 

_Only common tests should be described solely by name; describe more complex techniques in the Methods section._ 

A description of all covariates tested 

A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons 

A full description of the statistics including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals) 

For null hypothesis testing, the test statistic (e.g. _F_ , _t_ , _r_ ) with confidence intervals, effect sizes, degrees of freedom and _P_ value noted _Give P values as exact values whenever suitable._ 

For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings 

For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes 

Estimates of effect sizes (e.g. Cohen's _d_ , Pearson's _r_ ), indicating how they were calculated 

Clearly defined error bars 

_State explicitly what error bars represent (e.g. SD, SE, CI)_ 

_Our web collection on statistics for biologists may be useful._ 

## Software and code 

## Policy information about availability of computer code 

|Data collection<br>Data analysis|Serial 2 photon images were processed using the Allen informatics data pipeline (IDP), which manages the processing and organization of<br>the images and quantified data for analysis and display in the web application as previously described (Oh et al., 2014 and Kuan et al.<br>2015). Illumination and image acquisition for intrinsic signal imaging were controlled with an in-house GUI software written in Python.<br>For single cell morphologies, following acquisition of the complete fMOST image stack, it was converted to a multi-level navigable dataset<br>using the open source Vaa3D-TeraFly program then reconstructions were performed using Vaa3D-TeraVR software tools built to facilitate<br>semi-automated and manual reconstructions (Bria et al., 2016 and Wang et al., 2019).|
|---|---|
|||
||Unsupervised hierarchical clustering was conducted with the online software, Morpheus, (https://software.broadinstitute.org/<br>morpheus/) for algorithms and for visualization of the dendrogram and heat maps. The software program GraphPad Prism was used for<br>statistical tests and generation of all graphs, and the software program Gephi was used for visualization and layout of network diagrams.<br>The software program Vaa3D was used for visualization of single cell morphologies. Hierarchy analyses were performed as described in<br>detail in Methods. Code and data files for hierarchical analyses are available through the Allen SDK and Github (https://github.com/<br>AllenInstitute/MouseBrainHierarchy).|



For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers upon request. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information. 

## Data 

Policy information about availability of data 

- All manuscripts must include a data availability statement. This statement should provide the following information, where applicable: - Accession codes, unique identifiers, or web links for publicly available datasets 

- A list of figures that have associated raw data 

- A description of any restrictions on data availability 

Data (including high resolution images, segmentation, registration to CCFv3, and automated quantification of injection size, location, and distribution across brain structures) are available through the Allen Mouse Brain Connectivity Atlas portal (http://connectivity.brain-map.org/). Individual experiment summaries can be viewed using this link:http://connectivity.brain-map.org/projection/experiment/[insert experimental id]. In addition to visualization and search tools available at this site, users can download data using the Allen Brain Atlas API (http://help.brain-map.org/display/mouseconnectivity/API) and the Allen Brain Atlas Software Development Kit (SDK: http://alleninstitute.github.io/AllenSDK/connectivity.html). Through the SDK, structure and voxel-level projection data are available for download. Examples of code for common data requests are provided as part of the Mouse Connectivity Jupyter notebook to help users get started with their analyses. Our code for hierarchical analyses is also available through the Allen SDK and Github (https://github.com/AllenInstitute/MouseBrainHierarchy). 

## - Field specific reporting 

Please select the best fit for your research. If you are not sure, read the appropriate sections before making your selection. 

Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences For a reference copy of the document with all sections, see nature.com/authors/policies/ReportingSummary-flat.pdf 

## Life sciences study design 

All studies must disclose on these points even when the disclosure is negative. 

|Sample size<br>Data exclusions<br>Replication<br>Randomization<br>Blinding|In our previously published study (Oh et al., 2014), we demonstrated that an n=1 is a good predictor of connectivity strengths across multiple<br>animals. Here, we also found that the correlations between brain-wide projection strengths from experiments at matched locations are<br>positive and significant (r>0.8, Extended Data Figure 1). Thus, we are able to confidently and comprehensively sample across the entire cortex<br>(and entire brain) with n=1 experiment per source area and Cre line. This consistency is what allows us to map the connectome, which still<br>required 1,000 experiments (i.e. mice) for the coverage we determined was necessary for close to completeness.|
|---|---|
|||
||Image series for each tracer experiment were curated for inclusion based on pre-established QC metrics, and quantitative data had to pass<br>the threshold criteria described in the Results.|
|||
||As stated above, in our previously published study (Oh et al., 2014), we demonstrated that an n=1 is a good predictor of connectivity<br>strengths across multiple animals. Here, we also found that the correlations between brain-wide projection strengths from experiments at<br>matched locations are positive and significant (r>0.8, Extended Data Figure 1). Thus, we are able to confidently and comprehensively sample<br>across the entire cortex (and entire brain) with n=1 experiment per source area and Cre line. This consistency is what allows us to map the<br>connectome, which still required >1,000 experiments (i.e. mice) for the coverage we determined was necessary for close to completeness.|
||Randomization of animals to different groups is not relevant to our study design. We did not have experimental vs. control groups.|
||Image data acquisition and quantitative measures of projection strengths are automated, so blinding was not necessary. Investigators<br>performing manual target analyses were not blinded to injection source or cre line, but this was impossible as the annotation required an<br>anatomy expert to look through every single image. The location would be thus known, and the layer of origin of the cells thus obvious as well.|



## Reporting for specific materials, systems and methods 

|Materials & experimental systems<br>n/a<br>Involved in the study<br>Unique biological materials<br>Antibodies<br>Eukaryotic cell lines<br>Palaeontology<br>Animals and other organisms<br>Human research participants|Materials & experimental systems<br>n/a<br>Involved in the study<br>Unique biological materials<br>Antibodies<br>Eukaryotic cell lines<br>Palaeontology<br>Animals and other organisms<br>Human research participants|Materials & experimental systems<br>n/a<br>Involved in the study<br>Unique biological materials<br>Antibodies<br>Eukaryotic cell lines<br>Palaeontology<br>Animals and other organisms<br>Human research participants|Materials & experimental systems<br>n/a<br>Involved in the study<br>Unique biological materials<br>Antibodies<br>Eukaryotic cell lines<br>Palaeontology<br>Animals and other organisms<br>Human research participants|Materials & experimental systems<br>n/a<br>Involved in the study<br>Unique biological materials<br>Antibodies<br>Eukaryotic cell lines<br>Palaeontology<br>Animals and other organisms<br>Human research participants|Methods|Methods|Methods|
|---|---|---|---|---|---|---|---|
|n/a||Involved in the study|||n/a||Involved in the study<br>ChIP-seq<br>Flow cytometry<br>MRI-based neuroimaging|
||||Unique biological materials|||||
||||Antibodies|||||
||||Eukaryotic cell lines|||||
|||||||||
|||||||||
|||||||||



## Unique biological materials 

Policy information about availability of materials Obtaining unique materials Viral tracers are available through Addgene, the Penn Vector Core, or via request to the Allen Institute. Cre driver lines are available from the repositories indicated in Supplementary Table 1. 

## Animals and other organisms 

Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research Laboratory animals Mus musculus, C57Bl/6J, males and females, Cre driver transgenics, P56 (+/-7 days) Wild animals This study did not involve wild animals. Field-collected samples This study did not involve field-collected samples. 

