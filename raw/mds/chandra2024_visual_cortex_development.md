bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

# 1 Self-organized emergence of modularity, hierarchy, and mirror 2 reversals from competitive synaptic growth in a developmental 3 model of the visual pathway 

2 

3 

4 

5 

6 7 

8 

Sarthak Chandra[†1] , Mikail Khona[†1,2] , Talia Konkle[3] , and Ila R. Fiete[1] 

†Denotes equal contribution 

1Department of Brain and Cognitive Sciences & McGovern Institute, MIT 

2Department of Physics, MIT 

3Department of Psychology, Harvard University 

## **Abstract** 

9 10 A hallmark of the primate visual system is its _architectural organization_ consisting of multiple distinct (modu11 lar) areas that connect hierarchically. These areas exhibit specific _spatial organization_ on the cortical sheet, with 12 primary visual cortex at the center and subsequent regions in the hierarchy encircling the earlier one, and detailed 13 _topological organization_ , with retinotopy in each area but striking mirror reversals across area boundaries. The 14 developmental rules that drive the simultaneous formation of these architectural, spatial, and topographic aspects 15 of organization are unknown. Here we demonstrate that a simple synaptic growth rule driven by spontaneous 16 activity and heterosynaptic competition generates a detailed connectome of the visual pathway, with emergence 17 of all three types of organization. We identify a theoretical principle — local greedy wiring minimization via spon18 taneous drive (GWM-S) — implemented by the mechanism, and use this insight to propose biologically distinct 19 growth rules that predict similar endpoints but testably distinguishable developmental trajectories. The same 20 rules predict how input geometry and cortical geometry together drive emergence of hierarchical, convolution21 like, spatially and topographically organized sensory processing pathways for different modalities and species, 22 providing a possible explanation for the observed pluripotency of cortical structure formation. We find that the 23 few parameters governing structure emergence in the growth rule constitute simple knobs for rich control, that 24 could (potentially genetically) encode a projection neuron-like connectivity patterns and interneuron-like ones. 25 In all, the presented rules provide a parsimonious mechanistic model for the organization of sensory cortical hi26 erarchies even without detailed genetic cues for features like map reversal, and provide numerous predictions for 27 experiment during normal and perturbed development. 

28 The visual cortex of primates consists of multiple discrete visual areas. Each area provides full coverage of the 29 visual field, and the areas process information sequentially and hierarchically. The scale and semantic content of 30 features increases along the hierarchy. Areas in the early visual cortex such as V1, V2, V3, V4, and some areas in 31 the lateral occipital cortex preserve the global topography of visual inputs to the retina [1, 2, 3, 4, 5, 6, 7]. This 32 mapping of nearby locations on the retina to nearby regions of cortex, or retinotopy, is similar to the topographical 33 mapping of inputs seen in other sensory cortices [8, 9, 10]. These hierarchically connected early visual areas must 34 somehow be fit into one two-dimensional cortical sheet while also preserving topographic order. In primates, this 35 is accomplished by spatially organizing areas in a concentric way such that V2 surrounds V1, and so on [11]. 

36 In mammals from mice to humans, all three kinds of order — hierarchical, spatial, and topographic — are 37 present before eye-opening or in utero, prior to the receipt of detailed visual stimuli and even before photoreceptors 38 are present [12, 13, 14, 15, 16]. These and other observations suggest that genetic cues and internally generated 39 activity, rather than detailed external visual inputs, drive synaptic wiring. These factors lead to the formation of 40 discrete visual areas and their hierarchical, spatial and topographic organization during development [13]. 

41 Developmental biology is spanned by two polar hypotheses. One states that genes directly specify the detailed 42 endpoint architecture of organisms and brains (that brain regions are discrete, how many there are, and their 43 hierarchical connectivity), spatial layout (which part of the cortical sheet the regions occupy and the locations and 44 shapes of their boundaries), and topography (the nature of retinotopic order). This aligns with the chemoaffinity 45 hypothesis of Roger Sperry [17], the positional hypothesis of Lewis Wolpert [18] and extensive experimental 46 work showing a role for genetic hard-wiring or specification [19, 20, 21, 22, 23, 24]. The opposite hypothesis 47 is that the brain is a highly plastic system, a blank slate whose organization is created and shaped by external 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

48 inputs. This aligns with Karl Lashley’s doctrine of mass action [25], Turing’s pattern formation hypothesis [26], 49 and experimental work showing the flexible process of digit formation [27] and the potential of any region of 50 cortex to develop the properties of another with the right inputs [28]. 

51 In this work, we espouse a third hypothesis aligned with the body of work in modern developmental biology 52 showing a middle-path between these poles: in which genes specify a very small number of parameters [29, 30, 53 31, 32, 33] of a developmental growth process or program, and rich structure then gradually emerges via the 54 unfolding over time of this dynamical process [34, 35, 36]. In other words, structure is created from a dance 55 involving small amounts of genetic information interacting with a largely emergent and self-organizing dynamical 56 process, such that neither genetic information nor external inputs perform endpoint specification. The process 57 involves internally generated spontaneous activity and states that feed back into the unfolding dynamics and 58 serve as context for the next steps of emergence [37]. This view is supported by a body of experiments on cell 59 differentiation, embryogenesis, and in the specific case of the visual system the development of the topographic 60 retinotectal projection [13, 38]. The hypothesis of a bare-bones genetic scaffolding that sets a few parameters of 61 a developmental program, which then unfolds in an activity-dependent way, also opens the door to explaining 62 the fascinating pluripotency of cortical development: that when driven by visual inputs, auditory cortex develops 63 signatures of visual processing [28]. 

64 We explore how much brain structure can be induced by the unfolding of simple synaptic growth rules from 65 stimulus-independent spontaneous activity. We consider that competition between neurons and synapses to in66 nervate targets is a cornerstone mechanism for self-organization within and across areas in cortex [39, 40, 41]. 67 Similar competitive dynamics have been shown to organize the one-to-one precise and efficient neural control 68 of muscle fibers at the neuromuscular junction [42, 43, 44] and the crystalline organization of the cerebellum 69 such that multiple climbing fibers that initially innervate cerebellar Purkinje cells are winnowed to a single win70 ner [45]. Competitive models are also consistent with the emergence of sequential premotor neural activity in 71 songbird HVC [46, 47] and with rodent cortex [48]. Finally, the mammalian visual system has provided some 72 of the earliest and continuing evidence of the role of competitive innervation processes[49, 50, 13, 51]. Though 73 our focus in on mammalian circuit development, there is mounting evidence that even in the fly, an ideal of the 74 chemoaffinity hypothesis, there is a critical role for the self-organization of structure driven by spontaneous activity 75 [32, 38, 30, 52, 53]. 

76 We find that a simple learning rule, based on presynaptic activity-dependent synaptic growth and heterosynap77 tic competition[46] can organize an unstructured cortical sheet into a set of discrete regions that are hierarchically 78 connected, with concentric spatial organization on the cortical sheet. Moreover, the topographic order of regions 79 within the hierarchy combines the topography of the inputs with the geometry of the cortical sheet. In the vi80 sual input case the result is retinotopic order with mirror reversals observed in topography at region boundaries 81 [9, 8, 1]. Further, the resulting connectivity between adjacent regions in the hierarchy naturally yields a multi82 scale receptive field structure, with emergent signatures like the eccentricity-dependence of visual receptive fields 83 and local interneuron connectivity coexisting with projection neurons that form the hierarchy. The same rules, 84 applied to cortical sheets with different geometry or different input modality, can explain the organization of visual 85 cortex in different species and the hierarchical organization of various sensory modalities. Finally, we show that 86 this mechanistic process arrives at an endpoint of a local, greedy wiring connectome — offering an alternative to 87 prevalent global wiring minimization theories of cortical circuits [54]. 

- 88 In sum, the model bridges vastly different levels, from a small key set of putatively genetically specified param89 eters and the subcellular dynamics of synaptic growth and competition, to the mesoscopic organization of maps 90 within cortical regions, to the macroscopic organization of hierarchies between areas. As a result, it provides 91 multiple testable predictions for molecular neuroscience including transcriptomics; developmental neuroscience; 92 and connectomics. 

## 93 

## **Results** 

## 94 **Initial architecture, retinal activity, and competitive activity-dependent synaptic growth** 

- 95 The ingredients of our model are: 1) Spontaneous activity in the retinal inputs, putatively driven by retinal waves. 96 2) Topographic putative thalamic layout with all-to-all (non-topographic) projections into an undifferentiated 97 sheet of cortical neurons [55] with (non-topographic) all-to-all cortico-cortical connectivity. 3) A synaptic growth 98 rate determined by presynaptic activity and soma-to-synapse distance, with heterosynaptic competition between 99 synapses at each presynaptic and postsynaptic neuron [46]. 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [466 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
a unparcellated  b c Growth + heterosynaptic competition rules<br>      cortex<br>visual field LGN<br>visual hemi-field LGN to cortex<br>retina<br>unparcellated hemi-cortex<br>**----- End of picture text -----**<br>


Figure 1: **Initial architecture, and competitive synaptic growth rules** : (a) A schematic of the visual pathway in primates, wherein visual information is acquired by the retina, and is relayed through the Lateral Geniculate Nucleus(LGN) to reach the visual cortex. We construct our initial architecture based on this structure, beginning with an initially unparcellated cortex. (b) A schematic of our setup, where the visual hemifield of visual input is mapped onto an area representing the LGN. This area is then assumed to lie above and project to a sheet of latent cortical neurons. (c) Top: Synapses grow at a rate that depends on presynaptic activity ( _a j_ ) and inversely with the soma-dendritic distance ( _di j_ ). Bottom: The heterosynaptic competition rule: If the sum of incoming (resp. outgoing) weights exceeds a bound ( _Wmax_ ), all synapses undergo depression, a rule that proportionally penalizes weak synapses more than strong ones. Each individual synapse also has a weight bound _wmax < Wmax_ (not depicted). 

100 **Initial model architecture and inputs** We focus on the development of one hemisphere of the visual cortex, and 101 thus restrict the retinal inputs to one visual hemifield, Fig. 1a. Retinal drive, which is retinotopically organized in 102 its projection to an idealized LGN, is scaled in area by the log-conformal transformation [56, 57], Fig. 1b. To start 103 with minimal assumptions about pre-existing connectivity structure in cortex, the connectivity from this idealized 104 LGN to the undifferentiated and unparcellated cortical sheet [55] and within the cortical sheet is set as all-to-all, 105 Fig. 1b. Thus, there are no initial area divisions, topography, or hierarchy in cortex. (We will investigate other 106 versions of unstructured initial connectivity later.) 

107 **Spontaneous activity** Over development, the retina exhibits spontaneous activity in the form of retinal waves 108 [58, 59, 60, 61] that can drive activity in LGN and V1[58, 62]. These inputs have been linked to the formation of 109 the initial visual map before eye-opening [13, 63, 59, 64], and disruptions lead to some visual deficits [65]. 110 We assume that the propagation of retinal activity waves is relatively fast ( _∼_ 10’s of seconds [58]) while synap111 tic growth and decay is slow (minutes to days [66]) and depends on activity only through the magnitude of 112 presynaptic activity. Therefore, for the current model the spatio-temporal dynamics of the retinal wave patterns 113 are unimportant and on the timescale of plasticity we can replace retinal activity by its average value, which will 114 look like wide-field excitation. 

115 **Synaptic growth and competition rules** We consider a model of synaptic growth driven by presynaptic activity, 116 consistent with experiments [67, 68, 43, 69], Fig.1c. Critically, we assume that the growth rate of a synapse 117 is inversely modified by a distance variable: for cortico-cortical synapses, this distance takes the form of actual 118 soma-synapse distance along the neural arbors, putatively because of costs associated with resource trafficking; 119 for LGN-cortical synapses, this might be an effective distance set by a tract path (e.g. axons must travel along a 120 direct LGN-occipital cortex tract and then to innervate other parts of occipital cortex must grow further). The rate 121 of growth of synapse _i j_ , from neuron _j_ to neuron _i_ , is proportional to _∆i j_ : 

121 

**==> picture [273 x 28] intentionally omitted <==**

122 where _di j/d_ 0 is a relative soma-to-synapse distance normalized by a length-scale parameter _d_ 0, and _a j_ is the 123 presynaptic firing rate. 

124 Synapses compete with each other pre- and post-synaptically to drive the postsynaptic neuron [43, 69, 46]: 125 whenever the summed weights into or out of a neuron exceed a threshold ( _W_ max), all the weights into or out of 126 that neuron, respectively, are decremented by a small absolute amount _ε_ , Fig. 1c. This rule is highly competitive, 127 in that small weights are penalized by a larger fraction than large ones, resulting in sparse connectivity with a few 128 strong weights dominating. Each synapse is individually capped at a strength _w_ max ( _< W_ max), and weights are kept 129 non-negative, thus distributing connections across roughly _k_ = _W_ max _/w_ max synapses per neuron. These bounds 130 might be different for incoming versus outgoing connections and across neurons, but for simplicity we set them to 131 be identical unless otherwise specified. Note that the “weights” grown in the model represent a developmentally 132 developed skeleton, that can be later refined and trained based on visual inputs. 

133 Activity propagates across synapses of strength greater than a threshold of _εw ≪ w_ max. Neural activity propa134 gates linearly across synapses satisfying this threshold, with the magnitude of activity attenuated by a factor _γ_ for 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [377 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>90<br>135 45<br>θ<br>180 0<br>225 315<br>270<br>time<br>b d<br>hierarchical modularity<br>       4 hops<br>       3 hops<br>       2 hops      1 hop V4V3 +- [*]<br>LGN to cortex grown hemi-cortex V2 V2- [V3] -<br>c -<br>V1 V1<br>+<br>*<br>V2+V3+<br>**----- End of picture text -----**<br>


Figure 2: **The emergence of a hierarchical connectome from biologically plausible competitive growth rules:** (a) Beginning with all-to-all potential recurrent connectivity within cortex and from the putative LGN to cortex, the heterosynaptic competition rule (Fig. 1c) results in the pruning of synapses (top). The angular distribution of postsynaptic target neurons for each neuron in the network grows more directional (bottom). (b) In the formed network, neuron hierarchy can be assigned on the basis of the smallest number of hops with which they are connected to LGN.(c) The heterosynaptic competition growth, based on presynpatic activity, proceeds with each area forming a large number of initial connections (as seen as the wide light-blue shaded area) which are then pruned, eventually leading to the spontaneous emergence of another succeeding area (as determined by the connectivity, (b)).(d) The fully grown and stabilized network forms a set of discrete areas that abut and encircle each other (left), which matches the spatial layout of early visual cortical areas in humans [1](right) 

## 135 

## each synapse crossed (see _methods_ for details). 

## 136 

## **Emergence of a hierarchy of discrete areas with concentric spatial arrangement** 

137 Simulating the competitive growth dynamics with spontaneous retinal activity, starting from an unstructured 138 input projection (one-to-all projections) and a maximally unstructured cortical sheet (all-to-all connectivity), Fig. 139 2a, results in a network with a cellular-resolution synaptic connectome that exhibits remarkable self-organized 140 emergence of order. Initially weak weights strengthen based on distance, so that the shortest-distance connections 141 are strengthened while the heterosynaptic competition penalizes the weaker (and thus longer-distance) ones. 142 Cortical neurons receiving the shortest-distance inputs from LGN gain the strongest weights earliest. As a result, 143 the inputs to these neurons mature fastest (by hitting their saturated values of 0, _w_ max), and their inputs from 144 elsewhere in cortex weaken. These neurons are the most active, and most effectively able to saturate the weights 145 of their postsynaptic partners, for their closest partners. The strongly competitive process sends most connections 146 to zero, an effective pruning strategy. 

147 The distribution of outgoing weights of neurons in the cortical sheet becomes increasingly focused and direc148 tional, Fig. 2a (bottom). We characterize neurons based on the smallest number of hops with which they are 149 connected to the LGN, Fig. 2b. Initially, all neurons are a single hop from LGN, but as the simulation proceeds, 150 Fig. 2c, most neurons lose single-hop LGN connectivity because the nearest cortical neurons to LGN monopolize 151 the LGN outputs. The outgoing weights from the strongly driven single-hop cortical neurons drive their closest 152 neighbors, to render them two-hop neurons, and so on. As the synaptic dynamics proceed, the neurons stratify 153 into a clear hierarchy of independent discrete regions: neurons that are a single hop away from LGN, two hops 154 away from LGN and so on, Fig. 2d (left). We simulated these dynamics until four such discrete regions emerged 155 (Fig. 2d (left); continued simulation resulted in the formation of additional areas until the available cortical sheet 156 was exhausted, SI Fig. S1). 

157 The formed regions are spatially organized on the cortical sheet in a concentric arrangement: the 4-hop region 158 surrounds the 3-hop region, which encircles the 2-hop region; the 1-hop region is at the center. We putatively call 159 these regions V1, V2, V3, and V4, respectively, Fig. 2d (left). This arrangement of V1, V2 and V3 in our model 160 closely resembles human cortex, in particular in the posterior-medial part of the occipital lobe[1, 2], Fig. 2d 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [380 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>V4<br>probe stimulus V3V2<br>V1<br>fixation point<br>b eccentricity c polar angle<br>-90 90<br>**----- End of picture text -----**<br>


**==> picture [92 x 94] intentionally omitted <==**

Figure 3: **The emergence of mirrored map topography from biologically plausible competitive growth rules:** (a) Probing network organization to characterize which neurons respond to point stimuli in the visual field. (b) Neurons on the cortical sheet, colored by their response as a function of radial distance from the fixation point, generate an _eccentricity map_ (left), with the corresponding map from human experiments [1] (right). (c) _Polar angle map_ (angles from _−π/_ 2 on the lower vertical meridian up to _π/_ 2 on the upper vertical meridian with 0 at the horizontal meridian (left)). Note the alternations in polar angle, in contrast to the smooth eccentricity map. Connectomically defined emergent area boundaries based on the number of hops from LGN (cf. Fig. 2b,d) appear to exactly coincide with the emergent polar angle reversal locations. These reversals occur at the representations of the horizontal and vertical meridians. Polar angle alternations measured in humans [1] (right). 

## 161 (right). 

162 The size of each area is controlled by the ratio of number of incoming to outgoing connections, which is 163 approximately given by the ratio of the total incoming synaptic threshold to the total outgoing synaptic threshold 164 _k[in] /k[out]_ = _W_ max[incoming] _/W_ max[outgoing] , SI Fig. S2. 

## 165 

## **Emergence of retinotopy and polar angle alternation** 

166 To determine whether there is topographic order in each area of the formed cortical hierarchy, we use standard 167 receptive field mapping procedures, Fig. 3a, [1, 70]. Localized pulses of input in the retinal space drive activity 168 in downstream neurons. Each neuron in the network is then colored based on its preferred retinal location, using 169 different colorings to visualize the mapping of radial eccentricity and polar angle, Fig 3b-c. 

170 We find that retinal/LGN eccentricity is preserved in the mapping to cortex, within each area and between 171 areas: there is a globally smooth and monotonic mapping from retinal eccentricity to eccentricity representation 172 in the cortex, Fig. 3b (left). More-foveal regions map to one part of the cortical sheet, with an eccentricity gradient 173 that is similar across areas and runs along (parallel to) the area boundaries. This topography in eccentricity, with 174 the log-conformal transformation in LGN, closely matches recordings from human cortex, Fig. 3b (right) [1, 57]. 

175 The representation of polar angle is different: Each brain region exhibits local topography for polar angle, but 176 the 90–270 _[◦]_ polar angle representation is split in two halves, represented by the upper and lower halves of each 177 of the horseshoe-shaped visual area. In contrast to the eccentricity map, polar angle gradients run orthogonal to 178 area boundaries and there is not a globally smooth topographic mapping of polar angle across the hierarchy of 179 areas, Fig. 3c. Polar angle representations exhibit striking mirror reversals at the region boundaries. 

180 This emergent result also matches the findings from human visual cortex, Fig. 3c [1]. Indeed, mirror rever181 sals in polar angle are used to determine area boundaries in many experimental settings [1]. In the model, the 182 independent measure of area boundaries based on hops from LGN aligns perfectly with mirror reversal locations. 

183 We believe that this is the first synapse-level mechanistic model of architectural, spatial, and topographic struc184 ture emergence in primate visual systems, including the emergence of discrete areas with hierarchical architecture, 185 spatial organization with concentric areas on a cortical sheet, and topographic organization of eccentricity with 186 polar angle reversals coincident with area boundaries. It provides a possible mechanism for the mysterious origin 187 of polar angle alternations, for which there are no known underlying genetic gradient signals [71]. 

## 188 

## **Distillation of a principle for structure emergence: local greedy wiring minimization** 

189 The potent structure-inducing effects of the growth with heterosynaptic competition rule (Eq. 1) suggest the 190 possibility of a general principle at work. Conceptually, spontaneous retinal activity drives the growth of output 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [461 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
a LGN link placement order e f<br>    input  shortest    first V4 V4<br>saturated  shortest      input<br>shortest      first saturated<br>     first V1 V1 V2 V1 V2V3<br>V3 V3<br>b c d<br>V2 V2<br>V1 V1<br>visual field<br>coordinates<br>V3V4<br>V2<br>V1<br>hierarchy<br>**----- End of picture text -----**<br>


Figure 4: **Theoretical principle: Local greedy wiring minimization rule for the emergence of multiple mirrored hierarchical visual areas:** (a) A schematic of the greedy wiring minimization principle (left to right): synapses with presynaptic neurons in the previous completely formed area are placed in order of increasing wiring length until all presynaptic neurons saturate in out-degree. The postsynaptic neurons form the next area, and the process continues for this newly formed area. Color denotes the time at which the synapse stabilized. (b-d) The visual hierarchy grown according to the process highlighted above shows the formation of discrete areas with concentric spatial organization of these areas, and mapping (b), polar angle reversals (c) and topographic eccentricity representation (d). (e) Each neuron in the cortical sheet is placed along the z-axis according to its position in the formed hierarchy (left), then positioned on the x-y plane according to the center of its receptive field in visual field coordinates (right). Neurons are colored by eccentricity in (e) and by polar angle in (f). 

191 connections from LGN to cortex. Distance-dependent growth (Eq. 1) promotes more-rapid strengthening of short192 distance connections to cortex and within cortex. Simultaneously, the presynaptic activity-dependent growth term 193 means that LGN inputs to cortical cells outcompete cortical inputs to cortical cells. Together, these two effects 194 result in the shortest-distance LGN-to-cortex connections strengthening relative to and at the cost of all other 195 LGN-cortical and cortico-cortical connections. In this way, the very strongly LGN-driven set has become V1, an 196 area strongly innervated by LGN, Fig. 4a (left). 

197 These V1 neurons have an advantage over all other cortical neurons as potential presynaptic partners to other 198 cortical neurons, because of their higher (LGN-driven) activity. Within this V1 set, neurons closest to the edge 199 of the set have an advantage, because their connections to the surrounding cortical pool are the shortest and 200 strengthen first. Neurons in the interior of V1 are left to strengthen their synapses to available cortical neurons 201 further away. In this way, neurons at the V1 edge outcompete others to innervate the neurons nearest the edge, 202 and neurons at the V1 core connect the furthest away, Fig. 4a (second panel). This is the basis for topographic 203 mirror reversals. As the outputs of V1 saturate and inputs to the edge-proximal target population become strong, 204 this population gains an edge in strengthening its outputs to the remaining cortical neurons, and the next area 205 and mirror-reversal take shape, Fig. 4a (remaining panels). 206 These insights allow us to hypothesize that the dynamics induced by the learning rule can be distilled into a 207 simple and mathematically principled process that we call _local greedy wiring minimization via spontaneous drive_ 208 _(GWM-S for short)_ : starting from a progenitor set of neurons with some topographic ordering of features, in our 209 case the LGN, and a pool of potential target neurons (in our case the undifferentiated cortex), let the progenitor 210 neuron with the closest potential target create a connection at maximal strength to that target. Place the next211 nearest connection next (it might belong to the same or another progenitor neuron or end at the same or another 212 target neuron), and so on. Each neuron can place and receive a maximum of _m_ connections. Once the progenitor 213 set is saturated, the most-strongly innervated set becomes the progenitor set, and the connection placement process 214 repeats, until all cells are saturated or until cells in the target pool have run out (pseudocode and further detail 215 in the _Methods_ ). The process is _local_ because growth at any point is focused on a subset of cells (growth does 216 not happen globally); it is _greedy_ because it proceeds through placement of the shortest available connections at 217 the current moment and from the current set, rather than performing absolute wiring length minimization on the 218 global circuit (as considered in earlier works [72, 54, 73, 74]). 

219 Running the GWM-S process on our initial network recapitulates the architecture, spatial organization, and to220 pography that result from the neural growth and heterosynaptic competition rules, Fig. 4b-d. Thus, neural growth 221 with heterosynaptic competition is a biologically plausible mechanistic process that implements the principle of 222 GWM-S. 

223 **Three conceptually similar but biologically distinct rules reproduce visual hierarchy emer-** 224 **gence** 

225 The distillation of structure emergence dynamics into the GWM-S process suggests that other growth rules with the 226 same central elements but distinct biological mechanisms might achieve a similar outcome. The central elements 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

227 

## are: 

228 

229 

   1. A seed subset of topographically organized neurons with spontaneous activity. 

   2. Presynaptic activity-based and distance-dependent synapse formation, strengthening and pruning. 

- 230 3. In- out-degree saturation in individual neurons. 

- 231 4. A separation of time-scales between retinal/synaptic activity propagation (fast) and synaptic plasticity (slow). 

232 Indeed, at least two other biologically distinct and plausible growth rules result in quantitatively and qualita233 tively similar endpoint connectomes, each with hierarchical, spatially concentric, and topographically organized 234 and mirror-reversing retinotopic maps (Fig. 5). 

235 We call the first alternative _race-to-threshold_ growth (Fig. 5a-b). This rule begins with all-to-all connectivity 236 in the form of silent synapses from LGN neurons to cortex and within the cortical sheet. The silent connections 237 accumulate resources ferried from the soma; once the accumulated resources exceed a threshold that depends on 238 the soma-to-synapse distance and presynaptic activation (with a smaller threshold for higher presynaptic activity 239 and shorter soma-to-synapse distance; the threshold shares the same mathematical term _∆i j_ of Eq. 1: _Ti j_ = 240 _T − ∆i j_ ), the synapses become non-silent. As the silent synapses of a neuron become non-silent, the in and 241 out-degree of the neuron increases up to a maximal in and out degree. Once a neuron becomes in- or out-degree 242 saturated, no further synaptic resource is available for in- and out-synapse building. As a result, a ‘race’ for synaptic 243 resources occurs, leading to the activation of synapses with the smallest thresholds first. 

244 The second alternative that we propose is a _seek-and-prune_ growth rule (Fig. 5c-d). This model begins without 245 any connectivity between neurons. Spontaneous activity promotes the initial stochastic formation of synapses, 246 which are then selectively pruned based on their stability. Stability is measured by a quantity called ‘synaptic 247 permanence’, which is higher for shorter synapse-to-soma distance and synapses formed by higher presynaptic 248 activity. This type of selective synaptic pruning is a significant feature of the developing nervous systems and is 249 important for rewiring mistargeted axons and consolidation [42, 64, 75, 76, 77]. 

250 The functional form of the synaptic permanence is the same as the growth rate in the competition model, Eq. 1. 251 Both rules result in qualitatively similar architecture, structure, and topography (Fig. 5b,d) Despite their endpoint 252 similarity, we will see later that the different rules yield distinct predictions about the developmental trajectory of 253 visuotopic organization. 

## 254 

## **Spatial receptive field structure** 

255 Primate visual neurons have smaller foveal receptive fields with increasingly larger peripheral receptive fields 256 within and across areas [78, 70, 79, 80, 81] — the emergent hierarchical receptive field structure of our model 257 shows the same signatures, Fig. 6. Specifically, the log-conformal mapping from the eye to LGN also induces an 258 eccentricity dependence on LGN field sizes, with larger fields for more eccentric retinal locations. Each cortical area 259 inherits this qualitative eccentricity dependence, Fig. 6a (the eccentricity dependence is inherited, not amplified, 260 by the cortex, SI Fig. S3). We further observe in Fig. 6a that at very large eccentricities near the edge of the visual 261 field (which has not been examined closely in experimental work), the model predicts a mild downward trend of 262 visual receptive field sizes in each area. This finding holds across varied network sizes and across the different 263 growth rules as well as by direct implementation of the GWM-S process. 

264 Next, the receptive fields increase in size going up the hierarchy, Fig. 6a, also qualitatively consistent with 265 results in macaques and humans, Fig. 6b [78, 70, 79, 80, 81]. Sample receptive fields in V1 and V4 can be seen 266 in Fig. 6c. The ratio of receptive field sizes between successive hierarchical areas should approximate a geometric 267 progression (see next section for the reason why), but this does not hold precisely because of details like the finite 268 cortical sheet, its geometry, and the non-isotropic shapes of local connectivity. The macaque and human data also 269 do not exhibit a simple or consistent pattern of size progression, Fig. 6b. 

270 Additionally, when we plot the receptive field centers for all neurons in an area, the vertical and horizontal 271 visual meridians appear underrepresented, suggesting a repulsion of the field centers away from the meridians, 272 6d. On investigation, we find that this is an artifact of the fact that the horizontal and vertical visual meridians 273 correspond to cortical area boundaries and crossing a meridian corresponds to a representational switch to the 274 opposite cortical hemifield, with truncated receptive fields near the boundary. Defining the center-of-mass of a 275 receptive field as the field center will result in an apparent repulsion of the field center away from boundaries, 276 here and likely also in experiments. When the receptive fields of all neurons within an area are summed, they span 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [191 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
a race to threshold growth b V4V3<br>V2<br>V1<br>    active<br>presynaptic<br>    neuron<br>resources growing synapse formed resources fading<br>c seek and prune growth d V4<br>V3<br>V2<br>    active<br>presynaptic V1<br>    neuron<br>seeking formed pruned<br>**----- End of picture text -----**<br>


Figure 5: **Distinct biologically-plausible learning rules based on growth and pruning reproduce hierarchical, spatial, and topographic organization** (a) The _Race-to-threshold_ growth involves the ferrying of resources from active neurons to all their potential synapses. Synapses become active upon crossing a minimum resource thresholds. This resource threshold is higher for further away synapses and lower for more-active neurons. Neurons that hit their outgoing or incoming synaptic bound cannot build additional outgoing or incoming synapses, respectively. (c) The _Seek-and-prune_ growth involves a process in which active neurons seek nearby neurons to synapse with. Synapses compete with each other through a “permanance” factor that depends on presynaptic activity and distance. Synapses with higher permance are pruned with smaller probability than those with weaker permanence (see main text and Methods for details). (b,d) Both models result in the formation of hierarchical, spatially concentrically arranged, and retinotopicaly organized visual areas. 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [325 x 265] intentionally omitted <==**

**----- Start of picture text -----**<br>
a model b 25 macaqueV4 V2<br>V4 20<br>0.25 15<br>10 V1<br>0.20 5<br>0<br>0.15 V3 0 5 10 15 20 25 30 35 40 45 50<br>15 humans<br>VO1<br>0.10<br>10 hV4<br>0.05 V2<br>5 V3<br>0.0 V1 V2V1<br>0 20 40 60 80 5 10 15 20<br>receptive field eccentricity (deg) receptive field eccentricity (deg)<br>c sample receptive fields with Gaussian function fits d center of mass of receptive fields e sum of all receptive<br>fields in any<br>V1 V4 V1 V2 V3 V4 area<br>size (deg)<br>receptive field<br>fraction of visual field<br>size (deg)<br>receptive field<br>**----- End of picture text -----**<br>


Figure 6: **Receptive field structure in formed network.** (a) Receptive fields grow with eccentricity in each visual area, with a small but significant dip at the most eccentric locations, and grow along the hierarchy. (b) Experimental data showing the eccentricity dependence of visual receptive field size from macaque[78](top) and from humans[79](bottom). (c) Example receptive fields from area V1 and V4 in the model. (d) The center of mass of receptive fields appears to show an apparent repulsion away from the horizontal and vertical meridians (shown in gray), with larger repulsion in higher areas. (e) Nevertheless, receptive fields for any area completely sample the entire visual field. 

277 all parts of the visual field uniformly, contrary to the apparent underrepresentation of the vertical or horizontal 278 medians when using only field centers, Fig. 6e). 

279 Finally, we observed another interesting emergent model property: Define a cortico-visual field as the patch 280 in the visual field that a cortical cell responds to, and define a cortico-LGN field as the patch of LGN that a cortical 281 cell responds to. The growth model generates distortions – in the form of elliptical deviations from circularity – in 282 its cortico-LGN fields, in a way that generates circular cortico-visual fields, SI Fig. S4 [82]. Had the cortico-LGN 283 fields been circular, the cortico-visual fields would have been more elliptical. Thus, the growth process seems to 284 perform an automatic “whitening” of the shape of the cortico-visual receptive field, an experimental prediction. 

## 285 

## **Connectivity** 

286 Unlike previous approaches to modeling visual cortex topography based on self-organizing maps [83], the present 287 approach results in a complete neural circuit, with granularly specified synaptic connectivity between neurons. As 288 already seen, it possesses the gross architecture (multiple discrete hierarchically connected areas), spatial layout 289 (concentrically arranged areas), and topography (retinotopy and polar angle reversals) characteristic of primate 290 visual systems. Further, the model generates a detailed connectome that can be analyzed to predict synaptic 291 connectivity across visual cortical areas. 

292 

## **Sparse, hierarchical, and convolution-like connectivity in retinotopic coordinates** 

293 We target individual cells in the formed network, tracing their downstream and upstream partners across areas, 294 in a dense computational version of anterograde and retrograde tracing [84] or connectomics [85], Fig. 7. A cell 295 in a given hierarchical area sends outputs to a sparse subset of cells in the downstream area, and receives inputs 296 from a sparse set of cells in upstream areas, Fig. 7a. This sparse set of inputs and outputs is spatially clustered 297 in the cortical sheet (Fig. 7a). When organized based on retinotopic locations, these inputs and outputs form 298 regularly-shaped local patches (Fig. 7b). This connectivity closely resembles the tiled local spatial organization 299 posited to exist in brains [86, 87, 88, 89], in which neurons in each area pool inputs from the previous area through 300 a similar pooling function (a convolution-like kernel), and which is built by hand into models that provide the 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [461 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b V4<br>V3<br>V2<br>V1<br>visual field<br>coordinates<br>c input connections d e sum of lognormals  g 60<br>output connections in-length observed<br>100 V2<br>30<br>V4 V3<br>V4<br>long f 0 20 40 60 0<br>50 V3 wiring length 60<br>out-length short V1<br>40<br>V2<br>V2<br>V3<br>V1 20<br>0 0<br>V1 V2 V3 V4 0 20 40 60 80 0 0<br>0 20 40 60 0 90<br>area eccentricity (deg) in-length polar angle<br>hierarchy<br>count in-length<br>RF area to LGN<br>kernel width to adj. area<br>out-length<br>outgoing length<br>**----- End of picture text -----**<br>


Figure 7: **Connectivity in the grown network.** (a) Computational connectomics at 5 neurons shows the incoming and outgoing connections are both sparse and local, similar to a local filter motif. (b) Left: A ‘tree’ of outgoing connections showing all neurons in the grown visual cortex that receive information from a given neuron in V1. Right: a similar tree of incoming connections, showing all neurons in the visual cortex that send information to a given V4 neuron. (c) Violin plots showing the distribution of the size of the connectivity patch on adjacent areas through input (blue) and output (orange) connections to neurons in a given area (d) A map of in-connectivity lengths and out-connectivity lengths in the formed visual cortex. Although V1 received inputs from LGN, the connectivity lengths of those synapses have not been shown here. (e) Empirically observed distribution of connectivity lengths across the entire network. (f) In-connection lengths are inversely correlated with out-connection lengths, shown for all neurons with both in and out connections in the cortical sheet (i.e., V2 and V3). (g) For large eccentricities (here chosen as larger than one-third the extent of the visual field), the magnitude of polar angle is correlated with the in-connectivity length of V3 neurons and the connectivity length of V2 neurons; it is also inversely correlated with the in-connectivity length of V2 and V4 neurons and the out-connectivity length of V1 and V3 neurons. In all cases the network used has been constructed through direct implementation of the GWM-S process; similar results are observed when explicitly using either of the three proposed biologically plausible growth rules (see SI for details). 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [207 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
a V1 V2 V3 V4<br>local greedy wiring<br>b<br>V1 V2 proto-V3, V4...<br>heterosynaptic competition<br>c V1 V2 proto-V3, V4...<br>seek-and-prune<br>d V1 V2 proto-V3, V4...<br>race-to-threshold<br>distance from center of cortical sheet<br>90<br>polar angle (deg) 0<br>**----- End of picture text -----**<br>


Figure 8: **Distinguishable developmental trajectories under different growth rules.** (a) Mature cortical sheet under the GWM-S process (left). Horizontal white line: Iso-eccentricity slice along which the polar angle varies as shown (right). (b-d) Layout of mature cortical sheet for three wiring rules (left column), and quantification of the development of polar angle tuning (right column). Developmental trajectory around an intermediate stage of growth after the formation of V1 and V2 but before the complete development of retinotopy in V3. Magenta arrow shows the progression of developmental stages. 

301 best quantitative match to date to electrophysiological data from several visual areas and to behavioral data in 302 primates and rodents [90] (Fig. 7a, far right). 

303 The convolution-like connectivity profile widths are roughly similar across areas in the model (Fig. 7c left). 304 Thus, the increase in receptive field size in higher areas of the model results from the hierarchical nesting of 305 similar-sized local spatial kernels rather than from an increase in the kernel width between areas. As a result, the 306 expected scaling of receptive field sizes across areas (the ratio of receptive field sizes between adjacent levels in 307 the hierarchy) is a geometric progression. However, if spatial gradients in the cortical sheet were to modulate the 308 maximum synaptic weights per neuron, they could affect field sizes beyond the effects included in this simplest 309 version of a growth model. Similarly, variations of cortical connectivity width with eccentricity are weak, so that 310 the systematic increase in receptive field size with visual eccentricity is largely inherited from the input projections 311 to cortex, (Fig. 7c right). 

## 312 

## **Wiring length and location on cortical sheet** 

313 We next consider whether there are systematic variations in connectivity length within and across formed areas. 314 Coloring cells on the cortical sheet based on the length of the input wiring reveals a sawtooth-like in-connectivity 315 length profile, in which neurons near the inner edge of each area receive the shortest connections and those at the 316 outer edge receive the longest connections, Fig. 7d (top), as expected from Figure 4a. Conversely, for outgoing 317 connections, neurons at the outer edge of each area send the shortest connections, while those at the inner edge 318 send the longest ones, Fig. 7f (bottom). Pooling together all synapses from all neurons in V1, V2, V3 and V4, we 319 find a bimodal distribution of wiring lengths that is well-fit by a sum of two lognormals, Fig. 7e. 

320 Neurons with long out-connections have short in-connections, and vice versa, resulting in an inverse correlation 321 between in-connectivity and out-connectivity lengths, Fig. 7f. This pattern suggests a roughly constant summed 322 in- and out-wiring length across neurons in an area. Finally, the relationship between wiring in-length and polar 323 angle flips when moving along the hierarchy: in-connectivity length is negatively, then positively, then negatively 324 correlated with polar angle for V2, V3, and V4, respectively (Fig. 4g, top). The out-length-polar angle correlations 325 follow a similar pattern (Fig. 4g, bottom). 

326 Altogether, the connectome of the grown visual system model reveals how a hierarchically stacked convolution327 like architecture may be embedded into a locally-connected and spatially flat cortical surface with mirror-reversing 328 retinotopic maps. This is the first model of the primate visual hierarchy to generate connectivity de novo; thus, 329 these constitute a rich set of novel predictions for the next generation of connectomics work following the first 330 efforts undertaken in the visual pathway [85]. 

## 331 

## **Trajectories of retinotopy development** 

332 Across all growth rules, we already noted a similar developmental endpoint; we also observe a key common 333 characteristic of the trajectory to the endpoint — the development of retinotopy in the visual cortical hierarchy is 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

334 sequential, with retinotopy emerging and stabilizing in lower visual areas before higher areas. This constitutes a 335 robust and invariant prediction of all the growth models. To some extent, the maturation dynamics of the visual 336 pathway will depend on the spatiotemporal properties of the retinal waves that drive it. But under the assumption 337 of uniformly distributed waves (such that all parts of the retina are activated with equal probability on the time338 scale of development), the qualitative properties of emergence are relatively independent of the detailed form of 339 the retinal waves: cortical hierarchy, spatial physical organization, and topography with reversals emerge from 340 the growth rules, regardless of the details or source of the spontaneous activity that drives the process. This 341 relative independence on the one hand reaffirms the relationship of our models to the GWM-S process. And on 342 the other hand, it also helps explain the experimentally observed invariance of sensory hierarchy development in 343 cortex even in animals born without a retina or with early retinal damage [91, 92], assuming that spontaneous 344 activity is present in some downstream area. Our model therefore provides the strong prediction for future work 345 in development that spontaneous activity covering the visual space on average, regardless of the detailed statistics 346 of the activity, should be sufficient for architectural hierarchy, spatial organization of areas relative to each other, 347 and mirror reversals across area boundaries. Our model suggests that finer spatiotemporal characteristics of the 348 spontaneous activity are probably important for more detailed structure emergence and further refinement. 

## 349 

## **Discriminating between growth models** 

350 We next ask whether, despite their commonalities, the learning rules generate transient connectivities that are 351 distinguishable during development. We examine retinotopy development at the intermediate period after V1 352 and V2 formation and while V3 is partially organized (Fig.8). Under the heterosynaptic growth rule, all cortical 353 neurons beyond V1 and V2 are connected and receive input drive. A rough retinotopy is rapidly established across 354 all neurons in proto-V3 (Fig 8b, light blue curve), then the retinotopic organization is gradually sharpened _in situ_ 355 (Fig 8b, darker blue curves). 356 By contrast, under the seek-and-prune and race-to-threshold growth rules, neurons beyond V1 and V2 exhibit 357 no retinotopy initially, Fig. 8c-d. Under both these rules, the retinotopically structured part of proto-V3 slowly 358 expands outward. Under seek-and-prune growth, most neurons in proto-V3 are unconnected to V1 or V2, and 359 neurons in the region slowly gain connectivity to V2 inputs, forming an area V3. However, at any point, the 360 partially grown V3 contains a complete map of the visual field (i.e., coverage of all polar angles and eccentricities), 361 Fig. 8c. As V3 expands, the polar angle map stretches out in tandem. Under race-to-threshold growth, neurons in 362 proto-V3 represent only a small range of polar angle (the angles most similar to those at the V2 edge). However, 363 the angles represented by these proto-V3 neurons remains similar to the angles these neurons will represent in 364 mature V3. Over time, neurons further away in the proto-V3 gain a polar angle representation, steadily covering 365 a larger range of angles over time in tandem with the gain in polar tuning across proto-V3 (Fig. 8d). 

366 Across models, the shorter within-area connections are predicted to stabilize earlier than the longer within367 area connections. In sum, we have explored a set of biological growth rules that all follow the local GWM-S 368 principle, but differ in some biologically important ways that we predict can be distinguished based on specified 369 and measurable differences in their developmental trajectories. 

## 370 

## **Generalization to other cell types: Interneuron emergence** 

371 Only a small number of parameters modulate the growth dynamics, across all rules. The distance scale _d_ 0 in Eq. 1 372 and the activity propagation attenuation factor _γ_ in equation 3 are critical in shaping outcomes and are common 373 across rules. Two additional shared parameters set the maximum in-degree and out-degree of each neuron — in 374 race-to-threshold and seek-and-prune, these are _k[in]_ , _k[out]_ ; in heterosynaptic competition, these are (the ratio of) 375 the maximum per-synapse and per-neuron weights _w_ max, _W_ max. These degree parameters affect the relative sizes 376 of successive areas, SI Fig. S2, but do not qualitatively change the architecture. Finally, each growth role requires 377 growth rate parameters which affect numerical stability and convergence, but which do not qualitatively alter the 378 final network; for heterosynaptic competition, these are set by _η_ (growth rate), _ε_ (competition strength), and _εw_ 379 (activity propagation threshold); for growth-to-threshold, these are set by _η_ (growth rate) and _r_ 0 (normalization 380 of accumulated resources); for seek-and-prune, these are _ndraw_ (number of synapses neurons attempt to form in 381 each growth iteration). Combined with structural specification of the cortical sheet and LGN geometry, which are 382 held fixed across rules, this is the exhaustive list of parameters. 

383 For the two critical parameters related to activity propagation _γ_ and distance scale _d_ 0, the growth dynamics 384 are robust to variations (up to 5 orders of magnitude of variation in these parameters, cf. SI Fig. S5), However, we 385 found that there is a boundary in the _γ_ , _d_ 0 space across which the network switches from developing a hierarchical 386 architecture to instead developing a non-hierarchical one with purely local connectivity everywhere (Fig. S5). 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [461 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
a layout of cell types on the cortical sheet b type 1 neurons receive local and interareal connections type 1 neurons send feedforward interareal outputs c type 2 neurons send local outputs<br>Type 1 Type 2<br>presynaptic<br>postsynaptic<br>d e f<br>Type 1 presynaptic Type 2 presynaptic<br>visual field<br>coordinates<br>connectivity length (a.u.)<br>counts<br>**----- End of picture text -----**<br>


Figure 9: **Incorporation of cell types and emergent cell-type dependent connectivity motifs from growth:** (a) A schematic of layout of the 2 cell types in a square lattice on the cortical sheet (b) Simulation with the incorporation of the two cell types continues to result in the formation of concentrically arranged areas. Within these areas, cells of type 2 form local connections (open circles designate pre-synaptic partners; solid squares designate post-synaptic partners) (b), whereas cells of type 1 receive both local and feedforward connections (c, _left_ ), but form only feedforward connections (c, _right_ ). (d) Arranging the neurons according to their hierarchy and receptive field coordinates (similar to Fig. 7(a-b)) similarly shows that cells of type 1 project feedforward into the next hierarchical area, whereas cells of type 2 project only locally to neurons in the same area. (e) Histogram of all wiring lengths, with output connections from cell type 2 neurons shown in red, and output connections from cell type 1 neurons shown in black. (f) The associated eccentricity (left) and polar angle (right) maps. 

387 The latter connectivity is reminiscent of the projection patterns of inhibitory interneurons in cortex, predicting 388 that genetic specification in this _γ_ , _d_ 0 space could be a developmental control knob that is set differently across 389 cell types to govern their projection patterns. 

389 390 Thus, to investigate the potential for simultaneous emergence of both projection patterns, we created an un391 differentiated cortical consisting of two types of cells Fig.9a, interleaved in a 1:8 ratio (see _Methods_ for details). 392 Regardless of type, all neurons interact with and drive each other. They all compete together to innervate the 393 same set of potential neural targets. Remarkably, this mixed-neuron system again forms a hierarchy of discrete 394 areas that are concentrically organized on the cortical sheet, Fig. 9b,left. 395 Connectomic tracing of the in- and out-projections reveals that type 1 cells exhibit local spatial projection pat396 terns to successive areas in the hierarchy, Fig. 9b, like the single-cell-type results. We will call these projection 397 neurons. Type 2 cells exhibit purely local within-area projections, Fig. 9c. We will call these interneurons. In398 terneurons, like projection neurons, receive both local inputs and feedforward inputs from the preceding area. The 399 differences in the connectivity of the two cell types can also be visualized when neurons are organized based on 400 their retinal receptive field positions, Fig. 9d, and can be quantified in a wiring length histogram, Fig. 9e. As with 401 the single cell-type results on the spatial width of neural projections as a function of level in the formed hierarchy 402 (Fig. 7c), the interneuron connectivity width is also constant across levels of the hierarchy and determined by the 403 out-degree of the neurons, Fig. 9c. 404 The formed areas exhibit qualitatively similar mirrored retinotopic maps in areas V1-V4 as before, Fig. 9f, albeit 405 slightly noisier. This network constitutes a skeleton (connectivity graph) model of the ventral visual hierarchy with 406 both projection neuron and interneuron connectivity patterns simultaneously formed from the same set of simple 407 growth rules. 

## 408 

## **Generalization to other sensory modalities: Auditory hierarchy** 

409 The robust hierarchical structures that emerge from our developmental rules suggest that other sensory modalities 410 and sensory hierarchies in different species could be modeled in a similar way. 

411 In the case of vision, the input topography was specified by the visual field projected onto the retina. The 412 placement of LGN relative to cortex, in our case with LGN nearest to one edge of the cortical sheet, resulted in 413 concentric organization of hemi-circular or horeshoe-like areas around the primary cortex. Had the LGN been 414 aligned to the center of the cortical sheet, cortical areas would fully surround the primary area. 

415 

The radial topography and polar angle alternations were similarly a function of LGN geometry: the mirror 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [277 x 343] intentionally omitted <==**

**----- Start of picture text -----**<br>
experiments models<br>a b<br>MM MGN<br>RM undifferentiated auditory cortex<br>RT<br>RT R A1<br>CM<br>CL frequency (Hz)<br>R A1<br>AL ML<br>c d<br>V1<br>V1<br>azimuth (degrees)<br>e f<br>RL<br>LM<br>PM<br>V1 P<br>topographic reversals topographic reversals<br>altitude (degrees)<br>**----- End of picture text -----**<br>


Figure 10: **The greedy wiring minimization principle generates cortical processing hierarchies across sensory modalities and species.** (a) Top: A tonotopic map of auditory cortical areas from fMRI in humans exhibits smooth gradients in auditory frequency tuning as well as mirror reversals between areas [10]. Bottom: Schematic of the auditory cortical layout (H and L mark high- and low-frequency tuning, while A1, R, and RT designate successive areas in the auditory processing hierarchy). (b) Simulation of the local GWM-S process applied to a strip of undifferentiated cortex with spontaneous input assumed to arrive from a cochlea, results in a discrete set of auditory areas with mirror reversals of tonotopy. (c) (Top left) A map of the mouse visual cortex spanning areas including V1, P, PM, LM, RL [93]. The coverage map in visual space of V1 shown in gray (bottom left) is almost entirely covered by the coverage map of the higher areas, P, PM, LM and RL (right) with a marked hole in visual space representation. (d) A simulation of the GWM-S process on a cortical sheet seeded with the appropriate geometry results in the formation of a hierarchical second area (red) that surrounds the initial putative V1 (gray). the greedy wiring simulation results in similar coverage maps of V1 (bottom left), and a similar hole visual space representation of the higher area (right). (e) A retinotopic map of the mouse visual cortex, and (f) of a network grown with the GWM-S process. 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

416 reversal of maps across area boundaries corresponded to polar angle reversals because iso-polar-angle contours 417 ran parallel to the LGN boundaries. If the LGN geometry were flattened so that iso-eccentricity contours ran 418 parallel to its boundaries, this would result instead in a eccentricity map alternations along with a more-smooth 419 mapping of polar angle SI Fig. S6. Examples with different LGN positioning relative to the cortical sheet and LGN 420 geometry are given in Fig. 10 and SI Fig. S6. Differences in these initial geometric properties might be partly 421 responsible for variations across cortical modalities and species. 

422 In the auditory system, the sensory organ is the cochlea. Its tapered geometry induces a one-dimensional 423 tonotopic mapping between sound frequency and responding regions of the cochlea. Like the retinotopic LGN 424 projection into undifferentiated visual cortex, we assume a tonotopic cochlear projection via the auditory thalamus 425 MGN into undifferentiated auditory cortex. We model the undifferentiated auditory cortex as a rectangular strip 426 that roughly matches the geometry of the core-belt auditory regions, Fig. 10a, with MGN projecting toward the 427 caudal end [94, 95], Fig. 10b. 428 Competitive growth drives the formation of a discrete auditory hierarchy with tonotopic mirror reversals at 429 the area boundaries. We equate the formed regions with A1, R, and RT, which, based on response latencies, are 430 believed to form a hierarchy of processing areas in auditory cortex [10, 94, 95], Fig 10c. Given the relatively less431 detailed knowledge of maps in the auditory cortex, our hope is that information flow and connectivity predictions 432 from this model might provide interesting hypotheses about auditory cortical organization for experimental study. 

## 433 

## **Generalization to other species: Mouse visual cortex** 

434 The murine visual cortex has a less clear hierarchical structure than primates. The primary visual area V1 projects 435 to a number of regions, including P, LM, AL, and RL. It is a subject of debate whether these are distinct processing 436 areas or whether together they define a second stage in a processing hierarchy. Recent work with wide-field 437 calcium imaging generated a detailed retinotopic map of primary visual cortex and other extrastriate areas, Fig 438 10a (top) [93], revealing that secondary areas P, LM, AL, RL do not individually cover the visual field, but together 439 cover most of it, apart from a puncture near the center, Fig 10b (bottom, right). We ran the local greedy wiring 440 minimization (GWM-S) simulation with a neural sheet matching the mouse visual cortex and seeding it with an 441 input geometry that matches the mouse primary visual cortex. The result reproduced the retinotopy and the visual 442 field coverage of V1 and the surrounding areas, Fig 10b. 443 Thus, the same learning rules, applied to inputs from different modalities or to different cortical geometries 444 for different species, generate distinct sensory hierarchies in different animals. The framework of our model thus 445 provides detailed predictions at the neural and connectomic levels across sensory modalities and species. 

## 446 

## **Discussion** 

447 In the present work, we show how synaptic-level subcellular learning rules and cellular-level competition can 448 organize an unstructured cortical sheet into a set of discrete, hierarchically connected brain regions, with their 449 topographic mapping inherited from the metrics of the low-level sensory space and from the geometry of the 450 cortical sheet. Thus, the model parsimoniously explains how, driven by visual inputs, cortex would develop a 451 visual processing pathway with discrete brain areas and hierarchical architecture, spatially concentric organization 452 of these areas on the cortical sheet, and topographic structure in the form of retinotopy and polar alternations, 453 and how. The same rules and model, driven by auditory inputs, develop an auditory processing hierarchy. The 454 same model acting on a different cortical geometry also generates a mouse-like visual cortical processing stream. 455 Thus, the model provides a mechanistic hypothesis for fascinating discoveries on the pluripotency of cortical 456 development [28]. 457 Burgeoning data from connectomics and transcriptomics, as well as neural imaging and activity data, demand 458 models that link the disparate levels from genes and cells to connectivity, local circuit structure, and brain orga459 nization. Under the hypothesis that the small number of parameters of the growth rules are controlled by genetic 460 guidance, our model also provides predictions for linking all the way from gene expression to complex emergent 461 structure. These parameters control whether a cell’s connectivity is projection neuron-like or interneuron-like 462 and the thickness or size of each discrete cortical area. Thus, the model predicts that key combinations of gene 463 expression map onto the control knobs of the growth model to determine the projection patterns of cell types and 464 the macroscopic features of areal organization, such as area size, and should vary in specifically defined ways 465 according to the model to generate different cell types (projection neurons and interneurons), different sensory 466 cortices (visual and auditory), or different species (primate and mouse). 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

467 The proposed mechanisms of structure emergence via competitive growth rules that implement local greedy 468 wiring minimization result in self-organization driven by spontaneous activity. Thus, they contrast with the tradi469 tional chemoaffinity hypothesis of Sperry [17], in which genes instruct the detailed organization of synapses. This 470 is consistent with the finding that even in the fly, an exemplar of chemoaffinity-guided development, spontaneous 471 activity plays a critical role in brain development [32, 38, 30, 52, 53]. Our model provides a potential mechanism 472 for how self-organized structure emergence could work in tandem with or in addition to detailed genetic spec473 ification. Moreover, our model goes beyond the idea that spontaneous activity drives refinement of genetically 474 specified wiring; here, spontaneous activity also plays a role in setting gross features like discrete region formation, 475 hierarchy emergence, and global polar angle reversals. 

476 **Relationship to existing models: global wiring minimization and visual cortex organiza-** 477 **tion** 

478 Several works in the literature focus on global wiring optimization, showing that ocular dominance and orientation 479 preference maps can arise within the framework of optimizing a global synaptic wiring length objective between 480 co-tuned neurons [96, 72, 54]. These works contrast from ours in two ways: They focus on algorithms for global 481 optimization without biologically plausible processes to achieve such optimal solutions in the brain; and there is 482 no demonstration that global wiring optimization as a principle would generate discrete brain regions, hierarchical 483 order, spatial order, or topographic mirror reversals. Another wiring minimization approach involves supervised 484 learning: it begins with a pre-specified architecture (discrete hierarchical brain areas) and connectivity (spatially 485 local), then generates neural tuning and layouts within each area by maximizing performance on a visual task 486 while minimizing total wiring length through gradient learning [74, 97]. These global optimization approaches 487 do not lend themselves to the creation of mechanistic models of cortical development because global wiring length 488 minimization is an NP-hard problem and because they begin with a prespecified connectivity and focus on spatial 489 optimization based on that connectivity. 490 Alternatively, self-organizing map approaches have sought to model visual topographic signatures, including 491 ocular dominance [98, 99, 100], the development of the log-conformal map in primary visual cortex[101] and 492 more recently, multiple visual field maps in early visual cortical areas[102, 83]. These approaches generate a 493 spatial organization based on prespecified tuning profiles rather than a prespecified connectivity, but the resulting 494 models do not generate biologically plausible synaptic growth rules or result in circuit-level connectivity for how 495 the assumed tuning profiles might arise. 496 By contrast, we cast development as driven by local growth rules fueled by spontaneous activity, with neuron497 level synaptic constraints and local competition, in a process that precedes the emergence of specific visual feature 498 tuning, consistent with experimental findings. The unfolding dynamics naturally generates a hierarchical multi499 scale structure with a full neural-level connectome, in which connectivity is not globally optimized but is the result 500 of local search process where neurons sequentially stabilize their shortest connections. 501 Our work can be viewed as extending [35], which explains some properties of the visual system by growing 502 a network from developmental rules. Our model extends the quasi-one-dimensional structure of [35] into two 503 dimensions to capture the different topographies of both retinotopic eccentricity and polar angle (smooth ver504 sus mirror reversing topographies, respectively), naturally generates inter-areal alternations (in contrast to [35], 505 which requires that the degree of saturation in subsets of neurons is specifically modulated in time to generate 506 alternations), and generates a hierarchical organization (in contrast to [35], in which all resulting connections are 507 from V1 to other areas rather than a hierarchy). 

## 508 

## **Predictions** 

509 The model makes numerous predictions. Several include mechanisms to generate previously known aspects of 510 structure (hierarchy, spatial organization, and topography) in a highly compact and parsimonious way, while 511 predicting that region boundaries defined by two independent measures – synaptic hops or hierarchy index, and 512 topographic mirror reversals – should coincide. In a real sense, because the model includes both a growth process 513 and a full final connectome, it also generates an uncountable number of novel predictions, as development can 514 be simulated and the outcomes predicted for any cortical geometry and topology with or without cortical lesions 515 or retinal scotomas, any input geometry, and different settings of the few parameters of the growth rule. We have 516 described several specific predictions along the way in the Results and in the Discussion above; we list a few of 517 them here as well: 1) spontaneous activity that covers the visual space on average, regardless of the detailed 518 statistics of the activity, should be sufficient for the emergence of architectural hierarchy, the spatial organization 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

519 of areas relative to each other, and mirror reversals across area boundaries; 2) More-detailed spatiotemporal 520 patterns of the spontaneous activity are important only for further refinement and more-detailed structural and 521 functional characteristics. 3) Dip in field size with eccentricity at large eccentricites; 4) Sequential development of 522 retinotopy up the hierarchy, such that retinotopy emerges and stabilizes in lower visual areas before higher visual 523 areas, true across all the rules; 5) More-circular cortico-visual receptive fields compared to cortico-LGN fields; 6) 524 Two critical factors of the growth process and neural/synaptic saturation determine the width and size of each 525 discrete formed region when cortical size is held fixed; 7) Hypothesized relationship between growth process 526 parameters and genetic control is predicted to enable simple scaling of the size of each cortical are by simple 527 genetic manipulation; 8) Different synaptic growth rules, all under the greedy wiring minimization principle, 528 have developmental trajectories that differ in specific predicted ways; 9) Detailed predicted connectome for the 529 auditory processing pathway in primate cortex and for visual pathways in mice [103, 104] to assist in mapping out 530 these less-well characterized hierarchies; 10) Saw-tooth pattern of wiring length when moving from the center of 531 V1 radially outwards in cortex across areas, leading to a systematic (alternating inverse and direct) relationship 532 between polar angle and wiring length across areas; 11) Inverse relationship between pre-synaptic wiring length 533 and post-synpatic wiring length for feed-forward connections between areas; 12) Bimodal distribution of wiring 534 lengths for feed-forward connections between areas; 13) First full primate visual pathway connectomic model 535 including the effects of the log-normal magnification of the fovea, constituting a rich set of additional predictions 536 for the next generation of connectomics work in the visual pathway [85, 103]. 

## 537 

## **Limitations and future work** 

538 We have focused here on articulating a compact set of rules that drive modular hierarchical structure emergence. 539 Our model should be viewed as setting the backbone or connectivity structure of the ventral visual pathway in 540 the late embryonic or post birth but pre eye-opening stages. Future work will focus on how the spatiotemporal 541 structure of retinal waves could itself direct the formation of our assumed retinotopy in the LGN projection, and 542 the emergence of some aspects of image-feature tuning, including orientation selectivity and ocular dominance 543 columns, which occur at a later stage of development in the visual system [105].Two retinas will be required to 544 explore the formation of ocular dominance stripes, while patterned visual inputs from natural images might be 545 required to learn finer topographic features including orientation maps. 546 Our work does not yet extend to the laminar structure and specializations of individual cortical areas. The 547 result that dialing the growth rule parameters generates an interneuron-like cell class, and that these cells be548 come integrated into the feedforward backbone with the same growth rules, opens the prospect that it might 549 be possible to similarly extend the present model to incorporate more distinct cell types and for a combination 550 of self-organization and genetic specification to drive laminar organization [106]. Specifically, adding emergent 551 dynamics in setting the growth parameters themselves could allow for rich developmental outcomes including 552 laminar organization and different spreads in lateral connected at different hierarchical processing levels. Our 553 model lays the groundwork to begin modeling these finer features of cortical organization. It will also be inter554 esting to obtain extensions that generate top-down connections [107, 108]. Finally, this model can be extended 555 to study how regional neural waves in other sensory peripheries and higher-level areas such as thalamus shape 556 downstream connectivity [109, 110]. It will be interesting to investigate how to combine processes of parallel or 557 simultaneous modular circuit development [14, 35] with the present sequential development model. 

## 558 

## **Broader implications for brain organization** 

559 The present growth models or small modifications of them, within the GWM-S principle, might play a role in 560 explaining brain organization beyond the early sensory hierarchies. Specifically, mirror-symmetric map layouts 561 or topographic organization matching that of sensory pathways have been reported in higher brain areas [111], 562 such as in lateral prefrontal cortex [112] the intra-parietal sulcus [113, 70], frontal areas [70], cerebellum [114], 563 striatum [115], and hippocampus [116]. It is possible that the hierarchical map formation process with topo564 graphic mirror reversals in sensory areas could continue in some form up to higher areas in the brain, forming a 565 sensory-coordinate layout of cognitive brain regions [112, 115]. 

566 Finally, the present model uses precisely the same heterosynaptic competition-based learning rule that was 567 hypothesized to generate robust sequence-formation in songbird premotor circuits [46]. It is striking that the 568 same rule, when driven with retinal inputs and a spatial embedding robustly generates a discrete, modular sen569 sory hierarchy with various types of structure, while when driven with random inputs, and a strengthening term 570 that is asymmetrically spike-time-dependent rather than spatially dependent, robustly generates sets of long spa571 tiotemporal activity sequences. This striking potency of the competitive growth rule, in addition to explaining the 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

572 pluripotency of sensory cortical hierarchies, is another indication that it might be a universal driver of develop573 mental brain organization. 

574 This hypothesis and computational model is consistent with a long history of results from developmental neu575 roscience in which competitive interactions and winner-take-all-dynamics lead to self-organization and structure 576 emergence through spontaneous symmetry breaking [13, 117, 42, 43, 44, 45, 118, 119]. Neural-level competitive 577 synaptic interactions also occur beyond development, under conditions of resource scarcity, for instance set by 578 the rate of protein production [120], and can give rise to phenomena like synaptic clustering on dendritic arbors 579 [121] and recovery from lesions [122, 123]. 

## 580 

## **References** 

- 581 [1] Brian A Wandell, Serge O Dumoulin, and Alyssa A Brewer. Visual field maps in human cortex. _Neuron_ , 582 56(2):366–383, 2007. 

- 583 [2] Robert F Dougherty, Volker M Koch, Alyssa A Brewer, Bernd Fischer, Jan Modersitzki, and Brian A Wandell. 584 Visual field representations and locations of visual areas v1/2/3 in human visual cortex. _Journal of vision_ , 585 3(10):1–1, 2003. 

- 586 [3] Jonas Larsson and David J Heeger. Two retinotopic visual areas in human lateral occipital cortex. _Journal_ 587 _of neuroscience_ , 26(51):13128–13142, 2006. 

- 588 [4] Brian A Wandell and Jonathan Winawer. Imaging retinotopic maps in the human brain. _Vision research_ , 589 51(7):718–737, 2011. 

- 590 [5] Ricardo Gattass, Sheila Nascimento-Silva, Juliana GM Soares, Bruss Lima, Ana Karla Jansen, Antonia 591 Cinira M Diogo, Mariana F Farias, Eliã P Botelho, Marco Marcondes, Otávio S Mariani, João Azzi, et al. 592 Cortical visual areas in monkeys: location, topography, connections, columns, plasticity and cortical dy593 namics. _Philosophical Transactions of the Royal Society B: Biological Sciences_ , 360(1456):709–731, 2005. 

- 594 [6] Peter T Fox, Francis M Miezin, John M Allman, David C Van Essen, and Marcus E Raichle. Retinotopic 595 organization of human visual cortex mapped with positron-emission tomography. _Journal of Neuroscience_ , 596 7(3):913–922, 1987. 

- 597 [7] Madineh Sedigh-Sarvestani and David Fitzpatrick. What and where: Location-dependent feature sensitivity 598 as a canonical organizing principle of the visual system. _Frontiers in Neural Circuits_ , 16, 2022. 

- 599 [8] Vernon B Mountcastle. Modality and topographic properties of single neurons of cat’s somatic sensory 600 cortex. _Journal of neurophysiology_ , 20(4):408–434, 1957. 

- 601 [9] Jon H Kaas. Topographic maps are fundamental to sensory processing. _Brain research bulletin_ , 44(2):107– 602 112, 1997. 

- 603 [10] Colin Humphries, Einat Liebenthal, and Jeffrey R Binder. Tonotopic organization of human auditory cortex. 604 _Neuroimage_ , 50(3):1202–1211, 2010. 

- 605 [11] Mark M Schira, Christopher W Tyler, Michael Breakspear, and Branka Spehar. The foveal confluence in 606 human visual cortex. _Journal of Neuroscience_ , 29(28):9050–9058, 2009. 

- 607 [12] Michael Eyre, Sean P Fitzgibbon, Judit Ciarrusta, Lucilio Cordero-Grande, Anthony N Price, Tanya Poppe, 608 Andreas Schuh, Emer Hughes, Camilla O’keeffe, Jakki Brandon, et al. The developing human connectome 609 project: typical and disrupted perinatal functional connectivity. _Brain_ , 144(7):2199–2213, 2021. 

- 610 [13] Larry C Katz and Carla J Shatz. Synaptic activity and the construction of cortical circuits. _Science_ , 611 274(5290):1133–1138, 1996. 

- 612 [14] Tomonari Murakami, Teppei Matsui, Masato Uemura, and Kenichi Ohki. Modular strategy for development 613 of the hierarchical visual network in mice. _Nature_ , 608(7923):578–585, 2022. 

- 614 [15] Michael J Arcaro and Margaret S Livingstone. A hierarchical, retinotopic proto-organization of the primate 615 visual system at birth. _Elife_ , 6:e26196, 2017. 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 616 [16] Thomas A Coogan and David C Van Essen. Development of connections within and between areas v1 and 617 v2 of macaque monkeys. _Journal of Comparative Neurology_ , 372(3):327–342, 1996. 

- 618 [17] Roger W Sperry. Chemoaffinity in the orderly growth of nerve fiber patterns and connections. _Proceedings_ 619 _of the National Academy of Sciences_ , 50(4):703–710, 1963. 

- 620 [18] Lewis Wolpert. Positional information and the spatial pattern of cellular differentiation. _Journal of theoret-_ 621 _ical biology_ , 25(1):1–47, 1969. 

- 622 [19] Roger W Sperry. Effect of 180 degree rotation of the retinal field on visuomotor coordination. _Journal of_ 623 _experimental zoology_ , 1943. 

- 624 [20] M Tessier-Lavigne and C S Goodman. The molecular biology of axon guidance. _Science_ , 274(5290):1123– 625 1133, November 1996. 

- 626 [21] Emily L Heckman and Chris Q Doe. Establishment and maintenance of neural circuit architecture. _Journal_ 627 _of Neuroscience_ , 41(6):1119–1129, 2021. 

- 628 [22] Weizhe Hong and Liqun Luo. Genetic control of wiring specificity in the fly olfactory system. _Genetics_ , 629 196(1):17–29, 2014. 

- 630 [23] Joris De Wit and Anirvan Ghosh. Specification of synaptic connectivity by cell surface interactions. _Nature_ 631 _Reviews Neuroscience_ , 17(1):4–4, 2016. 

- 632 [24] S Lawrence Zipursky and Wesley B Grueber. The molecular basis of self-avoidance. _Annu. Rev. Neurosci._ , 633 36:547–568, July 2013. 

- 634 [25] Karl Spencer Lashley. Brain mechanisms and intelligence: A quantitative study of injuries to the brain. 635 1929. 

- 636 [26] Alan Mathison Turing. The chemical basis of morphogenesis. _Bulletin of mathematical biology_ , 52:153–197, 637 1952. 

- 638 [27] Jelena Raspopovic, Luciano Marcon, Laura Russo, and James Sharpe. Digit patterning is controlled by a 639 bmp-sox9-wnt turing network modulated by morphogen gradients. _Science_ , 345(6196):566–570, 2014. 

- 640 [28] Jitendra Sharma, Alessandra Angelucci, and Mriganka Sur. Induction of visual orientation modules in 641 auditory cortex. _Nature_ , 404(6780):841–847, 2000. 

- 642 [29] David J Willshaw and Christoph Von Der Malsburg. How patterned neural connections can be set up by self643 organization. _Proceedings of the Royal Society of London. Series B. Biological Sciences_ , 194(1117):431–445, 644 1976. 

- 645 [30] Peter Robin Hiesinger. _The self-assembling brain: how neural networks grow smarter_ . Princeton University 646 Press, 2021. 

- 647 [31] Jeremy BA Green and James Sharpe. Positional information and reaction-diffusion: two big ideas in devel648 opmental biology combine. _Development_ , 142(7):1203–1211, 2015. 

- 649 [32] Orkun Akin and S Lawrence Zipursky. Activity regulates brain development in the fly. _Current opinion in_ 650 _genetics & development_ , 65:8–13, 2020. 

- 651 [33] Anthony M Zador. A critique of pure learning and what artificial neural networks can learn from animal 652 brains. _Nature communications_ , 10(1):3770, 2019. 

- 653 [34] Marcello GP Rosa. Visual maps in the adult primate cerebral cortex: some implications for brain develop654 ment and evolution. _Brazilian Journal of Medical and Biological Research_ , 35:1485–1498, 2002. 

- 655 [35] Nabil Imam and Barbara L Finlay. Self-organization of cortical areas in the development and evolution of 656 neocortex. _Proceedings of the National Academy of Sciences_ , 117(46):29212–29220, 2020. 

657 

- [36] Richard Losick and Claude Desplan. Stochasticity and cell fate. _Science_ , 320(5872):65–68, April 2008. 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 658 [37] Aaron G Blankenship and Marla B Feller. Mechanisms underlying spontaneous patterned activity in devel659 oping neural circuits. _Nat. Rev. Neurosci._ , 11(1):18–29, January 2010. 

- 660 [38] Orkun Akin, Bryce T Bajar, Mehmet F Keles, Mark A Frye, and S Lawrence Zipursky. Cell-type-specific 661 patterned stimulus-independent neuronal activity in the drosophila visual system during synapse formation. 662 _Neuron_ , 101(5):894–904, 2019. 

- 663 [39] Jessica L Ables, Joshua J Breunig, Amelia J Eisch, and Pasko Rakic. Not(ch) just development: Notch 664 signalling in the adult brain. _Nature Reviews Neuroscience_ , 12(5):269–283, 2011. 

- 665 [40] Tarec Fares and Armen Stepanyants. Cooperative synapse formation in the neocortex. _Proceedings of the_ 666 _National Academy of Sciences_ , 106(38):16463–16468, 2009. 

- 667 [41] Yire Jeong, Hye-Yeon Cho, Mujun Kim, Jung-Pyo Oh, Min Soo Kang, Miran Yoo, Han-Sol Lee, and Jin-Hee 668 Han. Synaptic plasticity-dependent competition rule influences memory formation. _Nature communications_ , 669 12(1):3915, 2021. 

- 670 [42] Dale Purves and Jeff W Lichtman. Elimination of synapses in the developing nervous system. _Science_ , 671 210(4466):153–157, 1980. 

- 672 [43] Narayanan Kasthuri and Jeff W Lichtman. The role of neuronal identity in synaptic competition. _Nature_ , 673 424(6947):426–430, 2003. 

- 674 [44] Mario Buffelli, Robert W Burgess, Guoping Feng, Corrinne G Lobe, Jeff W Lichtman, and Joshua R Sanes. 675 Genetic evidence that relative synaptic efficacy biases the outcome of synaptic competition. _Nature_ , 676 424(6947):430–434, 2003. 

- 677 [45] Kouichi Hashimoto, Ryoichi Ichikawa, Kazuo Kitamura, Masahiko Watanabe, and Masanobu Kano. Translo678 cation of a “winner” climbing fiber to the purkinje cell dendrite and subsequent elimination of “losers” from 679 the soma in developing cerebellum. _Neuron_ , 63(1):106–118, 2009. 

679 

- 680 [46] Ila R Fiete, Walter Senn, Claude ZH Wang, and Richard HR Hahnloser. Spike-time-dependent plasticity 681 and heterosynaptic competition organize networks to produce long scale-free sequences of neural activity. 682 _Neuron_ , 65(4):563–576, 2010. 

- 683 [47] Tatsuo S Okubo, Emily L Mackevicius, Hannah L Payne, Galen F Lynch, and Michale S Fee. Growth and 684 splitting of neural sequences in songbird vocal development. _Nature_ , 528(7582):352–357, 2015. 

- 685 [48] Rachel E Field, James A D’amour, Robin Tremblay, Christoph Miehl, Bernardo Rudy, Julijana Gjorgjieva, 686 and Robert C Froemke. Heterosynaptic plasticity determines the set point for cortical excitatory-inhibitory 687 balance. _Neuron_ , 106(5):842–854, 2020. 

- 688 [49] David H Hubel and Torsten N Wiesel. Receptive fields of cells in striate cortex of very young, visually 689 inexperienced kittens. _Journal of neurophysiology_ , 26(6):994–1002, 1963. 

- 690 [50] Antonella Antonini and Michael P Stryker. Rapid remodeling of axonal arbors in the visual cortex. _Science_ , 691 260(5115):1819–1821, 1993. 

- 692 [51] Jason W Triplett, Cory Pfeiffenberger, Jena Yamada, Ben K Stafford, Neal T Sweeney, Alan M Litke, Alexan693 der Sher, Alexei A Koulakov, and David A Feldheim. Competition is a driving force in topographic mapping. 694 _Proceedings of the National Academy of Sciences_ , 108(47):19060–19065, 2011. 

- 695 [52] M Neset Özel, Abhishek Kulkarni, Amr Hasan, Josephine Brummer, Marian Moldenhauer, Ilsa-Maria Dau696 mann, Heike Wolfenberg, Vincent J Dercksen, F Ridvan Kiral, Martin Weiser, Steffen Prohaska, Max von 697 Kleist, and P Robin Hiesinger. Serial synapse formation through filopodial competition for synaptic seeding 698 factors. _Dev. Cell_ , 50(4):447–461.e8, August 2019. 

- 699 [53] Ben Jiwon Choi, Yu-Chieh David Chen, and Claude Desplan. Building a circuit through correlated spon700 taneous neuronal activity in the developing vertebrate and invertebrate visual systems. _Genes Dev._ , 35(9701 10):677–691, May 2021. 

- 702 [54] Dmitri B Chklovskii, Thomas Schikorski, and Charles F Stevens. Wiring optimization in cortical circuits. 703 _Neuron_ , 34(3):341–347, 2002. 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 704 [55] Richard Mooney, Anna A Penn, Roberto Gallego, and Carla J Shatz. Thalamic relay of spontaneous retinal 705 activity prior to vision. _Neuron_ , 17(5):863–874, 1996. 

- 706 [56] Jonathan R Polimeni, Mukund Balasubramanian, and Eric L Schwartz. Multi-area visuotopic map complexes 707 in macaque striate and extra-striate cortex. _Vision research_ , 46(20):3336–3359, 2006. 

- 707 

- 708 [57] Jinglong Wu, Tianyi Yan, Zhen Zhang, Fengzhe Jin, and Qiyong Guo. Retinotopic mapping of the peripheral 709 visual field to human visual cortex by functional magnetic resonance imaging. _Human brain mapping_ , 710 33(7):1727–1740, 2012. 

- 711 [58] James B Ackman, Timothy J Burbridge, and Michael C Crair. Retinal waves coordinate patterned activity 712 throughout the developing visual system. _Nature_ , 490(7419):219–225, 2012. 

- 713 [59] Markus Meister, Rachel OL Wong, Denis A Baylor, and Carla J Shatz. Synchronous bursts of action potentials 714 in ganglion cells of the developing mammalian retina. _Science_ , 252(5008):939–943, 1991. 

- 715 [60] Rachel OL Wong. Retinal waves and visual system development. _Annual review of neuroscience_ , 22(1):29– 716 47, 1999. 

- 717 [61] Xinxin Ge, Kathy Zhang, Alexandra Gribizis, Ali S Hamodi, Aude Martinez Sabino, and Michael C Crair. 718 Retinal waves prime visual motion detection by simulating future optic flow. _Science_ , 373(6553):eabd0830, 719 2021. 

- 720 [62] Ileana L Hanganu, Yehezkel Ben-Ari, and Rustem Khazipov. Retinal waves trigger spindle bursts in the 721 neonatal rat visual cortex. _Journal of Neuroscience_ , 26(25):6728–6736, 2006. 

- 722 [63] Francisco J Martini, Teresa Guillamón-Vivancos, Verónica Moreno-Juan, Miguel Valdeolmillos, and Guiller723 mina López-Bendito. Spontaneous activity in developing thalamic and cortical sensory networks. _Neuron_ , 724 109(16):2519–2534, 2021. 

- 725 [64] David K Simon and DD O’leary. Development of topographic order in the mammalian retinocollicular 726 projection. _Journal of Neuroscience_ , 12(4):1212–1232, 1992. 

- 726 

- 727 [65] Lupeng Wang, Krsna V Rangarajan, Courtney A Lawhn-Heath, Rashmi Sarnaik, Bor-Shuen Wang, Xiaorong 728 Liu, and Jianhua Cang. Direction-specific disruption of subcortical visual behavior and receptive fields in 729 mice lacking the _β_ 2 subunit of nicotinic acetylcholine receptor. _Journal of Neuroscience_ , 29(41):12909– 730 12918, 2009. 

- 731 [66] A Kimberley McAllister. Dynamic aspects of cns synapse formation. _Annu. Rev. Neurosci._ , 30:425–450, 732 2007. 

- 733 

   - [67] Ying Yang and Nicole Calakos. Presynaptic long-term plasticity. _Frontiers in synaptic neuroscience_ , 5:8, 2013. 

- 734 [68] Najia A Elkahlah, Jackson A Rogow, Maria Ahmed, and E Josephine Clowney. Presynaptic developmental 735 plasticity allows robust sparse wiring of the drosophila mushroom body. _Elife_ , 9:e52278, 2020. 

- 736 [69] Yukiko Goda and Graeme W Davis. Mechanisms of synapse assembly and disassembly. _Neuron_ , 40(2):243– 737 264, 2003. 

- 738 [70] Wayne E Mackey, Jonathan Winawer, and Clayton E Curtis. Visual field map clusters in human frontoparietal 739 cortex. _Elife_ , 6:e22974, 2017. 

- 740 

   - [71] Liqun Luo. _Principles of Neurobiology, 2nd Edition_ . Garland Science, 2020. 

- 741 [72] Dmitri B Chklovskii and Alexei A Koulakov. A wire length minimization approach to ocular dominance 742 patterns in mammalian visual cortex. _Physica A: Statistical Mechanics and its Applications_ , 284(1-4):318– 743 334, 2000. 

- 744 [73] Dina Obeid and Talia Konkle. Wiring minimization of deep neural networks reveal conditions in which 745 multiple visuotopic areas emerge. _Journal of Vision_ , 21(9):2135–2135, 2021. 

- 746 [74] Hyodong Lee, Eshed Margalit, Kamila M Jozwik, Michael A Cohen, Nancy Kanwisher, Daniel LK Yamins, 747 and James J DiCarlo. Topographic deep artificial neural networks reproduce the hallmarks of the primate 748 inferior temporal cortex face processing network. _bioRxiv_ , 2020. 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 749 [75] Liqun Luo and Dennis DM O’Leary. Axon retraction and degeneration in development and disease. _Annu._ 750 _Rev. Neurosci._ , 28:127–156, 2005. 

- 751 [76] Wei Li, Lei Ma, Guang Yang, and Wen-Biao Gan. Rem sleep selectively prunes and maintains new synapses 752 in development and learning. _Nature neuroscience_ , 20(3):427–437, 2017. 

- 753 [77] Naila Ben Fredj, Sarah Hammond, Hideo Otsuna, Chi-Bin Chien, Juan Burrone, and Martin P Meyer. Synap754 tic activity and activity-dependent competition regulates axon arbor maturation, growth arrest, and terri755 tory in the retinotectal projection. _Journal of Neuroscience_ , 30(32):10939–10951, 2010. 

- 756 [78] Jeremy Freeman and Eero P Simoncelli. Metamers of the ventral stream. _Nature neuroscience_ , 14(9):1195– 757 1201, 2011. 

- 758 [79] Jonathan Winawer and Nathan Witthoft. Human v4 and ventral occipital retinotopic maps. _Visual neuro-_ 759 _science_ , 32, 2015. 

- 760 [80] Marcello GP Rosa, Aglai PB Sousa, and Ricardo Gattass. Representation of the visual field in the second 761 visual area in the cebus monkey. _Journal of Comparative Neurology_ , 275(3):326–345, 1988. 

- 762 [81] Ricardo Gattass, AP Sousa, and CG Gross. Visuotopic organization and extent of v3 and v4 of the macaque. 763 _Journal of neuroscience_ , 8(6):1831–1845, 1988. 

- 764 [82] Garikoitz Lerma-Usabiaga, Jonathan Winawer, and Brian A Wandell. Population receptive field shapes in 765 early visual cortex are nearly circular. _Journal of Neuroscience_ , 41(11):2420–2427, 2021. 

- 766 [83] Talia Konkle. Emergent organization of multiple visuotopic maps without a feature hierarchy. _bioRxiv_ , 767 2021. 

- 768 [84] Christine Saleeba, Bowen Dempsey, Sheng Le, Ann Goodchild, and Simon McMullan. A student’s guide to 769 neural circuit tracing. _Frontiers in neuroscience_ , page 897, 2019. 

- 770 [85] Zhuokun Ding, Paul G Fahey, Stelios Papadopoulos, Eric Y Wang, Brendan Celii, Christos Papadopoulos, 771 Alexander B Kunin, Andersen Chang, Jiakun Fu, Zhiwei Ding, et al. Functional connectomics reveals general 772 wiring rule in mouse visual cortex. _bioRxiv_ , 2023. 

772 

- 773 [86] Kunihiko Fukushima. Neocognitron: A self-organizing neural network model for a mechanism of pattern 774 recognition unaffected by shift in position. _Biological cybernetics_ , 36(4):193–202, 1980. 

- 775 [87] Guy Wallis and Edmund T Rolls. Invariant face and object recognition in the visual system. _Progress in_ 776 _neurobiology_ , 51(2):167–194, 1997. 

- 777 [88] M Riesenhuber and T Poggio. Hierarchical models of object recognition in cortex. _Nat. Neurosci._ , 778 2(11):1019–1025, November 1999. 

- 779 [89] Brett Vintch, J Anthony Movshon, and Eero P Simoncelli. A convolutional subunit model for neuronal 780 responses in macaque v1. _Journal of Neuroscience_ , 35(44):14829–14841, 2015. 

- 781 [90] Martin Schrimpf, Jonas Kubilius, Ha Hong, Najib J Majaj, Rishi Rajalingham, Elias B Issa, Kohitij Kar, Pouya 782 Bashivan, Jonathan Prescott-Roy, Franziska Geiger, et al. Brain-score: Which artificial neural network for 783 object recognition is most brain-like? _BioRxiv_ , page 407007, 2020. 

- 784 [91] Andrew S Bock, Paola Binda, Noah C Benson, Holly Bridge, Kate E Watkins, and Ione Fine. Resting-state 785 retinotopic organization in the absence of retinal input and visual experience. _Journal of Neuroscience_ , 786 35(36):12366–12382, 2015. 

- 787 [92] Ella Striem-Amit, Smadar Ovadia-Caro, Alfonso Caramazza, Daniel S Margulies, Arno Villringer, and Amir 788 Amedi. Functional connectivity of visual cortex in the blind follows retinotopic organization principles. 789 _Brain_ , 138(6):1679–1695, 2015. 

- 790 [93] Jun Zhuang, Lydia Ng, Derric Williams, Matthew Valley, Yang Li, Marina Garrett, and Jack Waters. An 791 extended retinotopic map of mouse cortex. _elife_ , 6:e18372, 2017. 

791 

- 792 [94] Troy A Hackett. Information flow in the auditory cortical network. _Hearing research_ , 271(1-2):133–146, 793 2011. 

22 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 794 [95] Corrie R Camalier, William R D’Angelo, Susanne J Sterbing-D’Angelo, Lisa A de la Mothe, and Troy A 795 Hackett. Neural latencies across auditory cortex of macaque support a dorsal stream supramodal timing 796 advantage in primates. _Proceedings of the National Academy of Sciences_ , 109(44):18168–18173, 2012. 

796 

- 797 [96] Alexei A Koulakov and Dmitri B Chklovskii. Orientation preference patterns in mammalian visual cortex: 798 a wire length minimization approach. _Neuron_ , 29(2):519–527, 2001. 

- 799 [97] Nicholas M Blauch, Marlene Behrmann, and David C Plaut. A connectivity-constrained computational 800 account of topographic organization in primate high-level visual cortex. _Proceedings of the National Academy_ 801 _of Sciences_ , 119(3):e2112566119, 2022. 

- 802 [98] Kenneth D Miller, Joseph B Keller, and Michael P Stryker. Ocular dominance column development: analysis 803 and simulation. _Science_ , 245(4918):605–615, 1989. 

- 804 [99] Miguel A Carreira-Perpinán, Richard J Lister, and Geoffrey J Goodhill. A computational model for the 805 development of multiple maps in primary visual cortex. _Cerebral Cortex_ , 15(8):1222–1233, 2005. 

- 806 [100] Geoffrey J Goodhill and David J Willshaw. Elastic net model of ocular dominance: overall stripe pattern 807 and monocular deprivation. _Neural Computation_ , 6(4):615–621, 1994. 

- 808 [101] Ryan T Philips and V Srinivasa Chakravarthy. The mapping of eccentricity and meridional angle onto 809 orthogonal axes in the primary visual cortex: an activity-dependent developmental model. _Frontiers in_ 810 _computational neuroscience_ , 9:3, 2015. 

- 811 [102] Hsin-Hao Yu, Declan P Rowley, Nicholas SC Price, Marcello GP Rosa, and Elizabeth Zavitz. A twisted 812 visual field map in the primate dorsomedial cortex predicted by topographic continuity. _Science advances_ , 813 6(44):eaaz8673, 2020. 

- 814 [103] Shenqin Yao, Quanxin Wang, Karla E Hirokawa, Benjamin Ouellette, Ruweida Ahmed, Jasmin Bomben, 815 Krissy Brouner, Linzy Casal, Shiella Caldejon, Andy Cho, Nadezhda I Dotson, Tanya L Daigle, Tom Egdorf, 816 Rachel Enstrom, Amanda Gary, Emily Gelfand, Melissa Gorham, Fiona Griffin, Hong Gu, Nicole Hancock, 817 Robert Howard, Leonard Kuan, Sophie Lambert, Eric Kenji Lee, Jennifer Luviano, Kyla Mace, Michelle 818 Maxwell, Marty T Mortrud, Maitham Naeemi, Chelsea Nayan, Nhan-Kiet Ngo, Thuyanh Nguyen, Kat North, 819 Shea Ransford, Augustin Ruiz, Sam Seid, Jackie Swapp, Michael J Taormina, Wayne Wakeman, Thomas 820 Zhou, Philip R Nicovich, Ali Williford, Lydia Potekhina, Medea McGraw, Lydia Ng, Peter A Groblewski, 821 Bosiljka Tasic, Stefan Mihalas, Julie A Harris, Ali Cetin, and Hongkui Zeng. A whole-brain monosynaptic 822 input connectome to neuron classes in mouse visual cortex. _Nat. Neurosci._ , 26(2):350–364, February 2023. 

- 823 [104] Rinaldo D D’Souza, Quanxin Wang, Weiqing Ji, Andrew M Meier, Henry Kennedy, Kenneth Knoblauch, and 824 Andreas Burkhalter. Hierarchical and nonhierarchical features of the mouse visual cortical network. _Nat._ 825 _Commun._ , 13(1):503, January 2022. 

- 826 [105] Carla J Shatz. Emergence of order in visual system development. _Journal of Physiology-Paris_ , 90(3-4):141– 827 150, 1996. 

- 828 [106] Sarah Cheng, Salwan Butrus, Liming Tan, Runzhe Xu, Srikant Sagireddy, Joshua T Trachtenberg, Karthik 829 Shekhar, and S Lawrence Zipursky. Vision-dependent specification of cell types and function in the devel830 oping cortex. _Cell_ , 185(2):311–327.e24, January 2022. 

- 831 [107] Charles D Gilbert and Wu Li. Top-down influences on visual processing. _Nat. Rev. Neurosci._ , 14(5):350–363, 832 May 2013. 

- 833 [108] S K McConnell, A Ghosh, and C J Shatz. Subplate pioneers and the formation of descending connections 834 from cerebral cortex. _J. Neurosci._ , 14(4):1892–1907, April 1994. 

- 835 [109] Verónica Moreno-Juan, Anton Filipchuk, Noelia Antón-Bolaños, Cecilia Mezzera, Henrik Gezelius, Belen An836 drés, Luis Rodríguez-Malmierca, Rafael Susín, Olivier Schaad, Takuji Iwasato, Roland Schüle, Michael Rut837 lin, Sacha Nelson, Sebastien Ducret, Miguel Valdeolmillos, Filippo M Rijli, and Guillermina López-Bendito. 838 Prenatal thalamic waves regulate cortical area size prior to sensory processing. _Nat. Commun._ , 8:14172, 839 February 2017. 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

- 840 [110] Francisco J Martini, Teresa Guillamón-Vivancos, Verónica Moreno-Juan, Miguel Valdeolmillos, and Guiller841 mina López-Bendito. Spontaneous activity in developing thalamic and cortical sensory networks. _Neuron_ , 842 109(16):2519–2534, August 2021. 

- 843 [111] Michael A Silver and Sabine Kastner. Topographic maps in human frontal and parietal cortex. _Trends Cogn._ 844 _Sci._ , 13(11):488–495, November 2009. 

- 845 [112] Rui Xu, Narcisse P Bichot, Atsushi Takahashi, and Robert Desimone. The cortical connectome of primate 846 lateral prefrontal cortex. _Neuron_ , 110(2):312–327.e7, January 2022. 

- 847 [113] MI Sereno, S Pitzalis, and A Martinez. Mapping of contralateral space in retinotopic coordinates by a 848 parietal cortical area in humans. _Science_ , 294(5545):1350–1354, 2001. 

- 849 [114] Daniel M van Es, Wietske van der Zwaag, and Tomas Knapen. Topographic maps of visual space in the 850 human cerebellum. _Current Biology_ , 29(10):1689–1694, 2019. 

- 851 [115] Andrew J Peters, Julie M J Fabre, Nicholas A Steinmetz, Kenneth D Harris, and Matteo Carandini. Striatal 852 activity topographically reflects cortical activity. _Nature_ , 591(7850):420–425, March 2021. 

- 853 [116] Edward H Silson, Peter Zeidman, Tomas Knapen, and Chris I Baker. Representation of contralateral visual 854 space in the human hippocampus. _Journal of Neuroscience_ , 41(11):2382–2392, 2021. 

- 855 [117] Jean-Pierre Changeux and Antoine Danchin. Selective stabilisation of developing synapses as a mechanism 856 for the specification of neuronal networks. _Nature_ , 264(5588):705–712, 1976. 

- 857 [118] Kouichi Hashimoto and Masanobu Kano. Postnatal development and synapse elimination of climbing fiber 858 to purkinje cell projection in the cerebellum. _Neuroscience research_ , 53(3):221–228, 2005. 

- 859 [119] Kouichi Hashimoto and Masanobu Kano. Synapse elimination in the developing cerebellum. _Cellular and_ 860 _molecular life sciences_ , 70:4667–4680, 2013. 

- 861 [120] Rosalina Fonseca, U Valentin Nägerl, Richard GM Morris, and Tobias Bonhoeffer. Competing for memory: 862 hippocampal ltp under regimes of reduced protein synthesis. _Neuron_ , 44(6):1011–1020, 2004. 

- 863 [121] Jan H Kirchner and Julijana Gjorgjieva. Emergence of local and global synaptic organization on cortical 864 dendrites. _Nat. Commun._ , 12(1):4005, June 2021. 

- 865 [122] Charles D Gilbert and Wu Li. Adult visual cortical plasticity. _Neuron_ , 75(2):250–264, July 2012. 

- 866 [123] Homare Yamahachi, Sally A Marik, Justin N J McManus, Winfried Denk, and Charles D Gilbert. Rapid axonal 867 sprouting and pruning accompany functional reorganization in primary visual cortex. _Neuron_ , 64(5):719– 868 729, December 2009. 

## 869 

## **Methods** 

## 870 

## **Cortical geometry, retinal waves, initial connectivity** 

871 In this section, we provide mathematical and implementation details common to all growth models described in 872 the paper. In each growth-rule case, the LGN-cortical synapses and cortico-cortical synapses share a common rule, 873 with identical parameters. 

874 **Geometry:** Numerical simulations are initialized with two sets of neurons: 1) LGN cells, which are assumed to be 875 driven by the retina via a log-conformal mapping, and 2) cells in the initially undifferentiated cortical sheet. LGN 876 neurons are arranged according to the log-conformal map from a visual hemifield, a shape qualitatively similar 877 to a semi-ellipse, which we use as our LGN geometry. The cortical sheet is modeled as a semi-infinite sheet of 878 neurons. The straight edge of the LGN semi-ellipse is aligned with the straight edge of the semi-infinite sheet, 879 lying above this sheet. The distance between two cortical neurons is a two-dimensional Euclidean distance on the 880 cortical sheet, and the distance between an LGN neuron and a cortical neuron is the simple three-dimensional 881 Euclidean distance between points on the two-dimensional Euclidean semi-sheet and the two-dimensional LGN 882 semi-ellipse. 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

883 We assume that the LGN neurons, which receive retinal input, all start and remain “in-degree saturated”, i.e., 884 the LGN neurons cannot accept any additional inputs from other LGN neurons or cortical neurons. 885 We denote the spatial position of neuron _i_ by **x** _i_ . Directed connections from neuron _j_ to neuron _i_ are rep886 resented by the connectivity matrix _Ci j_ , whose binary elements ( _{_ 0,1 _}_ ) represent the absence or presence of a 887 directed connection. 

888 Synaptic weights at the connection _Ci j_ are represented by _Wi j_ . Note that _Ci j_ = 0 implies _Wi j_ = 0, however 889 _Wi j_ = 0 does not imply _Ci j_ = 0, as in the case of silent synapses. 

890 **Activity:** Activity in our network model is driven by retinal waves, and this activity propagates though the LGN 891 and cortex via the connectivity and weights formed by the growth rules. In turn, the growth rules are fueled by 892 this propagated activity. Here we describe activity in the network given the connectivity, and then below describe 893 the growth rules given activity. 894 Our activity model is highly simplified to capture a core set of properties of activity generation in the retina 895 and propagation across the cortex. Retinal waves are spatiotemporally propagating fronts of activation. Each 896 wave is initiated locally and spreads to cover part of the retina. Several such waves together cover the whole 897 retina. Suppose a set of retinal waves together covers the whole retina at some timescale _τsa_ . Suppose that the 898 process of cortical development and plasticity has a timescale _τpl_ ; we discretize time into steps on this timescale, 899 and index these times as _{t_ , _t_ + 1, _t_ + 2, _···}_ ). We assume, based on empirical results, that these timesteps are 900 significantly longer than _τsa_ . Thus, we can take retinal activation within one such time-step to be uniform across 901 the whole retina. Mathematically, we therefore set retinal activity as _a[R]_ ( _i_ ; _t_ ) = 1 across all retinal positions _i_ and 902 development timesteps _t_ . 

903 We assume a fixed feedforward 1-1 connectivity between retinal locations and a topographic set of LGN neu904 rons. Thus, _a_ ( _i_ ; _t_ ) = _f_ ( _a[R]_ ( _i_ , _t_ )) for all _i ∈ LGN_ (that is, for all LGN neurons), and for all _t_ . Based on empirical 905 results we also assume that the dynamics of activity propagation from the retina into LGN and the cortex is at a 906 timescale _τsp_ that is rapid relative to both _τsa_ and _τpl_ . We call these discrete time-steps _δt_ (with _δt ≪_ 1). Thus, 907 activity propagation in the LGN and cortex in the developmental time interval [ _t_ , _t_ + 1] can be written by the 908 iteration: 

**==> picture [323 x 25] intentionally omitted <==**

909 where _Θ_ ( _x_ ) is the Heaviside-theta function ( _Θ_ ( _x_ ) = 0 if _x ≤_ 0, and _Θ_ ( _x_ ) = 1 for _x >_ 0); _εW ≪_ 1 is a small 910 threshold on all synaptic weights, applied to prevent activity propagation across synapses with negligible strength. 911 The iteration should be performed _N_ = _τsa/τsp ≫_ 1 times, until the next step. For simplicity, we set the neural 912 transformation to be linear with a prefactor close to 1, _f_ ( _x_ ) = _γx_ ( _γ ≤_ 1). With this simplification, we can 913 explicitly sum the iteration over _N_ synaptic propagation steps to obtain that at _t_ + 1, activity is given by: 

913 

**==> picture [311 x 31] intentionally omitted <==**

914 where _U ≡ Θ_ ( _W > εW_ ) is the thresholded weight matrix. 

915 For numerical simulations, it suffices for _N_ to be larger than or equal to the number of layers desired at the end 916 of the simulation; we choose _N_ to be 5 in all of our numerical results across all growth rules. The activity reduction 917 factor _γ <_ 1 promotes the formation of a hierarchy by incentivizing feed-forward connections from lower layers 918 (which will have stronger pre-synaptic activity) over lateral connections in higher layers (with weaker pre-synaptic 919 activity). 

920 

## **Heterosynaptic competition rule and implementation** 

921 In this growth rule, we assume a fully connected initial network (i.e., _Ci j_ = 1), but the weights _Wi j_ are zero, akin 922 to silent synapses. At each time-step, weights grow at a rate proportional to _∆i j_ , 

**==> picture [277 x 29] intentionally omitted <==**

923 with _di j_ = _|_ **x** _i −_ **x** _j|_ . In other words, the rate of growth of a synaptic weight increases with the presynaptic firing 924 rate _a j_ , and is inversely proportional to the distance between the pair of neurons. 

25 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

925 Within each neuron, we assume a competitive dynamics for synaptic strengthening, such that all incoming 926 weights to a cell are decremented by the same amount when their sum hits a bound _Wmax[in]_[,][and][all][outgoing] 927 weights from a cell are decremented by the same amount when their sum hits a bound _Wmax[out]_[.][Thus,][the][total] 928 weight update is given by: 

**==> picture [492 x 47] intentionally omitted <==**

## **Race to threshold rule and implementation** 

## 931 

932 In this model, as above, we assume a fully connected initial network (i.e., _Ci j_ = 1) with silent synapses ( _Wi j_ (0) = 933 0). At all future times, synaptic weights are binary ( _Wi j_ ( _t_ ) _∈{_ 0,1 _}_ ). 

933 

934 Let _ri j_ represent the accumulation of synaptic resources that are being ferried from the soma to each connec935 tion. Once this quantity exceeds a threshold that is set in an activity- and distance-dependent way, the synaptic 936 weight becomes non-zero. Specifically, 

**==> picture [375 x 13] intentionally omitted <==**

937 where the rate of resource ferrying is constant to all silent synapses for which the pre- and post-synaptic neurons 938 are not out- or in-degree saturated (the out- and in-degrees are smaller than _dmax_ ). For non-silent synapses, the 939 rate of resource ferrying saturates as a function of synaptic strength ( _Wi j_ ). _r_ 0 is a small regularization constant 940 for numerical stability, and does not affect the qualitative nature of the dynamics beyond this effect. 

941 

Synapse _i j_ gains a non-zero weight once it accumulates resources that exceed a threshold: 

**==> picture [280 x 12] intentionally omitted <==**

942 where the threshold _Ti j_ grows with the distance between neurons _i_ , _j_ and decreases with the level of presynaptic 943 activity: _Ti j_ = _T −_ 1+ _�di ja/jd_ 0[=] _[ T][−][∆][i j]_[.][Note that the threshold here is closely related to the key quantity] _[ ∆][i j]_[from] 944 the heterosynaptic competition rule. 

## 945 

## **Seeking and pruning rule and implementation** 

946 The two synaptic growth rules above are deterministic functions of neural activity. In contrast, seeking and pruning 947 is a stochastic rule, where synapses are discretely and stochastically formed, then pruned. In this model, there are 948 initially no connections, i.e., _Ci j_ = 0. Weights at all future times are binary ( _Wi j_ ( _t_ ) _∈{_ 0,1 _}_ ). 

949 At each time-point, we randomly select _ndraw_ neurons which are not yet out-degree saturated with probability 950 proportional to the magnitude of their activity (initially this _ndraw_ set resides entirely within LGN neurons, since 951 only they are active due to retinal input). Each of the _ndraw_ neurons attempts to generate _d[out]_ new synapses with 952 the set of _d[out]_ spatially closest neurons to it on the neural sheet. For any given synapse, say from neuron _i_ to 953 neuron _j_ , this attempt is successful if either of the following hold: (a) neuron _j_ has fewer than _d[in]_ synapses (it is 954 not in-degree saturated, defined in the general setup earlier), or (b) the “permanence” _Pi j_ (defined below) of the 955 new synapse is larger than the permanence of at least one of the existing synapses onto neuron _j_ . In case (b), the 956 synapse to neuron _j_ with the weakest permanence is pruned, and the synapse from neuron _i_ to neuron _j_ takes its 957 place. If neither (a) nor (b) hold, the synapse from _i_ to _j_ cannot be formed and neuron _i seeks_ out the next-nearest 958 neuron. This proceeds until neuron _i_ (and each of the _ndraw_ neurons) successfully connects to _d[out]_ . 

958 

959 The synaptic “permanence” of each attempted and formed synapse is given by _Pi j_ = 1+ _�di ja/jd_ 0[, which determines] 960 how resistant it is to pruning (permanence is closely related to a key quantity used in the other rules, _Pi j_ = _∆i j_ ). 961 The permanence of a synapse varies proportionally with the activity in the presynaptic neuron and inversely with 962 the spatial distance between the pre- and post-synaptic neurons on the neural sheet. 

26 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

963 

964 

## **Parameter choices** 

|**Parameter choices**|**Parameter choices**|**Parameter choices**|**Parameter choices**|**Parameter choices**|**Parameter choices**|
|---|---|---|---|---|---|
|Biophysicalgrowth modelsparameters||||||
|Seekingand Pruningmodel||Race for resources model||Heterosynaptic competition model||
|_Nx_<br>_Ny_<br>_kin_<br>_kout_<br>_d_0<br>_ndraw_|75<br>150<br>8<br>8<br>30<br>5|_Nx_<br>_Ny_<br>_kin_<br>_kout_<br>_d_0<br>_η_<br>_r_0<br>T|75<br>150<br>8<br>8<br>8<br>0.00025<br>0.2<br>10|_Nx_<br>_Ny_<br>_W in_<br>_max_<br>_W out_<br>_max_<br>_d_0<br>_wmax_<br>_ε_<br>_η_|75<br>150<br>5<br>5<br>20<br>4<br>2.15_×_10_−_4<br>5|



## **Greedy wiring process principle** 

965 

966 The greedy wiring process principle is a normative algorithm that results in formed networks that have the same 967 features as the equilibrium formed networks obtained by running any of the three growth rules described above. 968 This principle provides a direct algorithmic description of which neurons should be connected, without the need 969 for synaptic activity propagation and explicit spontaneous activity. 970 We begin as for the growth rules above: with a semi-elliptical LGN placed above a semi-infinite unparcellated 971 cortical sheet, and with LGN neurons whose in-degree has already been saturated by inputs from the retina. 972 We define the initial ‘current’ area to be LGN. The greedy wiring process principle dictates that the shortest 973 possible connections are placed first. We computationally iterate over increasing connection lengths _n∆d_ starting 974 from _n_ = 0. We begin in the current area, and place all connections from neurons _i_ to _j_ that satisfy all of the 975 following: (a) neuron _i_ is in the ‘current’ layer; (b) neuron _i_ is not out-degree saturated; (c) neuron _j_ is not in976 degree saturated; (d) the Euclidean distance from neuron _i_ to neuron _j_ is between ( _n −_ 1 _/_ 2) _∆d_ and ( _n_ + 1 _/_ 2) _∆d_ . 977 This continues with increasing _n_ until all neurons in the current layer have become out-degree saturated. 

977 978 The set of neurons that receive a direct input from the now-out-degree saturated current layer become the 979 new ‘current’ layer. The above process repeats again starting with _n_ = 0 until the new ‘current’ layer is out-degree 980 saturated, leading to the formation of successive layers. 

**Algorithm 1:** Greedy wiring process principle 

**Data:** A grid of neurons comprising LGN, an empty semi-infinte cortical sheet, _∆d_ . **Result:** A formed connectome consisting of multiple visual areas. _W_ ( _x⃗_ , _⃗x[′]_ ) _←_ 0; In-degree( _x⃗_ ) _←_ 0; Out-degree( _x⃗_ ) _←_ 0; _d_ ( _x⃗_ , _⃗x[′]_ ) _←∥x⃗ − x⃗[′] ∥_ ; Occupied _←{}_ ; Module(1) _←_ LGN ; **for** mod-num _←_ 1 _to n_ **do for** _n ←_ 1 _to D_ **do** _Spre ←_ Module(mod-num) _∩{x⃗|_ Out-degree( _x⃗_ ) _< kout[max][}]_[;] Choose _x⃗pre_ randomly from _Spre_ ; _Spost ←_ Occupied _[c] ∩{x⃗[′] |_ In-degree( _x[⃗][′]_ ) _} ∩{x⃗[′] |_ ( _n −_ 1 _/_ 2) _∆d ≤ d_ ( _x⃗pre_ , _⃗x[′]_ ) _<_ ( _n_ + 1 _/_ 2) _∆d}_ ; Choose _x⃗post_ randomly from _Spost_ ; _W_ ( _x⃗post_ , _⃗x post_ ) _←_ 1; In-degree( _x⃗post_ ) _←_ In-degree( _x⃗post_ )+1; Out-degree( _x⃗pre_ ) _←_ Out-degree( _x⃗pre_ )+1; **if** In-degree( _x⃗post_ ) = _kin[max]_ **then** Occupied _←_ Occupied _∪{x⃗post }_ ; Module(mod-num +1) _←_ Module(mod-num+1) _∪{x⃗post }_ ; **end end end** 

27 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

|981|For notational simplicity, the above pseudocode does not make an explicit distinction between_W_ and_WLGN_. It|For notational simplicity, the above pseudocode does not make an explicit distinction between_W_ and_WLGN_. It|
|---|---|---|
|982|instead treats all interactions to be encompassed within|the same_W_(**x**,**x**_′_)— the distinction between LGN neurons|
|983|and those in the cortical sheet can be assumed to lie in the coordinates**x**itself, with LGN neurons being placed at||
|984|a_ε ≪∆d_ distance above the cortical sheet.||
||Greedywiring processgrowth modelparameters||
||_Nx_<br>150||
|985|_Ny_<br>300<br>_kin_<br>10||
||_kout_<br>10||
||_∆d_<br>0.5||



## **Two cell types that generate feed-forward and local connections** 

986 987 In SI Fig. S5, we observed that formed connections in the heterosynaptic competition rule (i.e., whether they 988 are feed-forward connections or local lateral connections) are determined via either of the two parameters, _d_ 0 or 989 _γ_ . We observed that it could be possible to model two co-existing cell types by allowing them to have different 990 values of _d_ 0 or _γ_ . To explore the formation of the visual hierarchy with both cell types, we adapt the greedy wiring 991 minimization process to accommadate both types of cells. 992 We add a type 2 neuron to the greedy wiring minimization process as follows: Allowing type 2 neurons to 993 throw out local lateral connections would require the neuron to get selected as a presynaptic neuron _before_ all 994 other local laterally situated neurons in the same level of ‘hierarchy’ have become in-degree-saturated. We model 995 this by allowing newly connected neurons, if they are of type 2, to immediately get selected to throw connections to 996 the closest available in-degree-unsaturated neurons during the locally greedy wiring algorithm. More specifically, 997 we ignore the hierarchy constraint in selecting neurons in the inner-most for loop, i.e., _Spre_ is now defined as 998 _{x⃗|_ Out-degree( _x⃗_ ) _< kout[max][}]_[.] 999 Note that this is qualitatively similar to what is achieved by increasing _γ_ in the proposed biologically plausible 1000 growth rules — a larger _γ_ leads to neurons later in the hierarchy being more active, effectively reducing the 1001 distinguishing effect of hierarchy in the network as it forms. Thus, neurons in later areas are more equivalent to 1002 earlier neurons for larger _γ_ . Hence, in the locally greedy wiring minimization algorithm, allowing later neurons 1003 to be selected ignoring hierarchy qualitatively captures the nature of type 2 neurons as induced by variation of _γ_ 1004 (or variation of _d_ 0, cf. Fig. S5). 1005 Thus, this provides a direct, computationally faster method within the greedy wiring minimization principle to 1006 recreate the effect of the two discovered cell-types in the biologically plausible learning rules: Cell type 1, follows 1007 the usual greedy wiring process principle, and Cell type 2 follows the changed principle described above, allowing 1008 Cell type 2 neurons to be included in _Spre_ as soon as they are connected to the growing network of neurons. We 1009 then generate the results of Fig. 9 by creating a cortical sheet with an interleaved mixture of both cell types, and 1010 then allow the greedy wiring process algorithm to run until the formation of multiple layers. 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [203 x 303] intentionally omitted <==**

Figure S1: **Growth proceeds until the available cortical sheet is exhausted:** If the network growth rules are allowed to continue, then the growth continues to form additional hierarchical areas. Each formed area is concentrically arranged around the previous area (left), and all areas exhibit retinotopic mirror-reversed maps (middle: polar angle, right: eccentricity). 

1011 

## **Supplementary Information** 

29 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [306 x 40] intentionally omitted <==**

**----- Start of picture text -----**<br>
in-degree   = 15 in-degree   = 15<br>out-degree = 20 out-degree = 10<br>**----- End of picture text -----**<br>


**==> picture [206 x 103] intentionally omitted <==**

**==> picture [190 x 96] intentionally omitted <==**

**==> picture [190 x 96] intentionally omitted <==**

**==> picture [190 x 89] intentionally omitted <==**

**==> picture [190 x 85] intentionally omitted <==**

Figure S2: **Relative sizes of areas are determined by the in-degree and out-degree of neurons** The ratio of sizes of successive areas is given by the ratio of the out-degree to the in-degree of neurons in the cortical sheet. A ratio larger than 1 (left) results in successive areas increasing in size, and a ratio smaller than 1 (right) results in areas decreasing in size. 

**==> picture [374 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
30<br>V4<br>V3<br>V2<br>0 V1<br>0 20 40 60 80<br>receptive field eccentricity (deg)<br>field on LGN<br>area of receptive<br>**----- End of picture text -----**<br>


Figure S3: **Receptive fields on LGN in neural space do not have eccentricity dependence** Area of receptive field onto LGN for each neuron in the cortical sheet is computed through fitting a two-dimensional Gaussian and computing the product of the two standard deviations. This area shows no significant dependence on the eccentricity of the receptive field in visual field coordinates. 

30 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [342 x 275] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sample receptive field in<br>1.0 model visual coordinates<br>0.5<br>Sample receptive<br>field on model LGN<br>0.0<br>1.0 2.0 3.0 4.0 5.0<br>Ellipticity<br>Frequency of occurance<br>**----- End of picture text -----**<br>


Figure S4: **Receptive fields in visual space are more circular than fields in neural coordinates on LGN** A two-dimensional Gaussian function is fit to each receptive field (in visual or neural coordinates). The ellipticity is defined as the ratio of the larger standard deviation to the smaller standard deviation of this Gaussian. The distribution of ellipticities in visual coordinates (in red) tends towards smaller values (and hence more circular fields) as compared to the distribution of ellipticities in neural coordinates (in black). Insets show an example of a receptive field in visual and neural coordinates for a randomly chosen neuron 

**==> picture [352 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
320<br>160 cell type: projection neuron<br>80<br>40<br>d 20<br>0<br>10<br>5<br>cell type: interneuron<br>2.5<br>1<br>γ 0 γ 0 γ 0 γ 0 γ 0 γ 0 2 γ 0 22 γ 0 23 γ 0 24 γ 0 25 γ 0 2 γ 0<br>25 24 23 22 2<br>γ<br>**----- End of picture text -----**<br>


Figure S5: Robustness of the heterosynaptic competition rule to parameters _d_ 0 and _γ_ : Shown is _d_ 0 varied across 2 orders of magnitude and _γ_ across 4 orders of magnitude. Each plot is a 1d simulation and the formed weight matrix is displayed. The simulations shown in red-boxes have formed locally recurrent-like connections, as can be seen by the large number of nonzero elements along the diagonal of the weight matrices. Both axes are on a log scale. 

31 

bioRxiv preprint doi: https://doi.org/10.1101/2024.01.07.574543; this version posted January 8, 2024. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [105 x 52] intentionally omitted <==**

**==> picture [18 x 31] intentionally omitted <==**

**==> picture [114 x 55] intentionally omitted <==**

**==> picture [127 x 63] intentionally omitted <==**

**==> picture [118 x 63] intentionally omitted <==**

**==> picture [7 x 51] intentionally omitted <==**

**----- Start of picture text -----**<br>
Increasing flatness<br>**----- End of picture text -----**<br>


**==> picture [131 x 75] intentionally omitted <==**

**==> picture [116 x 75] intentionally omitted <==**

Figure S6: **The effect of geometry of LGN on the form of the retinotopic map:** (Bottom to top) Increasing flatness of the projection from retina to the putative LGN can lead to retinotopic maps that have alternations in eccentricity as well. Grey lines denote boundaries of areas ascertained by connectivity (which coincides precisely with alternations). 

32 

