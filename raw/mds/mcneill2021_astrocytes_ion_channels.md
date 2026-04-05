REVIEW published: 20 May 2021 doi: 10.3389/fncel.2021.644126 

**==> picture [166 x 32] intentionally omitted <==**

**==> picture [28 x 29] intentionally omitted <==**

## Ion Channels and Electrophysiological Properties of Astrocytes: Implications for Emergent Stimulation Technologies 

_Jessica McNeill , Christopher Rudyk , Michael E. Hildebrand and Natalina Salmaso*_ 

_Department of Neuroscience, Carleton University, Ottawa, ON, Canada_ 

_Edited by: Wannan Tang, University of Oslo, Norway_ 

_Reviewed by: Hyungju Park, Korea Brain Research Institute,_ 

_South Korea Frank Kirchhoff, Saarland University, Germany_ 

_*Correspondence: Natalina Salmaso natalina.salmaso@carleton.ca_ 

Astrocytes comprise a heterogeneous cell population characterized by distinct morphologies, protein expression and function. Unlike neurons, astrocytes do not generate action potentials, however, they are electrically dynamic cells with extensive electrophysiological heterogeneity and diversity. Astrocytes are hyperpolarized cells with low membrane resistance. They are heavily involved in the modulation of K[+] and express an array of different voltage-dependent and voltage-independent channels to help with this ion regulation. In addition to these K[+] channels, astrocytes also express several different types of Na[+] channels; intracellular Na[+] signaling in astrocytes has been linked to some of their functional properties. The physiological hallmark of astrocytes is their extensive intracellular Ca[2+] signaling cascades, which vary at the regional, subregional, and cellular levels. In this review article, we highlight the physiological properties of astrocytes and the implications for their function and influence of network and synaptic activity. Furthermore, we discuss the implications of these differences in the context of optogenetic and DREADD experiments and consider whether these tools represent physiologically relevant techniques for the interrogation of astrocyte function. 

Keywords: glia, physiology, ion channels, calcium, potassium, sodium, optogenetics, DREADDs 

_Specialty section: This article was submitted to Non-Neuronal Cells, a section of the journal Frontiers in Cellular Neuroscience_ 

_Received: 20 December 2020 Accepted: 26 April 2021 Published: 20 May 2021_ 

_Citation:_ 

_McNeill J, Rudyk C, Hildebrand ME and Salmaso N (2021) Ion Channels and Electrophysiological Properties of Astrocytes: Implications for Emergent_ 

_Stimulation Technologies. Front. Cell. Neurosci. 15:644126. doi: 10.3389/fncel.2021.644126_ 

## INTRODUCTION 

Astrocytes comprise a heterogeneous population of macroglial cells that are the most abundant neural cell type in the central nervous system (CNS). Similar to both neurons and oligodendrocytes, astrocytes arise from the neural stem cell pool (Sloan and Barres, 2014). The process of gliogenesis in rodents begins around embryonic day 16–18 with the majority of cortical astrogliogenesis likely occurring in the postnatal period where a substantial increase in glial numbers are observed during the second and third postnatal weeks (Abney et al., 1981; Qian et al., 2000; Bushong et al., 2004; Freeman, 2010). The extensive morphological and functional heterogeneity of astrocytes is in part driven by their place of birth and neuronal neighbors during the course of development (Lanjakornsiripan et al., 2018; Bayraktar et al., 2020). This may be mediated, in part, through the release of specific neurotransmitters or neurotrophic factors from these nearby neurons. At least in cortical development, neuronal heterogeneity induces differential astroglial phenotypes (Bayraktar et al., 2020). 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

1 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

Morphologically, astrocytes can take many forms, though they are perhaps best known for their protoplasmic shape; a smaller soma surrounded by numerous processes that extend outwards (Sofroniew and Vinters, 2010), giving them a ‘‘starlike’’ shape for which they are named. In addition to these protoplasmic astrocytes, which predominantly exist in gray matter, there are fibrous astrocytes which are found throughout the white matter (Sofroniew and Vinters, 2010). The somata of these cells orient themselves in perpendicular rows between the axon bundles while their processes make connections to nodes of Ranvier (Oberheim et al., 2009). These two dominant morphological types of astrocytes are by no means an exhaustive list; velate astrocytes of the olfactory bulb and cerebellum, Bergmann glia of the cerebellum, Müller glia in the retina, pituicytes of the neurohypophysis, radial glia, and Gomori astrocytes of the hypothalamus all represent morphologicallydistinct classes of astrocytes (Verkhratsky and Nedergaard, 2018; Khakh and Deneen, 2019). 

Astrocytes display even greater diversity in their functional roles. Previously believed to only provide structural support to neurons, it is now well-established that astrocytes are key regulators of CNS homeostasis. Some of these homeostatic functions include the buffering of ions like potassium (K[+] ), sodium (Na[+] ), and protons (H[+] ), and the regulation of neurotransmitters. Astrocytes form an integral part of the tripartite synapse; their processes encompass the synapse, allowing them to remove excess neurotransmitters from the cleft. This is particularly important for the excitatory neurotransmitter, glutamate: astrocytes are responsible for removing and breaking down almost all central extracellular glutamate (Mahmoud et al., 2019). These glutamatergic transporters are also critical for modulating neuronal plasticity; for example, downregulation of the glutamate-1 transporter has been shown to impair long-term potentiation (LTP; Li Y.-K. et al., 2012). 

In addition, astrocytes contribute to CNS homeostasis by forming an integral part of the blood-brain barrier; their endfeet surround the cerebral capillaries as part of the neurovascular unit (Liedtke et al., 1996; Wilhelm et al., 2016). Thus, they play a key role in modulating the entry of molecules into the CNS; permitting access for essential substances like nutrients while preventing access of potentially harmful agents like oxidants (Wilhelm et al., 2016). Astrocytes are also crucial for regulating pH levels, modulating oxidative stress, and providing energy substrates to neurons. For example, astrocytes are key metabolizers of glucose, the main source of energy (ATP) production in the brain (Prebil et al., 2011). 

Astrocytes are also key players in CNS injury response, undergoing morphological and functional changes in a process known as reactive astrogliosis. Their response differs according to the extent and cause of the injury and includes molecular, morphological, and physiological changes (Sofroniew and Vinters, 2010). Reactive astrocytes can produce neurotoxic or neuroprotective effects. Two distinct classifications of reactive astrocytes, termed ‘‘A1’’ and ‘‘A2’’ (neurotoxic and neuroprotective, respectively) have recently been characterized (Liddelow et al., 2017), though it is likely more phenotypes exist. 

Despite the accumulating evidence demonstrating the extensive regional and sub-regional diversity of astrocytes, there remains very little understanding of how the electrophysiological properties of astrocytes may diverge across these subpopulations. A large body of evidence in the field suggests that astrocytes may not be as ‘‘electrically silent’’ as previously believed, so characterizing differences in these electrophysiological properties will be important for understanding the functional differences of astroglial cells. Moreover, the increased use of technologies such as designer receptors activated by designer drugs (DREADDs) and optogenetics in astrocytes, augments the need to understand the physiological properties of astrocytes as these properties will be critical for the future application of these tools to this cell population. A greater knowledge of astrocyte physiology will inform experimental design, determine the physiological relevance (or not) of specific electrical stimulation experiment(s) and help with acknowledging the limitations of each. In the remainder of this review, we will highlight the regional differences in astrocyte physiology, and discuss the implications for optogenetic and DREADD manipulation of astrocytes. 

## HETEROGENEITY OF ASTROCYTE MEMBRANE POTENTIAL, RESISTANCE AND CURRENT PATTERNS UNDER BASAL AND REACTIVE CONDITIONS 

## Astrocytes Are Electrically Active Cells 

Though neurons are the main excitable cell type of the brain, astrocytes are not ‘‘electrically silent’’ cells. Astrocytes have a hyperpolarized membrane (Du et al., 2016) that typically rests below that of neurons (see section below; Bolton et al., 2006; Zhou et al., 2006), in contrast to the majority of non-excitable cells that have relatively depolarized membrane potentials. Though they cannot generate an action potential, astrocytes are able to respond biochemically to stimuli within their environment, especially ions and neurotransmitters. Astrocytic membranes are rich with several cation and anion channels (including both voltage-dependent and voltage-independent channels), which help with the regulation of ions such as Na[+] , K[+] , Ca[2+] and Cl[−] , in addition to contributing to the resting membrane potential (RMP), resting conductance and intracellular signaling within astrocytes (Parpura et al., 2011; Ryoo and Park, 2016). Several of these channels have permeability properties that are independent of voltage (i.e., TWIK 1, TREK 1—see ‘‘Voltage-Independent K[+] Channels Contribute to Passive Conductance’’ section), but many are voltage-dependent (such as delayed–rectifying potassium channels—see ‘‘Voltage-Dependent K[+] Channels Have Distinct Subcellular Localization’’ section). Therefore, astrocytes are a dynamic cell type with functional and signaling properties that vary with changes in membrane potential. In addition to ion-permeable channels, astrocytes also express several electrogenic transporters to help facilitate the exchange of ions across their membrane. For example, the Na[+] -K[+] -ATPase pump exchanges three Na[+] ions out for every two K[+] ions in, and the 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

2 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

Na[+] -K[+] -2Cl[−] -cotransporter pump exchanges Na[+] , K[+] , and Cl[−] , with an accompanying influx of water into the cell (Bellot-Saez et al., 2017). These ion channels and transporters represent an important facet of astrocyte physiology; astrocytic Ca[2+] signaling represents another. 

Calcium signaling in astrocytes plays an important role in facilitating the bidirectional communication between neurons and astrocytes at the synapse (for a more complete review on neuron-astrocyte interactions at the synapse, see Allen and Eroglu, 2017). Astrocytes express a plethora of ionotropic and metabotropic receptors, enabling a diverse set of responses to neurotransmitters such as glutamate, serotonin, dopamine, and GABA (Verkhratsky et al., 2019). Neurotransmitter binding to astrocytes can induce intracellular Ca[2+] signals, and the magnitude, localization and time course of these signals vary significantly depending on the stimulus and synaptic network involved (Araque et al., 2014). However, this neuron to astrocyte communication is not the only form of interaction between these cell types. Astrocytes are able to modulate neuronal activity through the release of several active factors such as glutamate, ATP and D-serine in a process known as gliotransmission (Parpura et al., 1994; Cotrina et al., 2000; Henneberger et al., 2010; Araque et al., 2014; Perez et al., 2017). This process is partly mediated by intracellular Ca[2+] signaling pathways (Araque et al., 2014). The release of these gliotransmitters from astrocytes is known to regulate synaptic transmission and plasticity. Changes in the frequency of miniature and spontaneous excitatory postsynaptic currents (EPSCs) and inhibitory postsynaptic currents (IPSCs), and the modulation of both LTP and longterm depression (LTD) have all been observed following the release of gliotransmitters from astrocytes across several different brain regions including the hippocampus, cortex and cerebellum (Kang et al., 1998; Brockhaus and Deitmer, 2002; Takata et al., 2011; Navarrete et al., 2012; Araque et al., 2014). Calcium signaling in astrocytes has also been shown to stimulate the Na[+] -K[+] -ATPase pump, leading to a decrease in extracellular K[+] and subsequent neuronal hyperpolarization and suppression of baseline excitatory activity (Wang et al., 2012). 

## Astrocytes Display a Highly Negative Resting Membrane Potential 

Compared to their neuronal counterparts, astrocytes display a more hyperpolarized, or negative, RMP (Bolton et al., 2006). While neuronal membranes typically rest at between approximately −50 mV and −70 mV (Zaitzev et al., 2012; Shen et al., 2018; Fernandez et al., 2019), the RMP of astrocytes is typically lower. However, specific astrocyte RMP values vary substantially across the CNS. For example, mature astrocytes of the CA1 region of the hippocampus have an RMP of about −80 mV (Tang et al., 2009; Deemyad et al., 2018), whereas astrocytes of the optic nerve have an average RMP of −62 mV (Butt and Jennings, 1994). A comparison between telencephalic astrocytes found that those of the _stratum oriens_ and _stratum pyramidale_ regions of the hippocampus had a significantly more negative (RMP of −90 mV) average membrane potential compared to those of the layers V and VI of the cortex (with an RMP of about −85 mV; Mishima and Hirase, 2010). 

There is also extensive heterogeneity of astrocytes within the _same_ region; astrocytes of the optic nerve have an RMP ranging from −25 to −80 mV (Bolton et al., 2006) whereas those in the ventral tegmental area (VTA) ranged from −60 to −90 mV (Xin et al., 2019). The hippocampus has proven to have a diverse pool of astrocytes; astrocytes in this area have RMPs ranging from −80 mV in the CA1 and _stratum radiatum_ subregions (Zhong et al., 2016; Deemyad et al., 2018) to a more negative RMP (−90 mV) in the _stratum oriens_ and _stratum pyramidale_ (Mishima and Hirase, 2010). 

In neurons, the RMP is important for setting the threshold, propensity, and frequency of action potentials. In astrocytes, which lack action potentials, the highly negative (hyperpolarized) RMP is critical for enabling and regulating homeostatic functions such as K[+] buffering and even neurotransmitter reuptake (Zhou et al., 2006; Ryoo and Park, 2016). Variability in astrocytic RMPs throughout the CNS may therefore reflect differences in (some) astrocytic functions. 

The underlying reason(s) for differences in astrocyte RMP across brain regions and subtypes have not been fully elucidated, but it is likely a result of a complex interplay between numerous extrinsic and intrinsic factors. An astrocyte’s immediate environment and neuronal input may drive heterogeneity in RMP values across the CNS. The morphological characteristics of individual astrocytes may also play a role in determining RMP. For example, a heavily branched astrocyte with numerous processes and greater membrane surface area may have a higher number of ion channels, particularly leak channels (i.e., K[+] ), that could in part explain some of the differences in astrocyte RMP (relationships between morphology, RMP heterogeneity, and differential astrocytic Ca[2+] signaling- _are further discussed in ‘‘Ca[2+] signaling pathways in astrocytes’’_ ). However, as specific morphological classes of astrocytes have not been linked with particular ranges of RMPs, it is highly probable that several other factors also influence the RMP of an astrocyte, such as intracellular signaling pathways (see **Figure 1** ). 

One intracellular signaling cascade that may influence the RMP of astrocytes is the cAMP/PKA pathway. Bolton et al. (2006) demonstrated that incubation of astrocytes with a cAMP analog (to activate adenylate cyclase) hyperpolarized their mean RMP. The addition of a PKA inhibitor caused a significant depolarization of the astrocytic membrane, but this effect was only partially reversed with the cAMP analog, suggesting that cAMP influences astrocytic RMP _via_ both PKA-dependent and—independent pathways (Bolton et al., 2006). Therefore, the variability of astrocytic RMP may be mediated by differences in intracellular cAMP/PKA signaling. In astrocytes, this cAMP/PKA pathway has been linked to changes in cell morphology and gene expression. A recent study found that over 6,000 astroglial gene transcripts were differentially regulated by cAMP signaling; gene ontology revealed associations with pathways controlling antioxidant activity, cell metabolism, and ion transporters (Paco et al., 2016). For example, numerous ion channels, pumps and transporters such as Kcn2 (for K[+] ) and ATP2a2 (for Ca[2+] ) were all upregulated by cAMP (Paco et al., 2016). Given the critical role of cAMP in these various functions, 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

3 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

**==> picture [427 x 299] intentionally omitted <==**

FIGURE 1 | An astrocyte’s resting membrane potential (RMP) is likely influenced by multiple extrinsic and intrinsic factors including (A) ion channel subtype expression and density, particularly Ca[2+] , Na[+] , and K[+] channels (ions represented by green, red, and blue circles, respectively); (B) astrocyte morphology; (C) neighboring cells including neurons, oligodendrocytes, microglia, and other astrocytes through the release of neurotransmitters, gliotransmitters, and other factors; (D) intracellular astrocyte signaling cascades such as the cAMP pathway. cAMP PKA-dependent and PKA-independent mechanisms have been proposed to influence astrocyte RMP (Bolton et al., 2006). 

the differences in astrocyte RMP may be an electrophysiological hallmark of critical differences in cAMP signaling of astrocytes between and within regions (see **Figure 1** ). 

## Astrocytes Are Characterized by Low Membrane Resistance 

In addition to their negative RMP state, astrocytes typically have a dramatically lower membrane input resistance than neurons under basal conditions (Zhou et al., 2006; Ma et al., 2014; Du et al., 2015; Xin et al., 2019), suggesting a relatively high overall permeability to ions at rest. The low input resistance of astrocytes makes it particularly challenging to study their biophysical properties using electrophysiological approaches (for example, the low membrane resistance can cause a large portion of the voltage drop to occur across the electrode tip rather than across the cell membrane change; Ma et al., 2014). Nonetheless, the available data suggests astrocytic membrane resistance differs across brain regions, and even within the same region. For example, VTA astrocytes have, on average, a significantly lower membrane resistance compared to those of the cortex or hippocampus (approximately 1 M _�_ in the VTA compared to approximately 3 MΩ in the cortex and hippocampus; Xin et al., 2019), though no differences have been 

noted between cortical and hippocampal astrocytes (Mishima and Hirase, 2010; Xin et al., 2019). However, several studies have found differences in membrane resistance amongst astrocytes within the hippocampus (Isokawa and McKhann, 2005; Zhong et al., 2016), suggesting that the membrane resistance of only some hippocampal astrocytes are comparable to those in the cortex. In one study, two distinct electrophysiological phenotypes of astrocytes were identified in the _stratum radiatum_ ; one subclass was defined by a variable input resistance with an overall mean input resistance significantly higher than the other subclass (Zhong et al., 2016). 

Precisely what these differences mean is not fully understood, however, because input resistance is inversely proportional to overall ion permeability across the membrane, these differences might represent variability in the capacity of astrocytes to conduct/transport ions in and out of the cell. Therefore, differences in membrane resistance could offer significant insight into the ability of astrocytes to buffer various ions as well as resultant downstream intracellular signaling pathways driven by these ions. 

It is also important to consider how morphology, and specifically, membrane surface area, may influence membrane resistance. An increase in the number or length of astrocytic 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

4 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

processes and therefore, membrane surface area, will lead to an increase in leak channels (if channel density is equal across these membrane processes), and thus an increase in overall membrane conductance. An increase in membrane conductance will directly result in a decrease in membrane resistance. While differences in morphology alone may be insufficient to explain the heterogeneity in astrocytic membrane resistance, it is likely that it is a contributing factor. 

Challenges to the CNS have also been noted to influence membrane resistance in astrocytes, though these changes are variable and appear to depend on the type and extent of the challenge. Following a unilateral entorhinal cortex lesion, astrocytes of the denervated layer in the dentate gyrus had an increase in membrane resistance that persisted for up to 10 days post-lesion (Schröder et al., 1999). Another study observed changes of membrane resistance in some astrocytes, but not others, following incubation with high [K[+] ], a model of early astrocyte activation (Neprasova et al., 2007). A decrease in the membrane resistance of hippocampal astrocytes in slice was noted following exposure to ammonium (a model of hepatic encephalopathy; Stephan et al., 2012). 

In a cortical freeze lesion model, changes in the membrane resistance of astrocytes were noted though these changes varied significantly depending on the relative location of the astrocytes to the injury site (Bordey et al., 2001). Increased membrane resistance was noted in layer I astrocytes of a lesioned cortex compared to controls but astrocytes in the ‘‘hyperexcitable’’ zone (characterized by the epileptiform activity of neurons upon stimulation) showed virtually no changes in membrane resistance (Bordey et al., 2001). Additionally, this model induced a proliferative zone; an area surrounding the lesion characterized by proliferating astrocytes (Bordey et al., 2001). Interestingly, astrocytes in this proliferative zone had a mean membrane resistance that was significantly higher than astrocytes of the hyperexcitable zone under both control and lesioned conditions (Bordey et al., 2001). 

The changes in astrocytic membrane resistance following disturbances to the CNS may represent compensatory mechanisms. A low membrane resistance, such as the one typically seen in astrocytes, suggests increased ionic permeability across the astrocyte’s membranes. The initial increase in input resistance following a unilateral entorhinal cortex lesion (Schröder et al., 1999) suggests a reduced ability of ion conduction across the membrane in the proliferative zone. This might represent a mechanism to help regulate ion homeostasis during times of CNS perturbations. On the contrary, this increase in membrane resistance could also represent a mechanism that perpetuates CNS damage. If an increase in membrane resistance corresponds to a reduced ability to transport ions across the membrane, this could mean a reduced ability to maintain extracellular ion homeostasis, thus causing further damage. 

These injury-induced changes in astrocyte membrane resistance may correspond with the changes in astrocyte morphology that characterizes reactive astrogliosis. Following CNS injury, hypertrophy of astrocytes occurs in levels correlative to the severity of the injury (Sofroniew and Vinters, 2010). Retraction of astrocytic processes and a hypertrophied cell soma 

means a smaller membrane surface area (and potentially fewer leak channels), which could explain an increase in membrane resistance. As astrocytes closer to the site of injury tend to undergo greater hypertrophy, this could partially explain why the membrane resistance of astrocytes might vary across different zones of the injury site. In the case of localized CNS damage (such as a lesion or ischemic event), the location of astrocytes relative to the damage may represent a significant factor in determining whether the membrane resistance increases, decreases, or remains the same. In Bordey et al.’s (2001) study, the physiological changes differed significantly amongst the different zones of the injury, suggesting this may be an important factor influencing astrocyte physiology under reactive conditions. 

Reactive astrogliosis has long been recognized as a process that induces morphological, molecular and physiological changes. Data from studies that have induced CNS damage (Schröder et al., 1999; Bordey et al., 2001; Neprasova et al., 2007; Stephan et al., 2012) demonstrate clearly that the basic electrophysiological properties of astrocytes (i.e., membrane resistance) also change in response to perturbations in the CNS, though in many contexts, these changes are not well characterized and understood. As the perspective of astrocyte heterogeneity continues to develop, under basal and reactive conditions, it will be essential for the perspective of astrocyte electrophysiology to do the same. 

## Electrophysiological Properties of Astrocytes Across Development 

Further contributing to the complexity of astrocyte physiology is that many of the other basic electrophysiological properties of astrocytes such as their membrane potential change across development (Zhou et al., 2006; Zhong et al., 2016). One study found that neonatal astrocytes (P1–P3) of the _stratum radiatum_ had a more negative membrane potential compared to mature astrocytes ( _P >_ 21) of the same region (approximately −85 mV and −80.9 mV, respectively; Zhong et al., 2016). These changes across development highlight the caution that must be taken when generalizing electrophysiological data across studies and across timepoints. 

It is currently unknown what drives these changes in the electrophysiological properties of astrocytes throughout development. In the cortex, morphological and functional heterogeneity of astrocytes is influenced greatly by neuronal heterogeneity _via_ the release of specific neurotransmitters, ions, and neurotrophic factors (Verkhratsky and Nedergaard, 2018; Bayraktar et al., 2020); it is likely that this is also the case for the electrophysiological features of astrocytes. It is also possible these changes reflect shifts in the expression of ion transporters. For example, the K[+] -Cl[−] - cotransporter (KCC2) helps modulate Cl[−] levels in neurons through the export of 1 K[+] and 1 Cl[−] across the membrane (Annunziato et al., 2013). An increase in the neuronal expression of KCC2 early in development is believed to drive the shift of GABA from an excitatory to an inhibitory neurotransmitter (Moore et al., 2019). However, KCC2 is also expressed in astrocytes (Annunziato et al., 2013; Rurak et al., 2020), and this expression increases 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

5 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

across development (Rurak et al., 2020). Perhaps the increase in KCC2 expression in astrocytes, and subsequent changes in intracellular K[+] and Cl[+] levels and reversal potentials, is what drives the changes in the electrophysiological properties such as RMP over development. Moreover, increased ion transport across the membrane _via_ transporters such as KCC2 could also influence the input resistance of astrocytes. Developmental changes in transporter expression may represent one potential mechanism that drives changes in astrocyte electrophysiology across the lifespan. 

It is clear from the literature that astrocytes differ tremendously in many of their basic electrophysiological properties such as their RMP, membrane resistance, membrane currents, and selective ion permeability. The literature also shows that these properties differ significantly at both the regional and sub-regional levels. There remains a large gap in knowledge about the relationship between the specific electrophysiology properties of astrocyte subpopulations and how these properties correspond to their morphological, biochemical, and functional properties. It is likely that future studies on astrocyte electrophysiology, will result in new methods for classifying and modulating signaling within astrocyte subtypes. 

## Astrocyte Electrophysiology: Convergence Across Species 

The evidence presented thus far for the heterogeneity of astrocyte electrophysiology is primarily derived from studies utilizing _in vitro_ or _in vivo_ rodent models. However, whether the electrophysiological properties of astrocytes are conserved across species is not well characterized. Furthermore, while rodent astrocytes appear to exhibit extensive heterogeneity in their electrophysiology, it is unknown whether (or to what extent) human astrocytes show similar heterogeneity in _their_ electrophysiological properties. However, it is well established that rodent and human astrocytes do differ in many of their characteristics (Oberheim et al., 2009; Dossi et al., 2018; Miller, 2018). 

Morphological and transcriptional analyses have revealed differences between astrocytes across species. For example, several studies have demonstrated that human astrocytes tend to exhibit larger soma with a greater number of processes compared to their rodent counterparts (Oberheim et al., 2006, 2009; Zhang et al., 2016). Transcriptional differences have also been noted; one study found over 600 genes enriched in human astrocytes that were not enriched in mouse astrocytes (Zhang et al., 2016). Given this divergence between species, it is possible that human astrocytes also differ in terms of their electrophysiological properties. 

Few studies have been conducted that evaluate the electrophysiological properties of human astrocytes. Early studies of human astrocytes measured comparable RMPs to those observed in rodents (Bordey and Sontheimer, 1998; O’Connor et al., 1998; Hinterkeuser et al., 2000). One of these studies noted a higher membrane capacitance in human astrocytes (Bordey and Sontheimer, 1998), which is perhaps expected given the larger surface area of human astrocytes 

(Bedner et al., 2020). Interestingly though, this study did note a high input resistance (Bordey and Sontheimer, 1998). However, there is contention over whether these early studies successfully analyzed astrocytes, or whether they had actually identified NG2+ glial cells (Bedner et al., 2020). A more recent study of hippocampal astrocytes from patients with temporal lobe epilepsy revealed they exhibited a passive conductance and an RMP, membrane resistance and capacitance similar to rodent astrocytes of the same region (Bedner et al., 2015, 2020). This suggests that some electrophysiological properties of astrocytes are, in fact, conserved between rodents and humans (Bedner et al., 2020). However, there lacks sufficient studies/evidence to draw any strong conclusions. 

Given the heterogeneity of astrocytes in the rodent brain, it is possible that a similar diversity in electrophysiological properties exists in human astrocytes. Studies involving direct comparisons across species will also be critical; this is particularly important because of the observed differences in species morphology, and the link between morphology and membrane capacitance. Any differences between rodent and human astrocyte electrophysiology could potentially be explained by differences in morphology. However, one study did show comparable membrane capacitance values between mouse and human astrocytes (Bedner et al., 2015, 2020), which could mean other factors are influencing human astrocyte physiology such as the density of ion channel expression. At this time, too few studies have been conducted to reach reliable conclusions as to if, and to what extent, human astrocyte electrophysiology differs from their rodent counterparts. 

An additional caveat of astrocyte electrophysiology research is the extensive differences in the experimental protocol. Although _in vitro_ (i.e., cell culture and slice) and _in vivo_ data suggests comparable findings across experimental paradigms, few, if any, studies have directly compared electrophysiological properties of astrocytes from culture, slice and _in vivo_ samples. Therefore, this calls for caution when interpreting and extrapolating electrophysiological data across paradigms. 

## ASTROCYTES ARE KEY REGULATORS OF K[+] HOMEOSTASIS 

## Astroglial K[+] Spatial Buffering Mediated Through Kir4.1 Subtype 

The combination of a highly negative RMP and a low membrane resistance make astrocytes particularly well suited for buffering potassium (K[+] ; Du et al., 2015), one of their most critical homeostatic functions within the CNS. The extracellular concentration of K[+] ([K[+] ]o) rests at approximately 3.0 mM, and is critical in establishing the RMP of both neurons and astrocytes (Anderson et al., 1995; Bellot-Saez et al., 2017). Interestingly, the average RMP of astrocytes is close to the equilibrium potential of K[+] (Somjen, 1979; Guatteo et al., 1996), thus reflecting a high resting conductance for the ion (Somjen, 1979; Dallérac et al., 2013). 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

6 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

Changes in [K[+] ]o can be indicative of increased neuronal activity (Neprasova et al., 2007). Increases in [K[+] ]o occur following neuronal excitation whereby K[+] clearance from the neuron is used to co-transport Na[+] ions out of the cell following periods of high action potential-mediated Na[+] influx (Hertz and Chen, 2016). Thus, regulation and uptake of extracellular K[+] is essential in maintaining a homeostatic balance within the CNS. While both neurons and astrocytes are capable of regulating K[+] levels, this function is typically associated with astroglial cells. Several mechanisms of K[+] maintenance have been identified including passive spatial buffering and uptake mediated through active transporters. 

The concept of K[+] spatial buffering was first proposed decades ago (Walz, 1982; Verkhratsky and Nedergaard, 2018). In the proposed model, K[+] enters astrocytes _via_ K[+] - permeable membrane channels and diffuses to areas of lower K[+] concentration in the glial network _via_ gap junctions connecting the glial syncytium (Higashi et al., 2001; Verkhratsky and Nedergaard, 2018). This occurs without additional energy requirements (Orkand et al., 1966; Bellot-Saez et al., 2017). The initial uptake of extracellular K[+] prior to its redistribution throughout the glial syncytium is mediated through many subtypes of K[+] -permeable channels, including both voltagedependent (i.e., inward-rectifying and Kv families) and independent (i.e., two-pore domain or ‘‘leak’’ family, see next section) K[+] channels. Each of these families of channels express several subtypes including TREK 1, TWIK 1, and Kv 3.4 and 4.3 (this is not an exhaustive list but will be the focus in the remainder of this section). Of the variants of voltage-dependent K[+] channels, the inward-rectifying K[+] channels are a family consisting of 16 channels, subdivided into seven subfamilies (Bellot-Saez et al., 2017). The Kir4.1 subtype, a weakly inwardrectifying K[+] channel, is the predominant subtype expressed on astrocytes (Kofuji and Newman, 2004; Brasko et al., 2017). 

The robust expression of the Kir4.1 subtype is believed to contribute to the high resting conductance of K[+] in astrocytes (Tang et al., 2009). However, expression of the Kir4.1 subtype within astrocytes is variable; the channel is expressed in the spinal cord (Olsen et al., 2006), deep cerebellar nuclei, Müller glia of the retina as well as a subset of the hippocampus, but not in all astrocytes found within the hippocampus and white matter (Poopalasundaram et al., 2000; Higashi et al., 2001; Rurak et al., 2020). In a comprehensive analysis of Kir4.1 subtype expression in glial cells, Kir4.1 immunoreactivity was enriched in astrocytic processes wrapped around blood vessels (Hibino et al., 2004) and at synapses. Enrichment of Kir4.1 at blood vessels was also noted in human tissue (Tan et al., 2008). 

The channel subtype was observed on astrocytes in several regions, including the forebrain, midbrain, and hindbrain, albeit to varying degrees (Higashi et al., 2001). The percentage of total synapses covered by Kir4.1-positive processes varied substantially between brain regions, with over 60% of synapses covered in regions such as the entorhinal cortex, the superior and inferior colliculi and the pontine nucleus, but only 30%–60% of synapses covered in regions such as the anterior dorsal nucleus and lateral nuclei of the thalamus and the interpeduncular nucleus. Other regions, 

like the mitral cell layer of the olfactory bulb, exhibited very little Kir4.1-positive processes surrounding synapses (Higashi et al., 2001). 

The expression of the Kir4.1 subtype is also variable within the cortex. Benesova et al. (2012) identified distinct subpopulations of astrocytes within the cortex that differed in their extent of swelling following oxygen-glucose deprivation. These subpopulations were (nearly) uniformly distributed across each layer of the cortex but varied significantly in gene expression of several K[+] -related channels, including Kir4.1. There was approximately a 1.5 log difference in gene expression between the subpopulations (Benesova et al., 2012). In contrast, another study found differences in Kir4.1 immunoreactivity between layers of the cortex; there was greater Kir4.1 subtype expression in cortical layers II and III compared to layers IV–VI, though this study did not distinguish between (possible) subtypes of astrocytes (Higashi et al., 2001). 

The subregional diversity of astrocytic Kir4.1 subtype expression has been noted in other regions including the olfactory bulb and the hippocampus (Higashi et al., 2001). Each layer of the olfactory bulb, for example, has varying expression of the Kir4.1 subtype subunit, with high expression in layers such as the glomerular layer, and much lower expression in layers such as the olfactory nerve and mitral cell layers (Higashi et al., 2001). A similar pattern was seen in the hippocampal layers; almost no Kir4.1 was seen in the dentate gyrus but there was astroglial expression of the channel in the CA layers (Higashi et al., 2001). Moreover, co-localization of the Kir4.1 subtype with glial fibrillary acidic protein (GFAP), an intermediate filament protein commonly used as a marker for astrocytes, showed differences between each layer of the olfactory bulb (Higashi et al., 2001), further demonstrating the molecular and physiological heterogeneity of astrocytes. 

There is some evidence to indicate heterogeneous subcellular localization of Kir4.1 in astrocytes. One study of cerebellar glia found Kir4.1 expression in the radial processes of Bergmann glia in the Purkinje cell layer, whereas astrocytes of the granule cell layer expressed Kir4.1 in both the processes and somata (Brasko et al., 2017). In contrast, Muller glia of the retina preferentially express Kir4.1 in their perivascular endfeet vessels (Kofuji et al., 2002). Similarly, Kir4.1 is expressed in endfeet and fine processes of astrocytes within the rat optic nerve (Kalsi et al., 2004). The function of Kir4.1 may be mediated by its subcellular localization; at perivascular endfeet, the ion channel may be important for regulating K[+] in the blood vessels, but those localized at the processes or somata may be more important for regulating K[+] levels of the astrocyte itself. Nonetheless, the heterogeneity of subcellular Kir4.1 expression across different regions further emphasizes the extensive diversity of astrocyte electrophysiology. 

The variability of astrocytic Kir4.1 subtype expression further demonstrates the physiological heterogeneity of astrocytes. Whilst differing levels of the Kir4.1 subtype are not necessarily indicative of differing capabilities of K[+] regulation, it does suggest, at the very least, that astrocytes of varying brain regions utilize alternative mechanisms to regulate K[+] . It appears astrocytes of the _same_ region may also exhibit alternative mechanisms for K[+] regulation as they also display differing 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

7 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

levels of the Kir4.1 subtype; and since Kir4.1 appears to be particularly important in generating the RMP of astrocytes, it is possible that astrocyte subtypes with different membrane potentials express different levels of this K[+] channel. That astrocytes might differ concomitantly in distinct features (i.e., morphological, physiological, functional) demonstrates the complexity of astrocyte heterogeneity, and the importance of further understanding the physiological diversity of this unique cell population. 

## Voltage-Independent K[+] Channels Contribute to Passive Conductance 

The two-pore domain, voltage-independent K[+] channels (K2P) are thought to contribute substantially to the electrophysiological properties of astrocytes (Ryoo and Park, 2016; Verkhratsky and Nedergaard, 2018). This group of ‘‘leak channels’’ is a 15-member family of which at least three channel subtypes have been identified in astrocytes (Seifert et al., 2009; Du et al., 2016). TREK 1, TREK 2, and TWIK 1 have been observed in astrocytes of the hippocampus (Seifert et al., 2009; Du et al., 2016), cortex (Gnatenco et al., 2002), and forebrain (Cahoy et al., 2008), though it is likely that these channels are expressed in astrocytes throughout the CNS. 

Despite their voltage-independence, K2P channels mediate currents at a wide range of membrane potentials and are believed to contribute to the RMP of neurons and astrocytes (Ryoo and Park, 2016; Verkhratsky and Nedergaard, 2018). In the hippocampus, passive conductance (that is a linear currentvoltage relationship) in astrocytes was reduced following a pharmacological blockade and shRNA-mediated knockdown of TREK 1 and TWIK 1 (Zhou et al., 2009; Mi Hwang et al., 2014), suggesting a contributory role of these channels to the passive conductance and K[+] uptake observed in astrocytes (Seifert et al., 2009). However, there is some contradictory evidence to this as the genetic deletion of TWIK and/or TREK 1 did not alter passive conductance in hippocampal astrocytes (Du et al., 2016). If TWIK 1 and TREK 1 are involved in passive conductance, then differences in astrocytic conductance throughout the CNS suggests potential variability in the expression of these leak channels throughout the brain. Since the passive conductance of astrocytes is thought to be the reason for their ability to buffer K[+] (Tang et al., 2009), this suggests TREK 1 and TWIK 1 might also play a contributory role in the ability of astrocytes to buffer K[+] . Further research is needed to determine if indeed the expression of TREK 1 and TWIK 1 influence K[+] buffering, and to what extent. It is also possible (and likely) these channels are important in determining other functions in astrocytes, further highlighting the need for more research. 

## Voltage-Dependent K[+] Channels Have Distinct Subcellular Localization 

Beyond Kir4.1, several other types of voltage-dependent K[+] (KV) channels, with heterogeneous biophysical properties, have been identified in astrocytes (Verkhratsky and Nedergaard, 2018). As a first example, delayed rectifying K[+] currents have been observed in astrocytes from the spinal cord, hippocampus, cerebellum, and cortex (Bordey and Sontheimer, 2000). The delayed rectifying K[+] 

current ion channel subtype (KD) that mediates these currents has outward rectification and a higher conductance capability at potentials more positive than −50 mV. Transient ‘‘A’’-type currents are a second type of K[+] current present in astrocytes of the cerebrum, hippocampus, spinal cord, and the optic nerve (Sontheimer, 1994). The A-type channels are rapidly activating and inactivating and also require hyperpolarization to remove the tonic inactivation before they can activate (Sontheimer, 1994; Verkhratsky and Nedergaard, 2018). There are also additional subtypes of inward-rectifying K[+] channels beyond Kir4.1 that have been characterized in astrocytes (Bekar et al., 2005). In astrocytes, these voltage-gated K[+] channels are thought to play a role in modulating membrane potential; blockade of Kv channels in cortical astrocytes diminished their ability to repolarize (Wu et al., 2015). Blockade of these channels also reduced the influx of Ca[2+] , suggesting a role of these channels in the regulation of Ca[2+] entry into astrocytes (Wu et al., 2015). 

Various voltage-dependent K[+] channels are expressed in astrocytes; Kv1.1 and Kv1.6 are seen in cortical mouse astrocytes (Smart et al., 1997); Kv1.5 has been observed in the spinal cord and brains of rats, as well as in gliomas of human patients (Preussat et al., 2003). Kv1.3 is also expressed in human gliomas (Preussat et al., 2003). In addition, the subtype and subunit composition of voltage-gated K[+] channels differ across astrocyte subpopulations, at least in the hippocampus. One study found three families of K[+] channels, Kv4, Kv3, and Kv1 that each contributed a different percentage of the A-type currents observed in the hippocampus (about 70, 10 and 5%, respectively; Bekar et al., 2005). These K[+] channels also exhibit distinct subcellular localization in astrocytes; the Kv3.4 subtype was expressed primarily in the processes whereas the Kv4.3 was found localized to the somata (Bekar et al., 2005). The functional implications of this have not been fully elucidated, but do suggest that there may be distinct responses of the subcellular components in astrocytes to changes in voltage. Whether the differential expression of Kv families in hippocampal astrocytes is comparable to astrocytes of other brain regions has not yet been characterized. However, the variability in astrocytic membrane potential, which is partially modulated through voltage-gated K[+] channels, suggests there is likely variability in the expression of these channels across astrocytes of other areas. 

Like Kv3.4 and Kv4.3, the Kv1.3 and Kv1.6 subtypes exhibit distinct subcellular localization. In rat astrocytes, Kv1.3 is expressed on the Golgi apparatus and the Kv1.6 subtype is on the endoplasmic reticulum (Zhu et al., 2014), thus reiterating the heterogeneous nature of astrocytes and astrocyte physiology. 

At least one study has demonstrated that the cAMP/PKA pathway might influence the RMP of astrocytes (Bolton et al., 2006). It is possible that the cAMP pathway regulates RMP through the modulation of voltage-gated K[+] channels. In fact, one study did find that treating cultured astrocytes with activators of the cAMP pathway was sufficient to modulate the expression (both up-and downregulation) of several potassium channels (Paco et al., 2016). Activation of this pathway through neuronal input, intracellular (astrocyte) signals, environmental factors, or some combination of these, might influence the temporal and spatial expression of these channels, and ultimately 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

8 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

the RMP of an astrocyte. Particularly over the course of development, these neuronal inputs, signals and, environmental influences vary greatly from region to region, and this may (in part) explain the diversity of Kv expression and activity in astrocytes. 

Potassium-dependent activity is an integral part of CNS function, and astrocytes play a key role in regulating its levels. Throughout the CNS, astrocytes express these K[+] channels to varying degrees, demonstrating the physiological heterogeneity and diversity of these cells. The functional outcomes of these channel profile differences have not been completely elucidated, but several studies have found a correlation between the expression of particular K[+] channels and cell proliferation (Bordey et al., 2001). Additionally, given that high extracellular K[+] has been linked to neuronal damage, the heterogeneity of astrocytic K[+] channels may represent regional and subregional susceptibility to K[+] -induced neuronal damage. This susceptibility may be particularly exacerbated in times of stress or injury; it is possible that these functional differences may only be observed under reactive conditions, or when the system has been perturbed significantly. 

## Na[+] CHANNELS ARE NOT ONLY EXPRESSED IN NEURONS 

A classic dogma is that voltage-dependent sodium (Na[+] ) channels are only associated with excitable cells, such as neurons, because of their role in driving an action potential. Upon membrane depolarization, these voltage-dependent Na[+] channels open and allow a transient inward Na[+] current, which marks the initiation of the action potential (Pappalardo et al., 2016). However, these voltage-dependent Na[+] channels have also been identified on non-excitable cells, such as Schwann cells, microglia, and astrocytes (Black and Waxman, 2013; Pappalardo et al., 2016). Though these voltage-dependent Na[+] channels are not responsible for action potential initiation in astrocytes, they are thought to play an important role in some astrocytic functions, particularly ion and neurotransmitter homeostasis and reactive astrogliosis (Parpura and Verkhratsky, 2012; Pappalardo et al., 2016; Verkhratsky et al., 2019). Intracellular sodium transients in hippocampal astrocytes have been observed following Schaffer collateral stimulation, suggesting sodium signaling in astrocytes occurs in response to excitatory synaptic activity (Langer and Rose, 2009). Thus, understanding the heterogenous nature of astrocytic Na[+] signaling and channel expression may provide critical insight into astrocyte function. 

Voltage-dependent Na[+] channels consist of an α-subunit, of which there are nine isoforms (Nav1.1–Nav1.9) and a β- subunit of which there are only four isoforms (Pappalardo et al., 2016; Verkhratsky and Nedergaard, 2018). Astrocyte expression of these voltage-gated Na[+] channels has been noted in regions such as the spinal cord, cerebellum, optic nerve, cortex, and hippocampus (Sontheimer et al., 1991; Black et al., 1995; Kressin et al., 1995; Reese and Caldwell, 1999; Schaller and Caldwell, 2003; Ziemens et al., 2019; Rurak et al., 2020). Sodium signals have also been measured in astrocytes of the white matter (Moshrefi-Ravasdjani et al., 2017). In this study, Na[+] transients, 

as determined by changes in the fluorescence of the sodium indicator, SBFI, were observed following glutamate application (Moshrefi-Ravasdjani et al., 2017). 

The (gene) expression of these Nav subtypes has been noted to change across development, at least in cortical astrocytes (Rurak et al., 2020). In this study, the authors combined translating ribosome affinity purification with RNA sequencing (TRAPseq) to measure gene expression changes specifically in cortical astrocytes. Across development, there was significant differential expression of several genes that encode for voltagegated Na[+] channels, including SCN1A (which encodes for the Nav1.1 subtype), SCN3A (Nav1.3), SCN8A (Nav1.6), and SCN11A (Nav1.9; Rurak et al., 2020). Though these differentially expressed genes were not validated using alternative methods (i.e., RT-qPCR), they do suggest that the physiological properties of astrocytes (such as Na[+] channels and signaling) are highly dynamic across development, and extrapolating data to other studies must be done with caution. 

## Na[+] Channel Subtype Expression Is Heterogenous in Astrocytes 

Several of these Na[+] channel subtypes have been observed in this glial population, including Nav1.2, Nav1.3, Nav1.5, and Nav1.6 (Black et al., 1995; Schaller and Caldwell, 2003; Black and Waxman, 2013; Pappalardo et al., 2016). However, there is considerable heterogeneity in Nav subtype expression in astrocytes across the CNS. For example, one study evaluated the expression of Nav 1.2 and Nav 1.3 in cultured astrocytes of the spinal cord and optic nerve (Black et al., 1995). Immunocytochemistry revealed higher levels of Nav 1.2 and Nav 1.3 in spinal cord astrocytes compared to those of the optic nerve (Black et al., 1995). Furthermore, the researchers noted varying expression of these Na[+] channels in morphological subtypes of astrocytes. In particular, spinal cord astrocytes classified as ‘‘stellate’’ had moderate levels of Nav 1.2 but the ‘‘flat’’ astrocytes of this region expressed only low levels of the channel. Similarly, in the optic nerve, the ‘‘stellate’’ astrocytes expressed low levels of Nav 1.2, but this expression was negligible in astrocytes classified as ‘‘flat’’ (Black et al., 1995). This study demonstrates the heterogeneity of some voltage-dependent Na[+] channel subtypes across the CNS and further demonstrates how there is heterogenous expression within astrocytes of a given region. Data from this study suggests astrocyte morphology may be correlated to the diversity of Nav subtype expression. 

Another study in the cerebellum found heterogeneity in Nav expression amongst morphological subtypes of astrocytes in this region. In the cerebellum, Nav1.6 expression has been noted in the processes of Bergmann glia, but the subtype was not identified in astrocytes of the granule cell layer (Schaller and Caldwell, 2003), suggesting again that morphological subtypes of astrocytes express different voltage-dependent Na[+] channels. Interestingly, high expression of Nav1.6 was observed in cerebellar granule cells themselves (Schaller and Caldwell, 2003), implying that Nav expression in astrocytes may, in part, be driven by the expression of these channels in neighboring neurons. Like with the K[+] channels discussed above, it is probable that the heterogenous expression of voltage-dependent 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

9 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

Na[+] channels in astrocytes is the result of the interplay between various intrinsic and extrinsic factors. Understanding all these different influences will help uncover the molecular and electrophysiological underpinnings of the functional differences across astrocytes. 

The heterogenous expression of Nav1.6 may have important implications about an astrocyte’s ability to respond appropriately to injury. Zhu et al. (2016) demonstrated that Nav1.6 expression is significantly upregulated in hippocampal astrocytes following status epilepticus in the kainic acid model of epilepsy and that this upregulation is strongly correlated to the severity of both the seizures and the reactive astrogliosis. Interestingly, the authors noted several lines of evidence demonstrating large voltage-dependent Na[+] currents in reactive astrocytes following seizure (de Lanerolle and Lee, 2005), suggesting that the increase in Nav1.6 in reactive astrocytes may contribute to hyperexcitability in an epileptic brain (Zhu et al., 2016). This may be caused by a Ca[2+] -mediated release of glutamate from astrocytes. Upregulation of Nav1.6 could drive increases in Na[+] influx, which, _via_ the Na[+] /Ca[2+] exchanger, could subsequently induce increases in intracellular Ca[2+] levels, and Ca[2+] -mediated activities like the release of glutamate (Zhu et al., 2016). In an epiletic brain, this mechanism might further drive hyperexcitability and epileptogenesis. It is therefore possible that baseline differences in Nav1.6 expression in astrocytes might be indicative of the potential risk for hyperexcitability following seizure activity. 

Like Nav1.6, the Nav1.5 subtype may play an important role in reactive astrogliosis. Knockdown of Nav1.5 mRNA in primary rat cortical astrocytes resulted in impaired wound closure following a scratch injury (Pappalardo et al., 2014). Furthermore, the scratch injury induced an intracellular Ca[2+] response that was attenuated by the Nav1.5 knockdown (Pappalardo et al., 2014). 

Changes in astrocytic Nav1.5 expression have also been observed in other models of CNS injury. In one study, conditional knockouts lacking Nav1.5 in astrocytes were generated. Compared to wildtype animals, the conditional knockouts developed more severe clinical outcomes in an EAE model of Multiple Sclerosis, though this effect was only observed in female mice (Pappalardo et al., 2018). This suggests that Nav1.5 may be important in mediating the astrocytic response to pathological conditions, though these effects may be sex-specific. Interestingly, some of the astrocytes lacking Nav1.5 appeared to have a more simple morphology compared to those of wildtype animals (Pappalardo et al., 2018). 

## Astrocytic Na[+] Currents Are Linked to Specific Morphologies 

The differences in Nav subtype expression likely underlies variation in astrocytic Na[+] currents and associated pharmacology. Several studies have demonstrated heterogeneity of Na[+] currents in two morphological subclasses of astrocytes (Sontheimer and Waxman, 1992; Sontheimer et al., 1994), suggesting different (morphological) subclasses of astrocytes may express different densities of the various Nav subtypes. Fibrous astrocytes exhibit Na[+] currents comparable to neurons; they tend to activate at relatively depolarized potentials and 

inactivate rapidly. Protoplasmic astrocytes, on the other hand, tend to activate at relatively negative potentials and inactivate more slowly. Additionally, different morphological classes of astrocytes have distinct sensitivities to tetrodotoxin, a blocker of a subset of sodium channel isoforms including Nav1.1–1.4, Nav1.6, and Nav1.7 (Sontheimer et al., 1994). In the spinal cord, the Na[+] currents of astrocytes characterized as ‘‘stellate’’ (with numerous processes) were highly sensitive to tetrodotoxin but those that had a flat or ‘‘pancake’’ morphology exhibited Na[+] currents that were largely resistant to the drug (Sontheimer and Waxman, 1992), highlighting the extensive diversity of the astrocyte population. This suggests morphological subtypes of astrocytes may express different Na[+] channel subtypes, further emphasizing the heterogeneity of this cell population. 

Heterogeneous astrocytic Na[+] signals have also been observed in those from different regions, particularly the neocortex and hippocampus (Ziemens et al., 2019). Neocortical astrocytes exhibited larger intracellular Na[+] transients following glutamate application in slice compared to those of the hippocampus (Ziemens et al., 2019). 

The full extent to which the expression of these sodium channels and currents vary between astrocytes throughout the CNS has not been fully delineated but is imperative given the current evidence which suggests voltage-dependent Na[+] channels are involved in several critical astrocytic functions such as the regulation of ion channels and in response to CNS injury such as epileptogenesis (Qiao et al., 2013; Zhu et al., 2016). It is already established that Na[+] currents appear to differ between morphological subtypes of astrocytes but whether these properties also differ between other subtypes of astrocytes remains to be explored. Nonetheless, the differences in Nav subtype expression and the biophysical and pharmacological properties of Na[+] currents further demonstrate the electrophysiological heterogeneity of astrocytes. 

## MULTIPLE Ca[2+] SIGNALING PATHWAYS IN ASTROCYTES, AN INTEGRAL PART OF ASTROCYTE PHYSIOLOGY 

Traditionally, astrocytes were believed to be passive cells whose sole function was to provide support for neuronal function. However, seminal studies in the 1990s revealed that astrocytes are capable of responding to synaptic activity through increases in intracellular calcium [Ca[2+] ]i levels (Porter and McCarthy, 1995; Pasti et al., 1997; Kang et al., 1998; Agulhon et al., 2008). These effects are also seen in cultured human astrocytes (Navarrete et al., 2013; Hashioka et al., 2014). Since then, calcium signaling cascades have been recognized as an integral part of astrocyte physiology. Importantly, under physiological conditions, both spontaneous and receptor-activated Ca[2+] signals have been observed in astrocytes (Shigetomi et al., 2019). 

Astrocytes express a vast array of G-protein coupled receptors (GPCRs; Shigetomi et al., 2019). In particular, Gαq-linked GPCRs (GqPCRs) are coupled to internal Ca[2+] stores and may be the specific link between changes in [Ca[2+] ]i in response to neurotransmitter release at the synapse (Agulhon et al., 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

10 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

2008). Activation of a GqPCRs leads to the hydrolysis of the membrane lipid phosphatidylinositol 4,5-biphosphate (PIP2) _via_ the enzyme phospholipase C (PLC; Agulhon et al., 2008). This produces diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3), the latter which binds to and activates IP3 receptors on the endoplasmic reticulum membrane, thereby releasing Ca[2+] from intracellular stores (Agulhon et al., 2008). 

There are three isoforms of the IP3 receptor (IP3R; Sherwood et al., 2017). In astrocytes, the IP3R2 subtype appears to be the primary receptor subtype driving the PLC/IP3 pathway (Holtzclaw et al., 2002; Sheppard et al., 2002; Petravicz et al., 2008); deletion of IP3R2 resulted in a lack of spontaneous and GqPCR-induced elevations in Ca[2+] in astrocytes (Petravicz et al., 2008). However, some studies have demonstrated Ca[2+] signals still occur in the astrocytes of mice lacking the IP3R2 subtype (Stobart et al., 2018b), suggesting other mechanisms contribute to intracellular Ca[2+] astrocytic signaling. In fact, a recent study found that the first and third isoforms of IP3R may also contribute to Ca[2+] signaling in astrocytes, albeit to a lesser extent (Sherwood et al., 2017). 

Nonetheless, the IP3R2 subtype plays a particularly important role in Ca[2+] signaling. A study from Holtzclaw et al. (2002) demonstrated distinct regional astrocytic subcellular expression of IP3R2. Astrocytes of the hippocampus expressed IP3R2 in their somata and processes, though there appeared to be a higher density in the large and fine processes. This was also true for cerebellar Bergmann glia in the molecular layer, which had punctate expression of IP3R2 in their finer processes. In contrast, Bergmann glia of the Purkinje cell layer expressed IP3R2 primarily in their somata (Holtzclaw et al., 2002). The study also showed that IP3R2 is particularly enriched in astrocytic processes that encircle synapses, highlighting an important putative role of Ca[2+] signaling in mediating the link between neurotransmission and astroglia. 

## Spontaneous Ca[2+] Oscillations in Astrocytes 

Spontaneous Ca[2+] signaling events occur in the absence of neuronal activity (Parri et al., 2001) and have been observed in astrocytes throughout the CNS including in the hippocampus (Nett et al., 2002; Rungta et al., 2016), cortex, striatum, and thalamus (Parri et al., 2001; Aguado et al., 2002; Jiang et al., 2014); the presence of spontaneous Ca[2+] signals have also been confirmed, at least _in vitro_ , in human astrocytes (Navarrete et al., 2013). They have been observed in Bergmann glia of the cerebellum (Aguado et al., 2002) as well as in astrocytes of the olfactory bulb (Otsu et al., 2015). Both extracellular and intracellular Ca[2+] levels are critical for driving these spontaneous oscillations (Aguado et al., 2002); removal of extracellular Ca[2+] is sufficient to prevent spontaneous Ca[2+] signals _in vitro_ (Aguado et al., 2002) and the loss of the IP3R2 reduces spontaneous events _in vivo_ (Petravicz et al., 2008; Jiang et al., 2016; Yu et al., 2018). However, some reports have noted spontaneous Ca[2+] events even in the astrocytes of IP3R2[−] _[/]_[−] mice (Sherwood et al., 2017), suggesting that these mechanisms are not the only ones that drive spontaneous Ca[2+] signals in astrocytes. Recent evidence from Wu et al. (2019) suggests that the morphology 

of astrocytes may be an important factor in driving these spontaneous Ca[2+] signals- these events were more frequent in thin processes with a high surface-to-volume ratio. Given the extensive morphological heterogeneity of astrocytes, it is possible that the localization of transient Ca[2+] events to thinner processes can explain some of the diversity in astroglial calcium signaling, particularly spontaneous events. The spontaneity of these Ca[2+] signals fluctuate between astrocytes across the CNS, perhaps reflecting diversity in some of these processes. For example, hippocampal astrocytes, specifically of the CA1 _stratum radiatum_ region, have a higher frequency of spontaneous Ca[2+] events than those of the dorsolateral striatum (Chai et al., 2017), but fewer oscillations than those of the cortex (Navarrete et al., 2013), perhaps reflecting regional differences in the mechanisms that drive these spontaneous events. 

In the hippocampus, a subset of astrocytes displayed no spontaneous Ca[2+] signals, but of the astrocytes that did, there was significant variability in the frequency of these events (Nett et al., 2002). Some had fairly frequent Ca[2+] oscillations at intervals between 0.5 and 2 min, whilst others had much more irregular intervals between oscillations, with intervals that exceeded 2 mins (Nett et al., 2002). Similar heterogeneity has been observed in the thalamus; the majority of thalamic astrocytes showed multiple spontaneous Ca[2+] events over a 10-min period but several displayed only one spontaneous Ca[2+] signal in the same time (Parri et al., 2001). In the somatosensory cortex, astrocytes from layer I had nearly double the frequency of spontaneous Ca[2+] activity compared to those from layer II/III (Takata and Hirase, 2008). 

Precisely what the differences in spontaneous Ca[2+] signaling across astrocyte subpopulations mean has yet to be fully elucidated. One study found that hippocampal astrocytes which did not exhibit spontaneous Ca[2+] signals did not differ in morphology or electrophysiology from those that did (Nett et al., 2002), demonstrating that the classification of astrocytes is not so straightforward as one morphological class displaying one set of electrophysiological properties, or molecular markers. Regardless, it is plausible that the differences in these spontaneous Ca[2+] oscillations represent important distinctions between the various types of astrocytes. Astrocytes displaying no spontaneous Ca[2+] are still able to respond to some neurotransmitter release (Nett et al., 2002), but the lack of spontaneous Ca[2+] signals might indicate a decreased ability or less sensitive response to these types of events which normally evoke a Ca[2+] response. 

The mobilization of both intracellular and extracellular Ca[2+] may be another important mechanism driving spontaneous Ca[2+] events (Aguado et al., 2002). Removal of extracellular Ca[2+] blocked spontaneous Ca[2+] events in hippocampal astrocytes in slices (Aguado et al., 2002). Likewise, when thapsigargin, a drug which inhibits endoplasmic reticulum Ca[2+] -ATPase activity and thus depletes ER Ca[2+] stores, was applied to hippocampal slices, spontaneous Ca[2+] activity in astrocytes was blocked. This suggests that intracellular Ca[2+] stores are also necessary for spontaneous Ca[2+] events in astrocytes (Aguado et al., 2002). The lack of spontaneous Ca[2+] activity in astrocytes might therefore reflect a depletion of extracellular or intracellular 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

11 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

Ca[2+] signaling capacity, highlighting the influence of both extrinsic and intrinsic factors in the development of astroglial spontaneous Ca[2+] activity. As with the frequency, the amplitude of these spontaneous astrocyte Ca[2+] transients are variable- both inter-and intra-regionally (Aguado et al., 2002). This is true in several regions including the cortex, hippocampus, thalamus, hypothalamus, and spinal cord (Aguado et al., 2002). The heterogeneity of these spontaneous events is likely the result of regional and subregional diversity in the presence of extracellular Ca[2+] and the available intracellular Ca[2+] stores in astrocytes. 

It is clear that there are subtle differences between astrocytes displaying spontaneous Ca[2+] oscillations and those that do not (Nett et al., 2002). Furthermore, it is clear that of the astrocytes that do exhibit spontaneous Ca[2+] oscillations, they differ significantly in several of their properties including the frequency and the amplitude of these signals. It is possible these distinct spontaneous Ca[2+] oscillations have extensive functional consequences, making the understanding of this heterogeneity pertinent to comprehending the role of astrocytes within the CNS. 

## Astrocytic Ca[2+] Signals Differ in Subcellular Compartments 

Initial studies into astrocytic Ca[2+] signaling focused on cytosolic Ca[2+] signals, primarily in the somata of astrocytes, but the use of genetic encoded calcium indicators (GECIs) have enabled higher resolution visualization of localized Ca[2+] transients in the processes and finer processes of astrocytes (Shigetomi et al., 2013; Stobart et al., 2018a; for a comparison of calcium imaging techniques, see Smith et al., 2018). For example, spontaneous Ca[2+] transients have been observed in the somata, processes, and fine processes of striatal astrocytes (Jiang et al., 2014). These cytosolic and local transients have also been observed in astrocytes of the cortex (Agarwal et al., 2017), hippocampus (Zur Nieden and Deitmer, 2006; Jiang et al., 2014), somatosensory cortex (Wang et al., 2006), and olfactory bulb (Otsu et al., 2015). 

Like the extensive inter-and intraregional variability in the frequency and amplitude of astrocytic Ca[2+] signals, there is substantial data suggesting that these events are also variable across the distinct subcellular compartments of astrocytes. In particular, it seems that spontaneous Ca[2+] events occur more frequently in the processes compared to the somata of astrocytes. One study found the majority of Ca[2+] events (∼85%) were localized to the processes, with a much smaller percentage (∼10%) in the endfeet, and an even smaller percentage (∼5%) in the somata (Bindocci et al., 2017). A very similar distribution of spontaneous Ca[2+] events was seen in astrocytes within the somatosensory cortex, with approximately 80% of those signals occurring in the fine processes (Kanemaru et al., 2014). In astrocytes of the _stratum lucidum_ region of the hippocampus, spontaneous Ca[2+] signals were virtually absent in the somata but were frequently observed in the processes (in fact, there was about an 8-fold greater increase in these events in the processes compared to the somata; Haustein et al., 2014). The high frequency of spontaneous Ca[2+] transients in the fine processes of astrocytes relative to their somata has also been observed in the visual cortex (Asada et al., 2015). 

The spontaneous Ca[2+] transients observed throughout the subcellular compartments of astrocytes also differ in their ability to spread from the source event. In the CA1 region, for example, researchers identified distinct Ca[2+] fluctuations; one fluctuation produced a wave-like property, spreading to adjacent areas, whereas the other produced a restricted response which the authors referred to as a microdomain (Srinivasan et al., 2015). Both types of fluctuations were displayed in the processes, and each differed from fluctuations measured from the somata (Srinivasan et al., 2015). 

Spontaneous Ca[2] transients, while common in astrocytes, vary tremendously in the frequency, amplitude, and even type of fluctuation they produce. These properties differ at the regional, subregional, and subcellular levels. The current literature highlights the complexity of astroglial Ca[2+] signaling at the regional, sub-regional, and cellular level. 

This subcellular heterogeneity of Ca[2+] signals, combined with the varied expression of voltage-dependent and voltageindependent ion channels (such as those discussed previously), suggests that astrocytes possess different electrophysiological profiles amongst distinct microdomains of the cell. Thus, permitting a localized response to environmental changes. These differences in subcellular compartments may also explain voltage-dependent ion channels in astrocytes; while the relatively low membrane resistance and hyperpolarized phenotype would (generally) require highly depolarizing events to activate these channels, the intracellular heterogeneity means there could be local variability in the membrane resistance and RMP of the processes, fine processes, and soma of the astrocyte. 

## ASTROCYTE PHYSIOLOGY INFLUENCES SYNAPTIC NETWORKS 

Thus far, we have summarized the available data on the heterogeneity of astrocyte physiology. But what do these differences mean for the greater network? Does this heterogeneity translate to functional differences between other cells in the network such as neurons? If, and how, these differences may influence the network is not fully understood, but there is some evidence to suggest they can. 

K[+] homeostasis is a critical function of astroglia, but they are not the sole cell type that can buffer this ion. Neurons, too, are able to buffer against K[+] . Not all astrocytes may regulate K[+] equally; for example, the expression of the Kir4.1, a key channel in buffering K[+] , is highly variable amongst astrocytes. In areas where the K[+] buffering capacity of astrocytes is low, then neurons may need to be more active at regulating K[+] to help offset that deficit. This increased activity of neuronal transporters could drive higher energy and metabolic demands, which might, in turn, make these neurons more susceptible to electrical and chemical perturbations. The implications of this heterogeneity in K[+] buffering are not yet understood, but moving forward may be particularly important when considering why some neuronal populations are more susceptible to perturbations and damage than others. 

Several studies have shown a ‘‘wave-like’’ phenomena between astrocytes; that is, a Ca[2+] signal appears in one astrocyte followed 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

12 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

quickly by a Ca[2+] signal in another nearby (Verkhratsky, 2006). This is mediated through the extensive gap junction coupling of astrocytes, forming the ‘‘net-like’’ structure of the glial syncytium and demonstrates how astrocytes can influence surrounding astrocytes. Of course, Ca[2+] signals are only one way astrocytes can influence each other; ions (such as K[+] —see ‘‘Astroglial K[+] Spatial Buffering Mediated Through Kir4.1 Subtype’’ section) can also cross gap junctions as can energy substrates like glucose (Rouach et al., 2008) and lactate (Murphy-Royal et al., 2020). 

It has also been theorized that astrocytic Ca[2+] signals can influence synaptic activity. One study found that spontaneous Ca[2+] signals in hippocampal astrocytes were localized to specific regions in their processes (Nett et al., 2002). These ‘‘microdomains’’ were typically asynchronous, leading the authors to believe the astrocytes might be influencing neurons in a synapse-specific manner. However, they did note some ‘‘wavelike’’ activity between processes of the same astrocyte, suggesting a potential larger influence on the greater synaptic field (Nett et al., 2002). A recent study did find a more direct effect of the glial syncytium on synaptic activity (Murphy-Royal et al., 2020). In this experiment, an acute stressor was sufficient to reduce gap junction coupling between astrocytes, leading to a decrease in energy substrate transport between astrocytes and subsequent impairment in LTP (Murphy-Royal et al., 2020), clearly demonstrating that an intact glia syncytium is necessary for synaptic plasticity. 

## OPTOGENETICS AND DREADDs: PHYSIOLOGICALLY RELEVANT FOR THE STUDY OF ASTROCYTES? 

Understanding the physiology of astrocytes has been challenging partly because of a lack of technology sensitive enough to measure many of these properties. This has been compounded by the inability to directly target and manipulate select populations of astrocytes _in vivo_ . In the past couple of decades, the advent of novel technologies has enabled specific cell populations, such as astrocytes, to be selectively targeted and manipulated, thus permitting more in-depth analysis of their function within the CNS. In particular, optogenetics and DREADDs have been frontrunners for targeting astrocytes. 

With optogenetics, cells of interest are targeted with light-sensitive proteins, known as opsins, which generally exist as ion channels and pumps (Bang et al., 2016). The absorption of a specific wavelength by the opsin induces a conformational change, driving electrical changes across the plasma membrane (Bang et al., 2016). These cellular changes differ extensively depending on the type and variant of opsin used. Channelrhodopsin 2 (ChR2), for example, is a cation channel that is activated specifically by 473 nm (blue) light (Nagel et al., 2003), leading to an influx of cations (namely protons and Na[+] ) that produces membrane depolarization (Boyden et al., 2005). In astrocytes, the cation influx (particularly of Na[+] ) may be important for modulating neuron homeostasis and GABAergic transmission (Parpura and Verkhratsky, 2012). Na[+] signaling in astrocytes (particularly Na[+] influx mediated by 

voltage-dependent Na[+] channels) is thought to be necessary for the activity of the Na[+] /K[+] ATPase pump (Verkhratsky et al., 2019), suggesting a role in the maintenance of ion homeostasis. Additionally, intracellular Na[+] is important in controlling GABA uptake _via_ the GABA transporter (GAT) pathways; decreases in Na[+] can reverse GAT-dependent transport causing GABA to be released (Verkhratsky et al., 2019). However, ChR2 can also allow the influx of Ca[2+] , which has been shown to cause the release of gliostransmitters like ATP (Gourine et al., 2010; Chen et al., 2013) and glutamate (Haydon and Carmignoto, 2006). ChR2 stimulation in astrocytes has been reliably shown to induce changes in intracellular Ca[2+] (Li D. et al., 2012; Figueiredo et al., 2014; Perea et al., 2014; Mederos et al., 2019; Balachandar et al., 2020); these changes have been observed to enhance both excitatory and inhibitory synaptic transmission in the primary visual cortex (Perea et al., 2014). The use of ChR2 to activate astrocytes has also been shown to induce the release of ATP (Gourine et al., 2010; Figueiredo et al., 2014). 

Halorhodopsin, on the other hand, is optimally activated by approximately 590 nm (yellow) light and drives hyperpolarization of cells through the influx of Cl[−] ions (Bang et al., 2016). Cl[−] has been shown to affect outward K[+] currents in cultured astrocytes (Bekar and Walz, 1999), showing that the ion has an important role in mediating astrocyte physiology. Intracellular Cl[−] in astrocytes has also been theorized to play a role in mediating crosstalk between neurons and astrocytes because of its impact on several astrocytic transporters, including the excitatory amino acid transporters EAAT1 and EAAT 2 (GLAST and GLT-1 in rodents, respectively), GAT 1 and 3, and NKCC1 (Wilson and Mongin, 2019). Changes in astrocyte intracellular Cl[−] levels are associated with EAAT activity and the movement of Cl[−] across the membrane is necessary for GAT function (Wilson and Mongin, 2019). Given the apparent role of Cl[−] signaling in astrocyte physiology, the manipulation of this ion may be important for deepening our understanding of Cl[−] function within an astrocyte. Moving forward, the use of halorhodopsin in astrocytes will likely become an invaluable tool. As with neurons, the functional consequences of the use of different opsins will vary significantly in astrocytes. 

Like halorhodopsin, archaerhodopsin (Arch) and archaerhodopsin-T (Arch-T) also respond to yellow or green light (around 532 nm) and drive hyperpolarization of a cell (El-Gaby et al., 2016). However, unlike halorhodopsin, Arch and Arch-T induce hyperpolarization through the efflux of protons (El-Gaby et al., 2016; Poskanzer and Yuste, 2016). This hyperpolarization is sufficient to induce changes in intracellular Ca[2+] in astrocytes; work from Poskanzer and Yuste (2016) showed that Arch activation in cortical astrocytes evoked Ca[2+] transients. These transients appeared primarily in the branches and lasted approximately the same length as those generated from spontaneous events in non-stimulated controls (Poskanzer and Yuste, 2016). However, a slight decrease in the amplitude of these Ca[2+] transients was noted in the Arch-stimulated compared to the non-stimulated astrocytes (Poskanzer and Yuste, 2016), suggesting that optogenetic stimulation may recapitulate some, but not all, physiological properties of astrocytes. Which of these physiological properties are conserved may depend on 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

13 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

the type of opsin used, the region of interest, and the original physiological state of the astrocyte. 

Melanopsin responds to shorter wavelengths of light and is optimally activated by light of about 420–450 nm (blue) light (Newman et al., 2003; Wang et al., 2019). It is slightly different from other opsins as it binds to a GPCR, leading to Ca[2+] signaling _via_ activation of the PLC/IP3 pathway (Mederos et al., 2019). As such, it has been suggested as a good tool for investigating the physiological effects of astrocytes. One recent study transfected melanopsin into hippocampal astrocytes and found that stimulation resulted in robust IP3-dependent Ca[2+] signals in their fine processes and the release of ATP/adenosine at the synapse (Mederos et al., 2019). 

Adaptations to these opsins (particularly ChR2) have been generated in recent years, including ChETA and step function opsins (SFO; Bang et al., 2016). In neurons, ChETA has been shown to induce ultrafast spiking and SFOs are known to produce prolonged, sub-threshold membrane depolarizations (Bang et al., 2016) but how these differences might translate to astrocyte activity is not well characterized. 

Optogenetics provides precise spatial and temporal resolution for the manipulation of cells within the CNS. The high spatial resolution can be obtained _via_ the viral (i.e., adeno-associated virus or lentivirus) transfection of the genetically engineered opsin to a targeted region of interest. Combined with a celltype-specific promoter, a high degree of cell specificity is attainable. The ability to precisely modulate the frequency of light pulses delivered to these regions of interest allows extensive manipulation of these cells, and thus provides a high degree of temporal resolution that is not seen in many other technologies. Optogenetics has been particularly valuable for studying neuronal function throughout the CNS, and in more recent years, the technology is being applied to astrocytes. Since the effects of depolarization and hyperpolarization on astrocyte signaling are not as well understood as these effects in neurons, the relevance and generalizability of optogenetic approaches to manipulate and understand astrocytes remains to be fully elucidated. 

The use of designer receptors exclusively activated by designer drugs (DREADDs) provides an alternative to target cells, particularly astrocytes. DREADDs represent one of the most commonly employed forms of chemogenetics, in which genetically engineered receptors selectively bind ligands to drive transient changes (usually activation or inactivation) in the region of interest (Roth, 2016; Smith et al., 2016). The genetically engineered GPCRs have little to no response to endogenous ligands but a strong response to synthetic ones that are otherwise biologically inert (Bang et al., 2016). When the ligand (or actuator) is introduced, it binds to and activates the receptor, activating the downstream Gq, Gi, or Gs pathways that are coupled with these receptors. 

Activation of neuronal and non-neuronal cells is mediated through DREADDs targeting the Gq signaling pathway, of which the hM3Dq is most frequently used (Alexander et al., 2009; Roth, 2016). Inhibitory DREADDs, which silence neuronal activity, target the Gi pathway, the most common being the hM4Di receptor (Roth, 2016). Traditionally, clozapine-N-oxide 

(CNO) has been used as the chemical actuator for both hM3Dq and hM4Di (as well as several other DREADDs), but new evidence suggesting it can reverse-metabolize to its parent compound, clozapine (Manvich et al., 2018; Walker and Kullmann, 2020), and that it may have poor penetrance into the brain (Bonaventura et al., 2019) has led to the use of newer classes of chemical actuators including Compound 13, Compound 21, JHU37152, and JHU37160 (Bonaventura et al., 2019). 

Like opsins, these receptors can be placed under the control of cell-specific promoters, restricting expression to a particular group of cells. The use of a fluorescent tag such as green fluorescent protein (GFP) allows for easy visualization of the cells expressing the opsin or DREADD of interest. 

Since DREADDs use intracellular Ca[2+] signaling to modulate cell activity, many have suggested they are particularly useful for studying astroglial activity given the integral role of Ca[2+] signaling in astroglial function and communication; that is, the manipulation of astrocytes _via_ the GPCR activation might be physiologically relevant. However, neither DREADDs nor optogenetics may be physiologically relevant for the study of astrocytes unless the unique physiological features of astrocytic subtypes are addressed in the experimental design. 

Due to their low membrane resistance, astrocytes will likely elicit smaller current changes to optogenetic stimulation than neurons. As such, ‘‘stronger’’ or more ‘‘intense’’ stimulation may be needed to elicit a response in astrocytes. Fine-tuning of experimental guidelines is needed to determine what parameters would elicit a physiological response in astrocytes. 

Another important consideration for the manipulation of [Ca[2+] ]i in astrocytes is that the mechanism which induces a rise in [Ca[2+] ]i can influence the speed of the change in these levels (Bazargani and Attwell, 2016). This suggests that the use of opsin variants (such as channelrhodopsin 2, ChR2, and its variant ChETA), which have similar, but differing mechanisms (ChETA has faster kinetics and in neurons has been proven to have more rapid repolarization than ChR2; Gunaydin et al., 2010), may induce changes in [Ca[2+] ]i at varying speeds, possibly contributing to alternative downstream effects. This is further compounded by the regional and subregional diversity of astrocyte physiology previously discussed in this review, rendering rigorous pilot studies essential prior to the use of DREADDs or optogenetics to target astrocytes (see **Figure 2** ). 

One study compared several ChR2 variants; all four variants evaluated were sufficient to induce large increases in [Ca[2+] ]i (Figueiredo et al., 2014). There were no significant differences in the overall [Ca[2+] ]i responses or in the dynamics of these responses between the ChR2 variants (Figueiredo et al., 2014). However, another study found the Ca[2+] -translocating channelrhodopsin (CatCh) variant was more efficient than ChR2 in controlling Ca[2+] elevations in astrocytes (Li D. et al., 2012). This implies that generalizing results from studies that employ different opsin variants may be difficult. Selecting the appropriate opsin variant to employ (i.e., to produce a particular/desired effect) will be further complicated by the diverse nature of astrocytic Ca[2+] signaling. 

Differences between opsin types rather than just opsin variants may also induce significantly different effects. A recent 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

14 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

**==> picture [427 x 299] intentionally omitted <==**

FIGURE 2 | Ca[2+] signaling dynamics are influenced by the mechanism of Ca[2+] induction. Therefore, opsin and designer receptors exclusively activated by designer drug (DREADD) variants that utilize alternative mechanisms to exert their effects may also show varying Ca[2+] responses. These ion channel or receptor kinetics need to be considered when determining the best approach for targeting an astrocyte population. 

study compared the effects of stimulating hippocampal astrocytes with ChR2 and melanopsin (Mederos et al., 2019). Although melanopsin was more efficient at inducing Ca[2+] signals in both the soma and fine processes (referred to as microdomains in this study) of astrocytes, ChR2 stimulation elicited greater amplitude in miniature EPSCs of CA1 pyramidal neurons (Mederos et al., 2019). This effect on synaptic activity also persisted for longer following the ChR2 stimulation. However, these changes were only seen under certain stimulation parameters and not others (Mederos et al., 2019). Despite being ‘‘depolarizing’’ opsins, both melanopsin and ChR2 elicit different Ca[2+] signals and ultimately, different downstream effects. This makes direct comparisons between studies that utilize different opsins difficult and also highlights how opsins may be physiologically relevant for some contexts, but not others. The effects that different opsins have on Ca[2+] dynamics may be important for experimental design. Consideration of the effects that different opsins have on intracellular K[+] and Na[+] levels is also critical given their roles in numerous astrocyte functions. 

In studies where the activity of select cell populations are directly targeted and modulated, it is essential to validate that the expression of the opsin or DREADD is restricted to that population only. Co-localization of the fluorescent tag with a cell-specific marker can confirm the specificity 

of this expression. Within astroglial cells, Ca[2+] signals differ throughout their subcellular compartments, with potentially variable effects. Therefore, the precise subcellular localization of an opsin or DREADD receptor within an astrocyte may modulate the overall effect on that individual cell. Moving forward, it may be important to validate whether the subcellular expression does indeed alter functional outcomes, and what those functional outcomes might be. The physiological relevance of these technologies may therefore be better understood with the full knowledge of the cellular distribution of opsins and DREADD receptors in astrocytes. 

Through gap junction proteins, astrocytes can create a network of interconnected cells. Several studies have demonstrated that calcium waves initiated in one astrocyte can propagate to others surrounding it (Verkhratsky, 2006). This phenomenon was first observed from _in vitro_ culture work; these results were later confirmed in acute slices (Dani et al., 1992; Konietzko and Müller, 1994), and eventually with _in vivo_ experiments (Kuga et al., 2011). Similar effects have been noted with Na[+] signals; several studies have demonstrated the ability of astrocytes to propagate these signals from one cell to another _via_ these gap junctions (Rose and Ransom, 1997; Bernardinelli et al., 2004; Langer et al., 2012; Augustin et al., 2016; MoshrefiRavasdjani et al., 2017). What this means for studies in which 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

15 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

**==> picture [427 x 307] intentionally omitted <==**

FIGURE 3 | The glial syncytium may impact the physiological effects of optogenetics and DREADD technologies (optogenetics illustrated above). The connection of astrocytes _via_ gap junction proteins might produce a “double stimulation” or “spillover” effect. In the diagram above, only a portion of the astrocytes (orange and green) express the opsin of interest. The green astrocyte is first stimulated following the introduction of light into the system, and then again when a neighboring astrocyte (orange) is also stimulated, generating a larger than anticipated response. In the case of “spillover,” astrocytes that do not express the opsin or DREADD in use nonetheless become “stimulated” from the activation of its neighboring astrocytes. In the image above, the purple astrocyte still exhibits a response following light stimulation despite the lack of ChR2 expression. The “stimulation” arises from the influence of the connected astrocyte (orange) that is stimulated _via_ its ChR2 ion channels. 

astroglial cells are manipulated remains to be seen. In most cases, it is unlikely that all astrocytes in a region of interest express the opsin or DREADD receptor. However, _via_ the glial syncytium, it is possible that ‘‘activation’’ of one astrocyte leads to the activation of surrounding astrocytes. In one study, Ca[2+] changes were restricted to only astrocytes expressing the opsin (Arch; Poskanzer and Yuste, 2016). However, only Ca[2+] changes were measured, and it is possible that other ions/substrates were altered in coupled, Arch[−] astrocytes. The potential of Ca[2+] or other compounds to move from a stimulated astrocyte to its coupled neighbors needs to be studied under other parameters and with different opsin and DREADD variants. How far this effect could spread would likely depend on the extent of astroglial coupling within regions of interest. _In vivo_ imaging of astrocytes during optogenetic stimulation or DREADD activation may help answer these questions. 

Importantly, whether this stimulation of one astrocyte leads to the stimulation of other astrocytes will likely also depend on the integrity of the glial syncytium. The Murphy-Royal et al.’s (2020) study described in the previous section found 

acute stress was sufficient to reduce the amount of gap junction coupling between astrocytes. Therefore, the paradigm under which optogenetics is employed could significantly impact the extent to which the optogenetic stimulation of astrocytes ‘‘spreads’’ or influences astrocytes of the neighboring area. As such, optogenetic stimulation of astrocytes under normal, physiological conditions, when presumably the glial syncytium is intact, may have a greater impact than stimulation in a model of stress or injury where this may not be the case. 

Another consideration is the potential of ‘‘double stimulation.’’ An astroglial cell stimulated _via_ optogenetics or DREADDs could, through gap junction coupling, stimulate a neighboring astrocyte. If this astrocyte is also stimulated _via_ optogenetic or DREADD technology, this may result in a ‘‘double stimulation’’ effect, leading to a response much greater than physiological conditions. A stronger response could mean the stimulated astrocytes influence neighboring cells, in particular, neurons, in a manner incompatible with a normal physiological response. The strength of the glial syncytium in a given area may dictate the likelihood that this happens, further highlighting 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

16 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

the necessity of understanding the heterogeneous nature of astrocyte physiology and connectivity. As stress can influence the integrity of the glial syncytium (Murphy-Royal et al., 2020), this (potential) issue of ‘‘double stimulation’’ may be less of a concern in paradigms where the astrocytes are stimulated under conditions of stress or injury/disease. This demonstrates the importance of pilot studies to understand how optogenetics and DREADDs impact astoglial activity (see **Figure 3** ). 

In optogenetic and DREADD studies involving neurons, their heterogeneous nature is taken into consideration when designing experiments. The opsin variant or DREADD, for example, that is used to stimulate or inhibit a GABAergic neuron may differ from that of a glutamatergic or dopaminergic one. This same consideration needs to be taken for astrocytes. The literature shows that like neurons, astrocytes are a completely heterogenous population. They differ extensively in their morphology, electrophysiology, protein expression, and function. These subtypes are important to consider as each type may not respond in the same manner to different opsin and DREADD variants. Moving forward, understanding these subtypes will be crucial for informing experimental design. Greater knowledge of astrocyte electrophysiology will be an essential component for characterizing these astrocyte subtypes. 

Similarly, in neurons, the use of an opsin or DREADD variant largely depends on the desired effect that researchers are looking to elicit. In neurons, these desired effects are typically the facilitation or inhibition of an action potential, driven by depolarization or hyperpolarization of the targeted cell. However, with astrocytes, a depolarization or hyperpolarization will not elicit these same effects. As such, understanding astrocyte physiology, and the heterogeneous nature of this physiology, will be critical for making knowledgeable and appropriate decisions regarding experimental design. 

## CONCLUSION 

The research over the past few decades has demonstrated that astrocytes are a more ‘‘excitable’’ and heterogenous cell 

## REFERENCES 

- Abney, E. R., Bartlett, P. P., and Raff, M. C. (1981). Astrocytes, ependymal cells, and oligodendrocytes develop on schedule in dissociated cell cultures of embryonic rat brain. _Dev. Biol._ 83, 301–310. doi: 10.1016/0012-1606(81) 90476-0 

- Agarwal, A., Wu, P.-H., Hughes, E. G., Fukaya, M., Tischfield, M. A., Langseth, A. J., et al. (2017). Transient opening of the mitochondrial permeability transition pore induces microdomain calcium transients in astrocyte processes. _Neuron_ 93, 587.e7–605.e7. doi: 10.1016/j.neuron.2016. 12.034 

- Aguado, F., Espinosa-Parrilla, J. F., Carmona, M. A., and Soriano, E. (2002). Neuronal activity regulates correlated network properties of spontaneous calcium transients in astrocytes in situ. _J. Neurosci._ 22, 9430–9444. doi: 10.1523/JNEUROSCI.22-21-09430.2002 

- Agulhon, C., Petravicz, J., McMullen, A. B., Sweger, E. J., Minton, S. K., Taves, S. R., et al. (2008). What is the role of astrocyte calcium in neurophysiology? _Neuron_ 59, 932–946. doi: 10.1016/j.neuron.2008.09.004 

- Alexander, G. M., Rogan, S. C., Abbas, A. I., Armbruster, B. N., Pei, Y., Allen, J. A., et al. (2009). Remote control of neuronal activity in transgenic mice expressing 

population than previously believed. They differ in morphology, function, and physiology, though the extent of physiological diversity has not been fully characterized. In this review, we discussed how astrocytes exhibit a wide range of basic electrophysiological properties under basal conditions. The mechanisms underlying homeostatic potassium regulation vary between and within brain regions, as do the specific variants of K[+] channels that mediate this K[+] buffering. Likewise, the Na[+] currents and Na[+] channel subtypes that mediate those currents are also heterogenous in astrocytes. Ca[2+] signaling, a key component of astrocyte physiology is also highly variable. There are several different types of Ca[2+] waves present in astrocytes, and these vary considerably amongst astrocytes across the CNS. Precisely how all these electrophysiological differences influence surrounding network activity is still unclear, but there is some evidence to indicate that they do. For example, asynchronous Ca[2+] microdomains in astrocyte processes likely provides a synapse-specific influence of network activity. This heterogeneity is important to consider for optogenetic and DREADD technologies so that the limitations and generalization of each study can be fully assessed. 

Astrocytes represent a very heterogenous cell population; we have highlighted some of the vast differences between the electrophysiological properties of these cells. Despite the available evidence, there is still a substantial amount of research needed in order to truly understand the extensive diversity of this unique cell population. 

## AUTHOR CONTRIBUTIONS 

JM, MH, CR, and NS wrote the manuscript. JM and NS made the figures. All authors contributed to the article and approved the submitted version. 

## FUNDING 

This work was supported by a Canadian Institute of Health Research Canada Research Chair to NS. 

evolved G protein-coupled receptors. _Neuron_ 63, 27–39. doi: 10.1016/j.neuron. 2009.06.014 

- Allen, N. J., and Eroglu, C. (2017). Cell biology of astrocyte-synapse interactions. _Neuron_ 96, 697–708. doi: 10.1016/j.neuron.2017.09.056 

- Anderson, S., Brismar, T., and Hansson, E. (1995). Effect of external K[+] , Ca[2][+] and Ba[2][+] on membrane potential and ionic conductance in rat astrocytes. _Cell Mol. Neurobiol._ 15, 439–450. doi: 10.1007/BF02071879 

- Annunziato, L., Boscia, F., and Pignataro, G. (2013). Ionic transporter activity in astrocytes, microglia, and oligodendrocytes during brain ischemia. _J. Cereb. Blood Flow Metab._ 33, 969–982. doi: 10.1038/jcbfm.2013.44 

- Araque, A., Carmignoto, G., Haydon, P. G., Oliet, S. H. R., Robitaille, R., and Volterra, A. (2014). Gliotransmitters travel in space and time. _Neuorn_ 81, 728–739. doi: 10.1016/j.neuron.2014.02.007 

- Asada, A., Ujita, S., Nakayama, R., Oba, S., Ishii, S., Matsuki, N., et al. (2015). Subtle modulation of ongoing calcium dynamics in astrocytic microdomains by sensory inputs. _Physiol. Rep._ 3:e12454. doi: 10.14814/phy2. 12454 

- Augustin, V., Bold, C., Wadle, S. L., Langer, J., Jabs, R., Philippot, C., et al. (2016). Functional anisotropic panglial networks in the lateral superior olive. _Glia_ 64, 1892–1911. doi: 10.1002/glia.23031 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

17 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

- Balachandar, L., Montejo, K. A., Castano, E., Perez, M., Moncion, C., Chambers, J. W., et al. (2020). Simultaneous Ca[2][+] imaging and optogenetic stimulation of cortical astrocytes in adult murine brain slices. _Curr. Protoc. Neurosci._ 94:e110. doi: 10.1002/cpns.110 

- Bang, J., Kim, H. Y., and Lee, H. (2016). Optogenetic and chemogenetic approaches for studying astrocytes and gliotransmitters. _Exp. Neurobiol._ 25, 205–221. doi: 10.5607/en.2016.25.5.205 

- Bayraktar, O. A., Bartels, T., Holmqvist, S., Kleshchevnikov, V., Martirosyan, A., Polioudakis, D., et al. (2020). Astrocyte layers in the mammalian cerebral cortex revealed by a single-cell in situ transcriptomic map. _Nat. Neurosci._ 23, 500–509. doi: 10.1038/s41593-020-0602-1 

- Bazargani, N., and Attwell, D. (2016). Astrocyte calcium signaling: the third wave. _Nat. Neurosci._ 19, 182–189. doi: 10.1038/nn.4201 

- Bedner, P., Dupper, A., Hüttmann, K., Müller, J., Herde, M. K., Dublin, P., et al. (2015). Astrocyte uncoupling as a cause of human temporal lobe epilepsy. _Brain_ 138, 1208–1222. doi: 10.1093/brain/awv067 

- Bedner, P., Jabs, R., and Steinhäuser, C. (2020). Properties of human astrocytes and NG2 glia. _Glia_ 68, 756–767. doi: 10.1002/glia.23725 

- Bekar, L. K., Loewen, M. E., Cao, K., Sun, X., Leis, J., Wang, R., et al. (2005). Complex expression and localization of inactivating Kv channels in cultured hippocampal astrocytes. _J. Neurophysiol._ 93, 1699–1709. doi: 10.1152/jn.008 50.2004 

- Bekar, L. K., and Walz, W. (1999). Evidence for chloride ions as intracellular messenger substances in astrocytes. _J. Neurophysiol._ 82, 248–254. doi: 10.1152/jn.1999.82.1.248 

- Bellot-Saez, A., Kékesi, O., Morley, J. W., and Buskila, Y. (2017). Astrocytic modulation of neuronal excitability through K[+] spatial buffering. _Neurosci. Biobehav. Rev._ 77, 87–97. doi: 10.1016/j.neubiorev.2017.03.002 

- Benesova, J., Rusnakova, V., Honsa, P., Pivonkova, H., Dzamba, D., Kubista, M., et al. (2012). Distinct expression/function of potassium and chloride channels contributes to the diverse volume regulation in cortical astrocytes of GFAP/EGFP mice. _PLoS One_ 7:e29725. doi: 10.1371/journal.pone.00 29725 

- Bernardinelli, Y., Magistretti, P. J., and Chatton, J.-Y. (2004). Astrocytes generate Na[+] -mediated metabolic waves. _Proc. Natl. Acad. Sci. U S A_ 101, 14937–14942. doi: 10.1073/pnas.0405315101 

- Bindocci, E., Savtchouk, I., Liaudet, N., Becker, D., Carriero, G., and Volterra, A. (2017). Three-dimensional Ca[2][+] imaging advances understanding of astrocyte biology. _Science_ 356:eaai8185. doi: 10.1126/science.aai8185 

- Black, J. A., and Waxman, S. G. (2013). Noncanonical roles of voltagegated sodium channels. _Neuron_ 80, 280–291. doi: 10.1016/j.neuron.2013. 09.012 

- Black, J. A., Westenbroek, R., Minturn, J. E., Ransom, B. R., Catterall, W. A., and Waxman, S. G. (1995). Isoform-specific expression of sodium channels in astrocytes _in vitro_ : immunocytochemical observations. _Glia_ 14, 133–144. doi: 10.1002/glia.440140208 

- Bolton, S., Greenwood, K., Hamilton, N., and Butt, A. M. (2006). Regulation of the astrocyte resting membrane potential by cyclic AMP and protein kinase A. _Glia_ 54, 316–328. doi: 10.1002/glia.20384 

- Bonaventura, J., Eldridge, M. A. G., Hu, F., Gomez, J. L., Sanchez-Soto, M., Abramyan, A. M., et al. (2019). High-potency ligands for DREADD imaging and activation in rodents and monkeys. _Nat. Commun._ 10:4627. doi: 10.1038/s41467-019-12236-z 

- Bordey, A., Lyons, S. A., Hablitz, J. J., and Sontheimer, H. (2001). Electrophysiological characteristics of reactive astrocytes in experimental cortical dysplasia. _J. Neurophysiol._ 85, 1719–1731. doi: 10.1152/jn.2001.85.4. 1719 

- Bordey, A., and Sontheimer, H. (1998). Electrophysiological properties of human astrocytic tumor cells in situ: enigma of spiking glial cells. _J. Neurophysiol._ 79, 2782–2793. doi: 10.1152/jn.1998.79.5.2782 

- Bordey, A., and Sontheimer, H. (2000). Ion channel expression by astrocytes in situ: comparison of different CNS regions. _Glia_ 30, 27–38. doi: 10.1002/(sici)1098-1136(200003)30:1<27::aid-glia4>3.0.co;2-# 

- Boyden, E. S., Zhang, F., Bamberg, E., Nagel, G., and Deisseroth, K. (2005). Millisecond-timescale, genetically targeted optical control of neural activity. _Nat. Neurosci._ 8, 1263–1268. doi: 10.1038/nn1525 

- Brasko, C., Hawkins, V., De La Rocha, I. C., and Butt, A. M. (2017). Expression of Kir4.1 and Kir5.1 inwardly rectifying potassium channels in 

- oligodendrocytes, the myelinating cells of the CNS. _Brain Struct. Funct._ 222, 41–59. doi: 10.1007/s00429-016-1199-8 

- Brockhaus, J., and Deitmer, J. W. (2002). Long-lasting modulation of synaptic input to Purkinje neurons by Bergmann glia stimulation in rat brain slices. _J. Physiol._ 545, 581–593. doi: 10.1113/jphysiol.2002. 028423 

- Bushong, E. A., Martone, M. E., and Ellisman, M. H. (2004). Maturation of astrocyte morphology and the establishment of astrocyte domains during postnatal hippocampal development. _Int. J. Dev. Neurosci._ 22, 73–86. doi: 10.1016/j.ijdevneu.2003.12.008 

- Butt, A. M., and Jennings, J. (1994). Response of astrocytes to γ-aminobutyric acid in the neonatal rat optic nerve. _Neurosci. Lett._ 168, 53–56. doi: 10.1016/03043940(94)90414-6 

- Cahoy, J. D., Emery, B., Kaushal, A., Foo, L. C., Zamanian, J. L., Christopherson, K. S., et al. (2008). A transcriptome database for astrocytes, neurons, and oligodendrocytes: a new resource for understanding brain development and function. _J. Neurosci._ 28, 264–278. doi: 10.1523/JNEUROSCI. 4178-07.2008 

- Chai, H., Diaz-castro, B., Shigetomi, E., Monte, E., Octeau, J. C., Yu, X., et al. (2017). Neural circuit-specialized astrocytes: transcriptomic, proteomic, morphological, and functional evidence. _Neuron_ 95, 531–549. doi: 10.1016/j. neuron.2017.06.029 

- Chen, J., Tan, Z., Zeng, L. I., Zhang, X., He, Y., Gao, W., et al. (2013). Heterosynaptic long-term depression mediated by ATP released from astrocytes. _Glia_ 61, 178–191. doi: 10.1002/glia.22425 

- Cotrina, M. L., Lin, J. H., López-García, J. C., Naus, C. C., and Nedergaard, M. (2000). ATP-mediated glia signaling. _J. Neurosci._ 20, 2835–2844. doi: 10.1523/JNEUROSCI.20-08-02835.2000 

- Dallérac, G., Chever, O., and Rouach, N. (2013). How do astrocytes shape synaptic transmission? Insights from electrophysiology. _Front. Cell. Neurosci._ 7:159. doi: 10.3389/fncel.2013.00159 

- Dani, J. W., Chernjavsky, A., and Smith, S. J. (1992). Neuronal activity triggers calcium waves in hippocampal astrocyte networks. _Neuron_ 8, 429–440. doi: 10.1016/0896-6273(92)90271-e 

- de Lanerolle, N., and Lee, T.-S. (2005). New facets of the neuropathology and molecular profile of human temporal lobe epilepsy. _Epilepsy Behav._ 7, 190–203. doi: 10.1016/j.yebeh.2005.06.003 

- Deemyad, T., Lüthi, J., and Spruston, N. (2018). Astrocytes integrate and drive action potential firing in inhibitory subnetworks. _Nat. Commun._ 9:4336. doi: 10.1038/s41467-018-06338-3 

- Dossi, E., Vasile, F., and Rouach, N. (2018). Human astrocytes in the diseased brain. _Brain Res. Bull._ 136, 139–156. doi: 10.1016/j.brainresbull.2017. 02.001 

- Du, Y., Kiyoshi, C. M., Wang, Q., Wang, W., Ma, B., Alford, C. C., et al. (2016). Genetic deletion of TREK-1 or TWIK-1/TREK-1 potassium channels does not alter the basic electrophysiological properties of mature hippocampal astrocytes in situ. _Front. Cell. Neurosci._ 10:13. doi: 10.3389/fncel.2016.00013 

- Du, Y., Ma, B., Kiyoshi, C. M., Alford, C. C., Wang, W., and Zhou, M. (2015). Freshly dissociated mature hippocampal astrocytes exhibit passive membrane conductance and low membrane resistance similarly to syncytial coupled astrocytes. _J. Neurophysiol._ 113, 3744–3750. doi: 10.1152/jn.002 06.2015 

- El-Gaby, M., Zhang, Y., Wolf, K., Schwiening, C. J., Paulsen, O., and Shipton, O. A. (2016). Archaerhodopsin selectively and reversibly silences synaptic transmission through altered pH. _Cell Rep._ 16:2259. doi: 10.1016/j. celrep.2016.07.057 

- Fernandez, F. R., Noueihed, J., and White, J. A. (2019). Voltage-dependent membrane properties shape the size but not the frequency content of spontaneous voltage fluctuations in layer 2/3 somatosensory cortex. _J. Neurosci._ 39, 2221–2237. doi: 10.1523/JNEUROSCI.1648-18.2019 

- Figueiredo, M., Lane, S., Stout, R. F., Liu, B., Parpura, V., Teschemacher, A. G., et al. (2014). Comparative analysis of optogenetic actuators in cultured astrocytes. _Cell Calcium_ 56, 208–214. doi: 10.1016/j.ceca.2014.07.007 

- Freeman, M. R. (2010). Specification and morphogenesis of astrocytes. _Science_ 330, 774–778. doi: 10.1126/science.1190928 

- Gnatenco, C., Han, J., Snyder, A. K., and Kim, D. (2002). Functional expression of TREK-2 K[+] channel in cultured rat brain astrocytes. _Brain Res._ 931, 56–67. doi: 10.1016/s0006-8993(02)02261-8 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

18 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

- Gourine, A. V., Kasymov, V., Marina, N., Tang, F., Figueiredo, M. F., Lane, S., et al. (2010). Astrocytes control breathing through pH-dependent release of ATP. _Science_ 329, 571–575. doi: 10.1126/science.1190721 

- Guatteo, E., Stanness, K. A., and Janigro, D. (1996). Hyperpolarization-activated ion currents in cultured rat cortical and spinal cord astrocytes. _Glia_ 16, 196–209. doi: 10.1002/(SICI)1098-1136(199603)16:3<196::AID-GLIA2>3. 0.CO;2-0 

- Gunaydin, L. A., Yizhar, O., Berndt, A., Sohal, V. S., Deisseroth, K., and Hegemann, P. (2010). Ultrafast optogenetic control. _Nat. Neurosci._ 13, 387–392. doi: 10.1038/nn.2495 

- Hashioka, S., Wang, Y. F., Little, J. P., Choi, H. B., Klegeris, A., McGeer, P. L., et al. (2014). Purinergic responses of calcium-dependent signaling pathways in cultured adult human astrocytes. _BMC Neurosci._ 15:18. doi: 10.1186/14712202-15-18 

- Haustein, M. D., Kracun, S., Lu, X.-H., Shih, T., Jackson-Weaver, O., Tong, X., et al. (2014). Conditions and constraints for astrocyte calcium signaling in the hippocampal mossy fiber pathway. _Neuron_ 82, 413–429. doi: 10.1016/j.neuron. 2014.02.041 

- Haydon, P. G., and Carmignoto, G. (2006). Astrocyte control of synaptic transmission and neurovascular coupling. _Physiol. Rev._ 86, 1009–1031. doi: 10.1152/physrev.00049.2005 

- Henneberger, C., Papouin, T., Oliet, S. H. R., and Rusakov, D. A. (2010). Longterm potentiation depends on release of D-serine from astrocytes. _Nature_ 463, 232–236. doi: 10.1038/nature08673 

- Hertz, L., and Chen, Y. (2016). Importance of astrocytes for potassium ion (K[+] ) homeostasis in brain and glial effects of K[+] and its transporters on learning. _Neurosci. Biobehav. Rev._ 71, 484–505. doi: 10.1016/j.neubiorev.2016.09.018 

- Hibino, H., Fujita, A., Iwai, K., Yamada, M., and Kurachi, Y. (2004). Differential assembly of inwardly rectifying K[+] channel subunits, Kir4.1 and Kir5.1, in brain astrocytes. _J. Biol. Chem._ 279, 44065–44073. doi: 10.1074/jbc. M405985200 

- Higashi, K., Fujita, A., Inanobe, A., Tanemoto, M., Doi, K., Kubo, T., et al. (2001). An inwardly rectifying K[+] channel, Kir4.1, expressed in astrocytes surrounds synapses and blood vessels in brain. _Am. J. Physiol. Cell Physiol._ 281, C922–C931. doi: 10.1152/ajpcell.2001.281.3.C922 

- Hinterkeuser, S., Schröder, W., Hager, G., Seifert, G., Blümcke, I., Elger, C. E., et al. (2000). Astrocytes in the hippocampus of patients with temporal lobe epilepsy display changes in potassium conductances. _Eur. J. Neurosci._ 12, 2087–2096. doi: 10.1046/j.1460-9568.2000.00104.x 

- Holtzclaw, L. A., Pandhit, S., Bare, D. J., Mignery, G. A., and Russell, J. T. (2002). Astrocytes in adult rat brain express type 2 inositol 1,4,5-trisphosphate receptors. _Glia_ 39, 69–84. doi: 10.1002/glia.10085 

- Isokawa, M., and McKhann, G. M. (2005). Electrophysiological and morphological characterization of dentate astrocytes in the hippocampus. _J. Neurobiol._ 65, 125–134. doi: 10.1002/neu.20186 

- Jiang, R., Diaz-Castro, B., Looger, L. L., and Khakh, B. S. (2016). Dysfunctional calcium and glutamate signaling in striatal astrocytes from Huntington’s disease model mice. _J. Neurosci._ 36, 3453–3470. doi: 10.1523/JNEUROSCI. 3693-15.2016 

- Jiang, R., Haustein, M. D., Sofroniew, M. V., and Khakh, B. S. (2014). Imaging intracellular Ca[2][+] signals in striatal astrocytes from adult mice using genetically-encoded calcium indicators. _J. Vis. Exp._ 93:e51972. doi: 10.3791/51972 

- Kalsi, A. S., Greenwood, K., Wilkin, G., and Butt, A. M. (2004). Kir4.1 expression by astrocytes and oligodendrocytes in CNS white matter: a developmental study in the rat optic nerve. _J. Anat._ 204, 475–485. doi: 10.1111/j.0021-8782.2004. 00288.x 

- Kanemaru, K., Sekiya, H., Xu, M., Satoh, K., Kitajima, N., Yoshida, K., et al. (2014). _in vivo_ visualization of subtle, transient, and local activity of astrocytes using an ultrasensitive Ca[2][+] indicator. _Cell Rep._ 8, 311–318. doi: 10.1016/j.celrep.2014. 05.056 

- Kang, J., Jiang, L., Goldman, S. A., and Nedergaard, M. (1998). Astrocyte-mediated potentiation of inhibitory synaptic transmission. _Nat. Neurosci._ 1, 683–692. doi: 10.1038/3684 

- Kofuji, P., Biedermann, B., Siddharthan, V., Raap, M., Iandiev, I., Milenkovic, I., et al. (2002). Kir potassium channel subunit expression in retinal glial cells: implications for spatial potassium buffering. _Glia_ 39, 292–303. doi: 10.1002/glia.10112 

- Khakh, B. S., and Deneen, B. (2019). The emerging nature of astrocyte diversity. _Annu. Rev. Neurosci._ 42, 187–207. doi: 10.1146/annurev-neuro-070918050443 

- Kofuji, P., and Newman, E. A. (2004). Potassium buffering in the central nervous system. _Neuroscience_ 129, 1045–1056. doi: 10.1016/j.neuroscience.2004.06.008 

- Konietzko, U., and Müller, C. M. (1994). Astrocytic dye coupling in rat hippocampus: topography, developmental onset, and modulation by protein kinase C. _Hippocampus_ 4, 297–306. doi: 10.1002/hipo.450040313 

- Kressin, K., Kuprijanova, E., Jabs, R., Seifert, G., and Steinhäuser, C. (1995). Developmental regulation of Na[+] and K[+] conductances in glial cells of mouse hippocampal brain slices. _Glia_ 15, 173–187. doi: 10.1002/glia.440150210 

- Kuga, N., Sasaki, T., Takahara, Y., Matsuki, N., and Ikegaya, Y. (2011). Large-scale calcium waves traveling through astrocytic networks _in vivo_ . _J. Neurosci._ 31, 2607–2614. doi: 10.1523/JNEUROSCI.5319-10.2011 

- Langer, J., and Rose, C. R. (2009). Synaptically induced sodium signals in hippocampal astrocytes in situ. _J. Physiol._ 587, 5859–5877. doi: 10.1113/jphysiol.2009.182279 

- Langer, J., Stephan, J., Theis, M., and Rose, C. R. (2012). Gap junctions mediate intercellular spread of sodium between hippocampal astrocytes in situ. _Glia_ 60, 239–252. doi: 10.1002/glia.21259 

- Lanjakornsiripan, D., Pior, B. J., Kawaguchi, D., Furutachi, S., Tahara, T., Katsuyama, Y., et al. (2018). Layer-specific morphological and molecular differences in neocortical astrocytes and their dependence on neuronal layers. _Nat. Commun._ 9:1623. doi: 10.1038/s41467-018-03940-3 

- Li, D., Hérault, K., Isacoff, E. Y., Oheim, M., and Ropert, N. (2012). Optogenetic activation of LiGluR-expressing astrocytes evokes anion channel-mediated glutamate release. _J. Physiol._ 590, 855–873. doi: 10.1113/jphysiol.2011. 219345 

- Li, Y.-K., Wang, F., Wang, W., Luo, Y., Wu, P.-F., Xiao, J.-L., et al. (2012). Aquaporin-4 deficiency impairs synaptic plasticity and associative fear memory in the lateral amygdala: involvement of downregulation of glutamate transporter-1 expression. _Neuropsychopharmacology_ 37, 1867–1878. doi: 10.1038/npp.2012.34 

- Liddelow, S. A., Guttenplan, K. A., Clarke, L. E., Bennett, F. C., Bohlen, C. J., Schirmer, L., et al. (2017). Neurotoxic reactive astrocytes are induced by activated microglia. _Nature_ 541, 481–487. doi: 10.1038/nature21029 

- Liedtke, W., Edelmann, W., Bieri, P. L., Chiu, F. C., Cowan, N. J., Kucherlapati, R., et al. (1996). GFAP is necessary for the integrity of CNS white matter architecture and long-term maintenance of myelination. _Neuron_ 17, 607–615. doi: 10.1016/s0896-6273(00)80194-4 

- Ma, B., Xu, G., Wang, W., Enyeart, J. J., and Zhou, M. (2014). Dual patch voltage clamp study of low membrane resistance astrocytes in situ. _Mol. Brain_ 7:18. doi: 10.1186/1756-6606-7-18 

- Mahmoud, S., Gharagozloo, M., Simard, C., and Gris, D. (2019). Astrocytes maintain glutamate homeostasis in the CNS by controlling the balance between glutamate uptake and release. _Cells_ 8:184. doi: 10.3390/cells8 020184 

- Manvich, D. F., Webster, K. A., Foster, S. L., Farrell, M. S., Ritchie, J. C., Porter, J. H., et al. (2018). The DREADD agonist clozapine N-oxide (CNO) is reverse-metabolized to clozapine and produces clozapine-like interoceptive stimulus effects in rats and mice. _Sci. Rep._ 8:3840. doi: 10.1038/s41598-01822116-z 

- Mederos, S., Hernández-Vivanco, A., Ramírez-Franco, J., Martín-Fernández, M., Navarrete, M., Yang, A., et al. (2019). Melanopsin for precise optogenetic activation of astrocyte-neuron networks. _Glia_ 67, 915–934. doi: 10.1002/glia. 23580 

- Mi Hwang, E., Kim, E., Yarishkin, O., Ho Woo, D., Han, K.-S., Park, N., et al. (2014). A disulphide-linked heterodimer of TWIK-1 and TREK-1 mediates passive conductance in astrocytes. _Nat. Commun._ 5:3227. doi: 10.1038/ncomms4227 

- Miller, S. J. (2018). Astrocyte heterogeneity in the adult central nervous system. _Front. Cell. Neurosci._ 12:401. doi: 10.3389/fncel.2018.00401 

- Mishima, T., and Hirase, H. (2010). _in vivo_ intracellular recording suggests that gray matter astrocytes in mature cerebral cortex and hippocampus are electrophysiologically homogeneous. _J. Neurosci._ 30, 3093–3100. doi: 10.1523/JNEUROSCI.5065-09.2010 

- Moore, Y. E., Conway, L. C., Wobst, H. J., Brandon, N. J., Deeb, T. Z., and Moss, S. J. (2019). Developmental regulation of KCC2 phosphorylation 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

19 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

- has long-term impacts on cognitive function. _Front. Mol. Neurosci._ 12:173. doi: 10.3389/fnmol.2019.00173 

- Moshrefi-Ravasdjani, B., Hammel, E. L., Kafitz, K. W., and Rose, C. R. (2017). Astrocyte sodium signalling and panglial spread of sodium signals in brain white matter. _Neurochem. Res._ 42, 2505–2518. doi: 10.1007/s11064-017 -2197-9 

- Murphy-Royal, C., Johnston, A. D., Boyce, A. K. J., Diaz-Castro, B., Institoris, A., Peringod, G., et al. (2020). Stress gates an astrocytic energy reservoir to impair synaptic plasticity. _Nat. Commun._ 11:2014. doi: 10.1038/s41467-02015778-9 

- Nagel, G., Szellas, T., Huhn, W., Kateriya, S., Adeishvili, N., Berthold, P., et al. (2003). Channelrhodopsin-2, a directly light-gated cation-selective membrane channel. _Proc. Natl. Acad. Sci. U S A_ 100, 13940–13945. doi: 10.1073/pnas. 1936192100 

- Navarrete, M., Perea, G., Fernandez de Sevilla, D., Gómez-Gonzalo, M., Núñez, A., Martín, E. D., et al. (2012). Astrocytes mediate _in vivo_ cholinergic-induced synaptic plasticity. _PLoS Biol._ 10:e1001259. doi: 10.1371/journal.pbio.10 01259 

- Navarrete, M., Perea, G., Maglio, L., Pastor, J., Garcia de Sola, R., and Araque, A. (2013). Astrocyte calcium signal and gliotransmission in human brain tissue. _Cereb. Cortex_ 23, 1240–1246. doi: 10.1093/cercor/bhs122 

- Neprasova, H., Anderova, M., Petrik, D., Vargova, L., Kubinova, S., Chvatal, A., et al. (2007). High extracellular K[+] evokes changes in voltage-dependent K[+] and Na[+] currents and volume regulation in astrocytes. _Pflugers Arch._ 453, 839–849. doi: 10.1007/s00424-006-0151-9 

- Nett, W. J., Oloff, S. H., and McCarthy, K. D. (2002). Hippocampal astrocytes in situ exhibit calcium oscillations that occur independent of neuronal activity. _J. Neurophysiol._ 87, 528–537. doi: 10.1152/jn.002 68.2001 

- Newman, L. A., Walker, M. T., Brown, R. L., Cronin, T. W., and Robinson, P. R. (2003). Melanopsin forms a functional short-wavelength photopigment. _Biochemistry_ 42, 12734–12738. doi: 10.1021/bi035418z 

- O’Connor, E. R., Sontheimer, H., Spencer, D. D., and De Lanerolle, N. C. (1998). Astrocytes from exhibit human hippocampal epileptogenic foci action potential-like responses. _Epilepsia_ 39, 347–354. doi: 10.1093/cid/ ciab196 

- Oberheim, N. A., Takano, T., Han, X., He, W., Lin, J. H. C., Wang, F., et al. (2009). Uniquely hominid features of adult human astrocytes. _J. Neurosci._ 29, 3276–3287. doi: 10.1523/JNEUROSCI.4707-08.2009 

- Oberheim, N. A., Wang, X., Goldman, S., and Nedergaard, M. (2006). Astrocytic complexity distinguishes the human brain. _Trends Neurosci._ 29, 547–553. doi: 10.1016/j.tins.2006.08.004 

- Olsen, M. L., Higashimori, H., Campbell, S. L., Hablitz, J. J., and Sontheimer, H. (2006). Functional expression of Kir4.1 channels in spinal cord astrocytes. _Glia_ 53, 516–528. doi: 10.1002/glia.20312 

- Orkand, R. K., Nicholls, J. G., and Kuffler, S. W. (1966). Effect of nerve impulses on the membrane potential of glial cells in the central nervous system of amphibia. _J. Neurophysiol._ 29, 788–806. doi: 10.1152/jn.1966.29. 4.788 

- Otsu, Y., Couchman, K., Lyons, D. G., Collot, M., Agarwal, A., Mallet, J.-M., et al. (2015). Calcium dynamics in astrocyte processes during neurovascular coupling. _Nat. Neurosci._ 18, 210–218. doi: 10.1038/nn.3906 

- Paco, S., Hummel, M., Plá, V., Sumoy, L., and Aguado, F. (2016). Cyclic AMP signaling restricts activation and promotes maturation and antioxidant defenses in astrocytes. _BMC Genomics_ 17:304. doi: 10.1186/s12864-0162623-4 

- Pappalardo, L. W., Black, J. A., and Waxman, S. G. (2016). Sodium channels in astroglia and microglia. _Glia_ 64, 1628–1645. doi: 10.1002/glia. 22967 

- Pappalardo, L. W., Samad, O. A., Black, J. A., and Waxman, S. G. (2014). Voltage-gated sodium channel Nav 1.5 contributes to astrogliosis in an _in vitro_ model of glial injury _via_ reverse Na[+] /Ca[2][+] exchange. _Glia_ 62, 1162–1175. doi: 10.1002/glia.22671 

- Pappalardo, L. W., Samad, O. A., Liu, S., Zwinger, P. J., Black, J. A., and Waxman, S. G. (2018). Nav1.5 in astrocytes plays a sex-specific role in clinical outcomes in a mouse model of multiple sclerosis. _Glia_ 66, 2174–2187. doi: 10.1002/glia.23470 

- Parpura, V., Basarsky, T. A., Liu, F., Jeftinija, K., Jeftinija, S., and Haydon, P. G. (1994). Glutamate-mediated astrocyte-neuron signalling. _Nature_ 369, 744–747. doi: 10.1038/369744a0 

- Parpura, V., Grubisi´c,ˇ V., and Verkhratsky, A. (2011). Ca[2][+] sources for the exocytotic release of glutamate from astrocytes. _Biochim. Biophys. Acta_ 1813, 984–991. doi: 10.1016/j.bbamcr.2010.11.006 

- Parpura, V., and Verkhratsky, A. (2012). Homeostatic function of astrocytes: Ca[2][+] and Na[+] signalling. _Transl. Neurosci._ 3, 334–344. doi: 10.2478/s13380-0120040-y 

- Parri, H. R., Gould, T. M., and Crunelli, V. (2001). Spontaneous astrocytic Ca[2][+] oscillations in situ drive NMDAR-mediated neuronal excitation. _Nat. Neurosci._ 4, 803–812. doi: 10.1038/90507 

- Pasti, L., Volterra, A., Pozzan, T., and Carmignoto, G. (1997). Intracellular calcium oscillations in astrocytes: a highly plastic, bidirectional form of communication between neurons and astrocytes in situ. _J. Neurosci._ 17, 7817–7830. doi: 10.1523/JNEUROSCI.17-20-07817.1997 

- Perea, G., Yang, A., Boyden, E. S., and Sur, M. (2014). Optogenetic astrocyte activation modulates response selectivity of visual cortex neurons _in vivo_ . _Nat. Commun._ 5:3262. doi: 10.1038/ncomms4262 

- Perez, E. J., Tapanes, S. A., Loris, Z. B., Balu, D. T., Sick, T. J., Coyle, J. T., et al. (2017). Enhanced astrocytic d-serine underlies synaptic damage after traumatic brain injury. _J. Clin. Invest._ 127, 3114–3125. doi: 10.1172/JCI 92300 

- Petravicz, J., Fiacco, T. A., and McCarthy, K. D. (2008). Loss of IP3 receptordependent Ca[2][+] increases in hippocampal astrocytes does not affect baseline CA1 pyramidal neuron synaptic activity. _J. Neurosci._ 28, 4967–4973. doi: 10.1523/JNEUROSCI.5572-07.2008 

- Poopalasundaram, S., Knott, C., Shamotienko, O. G., Foran, P. G., Dolly, J. O., Ghiani, C. A., et al. (2000). Glial heterogeneity in expression of the inwardly rectifying K[+] channel, Kir4.1, in adult rat CNS. _Glia_ 30, 362–372. doi: 10.1002/(sici)1098-1136(200006)30:4<362::aid-glia50>3.0.co;2-4 

- Porter, J. T., and McCarthy, K. D. (1995). GFAP-positive hippocampal astrocytes in situ respond to glutamatergic neuroligands with increases in [Ca[2+] ]i. _Glia_ 13, 101–112. doi: 10.1002/glia.440130204 

- Poskanzer, K. E., and Yuste, R. (2016). Astrocytes regulate cortical state switching _in vivo_ . _Proc. Natl. Acad. Sci. U S A_ 113, E2675–E2684. doi: 10.1073/pnas. 1520759113 

- Prebil, M., Jensen, J., Zorec, R., and Kreft, M. (2011). Astrocytes and energy metabolism. _Arch. Physiol. Biochem._ 117, 64–69. doi: 10.3109/13813455.2010. 539616 

- Preussat, K., Beetz, C., Schrey, M., Kraft, R., Wölfl, S., Kalff, R., et al. (2003). Expression of voltage-gated potassium channels Kv1.3 and Kv1.5 in human gliomas. _Neurosci. Lett._ 346, 33–36. doi: 10.1016/s0304-3940(03) 00562-7 

- Qian, X., Shen, Q., Goderie, S. K., He, W., Capela, A., Davis, A. A., et al. (2000). Timing of CNS cell generation: a programmed sequence of neuron and glial cell production from isolated murine cortical stem cells. _Neuron_ 28, 69–80. doi: 10.1016/s0896-6273(00)00086-6 

- Qiao, X., Werkman, T. R., Gorter, J. A., Wadman, W. J., and van Vliet, E. A. (2013). Expression of sodium channel α subunits 1.1, 1.2 and 1.6 in rat hippocampus after kainic acid-induced epilepsy. _Epilepsy Res._ 106, 17–28. doi: 10.1016/j. eplepsyres.2013.06.006 

- Reese, K. A., and Caldwell, J. H. (1999). Immunocytochemical localization of NaCh6 in cultured spinal cord astrocytes. _Glia_ 26, 92–96. doi: 10.1002/(sici)1098-1136(199903)26:1<92::aid-glia10>3.0.co;2-4 

- Rose, C. R., and Ransom, B. R. (1997). Gap junctions equalize intracellular Na[+] concentration in astrocytes. _Glia_ 20, 299–307. doi: 10.1002/(sici)10981136(199708)20:4<299::aid-glia3>3.0.co;2-1 

- Roth, B. L. (2016). DREADDs for neuroscientists. _Neuron_ 89, 683–694. doi: 10.1016/j.neuron.2016.01.040 

- Rouach, N., Koulakoff, A., Abudara, V., Willecke, K., and Giaume, C. (2008). Astroglial metabolic networks sustain hippocampal synaptic transmission. _Science_ 322, 1551–1555. doi: 10.1126/science.1164022 

- Rungta, R. L., Bernier, L.-P., Dissing-Olesen, L., Groten, C. J., LeDue, J. M., Ko, R., et al. (2016). Ca[2][+] transients in astrocyte fine processes occur _via_ Ca[2][+] influx in the adult mouse hippocampus. _Glia_ 64, 2093–2103. doi: 10.1002/glia. 23042 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

20 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

- Rurak, G. M., Simard, S., Charih, F., Van Geel, A., Stead, J., Woodside, B., et al. (2020). Translatomic database of cortical astroglia across male and female mouse development reveals two distinct developmental phenotypes. _bioRxiv_ [Preprint]. doi: 10.1101/681684 

- Ryoo, K., and Park, J.-Y. (2016). Two-pore domain potassium channels in astrocytes. _Exp. Neurobiol._ 25, 222–232. doi: 10.5607/en.2016. 25.5.222 

- Schaller, K. L., and Caldwell, J. H. (2003). Expression and distribution of voltage-gated sodium channels in the cerebellum. _Cerebellum_ 2, 2–9. doi: 10.1080/14734220309424 

- Schröder, W., Hager, G., Kouprijanova, E., Weber, M., Schmitt, A. B., Seifert, G., et al. (1999). Lesion-induced changes of electrophysiological properties in astrocytes of the rat dentate gyrus. _Glia_ 28, 166–174. doi: 10.1002/(sici)10981136(199911)28:2<166::aid-glia8 _>_ 3.0.co;2-t 

- Seifert, G., Hüttmann, K., Binder, D. K., Hartmann, C., Wyczynski, A., Neusch, C., et al. (2009). Analysis of astroglial K[+] channel expression in the developing hippocampus reveals a predominant role of the Kir4.1 subunit. _J. Neurosci._ 29, 7474–7488. doi: 10.1523/JNEUROSCI.3790-08.2009 

- Shen, Y., Kyu Han, S., and Dong Ryu, P. (2018). Comparison of electrophysiological properties of two types of pre-sympathetic neurons intermingled in the hypothalamic paraventricular nucleus. _J. Vet. Sci._ 19, 483–491. doi: 10.4142/jvs.2018.19.4.483 

- Sheppard, C. A., Simpson, P. B., Sharp, A. H., Nucifora, F. C., Ross, C. A., Lange, G. D., et al. (2002). Comparison of type 2 inositol 1,4,5-trisphosphate receptor distribution and subcellular Ca[2][+] release sites that support Ca[2][+] waves in cultured astrocytes. _J. Neurochem._ 68, 2317–2327. doi: 10.1046/j.14714159.1997.68062317.x 

- Sherwood, M. W., Arizono, M., Hisatsune, C., Bannai, H., Ebisui, E., Sherwood, J. L., et al. (2017). Astrocytic IP3 Rs: contribution to Ca[2][+] signalling and hippocampal LTP. _Glia_ 65, 502–513. doi: 10.1002/glia. 23107 

- Shigetomi, E., Bushong, E. A., Haustein, M. D., Tong, X., Jackson-Weaver, O., Kracun, S., et al. (2013). Imaging calcium microdomains within entire astrocyte territories and endfeet with GCaMPs expressed using adeno-associated viruses. _J. Gen. Physiol._ 141, 633–647. doi: 10.1085/jgp.201210949 

- Shigetomi, E., Saito, K., Sano, F., and Koizumi, S. (2019). Aberrant calcium signals in reactive astrocytes: a key process in neurological disorders. _Int. J. Mol. Sci._ 20:996. doi: 10.3390/ijms20040996 

- Sloan, S. A., and Barres, B. A. (2014). Mechanisms of astrocyte development and their contributions to neurodevelopmental disorders. _Curr. Opin. Neurobiol._ 27, 75–81. doi: 10.1016/j.conb.2014.03.005 

- Smart, S. L., Bosma, M. M., and Tempel, B. L. (1997). Identification of the delayed rectifier potassium channel, Kv1.6, in cultured astrocytes. _Glia_ 20, 127–134. doi: 10.1002/(sici)1098-1136(199706)20:2 _<_ 127::aid-glia4 _>_ 3.0.co;2-6 

- Smith, K. S., Bucci, D. J., Luikart, B. W., and Mahler, S. V. (2016). DREADDS: use and application in behavioral neuroscience. _Behav. Neurosci._ 130, 137–155. doi: 10.1037/bne0000135 

- Smith, N. A., Kress, B. T., Lu, Y., Chandler-Militello, D., Benraiss, A., and Nedergaard, M. (2018). Fluorescent Ca[2][+] indicators directly inhibit the Na,K-ATPase and disrupt cellular functions. _Sci. Signal._ 11:eaal2039. doi: 10.1126/scisignal.aal2039 

- Sofroniew, M. V., and Vinters, H. V. (2010). Astrocytes: biology and pathology. _Acta Neuropathol._ 119, 7–35. doi: 10.1007/s00401-0090619-8 

- Somjen, G. G. (1979). Extracellular potassium in the mammalian central nervous system. _Annu. Rev. Physiol._ 41, 159–177. doi: 10.1146/annurev.ph.41.030179. 001111 

- Sontheimer, H. (1994). Voltage-dependent ion channels in glial cells. _Glia_ 11, 156–172. doi: 10.1002/glia.440110210 

- Sontheimer, H., Fernandez-Marques, E., Ullrich, I. N., Pappas, C. A., and Waxman, S. G. (1994). Astrocyte Na[+] channels are required for maintenance of Na[+] /K[+] -ATPase activity. _J. Neurosci._ 14, 2464–2475. doi: 10.1523/JNEUROSCI.14-05-02464.1994 

- Sontheimer, H., Minturn, J. E., Black, J. A., Ransom, B. R., and Waxman, S. G. (1991). Two types of Na[+] -currents in cultured rat optic nerve astrocytes: changes with time in culture and with age of culture derivation. _J. Neurosci. Res._ 30, 275–287. doi: 10.1002/jnr.490300202 

- Sontheimer, H., and Waxman, S. G. (1992). Ion channels in spinal cord astrocytes _in vitro_ . II. Biophysical and pharmacological analysis of two Na[+] current types. _J. Neurophysiol._ 68, 1001–1011. doi: 10.1152/jn.1992.68.4.1001 

- Srinivasan, R., Huang, B. S., Venugopal, S., Johnston, A. D., Chai, H., Zeng, H., et al. (2015). Ca[2][+] signaling in astrocytes from Ip3r2−/− mice in brain slices and during startle responses _in vivo_ . _Nat. Neurosci._ 18, 708–717. doi: 10.1038/nn.4001 

- Stephan, J., Haack, N., Kafitz, K. W., Durry, S., Koch, D., Hochstrate, P., et al. (2012). Kir4.1 channels mediate a depolarization of hippocampal astrocytes under hyperammonemic conditions in situ. _Glia_ 60, 965–978. doi: 10.1002/glia. 22328 

- Stobart, J. L., Ferrari, K. D., Barrett, M. J. P., Glück, C., Stobart, M. J., Zuend, M., et al. (2018a). Cortical circuit activity evokes rapid astrocyte calcium signals on a similar timescale to neurons. _Neuron_ 98, 726.e4–735.e4. doi: 10.1016/j. neuron.2018.03.050 

- Stobart, J. L., Ferrari, K. D., Barrett, M. J. P., Stobart, M. J., Looser, Z. J., Saab, A. S., et al. (2018b). Long-term _in vivo_ calcium imaging of astrocytes reveals distinct cellular compartment responses to sensory stimulation. _Cereb. Cortex_ 28, 184–198. doi: 10.1093/cercor/bhw366 

- Takata, N., and Hirase, H. (2008). Cortical layer 1 and layer 2/3 astrocytes exhibit distinct calcium dynamics _in vivo_ . _PLoS One_ 3:e2525. doi: 10.1371/journal. pone.0002525 

- Takata, N., Mishima, T., Hisatsune, C., Nagai, T., Ebisui, E., Mikoshiba, K., et al. (2011). Astrocyte calcium signaling transforms cholinergic modulation to cortical plasticity _in vivo_ . _J. Neurosci._ 31, 18155–18165. doi: 10.1523/JNEUROSCI.5289-11.2011 

- Tan, G., Sun, S.-Q., and Yuan, D.-L. (2008). Expression of Kir 4.1 in human astrocytic tumors: correlation with pathologic grade. _Biochem. Biophys. Res. Commun._ 367, 743–747. doi: 10.1016/j.bbrc.2008.01.014 

- Tang, X., Taniguchi, K., and Kofuji, P. (2009). Heterogeneity of Kir4.1 channel expression in glia revealed by mouse transgenesis. _Glia_ 57, 1706–1715. doi: 10.1002/glia.20882 

- Verkhratsky, A. (2006). Glial calcium signaling in physiology and pathophysiology 1. _Acta Pharmacol. Sin._ 27, 773–780. doi: 10.1111/j.1745-7254.2006. 00396.x 

- Verkhratsky, A., and Nedergaard, M. (2018). Physiology of astroglia. _Physiol. Rev._ 98, 239–389. doi: 10.1152/physrev.00042.2016 

- Verkhratsky, A., Parpura, V., Vardjan, N., and Zorec, R. (2019). Physiology of astroglia. _Adv. Exp. Med. Biol._ 1175, 45–91. doi: 10.1007/978-981-13-99 13-8_3 

- Walker, M. C., and Kullmann, D. M. (2020). Optogenetic and chemogenetic therapies for epilepsy. _Neuropharmacology_ 168:107751. doi: 10.1016/j. neuropharm.2019.107751 

- Walz, W. (1982). Do neuronal signals regulate potassium flow in glial cells? Evidence from an invertebrate central nenrous system. _J. Neurosci. Res._ 7, 71–79. doi: 10.1002/jnr.490070108 

- Wang, X., Lou, N., Xu, Q., Tian, G.-F., Peng, W. G., Han, X., et al. (2006). Astrocytic Ca[2][+] signaling evoked by sensory stimulation _in vivo_ . _Nat. Neurosci._ 9, 816–823. doi: 10.1038/nn1703 

- Wang, F., Smith, N. A., Xu, Q., Fujita, T., Baba, A., Matsuda, T., et al. (2012). Astrocytes modulate neural network activity by Ca[2][+] -dependent uptake of extracellular K[+] . _Sci. Signal._ 5:ra26. doi: 10.1126/scisignal.20 02334 

- Wang, M., Xu, Z., Liu, Q., Sun, W., Jiang, B., Yang, K., et al. (2019). Nongenetic optical modulation of neural stem cell proliferation and neuronal/glial differentiation. _Biomaterials_ 225:119539. doi: 10.1016/j.biomaterials.2019. 119539 

- Wilhelm, I., Nyúl-Tóth, Á., Suciu, M., Hermenean, A., and Krizbai, I. A. (2016). Heterogeneity of the blood-brain barrier. _Tissue Barriers_ 4:e1143544. doi: 10.1080/21688370.2016.1143544 

- Wilson, C. S., and Mongin, A. A. (2019). The signaling role for chloride in the bidirectional communication between neurons and astrocytes. _Neurosci. Lett._ 689, 33–44. doi: 10.1016/j.neulet.2018.01.012 

- Wu, Y.-W., Gordleeva, S., Tang, X., Shih, P.-Y., Dembitskaya, Y., Semyanov, A., et al. (2019). Morphological profile determines the frequency of spontaneous calcium events in astrocytic processes. _Glia_ 67, 246–262. doi: 10.1002/glia. 23537 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

21 

Astrocyte Ion Channels and Physiology 

McNeill et al. 

- Wu, K.-C., Kuo, C.-S., Chao, C.-C., Huang, C.-C., Tu, Y.-K., Chan, P., et al. (2015). Role of voltage-gated K[+] channels in regulating Ca[2][+] entry in rat cortical astrocytes. _J. Physiol. Sci._ 65, 171–177. doi: 10.1007/s12576-015-0356-9 

- Xin, W., Schuebel, K. E., Jair, K.-W., Cimbro, R., De Biase, L. M., Goldman, D., et al. (2019). Ventral midbrain astrocytes display unique physiological features and sensitivity to dopamine D2 receptor signaling. _Neuropsychopharmacology_ 44, 344–355. doi: 10.1038/s41386-018-0151-4 

- Yu, X., Taylor, A. M. W., Nagai, J., Golshani, P., Evans, C. J., Coppola, G., et al. (2018). Reducing astrocyte calcium signaling _in vivo_ alters striatal microcircuits and causes repetitive behavior. _Neuron_ 99, 1170.e9–1187.e9. doi: 10.1016/j. neuron.2018.08.015 

- Zaitzev, A. V., Povysheva, N. V., Gonzalez-Burgos, G., and Lewis, D. A. (2012). Electrophysiological classes of layer 2/3 pyramidal cells in monkey prefrontal cortex. _J. Neurophysiol._ 108, 595–609. doi: 10.1152/jn.00859.2011 

- Zhang, Y., Sloan, S. A., Clarke, L. E., Grant, G. A., Gephart, M. G. H., and Correspondence, B. A. B. (2016). Purification and characterization of progenitor and mature human astrocytes reveals transcriptional and functional differences with mouse. _Neuron_ 89, 37–53. doi: 10.1016/j.neuron.2015. 11.013 

- Zhong, S., Du, Y., Kiyoshi, C. M., Ma, B., Alford, C. C., Wang, Q., et al. (2016). Electrophysiological behavior of neonatal astrocytes in hippocampal stratum radiatum. _Mol. Brain_ 9:34. doi: 10.1186/s13041-016-0213-7 

- Zhou, M., Schools, G. P., and Kimelberg, H. K. (2006). Development of GLAST[+] astrocytes and NG2[+] glia in rat hippocampus CA1: mature astrocytes are electrophysiologically passive. _J. Neurophysiol._ 95, 134–143. doi: 10.1152/jn. 00570.2005 

- Zhou, M., Xu, G., Xie, M., Zhang, X., Schools, G. P., Ma, L., et al. (2009). TWIK1 and TREK-1 are potassium channels contributing significantly to astrocyte 

- passive conductance in rat hippocampal slices. _J. Neurosci._ 29, 8551–8564. doi: 10.1523/JNEUROSCI.5784-08.2009 

- Zhu, J., Yan, J., and Thornhill, W. B. (2014). The Kv1.3 potassium channel is localized to the cis-Golgi and Kv1.6 is localized to the endoplasmic reticulum in rat astrocytes. _FEBS J._ 281, 3433–3445. doi: 10.1111/febs.12871 

- Zhu, H., Zhao, Y., Wu, H., Jiang, N., Wang, Z., Lin, W., et al. (2016). Remarkable alterations of Nav1.6 in reactive astrogliosis during epileptogenesis. _Sci. Rep._ 6:38108. doi: 10.1038/srep38108 

- Ziemens, D., Oschmann, F., Gerkau, N. J., and Rose, C. R. (2019). Heterogeneity of activity-induced sodium transients between astrocytes of the mouse hippocampus and neocortex: mechanisms and consequences. _J. Neurosci._ 39, 2620–2634. doi: 10.1523/JNEUROSCI.2029-18.2019 

- Zur Nieden, R., and Deitmer, J. W. (2006). The role of metabotropic glutamate receptors for the generation of calcium oscillations in rat hippocampal astrocytes in situ. _Cereb. Cortex_ 16, 676–687. doi: 10.1093/cercor/ bhj013 

**Conflict of Interest** : The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. 

_Copyright © 2021 McNeill, Rudyk, Hildebrand and Salmaso. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms_ . 

Frontiers in Cellular Neuroscience | www.frontiersin.org 

May 2021 | Volume 15 | Article 644126 

22 

