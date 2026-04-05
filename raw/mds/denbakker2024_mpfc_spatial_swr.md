bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 1 Neurons in the medial prefrontal cortex are involved in spatial tuning and signaling 2 upcoming choice independently from hippocampal sharp-wave ripples. 

- 3 

- 4 Hanna den Bakker[1,2,*] , Fabian Kloosterman[1,2] 

- 5 1 Neuro-Electronics Research Flanders, Leuven, Belgium 

- 6 2 Brain & Cognition, KU Leuven, Leuven, Belgium 

- 7 * Corresponding author: hanna.denbakker@kuleuven.be 

- 8 

- 9 ABSTRACT 

- 10 The hippocampus is known to encode spatial information and reactivate experienced trajectories 

- 11 during sharp-wave ripple events. These events are thought to be key time-points at which 12 information about learned trajectories is transferred to the neocortex for long-term storage. It is 13 unclear, however, how this information may be transferred and integrated in downstream cortical 

- 14 regions. In this study, we performed high-density probe recordings across the full depth of the 

- 15 medial prefrontal cortex and in the hippocampus simultaneously in rats while they were performing 

- 16 a task of spatial navigation. We find that neurons in the medial prefrontal cortex encode spatial 

- 17 information and reliably predict upcoming choice on a maze, and we find that a subset of neurons in 

- 18 the mPFC is modulated by hippocampal sharp-wave ripples. However, sharp-wave ripple modulation 

- 19 does not appear to be the main driving factor in predicting upcoming choice. This indicates that the 

- 20 integration of spatial information requires the collaboration of different specialized populations of 21 neurons. 

- 22 KEYWORDS: hippocampus, prefrontal cortex, spatial learning, replay 

- 23 

- 24 Number of figures: 6 

Abstract: 158 words 

25 Number of tables: 0 Introduction: 777 words 26 Number of supplementary figures: 4 Results: 3658 words 27 Number of supplementary tables: 1 Discussion: 1291 words 28 Methods: 3891 words 

- 29 

30 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 31 INTRODUCTION 

- 32 The hippocampus is known to be important for spatial navigation. This is largely attributed to the 

- 33 spatially specific firing patterns of place cells, which fire sequentially as animals navigate through an 

- 34 environment in the timeframe of theta frequency (~8Hz) oscillations. These sequential firing 

- 35 patterns are often repeated or ‘’replayed’’ during short high frequency oscillations called sharp-wave 

- 36 ripples (SWRs) while the animal is in a state of behavioral immobility or sleep. The function of these 37 replay patterns is still somewhat under debate, but during awake immobility periods they have been 38 proposed to either predict immediate future behavior[1–5] , or reflect specific past experience[6] , and 39 adapt to reward[7,8] and task demand[9] , while during sleep, they are thought to be important for 40 memory consolidation[10] . 

- 41 A running hypothesis is that the hippocampus transfers information to neocortical areas during 42 these SWR events and this is thought to be a crucial mechanism to facilitate spatial learning[11] 43 Congruently, it has been shown that a subset of neurons in the medial prefrontal cortex shows 44 modulated firing patterns following SWRs in the hippocampus, where some neurons show an 45 increase and others a decrease of firing rate, both in a 200 millisecond window following SWR 46 onset[12,13] . Disrupting this window of activity in the mPFC slowed the acquisition of a spatial rule 47 reversal[14] . 

- 48 The mPFC can be divided into three regions: the anterior cingulate cortex (ACC), the prelimbic cortex 

- 49 (PLC) and the infralimbic cortex (ILC), which have been shown to have distinct functions in the 

- 50 context of fear-related memory[15–17] , cognitive flexibility[18] and preparatory attention and error- 

- 51 related events[19–23] .  However, due to practical limitations related to the anatomical layout of the 

- 52 region, it has been challenging to study electrophysiological differences between all three 

- 53 subregions simultaneously with sufficient single cell data to draw meaningful conclusions about 

- 54 functional specializations. Some authors argue that the mPFC subregions are not distinguishable as 

- 55 three separate subunits, but rather function as a continuum[24] .  Especially the function of the PLC is 56 under debate, and a recent study suggested to divide the PLC further into a dorsal and ventral 

- 57 section, where the dorsal PLC was found to be more related to ACC firing patterns, and the ventral 58 PLC more closely resembled the ILC[25] . 

- 59 The response to SWRs in the medial prefrontal cortex has been found to be specific to the place cell 

- 60 activity in the hippocampus during the SWR, where non-local replay events in the hippocampus are 

- 61 followed by a higher firing rate modulation in the medial prefrontal cortex, and this preference is 

- 62 predictive of future behavior[13] . The modulation to SWRs also seems to be stronger when the SWRs 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 63 occur during behavioral immobility or rest, compared to sleep SWRs[26] , potentially indicating a 64 different mechanism underlying the two states. 

- 65 Cells in the mPFC that are modulated by SWRs, are more likely to be phase-locked to the 

- 66 hippocampal theta rhythm seen mostly while the animal is actively exploring an environment[12,13] 

- 67 Ripple and theta oscillations are independent brain states, occurring primarily during rest and active 68 exploration, respectively. Therefore it is interesting that mPFC neurons are modulated by both 69 states, which suggests a network of prefrontal-hippocampal activity that is co-modulated during 70 both rest and active exploration[13] . 

- 71 Although the spatial specificity is lower in mPFC neurons compared to the hippocampus, some 

- 72 papers have reported replay trajectory events to occur in the mPFC as well[27–31] . The coordination 73 with replay events in the hippocampus remains unclear, where one study reports coordinated replay 74 trajectory events between the hippocampus and mPFC[31] , while another study found that mPFC 

- 75 replay occurs independently of hippocampal replay[28] . During sleep it has been found that 76 reactivation of previous experiences in the mPFC does occur time locked to SWRs in the 77 hippocampus, but only when a spatial rule on the maze had been learned[30] , indicating that this 78 interaction may be selective depending on the context in which it occurs. It has also been found that 79 the mPFC engages in replay events particularly after error trials[29] , which may reflect a mechanism of 80 negative feedback during learning. Finally, cells in the mPFC that are modulated by SWRs in the 81 hippocampus have been shown to be less tuned to space[12] , and therefore perhaps this modulation 82 of cellular activity is not necessarily (only) a reflection of spatial replay trajectories, but may reflect 83 another non-spatial mechanism instead. 

- 84 In this study, we performed high-density probe recordings across the full depth of the mPFC and in 

- 85 the hippocampus simultaneously while animals are performing a behavioral task of spatial 

- 86 navigation, to shed light on firing properties of SWR-modulated and unmodulated cells in the mPFC. 

- 87 We find that mPFC cells that are not modulated by hippocampal SWRs seem to be active at key time 

- 88 points in spatial decision making. 

- 89 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 90 Results 

- 91 Chronic Neuropixels probe recordings across mPFC subregions 

- 92 Adult Long Evans rats were implanted with either two Neuropixels 1.0 probes (mPFC and 93 hippocampus; N=5 animals) or a single probe (mPFC; N=1 animal; see Methods and Fig. 1a-b and 

- 94 Supplementary Table 1). Signals from the mPFC were classified as originating from the dorsal or 95 ventral subregion based on the implantation depth of the electrodes and the histological verification 96 of the probe track (see Methods and Supplementary Fig. S1). Both subregions showed ample spiking 97 activity (for example see Fig. 1b). In five animals, data from both dorsal and ventral mPFC was 98 obtained and in one animal only data for the dorsal mPFC was included (due to the probe 99 implantation being too posterior; see Supplementary Fig. S1). Spikes were assigned to a cluster 

- 100 (putative neuron) using automated spike sorting followed by manual curation (see Methods), and up 101 to 203 neurons were isolated from a single subregion per session (see Fig. 1d and Supplementary 102 Table 1). For all analyses presented here, data was averaged per session, so that sessions with a high 103 number of neurons did not skew the results. Due to the light-weight and compact design of the 104 implant[32] , animals were able to move freely on an elevated track. While we recorded neural activity, 105 the animals performed a spatial rule switching task in which they learned 4 different rules over the 106 course of multiple days (see Methods and Fig. 1c). Rules were based on either allocentric (“go 107 North” or “go South”) or cue-based (“go to illuminated arm” or “go to dark arm”) strategies, which 108 were to be deducted by the animals through trial and error. Each session started with a period of 20 109 minutes rest in a dark resting box. After this, the animal was placed by the experimenter pseudo110 randomly on either the East or the West arm of the maze and it had to learn to go (1) to the North 111 arm, (2) to the South arm, (3) to the illuminated arm (either South or North) or (4) to the non112 illuminated (South or North) arm. The order of the rules was counterbalanced between animals. The 

- 113 illumination of the arm was always present (also during allocentric learning) and was pseudo- 

- 114 randomly determined for each trial. After the animal made its choice, it was picked up by the 

- 115 experimenter, and placed back in the dark resting box for 30-60 seconds before continuing with the 

- 116 next trial. The animals were trained for a maximum of 1.5 hours or 60 trials per day. At the end of 117 the session, animals were placed back in the dark resting box for up to 60 minutes. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**==> picture [408 x 189] intentionally omitted <==**

**==> picture [373 x 25] intentionally omitted <==**

- 118 

**==> picture [403 x 194] intentionally omitted <==**

- 119 Figure 1 Chronic Neuropixels probe recordings across mPFC subregions. (a) Left: an image of the Neuropixels 120 probe, right: the probe mapping from one example animal where a part of the trace is seen going through the 121 hippocampus (top) and mPFC (bottom). (b) An example segment of data with the animals running speed (top) 122 and spiking activity recorded from the hippocampus, dorsal mPFC and ventral mPFC (top to bottom). (c) An 123 overview of the behavioral task. Each day starts with a period of rest, followed by rule learning in the maze. 

- 124 Each trial is interleaved with a short period (~45 seconds) of rest, and the day ends with a period of rest or sleep 125 of up to 60 minutes. Four different rules have to be learned over the course of multiple days, based on 

- 126 allocentric and cue-based strategies. (d) The number of sorted neurons per session for each (sub-)region. The 127 different markers indicate different animals. 

- 128 

- 129 Neurons in the dorsal and ventral mPFC are differentially modulated by hippocampal SWRs and theta 130 phase 

- 131 The mPFC is known to contain functionally distinct cell populations that differ in the modulation of 

- 132 their activity by hippocampal SWRs and theta oscillations[12] . Both SWR-excited and SWR-inhibited 

- 133 cell populations (but not SWR unmodulated cells) have been shown in the past to be phase-locked to 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 134 hippocampal theta oscillations and they are more likely to co-fire with cell members of their own 135 group[12] . Here we test if these cell populations are equally present across the dorsal-ventral extent of 136 the mPFC. 

- 137 We first confirmed the presence of SWR and theta-modulated subpopulations of mPFC neurons 138 while animals were on the maze. Following hippocampal SWR onset, 13.96% of all mPFC neurons 139 significantly increased their firing rate (SWR-excited) and 5.46% of neurons decreased their firing 140 rate (SWR-inhibited). The majority of neurons were not modulated by hippocampal SWRs (80.59%; 141 SWR-unmodulated, see Fig. 2a-d). These neurons had a lower overall firing rate than SWR 142 modulated neurons (mean firing rates in Hertz, SWR-excited: M=6.25, SEM=0.49, SWR-inhibited: 143 M=9.31, SEM=1.00, SWR-unmodulated: M=3.87, SEM=0.33, ANOVA: F(142)=19.57, p<.001, see Fig. 144 2e). Cells that changed their firing rate following hippocampal SWRs also were more likely to be 145 phase-locked to the hippocampal theta oscillation. Overall, 38.46% of cells in the mPFC and 79.42% 146 of cells in the hippocampus showed significant theta phase locking, similarly to previously reported 147 percentages[33] . Theta phase-locking was more prevalent among the population of SWR-modulated 148 mPFC cells (M=55.40%, SEM=4.50) than the population of SWR-unmodulated cells (M=33.53%, 149 SEM=1.94, Mann-Whitney U test: U(104)=1993, p<.001; see Fig. 2f-g). These data are consistent with 150 the idea that SWR- and theta-modulated cells form a functional subpopulation in the mPFC. 

- 151 Next, we tested if and how the SWR- and theta-modulated cell populations vary in the dorsal and 152 ventral subregions of the mPFC. We observed similar percentages of SWR-excited and SWR-inhibited 153 neurons in both subregions. However, the activity of SWR-excited and SWR-inhibited neurons in 154 ventral mPFC was more strongly modulated by SWRs than the activity of neurons in the dorsal mPFC 155 (mean modulation absolute z-score, dorsal: M=0.09, SEM=0.01, ventral: M=0.20, SEM=0.05; 156 independent samples t-test: t(86)=-2.11, p=.038; see Fig. 2b and Fig. 2c). The theta-modulated cells 157 were also similarly distributed in the dorsal and ventral mPFC (percent of theta modulated neurons, 158 dorsal: M=36.67%, SEM=3.07, ventral: M=42.88%, SEM=3.18; Mann-Whitney U test: U(104)=1139, 159 p=.117, see Fig. 2f). In both brain regions, there was a higher proportion of theta modulated cells 160 among the SWR-modulated compared to the SWR-unmodulated cells (percent of theta modulated 161 neurons, dorsal, SWR-modulated: M=55.53, SEM=4.85, SWR-unmodulated: M=31.93, SEM=2.51; 162 Mann-Whitney U test: U(98)=1794, p<.001. Ventral, SWR-modulated: M=59.14, SEM=5.63, SWR- 

- 163 unmodulated: M=37.46, SEM=2.96; Mann-Whitney U test: U(88)=1354, p=.005, see Fig. 2g). The 

- 164 preference for the hippocampal theta phase, however, was different between the dorsal and ventral 

- 165 subregions. Phase-locked neurons in the dorsal mPFC had a bias for firing just before the peak of the 

- 166 oscillation, while phase-locked neurons in the ventral mPFC were more likely to fire around the 

- 167 trough of the oscillation (theta phase locking dorsal mPFC versus ventral mPFC, Kolmogorov-Smirnov 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 168 difference in distributions, SWR-modulated neurons: K=0.8, p<.001; SWR-unmodulated neurons: 169 K=0.5, p=.012; see Fig. 2h). 

**==> picture [425 x 193] intentionally omitted <==**

170 

**==> picture [425 x 192] intentionally omitted <==**

171 Figure 2. Neurons in the dorsal and ventral mPFC are differentially modulated by hippocampal SWRs and 

172 theta phase. (a) Six example neurons in the mPFC that are SWR-excited (top), SWR-inhibited (middle) and SWR173 unmodulated (bottom; dorsal mPFC in olive, ventral mPFC in blue). (b) The average normalized firing rates 174 around SWR onset of all SWR-excited and SWR-inhibited neurons in the dorsal and ventral mPFC. Data is 175 presented as mean of all neurons ± SEM. (c) The mean of the SWR modulation per subregion during periods of 176 exploration in the maze. The p-value indicates the result of an independent samples t-test between the 177 absolute modulation scores in the dorsal versus ventral mPFC. (d) The percentage of neurons that is SWR178 excited (solid fill) and SWR-inhibited (dashed fill) per mPFC subregion. The p-value indicates the result of an 179 independent samples t-test between the dorsal and ventral mPFC.  (e) The mean overall firing rates per 180 subregion of SWR-excited (solid fill), SWR-inhibited (dashed fill) and SWR-unmodulated (no fill) neurons in the 181 maze. The p-values indicate an ANOVA between the different SWR modulation categories. (f) The percentage 182 of neurons that is phase-locked to hippocampal theta per brain region. The p-values indicate the results of 183 Mann-Whitney U test between the hippocampus and mPFC, and between the dorsal and ventral mPFC. (g) The 184 percentage of neurons that is phase-locked to hippocampal theta, divided between mPFC neurons that are 185 SWR-excited (solid fill), SWR-inhibited (dashed fill) and SWR-unmodulated (no fill). The p-values indicate an 186 ANOVA between the different SWR modulation categories.  (h) Left panels: the mean angle (-π to π) and  (0.0 187 to 0.6) for all dorsal mPFC clusters that were significantly phase locked to hippocampal theta, divided between 188 SWR-excited clusters (top), SWR-inhibited clusters (middle) and SWR-unmodulated clusters (bottom). Middle 189 panels: the mean angle and  for all phase locked clusters in the same configuration as the left panels, but for 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 190 the ventral mPFC. Right panels: histograms of the mean angles of all theta phase-locked clusters that were 191 SWR-excited, SWR-inhibited or SWR-unmodulated (top to bottom). The p-values indicate the result of a 192 Kolmogorov-Smirnov test to test the difference in distribution between the dorsal (olive) and ventral (blue) 193 mPFC. 

194 SWR-unmodulated neurons are spatially tuned, directionally selective and show theta cycle skipping 195 Previous research has demonstrated that neurons in the mPFC encode spatial information[27–29,34] , and 196 suggested that SWR-unmodulated neurons show lower spatial coverage (i.e. higher spatial tuning) 197 than SWR-excited and SWR-inhibited neurons[12] . Another paper found that the dorsal mPFC has 198 higher spatial tuning properties than the ventral mPFC[35] , from which the authors concluded that 199 spatial tuning in the mPFC is only partly dependent on direct input from the hippocampus. Here we 200 tested whether the difference in spatial tuning between SWR-modulated and SWR-unmodulated 201 neurons holds up when comparing the dorsal and ventral mPFC. We calculated the spatial specificity 202 score for each cluster (see Methods) and found a higher spatial tuning score in the hippocampus 203 (spatial information in bits/spike, M=0.64, SEM=0.06) than in the mPFC neurons (M=0.31, SEM=0.01, 204 Mann-Whitney U test: U(106)=2129, p<.001; Fig. 3a-b), as expected from previous literature[12,28] . In 205 contrast to the mentioned study[35] , we did not observe differences between spatial tuning properties 206 of neurons in the dorsal and ventral mPFC (spatial information in bits/spike, dorsal: M=0.32, 207 SEM=0.01, ventral: M=0.34, SEM=0.02; Mann-Whitney U test: U(121)=1969, p=.639). We did, 208 however, find that SWR-unmodulated mPFC neurons showed a higher spatial tuning score (M=0.33, 209 SEM=0.02) compared to SWR-excited (M=0.22, SEM=0.01) and SWR-inhibited neurons (M=0.11, 210 SEM=0.01; Kruskal-Wallis: H(142)=70.52, p<.001; Fig. 3b). This effect is robust and was seen for both 211 the dorsal and ventral subregions. 

212 Cells that fire selectively during particular head directions have been found in a variety of 213 brain regions as well[36–38] . We next investigated whether neurons in the mPFC are linked to certain 214 head directions and whether there is also a differential involvement of SWR-modulated and 215 unmodulated neurons in head direction selective firing patterns. We categorized the animals’ head 216 directions at the start of the maze in three categories (towards future choice or alternative choice, 217 towards North or South, and towards left or right, see Methods and Fig. 3c). First, we determined for 218 each neuron whether it spiked significantly more for one direction compared to its opposite counter 219 part (e.g. future choice versus alternative choice). In the hippocampus 31.35% of clusters (SEM=4.20) 220 showed significant directional selectivity, compared to 24.78% of clusters in the mPFC (SEM=1.52, 221 Mann-Whitney U test: U(103)=1505, p=.176; chance level is 15%; see Fig. 3d). Next, for each neuron 

222 a directional selectivity index was calculated, where the difference between the firing rates within 

- 223 one category were subtracted from the summed firing rate of that category (e.g. the difference 224 between firing rates during head directions towards the future choice and alternative choice, divided 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

225 by the sum of both direction; see Methods). This index thus indicates the preference of each neuron 226 to fire selectively during one type of head direction. For all three head direction categories (future 227 versus alternative, North versus South, and left versus right), the SWR-unmodulated neurons 228 showed significantly higher directional selectivity scores than the SWR-excited and SWR-inhibited 229 neurons (maximum absolute directional selectivity index, SWR-excited: M=0.37, SEM=0.02, SWR230 inhibited: M=0.27, SEM=0.02, SWR-unmodulated: M=0.48, SEM=0.02; Kruskal-Wallis: H(138)=41.26, 231 p<.001, see Fig. 3f). On a population level, there was no preference for any one of the categories 232 over another (see Supplementary Fig. S3b). 

233 Furthermore, both the mPFC and hippocampus are known to encode information about 234 upcoming trajectories in alternating cycles of theta oscillations[39–41] . A subset of cells in the 235 hippocampus and mPFC are found to skip every other cycle within the theta rhythm, and neurons in 236 the mPFC are thereby thought to favor the true upcoming trajectory over alternative choices[39] . Here 237 we were interested to see whether we observe differences in theta cycle skipping properties in SWR238 modulated and unmodulated neurons in the dorsal and ventral mPFC. For each neuron we 239 determined whether or not it showed cycle skipping properties by looking at the probability of 240 spiking at 125 ms (one theta cycle) and 250 ms (two theta cycles) in the spike time autocorrelation 241 (see Methods and Fig. 3e). A subset of neurons in the hippocampus (M=42.03%, SEM=4.70) and in 242 the mPFC (M=25.69%, SEM=1.87) showed theta cycle skipping properties. The percentage of 243 neurons showing theta cycle skipping properties was significantly higher for SWR-unmodulated 244 neurons, compared to SWR-excited and SWR-inhibited neurons (percentage of neurons showing 245 theta cycle skipping properties, SWR-excited: M=22.72, SEM=2.01, SWR-inhibited: M=12.39, 246 SEM=3.04, SWR-unmodulated: M=28.94, SEM=1.99; Kruskal-Wallis: H(140)=31.25, p<.001, see Fig. 3f 247 and Supplementary Fig. S3c). 

248 Together these results indicate that the population of SWR-unmodulated neurons seem to 249 have distinct functions in terms of spatial mapping, head direction selectivity, and cycle skipping 250 properties, with a stronger involvement compared to neurons that are either excited or inhibited by 251 hippocampal SWRs. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**==> picture [427 x 411] intentionally omitted <==**

252 253 254 Figure 3. SWR-unmodulated neurons are spatially tuned, directionally selective and show theta cycle 255 skipping. (a) The firing patterns of eight example neurons in the maze, showing a range of spatial tuning scores 256 (in bits/spike) sorted from highest to lowest. (b) Left panel: the spatial tuning score per subregion (p-values 257 indicate a Mann-Whitney U test). Right panel: the spatial tuning score per subregion divided between mPFC 258 neurons that are SWR-excited (solid fill), SWR-inhibited (dashed fill) and SWR-unmodulated (no fill; p-values 259 indicate a Kruskal-Wallis test). (c) Three example trials where quadrants on the maze are categorized as 260 upcoming or alternative choice, North or South, and left or right. (d) Left panel: the percentage of neurons that 261 fire significantly higher than the shuffled population for at least one of the head direction categories. The 262 chance level is indicated at 15%, as an alpha of 0.05 was maintained for each of the three direction categories 263 (future versus alternative, North versus South, and left versus right; p-values indicate the results of a Mann264 Whitney U test). Right panel: the absolute maximum directional selectivity index per subregion for mPFC 265 neurons that are SWR-excited (solid fill), SWR-inhibited (dashed fill) and SWR-unmodulated (no fill; p-values 266 indicate a Kruskal-Wallis test). (e) Spike time auto-correlations of two example neurons where the peak of the 267 smoothed signal (in black) at 250 ms is subtracted from the peak at 125 ms and normalized to the highest of 268 the two peaks to obtain the cycle skipping index (left panels). To determine the statistical significance, the score 269 is compared to a shuffled population (right panels).  (f) Left panel: the percentage of neurons that showed 270 significant theta cycle skipping properties per subregion (p-values indicate a Mann-Whitney U test). Right 271 panel: the theta cycle skipping index per subregion divided between mPFC neurons that are SWR-excited (solid 272 fill), SWR-inhibited (dashed fill) and SWR-unmodulated (no fill; p-values indicate a Kruskal-Wallis test). 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

273 274 Non-local representations in the mPFC are predictive of the animals’ choice 

275 Previous research has shown that the ensemble firing patterns in the mPFC can be used to decode 276 spatial locations[29] . Furthermore, decoded position data from the mPFC has been found to contain 277 excursions to non-local positions in the maze, which are thought to be related to the neurons’ 278 encoding of choice evaluation[29] . We were interested to see whether non-local representations in the 279 mPFC could be linked to the future arm choice of the animals as well, and whether there is a link 280 with hippocampal SWRs and SWR-modulated firing patterns. We decoded spatial information from 281 spiking activity along the depth of the mPFC, using a Bayesian decoding model to associate spike 282 features with the location in the maze at which the spikes occurred (see Methods). Using these 283 decoding models, we were able to decode the current location of the animal based on spiking 284 activity in the mPFC accurately (median cross-validated decoding error less than 20 cm) for a total of 285 40 sessions from 5 different animals. We decoded the spatial information at a theta time scale (50 286 ms bins with 80% overlap), and observed, aside from the local representations of the current arm, 287 segments of representations of the other arms of the maze, that were either predictive of the 288 upcoming choice, or of the alternative choice on the other side of the maze (see methods and Fig. 289 4a). Segments of non-local representations were defined as any number of consecutive time bins 290 where the summed decoded probability of one of the two goal arms was higher than 0.5 while the 291 animal was at the start or center of the maze (see Methods). Using the difference between the sum 292 of decoded probabilities of the segments of the upcoming choice and the segments of the 293 alternative choice, we obtained a prediction index between 1 and -1 corresponding to the direction 294 the animal did and did not turn, respectively. These scores could accurately predict the turning 295 direction of the animals, while the rule was still being learned as well as when it was already well 296 known (see Fig. 4b). 

- 297 Next, we asked if the predicted directions based on decoded non-local representations 298 either preceded or followed the change in behavior. For this, we overlayed the learning curves of the 299 animals with curves made from the predicted directions based on the non-local representations in 300 the mPFC and performed cross-correlations between the two curves (see Methods and Fig. 4c). It 301 was seen that the highest correlation between the two curves was found on average at a lag of -8 302 trials for the allocentric rules (M=-8.0, SEM=3.78, deviation from zero Wilcoxon one sample test: 303 W(5)=0, p=.043) and -6 trials for the cue-based rules (M=-5.52, SEM=2.29, Wilcoxon one sample test: 

- 304 W(30)=96, p=.015), indicating that the decoded directions precede the real directions over the 305 course of learning (see Fig. 4c). 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

306 

307 Furthermore, we looked at the distribution of decoded probabilities while the animal was at 308 the choice point, but had not yet entered any of the goal arms. The distribution of decoded 309 probabilities showed an overall increase of decoded bins of the upcoming choice compared to the 310 alternative choice on the maze (interaction maze bin and prediction category, repeated measures 311 ANOVA: F(9,351)=115.14, p<.001; Fig. 4d), with most notable increases in occurrence of decoded 312 timepoints of the start (post-hoc Bonferroni corrected p-value: p<.001) and end (post-hoc Bonferroni 313 corrected p-value: p<.001) of the arm representing the upcoming choice. To look at the relative 314 contribution of SWR-modulated and unmodulated mPFC neurons, we next built separate decoding 315 models for each subpopulation (see Methods).  The differences in decoded distributions between 316 the upcoming and alternative choice were also seen when using the SWR-unmodulated mPFC 317 neurons to build the decoding models (interaction maze bin and prediction category, repeated 318 measures ANOVA: F(9,288)=30.1, p<.001; post-hoc Bonferroni corrected p-values, start of the goal 319 arms: p<.001; end of the goal arms: p<.001), but not when using the SWR-modulated neurons for 320 the decoding (interaction maze bin and prediction category, repeated measures ANOVA: 321 F(9,279)=15.53, p=.135; Fig. 4d). This lack of differentiating the upcoming and alternative choices at 322 the center of the maze was true for both the SWR-inhibited and SWR-excited cell populations (SWR323 inhibited, interaction maze bin and prediction category, repeated measures ANOVA: F(9,270)=27.36, 324 p=.193; SWR-excited, repeated measures ANOVA: F(9,270)=17.50, p=.154). This indicates a larger 325 involvement of the SWR-unmodulated neurons in encoding the upcoming choice at the center of the 326 maze. 

327 In order to compare these findings with hippocampal spatial mapping, we decoded spatial 328 activity in the hippocampus and obtained representations of upcoming and alternative choices in the 329 same way as in the mPFC (see methods and Supplementary Fig. S4). Due to more limited multi-unit 330 activity recorded from the hippocampus, we were only able to reliably decode hippocampal activity 331 from N=12 sessions from 3 different animals, but the turning direction could still be predicted 332 reliably based on the non-local representations in this region when the animals were in the process 333 of learning a spatial rule (Supplementary Fig. S4b). To look at the overlap of the decoded 334 representations between the hippocampus and the mPFC, we computed the percentage of 

- 335 overlapping classifications for each session and compared this to shuffled data (i.e., the 

- 336 representations in the mPFC per category of local, upcoming and alternative choices, compared to 

- 337 N=500 times the shuffled decoded data from the hippocampus, see Methods). While the overlap 

- 338 between the hippocampus and mPFC in local representations was significantly higher than the 339 shuffled data (overlap local representations: M=10.10% of decoded time bins, SEM=1.30, shuffled 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

340 population: M=9.08, SEM=1.13, paired samples t-test: t(10)=3.31, p=.008), no such overlap was seen 341 for the representations of upcoming and alternative choices (overlap alternative choice: M=0.11%, 342 SEM=0.04, shuffled population: M=0.11, SEM=0.04, paired samples t-test: t(10)=0.03, p=.973; 343 overlap upcoming choice: M=0.48%, SEM=0.24, shuffled population: M=0.22, SEM=0.09, paired 344 samples t-test: t(10)=1.54, p=.154; Fig. 4e).   For the decoded data based on either the SWR345 modulated or SWR-unmodulated neurons in the mPFC, no significant overlap in time was seen with 346 the decoded data from the hippocampus. (Overlap local representations, SWR-modulated [shuffled]: 347 M=7.51%, SEM=1.22 [M=6.99%, SEM=1.00], paired samples t-test: t(10)=1.28, p=.228; SWR348 unmodulated [shuffled]: M=7.15%, SEM=1.04 [M=6.48%, SEM=0.82], paired samples t-test: 349 t(10)=2.02, p=.071. Overlap alternative choice: SWR-modulated [shuffled]: M=0.92%, SEM=0.60 350 [M=0.29%, SEM=0.10], paired samples t-test: t(10)=1.18, p=.266; SWR-unmodulated [shuffled]: 351 M=0.86%, SEM=0.61 [M=0.26%, SEM=0.10], paired samples t-test: t(10)=1.09, p=.302. Overlap 352 upcoming choice: SWR-modulated [shuffled]: M=0.66%, SEM=0.19, [M=0.51%, SEM=0.11], paired 353 samples t-test: t(10)=1.03, p=.325; SWR-unmodulated [shuffled]: M=0.80%, SEM=0.25 [M=0.51%, 354 SEM=0.13], paired samples t-test: t(10)=1.55, p=.151. See Fig. 4e). Again, this was the case for both 355 the SWR-excited and SWR-inhibited cell populations (Overlap upcoming choice, SWR-excited 356 [shuffled]: M=0.25%, SEM=0.07 [M=0.18%, SEM=0.04], paired samples t-test: t(10)=1.59, p=.143; 357 SWR-inhibited [shuffled]: M=0.86%, SEM=0.63 [M=0.27%, SEM=0.12], paired samples t-test: 358 t(10)=1.08, p=.305. Overlap alternative choice, SWR-excited [shuffled]: M=0.61%, SEM=0.17 359 [M=0.46%, SEM=0.09], paired samples t-test: t(10)=1.12, p=.290; SWR-inhibited [shuffled]: M=0.33%, 360 SEM=0.11 [M=0.29%, SEM=0.09], paired samples t-test: t(10)=0.43, p=.674). Thus, the encoding for 361 alternative and upcoming choices on the maze is largely separated in time between the mPFC and 362 hippocampus. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**==> picture [417 x 228] intentionally omitted <==**

- 363 

**==> picture [417 x 227] intentionally omitted <==**

364 Figure 4. Non-local representations in the mPFC are predictive of the animals’ upcoming choice. (a) Three 365 examples of trials where the decoded positions (grey scale) and real positions (red) are shown per maze 366 segment. Segments of upcoming and alternative choice are highlighted with light and dark brown spans. (b) 367 The prediction index per session based on the decoded non-local representations while the animal was at the 368 start and center of the maze, separated for when the rule was not yet learned and when the rule was learned, 369 and for the allocentric (navy) and cue-based (orange) rules. Shown in light grey is the prediction accuracy based 370 on the shuffled decoded posteriors, and p-values indicate the result of a paired samples t-test between the real 371 and shuffled predictions. (c) Left panel: an example learning curve (in black) with a rule switch from South to 372 North after 10 trials, and the predicted directions based on the non-local representations overlayed (navy). 373 Right panel: the lag (in number of trials) between the real direction and decoded direction per session for 374 allocentric (navy) and cue-based (orange) strategies. A negative lag indicates that the decoded direction 375 preceded the real direction over the course of learning. P-values indicate the result of a one-sample Wilcoxon 376 test to test the deviation from zero. (d) The distribution of decoded probabilities at the center of the maze for 377 all mPFC neurons (top panel), SWR-modulated neurons (middle panel) and SWR-unmodulated neurons (bottom 378 panel). P-values indicate the results of a two-way repeated measures ANOVA between the maze bins and 379 prediction categories (alternative versus upcoming choice). (e) The overlap between representations in the 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

380 hippocampus and mPFC (all neurons, SWR-modulated neurons and SWR-unmodulated neurons) for the local 381 representations (left panel), the representations of alternative choice (middle panel), and the upcoming choice 382 (right panel). P-values indicate the results of a paired samples t-test of  the percentage of overlapping decoded 383 time bins for each session compared to the overlap of the shuffled data for that session. 384 

385 Predictive representations in the mPFC are not linked to hippocampal SWRs and theta phase 

386 Finally, we were interested to see whether the non-local representations of the upcoming choice in 387 the mPFC are linked to hippocampal SWRs and theta phase. We obtained a histogram of SWR 388 occurrence in temporal proximity to the start of each segment of non-local representations in the 389 mPFC, and compared this to a shuffle distribution of decoded probabilities (see Methods). Only 390 segments of non-local representations were included that occurred within 2 seconds of a 391 hippocampal SWR. The occurrence of decoded segments at SWR onset were not significantly 392 different from shuffled distributions for both upcoming and alternative choices (occurrence of 393 segments of alternative choice at 0-20 ms from SWR onset, real: M=0.06, SEM=0.01, shuffled: 394 M=0.07, SEM=0.01, Wilcoxon signed-rank test: W(33)=190, p=.382; occurrence of segments of 395 upcoming choice at 0-20 ms from SWR onset, real: M=0.06, SEM=0.01, shuffled: M=0.07, SEM=0.01, 396 Wilcoxon signed-rank test: W(33)=174, p=.147; Fig. 5a). It was further seen that the SWR397 unmodulated mPFC neurons had higher normalized firing rates than SWR-modulated neurons during 398 representations of upcoming choice (z-scored firing rates of SWR-excited neurons: M=0.24, 399 SEM=0.07, SWR-inhibited neurons: M=0.06, SEM=0.07, SWR-unmodulated neurons: M=0.43, 400 SEM=0.10, Kruskal-Wallis: H(94)=7.55, p=.023; Fig. 5b). During representations of the alternative 401 choice, the difference was not significant (z-scored firing rates of SWR-excited neurons: M=0.18, 402 SEM=0.13, SWR-inhibited neurons: M=0.14, SEM=0.08, SWR-unmodulated neurons: M=0.37, 403 SEM=0.11, Kruskal-Wallis: H(94)=5.0, p=.082; Fig. 5b). 

- 404 Similarly, we obtained a histogram of hippocampal theta phase at which each segment of 405 non-local decoding occurred. Only segments of non-local representations that occurred within ‘theta 406 periods’ were included (which were selected based on a running speed of >5cm/s and the absence of 407 SWRs in the hippocampus; see Methods). The distribution of hippocampal theta phase at the onset 408 of representations of upcoming and alternative choices was very homogeneous with no clear bias 409 towards a particular phase of the theta cycle (Kolmogorov-Smirnov difference in distributions, 410 alternative versus shuffled: K=0.25, p=.292; upcoming versus shuffled: K=0.15, p=.644; see Fig. 5c 411 As such, the average phase-locking scores of upcoming and alternative segments were not 412 statistically significant compared to a randomized population (representations of alternative choice, 413 Rayleigh’s Z=0.03, randomized population M=0.01, CI=[0.00, 0.04], p=.060; representations of 414 upcoming choice, Rayleigh’s Z=0.01, randomized population M=0.01, CI=[0.00, 0.03], p=.116; Fig. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

415 5d). These results thus indicate that the non-local representations in the mPFC are not directly linked 

416 in time to hippocampal SWRs and theta phase. 

417 

**==> picture [425 x 168] intentionally omitted <==**

**==> picture [425 x 167] intentionally omitted <==**

418 Figure 5. Non-local representations in the mPFC are not linked to hippocampal SWRs and theta phase. (a) 419 The occurrence of representations of alternative choice (left) and upcoming choice (right) in the mPFC in 420 temporal proximity to the closest SWR. The p-values indicate the results of a Wilcoxon signed-rank test 421 between real and shuffled data at bin 0-20 ms from SWR onset. (b) The firing rates of mPFC neurons that are 422 SWR-excited, SWR-inhibited and SWR-unmodulated, during representations of upcoming and alternative 423 choices, normalized to the average firing rate at the start of the maze. The p-values indicate the results of a 424 Kruskal-Wallis test between the different SWR modulation categories.  (c) A histogram of the phase of 

- 425 hippocampal theta oscillations at which the start of each representation of upcoming and alternative choices in 426 the mPFC occurred. The p-values indicate the results of a Kolmogorov-Smirnov test for difference in 427 distributions between the representations of alternative and upcoming choices compared to shuffled decoded 428 probabilities. (d) Left: circular histograms of the phase locking shown in (c). Right: The phase locking score of 429 representations of upcoming and alternative choices (Rayleigh’s Z, dark and light brown dots) to hippocampal 430 theta oscillations compared to a randomized population (gray histograms). P-values indicate the result of a 431 left-tailed Monte Carlo test of the Rayleigh’s Z compared to the shuffled population. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

432 Predictive representations in the hippocampus are linked to SWRs and theta phase 

433 In order to compare these findings with non-local representations in the hippocampus,  we obtained 434 a histogram of SWR occurrence in temporal proximity to the start of each non-local representation 435 in the hippocampus. We found that hippocampal representations of upcoming choice, but not the 436 alternative choice were more time-locked to SWRs than the shuffled probabilities (occurrence of 437 segments of alternative choice at 0-20 ms from SWR onset, real: M=0.12, SEM=0.02, shuffled: 438 M=0.12, SEM=0.01, Wilcoxon signed-rank test: W(14)=59, p=.978; occurrence of segments of 439 upcoming choice at 0-20 ms from SWR onset, real: M=0.18, SEM=0.03, shuffled: M=0.12, SEM=0.01, 440 Wilcoxon signed-rank test: W(14)=12, p=.004; Fig. 6a). Furthermore, interestingly, SWR-excited 441 neurons in the mPFC fired significantly more during hippocampal representations of upcoming 442 choice compared to representations of alternative choice (z-scored firing rates during 443 representations of alternative choice: M=-0.15, SEM=0.05, during representations of upcoming 444 choice: M=0.06, SEM=0.06, Mann-Whitney U test: U(28)=57, p=.023; Fig. 6b). For SWR-inhibited 445 neurons, the opposite effect was seen, where firing rates were higher during hippocampal 446 representations of alternative choice, and decreased during representations of upcoming choice (z447 scored firing rates during representations of alternative choice: M=0.15, SEM=0.10, during 448 representations of upcoming choice: M=-0.13, SEM=0.08, Mann-Whitney U test: U(28)=162, p=.042; 449 Fig. 6b). For SWR-unmodulated neurons, no difference was seen in firing rate modulation linked to 450 representations of upcoming and alternative choices in the hippocampus (z-scored firing rates 451 during representations of alternative choice: M=0.04, SEM=0.04, during representations of 452 upcoming choice: M=0.04, SEM=0.03, Mann-Whitney U test: U(28)=100, p=.619; Fig. 6b). This 453 indicates that mPFC neurons that are modulated by hippocampal SWRs, respond selectively to 454 hippocampal representations of upcoming and alternative choices. 

455 Hippocampal representations of alternative and upcoming choice were differently 456 distributed with respect to the hippocampal theta cycle (Kolmogorov-Smirnov difference in 457 distributions, alternative versus shuffled: K=0.35, p=.175; upcoming versus shuffled: K=0.45, p=.034; 458 Fig. 6c). The representations of the upcoming choice occurred more during the rising phase of the 459 theta cycle (Rayleigh’s Z=1.05, randomized population M=0.06, CI=[0.00, 0.23], p=.001), whereas the 460 representations of alternative choice were more scattered in relation to the hippocampal theta cycle 461 (Rayleigh’s Z=0.05, randomized population M=0.09, CI=[0.00, 0.33], p=.599; Fig. 6d). Together, these 

- 462 results indicate that while mPFC non-local representations are not time-locked to hippocampal 463 SWRs and theta phase, the non-local representations in the hippocampus are. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**==> picture [425 x 170] intentionally omitted <==**

464 465 

**==> picture [425 x 169] intentionally omitted <==**

- 466 Figure 6. Non-local representations in the hippocampus are linked to SWRs and theta phase. (a) The 

- 467 occurrence of representations of alternative choice (left) and representations of upcoming choice (right) in the 468 hippocampus in temporal proximity to the closest SWR. The p-values indicate the results of a Wilcoxon signed469 rank test between real and shuffled data at bin 0-20 ms from SWR onset. (b) The firing rates of mPFC neurons 470 that are SWR-excited, SWR-inhibited and SWR-unmodulated, during  representations of upcoming and 471 alternative choices, normalized to the average firing rate at the start of the maze. The p-values indicate the 472 results of a Mann-Whitney U test for the firing rates during upcoming and alternative representations for each 473 of the SWR modulation categories. (c) A histogram of the phase of hippocampal theta oscillations at which the 474 start of each representation of upcoming and alternative choices in the hippocampus occurred. The p-values 475 indicate the results of a Kolmogorov-Smirnov test for difference in distributions between the representations of 476 alternative and upcoming choices compared to shuffled decoded probabilities. (d) Left: circular histograms of 477 the phase locking shown in (c). Right: The phase locking score of hippocampal representations of upcoming and 478 alternative choices (Rayleigh’s Z, dark and light brown dots) to hippocampal theta oscillations compared to a 479 randomized population (gray histograms). P-values indicate the result of a left-tailed Monte Carlo test of the 480 Rayleigh’s Z compared to the shuffled population.  Due to less multi-unit activity recorded in the hippocampus, 481 fewer sessions were available with good decoding quality, and figure is made with N=12 sessions from 3 482 animals. 

483 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 484 DISCUSSION 

- 485 In this study, we propose two populations of mPFC neurons that are important for spatial learning 486 and decision making. The first is more strongly influenced by hippocampal events, showing firing 487 patterns linked to hippocampal SWRs, hippocampal theta oscillations and hippocampal non-local 488 representations of upcoming choice. A second population of mPFC neurons is less modulated by 489 hippocampal events. These neurons have higher spatial tuning properties, fire more selectively 490 during certain head movements, and fire more during non-local representations in the mPFC that 491 are predictive of the upcoming choice. 

492 We first showed that neurons in the mPFC are modulated by SWRs in the hippocampus, and 493 this modulation was stronger for the ventral mPFC than the dorsal section of the mPFC. The 494 hippocampus and ventral mPFC are connected through several pathways[42] . The connection with the 495 dorsal mPFC, on the other hand, is much less established. One study has reported a monosynaptic 496 prefrontal cortex projection from the ACC to the hippocampus[43] , but no direct projection from the 497 hippocampus to the ACC. The denser connections with the ventral mPFC could explain the stronger 498 SWR modulation seen in the ventral compared to the dorsal mPFC. 

- 499 Congruent to previous research[12] , we next showed that mPFC neurons that were modulated 500 by hippocampal SWRs, were also phase locked to the hippocampal theta rhythm, suggesting a 501 network of hippocampal spatial mapping and mPFC firing patterns that is co-modulated during both 502 running and resting periods. We showed that these findings hold up for both the dorsal and ventral 503 mPFC, although the preferred phase of the hippocampal theta cycle was different. In the dorsal 504 mPFC, neurons fired more at the peak of the oscillation, while neurons in ventral mPFC fired more 505 just before the trough of the oscillation. An influential paper published in 2009 by Lubenov and 506 Siapas[44] has shown that theta oscillations are organized topographically across the hippocampus, 507 indicating that a segment of space, rather than a point, is represented across the hippocampus at 508 any given point in time. This concept of a ‘traveling wave’ of theta oscillations might translate to the 509 downstream cortical regions as well, as our data suggests that cells in the mPFC are phase locked to 510 later phases of the hippocampal theta cycle in the more ventral regions. 

- 511 We further showed that spatial locations could be reliably decoded based on spiking activity 512 in the mPFC, and that the non-local representations at the start of the maze predicted the future 513 choice of the animal. Moreover, following a rule switch, the mPFC decoded probabilities changed a 514 few trials before the behavioral switch, which points to a leading role of the mPFC in spatial rule 515 switching. There was very little overlap between the non-local representations in the mPFC and the 516 hippocampus for the representations of the upcoming choice and alternative choices. This indicates 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

517 a separation in time between the two regions when engaging in the planning of future trajectories 518 and representing alternative choices. 519 Previous research has shown that spatial mapping in the hippocampus is linked to theta 520 oscillations during running[45,46] , and spatial reactivations are frequently known to occur during SWRs 521 while resting[6,7,13,31,47,48] . Here we showed several pieces of evidence that suggest that spatial 522 mapping in the mPFC occurs at least partially independently from SWRs and theta phase in the 523 hippocampus. First, neurons in the mPFC that were not modulated by hippocampal SWRs, showed 524 higher spatial tuning scores, head direction selectivity and theta cycle skipping properties. The 525 spatial tuning scores and head direction selectivity indicate that these SWR-unmodulated neurons 526 are important for spatially mapping the environment, and theta cycle skipping properties in the 527 mPFC have in the past been linked to signaling upcoming choice[39,41] . The increased involvement of 528 SWR-unmodulated neurons in these functions was robust and consistent across subregions. Second, 529 non-local representations in the mPFC that were predictive of the animals’ upcoming choice, were 530 not linked to hippocampal SWRs and theta phase. In contrast, non-local representations in the 531 hippocampus showed a much higher phase locking score to hippocampal theta oscillations, and 532 these predictive segments were time-locked to SWR events. Finally, SWR-unmodulated neurons in 533 the mPFC preferentially encoded the upcoming choice over the alternative choice at the center of 534 the maze, and these neurons fired more during segments of upcoming choice in the mPFC than the 535 SWR-modulated neurons. This suggests a role for signaling upcoming choice for those neurons that 536 are not modulated by hippocampal SWRs. In contrast, SWR-modulated neurons were linked to non537 local representations in the hippocampus, with firing rate modulations that were homologous to 538 their modulation during SWRs (SWR-excited neurons fired more during hippocampal representations 539 of upcoming choice and SWR-inhibited neurons fired less during hippocampal representations of 540 upcoming choice). 

541 These findings are not directly intuitive, given the running hypothesis that that the 542 hippocampus transfers information to the cortex during SWR events[11] , which could lead one to 543 hypothesize that neurons in the cortex that respond to hippocampal SWRs are responsible for 544 integrating spatial information and creating a spatial map necessary for effective spatial decision 545 making. This hypothesis is supported by several previous findings. For one, a recent paper has shown 546 that spatial maps in several cortical areas become less well defined following hippocampal lesions, 547 indicating that cortical regions rely on input from the hippocampus in order to create a spatial 548 map[49] . A recent paper from our lab further showed that disrupting the mPFC during the 200 ms 549 following SWR onset, slowed learning of a new rule in a spatial alternation task[14] , indicating that the 550 input from the hippocampus during SWRs is indeed necessary for adaptive learning in response to 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 551 changing reward contingencies. However, none of these findings stipulate that the neurons that 552 respond to hippocampal SWRs should be the same neurons that integrate the spatial map and are 553 involved in establishing a behavioral strategy. Neurons in the mPFC that are modulated by 554 hippocampal SWRs have been shown to be selectively modulated by specific reactivation patterns or 555 replay sequences[13] . Therefore, we hypothesize that the population of neurons that is modulated by 556 SWRs is important for signaling which hippocampal reactivation patterns are important, after which 557 another population of mPFC neurons may alter its spatial map accordingly and signal the adapted 558 behavioral strategy following the external rewards and task demands. 

- 559 

- 560 Suggestions for future research 

- 561 Together, these findings raise some interesting questions about the function of SWR-modulated and 562 SWR-unmodulated neurons in spatial learning. We hypothesize that SWR-modulated and SWR563 unmodulated neurons work together by respectively integrating information from the hippocampus 564 and altering the spatial map necessary for effective spatial decision making. To test this hypothesis, a 565 future study could detect SWRs in the hippocampus and inhibit mPFC activity, while also performing 566 high-density probe recordings in the mPFC to obtain information about single cell firing patterns. If 567 the SWR-linked inhibition of the mPFC alters mPFC spatial coding, by lowering the prediction index 568 of the non-local representations for example, this would support the aforementioned hypothesis. 569 Finally, subregion specific disruptions of the dorsal and ventral mPFC, using optogenetics for 570 example, could test whether there is a differential involvement of the two regions in the spatial 571 decision making process. A task with more structured time points of decision making would be 572 recommended to disentangle the times at which this information is encoded in the different 573 subregions. 

- 574 

- 575 Conclusion 

- 576 In conclusion, neurons in the mPFC are able to predict future choice on a maze on a trial-to-trial 577 basis and their prediction precedes the behavioral change over the course of learning. This suggests 

- 578 an important role for the mPFC in spatial learning and decision making. Our results further show that 579 SWR-unmodulated neurons are active at key time points in spatial decision making, and timepoints 

- 580 of non-local decoding in the mPFC and hippocampus do not tend to overlap. This indicates that SWR- 

- 581 modulation is likely not the driving factor behind the non-local decoding in the PFC. 

- 582 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

583 

584 

## 585 METHODS 

- 586 

- 587 Animals 

- 588 Six male Long Evans rats were used in this study, weighing between 300 and 400 grams. The animals 589 were allowed at least one week to acclimatize upon arrival, during which time they were housed in 590 pairs and had unlimited access to food and water. During the course of the experiment, the rats 

- 591 were single housed and kept at a mild food restriction schedule, maintaining over 85% of their initial 592 body weight. 

- 593 

- 594 Apparatus 

- 595 The experiments were conducted in a room of 2.9 by 4.2 meters, with in the center a plus shaped 596 maze that was elevated 50 cm above the ground. The four arms of the maze were 60 cm each, with 597 at the end a platform of 20 by 20 cm holding a reward container, and in the center a piece of 38 by 598 38 cm. 

- 599 

- 600 Pre-training 

- 601 Pre-training was performed with a protocol adapted from previous literature[50] , and consisted of four 602 stages during which the animals slowly got acclimatized to the maze and learned to forage for food 603 reward pellets (chocolate covered rice cereal). First, the rats were familiarized with the maze during 

- 604 5 minutes of free exploration. Next, the day after, 10 reward pellets were spread across the maze 

- 605 and the animals were allowed to forage for 15 minutes. On the third day, three reward pellets were 

- 606 placed in each of the four reward containers and the animal was again allowed to forage for 15 607 minutes. After this, on all consecutive days, only one reward pellet was placed in each reward 

- 608 container, and the animal had to empty all four reward containers in order for them to be refilled. 

- 609 The maze familiarization was completed when the animal consumed all four rewards at least four 

- 610 times within 15 minutes. The animals took on average 8 days to complete the pre-training. 

- 611 

- 612 Allocentric and cue-based rule learning on the plus maze 

- 613 Animals had to learn allocentric and cue-based rules in the maze, which were to be deducted 614 through trial and error over the course of multiple days. Each day started with a rest period of 20 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

615 minutes. After this, the animal was placed by the experimenter on either the East or the West arm of 616 the maze pseudo-randomly and it had to learn to turn to the North, South, illuminated or non617 illuminated arm. The order of the rules was counterbalanced between animals, and the illumination 618 of the arm was always present (also during allocentric learning) and was pseudo-randomly 619 determined for each trial. After arriving at the end of the goal arm, the animal was picked up by the 620 experimenter and placed back in the dark resting box for 30-60 seconds before continuing with the 621 next trial. The training lasted for a maximum of 1.5 hours or 60 trials per day. At the end of the 622 session, animals were placed back in the dark resting box for up to 60 minutes. After reaching the 623 learning criterium (more than 80% of trials correct on three consecutive days), the animals 624 underwent probe implantation surgery (see below). After surgery, the same rule was reinstated until 625 learning criterium. After reinstatement, the rule was switched, either within the same strategy (i.e., 626 rule reversal – from North to South), or to a different strategy (i.e. attentional Set-shift – from North 627 to Illuminated arm), without any indication for the animal. Throughout learning, one of two sounds 628 was played every time the animal passed a sensor halfway through the end arm (at 90 cm along the 629 track). The sounds, a high and low buzz, were associated with correct and incorrect trials. They 630 therefore provided feedback to the animals about whether a reward would be obtained, a few 631 seconds before actually receiving it. Which sound was played to indicate the outcome was 632 counterbalanced across animals but remained constant for each animal during learning. The 633 recordings were completed once the animals had learned all four rules. 

- 634 

635 Implant preparation 

636 To record electrophysiological signals from the hippocampus and mPFC simultaneously while the 637 animals were freely moving in the maze, a dual probe implant was used, designed to hold two 1.0 638 Neuropixels probes (Imec, Leuven, Belgium) at a distance of 6.28 cm[32] . For one of the six animals, 639 there was no probe implanted in the hippocampus, so this animal was excluded from the SWR640 related analyses. Prior to implantation, the implant was assembled containing the two probes. The 

- 641 probes were aligned in the stereotaxic frame to be as parallel to each other as possible and 642 perpendicular to the base of the implant. Two holes at the base of the implant were covered in a 

- 643 mixture of bone wax and mineral oil, and the whole surface was cleaned with Baytril (50 mg/ml). The 

- 644 probes were dipped in isopropanol for sterilization, and then in DiI (DIIC18(3) orange/red 645 carbocyanine dye 549/565 nm, VWR, Radnor, Pa, USA) for visualization of the probe tracks later on. 

- 646 

- 647 Surgical procedures 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

648 Surgery was performed under full anesthesia, using isoflurane (1-2%) administered via a nose cap 649 and adjusted according to the vital signs of the animal (measured with PhysioSuite monitoring 650 system, Kent Scientific, Torrington, CT, USA). A stereotaxic frame with ear bars kept the head in 651 position and the eyes were covered with eye ointment and aluminum foil for protection. After 652 shaving and disinfecting the area, a midline incision was made from the eyes to the ears, exposing 653 both the lambda and bregma on the skull. Craniotomies were drilled above the right hemisphere at 654 the coordinates 2.0 ML and -3.4 AP for the hippocampus and 0.4 ML and +2.7 AP for the mPFC. After 655 carefully removing the dura in both craniotomies, the probes were inserted with a micromanipulator 656 at a speed of 20 µm/s to a depth of maximum 7 mm. 

657 The implant was anchored with 8 self-tapping bone screws (1.19 x 4.8 mm self-tapping bone screws, 658 19010-00, Fine Science Tools, Foster City, CA, USA) placed in a semi-circle in the scull around the 659 implant. One of the posterior screws was connected to grounding wire which in turn connected to 660 the ground of both probes. The implant was fixed using C&B Metabond (Parkell, Edgewood, NM, 661 USA) covering all the bone screws and the exposed part of the scull. After this, the isoflurane level 662 was lowered to 0% and the animal was carefully monitored while regaining consciousness. Post663 operative care included subcutaneous injections of 0.35 ml Metacam as an analgesic and topical 664 application of antibacterial cream (Picri-Baume) and an anesthetic cream (lidocaine) immediately 665 after surgery and on the three days following. 

- 666 

- 667 Histology 

- 668 After completing all the training, animals were euthanized using pentobarbital (5ml intraperitoneal 669 injection of Dolethal, 200 mg/ml). Consecutively, they were perfused transcardially with phosphate 670 buffered saline (PBS), followed by a 4% formaldehyde solution. The brain was removed and stored in 671 a cold room (4[o] C). After 24 hours, it was transferred to a 30% sucrose solution where it was left for 672 at least three days, until it sank to the bottom of the tube. Brains were sectioned using a vibratome 673 (VT1000 S, Leica, Wetzlar, Germany) at 100 µm thickness, after which they were left to dry 674 overnight. Brain sections were stained with a fluorescent Nissl stain (NeuroTrace 530/615 Red 675 Fluorescent Nissl Stain, Thermo Fisher, Waltham, MA, USA), and the probe tracks were visualized 

676 with a fluorescent microscope (MVX10, Olympus, Tokyo, Japan). In order to define the subregions of 677 the mPFC, the probe tracks were reconstructed and mapped using a rat brain atlas[51] . To get the 678 most accurate estimation, information was used from the histological images, together with the 679 known insertion depth during surgery, and the electrophysical signatures in the hippocampus (depth 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 680 at which SWRs occurred). For one animal only the dorsal mPFC was included, and for the other five 

- 681 animals we recorded from both subregions (see Supplementary Fig. S1). 

- 682 

- 683 Data acquisition 

- 684 Neural data was acquired at 30 kHz using a PXIe acquisition module (National Instruments, Austin, 685 TX, USA) and SpikeGLX software (https://billkarsh.github.io/SpikeGLX/) and video data was acquired 686 at 50 Hz via an overhead camera and recorded with Cheetah software (Neuralynx, Bozeman, MT, 687 USA).  An Arduino Uno (Arduino, Turin, Italy) was used to send pulses at fixed intervals but varying 688 durations to the ongoing neural data and video acquisitions, to facilitate the time alignment of the 689 two streams later on (see below). 

- 690 

- 691 Data analysis 

- 692 Position data. Position data was determined using DeepLabCut[52] , a deep neural network algorithm 693 designed for animal behavior tracking. 1084 frames were labelled manually indicating a red and blue 694 LED at the top of the implant, and the tail base of the animal.  The model was trained for 500,000 695 iterations, and the obtained position data was then smoothed, removing any spurious position 696 detections outside of the maze area and position jumps of more than 20 pixels. The positions were 697 linearized in a range from 0 to 240 cm, where positions 0-60 and 120-180 were the two start arms 698 (West and East), and positions 60-120 and 180-240 corresponded to the two goal arms (South and 

- 699 North respectively). For decoding, the position data was binned into 5 cm bins and smoothed with a 700 Gaussian kernel (SD = 5 cm). 

- 701 

- 702 Time synchronization. A time alignment function was created for each session in order to associate 703 the neural signals with the positions in the maze at which they occurred. The time alignment was 

- 704 based on the duration of pulses sent to both systems (neural- and position data) generated by an 705 Arduino Uno. For each timepoint in the analysis, the corresponding timestamp of the other system 706 was extrapolated using a cross-correlation of the pulse durations. 

- 707 

- 708 Spike sorting. Data was pre-processed using CatGT (https://billkarsh.github.io/SpikeGLX/#catgt) with 

- 709 a local common average reference (CAR), using the average between rows 2 and 8 from each 

- 710 electrode as a reference. The pre-processed data was then sorted using Kilosort 2 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

711 (https://github.com/MouseLand/Kilosort/releases/tag/v2.0), with a detection threshold of 5 and a 712 lower frequency limit of 150 Hz. The output for each session was manually curated using Phy2 713 (https://github.com/cortex-lab/phy), and clusters (putative single cells) were selected based on their 714 waveform, principal component features and conformity to the refractory period. After manual 715 curation, the selected clusters (N=11657) underwent an objective quality assessment using spike 716 interface[53] , where only the clusters that were compliant with the neural refractory period (an inter717 spike-interval violation score of less than 0.1, corresponding to less than 10% of contaminating 718 spikes) were included for further analysis. This step eliminated 2798 clusters. Then, putative fast719 spiking interneurons were detected based on the shape of the waveform and the overall firing rate 720 of the neuron (spike half-width < 0.15 ms and firing rate > 17 Hz)[12] , which eliminated an additional 721 189 clusters. Finally, clusters that showed very low spiking in the SWR modulation windows (less 722 than 50 spikes; N=2727) were also excluded from analysis, as this could lead to spurious SWR 723 modulation classifications. These procedures led to a total of 5943 remaining clusters to include for 724 analyses. 

- 725 

726 SWR detection. For each animal with a probe in the hippocampus (N=5), one channel was selected 727 from the top layer of dorsal CA1. This signal was filtered between 160 and 225 Hertz, and a contrast 728 frequency signal was calculated by subtracting the average power of the neighboring frequency 729 bands (100-140 Hertz and 250-400 Hertz), in order to eliminate potential spurious detections due to 730 bursts of high frequency oscillations that are not restricted to the ripple frequency range (e.g. 731 chewing artefacts). A threshold for detection was determined by taking the median amplitude of the 732 computed contrast frequency signal, plus 9 times the median absolute deviation (MAD). A low 733 threshold of the median amplitude plus 0.5 times the MAD was used for determining the start and 734 end times. SWRs were only included if they were longer than or equal to 30 milliseconds in duration. 

- 735 

736 SWR modulation. Spike rates from sorted neurons in the mPFC were obtained and normalized to the 737 pre-ripple window (from 1 until 0 seconds before SWR onset). For each cluster, SWR modulation was 738 calculated by averaging the spike rates over all the SWRs of that session. Neurons were considered 739 SWR-modulated if the absolute peak of the z-score in the first 200 milliseconds after SWR onset was 740 significantly higher than the shuffled population. The shuffled population was obtained by taking the 741 spike rates of the cluster around all SWRs of that session, shuffling along the time axis, and 742 calculating the peak z-score for each of the N=250 shuffles. Statistical significance was determined 

743 by using a Monte-Carlo p-value considering an alpha of .05. 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 744 

- 745 Theta phase locking. Theta epochs were selected based on a running speed of more than 5 cm/s and 746 the absence of SWRs in the hippocampus. The theta phase was then calculated by filtering the 747 hippocampal LFP between 9 and 12 Hertz and taking the angle of the Hilbert transformed signal. 

- 748 Rayleigh’s Z score with associated p-value was calculated for each cluster and theta phase-locking 749 was determined based on the obtained p-value considering an alpha of .05. 

- 750 

- 751 Spatial tuning. To calculate a spatial tuning score for each sorted cluster, the maze was segmented 752 into bins of 5 cm. To avoid SWR-modulated spiking from biasing the data, spike rates during SWR 753 windows (0 to 200 ms after the onset of SWRs) were not included in this analysis. The spike rate in 754 each maze bin was calculated by taking the number of spikes recorded in that bin divided by the 755 time spent there over the course of a session. Then the spatial tuning score was calculated using a 756 method described in previous literature[54] , where the normalized spike count per maze bin is 757 multiplied by the base-2 logarithm of the normalized spike rate, and the output is summed over all 758 maze bins. This gives a spatial index score expressed in bits per spike, which indicates how much 759 spatial information each spike carries. The spatial information score was only calculated for a cluster 760 if there were at least 50 spikes in the maze during the session (more than 2 times the number of 761 bins). 

- 762 

- 763 Head direction selectivity. For each position at the start of the maze, the head direction of the 764 animals was determined based on the two LEDs on top of the animals’ head. Head direction angles 765 were divided in 4 equal quadrants based on the orientation of the maze. The head directions 766 towards the goal arms were then categorized in each of three categories: towards future choice or 767 alternative choice, towards North or South and towards left or right. The spike rates during each 768 head direction were calculated for each neuron, and a neuron was labeled directionally selective if 

- 769 the firing rate was significantly higher during one of the head directions compared to its opposite 

- 770 counterpart (e.g. significantly higher during head directions towards the upcoming choice compared 

- 771 to the alternative choice). Statistical significance was determined by comparing the spike rates to a 772 population of 250 shuffles, where the spike rates per trial were swapped randomly. A directional 

- 773 selectivity index was then calculated by subtracting the overall firing rate during one direction from 

- 774 the firing rate during the other direction and dividing by the sum of both firing rates for each 

- 775 direction category. Thus, this resulted in three scores between -1 (the neuron fired only during head 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 776 directions towards the alternative choice, towards the South arm, or towards right respectively) and 777 1 (the neuron fired only during head direction towards the upcoming choice, towards the North arm, 778 or towards left). Head directions in the other two quadrants (forward and backwards) were not 779 taken into account. Since the head direction selectivity was stronger in the SWR-unmodulated 780 neurons for each of the six directions (see Supplementary Fig. S3), the overall absolute directional 

- 781 selectivity index was calculated by obtaining the absolute maximum score out of each of the three 782 categories per neuron. 

- 783 

- 784 Theta cycle skipping. To determine the theta cycle skipping properties for each cluster, spikes were 785 extracted from periods where the animals were at the start platform, arm and center of the maze. 786 For each of the four possible trajectories on the maze (East-North, East-South, West-North, West787 South), an autocorrelation of spike times was obtained to determine the rhythmicity of firing from 788 one spike to the next. The average histogram of spike times was smoothed, and two peaks were 789 extracted: one at around 125 ms and one at 250 ms, corresponding to one and two theta cycles of 8 790 Hz. The theta cycle skipping index was calculated by subtracting the height of the first peak from the 791 height of the second and normalizing to the maximum height of both peaks. The highest cycle 792 skipping index was selected out of the autocorrelations from the four trajectories. The obtained 793 theta cycle skipping index was then compared to a population of N=250 shuffled scores, which were 794 obtained by a shuffling procedure designed to shuffle the spike times while keeping the existing 795 periodicity of the theta cycle (125 ms) intact. 

- 796 

- 797 Decoding. To decode spatial information from the hippocampus and mPFC, spikes were detected 798 from the CatGT pre-processed data using an amplitude threshold of -50 µV on the high frequency 799 (300-6000 Hertz) filtered signal. Five features were obtained from each detected spike: depth of the 800 channel, spike amplitude, slope of the waveform, height of the positive peak and latency to the 801 positive peak. A Bayesian decoding algorithm was built, associating the spike features with the 802 position in the maze at which they occurred[55] . Periods where the running speed was less than 15 803 cm/s were excluded from the model. A median cross-validated decoding error of less than 20 cm 

- 804 was used as an inclusion criterium, which resulted in 40 sessions from 5 different animals for the 

- 805 mPFC decoding and 12 sessions from 3 different animals for the decoding of the data from the 

- 806 hippocampus. For the decoding models based on only SWR-modulated or SWR-unmodulated 

- 807 neurons, the spike times and amplitudes were selected for each neuron that was classified as SWR- 

- 808 unmodulated or SWR-modulated (as well as SWR-excited and SWR-inhibited separately), after which 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

809 the decoding model was built in the same way as the mPFC decoding, for the same 40 sessions. 

810 

- 811 Prediction index. To predict turning directions based on decoded data, trials were decoded with a bin 812 of 50 ms and 80% overlap, such that every 130 ms was consecutively decoded, corresponding to 813 roughly one theta cycle (at 8 Hz). The decoded probabilities were summed for each maze segment 814 (the two start arms, the center and the two goal arms), and segments of local representations, 815 upcoming choice and alternative choice were obtained by grouping probabilities together in time 816 that had a summed probability of more than 0.5 per maze segment. Segments that were 50 817 milliseconds apart were joined together. The prediction index per trial was then calculated by 818 subtracting the summed probabilities of the non-taken goal arm from the summed probabilities of 819 the taken goal arm and normalizing to the total summed probabilities of both categories. In this way, 820 a score of -1 corresponds to a trial that only contains probabilities of the non-taken goal arm, and a 821 score of 1 corresponds to a trial where all the non-local probabilities are of the taken goal arm. The 822 prediction indices were separated by whether the spatial rule had or had not been learned, and 823 which spatial rule was in place at the time (allocentric or cue-based). For determining the statistical 824 significance of the prediction index, the posterior probabilities were randomized by shuffling the 825 positions in the two goal arms for each time bin in the start, arm and center of the maze. The 826 prediction index was calculated in the same way for the shuffled data as for the real posterior 827 probabilities, and statistical significance was determined by comparing the real and shuffled data. 

- 828 Prediction accuracy versus learning. To determine whether the prediction accuracy per trial was 829 leading or lagging with respect to the behavior, learning curves were obtained with a moving 830 average of N=10, and overlaid with curves made from the predicted direction based on the non-local 831 representations in the mPFC. The correlation between the two curves (Pearson’s r) was calculated 832 for each trial lag of -N/2 to N/2 (N denotes the total number of trials), such that a peak of 833 correlations at a negative lag indicates that the real direction is lagging behind the predicted 834 direction and a peak of correlations at a positive lag indicates that the real direction is leading the 835 predicted direction. 

- 836 

- 837 Overlap decoding mPFC versus hippocampus. To assess the overlap of decoding between the 838 hippocampus and the mPFC, each decoded time bin (of 50 ms and 80% overlap), was classified as 839 ‘local’ (the same arm or reward platform as the animal is physically present), ‘alternative choice’ (the 

- 840 arm or reward platform that the animal does not end up visiting on this trial), ‘upcoming choice’ (the 

- 841 arm or reward platform that the animal will visit), or ‘other’ (the other start arm, the center of the 

- 842 maze or low decoding probabilities, i.e. <0.5, for all of the categories). Then the number of 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 843 overlapping classifications was counted and divided by the total number of decoded time bins of the 844 session and multiplied by 100 to obtain the percentage of overlap. For each session, the 845 classifications from the hippocampus were shuffled 500 times using a rolling method over the 846 position axis. The mean overlap of the shuffled data was compared to the true overlap per session 847 using a paired samples t-test. This procedure was repeated for the decoded data from all mPFC 848 neurons, and for the SWR-unmodulated, SWR-modulated, SWR-excited and SWR-inhibited decoded 849 data separately. 

- 850 

- 851 Time-locking to hippocampal SWRs and theta phase. To determine the time locking of segments of 852 upcoming and alternative choice in the mPFC and hippocampus to hippocampal SWRs, each decoded 853 segment of alternative and upcoming choice (any number of consecutive time bins where the 854 decoded probabilities of the alternative and upcoming choice respectively were more than 0.5), was 855 assessed for its temporal proximity to hippocampal SWRs. Only non-local segments that occurred 856 within 2 seconds of a SWR were taken into account for this analysis, and only the SWR that occurred 857 closest in time to the non-local segment was included. The histogram of temporal proximity was then 858 normalized to the total number of SWRs per session, and compared to the temporal proximity of 859 shuffled posterior probabilities (randomly rolled over the position axis for each decoded time bin). To 860 determine the phase locking to hippocampal theta, theta epochs were selected as described above 861 (based on a running speed of more than 5 cm/s and the absence of SWRs in the hippocampus), and 862 the theta phase of each decoded bin was determined using a band-pass filter of 9-12 Hertz, and 863 obtaining the angle of the Hilbert transform of this signal. Then, the histogram of theta phases was 864 obtained for the segments of alternative and upcoming choice separately and normalized to the 865 number of segments included. To determine statistical significance, the histograms were compared 866 to shuffled posterior probabilities using a Kolmogorov-Smirnov test. 

- 867 Statistics. All statistical tests were performed using the SciPy library for python[56] . All comparisons 868 were done on the means per session, so that sessions with a very high number of neurons in a 869 certain subregion did not skew the results for that subregion. For every comparison, the 870 assumptions of normality and heteroscedasticity were tested and non-parametric tests were chosen 871 if the assumptions were violated. The difference between firing rates of SWR-modulated and SWR- 

- 872 unmodulated neurons was calculated using an ANOVA or Kruskall-Wallis test (non-parametric). For 

- 873 comparisons between two groups, independent samples t-tests or Mann-Whitney U tests (non874 parametric) were used. 

875 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 876 Acknowledgements 

- 877 We thank Frederic Michon, Cagatay Aydin and Rik van Daal for their contributions in the set-up for 

- 878 chronic Neuropixels probes recordings in freely moving animals and Marine Guyot for her software 

- 879 contributions. F.K is funded by Research Foundation Flanders (FWO), Belgium under grant number 

- 880 G0A5422N, and grant number G077321N and KU Leuven, Belgium C1 grant C14/17/042. 

- 881 

- 882 Author contributions 

- 883 Conceptualization, H.d.B. and F.K.; Methodology, H.d.B. and F.K.; Software, F.K.; Formal analysis, 

- 884 H.d.B, and F.K.; Investigation, H.d.B; Writing - Original draft, H.d.B, and F.K.; Writing - review and 

- 885 editing, H.d.B., and F.K.; Visualization, H.d.B. and F.K.; Supervision, F.K.; Funding Acquisition, F.K. 

- 886 

- 887 Competing interests 

- 888 The authors declare no competing interests 

- 889 

## 890 Materials & Correspondence 

- 891 Correspondence and request for materials can be addressed to Hanna den Bakker. 

- 892 

- 893 Data Availability 

- 894 The data that support the findings of this study are available from the corresponding author upon 

- 895 reasonable request 

- 896 

- 897 

- 898 

- 899 

- 900 

- 901 

- 902 

bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 903 References 

- 904 1. Pfeiffer, B. E. & Foster, D. J. Hippocampal place-cell sequences depict future paths to 905 remembered goals. Nature 497, 74–79 (2013) doi: 10.1038/nature12112. 

- 906 2. Pastalkova, E., Itskov, V., Amarasingham, A. & Buzsáki, G. Internally Generated Cell Assembly 907 Sequences in the Rat Hippocampus. Science 321, 1322–1327 (2008) doi: 908 10.1126/science.1159775. 

|909|3.|Johnson, A. & Redish, A. D. Neural ensembles in CA3 transiently encode paths forward of the|
|---|---|---|
|910||animal at a decision point.J. Neurosci. 27, 12176–12189 (2007) doi:|
|911||10.1523/JNEUROSCI.3761-07.2007.|
|912|4.|Dragoi, G. & Tonegawa, S. Preplay of future place cell sequences by hippocampal cellular|
|913||assemblies.Nature 469, 397–401 (2011) doi: 10.1038/nature09633.|
|914|5.|Dragoi, G. & Tonegawa, S. Distinct preplay of multiple novel spatial experiences in the rat.|
|915||Proc. Natl. Acad. Sci. U. S. A. 110, 9100–9105 (2013) doi: 10.1073/pnas.1306031110.|
|916|6.|Gillespie, A. K.et al.Hippocampal replay reflects specific past experiences rather than a plan|
|917||for subsequent choice.Neuron 109, 3149–3163 (2021) doi: 10.1016/j.neuron.2021.07.029.|
|918|7.|Ambrose, R. E., Pfeiffer, B. E. & Foster, D. J. Reverse Replay of Hippocampal Place Cells Is|
|919||Uniquely Modulated by Changing Reward.Neuron 91, 1124–1136 (2016) doi:|
|920||10.1016/j.neuron.2016.07.047.|
|921|8.|Ólafsdóttir, H. F., Carpenter, F. & Barry, C. Task Demands Predict a Dynamic Switch in the|
|922||Content of Awake Hippocampal Replay.Neuron 96, 925–935 (2017) doi:|
|923||10.1016/j.neuron.2017.09.035.|
|924|9.|Ólafsdóttir, H. F., Bush, D. & Barry, C. The Role of Hippocampal Replay in Memory and|
|925||Planning.Curr. Biol. 28, 37–50 (2018) doi: 10.1016/j.cub.2017.10.073.|
|926|10.|Bendor, D. & Wilson, M. A. Biasing the content of hippocampal replay during sleep.Nat.|
|927||Neurosci. 15, 1439–1444 (2012) doi: 10.1038/nn.3203.|
|928|11.|Buzsáki, G. Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and|
|929||planning.Hippocampus 25, 1073–1188 (2015) doi: 10.1002/hipo.22488.|
|930|12.|Jadhav, S. P., Rothschild, G., Roumis, D. K. & Frank, L. M. Coordinated Excitation and|
|931||Inhibition of Prefrontal Ensembles During Awake Hippocampal Sharp-Wave Ripple Events.|
|932||Neuron 90, 113–127 (2016) doi: 10.1016/j.neuron.2016.02.010.|
|933|13.|Berners-Lee, A., Wu, X. & Foster, D. J. Prefrontal cortical neurons are selective for non-local|
|934||hippocampal representations during replay and behavior.J. Neurosci. 41, 5894–5908 (2021)|
|935||doi: 10.1523/JNEUROSCI.1158-20.2021.|
|936|14.|den Bakker, H., Van Dijck, M., Sun, J.-J. & Kloosterman, F. Sharp-wave ripple associated|
|937||activity in the medial prefrontal cortex supports spatial rule switching.Cell Rep. 42, (2023)|
|938||doi: https://doi.org/10.1016/j.celrep.2023.112959.|
|939|15.|León, L. A.et al.Behavioral effects of systemic, infralimbic and prelimbic injections of a|
|940||serotonin 5-HT2A antagonist in carioca high- and low-conditioned freezing rats.Front. Behav.|
|941||Neurosci. 11, 1–13 (2017) doi: 10.3389/fnbeh.2017.00117.|
|942|16.|Sangha, S., Robinson, P. D., Greba, Q., Davies, D. A. & Howland, J. G. Alterations in reward,|
|943||fear and safety cue discrimination after inactivation of the rat prelimbic and infralimbic|
|944||cortices.Neuropsychopharmacology 39, 2405–2413 (2014) doi: 10.1038/npp.2014.89.|



bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

|945|17.|Sun, W., Li, X. & An, L. Distinct roles of prelimbic and infralimbic proBDNF in extinction of|
|---|---|---|
|946||conditioned fear.Neuropharmacology 131, 11–19 (2018) doi:|
|947||10.1016/j.neuropharm.2017.12.018.|



|948|18.|Rich, E. L. & Shapiro, M. Rat prefrontal cortical neurons selectively code strategy switches.J.|
|---|---|---|
|949||Neurosci. 29, 7208–7219 (2009) doi: 10.1523/JNEUROSCI.6068-08.2009.|
|950|19.|Holroyd, C. B. & Coles, M. G. H. The neural basis of human error processing: Reinforcement|
|951||learning, dopamine, and the error-related negativity.Psychol. Rev. 109, 679–709 (2002) doi:|
|952||10.1037/0033-295X.109.4.679.|
|953|20.|Holroyd, C. B. & Krigolson, O. E. Reward prediction error signals associated with a modified|
|954||time estimation task.Psychophysiology 44, 913–917 (2007) doi: 10.1111/j.1469-|
|955||8986.2007.00561.x.|
|956|21.|Hyman, J. M., Holroyd, C. B. & Seamans, J. K. A Novel Neural Prediction Error Found in|
|957||Anterior Cingulate Cortex Ensembles.Neuron 95, 447–456 (2017) doi:|
|958||10.1016/j.neuron.2017.06.021.|
|959|22.|Sambrook, T. D. & Goslin, J. A neural reward prediction error revealed by a meta-analysis of|
|960||ERPs using great grand averages.Psychol. Bull. 144, 213–235 (2015) doi:|
|961||10.1037/bul0000006.|
|962|23.|Totah, N. K. B., Kim, Y. B., Homayoun, H. & Moghaddam, B. Anterior cingulate neurons|
|963||represent errors and preparatory attention within the same behavioral sequence.J. Neurosci.|
|964||29, 6418–6426 (2009) doi: 10.1523/JNEUROSCI.1142-09.2009.|
|965|24.|Howland, J. G., Ito, R., Lapish, C. C. & Villaruel, F. R. The rodent medial prefrontal cortex and|
|966||associated circuits in orchestrating adaptive behavior under variable demands.Neurosci.|
|967||Biobehav. Rev. 135, 1–12 (2022) doi: 10.1016/j.neubiorev.2022.104569.|
|968|25.|Diehl, G. W. & Redish, A. D. Differential processing of decision information in subregions of|
|969||rodent medial prefrontal cortex.Elife 12, 1–36 (2023) doi:|
|970||https://doi.org/10.7554/eLife.82833.|
|971|26.|Tang, W., Shin, J. D., Frank, L. M. & Jadhav, S. P. Hippocampal-prefrontal reactivation during|
|972||learning is stronger in awake compared with sleep states.J. Neurosci. 37, 11789–11805|
|973||(2017) doi: 10.1523/JNEUROSCI.2291-17.2017.|
|974|27.|Jiang, X.et al.Replay of large-scale spatio-temporal patterns from waking during subsequent|
|975||NREM sleep in human cortex.Sci. Rep. 7, 1–17 (2017) doi: 10.1038/s41598-017-17469-w.|
|976|28.|Kaefer, K., Nardin, M., Blahna, K. & Csicsvari, J. Replay of Behavioral Sequences in the Medial|
|977||Prefrontal Cortex during Rule Switching.Neuron 106, 154–165 (2020) doi:|
|978||10.1016/j.neuron.2020.01.015.|
|979|29.|Mashhoori, A., Hashemnia, S., McNaughton, B. L., Euston, D. R. & Gruber, A. J. Rat anterior|
|980||cingulate cortex recalls features of remote reward locations after disfavoured|
|981||reinforcements.Elife 7, 1–18 (2018) doi: 10.7554/eLife.29793.|
|982|30.|Peyrache, A., Khamassi, M., Benchenane, K., Wiener, S. I. & Battaglia, F. P. Replay of rule-|
|983||learning related neural patterns in the prefrontal cortex during sleep.Nat. Neurosci. 12, 919–|
|984||926 (2009) doi: 10.1038/nn.2337.|
|985|31.|Shin, J. D., Tang, W. & Jadhav, S. P. Dynamics of awake hippocampal-prefrontal replay for|
|986||spatial learning and memory-guided decision making.Neuron 104, 1110–1125 (2019) doi:|
|987||10.1016/j.neuron.2019.09.012.|



bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

|988|32.|van Daal, R. J. J.et al.Implantation of Neuropixels probes for chronic recording of neuronal|
|---|---|---|
|989||activity in freely behaving mice and rats.Nat. Protoc. 16, 3322–3347 (2021) doi:|
|990||10.1038/s41596-021-00539-9.|
|991|33.|Siapas, A. G., Lubenov, E. V. & Wilson, M. A. Prefrontal phase locking to hippocampal theta|
|992||oscillations.Neuron 46, 141–151 (2005) doi: 10.1016/j.neuron.2005.02.028.|
|993|34.|Shin, J. D., Tang, W. & Jadhav, S. P. Awake Hippocampal-Prefrontal Replay Mediates Spatial|
|994||Learning and Decision Making.SSRN Electron. J.(2019) doi:10.2139/ssrn.3385138 doi:|
|995||10.2139/ssrn.3385138.|
|996|35.|Sauer, J.-F., Folschweiller, S. & Bartos, M. Topographically organized representation of space|
|997||and context in the medial prefrontal cortex.Proc. Natl. Acad. Sci. 119, 1–8 (2022) doi:|
|998||10.1073/pnas.2117300119.|
|999|36.|Sargolini, F.et al.Conjunctive Representation of Position, Direction, and Velocity in|
|1000||Entorhinal Cortex.Science 312, 758–763 (2006) doi: 10.1126/science.1125572.|
|1001|37.|Jankowski, M. M.et al.Nucleus reuniens of the thalamus contains head direction cells.Elife 3,|
|1002||1–10 (2014) doi: 10.7554/eLife.03075.|
|1003|38.|Lozano, Y. R.et al.Retrosplenial and postsubicular head direction cells compared during|
|1004||visual landmark discrimination.Brain Neurosci. Adv. 1, 1–17 (2017) doi:|
|1005||10.1177/2398212817721859.|
|1006|39.|Robinson, J. C. & Brandon, M. P. Skipping ahead: A circuit for representing the past, present,|
|1007||and future.Elife 10, 1–20 (2021) doi: 10.7554/eLife.68795.|
|1008|40.|Tang, W., Shin, J. D. & Jadhav, S. P. Multiple time-scales of decision-making in the|
|1009||hippocampus and prefrontal cortex.Elife 10, 1–27 (2021) doi:|
|1010||https://doi.org/10.7554/eLife.66227.|
|1011|41.|Kay, K.et al.Constant Sub-second Cycling between Representations of Possible Futures in the|
|1012||Hippocampus.Cell 180, 552–567 (2020) doi: 10.1016/j.cell.2020.01.014.|
|1013|42.|Eichenbaum, H. Prefrontal – hippocampal interactions in episodic memory.Nat. Rev.|
|1014||Neurosci. 18, 547–558 (2017) doi: 10.1038/nrn.2017.74.|
|1015|43.|Rajasethupathy, P.et al.Projections from neocortex mediate top-down control of memory|
|1016||retrieval.Nature 526, 653–659 (2015) doi: 10.1038/nature15389.|
|1017|44.|Lubenov, E. V. & Siapas, A. G. Hippocampal theta oscillations are travelling waves.Nature|
|1018||459, 534–539 (2009) doi: 10.1038/nature08010.|
|1019|45.|Zielinski, X. M. C., Shin, X. J. D. & Jadhav, X. S. P. Coherent Coding of Spatial Position Mediated|
|1020||by Theta Oscillations in the Hippocampus and Prefrontal Cortex.J. Neurosci. 39, 4550–4565|
|1021||(2019) doi: https://doi.org/10.1523/JNEUROSCI.0106-19.2019.|
|1022|46.|Zielinski, M. C., Tang, W. & Jadhav, S. P. The role of replay and theta sequences in mediating|
|1023||hippocampal-prefrontal interactions for memory and cognition.Hippocampus 30, 60–72|
|1024||(2020) doi: 10.1002/hipo.22821.|
|1025|47.|Denovellis, E. L.et al.Hippocampal replay of experience at real-world speeds.Elife 10, 1–33|
|1026||(2021) doi: 10.7554/eLife.64505.|
|1027|48.|Karlsson, M. P. & Frank, L. M. Awake replay of remote experiences in the hippocampus.Nat.|
|1028||Neurosci. 12, 913–918 (2009) doi: 10.1038/nn.2344.|



bioRxiv preprint doi: https://doi.org/10.1101/2024.09.09.610935; this version posted July 14, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

|1029|49.|Esteves, I. M.et al.Spatial information encoding across multiple neocortical regions depends|
|---|---|---|
|1030||on an intact hippocampus.J. Neurosci. 41, 307–319 (2021) doi: 10.1523/JNEUROSCI.1788-|
|1031||20.2020.|
|1032|50.|Floresco, S. B., Zhang, Y. & Enomoto, T. Neural circuits subserving behavioral flexibility and|
|1033||their relevance to schizophrenia.Behav. Brain Res. 204, 396–409 (2009) doi:|
|1034||10.1016/j.bbr.2008.12.001.|
|1035|51.|Paxinos, G. & Watson, C.The Rat Brain in Stereotaxic Coordinates. (Academic Press, 2006).|
|1036|52.|Mathis, A.et al.DeepLabCut: markerless pose estimation of user-defined body parts with|
|1037||deep learning.Nat. Neurosci. 21, (2018) doi: 10.1038/s41593-018-0209-y.|
|1038|53.|Buccino, A. P.et al.SpikeInterface, a unified framework for spike sorting.Elife1–24 (2020).|
|1039|54.|Skaggs, W. E., McNaughton, B., Gothard, K. M. & Markus, E. J. An information-theoretic|
|1040||approach to deciphering the hippocampal code.Neural Inf. Process. Syst. 5, 1030–1038|
|1041||(1993).|
|1042|55.|Kloosterman, F., Layton, S. P., Chen, Z. & Wilson, M. A. Bayesian decoding using unsorted|
|1043||spikes in the rat hippocampus.J. Neurophysiol. 111, 217–227 (2014) doi:|
|1044||10.1152/jn.01046.2012.|
|1045|56.|Virtanen, P.et al.SciPy 1.0: fundamental algorithms for scientific computing in Python.Nat.|
|1046||Methods 17, (2020) doi: 10.1038/s41592-019-0686-2.|
|1047|||
|1048|||



a 

**==> picture [8 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
b<br>**----- End of picture text -----**<br>


**==> picture [311 x 235] intentionally omitted <==**

**==> picture [24 x 134] intentionally omitted <==**

**==> picture [88 x 102] intentionally omitted <==**

**==> picture [84 x 102] intentionally omitted <==**

**==> picture [160 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
d<br>number of neurons<br>200 animal A<br>animal C<br>animal D<br>175<br>animal E<br>animal F<br>150 animal I<br>125<br>100<br>75<br>50<br>25<br>0<br>HPC dorsal ventral<br>mPFC mPFC<br>**----- End of picture text -----**<br>


c 

**==> picture [261 x 152] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>**----- End of picture text -----**<br>


**==> picture [162 x 75] intentionally omitted <==**

**==> picture [168 x 330] intentionally omitted <==**

**----- Start of picture text -----**<br>
b<br>**----- End of picture text -----**<br>


**==> picture [377 x 496] intentionally omitted <==**

**----- Start of picture text -----**<br>
c e<br>f h<br>100<br>p<.001<br>80<br>60<br>p=.117<br>40<br>20<br>0<br>g<br>p<.001<br>p=.005<br>**----- End of picture text -----**<br>


a 

**==> picture [55 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
spatial tuning<br>**----- End of picture text -----**<br>


**==> picture [286 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
SI=0.93, p=.004 SI=0.42, p=.036 SI=0.15, p=.004 SI=0.05, p=.044<br>max = 18 Hz max = 15 Hz max = 21 Hz max = 35 Hz<br>max<br>SI=0.69, p=.004 SI=0.19, p=.120 SI=0.10, p=.199 SI=0.02, p=.912<br>max = 3 Hz max = 10 Hz max = 12 Hz max = 13 Hz<br>0<br>**----- End of picture text -----**<br>


## head direction 

## c 

**==> picture [287 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
alternative | North | right alternative | North | left upcoming | North | left<br>upcoming | South | left upcoming | South | right alternative | South | right<br>**----- End of picture text -----**<br>


## theta cycle skipping 

## e 

**==> picture [286 x 138] intentionally omitted <==**

**==> picture [247 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
b<br>spatial tuning (bits/spike) spatial tuning (bits/spike)<br>p<.001<br>0.7<br>0.4<br>0.6<br>0.5<br>0.3<br>p=.639<br>0.4<br>0.2<br>0.3<br>0.2<br>0.1<br>0.1<br>0.0 0.0<br>HPC dorsal ventral dorsal mPFC ventral mPFC<br>mPFC<br>**----- End of picture text -----**<br>


**==> picture [246 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
d<br>selective neurons (%) directional selectivity index<br>p=.176 p<.001<br>40 p<.001<br>0.5<br>35<br>p=.831<br>30 0.4<br>25<br>0.3<br>20<br>15 0.2<br>10<br>0.1<br>5<br>0 0.0<br>HPC dorsal ventral dorsal mPFC ventral mPFC<br>mPFC<br>**----- End of picture text -----**<br>


**==> picture [246 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
f<br>cycle skipping neurons (%) cycle skipping neurons (%)<br>50 p=.003 p<.001 p=.004<br>30<br>40 25<br>p=.412 20<br>30<br>15<br>20<br>10<br>10<br>5<br>0 0<br>HPC dorsal ventral dorsal mPFC ventral mPFC<br>mPFC<br>**----- End of picture text -----**<br>


**==> picture [444 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
a decoded segment of upcoming choice decoded segment of alternative choice real location<br>alternative choice<br>upcoming choice<br>center<br>alternative start<br>start arm<br>decoded probability<br>500 ms 500 ms 500 ms<br>0.0 0.4 0.8<br>b c<br>p<.001 1.0<br>p<.001 old rule new rule<br>p=.072<br>p<.001 0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>Trials: 0 10 20 30 40 50 60<br>**----- End of picture text -----**<br>


**==> picture [441 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
d distribution of decoded probabilities at center of maze e overlap decoded probabilities<br>0.06 all PFC neurons p<.001 shufflelocal 8 shufflealternative shuffleupcoming<br>18<br>0.04 p=.008 3 [p=.154]<br>0.02 16 p=.228 p=.151<br>14 6<br>0.00<br>SWR-modulated p=.071<br>0.06 p=.135 12 2 p=.325<br>0.04<br>10 4<br>0.02<br>8<br>0.00<br>SWR-unmodulated 6 1<br>0.06 p<.001 2 p=.266<br>p=.302<br>4<br>0.04<br>p=.973<br>0.02 2<br>0 0<br>0.00 0<br>end middle start start middle end all mod unmod all mod unmod all mod unmod<br>decoded maze bins  decoded maze bins SWR modulation SWR modulation SWR modulation<br>alternative choice upcoming choice decoding in the prefrontal cortex<br>overlap with hippocampal decoding (% of time bins)<br>fraction of time<br>**----- End of picture text -----**<br>


**==> picture [448 x 361] intentionally omitted <==**

**----- Start of picture text -----**<br>
decoded segments in the prefrontal cortex b<br>alternative choice upcoming choice<br>shuffle shuffle 0.5 p=.082 p=.023<br>25<br>0.4<br>20<br>0.3<br>15 0.2<br>0.1 p=.420<br>10 p=.380 p=.147<br>0.0<br>5 -0.1 SWR-excited<br>SWR-inhibited<br>SWR-unmodulated<br>-0.2<br>0<br>-2 -1 0 1 2 -2 -1 0 1 2 local alternative upcoming<br>time to closest SWR (s) time to closest SWR (s) choice choice<br>10 decoded segments in the prefrontal cortex d alternative p=.060 p=.116<br>alternative choice upcoming choice 0<br>shuffle shuffle 0.06<br>8 0.05<br>-π/2 π/2<br>p=.292 p=.644 0.04<br>6<br>π<br>0.03<br>upcoming<br>4 0<br>0.02<br>2 -π/2 π/2 0.01<br>0.00<br>0 -π -π/2 0 π/2 π -π -π/2 0 π/2 π π alternative upcoming<br>hippocampal theta phase hippocampal theta phase choice choice<br>**----- End of picture text -----**<br>


**==> picture [454 x 360] intentionally omitted <==**

**----- Start of picture text -----**<br>
a decoded segments in the hippocampus b<br>alternative choice upcoming choice<br>shuffle shuffle 0.5<br>25<br>p=.004 0.4<br>20 0.3<br>p=.978<br>15 0.2<br>0.1<br>10<br>0.0<br>5 -0.1<br>-0.2<br>0<br>-2 -1 0 1 2 -2 -1 0 1 2 local alternative upcoming<br>time to closest SWR (s) time to closest SWR (s) choice choice<br>c 10 decoded segments in the hippocampus d alternative p=.618 p=.001<br>alternative choice upcoming choice 0<br>shuffle shuffle 1.0<br>8<br>p=.175 p=.034 -π/2 π/2 0.8<br>6<br>π 0.6<br>upcoming<br>4 0 0.4<br>2 -π/2 π/2 0.2<br>0.0<br>0 -π -π/2 0 π/2 π -π -π/2 0 π/2 π π alternative upcoming<br>hippocampal theta phase hippocampal theta phase choice choice<br>**----- End of picture text -----**<br>


