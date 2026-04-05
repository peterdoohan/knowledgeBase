bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

## **A Prefrontal Neural Circuit for Maternal Behavioural Learning in Mice** 

Gen-ichi Tasaka[1,2*] , Mitsue Hagihara[1] , Satsuki Irie[1] , Haruna Kobayashi[1] , Kengo Inada[1] , Miho Kihara 3, Takaya Abe 3, and Kazunari Miyamichi1* 

- 1 Laboratory for Comparative Connectomics, RIKEN Center for Biosystems Dynamics Research, Kobe, Hyogo 650-0047, Japan 

- 2 Japan Science and Technology Agency, PRESTO, Kawaguchi, Saitama 332-0012, Japan 

- 3 Laboratory for Animal Resources and Genetic Engineering, RIKEN Center for Biosystems Dynamics Research, Kobe, Hyogo 650-0047, Japan. 

*Corresponding author: genichi.tasaka@riken.jp; kazunari.miyamichi@riken.jp 

## **Summary** 

**Maternal behaviours, which are crucial for the survival of mammalian infants[1] , can be learned[2,3] . How the efficient acquisition of these behaviours is implemented at the neural circuitry level remains poorly understood. Although prevalent models of neural circuits for parental behaviours often assume the frontal cortical network as an integrator of infant-related sensory signals and a controller of decision-making and motivation[1,4] , these ideas have not been functionally tested. As such, detailed input/output neural circuit organizations of the frontal cortex in relation to parental behaviours remain unknown. Here we show that the orbitofrontal cortex (OFC) promotes efficient learning of maternal behaviours in virgin female mice when they are co-housed with lactating mothers. Chronic microendoscopy in freely behaving animals reveals robust representations of pup-directed anticipatory activities and ongoing sequential motions of pup retrieval that are innately sculpted and largely unaffected by learning. Through viral tracing and manipulations, we functionally identify the submedius thalamus as a prominent presynaptic partner of the OFC that shapes pup-related representations. Optogenetic inactivation of OFC reduces the pup retrieval-related activities of midbrain dopamine neurons[5,6] that promote maternal behaviours. Collectively, these findings reveal a higher-order cognitive network that connects innately formed, pup-related integrated representation to the top-down control of motivation centers, thus enabling efficient maternal behavioural learning.** 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

While recent molecular genetic studies in mice have described precise circuit architectures of subcortical parental behavioural centers at the resolution of specific cell types[5,7-11] , the functional organization of the prefrontal cortex (PFC) network that potentially links sensory signals to maternal behavioural execution remains mostly elusive[12] . Based on preceding studies reported that the orbitofrontal cortex (OFC) of mother mice and humans is activated by infants related sensory signals[13-] 15, we examined the requirement of the excitatory layer 5 pyramidal cells in the OFC (OFCRbp4 neurons) as a major output of the OFC[16,17] . Injection of taCasp3 encoding adeno-associated virus (AAV)[18] significantly ablated OFC[Rbp4] neurons by approximately 30% (Extended Data Fig. 1a–c). To evaluate the effects of the bilateral OFC ablation, we utilized the learning paradigm of alloparental behaviours by co-housing virgin female mice with a mother and pups (Extended Data Fig. 1d)[3,19] . We found a significant delay of maternal behavioural learning, with a prolonged latency to the pup retrieval and reduced number of retrieved pups in OFC-ablated mice (Extended Data Fig. 1e–i). Thus, OFC[Rbp4] neurons are required for the efficient learning of maternal behaviours in female mice. 

## **Representation of pup retrieval in OFC[Rbp4] neurons** 

To explore how maternal behaviours are represented in the OFC[Rbp4] neurons, we performed chronic Ca[2+] imaging across the different stages of maternality: naïve virgin (NV), co-housed virgin on day 1 (CV1) and day 2 (CV2), lactating mother (LM), and weaned mother (WM) (Fig. 1a, b). We utilized microendoscopic Ca[2+] imaging[20] with _Rbp4-Cre_ ; _Ai162_ female mice[21,22] that were implanted with a gradient refractive index (GRIN) lens (500-  m diameter) above layer 5 of the OFC. Maternal behaviours during the imaging sessions were significantly facilitated by CV2 (Fig. 1c, left and middle panels). Several NV mice showed a substantial number of spontaneous retrievals, although these were associated with a higher rate of failure to complete (Fig. 1c, right panel). 

Expression of GCaMP6s and placement of the lens were confirmed histologically (Fig. 1d, e). We detected typically 55.4 ± 15.2 (mean ± standard deviation) cells in the fields of view (Fig. 1f). Pup retrieval consists of three major behavioural categories (in the following order): interaction with a pup, retrieval onset, and dropping a pup into the nest (completion). In CV2 females, we found that some OFC[Rbp4] neurons exhibited an increased Ca[2+] transient (elevated) response, whereas others showed a decreased (suppressed) response upon the onset of pup retrieval (Fig. 1g). We also noticed elevated and suppressed responses time-locked to interaction and completion. In addition, a distinct population showed elevated or suppressed responses just before the interaction (gray traces shown in Extended Data Fig. 2a–c). We refer to this category as anticipatory, the presence of which suggests that a subpopulation of OFC[Rbp4] neurons may encode the premoter signals. These data show that the OFC of learned female mice contains neural populations responsive to various behavioural categories of pup retrieval, covering the entire sequential actions at the population level. 

How does the representation of pup retrieval in the OFC[Rbp4] neurons develop? In one scenario, it is gradually formed in an experience-dependent manner upon interaction with pups during learning of alloparental behaviours. Alternatively, the OFC[Rbp4] neurons are innately dedicated to stable 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

representations of pup retrieval. To distinguish these possibilities, we analyzed Ca[2+] imaging data across the different stages of maternality from NV to WM (Fig. 1a). Because each neuron exhibited either elevated or suppressed responses during a specific time window of pup retrieval without bimodal patterns (see Fig. 1j below and Methods), we classified responsive OFC[Rbp4] neurons into eight subgroups based on either elevated or suppressed and on behavioural categories to which the Ca[2+] transients were locked: anticipatory, interaction, retrieval onset, and completion (Fig. 1h, i). Notably, behaviour-locked Ca[2+] responses were well observed, even in NV mice which had never met pups before, and consistently detected across all maternality stages, with only a slight reduction of elevatedresponsive populations was seen in the LM and WM stages as compared with the NV and CV1 stages. These data indicate that OFC[Rbp4] neurons contain a temporally stable representation of pup retrieval. 

To enhance the temporal resolution of Ca[2+] responses, we sorted cells by the time of their maximum responses in alignment with the onset of pup interaction to draw activity heat maps (Fig. 1j). In all maternality stages, peak response times tiled the entire pup retrieval, including the anticipatory periods. Quantifying the Ca[2+] traces showed that the amplitude of responsiveness was grossly similar across all categories and maternality stages (Fig. 1k, l). Notably, the same cells exhibited comparable activity patterns between CV1 and CV2, and even between CV2 and LM, implying that individual cell activity patterns are largely unaffected by learning of maternal behaviours (Extended Data Fig. 2d–g). As not all interaction behaviours were followed by pup retrieval, we also analyzed the activities of OFC[Rbp4] neurons during the interaction trials that were not followed by pup retrieval (non-retrieval). Activity heat maps showed that both elevated and suppressed responses to all behavioural categories were weak during the non-retrieval trials (Extended Data Fig. 2h). Statistical analyses revealed that a small fraction of anticipatory- and interaction-responding neurons exhibited a weak but significant response, even during non-retrieval trials, whereas the onset-responding cells were mostly silent during the corresponding time window of the non-retrieval trials (Extended Data Fig. 2i, j). These observations suggest that most responses during pup retrieval are behaviour-locked and that weak responses in the anticipatory and interaction stages may be caused by pup-related sensory stimuli. 

To examine further whether the representation of pup retrieval in OFC[Rbp4] neurons is formed without prior interactions with pups, we artificially facilitated NV mice to evoke maternal behaviours without co-housing by pharmacogenetically activating oxytocin (OT) neurons in the paraventricular hypothalamic nucleus (PVN) (Extended Data Fig. 3a–d)[23,24] . We found that OT-activated NV female mice showed neural responses to all behavioural categories of pup retrieval (Extended Data Fig. 3e– i), which closely resembled those observed in co-housed females (Fig. 1). Notably, their activity patterns of OFC neurons and behavioural performance were maintained the next day. Collectively, our data indicate that OFC[Rbp4] neurons are innately tuned to represent all behavioural categories of pup retrieval that are minimally affected by the experience of pups or maternal behavioural learning. 

## **Selectivity of OFC representations of pup retrieval** 

The sensory cues of infants, especially olfactory signals in rodents, trigger pup-directed behaviours 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

and are essential for the recognition of pups[25] . We carried out Ca[2+] imaging to determine whether pup retrieval-responsive OFC[Rbp4] neurons overlap with those responding to pup odor (Fig. 2a–c). While we identified pup retrieval-responsive (Fig. 2d, e; colored circles) and pup odor-responsive (black circles) OFC[Rbp4] neurons, a small amount of overlap was seen between them; only 14% of pup retrieval-responding cells were significantly active upon exposure to pup odor, regardless of whether the response was elevated or suppressed (yellow circles). These data demonstrate the mostly nonoverlapping representations of pup retrieval and pup-related olfactory signals in OFC[Rbp4] neurons, supporting the notion that representations of pup retrieval are not merely due to pup-related sensory signals. 

We also explored the degree to which the OFC[Rbp4] neurons responsive to pup retrieval overlap with those activated by a non-social reward, sugar water (10% sucrose) for water-deprived mice. We performed Ca[2+] imaging for pup retrieval and licking water in the same imaging sessions (Fig. 2f–h). We found that 98 and 30 OFC[Rbp4] neurons showed an elevated response to pup retrieval and the nonsocial reward, respectively, suggesting that OFC[Rbp4] neurons are more preferentially tuned to social than to non-social cues (Fig. 2i, j). Whereas only 14% of the pup retrieval-responding OFC[Rbp4] neurons were active upon exposure to the water reward, 47% of water-reward-responding OFC[Rbp4] neurons were active during pup retrieval. Regarding suppressed responses, we found substantial overlap between OFC[Rbp4] neurons that responded to pup retrieval and the non-social reward (Figure 2i, j). Collectively, under the constraints imposed by the behavioural paradigm (see Discussion), these observations suggest the presence of OFC[Rbp4] subpopulations that are preferentially tuned to elevated responses to pup-retrieval behaviours, pup-associated sensory stimuli, or non-social rewards. In addition, some OFC[Rbp4] neurons show mixed selectivity. 

## **The SMT shapes pup-retrieval representations** 

How do OFC[Rbp4] neurons form representations of pup retrieval? To map their presynaptic inputs, we applied Cre-dependent rabies virus-based retrograde monosynaptic tracing[26] to OFC[Rbp4] neurons using _Rbp4-Cre_ mice (Fig. 3a). The vast majority of the starter cells, defined as the overlap of TVA-mCherry and rabies-derived GFP, were located in the OFC, predominantly in the ventral and lateral subdivisions (Fig. 3b, c), where we performed Ca[2+] imaging (Figs. 1, 2). To analyze the distribution of presynaptic partners quantitatively, we utilized a section-based whole-brain analysis platform called AMaSiNe[27] for the three-dimensional reconstruction and annotation of brain regions to which the labeled neurons belonged (Methods). The majority of the presynaptic neurons were located in the other cortices, including the contralateral OFC, and the medial thalamic nuclei (Fig. 3d–g, Extended Data Fig. 4). 

Given that thalamocortical afferents are suited for conveying pup-related sensorimotor signals to the OFC, we focused on the thalamic input to the OFC. Qualitative analyses of the thalamic nuclei revealed that the submedius thalamus (SMT) and mediodorsal thalamus (MD) provided most inputs (Fig. 3f). Notably, we found that the majority (83%) of the rabies-GFP-expressing cells in the SMT were positive for a region-specific thalamic marker, _Tnnt1_ , encoding a subunit of troponin[28] (Fig. 3h). 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

To provide genetic access to _Tnnt1_ neurons for the anatomical and functional characterization of SMT, we generated _Tnnt1-Cre_ knock-in mice using CRISPR-Cas9-mediated genome editing (Extended Data Fig. 5a, b). We found that _Tnnt1-Cre_ crossed with _Ai162_ showed selective expression of GCaMP6s in both the SMT and MD, with several additional thalamic nuclei, consistent with the mRNA expression pattern described in a previous report[28] . The vast majority of GCaMP6s-expressing neurons in the SMT and MD of _Tnnt1-Cre_ ; _Ai162_ mice expressed _Tnnt1_ and _vGluT2_ mRNAs (Extended Data Fig. 5c–e). Therefore, _Tnnt1-Cre_ mice allow selective targeting to excitatory _Tnnt1_ neurons in the SMT and MD (SMT[Tnnt1] and MD[Tnnt1] neurons, respectively) without affecting neighboring _Tnnt1_ -negative cells. 

To identify the projection targets of SMT[Tnnt1] and MD[Tnnt1] neurons, respectively, we injected AAV _FLEx-TVA-mCherry_ into the SMT and MD of _Tnnt1-Cre_ mice (Fig. 3i). We quantified the number of mCherry-expressing cells (Extended Data Fig. 5f, g), which were utilized to normalize axonal projections for each animal. Focusing on the frontal region, SMT[Tnnt1] neurons projected mainly to the ventral and lateral parts of the OFC (vOFC and lOFC, respectively), whereas MD[Tnnt1] neurons intensively projected to the medial and lateral parts of the OFC (mOFC and lOFC, respectively) and agranular insular cortex (AI) (Fig. 3j, k). In addition, MD[Tnnt1] but not SMT[Tnnt1] neurons sent axons to mPFC structures such as the prelimbic cortex (PL) and also the amygdala and ventral striatum (Fig. 3k). Collectively, our anterograde tracing revealed that SMT[Tnnt1] neurons selectively project to OFC subregions where we performed Ca[2+] imaging, while MD[Tnnt1] neurons send complementary and more broad projections. 

To dissect the functional roles of SMT or MD in shaping neural representations of pup retrieval in OFC[Rbp4] neurons, we first conducted microendoscopic Ca[2+] imaging of SMT[Tnnt1] or MD[Tnnt1] neurons during pup retrieval in _Tnnt1-Cre; Ai162_ female mice at CV1 and CV2 stages (Fig. 4a, b, Extended Data Fig.6). At the CV1 stage, 26% of the imaged SMT[Tnn1] neurons showed elevated responses to one of the behavioural categories of pup retrieval, while 32% was suppressed (Fig. 4c). By contrast, at the CV2 stage, both elevated- and suppressed-responsive SMT[Tnn1] neurons significantly decreased. The fraction of responsive behavioural categories in pup retrieval was grossly unchanged (Fig. 4d). Activity heat maps based on all imaged SMT[Tnnt1] neurons showed that peak response times tiled the entire pup retrieval in the CV1 and CV2 stages (Fig. 4e), resembling what we observed in the downstream OFC[Rbp4] neurons (Fig. 1). The amplitude of the responsive SMT[Tnnt1] neurons in each of the behavioural categories was grossly unchanged between the CV1 and CV2 stages (Fig. 4f, g), and these activity patterns were not seen in the interaction trials followed by no pup retrieval (Extended Data Fig. 7). These observations indicate that SMT[Tnnt1] neurons exhibit a similar neural representation of pup retrieval as compared with those observed in downstream OFC[Rbp4] neurons, while the neural representation of SMT[Tnnt1] neurons may be uniquely modulated by experience or learning. 

To test the contributions of SMT to the representations of pup retrieval in OFC[Rbp4] neurons, we combined projection-based chemogenetic inhibition of SMT neurons with microendoscopic Ca[2+] imaging of OFC[Rbp4] neurons before and after CNO injection in _Rbp4-Cre_ ; _Ai162_ mice at CV2 stage 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

(Fig. 4h, Extended Data Fig. 8a). We found that silencing of SMT[→OFC] neurons (Extended Data Fig. 9a) attenuated the elevated responses in OFC[Rbp4] neurons during pup retrieval, except for interactionresponses, whereas there was no effect on suppressed responses (Fig. 4i, j). In mCherry-expressing control mice, CNO injection did not affect the pattern of representation (Extended Data Fig. 8). Of note, silencing of SMT[→OFC] neurons did not affect the behavioural performance (Extended Data Fig 9c–e), presumably due to the remaining OFC representations of pup retrieval. In sharp contrast to SMT, we found silencing of MD `[→]`[OFC] neurons (Extended Data Fig. 9b) did not affect elevated or suppressed responses of OFC[Rpb4] neurons during pup retrieval, except for a small change in suppressed interaction-responses (Extended Data Fig. 6h–j), although MD[Tnnt1] neurons exhibited pup-retrievallocked neural representations (Extended Data Figs. 6, 7). Collectively, these data indicate that SMT, a prominent presynaptic structure of the OFC[Rbp4] neurons, functionally contributes to the formation of pup retrieval-related neural representations. 

## **OFC facilitates VTA[DA] neurons during pup retrieval** 

How do OFC[Rbp4] neurons facilitate behavioural learning (Extended Data Fig. 1) in the downstream neural circuit? As the dopamine (DA) neurons in the ventral tegmental area (VTA[DA] ) can be directly regulated by OFC[29] and critically guide maternal motivation toward infants[6] , we next aimed to characterize VTA[DA] neurons as a potential output of the OFC. We first confirmed the direct projections from OFC[Rbp4] neurons to the VTA (Extended Data Fig. 10a–c). We then combined the optogenetic silencing of the OFC by inhibitory opsin GtACR2 with Ca[2+] imaging of VTA[DA] using fiber photometry in _DAT-Cre_ mice[30] crossed with _Ai162_ mice (Fig. 5a–c). GCaMP6s was selectively expressed by DA neurons in the _DAT-Cre_ ; _Ai162_ mice (Fig. 5d). 

We performed a total of four sessions of pup retrieval assay during imaging with or without laser stimulation (Fig. 5b). Consistent with preceding studies[5,6] , VTA[DA] neurons showed time-locked activity immediately after pup interaction (Fig. 5e). Silencing the OFC significantly reduced the Ca[2+] activity of VTA[DA] at the CV1 and CV2 stages (Fig. 5e–g). In accordance with a previous report[6] , we observed a trend of declining Ca[2+] transients as maternality stages progressed from CV1 to LM, which seemed to correspond to the reduction caused by silencing the OFC neurons (Extended Data Fig. 10d). Response magnitude was inversely correlated with the performance (Extended Data Fig. 10e). Notably, silencing the OFC did not affect the activity of VTA[DA] neurons at the LM stage (Fig. 5f, g). We also found that acute optogenetic inhibition of the OFC reduced the number of retrievals only at the early stage of behavioural learning, CV1 (Fig. 5h). Taken together, these data show that OFC functionally facilitates VTA[DA] and this effect can underlie efficient learning of maternal behaviours. 

## **DISCUSSION** 

Parental behaviours, which are essential for the survival of mammalian infants, can be learned. In primates and rodents, including humans, marmosets, and mice, non-biological parents can provide care for infants after the instruction or observation of experienced caretakers[2] . A recent seminal study 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

demonstrated the involvement of PVN[OT] in this learning of alloparental behaviours[3] ; however, the neural underpinnings remain incompletely understood. The present study provides a systematic examination of the structural and functional organization of higher cognitive areas for pup-directed caregiving behaviours. Specifically, our data suggest that the SMT-OFC circuit forms innate and learning-invariant representations of pup retrieval in the OFC, which in turn support the efficient learning of maternal behaviours by facilitating the VTA[DA] system. 

Decades of studies have revealed that the OFC is involved in value-based decision-making and reversal learning by representing and updating subjective values[31-33] . Artificial learning paradigms utilizing mono-modality sensory cues are often used in these studies. However, neural representations of the OFC during naturally occurring behavioural learning have been much less studied. In contrast to a prevalent view that the PFC can modulate social behaviours based on its flexible coding shaped by prior experiences or learning[34-36] , our data revealed a rich representation of pup retrieval in the OFC that are innately sculpted and largely unaffected by learning (Fig. 1). Such invariance is compatible with an abstract representation of the identity of behaviour (pup retrieval), which is suited for guiding decision-making or encoding the valance of behaviours in downstream neural circuits. Importantly, OFC contains many neurons selectively tuned to pup retrieval, pup-related sensory signals, or pure rewards (Fig. 2). These observations suggest that the OFC could utilize distinct neural coding schemes for behaviourally relevant objects (“pups”) from fragmented mono-modality signals. The number of responsive neurons to pup retrieval was three times larger than that of neurons responsive to non-social rewards (Fig. 2), suggesting that the OFC may engage more in adjusting innately defined social behaviours. Future studies should address how the OFC is involved in other types of social behaviours, such as social dominance, sexual behaviours, and territorial aggression. 

Although thalamocortical afferents to the frontal cortex have received interest in the context of sensory processing, attention, decision-making, and memory[37] , the exact presynaptic structures of the OFC remain incompletely characterized. Our data by rabies virus-mediated trans-synaptic tracing give a quantitative brain-wide presynaptic landscape of OFC[Rbp4] neurons (Fig. 3) that is also partly supported by previous studies using classical tracing methods[38-40] . Specifically, we revealed that the SMT, a previously less studied area of the higher thalamic regions[41,42] , is an anatomically and functionally prominent presynaptic partner of OFC[Rbp4] neurons that contributes to the formation of pup retrieval-related neural representation in OFC[Rbp4] neurons (Figs. 3, 4). The remaining OFC representations of pup retrieval after inactivation of the SMT might be due to incomplete silencing by projection-based targeting of hM4Di and/or the presence of a redundant neural pathway. How does the SMT shape the representation of pup retrieval in OFC[Rbp4] neurons? In one scenario, sensory signals from multiple primary sensory areas may be integrated into the SMT neurons, which are then conveyed to the OFC. Alternatively, the reciprocal OFC-SMT feedforward loop (Extended Data Fig. 10b) contributes to the formation of similar neural representations in these two structures, a phenomenon well realized in other parts of the interconnected frontal cortex-thalamus network[43,44] . To dissect the exact functions of SMT, future studies including the imaging of SMT neurons while manipulating the 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

OFC or other presynaptic structures of the SMT are needed. Given that the newly established _Tnnt1Cre_ mice allow selective labeling and manipulation of the SMT with minimal effects on the surrounding structures, we expect to facilitate future studies of input/output organizations and functions of this less-studied thalamic nucleus. 

A classical study suggests that VTA[DA] neurons play an essential role in maternal behaviours[45] , and more recent studies have uncovered the temporal dynamics of their neural activity during pup retrieval[5,6] . Our data demonstrate a functional link through which OFC neurons facilitate pup-retrievallocked VTA[DA] activities only during the early stages of learning (Fig. 5). Given that VTA[DA] neuron activities during pup retrieval are thought to encode a social reward prediction error[6] , one intriguing possibility is that some activities in the OFC, particularly those time-locked to anticipatory and interaction categories, may contribute to this process. If this is the case, how does the OFC lose influence on VTA[DA] activities at the LM stage when maternal behavioural learning is completed? The maternal plasticity in the OFC to VTA[DA] neural circuits should be worth investigating in future studies. In this context, direct axonal projections from the OFC to VTA (Extended Data Fig. 10) are an interesting target[29,46] , although multiple synaptic pathways may also be significant. 

The present study has several limitations. First, although we focused on the OFC based on its neural activation by infant-related sensory inputs in humans and mice[13-15] , we did not analyze the specificity of the OFC in the regulation of maternal behavioural learning. Other parts of the frontal cortices, such as the mPFC[12] , may have a similar function in parallel with the OFC-SMT network. Second, although we found OFC[Rbp4] neurons whose activities tiled the entire behavioural categories, whether those distinct populations can be associated with subtypes of neurons based on their axonal projection or gene expression pattern[17,47] remains unclear. As projection-defined neurons can encode unique or overlapping information[29,48] , future studies should address whether transcriptional types or projectiondefined neurons in the OFC encode unique information about pup retrieval to the defined downstream targets. Third, we cannot rule out the possibility that the disparity in behavioural paradigms, specifically pup retrieval in a freely moving setting versus a head-fixed condition for odor exposure, may impact the sensitivity of identifying responsive cells or the character of their responsiveness (Fig. 2). For instance, some anticipatory and interaction-responsive cells during pup retrieval may encode active motor planning towards pup-related signals, which would be disrupted in the head-fixed paradigm. Future studies should devise an imaging or recording protocol whereby multiple diverse task categories can be analyzed in a consistent manner. Fourth, although our study showed that the OFC facilitated the pup retrieval-locked neural activities of VTA[DA] neurons, we did not identify which behavioural category-locked OFC activities were required for this effect. It also remains unclear whether OFC activities are acutely required for trial-based learning of pup retrieval. Lastly, although recent studies have suggested the functional heterogeneity of VTA[DA] neurons[49,50] , our study treated the entire VTA[DA] as one. Thus, we expect future studies to record VTA[DA] at single-cell resolution and manipulate their specific transcriptomic or projection types, which could illuminate the neural basis that converts parental motivation into motor execution. 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

## **Main Figures** 

**==> picture [309 x 653] intentionally omitted <==**

**Fig. 1 A stable representation of pup retrieval in the OFC[Rbp4] neurons. a** , Schematic of the 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

experimental paradigm. NV, naïve virgin; CV1, co-housed virgin on day 1; CV2, co-housed virgin on day 2; LM, lactating mother (postpartum days 2–4 [P2–4]); WM, weaned mother (P27–30). **b** , Schematic of pup retrieval assay during Ca[2+] imaging. **c** , Quantification of the performance of pup retrieval. *, p < 0.05, **, p < 0.01, and ***, p < 0.001 by post hoc Tukey’s honestly significant difference (HSD) test after a significant Kruskal–Wallis test. Error bars, SEM. **d** , Representative image showing the GRIN lens tract and the expression of GCaMP6s. Scale bar, 1 mm. **e** , Schematics of coronal sections showing the position of the GRIN lens tip (lines) for each mouse (N = 16). **f** , Example of a spatial map of cells that responded during pup retrieval from one CV2 mouse. Identified region of interest (ROI) are drawn with a black line. Colors within the ROI correspond to the elevated (orange) or suppressed (light green) response. A, anterior, M, medial. Scale bar, 100  m. **g** , The trial-average activity (top) of the individual elevated- and suppressed-responsive cells (cell IDs are shown at the top) to the onset of pup retrieval, exhibiting the normalized (norm)  F/F values to the maximum  F/F within the individual. Colored heat maps at the bottom show the corresponding single trials. **h** , Bar graph showing the fraction of elevated (orange) and suppressed (blue) responses during pup retrieval. ***, p < 0.001 by the chi-squared test for equality of proportions with Bonferroni correction. **i** , Fraction of cells that responded to one of the four behavioural categories of pup retrieval among the elevated (left) or suppressed (right) population. ***, p < 0.001 by the chi-squared test for equality of proportions with Bonferroni correction. **j** , Activity heat map representations showing normalized and averaged single-cell responses during pup retrieval. Cells are sorted by the time of their maximum responses on each day, with 0 indicating the timing of the interaction with a pup followed by retrieval. **k** , Averaged activity trace of significantly responsive cells to anticipatory, interaction, the onset of retrieval, and completion. Solid and dotted lines indicate elevated and suppressed responses, respectively. The numbers in parentheses indicate the number of cells that exhibited elevated or suppressed (sup) responses. l, Quantification of averaged response (ns, not significant by the Kruskal–Wallis test). Error bars, SEM. 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [488 x 365] intentionally omitted <==**

**Fig. 2 Selectivity of OFC representations of pup retrieval. a** , **f** , Schematic of the experimental paradigm. **b** , **g** , Example of a spatial map of OFC[Rbp4] neurons that responded during pup retrieval and passive exposure of pup odor ( **b** ) or 10% sucrose water as a non-social reward ( **g** ). A, anterior, M, medial. Scale bar, 100  m. **c** , **h** , Trial-averaged activities (top) and corresponding activity heat maps of individual trials (bottom) for a single OFC[Rbp4] neuron responding to both the interaction stage and pup odor ( **c** ) or both the onset stage and the non-social reward ( **h** ). **d** , **i** , Mean response of individual OFC[Rbp4] neurons to retrieval-related activity (x-axis) and pup odor (y-axis of **d** ) or the non-social reward (y-axis of **i** ). Colored dots indicate the cells that showed a significant response (n = 384 cells from N = 7 mice in **d** ; n = 344 cells from N = 6 mice in **i** ). Numbers in parentheses ( _x_ , _y_ , _z_ ) indicate: _x_ , the number of cells responsive to pup odor ( **d** ) or the non-social reward ( **i** ); _y_ , the number of dually responsive cells; and _z_ , the number of cells singly responsive to one of the behavioural categories. **e** , **j** , Venn plots showing the number of cells responding to one of the behavioural categories of pup retrieval and pup odor ( **e** ) or the non-social reward ( **j** ). 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [362 x 642] intentionally omitted <==**

**Fig. 3 Presynaptic landscape of OFC[Rbp4] neurons. a** , Schematic of the experimental paradigm (left) and a representative fluorescent micrograph from the injection site (right). Scale bar, 1 mm. **b** , Number 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

of starter cells in the frontal cortical areas; most are located in the OFC. **c** , Fraction of starter cells within the OFC. **d** , Three-dimensional illustration of the anatomical distribution of the starter (left) and rabies-GFP-labeled input cells (middle and right). Data from four animals are superimposed on a common brain atlas. **e** , Fraction of input cells in different regions of the brain. A large fraction of input cells is located in the ipsi and contra pan-cortex and pan-thalamus (N = 4 mice). **f** , Top left: Representative micrograph showing input neurons located in the mediodorsal (MD) and submedius thalamus (SMT). Scale bar, 1 mm. Top right: Schematic of detected input cells and annotated thalamic regions using AMaSiNe. Bottom: Quantification of the fraction of input cells in different thalamic regions. **g** , Schematic map of selected long-range monosynaptic inputs into the OFC[Rbp4] neurons. The colors indicate the proportion of each region out of the total inputs. Injection sites are shown by a green circle. **h** , Representative micrograph of input neurons (anti-GFP, green) in the thalamus stained with a _Tnnt1_ RNA probe. Scale bar, 50  m. In total, 54 of 65 GFP+ cells were _Tnnt1_ -positive. **i** , Schematic of the experimental design for axonal tracing. **j** , Representative micrographs of the injection site (left) showing mCherry expression in the SMT (top) and MD (bottom). **k** , Quantification of the axonal projection density in SMT[Tnnt1] and MD[Tnnt1] projection targets (N = 3 mice). Error bars, SEM. For abbreviations, see Supplementary Table 1. 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [474 x 378] intentionally omitted <==**

**Fig. 4 SMT functionally shapes pup-retrieval representations in the OFC[Rbp4] neurons. a** , Top: Schematic of head-attached microendoscope and GRIN lens implantation above the SMT. Bottom: Representative images showing the GRIN lens tract and expression of GCaMP6s in _Tnnt1-Cre; Ai162_ mice. Scale bar, 200  m. **b** , Quantification of the performance of pup retrieval during the imaging sessions. *, p < 0.05 by post hoc Tukey’s HSD test after a significant Kruskal–Wallis test (N = 5 mice). **c** , Pie charts showing the fractions of elevated (red) and suppressed (blue) responses during pup retrieval. CV2 shows the decreased number of fractions in both elevated and suppressed responses. *, p < 0.05 by the chi-squared test for equality of proportions. ns, not significant. **d** , Fraction of cells that showed elevated (left) or suppressed (right) responses to one of the behavioural categories of pup retrieval. **e** , Activity heat map as in Fig. 1j. **f** , Averaged activity traces of cells that responded significantly to anticipatory, interaction, the onset of retrieval, and completion of retrieval. The numbers in parentheses indicate the number of cells that exhibited elevated or suppressed (sup) responses. **g** , Quantification of the averaged response. *, p < 0.05 by a post hoc Tukey’s HSD test after a significant Kruskal–Wallis test; ns, not significant. Error bars, SEM. **h** , Schematic of the experimental design. **i** , Activity heat map before (left) and after (right) CNO. **j** , Quantification of averaged response before and after CNO. **, p < 0.01 and *, p < 0.05 by the Wilcoxon signed-rank test. ns, not significant. The number of data sets is indicated in the panel. 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [369 x 555] intentionally omitted <==**

**Fig. 5 OFC facilitates pup retrieval-related activities of VTA[DA] neurons. a** , Schematic of the experimental design. AAV1 _CaMKII-stGtACR2-fusionRed_ or AAV1 _CaMKII-YFP_ was injected into the bilateral OFC of the virgin _DAT-Cre; Ai162_ mice. **b** , Schematic of the experimental timeline, including four imaging sessions (duration: 2.5 min). The first and third sessions are with light (blue), and the second and fourth sessions are without light as internal controls. Scale bar, 1 mm. **c** , Representative coronal sections showing optic fiber tract and expression of stGtACR2 (left), YFP (middle), and GCaMP6s (right) from _DAT-Cre; Ai162_ mice. Scale bar, 50  m. **d** , Left: Representative 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

coronal section showing _DAT_ mRNA (magenta) and GCaMP6s (anti-GFP, green) in _DAT-Cre; Ai162_ mice. Right: Quantification of specificity ( _DAT_ /GCaMP6s) and efficiency (GCaMP6s/ _DAT_ ) (N = 3 mice). **e** , Trial-averaged activities (top) and the corresponding activity heat maps of individual trials (bottom) of VTA[DA] neurons during pup retrieval with and without light-based inactivation of the OFC in a CV2 mouse. 0 indicates the timing of the interaction with a pup followed by retrieval. **f** , Z-scored peri-event time histograms (PETHs) with light (blue) and without light (black) per group. The number of animals is indicated in the panel. **g** , Quantification of averaged PETHs. Light inactivation of the OFC with stGtACR2 reduced the population activity of VTA[DA] neurons at the CV1 and CV2 stages. *, p < 0.05 and **, p < 0.01 by the Wilcoxon signed-rank test. ns, not significant. **h** , Quantification of the performance of pup retrieval during the photometry imaging sessions. The number of animals is indicated in the panel. *, p < 0.05 by the Wilcoxon signed-rank test. ns, not significant. 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

## **Supplementary Figures** 

**==> picture [312 x 369] intentionally omitted <==**

**Extended Data Fig. 1 Necessity of OFC[Rbp4] neurons for effective learning of maternal behaviours, related to Fig. 1. a** , Schematic of the experimental design. AAV1 _EF1a-FLEx-taCasp3-TEVp_ was injected unilaterally into the ventral and lateral OFC (vOFC and lOFC, respectively) of _Rbp4-Cre; Ai162_ mice. **b** , Representative coronal section showing ablation of cells only in the taCasp3-injected hemisphere. Scale bar, 1 mm. **c** , Quantification of the number of GCaMP6s-expressing cells in the OFC. Introducing taCasp3 reduced the number of GCaMP6s-expressing cells in the OFC. **, p < 0.01 by the Wilcoxon signed-rank test (N = 5 mice). Error bars, standard error of the mean (SEM). **d** , Schematic of the experimental design. AAV1 _EF1a-FLEx-taCasp3-TEVp_ or AAV1 _EF1a-DIO-YFP_ was injected into the bilateral OFC of virgin _Rbp4-Cre_ mice more than 3 weeks before the behaviour assay. **e** , Proportion of animals that retrieved six pups within 4 min. A significant delay was observed in taCasp3-injected animals (N = 10 mice each for the taCasp3 and control groups, *, p < 0.05 by the Fisher’s exact test). **f** – **h** , Time to the first interaction ( **f** ), time to the first retrieval ( **g** ), and the number of retrieved pups ( **h** ). ns, not significant and *, p < 0.05 by the Wilcoxon signed-rank test (N = 10 for each group). Error bars, SEM. **i** , Cumulative probability of pup retrieval. **, p < 0.01 by KolmogorovSmirnov test. 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [406 x 678] intentionally omitted <==**

**Extended Data Fig. 2 Longitudinal tracking across days of imaging and more data of their** 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**neural representations of pup retrieval, related to Fig. 1. a** , Example of a spatial map of cells that responded during pup retrieval from one CV2 female mouse. Identified cells (region of interest [ROI]) are drawn with a black line. Colors within the ROI correspond to the elevated-response categories described in panel C: gray, anticipatory; blue, interaction; red, onset of retrieval; and green, completion. A, anterior, M, medial. Scale bar, 100  m. **b** , Examples of Ca[2+] traces of cells responding to anticipatory, interaction, the onset of retrieval, or completion. Indicated cell IDs correspond to the numbers in panel A. **c** , The trial-average activity (top) of significantly responding individual cells (cell IDs are shown at the top) to indicated behavioural categories, exhibiting the normalized (norm)  F/F values to the maximum  F/F within the individual. Colored heat maps at the bottom show the corresponding single trials. **d** , **f** , Longitudinal tracking of the same cells across different maternality stages. Activity heat map representations showing normalized and averaged single-cell responses between CV1 and CV2 ( **d** ), and CV2 and LM ( **f** ). Cells are sorted by the time of their maximum responses on CV1 ( **d** ) or CV2 ( **f** ), with 0 indicating the timing of the interaction with a pup followed by retrieval. **e** , **g** , Quantification of averaged response comparing between CV1 and CV2, and CV2 and LM. *, p < 0.05 by the Wilcoxon signed-rank test. ns, not significant. The number of data sets is indicated in the panel. **h** , Activity heat map representations showing normalized and averaged singlecell responses during the trials with pup retrieval (left, the same data as Fig. 1j) and interaction trials that were not followed by pup retrieval (right, “Non-retrieval”). 0 indicates the timing of the interaction with a pup. To avoid a low statistical power, data of cells from the mice that performed seven or fewer non-retrieval interaction trials were excluded (shown in dark blue rows). **i** , **j** , Mean response during non-retrieval trials (x-axis) of individual OFC[Rbp4] neurons that exhibited a significant response during the retrieval trials (y-axis). Black dots indicate the dual responders, and colored dots indicate the mean value (± SEM) of the averaged response. Numbers in parentheses indicate the fraction of dual responders. For the onset-responding cells, a 1.0–3.5 s time window relative to the onset of interaction was used for the calculation. 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [423 x 371] intentionally omitted <==**

**Extended Data Fig. 3 Representation of pup retrieval emerges by activating OT neurons in the PVN of virgin female mice, related to Fig. 1. a** , Schematics of the experimental design. AAV5 _OTphM3D(Gq)-Myc_ was injected into the bilateral PVN of virgin _Rbp4-Cre; Ai162_ mice. **b** , Schematic of the experimental timeline. **c** , Representative coronal sections showing the tract of the GRIN lens in the OFC (left) and expression of Gq-Myc in the PVN (right). Scale bars, 500  m. **d** , Quantification of the performance of pup retrieval during the imaging sessions. Left: Number of pup retrievals. Middle: Success rate. Right: Failure rate. *, p < 0.05 by a post hoc Tukey’s HSD test after a significant Kruskal– Wallis test (N = 4 mice). Error bars, SEM. **e** , Pie charts showing the fraction of elevated (red) and suppressed (blue) responses during pup retrieval. **f** , Fraction of cells that showed elevated (left) or suppressed (right) responses to one of the behavioural categories of pup retrieval. **g** , Activity heat map representations showing normalized and averaged single-cell responses during pup retrieval. 0 indicates the timing of the interaction with a pup followed by retrieval. **h** , **i** , Averaged activity traces of significantly responsive cells to anticipatory, interaction, the onset of retrieval, and completion of retrieval. The number of data sets is indicated in the panel. 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [330 x 434] intentionally omitted <==**

**Extended Data Fig. 4 Whole-brain-wide presynaptic distributions for OFC[Rbp4] neurons, related to Fig. 3.** Quantification of the proportion of rabies-GFP-labeled input cells in the cortical and subcortical areas (N = 4 mice). Error bars, SEM. 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [455 x 377] intentionally omitted <==**

**Extended Data Fig. 5 Generation of** _**Tnnt1-Cre**_ **mouse, related to Fig.3. a** , Top: Schematic of _Tnnt1iCre_ knock-in allele. Bottom: Representative micrographs of a _Tnnt1-Cre; Ai162_ mouse (left) and high-magnification micrographs showing reporter expression in the SMT and MD (right). Scale bar, 100  m. **b** , Top: Schematic of the primer design. Bottom: Representative gel image of electrophoresis examining the iCre allele and negative control (wild-type animal). **c** , Representative coronal sections showing the expression of _Tnnt1_ mRNA (magenta) and GCaMP6s (anti-GFP, green) in the MD (top) and SMT (bottom) of a _Tnnt1-Cre; Ai162_ mouse. **d** , **e** , Quantification of specificity ( _Tnnt1_ +/GCaMP6s+ in **d** , and _vGluT2_ +/GCaMP6s+ in **e** ) and efficiency (GCaMP6s+/ _Tnnt1_ + in **d** , and GCaMP6s+/ _vGluT2_ + in **e** ) (N = 6 hemispheres). Notably, GCaMP6s is faithfully expressed by _Tnnt1_ + neurons, while only a subset of _Tnnt1_ + neurons express GCaMP6s. Although the exact reason for this suboptimal efficiency is unknown, it might reflect the stochastic inactivation of the _tetracycline response element_ promoter in the _Ai162_ line. Of note, we observed a similar subset expression in OT neurons by _OT-Cre_ ; _Ai162_ mice[51] . **f** , **g** , Top: Schematic of the virus injection strategy. AAV5 _CAGFLEx-TC[b]_ was injected into the left SMT ( **f** ) or MD ( **g** ). Middle left: Schematic of detected soma and the annotated thalamic regions using AMaSiNe. Middle right: Representative coronal section of the injection site. Scale bar, 1 mm. Bottom: Quantification of the fraction of mCherry+ cells in the thalamic areas (N = 3 mice). 

22 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [486 x 387] intentionally omitted <==**

**Extended Data Fig. 6 MD[Tnnt1] neurons respond to pup retrieval yet do not affect pup-retrieval representations in the OFC[Rbp4] neurons related to Fig. 4. a** , Top: Schematic of head-attached microendoscope and GRIN lens implantation above the SMT. Bottom: Representative images showing the GRIN lens tract and expression of GCaMP6s in _Tnnt1-Cre; Ai162_ mice. Scale bar, 200  m. **b** , Quantification of the performance of pup retrieval during the imaging sessions. Top: Number of retrievals. Bottom: Success rate calculated as the number of retrievals over the number of interactions with pups. *, p < 0.05 by post hoc Tukey’s HSD test after a significant Kruskal–Wallis test (N = 5 mice). **c** , Pie charts showing the fractions of elevated (red) and suppressed (blue) responses during pup retrieval. ns, not significant by the chi-squared test for equality of proportions. Of note, we omitted the NV conditions from the analysis because only a few NV mice performed pup retrieval (see **b** ). **d** , Fraction of cells that showed elevated (left) or suppressed (right) responses to one of the behavioural categories of pup retrieval. **e** , Activity heat map representations as in Fig. 4e. **f** , Averaged activity traces of cells that responded significantly to anticipatory, interaction, the onset of retrieval, and completion of retrieval. The numbers in parentheses indicate the number of cells that exhibited elevated or suppressed (sup) responses. **g** , Quantification of the averaged response. *, p < 0.05 by a post hoc Tukey’s HSD test after a significant Kruskal–Wallis test; ns, not significant. Error bars, SEM. **h** , 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

Schematic of the virus injection strategy. **i** , Activity heat map before (left) and after (right) CNO. **j** , Quantification of averaged response before and after CNO. **, p < 0.01 by the Wilcoxon signed-rank test. ns, not significant. The number of data sets is indicated in the panel. 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [282 x 313] intentionally omitted <==**

## **Extended Data Fig. 7 Neural representation of non-retrieval trials in the SMT and MD, related** 

**to Fig. 4. a** , **c** , Activity heat map representations as in Fig. 1j during pup retrieval (left, same data as Fig. 4e and Extended Data Fig. 6e, respectively) and non-retrieval trials (right). To avoid a low statistical power, data of cells from the mice that performed seven or fewer non-retrieval interaction trials were excluded (shown in dark blue rows). **b** , **d** , Mean responses during the non-retrieval trials (x-axis) of individual SMT[Tnnt1] (panel b) and MD[Tnnt1] (panel d) neurons that exhibited a significant response during the retrieval trials (y-axis). Black dots indicate the dual responders, and colored dots indicate the mean value (± SEM) of the averaged response. Numbers in parentheses indicate the fraction of dual responders. For the onset-responding cells, a 1.0–3.5 sec time window relative to the onset of interaction was used for the calculation. 

25 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [288 x 334] intentionally omitted <==**

## **Extended Data Fig. 8 A control experiment for the manipulation of thalamic activities, related to** 

**Fig. 4. a** , Timeline of the experimental paradigm. Two 6-min imaging sessions were performed before and after CNO injection. **b** , Schematic of the virus injection strategy. AAV8 _hSyn-fDIO-mCherry_ was injected into the MD or SMT (N = 3 and 2 mice, respectively) instead of AAV8 _hSyn-fDIO-hM4DimCherry_ in Extended Data Fig. 6h. **c** , Activity heat map representations showing normalized and averaged single-cell responses during pup retrieval before (left) and after (right) CNO. 0 indicates the timing of the interaction with a pup followed by retrieval. **d** , Quantification of averaged response before and after CNO. ns, not significant by the Wilcoxon signed-rank test. The number of data sets is indicated in the panel. 

26 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [428 x 468] intentionally omitted <==**

**Extended Data Fig. 9 SMT[→OFC] or MD[→OFC] neurons do not alter the performance of pup retrieval, related to Fig. 4. a** , **b** , Left: Schematic of the virus injection strategy. AAV8 _hSyn-fDIO-GimCherry_ was injected into the bilateral SMT ( **a** ) or MD ( **b** ). AAVrg _EF1a-FlpO_ was injected into the bilateral OFC. Middle: Representative coronal sections showing injection site into the SMT ( **a** ) or MD ( **b** ). Scale bar, 1 mm. Right: Number of mCherry-expressing cells in the thalamus (N = 4 mice in **a** and N = 5 mice in **b** ). **c** – **e** , Top: Virus injection strategy. Bottom: Quantification of the performance of pup retrieval during the imaging sessions. Left: Number of pup retrievals. Middle: Success rate (number of retrievals over the number of interactions with pups). Right: Failure rate. ns, nonsignificant by the Mann–Whitney _U_ test. Error bars, SEM. 

27 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [372 x 407] intentionally omitted <==**

**Extended Data Fig. 10. OFC[Rbp4] neurons project axons to the thalamus and VTA, and more data on pup-retrieval-related activities of VTA[DA] neurons, related to Fig. 5. a** , Top: Schematic of the virus injection strategy. A mixture of AAVrg _CAG-FLEx-FlpO_ and AAV9 _hSyn-fDIO-mGFP_ was injected into the left OFC. Bottom: Representative coronal section showing the injection site. **b** , Representative coronal section showing axonal projections to the thalamic areas. **c** , Representative coronal section showing axonal projections to the midbrain. Scale bars, 1 mm. For abbreviations, see Table 1. **d** , Normalized mean response of VTA[DA] during pup retrieval across different experimental days. NV is omitted from the data analysis because no animal showed pup retrieval at the NV stage. Response magnitude is quantified as the mean of the averaged Z scored response trace over a 2.5 s window relative to the onset of interaction. Then the value is normalized per animal relative to the light-off condition of CV1 after the subtraction by the baseline, which is calculated using a 2 s window prior to the onset of interaction. Left: Pooled data from YFP- (Control) and stGtACR-injected mice, showing the relative response magnitude is decreased as the maternality stages progress. *, p < 0.05 by a post hoc Tukey’s HSD test after a significant one-way ANOVA (N = 13 mice). Middle: Data from YFP-injected animals with (blue) or without (black) light (N = 6 mice). Right: Data from stGtACR2- 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

injected animals with (blue) or without (black) light (N = 7 mice). **e** , Scatterplots and Spearman correlation of averaged Z scored responses and the number of pup retrieval Data from CV1 and CV2 from GtACR-injected animals with (blue) or without (black) light (N = 8 mice). 

29 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**Supplementary Table 1. List of abbreviations, related to Fig. 3.** 

**==> picture [397 x 667] intentionally omitted <==**

**----- Start of picture text -----**<br>
Acronym  Name<br>AAA  anterior amygdalar area<br>ACC  anterior cingulate cortex<br>AD  anterodorsal nucleus<br>AI  agranular insular cortex<br>AM  anteromedial nucleus<br>ATN  anterior group of the dorsal thalamus<br>AV  anteroventral nucleus<br>BLA  basolateral amygdalar nucleus<br>BMA  basomedial amygdalar nucleus<br>CA1  hippocampus CA1<br>CEA  central amygdalar nucleus<br>CL  central lateral nucleus<br>CLA  claustrum<br>CM  central medial nucleus<br>dStr  dorsal striatum<br>EPI  epithalamus<br>IAD  interanterodorsal nucleus<br>IAM  interanteromedial nucleus<br>IL  infralimbic cortex<br>ILM  intralaminar nuclei of the dorsal thalamus<br>IMD  intermediodorsal nucleus<br>LA  lateral amygdalar nucleus<br>LD  lateral dorsal nucleus<br>LH  lateral habenula<br>M1  primary motor cortex<br>M2  secondary motor cortex<br>MD  mediodorsal nucleus<br>MED  medial group of the dorsal thalamus<br>MH  medial habenula<br>MTN  midline group of the dorsal thalamus<br>NAC  nucleus accumbens<br>OT  olfactory tubercle<br>PCN  paracentral nucleus<br>PF  parafascicular nucleus<br>Pir  piriform cortex<br>**----- End of picture text -----**<br>


30 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

**==> picture [397 x 334] intentionally omitted <==**

**----- Start of picture text -----**<br>
PL  prelimbic cortex<br>PO  posterior complex of the thalamus<br>PR  perieunensis nucleus<br>PT  parataenial nucleus<br>PVT  paraventricular nucleus<br>RE  nucleus of reuniens<br>RH  rhomboid nucleus<br>RSP  retrosplenial cortex<br>RTN  reticular nucleus<br>S1  primary somatosensory cortex<br>S2  secondary somatosensory cortex<br>SI  substantia innominata<br>SMT  submedial nucleus of the thalamus<br>VAL  ventral anterior-lateral complex of the thalamus<br>VENT  ventral group of the dorsal thalamus<br>VM  ventral medial nucleus<br>VPM  ventral posteromedial nucleus<br>Xi  xiphoid thalamic nucleus<br>**----- End of picture text -----**<br>


31 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

## **References** 

- 1 Dulac, C., O'Connell, L. A. & Wu, Z. Neural control of maternal and paternal behaviors. Science 345 , 765-770, doi:10.1126/science.1253291 (2014). 

- 2 Insel, T. R. & Young, L. J. The neurobiology of attachment. Nat Rev Neurosci 2 , 129-136, doi:10.1038/35053579 (2001). 

- 3 Carcea, I. et al. Oxytocin neurons enable social transmission of maternal behaviour. Nature, doi:10.1038/s41586-021-03814-7 (2021). 

- 4 Numan, M. & Young, L. J. Neural mechanisms of mother-infant bonding and pair bonding: Similarities, differences, and broader implications. Horm Behav 77 , 98112, doi:10.1016/j.yhbeh.2015.05.015 (2016). 

- 5 Fang, Y. Y., Yamaguchi, T., Song, S. C., Tritsch, N. X. & Lin, D. A Hypothalamic Midbrain Pathway Essential for Driving Maternal Behaviors. Neuron 98 , 192-207 e110, doi:10.1016/j.neuron.2018.02.019 (2018). 

- 6 Xie, Y., Huang, L., Corona, A., Pagliaro, A. H. & Shea, S. D. A dopaminergic reward prediction error signal shapes maternal behavior in mice. Neuron, doi:10.1016/j.neuron.2022.11.019 (2022). 

- 7 Wu, Z., Autry, A. E., Bergan, J. F., Watabe-Uchida, M. & Dulac, C. G. Galanin neurons in the medial preoptic area govern parental behaviour. Nature 509 , 325330, doi:10.1038/nature13307 (2014). 

- 8 Kohl, J. et al. Functional circuit architecture underlying parental behaviour. Nature 556 , 326-331, doi:10.1038/s41586-018-0027-0 (2018). 

- 9 Moffitt, J. R. et al. Molecular, spatial, and functional single-cell profiling of the hypothalamic preoptic region. Science 362 , doi:10.1126/science.aau5324 (2018). 

- 10 Tsuneoka, Y. et al. Functional, anatomical, and neurochemical differentiation of medial preoptic area subregions in relation to maternal behavior in the mouse. J Comp Neurol 521 , 1633-1663, doi:10.1002/cne.23251 (2013). 

- 11 Yoshihara, C. et al. Calcitonin receptor signaling in the medial preoptic area enables risk-taking maternal care. Cell Rep 35 , 109204, doi:doi: 10.1016/j.celrep.2021.109204. (2021). 

- 12 Febo, M., Felix-Ortiz, A. C. & Johnson, T. R. Inactivation or inhibition of neuronal activity in the medial prefrontal cortex largely reduces pup retrieval and grouping in maternal rats. Brain Res 1325 , 77-88, doi:10.1016/j.brainres.2010.02.027 (2010). 

- 13 Tasaka, G. I. et al. The Temporal Association Cortex Plays a Key Role in AuditoryDriven Maternal Plasticity. Neuron 107 , 566-579 e567, doi:10.1016/j.neuron.2020.05.004 (2020). 

- 14 Parsons, C. E. et al. Duration of motherhood has incremental effects on mothers' neural processing of infant vocal cues: a neuroimaging study of women. Sci Rep 7 , 1727, doi:10.1038/s41598-017-01776-3 (2017). 

32 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

- 15 Noriuchi, M., Kikuchi, Y. & Senoo, A. The functional neuroanatomy of maternal love: mother's response to infant's attachment behaviors. Biol Psychiatry 63 , 415423, doi:10.1016/j.biopsych.2007.05.018 (2008). 

- 16 DeNardo, L. A., Berns, D. S., DeLoach, K. & Luo, L. Connectivity of mouse somatosensory and prefrontal cortex examined with trans-synaptic tracing. Nat Neurosci 18 , 1687-1697, doi:10.1038/nn.4131 (2015). 

- 17 Lui, J. H. et al. Differential encoding in prefrontal cortex projection neuron classes across cognitive tasks. Cell 184 , 489-506 e426, doi:10.1016/j.cell.2020.11.046 (2021). 

- 18 Yang, C. F. et al. Sexually dimorphic neurons in the ventromedial hypothalamus govern mating in both sexes and aggression in males. Cell 153 , 896-909, doi:10.1016/j.cell.2013.04.017 (2013). 

- 19 Cohen, L., Rothschild, G. & Mizrahi, A. Multisensory integration of natural odors and sounds in the auditory cortex. Neuron 72 , 357-369, doi:10.1016/j.neuron.2011.08.019 (2011). 

- 20 Ghosh, K. K. et al. Miniaturized integration of a fluorescence microscope. Nat Methods 8 , 871-878, doi:10.1038/nmeth.1694 (2011). 

- 21 Daigle, T. L. et al. A Suite of Transgenic Driver and Reporter Mouse Lines with Enhanced Brain-Cell-Type Targeting and Functionality. Cell 174 , 465-480 e422, doi:10.1016/j.cell.2018.06.035 (2018). 

- 22 Gong, S. et al. Targeting Cre recombinase to specific neuron populations with bacterial artificial chromosome constructs. J Neurosci 27 , 9817-9823, doi:10.1523/JNEUROSCI.2707-07.2007 (2007). 

- 23 Inada, K. et al. Plasticity of neural connections underlying oxytocin-mediated parental behaviors of male mice. Neuron, doi:10.1016/j.neuron.2022.03.033 (2022). 

- 24 Marlin, B. J., Mitre, M., D'Amour J, A., Chao, M. V. & Froemke, R. C. Oxytocin enables maternal behaviour by balancing cortical inhibition. Nature 520 , 499-504, doi:10.1038/nature14402 (2015). 

- 25 Levy, F., Keller, M. & Poindron, P. Olfactory regulation of maternal behavior in mammals. Horm Behav 46 , 284-302, doi:10.1016/j.yhbeh.2004.02.005 (2004). 

- 26 Miyamichi, K. et al. Dissecting local circuits: parvalbumin interneurons underlie broad feedback control of olfactory bulb output. Neuron 80 , 1232-1245, doi:10.1016/j.neuron.2013.08.027 (2013). 

- 27 Song, J. H. et al. Precise Mapping of Single Neurons by Calibrated 3D Reconstruction of Brain Slices Reveals Topographic Projection in Mouse Visual Cortex. Cell Rep 31 , 107682, doi:10.1016/j.celrep.2020.107682 (2020). 

- 28 Phillips, J. W. et al. A repeated molecular architecture across thalamic pathways. Nat Neurosci 22 , 1925-1935, doi:10.1038/s41593-019-0483-3 (2019). 

33 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

- 29 Beier, K. T. et al. Circuit Architecture of VTA Dopamine Neurons Revealed by Systematic Input-Output Mapping. Cell 162 , 622-634, doi:10.1016/j.cell.2015.07.015 (2015). 

- 30 Backman, C. M. et al. Characterization of a mouse strain expressing Cre recombinase from the 3' untranslated region of the dopamine transporter locus. Genesis 44 , 383-390, doi:10.1002/dvg.20228 (2006). 

- 31 Wallis, J. D. Cross-species studies of orbitofrontal cortex and value-based decisionmaking. Nat Neurosci 15 , 13-19, doi:10.1038/nn.2956 (2011). 

- 32 Stalnaker, T. A., Cooch, N. K. & Schoenbaum, G. What the orbitofrontal cortex does not do. Nat Neurosci 18 , 620-627, doi:10.1038/nn.3982 (2015). 

- 33 Izquierdo, A. Functional Heterogeneity within Rat Orbitofrontal Cortex in Reward Learning and Decision Making. J Neurosci 37 , 10529-10540, doi:10.1523/JNEUROSCI.1678-17.2017 (2017). 

- 34 Kingsbury, L. et al. Cortical Representations of Conspecific Sex Shape Social Behavior. Neuron, doi:10.1016/j.neuron.2020.06.020 (2020). 

- 35 Zhou, T. et al. History of winning remodels thalamo-PFC circuit to reinforce social dominance. Science 357 , 162-168, doi:10.1126/science.aak9726 PMID - 28706064 (2017). 

- 36 Padilla-Coreano, N. et al. Cortical ensembles orchestrate social competition through hypothalamic outputs. Nature 603 , 667-671, doi:10.1038/s41586-02204507-5 PMID - 35296862 (2022). 

- 37 Roy, D. S., Zhang, Y., Halassa, M. M. & Feng, G. Thalamic subnetworks as units of function. Nat Neurosci 25 , 140-153, doi:10.1038/s41593-021-00996-1 (2022). 

- 38 Kuramoto, E. et al. Individual mediodorsal thalamic neurons project to multiple areas of the rat prefrontal cortex: A single neuron-tracing study using virus vectors. J Comp Neurol 525 , 166-185, doi:10.1002/cne.24054 (2017). 

- 39 Murphy, M. J. M. & Deutch, A. Y. Organization of afferents to the orbitofrontal cortex in the rat. J Comp Neurol 526 , 1498-1526, doi:10.1002/cne.24424 (2018). 

- 40 Barreiros, I. V., Ishii, H., Walton, M. E. & Panayi, M. C. Defining an orbitofrontal compass: Functional and anatomical heterogeneity across anterior-posterior and medial-lateral axes. Behav Neurosci 135 , 165-173, doi:10.1037/bne0000442 (2021). 

- 41 Alcaraz, F. et al. Flexible Use of Predictive Cues beyond the Orbitofrontal Cortex: Role of the Submedius Thalamic Nucleus. J Neurosci 35 , 13183-13193, doi:10.1523/JNEUROSCI.1237-15.2015 (2015). 

- 42 Fresno, V., Parkes, S. L., Faugere, A., Coutureau, E. & Wolff, M. A thalamocortical circuit for updating action-outcome associations. Elife 8 , doi:10.7554/eLife.46187 (2019). 

- 43 Guo, Z. V. et al. Maintenance of persistent activity in a frontal thalamocortical loop. 

34 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

Nature 545 , 181-186, doi:10.1038/nature22324 (2017). 

- 44 Inagaki, H. K. et al. A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement. Cell 185 , 1065-1081 e1023, doi:10.1016/j.cell.2022.02.006 (2022). 

- 45 Numan, M., Stolzenberg, D. S., Dellevigne, A. A., Correnti, C. M. & Numan, M. J. Temporary inactivation of ventral tegmental area neurons with either muscimol or baclofen reversibly disrupts maternal behavior in rats through different underlying mechanisms. Behav Neurosci 123 , 740-751, doi:10.1037/a0016204 (2009). 

- 46 Watabe-Uchida, M., Zhu, L., Ogawa, S. K., Vamanrao, A. & Uchida, N. Wholebrain mapping of direct inputs to midbrain dopamine neurons. Neuron 74 , 858873, doi:10.1016/j.neuron.2012.03.017 (2012). 

- 47 Nakajima, M., Schmitt, L. I. & Halassa, M. M. Prefrontal Cortex Regulates Sensory Filtering through a Basal Ganglia-to-Thalamus Pathway. Neuron 103 , 445-458 e410, doi:10.1016/j.neuron.2019.05.026 (2019). 

- 48 Schwarz, L. A. et al. Viral-genetic tracing of the input-output organization of a central noradrenaline circuit. Nature 524 , 88-92, doi:10.1038/nature14600 (2015). 

- 49 Watabe-Uchida, M. & Uchida, N. Multiple Dopamine Systems: Weal and Woe of Dopamine. Cold Spring Harb Symp Quant Biol 83 , 83-95, doi:10.1101/sqb.2018.83.037648 (2018). 

- 50 Engelhard, B. et al. Specialized coding of sensory, motor and cognitive variables in VTA dopamine neurons. Nature 570 , 509-513, doi:10.1038/s41586-019-1261-9 (2019). 

## **METHOD** 

## **Animals** 

All animals were housed under a regular 12-h dark/light cycle with _ad libitum_ access to food and water. Wild-type FVB mice were purchased from CLEA Japan, Inc. (Tokyo, Japan) for backcrossing. _DATCre_ (Jax# 006660) and _Ai162_ ( _TIT2L-GC6s-ICL-tTA2_ , Jax#031562) were purchased from the Jackson Laboratory. _Rbp4-Cre_ mice were originally obtained from the Mutant Mouse Regional Resource Center. _Tnnt1-Cre_ mice were generated as detailed below (background strain C57BL/6). We used the F1 hybrid of C57BL/6 and FVB strain for all experiments. _Rbp4-Cre_ heterozygous female mice (age 2–5 months) were used for ablation experiments using taCasp3 and rabies tracing experiments. _Rbp4Cre; Ai162_ double heterozygous female mice (age 2–5 months) were used for _in vivo_ microendoscopic imaging of the OFC. _DAT-Cre; Ai162_ double heterozygous female mice (age 2–5 months) were used for the fiber photometry experiments. _Tnnt1-Cre; Ai162_ double heterozygous female mice (age 2–5 months) were used for _in vivo_ microendoscopic imaging of the thalamic nuclei. _Tnnt1-Cre_ 

35 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

heterozygous female mice (age 2–5 months) were used for the anterograde tracing experiments. 

## **Generation of the** _**Tnnt1-Cre**_ **line** 

The _Tnnt1-Cre_ line (Accession No. CDB0152E, listed in https://large.riken.jp/distribution/mutantlist.html) was generated by CRISPR/Cas9-mediated knock-in in zygotes, as previously described[52] . The donor vector consisting of _T2A-iCre_ was inserted just before the stop codon of _Tnnt1_ . The guide RNA (gRNA) sites were designed by using CRISPRdirect[53] to target upstream and downstream locations of the stop codon (Extended Data Fig. 5a). For microinjection, a mixture of two CRISPR RNAs (crRNAs) (50 ng/  L), trans-activating crRNA (tracrRNA) (200 ng/  L), donor vector (10 ng/  L), and Cas9 protein (100 ng/  L) was injected into the pronucleus of a C57BL/6 one-cell stage zygote. As a result, 72 F0 founder mice were obtained from 227 injected zygotes, seven of which were iCrepositive as identified by PCR and sequencing. The line was established by one male that harbored a targeted sequence identified by PCR and sequencing. Genotyping PCR was performed using the following primers: Tnnt1-iCre-F: 5’-GGTGGGTATTTGGTGGACTTCCTG, Tnnt1-iCre-R: 5’GATGGCTCTCCCAGGCAGTATG, and iCre-F: 5’-TACCAAGCTGGTGGAGAGATGGATC, as shown in Figure S4B. For the sequence analysis, we designed the following primers: 3’-junc-R: 5’AGGTCATGTCCTGGCAGTCTCAGTCC, and 5’-junc-F: 5’GCCGCTGGAAGGGCTCTGGCGAA. The PCR products from using the primers Tnnt1-iCre-F and 3’ junc-R, and 5’ junc-F and Tnnt1-iCre-R were subcloned into the pCR Blunt II TOPO vector for each (Zero Blunt TOPO PCR Cloning Kit, ThermoFisher) and sequenced using M13-Foward and M13-Reverse primers. Tnnt1 crRNA (5’- CUG GAA GUG AGA CUG CCA GGg uuu uag agc uau gcu guu uug), PITCh 3 crRNA (5’-GCA UCG UAC GCG UAC GUG UUg uuu uag agc uau gcu guu uug), and tracrRNA (5'-AAA CAG CAU AGC AAG UUA AAA UAA GGC UAG UCC GUU AUC AAC UUG AAA AAG UGG CAC CGA GUC GGU GCU) were purchased from FASMAC (Atsugi, Japan). The germline transmission of the _Tnnt1-iCre_ allele was confirmed by genotyping of F1 mice. Of note, histochemical analysis by _in situ_ hybridization (ISH) also confirmed the consistent expression pattern with the endogenous mRNA expression pattern (Extended Data Fig 5). 

## **Viral preparations** 

The following AAV vectors were generated by UNC viral core using the corresponding plasmids as described in the original literature[26] . The titer of the AAV was estimated by quantitative PCR methods and shown as genome particles (gp) per milliliter. 

AAV serotype 5 _CAG-FLEx-TC[b]_ (9.3  10[12] gp/mL) 

AAV serotype 8 _CAG-FLEx-RG_ (2.8  10[12] gp/mL) 

The following AAV vectors were generated by the UNC viral core, Canadian Neurophotonics Platform viral vector core facility, and Addgene using the corresponding plasmids (Addgene #45580, #27056, #184753, #154867, #177328, #105669, #105622, #171690, and #71761) described in the original 

36 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

literature. 

AAV serotype 1 _EF1a-FLEx-taCasp3-TEVp_ (5.8  10[12] gp/mL) 

AAV serotype 5 _EF1a-DIO-YFP_ (1.3  10[13] gp/mL) AAV serotype 5 _OTp -hM3Dq-Myc_ (2.9  10[12] gp/mL) AAV serotype 8 _hSyn-fDIO-hM4Di-mCherry_ (6.8  10[12] gp/mL) AAV serotype 8 _hSyn-fDIO-mCherry_ (8.9  10[12] gp/mL) 

AAV serotype 1 _CaMK2a-stGtACR2-FusionRed_ (1.3  10[13] gp/mL) AAV serotype 1 _CaMK2a-EYFP_ (1.0  10[13] gp/mL) 

AAV serotype retro _CAG-FLEx-FlpO_ (5.5  10[12] gp/mL) 

AAV serotype 9 _hSyn-FLEx(FRT)-mGFP_ (7.4  10[12] gp/mL) 

Rabies  _G-GFP_ +EnvA was prepared by using B7GG and BHK-EnvA cells (kindly gifted by Ed Callaway) according to the published protocol[54] . The EnvA-pseudotyped RV  _G-GFP_ +EnvA titer was estimated to be 1.0  10[9] infectious particles/mL based on serial dilutions of the virus stock, followed by infection of the HEK293-TVA800 cell line. 

## **Stereotactic injection** 

For targeting AAV or rabies virus into a certain brain region, stereotactic coordinates were first defined for each brain region based on the Allen Brain Atlas[55] . Mice were anesthetized with 65 mg/kg ketamine (Daiichi-Sankyo) and 13 mg/kg xylazine (Sigma-Aldrich) via intraperitoneal injection and head-fixed to the stereotactic equipment (Narishige). For the rabies tracing experiments (Fig. 3 and Extended Data Fig 4), 100 nL of a 1:1 mixture of AAV5 _CAG-FLEx-TC[b]_ and AAV8 _CAG-FLEx-RG_ was injected into the OFC (coordinates relative to the bregma: anterior 2.5 mm, lateral 1.2 mm, depth 1.9 mm from the brain surface) at a speed of 50 nL/min using a UMP3 pump regulated by Micro-4 (World Precision Instruments), followed by 200 nL of rabies  _G-GFP_ +EnvA injection 2 weeks later. To minimize the starter cells along the injection trajectories, we injected rabies by tilting the injector (coordinates relative to the bregma: anterior 2.5 mm, lateral 0.5 mm, depth 1.9 mm with tilting 15  from the vertical). For the anterograde tracing experiments (Fig. 3i–k), 100 nL of AAV5 _CAG-FLEx-TC[b]_ was injected into the unilateral MD or SMT (MD, coordinates relative to the bregma: posterior 0.8 mm, lateral 0.5 mm, depth 3.1 mm from the brain surface; SMT, coordinates relative to the bregma: anterior 0.8 mm, lateral 1.0 mm, depth 4.0 mm from the brain surface with tilting 15  from the vertical to minimize the leakage into the MD). For the pharmacogenetic experiments (Fig. 4 and Extended Data Fig. 6), 200 nL of AAV8 _hSyn-fDIO-hM4Di-mCherry_ or AAV8 _hSyn-fDIO-mCherry_ was injected into the bilateral MD or SMT, and 100 nL of retro-AAV _EF1a-FlpO_ was injected into the bilateral OFC. For the optogenetic experiments with photometry recordings (Fig. 5), 200 nL of AAV1 _CaMK2a-stGtACR2FusionRed_ or AAV1 _CaMK2a-EYFP_ was injected into the bilateral OFC. For the ablation experiments (Extended Data Fig. 1), 200 nL of AAV1 _EF1a-FLEx-taCasp3-TEVp_ was injected into the right hemisphere (Extended Data Fig. 1a–c) or bilateral OFC (Extended Data Fig. 1d–i). To activate OT 

37 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

neurons in the PVN (Extended Data Fig.3), 200 nL of AAV5 _OTp-hM3D(Gq)-Myc_ was injected into the bilateral PVN (coordinates relative to the bregma: anterior –0.5 mm, lateral 0.2 mm, depth 4.4 mm from the brain surface). For anterograde tracing from the OFC (Extended Data Fig. 10a–c), 100 nL of a 1:1 mixture of AAVretro _CAG-FLEx-FlpO_ and AAV9 _hSyn-FLEx(FRT)-mGFP_ was injected into the left OFC. After viral injection, the incision was sutured, and the animal was warmed using a heating pad to facilitate recovery from anesthesia. The animal was then returned to the home cage. 

## **Pup retrieval assay** 

Animals were placed in their home cage with standard wood chip bedding. If the animals were CV1, CV2, or CV3, we took out the co-housed mother and pups and waited for 5–10 min before starting the assay. We first introduced two pups in opposite corners of the nest. If the two pups were retrieved, we placed another two pups in the same corners as before. We repeated until a total of six pups were collected or until a 4-min time-out. Success rate was calculated as the number of retrievals over the number of pup interactions, and failure rate was calculated as the number of incomplete retrievals normalized to the total number of retrievals. 

## _**In vivo**_ **microendoscopic imaging** 

For microendoscopic recording, a ProView GRIN lens (500-  m diameter, 4 mm or 6.1 mm length, Inscopix) insertion was performed (OFC, coordinates relative to the bregma: anterior –2.5 mm, lateral 1.2 mm, depth 1.8 mm from the brain surface, MD, coordinates relative to the bregma: anterior 0.8 mm, lateral 1 mm, depth 3.0 mm from the brain surface with tilting 10  from the vertical; SMT, coordinates relative to the bregma: anterior 0.8 mm, lateral 1.2 mm, depth 4.0 mm from the brain surface with tilting 15  from the vertical). Mice were anesthetized with 65 mg/kg ketamine (DaiichiSankyo) and 13 mg/kg xylazine (Sigma-Aldrich) via intraperitoneal injection and head-fixed to the stereotactic equipment (Narishige). Next, we performed a craniotomy (1 mm diameter round shape) over the lens target area, clearing any remaining bone and overlying dura using fine forceps. We aspirated the brain tissue in 1-, 2-, or 3-mm for the OFC, MD, or SMT, respectively. Then, a GRIN lens was loaded onto the ProView lens holder and attached to Inscopix nVista. This unit was slowly lowered into the brain while we monitored the expression of GCaMP6s through nVista. Once the intended depth was reached and the signals from GCaMP6s were confirmed, we finalized lens placement by permanently gluing the lens with Super-Bond (Sun Medical) and sealing the lens and skull together. In this step, we also glued a metal bar (Narishige, CF-10), which allowed us to attach and detach the microscope easily. For the imaging under the head-fixed condition, we glued an M4 screw (Thorlabs), which connects the animal to a custom-made stage. After the glue was completely hardened, the camera and lens holder were carefully released from the lens, and Kwik-Kast (WPI) was used to protect the exposed lens surface. After more than 3 weeks of recovery, the mice were anesthetized and placed in the stereotaxic equipment again. The focal plane was adjusted until GCaMP6s-labeled cells were in focus, and then a baseplate (Inscopix) was permanently glued with 

38 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

Super-Bond. After more than a week of recovery, we attached the microscope and let the mice explore freely in their home cage for 5–10 min. We performed this habituation session more than twice before the first imaging session. 

We performed microendoscopic imaging using the Inscopix nVista system (Inscopix). We performed imaging without refocusing the microscopes across imaging sessions during the day, whereas the focal plane was adjusted each day before the first imaging session. Before imaging, we attached the microendoscope to the animals while holding the implanted head bar. Images (1080  1080 pixels) were acquired using nVista HD software (Inscopix) at 10 Hz, with LED power of 0.4–1 mW/mm[2] and a gain of 2.0–3.0. Timestamps of the imaging frames, camera, delivery of sucrose water, and olfactory stimuli were collected for alignment using WaveSurfer (https://wavesurfer.janelia.org/). We performed two to three imaging sessions, each lasting for 6 min with a couple minutes of interval between sessions. The imaging data were cropped to 800  700 pixels and exported as .tiff files using the Inscopix Data Processing Software. To identify putative cell bodies for the extraction of neural signals, we used v2 of MIN1PIPE (https://github.com/JinghaoLu/MIN1PIPE[56] ) with a spatial downsampling rate of 2. All traces from identified cells were manually inspected to ensure quality signals and excluded if they had an abnormal shape or overlapped signal from adjacent cells. Relative changes in calcium fluorescence _F_ were calculated by  _F/F0 = (F-F0)/F0_ (where _F0_ is the median fluorescence of the entire trace).  _F/F_ was normalized within each cell. 

To define significant responsive cells, trial-averaged Ca[2+] signals were compared between the behavioural events and a baseline period using the Mann–Whitney _U_ test, with a significance threshold of p < 0.05. Behaviour videos were acquired at 20 Hz using a camera (Imaging source, DMK 33UX174). WaveSurfer was used to generate precise TTL pulses to synchronize behavioural tracking and microendoscopic imaging. The animals that showed eight or more successful pup retrievals were included in the following analysis. In Figs. 1, 4, and Extended Data Fig. 6, female mice in different maternality stages showed a different number of retrieval trials. To normalize the statistical power across different maternality stages, we randomly selected the same number of trials across each animal to determine responsive cells. The p-value was calculated by the mean of p-values based on 10,000 iterated calculations. Because the activity heat maps (Figs. 1j, 4e, and Extended Data Fig. 6e) showed no bimodal elevated or suppressed responses (e.g., elevated responses to both anticipatory and completion stages), we decided to classify cells into one of eight types, either elevated or suppressed in one of four behavioural categories. The following time windows were used for averaging: anticipatory, –1 to 0 s relative to the initiation of interaction; interaction, 0 to +1.5 s after the initiation of interaction; onset, 2 s following the onset of pup retrieval; and completion, 2 s following the completion of retrieval. The time window for the baseline was –1.5 to 0 s relative to each behavioural event. We first assigned elevated responding cells to anticipatory, interaction, onset of retrieval, or completion, in this order. In some cases, we noticed that the baseline fluctuated because of suppressed responses. For example, a cell that showed a suppressed response to the interaction stage could be mistakenly assigned to an elevated responder to onset or completion because of the reduced baseline. 

39 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

In such cases, we retook the baseline –1.5 to 0 s relative to the initiation of interaction to recalculate the significance. Once all cells that showed elevated responses to one of four behavioural categories were assigned, we classified the remainder of the cells if they showed significant suppressed responses to anticipatory, interaction, onset of retrieval, or completion, in this order. 

For longitudinal tracking of the same cells across different days (Extended Data Fig. 2d–g), the spatial footprints of the cell extracted with MIN1PIPE pipeline were processed with CellReg[57] using default parameters (maximum translation of 12 microns, registration threshold P_same of 0.5). CV2 was set as a reference session for alignment of the field of view. 

## **Passive odor stimulation with head-fixed animals** 

To habituate the animals to the head-fixed setup, we head-fixed animals without imaging at least three times before the imaging day. On the day of the experiment, we head-fixed animals after two imaging sessions with pup retrieval. Pup odor was delivered with 20 repetitions of 3 s duration and an interstimulus interval of 12 s using an olfactometer (PHM-275; Med Associates). Wavesurfer was used to generate precise TTL pulses to synchronize the stimulation timing and microendoscopic imaging. 

## **Non-social reward presentation** 

10% sucrose water was delivered from a behavioural lick port (Sanworks) controlled by an open source code MATLAB-based state machine (Bpod; Sanworks). Mice could access the sucrose water whenever they broke an IR beam in front of the lick port and waited for longer than 1 s. To habituate the mice with the setup, we introduced this drinking port 1 day before the imaging session. After a habituation period for longer than 12 h, we deprived the water supply for 12–16 h to enhance the value of water. Then, we performed imaging with a pup retrieval assay. During the session, mice could freely access the licking port. For each animal, we performed two to four imaging sessions (duration 6 min). TTL pulses from the state machine were used to synchronize the timing of water delivery and microendoscopic imaging. 

## **Pharmacogenetics** 

To activate (Extended Data Fig. 3) or silence (Fig. 4h–j and Extended Data Fig. 6h–j) neural activity by hM3Dq or hM4Di, respectively, 100  L of CNO (0.5 mg/mL, Sigma; C0832) was intraperitoneally injected after two 6-min imaging sessions (pre-CNO sessions). The two imaging sessions were performed 30 min after the injection of CNO (post-CNO sessions). 

## **Histology and histochemistry** 

Mice were given an overdose of isoflurane and perfused transcardially with PBS followed by 4% paraformaldehyde (PFA) in PBS. Brain tissues were post-fixed with 4% PFA in PBS overnight at 4  C, cryoprotected with 30% sucrose solution in PBS at 4  C for 24–48 h, and embedded in O.C.T. compound (Tissue-Tek, cat#4583). For the quantitative analysis of the trans-synaptic tracing, we 

40 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

collected 40-  m coronal sections of the whole brain using a cryostat (model #CM1860; Leica). Freefloating slices were then incubated in the following solutions with gentle agitation at room temperature: 2 h in blocking solution (5% heat-inactivated goat serum, 0.4% Triton-X100 in PBS); overnight at room temperature in primary antibody 1:1000 mouse anti-GFP (GFP-1010, Aves Labs), anti-RFP (5f8, Chromotek), or anti-Myc (Santa Cruz, Cat #sc-40, RRID: AB_627268) in blocking solution; 2–3 h in secondary antibody 1:500 anti-chicken-IgY Alexa488-conjugated, goat anti-mouseIgG Cy3-conjugated, or goat anti-rat-IgG Cy3-conjugated or goat (Jackson ImmunoResearch) in blocking solution; 15 min in 2.5  g/mL of DAPI (Santa Cruz, Cat #sc-3598) in PBS. Sections were mounted on slides and cover-slipped with mounting media (Fluoro-gold). 

Sections were imaged using an Olympus BX53 microscope with a 4  (NA 0.16) or 10  (NA 0.4) objective lens equipped with a cooled CCD camera (DP80; Olympus) or Zeiss Axio Scan.Z1 with a 20  (NA 0.8) objective lens. Unless otherwise noted, every second (Fig. 3a–g and Extended Data Fig. 4) or third (Fig. 3i–k, Extended Data Figs. 1, 5, 9) coronal brain section was analyzed for quantification. 

## **Rabies trans-synaptic tracing from the OFC** 

We sacrificed animals at 5 days after rabies injection (see **Stereotactic injection** ). To quantify the rabies tracing data, we imaged every second 40-  m coronal slice along the whole brain with a 10  (NA 0.45) objective lens using Zeiss Axio Scan.Z1. We counted the starter and input cells semiautomatically using open source software, including ilastik[58] and AMaSiNe[27] , with a custom-written MATLAB code. 

First, we trained ilastik with several slices to detect GFP and mCherry. Using these trained ilastik algorithms, we generated the binary mask for GFP and mCherry channels. We used the morphological opening function on MATLAB on the binary masks to eliminate noise from those masks. Then, we detected all GFP+ cells and made binary masks for those GFP+ cells to aid the detection of cells in AMaSiNe. For detecting starter cells, we generated the binary mask, which had an overlapped fraction between GFP and mCherry channels. We counted signals larger than 5 pixels as starter cells. We reconstructed the binary masks according to the location of detected input/starter cells, and then analyzed and annotated the cells to the brain region by AMaSiNe. All the detected cells and regional annotations were manually checked and corrected using the built-in function of AMaSiNe to ensure the quality of the analysis. 

For long-range inputs, we omitted the regions where we found the starter cells, such as the mOFC, M2, and prelimbic cortex (Extended Data Fig. 4), to avoid Cre-independent nonspecific labeling of rabies-GFP[26] . 

## **Axon tracing from the SMT/MD** 

We injected the AAV5 _CAG-FLEx-TC[b]_ into the SMT or MD (see **Stereotactic injection** ). More than 3 weeks after the injection of AAVs, we sacrificed the animals. To enhance the signal of axonal fibers, we stained with anti-RFP (Chromotek). To quantify the axon tracing data, we imaged every third 40- 

41 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

 m coronal slice along the whole brain with 10  objective lens using Zeiss Axio Scan.Z1. We then counted the soma and axons semi-automatically using ilastik and AMaSiNe, with a custom-written MATLAB code. Briefly, we trained ilastik with several slices to detect axon fibers and soma separately. Using these trained ilastik algorithms, we generated a binary mask for an mCherry channel. For counting soma, we used the same method as described above for rabies tracing data (Extended Data Fig. 4f, g). For counting axon fibers, each pixel was treated as a “cell” in AMaSiNe and annotated to the brain regions to calculate the axon density (Fig. 3k). 

## **Fluorescent** _**in situ**_ **hybridization** 

Fluorescent ISH was performed as previously described[59] . In brief, mice were anesthetized with sodium pentobarbital and perfused with PBS followed by 4% PFA in PBS. The brain was post-fixed with 4% PFA overnight. Thirty-micron coronal brain sections were made using a cryostat (Leica) and placed them on MAS-coated glass slides (Matsunami). To generate cRNA probes, DNA templates were amplified by PCR from the C57BL/6j mouse genome or whole-brain cDNA (Genostaff, cat#MD01). A T3 RNA polymerase recognition site (5’-AATTAACCCTCACTAAAGGG) was added to the 3’ end of the reverse primers. The primer sets to generate DNA templates for cRNA probes were as follows (the first one, forward primer, the second one, reverse primer): 

_Tnnt1_ 5’-AGCAGGCAGAAGATGAGGAA; 5’-TGGGGGCACTTTATTTTGAG 

_DAT_ 5’-TGCTGGTCATTGTTCTGCTC; 5’-ATGGAGGATGTGGCAATGAT 

_vGluT2_ -1 5’-TAGCTTCCTCTGTCCGTGGT; 5’-GGGCCAAAATCCTTTGTTTT 

_vGluT2_ -2 5’-CCACCAAATCTTACGGTGCT; 5’-GGAGCATACCCCTCCCTTTA 

_vGluT2_ -3 5’-CTCCCCCATTCACTACCTGA; 5’-GGTCAGGAGTGGTTTGCATT 

DNA templates (500–1000 ng) amplified by PCR were subjected to _in vitro_ transcription with DIG (cat#11277073910)-RNA labeling mix and T3 RNA polymerase (cat#11031163001) according to the manufacturer’s instructions (Roche Applied Science). In the case of _vGluT2_ , three independent RNA probes were mixed to increase the signal/noise ratio. 

For ISH combined with anti-GFP staining, after hybridization and washing, sections were incubated with horseradish peroxidase-conjugated anti-DIG (Roche Applied Science cat#11207733910, 1:500) and anti-GFP (Aves Labs cat#GFP-1020, 1:500) antibodies overnight. Signals were amplified by TSAplus Cyanine 3 (AKOYA Bioscience, NEL744001KT, 1:70 in 1  plus amplification diluent) for 25 min, followed by washing, and then GFP-positive cells were visualized by anti-chicken Alexa Fluor 488 (Jackson Immuno Research cat#703-545-155, 1:250). 

## **Fiber photometry with optogenetic stimulation** 

For fiber photometry recording (Fig. 5), _DAT-Cre/+; Ai162/+_ double heterozygous female mice were used. We implanted the optical fibers (NA = 0.50, core diameter = 200  m from RWD) into the bilateral OFC for optogenetic stimulation at 2 weeks after AAV injection into the OFC (coordinates relative to the bregma: anterior 2.5 mm, lateral 0.6 mm, depth 1.7 mm from the brain surface with tilting 5  from 

42 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

the vertical). At the same surgery, an optical fiber (NA = 0.50, core diameter = 400  m from Kyocera) was implanted above the VTA for fiber photometry. After surgery, the animals were crossed with stud males and housed in the home cage until recording. We performed Ca[2+] imaging by delivering excitation lights (470 nm modulated at 530.481 Hz and 405 nm modulated at 208.616 Hz) and collected the emitted fluorescence using the integrated Fluorescence Mini Cube (Doric, iFMC4_AE(405)_E(460-490)_F(500-550)_S). Light collection, filtering, and demodulation were performed using the Doric photometry setup and Doric Neuroscience Studio Software (Doric Lenses, Inc.). The 405-nm signal was recorded as a background (non-calcium-dependent), and the 470-nm signal reported calcium-dependent GCaMP6s excitation/emission. The power output at the tip of the fiber was about 50  W. The signals were initially acquired at 12 kHz and then decimated to 120 Hz. 

For optogenetic stimulation, animals were connected to a 465-nm laser (RWD) via split optical patch cords (NA = 0.50, core diameter = 200  m, 200TH200FL1A; Thorlabs) and a rotary joint (RJ1; Thorlabs). For optogenetic inhibition of the OFC using GtACR2, 150 s of 465 nm continuous photostimulation at 5 mW mm[2] at the fiber tip was used during the pup retrieval session. We first performed a photometry imaging session without light stimulation, followed by a session with light stimulation, which was repeated twice. 

We further analyzed the data using custom-written MATLAB codes. The 405-nm signal was subtracted from the 470-nm signal to minimize the motion noise. Then, we down-sampled the raw Ca[2+] data to 20 Hz. Ca[2+] traces during a session were Z-scored by the mean and standard error of the traces during 60 s preceding the onset of each session. To calculate the averaged response (Fig. 5g), we took a 2.5 s time window following the onset of the interaction, and that value was subtracted by the mean of 2 s preceding the interaction. 

## **Quantification and statistics** 

Statistical tests were performed using custom-written MATLAB codes. All tests were two-tailed. The sample size and statistical tests used are indicated in the figure or figure legends. The criteria for statistical significance were set at P < 0.05. Mean ± standard error of the mean (SEM) was used to report statistics unless otherwise indicated. 

In Fig. 1c, data set included 16 mice that were successfully imaged across all five maternality states. In Fig. 1h, the data set included the animals that showed more than 13 trials of pup retrieval. To normalize the statistical power among different stages, the same number of trials were used for each animal to determine whether a cell showed a significant response. In Fig. 4, we omitted the NV conditions from the analysis because only a few NV mice performed pup retrieval (see Fig. 4b). In Fig. 5, mice that retrieved no pups were excluded from the data sets. 

51. Yukinaga, H., Hagihara, M., Tsujimoto, K., Chiang, H.L., Kato, S., Kobayashi, K., and Miyamichi, K. (2022). Recording and manipulation of the maternal oxytocin neural activities in mice. Curr Biol 32, 3821-3829 e3826. 

43 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

   - 10.1016/j.cub.2022.06.083. 

52. Abe, T., Inoue, K.I., Furuta, Y., and Kiyonari, H. (2020). Pronuclear Microinjection during S-Phase Increases the Efficiency of CRISPR-Cas9-Assisted Knockin of Large DNA Donors in Mouse Zygotes. Cell Rep 31, 107653. 10.1016/j.celrep.2020.107653. 

53. Naito, Y., Hino, K., Bono, H., and Ui-Tei, K. (2015). CRISPRdirect: software for designing CRISPR/Cas guide RNA with reduced off-target sites. Bioinformatics 31, 1120-1123. 10.1093/bioinformatics/btu743. 

54. Osakada, F., and Callaway, E.M. (2013). Design and generation of recombinant rabies virus vectors. Nat Protoc 8, 1583-1601. 10.1038/nprot.2013.094. 

55. Lein, E.S., Hawrylycz, M.J., Ao, N., Ayres, M., Bensinger, A., Bernard, A., Boe, A.F., Boguski, M.S., Brockway, K.S., Byrnes, E.J., et al. (2007). Genome-wide atlas of gene expression in the adult mouse brain. Nature 445, 168-176. 10.1038/nature05453. 

56. Lu, J., Li, C., Singh-Alvarado, J., Zhou, Z.C., Frohlich, F., Mooney, R., and Wang, F. (2018). MIN1PIPE: A Miniscope 1-Photon-Based Calcium Imaging Signal Extraction Pipeline. Cell Rep 23, 3673-3684. 10.1016/j.celrep.2018.05.062. 

57. Sheintuch, L., Rubin, A., Brande-Eilat, N., Geva, N., Sadeh, N., Pinchasof, O., and Ziv, Y. (2017). Tracking the Same Neurons across Multiple Days in Ca(2+) Imaging Data. Cell Rep 21, 1102-1115. 10.1016/j.celrep.2017.10.013. 

58. Berg, S., Kutra, D., Kroeger, T., Straehle, C.N., Kausler, B.X., Haubold, C., Schiegg, M., Ales, J., Beier, T., Rudy, M., et al. (2019). ilastik: interactive machine learning for (bio)image analysis. Nat Methods 16, 1226-1232. 10.1038/s41592-019-0582-9. 

59. Ishii, K.K., Osakada, T., Mori, H., Miyasaka, N., Yoshihara, Y., Miyamichi, K., and Touhara, K. (2017). A Labeled-Line Neural Circuit for Pheromone-Mediated Sexual Behaviors in Mice. Neuron 95, 123-137 e128. 10.1016/j.neuron.2017.05.038. 

## **Data Availability** 

The data on which this study is based are available on reasonable request. 

## **Code Availability** 

The custom MATLAB codes used to analyze the data in this study are available on request. 

## **Acknowledgments** 

We thank Liqun Luo, Adi Mizrahi, Ido Maor, and members of the Miyamichi lab for the critical reading of the manuscript, Edward M. Callaway for sharing the B7GG, BHK-EnvA, and HEK293-TVA800 cell lines, the University of North Carolina vector core and the Canadian Neurophotonics Platform viral vector core facility for the AAV productions, Masanori Murayama for sharing the _Rbp4-Cre_ mice, 

44 

bioRxiv preprint doi: https://doi.org/10.1101/2023.02.03.527077; this version posted February 5, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license. 

Noriaki Ohkawa for the advice on the miniaturized microscope, and the animal facility of RIKEN BDR for taking care of the animals and _in vitro_ fertilization. This work was supported by the JST PRESTO program (JPMJPR21S7), JSPS KAKENHI (20K15941), and RIKEN incentive and diversity promotion grants to G.T., and a Takeda Science Foundation Research Grant, JSPS KAKENHI (20K20589, 21H02587), and a RIKEN center project grant to K.M. 

## **Author Contributions** 

G.T. and K.M. conceived the experiments. G.T. performed all the experiments and analyzed the data, with technical support from M.H., S.I., and H.K. K.I. and M.H. provided the AAV _OT-hM3D(Gq)-Myc_ . M.K. and T.A. designed and generated the _Tnnt1-Cre_ mice, and M.H. confirmed their genomic structure. G.T. and K.M. wrote the paper with help from all authors. 

## **Declaration of Interests** 

The authors declare that they have no competing interests. 

45 

