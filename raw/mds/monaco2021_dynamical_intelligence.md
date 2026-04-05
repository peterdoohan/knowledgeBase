**A brain basis of dynamical intelligence for AI and computational neuroscience** 

Joseph D. Monaco[1] _[∗]_ , Kanaka Rajan[2] , and Grace M. Hwang[3] _[†∗]_ 

**1** Department of Biomedical Engineering, Johns Hopkins University (JHU) School of Medicine, Baltimore, MD, USA; 

**2** Icahn School of Medicine at Mount Sinai, New York, NY, USA; **3** JHU/Applied Physics Lab, Laurel, MD, USA; JHU Kavli Neuroscience Discovery Institute, Baltimore, MD, USA. 

> _†_ This material is based on work supported by (while serving at) the National Science Foundation. Any opinion, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation. 

> _∗_ Correspondence to jmonaco@jhu.edu or grace.hwang@jhuapl.edu. 

## **Abstract** 

The deep neural nets of modern artificial intelligence (AI) have not achieved defining features of biological intelligence, including abstraction, causal learning, and energy-efficiency. While scaling to larger models has delivered performance improvements for current applications, more brain-like capacities may demand new theories, models, and methods for designing artificial learning systems. Here, we argue that this opportunity to reassess insights from the brain should stimulate cooperation between AI research and theory-driven computational neuroscience (CN). To motivate a brain basis of neural computation, we present a dynamical view of intelligence from which we elaborate concepts of sparsity in network structure, temporal dynamics, and interactive learning. In particular, we suggest that temporal dynamics, as expressed through neural synchrony, nested oscillations, and flexible sequences, provide a rich computational layer for reading and updating hierarchical models distributed in long-term memory networks. Moreover, embracing agent-centered paradigms in AI and CN will accelerate our understanding of the complex dynamics and behaviors that build useful world models. A convergence of AI/CN theories and objectives will reveal dynamical principles of intelligence for brains and engineered learning systems. This article was inspired by our symposium on dynamical neuroscience and machine learning at the 6th Annual US/NIH BRAIN Initiative Investigators Meeting. 

## **Main** 

The functional limitations of the current wave of artificial intelligence (AI), based on deploying deep neural nets for perception, language, and reinforcement learning applications, are coming into focus. A recent avalanche of reviews, perspectives, podcasts, virtual seminars, and keynotes have collectively signaled remarkable agreement about brain-like capacities that escape our understanding: abstraction, generalization, and compositionality; causal learning and inference; cognitive flexibility for generalized problem-solving; construction of world models; low sample-complexity and high energy-efficiency. These conversations have 

1/24 

Monaco, Rajan, & Hwang 

not only coursed through the AI and machine learning communities, but also the neuroscience, psychology, cognitive science, robotics, and philosophy of mind communities. As AI may be unlikely to bridge these acknowledged gaps by continuing to simply scale up models, datasets, and training compute, the opportunity arises to return to the brain for insight. 

Neuroscientists have begun to integrate deep neural nets into their methods[1,2] and to search for representations predicted by deep learning[3,4] . The critical question is whether this benefit can be reciprocated: Can our current, albeit incomplete, knowledge of brain-based intelligence translate to meaningful algorithmic innovation in AI? A corollary question is equally important: Could stronger partnerships between neuroscientists and AI researchers help to resolve obstacles in both fields? In this Perspective, we hope to stimulate the search for the critical set of neurobiological features that supports the adaptive intelligence of humans and other animals. Not every biological detail is relevant to the brain’s computational capacities, but the minimal set of idealized neural features in AI leaves the door open to many potential brain-based innovations. We argue that the still adolescent field of _computational neuroscience_ (CN) (see Box 1) should play a key role in this search. 

Given this context, some discussions below might appear overly theoretical. We embrace the fact that, as neuroscientists, we cannot yet point to certain physiological details or write down a set of equations as definitive keys to neural algorithms of intelligence. Instead, we take a step back to synthesize ideas from biology, neuroscience, cognitive science, and dynamical systems to outline a brain basis of neural computation that we think points in the right direction. Thus, we elaborate, in the next section, a working definition of intelligence, and then consider its neural contingencies by addressing network structure, temporal dynamics, and future directions based on interactive learning. These last three sections emphasize distinct perspectives on sparsity. 

## **A dynamical/behavioral view of intelligence** 

While it is difficult to answer “What is intelligence?”, it is almost as useful to answer “What is intelligence _for_ ?”: Intelligence is _for_ adaptive behavior. Otherwise, an organism would have been better off (as in the neuromythology surrounding the sea squirt) ingesting its brain and attaching itself to a rock. A corresponding yardstick for intelligence would be the degree to which an organism or agent controls its environment in service of continued survival[8,9] . Indeed, extending this assessment to novel or unpredicted situations, along ecological dimensions, should correlate with generalized problem-solving capacity[10] . 

This not-unusual definition of intelligence puts AI (based on disembodied and nonagentic neural nets trained on datasets lacking spatial, temporal, epistemic, mnemonic, social, and/or environmental context) at a disadvantage for purposes beyond hypercompetent regression and classification. Behavior is variable and complex, but it is also hierarchically organized through time in all animals, with humans exhibiting perhaps the deepest such hierarchies. Conceptual knowledge is similarly hierarchical and demanding of flexibility, reconfigurability, and combinatoric expressiveness (cf. the _compositionality_ and _systematicity_ of language). Highlevel cognition is ordered, temporal, and dynamical in that what came before conditions the _meaning_ of what comes after, with lifelong horizons in both directions. 

But where is the computational layer? Network _preconfiguration_ and its metabolic advantages preclude basing this dynamism on first-order mechanisms of structural plasticity. For instance, conceptual learning would require regular rebalancing of global connectivity distributions because the linear ‘training 

2/24 

Monaco, Rajan, & Hwang 

## **Box 1. Glossary of terminology.** 

_**afferent/efferent**_ providing input to a given target/carrying output from a given source _**causal invariance class**_ a set of system states that, conditioned on other members of the set, cause the same effect; to support effective causal learning and inference, causal invariance with respect to a discrete or binary outcome, such as the activation of a downstream reader or token, must be understood as an independent causal capacity, i.e., a mechanism, of the class itself [5] _**cell assembly**_ a fundamental but evolving concept in neuroscience that posits connected sets of neurons with topologically closed (‘reentrant’) loops among their synapses that autonomously sustain the cells’ activation; crucially, Hebb realized [6] that such activation would itself modify the loop and potentially find new pathways to distribute, or consolidate, the cell assembly (Fig 1e) _**compositionality**_ the property of symbolic systems that the meaning of complex expressions (e.g., sentences) is completely determined by syntax and the meanings of simple parts _**computational neuroscience**_ the theoretical investigation of computational models of brain function _**computationalism**_ the classical cognitive science theory that minds and brains are information processing systems and that cognition should be understood as computation _**connectome**_ a detailed network connectivity map of an individual brain _**dynamical systems**_ a mathematical approach to the long-term behavior of complex adaptive systems as ensembles of particles whose states obey differential equations over time _**ergodicity**_ the property of a dynamical system that, from any initial state, it will visit all reachable states over the long term, including a return to the initial state; thus, ergodic dynamics are not reducible or decomposable _**ethological relevance**_ the degree to which a situation or experiment aligns with an animal’s natural behavior in ecologically appropriate environments _**hierarchy**_ a coherent organization of transitive superiority relations (‘above’, ‘below’, or ‘equal’) among elements, typically represented as a tree _**meaning**_ internally constructed information with adaptive or ethological relevance to an agent or organism _**minimal models**_ an approach to model design that relies on theory, intuition, and explanatory power to maximally abstract, idealize, and distill complicated systems into a set of essential functions _**network of networks**_ large-scale computational models built from complex recurrent neural networks wherein distinct submodules simultaneously represent different brain regions _**neural inspiration**_ a vacuous notion that allows nearly any system or model to be described as brain-like (cf. ‘biologically plausible’) _**physical layer**_ the material organization of a computer that establishes the lowest level of information processing; mechanisms within the layer may abstract its raw states into the codes and parameters of computation _**preconfiguration**_ the relative multi-scale stability of connectivity patterns in mature brains _**pseudohierarchy**_ our relaxed conception of hierarchy based on arrangements of specialists and generalists that allows some degree of level or modularity violations (Fig 1b) _**quasiattractor**_ a local energy minimum that shapes weakly convergent flows but nonetheless provides access to divergent flows and chaotic states _**readers**_ downstream targets, _viz._ neurons, cell assemblies, tokens, or networks, that respond to configurations of states among their inputs [7]; i.e., they read out brain states and contribute to expressive transformations of internal sequences _**rich club**_ a set of strongly interconnected generalists that acts as a global information hub _**small world**_ the property that average path lengths tend to grow only logarithmically with network size _**spandrel**_ an evolutionary trait that is contingent upon other adaptive traits but not necessarily adaptive itself _**specialists/generalists**_ neurons or networks with high/low prevalence and low/high degrees of convergent (afferent) input; they constitute lower/higher ‘levels’ of the brain’s pseudohierarchy _**systematicity**_ the combinatoric capacity of a compositional system for producing complex expressions _**tokens**_ a mechanistic concept (elaborated below) of a computational unit for the brain, grounded in the physical layer of synaptic memory loops, that bridges low-level dynamics to functional states 

3/24 

Monaco, Rajan, & Hwang 

curriculum’ of experience would at most be capable of incrementally appending leaves to the concept tree during the first (online) stage of standard two-stage memory models[6,11] . This rebalancing would become increasingly necessary, due to finer-grained categories, and increasingly expensive, due to deeper branching. Thus, a different kind of substrate must efficiently maintain, update, and operate on the hierarchical models in long-term memory. We focus on temporal and attractor dynamics as the axes of this computational layer. 

## **Sparse, skewed structures for flexible abstraction and generalization** 

Typically _<_ 1–2% of possible unit-wise connections exist within the cortico-limbic circuits of the hippocampus and neocortex. The impressive combinatorics inherent in this level of sparsity[12] give rise to the intuitive, but perhaps wishful, notion that discovering the underlying motifs, generating functions, or _connectomes_ of synaptic connectivity will unlock the brain’s neural coding secrets. Without such sparsity, dense connectivity (Fig 1a) either reliably relaxes into pattern completion for recurrent models _viz._ Hopfield nets, or universal function approximation for feedforward models _viz._ multi-layer perceptrons and deep learning. Brains appear to do both, but also much more[13,141] . Density, as in typical artificial neural nets (ANNs), collapses the space of possible network configurations to that of size and layer architecture. Having far fewer degrees-of-freedom greatly restricts structural, and thus functional, diversity. As brains evolved, such restricted variation would have shunted the phylogenetic discovery of the inductive biases[14] that now presumably undergird brain function. If so, structural sparsity is an ancient precondition for biological intelligence. 

## **Obstacles for network models with sparse connectivity** 

The recognized importance of anatomical/structural sparsity has taken distinct forms in CN/neuroscience and AI. In neuroscience, a current approach posits that commiditizing connectomes (in the tradition of the genetic sequencing project) will unlock crucial new technologies and potential therapies[15] . Recent advances in AI, including network distillation[16] , lottery tickets[17] , and synaptic flow[18] , have wielded structural sparsity to reduce model complexity in light of Sutton’s cautionary note[19] and concerns about training extremely large models, such as ‘double descent’[20] and environmental sustainability[21] . These reactions reflect the fields’ respective mainstream interests: neuroscience wants neurotechnology capital to keep funding big labs and consortia[22–24] ; AI wants more efficient training to quickly deploy updated models for its trending applications[25,26] . 

First, generalizing from frozen, or static, connectivity patterns is complicated by the ‘synaptic weight’, one of the two main parameters tuned when training an ANN (along with unit bias). The resulting weight matrices determine the gains of unit-wise directed connections in a network. However, the gains of biological synapses as measured from imaging or electrophysiology are in constant flux due to, e.g., homeostatic and neuromodulatory brain states that complement experience-dependent learning in nontrivial ways[27] . At best, synaptic volatility obscures the functional relevance of any particular weight matrix, or learning rule, over meaningful periods of time. In CN modeling, an inherent trade-off between the level of data-driven biological detail and empirical capacities for inference and generalization[28] forces strong assumptions to be made about behavioral and 

4/24 

Monaco, Rajan, & Hwang 

**==> picture [471 x 432] intentionally omitted <==**

**Fig 1. Brain networks are sparse, pseudohierarchical, and distributed with log-skewed connectivity.** The multi-scale neural structures of the brain constitute its physical layer of computation. Typical neural net models acquire sparsity via rectified unit activations, but the brain may take advantage of its sparse pseudohierarchical structures to amplify the computational capacities of neurons and networks. **a** , Dense recurrent and feedforward networks as in Hopfield nets and deep hierarchical neural nets, respectively. **b** , Hierarchies are powerful data structures, but they strictly require binary and unambiguous superiority relations. Neurons and networks inhabit a continuum of input connectivity from _specialists_ to _generalists_ . Sparse, multi-scale arrangements of elements from this skewed distribution will form pseudohierarchical structures with lateral and ascending/descending violations (e.g., level skips). **c** , For ease of visualization, we show a balanced hierarchy with a core subset of strongly interconnected generalist neurons _viz._ a rich club. Hierarchy violations like those in **b** are implied. **d** , The cortico-limbic system comprises networks linked by sparse, long-range hub connections that make a small world from rich clubs. **e** , The flow of cortical computation emanates from self-sustaining activity within the reentrant synaptic loops of interconnected cell assemblies (red circles, 1 and 2). Loops may branch into subloops or aggregate new traces (purple circles, 1 _[′]_ and 2 _[′]_ ) that entail different effects on downstream targets, thus instantiating distinct _tokens_ of neural computation (see below). 

5/24 

Monaco, Rajan, & Hwang 

functional states. These factors preclude highly efficient ANN idealizations like rectified-linear unit activations[29] and backpropagation of error (‘backprop’)[30] . 

Second, whereas synaptic weights fluctuate, the overall pattern of connectivity (in mature, developed brains) is less dynamic. This might appear to boost the value of frozen connectomes, but evidence for numerous conserved, functional brain states across individuals and species through waking and sleep[31,32] implies that any particular connectome (within healthy interindividual variability) underdetermines its associated functional states. Why should this be the case? If metabolic efficiency were an evolutionary driver of structural sparsity[33,34] , then the energetics of functional states that continually reorganized axon collaterals, synaptic boutons, dendritic arbors, etc., would surely be selected against. 

CN network models examine conditions of theory-driven, kernel-based, or sparse-random connectivity, wherein sparsity is typically around 5-10% due to the breakdown of smaller (i.e., computationally feasible) models at more brain-like sparsity. Methods for scaling up CN models include partial inference such as isolated cell-type pre-tuning[35] , multi-region _network of networks_ models[36] , and formal (e.g., mean field or master equation) approaches to mesoscopic dynamics[37,38] . Further, CN models typically study learning rules based on Hebbian association (or similar) and the types of local plasticity mechanisms that have been the focus of experiments. Thus, global update rules like backprop have only recently renewed theoretical attention in neuroscience[39] . 

## **It’s a log-log world (after all)** 

Which properties of cortical connectivity form the computational layer of dynamical intelligence? We highlight two points about connection structure. First, in a sparse cortex, one effect of surprisingly low average path lengths[40] is global inter-regional accessibility. This _small world_ network property[41] can emerge developmentally, via activity-dependent pruning, from simple rules in dynamically synchronous populations[42,43] . The resulting logarithmic scaling of _efferent_ connections forms coherent local neighborhoods with efficient access to any other neighborhood in the cortical sheet. Second, in a hierarchical cortex, the connectivity graph, between neurons or minicolumns, need not be strictly isomorphic to a tree in the computer science sense. In fact, a cortical B-tree would be unacceptably fragile toward the root node due to poor distribution of connections. 

Indeed, general conceptual knowledge and remote memories are more robustly accessible than their specific and recent counterparts, likely from having aggregated multiple traces, grounded in the medial temporal lobe and hippocampal-entorhinal cortical complex[11,44–46] . Consequently, while we refer to the cortico-limbic long-term memory graph as a _hierarchy_ , systems consolidation implies that the graph is more like a distributed multi-scale arrangement of neurons and networks along a continuum of _afferent_ input convergence, i.e., from _specialists_ to _generalists_ (Fig 1b). Indeed, studies of mature preconfigured memory networks revealed, again, log-skewed distributions with long tails of more excitable generalist neurons[47–49] . The generalist neurons and networks can organize, despite their smaller numbers, into highly stable _rich clubs_[50–53] that serve to robustly distribute the higher levels of the hierarchy (Fig 1c). Thus, small world output (i.e., log-skewed efferent access) and rich club input (i.e., log-skewed afferent tuning) may constitute a slide-rule-like _physical layer_ of computation (Fig 1d) for flexible abstraction and generalization. 

6/24 

Monaco, Rajan, & Hwang 

## **Complex temporal dynamics for computational sequences of sparse states** 

In contrast to the timing agnosticism of classical _computationalism_ , the dynamical/behavioral view of intelligence prioritizes timing (vs. order): The right behavior at the wrong time is equally deadly as the wrong behavior, because it is nonetheless coupled to the rest of the world. That the phylogeny of biological intelligence is a story of interacting with the world emphasizes cognition as an internal physical process that unfolds through time to manage this inextricable coupling to external forces. The analysis of mechanistic couplings over time is the domain of _dynamical systems_ theory. Thus, a dynamical systems perspective has emerged[54–67] within cognitive science, philosophy of mind, and neuroscience, wherein “[c]ognition is then seen as the simultaneous, mutually influencing unfolding of complex temporal structures”[56] . 

Respecting the transparency of temporal variation unlocks a crucial dimension along which to organize and interrelate neural events. Continuous-time networks of dynamical spiking neuron models robustly demonstrate self-organized synchronous groupings that expand functional capacities[68,69] (Fig 2a) and provide a stronger causal basis for empirical explanation[70,71] compared to discrete, rate-based ANNs and similar _minimal models_ in CN. The ‘rate vs. time’ argument about neural coding goes back at least 50 years[72] and has mostly revealed new ways for theorists to talk past each other. Thus, the dynamical systems view emphasizes spike timing (vs. firing rates) because temporal relationships (1) allow causal mechanisms to continuously unfold in sequence[56] and (2) avoid the observer bias inherent in calculating time-binned average firing rates[71,73] . 

## 

If interaction is the net effect of intelligence and behavior is deeply hierarchical, then we might expect the neural mechanisms of intelligence to vary over a hierarchy that is functionally isomorphic to that of behavior. By construing this variation as temporal, oscillations and neural synchrony become candidates for this isomorphism, particularly on the basis of oscillatory nesting between timescales (Fig 2b). To illustrate the _why_ and _how_ of functional oscillations, we sketch several findings: 

- Observed frequency bands span from circadian (1 day) and ultradian (90 min) periods through infraslow (1/10 Hz) and slow (1 Hz) cycles up to theta (4–8 Hz), alpha (8–12 Hz), beta (12–30 Hz), and gamma (30–100 Hz) oscillations, and transient ripples (100–200 Hz)[75] ; 

- The frequency ratios between successive bands are approximately ( _∼ e_ ) constant[76] ; i.e., they follow logarithmic intervals, minimizing overlap and harmonic interference; 

- Slower oscillations maintain spatial coherence over larger regions, and no mammalian oscillation has been found that was not nested in the cycles of a slower oscillation, e.g., via the phase-amplitude form of cross-frequency coupling (CFC)[48,77–79] , thus forming a spatiotemporal hierarchy; 

- The foregoing properties, including approximate frequencies, are evolutionarily conserved across mammals, scaling from the brains of shrews to baleen whales over three orders-of-magnitude[48,75] ; 

7/24 

Monaco, Rajan, & Hwang 

**==> picture [471 x 212] intentionally omitted <==**

**Fig 2. Phase synchronization and nested oscillations can sequence, segregate, and communicate.** Robust neural mechanisms for transforming inputs into timing signals aligned to ongoing oscillations (i.e., phase codes) may organize neural activity into computationally ordered sequences and inter-regional communication channels. **a** , (Top) The spike timing of a model neuron reveals a phase-rate code for a slowly ramping input (green). This phase dependence arises from an oscillatory input (inhibitory, pink) such as from a theta-rhythmic interneuron. (Bottom) A simple extension of this model to a circuit with two bursting cell types (purple vs. orange, left) demonstrates that input level controls the oscillatory phase of bursts emitted by the circuit (133-ms theta cycles, right). Adapted from Monaco et al. (2019) [74] as permitted by the CC-BY 4.0 International License (creativecommons.org/licenses/by/4.0/). **b** , Nested oscillations consist of a fast oscillator (FO) whose amplitude is modulated by the phase of a slow oscillation (SO). The broader spatial coherence of the SO means that it may influence more remote levels of the cortical pseudohierarchy (Fig 1b). For example, a communication request may be initiated by a specialist (green) that successfully resets the SO phase-angle (cyan circles with arrow) of a generalist (blue), which then customizes a FO sequence (purple double-arrow) for the input-receptive SO phase of the specialist. Readers, like this generalist, may use phase-amplitude coupling to flexibly and selectively communicate with their inputs (e.g., _Channel 1_ vs. _Channel 2_ ). Thus, temporal dynamics within an oscillatory hierarchy may support crucial neurocomputational capacities. 

8/24 

Monaco, Rajan, & Hwang 

- Detailed CN models of the locally recurrent excitatory/inhibitory (E/I) networks prevalent in cortico-limbic areas demonstrate robust emergence of rhythmic synchrony based on relative E/I gains and synaptic timeconstants[80–84] ; 

- Input drive may balance E/I currents to produce _desynchronized_ (e.g., low-amplitude gamma) activity[85–87] in networks that otherwise relax into _synchronized_ (e.g., high-amplitude alpha) states[88,89] . 

In AI, attempts to incorporate timing have reductively mapped stochasticity to dropout[90] , continuous dynamics to spikes or binary activation[91–93] , and nonlinear recurrence to memory gates[94,95] . In the brain, however: variability should not be confused with noise; spikes can be understood as autonomous oscillations that can be nested within bursts or ripples[96,97] , suggesting they are the root of the oscillatory hierarchy; and biological recurrence foments the chaos of total history-dependence, presciently described in 1919 by the French zoologist Yves Delage (as quoted by Buzs´aki [48, p. 85]), “the neuron’s vibratory mode as a result of its coaction with others leaves a trace that is more or less permanent in the vibratory mode resulting from its hereditary structures and from the effects of its previous coactions.” 

What is the function of hierarchically nested oscillations? Dynamics unfolding through time are about sequences and sequences are about computationally ordered trajectories of states. That is, nested oscillations may _read out chunks_ of the long-term hierarchical models described above. Brain oscillations are weakly chaotic, meaning that the slower oscillation of a nested pair can quickly ( _<_ 1 cycle) entrain a remote brain area into a sender/receiver channel defined by the direction of nonzero phase lags[48,98–101] . Over large networks, directional gradients in coupling frequency[102] might coordinate macroscale dynamical flows as traveling or rotating waves[103–107] . A recent intervention study of transcranial stimulation in humans showed that prefrontal cognitive functions were distinctly modulated by CFC-like stimulation in separate bands[108] . Thus, while large waves (and nonspecific modulation) broadly promote synchrony, temporal phase-organization is what allows readers to flexibly select from among their inputs[74] (Fig 2b). 

## **Syntactic causal tokens as the unit of cortical computation** 

The above findings suggest a candidate function for dynamical sparsity: Temporal dynamics sparsely activate discrete, distributed _tokens_ from the structural world model, and then recursively, compositionally, and systematically sequence those tokens into higher-order cognitive processes (cf. theories of neural syntax[7,79] , linguistic construction schema[109,110] , and conceptual cognitive maps[111–114] ). To motivate this concept of tokens, we note that a dynamical unit of computation should be discrete (i.e., bounded in state space), syntactic (i.e., intrinsically formal), and mechanistic (i.e., grounded in causal interactions of its substrate). Tokens encapsulate active computational states, in contrast to latent memory states considered as reentrant loops in the synaptic pathways of cortico-limbic networks (Fig 1e) _viz._ the Lashley-Hebb _cell assembly_[6] . 

We define tokens as classes of syntactic neural states that (1) transiently selfsustain activation and (2) competitively suppress accessible successor tokens. We posit that token discretization arises from the activation of structurally segregated latent memory states into dynamically integrated _causal invariance classes_ with respect to downstream effects (Fig 1e). For a given latent memory state, a token is the class of active states that _ergodically_ self-reinforces the reentrant flow through its 

9/24 

Monaco, Rajan, & Hwang 

synaptic pathways, conditioned on its targets, or _readers_[7] . Thus, tokens are discrete functional states guided by multi-scale _quasiattractors_ of the brain’s complex energy landscape[13,49,74,115–123] . 

Why are neural tokens necessary? First, the causal invariance constraint serves to mechanistically ground the computational layer[59,63] and provides essential scaffolding for adaptive causal learning[5] . Second, to embed the Lashley-Hebb cell assembly[6] into the oscillatory hierarchy described above, we needed to recast its assumption of binding via simultaneous firing[124] . Given temporal dynamics beyond simultaneity, instantaneous active states are no longer identified with their latent memory states. Tokens span this ontological gap by mapping the periattractor transits of dynamical microstates to causal units of computation. 

## **Computing with flexible, composable sequences of quasiattractors** 

If neural tokens are indeed the functional unit of cortical computation and cognition, then their attractor-driven stability must be continually broken. A recent contraction-theoretic analysis showed that dynamic stabilization of sparse recurrent networks may require nonassociative (anti-Hebbian or inhibitory) plasticity[125] ; however, CN models have shown that short-term plasticity, including synaptic depression[126,127] and neuronal adaptation[128–131] , can robustly destabilize active states and facilitate sequence production, even without the asymmetric connectivity relied upon by earlier models of sequence learning. Yet, how is the next token selected for activation? Flexible, expressive sequence generators must have access to novel, divergent paths, but the neurocomputational mechanisms of this access remain unclear. Several theoretical frameworks and models provide useful insights, including distributed inference[132] , local context[133,134] , modular latching[129,135] , metastability[136] , winnerless competition[64] , and chaotic itinerancy[137,138] , wherein the orbits of neural tokens might follow quasiattractors that fluctuate within nested oscillatory cycles. Nonetheless, these bottom-up sequences will necessarily be guided and sculpted by cortical control flow, perhaps implemented by minicolumn circuits[139] , to support inference, composition, and other cognitive processes. Thus, the waking cyclical production of internal token sequences provides the “bicycle for the mind” for the brain (apologies to S. Jobs). Riding this bicycle will require new theories and models of joint temporal-attractor dynamics in biological and artificial systems. For instance, a recent model from two of the authors demonstrated self-organized swarm control with phase-coupling and attractor dynamics[140] . 

## **Future directions: Breaking the learning impasse with sparse, interactive behavior** 

## 

It is not enough to abstract or idealize some function, like attractor sequences, to declare a biological basis of intelligence. Miłkowski (2013)[59] presents a mechanistic account of neural computation by requiring complete causal descriptions of the neural phenomena that produce those functions, because those capacities arise from constitutive mechanisms grounded in brain organization (of which, e.g., the connectome is only one aspect). In this account, computational functions must “bottom out”[63] within mechanistic sublevels to both isolate and limit the external dependencies of computational states. If this is the case, then our history of scientific uncertainty about the organizational levels wherein cortical computations bottom out means that the minimalist _neural inspiration_ for early connectionist 

10/24 

Monaco, Rajan, & Hwang 

ANNs was likely an early-stopping mistake. Given the state of brain science in the time of Pitts and Rosenblatt, and even the 1980s, connectionist abstractions necessarily settled at more general, less explanatory levels. 

AI models evolved to substitute many-layered hierarchies for biological complexity, while protecting the critical path of backprop because of its “unreasonable effectiveness” (apologies to R. Hamming). That strategy is paid for by the exorbitant training complexity of computational systems that are essentially open in high dimensions (i.e., blank slates); several recent models showed that this trade-off can be mitigated with relevant biological priors[14,142,143] . However, the use of technology, in introducing GPUs to avoid the von Neumann bottleneck[90] , triggered an entrenchment of hardware and software codesign that at least rhymes with history[144] . The impressive recent progress in AI applications has conditioned its models on backprop and a competitive benchmarking culture. Without relaxing those conditions, the search for qualitatively new models will remain disincentivized[145] and inductive theoretical interpretation will suffer as _spandrels_ become more common, such as the inexplicable outperformance of the Adam optimizer with default parameters. 

Experimental neuroscience has become similarly trapped. Advancing neurotechnologies[23] have entrenched the blinkered reductionism of necessaryand-sufficient circuit explanations for experimenter-relative ‘behavior’[146,147] . The linear causality implicit in this paradigm provides inferences without guarantee of _ethological relevance_ . Thus, we must admit the circular causality of dynamical control and action-perception loops that subserve the behavioral teleology of intelligent animals[148,149] . 

## **Interactive, agentic learning is global learning** 

Animals are agents and, as such, have high-level goals; they behave so as to reliably achieve those goals[150–152] . This agentic view favors a system of goaldirected behavior based on a simultaneous coupling of internal simulation (i.e., prediction) and external interaction (i.e., error correction). Indeed, a predictive coding analysis of canonical cortical circuits revealed that beta and gamma oscillations may, respectively, carry such prediction and error signals[153] . This oscillatory division-of-labor is consistent with a “spectral connectome” for internal generative models[9,52,154–156] and a recent striking discovery of a beta-band hippocampal mode that emits reversed sequences[157] . Corroboration of unifying theories may require new methods and practices for running experiments in naturalistic environments that promote authentic interactions, as demonstrated by an innovative study of rats that happily learned to play hide-and-seek with human experimenters[158] . Open-loop experiments like this can provide rich complementary datasets to help constrain complex models and improve the generality of causal inferences in neuroscience. Recent advances in AI have embraced agentic interaction, rich environments, and especially play[159] , but these feats have depended on rule-based games with quantified rewards[160,161] . Humans and other animals play lifelong games involving unpredicted situations and ambiguous or unquantifiable outcomes. Thus, both AI and CN would benefit from the roboticists’ focus on how agents actively construct meaningful world models and prioritize behaviors according to self-confidence in beliefs and predictions. 

Animals learn continually, but not continuously. Experience is punctuated by learning bouts driven by conjunctions of global states including arousal and attention. These global states emanate from the subcortex, particularly highly-conserved brainstem structures that modulate awareness and intentional action[163–165] . For example, one of the authors previously showed that rats’ 

11/24 

Monaco, Rajan, & Hwang 

**==> picture [471 x 221] intentionally omitted <==**

**Fig 3. Animals are agents that use behavior to learn from discrete interactions.** We illustrate the punctuated, action-oriented nature of biological learning by describing a study of lateral head-scanning and hippocampal place fields in rats (Monaco et al. (2014) [162]). To elucidate long-term episodic memories, it is critical to understand how cognitive maps in the hippocampus change over time. (Photo) Behavioral observations of rats on circular tracks led to the hypothesis that lateral head-scanning movements during pauses in running may influence place cells. (Bottom left) Quantification of pause behaviors allowed isolation of head scans. (Top right) Place-cell activity was quantified on a lap-to-lap basis to detect the initial formation or abrupt strengthening of individual place fields. Statistical analysis demonstrated a highly predictive and specific relationship between unexpectedly high levels of spiking during a head scan and the formation or potentiation of a place field at that location on the next lap. Example plots show scan spikes (blue) and place-field spikes (red) for a scan-potentiation event on lap 6 (cf. radial firing-rate plots, before vs. after; peak rate in spikes/s). (Bottom right) By unrolling 20 laps of spikes from 5 simultaneously recorded place cells in a novel room, it can be seen that every instance of strong scan firing (blue dotted boxes) was followed by a new place field (pink dotted boxes) on the next lap. Thus, over several minutes, these cells were only recruited into the emerging map in precise conjunction with volitional, attentive actions of the rat. 

12/24 

Monaco, Rajan, & Hwang 

hippocampal place-cell maps are abruptly modified during discrete, attentive head-scanning behaviors[162] (Fig 3). Recent CN models have shown that this kind of sparse, action-driven plasticity may facilitate active inference for learning parsimonious and effective world models[166,167] . In contrast, neuroscientific knowledge is most complete for local plasticity mechanisms at the microscales of transcription, biophysics, and synaptic ultrastructure. These low-level details are compounded by additional complexities of cell-type diversity, the role of microglia in pruning connections, nonlinear integration in dendritic arbors, etc. Whereas AI profits from the global efficiency of backprop, CN has allowed neurobiological complexity and a bias for local associative plasticity to obscure theories of global learning in the brain. Steps toward an agentic modeling paradigm for CN and (non-reinforcement learning) AI might include global, ethologically relevant learning signals from agent-equivalents of volitional behaviors, sympathetic arousal, homeostatic errors, or attentional saliency. 

## **A dynamical future for AI and computational neuroscience** 

A recently announced US/NSF Emerging Frontiers in Research and Innovation program, called BRAID[168] , will be positioned to support innovative convergent approaches to engineered learning systems with brain-like energy efficiency based on codesign of neural theories, algorithms, and hardware, the latter of which has undergone rapid iteration based on innovations including hardware simulation, event-based sensory inputs, and structured dendrites[169–173] . Promising neural adaptations of backprop include the relaxation dynamics of equilibrium propagation[174,175] ; compartmentalization of errors in dendrites, cell populations, or feedback pathways[39,176,177] ; and gradient descent based on diffusive celltype-specific neuropeptide signals[178] . CN research would likewise benefit from increased adoption of computational practices from AI to promulgate transparency, reproducibility and replicability, and large-scale model inference _viz._ automated testing and hyperparameter optimization, architecture search, regularization, and cross-validation. A mechanistic understanding of the intertwined concepts of sparsity in network structure, temporal dynamics, and learning behaviors will help unravel the biological basis of cognitive computations in humans and other animals. An AI/CN consilience will accelerate our discovery of shared dynamical principles of intelligence. 

## **Acknowledgments** 

This work was supported by NSF NCS/FO 1835279 (JDM and GMH), NSF NCS/FO 1926800 (KR), BRAIN Initiative NIH NINDS UF1NS111695 (JDM), and NIH NINDS R03NS109923 (JDM). Further support to KR was provided by the Understanding Human Cognition Scholar award from the McDonnell Foundation. Further support to GMH was provided by the JHU Kavli Neuroscience Discovery Institute, JHU/APL Innovation and Collaboration Janney Program, and National Science Foundation (see author footnote). This article was inspired by open-ended and elucidating discussions with our BRAIN Initiative symposium panelists, Xaq Pitkow, Brad Pfeiffer, Konrad Kording, and Nathaniel Daw, all of whom commented on early versions. The authors thank Patryk Laurent for insightful feedback on the manuscript. 

13/24 

Monaco, Rajan, & Hwang 

## **References** 

1. Storrs, K. R. & Kriegeskorte, N. Deep learning for cognitive neuroscience. _arXiv preprint arXiv:1903.01458_ (2019). 

2. Mathis, M. W. & Mathis, A. Deep learning tools for the measurement of animal behavior in neuroscience. _Current Opinion in Neurobiology_ **60** , 1–11 (2020). 

3. Cadieu, C. F. _et al._ Deep neural networks rival the representation of primate IT cortex for core visual object recognition. _PLOS Computational Biology_ **10** , 1–18 (2014). 

4. Yamins, D. L. K. & DiCarlo, J. J. Using goal-driven deep learning models to understand sensory cortex. _Nature Neuroscience_ **19** , 356–365 (2016). 

5. Cheng, P. W. & Lu, H. Causal invariance as an essential constraint for creating a causal representation of the world. In _The Oxford Handbook of Causal Reasoning_ , chap. 5, 65–84 (Oxford University Press, New York, NY, 2017). 

6. Nadel, L. & Maurer, A. Recalling Lashley and reconsolidating Hebb. _Hippocampus_ **30** , 776–793 (2020). 

7. Buzs´aki, G. Neural syntax: cell assemblies, synapsembles, and readers. _Neuron_ **68** , 362–85 (2010). 

8. Friston, K. Life as we know it. _Journal of The Royal Society Interface_ **10** , 20130475 (2013). 

9. Parr, T. & Friston, K. J. The anatomy of inference: Generative models and brain structure. _Frontiers in Computational Neuroscience_ **12** , 90 (2018). 

10. Chollet, F. On the measure of intelligence. _arXiv preprint arXiv:1911.01547_ (2019). 

11. Nadel, L. & Moscovitch, M. Memory consolidation, retrograde amnesia and the hippocampal complex. _Current Opinion in Neurobiology_ **7** , 217–227 (1997). 

12. Treves, A. & Rolls, E. T. What determines the capacity of autoassociative memories in the brain? _Network: Computation in Neural Systems_ **2** , 371–397 (1991). 

13. Barack, D. L. & Krakauer, J. W. Two views on the cognitive brain. _Nature Reviews Neuroscience_ **[Epub ahead of print]** (2021). 

14. Sinz, F. H., Pitkow, X., Reimer, J., Bethge, M. & Tolias, A. S. Engineering a less artificial intelligence. _Neuron_ **103** , 967–979 (2019). 

15. Fornito, A., Zalesky, A. & Breakspear, M. The connectomics of brain disorders. _Nature Reviews Neuroscience_ **16** , 159–172 (2015). 

16. Burda, Y., Edwards, H., Storkey, A. & Klimov, O. Exploration by random network distillation. _arXiv preprint arXiv:1810.12894_ (2018). 

17. Frankle, J. & Carbin, M. The lottery ticket hypothesis: Finding sparse, trainable neural networks (2019). 

14/24 

Monaco, Rajan, & Hwang 

18. Tanaka, H., Kunin, D., Yamins, D. L. & Ganguli, S. Pruning neural networks without any data by iteratively conserving synaptic flow. _arXiv preprint arXiv:2006.05467_ (2020). 

19. Sutton, R. The Bitter Lesson (2019). URL http://www. incompleteideas.net/IncIdeas/BitterLesson.html. 

20. Nakkiran, P. _et al._ Deep double descent: Where bigger models and more data hurt. _arXiv preprint arXiv:1912.02292_ (2019). 

21. Thompson, N. C., Greenewald, K., Lee, K. & Manso, G. F. The computational limits of deep learning. _arXiv preprint arXiv:2007.05558_ (2020). 

22. Litvina, E. _et al._ BRAIN Initiative: Cutting-edge tools and resources for the community. _Journal of Neuroscience_ **39** , 8275–8284 (2019). 

23. Hsu, N. S. _et al._ The promise of the BRAIN initiative: NIH strategies for understanding neural circuit function. _Current Opinion in Neurobiology_ **65** , 162–166 (2020). 

24. Wool, L. E. Knowledge across networks: how to build a global neuroscience collaboration. _Current Opinion in Neurobiology_ **65** , 100–107 (2020). 

25. Brown, T. B. _et al._ Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ (2020). 

26. Schick, T. & Sch¨utze, H. It’s not just size that matters: Small language models are also few-shot learners. _arXiv preprint arXiv:2009.07118_ (2021). 

27. Mongillo, G., Rumpel, S. & Loewenstein, Y. Intrinsic volatility of synaptic connections — a challenge to the synaptic trace theory of memory. _Current Opinion in Neurobiology_ **46** , 7–13 (2017). 

28. Levenstein, D. _et al._ On the role of theory and modeling in neuroscience. _arXiv preprint arXiv:2003.13825_ (2020). 

29. Glorot, X., Bordes, A. & Bengio, Y. Deep sparse rectifier neural networks. In _Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics_ , 315–323 (2011). 

30. Ahmad, S. & Scheinkman, L. How can we be so dense? The benefits of using highly sparse representations. _arXiv preprint arXiv:1903.11257_ (2019). 

31. McCormick, D. A., Nestvogel, D. B. & He, B. J. Neuromodulation of brain state and behavior. _Annual Review of Neuroscience_ **43** , 391–415 (2020). 

32. Jacobs, E. A. K., Steinmetz, N. A., Peters, A. J., Carandini, M. & Harris, K. D. Cortical state fluctuations during sensory decision making. _Current Biology_ **30** , P4944–4955.e7 (2020). 

33. Attwell, D. & Laughlin, S. B. An energy budget for signaling in the grey matter of the brain. _Journal of Cerebral Blood Flow & Metabolism_ **21** , 1133–1145 (2001). 

34. Levy, W. B. & Calvert, V. G. Communication consumes 35 times more energy than computation in the human cortex, but both costs are needed to predict synapse number. _Proceedings of the National Academy of Sciences_ **118** (2021). 

15/24 

Monaco, Rajan, & Hwang 

35. Markram, H. _et al._ Reconstruction and simulation of neocortical microcircuitry. _Cell_ **163** , 456–492 (2015). 

36. Perich, M. G. & Rajan, K. Rethinking brain-wide interactions through multi-region ‘network of networks’ models. _Current Opinion in Neurobiology_ **65** , 146–151 (2020). 

37. Leen, T. K., Friel, R. & Nielsen, D. Approximating distributions in stochastic learning. _Neural Networks_ **32** , 219–228 (2012). 

38. Zerlaut, Y., Chemla, S., Chavane, F. & Destexhe, A. Modeling mesoscopic cortical dynamics using a mean-field model of conductance-based networks of adaptive exponential integrate-and-fire neurons. _Journal of Computational Neuroscience_ **44** , 45–61 (2018). 

39. Lillicrap, T. P., Santoro, A., Marris, L., Akerman, C. J. & Hinton, G. Backpropagation and the brain. _Nature Reviews Neuroscience_ (2020). 

40. Sporns, O. _Networks of the Brain_ (MIT press, 2010). 

41. Watts, D. J. & Strogatz, S. H. Collective dynamics of ‘small-world’ networks. _Nature_ **393** , 440–442 (1998). 

42. Kwok, H. F., Jurica, P., Raffone, A. & van Leeuwen, C. Robust emergence of small-world structure in networks of spiking neurons. _Cognitive Neurodynamics_ **1** , 39 (2006). 

43. Jarman, N., Trengove, C., Steur, E., Tyukin, I. & van Leeuwen, C. Spatially constrained adaptive rewiring in cortical networks creates spatially modular small world architectures. _Cognitive Neurodynamics_ **8** , 479–497 (2014). 

44. Barsalou, L. W. Perceptual symbol systems. _Behavioral and brain sciences_ **22** , 577–660 (1999). 

45. Haist, F., Gore, J. B. & Mao, H. Consolidation of human memory over decades revealed by functional magnetic resonance imaging. _Nature Neuroscience_ **4** , 1139–1145 (2001). 

46. Mok, R. M. & Love, B. C. Abstract neural representations of category membership beyond information coding stimulus or response. _Journal of Cognitive Neuroscience_ 1–17 (2021). 

47. Buzs´aki, G. & Mizuseki, K. The log-dynamic brain: how skewed distributions affect network operations. _Nat Rev Neurosci_ **15** , 264–78 (2014). 

48. Buzs´aki, G. _The Brain from Inside Out_ (Oxford University Press, Oxford, UK, 2019). 

49. McKenzie, S. _et al._ Preexisting hippocampal network dynamics constrain optogenetically induced place fields. _Neuron_ **109** , 1040–1054.e7 (2021). 

50. van den Heuvel, M. P. & Sporns, O. Rich-club organization of the human connectome. _The Journal of Neuroscience_ **31** , 15775 (2011). 

51. Binicewicz, F. Z. M., van Strien, N. M., Wadman, W. J., van den Heuvel, M. P. & Cappaert, N. L. M. Graph analysis of the anatomical network organization of the hippocampal formation and parahippocampal region in the rat. _Brain Struct Funct_ (2015). 

16/24 

Monaco, Rajan, & Hwang 

52. Dann, B., Michaels, J. A., Schaffelhofer, S. & Scherberger, H. Uniting functional network topology and oscillations in the fronto-parietal single unit network of behaving primates. _eLife_ **5** , e15719 (2016). 

53. Rees, C. L. _et al._ Graph theoretic and motif analyses of the hippocampal neuron type potential connectome. _eNeuro_ **3** , ENEURO.0205–16.2016 (2016). 

54. Skarda, C. A. & Freeman, W. J. How brains make chaos in order to make sense of the world. _Behavioral and Brain Sciences_ **10** , 161–173 (1987). 

55. van Gelder, T. What might cognition be, if not computation? _Journal of Philosophy_ **92** , 345–381 (1995). 

56. van Gelder, T. The dynamical hypothesis in cognitive science. _Behavioral and brain sciences_ **21** , 615–628 (1998). 

57. Freeman, W. J. Neurodynamic models of brain in psychiatry. _Neuropsychopharmacology_ **28 Suppl 1** , S54–63 (2003). 

58. Izhikevich, E. M. _Dynamical systems in neuroscience: The geometry of excitability and bursting_ (MIT Press, Cambridge, MA, 2007). 

59. Miłkowski, M. _Explaining the computational mind_ (MIT Press, 2013). 

60. Aihara, K. _et al. Cognitive Phase Transitions in the Cerebral Cortex-Enhancing the Neuron Doctrine by Modeling Neural Fields_ (Springer, 2015). 

61. Rabinovich, M. I., Simmons, A. N. & Varona, P. Dynamical bridge between brain and mind. _Trends Cogn Sci_ **19** , 453–61 (2015). 

62. Jonas, E. & Kording, K. P. Could a neuroscientist understand a microprocessor? _PLoS Comput Biol_ **13** , e1005268 (2017). 

63. Miłkowski, M. From computer metaphor to computational modeling: The evolution of computationalism. _Minds and Machines_ **28** , 515–541 (2018). 

64. Rabinovich, M. I. & Varona, P. Discrete sequential information coding: Heteroclinic cognitive dynamics. _Front Comput Neurosci_ **12** , 73 (2018). 

65. Mastrogiuseppe, F. & Ostojic, S. Linking connectivity, dynamics, and computations in low-rank recurrent neural networks. _Neuron_ **99** , 609–623.e29 (2018). 

66. Dannenberg, H., Alexander, A. S., Robinson, J. C. & Hasselmo, M. E. The role of hierarchical dynamical functions in coding for episodic memory and cognition. _Journal of Cognitive Neuroscience_ 1–19 (2019). 

67. Vyas, S., Golub, M. D., Sussillo, D. & Shenoy, K. V. Computation through neural population dynamics. _Annual Review of Neuroscience_ **43** , 249–275 (2020). 

68. Izhikevich, E. M. Polychronization: computation with spikes. _Neural Comput_ **18** , 245–82 (2006). 

69. Kilpatrick, Z. P. & Ermentrout, B. Sparse gamma rhythms arising through clustering in adapting neuronal networks. _PLOS Computational Biology_ **7** , 1–17 (2011). 

17/24 

Monaco, Rajan, & Hwang 

70. Brette, R. Computing with neural synchrony. _PLoS Comput Biol_ **8** , e1002561 (2012). 

71. Brette, R. Philosophy of the spike: Rate-based vs. spike-based theories of the brain. _Front Syst Neurosci_ **9** , 151 (2015). 

72. Perkel, D. H. & Bullock, T. H. Neural Coding - A report based on an NRP work session. Technical Report 19690022317, Neuroscience Research Program, Brookline, MA (1968). 

73. Brette, R. Is coding a relevant metaphor for the brain? _Behav Brain Sci_ 1–44 (2019). 

74. Monaco, J. D., De Guzman, R. M., Blair, H. T. & Zhang, K. Spatial synchronization codes from coupled rate-phase neurons. _PLoS Comput Biol_ **15** , e1006741 (2019). 

75. Buzs´aki, G., Logothetis, N. & Singer, W. Scaling brain size, keeping timing: Evolutionary preservation of brain rhythms. _Neuron_ **80** , 751–764 (2013). 

76. Penttonen, M. & Buzs´aki, G. Natural logarithmic relationship between brain oscillators. _Thalamus & Related Systems_ **2** , 145–152 (2003). 

77. Canolty, R. T. _et al._ High gamma power is phase-locked to theta oscillations in human neocortex. _Science_ **313** , 1626–1628 (2006). 

78. Aru, J. _et al._ Untangling cross-frequency coupling in neuroscience. _Current Opinion in Neurobiology_ **31** , 51–61 (2015). 

79. Hyafil, A., Giraud, A.-L., Fontolan, L. & Gutkin, B. Neural cross-frequency coupling: Connecting architectures, mechanisms, and functions. _Trends in Neurosciences_ **38** , 725–740 (2015). 

80. Wang, X. J. & Buzs´aki, G. Gamma oscillation by synaptic inhibition in a hippocampal interneuronal network model. _J Neurosci_ **16** , 6402–13 (1996). 

81. Whittington, M. A., Traub, R. D., Kopell, N., Ermentrout, B. & Buhl, E. H. Inhibition-based rhythms: experimental and mathematical observations on network dynamics. _Int J Psychophysiol_ **38** , 315–36 (2000). 

82. Geisler, C., Brunel, N. & Wang, X.-J. Contributions of intrinsic membrane dynamics to fast network oscillations with irregular neuronal discharges. _J Neurophysiol_ **94** , 4344–61 (2005). 

83. Buzs´aki, G. & Wang, X.-J. Mechanisms of gamma oscillations. _Annu Rev Neurosci_ **35** , 203–25 (2012). 

84. Verduzco-Flores, S. O., Bodner, M. & Ermentrout, B. A model for complex sequence learning and reproduction in neural populations. _J Comput Neurosci_ **32** , 403–23 (2012). 

85. Hennequin, G., Vogels, T. P. & Gerstner, W. Optimal control of transient dynamics in balanced networks supports generation of complex movements. _Neuron_ **82** , 1394–1406 (2014). 

86. Zerlaut, Y. & Destexhe, A. Enhanced responsiveness and low-level awareness in stochastic network states. _Neuron_ **94** , 1002–1009 (2017). 

18/24 

Monaco, Rajan, & Hwang 

87. Ahmadian, Y. & Miller, K. D. What is the dynamical regime of cerebral cortex? _arXiv preprint arXiv:1908.10101_ (2019). 

88. Pfurtscheller, G., Stanc´ak, A. & Neuper, C. Event-related synchronization (ERS) in the alpha band — an electrophysiological correlate of cortical idling: A review. _International Journal of Psychophysiology_ **24** , 39–46 (1996). 

89. Parish, G., Hanslmayr, S. & Bowman, H. The Sync/deSync model: How a synchronized hippocampus and a desynchronized neocortex code memories. _Journal of Neuroscience_ **38** , 3428–3440 (2018). 

90. Krizhevsky, A., Sutskever, I. & Hinton, G. E. ImageNet classification with deep convolutional neural networks. In _Advances in neural information processing systems_ , 1097–1105 (2012). 

91. Lee, J. H., Delbruck, T. & Pfeiffer, M. Training deep spiking neural networks using backpropagation. _Frontiers in Neuroscience_ **10** , 508 (2016). 

92. Tavanaei, A. & Maida, A. BP-STDP: Approximating backpropagation using spike timing dependent plasticity. _Neurocomputing_ **330** , 39–47 (2019). 

93. Kheradpisheh, S. R., Mirsadeghi, M. & Masquelier, T. BS4NN: Binarized spiking neural networks with temporal coding and learning. _arXiv preprint arXiv:2007.04039_ (2020). 

94. Hochreiter, S. & Schmidhuber, J. Long Short-Term Memory. _Neural Computation_ **9** , 1735–1780 (1997). 

95. Chung, J., Gulcehre, C., Cho, K. & Bengio, Y. Empirical evaluation of gated recurrent neural networks on sequence modeling. _arXiv preprint arXiv:1412.3555_ (2014). 

96. Buzs´aki, G. Hippocampal sharp wave-ripple: a cognitive biomarker for episodic memory and planning. _Hippocampus_ **25** , 1073–88 (2015). 

97. Kay, K. & Frank, L. M. Three brain states in the hippocampus and cortex. _Hippocampus_ **29** , 184–238 (2019). 

98. Colgin, L. L. Theta–gamma coupling in the entorhinal–hippocampal system. _Current Opinion in Neurobiology_ **31** , 45–50 (2015). 

99. Bastos, A. M., Vezoli, J. & Fries, P. Communication through coherence with inter-areal delays. _Current Opinion in Neurobiology_ **31** , 173–180 (2015). 

100. Helfrich, R. F. & Knight, R. T. Oscillatory dynamics of prefrontal cognitive control. _Trends in Cognitive Sciences_ **20** , 916–930 (2016). 

101. Eichenbaum, H. Prefrontal–hippocampal interactions in episodic memory. _Nature Reviews Neuroscience_ **18** , 547 (2017). 

102. Lundqvist, M., Bastos, A. & Miller, E. K. Preservation and changes in oscillatory dynamics across the cortical hierarchy. _Journal of Cognitive Neuroscience_ **32** , 2024–2035 (2020). 

103. Patel, J., Fujisawa, S., Ber´enyi, A., Royer, S. & Buzs´aki, G. Traveling theta waves along the entire septotemporal axis of the hippocampus. _Neuron_ **75** , 410–7 (2012). 

19/24 

Monaco, Rajan, & Hwang 

104. Zhang, H. & Jacobs, J. Traveling theta waves in the human hippocampus. _Journal of Neuroscience_ **35** , 12477–12487 (2015). 

105. Muller, L. _et al._ Rotating waves during human sleep spindles organize global patterns of activity that repeat precisely through the night. _eLife_ **5** , e17267 (2016). 

106. Zhang, H., Watrous, A. J., Patel, A. & Jacobs, J. Theta and alpha oscillations are traveling waves in the human neocortex. _Neuron_ **98** , 1269–1281.e4 (2018). 

107. Hern´andez-P´erez, J. J., Cooper, K. W. & Newman, E. L. Medial entorhinal cortex activates in a traveling wave in the rat. _eLife_ **9** , e52289 (2020). 

108. Riddle, J., McFerren, A. & Frohlich, F. Causal role of cross-frequency coupling in distinct components of cognitive control. _Progress in Neurobiology_ 102033 (2021). 

109. Bickerton, D. & Szathm´ary, E. _Biological foundations and origin of syntax_ , vol. 3 (MIT Press, 2009). 

110. Steels, L. & Szathm´ary, E. The evolutionary dynamics of language. _Biosystems_ **164** , 128–137 (2018). 

111. Theves, S., Fernandez, G. & Doeller, C. F. The hippocampus encodes distances in multidimensional feature space. _Current Biology_ **29** , 1226–1231.e3 (2019). 

112. Rikhye, R. V. _et al._ Learning cognitive maps as structured graphs for vicarious evaluation. _bioRxiv preprint bioRxiv:864421_ (2020). 

113. Peer, M., Brunec, I. K., Newcombe, N. S. & Epstein, R. A. Structuring knowledge with cognitive maps and cognitive graphs. _Trends in Cognitive Sciences_ **25** , 37–54 (2021). 

114. Morton, N. W. & Preston, A. R. Concept formation as a computational cognitive process. _Current Opinion in Behavioral Sciences_ **38** , 83–89 (2021). 

115. Milnor, J. On the concept of attractor. _Comm. Math. Phys._ **99** , 177–195 (1985). 

116. Tsuda, I. & Umemura, T. Chaotic itinerancy generated by coupling of Milnor attractors. _Chaos_ **13** , 937–946 (2003). 

117. Cossart, R., Aronov, D. & Yuste, R. Attractor dynamics of network UP states in the neocortex. _Nature_ **423** , 283–8 (2003). 

118. Lundqvist, M., Rehn, M., Djurfeldt, M. & Lansner, A. Attractor dynamics in a modular network model of neocortex. _Network: Computation in Neural Systems_ **17** , 253–276 (2006). 

119. Knierim, J. J. & Zhang, K. Attractor dynamics of spatially correlated neural activity in the limbic system. _Annu Rev Neurosci_ **35** , 267–85 (2012). 

120. Demircigil, M., Heusel, J., L¨owe, M., Upgang, S. & Vermet, F. On a model of associative memory with huge storage capacity. _Journal of Statistical Physics_ **168** , 288–299 (2017). 

121. Krotov, D. & Hopfield, J. Dense associative memory is robust to adversarial inputs. _Neural Computation_ **30** , 3151–3167 (2018). 

20/24 

Monaco, Rajan, & Hwang 

122. Gardner, R. J. _et al._ Toroidal topology of population activity in grid cells. _bioRxiv preprint bioRxiv:2021.02.25.432776_ (2021). 

123. Siegle, J. H. _et al._ Survey of spiking in the mouse visual system reveals functional hierarchy. _Nature_ **592** , 86–92 (2021). 

124. Milner, P. M. The cell assembly: Mark II. _Psychological Review_ **64** , 242–252 (1957). 

125. Kozachkov, L., Lundqvist, M., Slotine, J.-J. & Miller, E. K. Achieving stable dynamics in neural circuits. _PLOS Computational Biology_ **16** , e1007659– (2020). 

126. Barak, O. & Tsodyks, M. Persistent activity in neural networks with dynamic synapses. _PLoS Comput Biol_ **3** , e35 (2007). 

127. Romani, S. & Tsodyks, M. Short-term plasticity based network model of place cells dynamics. _Hippocampus_ **25** , 95–105 (2014). 

128. Deco, G. & Rolls, E. T. Sequential memory: a putative neural and synaptic dynamical mechanism. _J Cogn Neurosci_ **17** , 294–307 (2005). 

129. Akrami, A., Russo, E. & Treves, A. Lateral thinking, from the Hopfield model to cortical dynamics. _Brain Research_ **1434** , 4–16 (2012). 

130. Azizi, A. H., Wiskott, L. & Cheng, S. A computational model for preplay in the hippocampus. _Front Comput Neurosci_ **7** , 161 (2013). 

131. Stella, F., Urdapilleta, E., Luo, Y. & Treves, A. Partial coherence and frustration in self-organizing spherical grids. _Hippocampus_ **30** , 302–313 (2020). 

132. Braitenberg, V. _Vehicles: Experiments in synthetic psychology_ , chap. _Vehicle 12_ (MIT Press, 1986). 

133. Levy, W. B. A sequence predicting CA3 is a flexible associator that learns and uses context to solve hippocampal-like tasks. _Hippocampus_ **6** , 579–90 (1996). 

134. Monaco, J. D. & Levy, W. B. T-maze training of a recurrent CA3 model reveals the necessity of novelty-based modulation of LTP in hippocampal region CA3. In _Proc Int Joint Conf Neural Netw_ , 1655–1660 (IEEE, Portland, OR, 2003). 

135. Song, S., Yao, H. & Treves, A. A modular latching chain. _Cognitive Neurodynamics_ **8** , 37–46 (2014). 

136. Tognoli, E. & Kelso, J. A. S. The metastable brain. _Neuron_ **81** , 35–48 (2014). 

137. Tsuda, I. Chaotic itinerancy and its roles in cognitive neurodynamics. _Current Opinion in Neurobiology_ **31** , 67–71 (2015). 

138. Miller, P. Itinerancy between attractor states in neural systems. _Current Opinion in Neurobiology_ **40** , 14–22 (2016). 

139. George, D., L´azaro-Gredilla, M., Lehrach, W., Dedieu, A. & Zhou, G. A detailed mathematical theory of thalamic and cortical microcircuits based on inference in a generative vision model. _bioRxiv preprint bioRxiv:2020.09.09.290601_ (2020). 

21/24 

Monaco, Rajan, & Hwang 

140. Monaco, J. D., Hwang, G. M., Schultz, K. M. & Zhang, K. Cognitive swarming in complex environments with attractor dynamics and oscillatory computing. _Biological Cybernetics_ **114** , 269–284 (2020). 

141. Sejnowski, T. J. The unreasonable effectiveness of deep learning in artificial intelligence. _Proceedings of the National Academy of Sciences_ 201907373 (2020). 

142. George, D. _et al._ A generative vision model that trains with high data efficiency and breaks text-based CAPTCHAs. _Science_ **358** , eaag2612 (2017). 

143. Dalgaty, T., Miller, J. P., Vianello, E. & Casas, J. Bio-inspired architectures substantially reduce the memory requirements of neural network models. _Frontiers in Neuroscience_ **15** , 156 (2021). 

144. Hooker, S. The Hardware Lottery. _arXiv preprint arXiv:2009.06489_ (2020). 

145. Stanley, K. O. & Lehman, J. _Why greatness cannot be planned: The myth of the objective_ (Springer, 2015). 

146. Gomez-Marin, A., Paton, J. J., Kampff, A. R., Costa, R. M. & Mainen, Z. F. Big behavioral data: psychology, ethology and the foundations of neuroscience. _Nature Neuroscience_ **17** , 1455–1462 (2014). 

147. Gomez-Marin, A. Causal circuit explanations of behavior: Are necessity and sufficiency necessary and sufficient? In C¸ elik, A. & Wernet, M. F. (eds.) _Decoding Neural Circuit Structure and Function_ , 283–306 (Springer, Cham, 2017). 

148. Krakauer, J. W., Ghazanfar, A. A., Gomez-Marin, A., MacIver, M. A. & Poeppel, D. Neuroscience needs behavior: Correcting a reductionist bias. _Neuron_ **93** , 480–490 (2017). 

149. Niv, Y. The primacy of behavioral research for understanding the brain. _PsyArXiv preprint PsyArXiv:y8mxe_ (2020). 

150. Powers, W. T. Feedback: Beyond behaviorism. _Science_ **179** , 351–356 (1973). 

151. Bell, H. C. Behavioral variability in the service of constancy. _International Journal of Comparative Psychology_ **27** , 338–360 (2014). 

152. Musall, S., Urai, A. E., Sussillo, D. & Churchland, A. K. Harnessing behavioral diversity to understand neural computations for cognition. _Current Opinion in Neurobiology_ **58** , 229–238 (2019). 

153. Bastos, A. M. _et al._ Canonical microcircuits for predictive coding. _Neuron_ **76** , 695–711 (2012). 

154. Friston, K. Hierarchical models in the brain. _PLOS Computational Biology_ **4** , e1000211– (2008). 

155. Friston, K. J., Bastos, A. M., Pinotsis, D. & Litvak, V. LFP and oscillations— what do they tell us? _Current Opinion in Neurobiology_ **31** , 1–6 (2015). 

156. Issa, E. B., Cadieu, C. F. & DiCarlo, J. J. Neural dynamics at successive stages of the ventral visual stream are consistent with hierarchical error signals. _eLife_ **7** , e42870 (2018). 

22/24 

Monaco, Rajan, & Hwang 

157. Wang, M., Foster, D. J. & Pfeiffer, B. E. Alternating sequences of future and past behavior encoded within hippocampal theta oscillations. _Science_ **370** , 247–250 (2020). 

158. Reinhold, A. S., Sanguinetti-Scheck, J. I., Hartmann, K. & Brecht, M. Behavioral and neural correlates of hide-and-seek in rats. _Science_ **365** , 1180–1183 (2019). 

159. Kosoy, E. _et al._ Exploring Exploration: Comparing Children with RL Agents in Unified Environments. _arXiv preprint arXiv:2005.02880_ (2020). 

160. Silver, D. _et al._ Mastering the game of Go without human knowledge. _Nature_ **550** , 354–359 (2017). 

161. Badia, A. P. _et al._ Agent57: Outperforming the Atari human benchmark. _arXiv preprint arXiv:2003.13350_ (2020). 

162. Monaco, J. D., Rao, G., Roth, E. D. & Knierim, J. J. Attentive scanning behavior drives one-trial potentiation of hippocampal place fields. _Nat Neurosci_ **17** , 725–731 (2014). 

163. Merker, B. Consciousness without a cerebral cortex: A challenge for neuroscience and medicine. _Behavioral and Brain Sciences_ **30** , 63–81 (2007). 

164. Solms, M. & Friston, K. How and why consciousness arises: some considerations from physics and physiology. _Journal of Consciousness Studies_ **25** , 202–238 (2018). 

165. Munn, B., M¨uller, E. J., Wainstein, G. & Shine, J. M. The ascending arousal system shapes low-dimensional brain dynamics to mediate awareness of changes in intrinsic cognitive states. _bioRxiv preprint bioRxiv:2021.03.30.437635_ (2021). 

166. Tschantz, A., Seth, A. K. & Buckley, C. L. Learning action-oriented models through active inference. _PLOS Computational Biology_ **16** , 1–30 (2020). 

167. M´arton, C. D., Schultz, S. R. & Averbeck, B. B. Learning to select actions shapes recurrent dynamics in the corticostriatal system. _Neural Networks_ **132** , 375–393 (2020). 

168. NSF announces next topics for the Emerging Frontiers in Research and Innovation (EFRI) program. URL https://www.nsf.gov/news/news_ summ.jsp?cntn_id=302424&org=EFMA. 

169. Roy, K., Jaiswal, A. & Panda, P. Towards spike-based machine intelligence with neuromorphic computing. _Nature_ **575** , 607–617 (2019). 

170. Mead, C. How we created neuromorphic engineering. _Nature Electronics_ **3** , 434–435 (2020). 

171. Aimone, J. B. A roadmap for reaching the potential of brain-derived computing. _Advanced Intelligent Systems_ 2000191 (2020). 

172. Zenke, F. & Neftci, E. O. Brain-inspired learning on neuromorphic substrates. _Proceedings of the IEEE_ **[Epub ahead of print]** (2021). 

173. Zenke, F. _et al._ Visualizing a joint future of neuroscience and neuromorphic engineering. _Neuron_ **109** , 571–575 (2021). 

23/24 

Monaco, Rajan, & Hwang 

174. Scellier, B. & Bengio, Y. Equivalence of equilibrium propagation and recurrent backpropagation. _arXiv preprint arXiv:1711.08416_ (2018). 

175. Millidge, B., Tschantz, A., Buckley, C. L. & Seth, A. Activation relaxation: A local dynamical approximation to backpropagation in the brain. _arXiv preprint arXiv:2009.05359_ (2020). 

176. Guerguiev, J., Lillicrap, T. P. & Richards, B. A. Towards deep learning with segregated dendrites. _eLife_ **6** , e22901 (2017). 

177. Bartunov, S. _et al._ Assessing the scalability of biologically-motivated deep learning algorithms and architectures. _arXiv preprint arXiv:1807.04587_ (2018). 

178. Liu, Y. H., Smith, S., Mihalas, S., Shea-Brown, E. & S¨umb¨ul, U. A solution to temporal credit assignment using cell-type-specific modulatory signals. _bioRxiv preprint bioRxiv:2020.11.22.393504_ (2021). 

24/24 

Monaco, Rajan, & Hwang 

