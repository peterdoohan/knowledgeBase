PERSPECTIVE published: 21 August 2020 doi: 10.3389/fnsys.2020.00064 

**==> picture [28 x 29] intentionally omitted <==**

# Dissecting Brainstem Locomotor Circuits: Converging Evidence for Cuneiform Nucleus Stimulation 

_Stephano J. Chang[1,2,3] , Iahn Cajigas[2,4] , Ioan Opris[2] , James D. Guest[1,2,4] and Brian R. Noga[1,2,4] *_ 

_1Neuroscience Graduate Program, University of Miami Miller School of Medicine, Miami, FL, United States, 2The Miami Project to Cure Paralysis, University of Miami Miller School of Medicine, Miami, FL, United States,[3] Division of Neurosurgery, Department of Surgery, University of British Columbia, Vancouver, BC, Canada,[4] Department of Neurological Surgery, University of Miami Miller School of Medicine, Miami, FL, United States_ 

There are a pressing and unmet need for effective therapies for freezing of gait (FOG) and other neurological gait disorders. Deep brain stimulation (DBS) of a midbrain target known as the pedunculopontine nucleus (PPN) was proposed as a potential treatment based on its postulated involvement in locomotor control as part of the mesencephalic locomotor region (MLR). However, DBS trials fell short of expectations, leading many clinicians to abandon this strategy. Here, we discuss the potential reasons for this failure and review recent clinical data along with preclinical optogenetics evidence to argue that another nearby nucleus, the cuneiform nucleus (CnF), may be a superior target. 

Keywords: mesencephalic locomotor region, deep brain stimulation, gait dysfunction, cuneiform nucleus, pedunculopontine nucleus 

_Edited by: Natalie M. Zahr, Stanford University, United States_ 

_Reviewed by:_ 

_Yue Dai,_ 

_East China Normal University, China Jeffrey B. Eells, The Brody School of Medicine at East Carolina University, United States_ 

_*Correspondence: Brian R. Noga bnoga@miami.edu_ 

_Received: 17 June 2020 Accepted: 03 August 2020 Published: 21 August 2020_ 

_Citation:_ 

_Chang SJ, Cajigas I, Opris I, Guest JD and Noga BR (2020) Dissecting Brainstem Locomotor Circuits: Converging Evidence for Cuneiform Nucleus_ 

_Stimulation._ 

_Front. Syst. Neurosci. 14:64. doi: 10.3389/fnsys.2020.00064_ 

## INTRODUCTION 

Gait disturbances present in many neurological diseases and injuries, including Parkinson’s disease (PD), stroke, and spinal cord injuries. Neurological gait disorders are particularly common in older adults, with a prevalence of more than 20% after the age of 60 (Mahlknecht et al., 2013), and are likely to represent an increasing societal health burden as demographic shifts continue. These impairments lead to immobility and falls, and contribute to social isolation, reduced quality of life, and loss of independence (Mahlknecht et al., 2013). Few treatment options exist, making research in this field imperative. In this Perspective article, we review the preclinical developments that led to clinical trials for deep brain stimulation (DBS) of the pedunculopontine nucleus (PPN), discuss potential reasons why these trials have not been successful, and present new research supporting our view that the nearby cuneiform nucleus (CnF) may be a more efficacious target. 

## THE MESENCEPHALIC LOCOMOTOR REGION 

The mesencephalic locomotor region (MLR) is a physiologically defined midbrain area, where low-threshold electrical stimulation initiates locomotion in decerebrate and intact animals (Shik et al., 1966; Mori et al., 1989). First described in cats in 1966, the MLR has since been identified as a conserved regulatory node within the supraspinal locomotor network in multiple vertebrate 

**Abbreviations:** CnF, cuneiform nucleus; DBS, deep brain stimulation; FOG, freezing of gait; MLR, mesencephalic locomotor region; NHP, non-human primate; PAG, periaqueductal gray; PD, Parkinson’s disease; PPN, pedunculopontine nucleus; PSP, progressive supranuclear palsy. 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

1 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

species (Eidelberg et al., 1981; Skinner and Garcia-Rill, 1984; Cabelguen et al., 2003; Ryczko and Dubuc, 2013), with electrophysiological and functional imaging evidence supporting its existence in humans (Jahn et al., 2008; Piallat et al., 2009). Anatomically, the MLR occupies the upper brainstem tegmentum, where it is hypothesized to integrate numerous sensorimotor, cognitive, and limbic inputs to regulate locomotion both directly, through descending reticulospinal and monoaminergic pathways to spinal locomotor networks (Noga et al., 2003, 2017b; Ryczko and Dubuc, 2013), and indirectly, through ascending connections to numerous higher brain centers ( **Figure 1A** ; Martinez-Gonzalez et al., 2011; Kroeger et al., 2017; Sébille et al., 2017). These diffuse projections also allow the MLR to regulate attention, arousal, and cortical state and couple them to locomotor states (Lee et al., 2014). 

Historically, two adjacent nuclei have been put forth as putative neuroanatomical correlates of the MLR. Much of the preclinical literature, including Shik et al.’s original description (Shik et al., 1966), has supported the more dorsally located CnF, where electrical mapping studies consistently show it to promote locomotion ( **Figure 1B** ; Takakusaki et al., 2016; Opris et al., 2019). Conversely, others have favored the more ventral, cholinergic cell-containing PPN (Garcia-Rill et al., 1987), despite its more varied electrical mapping results ( **Figure 1B** ; Takakusaki et al., 2016). 

Notwithstanding this controversy, two other converging narratives at the turn of the century ultimately led clinicianscientists to conduct non-human primate (NHP) PPN experiments: first, the discovery that dense inhibitory outputs from the globus pallidus interna terminated near the PPN generated the hypothesis that hyperactivity of the globus pallidus interna in PD could produce akinesia through excessive inhibition of the PPN (Aziz et al., 1998); and second, histopathological observations of the PPN in PD and progressive supranuclear palsy (PSP) patients showed significant cholinergic neuronal degeneration, suggesting a pathophysiological link to the dopamine-resistant postural instability and freezing of gait (FOG) commonly observed in these patients (Hirsch et al., 1987; Jellinger, 1988). Early NHP studies creating PPN area lesions did demonstrate significant akinesia (Aziz et al., 1998; Jenkinson et al., 2004), but received criticism for producing large lesions that may have encompassed surrounding structures (Winn, 2008). In response to these criticisms, Karachi et al. (2010) created cholinergic cell-specific lesions within the PPN of macaques that produced gait and balance abnormalities. While this seemed to provide evidence that cholinergic PPN neurons were critical for gait and posture, the urotensin II-conjugated toxin used in their study has only been shown to have selective effects on cholinergic cells of the PPN in rodents. The Supplemental data in Karachi et al.’s study demonstrates that the injected toxin also significantly destroyed noncholinergic cells in the region, preventing them from ruling out the possibility that the observed gait and balance abnormalities may have been due to other cell populations, such as glutamatergic neurons (Karachi et al., 2010). 

Despite these and other potential concerns, including one NHP study showing worsening of akinesia and tremor with PPN 

stimulation (Nandi et al., 2002), DBS studies moved forward in patients with PD and PSP, and have focused solely on the PPN (Mazzone et al., 2005; Stefani et al., 2007; Ferraye et al., 2010; Moro et al., 2010; Doshi et al., 2015; Mestre et al., 2016). While these studies have documented the general safety of targeting this brainstem region for DBS, suboptimal targeting of the MLR has been proposed as a possible explanation for the mixed outcomes and muted efficacy of these DBS studies compared to earlier preclinical studies (Thevathasan et al., 2018). In the sections that follow, we further explore this hypothesis through an appraisal of the most current literature investigating the functional organization of the MLR. Furthermore, we propose that these studies support our perspective that glutamatergic neurons within the CnF likely represent the neuroanatomic basis for the MLR. 

## NEUROCHEMICAL SEGREGATION OF FUNCTIONS WITHIN THE MLR 

At least three neurochemical populations are found in the MLR, with glutamatergic and GABAergic neurons dispersed throughout the CnF and PPN, while cholinergic neurons have traditionally delineated the PPN ( **Figure 1D** ; Martinez-Gonzalez et al., 2012; Roseberry et al., 2016; Sebille et al., 2019). As cholinergic neurons were its most obvious immunohistochemical feature, the PPN was long considered a primarily cholinergic nucleus, with some attributing cholinergic neurons central importance in locomotor control (Ryczko and Dubuc, 2013). Stereological estimates in the rat PPN have since shown that cholinergic neurons number the fewest of the three neuronal subtypes (25%), with glutamatergic neurons being the most abundant (43%), followed by GABAergic neurons (32%; Luquin et al., 2018). Topographically, glutamatergic and cholinergic populations are concentrated caudally in the rat PPN, while GABAergic neurons are concentrated rostrally (MenaSegovia et al., 2009; Luquin et al., 2018). Similar topographical descriptions of populations in the CnF are lacking. 

These neurochemical populations have also been characterized in the human MLR (Pienaar et al., 2013; Sebille et al., 2019). Interestingly, while the rostrocaudal distribution of GABAergic neurons was found to be similar between humans and rats, cholinergic neurons demonstrated a reverse topography, suggesting species differences (Sebille et al., 2019). Mapping the distribution of glutamatergic neurons in the human MLR remains an important goal to complete this dataset and could have implications for DBS targeting. Notably, whereas earlier studies highlighted the loss of cholinergic neurons within the PPN in PD or PSP patients as evidence of their involvement in dopamine-resistant signs such as FOG (Hirsch et al., 1987; Jellinger, 1988; Zweig et al., 1989), newer studies reveal that noncholinergic neurons in both the PPN and CnF also show significant degeneration in PD and PSP (Pienaar et al., 2013; Sebille et al., 2019). 

Optogenetic studies in mice provide further insights into the functions of these neurochemical populations. Roseberry et al. (2016) demonstrated that photoactivation of glutamatergic neurons in the mouse MLR initiates and controls the speed of 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

2 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

**==> picture [395 x 244] intentionally omitted <==**

FIGURE 1 | Anatomical, neurochemical, and connectome-based characterizations of the mesencephalic locomotor region (MLR). Schematic summaries of (A) major inputs and outputs of the CnF and PPN in rodents, (B) anatomical electrical mapping of the MLR in cats from Takakusaki et al. (2016), (C) CnF and PPN vGlut2+ photostimulation results from Josset et al. (2018) and (D) cell-type-specific functional characterizations of the CnF and PPN reported in the literature. Abbreviations: ChAT, choline acetyltransferase; CnF, cuneiform nucleus; IC, inferior colliculus; PAG, periaqueductal gray; PPN, pedunculopontine nucleus; SC, superior colliculus; SCP, superior cerebellar peduncle; vGAT, vesicular GABA transporter; vGlut2, vesicular glutamate transporter 2. *Denotes behavioral effects elicited from subsets of a neurochemical population projecting to specific targets. 

locomotion, while photoinhibition of these neurons in running animals arrests them. Photoactivation of GABAergic neurons in the MLR also stopped locomotion, at least in part through local inhibitory mechanisms (Roseberry et al., 2016). Three separate studies have shown that photoactivation of cholinergic neurons in the PPN is unable to initiate locomotion, though it may modulate speed in ongoing locomotion (Roseberry et al., 2016; Caggiano et al., 2018; Josset et al., 2018). Altogether, these studies dispute the long-debated view that cholinergic PPN neurons play a primary role in the initiation and control of locomotion, implicating glutamatergic neurons instead (Noga et al., 2017a; Albin et al., 2018). 

## ANATOMICAL SEGREGATION OF GLUTAMATERGIC MLR FUNCTION 

Two recent studies compared the function of glutamatergic neurons in the CnF and the PPN (Caggiano et al., 2018; Josset et al., 2018), while others have characterized the function of glutamatergic PPN neurons (Kroeger et al., 2017; Yoo et al., 2017; Assous et al., 2019). In support of this distinction, Caggiano et al. (2018) demonstrated that glutamatergic neurons in the CnF and PPN have vastly different inputs and outputs. While glutamatergic CnF neurons receive most of their monosynaptic inputs from a few midbrain structures, such as the inferior colliculus (IC) and the periaqueductal gray (PAG), glutamatergic PPN neurons receive projections from many brain 

regions, including numerous brainstem nuclei, the basal ganglia, hypothalamus, and frontal cortex ( **Figure 1A** ). Glutamatergic CnF neurons were also found to have a more focused descending output, primarily restricted to the ventrocaudal medulla, while glutamatergic PPN neurons showed broad projections to pontine, medullary, and even upper cervical spinal cord regions (Caggiano et al., 2018), all in addition to their numerous known ascending projections ( **Figure 1A** ; Martinez-Gonzalez et al., 2011; Kroeger et al., 2017; Yoo et al., 2017; Assous et al., 2019). 

Both Caggiano et al. (2018) and Josset et al. (2018) show that activation of glutamatergic CnF neurons is sufficient to initiate locomotion at short latencies; however, the two studies differ on the role of PPN glutamatergic neurons. In addition to demonstrating increased exploratory behavior, Caggiano et al. (2018) found that photoactivation of glutamatergic PPN neurons was able to induce low-speed locomotion from rest in a subset (46%) of trials, albeit with longer latencies (∼1 s) and requiring higher frequency stimulation (50 Hz). In contrast, Josset et al. (2018) found that photoactivation of glutamatergic PPN neurons, particularly ventrally, could not initiate locomotion, and decelerated ongoing locomotion. 

Several potential reasons could explain this discrepancy—there were methodological differences in viral transfection of channelrhodopsin between the two groups and the viral expression profile in the PPN in Josset et al. (2018) appears more restricted than in Caggiano et al. (2018). Furthermore, there were methodological differences in the 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

3 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

stimulation of the PPN between the two groups: dorsal PPN optrode locations with varying pulse width and frequency of stimulation by Caggiano et al. (2018) compared to both dorsal and ventral PPN optrode locations with a more uniform 10 ms pulse width, 20 Hz stimulation protocol by Josset et al. (2018). Interestingly, in trials where Josset et al. (2018) used crossed transgenic mice expressing channelrhodopsin in all glutamatergic neurons, the more dorsally located PPN stimulations were able to initiate low-speed locomotion from rest, where they could not with more ventrally located PPN stimulations ( **Figure 1C** ), nor with the PPN-specific virally-transfected mice. At least one other group supports the view that activation of glutamatergic CnF neurons produces robust locomotion in mice, while activation of glutamatergic PPN neurons reduces locomotor activity, citing important differences between these subpopulations again in terms of their connectivity, but also in their intrinsic membrane properties (Dautan et al., 2020). Their finding that glutamatergic CnF neurons are mostly rapidly adapting and accommodating, while glutamatergic PPN neurons are more heterogeneous in their electrophysiologic properties, provides further insight into why experiments regarding the PPN have often provided mixed behavioral results (Dautan et al., 2020). 

A third study evaluating PPN glutamatergic function in mice using chemogenetics also suggests that these neurons do not directly control locomotion. Kroeger et al. (2017) found that beyond significantly increasing wake time, activating glutamatergic PPN neurons had highly context-dependent results. In the unenriched home cage, animals mostly sat quietly awake, with decreased exploration and feeding compared to normal wake behavior, while the addition of a running wheel encouraged moderate running comparable to that seen during normal wake cycles (Kroeger et al., 2017). In an open field, glutamatergic PPN activation led to animals spending more time in corners, suggesting mild anxiety (Kroeger et al., 2017). Taken together, these studies suggest that while the locomotor contributions of glutamatergic PPN neurons cannot be completely excluded, they likely represent a more functionally heterogeneous population than glutamatergic CnF neurons, which have a clearer role in the initiation and control of gait. 

## CONNECTOME-BASED EVALUATIONS OF MLR FUNCTION 

Given the diffuse projections of glutamatergic and cholinergic PPN neurons, several groups have isolated the effects of selectively activating glutamatergic or cholinergic terminals projecting from the PPN to specific targets of interest. One of the earliest optogenetic studies in the MLR showed that the enhanced visual processing observed with MLR stimulation could largely be dissociated from its locomotor effects by selectively activating PPN terminals targeting cholinergic groups of the basal forebrain (Lee et al., 2014). Additionally, activation of glutamatergic projections from the PPN to dopaminergic neurons in the ventral tegmental area, an area known for its involvement in motivation and addiction, induces robust reinforcement of lever-pressing behavior in mice (Yoo et al., 

2017). In contrast, activating cholinergic PPN projections to the ventral tegmental area only delays the extinction of trained lever-pressing behavior (Dautan et al., 2016). Finally, unilateral activation of glutamatergic PPN projections to the striatum was found to induce ipsiversive head-turning (Assous et al., 2019). Overall, these studies demonstrate the diversity of behaviors attributable to the PPN and conceivably explain why electrical, pharmacological, and even optogenetic manipulations of the PPN have produced such variable behavioral results. Such functional heterogeneity, while potentially providing the PPN with important regulatory properties, ultimately makes the PPN a poor candidate target for DBS to promote a specific function such as gait. 

Conversely, most glutamatergic CnF neurons project to glutamatergic reticulospinal neurons in the medial reticular formation as well as monoaminergic neurons in the locus coeruleus (LC) and raphe nuclei, which form important descending pathways to spinal locomotor networks (Steeves and Jordan, 1980; Noga et al., 2017b). In the mouse, these glutamatergic reticulospinal neurons are necessary and sufficient for mediating MLR-evoked locomotion. Tracing studies have shown that, in addition to receiving presynaptic inputs directly from multiple brain regions [including the superior colliculus (SC), hypothalamus, PAG, deep cerebellar nuclei, red nucleus (RN), zona incerta, and motor cortex], these reticulospinal neurons receive input from both the CnF and the PPN, with more input from the CnF (Capelli et al., 2017). This is consistent with the idea that glutamatergic CnF neurons play a primary role in brainstem locomotor control, and highlight its potential as a DBS target. 

## CLINICAL CONSIDERATIONS 

The results of DBS in this region for gait dysfunction have been variable, although a recent review and meta-analyses suggest that PPN DBS may provide a small benefit concerning postural instability, falls, and FOG (Wang et al., 2016, 2017; Thevathasan et al., 2018). Several explanations have been proposed to account for the absence of a larger effect. First, there may be significant species differences in MLR function, particularly given our bipedal gait and the dominance of our corticospinal tracts (Alam et al., 2011). These differences may have relegated the functional role of the MLR in human gait, such that DBS of this region may not have the same effects in humans. Another possibility is that the stimulation of degenerated or abnormal neurons in the MLR, especially in the context of diseased basal ganglia, may have limited efficacy in compensating for lost function (Benarroch, 2013). A third scenario is that the neurons within the PPN do not represent the MLR and that optimizing the targeting of the MLR could improve its effectiveness. 

Certainly, demonstrating success with DBS of the MLR would speak against the first two possibilities. A recent study of MLR DBS by Goetz et al. (2019) shows that DBS in this area can significantly alleviate FOG in PD patients and highlights the importance of electrode-position. Using responder analysis, the authors demonstrated that while there was significant variability in FOG outcomes among their subjects, categorizing the group 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

4 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

**==> picture [381 x 334] intentionally omitted <==**

FIGURE 2 | Three-dimensional reconstructions of the human MLR and regional anatomy. Reconstructions were made using Lead-DBS and available MNI-space subcortical atlases (Horn and Kühn, 2015). A separate CnF NIfTI object (cyan) was created in MATLAB in relation to the PPN (purple) based on Olszewski and Baxter (1982). (A) A parasagittal projection (5 mm lateral to the midline) of the CnF and PPN is overlaid with active contacts from PPN DBS patients with poor (red), good (green), best (dark blue), and unevaluated (yellow) FOG outcomes from Goetz et al. (2019). (B) Sideview of 3D reconstruction of MLR and regional anatomy, with left ML and STT removed to show the CnF and PPN. (C) Diagonal view with right ML and STT removed, projected on to a transverse slice of the brain at the level of the pons. Abbreviations: CnF, cuneiform nucleus; CTT, central tegmental tract; dSCF, decussating superior cerebellar fibers; LC, locus coeruleus; ML, medial lemniscus; PPN, pedunculopontine nucleus; RN, red nucleus; STT, spinothalamic tract. 

by these outcomes revealed a ‘‘good responder’’ cluster with a significant reduction in % time spent in FOG with DBS on compared to off (34.1 ± 14% vs. 2.7 ± 2.6%). Furthermore, all of these good responders had active electrode contacts either in or bordering the CnF ( **Figure 2A** ; Goetz et al., 2019). This is in agreement with computer modeling studies of DBS in the region, which demonstrate that lead shifts as little as 1 mm significantly decrease target activation selectivity (Zitella et al., 2013). 

The mechanisms of DBS, albeit incompletely understood, are currently believed to encompass electrical, cellular, molecular, and network effects on multiple timescales (Jakobs et al., 2019). Electrically, this is thought to include the induction of orthodromic and antidromic action potentials along both efferent and afferent fibers passing within an electrode’s volume of activation (Anderson et al., 2019; Jakobs et al., 2019). With regards to DBS of the MLR for gait, several potential mechanisms have been proposed: through ascending effects on arousal; by afferent-mediated disruption of cortical and subcortical 

pathological oscillations; through modulatory effects on other structures such as the subthalamic nucleus and substantia nigra; and through descending activation of spinal locomotor networks (Garcia-Rill et al., 2019). Based on the most current understanding of the MLR circuitry, and the anatomo-clinical findings in Goetz et al. (2019), our perspective is that DBS causes orthodromic activation of efferent and/or afferent fibers of glutamatergic CnF neurons targeting reticulospinal neurons in the medulla, which in turn excite spinal central pattern generators to promote gait (Noga et al., 2003). 

## CONCLUSIONS AND FUTURE DIRECTIONS 

More than 50 years after the discovery of the MLR, and 15 years after the first-in-man reports of DBS of the PPN, there remains a conspicuous disconnect between basic science and clinical investigations into this midbrain region. Though the electrical 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

5 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

mapping literature has arguably always favored the CnF, new insights into the functional organization of the MLR further challenges the exclusive focus on the PPN as a DBS target for enhancing gait. Several groups have started to acknowledge this in different ways, ranging from the adoption of a broader ‘‘PPN area’’ terminology (Ferraye et al., 2010; Mestre et al., 2016; Goetz et al., 2019), to asserting that DBS of the PPN should be reconsidered altogether (Albin et al., 2018). Given that subsets of PD patients demonstrate significant improvements in FOG with DBS in this region, further refinement of electrode location, stimulation parameters, and patient selection would seem a reasonable goal. Our view that the CnF should be considered as a DBS target is supported by studies suggesting that glutamatergic CnF neurons represent a primary locus for direct brainstem control of locomotion, with converging clinical evidence that dorsal locations within the MLR are associated with the best gait outcomes. 

Currently, several labs are working to test the hypothesis that CnF DBS may improve gait function, including optogenetic studies assessing the contributions of glutamatergic CnF neurons to locomotor recovery in a rodent model of spinal cord injury (Roussel et al., 2019), detailed characterizations of CnF DBS in a large animal model (Chang et al., 2019), and a pilot clinical study of CnF DBS for FOG (Chang et al., 2020). Topographical analyses of glutamatergic projection neurons within the human CnF and MLR, including the location and orientations of their afferent and efferent pathways, may provide further guidance for targeting electrodes to optimally and selectively activating this circuit ( **Figures 2B,C** ). 

## REFERENCES 

- Alam, M., Schwabe, K., and Krauss, J. K. (2011). The pedunculopontine nucleus area: critical evaluation of interspecies differences relevant for its use as a target for deep brain stimulation. _Brain_ 134, 11–23. doi: 10.1093/brain/awq322 

- Albin, R. L., Surmeier, D. J., Tubert, C., Sarter, M., Müller, M. L. T. M., Bohnen, N. I., et al. (2018). Targeting the pedunculopontine nucleus in Parkinson’s disease: time to go back to the drawing board. _Mov. Disord._ 33, 1871–1875. doi: 10.1002/mds.27540 

- Anderson, D. N., Duffley, G., Vorwerk, J., Dorval, A. D., and Butson, C. R. (2019). Anodic stimulation misunderstood: preferential activation of fiber orientations with anodic waveforms in deep brain stimulation. _J. Neural Eng._ 16:016026. doi: 10.1088/1741-2552/aae590 

- Assous, M., Dautan, D., Tepper, J. M., and Mena-Segovia, J. (2019). Pedunculopontine glutamatergic neurons provide a novel source of feedforward inhibition in the striatum by selectively targeting interneurons. _J. Neurosci._ 39, 4727–4737. doi: 10.1523/jneurosci.2913-18.2019 

- Aziz, T. Z., Davies, L., Stein, J., and France, S. (1998). The role of descending basal ganglia connections to the brain stem in parkinsonian akinesia. _Br. J. Neurosurg._ 12, 245–249. doi: 10.1080/02688699845078 

- Benarroch, E. E. (2013). Pedunculopontine nucleus: functional organization and clinical implications. _Neurology_ 80, 1148–1155. doi: 10.1212/wnl. 0b013e3182886a76 

- Cabelguen, J. M., Bourcier-Lucas, C., and Dubuc, R. (2003). Bimodal locomotion elicited by electrical stimulation of the midbrain in the salamander notophthalmus viridescens. _J. Neurosci._ 23, 2434–2439. doi: 10.1523/jneurosci. 23-06-02434.2003 

- Caggiano, V., Leiras, R., Goñi-Erro, H., Masini, D., Bellardita, C., Bouvier, J., et al. (2018). Midbrain circuits that set locomotor speed and gait selection. _Nature_ 553, 455–460. doi: 10.1038/nature25448 

## DATA AVAILABILITY STATEMENT 

The data analyzed in this study is subject to the following licenses/restrictions: the datasets generated during and/or analyzed during the current study are available from the corresponding author on reasonable request. Requests to access these datasets should be directed to bnoga@med.miami.edu. 

## AUTHOR CONTRIBUTIONS 

All authors were involved in the conception and substantial revision of this manuscript. SC wrote the manuscript and drafted the figures. 

## FUNDING 

This work was supported by the National Institutes of Neurological Disorders and Stroke (NINDS) grant R01 NS089972 and U.S. Department of Defense (DOD) award SCI140238. SC was supported by a research fellowship from the Neurosurgery Research and Education Foundation (GR010471). 

## ACKNOWLEDGMENTS 

We would like to thank Francisco Sanchez and Luz Villamil for their support and helpful contributions to this research. 

- Capelli, P., Pivetta, C., Soledad Esposito, M., and Arber, S. (2017). Locomotor speed control circuits in the caudal brainstem. _Nature_ 551, 373–377. doi: 10.1038/nature24064 

- Chang, S. J., Cajigas, I., Guest, J. D., Noga, B. R., Luca, C. C., and Jagid, J. R. (2020). Deep brain stimulation of the cuneiform nucleus for Levodopa-resistant freezing of gait in Parkinson’s Disease: study protocol for a prospective, pilot trial. Pilot and feasibility studies [Preprint]. doi: 10.21203/rs.3.rs-60496/v1 

- Chang, S. J., Santamaria, A. J., Sanchez, F. J., Saraiva, P. M. P., Villamil, L. M., Nunez-Gomez, Y., et al. (2019). ‘‘Deep brain stimulation of the mesencephalic locomotor region acutely enhances locomotion in a large animal model of incomplete spinal cord injury,’’ in _Neuroscience Meeting Planner_ (Chicago, IL: Society for Neuroscience). 

- Dautan, D., Kovács, A., Bayasgalan, T., Diaz-Acevedo, M. A., Pal, B., and Mena-Segovia, J. (2020). Modulation of motor behavior by the mesencephalic locomotor region. _BioRxiv_ [Preprint]. doi: 10. 1101/2020.06.25. 172296 

- Dautan, D., Souza, A. S., Huerta-Ocampo, I., Valencia, M., Assous, M., Witten, I. B., et al. (2016). Segregated cholinergic transmission modulates dopamine neurons integrated in distinct functional circuits. _Nat. Neurosci._ 19, 1025–1033. doi: 10.1038/nn.4335 

- Doshi, P. K., Desai, J. D., Karkera, B., and Wadia, P. M. (2015). Bilateral pedunculopontine nucleus stimulation for progressive supranuclear palsy. _Stereotact. Funct. Neurosurg._ 93, 59–65. doi: 10.1159/000368702 

- Eidelberg, E., Walden, J. G., and Nguyen, L. H. (1981). Locomotor control in macaque monkeys. _Brain_ 104, 647–663. doi: 10.1093/brain/104. 4.647-a 

- Ferraye, M. U., Debu, B., Fraix, V., Goetz, L., Ardouin, C., Yelnik, J., et al. (2010). Effects of pedunculopontine nucleus area stimulation on gait disorders in Parkinson’s disease. _Brain_ 133, 205–214. doi: 10.1093/brain/ awp229 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

6 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

- Garcia-Rill, E., Houser, C. R., Skinner, R. D., Smith, W., and Woodward, D. J. (1987). Locomotion-inducing sites in the vicinity of the pedunculopontine nucleus. _Brain Res. Bull._ 18, 731–738. doi: 10.1016/0361-9230(87)90208-5 

- Garcia-Rill, E., Saper, C. B., Rye, D. B., Kofler, M., Nonnekes, J., Lozano, A., et al. (2019). Focus on the pedunculopontine nucleus. Consensus review from the may 2018 brainstem society meeting in Washington, DC, USA. _Clin. Neurophysiol._ 130, 925–940. doi: 10.1016/j.clinph.2019. 03.008 

- Goetz, L., Bhattacharjee, M., Ferraye, M. U., Fraix, V., Maineri, C., Nosko, D., et al. (2019). Deep brain stimulation of the pedunculopontine nucleus area in Parkinson disease: MRI-based anatomoclinical correlations and optimal target. _Neurosurgery_ 84, 506–518. doi: 10.1093/neuros/nyy151 

- Hirsch, E. C., Graybiel, A. M., Duyckaerts, C., and Javoy-Agid, F. (1987). Neuronal loss in the pedunculopontine tegmental nucleus in Parkinson disease and in progressive supranuclear palsy. _Proc. Natl. Acad. Sci. U S A_ 84, 5976–5980. doi: 10.1073/pnas.84.16.5976 

- Horn, A., and Kühn, A. A. (2015). Lead-DBS: a toolbox for deep brain stimulation electrode localizations and visualizations. _NeuroImage_ 107, 127–135. doi: 10.1016/j.neuroimage.2014.12.002 

- Jahn, K., Deutschländer, A., Stephan, T., Kalla, R., Wiesmann, M., Strupp, M., et al. (2008). Imaging human supraspinal locomotor centers in brainstem and cerebellum. _NeuroImage_ 39, 786–792. doi: 10.1016/j.neuroimage.2007.09.047 

- Jakobs, M., Fomenko, A., Lozano, A. M., and Kiening, K. L. (2019). Cellular, molecular and clinical mechanisms of action of deep brain stimulation-a systematic review on established indications and outlook on future developments. _EMBO Mol. Med._ 11:e9575. doi: 10.15252/emmm. 201809575 

- Jellinger, K. (1988). The pedunculopontine nucleus in Parkinson’s disease, progressive supranuclear palsy and Alzheimer’s disease. _J. Neurol. Neurosurg. Psychiatry_ 51, 540–543. doi: 10.1136/jnnp.51.4.540 

- Jenkinson, N., Nandi, D., Miall, R. C., Stein, J. F., and Aziz, T. Z. (2004). Pedunculopontine nucleus stimulation improves akinesia in a Parkinsonian monkey. _Neuroreport_ 15, 2621–2624. doi: 10.1097/00001756-200412030-00012 

- Josset, N., Roussel, M., Lemieux, M., Lafrance-Zoubga, D., Rastqar, A., and Bretzner, F. (2018). Distinct contributions of mesencephalic locomotor region nuclei to locomotor control in the freely behaving mouse. _Curr. Biol._ 28, 884.e3–901.e3. doi: 10.1016/j.cub.2018.02.007 

- Karachi, C., Grabli, D., Bernard, F. A., Tande, D., Wattiez, N., Belaid, H., et al. (2010). Cholinergic mesencephalic neurons are involved in gait and postural disorders in Parkinson disease. _J. Clin. Invest._ 120, 2745–2754. doi: 10.1172/JCI42642 

- Kroeger, D., Ferrari, L. L., Petit, G., Mahoney, C. E., Fuller, P. M., Arrigoni, E., et al. (2017). Cholinergic, glutamatergic and GABAergic neurons of the pedunculopontine tegmental nucleus have distinct effects on sleep/wake behavior in mice. _J. Neurosci._ 37, 1352–1366. doi: 10.1523/jneurosci.1405-16. 2016 

- Lee, A. M., Hoy, J. L., Bonci, A., Wilbrecht, L., Stryker, M. P., and Niell, C. M. (2014). Identification of a brainstem circuit regulating visual cortical state in parallel with locomotion. _Neuron_ 83, 455–466. doi: 10.1016/j.neuron.2014. 06.031 

- Luquin, E., Huerta, I., Aymerich, M. S., and Mengual, E. (2018). Stereological estimates of glutamatergic, gabaergic and cholinergic neurons in the pedunculopontine and laterodorsal tegmental nuclei in the rat. _Front. Neuroanat._ 12:34. doi: 10.3389/fnana.2018.00034 

- Mahlknecht, P., Kiechl, S., Bloem, B. R., Willeit, J., Scherfler, C., Gasperi, A., et al. (2013). Prevalence and burden of gait disorders in elderly men and women aged 60-97 years: a population-based study. _PLoS One_ 8:e69627. doi: 10.1371/journal.pone.0069627 

- Martinez-Gonzalez, C., Bolam, J. P., and Mena-Segovia, J. (2011). Topographical organization of the pedunculopontine nucleus. _Front. Neuroanat._ 5:22. doi: 10.3389/fnana.2011.00022 

- Martinez-Gonzalez, C., Wang, H.-L., Micklem, B. R., Bolam, J. P., and Mena-Segovia, J. (2012). Subpopulations of cholinergic, GABAergic and glutamatergic neurons in the pedunculopontine nucleus contain calciumbinding proteins and are heterogeneously distributed. _Eur. J. Neurosci._ 35, 723–734. doi: 10.1111/j.1460-9568.2012.08002.x 

- Mazzone, P., Lozano, A., Stanzione, P., Galati, S., Scarnati, E., Peppe, A., et al. (2005). Implantation of human pedunculopontine nucleus: a safe and 

- clinically relevant target in Parkinson’s disease. _Neuroreport_ 16, 1877–1881. doi: 10.1097/01.wnr.0000187629.38010.12 

- Mena-Segovia, J., Micklem, B. R., Nair-Roberts, R. G., Ungless, M. A., and Bolam, J. P. (2009). GABAergic neuron distribution in the pedunculopontine nucleus defines functional subterritories. _J. Comp. Neurol._ 515, 397–408. doi: 10.1002/cne.22065 

- Mestre, T. A., Sidiropoulos, C., Hamani, C., Poon, Y.-Y., Lozano, A. M., Lang, A. E., et al. (2016). Long-term double-blinded unilateral pedunculopontine area stimulation in Parkinson’s disease. _Mov. Disord._ 31, 1570–1574. doi: 10.1002/mds.26710 

- Mori, S., Sakamoto, T., Ohta, Y., Takakusaki, K., and Matsuyama, K. (1989). Sitespecific postural and locomotor changes evoked in awake, freely moving intact cats by stimulating the brainstem. _Brain Res._ 505, 66–74. doi: 10.1016/00068993(89)90116-9 

- Moro, E., Hamani, C., Poon, Y.-Y., Al-Khairallah, T., Dostrovsky, J. O., Hutchison, W. D., et al. (2010). Unilateral pedunculopontine stimulation improves falls in Parkinson’s disease. _Brain_ 133, 215–224. doi: 10.1093/brain/awp261 

- Nandi, D., Liu, X., Winter, J. L., Aziz, T. Z., and Stein, J. F. (2002). Deep brain stimulation of the pedunculopontine region in the normal non-human primate. _J. Clin. Neurosci._ 9, 170–174. doi: 10.1054/jocn.2001.0943 

- Noga, B. R., Kriellaars, D. J., Brownstone, R. M., and Jordan, L. M. (2003). Mechanism for activation of locomotor centers in the spinal cord by stimulation of the mesencephalic locomotor region. _J. Neurophysiol._ 90, 1464–1478. doi: 10.1152/jn.00034.2003 

- Noga, B. R., Sanchez, F. J., Villamil, L. M., O’toole, C., Kasicki, S., Olszewski, M., et al. (2017a). LFP oscillations in the mesencephalic locomotor region during voluntary locomotion. _Front. Neural Circuits_ 11:34. doi: 10.3389/fncir.2017. 00034 

- Noga, B. R., Turkson, R. P., Xie, S., Taberner, A., Pinzon, A., and Hentall, I. D. (2017b). Monoamine release in the cat lumbar spinal cord during fictive locomotion evoked by the mesencephalic locomotor region. _Front. Neural Circuits_ 11:59. doi: 10.3389/fncir.2017.00059 

- Olszewski, J., and Baxter, D. (1982). _Cytoarchitecture of the Human Brain Stem._ Basel: S. Karger. 

- Opris, I., Dai, X., Johnson, D. M. G., Sanchez, F. J., Villamil, L. M., Xie, S., et al. (2019). Activation of brainstem neurons during mesencephalic locomotor region-evoked locomotion in the cat. _Front. Syst. Neurosci._ 13:69. doi: 10.3389/fnsys.2019.00069 

- Piallat, B., Chabardes, S., Torres, N., Fraix, V., Goetz, L., Seigneuret, E., et al. (2009). Gait is associated with an increase in tonic firing of the sub-cuneiform nucleus neurons. _Neuroscience_ 158, 1201–1205. doi: 10.1016/j.neuroscience. 2008.10.046 

- Pienaar, I. S., Elson, J. L., Racca, C., Nelson, G., Turnbull, D. M., and Morris, C. M. (2013). Mitochondrial abnormality associates with type-specific neuronal loss and cell morphology changes in the pedunculopontine nucleus in Parkinson disease. _Am. J. Pathol._ 183, 1826–1840. doi: 10.1016/j.ajpath.2013. 09.002 

- Roseberry, T. K., Lee, A. M., Lalive, A. L., Wilbrecht, L., Bonci, A., and Kreitzer, A. C. (2016). Cell-type-specific control of brainstem locomotor circuits by basal ganglia. _Cell_ 164, 526–537. doi: 10.1016/j.cell.2015.12.037 

- Roussel, M., Godet, H., Clain, G., Lafrance-Zoubga, D., Lemieux, M., and Bretzner, F. (2019). ‘‘Functional contribution of the mesencephalic locomotor region to locomotor recovery after spinal cord injury,’’ in _Neuroscience Meeting Planner_ (Chicago, IL: Society for Neuroscience). 

- Ryczko, D., and Dubuc, R. (2013). The multifunctional mesencephalic locomotor region. _Curr. Pharm. Des._ 19, 4448–4470. doi: 10.2174/13816128113 19240011 

- Sébille, S. B., Belaid, H., Philippe, A.-C., André, A., Lau, B., François, C., et al. (2017). Anatomical evidence for functional diversity in the mesencephalic locomotor region of primates. _NeuroImage_ 147, 66–78. doi: 10.1016/j. neuroimage.2016.12.011 

- Sebille, S. B., Rolland, A.-S., Faillot, M., Perez-Garcia, F., Colomb-Clerc, A., Lau, B., et al. (2019). Normal and pathological neuronal distribution of the human mesencephalic locomotor region. _Mov. Disord._ 34, 218–227. doi: 10.1002/mds. 27578 

- Shik, M. L., Severin, F. V., and Orlovskii, G. N. (1966). Control of walking and running by means of electric stimulation of the midbrain. _Biofizika_ 11, 659–666. 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

7 

Chang et al. 

Cuneiform Nucleus Stimulation for Gait 

- Skinner, R. D., and Garcia-Rill, E. (1984). The mesencephalic locomotor region (MLR) in the rat. _Brain Res._ 323, 385–389. doi: 10.1016/0006-8993(84) 90319-6 

- Steeves, J. D., and Jordan, L. M. (1980). Localization of a descending pathway in the spinal cord which is necessary for controlled treadmill locomotion. _Neurosci. Lett._ 20, 283–288. doi: 10.1016/0304-3940(80)90161-5 

- Stefani, A., Lozano, A. M., Peppe, A., Stanzione, P., Galati, S., Tropepi, D., et al. (2007). Bilateral deep brain stimulation of the pedunculopontine and subthalamic nuclei in severe Parkinson’s disease. _Brain_ 130, 1596–1607. doi: 10.1093/brain/awl346 

- Takakusaki, K., Chiba, R., Nozu, T., and Okumura, T. (2016). Brainstem control of locomotion and muscle tone with special reference to the role of the mesopontine tegmentum and medullary reticulospinal systems. _J. Neural Transm._ 123, 695–729. doi: 10.1007/s00702-015-1475-4 

- Thevathasan, W., Debu, B., Aziz, T., Bloem, B. R., Blahak, C., Butson, C., et al. (2018). Pedunculopontine nucleus deep brain stimulation in Parkinson’s disease: a clinical review. _Mov. Disord._ 33, 10–20. doi: 10.1002/mds.27098 

- Wang, H., Gao, H., Jiao, T., and Luo, Z. (2016). A meta-analysis of the pedunculopontine nucleus deep-brain stimulation effects on Parkinson’s disease. _Neuroreport_ 27, 1336–1344. doi: 10.1097/WNR.0000000000000697 

- Wang, J. W., Zhang, Y. Q., Zhang, X.-H., Wang, Y.-P., Li, J.-P., and Li, Y.-J. (2017). Deep brain stimulation of pedunculopontine nucleus for postural instability and gait disorder after Parkinson disease: a meta-analysis of individual patient data. _World Neurosurg._ 102, 72–78. doi: 10.1016/j.wneu.2017.02.110 

- Winn, P. (2008). Experimental studies of pedunculopontine functions: are they motor, sensory or integrative? _Parkinsonism Relat. Disord._ 14, S194–S198. doi: 10.1016/j.parkreldis.2008.04.030 

- Yoo, J. H., Zell, V., Wu, J., Punta, C., Ramajayam, N., Shen, X., et al. (2017). Activation of pedunculopontine glutamate neurons is reinforcing. _J. Neurosci._ 37, 38–46. doi: 10.1523/JNEUROSCI.3082-16.2016 

- Zitella, L. M., Mohsenian, K., Pahwa, M., Gloeckner, C., and Johnson, M. D. (2013). Computational modeling of pedunculopontine nucleus deep brain stimulation. _J. Neural Eng._ 10:045005. doi: 10.1088/1741-2560/10/4/045005 

- Zweig, R. M., Jankel, W. R., Hedreen, J. C., Mayeux, R., and Price, D. L. (1989). The pedunculopontine nucleus in Parkinson’s disease. _Ann. Neurol._ 26, 41–46. doi: 10.1002/ana.410260106 

**Conflict of Interest** : The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. 

_Copyright © 2020 Chang, Cajigas, Opris, Guest and Noga. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms_ . 

Frontiers in Systems Neuroscience | www.frontiersin.org 

August 2020 | Volume 14 | Article 64 

8 

