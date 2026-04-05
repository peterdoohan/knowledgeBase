Current Biology Dispatches 

**==> picture [60 x 60] intentionally omitted <==**

   9. Liu, O.W., Chun, C.D., Chow, E.D., Chen, C., (2018). RNAi is a critical determinant of Madhani, H.D., and Noble, S.M. (2008). centromere evolution in closely related fungi. Systematic genetic analysis of virulence in the Proc. Natl. Acad. Sci. USA 115, 3108–3113. human fungal pathogen Cryptococcus neoformans. Cell 135, 174–188. 

7. Catania, S., Dumesic, P.A., Pimentel, H., Nasif, A., Stoddard, C.I., Burke, J.E., Diedrich, J.K., Cook, S., Shea, T., Geinger, E., et al. (2020). Evolutionary persistence of DNA methylation for millions of years after ancient loss of a de novo methyltransferase. Cell 180, 263–277 e220. 

      12. Selker, E.U. (1999). Gene silencing: repeats that count. Cell 97, 157–160. 

   10. Law, J.A., and Jacobsen, S.E. (2010). Establishing, maintaining and modifying DNA methylation patterns in plants and animals. Nat. Rev. Genet. 11, 204–220. 11, 204–220., 204–220.. 

- methylation patterns in plants and animals. 13. Colot, V., Maloisel, l.L., and Rossignol, J.-L. Nat. Rev. Genet. 11, 204–220. 11, 204–220., 204–220.. (1996). Interchromosomal transfer of 

- 8. Huff, J.T., and Zilberman, D. (2014). Dnmt1epigenetic states in Ascobolus: transfer of independent CG methylation contributes to 11. Yadav, V., Sun, S., Billmyre, R.B., Thimmappa, DNA methylation is mechanistically related nucleosome positioning in diverse eukaryotes. B.C., Shea, T., Lintner, R., Bakkeren, G., to homologous recombination. Cell 86, Cell 156, 1286–1297. Cuomo, C.A., Heitman, J., and Sanyal, K. 855–864. 

## Reinforcement Learning: Full Glass or Empty — Depends Who You Ask 

## Jacob J.W. Bakermans[1] , Timothy H. Muller[2] , and Timothy E.J. Behrens[1][,][3] 

1Wellcome Centre for Integrative Neuroimaging, FMRIB, Nuffield Department of Clinical Neurosciences, University of Oxford, John Radcliffe Hospital, Oxford OX3 9DU, UK 

2Institute of Neurology, Department of Clinical and Movement Neurosciences, University College London, London WC1N 3BG, UK 

3Wellcome Centre for Human Neuroimaging, University College London, London WC1N 3AR, UK 

Correspondence: Jacob.bakermans@ndcn.ox.ac.uk (J.J.W.B.), timothymuller127@gmail.com (T.H.M.), behrens@fmrib.ox.ac.uk (T.E.J.B.) https://doi.org/10.1016/j.cub.2020.02.062 

An extension of the prediction error theory of dopamine, imported from artificial intelligence, represents the full distribution over future rewards rather than only the average and better explains dopamine responses. 

The relationship between neuroscience and artificial intelligence is a long and fruitful one, with many of the greatest advances in each inspired by the other [1]. This is exemplified by the field of reinforcement learning: how, from rewards and punishments, we learn the values of our actions to choose better next time [2]. Formalising observations from animal behaviour led to simple mathematical models of how animals learnt the expected reward (or value) that would accrue from choosing particular stimuli, or taking particular actions [3]. Artificial intelligence researchers noticed limitations in these models and developed a general value-learning algorithm, referred to as temporal difference learning [2]. Neuroscientists then discovered that the key signal underlying temporal difference learning — the temporal difference prediction error — matched the firing of dopamine neurons with beautiful precision [4]. This work paved the way for entire fields of neuroscience, but left open 

important questions: While temporal difference learning learns the average, or expected, values of actions, it loses track of all the different outcomes that might follow a given action. Additionally, it did not predict the diversity of dopamine responses that is observed, suggesting not all dopamine neurons track the same expected reward. Decades after this initial discovery, Dabney et al. [5] have imported another insight from artificial intelligence into neuroscience that elegantly solves both these problems: the diversity of dopamine responses in fact reflects the representation of the probability distribution over different possible outcomes. 

Reinforcement learning is finding how to act in order to maximise future reward. This is a difficult task because often it is not clear how actions taken now cause favourable outcomes later on. Once you achieve your goal, how do you know which actions were crucial for getting there? In the 1980s, artificial 

intelligence researchers developed the temporal difference learning algorithm to overcome this problem [2]. Temporal difference learning not only keeps track of reward that directly follows an action, but also the expected rewards accumulating in the extended future — when you are enjoying a hot cappuccino, you should credit value to the earlier decision to leave the office, so you are likely to make it again. Temporal difference learning updates value using the temporal difference reward prediction error — the difference between received and expected longterm average reward. This ensures that, after many experiences, the value of the coffee percolates back to the office door. 

This temporal difference prediction error precisely explains the firing of dopamine neurons [4]. For example, the dopamine neurons of a coffee aficionado would initially fire only to the taste of the coffee. After many trips to the coffee 

**==> picture [17 x 17] intentionally omitted <==**

Current Biology 30, R302–R328, April 6, 2020 ª 2020 Published by Elsevier Inc. R321 

Current Biology Dispatches 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [294 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Berry bush B<br>or<br>Reward Mean Minimum<br>to survive<br>Apple tree<br>Current Biology<br>??<br>Probability<br>**----- End of picture text -----**<br>


mechanism underlying dopamine signalling? 

Dabney et al. [5] drew inspiration from artificial intelligence once again to show this diversity reflects representation of a distribution over possible outcomes. Recently, machine learning agents for reinforcement learning problems (like videogames) have been improved by distributional reinforcement learning [10,11]. Instead of learning a single prediction, of expected reward, a distributional reinforcement learning agent learns a whole set of different predictions, allowing it to represent the full distribution of possible rewards. Encouraged by the biological plausibility of the mechanisms for distributional reinforcement learning, the authors [5] set out to find its signatures in the firing of dopamine neurons — and found compelling evidence. 

Figure 1. Surviving the night. 

(A) Forage at a berry bush (blue) or an apple tree (orange)? (B) The amount of food on the berry bush is higher on average (arrows), as the apple tree is likely to be depleted. But since the bird won’t survive the night when its energy is below-threshold (dotted line), the apple tree is the better option. Icons by Freepik from flaticon.com. 

The different predictions that allow a distributional reinforcement learning agent, or brain, to represent the full reward distribution can be thought of as differences in ‘optimism’ across neurons (Figure 2). An optimistic neuron predicts high reward. It will therefore produce reward prediction errors that are mostly negative, as usually the experienced reward is lower than its expectation. These neurons inform the agent about the 

shop, dopamine neurons start to fire upon leaving the office, in expectation of coffee in the (not-so-distant) future [4]. 

stronger prediction errors than others to the same reward [8,9]. This is surprising: if the neurons implement the classic temporal difference learning algorithm, they all learn the same (expected) reward and therefore signal the same prediction error. Could this diversity actually be a signature of a more complex and sophisticated 

However, this now ‘classical’ theory of temporal difference learning only tracks the average — or expectation — of possible future reward. It would therefore struggle with problems that require knowledge (representation) of the distribution over possible outcomes of an action. 

**==> picture [324 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Mean B RPE: D<br>Learning the way that<br>reward is distributed:<br>Received<br>reward Dopamine neurons<br>accomplish this task.<br>Reward<br>C Pessimist Optimist RPE scalings are<br>Average Overweight<br>positive RPEs heterogeneous.<br>Full glass or empty?<br>Underweight<br>negative RPEs Depends who you ask.<br>Reward Equal sensitivity<br>Current Biology<br>Probability<br>RPE<br>**----- End of picture text -----**<br>


What does it mean to represent the distribution over possible outcomes? Imagine a bird that has to decide where to forage, to gather enough nutrients to make it through the night (Figure 1) [6,7]. Either it flies to its favourite berry bush, which provides a steady amount of food, or it chooses a big apple tree. The apple tree has most likely already been raided by other birds, but if not, it has a lot of juicy apples. On average, the berry bush yields the most fruit; but because the berries are insufficient to survive the night, the apple tree gamble is the better option. In order to realise this, the brain must represent the possibility of the two different outcomes of foraging at the apple tree. Simply averaging them, as in temporal difference learning, would result in preferring the berries and guarantee starvation. 

Figure 2. Learning distributions. 

(A) Optimistic and pessimistic neurons predict different amounts of reward, whereas classical temporal difference neurons all predict the average reward. (B) As a consequence, distributional reinforcement learning predicts a diversity of positive and negative prediction errors for a given reward. (C) Optimistic predictions arise from the overweighting of positive reward prediction errors, and underweighting of negative ones (and vice versa for pessimistic predictions). Classical temporal difference learning neurons only predict the average reward by being equally sensitive to positive and negative reward prediction errors. (D) Summary in double dactyl. 

In addition to this computational problem, dopamine neurons do not all fire equally; some respond with 

R322 Current Biology 30, R302–R328, April 6, 2020 

Current Biology Dispatches 

**==> picture [60 x 60] intentionally omitted <==**

higher end of the reward distribution. A pessimistic neuron predicts low reward, will usually produce positive prediction errors, and is informative of the lower end of the reward distribution. By contrast, in the classical temporal difference learning theory, all neurons predict the same amount of reward — the average reward. Above-average rewards always produce positive prediction errors and belowaverage rewards always negative prediction errors. Therefore, these two theories can be distinguished by the reversal points — the reward at which lower rewards produce negative, and higher rewards positive prediction errors — of neurons across the population. 

Dabney et al. [5] tested for signatures of distributional reinforcement learning using dopamine neurons previously recorded [12] in the ventral tegmental area of mice while the animals received a random amount of reward (one of 0.1, 0.3, 1.2, 2.5, 5, or 10 ml) on each trial. Consistent with distributional reinforcement learning, the authors found a range of different reversal points across the population. Concretely, some (pessimistic) neurons produced a positive reward prediction error at 0.3 ml, while other (optimistic) neurons produced a negative reward prediction error at 5 ml. 

What makes a neuron optimistic or pessimistic — what determines its reversal point? A single change to classical temporal difference learning leads to a diversity of reversal points. In classical temporal difference learning, the scaling of reward prediction errors is identical for positive and negative reward prediction errors. Positive and negative prediction errors balance each other when they appear equally often: when the neuron predicts the average reward. Now imagine a neuron with a steeper scaling to — or higher rate of learning from — positive reward prediction errors. These strong positive reward prediction errors are balanced out when they are less frequent than weaker negative reward prediction errors. This equilibrium occurs when the neuron’s reversal point, its reward prediction, is high; we obtain an optimistic neuron (Figure 2C). The opposite, a steeper scaling of negative reward prediction errors, 

**==> picture [325 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Optimistic Neurons Pessimistic D<br>Task<br>B Overweight – RPEs Overweight +<br>Neurons<br>C What are predictions after learning?<br>Decoded<br>Current Biology<br>**----- End of picture text -----**<br>


Figure 3. Reconstructing distributions. 

(A) Across the population, neurons are optimistic (or pessimistic) to different extents. (B) Each neuron will learn its own reward prediction (teal, blue, purple) because of differences in sensitivity to positive versus negative reward prediction errors. (C) If a very optimistic neuron learns a reward prediction of 5 ml, reward will usually be below 5 ml. In other words, if you know the sensitivity asymmetry of each neuron and the resulting reward prediction, you can reconstruct the underlying true distribution (like the one on the left or the right). (D) For a given task’s reward distribution (top), the authors measure individual dopamine neurons (middle) and successfully decode (bottom) the ground truth. 

is beneficial to artificial neural networks. In most cases, in fact, distributional reinforcement learning algorithms still make choices on the basis of the average reward. Learning the reward distribution is beneficial to these agents because it makes them build a better internal representation of their inputs. Two situations with the same average reward but different distributions would be treated as the same in classical temporal difference learning, but distributional reinforcement learning forces the network to separate them. Biological brains also have to transform sensory input into useful representations. This raises an intriguing question. Is the function of distributional reinforcement learning the same in mouse and machine, or could each benefit from the reward distribution for completely different reasons? 

leads to a pessimistic neuron. The theory therefore predicts diversity in the slopes of the positive versus the negative prediction errors across the population of dopamine neurons, and furthermore that this should correlate with the reversal points — not expected by random diversity across neurons. Dabney et al. [5] present strong evidence for both these predictions. 

Distributional reinforcement learning posits that the specific set of reward predictions encodes the full distribution of rewards. Dabney et al. [5] put this to the test in their final and perhaps most ambitious analysis (Figure 3). 

Remarkably, they were able to decode the probability density function of the reward distribution in the task from the set of reversal points and associated response asymmetries. They successfully reconstructed multimodal distributions from cell activity alone. Such distributions are particularly interesting because the mean is a bad approximation of the full distribution. The possible outcomes of choosing the apple tree in our example are a typical case of a multimodal distribution. 

## REFERENCES 

1. Hassabis, D., Kumaran, D., Summerfield, C., and Botvinick, M. (2017). NeuroscienceInspired Artificial Intelligence. Neuron 95, 245–258. 

2. Sutton, R., and Barto, A. (1998). Reinforcement Learning: An Introduction (MIT Press). 

Dabney et al. [5] thus provide evidence of distributional reinforcement learning in the population of dopamine neurons in the mouse ventral tegmental area. This work answers old questions and raises new. The hungry bird described above needed access to the reward distribution to make a good choice, but this is not the reason it 

3. Rescorla, R.A., and Wagner, A.R. (1972). A theory of Pavlovian conditioning: variations in the effectiveness of reinforcement and nonreinforcement. In Classical Conditioning II: Current Research and Theory, A.H. Black, and W.F. Prokasy, eds. (New York: AppletonCentury-Crofts), pp. 64–99. 

Current Biology 30, R302–R328, April 6, 2020 R323 

Current Biology Dispatches 

**==> picture [60 x 60] intentionally omitted <==**

   7. Caraco, T. (1981). Energy budgets , risk and foraging preferences in dark-eyed juncos (Junco hyemalis). Behav. Ecol. Sociobiol., 213–217. 

4. Schultz, W., Dayan, P., and Montague, P.R. (1997). A neural substrate of prediction and reward. Science 275, 1593–1599. 

5. Dabney, W., Kurth-Nelson, Z., Uchida, N., Starkweather, C.K., Hassabis, D., Munos, R., and Botvinick, M. (2020). A distributional code for value in dopamine- based reinforcement learning. Nature 577, 671–675. 

   8. Fiorillo, C., Tobler, P., and Schultz, W. (2003). Discrete coding of reward dopamine neurons. Science 299, 1898–1903. 

   9. Lammel, S., Lim, B.K., and Malenka, R.C. (2014). Reward and aversion in a heterogeneous midbrain dopamine system. Neuropharmacology 76, 351–359.. 

6. Kolling, N., Wittmann, M., and Rushworth, dopamine system. Neuropharmacology 76, M.F.S. (2014). Multiple neural mechanisms of 351–359.. decision making and their competition under changing risk pressure. Neuron 81, 1190– 10. Bellemare, M.G., Dabney, W., and Munos, R. 1202. (2017). A distributional perspective on 

reinforcement learning. Proc. 34th Int. Conf. Mach. Learn. 70, 449–458. 

11. Dabney, W., Rowland, M., Bellemare, M.G., and Brain, G. (2018). Distributional reinforcement learning with quantile regression. The Thirty-Second AAAI Conference on Artificial Intelligence, 2892– 2901. 

12. Eshel, N., Bukwich, M., Rao, V., Hemmelder, V., Tian, J., and Uchida, N. (2015). Arithmetic and local circuitry underlying dopamine prediction errors. Nature 525, 243–246. 

## Biofilms: Managing Stress to Navigate Group Dynamics 

## Murray J. Tipping and Karine A. Gibbs* 

Department of Molecular and Cellular Biology, Harvard University, Cambridge, MA, USA *Correspondence: kagibbs@mcb.harvard.edu https://doi.org/10.1016/j.cub.2020.02.045 

To thrive in dense communities, organisms have to navigate neighbors and resources. A new study reveals that bacteria integrate cues of communal living through stress pathways. The primary source of the stress — at least for one bacterium — is a direct conflict with neighbors. 

Living in a community can be tricky. It requires trade-offs — budgeting resources for growth, managing conflicts, and protecting one’s gains. These dynamics hold for populations at all scales, from herds of animals to the gut microbiome and bacterial biofilms [1]. Ubiquitous in nature, mixed-species biofilms involve intricate mixtures of competition and cooperation. These communities are a useful testbed for examining population dynamics, allowing one to tease apart the evolution of social behavior, the emergence of stable multispecies ecosystems, and the principles governing cell–cell communication [2–4]. Further, bacteria communicate and respond to a dizzying array of signaling molecules. Cues from neighbors and the abiotic environment inform behavior. Cells must integrate multiple potentially conflicting cues to efficiently react to neighbors’ behaviors and survive in mixed-species communities. A new study by Lories and colleagues [5] in this issue of Current Biology elegantly shows that Salmonella 

typhimurium, a pathogenic bacterium, uses its major stress-response systems to integrate signals of competition, and deploys a coherent response to the challenges of communal life. 

The transition to communal living in a biofilm involves profound changes in gene expression — communities can be hives of activity. These factors make investigation of competition in biofilms tricky to navigate. How does one separate the effects of competition from those associated with the transition to communal living? How does one account for the highly heterogeneous environment found within highly structured biofilms, where neighboring cells can experience different social and environmental pressures? Lories et al. neatly solved many of these issues by using a promoter trap library of S. typhimurium strains, each containing a small section of the chromosome followed by a green fluorescent protein (GFP) reporter. Through this clever experimental design, the authors were able to detect — at single-cell resolution — transcriptional 

changes associated with mixed biofilm formation, thereby avoiding the averaging effects of bulk measurements. 

The mixed-species biofilm model employed by Lories et al. comprised two different S. typhimurium strains, S1 and S2, and the E. coli strain E1. Using confocal microscopy, the authors showed that all three strains made wellmixed biofilms in combination with one another. Biofilms that formed from combinations of strains showed lower cellular yield than those formed from monocultures, indicating that the strains compete with one another in biofilms. However, the strains did not compete with one another in liquid cultures. This pattern of competitive behavior, where strains lowered each others’ fitness only in the close confines of biofilms, showed that cells of each strain were doing more than passively competing for resources. Instead, strains were actively harming each other, a phenomenon known as ‘interference competition’ [4]. 

**==> picture [16 x 17] intentionally omitted <==**

R324 Current Biology 30, R302–R328, April 6, 2020 ª 2020 Elsevier Inc. 

