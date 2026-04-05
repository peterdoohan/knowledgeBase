bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

Bhattacherjee et al. 

1 

1 

2 

3 

## **Understanding prefrontal cortex functions** 

## **by decoding its molecular, cellular and circuit organization** 

4 5 

6 

7 

Aritra Bhattacherjee[1,2,3#] , Chao Zhang[1,2,3#] , Brianna Watson[2,4] , Mohamed Nadhir Djekidel[1,2,3,5] , Jeffrey R. Moffitt[2,4*] and Yi Zhang[1,2,3,6,7*] 

8 

- 9 1Howard Hughes Medical Institute, Boston Children’s Hospital, Boston, Massachusetts 02115, USA; 

- 10 2Program in Cellular and Molecular Medicine, Boston Children’s Hospital, Boston, Massachusetts 

- 11 02115, USA;[3] Division of Hematology/Oncology, Department of Pediatrics, Boston Children’s Hospital, 12 Boston, Massachusetts 02115, USA;[4] Department of Microbiology, Harvard Medical School, Boston, 13 Massachusetts 02115, USA;[5] Center for Applied Bioinformatics, St. Jude Children's Research Hospital, 14 262 Danny Thomas Place, Memphis, TN, 38105, USA;[ 6] Department of Genetics, Harvard Medical 

- 15 School, Boston, Massachusetts 02115, USA;[7] Harvard Stem Cell Institute, WAB-149G, 200 Longwood 16 Avenue, Boston, Massachusetts 02115, USA. 

- 17 

- 18 

- 19 

#These authors contributed to this work equally 

*To whom correspondence should be addressed 

- 20 E-mail: yzhang@genetics.med.harvard.edu 

- 21 Jeffrey.Moffitt@childrens.harvard.edu 

- 22 

- 23 

- 24 

- 25 Running title: Spatial transcriptomics analysis of mouse PFC 

- 26 

- 27 

- 28 Keywords: Mouse prefrontal cortex, spatial transcriptomics, MERFISH, neuron cluster projection, pain 29 

- 30 

- 31 Manuscript information: 36 pages, 6 figures, 8 supplemental figures, 3 supplemental tables 

- 32 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

Bhattacherjee et al. 

2 

## 33 **Abstract** 

- 34 

35 The prefrontal cortex (PFC) is functionally one of the most complex regions of mammalian 36 brain. Unlike other cortical areas that process single sensory modalities (like vision, touch, smell, etc.), 37 the PFC integrates information across brain regions to regulate diverse functions ranging from cognition, 38 emotion, executive action to even pain sensitivity. However, it is unclear how such diverse functions are 39 organized at the cellular and circuit levels within the anatomical modules of the PFC. Here we employed 40 spatially resolved single-cell transcriptome profiling to decode PFC’s organizational heterogeneity. The 41 results revealed that PFC has very distinct cell type composition relative to all neighboring cortical 42 areas. Interestingly, PFC also adopts specialized transcriptional features, different from all neighbors, 43 with differentially expressed genes regulating neuronal excitability.  The projections to major 44 subcortical targets of PFC emerge from combinations of neuron subclusters determined in a target45 intrinsic fashion. These cellular and molecular features further segregated within subregions of PFC, 46 alluding to the subregion-specific specialization of several PFC functions. Finally, using these unique 47 cellular, molecular and projection properties, we identified distinct cell types and circuits in PFC that 48 engage in pathogenesis of chronic pain. Collectively, we not only present a comprehensive 49 organizational map of the PFC, critical for supporting its diverse functions, but also reveal the cluster 50 and circuit identity of a pathway underlying chronic pain, a rapidly escalating healthcare challenge 51 limited by molecular understanding of maladaptive PFC circuits. 

- 52 

- 53 

## 54 **Major points** 

55 

   - PFC adopts unique cellular composition, distinct from other cortical areas 

- 56 ~~•~~ Selective transcriptomic features emerge in PFC to support its divergent functional portfolio 

- 57 

   - Subcortical projections of PFC assume target-intrinsic specification for innervating clusters 

- 58 • A molecularly defined L5 projection neuron cluster (to PAG) potentially mediates chronic pain 59 pathogenesis 

60 

61 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

3 

Bhattacherjee et al. 

## 62 **Introduction** 

63 

The prefrontal cortex (PFC) is a major region of the mammalian brain that has evolved to perform highly complex behavioral functions. It plays important roles in cognition, emotion and executive function. Unlike somatosensory, visual, auditory, motor or other cortices, which are unimodal (process single modalities like touch, vision, hearing, movement etc.), the PFC engages in complex executive tasks that dynamically coordinate cognition, attention, learning, memory, judgement, etc. to direct the action of an organism[1,2] . As such, dysfunctions of the PFC are associated with many cognitive and neuropsychiatric disorders[3,4] . 

64 

65 

66 

67 

68 

69 70 71 

In addition to regulating intellectual and emotional behaviors, PFC is even involved in modulating pain sensitivity as well as the negative affect of pain[5,6] . Increasing evidence indicates that disruption of this regulation is associated with the development of chronic pain, a rapidly increasing healthcare challenge that affects about 20% of the US population, exceeding cost burden of diabetes or heart disease[7,8] . Chronic pain has been associated with PFC hypoactivity, and transcranial stimulation of the PFC can induce pain relief[9-15] . Although projections from PFC to brainstem has been historically described in descending inhibition of pain[5,16,17] , the underlying molecular mechanism is poorly characterized. Besides, PFC interacts with many downstream targets including the amygdala, nucleus accumbens and thalamus - the major components of the central pain matrix, critical for the sensory or affective symptoms of chronic pain[6,18] . As such, PFC plays an important role in pain “chronification”[5,17] 

72 73 74 75 76 77 78 79 80 81 

81 Thus, a central question is how does PFC organize and manage such diverse functions: from 82 cognitive processes to autonomic pain modulation? To address this question, we and others have 83 previously performed single-cell RNA-seq (scRNA-seq) to decode the cellular heterogeneity of the 84 PFC[2,19] , which revealed a myriad of cell types comprising PFC. However, those studies lacked 85 information about the spatial organization and interaction of the diverse cell types, which are major 86 determinants of the functional diversity of the PFC. A relatively homogeneous histology, with a laminar 87 organization, is the most striking feature of the mammalian cerebral cortex[20-22] . Yet, distinct regions of 88 cortex perform highly specialized functions, including vision, locomotion, and somatosensation, etc. 89 This regional specialization of functions, despite apparent homogeneity, must be due to distinct features 90 at multiple levels including - molecular composition (transcriptome), circuit organization (connectome) 91 and anatomical (spatial) organization of cell subtypes within each cortical area. Decoding such 92 organizational logic is critical not only for mechanistic understanding of cortical function, but also for 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

4 

Bhattacherjee et al. 

93 developing drugs to selectively target neurological disorders of cortical origin, such that drugs directed 94 for either cognitive (frontal cortex) or hearing (auditory cortex) defect, do not disrupt visual or motor 95 function. 

96 Approaching such questions has been historically limited by technological barriers, despite 97 extensive scRNAseq profiling across brain, including cortex[23-25] . However, with recent advances in 98 spatial transcriptomics techniques, such questions can now be addressed. Using multiplexed error-robust 99 fluorescence in situ hybridization (MERFISH), an image-based method for spatially resolved single cell 100 transcriptomics[26,27] , here we vividly decode the spatial organization of the PFC and its various 101 subregions. Our results demonstrate distinct cellular composition of the PFC relative to its adjoining 102 cortical areas. PFC adopts unique molecular features to suit its specific electrophysiological properties 103 different from its adjacent motor cortex. We map molecular identities (and layer localization) of 104 projection neurons to major subcortical targets. Finally, based on projection, transcription and activity 105 marks, we reveal the molecular identity of PFC clusters most significantly affected in chronic pain. 106 

- 107 

108 

109 

110 

111 

- 112 

- 113 

- 114 

115 

116 

- 117 

- 118 119 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

5 

121 

Bhattacherjee et al. 

## 120 **Results** 

122 **MERFISH reveals molecular diversity and location of cell types in the frontal cortex** 

123 To understand the diversity of cell types and determine their spatial organization within the PFC, 124 we performed MERFISH[26][27-29] , the imaging-based method for single cell transcriptomics that uses 125 combinatorial labeling of RNA species with error-robust barcoding which are read through iterative 126 rounds of single-molecule FISH. MERFISH detects the precise location of each RNA molecule to 127 ultimately reveal the spatial organization of diverse cell types within anatomically defined tissue regions 128 (Fig. S1a)[29][28] . We constructed a MERFISH library to interrogate 416 genes consisting of cell-type 129 markers and functionally important genes including- ion channels, neuropeptides, G-protein coupled 130 receptors and a panel of neuronal activity regulated genes (Supplementary Table 1). We collected brain 131 samples from three different mice and prepared rostral to caudal coronal slices covering +2.5 to +1.3 132 from Bregma to broadly image the frontal cortex. Using established analysis pipelines[29] , imaged RNA 133 species were detected, decoded and assigned to individual cells by segmentation based on poly(A) and 134 nuclear (DAPI) staining (Fig. S1a). Overall, we obtained 487,224 high-quality cells in the frontal 135 cortical region from three independent biological replicates with high consistency (Fig. S1b). Expression 136 of individual genes showed good correlation with that of the bulk RNA-seq of the PFC (Fig. S1c). 

137 

138 

139 

140 

141 

142 

143 

144 

After unsupervised clustering, we identified the major cell types including excitatory neurons, inhibitory neurons, and non-neuronal cells that include oligodendrocytes, oligodendrocyte precursors (OPC), microglia, endothelia, astrocytes and vascular leptomeningeal cells (VLMC) (Fig. 1a). Within the excitatory neurons, the major subgroups clustered together, as described by the commonly used nomenclature[23] : the intra-telencephalic (IT) populations of different layers, the extra-telencephalic (ET) neurons, the near projecting (NP) and the cortico-thalamic (CT) populations (Fig. 1a). Within the inhibitory neurons, populations from the medial ganglionic eminence ( _Pvalb_ and _Sst_ ) and the caudal ganglionic eminence ( _Vip_ , _Sncg_ and _Lamp5_ ) clustered distinctly (Fig. 1a). 

145 The major cell types were further clustered into 52 hierarchically organized cell subtypes, 146 including 18 excitatory neuron subtypes, 19 inhibitory neuron subtypes, and 15 non-neuron subtypes 147 (Fig. 1b). Among the excitatory IT neurons, four subtypes were detected in L2/3 (L2/3 IT 1 to 4), two 148 subtypes in L4/5, three subtypes in L5, and two subtypes in L6. Additionally, the L5 ET split in two 149 subtypes, the L6 CT into four subtypes and L5/6 NP formed a single cluster. Among the inhibitory 150 neurons, the Pvalb and Sst each split into six subtypes, the Lamp5 into three subtypes, the Vip and Sncg 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

6 

Bhattacherjee et al. 

151 into two subtypes each (Fig. 1b). Among the non-neurons, the endothelial cells formed five subtypes, 152 Endo1-5, while astrocytes formed three subtypes, oligodendrocytes and OPCs each formed two 153 subtypes. 

154 Projecting these clusters in space (based on MERFISH coordinates) revealed the anatomical 155 layout of the coronal section and depicted precise localization of every single cell (Fig. 1c; inset – 156 magnified view showing individual cells). We found that molecularly similar excitatory neurons are 157 localized together in space to form distinct layers, from which a laminar histology, characteristic of 158 cerebral cortex, emerged (L2/3 IT to L6 CT: outside inwards) (Fig. 1c, left half). Within each layer, the 159 subtypes are further organized in strata (e.g., L2/3 IT 1 to L2/3 IT 4) (Fig. 1c, right half: distribution of 160 subtypes). Inhibitory neurons are broadly distributed and do not form specific layers, although some 161 subtypes appear to be enriched within certain layers or subregions (Fig. 1c). Non-neuronal cells are also 162 broadly distributed, except for enrichment of oligodendrocytes near the fiber tracts (e.g., corpus 163 callosum) and the VLMC in the outermost layer of brain (Fig. 1c, yellow). As evidence of accurate 164 localization, we mapped the RNA location of a few well-characterized genes that are known to express 165 only in specific cortical layers. We found _Otof_ , _Cux2_ and _Fezf2_ mRNAs are respectively localized to L2, 166 L2/3 and L5 on the MERFISH slice, consistent with the ISH Images from Allen Brain Institute (Fig. 167 S1d) 

168 Together, excitatory neurons comprise the largest population in PFC, followed by non-neuronal 169 cells combined and then the inhibitory neurons (Fig. 1d, left). Within excitatory, the IT neurons are the 170 largest subgroup, followed by the ET, NP and CT of deeper layers, respectively (Fig. 1d, middle). 171 Within the inhibitory, Sst and Pvalb neurons are most abundant followed by the Lamp5, Scng and Vip 172 (Fig. 1d, right). 

173 To further evaluate our detection accuracy, we first performed an integrated analysis of the 174 MERFISH data with scRNA-seq data of the PFC from the Allen Institute[23] . All the major subtypes 175 showed strong correlation between the two datasets (Fig. 1e). Similar integrated analysis comparing the 176 MERFISH data with our own scRNA-seq of PFC[19] revealed strong correspondence even at the subtype 177 levels (Fig. S2a-e, see Method).  In fact, MERFISH could classify some of the scRNA-seq clusters at a 178 finer resolution to reveal distinct subclusters (Fig. S2d, e). This point is particularly true for the 

179 inhibitory neurons (e.g. Inh 1, 2 and 7 of scRNA-seq), possibly due to their higher rate of detection in 180 MERFISH (Fig. S2f). 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

7 

185 

Bhattacherjee et al. 

181 Collectively, our results indicate that we have faithfully detected all known cell subtypes and 182 their locations within the mouse frontal cortex, which enables us to analyze their spatial organization 183 along all 3D axes within this region. 

184 

**Marked heterogeneity in spatial distribution of neuron subtypes along AP and DV axes in PFC** 

186 To understand spatial organization of the different neuron subtypes within the anatomically 187 defined PFC region, we aligned our profiled frontal cortex sections with the Allen Mouse Brain 188 Common Coordinate Framework (CCFv3)[30] , a reference created for the mouse brain based on serial two 189 photon tomography images of the 1675 C57Bl6/J mice (Fig. S3a), which outlines the PFC-boundaries 190 within each section. 

191 

192 

193 

194 

195 

196 

197 

198 

199 

200 

201 

202 

203 

Mapping the MERFISH clusters onto the sequential antero-posterior sections revealed the order of cellular organization in 3D throughout the frontal cortex (Fig. 2a). Heterogeneous distribution of several neuron subtypes along the antero-posterior (A-P) and dorsal-ventral (D-V) axes was visually evident. Analysis along the AP axis revealed that L2/3 IT and L4/5 IT neuron subtypes are most enriched in the anterior-most part of the frontal cortex, where all types of L5 and L6 neurons are generally low (Fig. 2b). This density gradient follows a reverse order in posterior direction where deep layer neurons like L5 ET 1 or L6 CT 1-3 are gradually enriched (Fig. 2b). Detailed mapping of various neuron subtypes on the serial brain sections clearly revealed the uneven distribution along the A-P axis (Fig. 2c, S3b). In contrast, some subtypes such as L5/6 NP are modularly distributed and few others (e.g., L5 IT 2 or L6 IT 1) are sparse, but uniform throughout the A-P axis (Fig. 2b). IT neurons generally project to shorter distances within the telencephalon or cortex, while non-IT neurons predominantly project long distances outside telencephalon. This distribution likely favors the anterior bias of IT cells and the posterior bias of non-IT neurons closer to the subcortical region and the major fiber tracts. 

204 There is also strong distribution heterogeneity among the inhibitory neurons, but it follows a 205 pattern of regional enrichment instead of gradual transitions along the A-P axis (Fig. 2b). For some 206 subtypes, such as Lamp5 3, Pvalb 4 and Vip 2, the fluctuation in density along the A-P axis is very 207 prominent (Fig. 2b). Neighborhoods with high density of distinct interneuron subtypes may indicate 208 regulatory hotspots and/or focal points for specific subcortical projections circuits. Such unique 209 organization reaffirms the principle that function begets structure in biological systems. It is only 210 through spatial transcriptomics that such information can be accurately revealed. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

8 

Bhattacherjee et al. 

211 Another readily recognizable feature from the coronal slices is the laminar organization of 212 various excitatory neurons along the DV axis, within each representative section (Fig. 2a). Computation 213 of physical depth inward from the cortical surface revealed that IT neurons locate more superficially 214 within each layer. The L2/3 IT (and L4/5 IT) subtypes are most superficial and closer to the surface of 215 the brain (Fig. 2d). Similarly, in L5, most IT neurons (L5 IT 1, L5 IT 3) are superficial to the other 216 populations of the layer (L5 ET 1, L5 ET 2) (Fig. 2d). Within Layer 6, although L6 IT 1 is superficial, 217 L6 IT 2 mingles with the deepest CT subtypes (Fig. 2d). Plotting each population individually onto a 218 representative coronal section, a highly specific spatial localization of each neuron subtypes in layers 219 inwards from the surface is clearly resolved (Fig. 2f, S4a). This layered organization is precisely 220 achieved during developmental migration of cortical neurons when the migrating wave of each cell type 221 is regulated by cues originating from their final homing site/layer[31] . As such, the types and density of 222 neurons can be influenced by local signals to form circuits or hotspots characteristic of distinct 223 subregions. How such anatomic assemblies locally emerge, remains a matter of further study. 224 The DV organization of GABAergic interneurons was even more interesting. Although, 225 inhibitory neurons, unlike the excitatory, are not organized in layers, most subtypes appear to be 226 enriched within specific excitatory layers or subregions (Fig. 2e). Broadly, the Lamp5 (Lamp5 1 to 3) 227 and Vip (Vip 1 and 2) neurons along with Sncg 1 are more enriched in superficial layers. Lamp5 3, for 228 example, is restricted only to the superficial layer (Fig. 2e, f). However, Sncg 2 is broadly distributed 229 along the entire depth (Fig. 2e, S4b). This appears to be different from neighboring motor cortex, as per 230 recent reports[32] , where all subtypes of _Sncg_ neurons are present only in superficial layers. Additionally, 231 motor cortex also has some subtypes of _Vip_ neurons in deeper layers, which was not detected in PFC. 232 However, the most interesting observation is that specific molecular subtypes of Pvalb and Sst neurons 233 are differentially enriched in various layers along the cortical depth (Fig. 2e). For example, while Pvalb 234 5 and Pvalb 2 have higher density towards the superficial layers, Pvalb 3 and Pvalb 6 are enriched in the 235 very deep layers, and Pvalb 1 and Pvalb 4 are maximally enriched in the intermediate region (Fig. 2e, 2f, 236 S4b). Likewise, Sst 1 and Sst 5 are more superficially enriched, and the remaining are distributed in the 237 intermediate to deep layers (Fig. 2e, S4b). Pvalb neurons can regulate excitatory pyramidal neuron firing 238 through feedforward inhibition delivered directly onto the somatic compartment, while Sst neurons 239 targets distal dendrites of excitatory neurons to impose feedback inhibition[33,34] . Although these 240 interactions are indispensable to calibrate cortical excitatory output[35] , it is striking that inhibitory 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

9 

Bhattacherjee et al. 

241 neurons diversified distinct molecular subtypes to adapt to the molecular diversity of excitatory 242 pyramidal neurons in each cortical layer. 243 

Most non-neuronal subtypes displayed a more broad and dispersed distribution (Fig. S4c), with few exceptions. The vascular leptomeningeal cells (VLMC), for example, line the outermost surface along the cortex. The Oligo 1 and Oligo 2 are enriched near the regions of origin of the white matter tracts (Fig. S3c). The Astro 2 had significant presence in L1 and somewhat greater enrichment in the medial prefrontal region (Fig. S4c). 

244 

245 

246 

247 

248 

249 **Distinct neuron subtypes are uniquely enriched in PFC** 

250 PFC is very distinct in function and connectivity compared to the adjacent cortices. We asked 251 whether this functional and connectivity distinction is associated with its specialized cell composition. 252 To this end, we identified the PFC boundary in each section by aligning with CCFv3 (Fig. S3a). By 253 projecting the cells identified from the alignment as ‘in’-PFC onto the combined UMAP of frontal 254 cortex (Fig. 3a), we found that some subtypes of excitatory neurons are selectively biased ‘in’, and some 255 others ‘out’ of the defined PFC region (Fig. 3a), indicating different cellular composition in PFC and the 256 adjacent areas. Relative population enrichment calculation showed that L2/3 IT 1, L5 ET 1 and L5 IT 1 257 are about 8 folds enriched within the PFC, whereas L6 CT 2 and L6 CT 3 are enriched by more than 2 258 folds (Fig. 3b). In contrast, L2/3 IT 4, L4/5 IT 1 or L6 IT 1 are markedly depleted (4-8 folds) in the PFC 259 (Fig. 3b). When mapped onto the representative coronal section, the enriched, depleted and unbiased 260 populations were clearly visible with respect to the boundaries of the PFC (Fig. 3c). Inhibitory neurons, 261 although less abundant, exhibit clear subtype selectivity across all the major types in PFC (Fig. 3b). 262 Switching of Pvalb subtypes (~2 fold enriched in Pvalb 3 and 4, and depleted in Pvalb 1, 2, and 6), 263 depletion of Sncg 2 and enrichment of Sst 4 and 6, are the most prominent features (Fig. 3b, S5a). Also 264 notably, Lamp5 3, the most superficially located interneuron (L1) is the only enriched Lamp5 neuron in 265 PFC (Fig. 3b). The relative proportions of specific IT, ET and CT subtypes are intimately tied to the 266 projections of a cortical area (inside and outside the telencephalon). The selection of specific 267 interneurons determines the precise excitatory-inhibitory balance in the input/output circuits of the 268 projections. In combination, these circuit motifs likely serve as a blueprint for the specialized functions 269 of a cortical area, and PFC is clearly organized into a highly selective assembly in this regard. 

270 The PFC has distinct functional subregions from its dorsal to ventral end, viz. anterior cingulate 271 cortex (ACAd), prelimbic cortex (PL), infralimbic cortex (ILA) and dorso-peduncular cortex (DPP) 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

10 

Bhattacherjee et al. 

272 (Fig. 3d). We asked whether these subregions have distinct cellular composition. Indeed, clustering with 273 the normalized cell proportions across all subregions revealed the most enriched excitatory neurons in 274 each subregion (Fig. 3e). Projecting cell types on to a coronal slice with subregion demarcations 275 revealed heterogeneity of subtype distribution across different subregions (Fig. 3f). For example, L5 ET 276 1 is enriched in PL and ILA (but depleted in ACAd), while L6 CT 2 is mainly in ILA and L5 IT 3 is 277 mainly in ACAd (Fig. 3e, f – enriched cells in 3e labeled red fonts). We also estimated the percent 278 abundance of each cell type in each subregion (Fig. S5b). For example, L5 ET 1, L6 CT 2, L6 CT 3 or 279 L6 CT 4 as well as inhibitory subtypes like Pvalb 5 or Sncg 2 are enriched in the infralimbic (ILA) 280 relative to other subregions, while L2/3 IT 4, L4/5 IT 1, L5 IT 3 and especially L6 IT 1 are depleted in 281 this subregion. Similarly, the dorsal anterior cingulate (ACAd) is enriched in L6 IT 1 or L2/3 IT 4, but 282 depleted in L2/3 IT 1, L5 ET 2, L6 CT 2, L6 CT 3, L6 CT 4. Strikingly, the prelimbic (PL) maintains a 283 steady share of cells from most subpopulations except for a higher percentage of L2/3 IT 2 and L4/5 IT 284 2.  It is well established that many behavioral functions are specifically regulated by distinct subregions 285 of the PFC. For example, conditioned fear response or trauma (as evidenced in PTSD) is encoded in the 286 ILA[36] , while cue or context-associated reward memory is encoded in PL[37,38] , and compulsive behavior 287 (often associated with drug addiction) is associated with ORBm[39] . Thus, revealing the differential 288 neuron subtype distribution in the different PFC subregions may help link the PFC subregion-specific 289 functions to the various differentially distributed neuron subtypes. 

290 

291 **Unique transcriptional signatures emerge in PFC** 

292 Functional differences across brain regions often underlie molecular adaptations[23] . The cortex is 293 believed to be no exception. Thus, we asked whether the distinctive functions and cellular organization 294 of the PFC is associated with specialized molecular features by comparing the transcriptome of PFC 295 with that of the adjacent cortical regions. Indeed, a large number of genes interrogated in the MERFISH 296 library are differentially expressed between the PFC and the neighboring cortices (Fig. 4a). Among the 297 416 genes analyzed, 54 were significantly enriched and 40 depleted in PFC (adjusted p-Value <0.05; 298 DEG >20%) (Supplementary Table S2). Mapping expression of significantly enriched ( _Nnat_ ) or 

299 depleted ( _Scn4b_ ) genes onto the coronal section showed clear enrichment or depletion in the PFC region 300 (Fig. 4b), which is consistent with the ISH data from the Allen Brain Institute (Fig. 4c), validating our 301 MERFISH results. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

11 

Bhattacherjee et al. 

302 We next asked whether specific types or categories of genes are selectively enriched or depleted 303 in PFC. The differentially expressed genes had a strong representation of several ion channels and some 304 key neurotransmitter receptors- which can impart very distinct electrical properties of the PFC relative to 305 adjoining cortices[40] . In the ion channels group, several potassium channels are enriched or depleted 306 (Supplementary table 2). The voltage-gated potassium channels subtypes[40-42] , especially delayed 307 rectifiers ( _Kcna2, Kcnb2, Kcnc2, Kcnc3, Kcnq3, Kcnq5_ ) are depleted (Fig. 4a, Supplementary table 2). 308 However, some other delayed rectifiers (e.g., _Kcna1, Kcna4, Kcna5_ , etc.) are not changed 309 (Supplementary table S2). On the other hand, the inward ( _Kcnh7)_ and outward ( _Kcnh5_ ) rectifier 310 channels are depleted (Fig. 4a). Additionally, enrichment of BK channel like _Kcnmb4_ , and reciprocally 311 enriched modifier/silencer _Kcng1_ (up), _Kcnf1_ (up) but _Kcnv1_ (down), were also observed (Fig. 4a, 312 Supplementary table S2) Interestingly, _Kcnn3_ is upregulated, that controls neuronal firing through after313 hyperpolarization and its mutation is implicated in schizophrenia and bipolar disorder[43] . Apart from 314 potassium, some prominent calcium channels ( _Cacna1e, Cacna1h,_ Fig. S6a) and sodium ( _Scn3b_ ) 

- 315 channels, which have been implicated in major neurological disorders like autism and epilepsy[44-47] , are 316 also enriched. 

- 317 Apart from gated ion channels, another striking observation is the selective enrichment of _Gria1_ 318 (Fig. 4a), a principal ionotropic AMPA glutamate receptor subunit, in PFC. A GluA1 (protein product of 319 _Gria1_ gene) dimer binds a GluA2 (from _Gria2_ gene) dimer to form a tetrameric ionotropic glutamate 320 receptor. The GluA1 is strongly implicated in several neuropsychiatric disorders (schizophrenia, 

- 321 epilepsy, depression), chronic pain (increase) and drug addiction (decrease)[48] . Its expression in PFC 322 declines with age and GluA1 is also implicated in Alzheimer’s disorder[49] . More interestingly, _Cacng8_ , a 323 transmembrane AMPA receptor-regulating auxiliary subunit, is also enriched within PFC (Fig. 4a). It 324 regulates trafficking and gating of AMPA receptors and is implicated in several neuropsychiatric 325 disorders (attention deficit or personality disorder)[50,51] . Enrichment of _Cxcl12_ (Fig. 4a, S6a) is likely a 326 final proof of the functional diversity of PFC. Aa a chemokine, _Cxcl12_ plays roles from sculpting 

- 327 inhibitory neuron synapses to neuro-immune interactions, which in the adult cortex are characteristic of 328 the PFC[52-54] . 

- 329 To globally represent the remarkable transcriptional features of PFC neurons, we calculated the 330 “PFC signature”, the average expression of the top 10 enriched genes minus top 10 depleted genes. 331 When values for this index were projected (as red color) onto cells in the original UMAP, the PFC- 

- 332 enriched excitatory neurons clearly clustered and emerged (Fig. 4d). When PFC signature was mapped 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

12 

Bhattacherjee et al. 

333 onto a representative coronal section, it localized precisely within the anatomical limits of the PFC (Fig. 334 4e), indicating a distinct molecular composition of the PFC relative to the adjacent cortices. 

335 

## 336 **iSpatial revealed transcriptome-wide PFC-enriched genes and functional pathways** 

337 To expand our spatial mapping of gene expression to the transcriptome scale, we next combined 338 scRNA-seq with MERFISH to make predictions for spatial genes expression enrichment in PFC for 339 genes not measured with MERFISH. To this end, we integrated our prior PFC scRNA-seq data[19] and 340 current MERFISH data to predict the expression pattern of all genes using iSpatial[55] , a bioinformatic 341 tool we developed. The analysis revealed 190 PFC-enriched and 182 PFC-depleted genes (Fig. 4f, 342 Supplementary table S2). Mapping enriched and depleted candidate genes predicted by iSpatial, _Cdh13_ 343 and _Abcd2_ respectively, on to a coronal section revealed consistent localization with respect to the PFC 344 boundaries (Fig. S6b), which is in line with the Allen Brain ISH results (Fig. S6b). 

345 Gene Ontology enrichment analysis of the 364 spatially differentially expressed genes revealed 346 _biological function_ categories highly enriched in transporters, channels and receptor activity, which are 347 known to modulate membrane potential (Fig. 4g). Depletion of voltage-gated potassium channels or 348 transmembrane potassium transporter concur with a poised state of activity that PFC neurons must 349 maintain for working memory function, a feature not essential for adjacent motor or sensory cortices[42,56] . 350 Greater enrichment of ‘postsynaptic neurotransmitter activity’ or ‘glutamate receptor activity’ (Fig. 4g) 351 relative to adjacent cortices reaffirm that PFC retains significant plasticity compared to these regions, 352 even in adult. Curiously, some functions like ‘gated channel’ or ‘cation channel activity’ are both 353 enriched and depleted (Fig. 4g). This indicates that PFC likely uses a different subset of receptors (class 354 switching) for the same functions compared to adjacent cortices to adapt to its distinct 355 electrophysiological needs. 

356 A signaling pathways enrichment analysis of these 364 genes revealed opioid signaling, 357 endocannabinoid pathway and glutamate receptor signaling as the top three pathways (Fig. S6c). While 358 glutamate signaling is widespread in cortex, opioid and cannabinoid signaling are more uniquely 359 characteristic of the PFC and are known to be essential for normal physiological functions of mood, 

- 360 memory, feeding, etc.[57-60] . This indicates that the distinct molecular composition of PFC is indeed tied to 361 its specialized functions. 

362 Decoding the transcriptome-wide, spatially enriched, gene expression patterns also allowed us to 363 investigate whether there is expression bias between subregions of the PFC. Indeed, we detected several 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

13 

Bhattacherjee et al. 

364 genes (e.g., _Nnat_ , _Fezf2_ , _Nr4a1_ , and _Scn4b_ , etc.) that are preferentially expressed in certain subregions 365 of the PFC (Fig. 4h, S6d), which are also validated in Allen Brain ISH data (Fig. S6d). Thus, subregion366 specific functions of PFC are potentially enabled by their discrete molecular compositions imparting 367 specific electrical and signaling properties. 

368 

369 **Spatial organization predicts subtype-specific interactomes in PFC** 

370 Extensive local processing of convergent and divergent signals is one of the principal 371 characteristics of cortex and is particularly prominent in PFC, an area that integrates sensory/cognitive 372 inputs in real time to govern executive function[61] . Integration of multilevel (thalamic, cortical or 373 subcortical) inputs, their transfer through cortical layers, and modulation by interneuron inhibition as 374 well as disinhibition all rely on extensive local interactions between neurons that are neighboring or 375 located in close proximity within PFC[34,62-64] . Given that MERFISH allowed the mapping of the precise 376 location of every cell in PFC, we explored the potential cell-cell interactions at the cell subtype level. To 377 this end, we inspected the cell subtypes composition of the neighboring cells for each cell and calculated 378 the enrichments of paired subtype-subtype colocalizations. Enrichment of proximity was notable 379 amongst many groups of cells (Fig. S7a). IT subtypes of L2/3 are closely apposed in the superficial 380 layers and engage in cortico-cortical interactions to integrate signals from sensory and association 381 cortices (Fig. S7a). Interestingly, most of these subtypes have interactions with L4/5 IT subtypes (Fig. 382 S7a) that receive exclusive inputs from thalamus or lower order cortex (since PFC has no clear L4), and 383 are known to relay processed information mainly to L2/3[65] . This observation reinforces the notion that 384 spatial organization of neuronal types reflect the order of information flow within the circuits they 385 comprise, which in turn emerges as the systematic layered cortical structure.  Interestingly, our analysis 386 revealed specific interactions in the deeper layers that may not be apparent from histological 387 organization alone. For example, L6 IT neurons (like L6 IT 1) share proximity with specific ET neurons 388 (L5 ET 2), revealing subtype selectivity (and in turn circuit selectivity) within L5-L6 communication 389 (Fig. S7a). Subtype selectivity is perhaps most important in excitatory-inhibitory coupling. The 390 inhibitory _Pvalb_ neurons directly access the soma of excitatory pyramidal neurons to regulate firing 391 through feed forward inhibition[66] . Preferential pairing of many excitatory subtypes with one or few (but 392 not all) specific Pvalb subtypes were detected in our analysis (Fig. S7a). For example, L5 IT 3 scored 393 the highest proximity with Pvalb 1, while L5 ET 2 (located within the same layer) has greater interaction 394 probability with Pvalb 6 (Fig. S6a- highlighted boxes). Mapping cells on to a representative coronal 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

14 

Bhattacherjee et al. 

395 section revealed the relative proximities of each of these two excitatory-inhibitory pairs, and also a 396 different spatial enrichment of the Pvalb 1 and Pvalb 6 subtypes (Fig. S7b). 397 

In summary, MERFISH measurements in the PFC allowed us to provide an entry point (or repository) for predicting subtype-specific synaptic interactions in the 3D anatomical space, which can be then studied by using appropriate experimental approaches. 

398 

399 400 

401 **Spatial and molecular organization of PFC projection circuits to major subcortical targets** 

402 It is well known that the PFC excitatory pyramidal neurons project to different subcortical targets 403 including striatum, nucleus accumbens, thalamus, hypothalamus, amygdala, periaqueductal gray or 404 ventral tegmental area[18,67] . However, the spatial organization and whether different neuron subtypes 405 project to different targets are not well characterized. 

406 A prior study has performed retrograde labeling and scRNA-seq for some of these major targets 407 of labeled PFC neurons[2] . We integrated our PFC MERFISH data with this dataset to predict the PFC 408 neuron subtypes with spatial/layer location projecting to these different targets. Through joint 409 embedding and supervised machine learning, we could assign respective projection identity to the 410 molecular clusters organized in space within the PFC (Fig. 5a). An overlap of the MERFISH and 411 scRNA-seq clusters through UMAP visualization revealed a strong correspondence (Fig. 5b, S8a). The 412 ROC curve for the prediction model independently predicted 6 different projection targets with high 413 confidence, including contralateral PFC (cPFC), dorsal striatum (DS), hypothalamus (Hypo), nucleus 414 accumbens (NAc), periaqueductal gray (PAG), and amygdala (Amyg) (Fig. 5c). Mapping these 415 projection cells onto a coronal slice of frontal cortex revealed the identity and spatial organization of 416 neurons that project to each of these 6 targets within the PFC (Fig. 5d). Distinct spatial localization of 417 each of these 6 groups of cells can be visualized when mapped individually on the coronal slice (Fig. 418 S8b). This analysis allowed us to associate different subsets of each neuronal type that project to 419 different regions with their location within the brain (Fig. 5e), which reveals that most of the target brain 420 regions receive projection from more than one neuron subtypes. For example, the amygdala receives 421 projections from all four subtypes of L6 CT neurons as well L5 ET 1 neurons, but the majority comes 422 from L6 CT 2. Likewise, the hypothalamus receives its projections from L5 ET 1 and L6 CT 1; dorsal 423 striatum from L6 CT 1, 2, and 3; and NAc gets mainly from L6 CT 1, L5 ET 1 and some from L6 CT 2. 424 However, one exception to the general rule is the PAG, which receives its projections almost exclusively 425 from L5 ET, predominantly from L5 ET 1 (and some from L5 ET 2). Consistent with prior knowledge, 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

15 

Bhattacherjee et al. 

426 superficial layer IT neurons project to the contralateral hemisphere of PFC[68] . It should be noted that 427 each of these target brain regions are involved in many different behavioral functions. For example, 428 amygdala alone is implicated in fear, addiction, emotion, memory and pain[69-71] . It is expected that inputs 429 will likely to be received from diverse projections (of different neuron subtypes) to selectively trigger 430 specific synapses/pathways to sustain the functional complexity of PFC. 

431 To validate our computational model-based neuron projection predication, we performed 432 retrograde tracing from two of these target regions by injecting retrograde AAV virus into the PAG and 433 the amygdala to drive mCherry expression.  Four weeks after the injection, we prepared cryosections 434 and performed single molecule FISH (RNAScope) to co-label mCherry RNA and the respective cell435 type specific markers. Consistent with the prediction, all mCherry expressing PAG retro-traced PFC 436 neurons exclusively colocalized with _Pou3f1,_ a selective marker for L5 ET 1 and L5 ET 2 (Fig. 5f). In 437 contrast, colocalization of mCherry was detected for both _Pou3f1_ (L5 ET 1) and _Foxp2_ (L6 CT) for 438 amygdala as predicted (Fig. S8c). These data support the accuracy of our circuit predications. 

439 

440 **Identifying PFC neuron subtypes involved in chronic pain** 

441 Functions of PFC in cognition or execution are most widely studied. However, besides those 442 voluntary behaviors, PFC also plays a pivotal role in autonomically modulating pain perception, and 443 aberrations in this process is emerging as a major player in pain “chronification”[5,14] . While chronic pain 444 is escalating as a leading healthcare challenge[7] , molecular underpinnings of the dysfunction remain 445 unknown.  Chronic pain has been strongly associated with transcriptional adaptations across the 446 PFC[5,72,73] , the spatial or cell type-specific resolution of these changes are less clear. To explore the 447 utility of our MERFISH datasets, we attempted to identify the PFC neuron subtypes involved in chronic 448 pain by identifying the neuron subtypes that undergo the strongest transcriptional response in chronic 449 pain. 

450 To this end, we utilized the well-established spared nerve injury (SNI) model of chronic 451 neuropathic pain in mice[74] where two of the three branches of the sciatic nerve are transected (Fig. 6a), 452 which causes a state of chronic neuropathic pain in hind paw that lasts for months. Six weeks after 453 surgery, brains from 3 pairs of sham and SNI mice were collected and characterized with MERFISH 454 (Fig. 6a).  Of all the neuronal subtypes, L5 ET 1 registered the strongest transcriptional response (with 455 largest total number of differentially expressed genes), followed by the L6 CT 2 and L5 ET 2 (Fig. 6b). 456 Lesser changes were detected in L6 CT 3, L5 IT 1, L6 IT 2, L2/3 IT 2 and L4/5 IT 2 (Fig. 6b). No 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

16 

Bhattacherjee et al. 

457 significant changes were detected in the other 30 clusters despite many of the excitatory neuron subtypes 458 being highly abundant in PFC, suggesting these clusters are minimally affected in chronic pain. 459 Interestingly, the two highest impacted clusters respectively project to PAG (L5 ET 1) and amygdala 460 (L6 CT 2) (Fig. 5e), the two major hotspots known to regulate sensory and affective aspects of pain[5,71] . 

- 461 Chronic pain is known to inflict strong and sustained hypoactivity across the PFC[9,12,14,75] . We 462 asked whether this can be detected in the baseline expression of neuronal activity-regulated genes 463 (ARGs) to identify prominently affected neuron subtypes. We calculated ARG score using the mean 464 expression of a panel of 5 ARGs (Arc, Junb, Fos, Npas4, Nr4a1) and compared between sham and SNI 465 groups. We observed a strong and widespread reduction of ARG score when it is plotted on 

- 466 representative coronal sections (Fig. 6c). A subregion-specific calculation revealed that the ACAd and 467 PL are the most impact PFC regions (Fig. 6d). We next compared the differences of ARG score across 468 the individual excitatory neuron clusters (Fig. 6e), and found it is downregulated in several clusters, 469 including those exhibiting transcriptional changes (e.g., L5 ET 1, L6 CT 3, Fig. 6b). 

- 470 To validate chronic pain-induced hypoactivity across PFC, we performed single molecule FISH 471 (smFISH) to compare Fos expression between sham and SNI brain sections. Although sham shows a 472 baseline Fos activity in PFC, a general Fos depletion is obvious in the SNI (Fig. 6f). Co-staining Fos 473 with Pou3f1, a selective marker for L5 ET1, revealed significant Fos depletion in this neuron subtype in 474 the SNI brains (Fig. 6g, h). 

- 475 Despite the conventional knowledge that a PFC-PAG circuit is involved in descending 

- 476 modulation of pain[5] , its cell type identity or changes in chronic pain were unclear. Our findings revealed 

- 477 the molecular identity and spatial organization of this circuit: the L5 ET 1 neurons with PAG projection 

- 478 (Fig. 5e), which are strongly deactivated in chronic pain (Fig. 6g) with the maximum transcriptional 

- 479 adaptation (Fig. 6b). Additionally, we also identified at least two CT subtypes in L6 (L6 CT 2 and 3) 

- 480 that project to limbic structures like amygdala, NAc and hypothalamus (Fig. 5e) that may be involved in 481 the affective response to pain. 

- 482 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

17 

484 

Bhattacherjee et al. 

## 483 **Discussion** 

485 In this study we present an account of how the PFC is distinctly organized at the cellular, 486 molecular and projection levels relative to the adjacent regions within the frontal cortex. We exploit this 487 characterization to reveal the molecular identity of key neuron subtypes that are engaged in chronic pain, 488 and, more broadly, we provide a resource for the systematic mapping of functional ensembles and 489 circuits selectively engaged in various cognitive and executive functions associated with PFC. Spatial 490 transcriptomics is a rapidly growing field[76] and similar to recently reported brain regions[29,32,77] , 491 MERFISH enabled a systematic decoding of PFC’s cellular and molecular organization. 

492 

493 **The diversity of PFC neuron subtypes is consistent with its functional diversity** 

494 We observed that there were a variety of neuronal subtypes largely specific to the PFC or to 495 surrounding regions (Fig. 3a-c). Cellular composition of a cortical area should be predominantly 496 governed by the input and output circuits associated with its function. This regional neuronal subtype 497 specificity, in turn, may underlie the unique properties of the PCF relative to other cortical regions. For 498 example, the PCF is agranular and lacks a typical L4, associated with thalamic input, it receives long499 range inputs across all of its layers, and PFC neurons project to subcortical targets from almost all layers 500 while PFC neurons engage in reciprocal connections with most of these functions[78,79] . Perhaps for the 501 diverse functions, there is a 2-fold enrichment of the superficial-most IT neurons (L2/3 IT 1) to handle 502 the cortico-cortical communications, but the subsequent IT populations (L2/3 IT 4 or L4/5 IT 1) are 503 markedly depleted to make room for enrichment of L5 IT 1 or L5 ET 1 that engage in long distance 504 subcortical projections. Enrichment of two CT subtypes (L6 CT 2 and 3) is consistent with the 505 observation that CT neurons of PFC, unlike other cortices, project to several subcortical targets (Fig. 506 5e), rather than thalamus alone. Notably, two of these enriched neuron subtypes (L5 ET 1 and L6 CT 2) 507 eventually emerge as key subtypes engaged in chronic pain, a function exclusively performed by PFC 508 (Fig. 6). 

509 Depletion of certain subtypes of Pvalb (Pvalb 1, 2, 6), which also accounted for an overall lower 510 count of Pvalb neurons in the PFC (relative to the adjacent regions), suggests that feedforward inhibition 511 is differently organized in PFC. This either indicates an overall lower level of feed forward inhibition 512 and perhaps a greater flexibility in excitatory-inhibitory balance; or larger receptive fields are covered 513 by individual Pvalb neurons, synapsing with more pyramidal neurons towards a goal of regional 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

18 

Bhattacherjee et al. 

514 synchronization. In either case, this is an important observation as functional imbalance of Pvalb 515 neurons has been implicated in almost every PFC-associated diseases, such as schizophrenia[80] , bipolar, 516 depression, and chronic pain[81] . It should be noted that detection of such regional differences would not 517 be possible without the spatial profiling techniques like MERFISH. 

- 518 Besides cellular composition, we detected strong transcriptional features unique to the PFC. We 519 found expression of a large number of ion channels and receptors is selectively increased or decreased in 520 PFC relative to the adjacent cortical regions (Fig. 4). It is generally appreciated that different cortical 521 regions have different baseline electrical properties and qualitatively different activity patterns, which in 522 turn is critical for its specific function[23] . For example, sensory cortices, such as visual cortex, have 523 millisecond scale dynamics which is believed to be much faster than that of frontal regions involved in 524 decision, deliberation or short-term memory. Recording of electrical field potentials across cortical areas 525 provide strong evidence supporting such regionally variable activity patterns[82,83] . However, the 526 biological substrates underlying such functional differences have been less clear. Our findings revealing 527 preferential expression or repression, or even subtype switch of a wide range of cation channels and key 528 glutamate receptor subunits in PFC establish a foundation for identifying the potential biological 529 substrates explaining the diverse PFC functions. 

- 530 

- 531 **The diverse projections of the PFC neuron subtypes** 

- 532 As the apex controlling center for cognitive, executive and emotional behaviors, PFC has one of 533 the most diverse efferent projection profiles amongst all cortical areas. However, a striking observation 534 was that while targets like PAG receives projection from a more homogeneous molecular subtype in L5 535 (L5 ET), most other brain regions receive heterogeneous projections from multiple cell types of different 536 layers (Fig. 5). Although intriguing, this may in fact reflect a more sophisticated model of top-down 537 control by PFC. Most of these target regions such as amygdala, striatum, nucleus accumbens, and 538 hypothalamus engage in many different behavioral processes, which may also be regulated by distinct 539 groups of neurons within each of these target regions. Accordingly, different lines of afferent projections 540 from PFC can synapse on to different neuron populations to form separate circuits within a target and 541 thereby separately modulate different behaviors under different contexts. Additionally, different 

- 542 subtypes in separate layers can receive distinct upstream inputs within PFC that can be separately 

- 543 relayed to the targets through specific projection clusters. For example, L5 ET1 and L6 CT2 may receive 544 different upstream inputs in PFC and can also project to separate cell types within amygdala to modulate 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

19 

Bhattacherjee et al. 

545 different behaviors in separate contexts (Fig. 5e). Further work in this direction should reveal the 546 cellular and molecular organization of all PFC projection circuits and identify specific ensembles 547 engaged by different behaviors. 

548 

## 549 **The L5 ET1 neuron subtype might regulate chronic pain through PFC to PAG projection** 

550 We identified the key cell types that are specifically impacted in PFC under chronic pain (Fig. 6). 551 Amidst the rising prevalence of chronic pain and emerging consensus that transition to chronic pain is 552 centrally regulated, there has been little clarity about the cellular and molecular mechanisms underlying 553 the chronification, which is key to therapeutic targeting. Previous studies have shown that transcranial 554 stimulation of PFC could relieve chronic pain[15,84,85] . Such studies, although established a causal 555 connection, did not provide a long-term solution for pain management owing to the deleterious effects of 556 broad non-specific cortex-wide stimulations. Despite a long-standing knowledge of putative PFC to 557 PAG projections in descending inhibition of pain[5] , the molecular identity of this circuit was unknown. In 558 this regard, our study revealing the L5 ET 1 as a major neuron subtype with exclusive projection to the 559 PAG, and undergoes transcriptional changes under chronic pain state is of particular relevance. While it 560 is likely that deactivation of this cluster will impair descending inhibition of pain which paves way for 561 persistent pain/sensitivity, it remains to be determined if it also contributes to the affective component of 562 pain. However, L6 CT 2 and L6 CT 3, the two other implicated clusters, project to multiple limbic 

563 regions including amygdala, NAc and hypothalamus, and their dysfunctions may elicit strong negative 

- 564 effect characteristic of chronic pain states[71,86,87] . All these remain valuable prospects for future 

565 functional studies through targeted neuronal activity manipulation using genetically engineered animal 566 models. 

567 

568 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

20 

Bhattacherjee et al. 

## 569 **Materials and methods** 

570 

571 **Mice and Surgery** 

572 All experiments were conducted in accordance with the National Institute of Health Guide for 573 Care and Use of Laboratory Animals and approved by the Institutional Animal Care and Use Committee 574 (IACUC) of Boston Children’s Hospital and Harvard Medical School. Wildtype male C57BL6 mice of 575 about 10 weeks old were used for the study. Mice were maintained at 12h light/dark cycles with food 576 and water ad libitum. For the spared nerve injury surgery, mice were anesthetized with ketamine. Hair 577 was shaved above the knee on one side (usually left) and the skin was sterilized with iodine and 578 isopropanol. The muscles were separated by blunt dissection to expose all three branches of the sciatic 579 nerve. The tibial and common peroneal branches of the nerve that run parallel were tied tightly with two 580 sutures and a piece between the two ties was transected and removed. Care was taken that the third 581 branch (sural nerve) was untouched during the whole procedure. The retracted muscles were released, 582 and the skin stitched back. In the sham surgery group, identical steps were followed to expose the nerve, 583 but no transection was performed, and skin was stitched back in position. Mice tissues were harvested 6 584 weeks after the surgery. 

585 

586 **MERFISH Encoding Probes** 

587 A library of MERFISH encoding probes for all target genes was generated as described 588 previously[29] . Briefly, a unique binary barcode was assigned to each gene based on an encoding scheme 589 with 24-bits, a minimum Hamming distance of 4 between all barcodes, and a constant Hamming weight 590 of 4. This barcoding scheme left 60 ‘blank’ barcodes unused to serve as a measure of false-positive 591 rates. For each gene, 50 to 70 30-nt-long targeting regions with limited homology to other genes and 592 narrow melting temperature and GC ranges were selected, and individual encoding probes to that gene 593 were created by concatenating two 20-nt-long readout sequences to each of these target regions. Each of 594 the 24 bits were associated with a unique readout sequences, and encoding probes for a given gene 595 contained only readout sequences for which the associated bit in the barcode assigned to that gene 596 contained a ‘1’. Template molecules to allow the production of these encoding probes were designed by 597 adding flanking PCR primers, with one primer representing the T7 promoter. This template oligopool 598 was synthesized by Twist Biosciences and enzymatically amplified to produce encoding probes using 599 published protocols[29] . 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

Bhattacherjee et al. 

21 

600 

601 **MERFISH tissue processing and imaging** 

602 Tissue was prepared for MERFISH as described previously[29] . Briefly, mice were euthanized under CO2 603 and brains were quickly harvested and rinsed with ice-cold calcium and magnesium free PBS. The 604 brains were frozen on dry ice and stored at -80[0] C till sectioning. The frozen brains were embedded in 605 OCT on a mixture of ethanol and dry ice. Serial 14-μm-thick sections of the frontal cortex spaced about 606 150 μm apart were collected and placed on poly-D lysine coated, silanized coverslips, containing orange 607 fiducial beads, prepared as described previously[29] . The sections were allowed to briefly air dry and 608 immediately fixed with 4% PFA for 10 mins. Sections were washed in PBS and stored in 70% ethanol 609 for at least 12h to permeabilize. The sections were washed in hybridization buffer (2xSSC+30% 610 formamide) and then drained and inverted over parafilm in petri dish onto a 50 μl droplet of mixture 611 containing encoding probes and a poly(A) anchor probe[29] in hybridization buffer (2xSSC, 30% 612 formamide, 0.1% yeast tRNA, 10% dextran sulfate) and hybridized in a covered humid incubator at 613 37[0] C for 2 days. Coverslips were then washed in hybridization buffer and the sections were embedded 614 into a thin film of poly-acrylamide gel, as described previously. The embedded sections were then 615 digested for 2 days in a 2xSSC buffer containing 2% SDS, 0.5% Triton X-100 and 1:100 proteinase K. 616 The coverslips were washed and stored in 2xSSC at 4[0] C until imaging.  MERFISH imaging was 617 performed on a custom microscope and flow system, as described previously[29] . In each imaging round, 618 the volume of each slice was imaged by collecting a z-stack at each field-of-view containing 10 images 619 each spaced by 1 micron. 12 imaging rounds using two readout probes per imaging round were used to 620 read out the 24-bit barcodes. Readout probes were synthesized by Biosynthesis and contained either a 621 Cy5 or Alexa750 conjugated to the oligonucleotide probe via a disulfide bond, which allowed reductive 622 cleavage to remove fluorophores after imaging, as described previously. A readout conjugated to 623 Alexa488 and complementary to a readout sequence contained on the polyA anchor probe was 624 hybridized with readouts associated with the first two bits in the first round of imaging. 

- 625 

- 626 **Image processing, decoding and cell segmentation** 

- 627 MERFISH data was decoded as previously described[29] . Briefly, images of fiducial beads 628 collected for each field-of-view in each imaging round were used to align images across imaging rounds. 629 RNAs were detected using a pixel-based approach, in which images were first high-pass filtered, 630 deconvolved, and low-pass filtered. Differences in the brightness of different imaging rounds were 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

22 

Bhattacherjee et al. 

631 corrected by an optimized set of scaling values, determined from an iterative process of decoding 632 performed on a randomly selected subset of fields-of-view, and the intensity trace for individual pixels 633 across all imaging rounds was matched to the barcode with the closest predicted trace as judged via a 634 Euclidean metric and subject to a minimum distance. Adjacent pixels matched to the same barcode were 635 aggregated to form putative RNAs. RNA molecules were then filtered based on the number of pixels 636 associated with each molecule (greater than 1) and their brightness to remove background. 

637 As described previously[29] , the identification of cell boundaries within each FOV was performed 638 by a seeded watershed approaching using DAPI images as the seeds, and the poly(A) signals to identify 639 segmentation boundaries. Following segmentation, individual RNA molecules were assigned to specific 640 cells based on localization within the segmented boundaries. 

641 

642 **Preprocessing of MERFISH data** 

643 The decoded data was preprocessed by the following steps: 1) Segmented “cells” with a cell 644 body volume less than 100 µm[3] or larger than 4000 were removed; 2) Cells with total RNA counts of 645 less than 10 or higher than 98% quantile, and cells with total RNA features less than 10, were removed; 646 3) To correct for the minor batch fluctuations in different MERFISH experiments, we normalized the 647 total RNA counts per cell to a same value (500 in this case); 4) Doublets were removed by Scrublet[88] ; 5) 648 The processed cell-by-gene matrix was transferred to gene-by-cell matrix and then loaded into Seurat 649 V4[89] for downstream analysis. The matrix was log-transformed by the Seurat standard pipeline. 

650 

651 **Cell clustering** 

652 Two rounds of cell clustering were used to identify cell types and subtypes. In the first round, we 653 identified the three major cell types: excitatory neurons, inhibitory neurons, and non-neuronal cells. In 654 the second round, each major cell type was further clustered. Excitatory neuron was further clustered 655 into 18 subtypes, inhibitory neurons was further clustered into 19 subtypes, non-neuronal cell was 656 further clustered into 15 subtypes. Then, we separated the excitatory subtypes into seven groups 657 according to the neuronal projection: L2/3 IT, L4/5 IT, L5 IT, L6 IT, L5 ET, L5/6 NP, and L6 CT. The 658 inhibitory neuron was cataloged into five groups based on the main markers: Lamp5, Pvalb, Sncg, Sst, 659 and Vip. Non-neuronal cells were cataloged into six groups: endothelial cells, microglia, 

660 oligodendrocytes, OPC, astrocytes, and VLMC. Each round of clustering following the same workflow 661 as described previously. First, all gene expression was centered and scaled via a z-score, and PCA was 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

23 

Bhattacherjee et al. 

662 applied on the scaled matrix. To determine the number of principal components (PCs) to keep, we used 663 the same method described before[29,77] . Briefly, the scaled matrix was randomly shuffled and PCA was 664 performed based on the shuffled matrix. This shuffling step was repeated 10 times and the mean 665 eigenvalue of the first principal component crossing the 10 iterations was calculated. Only the principal 666 components derived from the original matrix that had an eigenvalue greater than the mean eigenvalue 667 were kept. Harmony[90] was then used to remove apparent batch effect among different MERFISH 668 samples. The corrected PCs were used for cell clustering. The nearest neighbors for each cell were then 669 computed by a K-nearest neighbor (KNN) graph in corrected PC space. Bootstrapping was used for 670 determining the optimal k value for KNN as previously described[29,77] (k = 10 in the first round 671 clustering. k = 50, 20, 15 for excitatory neurons, inhibitory neurons, and non-neuronal cells in the 672 second round). Leiden method was used for detecting clusters[91] . The resolution was set to 0.3 in the first 673 round clustering, and to 2 for the second round. Finally, we manually removed the clusters representing 674 doublets, which express high levels of the established markers of multiple cell types. Clusters located 675 outside of the cortex were also removed. 

- 676 

- 677 **Correspondence between scRNA-seq and MERFISH clusters** 

- 678 To compare the cell clusters identified by scRNA-seq and MERFISH, we first co-embedded the 679 two datasets in a corrected PCA space using Harmony as described above. Then, all the cells from both 680 scRNA-seq and MERFISH were used to build the KNN graph. The first 30 corrected PCs were inputted 681 into Seurat::FindNeighbors to compute the KNN. For each cell cluster in MERFISH, we obtained the 682 cell cluster’s nearest 30 neighbor cells’ information. Then, we calculated the percentages of the cell 683 clusters derived from scRNA-seq that were near to this MERFISH cluster, from which we obtained a 684 correspondence matrix, where each row is a cluster from scRNA-seq, each column is a cluster from 685 MERFISH, the element in the matrix indicates the similarity between the two clusters. Similarly, for 686 each cell cluster in scRNA-seq, we inquired the nearest clusters derived from MERFISH data to 687 generate another correspondent matrix. The average of the two correspondent matrices were used to 688 indicate the similarities between the cell clusters defined by scRNA-seq and MERFISH. 

- 689 

- 690 **Cell-cell proximity** 

- 691 For each cell, we first identified the nearest 30 neighbors based on spatial distance. Next, we 692 derived the cell subtypes of these neighboring cells, and obtained the cell subtypes composition of these 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

24 

Bhattacherjee et al. 

693 cells nearby the inquired cell. After iteration of all cells in all subtypes, we could calculate the number of 694 occurrences of paired cell-cell and obtain the cell-cell proximity matrix (Observed matrix). Because of 695 the cell number differences for each subtype, we normalized cell-cell proximity matrix by a random 696 shuffled matrix (Expected matrix). To derive the shuffled matrix, we first shuffled the cell identities by 697 random assign a subtype for each cell. Then, the random cell-cell proximity matrix was calculated by the 698 same method before. Finally, the normalized cell-cell proximity matrix was calculated by log2(Observed 699 matrix/Expected matrix). In addition, the p-values were calculated by wilcoxon rank tests (using 700 wilcox.test in R) and then adjusted by Benjamini-Hochberg method (using p.adjust in R, method = 701 "BH"). 

702 

703 **Excitatory neuron projection prediction** 

704 The scRNA-seq data (GEO: GSE161936)[2] was first preprocessed by standard Seurat pipeline. 705 Only the cells from dorsomedial (dmPFC) and ventromedial (vmPFC) regions were used. We integrated 706 the MERFISH and scRNA-seq data using Harmony, and all the cells derived from MERFISH/scRNA707 seq were co-embedded on a corrected PCA space. The first corrected 30 PCs were selected as features to 708 train a multi-class support vector machine (SVM) for predicting the neuronal projection. The cells from 709 scRNA-seq were separated into training and test groups. Then, the SVM was trained on training data 710 and validated on test data by using the radial basis function kernel. Gamma was set to 0.01, cost was set 711 to 10. The receiver operating characteristic (ROC) curve was plotted to evaluate the performance using 712 pROC package in R and the area under the AUC curve (AUC) was equal to 0.913. Finally, the model 713 was applied to MERFISH cells to predict their projections. 

- 714 

- 715 **Register MERFISH slice to Allen Brain Atlas** 

- 716 To align MERFISH slices to the Allen common coordinate framework (CCF) v3 we leveraged 717 the spatial distribution of cells identified by MERFISH in each slice as well as DAPI images of that 718 slice. First, each brain slice was paired to the closest matching coronal section in CCF v3 with the help 719 of DAPI image and spatial location of the cell types. Then, we modified the WholeBrain package[92] to 720 align the MERFISH slice to the corresponding matching CCF coronal section. To assure accurate 

- 721 alignment, we leveraged the MERFISH cell typing result at single cell resolution and used certain cell 722 types as anchors to help locating the anatomic features. VLMC cells are used for marking the surface of 723 brain slice as follows: Inhibitory neuron subtype, Lamp5 3, for locating layer 1; L2/3 IT neurons for 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

25 

Bhattacherjee et al. 

- 724 locating layer 2, L6 CT neurons for locating layer 6, oligodendrocytes for locating corpus callosum. 

- 725 Since some small slices do not have sufficient features to align, 45 out of 60 slices are successfully 

- 726 registered to CCF v3, which allowed us to define the anatomic PFC and PFC subregions. 

- 727 

## 728 **Differentially expressed genes between pain and control conditions** 

- 729 To detect differentially expressed genes (DEGs) and correct the batch effects, we used a logistic 

- 730 regression framework. For each gene, we constructed a logistic regression model to predict the sample 

- 731 conditions _C_ by considering the batch information S, � ~ �+  S, and compared with a null model, 

- 732 � ~ 1 +  S, with a likelihood ratio test. Then, Bonferroni correction method was applied to adjust for 

- 733 multiple comparisons. Here, “LR” method in Seurat FindAllMarkers was used for conducting this 

- 734 analysis. 

- 735 

## 736 **Data and code availability** 

- 737 The MERFISH data generated in this study has been deposited to Brain Image Library with 

- 738 accession number: in the process of uploading. Interactive visualization of MERFISH data can be 

- 739 accessed at: https://yizhang-lab.github.io/PFC. Code for MERFISH analysis is available at 

- 740 https://github.com/YiZhang-lab/PFC-MERFISH. 

- 741 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

26 

Bhattacherjee et al. 

## 742 **Acknowledgements** 

- 743 We thank Drs. Barbara Calderone and Olga Alekseenko from the Harvard Neurobehavior Core 

- 744 for their support; Dr. Renchao Chen for critical reading of the manuscript and valuable suggestions; Drs. 

- 745 Yingying Zhang, Yuanyou Wang and Paolo Cadinu, and Ms. Rosalind Xu for help with MERFISH 

- 746 troubleshooting and pipelines. This project was supported by the National Institutes of Health 

- 747 (1R01DA042283, 1R01DA050589), the Open Philanthropy Foundation, and the HHMI. Y.Z. is an 

- 748 investigator of the Howard Hughes Medical Institute. This article is subject to HHMI’s Open Access to 

- 749 Publications policy. HHMI lab heads have previously granted a nonexclusive CC BY 4.0 license to the 750 public and a sublicensable license to HHMI in their research articles. Pursuant to those licenses, the 751 author-accepted manuscript of this article can be made freely available under a CC BY 4.0 license 752 immediately upon publication. 

- 753 

- 754 **Author Contributions** 

- 755 Y.Z. conceived the project; A.B., Y.Z., and J.R.M. designed experiments; Y.Z. and J.R.M. 756 supervised the project; A.B. performed experiments; C.Z. analyzed the data; M.N.D helped with probe 757 design; B.W. built the MERFISH microscope and trained A.B. for MERFISH experiments; A.B., C.Z., 758 Y.Z. and J.R.M. interpreted the data and wrote the manuscript. 

- 759 

- 760 **Competing Interests** 

- 761 J.R.M. is a co-founder of and consultant for Vizgen. The remaining authors declare no 

762 competing interests. 

763 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

27 

Bhattacherjee et al. 

## 764 **Figure legends** 

765 

766 **Fig. 1: MERFISH reveals the molecularly diverse cell types and subtypes comprising the PFC** . **a** , 767 UMAP visualization of all cells identified by MERFISH. Cells are colored coded by their identities. **b** , 768 Dendrogram showing the hierarchical relationship among all molecular defined cell subtypes. The 769 expression of marker genes is shown below. The color represents the average expression, and dot size 770 indicates the percentage of cells expressing each gene. **c** , Spatial map of all cell subtypes in a 771 represented coronal slice. An enlarged view of a zoom-in region is shown in the top-right. **d** , Pie charts 772 showing the cell proportions of the major cell types (left), excitatory neurons (middle) and inhibitory 773 neurons (right) in PFC. **e** , Heatmap showing the gene-expression correlation between cell types and 774 subtypes defined by MERFISH and scRNA-seq. scRNA-seq data are downloaded from Allen brain 775 atlas, and only cells from PFC are used. 

776 

777 **Fig. 2: Spatial organization of different neuron subtypes in PFC. a** , Coronal MERFISH slices 778 showing the spatial organization of neuron subtypes from anterior to posterior in PFC and adjacent 779 regions. The dotted lines indicate the PFC region. The color scheme is the same as in Fig. 1c. **b** , 780 Heatmap showing the proportions of neuron subtypes within PFC from anterior to posterior (A to P) 781 sections in excitatory (left) and inhibitory (right) neurons. **c** , Spatial organization of L4/5 IT 1 and L5 782 ET 1 from anterior to posterior sections. **d** , **e** , Violin plots showing the cortical depth distributions of 783 excitatory neuron subtypes ( **d** ) and inhibitory neuron subtypes ( **e** ) in PFC. The maximum cortical depth 784 is normalized to 1. **f** , Spatial location of five representative neuron subtypes (excitatory neuron subtypes: 785 L2/3 IT 2, L5 ET 1 L5/6 NP; and inhibitory neuron subtypes: Lamp5 3, Pvalb 3) on a coronal slice. Red 786 dots mark the indicated cell types and gray dots mark the other cells. 

- 787 

788 **Fig. 3: Distinct neuron subtypes are uniquely enriched or depleted in PFC relative to the adjacent** 789 **cortical regions. a** , UMAP of all MERFISH cells colored by their spatial location whether in or out of 790 PFC. **b** , Barplot showing the log2 of the abundance ratio of subtype neurons in or out of PFC. **c** , Spatial 791 location of excitatory neuron subtypes enriched (left), depleted (middle), and unbiased (right) 

792 distribution in PFC compare with adjacent regions. Dotted line marks PFC in the slice. **d,** Diagram of 793 anatomical subregions of PFC and adjacent cortical regions. **e** , The normalized neuron proportion of 

794 excitatory subtypes in different anatomical subregions. **f** , Spatial location of four representative 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

28 

Bhattacherjee et al. 

795 excitatory neuron subtypes on a coronal slice. Red dots represent the indicated subtypes. The dotted 796 lines indicate the anatomical subregions from Allen Brain Atlas CCF v3. 

- 797 

- 798 **Fig. 4: Genes with expression enriched or depleted in PFC. a** , Volcano plot showing the 799 differentially expressed genes (DEGs) that are enriched or depleted in PFC neurons relative to the 800 neurons out of PFC. Expression of genes enriched, depleted in PFC are colored in red, blue dots, 801 respectively. **b** , Spatial gene expression of _Nnat_ (top) and _Scn4b_ (bottom) in all excitatory neurons. 802 Dotted line marks PFC region. **c** , _In situ_ hybridization (ISH) data from Allen Brain Atlas showing the 803 spatial expression of Nnat and Scn4b in a coronal slice (right) with zoom-in (left). **d** , UMAP of all 804 MERFISH cells (bottom-left) and excitatory neurons colored by the PFC signature, which is defined as 805 the average expression of top 10 enriched genes minus the average expression of top 10 depleted genes. 806 **e** , Align the PFC signature onto a representative slice to show the spatial distribution of PFC signature. **f** 807 Volcano plot showing the expressions of genes enriched or depleted in PFC after imputing by iSpatial. 808 A total 20,733 genes are analyzed. Genes analyzed by MERFISH are colored in black, and genes 809 inferred by iSpatial are colored in yellow. **g** , The gene ontology enrichment analysis of genes that 810 enriched or depleted in PFC. **h** , Gene expression enrichment analysis of genes enriched in the different 811 anatomical subregions of PFC and the adjacent cortical regions. 

- 812 

- 813 **Fig. 5: Spatial and molecular organization of PFC excitatory subtypes projection to the major** 

- 814 **PFC targets. a** , Schematics of the strategy for inferring neuronal projection of MERFISH clusters. The 815 MERFISH and scRNA-seq data are integrated into a reduced dimensional space. A support vector 816 machine is used to predict neuronal projection of the MERFISH neuron subtypes (see methods). **b** , 817 UMAP visualization of cells derived from MERFISH and scRNA-seq data after integration. **c** , The ROC 818 curves showing the prediction powers of six projection targets. w/o represents the cells without 

- 819 projection information. **d** , A coronal slice showing _in silico_ retrograde tracing from six injection sites, 

- 820 labeled by different colors as indicated. **e** , The inferred projection targets of molecularly defined 

- 821 excitatory neuron subtypes, represented by an alluvial diagram. **f** , PFC to PAG projection validation. 

- 822 Retrograde mCherry expressing AAV was injected in PAG and brain slice of PFC was used for 

- 823 smFISH. mCherry (red) labeled neurons co-express the L5 ET1 marker _Pou3f1_ (green). All mCherry 824 positive neurons are Pou3f1-positive. 

- 825 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

29 

Bhattacherjee et al. 

## 826 

- 827 **Fig. 6: Chronic pain caused cellular and molecular changes in PFC excitatory neurons. a** , 

- 828 Overview of chronic pain sample preparation. For each MERFISH run, one brain slice from each of 

- 829 control and pain condition are loaded together to avoid batch effect. Seven paired samples from three 

- 830 paired mice were imaged. **b** , The numbers of differentially expressed genes comparing pain and control 831 samples for the indicated neuron subtypes are shown. The numbers of up-regrated and down-regulated 832 genes are colored in red and blue, respectively. **c** , Spatial distribution of cells colored by activity- 

833 regulated genes (ARG) scores in control and pain conditions. The anatomical subregions of PFC are also 834 shown. **d** , Heatmap showing ARG score in PFC subregions in pain and control samples. **e** , ARG scores 835 of PFC excitatory subtypes in pain and control samples. Paired dots represent the control-pain paired 836 samples which were imaged together. Color of the paired dots represent the paired mice ID. Two-tailed 837 paired t-test is used to calculate the p-value. **f,** Global overview of PFC in half coronal section with Fos 838 smFISH (red) in Sham (Control) and chronic pain conditions. **g,** smFISH co-labeling of Fos and Pou3f1 839 (L5 ET marker) at high magnification in Sham and chronic pain conditions. Arrowheads in merged 840 images indicate double positive neurons. **h** , Barplot showing the percentage of cFos+ cells to Pou3f1+ 841 cells. Nine random fields are surveyed. Two-tailed Mann-Whitney test is used to calculate the p-value. 

- 842 

- 843 

- 844 

- 845 

- 846 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

30 

Bhattacherjee et al. 

## 847 **Supplementary figure legends** 

- 848 

- 849 **Fig. S1: The workflow and quality control for MERFISH profiling. a** , The workflow of MERFISH 850 profiling of mouse PFC, including MERFISH imaging, decoding, segmentation and data analysis. **b** , 851 Scatterplot showing the spearman correlation of the RNA counts per cell of individual genes measured 852 by MERFISH in two independent experiments. **c** , Scatterplot of the RNA counts per cell of individual 853 genes measured by MERFISH versus bulk RNA-seq data. The counts are natural logarithms. **d** , Spatial 854 gene expression of three representative genes detected by MERFISH. _In situ_ hybridization (ISH) data 855 from Allen Brain Atlas are shown at the bottom. 

- 856 

- 857 **Fig. S2: MERFISH and scRNA-seq based clusters are consistent** . **a** , UMAP showing integration of 858 cells from MERFISH or scRNA-seq data (GSE124952). **b** , UMAP showing the cell clusters defined by 859 scRNA-seq (left) or MERFISH (right). **c** , **d** , **e** , Heatmap showing the correspondence between main cell 860 types ( **c** ), excitatory ( **d** ) and inhibitory ( **e** ) subtypes defined by MERFISH and scRNA-seq. **f** , The cell 861 proportions of the excitatory, inhibitory and non-neuronal cells from scRNA-seq or MERFISH. 

- 862 

- 863 **Fig. S3: Spatial distribution of molecularly defined excitatory neuron subtypes along the anterior** 

- 864 **to posterior axis. a** , Schematics of coronal brain slices aligned to Allen Brain Atlas CCF-v3 from 865 anterior to posterior sections. **b** , Spatial organization of the indicated representative excitatory neuron 866 subtypes across anterior to posterior sections. 

- 867 

- 868 **Fig. S4: Spatial location of all molecularly defined PFC cell types and subtypes.** 

- 869 **a** , Excitatory neuron subtypes; **b** , Inhibitory neuron subtypes; **c** , non-neuron cell types and subtypes. Red 870 dots represent the indicated cell types and subtypes. 

- 871 

- 872 **Fig. S5: Distinct neuron subtypes are uniquely enriched in PFC and PFC subregions. a,** Spatial 

- 873 location of three enriched (top panels: Pvalb 1, Pvalb 2, and Pvalb 6) and three depleted (bottom panels: 

- 874 Pvalb 3, Pvalb 4, and Sst 6) inhibitory subtypes on a coronal slice. **b** , The proportion of cell numbers 

- 875 from different PFC subregions and adjacent cortical regions of all neuron and non-neuron subtypes. 

- 876 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

31 

Bhattacherjee et al. 

- 877 **Fig. S6: Specific gene expression signatures of PFC and PFC subregions. a** , **b** , Spatial expression of 

- 878 two representative genes enriched ( **a** ) and depleted ( **b** ) in PFC relative to adjacent cortical regions. Only 879 excitatory neurons are shown. Corresponding ISH data from Allen Brain Atlas are shown on the right. 

- 880 Dotted line marks PFC region. **c** , Ingenuity pathway analysis (IPA) of the genes, identified after 

- 881 imputation, showing enriched or depleted in PFC. The red/blue bars indicate the pathway more active 

- 882 in/out PFC, respectively. **d** , Spatial gene expression of four representative genes enriched in PFC 

- 883 subregions. A diagram of anatomical subregions in PFC and adjacent regions is shown on the left. Only 884 the excitatory neurons are shown. ISH data from Allen Brain Atlas are shown on the right. Dotted line 885 marks PFC subregion. 

- 886 

- 887 **Fig. S7: Cell-Cell proximity across all cell types. a** , Enrichment of cell-cell proximity between 888 different cell types and subtypes shown in dot plot. The color represents log2 transformed observation to 889 expectation of co-localized frequency of two clusters. The size of dots indicates the significance of the 890 co-localization. **b** , The cell-cell proximity between Pvalb 1 and L5 IT 3 neurons (left), and between 891 Pvalb 6 and L5 ET 2 neurons (right). 

- 892 

- 893 **Fig. S8: Integrate MERFISH and scRNA-seq data to predict neuronal projections. a** , UMAP 

- 894 showing integration of cells from scRNA-seq (left) and MERFISH (right). The colors represent the 

- 895 projection sites in scRNA-seq data and the excitatory subtype in MERFISH data, respectively. **b** , Spatial 

- 896 location of neurons projecting to six different brain regions. **c** , Amygdala projection validation: mCherry 897 expressing retrograde AAV was injected in amygdala. Brain slice of PFC were stained with DAPI and 

- 898 mCherry to image the labeled neurons. smFISH co-labeling of mCherry with _Pou3f1_ (L5 ET marker), or 899 _Foxp2_ (L6 CT marker) reveal partial overlap with both neuron subtypes. 

- 900 

- 901 

- 902 **List of Supplemental Tables** 

- 903 

- 904 **Table S1: List of MERFISH probes** 

- 905 **Table S2: List of enriched and depleted genes in PFC compared to the adjacent cortical regions** 

- 906 **Table S3: List of genes whose expression is affected by chronic pain** 

- 907 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

32 

Bhattacherjee et al. 

## 908 **References** 

909 

- 910 1 Miller, E. K. & Cohen, J. D. An integrative theory of prefrontal cortex function. _Annu Rev Neurosci_ **24** , 911 167-202 (2001). https://doi.org:10.1146/annurev.neuro.24.1.167 

- 912 2 Lui, J. H. _et al._ Differential encoding in prefrontal cortex projection neuron classes across cognitive tasks. 913 _Cell_ **184** , 489-506 e426 (2021). https://doi.org:10.1016/j.cell.2020.11.046 

- 914 3 Gamo, N. J. & Arnsten, A. F. Molecular modulation of prefrontal cortex: rational development of 915 treatments for psychiatric disorders. _Behav Neurosci_ **125** , 282-296 (2011). 916 https://doi.org:10.1037/a0023165 

- 917 4 Chini, M. & Hanganu-Opatz, I. L. Prefrontal Cortex Development in Health and Disease: Lessons from 918 Rodents and Humans. _Trends Neurosci_ **44** , 227-240 (2021). https://doi.org:10.1016/j.tins.2020.10.017 

- 919 5 Tan, L. L. & Kuner, R. Neocortical circuits in pain and pain relief. _Nat Rev Neurosci_ **22** , 458-471 (2021). 920 https://doi.org:10.1038/s41583-021-00468-2 

- 921 6 Bushnell, M. C., Ceko, M. & Low, L. A. Cognitive and emotional control of pain and its disruption in 922 chronic pain. _Nat Rev Neurosci_ **14** , 502-511 (2013). https://doi.org:10.1038/nrn3516 

- 923 7 Yong, R. J., Mullins, P. M. & Bhattacharyya, N. Prevalence of chronic pain among adults in the United 924 States. _Pain_ **163** , e328-e332 (2022). https://doi.org:10.1097/j.pain.0000000000002291 

- 925 8 Gaskin, D. J. & Richard, P. The economic costs of pain in the United States. _J Pain_ **13** , 715-724 (2012). 926 https://doi.org:10.1016/j.jpain.2012.03.009 

- 927 9 Zhou, H. _et al._ A novel neuromodulation strategy to enhance the prefrontal control to treat pain. _Mol_ 928 _Pain_ **15** , 1744806919845739 (2019). https://doi.org:10.1177/1744806919845739 

- 929 10 Deer, T. R. _et al._ The appropriate use of neurostimulation: new and evolving neurostimulation therapies 930 and applicable treatment for chronic pain and selected disease states. Neuromodulation 931 Appropriateness Consensus Committee. _Neuromodulation_ **17** , 599-615; discussion 615 (2014). 932 https://doi.org:10.1111/ner.12204 

- 933 11 Baliki, M. N., Geha, P. Y., Apkarian, A. V. & Chialvo, D. R. Beyond feeling: chronic pain hurts the brain, 934 disrupting the default-mode network dynamics. _J Neurosci_ **28** , 1398-1403 (2008). 935 https://doi.org:10.1523/JNEUROSCI.4123-07.2008 

- 936 12 Davis, K. D. & Moayedi, M. Central mechanisms of pain revealed through functional and structural MRI. _J_ 937 _Neuroimmune Pharmacol_ **8** , 518-534 (2013). https://doi.org:10.1007/s11481-012-9386-8 

- 938 13 Nardone, R. _et al._ rTMS of the prefrontal cortex has analgesic effects on neuropathic pain in subjects 939 with spinal cord injury. _Spinal Cord_ **55** , 20-25 (2017). https://doi.org:10.1038/sc.2016.87 

- 940 14 Jefferson, T., Kelly, C. J. & Martina, M. Differential Rearrangement of Excitatory Inputs to the Medial 941 Prefrontal Cortex in Chronic Pain Models. _Front Neural Circuits_ **15** , 791043 (2021). 942 https://doi.org:10.3389/fncir.2021.791043 

- 943 15 Li, C. _et al._ Prolonged Continuous Theta Burst Stimulation Can Regulate Sensitivity on Abeta Fibers: An 944 Functional Near-Infrared Spectroscopy Study. _Front Mol Neurosci_ **15** , 887426 (2022). 945 https://doi.org:10.3389/fnmol.2022.887426 

- 946 16 Ong, W. Y., Stohler, C. S. & Herr, D. R. Role of the Prefrontal Cortex in Pain Processing. _Mol Neurobiol_ **56** , 947 1137-1166 (2019). https://doi.org:10.1007/s12035-018-1130-9 

- 948 17 Ossipov, M. H., Morimura, K. & Porreca, F. Descending pain modulation and chronification of pain. _Curr_ 949 _Opin Support Palliat Care_ **8** , 143-151 (2014). https://doi.org:10.1097/SPC.0000000000000055 

- 950 18 Anastasiades, P. G. & Carter, A. G. Circuit organization of the rodent medial prefrontal cortex. _Trends_ 951 _Neurosci_ **44** , 550-563 (2021). https://doi.org:10.1016/j.tins.2021.03.006 

- 952 19 Bhattacherjee, A. _et al._ Cell type-specific transcriptional programs in mouse prefrontal cortex during 953 adolescence and addiction. _Nat Commun_ **10** , 4169 (2019). https://doi.org:10.1038/s41467-019-12054-3 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

33 

Bhattacherjee et al. 

- 954 20 Zeng, H. & Sanes, J. R. Neuronal cell-type classification: challenges, opportunities and the path forward. 955 _Nat Rev Neurosci_ **18** , 530-546 (2017). https://doi.org:10.1038/nrn.2017.85 

- 956 21 Network, B. I. C. C. A multimodal cell census and atlas of the mammalian primary motor cortex. _Nature_ 957 **598** , 86-102 (2021). https://doi.org:10.1038/s41586-021-03950-0 

- 958 22 Radnikow, G. & Feldmeyer, D. Layer- and Cell Type-Specific Modulation of Excitatory Neuronal Activity in 959 the Neocortex. _Front Neuroanat_ **12** , 1 (2018). https://doi.org:10.3389/fnana.2018.00001 

- 960 23 Tasic, B. _et al._ Shared and distinct transcriptomic cell types across neocortical areas. _Nature_ **563** , 72-78 961 (2018). https://doi.org:10.1038/s41586-018-0654-5 

- 962 24 Loo, L. _et al._ Single-cell transcriptomic analysis of mouse neocortical development. _Nat Commun_ **10** , 134 963 (2019). https://doi.org:10.1038/s41467-018-08079-9 

- 964 25 Li, Y. E. _et al._ An atlas of gene regulatory elements in adult mouse cerebrum. _Nature_ **598** , 129-136 965 (2021). https://doi.org:10.1038/s41586-021-03604-1 

- 966 26 Chen, K. H., Boettiger, A. N., Moffitt, J. R., Wang, S. & Zhuang, X. RNA imaging. Spatially resolved, highly 967 multiplexed RNA profiling in single cells. _Science_ **348** , aaa6090 (2015). 968 https://doi.org:10.1126/science.aaa6090 

- 969 27 Xia, C., Fan, J., Emanuel, G., Hao, J. & Zhuang, X. Spatial transcriptome profiling by MERFISH reveals 970 subcellular RNA compartmentalization and cell cycle-dependent gene expression. _Proc Natl Acad Sci U S_ 971 _A_ **116** , 19490-19499 (2019). https://doi.org:10.1073/pnas.1912459116 

- 972 28 Moffitt, J. R. & Zhuang, X. RNA Imaging with Multiplexed Error-Robust Fluorescence In Situ Hybridization 973 (MERFISH). _Methods Enzymol_ **572** , 1-49 (2016). https://doi.org:10.1016/bs.mie.2016.03.020 

- 974 29 Moffitt, J. R. _et al._ Molecular, spatial, and functional single-cell profiling of the hypothalamic preoptic 975 region. _Science_ **362** (2018). https://doi.org:10.1126/science.aau5324 

- 976 30 Wang, Q. _et al._ The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas. _Cell_ **181** , 977 936-953 e920 (2020). https://doi.org:10.1016/j.cell.2020.04.007 

- 978 31 Oishi, K. _et al._ Identity of neocortical layer 4 neurons is specified through correct positioning into the 979 cortex. _Elife_ **5** (2016). https://doi.org:10.7554/eLife.10907 

- 980 32 Zhang, M. _et al._ Spatially resolved cell atlas of the mouse primary motor cortex by MERFISH. _Nature_ **598** , 981 137-143 (2021). https://doi.org:10.1038/s41586-021-03705-x 

- 982 33 Isaacson, J. S. & Scanziani, M. How inhibition shapes cortical activity. _Neuron_ **72** , 231-243 (2011). 983 https://doi.org:10.1016/j.neuron.2011.09.027 

- 984 34 Jang, H. J. _et al._ Distinct roles of parvalbumin and somatostatin interneurons in gating the 985 synchronization of spike times in the neocortex. _Sci Adv_ **6** , eaay5333 (2020). 986 https://doi.org:10.1126/sciadv.aay5333 

- 987 35 Brown, J. A. _et al._ Inhibition of parvalbumin-expressing interneurons results in complex behavioral 988 changes. _Mol Psychiatry_ **20** , 1499-1507 (2015). https://doi.org:10.1038/mp.2014.192 

- 989 36 Santini, E., Quirk, G. J. & Porter, J. T. Fear conditioning and extinction differentially modify the intrinsic 990 excitability of infralimbic neurons. _J Neurosci_ **28** , 4028-4036 (2008). 991 https://doi.org:10.1523/JNEUROSCI.2623-07.2008 

- 992 37 Otis, J. M. _et al._ Prefrontal cortex output circuits guide reward seeking through divergent cue encoding. 993 _Nature_ **543** , 103-107 (2017). https://doi.org:10.1038/nature21376 

- 994 38 Spring, M. G., Soni, K. R., Wheeler, D. S. & Wheeler, R. A. Prelimbic prefrontal cortical encoding of 995 reward predictive cues. _Synapse_ **75** , e22202 (2021). https://doi.org:10.1002/syn.22202 

- 996 39 Harada, M., Pascoli, V., Hiver, A., Flakowski, J. & Luscher, C. Corticostriatal Activity Driving Compulsive 997 Reward Seeking. _Biol Psychiatry_ **90** , 808-818 (2021). https://doi.org:10.1016/j.biopsych.2021.08.018 

- 998 40 Humphries, E. S. & Dart, C. Neuronal and Cardiovascular Potassium Channels as Therapeutic Drug 999 Targets: Promise and Pitfalls. _J Biomol Screen_ **20** , 1055-1073 (2015). 

- 1000 https://doi.org:10.1177/1087057115601677 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

34 

Bhattacherjee et al. 

- 1001 41 Gonzalez Sabater, V., Rigby, M. & Burrone, J. Voltage-Gated Potassium Channels Ensure Action Potential 1002 Shape Fidelity in Distal Axons. _J Neurosci_ **41** , 5372-5385 (2021). 1003 https://doi.org:10.1523/JNEUROSCI.2765-20.2021 

- 1004 42 Lai, H. C. & Jan, L. Y. The distribution and targeting of neuronal voltage-gated ion channels. _Nat Rev_ 1005 _Neurosci_ **7** , 548-562 (2006). https://doi.org:10.1038/nrn1938 

- 1006 43 Grube, S. _et al._ A CAG repeat polymorphism of KCNN3 predicts SK3 channel function and cognitive 1007 performance in schizophrenia. _EMBO Mol Med_ **3** , 309-319 (2011). 1008 https://doi.org:10.1002/emmm.201100135 

- 1009 44 Andrade, A. _et al._ Genetic Associations between Voltage-Gated Calcium Channels and Psychiatric 1010 Disorders. _Int J Mol Sci_ **20** (2019). https://doi.org:10.3390/ijms20143537 

- 1011 45 Eckle, V. S. _et al._ Mechanisms by which a CACNA1H mutation in epilepsy patients increases seizure 1012 susceptibility. _J Physiol_ **592** , 795-809 (2014). https://doi.org:10.1113/jphysiol.2013.264176 

- 1013 46 Carvill, G. L. Calcium Channel Dysfunction in Epilepsy: Gain of CACNA1E. _Epilepsy Curr_ **19** , 199-201 1014 (2019). https://doi.org:10.1177/1535759719845324 

- 1015 47 Splawski, I. _et al._ CACNA1H mutations in autism spectrum disorders. _J Biol Chem_ **281** , 22085-22091 1016 (2006). https://doi.org:10.1074/jbc.M603316200 

- 1017 48 Zhang, J. & Abdullah, J. M. The role of GluA1 in central nervous system disorders. _Rev Neurosci_ **24** , 4991018 505 (2013). https://doi.org:10.1515/revneuro-2013-0021 

- 1019 49 Qu, W. _et al._ Emerging role of AMPA receptor subunit GluA1 in synaptic plasticity: Implications for 1020 Alzheimer's disease. _Cell Prolif_ **54** , e12959 (2021). https://doi.org:10.1111/cpr.12959 

- 1021 50 Forrest, M. P., Parnell, E. & Penzes, P. Dendritic structural plasticity and neuropsychiatric disease. _Nat_ 1022 _Rev Neurosci_ **19** , 215-234 (2018). https://doi.org:10.1038/nrn.2018.16 

- 1023 51 Peng, S. X. _et al._ SNP rs10420324 in the AMPA receptor auxiliary subunit TARP gamma-8 regulates the 1024 susceptibility to antisocial personality disorder. _Sci Rep_ **11** , 11997 (2021). 1025 https://doi.org:10.1038/s41598-021-91415-9 

- 1026 52 Festa, L. K. _et al._ CXCL12-induced rescue of cortical dendritic spines and cognitive flexibility. _Elife_ **9** 1027 (2020). https://doi.org:10.7554/eLife.49717 

- 1028 53 Wu, P. R., Cho, K. K. A., Vogt, D., Sohal, V. S. & Rubenstein, J. L. R. The Cytokine CXCL12 Promotes Basket 1029 Interneuron Inhibitory Synapses in the Medial Prefrontal Cortex. _Cereb Cortex_ **27** , 4303-4313 (2017). 1030 https://doi.org:10.1093/cercor/bhw230 

- 1031 54 Sanfilippo, C., Castrogiovanni, P., Imbesi, R., Nunnari, G. & Di Rosa, M. Postsynaptic damage and 1032 microglial activation in AD patients could be linked CXCR4/CXCL12 expression levels. _Brain Res_ **1749** , 1033 147127 (2020). https://doi.org:10.1016/j.brainres.2020.147127 

- 1034 55 Zhang, C., Chen, R. & Zhang, Y. Accurate inference of genome-wide spatial expression with iSpatial. _Sci_ 1035 _Adv_ **8** , eabq0990 (2022). https://doi.org:10.1126/sciadv.abq0990 

- 1036 56 Kurowski, P., Grzelka, K. & Szulczyk, P. Ionic Mechanism Underlying Rebound Depolarization in Medial 1037 Prefrontal Cortex Pyramidal Neurons. _Front Cell Neurosci_ **12** , 93 (2018). 1038 https://doi.org:10.3389/fncel.2018.00093 

- 1039 57 Selleck, R. A. _et al._ Endogenous Opioid Signaling in the Medial Prefrontal Cortex is Required for the 1040 Expression of Hunger-Induced Impulsive Action. _Neuropsychopharmacology_ **40** , 2464-2474 (2015). 1041 https://doi.org:10.1038/npp.2015.97 

- 1042 58 Baldo, B. A. Prefrontal Cortical Opioids and Dysregulated Motivation: A Network Hypothesis. _Trends_ 1043 _Neurosci_ **39** , 366-377 (2016). https://doi.org:10.1016/j.tins.2016.03.004 1044 59 Tan, H., Ahmad, T., Loureiro, M., Zunder, J. & Laviolette, S. R. The role of cannabinoid transmission in 1045 emotional memory formation: implications for addiction and schizophrenia. _Front Psychiatry_ **5** , 73 1046 (2014). https://doi.org:10.3389/fpsyt.2014.00073 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

Bhattacherjee et al. 

35 

- 1047 60 Egerton, A., Allison, C., Brett, R. R. & Pratt, J. A. Cannabinoids and prefrontal cortical function: insights 1048 from preclinical studies. _Neurosci Biobehav Rev_ **30** , 680-695 (2006). 1049 https://doi.org:10.1016/j.neubiorev.2005.12.002 

- 1050 61 Peron, S. _et al._ Recurrent interactions in local cortical circuits. _Nature_ **579** , 256-259 (2020). 1051 https://doi.org:10.1038/s41586-020-2062-x 

- 1052 62 LaBerge, D. & Kasevich, R. S. Neuroelectric Tuning of Cortical Oscillations by Apical Dendrites in Loop 1053 Circuits. _Front Syst Neurosci_ **11** , 37 (2017). https://doi.org:10.3389/fnsys.2017.00037 

- 1054 63 Lacefield, C. O., Pnevmatikakis, E. A., Paninski, L. & Bruno, R. M. Reinforcement Learning Recruits 1055 Somata and Apical Dendrites across Layers of Primary Sensory Cortex. _Cell Rep_ **26** , 2000-2008 e2002 1056 (2019). https://doi.org:10.1016/j.celrep.2019.01.093 

- 1057 64 Karimi, A., Odenthal, J., Drawitsch, F., Boergens, K. M. & Helmstaedter, M. Cell-type specific innervation 1058 of cortical pyramidal cells at their apical dendrites. _Elife_ **9** (2020). https://doi.org:10.7554/eLife.46876 

- 1059 65 Harris, K. D. & Shepherd, G. M. The neocortical circuit: themes and variations. _Nat Neurosci_ **18** , 170-181 1060 (2015). https://doi.org:10.1038/nn.3917 

- 1061 66 Wamsley, B. & Fishell, G. Genetic and activity-dependent mechanisms underlying interneuron diversity. 1062 _Nat Rev Neurosci_ **18** , 299-309 (2017). https://doi.org:10.1038/nrn.2017.30 

- 1063 67 Gabbott, P. L., Warner, T. A., Jays, P. R., Salway, P. & Busby, S. J. Prefrontal cortex in the rat: projections 1064 to subcortical autonomic, motor, and limbic centers. _J Comp Neurol_ **492** , 145-177 (2005). 1065 https://doi.org:10.1002/cne.20738 

- 1066 68 Zingg, B. _et al._ Neural networks of the mouse neocortex. _Cell_ **156** , 1096-1111 (2014). 1067 https://doi.org:10.1016/j.cell.2014.02.023 

- 1068 69 Baxter, M. G. & Croxson, P. L. Facing the role of the amygdala in emotional information processing. _Proc_ 1069 _Natl Acad Sci U S A_ **109** , 21180-21181 (2012). https://doi.org:10.1073/pnas.1219167110 

- 1070 70 Bonnet, L. _et al._ The role of the amygdala in the perception of positive emotions: an "intensity detector". 1071 _Front Behav Neurosci_ **9** , 178 (2015). https://doi.org:10.3389/fnbeh.2015.00178 

- 1072 71 Corder, G. _et al._ An amygdalar neural ensemble that encodes the unpleasantness of pain. _Science_ **363** , 1073 276-281 (2019). https://doi.org:10.1126/science.aap8586 

- 1074 72 Topham, L. _et al._ The transition from acute to chronic pain: dynamic epigenetic reprogramming of the 1075 mouse prefrontal cortex up to 1 year after nerve injury. _Pain_ **161** , 2394-2409 (2020). 1076 https://doi.org:10.1097/j.pain.0000000000001917 

- 1077 73 Descalzi, G. _et al._ Neuropathic pain promotes adaptive changes in gene expression in brain networks 1078 involved in stress and depression. _Sci Signal_ **10** (2017). https://doi.org:10.1126/scisignal.aaj1549 

- 1079 74 Richner, M., Bjerrum, O. J., Nykjaer, A. & Vaegter, C. B. The spared nerve injury (SNI) model of induced 1080 mechanical allodynia in mice. _J Vis Exp_ (2011). https://doi.org:10.3791/3092 

- 1081 75 Denk, F., McMahon, S. B. & Tracey, I. Pain vulnerability: a neurobiological perspective. _Nat Neurosci_ **17** , 1082 192-200 (2014). https://doi.org:10.1038/nn.3628 

- 1083 76 Moffitt, J. R., Lundberg, E. & Heyn, H. The emerging landscape of spatial profiling technologies. _Nat Rev_ 1084 _Genet_ **23** , 741-759 (2022). https://doi.org:10.1038/s41576-022-00515-3 1085 77 Chen, R. _et al._ Decoding molecular and cellular heterogeneity of mouse nucleus accumbens. _Nat_ 1086 _Neurosci_ **24** , 1757-1771 (2021). https://doi.org:10.1038/s41593-021-00938-x 

- 1087 78 Collins, D. P., Anastasiades, P. G., Marlin, J. J. & Carter, A. G. Reciprocal Circuits Linking the Prefrontal 1088 Cortex with Dorsal and Ventral Thalamic Nuclei. _Neuron_ **98** , 366-379 e364 (2018). 1089 https://doi.org:10.1016/j.neuron.2018.03.024 

- 1090 79 Song, C. & Moyer, J. R., Jr. Layer- and subregion-specific differences in the neurophysiological properties 1091 of rat medial prefrontal cortex pyramidal neurons. _J Neurophysiol_ **119** , 177-191 (2018). 1092 https://doi.org:10.1152/jn.00146.2017 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

36 

Bhattacherjee et al. 

- 1093 80 Lodge, D. J., Behrens, M. M. & Grace, A. A. A loss of parvalbumin-containing interneurons is associated 1094 with diminished oscillatory activity in an animal model of schizophrenia. _J Neurosci_ **29** , 2344-2354 1095 (2009). https://doi.org:10.1523/JNEUROSCI.5419-08.2009 

- 1096 81 Zhang, Z. _et al._ Role of Prelimbic GABAergic Circuits in Sensory and Emotional Aspects of Neuropathic 1097 Pain. _Cell Rep_ **12** , 752-759 (2015). https://doi.org:10.1016/j.celrep.2015.07.001 

- 1098 82 Gallego-Carracedo, C., Perich, M. G., Chowdhury, R. H., Miller, L. E. & Gallego, J. A. Local field potentials 1099 reflect cortical population dynamics in a region-specific and frequency-dependent manner. _Elife_ **11** 1100 (2022). https://doi.org:10.7554/eLife.73155 

- 1101 83 Herreras, O. Local Field Potentials: Myths and Misunderstandings. _Front Neural Circuits_ **10** , 101 (2016). 1102 https://doi.org:10.3389/fncir.2016.00101 

- 1103 84 Liu, Y. _et al._ Frequency Dependent Electrical Stimulation of PFC and ACC for Acute Pain Treatment in 1104 Rats. _Front Pain Res (Lausanne)_ **2** , 728045 (2021). https://doi.org:10.3389/fpain.2021.728045 

- 1105 85 Dale, J. _et al._ Scaling Up Cortical Control Inhibits Pain. _Cell Rep_ **23** , 1301-1313 (2018). 1106 https://doi.org:10.1016/j.celrep.2018.03.139 

- 1107 86 Baliki, M. N., Geha, P. Y., Fields, H. L. & Apkarian, A. V. Predicting value of pain and analgesia: nucleus 1108 accumbens response to noxious stimuli changes in the presence of chronic pain. _Neuron_ **66** , 149-160 1109 (2010). https://doi.org:10.1016/j.neuron.2010.03.002 

- 1110 87 Generaal, E. _et al._ Reduced hypothalamic-pituitary-adrenal axis activity in chronic multi-site 

- 1111 musculoskeletal pain: partly masked by depressive and anxiety disorders. _BMC Musculoskelet Disord_ **15** , 1112 227 (2014). https://doi.org:10.1186/1471-2474-15-227 

- 1113 88 Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: Computational Identification of Cell Doublets in Single1114 Cell Transcriptomic Data. _Cell Syst_ **8** , 281-291 e289 (2019). https://doi.org:10.1016/j.cels.2018.11.005 

- 1115 89 Hao, Y. _et al._ Integrated analysis of multimodal single-cell data. _Cell_ **184** , 3573-3587 e3529 (2021). 1116 https://doi.org:10.1016/j.cell.2021.04.048 

- 1117 90 Korsunsky, I. _et al._ Fast, sensitive and accurate integration of single-cell data with Harmony. _Nat_ 1118 _Methods_ **16** , 1289-1296 (2019). https://doi.org:10.1038/s41592-019-0619-0 

- 1119 91 Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden: guaranteeing well-connected 1120 communities. _Sci Rep_ **9** , 5233 (2019). https://doi.org:10.1038/s41598-019-41695-z 

- 1121 92 Furth, D. _et al._ An interactive framework for whole-brain maps at cellular resolution. _Nat Neurosci_ **21** , 1122 139-149 (2018). https://doi.org:10.1038/s41593-017-0027-7 

- 1123 

- 1124 

- 1125 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.29.522242; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

