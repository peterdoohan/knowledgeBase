bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 1 **Emerging many-to-one weighted mapping in hippocampus-amygdala network underlies** 

- 2 **memory formation** 

- 3 Jun Liu, Arron F Hall, & Dong V Wang* 

- 4 Department of Neurobiology & Anatomy, Drexel University College of Medicine, Philadelphia, 5 PA 19129. 

- 6 *Correspondence: dw657@drexel.edu 

- 7 **Abstract** 

- 8 Memories are crucial for our daily lives, yet the network-level organizing principle that governs 

- 9 neural representations of our experiences remains to be determined. Employing dual-site 

- 10 electrophysiology recording in freely behaving mice, we discovered that hippocampal dorsal 

- 11 CA1 (dCA1) and basolateral amygdala (BLA) utilize distinct coding strategies to represent novel 

- 12 experiences. A small assembly of BLA neurons rapidly emerged during memory acquisition and 

- 13 remained active during subsequent consolidation, whereas the majority of dCA1 neurons 

- 14 engaged in the same processes. Machine learning decoding revealed that dCA1 population 

- 15 spikes predicted the BLA assembly firing rate. This suggests that most dCA1 neurons 

- 16 concurrently index an episodic event by rapidly establishing weighted communications with a 

- 17 specific BLA assembly, a process we call “many-to-one weighted mapping.” Furthermore, we 

- 18 demonstrated that closed-loop optoinhibition of BLA activity triggered by dCA1 ripples after new 

- 19 learning resulted in impaired memory. These findings highlight a new principle of hippocampus- 

- 20 amygdala communication underlying memory formation and provide new insights into how the 

- 21 brain creates and stores memories. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 22 **Introduction** 

23 Converging evidence suggests that the formation of new memories involves a complex neural 24 network of multiple brain regions, including the hippocampal dorsal CA1 (dCA1) and basolateral 25 amygdala (BLA). How neuronal populations within these brain regions encode and exchange 26 information is yet to be fully understood [1-4]. The formation of episodic memories, or memories 27 of events, can be divided into two processes: memory acquisition and consolidation. Memory 28 acquisition is rapid and can index episodic events almost instantaneously; however, these 29 memories are often fragile and only become stabilized after a slow transformation process 30 known as memory consolidation [5, 6]. This process critically involves sleep, with dCA1 ripples, 31 fast oscillations (100–300 Hz) that occur predominantly during slow-wave sleep and immobility, 32 playing a crucial role [5-7]. Despite this understanding, it is still unclear how the dCA1–BLA 33 circuitry enables such rapid indexing and gradual consolidation of new memories. 

34 Memories of events consist of three primary components: where, when, and what [8, 9]. 35 Previous studies have demonstrated that the dCA1 encodes where and when by sequences 36 [10, 11]. In contrast, no consensus has been reached regarding how dCA1 neurons encode 37 specific events (what). Given the continuous unfolding of episodic events in our daily life, the 38 encoding of these events becomes intricately intertwined with recall of prior relevant 39 experiences. Consequently, dCA1 neurons become highly entangled in the process of encoding 40 both ongoing and past event information [12], making it challenging to disentangle dCA1 spike 41 patterns that specifically encode individual events. 

42 Presently, there are two major hypotheses regarding how the hippocampus encodes episodic 43 events (what). One prominent view holds that “(event) information is sparsely encoded in 44 distributed ensembles of hippocampal neurons” [13], although there is limited evidence 45 supporting this sparse-coding hypothesis by dCA1 neurons [13-15]. In fact, recent findings 46 suggest the contrary, revealing that a substantial portion of dCA1 neurons (up to 50%), instead 47 of a minority, are activated during fear memory procedures [16-19]. Moreover, it has been 48 shown that up to 30% dCA1 neurons exhibit co-activation upon exposure to two distinct 49 contexts [16], indicating a substantial overlap of dCA1 neurons in encoding different memories. 

- 50 The other influential view suggests that the hippocampus functions to link or bind, rather than 51 encode event information that is otherwise represented in a distributed neural network [20, 21]. 52 This viewpoint, however, fails to address the precise mechanisms through which dCA1 activity 53 effectively achieves such linking/binding, and it has not been directly tested experimentally. To 54 address this knowledge gap, our study employs a different approach to deduce dCA1 encoding 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 55 principles by computing activity correlations between dCA1 neurons and selective BLA 

- 56 assembles. This approach leverages recent findings that BLA neurons form distinct assembles 

- 57 to represent salient events [22-24]. 

- 58 **Results** 

- 59 **Emerging dCA1 ripple–BLA communication underlies memory consolidation** 

- 60 To investigate the encoding principles and communication dynamics of the dCA1 and BLA 

- 61 neuronal populations, we conducted dual-site _in vivo_ recording of the dCA1 and BLA (up to 16 

- 62 tetrodes per site; Figure 1A). All mice received a contextual fear memory procedure that 

- 63 consisted of pre-training sleep, training, post-training sleep, and fear recall test (Figure 1B). 64 Neuronal spikes and local field potentials (LFPs) were recorded throughout the entire process, 65 which enabled us to study dCA1–BLA neuronal ensemble dynamics at each memory stage, 66 including acquisition, consolidation, and retrieval. 

67 We first identified slow-wave sleep (SWS) stages based on prominent dCA1 delta [25] and 68 ripple oscillations (Figure 1C). Next, we conducted an independent component analysis (ICA) of 69 population spikes recorded during SWS to identify major BLA assembles, i.e., small groups of 70 co-activated neurons [26]. As an example, the ICA identified 14 assembles based on the activity 71 of 58 BLA neurons recorded during post-training SWS (Figure 1D; Figure S1). We observed that 72 one selective BLA assembly (#2), which we termed “BLA memory assembly,” robustly increased 73 its activity after a subset of dCA1 ripples (Figure 1E). Subsequent cross-correlation analysis 74 confirmed this observation and revealed additional BLA assembles that showed decreased (# 75 1&8), decreased followed by a rebound (#3), or little change of activity (Figure 1F). Notably, 76 none of these BLA assembles showed dCA1 ripple-correlated activity during pre-training sleep 77 (Figure 1F). This suggests the emergence of dCA1 ripple-to-BLA assembly communication 78 underlying memory consolidation. 

79 Next, we sought to determine if the BLA assembles preexisted prior to learning or if they were 80 newly formed during the learning process. Our analyses revealed that nearly all BLA assembles 81 were already highly active during the pre-training sleep (Figure 1G). This suggests that memory 82 formation primarily recruits preconfigured or preexisting BLA assembles [3], albeit with a minor 83 degree of membership swapping within certain assemblies. Additionally, we investigated the 84 time course of dCA1-to-BLA communication and found that such communication was more 85 prevalent during early-stage SWS (Figure 1 H&I). 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 86 **Memory-associated ripples are enlarged and elongated** 

- 87 We next asked if the dCA1 ripple-to-BLA assembly communication conveyed unique 

88 information. To address this, we classified dCA1 ripples into two categories: memory and non89 memory associated ripples. Memory-associated ripples were defined if they occurred coinciding 90 with BLA memory assembly activation, while the remaining ripples were defined as non-memory 91 ripples (Figure 2A). Our analyses revealed that memory-associated ripples had significantly 92 larger amplitude and longer duration (Figure 2B). Moreover, these memory-associated ripples 93 contained distinct contents, i.e., spikes of distinct dCA1 neurons (Figure 2C). Comparing 94 memory-associated ripples to non-memory ones, most dCA1 neurons showed further firing 95 changes on top of their already increased activity: about one third of them increased activity 96 while another one third decreased activity significantly (Figure 2D). These findings suggest that 97 dCA1 sends specific information to a selective BLA assembly for memory consolidation. 

98 We observed that the increased dCA1 activity during memory-associated ripples tend to be 99 prolonged (Figure 2D, right). To verify this, we conducted an unbiased analysis on all dCA1 100 neurons that increased activity during either memory or non-memory ripples. Our analyses 101 confirmed that dCA1 neuronal firings were elongated and more robust during memory102 associated ripples across animals (Figure 2E). These elongated dCA1 ripples and enhanced 103 firings likely signify the consolidation of newly formed memories [27]. Taken together, we 104 propose a model of ripple-associated memory consolidation, as depicted in Figure 2F. During 105 non-memory ripples, most dCA1 neurons exhibit a baseline probability of activation that possibly 106 represents preconfigured rigid motifs [28, 29]. Upon memory consolidation, relevant dCA1 107 neurons exhibit robust increase and/or prolongation of activity during ripples, while other dCA1 108 neurons show decrease or no change of activity, which collectively represent specific 109 information coding. 

- 110 **dCA1 population spikes predict BLA memory assembly firing rate** 

111 We next asked if dCA1 population spikes can predict the firing rate of BLA assembles or 112 neurons. To address this, we implemented generalized linear model (GLM) machine learning 113 decoding [30]. Given that dCA1 neuronal activity preceded BLA memory assembly activity by 114 ~35 ms (Figure 3 A&B), we used a shift of 35 ms or longer between dCA1 and BLA neurons for 

- 115 the GLM decoding. Overall, dCA1 and BLA neuronal spikes across multiple sliding windows 

- 116 (lasting 100 ms; Figure 3C) before or after dCA1 ripples were extracted: 50% of them were used 117 for training of the GLM decoder, and the remaining 50% were used for decoding. We used 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 118 correlation coefficients between the real and predicted firing rates to indicate prediction power, 

- 119 resulting in a scale between –1 and 1 (Figure 3D). 

- 120 Our findings demonstrated that the dCA1 population spikes predicted BLA memory assembly 

- 121 firing rate during the post-, but not pre-training sleep (Figure 3 D–F). This provides direct 

- 122 evidence of emerging weighted communications from dCA1 neurons to a selective BLA 

- 123 assembly in memory formation. In contrast, dCA1 population spikes had limited prediction on 

- 124 non-memory neurons, although the prediction power on a small subset of them appeared to be 

- 125 high during both pre- and post-training sleeps, which may reflect pre-existing dCA1-to-BLA 

- 126 communications (Figure 3G). Interestingly, the overall prediction power on non-memory neurons 127 decreased after learning (Figure 3G, right), suggesting a bias towards the consolidation of newly 128 acquired memories and skipping older ones, at least during the early-stage sleep. 

## 129 **Emerging many-to-one weighted mapping underlies memory formation** 

- 130 Previous attempts to directly characterize dCA1 spike patterns that encode specific episodic 131 events, such as receiving shocks or air puffs [2, 31], have not yielded a framework for 

- 132 understanding dCA1 information coding principles. Therefore, we employed a different 

- 133 approach to deduce the encoding principle of dCA1 neurons by analyzing their relationship with 134 selective BLA assembles. This leverages our findings of robust BLA memory assembly activity 135 during all memory stages that include acquisition, consolidation, and retrieval (Figure 1; Figure 136 S2). Our results revealed that most dCA1 neurons exhibit BLA assembly-correlated activity 137 during training and post-training sleep, but not pre-training sleep (Figure 4A). This suggests the 138 involvement of a significant proportion of dCA1 neurons compared to a small assembly of BLA 139 neurons in memory formation and consolidation. 

- 140 Next, we divided the dCA1 neurons into subgroups based on their high or low correlated activity 141 with the BLA memory assembly (Figure 4A). Our GLM decoding results showed that not only 142 the higher-, but also lower-weight dCA1 neurons predicted the BLA assembly firing rate (Figure 143 4 B&C). This suggests that the decoding of the BLA assembly activity involves a contribution 144 from many dCA1 neurons, rather than a few. Taken together, we propose a model of emerging 145 many-to-one weighted mapping from dCA1 neurons to a selective BLA assembly that underlies 146 the formation of a new memory (Figure 4D). 

- 147 Additionally, we conducted place cell analysis. Our results showed that subsets of dCA1 

- 148 neurons can function as place cells, with similar place field sizes between the higher- and lower- 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 149 weight neurons (Figure 4 E&F). These results suggest that memory coding (non-spatial) and 150 spatial coding are represented by partially overlapping groups of dCA1 neurons [32, 33]. 

## 151 **Closed-loop optoinhibition during post-training sleep impairs memory** 

- 152 To determine if dCA1 ripple-coincided BLA activity is necessary for memory consolidation, we 153 employed a closed-loop optoinhibition approach. We microinjected AAV-CaMKII-stGtACR2 [34] 

- 154 into the BLA bilaterally and then implanted two optic fibers slightly above the injection sites, 155 which enabled later optoinhibition of BLA pyramidal neurons. Meanwhile, we implanted four 156 tetrodes into the dCA1 to record ripple activity (Figure 5A). After 2–3 weeks to allow viral 157 expression, mice underwent a contextual fear conditioning procedure, followed by closed-loop, 158 delayed, or no-stimulation of the BLA (Figure 5B). This procedure lasted two hours during post159 training rest/sleep, similar to that reported previously [35, 36]. 

- 160 Our analysis showed that large-amplitude dCA1 ripples had a greater impact on memory 161 consolidation (Figure 2B). Therefore, we used a high threshold (8 s.d.) to trigger closed-loop 162 optoinhibitions, which preferentially targeted memory-associated ripples (Figure 5C). Our offline 163 analysis confirmed that the closed-loop group mice received the optoinhibition within a short 164 latency of ~10 ms after ripple detection, whereas the delayed group had an extended latency of 165 ~160 ms (Figure 5D). Behaviorally, the closed-loop group mice exhibited significantly reduced 166 freezing compared to the delayed or no-stimulation groups, indicating impaired contextual fear 167 memory (Figure 5E). 

- 168 **Discussion** 

- 169 Our findings suggest that most dCA1 neurons concurrently index an episodic event by rapidly 170 establishing weighted communications with a specific BLA assembly. We refer to this process 171 as “many-to-one weighted mapping.” The involvement of a significant portion of dCA1 neurons 172 in encoding a specific event presents several theoretical advantages. Firstly, this mechanism 173 offers immense encoding capacity due to the numerous potential combinations of dCA1 174 weighted mappings. Secondly, it provides robustness and redundancy, thereby enhancing 175 single-trial learning and minimizing potential disruptions from background or external noises [9, 176 37]. It is noteworthy that single-trial learning and memory formation are recognized as features 177 of biological intelligence in comparison to long-training sessions of artificial intelligence [38]. 

- 178 In essence, we propose that many-to-one weighted mappings are responsible for creating 

- 179 distinct memories in network representation. Specifically, when intermittent dCA1 firings occur 

- 180 that represent any significant mental or cognitive process spanning a few hundred milliseconds, 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

181 they constitute an exclusive population activity pattern. This patterned firing enables the 182 establishment of a unique weighted mapping from many dCA1 neurons to a specific BLA 183 assembly that represents the relevant significant event, likely through rapid long-term 184 potentiation [39]. In other words, distinct dCA1 population activity patterns communicate with 185 corresponding BLA assembles to rapidly index various episodic memories. It is possible that 186 one dCA1 population activity pattern simultaneously communicates with multiple neuronal 187 assembles that are distributed across the brain through collateral projections [40]. 188 Consequently, dCA1 reactivations during ripples bind these distributed assembles to form a 189 network representation of long-term memories. In support, we have demonstrated that closed190 loop optoinhibition of the BLA activity triggered by dCA1 ripples following a new learning 191 experience impairs relevant memory. 

192 Only a few studies have investigated hippocampus-amygdala interactions at the neuronal 193 ensemble level during memory formation [2, 3]. One study found that dCA1 neurons increased 194 correlation with selective BLA neurons during fear memory formation [2]. Our study extended 195 this finding by demonstrating that population dCA1 spikes predicted the firing rate of a selective 196 BLA assembly during ripples. Another study found that the BLA assembles are preconfigured 197 prior to memory acquisition [3]. Our results confirmed this and showed that the activity of these 198 preexisting BLA assembles was not driven by dCA1 ripples. We speculate that the recruitment 199 of preexisting BLA assembles to establish communication with the dCA1 enables rapid and 200 efficient circuit mapping. Together, an emerging hippocampus-to-amygdala communication 201 appears to underline emotional memory acquisition and consolidation. 

202 203 

204 

205 

206 207 

208 

209 

210 

211 

212 

Anatomically, dCA1 and BLA are not directly connected by synapses [41, 42]. Accordingly, we found that the dCA1-to-BLA information flow took about 35 ms, which indicates a di-synaptic communication. It appears that only the entorhinal, perirhinal, and ectorhinal cortices receive direct inputs from the dCA1 and project directly to the BLA, based on comprehensive anterograde and retrograde tracing studies shown in Allen Brain Connectivity and Mouse Connectome Project (Figure S3). Theoretically, information relayed from the dCA1 to BLA can utilize a many→fewer→one _or_ many→many→one principle (Figure S3). The former notion gains support in findings from immediate early gene studies, which have demonstrated that a large portion of dCA1 neurons (up to 50%) are activated during memory processing, whereas a moderate portion of entorhinal neurons (~25%), and only a small portion of BLA neurons (~10%) are activated in the same process [16-18]. These differences are further amplified with 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

213 decreasing neuron numbers, from ~400k in dCA1, ~330k in deep-layer entorhinal cortex, to only 214 ~83k in BLA of rats [43-46]. 

- 215 Our research also demonstrated that memory-associated dCA1 ripples are elongated, which is 216 consistent with a recent study showing that prolonging dCA1 ripples after learning improves 217 memory [27]. Furthermore, we found that the elongation of ripples is accompanied by an overall 218 prolongation and enhancement of neuronal firings in the dCA1, with some neurons increasing 219 while others decreasing their activity. Additionally, our results revealed that memory-associated 220 ripples were enlarged in amplitude, contrary to a previous study [27], which may reflect species 221 differences between mice and rats [47]. Together, our findings suggest that elongated and 222 enlarged ripples signify the consolidation of newly acquired memories, while shorter and smaller 223 ripples may indicate baseline activity or preconfigured dCA1 rigid motifs [28]. 

- 224 **Methods** 

225 **Mice.** Male C57BL/6 mice were purchased from the Jackson Laboratory (stock #000664). Mice 226 were 3–4 months old at the time of surgery; after surgery, they were singly housed in cages (40 227 × 20 × 25 cm) containing corn cob and cotton material and kept on a 12 h light/dark cycle 228 with _ad libitum_ access to food and water. Experimental procedures were approved by the 229 Institutional Animal Care and Use Committees of Drexel University and were in accordance with 230 the National Research Council _Guide for the Care and Use of Laboratory Animals_ . 

231 **Stereotaxic surgery.** Surgery procedures were similar to that used in our lab [23]. In brief, mice 232 were anesthetized with ketamine/xylazine mixture ( ∼ 100/10 mg/kg, i.p.) and kept on a heating 233 pad at 37°C. For _in vivo_ electrophysiology recording, mice received implantation of two 234 electrode arrays (8–16 tetrodes each) into the BLA and dCA1, respectively [48]. For closed-loop 235 optoinhibition, mice received microinjection of AAV viruses (AAV1-CKIIa-stGtACR2-FusionRed; 236 0.25 μl; _Addgene_ 105669) and implantation of two optic fibers (diameter 200 μm) into the BLA 237 bilaterally; meanwhile, they received implantation of 4 tetrodes into the dCA1 unilaterally. The 238 BLA coordinates were AP –1.7 mm, ML 3.4 mm, DV 3.9 mm; the dCA1 coordinates were AP – 239 2.6 mm, ML 1.8 mm, and DV 1.1 mm. 

240 _**In vivo**_ **electrophysiology.** Each tetrode consisted of four wires (90% platinum 10% iridium; 18 241 μm diameter; _California Fine Wire_ ). A microdrive was used to couple with the electrode bundle, 242 similar to that used in our lab [23, 25]. Neural signal was preamplified, digitized, and recorded 243 using a _Blackrock_ CerePlex or _Plexon_ acquisition system; meanwhile, animals’ behaviors were 244 recorded. With the _Blackrock_ system, the local field potentials (LFPs) were digitized at 2 kHz 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

245 and filtered at 500 Hz low cut; spikes were digitized at 30 kHz and filtered between 600–6000 246 Hz. For the _Plexon_ system, the LFPs were digitized at 1 kHz and filtered between 0.7–300 Hz; 247 spikes were digitized at 40 kHz and filtered between 400–7000 Hz. The tetrode arrays were 248 gradually lowered daily until we recorded clear ripples and a substantial number of neurons; 249 otherwise, mice were excluded from further analyses. The recorded spikes were sorted using 250 the MClust 3.5 [23]; key dataset was manually verified using _Plexon_ Offline Sorter. In total, 251 spikes from five mice were used for analyses in this study; the neuron numbers in BLA and 252 dCA1 were 58/55, 41/63, 36/52, 35/18, and 14/15, respectively. 

253 **Assembly detection by independent component analysis (ICA).** ICA was performed like that 254 described previously [26]. In brief, spike counts of each neuron were binned at 25 ms and z- 255 scored to generate a neuronal population activity matrix (neurons × bins). Coactivity patterns 256 were then extracted from this data matrix in two major steps. Firstly, the number of significant 257 coactivation patterns was estimated by calculating the principal components (PCs) of the data 258 matrix with variances above a threshold derived from an analytical probability function for 259 uncorrelated data (Marchenko-Pastur distribution; Figure S1). Secondly, fastICA was used to 260 extract the coactivity patterns from the projection of the data matrix into the subspace spanned 261 by the significant PCs. In simple terms, this method first finds the significant PCs and then 262 rotates them to match the ideal assembly patterns. These detected assembly patterns often 263 were comprised of a small number of neurons with high weights, along with a larger group of 264 neurons with low or zero weights. Neurons whose weights exceeded 2 s.d. from the mean 265 weight of each assembly pattern were classified as members of an assembly (Figure 1D). The 266 activation strength of each assembly was calculated by projecting the columns of the z-scored 267 spike matrix onto the axis defined by the corresponding assembly pattern. The activation events 268 were identified when the activation strength exceeded 5 s.d. from the mean activation strength 269 of each assembly (Figure S1B). To investigate the significance of activation event rates, we 270 computed the activation strength of surrogate assembles (500 surrogates for each assembly) 271 generated by randomly permuting the data matrix (Figure 1G; Figure S1B). For all activation 272 strength calculations, the assembly patterns extracted from post-training SWS sessions were 273 utilized as templates. 

274 

275 

276 

277 

**Ripples.** Ripples were band-pass filtered between 100–250 Hz and ripple envelope was smoothed with a Gaussian kernel of 32 ms [49]. Ripple amplitudes were defined as the peak values of ripple envelopes (Figure 2A): those with amplitude exceeding 3 s.d. above the mean were used for analysis in Figure 2. In Figures 1/3/4, ripple amplitudes exceeding 5 s.d. above 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

278 the mean were used for analysis. Ripple onsets and offsets were defined when ripple 279 amplitudes exceed 1 s.d. above the mean before and after corresponding ripple peaks (Figure 280 2A). Ripple length was defined as the duration between the ripple onset and offset: only those 281 longer than 20 ms were used for further analysis. 

282 **Memory and non-memory associated ripples.** We first identified BLA memory assembles or 283 neurons if: 1) they showed significant activations within 150 ms after dCA1 ripple onsets during 284 post- but not pre-training sleep (Figure 1F); and 2) they showed robust activation after receiving 285 footshocks (>5-fold above baseline lasting 10 min or longer; Figure S2). Ripples (recorded 286 during the post-training sleep) were defined as memory-associated ripples if the BLA memory 287 assembly or neuron showed high activation (2 s.d. above the median) within 150 ms of the 288 ripple onset. The remaining ripples were defined as non-memory ripples (Figure 2A). 

289 **Ripple contents** (related to Figure 2C) **.** M (or N) indicates the mean firing rate for each dCA1 290 neuron ±100 ms from memory-associated (or non-memory) ripples. Firing difference score M **|** N 291 was defined as abs(M–N)/(M+N). M1 **|** M2 was defined as abs(M1–M2)/(M1+M2), in which M1 292 and M2 indicate mean firing rates for each dCA1 neuron with randomly selected spikes (±100 293 ms from memory associated ripples). N1 **|** N2 was similarly defined as abs(N1–N2)/(N1+N2). 294 **GLM decoding.** We constructed generalized linear models (GLMs) with a log link function to 295 predict spike counts of single BLA assembles or neurons during ripples based on population 296 spike counts in dCA1 across specific time windows [30]. Ripples detected during pre- and post297 training sleeps, and all dCA1 and BLA neurons were included for the analysis. Spike counts of 298 each neuron or assembly were binned in 100-ms bins relative to ripple onset: −300 to −200 ms, 299 −200 to −100 ms, −100 to 0 ms, 0 to 100 ms for dCA1, and −65 to 35 ms, 35 to 135 ms, 135 to 300 235 ms, 235 to 335 ms for BLA. We used dCA1 population spike counts in different time bins to 301 predict the spike count of a single BLA assembly or neuron. We randomly partitioned the ripples 302 into two equally sized datasets: one of them was used to train the GLM decoder, and the other 303 was used for the test. For the test phase, the model derived from the training phase was applied 304 to the dCA1 population spike data in the test set, yielding predictions for the predicted BLA 305 spike counts across ripples. Lastly, we conducted correlation coefficient analysis between the 306 predicted and real BLA spike counts to measure GLM decoding power on a scale from −1 to 1. 307 **Place cell analysis.** To quantify place cells, the firing rate maps were generated in 1 × 1 cm 308 spatial bins in NeuroExplorer and smoothed by a Gaussian filter (filter width, 5 bins) before 309 being sent to MATLAB for further analyses. Low-activity dCA1 neurons with peak firing rate 310 within any given spatial bin <1 Hz were excluded from further analysis. A place field was 

**GLM decoding.** We constructed generalized linear models (GLMs) with a log link function to predict spike counts of single BLA assembles or neurons during ripples based on population spike counts in dCA1 across specific time windows [30]. Ripples detected during pre- and posttraining sleeps, and all dCA1 and BLA neurons were included for the analysis. Spike counts of each neuron or assembly were binned in 100-ms bins relative to ripple onset: −300 to −200 ms, −200 to −100 ms, −100 to 0 ms, 0 to 100 ms for dCA1, and −65 to 35 ms, 35 to 135 ms, 135 to 235 ms, 235 to 335 ms for BLA. We used dCA1 population spike counts in different time bins to predict the spike count of a single BLA assembly or neuron. We randomly partitioned the ripples into two equally sized datasets: one of them was used to train the GLM decoder, and the other was used for the test. For the test phase, the model derived from the training phase was applied to the dCA1 population spike data in the test set, yielding predictions for the predicted BLA spike counts across ripples. Lastly, we conducted correlation coefficient analysis between the predicted and real BLA spike counts to measure GLM decoding power on a scale from −1 to 1. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

311 identified by counting the number of spatial bins where a neuron's firing rate surpassed 50% of 312 its peak firing rate. A neuron with combined place fields of less than one third of the total 313 exploration area was considered a place cell. 

314 **Fear conditioning (** _**in vivo**_ **recording).** The fear-conditioning chamber used in the experiment 315 was a square chamber measuring 25 × 25 × 32 cm, with a 36-bar shock grid floor ( _Med_ 316 _Associates_ ). The behaviors of the mice were recorded using either the Blackrock Neurotech 317 NeuroMotive or Plexon CinePlex video system. During training, the mice were first allowed to 318 explore the footshock chamber for ∼ 3 minutes. They then received up to 10 mild footshocks 319 (0.75 mA, 0.5 sec), with a 2–3 min interval between shocks. Note that we used direct-current 320 footshocks to minimize electromagnetic noise, so occasionally mice missed a shock if they 321 stood on two positively or negatively charged grids. One minute after the last shock, the mice 322 were returned to their home cages. Approximately 2 hours later, the mice were placed back in 323 the footshock chamber for a 5-minute contextual fear test. Neural activity was recorded 324 continuously, including the pre-training sleep (1–2 hours), training ( ∼ 0.5 hour), post-training 325 sleep (1–2 hours), and contextual fear test (5 min). 

326 **Fear conditioning (closed-loop optoinhibition).** Three groups of mice were used: 1) closed327 loop; 2) delayed; and 3) no-stimulation groups. All mice were singly housed and received daily 328 handling for 1–2 weeks. All mice underwent a contextual fear procedure that consisted of three 329 footshocks (0.75 mA, 2 sec; 1–1.5 min apart), similar to that described previously [50]. Freezing 330 behaviors were automatically scored using _Med Associates_ VideoFreeze [50]. To conduct 331 closed-loop optoinhibition, we used the _Open Ephys_ recording system and _Opto Engine_ lasers. 332 Only large dCA1 ripples (raw 100–250 Hz filtered traces) with peak amplitude exceeding 8 s.d. 333 [51] were used to trigger bilateral optoinhibition of the BLA (0.5 mW; 150 ms), either 334 immediately (closed-loop group) or after a delay of 150 ms (delayed-stimulation group). 

335 **Histology.** To mark the final recording sites, we made electrical lesions by passing 20-second, 336 10-μA currents through two tetrodes. Mice were deeply anesthetized and intracardially perfused 337 with ice-cold PBS or saline, followed by 10% formalin. The brains were removed and postfixed 338 in formalin for at least 24 hours. The brains were sliced into coronal sections of 50-μm thickness 339 using _Leica_ vibratome. Sections from the dual-site recording mice were stained with cresyl violet 340 for microscopic examination of electrode placements, whereas other sections were mounted 341 with Mowiol mounting medium mixed with DAPI for microscopic fluorescent examination of viral 342 vector expression and optical fiber placements. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 343 **Statistics.** Sample sizes were based on previous similar studies in our labs [23, 25]. To 

- 344 determine firing-rate change during dCA1 ripples, the value that deviates from the mean by a _z_ - 

- 345 score of >3.3 (P < 0.001) for at least three consecutive bins (bin = 5 ms) was considered 

- 346 significant. Other statistical analyses include Analysis of Variance (ANOVA) followed by post- 

- 347 hoc Bonferroni, Wilcoxon rank-sum test, and Student’s _t_ test. All statistical tested are two-sided 

- 348 when applicable; P-values of 0.05 or lower were considered significant. 

- 349 **Acknowledgements** 

- 350 We thank Dr. Vitor Lopes-dos-Santos for discussions on the ICA analysis and Drs. Gideon 

- 351 Rothchild and Hualou Liang for discussions on the GLM decoding. We thank Dr. Wen-Jun Gao 

- 352 for comments on an earlier version. This work was supported by the National Institutes of Health 353 grants R01MH119102 (D.V.W.) and F31MH134582 (A.F.H.). 

- 354 **Author contributions** 

- 355 Conceptualization & Methodology: LJ, DVW; Investigation: LJ, AFH, DVW; Writing – original draft: 356 LJ, DVW; Writing – review & editing: LJ, AFH, DVW 

- 357 **Competing interests:** The authors declare no competing interests. 

- 358 **Data and materials availability:** All data, code, and materials used in the analysis will be 359 available upon publication of this manuscript. 

- 360 

## **Supplementary Materials** 

- 361 Figs. S1 to S3 

- 362 

## **References** 

- 363 1. Kitamura, T., et al., _Engrams and circuits crucial for systems consolidation of a memory._ Science, 364 2017. **356** (6333): p. 73-78. 

- 365 2. Girardeau, G., I. Inema, and G. Buzsaki, _Reactivations of emotional memory in the hippocampus-_ 366 _amygdala system during sleep._ Nat Neurosci, 2017. **20** (11): p. 1634-1642. 

- 367 3. Miyawaki, H. and K. Mizuseki, _De novo inter-regional coactivations of preconfigured local_ 368 _ensembles support memory._ Nat Commun, 2022. **13** (1): p. 1272. 

- 369 4. Kim, W.B. and J.H. Cho, _Encoding of contextual fear memory in hippocampal-amygdala circuit._ 370 Nat Commun, 2020. **11** (1): p. 1382. 

- 371 5. Walker, M.P. and R. Stickgold, _Sleep-dependent learning and memory consolidation._ Neuron, 372 2004. **44** (1): p. 121-33. 

- 373 6. Diekelmann, S. and J. Born, _The memory function of sleep._ Nat Rev Neurosci, 2010. **11** (2): p. 114374 26. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 375 7. Buzsaki, G., _Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and_ 376 _planning._ Hippocampus, 2015. **25** (10): p. 1073-188. 

- 377 8. Ergorul, C. and H. Eichenbaum, _The hippocampus and memory for "what," "where," and "when"._ 378 Learn Mem, 2004. **11** (4): p. 397-405. 

- 379 9. Sugar, J. and M.B. Moser, _Episodic memory: Neuronal codes for what, where, and when._ 380 Hippocampus, 2019. **29** (12): p. 1190-1205. 

- 381 10. Buzsaki, G. and D. Tingley, _Space and Time: The Hippocampus as a Sequence Generator._ Trends 382 Cogn Sci, 2018. **22** (10): p. 853-869. 

- 383 11. Eichenbaum, H., _Time cells in the hippocampus: a new dimension for mapping memories._ Nat 384 Rev Neurosci, 2014. **15** (11): p. 732-44. 

- 385 12. Moser, M.B. and E.I. Moser, _Distributed encoding and retrieval of spatial memory in the_ 386 _hippocampus._ J Neurosci, 1998. **18** (18): p. 7535-42. 

- 387 13. Kandel, E.R., Y. Dudai, and M.R. Mayford, _The molecular and systems biology of memory._ Cell, 388 2014. **157** (1): p. 163-86. 

- 389 14. Nadel, L. and M. Moscovitch, _Memory consolidation, retrograde amnesia and the hippocampal_ 390 _complex._ Curr Opin Neurobiol, 1997. **7** (2): p. 217-27. 

- 391 15. Josselyn, S.A. and S. Tonegawa, _Memory engrams: Recalling the past and imagining the future._ 392 Science, 2020. **367** (6473). 

- 393 16. Ramirez, S., et al., _Creating a false memory in the hippocampus._ Science, 2013. **341** (6144): p. 394 387-91. 

- 395 17. Tayler, K.K., et al., _Reactivation of neural ensembles during the retrieval of recent and remote_ 396 _memory._ Curr Biol, 2013. **23** (2): p. 99-106. 

- 397 18. Zelikowsky, M., et al., _Neuronal ensembles in amygdala, hippocampus, and prefrontal cortex_ 

- 398 _track differential components of contextual fear._ J Neurosci, 2014. **34** (25): p. 8462-6. 

- 399 19. Liu, X., et al., _Optogenetic stimulation of a hippocampal engram activates fear memory recall._ 400 Nature, 2012. **484** (7394): p. 381-5. 

- 401 20. Fortin, N.J., K.L. Agster, and H.B. Eichenbaum, _Critical role of the hippocampus in memory for_ 402 _sequences of events._ Nat Neurosci, 2002. **5** (5): p. 458-62. 

- 403 21. Eichenbaum, H., _Hippocampus: cognitive processes and neural representations that underlie_ 404 _declarative memory._ Neuron, 2004. **44** (1): p. 109-20. 

- 405 22. Redondo, R.L., et al., _Bidirectional switch of the valence associated with a hippocampal_ 406 _contextual memory engram._ Nature, 2014. **513** (7518): p. 426-30. 

- 407 23. Liu, J., L. Lin, and D.V. Wang, _Representation of Fear of Heights by Basolateral Amygdala_ 408 _Neurons._ J Neurosci, 2021. **41** (5): p. 1080-1091. 

- 409 24. Liu, J., et al., _Neural Coding of Appetitive Food Experiences in the Amygdala._ Neurobiol Learn 410 Mem, 2018. **155** : p. 261-275. 

- 411 25. Wang, D.V., et al., _Mesopontine median raphe regulates hippocampal ripple oscillation and_ 412 _memory consolidation._ Nat Neurosci, 2015. **18** (5): p. 728-35. 

- 413 26. Lopes-dos-Santos, V., S. Ribeiro, and A.B. Tort, _Detecting cell assemblies in large neuronal_ 414 _populations._ J Neurosci Methods, 2013. **220** (2): p. 149-66. 

- 415 27. Fernandez-Ruiz, A., et al., _Long-duration hippocampal sharp wave ripples improve memory._ 416 Science, 2019. **364** (6445): p. 1082-1086. 

- 417 28. Hall, A.F. and D.V. Wang, _The two tales of hippocampal sharp-wave ripple content: The rigid and_ 418 _the plastic._ Prog Neurobiol, 2023. **221** : p. 102396. 

- 419 29. Grosmark, A.D. and G. Buzsaki, _Diversity in neural firing dynamics supports both rigid and_ 420 _learned hippocampal sequences._ Science, 2016. **351** (6280): p. 1440-3. 

- 421 30. Rothschild, G., E. Eban, and L.M. Frank, _A cortical-hippocampal-cortical loop of information_ 422 _processing during memory consolidation._ Nat Neurosci, 2017. **20** (2): p. 251-259. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 423 31. McEchron, M.D., W. Tseng, and J.F. Disterhoft, _Single neurons in CA1 hippocampus encode trace_ 424 _interval duration during trace heart rate (fear) conditioning in rabbit._ J Neurosci, 2003. **23** (4): p. 425 1535-47. 

- 426 32. Tanaka, K.Z., et al., _The hippocampal engram maps experience but not place._ Science, 2018. 427 **361** (6400): p. 392-397. 

- 428 33. Aronov, D., R. Nevers, and D.W. Tank, _Mapping of a non-spatial dimension by the hippocampal-_ 429 _entorhinal circuit._ Nature, 2017. **543** (7647): p. 719-722. 

- 430 34. Mahn, M., et al., _High-efficiency optogenetic silencing with soma-targeted anion-conducting_ 431 _channelrhodopsins._ Nat Commun, 2018. **9** (1): p. 4125. 

- 432 35. Girardeau, G., et al., _Selective suppression of hippocampal ripples impairs spatial memory._ Nat 433 Neurosci, 2009. **12** (10): p. 1222-3. 

- 434 36. Maingret, N., et al., _Hippocampo-cortical coupling mediates memory consolidation during sleep._ 435 Nat Neurosci, 2016. **19** (7): p. 959-64. 

- 436 37. Wiltgen, B.J., et al., _Context fear learning in the absence of the hippocampus._ J Neurosci, 2006. 437 **26** (20): p. 5484-91. 

- 438 38. Coppolino, S. and M. Migliore, _An explainable artificial intelligence approach to spatial_ 439 _navigation based on hippocampal circuitry._ Neural Netw, 2023. **163** : p. 97-107. 

- 440 39. Lynch, M.A., _Long-term potentiation and memory._ Physiol Rev, 2004. **84** (1): p. 87-136. 

- 441 40. Ciocchi, S., et al., _Brain computation. Selective information routing by ventral hippocampal CA1_ 442 _projection neurons._ Science, 2015. **348** (6234): p. 560-3. 

- 443 41. van Groen, T. and J.M. Wyss, _Extrinsic projections from area CA1 of the rat hippocampus:_ 

- 444 _olfactory, cortical, subcortical, and bilateral hippocampal formation projections._ J Comp Neurol, 445 1990. **302** (3): p. 515-28. 

- 446 42. Oh, S.W., et al., _A mesoscale connectome of the mouse brain._ Nature, 2014. **508** (7495): p. 207447 14. 

- 448 43. Berdel, B., J. Morys, and B. Maciejewska, _Neuronal changes in the basolateral complex during_ 449 _development of the amygdala of the rat._ Int J Dev Neurosci, 1997. **15** (6): p. 755-65. 

- 450 44. Mulders, W.H., M.J. West, and L. Slomianka, _Neuron numbers in the presubiculum,_ 

- 451 _parasubiculum, and entorhinal area of the rat._ J Comp Neurol, 1997. **385** (1): p. 83-94. 

- 452 45. Merrill, D.A., A.A. Chiba, and M.H. Tuszynski, _Conservation of neuronal number and size in the_ 453 _entorhinal cortex of behaviorally characterized aged rats._ J Comp Neurol, 2001. **438** (4): p. 445454 56. 

- 455 46. Schmidt, B., D.F. Marrone, and E.J. Markus, _Disambiguating the similar: the dentate gyrus and_ 456 _pattern separation._ Behav Brain Res, 2012. **226** (1): p. 56-65. 

- 457 47. Mou, X., et al., _Comparing Mouse and Rat Hippocampal Place Cell Activities and Firing Sequences_ 458 _in the Same Environments._ Front Cell Neurosci, 2018. **12** : p. 332. 

- 459 48. Lin, L., et al., _Large-scale neural ensemble recording in the brains of freely behaving mice._ J 460 Neurosci Methods, 2006. **155** (1): p. 28-38. 

- 461 49. Karlsson, M.P. and L.M. Frank, _Awake replay of remote experiences in the hippocampus._ Nat 462 Neurosci, 2009. **12** (7): p. 913-8. 

- 463 50. Opalka, A.N. and D.V. Wang, _Hippocampal efferents to retrosplenial cortex and lateral septum_ 464 _are required for memory acquisition._ Learn Mem, 2020. **27** (8): p. 310-318. 

- 465 51. Wang, D.V. and S. Ikemoto, _Coordinated Interaction between Hippocampal Sharp-Wave Ripples_ 466 _and Anterior Cingulate Unit Activity._ J Neurosci, 2016. **36** (41): p. 10663-10672. 

467 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [468 x 435] intentionally omitted <==**

468 469 **Figure 1. Emerging dCA1 ripple-to-BLA assembly communication during memory consolidation.** 470 **A,** Schematic of dual-site recording (top) and representative brain sections showing recording sites in the 471 BLA and dCA1 (bottom). Inset, a self-constructed 16-tetrode array. **B,** Schematic of contextual fear 472 memory procedure. **C,** Spectrogram (left), and power spectral density analysis (right) of representative 473 dCA1 LFP recorded during post-training sleep. **D,** Independent component analysis identified 14 474 assembles (shown in colors) based on spikes of 58 BLA neurons recorded during the same sleep session 475 as shown in C. **E,** Representative dCA1 LFP, band-pass filtered ripples (100–250 Hz), and spikes of the 476 same 58 BLA neurons as shown in D. Note that assembly-2 exhibits robust activation after a subset of 477 dCA1 ripples. **F,** Cross-correlograms between dCA1 ripples (n = 2147) and the 14 BLA assembles. Grey 478 and color lines indicate pre- and post-training sleep, respectively. **G,** Activation rates of all identified BLA 479 assembles (n = 48 from 5 mice) are significantly higher than chance during both pre- and post-training 480 sleep. P < 0.0001, F1.860, 87.42 = 208.6, one-way ANOVA; ****P < 0.0001, Bonferroni post-hoc. **H,** Cross481 correlograms between dCA1 ripples and BLA assembly-2 (as shown in E) across post-training 20-min 482 sleep epochs. **I,** A gradual decay in the correlation between dCA1 ripples and BLA memory neurons (n = 483 10 from 5 mice) across the post-training sleep epochs. P = 0.0003, F1.307, 11.77 = 22.02, one-way ANOVA; 484 **P = 0.0039, *P = 0.0108, **P = 0.0041, Bonferroni post-hoc. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

485 

**==> picture [468 x 338] intentionally omitted <==**

486 **Figure 2. Memory-associated ripples are enlarged and elongated.** 487 **A,** The BLA assembly (assembly #2 as shown in Figure 1 D/E) exhibits activation at larger/longer ripples. 488 Overall, 219 memory and 2390 non-memory ripples were classified in this post-training recording session 489 (~1h). **B,** Memory-associated ripples have significantly larger amplitude (left) and longer duration (right). 490 **C,** Memory-associated ripples convey distinct contents. M/M1/M2 and N/N1/N2 indicate memory and non491 memory ripples, respectively (see **Methods** ). **D,** Left, z-scored activity of dCA1 neurons (n = 55; recorded 492 simultaneously with the 58 BLA neurons as shown in Figure 1 D/E) in relation to the onset of non-memory 493 ripples. Middle, activity difference of the same 55 dCA1 neurons in relation to memory _vs._ non-memory 494 ripples. The neurons are arranged in the same order in the two heatmaps. Right, mean activity of the 495 activated (#1–18), unmodulated (#19–39), and inhibited dCA1 neurons (#40–55). **E,** Left, Mean activity (± 496 s.e.m.) of all dCA1 neurons that were activated during memory or non-memory ripples (n = 105 _vs._ 171 497 neurons, from 5 mice). Middle & Right, dCA1 neuronal activity was higher and peaked later at memory498 associated ripples. **F,** Our proposed model of large/elongated ripples that contain distinct contents. 499 Red/blue ticks denote dCA1 neurons that decrease or increase activity; light blue ticks denote dCA1 500 neurons that show emerged activity; grey ticks denote dCA1 neurons that show little activity change 501 during memory-associated ripples. All statistics are Wilcoxon rank-sum test. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

502 

**==> picture [468 x 300] intentionally omitted <==**

503 **Figure 3. dCA1 population spikes can decode BLA assembly firing rate.** 

504 **A,** Mean peri-ripple histograms (± s.e.m.) of simultaneously recorded dCA1 neurons and one BLA 505 memory assembly. **B,** Peak firing rate latencies of dCA1 neurons and BLA memory neurons. **C,** Diagram 506 of GLM decoding. Spikes of dCA1 and BLA neurons were binned at multiple 100-ms time windows. 507 “Predictor cells” indicate dCA1 neurons; “Predicted cell” indicates a BLA assembly or neuron. **D,** 508 Decoding the firing rate of one representative BLA memory assembly based on population dCA1 spike 509 counts sampled at multiple bins as shown in C. **E&F,** Correlation coefficients between real and predicted 510 firing rates of BLA memory neurons across multiple bins. Only recordings of 50 dCA1 neurons or more 511 simultaneously (from 3 mice) were used for the decoding. Wilcoxon rank-sum tests revealed significant 512 differences between the real and shuffled data at all time windows (P = 0.0148, 0.0030, 0.0002 for −200 513 to −100, −100 to 0, 0–100 ms windows in E; P = 0.0002, 0.0002, 0.0019 for −65 to 35, 35–135, 135–235 514 ms windows in F) except the -300 to -200-ms window in E (P = 0.1049) and 235–335 ms window in F (P 515 = 0.6454). **G,** Correlation coefficients between real and predicted firing rates of BLA memory and non516 memory (other) neurons during pre- or post-training sleep. ***P = 0.0008, ***P = 0.0002, paired _t_ test. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

517 

**==> picture [422 x 466] intentionally omitted <==**

518 **Figure 4. Emerging many-to-one weighted mapping underlies memory formation.** 519 **A,** Cross-correlogram heatmaps between one BLA memory assembly and simultaneously recorded dCA1 520 neurons during the pre-training sleep (left), training (middle), and post-training sleep (right). Neurons are 521 arranged in the same order in the three heatmaps. **B,** Both the top 50% (corresponding to neurons #1–27 522 shown in A) and bottom 50% neurons (#29–55) predicted the firing rates of the BLA assembly, in 523 comparison to the shuffled data (repeated for 100 times). **C,** Both the top 50% and bottom 50% neurons 524 predicted the firing rates of individual BLA memory neurons (n = 8). Only recordings of 50 dCA1 neurons 525 or more simultaneously (from 3 mice) were used for the decoding. **P < 0.01; ***P < 0.001; ****P < 526 0.0001; paired _t_ test. **D,** Proposed model of many-to-one weighted mapping from dCA1 to BLA. **E,** A 527 representative navigation path (left) and firing rate heatmaps of 4 example dCA1 neurons. **F,** Left, number 528 of place cells among the top or bottom 50% dCA1 neurons from individual mice (n = 3; shown in different 529 colors). Right, similar place field sizes between the top and bottom 50% place cells (P = 0.2180, unpaired 530 _t_ test). 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

531 

**==> picture [390 x 465] intentionally omitted <==**

532 **Figure 5. Closed-loop optoinhibition during sleep impairs memory consolidation.** 533 **A,** Schematic of surgical procedure (top), and representative coronal sections showing viral 534 expression mainly in the BLA (middle) and recording site in the dCA1 (bottom). **B,** Schematic of 535 contextual fear memory procedure and closed-loop optoinhibition. **C,** Ripples detected at higher threshold 536 (8 _vs._ 6 _vs._ 4 s.d.) have higher selectivity of memory-associated ripples. Selectivity index = M/(M+N). M 537 (or N) indicates the percentage of above-threshold ripples among memory-associated (or non-memory) 538 ripples. **D,** Optoinhibition latencies of the closed-loop group mice (top) and delayed-stimulation group 539 (bottom). **E,** Closed-loop group mice shows impaired fear memory compared to delayed- or no-stimulation 540 groups (P = 0.0013, F2, 19 = 9.583, one-way ANOVA; *P = 0.0303, **P = 0.0011, Bonferroni post-hoc). 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

541 

**==> picture [363 x 324] intentionally omitted <==**

542 **Figure S1. Independent component analysis (ICA). A,** Correlation coefficient map of 58 BLA neurons 543 (left; the same neurons as shown in Figure 1D) and Eigenvalues of the principle components (right; 544 Marchenko-Pastur threshold was used to determine the number of assembles). **B,** Activity strength of 545 assembly 2 (as shown in Figure 1 D/E) during pre- and post-training sleep and surrogate. 

546 

**==> picture [435 x 183] intentionally omitted <==**

547 **Figure S2. Emerged BLA memory assembly activity after footshock delivery. A,** Left, the same 548 assembly 2 (neurons #6–9) as shown in Figure 1 D/E. Middle & Right, firing rate histograms of the same 549 4 neurons during contextual fear training (middle; 10 footshocks) and memory retrieval (right). **B,** Mean 550 activity (± s.e.m.) of BLA memory neurons during the training (top) and memory retrieval (bottom). Note 551 that there’s little change of activity between 0–3 min before footshock delivery. 

bioRxiv preprint doi: https://doi.org/10.1101/2023.09.06.556568; this version posted September 6, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

552 

**==> picture [476 x 367] intentionally omitted <==**

553 **Figure S3. dCA1 communicates with BLA indirectly. A,** Retrograde tracing of inputs to the BLA. 554 Retrograde tracer CTB was microinjected into the BLA (A1). A2–A4, Retrograde labeling of neurons 555 primarily in deep layers of entorhinal (Ent), perirhinal (Prh), and ectorhinal cortices (Ect). **B,** Anterograde 556 tracing of dCA1 efferents. Anterograde tracer (AAV-Syn-EGFP) was microinjected into the dCA1 and 

557 adjacent subiculum (B2). Anterograde projection is seen mainly in the Ent (B3) and Prh/Ect (B2–B4), but 558 minimal in the BLA. **C,** Two theoretical models of dCA1-to-BLA communication (many→fewer→one _vs._ 559 many→many→one). Brain images are adapted from Mouse Connectome Project (A; 560 https://cic.ini.usc.edu/) and Allen Brain Atlas (B; https://connectivity.brain-map.org/). 

