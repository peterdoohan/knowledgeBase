acta ethol (2017) 20:165–173 DOI 10.1007/s10211-017-0260-9 

ORIGINAL ARTICLE 

**==> picture [20 x 19] intentionally omitted <==**

# Studying hunting behaviour in the striped field mouse using data compression 

Zhanna Reznikova[1,2] & Jan Levenets[1] & Sofia Panteleeva[1,2] & Boris Ryabko[2,3] 

Received: 5 August 2016 /Revised: 4 April 2017 /Accepted: 6 April 2017 /Published online: 13 April 2017 # Springer-Verlag Berlin Heidelberg and ISPA 2017 

Abstract We compare predatory behaviour towards a mobile insect in three species of small mammals: the granivorous striped field mouse, the insectivorous common shrew and the Norway rat (a generalist). The striped field mouse displays a surprisingly efficient hunting stereotype. We apply the data compression method (Ryabko et al. Theory Comput Syst 52:133–147, 2013) to compare the complexity of hunting behavioural patterns and to evaluate the flexibility of stereotypes and their succinctness. Norway rats demonstrated the highest level of complexity of hunting behaviour, with the highest proportion of ‘auxiliary’ and ‘noise’ elements and relatively low proportion of ‘key’ elements in their behaviours. The predominance of ‘key’ elements resulted in similarly low levels of complexity of hunting stereotypes in striped field mice and shrews. The similarity between hunting stereotypes of the insectivorous shrew and the granivorous striped field mouse enables us to argue about evolutionary roots of hunting behaviour in small mammals. We show that this method is a useful tool for comparing ‘ ’ ethograms as biological texts . 

Electronic supplementary material The online version of this article (doi:10.1007/s10211-017-0260-9) contains supplementary material, which is available to authorized users. 

- Zhanna Reznikova zhanna@reznikova.net 

- 1 Institute of Systematics and Ecology of Animals, Siberian Branch RAS, Frunze 11, Novosibirsk 630091, Russia 

- 2 Novosibirsk State University, Pirogova 2, Novosibirsk 630090, Russia 

- 3 Institute of Computational Technologies, Siberian Branch RAS, Academician M.A. Lavrentiev Avenue, 6, Novosibirsk 630090, Russia 

Keywords Ethograms[. ] Rodents[. ] Shrews[. ] Pattern[. ] Insects[.] Prey 

## Introduction 

Small rodents play a central role in many ecosystems; however, their foraging ecology and behavioural adaptations for choosing optimal diets in changeable environment have been insufficiently investigated. It is of particular interest to study hunting behaviour in those species that possess a diverse diet and can switch to live prey in order to broaden their feeding niche. Recently, we revealed advanced hunting behaviour in the striped field mouse Apodemus agrarius. In our laboratory experiments A. agrarius displayed surprisingly advanced skills in hunting such aggressive, fast-moving and relatively large prey as red wood ants. Their hunting efficiency appeared to be comparable with that of specialised predators: striped field mice killed and ate 0.36 ± 0.19 ants per minute (Panteleeva et al. 2013). This is the first study of ant-hunting in Muridae, even though insect predation has been described in this family previously. While nearly every rodent species is to some degree omnivore (Landry 1970), the degree of carnivory has been poorly estimated for Muridae, except for the studies on ‘predator aggression’ towards insects in genetic lines of house mice (see for example Whelton and O’Boyle 1977; Gammie et al. 2003). It is known that striped field mice, although they eat mainly seeds and plants, include a great deal of insects in their rather diverse diet (Babińska-Werka et al. 1981); however, details of insect hunting were not studied in this species and that A. agrarius can be considered advanced hunters has not been known before. We hypothesise that the striped field mouse possesses specific behavioural adaptations for hunting. To test this hypothesis, we need a reliable criterion to compare hunting behaviour of this species with a known 

acta ethol (2017) 20:165–173 

166 

specialised predator such as the insectivorous shrew on the one hand and with a generalist such as the Norway rat, on the other hand. 

To obtain quantitative comparative characteristics of behavioural patterns in different species, we apply the data compression method of Ryabko et al. (2013), which is based on the evaluation of complexity of biological ‘texts’, from DNA sequences to ethograms. The concept of complexity of animal behaviour is still mainly intuitive. First of all, one has to distinguish between the complexity of flexible and stereotypic behaviour. In the first case, we mean levels of complexity of problems to solve and decisions to make (Reznikova 2007), whereas in the second case, we mean the inner coordination and regularity of species-specific repertoire (Reznikova et al. 2012). The more ‘complex’ a behavioural pattern is, the more difficult it is to detect regularities in it and predict sequences of elements. In our study, we are focusing on searching for regularities in species-specific hunting stereotypes in three species of small mammals with different diets. 

Although recognition and description of behavioural patterns is one of the keystones in behavioural studies (Bateson and Martin 1999), attempts to examine the organisational complexity of patterns so far have been aimed mainly at signal activities (Beecher 1989; Ryabko and Reznikova 1996; McCowan et al. 2002; Forrester 2008; Oller and Griebel 2008; Pollard and Blumstein 2012; Kershenbaum et al. 2014). The prevalent method of comparative ethological studies is based on the analysis of ethograms, that is, recordings of behavioural sequences of letters from an alphabet that consists, on average, of 10–15 symbols or letters, each corresponding to a certain behavioural element (an act) (Tinbergen 1951; Martin and Bateson 1993). For example, hunting attacks in many species, both vertebrates and invertebrates, consist of more or less constant sequences of acts (for reviews, see MacNulty et al. 2007; Fedderwitz et al. 2015). Ethograms can be presented roughly as a recording like this: R – – – – (running) A (approaching) J (jumping) F (fighting) C (capturing)–H (handling)–K (killing). Analysis of ethograms as sequences of symbols from a finite alphabet (or ‘texts’) in ethology presents the same problem as in many other scientific fields, including molecular biology and genetics (genetic texts), linguistics (literary and musical texts), zoosemiotics (animal communications), and others (Gauvrit et al. 2014). An important difficulty that researchers face in these domains is finding an adequate model which would allow for an assessment of certain characteristics of a ‘text’ while using a relatively small number of parameters. For instance, one of the most popular approaches is based on the modelling sequences by stochastic processes. Modelling DNA sequences by Markov processes of finite depth, or connectivity, can serve as a good example here, as well as analysing vocal sequences in animals (Kershenbaum et al. 2014). In order to obtain an approximately adequate model of a text of a certain type, it is 

necessary to increase the number of parameters which, in turn, should be estimated statistically based on real data. For example, if the frequency of each letter in a genetic text depends on n, n > 0 previous letters, then the number of parameters equals 4[n] . When n = 10, the numbers of parameters is 2[20] , that is, about one million, and one needs at least several times more data to estimate these parameters with any reasonable precision. Such amounts of data are typically not available in the behavioural applications considered. 

The data compression method (Ryabko et al. 2013) is based on the concept of Kolmogorov complexity and allows to search for regularities within sequences of symbols with relatively small numbers of parameters. The main idea behind the data compression method is that it is able to capture all kind of regularities in the text and do so in a way amenable to formal statistical analysis. An ideal data compressor would be able to capture all possible regularities in a text, and thus compress it to its Kolmogorov complexity (see details in the ‘Hypothesis testing’ section). A real data compressor is of course able to capture only some regularities—those that the algorithm behind the data compressors is designed to capture. Nevertheless, this typically goes well beyond the frequencies of individual letters or frequencies of all words of a given length (which is what is analysed by Markov models). In any case, whatever the data compressor, we are able to reason precisely about the outcome of the resulting test. Specifically, the probability of type I error (that the difference in complexities is found whereas there is none) is guaranteed to be less than the pre-specified confidence level. It is worth mentioning that some other specific regularities of biological texts have been studied previously. One rich and important class of regularities is studied by what is known as T-pattern analysis (Magnusson 2000; Casarrubea et al. 2009, 2015). This approach makes it possible to reveal recurring sequences of events that are not necessarily consecutive, allowing for a deeper analysis of the structure of the behaviour including its temporal characteristics. However, there are no formal and rigorous statistical tests available based on these regularities. 

Here we use the data compression method (Ryabko et al. 2013) to analyse ethograms of hunting behaviour in three species of small mammals with different levels of hunting activity: the common shrew Sorex araneus, well-known as an insectivorous predator (Vogel 1976; Saarikko 1989; Churchfield et al. 2012), the striped field mouse A. agrarius known before as granivorous, and the Norway rat Rattus norvegicus as a generalist species with highly flexible behaviour (Calhoun 1962; Whishaw and Kolb 2004). We show that the values of complexity of hunting behaviours in the first two species are rather close, and both differ essentially from the third one. This enables us to conclude that the striped field mouse is an advanced insect hunter and argue about the adaptive value of this behaviour for a small rodent. 

acta ethol (2017) 20:165–173 

167 

## Material and methods 

Reznikova et al. (2012), that is, ‘a relatively stable chain of ’ behavioural elements . 

## Animals and housing 

The experiment was conducted in the laboratory on three species of small mammals. We used 81 non-pedigree Norway rats (41 females and 40 males), 26 striped field mice (13 females and 13 males), and 11 common shrews (7 females and 4 males). Out of the 26 mice, 6 females and 3 males were born in the laboratory being the progeny of the wild-caught mice, while 10 males and 7 females, as well as all of the shrews, were captured in the mixed-pine forest near Novosibirsk. All animals were of different ages. 

Rats were housed in plastic cages (40 × 30 × 60 cm) containing cotton nesting material, 3–4 individuals per cage. Striped field mice and common shrews were housed singly in clear plastic cages (40 × 30 × 20 cm) that contained cotton nesting material. The light/dark cycle was 16:8. All animals were fed each day once, and they had ad libitum access to water. Striped field mice and rats received mixed seeds, fruits, and dried shrimps, and rats also received pieces of boiled eggs. Common shrews received one imago and two larvae of the yellow mealworm beetle (Tenebrio molitor) every 2 h. It is worth to note that, in contrast with the majority of studies of hunting behaviour in small rodents, in which animals have to go through a period of fasting before being used in experiments (Sadowska et al. 2008, 2015), our animals were provided with all types of food before being taken into experimental arenas. 

## Experimental procedures 

We investigated the process of hunting in small mammals using the lobster cockroach, Nauphoeta cinerea (27.93 ± 0.22 mm) as a live mobile prey. We placed each animal in a separate Noldus arena: 45 × 45 × 50 cm for the rats and 30 × 30 × 35 for the other two species. The arena was covered with a transparent lid in order to prevent animals from getting out. In each trial a cockroach was placed into the arena 5 min after the vertebrate animal. Video recordings were made using a Sony Handycam DCR-SR68 camera (frame rate, 25 frames per second) for rats and mice, and Sony HDR-AS200V (60 frames per second) for shrews, fixed on a tripod attached to a mobile platform in a way which allowed to keep the focal centre. Animals received three exemplars of cockroach in turn. In case of unsuccessful hunting, we were waiting for 10 min since the last contact between the animal and the prey, and then finished the observation. Each animal was tested only once. After each test, the arena was cleaned using 70% alcohol. We selected complete hunting stereotypes for the analysis, that is, those which ended with killing and eating the prey. Here we use the notion ‘stereotype’ as it is used in 

## Data encoding 

The alphabet for the analysis of hunting behaviours was devised based on the video records. Videos were slowed down 25 times from their normal speed, that is, with a temporal resolution of 1 frame per second for mice and rats and 2.4 for shrews. With the use of The Observer XT 10.1 (Noldus Information Technology), we selected behavioural elements, each including positions of different body parts: the head (h), forepaws (fl), fingers (ha), body (c), hind legs (hl), jaws (j), and the movements (mv). The position or the motion of different body parts is encoded using numerical indexes. For the head: calm, straight (0), outstretched forward (1), bent (2). For the forepaws: calm, touching the ground (0), raised straight (1), both stretched (2), calm, not touching the ground (3), one paw is stretched (4). For the fingers: fingers are not griping (0), fingers are griping (1). For the body: calm, straighten (0), stretched (1), bent (2), cranked laterally (3). For hind legs: calm, touching the ground (0), stretches, touching the ground (1), calm, not touching the ground (2). For jaws: calmly closed (0), clenched on the victim (1). Movements were denoted as follows: stop, freezing (0), quiet walking (1), run, trot (2), turn of the head (3), 90° turn (4), 180° turn (5), back movement (6). The choice of the letters bears no significance. The use of these indexes helps us to unify the description of hunting behaviour in such taxonomically distant species as shrews and rodents. 

We then encoded each behavioural element by a separate letter (again, the choice of the letters bears no significance), such as ‘W’ for biting, ‘E’ for capturing the prey by forepaws, ‘C’ for freezing, ‘S’ for quiet walking. Each letter includes several numerical indices describing the particular behavioural element as it can be observed. For example, ‘S’ (quiet walking) includes the following set of indexes: h-0 fl-0 ha-0 c-0 hl0 j-0 mv-1. Here h-0 corresponds to the quiet (natural) head position; fl-0 means that forepaws quietly touch the ground; ha-0 means fingers are not griped; c-0 means the body is calmly straightened; hl-0 means that hind legs quietly touch the ground; j-0 describes calmly closed jaws, while mv-1 describes walking as quiet and slow. In the case of several possible positions and movements of a particular body part, we separate them by a comma. Another example: the bite (W) includes the following set of indexes: h-0,1,2 fl-0,1 ha-0,1 c- 0,1,2 hl-0 j-1 mv-0,1,2. This means that the head can be quiet and calm (0), outstretched (1) and inclined (2); forepaws can touch the ground (0) or be raised straight (1) whereas fingers can be quiet (ha-0) or locked to grasp the prey (h-1); position of the body can be calmly straightened (с-0), outstretched (с1) and hunched (c-2); the animal can bite the victim in one of 

acta ethol (2017) 20:165–173 

168 

three positions: during stopping (0), slow walking (1), and running (2). 

Overall, we selected 19 behavioural elements and divided them into three groups (Table 1). The first one includes ‘key’ elements that are strongly necessary for accomplishing the hunting stereotype, such as bite (W), seizing an insect with forepaws (E) observed in rodents only (Fig. 1b, c), pursuing the prey by walking (S) or running (Q) (Fig. 1a). We considered both the initial biting to seize the prey and biting during handling as (W); series of biting as (WW) and (WWW) were possible as well. The second group includes ‘auxiliary’ elements related to the prey handling (R), sniffing (D), carrying the prey in the teeth (G), nibbling the insect’s legs (H), and pinning it down to the ground with one (N) or two (M) paws (the latter two elements were observed in shrews only). The third group consisted of the ‘noise’ elements which do not influence the performance of the stereotype at all: (C) freezing, (V) turning a body to 90, (B) U-turn, (F) turning a head, (Y) rearing against the wall, (I) free-standing rearing, (U) backwards movement, (X) self-grooming, and (J) jump (was observed only in shrews and striped field mice but not in rats). We included ‘J’ into the third group of elements because our animals do not jump at an insect; they just jump up on the spot. 

## Hypotheses testing 

The essence of the data compression method (Ryabko et al. 2013) is that we are trying to apply an adequate model which 

would allow for an assessment of certain characteristics of a text, while using a relatively small number of parameters. The degree of complexity of a ‘text’ could be estimated by its Kolmogorov complexity. Although Kolmogorov complexity is not algorithmically computable, it can be, in a certain sense, estimated by means of data compressors (Ryabko and Schmidhuber 2009). The compression-based method allows to combine the advantages of methods based on Kolmogorov complexity with classic methods of testing statistical hypotheses. This approach does not contradict the probabilistic one, because if one looks at a sequence as generated by a stochastic process, the length of the compressed sequence can be considered an estimate of the Shannon entropy of the process, which, in turn, equals Kolmogorov complexity of a typical sequence. 

We consider the two following hypotheses: H0 = {the sequences from both sets are generated by one source} and H1 = {the sequences from the different sets are generated by stationary and ergodic sources with different Kolmogorov complexities per letter of generated sequences}. Specifically, this can be done as follows: (1) from the sequences to be compared fragments (x1...xt) of equal length t are selected randomly so that the Mann–Whitney–Wilcoxon test can be applied to the resulting fragments; (2) the complexity of each fragment is defined as K(x1...xt) = |ϕ(x1...xt)| / t, where ϕ is a data compressor, and |ϕ(x1...xt)| is the length of the fragment of the sequence compressed by the data compressor; (3) applying the Mann–Whitney–Wilcoxon test, we test the hypothesis H0. To test the hypotheses, we should represent the sequence of 

Table 1 An ‘alphabet’ consisting of elements of hunting patterns in the three species of small mammals 

|Symbols|Behavioural elements|Sets of indexes|
|---|---|---|
|Q|Running|h-0 fl-0 ha-0 c-0 hl-0 j-0 mv-2|
|S|Walking|h-0 fl-0 ha-0 c-0 hl-0 j-0 mv-1|
|W|Bite|h-0,1,2 fl-0,1 ha-0,1 c-0,1,2 hl-0 j-1 mv-0,1,2|
|E|Capturing the prey by forepaws|h-0,1 fl-2 ha-1 c-0,1 hl-0 j-0 mv-0,1,2|
|R|Handling|h-0,2 fl-1 ha-1 c-2 hl-0 j-0 mv-0|
|H|Nibbling insects’legs|h-2 fl-0,1 ha-0,1 c-0,2 hl-0 j-0,1 mv-0|
|G|Carrying the prey in teeth|h-0 fl-0 ha-0 c-0 hl-0 j-1 mv-1,2|
|D|Sniffing|h-0,1 fl-0,1 ha-0 c-0,1 hl-0 j-0 mv-0,1,2,3|
|N|Pinning the prey down to the ground by one paw|h-0,1 fl-2 ha-4 c-0,1 hl-0 j-0 mv-0|
|M|The same, by two paws|h-0,1 fl-2 ha-2 c-0,1 hl-0 j-0 mv-0|
|C|Freezing|h-0 fl-0,1 ha-0,1 c-0,2 hl-0 j-0 mv-0|
|V|Turning a body to 90°|h-0,1 fl-0 ha-0 c-3 hl-0 j-0 mv-4|
|B|U-turn|h-0,1 fl-0 ha-0 c-3 hl-0 j-0 mv-5|
|F|Turning a head|h-0 fl-0,1 ha-0,1 c-0,2 hl-0,1 j-0 mv-0|
|Y|Rearing against the wall|h-0,1 fl-2 ha-0 c-1 hl-1 j-0 mv-0|
|U|Backwards movement|h-0,2 fl-0,1 ha-0 c-2 hl-0 j-0 mv-6|
|X|Self-grooming|h-2 fl-1 ha-0 c-2 hl-0 j-0 mv-0|
|J|Jump|h-0,2 fl-3 ha-0 c-0 hl-2 j-0 mv-0|
|I|Free-standing rearing|h-0,1 fl-1 ha-0 c-1 hl-1 j-0 mv-0|



acta ethol (2017) 20:165–173 

169 

**==> picture [427 x 167] intentionally omitted <==**

Fig. 1 A rat pursuing the prey by running (a) and seizing an insect with its paws (c). A striped field mouse (b) and a common shrew (d) seizing the prey 

symbols as text files. Then these text files should be compressed by the chosen data compression method. The level of compression corresponds to the ratio between the length of the file after and before the compression. The difference between compression ratios of files to be compared reflects the difference between complexities of the symbol sequences recorded. So we can use the compression ratio as a characteristic of complexity (see details in Ryabko et al. 2013). The possibility to compress information realised by different data compressors is highly dependent on the chosen method of compression, that is, on the algorithm used to find regularities in the file to be compressed. The more regularities, the compression method used can spot, the better is the compression and thus the smaller is the estimated complexity of the text in the compressed file and, finally, the more powerful is the resulting method. There are many lossless data compressors applicable to texts, for example, WinRAR, WinZip, 7-zip, and PeaZip. A data compressor can fail to spot any regularities within a file to be compressed in case its size is too small, as well as in the case the alphabet is too large relative to the volume. The level of compression of such a file will be greater than or equal to 1: the auxiliary data added to the compressed file by the compressor make the file larger, which may result in the compressed file being larger than the original. We have chosen the open-source data compressor 7-zip v.9.2.0 (32 bit), which uses the method of data compression called Bzip2, (compressed file format .bz2). This version was kept stable since 2010. The parameters used in the graphical user interface (GUI) were the following: compression level— normal; dictionary size—100 kb; number of CPU threads—4. It is worth noting that using a weak data compressor, that is, a one that cannot spot fewer regularities, results in a lower power of the test. It means that in such a case, H0 can be chosen where H1 should have been; however, the opposite probably cannot happen with a probability higher than the pre-specified level, no matter how bad the data compressor is. 

## Constructing sequences for hypothesis testing 

Overall, 17 striped field mice, 11 common shrews, and 42 Norway rats displayed completely successful hunting behaviour. In order to equalise the numbers of hunting animals to compare, we randomly chose 21 individuals out of 42 hunting rats. Using The Observer XT and the alphabet consisting of behavioural elements, we obtained sequences of letters of the c o m p l e t e h u n t i n g s t e r e o t y p e s , s u c h a s SWWHNWWNWWW, QWWWWWWWWWW, or YWWVQWBBWWWNWWWWWWWWWHWWWH. 

We copied all blank-separated sequences obtained into text files, each file for each of the three species. Thus we obtained three resulting files: one for each species. In order to obtain text fragments of equal length, a special program has been written which randomly chooses sequences from the resulting files and copied them into separate text files, each 200 bytes in size. We entered (input) a resulting file (.txt) containing letters corresponding to behavioural acts, and the output included 200 bytes files composed of several behavioural sequences taken from the resulting file and divided by a blank. For example, one of the text files included six behavioural sequences (195 symbols) and five blanks. The number of files in the output depends on the size of the initial file. We obtained eight files for Norway rats, seven files for striped field mice, and four files for common shrews, in such a way that each sequence would not be copied twice, that is, it would appear in one file only. 

## Results 

## Hunting activity 

In our experiments, 42 out of 81 Norway rats, 17 out of 26 striped field mice, and all 11 common shrews demonstrated complete hunting stereotypes that ended with killing the prey. 

acta ethol (2017) 20:165–173 

170 

As it was noted before, we randomly chose 21 out of 42 rats. In total, we selected 63 stereotypes of rats, 45 of striped field mice, and 33 of shrews to be included into three resulting files for three species. The volumes of these resulting text files (as described above) were 1662, 1527, and 807 bytes correspondingly. Stereotypes are longer in mice (32.95 ± 2.81 behavioural elements) than in rats (25.39 ± 2.57 elements) and shrews (23.48 ± 3.05); the difference is significant according to the Student criterion: t = 1.984, P < 0.05; t = 2.281, P < 0.05. This means that from three species compared, the common shrew possesses the most succinct hunting stereotype. 

Nearly all behavioural elements of hunting stereotypes turned out to be common for all the three species, with a few differences. We never observed jumps (J) and free-standing rearing (I) in rats, only in striped field mice and common shrews. As distinct from mice and rats, shrews never seized the prey with their forepaws but only with their teeth, so the elements ‘E’ and ‘R’ were absent in the shrews’ hunting stereotype. The elements ‘M’ and ‘N’ (pinning the prey down to the ground with one or two forepaws) were observed only in shrews, and not in mice and rats. It is worth to note that striped field mice and Norway rats, although they used their teeth to snap the insect much more frequently, sometimes caught the prey with forepaws (E) and then bit it (W) (Fig. 1). Rats seized the prey with their paws in 15% of cases of pursuing, and striped field mice did so in 14% of the cases. When starting the attack by seizing the prey with their teeth (85% in mice and 80% in rats), rodents immediately set their paws at work. Norway rats usually bite the insect once and then capture the prey with their paws and handle it (R), rotating the live cockroach, biting it many times and nibbling the insect’s legs (H). Rats are trying to eat the struggling prey and sometimes drop it and catch it again. In contrast, striped field mice first quickly kill the insect by a series of bites (WWW) and then hold it with their paws and proceed to eating. 

In Norway rats the proportion of key elements constitutes 66.7% (1069 out of 1600), 24.2% (387) are ‘auxiliary’, and 7.1% (114) belong to the ‘noise’ group. The corresponding values in striped field mice are as follows: 86% (1276 out of 1483), 8.3% (122), and 5.7% (85), and in common shrews they are, correspondingly, 74.8% (580 out of 775), 19.5% (151), and 5.7% (44). The proportion of key elements in shrews’ hunting stereotypes is higher than in rats (Fisher’s exact test, P < 0.005), and, what is more interesting, smaller than in striped field mice; the proportion of ‘auxiliary’ elements in shrews’ hunting stereotypes is smaller than in rats (P < 0.005) and higher than in striped field mice. The proportion of ‘noise’ elements does not differ significantly in all three species. 

We compared ‘rates of hunting’ in the three species, that is, relations between the length of stereotypes (expressed in the number of elements) and their duration in seconds (Fig. 2). 

**==> picture [186 x 139] intentionally omitted <==**

Fig. 2 Rates of hunting in three species: relations between the length of stereotypes (expressed in numbers of elements) and their duration in seconds. The figure shows mean ± SEM. Student’s t test: *P < 0.05. **P < 0.01 

Shrews displayed a greater rate of hunting than rats (t test, t = 9.075, P < 0.01) and than striped field mice (t test, t = 2.197, P < 0.05); however, the rate of hunting in rats is less than in mice (t test, t = 7.879, P < 0.01). 

## Complexities of hunting stereotypes 

As noted before, the compression ratios of sequences can be considered characteristic of the complexity of the files being compressed. As can be seen from Fig. 3, compression ratios in the field striped mouse (the average value 0.596) and the common shrew (0.59) are similar (Uemp. = 12.5, Ucr. = 1, P = 0.774), and they differ significantly from the compression ratio in the Norway rat (0.631): Uemp. = 4, Ucr. = 5, P = 0.041 for rats and shrews and Uemp. = 7, Ucr. = 8, P = 0.02 for rats and striped field mice. 

In order to understand which factors underlie the differences in compression ratios of files containing hunting stereotypes of the three species, we investigated the characteristics of these files and the correlation of these characteristics with the compression ratio by means of Pearson correlation coefficient. The following characteristics were chosen: (1) the 

**==> picture [186 x 138] intentionally omitted <==**

Fig. 3 Differences between the compression ratios of behavioural sequences in three species. The figure shows mean ± SEM. Mann– Whitney U test: * P < 0.05 

acta ethol (2017) 20:165–173 

171 

Table 2 Values of Pearson coefficient (r) for compression ratios and different characteristics of hunting stereotypes, represented as sequences of symbols in 200 bytes (.txt) files 

|Characteristics of files|File volume 200|
|---|---|
||(bytes)|
|Number of stereotypes|0.019|
|Number of behavioural elements|0.012|
|Proportion of‘W’(bite) in stereotypes|−0.676**|
|Proportion of‘key’behavioural elements in|−0.693**|
|stereotypes||
|Proportion of‘auxiliary’elements|0.527*|
|Proportion of‘noise’elements|0.780**|



*P < 0.05; ** P < 0.01 

number of stereotypes being written in the file; (2) the number of behavioural elements; (3) the proportion of ‘key’, ‘auxiliary’, and ‘noise’ elements; and the (4) parts of ‘bites’ (W). As can be seen from Table 2, there is a negative correlation between the ratio of compression and the proportions of key behavioural elements within stereotypes, as well as with the total number of elements, and a positive correlation between the proportion of ‘auxiliary’ and ‘noise’ elements and the ratio of compression. 

One can suggest that the greater complexity of rats’ hunting behavioural stereotypes may be caused by the smaller proportion of ‘key’ elements and the higher proportion of ‘noise’ elements in comparison with common shrews and striped field mice. The high similarity between the levels of complexity of hunting stereotypes in mice and shrews is possibly caused by the predominance of ‘key’ elements over ‘auxiliary’ and ‘noise’ ones as well as greater lengths of hunting stereotypes in both species. 

## Discussion 

In our laboratory experiments, striped field mice displayed hunting behaviour typical for pursuit predators, and they used a detection and pursuit phase at least over a short distance in order to obtain insect prey. Among small rodents, skilful attacks towards insects have been described before mainly in Cricetidae, such as grasshopper mice of the genus Onychomys, deer mice of the genus Peromyscus (Timberlake and Washburne 1989; Langley 1994), the golden hamster Mesocricetus auratus (Polsky 1977; Gattermann et al. 2001), and some others. In contrast to the grasshopper mouse, which possesses numerous morphological and physiological specialisations for predation (Sarko et al. 2011), the striped field mouse displays only behavioural adaptations to the carnivorous lifestyle (Panteleeva et al. 2013). Similar results have been obtained on the bank vole Myodes glareolus, an omnivorous species, which demonstrated an unexpected 

hunting potential while lacking morphological adaptations (Sadowska et al. 2008, 2015). 

In order to evaluate similarities between hunting stereotypes of the granivorous, the insectivorous, and the generalist species, we suggest the data compression method (Ryabko et al. 2013) as an easy tool for comparative analysis of behaviours between and within species and groups of individuals. This method allows to spot undetectable regularities which can influence the complexity of behavioural sequences and then to proceed with searching for explanations of similarities and differences in behaviours. 

In our study, the Norway rat demonstrated the highest level of complexity of hunting behaviour among the three species compared. This reflects the high variability of rats’ reactions to live prey. What we found especially interesting is the high similarity between the levels of complexity of hunting stereotypes in such a specialised insectivorous predator as the common shrew and in the striped field mouse. As far as we know, this is the first evidence of similarity between hunting behaviours in the members of Muridae and Soricidae. 

The comparison of several characteristics of behavioural sequences suggests that the high complexity of hunting stereotype in the Norway rat may be caused by the high proportion of ‘auxiliary’ and ‘noise’ elements and relatively low proportion of ‘key’ elements in their behaviours, whereas predominance of ‘key’ elements over ‘auxiliary’ and ‘noise’ ones results in similarly low levels of complexity of hunting stereotypes in striped field mice and shrews. One can conclude that hunting behaviour is highly stereotypic in both species. 

The obtained results on similarities between succinct and highly predictable hunting stereotypes of the insectivorous shrew and the striped field mouse enable us to argue about evolutionary roots of hunting behaviour in small mammals. It is likely that granivorous A. agrarius share hunting stereotypes with specialised predatory rodents, possibly inheriting these behaviours from common ancestors. It is possible that the highly specific hunting behavioural pattern in the striped field mouse may be a specific adaptation, which allows this species to switch to live prey and thus broaden its food resources. 

## Conclusion 

The striped field mouse A. agrarius can be considered an advanced ‘hunter’ among Muridae. This species displays behaviours typical for pursuit predators, using a detection and pursuit phase at least over short distance in order to obtain insect prey. The compression-based method aimed at the comparison of the ethograms as biological ‘texts’ revealed a similarity between hunting stereotypes in the striped field mouse and such а specialised predator as the common shrew. Both species essentially differ from the generalist Norway rat. The method allows us to spot unevident regularities which can 

acta ethol (2017) 20:165–173 

172 

influence the complexity of behavioural sequences and then to proceed with searching for explanations of similarities and differences in behaviours. Norway rats demonstrated the highest level of complexity of hunting behaviour, which could be caused by the higher proportion of ‘auxiliary’ and ‘noise’ elements and relatively low proportion of ‘key elements in their behaviours. On the other hand, the predominance of ‘key’ elements over ‘auxiliary’ and ‘noise’ ones resulted in similarly low levels of complexity of hunting stereotypes in striped field mice and shrews. The similarity between succinct and easily predictable hunting stereotypes of the insectivorous shrew and the granivorous striped field mouse suggests that a highly specific hunting behavioural pattern in A. agrarius allows this species to broaden its trophic niche. 

Acknowledgements The study was supported by the Russian Fund for Basic Research (No. 17-04-00702). We are grateful to Daniil Ryabko for the helpful discussion and useful comments. We thank Maxim Novikov and Danil Reusov for writing auxiliary programs for handling the data. 

## References 

- Babińska-Werka J, Gliwicz J, Goszczyński J (1981) Demographic processes in an urban population of the striped field mouse. Acta Theriol 26:275–283 

- Bateson P, Martin PR (1999) Design for a life: how behaviour develops. Jonathan Cape, London 

- Beecher MD (1989) Signalling systems for individual recognition: an information theory approach. Anim Behav 38:248–261 

- Calhoun JB (1962) The ecology and sociobiology of the Norway rat. Public Health Service Publication, Washington D.C., p 288 

- Casarrubea M, Sorbera F, Crescimanno G (2009) Multivariate data handling in the study of rat behavior: an integrated approach. Behav Res Methods 41:772–781. doi:10.3758/BRM.41.3.772 

- Casarrubea M, Jonsson GK, Faulisi F, Sorbera F, Di Giovanni G, Benigno A, Benigno A, Crescimanno G, Magnusson MS (2015) T-pattern analysis for the study of temporal structure of animal and human behavior: a comprehensive review. J Neurosci Methods 239:34–46. doi:10.1016/j.jneumeth.2014.09.024 

- Churchfield S, Rychlik L, Taylor JR (2012) Food resources and foraging habits of the common shrew, Sorex araneus: does winter food shortage explain Dehnel’s phenomenon? Oikos 121:1593–1602. doi:10. 1111/j.1600-0706.2011.20462.x 

- Fedderwitz F, Björklund N, Ninkovic V, Nordlander G (2015) The structure of feeding behavior in a phytophagous insect (Hylobius abietis). Entomologia Experimentalis et Applicata 155:229–239. doi:10. 1111/eea.12302 

- Forrester GS (2008) A multidimensional approach to investigations of behaviour: revealing structure in animal communication signals. Anim Behav 76:1749–1760. doi:10.1016/j.anbehav.2008.05.026 

- Gammie SC, Hasen NS, Rhodes JS, Girard I, Garland T (2003) Predatory aggression, but not maternal or intermale aggression, is associated with high voluntary wheel-running behavior in mice. Horm Behav 44:209–221 

- Gattermann R, Fritzsche P, Neumann K, Al-Hussein I, Kayser A, Abiad M, Yakti R (2001) Notes on the current distribution and the ecology of wild golden hamsters (Mesocricetus auratus). J Zool 254:359– 365. doi:10.1017/S0952836901000851 

- Gauvrit N, Zenil H, Delahaye JP, Soler-Toscano F (2014) Algorithmic complexity for short binary strings applied to psychology: a primer. Behav Res Methods 46:732–744. doi:10.3758/s13428-013-0416-0 

- Kershenbaum A, Blumstein DT, Roch MA et al (2014) Acoustic sequences in non-human animals: a tutorial review and prospectus. Biol Rev. doi:10.1111/brv.12160 

- Landry SO (1970) The Rodentia as omnivores. Q Rev Biol 45:351–372 

- Langley WM (1994) Comparison of predatory behaviors of deer mice (Peromyscus maniculatus) and grasshopper mice (Onychomys leucogaster). J Comp Psychol 108:394 

- MacNulty DR, Mech LD, Smith DW (2007) A proposed ethogram of large-carnivore predatory behavior, exemplified by the wolf. J Mammalogy 88:595–605. doi:10.1644/06-MAMM-A-119R1.1 

- Magnusson MS (2000) Discovering hidden time patterns in behavior: T- patterns and their detection. Behav Res Methods 32:93–110. doi:10. 3758/BF03200792 

- Martin PR, Bateson P (1993) Measuring behaviour: an introductory guide. Cambridge University Press, Cambridge 

- McCowan B, Doyle LR, Hanser SF (2002) Using information theory to assess the diversity, complexity, and development of communicative repertoires. J Compar Psychol 116:166. doi:10.1037/0735-7036. 116.2.166 

- Oller DK, Griebel U (2008) Evolution of communicative flexibility: complexity, creativity, and adaptability in human and animal communication. MIT Press (MA), London 

- Panteleeva S, Reznikova Z, Vygonyailova O (2013) Quantity judgments in the context of risk/reward decision making in striped field mice: first Bcount,^ then hunt. Front Psychol 4:53. doi:10.3389/fpsyg. 2013.00053 

- Pollard KA, Blumstein DT (2012) Evolving communicative complexity: insights from rodents and beyond. Philosophical Transactions of the Royal Society of London B: Biological Sciences 367:1869–1878. doi:10.1098/rstb.2011.0221 

- Polsky RH (1977) The ontogeny of predatory behaviour in the golden hamster (Mesocricetus A. auratus). I. The influence of age and experience. Behaviour 61:26–56. doi:10.1163/156853977X00478 

- Reznikova Z (2007) Animal intelligence: from individual to social cognition. Cambridge University Press, Cambridge 

- Reznikova Z, Panteleeva S, Danzanov Z (2012) A new method for evaluating the complexity of animal behavioral patterns based on the notion of Kolmogorov complexity, with ants’ hunting behavior as an example. Neurocomputing 84:58–64. doi:10.1016/j.neucom.2011. 12.019 

- Ryabko B, Reznikova Z (1996) Using Shannon entropy and Kolmogorov complexity to study the communicative system and cognitive capacities in ants. Complexity 2:37–42 

- Ryabko D, Schmidhuber J (2009) Using data compressors to construct order tests for homogeneity and component independence. Appl Math Lett 22:1029–1032. doi:10.1016/j.aml.2008.01.008 

- Ryabko B, Reznikova Z, Druzyaka A, Panteleeva S (2013) Using ideas of Kolmogorov complexity for studying biological texts. Theory of Computing Systems 52:133–147. doi:10.1007/s00224-012-9403-6 

- 

- Saarikko J (1989) Foraging behaviour of shrews. Ann Zool Fenn 26:411 423 

- Sadowska ET, Baliga-Klimczyk K, Chrząścik KM, Koteja P (2008) Laboratory model of adaptive radiation: a selection experiment in the bank vole. Physiol Biochem Zool 81:627–640. doi:10.1086/ 590164 

- Sadowska ET, Stawski C, Rudolf A et al (2015) Evolution of basal metabolic rate in bank voles from a multidirectional selection experiment. Proc Biol Sci 282:20150025. doi:10.1098/rspb.2015.0025 

- Sarko DK, Leitch DB, Girard I, Sikes RS, Catania KC (2011) Organization of somatosensory cortex in the northern grasshopper mouse (Onychomys leucogaster), a predatory rodent. J Comp Neurol 519:64–74. doi:10.1002/cne.22504 

acta ethol (2017) 20:165–173 

173 

- Timberlake W, Washburne DL (1989) Feeding ecology and laboratory predatory behavior toward live and artificial moving prey in seven rodent species. Anim Learn Behav 17:2–11. doi:10.3758/ BF03205206 

- Tinbergen N (1951) The study of instinct. Oxford University Press, London 

   - Whelton JP, O’Boyle M (1977) Early experience and the development of predatory and intraspecific aggression in mice. Anim Learn Behav 5:291–296 

   - Whishaw IQ, Kolb B (2004) The behavior of the laboratory rat: a handbook with tests. Oxford University Press. doi:10.1093/acprof:oso/ 9780195162851.001.0001 

- Vogel P (1976) Energy consumption of European and African shrews. Acta Theriol 21:195–206 

