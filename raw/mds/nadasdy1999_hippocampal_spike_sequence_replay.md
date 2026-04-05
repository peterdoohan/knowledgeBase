The Journal of Neuroscience, November 1, 1999, _19_ (21):9497–9507 

# **Replay and Time Compression of Recurring Spike Sequences in the Hippocampus** 

## **Zolta´ n Na´ dasdy, Hajime Hirase, Andra´ s Czurko´ , Jozsef Csicsvari, and Gyo¨ rgy Buzsa´ ki** 

_Center for Molecular and Behavioral Neuroscience, Rutgers, The State University of New Jersey, Newark, New Jersey 07102_ 

Information in neuronal networks may be represented by the spatiotemporal patterns of spikes. Here we examined the temporal coordination of pyramidal cell spikes in the rat hippocampus during slow-wave sleep. In addition, rats were trained to run in a defined position in space (running wheel) to activate a selected group of pyramidal cells. A template-matching method and a joint probability map method were used for sequence search. Repeating spike sequences in excess of chance occurrence were examined by comparing the number of repeating sequences in the original spike trains and in surrogate trains after Monte Carlo shuffling of the spikes. Four different shuffling procedures were used to control for the population dynamics of 

hippocampal neurons. Repeating spike sequences in the recorded cell assemblies were present in both the awake and sleeping animal in excess of what might be predicted by random variations. Spike sequences observed during wheel running were “replayed” at a faster timescale during single sharpwave bursts of slow-wave sleep. We hypothesize that the endogenously expressed spike sequences during sleep reflect reactivation of the circuitry modified by previous experience. Reactivation of acquired sequences may serve to consolidate information. 

_Key words: sharp waves;_ � _; memory; coding; decoding; retrieval; network; sleep_ 

Although it is a widely accepted notion that information is distributed in cell assemblies rather than encoded by single cells, the nature of coding in cell assembly has remained a major challenge for neuroscience research. Several explanations have been proposed on theoretical grounds, including frequency coding (Sherrington, 1906; Eccles, 1957; Barlow, 1972; Georgopoulos et al., 1982), temporal coincidence coding (von der Malsburg and Bienenstock, 1986; Singer, 1993), temporal delay of spikes (O’Keefe and Recce, 1993; Buzsa´ki and Chrobak, 1995; Hopfield, 1995; Lisman and Idiart, 1995; Skaggs et al., 1996), and spatiotemporal spike sequence coding (Buzsa´ki, 1989; Abeles, 1991). If spatiotemporal patterns of neural activities serve to code and/or decode information, one could look for evidence in the temporal structure of activity within neuronal ensembles. Temporal coordination of spike sequences, in relation to stimulus presentation, has been described in various invertebrate (Dayhoff and Gerstein, 1983; Laurent et al., 1996; Marder and Calabrese, 1996) and vertebrate (Strehler and Lestienne, 1986; Ts’o et al., 1986; Vaadia and Abeles, 1987; Eckhorn et al., 1988; Gray and Singer, 1989; Frostig et al., 1990b; Aertsen et al., 1991; Abeles et al., 1993; Riehle et al., 1997) brains. 

Because hippocampal pyramidal neurons discharge selectively at certain spatial locations [“place” cells (O’Keefe and Nadel, 1978)], it is expected that they are activated sequentially while the 

Received May 24, 1999; revised Aug. 13, 1999; accepted Aug. 16, 1999. 

This work was supported by National Institutes of Health Grants NS34994 and MH54671 and by the Human Science Frontier Program. We thank Moshe Abeles, Michale Fee, Stuart Geman, Stephen Hanson, Darrell Henze, Gu¨nther Palm, Michael Recce, and Matthew Wilson for their suggestions with data analysis and comments on this manuscript. 

Correspondence should be addressed to Dr. Gyo¨rgy Buzsa´ki, Center for Molecular and Behavioral Neuroscience, Rutgers University, 197 University Avenue, Newark, NJ 07102. E-mail: buzsaki@axon.rutgers.edu. Dr. Na´dasdy’s present address: Department of Physiology, The Hebrew University of Jerusalem, Jerusalem, 91120 Israel. Copyright © 1999 Society for Neuroscience 0270-6474/99/199497-11$05.00/0 

animal moves about in a structured environment (Wilson and McNaughton, 1994; Skaggs and McNaughton, 1996; Brown et al., 1998; Zhang et al., 1998). During sleep, on the other hand, there is no external perceptual reference or motor behavior to drive hippocampal cells. Therefore, if recurring spike sequences are present during sleep, they are likely to be internally generated. In a previous study, Pavlides and Winson (1989) examined pairs of putative pyramidal cells recorded by the same single wire. When one of the neurons in the pair was activated by confining the rat to the spatial field of the unit, the firing rate of the neuron during the subsequent sleep epoch increased relative to that of its pair. A more recent study, however, failed to confirm the relationship between firing rates in the awake and sleeping rat (Wilson and McNaughton, 1994). On the other hand, neuron pairs, which represented similar parts of the environment in the awake rat and therefore fired together during exploration, showed an increased correlation in their firing during the subsequent slow-wave sleep episode compared with the preceding sleep episode (Wilson and McNaughton, 1994; Skaggs and McNaughton, 1996). Pairwise cross-correlograms, however, are not sufficient to analyze the exact temporal structure of more than two cells (Hampson et al., 1996; McNaughton et al., 1996; Moore et al., 1996; Quirk and Wilson, 1998). 

Here we examined the spatiotemporal firing patterns of hippocampal CA1 principal neurons in awake and sleeping rats. Spatiotemporal sequences of spike patterns were detected either by a template-matching method or by the joint probability mapping of spikes. The results indicate that repeating spike sequences are present in both the awake and sleeping animal in excess of what is predicted by random coincidences. Furthermore, the spike sequences observed in the behaving rat were “replayed” at a faster timescale during sharp-wave bursts of slow-wave sleep. 

Parts of this paper have been published previously (Nadasdy et al., 1996, 1997, 1998). 

**9498** J. Neurosci., November 1, 1999, _19_ (21):9497–9507 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

**==> picture [503 x 330] intentionally omitted <==**

_Figure 1._ Spike sequence extraction methods. _Panel a,_ Unit activity was recorded simultaneously from multiple tetrodes. Filtered recordings from a single tetrode are shown ( _Ch1–Ch4_ ). _Panel c_ , Spike sorting resulted in 4–8 neurons/tetrode. _Panel b_ , Superimposed waveforms of a single cell are shown _. Panel d,_ The parallel spike train ( _vertical tics_ ; cells 0–4) was analyzed by a sequence-search algorithm for repeating spike sequences. All possible sequences were considered as a template. The duration of the template window ( _w_ ) was typically 200 msec. The tolerance of spike match (spike window; d _t_ ) was 10 or 20 msec. _Neur_ , Neuron. _Panel e_ , Spike sequences of neurons _a–d_ are represented as spatiotemporal vectors. For graphical illustrations, repeating sequences are superimposed in subsequent figures. _Panel f_ , The significance of sequence repetition was tested by Monte Carlo statistics. _Panel g_ , Spike triplets were also detected by the JPM method. The distribution of spike triplets ( _a_ , _b_ , _c_ ; � _tab_ , � _tac_ ) within the _w_ time window was investigated by constructing a joint peri-event time histogram. A difference map ( _Dij_ ) was created by subtracting chance combinations, as predicted by the corresponding spike doublets, from the joint peri-event time histogram. The pixels of the difference map (JPM) represent the probability of observing a given triplet. 

## **MATERIALS AND METHODS** 

The surgical procedures, electrode implantation, and spike sorting have been described in detail previously (Csicsvari et al., 1999). Briefly, wire tetrodes or silicon electrode arrays were implanted in the CA1 pyramidal layer of 18 Sprague Dawley rats. Electrical activity was recorded while the rat was in its home cage followed by exploration. Six rats were trained to run in a wheel for a water reward (Czurko et al., 1999). The apparatus was a 30 � 40 � 35 cm box with a glass front wall. The running wheel (10 cm wide; 29.5 cm in diameter) was attached to the side of the box. A drinking tube protruded from the back wall of the box 5 cm above the floor. Five to 20 turns of the wheel triggered an acoustic “go” signal, which indicated the availability of the water reward (Czurko et al., 1999). After the task is learned, the behavior is stereotypic: running in the wheel, approaching the waterspout, drinking, and returning to the wheel. In the trained rats, electrical activity was recorded during sleep in the home cage (session 1), followed by wheel running in an identical wheelrunning apparatus but in a different spatial location of the room (session 2) and a second recording session during sleep (session 3). Units were separated on the basis of their spike amplitude and waveform using principal component analysis and spatial clustering (Wilson and McNaughton, 1994; Na´dasdy et al., 1998; Csicsvari et al., 1999). Only pyramidal cells with clear cluster boundaries and �2 msec refractory periods were included in the analyses (Fig. 1). For the extraction of sharp-wave (SPW) ripple events during sleep, the wide-band recorded data were bandpass filtered digitally (150–250 Hz). The power (root mean 

square) of the filtered signal was calculated, and the beginning, peak, and end of individual ripple episodes were determined. The threshold for ripple detection was set to 7 SDs above the background mean power (Csicsvari et al., 1999). � epochs were detected by calculating the ratio of the � (5–10 Hz) and � (2–4 Hz) frequency bands in 2.0 sec windows. A Hamming window was used during the power spectra calculations. 

Neuronal spike times of simultaneously recorded neurons are referred to as the “parallel spike train.” For the detection of invariant temporal structures of spikes from parallel spike trains, two different methods were used: (1) the template-matching method and (2) the joint probability map method. Complex-spike bursts [�6 msec interspike intervals (Ranck, 1973)] were regarded as single events, represented by the time of the first spike. 

## _The template-matching method_ 

The template-matching method was a modified version of the “slidingsweeps” algorithm introduced by Gerstein and colleagues (Dayhoff and Gerstein, 1983; Abeles and Gerstein, 1988; Frostig et al., 1990a). The search for repeating spike sequences was performed within a specific time window, denoted as the template window _w_ (Fig. 1 _d_ ). The 0 point of a _w_ time window was assigned to a spike of the selected reference neuron. The temporal positions of _c_ spikes, detected from the spike train, within the _w_ time window were considered as a template. The _T_ template was represented by a temporal vector of _p_ neurons and _t_ spike positions relative to the _t_ (0) reference spike and the _c_ � 1 co-occurring spikes from 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

J. Neurosci., November 1, 1999, _19_ (21):9497–9507 **9499** 

the other spike trains: _T_ � ( _pi_ ; _tj_ ). Here _p_ denotes the different cells as _p_ � ( _pi_ , . . . , _pn_ ), where _n_ is the number of parallel-recorded cells, and _t_ � (� _tj_ , . . . , � _tc_ �1) denotes the corresponding intervals between the initial spike and subsequent spikes where � _tc_ �1 � _w._ Next, the template was shifted to successive spikes of the reference neuron throughout the recording session, and recurrences of the _T_ template were counted. During the search, each spike sequence was considered as an exemplar and compared with the _T_ template sequence. A match between the template and the exemplar was counted when spikes occurred within a predetermined time window d _T_ (or spike jitter; Fig. 1 _d_ ). The spike time window (d _T_ ) was set at 10 or 20 msec in most searches because in preliminary experiments the best separation between the real spike train and shuffled spike trains was observed using 10–20 msec spike windows (d _T_ was varied between 2.5 and 20 msec; _n_ � 2 rats). In each search, the template window ( _w_ ) and the spike window (d _T_ ) were set by the experimenter. The template window was typically set to 200 msec (Fig. 1 _d_ ). The dependent variables of the search were the number of spikes in a given template (sequence complexity), the number of different sequences ( _m_ ), and the number of repetitions of a given sequence ( _r_ ). During the search, every spike was considered as a part of a template sequence of _c_ complexity, each template occurred at least once, and the entire spike train was searched exhaustively by templates. The sequences were visualized as temporal vectors (Fig. 1 _e_ ). 

The statistical significance of the observed repetition of spike sequences was assessed by comparing the repetition of the original sequences ( _r_ orig) with the repetition of the pseudorandom sequences ( _r_ rnd) generated by spike shuffling. The null hypothesis was that the statistical distribution of _r_ orig is equal to that of _r_ rnd. We reasoned that if _r_ rnd of every possible sequence in 100 simulated spike trains is smaller than the _r_ orig, the null hypothesis can be rejected with _p_ � 0.01 probability (Fig. 1 _f_ ). In these comparisons, we assumed that in a shuffled parallel spike train with the same first-order statistics (firing rate and population covariance) as the original spike train, the number of repeating spike sequences should reflect chance occurrences. Spike shuffling thus served to eliminate the temporal correlation generated by an assumed biological mechanism. Four randomization procedures were applied. 

_Within-spike-train random shuffling._ Interspike intervals, derived from the original spike trains, were exchanged between two pseudorandomly selected positions from the first to the last interspike interval, and this procedure was iterated (Fig. 2 _b_ ). Within-spike-train shuffling preserves the average firing rates of individual cells. However, it can eliminate population synchrony among the simultaneously recorded spike trains, present during � and sharp-wave patterns. 

_Temporal displacement of spikes._ This procedure is similar, in principle, to the within-spike-train shuffling. However, in this procedure spikes were displaced temporally by adding a pseudorandom interval from 0 to 50 msec. This range was used because this temporal displacement was small enough to preserve population synchrony during both � and sharp waves (Fig. 2 _c_ ). 

_Across-spike-train shuffling._ Each spike of the spike trains was assigned to a pseudorandomly selected cell (Fig. 2 _d_ ). As a result, the population level modulation of the firing rate in the surrogate spike trains remained the same as in the original spike train. A caveat of this procedure is that the differences in discharge frequencies of individual spike trains, which may be present in the original spike trains, are reduced as a result of spike shuffling across trains. 

� _phase-invariant shuffling._ This procedure preserved the periodic modulation of discharge frequency both within and across the spike trains (see Fig. 5 _a_ ). First, the peaks of the field � waves were identified. Second, the spike times were converted to phases of the � cycle (Csicsvari et al., 1999). Third, the phase-encoded spikes within a given � cycle were exchanged with other pseudorandomly selected cycles within the same spike train. 

## _Joint probability map method_ 

Repeating spike triplets were detected by the joint peri-event time histogram method (JPTH) (Aertsen et al., 1989). The construction of a joint peri-event time histogram was restricted to spike triplets cooccurring within a _w_ time window. The histogram displayed the repetition of the same triplet at all interspike intervals. First, all possible _n_ !/( _n_ � 3)! variations of temporal orders of triplets were determined, where _n_ is the number of parallel spike trains. All triplets _T_ � ( _p_ 1, _p_ 2, _p_ 3; � _t_ 1, � _t_ 2) with � _t_ 1 �� _t_ 2 and _w_ � � _t_ 2 were registered and represented as pixels in a two-dimensional coordinate system at � _t_ 1 and � _t_ 2 as _x_ and _y_ coordinates, respectively. For the estimation of the spurious occurrence 

**==> picture [250 x 192] intentionally omitted <==**

_Figure 2._ Spike-shuffling methods. _Panel a,_ Original parallel spike train. Three repetitions of the same spike sequence (0, 1, 2, 3) are shown. _Panel b,_ Elimination of temporal correlation between the spikes by shuffling the interspike intervals ( _ISI_ ) within each spike train. _Gray tics_ indicate the original spikes. _Panel c,_ Spike displacement. Spikes of the original spike train ( _gray tics_ ) are randomly shifted in time by 0–50 msec (�t; _black tics_ ). Although the interspike intervals may change somewhat by this method, the field modulation of the neurons is better preserved. _Panel d,_ Shuffling of spikes across spike trains. This method preserves population modulation of spike timing but may reduce firing-rate differences between the original spike trains. A fourth method (phase-invariant spike shuffling) is illustrated below (see Fig. 5). 

of triplets, the cross products of the (neuron1 neuron2), (neuron1 neuron3), and the (neuron2 neuron3) cross-correlograms were constructed and normalized by the total number of observed triplets (Fig. 1 _g_ ). The histogram of expected triplets was subtracted from the histogram of observed triplets, resulting in a histogram of unexpected triplets [difference map or joint probability map (JPM)]. Each pixel of the JPM was tested with the Fisher’s exact probability test (Frostig et al., 1990a,b). To reduce the error inherent in repeated comparisons, the exact probability was multiplied by the number of pixels of the JPTH. The difference map is referred to as the JPM. Similar JPMs were constructed also from all shuffled surrogate trains. In the next step, the incidences of significant pixels in the JPM of the original and shuffled trains were compared statistically. Again, we assumed that if the number of significant triplets in 100 simulated spike trains is smaller than the observed number of triplets in the original spike train, the null hypothesis can be rejected with _p_ � 0.01 probability. Because of the behavior-dependent time compression of spike sequences (see Results), the temporal information between spikes was discarded for this analysis. 

## _Clustering artifacts_ 

The reliable identification of spikes with individual neurons is a prerequisite for sequence detection. False clustering can cause the dispersion of single-unit activity to different clusters, and the spike train will be erroneously decomposed to different spike trains. A potential source of false clustering is the amplitude variation of extracellular units (Quirk and Wilson, 1998). As a consequence, temporal regularities of action potentials of a single neuron would lead to spuriously recurring multipleunit spike sequences in parallel spike trains. The potential contribution of such an artifactual cause of the repeating spike sequences was tested by dividing the original clusters into small-amplitude and largeamplitude subclusters. As a result, the firing rate was reduced by 50% in each of the newly created trains. According to the formula of Abeles and Gerstein (1988), the number of spurious spike sequences should decrease exponentially as a function of spike count. In contrast, we found that the number of different sequences and the number of recurring sequences decreased only slightly less than one-half, indicating that spike amplitude variation cannot account for the repeating spike sequences. It is important to emphasize that only well-identified spike clusters with clear boundaries and refractory periods (Csicsvari et al., 1999) were included 

**9500** J. Neurosci., November 1, 1999, _19_ (21):9497–9507 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

in this study. In another approach, spikes that were part of the detected spikes sequences were highlighted in the original unit clusters. The rationale of this approach was that if spike sequences result as a consequence of poor clustering, spikes of the detected sequences should either reside near the cluster borders or coincide with small-amplitude spikes. This backprojection method, however, clearly revealed that spikes that were part of sequences were evenly distributed in the cluster clouds of spikes. 

## _Computation_ 

The sequence search, spike train shuffling, and the Monte Carlo statistics were run on an IBM SP2 scalable parallel computer with six nodes of RS/6000, 120 MHz P2SC processors (IBM, White Plains, NY), on a Silicon Graphics Onix2 with a 120 MHz MIPS R10000 processor (Silicon Graphics, Mountain View, CA), and on a Sun Enterprise with two UltraSPARC processors (Sun Microsystems, Palo Alto, CA). Identification of repeating spike sequences in a 10-min-long file, containing five parallel spike trains, typically required 175 min (Onix2) or 12.5 hr (SP2) of central processing unit time. The complete hypothesis testing of a single data set, including the generation of 100 surrogates and the sequence search, required 175 � 101 � 17,675 min (294.6 hr or �12 d) on the Onix2. 

## **RESULTS** 

The most prominent slow-wave sleep pattern in the hippocampus is an irregularly occurring population burst of pyramidal cells, associated with an SPW in the stratum radiatum and fast (150– 200 Hz) field oscillation in the pyramidal layer of the CA1 region. Population activity of pyramidal cells between SPW events is relatively quiescent (Csicsvari et al., 1999). The long-term firing rates of pyramidal cells were similar during � (1.4 � 0.10 Hz) and non-� (1.4 � 0.09 Hz) behaviors. However, during SPW events, the firing rates of pyramidal cells increased by sevenfold (Csicsvari et al., 1999). 

First, we examined whether participation of pyramidal neurons in SPW bursts is stochastic. On average, a pyramidal cell participated in 15% of successive SPWs. The probability of participation of individual neurons, however, varied extensively (2–40%; Fig. 3 _A_ ). In other words, some pyramidal cells discharged consistently more reliably during SPW bursts than did others. The participation probability of a pyramidal neuron during SPW could be predicted from the firing rate of the cell during � activity in rapid-eye-movement (REM) sleep ( _r_ � 0.59; _p_ � 0.0001; Fig. 3 _B_ ). These findings indicated that participation of pyramidal cells in the SPW event is not random and that the probability of their discharge in SPW correlates with the discharge frequency during � behaviors. 

## **Spike sequences in the awake and sleeping animal** 

The database for spike sequence analysis consisted of 10 sets of parallel-recorded spike trains of physiologically identified pyramidal neurons ( _n_ � 4–13 cells) from six rats. Repetition of spike sequences was observed in every animal investigated (Fig. 4). Sequences were detected from neurons recorded from both a single tetrode and neighboring tetrodes. Spike trains of larger numbers of simultaneously recorded cells yielded more sequences, but spike sequences could be identified reliably in records containing as few as four neurons. As expected, a large number of repeating spike patterns were observed in the wheelrunning behavioral task, especially when two or more of the recorded pyramidal cells were selectively activated in the wheel (Czurko et al., 1999) (Fig. 4 _b_ ). Importantly, repeating spike sequences were also present during sleep, when no external reference or motor behavior was available to generate repeating discharge sequences (Fig. 4 _a_ ). The fraction of repeating spike sequences ( _r_ � 2) and single (nonrepeating) patterns varied from 

**==> picture [230 x 454] intentionally omitted <==**

_Figure 3._ Relationship between the firing rate during � behavior and the probability of spike participation in SPW. _A_ , Probability of discharge of single pyramidal neurons in SPW events. Note that the majority of pyramidal neurons discharge �15% of all recorded SPWs. _B_ , Relationship between the firing rate during � and the probability of discharge during SPW events. Note that increased discharge rate during � predicts a higher incidence of participation in SPWs. 

8 to 56%. The exact percentage depended on the choice of sequence-search parameters (time window and spike jitter). 

The number of repeating spike sequences detected also depended on the reference (sequence “initiator”) neuron (Fig. 4). The inequality of the number of repeating sequences for different initiator neurons indicated that the sequences may reflect biological mechanisms because, in a random parallel spike train, spikes of a given neuron are expected to precede and follow spikes of other neurons with equal probability regardless of the firing rates. To examine further whether the repeating spike sequences reflected cellular interactions or simply Poisson coincidences of random events (Abeles and Gerstein, 1988), we compared the original spike trains with their shuffled surrogates. 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

J. Neurosci., November 1, 1999, _19_ (21):9497–9507 **9501** 

**==> picture [253 x 383] intentionally omitted <==**

_Figure 4._ Examples of the spike sequences during sleep ( _a_ ) and running ( _b_ ) sessions, detected by the template-matching method. Only spike sequences of neurons, recorded by a single tetrode, are shown. The sleep session preceded the run session. The sequence initiator neuron is indicated by _arrows_ . Recordings during sleep and running sessions were obtained from a single rat. The spike window (d _t_ ) was set to 10 msec in these searches. Different _colors_ indicate different patterns. The _gray lines_ in _b, top,_ indicate all nonrepeating (single) sequences for comparison. _Cell numbers_ refer to the same cells within the same behavioral category. _m_ , Number of different sequences; _r_ , number of repetitions of a given sequence. Also see: FTP://speedy2.md.huji.ac.il/pub/neuron.mid. 

The incidence of repeating spike sequences during wheel running was compared with surrogate trains obtained by each of the four shuffling methods ( _n_ � 1 rat). The number of repeating sequences extracted from the original spike train exceeded the number of repeating sequences present in each of the 100 surrogate trains. Comparison between the original spike train and its � phase-corrected shuffled surrogates (see � phase-invariant shuffling in Materials and Methods) is illustrated in Figure 5. The � phase-corrected shuffling procedure preserved the phase relationship between � and the individual spikes, therefore reproducing the population dynamics of the parallel spike train as revealed by the identical � phase-locked modulation and the similar crosscorrelograms of both original and shuffled spikes (Fig. 5 _b,c_ ). This procedure also preserved the within-spike-train dynamics of single neurons, as indicated by the similar autocorrelograms of the original and shuffled spike trains (Fig. 5 _d_ ). Comparison of repeat- 

**==> picture [253 x 315] intentionally omitted <==**

_Figure 5._ Comparison of repeating spike sequences in a parallel spike train, recorded during wheel running, with its shuffled surrogates. _a,_ Peaks of � oscillation were taken as a reference point, and the spike timing was converted to phase values within the � cycle. During shuffling, sets of spikes within a given � cycle were transposed randomly ( _arrows_ ). _b_ , Phase-normalized spike density histograms during the � cycle are shown. _c_ , Cross-correlogram between the negative peaks of local � and unit discharges is shown. _d_ , Spike autocorrelograms of units are shown. Note the similar spike dynamics in the original and shuffled spike trains. _e_ , Repetition curves of spike sequences in the original spike train and in its shuffled surrogates are shown. 

ing spike sequences indicated that the number of repeating spike sequences ( _r_ ) was less for all sequences ( _m_ ) in any of the 133 shuffled surrogates compared with the original spike train (Fig. 5 _e_ ). Of the various shuffling methods, across-spike-train shuffling resulted in the most spike sequence repetitions; therefore it may be regarded as the most rigorous test. Figure 6 illustrates the difference between repeating spike sequences obtained from the original parallel spike trains recorded from five rats and the Monte Carlo surrogates of those recordings (100 shuffled trains in each case). Shuffling was performed across spike trains for these tests because the spike trains contained both � and non-� epochs (see Across-spike-train shuffling; Fig. 2). For a given spike sequence ( _c_ ), the number of spike sequences ( _m_ ) that recurred at least _r_ min number of times was determined, and the average of the actual repetitions ( _r_ 1, _r_ 2, _r_ 3, . . . , _rn_ ) was calculated. In all five cases, the number of repeating spike sequences in the surrogates was less than that in the original parallel spike trains ( _p_ � 0.01) in the entire range of _ms–s_ . 

A second method used for the evaluation of repeating spike sequences was the JPM. In contrast to the template-matching method, the complexity of the spike sequence was limited to three in this analysis. On the other hand, the JPM detected all se- 

**9502** J. Neurosci., November 1, 1999, _19_ (21):9497–9507 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

**==> picture [251 x 451] intentionally omitted <==**

_Figure 6._ Comparison of repeating spike sequences in real spike trains (original) and their shuffled surrogates. _a–e_ , Data from five different rats. The _y_ -axis indicates the number of different sequences ( _m_ ), and the _x_ -axis indicates the average number of repeating sequences ( _r_ ); e.g, 50 different sequences were repeated 16 times on average in rat k12-30 ( _panel c_ ). Note that the repetition rate in the original spike train is higher than that in any of the 100 shuffled surrogates ( _p_ �� 0.01). In these comparisons, shuffling was done across spike trains. Rats are identified in each _top right corner_ . 

quences of spike triplets within a predefined time window ( _w_ ), regardless of the specific temporal position of spikes (Fig. 1 _g_ ). The distribution of repeating spike triplets was visualized as cumulative values in the bins of a joint peri-event histogram (Fig. 7 _a_ ). Cross-correlation histograms for spike doublets were also calculated (Fig. 7 _b_ ), and the expected co-occurrences of the corresponding spike doublets (i.e., random triplets) were subtracted from the observed distribution of triplets, resulting in a histogram of unexpected triplets (JPM, Fig. 7 _c_ ; see Materials and Methods). The statistical significance of the difference between the observed and expected spike triplets was calculated by the Fisher’s exact 

probability test. In the example shown in Figure 7 _a–d_ , a high incidence of triplets occurred at the temporal positions between _x_ values of 50 and 80 msec and _y_ values of 150 and 190 msec (e.g., 3, 2, 0; 50, 180 msec). The Fisher’s exact probability test indicated three significant ( _p_ � 0.02) triplet positions in the corresponding pixels [(3, 2, 0; 50, 182 msec), (3, 2, 0; 64, 173 msec), and (3, 2, 0; 72, 154 msec)]. Importantly, these time patterns were similar to the repeating spike sequences detected independently by the template-matching method from the same data set (Fig. 7 _d_ ). 

To examine the null hypothesis that significant spike triplets are generated by random coincidences, 100 JPMs were created from the shuffled surrogates and compared with the original data sets shown in Figure 6. In these shuffling tests, the temporaldisplacement-of-spikes procedure was used to ensure that shuffled spike trains have the same average firing rates and the same joint probability as the original data. Spikes were displaced in time by adding random intervals from 0 to 50 msec (see Temporal displacement of spikes; Fig. 2). For each of the original and the corresponding surrogate trains (total of 505 data sets), three separate JPMs were created, using 5, 6.7, and 10 msec bins. The number of repeating spike triplets in the original data sets was significantly larger than that in the shuffled correlates in every rat at the 6.7 and 10 msec bins (Fig. 7 _e_ ). At 5 msec, more spike triplets were detected from the shuffled spike trains in two animals than in the original spike trains (j0-08 and k9-02). However, the differences were not significant for either of the two animals. 

## **Behavioral modification of spike sequences** 

Next, we addressed the issue whether behaviorally imposed sequences can modify the probability of occurrence of those same sequences during subsequent slow-wave sleep. In two rats, stable recordings from the same neurons were obtained during Sleep1, Run, and Sleep2 sessions (Fig. 8). The similarity of spike sequence structure between any two states was tested in two steps. First, the significant triplets at all possible temporal positions were identified by the JPM method in each state. Second, the number of shared repeating spike sequences in different states was calculated, regardless of the exact temporal position of the spikes. For example, if the sequence 2;1;4 had significant pixels at any interspike intervals during the Run but not during the Sleep1 session, then it was not a common triplet between Run and Sleep1. However, if the triplet 2;1;4 was significant at 3 and 15 different temporal positions (pixels) during Run and Sleep2 sessions, respectively, then it was a common triplet. In the first rat, 13 pyramidal cells were recorded (Fig. 8). Only 87 of the 1716 possible triplets (5%) were common to both Sleep1 and Run sessions (Fig. 8 _a_ ). In contrast, 160 triplets (9%) were observed in both Run and Sleep2 sessions (Fig. 8 _b_ ; �[2] � 21.58; _p_ � 0.01). In addition, the number of significant pixels of common triplets correlated significantly between Run and Sleep2 sessions (Pearson _r_ � 0.737; _p_ � 0.001). In contrast, during the Run session, triplet incidences during Sleep1 were independent from those in Run and Sleep2 sessions (Pearson _r_ � 0.393; _r_ � 0.326; _p_ � 0.05). In the second rat four pyramidal cells were recorded in all three sessions. In this animal, statistically significant spike triplets common to two testing conditions were detected only between Run and Sleep2 sessions (Pearson _r_ � 0.679; _p_ � 0.001). 

Both the template-matching and the JPM methods indicated that the majority of spike sequences were either �50 or �100 msec. In general, short sequences dominated in slow-wave sleep, whereas the longer sequences occurred in the awake animal or REM sleep (e.g., Fig. 4 _a,b_ ). To quantify this observation, we 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

J. Neurosci., November 1, 1999, _19_ (21):9497–9507 **9503** 

**==> picture [513 x 581] intentionally omitted <==**

_Figure 7._ Spike triplets detected by the JPM method. _a,_ The JPTH of a spike triplet (3, 2, 0). Summed pixels in the _x-_ and _y_ -axes are also shown. _b,_ “Expected” JPTH, constructed on the assumption that triplets are random coincidences of spike doublets (see Materials and Methods). _c,_ The excess number of triplets expressed as the difference between the observed and expected JPTHs. Significant pixels (Fisher’s exact probability test) are _framed_ in _boxes_ . _d,_ Vector representation of 3, 2, 0 sequences extracted by the template-matching method. Note that the latencies of the triplets match the significant pixels in the JPM. _e,_ JPM maps constructed using three different pixel sizes (5, 6.7, and 10 msec) from the original and 100 shuffled surrogates (same original data sets shown in Fig. 6). The number of significant pixels in the surrogate JPMs is expressed as a percentage of the significant pixels in the original JPM. _Color bars,_ Number of events. 

**9504** J. Neurosci., November 1, 1999, _19_ (21):9497–9507 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

**==> picture [253 x 332] intentionally omitted <==**

_Figure 8._ Spike sequences during sleep are influenced by previous wheelrunning behavior. Histograms of significant triplets common to Sleep1 and Run sessions ( _a_ ), to Run and Sleep2 sessions ( _b_ ), and to Sleep1 and Sleep2 sessions ( _c_ ). A sequence was considered to be “common” if it was significant by the JPM method (Fig. 7) in both behavior sessions regardless of the interspike intervals (e.g., 4-1-2 at 50 and 80 msec and at 5 and 8 msec). Individual triplets are listed on the _x_ -axis. The _upward_ and _downward bars_ at any given location on the _x_ -axis indicate the number of significant pixels of the JPM of a common triplet in the two sessions, respectively. Note that there were almost twice as many triplets common to Run and Sleep2 sessions than to Sleep1 and Run sessions. The _r_ values (Pearson’s product moment correlation coefficient) indicate the correlation of the number of common triplets between the respective two sessions. 

examined the EEG correlates of repeating spike sequences. The independent variable in these tests was the length of the spike sequences, irrespective of the behavioral state of the rat. Spike sequences of the same pyramidal cells and temporal order were selected and subdivided into two groups, one with sequence termination �50 msec and one with termination �100 msec, and the power spectra of their associated background field activity were compared. Two different epochs were extracted from the EEG. The shorter epochs (204.8 msec before the first spike of the sequence) provided a more precise estimate of the exact EEG � state, whereas the longer ones ( 819.2 to 2457.6 msec) were used to assess the EEG power at lower frequencies. For these comparisons, spike sequences common to � and SPW states were used. Power spectra, calculated from the short and long EEG epochs (0–300 and 0–20 Hz, respectively), revealed that short spike sequences were associated with a significant peak at 140–200 Hz (Fig. 9 _b_ ), corresponding to field “ripples” in the EEG (Buzs�ki et al., 1992). Conversely, the long spike sequences were associated 

**==> picture [250 x 407] intentionally omitted <==**

_Figure 9._ Long and short repeating spike sequences are associated with � and ripple field activity, respectively. The power spectra of background field activity, associated with short and long sequences, were compared. The first spike of the same long (termination � 100 msec; _n_ � 47) or short (termination � 50 msec; _n_ � 78) spike sequences was regarded as the reference event for extracting field EEG information. _a,_ EEG power in the low-frequency band surrounding long ( _solid line_ ) and short ( _interrupted line_ ) repeating spike sequences. Note the increased � power during long sequences. _b,_ EEG power in the ripple frequency band (100–200 Hz) surrounding long and short repeating spike sequences. Note the large power peak at 160 Hz during short sequences. _Insets,_ Long (in _a_ ) and short (in _b_ ) sequences of the same neurons. Note the difference in timescale; short sequences are shown at an enhanced timescale. 

with increased power at � frequency (Fig. 9 _a_ ). These findings suggested that sequences associated with � behavior were replayed during SPW-associated ripples in a time-compressed manner. 

## **DISCUSSION** 

## **Quantification of repeating spike sequences** 

The template method and the JPM detected similar spike sequences. Nevertheless, a critical issue that must be addressed is whether the repeating spike sequences were generated by biological mechanisms or emerged simply as a result of random coincidences of spike trains. The reliability of the Monte Carlo test 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

J. Neurosci., November 1, 1999, _19_ (21):9497–9507 **9505** 

depends critically on the choice of the proper shuffling method. The ideal shuffling protocol should maintain the discharge frequency of individual spike trains and should not alter the population dynamics of the parallel-recorded neurons. Because none of the known shuffling methods are universally applicable in all situations, we used four different shuffling protocols. 

If the dynamics of cortical neurons could be described by a Poisson process (Bair and Koch, 1996; Shadlen and Newsome, 1998), then within-spike-train randomization of spike occurrences would be appropriate because this procedure does not alter the average firing rate of the individual neurons. Unfortunately, random shuffling within the same spike train (see Withinspike-train random shuffling) may alter the population dynamics of the parallel spike trains. This issue is very important, because population synchrony of hippocampal pyramidal cells varies with behavior and their dynamics do not follow simple Poisson statistics (Csicsvari et al., 1999). Random shuffling across spike trains (see Across-spike-train shuffling) preserved the population dynamics. However, this method tends to equalize the firing-rate differences of individual neurons relative to the original spike trains. This may be important because the number of repeating spike sequences in random spike trains varies with discharge frequency (Abeles and Gerstein, 1988). To retain both population behavior and firing-rate changes, two additional shuffling protocols were used. The temporal displacement method (see Temporal displacement of spikes) shifted spikes randomly within a 50 msec time window with the goal of retaining the population synchrony across spike trains during both � waves and SPWs. The phase-invariant shuffling method (see � phase-invariant shuffling) preserved spike dynamics both within and across spike trains. Regardless of the shuffling method used, excessively repeating spike sequences were found in each of the parallel-recorded spike trains. Furthermore, the number of different sequences, the number of repeating spike sequences, and the number of spikes within a given sequence (complexity) varied even within the same data set depending on the neuron that served as a sequence initiator. Finally, the discharge probability of pyramidal cells in SPW varied substantially from cell to cell. Together, these observations indicate that the observed spike sequences cannot be accounted for fully by random coincidences of neuronal discharges of hippocampal cells. 

is hypothesized to transfer the stored representations in the hippocampus to neocortical networks (Buzsa´ki, 1989; Wilson and McNaughton, 1994; McClelland et al., 1995; Siapas and Wilson, 1998). Consistent with this speculation, the probability of SPWassociated discharge of pyramidal neurons correlated with the discharge frequency of these neurons during � behavior. In addition, spike sequences that were observed in the wheel-running task were observed in the subsequent slow-wave sleep episode at a higher probability than during sleep before the wheel-running session. These findings support and extend observations by Wilson and McNaughton (1994) and Skaggs and McNaughton (1996) [but see also Hampson et al. (1996); McNaughton et al. (1996); Moore et al. (1996)], who found that cell pairs with overlapping place fields had an increased correlation during subsequent sleep. Our findings also demonstrate that sleep-associated replay of the sequences observed during � behavior are mainly confined to SPW bursts. It was demonstrated previously that the correlation between cell pairs is significantly increased during SPW (Wilson and McNaughton, 1994). However, such increased correlation may be a spurious consequence of an increased firing rate during SPW (Csicsvari et al., 1999). In the present study, the SPWassociated time compression of spike sequences was demonstrated by the correlation between the occurrence of short sequences and increased power at the ripple frequency. The effect of increased discharge rate on the probability of sequences during SPW was reduced or eliminated by shuffling across spike trains. These observations support the suggestion that time-compressed neuronal patterns during SPW bursts are generated within the hippocampus and are a consequence of firing patterns in the wake brain (Buzsa´ki, 1989; Chrobak and Buzsaki, 1994; Bibbig et al., 1995; Hinton et al., 1995; McClelland et al., 1995; Skaggs and McNaughton, 1996; Wallenstein and Hasselmo, 1997; Menschik and Finkel, 1998; August and Levy, 1999). It may be argued that both the slow and fast sequences were imposed onto the hippocampal circuitry by the entorhinal input; thus the hippocampus does not play an active role in generating endogenous repeating spike sequences. This possibility is not likely because during sleep SPW bursts are initiated in the CA3 region of the hippocampus (Buzsa´ki, 1989). In fact, the incidence of SPWs increases dramatically after entorhinal cortex lesion (Bragin et al., 1995). 

## **Physiological role of spike sequence replay** 

## **Externally controlled and internally generated recurring spike sequences** 

Spike sequences were observed in both the awake and sleeping animal. The spatially distributed pattern of temporally precise single pyramidal neuron spikes during sleep could be a consequence of some hard wiring (Hampson et al., 1996) or may reflect synaptic changes as a result of learning in the awake animal (Wilson and McNaughton, 1994; Mehta et al., 1997). We hypothesized previously that the behavior-dependent electrical changes in the hippocampal formation (�- and SPW-associated states) might subserve a two-stage process of information storage (Buzsa´ki, 1989). Mnemonic information is assumed to be encoded in the recurrent and Schaffer collateral synapses of CA3 pyramidal cells during �-associated learning behavior. When the network state of the CA3 matrix switches to SPW bursts during consummatory behaviors and slow-wave sleep, synaptic connections that were active during the learning state are spontaneously reactivated. Rapid reinstatement of the spatiotemporal patterns of pyramidal cell activity in the CA3–CA1 regions and deep layers of the entorhinal cortex (Chrobak and Buzsaki, 1994, 1996) 

What is the physiological importance of the recurring spike sequences (Lisman, 1998)? In a weaker formulation of the replay hypothesis, the exact sequence of neuronal firing is not critical. What is important is that neurons, which discharge in a temporally discontiguous manner during � behavior and possibly encode different representations, are brought together during SPW on the timescale of the time constant of NMDA receptors. From this perspective, the function played by the time-compressed replay of the active neurons in the awake animal is to ensure Hebbian modification among pyramidal cells, which did not discharge together within the critical time window of synaptic plasticity during learning but nevertheless carry related information. For example, during spatial behavior, various place cells are activated as the animal explores its environment (O’Keefe and Nadel, 1978). Because the same spatial position can be approached from various directions, hence associated by the activation of different neuronal sequences, most neurons do not discharge together in time. During SPW bursts, these same neuron sets may be endogenously reactivated within the time constant of the NMDA receptors, providing an opportunity for Hebbian 

**9506** J. Neurosci., November 1, 1999, _19_ (21):9497–9507 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

synaptic modification of the recurrent and Schaffer synapses of the CA3 pyramidal cells. 

Alternatively, one can argue that the replay of spike sequences is critical for the activation of relevant target neurons downstream from the hippocampus (Chrobak and Buzsa´ki, 1996; Siapas and Wilson, 1998). This model assumes the existence of neuronal mechanisms for decoding spike sequences with ripple frequency (5 msec) resolution both within the hippocampus and in its targets. Recent works on individual pyramidal neurons and their network interactions suggest that pyramidal cells are equipped with intrinsic oscillatory properties (Llina´s, 1988; Leung and Yim, 1991; Kamondi et al., 1998) and are embedded in an oscillatory network of interneurons (Buzsa´ki and Chrobak, 1995; Whittington et al., 1995). Within these oscillatory patterns, the ratio of excitation and inhibition can vary substantially (Rudell et al., 1980; Buzsa´ki et al., 1981; Csicsvari et al., 1999). We hypothesize that the oscillatory network of neuronal assemblies may provide “temporal windows of opportunity” to ignore or enhance selectively the effectiveness of presynaptic activity. As a result, individual spikes of a given spike sequence, as shown here, could exert a differential impact on their postsynaptic targets, depending on the relationship between the spike and network activity. 

Finally, it should be emphasized that the time-compression effect is caused by the population dynamics of the hippocampal network and that its mechanism is orthogonal to the formation of spike sequences. During SPW bursts, the discharge probability of pyramidal neurons increases several-fold (Csicsvari et al., 1999), independent of whether a neuron is part of an observed spatiotemporal spike sequence or not. Nevertheless, temporal coactivation of neurons, brought about by SPW bursts, is expected to strengthen their synaptic weights. Direct demonstration of SPWinduced synaptic changes, however, remains a future challenge. 

_Note added in proof._ While this manuscript was under review, a paper with relevant content has been published [Barnes CA, McNaughton BL (1999) Reactivation of hippocampal cell assemblies: effects of behavioral state, experience, and EEG dynamics. J Neurosci 19:4090–4101]. 

## **REFERENCES** 

- Abeles M (1991) Corticonics: neural circuits of the cerebral cortex. Cambridge, U.K.: Cambridge UP. 

Abeles M, Gerstein GL (1988) Detecting spatiotemporal firing patterns among simultaneously recorded single neurons. J Neurophysiol 60:909–924. 

- Abeles M, Bergman H, Margalit E, Vaadia E (1993) Spatiotemporal firing patterns in the frontal cortex of behaving monkeys. J Neurophysiol 70:1629–1638. 

Aertsen AM, Gerstein GL, Habib MK, Palm G (1989) Dynamics of neuronal firing correlation: modulation of “effective connectivity.” J Neurophysiol 61:900–917. 

- Aertsen A, Vaadia E, Abeles M, Ahissar E, Bergman H, Karmon B, Lavner Y, Margalit E, Nelken I, Rotter S (1991) Neural interactions in the frontal cortex of a behaving monkey: signs of dependence on stimulus context and behavioral state. J Hirnforsch 32:735–743. 

August DA, Levy WB (1999) Temporal sequence compression by an integrate-and-fire model of hippocampal area CA3. J Comput Neurosci 6:71–90. 

Bair W, Koch C (1996) Temporal precision of spike trains in extrastriate cortex of the behaving macaque monkey. Neural Comput 8:1185–1202. Barlow HB (1972) Single units and sensation: a neuron doctrine for perceptual psychology? Perception 1:371–394. 

Bibbig A, Wennekers T, Palm G (1995) A neural network model of the cortico-hippocampal interplay and the representation of contexts. Behav Brain Res 66:169–175. 

Bragin A, Jando G, Nadasdy Z, van Landeghem M, Buzsa´ki G (1995) 

- Dentate EEG spikes and associated population bursts in the hippocampal hilar region of the rat. J Neurophysiol 73:1691–1705. 

- Brown EN, Frank LM, Tang D, Quirk MC, Wilson MA (1998) A statistical paradigm for neural spike train decoding applied to position prediction from ensemble firing patterns of rat hippocampal place cells. J Neurosci 18:7411–7425. 

- Buzsa´ki G (1989) Two-stage model of memory trace formation: a role for “noisy” brain states. Neuroscience 31:551–570. 

- Buzsa´ki G, Chrobak JJ (1995) Temporal structure in spatially organized neuronal ensembles: a role for interneuronal networks. Curr Opin Neurobiol 5:504–510. 

- Buzsa´ki G, Grastya´n E, Czopf J, Kellenyi L, Prohaska O (1981) Changes in neuronal transmission in the rat hippocampus during behavior. Brain Res 225:234–247. 

- Buzsa´ki G, Horvath Z, Urioste R, Hetke J, Wise K (1992) Highfrequency network oscillation in the hippocampus. Science 256:1025–1027. 

- Chrobak JJ, Buzsa´ki G (1994) Selective activation of deep layer (V–VI) retrohippocampal cortical neurons during hippocampal sharp waves in the behaving rat. J Neurosci 14:6160–6170. 

- Chrobak JJ, Buzsa´ki G (1996) High-frequency oscillations in the output networks of the hippocampal-entorhinal axis of the freely moving rat. J Neurosci 16:3056–3066. 

- Csicsvari J, Hirase H, Czurko A, Mamiya A, Buzsa´ki G (1999) Oscilatory coupling of hippocampal pyramidal cells and interneurons in the behaving rat. J Neurosci 19:274–287. 

- Czurko A, Hirase H, Csicsvari J, Buzsa´ki G (1999) Sustained activation of hippocampal pyramidal cells by “space clamping” in a running wheel. Eur J Neurosci 1:344–352. 

- Dayhoff JE, Gerstein GL (1983) Favored patterns in spike trains. I. Detection. J Neurophysiol 49:1334–1348. 

- Eccles JC (1957) The physiology of nerve cells. Baltimore: Johns Hopkins. 

- Eckhorn R, Bauer R, Jordan W, Brosch M, Kruse W, Munk M, Reitboeck HJ (1988) Coherent oscillations: a mechanism of feature linking in the visual cortex? Multiple electrode and correlation analyses in the cat. Biol Cybern 60:121–130. 

- Frostig RD, Frostig Z, Harper RM (1990a) Recurring discharge patterns in multiple spike trains. I. Detection. Biol Cybern 62:487–493. 

- Frostig RD, Frysinger RC, Harper RM (1990b) Recurring discharge patterns in multiple spike trains. II. Application in forebrain areas related to cardiac and respiratory control during different sleep-waking states. Biol Cybern 62:495–502. 

- Georgopoulos AP, Kalaska JF, Caminiti R, Massey JT (1982) On the relation between the two-dimensional arm movements and cell discharge in primate motor cortex. J Neurosci 2:1527–1537. 

- Gray CM, Singer W (1989) Stimulus-specific neuronal oscillations in orientation columns of cat visual cortex. Proc Natl Acad Sci USA 86:1698–1702. 

- Hampson RE, Byrd DR, Konstantopoulos JK, Bunn T, Deadwyler SA (1996) Hippocampal place fields: relationship between degree of field overlap and cross-correlations within ensembles of hippocampal neurons. Hippocampus 6:281–293. 

- Hinton GE, Dayan P, Frey BJ, Neal RM (1995) The “wake-sleep” algorithm for unsupervised neural networks. Science 268:1158–1161. 

- Hopfield JJ (1995) Pattern recognition computation using action potential timing for stimulus representation. Nature 376:33–36. 

- Kamondi A, Acsa´dy L, Wang X-J, Buzsa´ki G (1998) Theta oscillations in somata and dendrites of hippocampal pyramidal cells in vivo: activity dependent phase-precession of action potentials. Hippocampus 8:244–261. 

- Laurent G, Wehr M, Davidowitz H (1996) Temporal representations of odors in an olfactory network. J Neurosci 16:3837–3847. 

- Leung LS, Yim CY (1991) Intrinsic membrane potential oscillations in hippocampal neurons in vitro. Brain Res 553:261–274. 

- Lisman JE (1998) What makes the brain’s tickers tock. Nature 394:132–133. 

- Lisman JE, Idiart MA (1995) Storage of 7 � 2 short-term memories in oscillatory subcycles. Science 267:1512–1515. 

- Llina´s RR (1988) The intrinsic electrophysiological properties of mammalian neurons: insights into central nervous system function. Science 242:1654–1664. 

- Marder E, Calabrese RL (1996) Principles of rhythmic motor pattern generation. Physiol Rev 76:687–717. 

- McClelland JL, McNaughton BL, O’Reilly RC (1995) Why there are 

Na´ dasdy et al. • Spike Sequences in the Hippocampus _in vivo_ 

J. Neurosci., November 1, 1999, _19_ (21):9497–9507 **9507** 

- complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychol Rev 102:419–457. 

- McNaughton BL, Barnes CA, Gerrard JL, Gothard K, Jung MW, Knierim JJ, Kudrimoti H, Qin Y, Skaggs WE, Suster M, Weaver KL (1996) Deciphering the hippocampal polyglot: the hippocampus as a path integration system. J Exp Biol 199:173–185. 

- Mehta MR, Barnes CA, McNaughton BL (1997) Experiencedependent, asymmetric expansion of hippocampal place fields. Proc Natl Acad Sci USA 94:8918–8921. 

- Menschik ED, Finkel LH (1998) Neuromodulatory control of hippocampal function: towards a model of Alzheimer’s disease. Artif Intell Med 13:99–121. 

- Moore GP, Rosenberg JR, Hary D, Breeze P, Skaggs WE, McNaughton BL (1996) “Replay” of hippocampal “memories.” Science 274: 216–1217. 

- Nadasdy Z, Bragin A, Buzsa´ki G (1996) Repeating spatio-temporal patterns of neuronal activity in the hippocampus during sleep. Soc Neurosci Abstr 22:445.11. 

- Nadasdy Z, Bragin A, Csicsvari J, Hirase H, Moore K, Buzsa´ki G (1997) Relationship between recurring spatio-temporal spike patterns and local field oscillations in the hippocampus. Soc Neurosci Abstr 23:188.5. 

- Nadasdy Z, Csicsvari J, Hirase H, Czurko A, Buzsa´ki G (1998) Persistence, compression and behavioral induction of spike sequences in the hippocampus. Soc Neurosci Abstr 24:362.18. 

- Na´dasdy Z, Csicsvari J, Penttonen M, Hetke J, Wise K, Buzsa´ki G (1998) Extracellular recording and analysis of neuronal activity: from single cells to ensembles. In: Neuronal ensembles: strategies for recording and encoding (Eichenbaum H, Davis J, eds), pp 17–55. New York: Wiley. 

- O’Keefe J, Nadel L (1978) The hippocampus as a cognitive map. Oxford: Clarendon. 

- O’Keefe J, Recce ML (1993) Phase relationship between hippocampal place units and the EEG theta rhythm. Hippocampus 3:317–330. 

- Pavlides C, Winson J (1989) Influences of hippocampal place cell firing in the awake state on the activity of these cells during subsequent sleep episodes. J Neurosci 9:2907–2918. 

- Quirk MC, Wilson MA (1998) Temporal changes in the firing properties of CA1 pyramidal cells in the freely behaving rat. Soc Neurosci Abstr 24:758.13. 

- Ranck JB (1973) Studies on single neurons in dorsal hippocampal formation and septum in unrestrained rats. I. Behavioral correlates and firing repertoires. Exp Neurol 42:461–531. 

- Riehle A, Gru¨n S, Diesmann M, Aertsen A (1997) Spike synchronization and rate modulation differentially involved in motor cortical function. Science 278:1950–1953. 

- Rudell AP, Fox SE, Ranck JB (1980) Hippocampal excitability phaselocked to the theta rhythm in walking rats. Exp Neurol 68:87–96. 

- Shadlen MN, Newsome WT (1998) The variable discharge of cortical neurons: implications for connectivity, computation and information coding. J Neurosci 18:3870–3896. 

- Sherrington CS (1906) Integrative action of the nervous system. New Haven, CT: Yale UP. 

- Siapas AG, Wilson MA (1998) Coordinated interactions between hippocampal ripples and cortical spindles during slow-wave sleep. Neuron 21:1123–1128. 

- Singer W (1993) Synchronization of cortical activity and its putative role in information processing and learning. Annu Rev Physiol 55:349–374. 

- Skaggs WE, McNaughton BL (1996) Replay of neuronal firing sequences in rat hippocampus during sleep following spatial experience. Science 271:1870–1873. 

- Skaggs WE, McNaughton BL, Wilson MA, Barnes CA (1996) Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. Hippocampus 6:149–172. 

- Strehler BL, Lestienne R (1986) Evidence of precise time-coded symbols and memory patterns in monkey cortical spike trains. Proc Natl Acad Sci USA 83:9812–9816. 

- Ts’o DJ, Gilbert CD, Wiesel TN (1986) Relationship between horizontal interactions and functional architecture in cat striate cortex as revealed by cross-correlation analysis. J Neurosci 6:1160–1170. 

- Vaadia E, Abeles M (1987) Temporal firing patterns of single units, pairs and triplets of units in the auditory cortex. Isr J Med Sci 23:75–83. 

- von der Malsburg C, Bienenstock E (1986) A neural network for the retrieval of superimposed connection patterns. Neurosci Lett 3:1243–1249. 

- Wallenstein GV, Hasselmo ME (1997) GABAergic modulation of hippocampal population activity: sequence learning, place field development, and the phase precession effect. J Neurophysiol 78:1393–1408. 

- Whittington MA, Traub RD, Jefferys JG (1995) Synchronized oscillations in interneuron networks driven by metabotropic glutamate receptor. Nature 373:612–615. 

- Wilson MA, McNaughton BL (1994) Reactivation of hippocampal ensemble memories during sleep. Science 265:676–679. 

- Yuste R, Denk W (1995) Dendritic spines as basic functional units of neuronal integration. Nature 375:682–684. 

- Zhang K, Ginzburg I, McNaughton BL, Sejnowski TJ (1998) Interpreting neuronal population activity by reconstruction: unified framework with application to hippocampal place cells. J Neurophysiol 79:1017– 1044. 

