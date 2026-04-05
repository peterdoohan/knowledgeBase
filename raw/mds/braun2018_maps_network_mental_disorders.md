Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

## From Maps to Multi-dimensional Network Mechanisms of Mental Disorders 

Urs Braun,[1] Axel Schaefer,[1] Richard F. Betzel,[2] Heike Tost,[1] Andreas Meyer-Lindenberg,[1] and Danielle S. Bassett[2][,][3][,] * 1Central Institute of Mental Health, Medical Faculty Mannheim/University of Heidelberg, 68159 Mannheim, Germany 2Department of Bioengineering, University of Pennsylvania, Philadelphia, PA 19104, USA 

3Department of Electrical and Systems Engineering, University of Pennsylvania, Philadelphia, PA 19104, USA *Correspondence: dsb@seas.upenn.edu https://doi.org/10.1016/j.neuron.2017.11.007 

The development of advanced neuroimaging techniques and their deployment in large cohorts has enabled an assessment of functional and structural brain network architecture at an unprecedented level of detail. Across many temporal and spatial scales, network neuroscience has emerged as a central focus of intellectual efforts, seeking meaningful descriptions of brain networks and explanatory sets of network features that underlie circuit function in health and dysfunction in disease. However, the tools of network science commonly deployed provide insight into brain function at a fundamentally descriptive level, often failing to identify (patho-)physiological mechanisms that link system-level phenomena to the multiple hierarchies of brain function. Here we describe recently developed techniques stemming from advances in complex systems and network science that have the potential to overcome this limitation, thereby contributing mechanistic insights into neuroanatomy, functional dynamics, and pathology. Finally, we build on the Research Domain Criteria framework, highlighting the notion that mental illnesses can be conceptualized as dysfunctions of neural circuitry present across conventional diagnostic boundaries, to sketch how network-based methods can be combined with pharmacological, intermediate phenotype, genetic, and magnetic stimulation studies to probe mechanisms of psychopathology. 

Brain function depends on highly complex interactions between distributed brain regions (Medaglia et al., 2015; Sporns, 2014). Neuroimaging remains a core method to study these interactions at the large-scale system level. The conceptual framework through which these data are analyzed has evolved from univariate analyses, through connectivity measures, to modern network neuroscience (Bassett and Sporns, 2017; Sporns, 2010). This line of research is especially relevant for mental disorders, where since the time of Wernicke it has been proposed that altered interactions of brain regions within networks are at the core of pathophysiology. Originating from a branch of mathematics called graph theory (Bollobas, 1985, 2012), network models represent complex systems as sets of discrete nonoverlapping entities (nodes) and their pairwise relationships (edges) that can be summarized in the form of a graph. The patterns by which edges connect nodes constitute the network’s topology, which is amenable to descriptive analysis through a broad array of measures that probe local and global aspects of network organization (Newman, 2010). The rather abstract form and simple representation highlight one of the key advantages of network neuroscience: its broad applicability. Network methods can be applied to all spatial and temporal scales of brain physiology (Betzel and Bassett, 2016), and they can be used to analyze data types as diverse as cellular-level networks, gene expression profiles, and structural or functional neuroimaging data. 

In recent years, network neuroscience has generated detailed maps of the large-scale structural and functional architecture of healthy human brain networks (Sporns, 2015). Moreover, it has 

demonstrated organizational features of that architecture that are conserved across species (Rubinov et al., 2015; Scholtens et al., 2014; van den Heuvel et al., 2016), sketched the network structures that underlie and enable cognition (Medaglia et al., 2015), and delineated their alteration in disease (Bassett and Bullmore, 2009; Fornito and Bullmore, 2015; Stam, 2014). Though the extent and pace of these characterizations are impressive, their application to the clinic has been surprisingly limited. The lack of translational impact stems in part from the fact that the current approaches are largely descriptive and, therefore, ultimately cannot provide a mechanistic account of circuit (dys-)function. Addressing this limitation is critical for the prospective development of interventions and treatments for psychiatric disorders and for the enhancement of cognitive function in health and disease. 

In this article, we have two major goals. First, we describe a set of new computational tools from a field we coin ‘‘multi-dimensional network neuroscience’’ (Figure 1). These methods extend current network analytic tools by including an additional dimension, of time, space, or function. In doing so, they make it possible to generate network models of processes and mechanisms, going beyond simple statistical dependencies or correlations. Specifically, we concentrate on three tools of multi-dimensional network neuroscience: (1) multilayer networks (Kivela€ et al., 2014), (2) generative models of networks (Ve´ rtes et al., 2012), and (3) network control theory (Liu et al., 2011; Motter, 2015; Pasqualetti et al., 2014). Second, we sketch out strategies for how these new tools can be used to probe mechanisms that underlie circuit function and dysfunction in psychiatric (Hulshoff 

**==> picture [20 x 20] intentionally omitted <==**

14 Neuron 97, January 3, 2018 ª 2017 Elsevier Inc. 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

Figure 1. Graphical Overview of Network Approaches Discussed 

**==> picture [323 x 431] intentionally omitted <==**

Traditional tools from the mathematical discipline of graph theory have emerged as particularly useful in describing structural and functional brain networks. Multilayer network approaches extend this static representation by adding an additional dimension to the 2D graph, such as time or data modality. Generative network methods can be used to study the mechanisms by which brain networks have evolved or have been shaped over development. Network growth is simulated based on some predefined rules and is then compared to a real brain network. Finally, network control theory offers a mechanistic explanation for how activation patterns in the brain are controlled based on the underlying structure. 

## 2D Network Neuroscience: Graph Theoretical Assessment of the Human Connectome 

The characterization of whole-brain structural and functional connectomes using different neuroimaging modalities in combination with graph theoretical measures has offered insight into brain maturation (Whitaker et al., 2016), cognitive function (Medaglia et al., 2015), and neuropsychiatric disorders (Fornito et al., 2012; Siegel et al., 2016). Graph theory (Bollobas, 1985, 2012) provides a mathematical language by which to distill complex systems into a set of component parts (nodes) and their interactions (edges). The pattern of nodes and edges forms a graph, and the architecture of that graph can offer insights into the dynamics that the system can support (Newman et al., 2006; Newman, 2003). 

In the context of human or non-human neuroimaging, data can be rendered into different classes of graphs or networks. Structural networks model the physical, hard-wired connections between neural 

Pol and Bullmore, 2013) and neurological disorders. We describe how multi-dimensional network neuroscience methods can be used to link levels of brain function, starting from gene interaction systems or neurotransmitter systems to brain-wide connectivity, thereby revealing the underlying mechanisms of brain function (Figure 1). 

elements; examples include brain regions linked by white matter tracts (Hagmann et al., 2008), neuronal populations linked by axonal projections (Markov et al., 2013b), and individual cells linked by synapses (Eichler et al., 2017; Lee et al., 2016; Watts and Strogatz, 1998). Functional connectomes capture statistical relationships between time series reflecting the activity of neural elements (Friston, 2011); examples include correlations between fMRI blood-oxygen-level-dependent (BOLD) signals (Achard et al., 2006), statistical similarities in neuronal firing patterns (Muldoon et al., 2013), or causal relationships between neurons, regions, or sensors (Korzeniewska et al., 2011). Finally, morphometric networks capture statistical relationships between markers of regional morphology, such as gray matter thickness or volume, across large cohorts of individuals (Alexander-Bloch et al., 2013; Evans, 2013). Each of these network classes uniquely quantifies one specific aspect of a neural system’s 

We begin by briefly reviewing the current state of network neuroscience (Bullmore and Sporns, 2009), drawing predominantly on the pioneering successes of graph theoretical approaches and their applications to cognitive neuroscience. After discussing conceptual limitations of these approaches, we introduce three major advances from multi-dimensional network neuroscience that offer the potential to directly infer or manipulate mechanisms of network function. We conclude by sketching concrete analysis strategies, possible pitfalls, and future areas of investigation. 

Neuron 97, January 3, 2018 15 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

organization and function. Variations in the topology of these networks, then, can foreshadow dysfunction, leading to cogni- 

One of the most fundamental findings of the young field of network neuroscience is that neural systems, from the neuronlevel connectivity of C. elegans to the white matter connectivity of high-functioning humans, display hubs, nodes that occupy positions of influence within the network. Empirically, hubs tend to be highly connected and more central than anticipated in an appropriate random network null model. Hubs also tend to form many long-distance connections, linking distant neural elements to one another. These long-range connections, in combination with locally dense connectivity, form the substrate for small-world architecture (Bassett and Bullmore, 2006), a combination of short path length (shortest path between two nodes is the minimum number of edges that must be traversed to go from one node to another) and high clustering (a measure of that node’s local connection density quantified as the fraction of closed triangles between its nearest neighbors, normalized by the maximal number of such triangles) facilitating rapid information transmission and efficient communication (Barrat et al., 2007; Latora and Marchiori, 2001). It is worth mentioning that the presence of small-world network architecture has been challenged by studies employing high-resolution anatomical tracing methods, which report substantially denser connectivity in macaque brain than previously reported, leading to shorter path length and reduced small-world measures estimated on the binary network (Markov et al., 2013a, 2013b). However, recently developed methods to assess small-world organization in weighted networks confirm the presence of small-world topology across multiple species (Bassett and Bullmore, 2016; Muldoon et al., 2016a). 

More recently, these global attributes have been shown to accompany a distinct community structure (Fortunato, 2010; Porter et al., 2009), wherein networks can be decomposed into communities or modules, internally dense clusters of neural elements that are sparsely linked to one another (Newman, 2006). Modular organization is thought to facilitate optimal segregation of information and relative autonomy of function (Bassett et al., 2011a; Meunier et al., 2009; Salvador et al., 2005). Interestingly, hubs tend to be distributed across modules while remaining densely interconnected with one another, thereby forming a rich club, which is thought to act as a backbone for integrating information from specific modules and rapidly transmitting it across the brain (Sporns and Betzel, 2016). More generally, rich-club organization is a type of core-periphery structure (Borgatti and Everett, 2000), in which a core of densely interconnected nodes is accompanied by a more sparsely connected periphery (Bassett et al., 2013; Chai et al., 2016). 

These fundamental attributes have now been observed across species (from worms through mice to humans), across age ranges (from infancy through senescence), and across multiple brain-imaging modalities, forming a robust set of characteristics that typify structural, functional, and morphometric networks. 

## Limitations and Challenges 

The simplicity of graph theory can also be a limitation. While powerful, its application to neuroimaging data belies some 

weaknesses that challenge its long-term utility in uncovering mechanisms of psychiatric disease. The exact definition of the word ‘‘mechanism’’ is of course subject to some debate (Craver and Tabery, 2015; Craver and Darden, 2013; Glennan, 1996, 2016; Machamer et al., 2000), but one ecumenical view characterizes a mechanism for a phenomenon as ‘‘entities whose activities are organized in such a way that they produce the phenomenon’’ (Craver and Tabery, 2015; Glennan, 2016). This definition highlights the importance of a detailed description of the entities and their organization as a first step in providing a mechanistic explanation. Importantly, this precondition has been successfully addressed in the neuroimaging community by the extensive efforts in brain mapping over recent years. In addition, organization refers not only to a spatial but also to a temporal component, which is becoming increasingly recognized as important in the neuroimaging community (Cabral et al., 2017). However, the definition stated above also draws the reader’s attention to a major aspect of mechanism that has been largely neglected, namely, the activities of the entity. In most neuroimaging studies, activities, e.g., the interaction between the constituting entities of the mechanism, have so far been described by either regional activations (the activity here being that a region is active) or a statistical or morphological interdependence (the activity here being that regions are connected). Both of these notions of activities are simplistic models that fail to provide an account of circuit function, e.g., how computations are actually performed to produce the studied phenomena. 

Although network models have helped to identify some fundamental principles of brain organization that might underlie normative cognitive function, these insights are often derived from statistical differences in graph theoretical parameters or from correlations between parameters and empirically measured estimates of behavior, cognition, or disease. Yet, parameters do not equate to mechanisms and correlations do not equate to causal drivers. For a more complete understanding of brain function, we wish to move beyond statements such as ‘‘network A is different from network B’’ to questions of why these differences appear in the first place and how architectural differences causally affect brain function. This goal requires us to move from a focus on mapping to a focus on mechanism and to develop tools that make explicit predictions about how network structure and function influence human cognition and behavior. Such a paradigm shift from mapping to mechanism might necessitate more extensive assessments across subjects, times, and imaging modalities; but, in doing so, it would have the potential to directly address the National Institute of Mental Health (NIMH) Research Domain Criteria (RDoC) goals in understanding mechanisms of psychiatric disorders in a trans-diagnostic manner. 

## From Description to Prediction: Multi-dimensional Network Neuroscience Multilayer Networks 

Traditional network approaches model the brain as a network of nodes and edges, and in doing so they are constrained to use a single definition of what constitutes a node and a single definition of what constitutes an edge. Node definitions can be problematic if within-region processing features are insufficiently 

16 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

captured. Moreover, evidence suggests that several parcellation schemes might be useful for studying the brain across spatial scales ranging from single voxels to gross neuroanatomical features. Edges can be defined in many different ways, and they can be estimated from many different imaging modalities or contexts, including structural imaging, task-related functional imaging, and task-unrelated functional imaging (Muldoon and Bassett, 2016). Moreover, in functional imaging, edges may be defined over different time windows of imaging data potentially corresponding to different cognitive states of the participant under study (Betzel and Bassett, 2016). In applied mathematics, the development of multilayer network analyses has become a recent focus of research, in an effort to determine how best to incorporate these additional layers and dimensions into network models (De Domenico et al., 2016b; Kivela et al., 2014€ ). From the perspective of network neuroscience, multilayer network models of neural systems offer the potential to illuminate aspects of brain function that could not otherwise be gleaned from traditional, single-layer network models (Buldyrev et al., 2010). 

Unfortunately, the recent interest in describing complex systems in terms of multilayer networks has led to some confusing and often parallel terminology. Here we adopt the generalized definition of multilayer networks proposed by Kivela€ et al. (2014), which can be used to represent most types of complex systems that consist of multiple networks (Figure 1). In this framework, connectivity matrices representing either the state of the network at a particular time point or different connectivity modalities can be linked together by connecting each node in one layer to itself in a different layer (Muldoon and Bassett, 2016). In the specific case of a temporal network where edges are defined with respect to a time window, the adjacency matrices can be linked in an ordinal fashion as follows: node i in layer s (time window) is linked to node i in the adjacent time windows, s – 1 and s + 1 (Sizemore and Bassett, 2017). In the case of multimodal networks where edges are defined with respect to a type of interaction, the adjacency matrices are not linked in an ordinal fashion but rather in a categorical fashion. One common technique is to link each node to itself in all other layers (Mucha et al., 2010), although other more complicated patterns are also possible and, in some cases, preferable. The general multilayer construction is also useful when layers represent connections in different frequency bands; in this case, the inter-layer coupling could be all-to-all, thereby connecting data across all frequency bands, and the weight of the inter-layer link could represent the magnitude of cross-frequency coupling between individual brain regions. Many classical network diagnostics, such as path length, clustering coefficient, and summary statistics characterizing community structure, have been extended to multilayer networks, and these have begun to be applied across many disciplinary domains (Holme and Saramaki, 2012; Kivel€ a et al., 2014; Mucha et al., 2010€ ). 

In parallel to these methodological advances, the view that brain networks are not static during cognitively effortful task processing but rather dynamic has gained increasing traction, reinforcing the intuition that networks change their configuration on timescales from milliseconds to years (Deco et al., 2011; Hutchison et al., 2013; Leonardi and Van De Ville, 2015; Supekar et al., 2009; Telesford et al., 2016; Uhlhaas, 2013; Zalesky and 

Breakspear, 2015; Zalesky et al., 2014). The first applications of (temporal) multilayer network techniques to neuroimaging data demonstrated that brain networks reconfigure during a range of cognitive phenomena. This work found that flexible, i.e., variable across time, patterns of functional connectivity predicted individual differences in learning (Bassett et al., 2011b), leading to an increasing independence of the underlying subnetworks as learning progressed to automaticity (Bassett et al., 2015). Subsequent work extended the idea of flexible network reconfiguration to other cognitive domains, including working memory (Braun et al., 2015), attention (Shine et al., 2016b), cognitive flexibility (Braun et al., 2015), and language processing (Chai et al., 2016; Doron et al., 2012), suggesting that dynamic network reconfiguration might be a more generic prerequisite for healthy executive function. Many argue that these types of dynamic network techniques are fundamentally necessary to understand cognitive functions more broadly (Fedorenko and Thompson-Schill, 2014; Medaglia et al., 2015), and recent studies have demonstrated that dynamic network parameters can indeed capture aspects of brain functioning that are not detected by more traditional measures of brain activity or connectivity (Bassett et al., 2015; Braun et al., 2015). 

In addition to the use of multilayer networks to assess network reconfiguration during a single task, a few studies have begun to use this formulation to investigate network reconfiguration across several tasks (Cole et al., 2014; Mattar et al., 2015; Telesford et al., 2016). In the simplest scenario, one might be interested in differences between two states, such as a resting state and a cognitively demanding task state (Cole et al., 2014). In this scenario, connectivity matrices are estimated for both states and treated as layers in a two-layer multilayer network. This simple extension enables one to explicitly model the similarities and differences between tasks in a single formal model. Of course, this two-state example can easily be extended to include additional layers corresponding to connectivity estimated during other tasks. The multilayer formalism then makes it possible to address the questions of whether network dynamics are similar or different across tasks and whether inter-task differences are greater or lesser than inter-subject differences (Telesford et al., 2016). Finally, one might wish to know how a brain transitions between large sets of states and whether the role of cognitive systems changes over these task sets in a predictable manner (Mattar et al., 2015). Multilayer approaches offer a principled means of dissolving the dichotomous distinction between task and resting-state brain networks or between functional and structural networks. Instead, they suggest that these different statistical representations are simply different views of the same underlying dynamical system, which traverses a complex energy landscape constrained by neuroanatomy (Watanabe et al., 2013) to move between and among behaviorally meaningful cognitive states (Ashourvan et al., 2017; Gu et al., 2016; Watanabe et al., 2014). 

Perhaps the most powerful, but also the least studied, application of multilayer networks to neuroimaging data lies in the integration of data across imaging modalities. For example, questions of how structure impacts or constrains functional dynamics, questions of how one frequency may couple to another frequency (Canolty et al., 2006; Canolty and Knight, 2010; 

Neuron 97, January 3, 2018 17 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

Siebenhuhner et al., 2013€ ), and questions of how morphological characteristics might relate to genetic information (Ve´ rtes et al., 2016; Whitaker et al., 2016) or to neurotransmitter distributions (Braun et al., 2016) are particularly appropriate to address using multilayer network models, in which brain regions may relate to one another in distinct ways estimated by distinct imaging modalities (De Domenico et al., 2016a; Brookes et al., 2016). Indeed, most generally, understanding how different estimates of regional relations and interactions estimated from different imaging modalities are related to one another (Gon˜ i et al., 2014; Hermundstad et al., 2013; Honey et al., 2009), and how those relationships impinge on behavior (Hermundstad et al., 2014), remains a critical challenge. 

## Generative Network Models 

A broad class of questions in network neuroscience lies in the characterization and understanding of how brain networks evolve over evolutionary timescales, develop from childhood to adulthood, or reconfigure during normal healthy aging. While an important initial strategy is to simply describe these changes in network structure, the quizzical scientist also yearns for the mechanistic understanding that is often only possible from a predictive model (R.F.B. and D.S.B., unpublished data). In the context of brain connectivity, generative network models form particularly appealing frameworks in which to satiate this curiosity. 

Generative network models are a collection of methods that can be used to simulate the growth and evolution of networks based on simple, hypothesized mechanisms (A.Z. Jacobs and A. Clauset, 2014, NIPS, workshop; Park and Newman, 2004) (Figure 2A). For example, one class of generative models supposes that the probability with which two nodes are connected depends on their latent (hidden) attributes. The modeling aspect involves fitting the parameters of this model so that it generates synthetic networks with the same properties as the real-world network. Typically, one tests multiple possible models and wiring rules, but ultimately one focuses on the model with the greatest goodness of fit; that is, the model that generates synthetic networks most similar to the observed network (Newman, 2010). If the model network and real network are similar, it suggests that the modeled generative mechanism may drive the growth and evolution of the real-world network. 

Generative models have a long history in network science. Among the most studied is the preferential attachment model, which generates networks with heavy-tailed degree distributions similar to those observed in many real-world socio-technical networks like Facebook and Twitter. In this model, originally proposed by de Solla Price (1965) and later reintroduced by Barabasi and Albert (1999), links to a node are added probabilistically and proportional to the node’s degree, such that hubs gain more connections than non-hubs. However, the utility of these simple preferential attachment models in accurately modeling neural systems has been questioned, as they fail to reproduce essential features of human brain networks (Hilgetag and Kaiser, 2007; Ve´ rtes et al., 2012). It has been argued that the poor fit is due to the model’s simple focus on topological network features, without considering that brain networks have evolved under evolutionary pressure and are spatially embedded (Bullmore and Sporns, 2009, 2012; Kaiser and Varier, 2011). Following these initial studies, research on brain networks has begun to 

focus more on models that account for geometric features (Hilgetag and Kaiser, 2007; Lo et al., 2015b; Roberts et al., 2016), by penalizing connection distance as a proxy for the biological minimization of wiring costs under evolutionary pressure (Samu et al., 2014). Although these models can replicate certain features of observable brain networks, many cannot account for all topological aspects (Betzel et al., 2016a; Kaiser and Hilgetag, 2006). However, see also Ercsey-Ravasz et al. (2013) and Song et al. (2014) for contradicting accounts. 

Merging topological and geometric network features, Ve´ rtes and colleagues tested the hypothesis that brain networks have evolved under an economic trade-off between minimizing wiring costs and allowing the emergence of adaptively valuable, but metabolically costly, topological patterns of anatomical or functional connectivity (Bullmore and Sporns, 2012; Ve´ rtes et al., 2012) (Figure 2B). Evaluating different growth rules, the authors found the greatest similarity to real brain networks when using a generative model that penalizes long-distance connections and favors intra-community connectivity. In a similar study, Betzel et al. (2016a) used several generative models to probe the organization of structural brain networks obtained from healthy adult individuals (Figure 2C). The authors again found highest fitness for a model incorporating a penalization of distance and a preference for a normalized topological measure of overlap in two nodes’ neighborhoods (Betzel et al., 2016a). Interestingly, when applying their bestfitting model to a dataset spanning a large group of individuals from age 7 to 85 years, they observed that the influence of the penalty on long-distance connections weakened with age, supporting the notion that the organization of brain networks is shaped less by spatial relationships with increasing age (Giedd et al., 2008). 

While the framework is generalizable across other contexts, including adaptation and learning, perhaps the most interesting context in which to exercise these models is that of psychiatric disease. In particular, it is critical to determine generative rules for normal brain development and to pinpoint deviations from that trajectory that might foreshadow the emergence of psychiatric symptoms. To realize these goals, efforts are also needed in methodological innovation, as it is not yet clear which parameters to use for the evaluation of synthetic network fitness. Furthermore, it is important to keep in mind the interpretational caveat that similar structure in the synthetic networks does not necessarily prove similar mechanisms; it only supports the possibility of such a mechanism. 

Once one constructs a generative model that fits adult human neuroimaging data, the next question is whether one can construct a generative growth model that fits longitudinal neuroimaging data across development from childhood to adulthood. Similarly, can one construct a generative growth model to explain reconfiguration during normal healthy aging? If so, then the natural next step would be to encode predicted neurodevelopmental alterations (e.g., autism) in a generative disordered growth model or to encode predicted alterations in abnormal aging (e.g., Alzheimer’s disease) in a generative disordered aging model (Ve´ rtes and Bullmore, 2015). These models could then be tested explicitly in neuroimaging data acquired in neurodevelopmental disorders and disorders of healthy aging. Because 

18 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 324] intentionally omitted <==**

Figure 2. Multilayer Network and Generative Modeling Approaches Generative network models investigate possible underlying mechanisms that contribute to the development or evolution of brain networks. (A) A generative network model is created by adding links to a network in a stepwise fashion based on a predefined rule (here preferential attachment: higher likelihood for links to appear at already highly connected nodes). The final network is then compared to a real (brain) network and evaluated in terms of several topological metrics, for example, by using Kolmogorov-Smirnov statistics. (B) Ve´ rtes et al. (2012) showed that functional resting-state brain networks have evolved under an economic trade-off between minimizing wiring length and persevering topological complexity. Schizophrenia patients showed a lower penalty for wiring cost, suggesting a differential regulation of neuronal migration, differentiation, and axon guidance. 

(C) Betzel et al. (2016a) tested various growth rules based on several topological measures as well as Euclidean distance between regions. They demonstrated that penalization of distance and a preference for a normalized topological measure of overlap in two nodes’ neighborhoods are dominant drivers of the observed structural connectome but that their relative contributions change in healthy aging. Boxes are interquartile ranges (IQR). The whiskers (error bars) define the full range of the distribution, excluding outliers (more than 1.5 IQRs beyond the top/bottom of the box). These outliers are plotted as individual points. (D) Hypothesized neurobiological mechanisms contributing to altered network generation in developmental disorders that can be directly instantiated in generative models: altered neuronal migration by distance-dependent guidance factors (top); activity-dependent wiring of neurons that share a nearest neighbor (middle); and degeneration of existing links by excitotoxicity (bottom). 

these models are mechanistic, they offer the potential for disentangling different developmental processes and identifying underlying cellular mechanisms, such as alterations in axonal guidance or synaptic pruning (Kaiser, 2017) (Figure 2D). In developmental disorders in which the genetic basis is known, the approach could also provide a link between risk genes and their system-level sequelae. 

## Network Control Theory 

A true understanding of a system offers the ability to control its features or to perturb a system so that it behaves in a desired way. Recent advances in the field of network control theory have established a powerful framework to study controllability in complex biological networks (Campbell et al., 2015). Putting aside the global question of whether a system is generally 

controllable (Liu et al., 2011), control theory can be used to examine the (energy) landscape of possible brain states; that is, which states within a dynamic regime would the system have difficulty accessing, which regions need to be perturbed to make those states accessible, and how energetic should a particular perturbation be in order to reach those states (Gutie´ r- rez et al., 2012; Liu et al., 2011; Yuan et al., 2013). 

In control theory, a dynamical system is controllable if it can be driven from any initial state to any desired final state within finite time (Betzel et al., 2016b). For simplicity, the observed system is often assumed to be linear (Gala´ n et al., 2008; Honey et al., 2009) (Figure 3A). Controlling a complex network then reduces to (1) the selection of specific nodes that, by virtue of being directly controlled, can indirectly drive the rest of the network to any 

Neuron 97, January 3, 2018 19 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 268] intentionally omitted <==**

Figure 3. Network Control Theory Approaches (A) Based on a structural network backbone, A, network control theory can be used to model how the network transitions from an initial state x0 (left side, active nodes in blue) to a final target state xt (right side, active nodes in blue). The particular nodes that exhibit control, B, over the network are selected (middle, red arrows), and the minimum amount of control energy u(t) in each control node that is necessary to drive the network from x0 to xt is computed by finding the optimal solution to the minimization problem of the corresponding Hamiltonian. (B) Gu et al. (2015) investigated the controllability of structural brain networks. Regions within the default-mode network supported transitions into easy-to-reach brain states (average controllability), while cognitive control areas facilitated transitions into hard-to-reach brain states (modal controllability). (C) First evidence for altered controllability in disease was demonstrated for mild traumatic brain injury (TBI) by Gu and colleagues (Gu et al., 2017). Although healthy and TBI subjects showed a high overlap in brain areas contributing to controllability, the TBI group showed a significant reduction in mean control efficiency. Error bars indicate SEM. 

(D) Applications of network control theory to clinical populations can offer the possibility to mechanistically understand perturbation and therapeutic interventions, such as medication, transcranial magnetic stimulation (TMS), transcranial direct current stimulation (tDCS), or deep brain stimulation on a circuit level, to prevent transition to pathologic states and to steer the brain toward more favorable conditions. 

desired state; and (2) the prescription of time-dependent control inputs that, when applied to these nodes, will drive the system to a desired state (Ruths and Ruths, 2014). Theoretical work has provided important insights into how the topological structure of the underlying network influences the control properties of the system (Kim et al., 2017; Po´ sfai et al., 2013). For example, sparse inhomogeneous networks such as the brain are harder to control than dense, regular networks (Liu et al., 2011). 

The traditional application of control theory to neural systems has largely focused on small circuit diagrams (Schiff, 2012) or on neuron-level dynamics (Wilson and Moehlis, 2014), for example, in identifying optimal targets for deep brain stimulation in the treatment of Parkinson’s disease (Santaniello et al., 2012) or burst suppression in coma (Ching et al., 2012). Explicit applications to complex network architectures derived from large-scale neuroimaging data are rare, but recent pioneering work assessed the controllability of structural brain networks in adult humans as estimated from high-resolution diffusion spectrum imaging data (Figure 3B). Regions within the default-mode network supported transitions into easy-to-reach brain states, while cognitive control areas facilitated transitions into hard-to-reach 

states (Gu et al., 2015). Moreover, regions with a large number of indirect (long-distance) paths to the areas of high activity in the target state tended to be optimal controllers (Betzel et al., 2016b; Gu et al., 2017), and the effectiveness of these controllers was altered in development (Tang et al. 2017) and following mild traumatic brain injury (Gu et al., 2017) (Figure 3C). 

A necessary next step is to model transitions among more realistic brain states obtained using a data-driven approach from observed fMRI activation patterns. These patterns can be estimated from resting-state data and from data obtained from task paradigms. The ease or difficulty, as measured by the minimal control energy, with which subjects transition to and from these states could be used to identify structural and functional driver nodes or subsystems of relevance to multiple cognitive and emotional domains. These drivers can be used to construct subject-specific control profiles, which may be useful in building a more biologically and mechanistically informed understanding of psychological and clinical deficits in patients. In initial pioneering work in this vein, network control theory has recently been used to define optimal control principles for seizure abatement in epilepsy (Taylor et al., 2015). Important current frontiers 

20 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

include work developing similar intervention strategies in other neurological disorders or in psychiatric disease. 

## Perspective: Strategies for Clinical Translation 

The examples discussed thus far illustrate how multi-dimensional network neuroscience, in the form of multilayer networks, generative models, and network control theory, can be used to support an increasingly mechanistic understanding of brain network function in healthy adults, children, and the elderly. But how can these methods be extended or potentially translated to neuropsychiatry, thereby contributing to a better identification of underlying pathophysiological mechanisms of mental disorders? Despite the success of neuroimaging and network neuroscience in establishing the view of mental disorders as dysfunctions of circuits and networks (Fornito et al., 2012; Rubinov and Bullmore, 2013a), translation to clinical contexts and demonstrable clinical utility have remained limited. Reasons for this lack of translation may be methodological (unknown relations between observed signals and neurovascular coupling or neural computations), or they may be inherent to the nature in which mental disorders are currently diagnosed, which contribute to the lack of a gold standard definition of mental disorders on the biological level (Kapur et al., 2012), heterogeneity of mental disorders, and the complexity of interacting biological levels and timescales. Still, many of these problems have been especially difficult to address because of the limitations of univariate neuroimaging analysis strategies. 

## Phenotypic and Biological Heterogeneity of Mental Disorders 

Current diagnostic approaches to mental illness (e.g., Diagnostic and Statistical Manual of Mental Disorders [DSM-5]) rely on identifying combinations of symptoms to reach a diagnosis of a disorder. Patients sharing the same diagnosis may exhibit very different symptoms. For example, there are 636,120 symptom combinations that would all qualify for diagnosis of PTSD (Galatzer-Levy and Bryant, 2013). While all of these symptom combinations may not be clinically plausible, studies in outpatients suggest that this heterogeneity of presentation does occur, with 1,030 unique symptom profiles observed in 3,703 depressed outpatients (Fried and Nesse, 2015), for example. The symptom heterogeneity within diagnostic categories represents a challenge for elucidating the biological determinants of psychiatric disorders, especially if the symptom heterogeneity reflects etiological heterogeneity (Olbert et al., 2014). 

Further complicating the picture, diagnosis of more than one mental disorder (i.e., comorbidity) is extremely common, often cited as the rule rather than the exception for mental disorders (Brady et al., 2000; Kessler et al., 2005). The clustering of multiple disorders within persons may indicate shared biological vulnerabilities that may act as better targets for identifying underlying mechanisms of disorders than the diagnostic categories themselves. Alternatively, network approaches to psychopathology highlight that shared symptoms between disorders act as causal bridges between disorders (Cramer et al., 2010). Here a focus on interactions among symptoms rather than on the presence of two latent disorders would be warranted. 

The heterogeneity of the presentation of a mental disorder, and the fact that the current nosology of mental illness is not bio- 

logically based, implies that differential biological processes are impaired in different mental illnesses. A typical example lies in the spectrum nature of schizophrenia, which stems from at least three sources. First, genetic risk, which in itself can be decomposed into a complex polygenetic basis with a large number of single-genome variants conveying (small) risk (O’Donovan et al., 2008; Ripke et al., 2013) and rare copy number variants (CNVs) contributing larger risk effects (International Schizophrenia Consortium, 2008; Stefansson et al., 2014), showing a substantial overlap with bordering disorders such as bipolar disorder (Lee et al., 2013). Although there is evidence that the identified genetic variants may converge on only a limited set of intracellular signaling pathways (Krystal and State, 2014), neuroimaging studies suggest pleiotropic effects of single SNPs and sets of variants on different subsystems, such as working memory (Esslinger et al., 2009), emotional processing (Cao et al., 2016), or reward anticipation (Grimm et al., 2014). 

Second, social-environmental factors, such as obstetric complications (Nicodemus et al., 2008), cannabis use (Hall and Degenhardt, 2008; Moore et al., 2007), stress, urban upbringing (Krabbendam and van Os, 2005), and migration (Cantor-Graae and Selten, 2005) contribute to the risk of schizophrenia and impact specific neural circuits (Akdeniz et al., 2014; Lederbogen et al., 2011). Although as a group these factors explain less risk than genes, individually they have an associated risk that far exceeds that of common genetic variants (Meyer-Lindenberg, 2010). The neural mechanisms underlying these environmental factors are only now coming into focus, with one such proposed mechanism being social stress, which activates the hypothalamic-pituitary-adrenal axis and sensitizes dopaminergic circuitry (Lieberman et al., 1997). Similar to genes, environmental risk factors tend to be associated with several categorical psychiatric disorders, and they may contribute to underlying vulnerability to many psychiatric symptoms (Caspi et al., 2014). The story is further complicated by gene-environment interactions. For example, most of the abovementioned social-environmental risk factors modulate the expression of risk genes (van Os et al., 2008) and change their methylation, resulting in longterm and partly heritable (epigenetic) effects. 

Third, most mental disorders, and certainly schizophrenia, have a developmental aspect: they manifest in functional and structural brain alterations prior to the actual symptomatic onset of the disease. Further, many risk factors have a specific vulnerability time window in which their influence can change the trajectory of brain development toward states of illness (Millan et al., 2016). While studies of healthy brain network architecture increasingly take different developmental trajectories into account (Di Martino et al., 2014; Satterthwaite et al., 2016), studies on mental disorders addressing developmental effects are relatively rare (Di Martino et al., 2014). 

The combination of the factors described above (polygenetic basis, social-environmental, and developmental factors) leads to a heterogeneous dysfunction of differential systems that are unlikely to respect current diagnostic boundaries. While the heterogeneity within and the comorbidity across diagnostic categories are beginning to be appreciated, most neuroimaging and network neuroscience studies use categorical diagnostic categories to compare disease states. As such, work applying 

Neuron 97, January 3, 2018 21 

Neuron 

Review 

**==> picture [60 x 60] intentionally omitted <==**

network methodologies that adhere to existing diagnostic categories will inherit existing difficulties in identifying the mechanisms underlying heterogeneous and diffuse disorders. Innovations in network methodologies, then, must be paired with innovations in theoretical frameworks that focus less on monothetic criteria and more on the dimensional and multiplex nature of mental disorders, such as RDoC and emerging network approaches (Borsboom, 2017; Fried and Cramer, 2017; Insel, 2010). 

## Complexity on Biological and Temporal Scales 

As outlined above, various pathophysiological mechanisms contribute to the heterogeneity of mental disorders likely to be reflected in the dysfunction of different underlying biological systems. These systems, however, show perturbations over a large range of spatial and temporal scales, starting from genes and molecules through neurons and ending in brain systems driving behavior. For example, schizophrenia is increasingly recognized as a disorder of widespread disturbances in the dynamics of large-scale brain networks (Fornito et al., 2012), extending the prominent concept of dysconnectivity in schizophrenia (Stephan et al., 2009). This dysconnectivity is grounded in two different but interrelated pathophysiological mechanisms: (1) topological aberrations in the structural connectome (Fornito et al., 2012, 2015; Zalesky et al., 2015), stemming from impaired developmental processes such as neuronal migration and maturation (Fatemi and Folsom, 2009); and (2) physiological aberrations in the functional interactions between brain regions and cognitive systems. These altered functional interactions have been conceptually linked to the pathophysiological changes observed over a range of spatial and temporal scales in schizophrenia. Many genomewide risk variants converge on dysfunctions in synaptic transmission, especially of glutamatergic and dopaminergic pathways (Kantrowitz and Javitt, 2010; Ripke et al., 2013; Stephan et al., 2009). This primary pathology at the level of synapses then leads to impaired feedback loops in microcircuits, which in turn result in asynchronous firing of long-range pyramidal neurons and, consequently, to impaired synchrony between distant brain regions, eventually resulting in impaired long-range connectivity. 

Although these multiple and hierarchical levels of pathophysiological mechanisms have been linked to one another from a theoretical perspective (Stephan et al., 2009; Uhlhaas and Singer, 2010, 2012), network neuroscience studies incorporating different spatial scales and different imaging modalities are relatively rare. Previously developed approaches, such as imaging genetics, have contributed substantially to our understanding of brain function, but they are in need of extension beyond taking single genetic variants into account. Moreover, without an explicit attempt to model dynamic effects on other brain areas, these approaches, too, are in danger of remaining descriptive. Dynamical studies would be particularly useful in examining patient groups, where a multi-level approach would offer a window into the molecular and cellular underpinnings of pathophysiology, while simultaneously identifying targets for future treatments (Frank and Hargreaves, 2003; Smucny et al., 2014). 

## Targeting Interventions to Brain Systems 

Neuroimaging approaches can be used to characterize brain function at the system level. However, this scale of inquiry is 

not directly targeted by current pharmacological interventions, which instead act at the molecular scale, or by current psychotherapeutic interventions, which instead target assessable behavior, cognition, and affect. Studies bridging molecular and systems scales are relatively rare and include pharmacological imaging or imaging genetics. Yet even these approaches are inherently descriptive in nature, hampering the identification of mechanisms that can be targeted with molecular interventions. Some therapeutic strategies currently under development, such as deep brain stimulation (Lozano et al., 2008; Puigdemont et al., 2009; Schlaepfer and Lieb, 2005) and neurofeedback (Cohen Kadosh et al., 2016; Hamilton et al., 2016; Paret et al., 2016), explicitly target system-level circuit dysfunction. However, due to our limited mechanistic account of how local perturbations impact whole-brain dynamics (Saenger et al., 2017), brain imaging has so far contributed little to the identification of interventional targets on a system level, despite being ideally suited to do so (Bassett and Khambhati, 2017). 

In summary, many of the challenges outlined above are inherent to the approaches of biological (and even computational) psychiatry and cannot exclusively be tackled with increasingly sophisticated data analysis methods. In particular, the phenotypic and biological heterogeneity of mental disorders requires a restructuring of our conceptual and theoretical frameworks, our hypotheses, and our empirical study designs, such as proposed by the recent RDoC initiative. This change in perspective can be usefully complemented by an intensified search for mechanistic network models that align with core psychopathological processes rather than with disease entities. Since a mechanistic description (as provided by multi-dimensional network neuroscience tools) requires a characterization of the objects involved and their spatiotemporal dynamic organization, these models are likely to capture underlying (patho)physiological processes more accurately than correlative depictions of the final outcomes of those processes. Therefore, some of the limitations of current neuroimaging and network neuroscience approaches, particularly in terms of developmental trajectories, multimodal approaches, and increasingly mechanistic understanding of circuits’ multi-level dysfunction, can be overcome by multi-dimensional network neuroscience. In the following sections, we will briefly outline how combinations of multidimensional network neuroscience with pharmacological, intermediate phenotype, genetic, and cross-species studies could potentially advance this important translational enterprise. 

## Developmental Trajectories and Network Formation 

Growing evidence supports the notion that brain networks are altered in many disorders prior to disease onset (Di Martino et al., 2014) and that differential trajectories after onset are based on genetic risk architecture and (even) pharmacological interventions. However, most current studies of mental disorders ignore the notion of dynamically changing brains over the lifespan, due to the lack of appropriate modeling approaches that incorporate empirical estimates for parameters of brain network development. Here, multilayer network approaches could offer a key advantage in explicitly modeling time dependence of network reconfiguration (Betzel and Bassett, 2016; Mucha et al., 2010; Muldoon and Bassett, 2016). For example, in autism, different changes in several brain systems at different age ranges 

22 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [491 x 312] intentionally omitted <==**

Figure 4. Graphical Summary of Multilayer Network Approaches and Developmental Applications (A) Temporal network approaches link connectivity matrices that represent a networks’ connectivity pattern at a particular time in an ordinal fashion as follows: node i in layer s (time window) is linked to node i in the adjacent time windows, s – 1 and s + 1. Multilayer network approaches can then be used to find timeresolved patterns of coherent connectivity over time. Two essential model parameters determine the temporal cohesiveness (6) and the structural scale of resolution (g). (B) Fair et al. demonstrate a shift from local, anatomically arranged organization to a more functionally distributed network architecture during development; adapted from Fair et al. (2009). 

(C) Braun et al. (2016) used temporal networks to investigate the time-resolved reconfiguration of functional brain networks during a working memory task. Schizophrenia patients (SZ) and first-degree relatives (REL) showed more inefficient reconfiguration than healthy controls (HC), as measured by a network flexibility metric. Interestingly, such a high-flexibility state could be induced in healthy controls by administering an NMDA receptor antagonist (DXM), pointing toward a critical role of glutamate in the development of less stable network patterns in schizophrenia. Error bars indicate SEM. (D) A schematic representation of changes in community structure in typically developing (TD) and autism spectrum disorder (ASD) subjects, as assessed by multilayer community detection tools. 

have been described (Ecker et al., 2015; Supekar et al., 2009; Uddin et al., 2013), but whether those differences are due to aberrant developmental trajectories or to idiosyncrasies characteristic of autism spectrum disorder (ASD) brains remains under debate (Byrge et al., 2015; Uddin, 2015). The application of multilayer community detection methods on longitudinal samples, in which model parameters can be tuned to emphasize either idiosyncrasies of individual subjects or properties common to the entire cohort, can be used to disentangle both influences on the development of brain systems. Assessing the age-dependent variability within and between subjects could help to identify critical periods in development during which community structure undergoes major reorganization (Figure 4). Identification of these critical periods in neurodevelopmental disorders like autism and schizophrenia could provide insight into periods for which interventions can be focused, such as during periods of high plasticity (Di Martino et al., 2014). Moreover, the identifica- 

tion of brain systems or regions that show particularly swift reorganization at certain ages could provide anatomical targets for neurotherapeutic interventions, such as transcranial magnetic stimulation (TMS). 

In addition to multilayer network approaches, generative growth models of brain networks have proven useful in explaining brain network reconfiguration during healthy aging (Betzel et al., 2016a). A natural next step would, therefore, be to encode predicted neurodevelopmental alterations, such as are observed in autism or subsequent to genetic or environmental variation, in a generative disordered growth model (Figure 4). Such a model could also be used to probe mechanism of pruning in healthy adolescence. Similarly, one could choose to encode predicted alterations in abnormal aging, such as are observed in Alzheimer’s disease, in a generative disordered aging model (Ve´ rtes and Bullmore, 2015) built to probe mechanism of network degeneration. While these ideas represent exciting possibilities 

Neuron 97, January 3, 2018 23 

Neuron 

Review 

**==> picture [60 x 60] intentionally omitted <==**

for future work, current generative network models have only incorporated intrinsic network features, such as degree, as parameters for their growth rules. Nevertheless, inclusion of neurobiologically derived parameters is feasible, and it could provide more biologically informed models of network growth. For example, regional plaque deposition could be included as a predictor of network growth in Alzheimer’s disease, or regional and age-dependent gene co-expression data could be included as a predictor of network alteration in schizophrenia and autism. These models could then be tested explicitly in neuroimaging data acquired in neurodevelopmental disorders and disorders of normal aging. Because these models are mechanistic, they offer the potential for disentangling different developmental processes and identifying underlying cellular mechanisms, such as alterations in axonal guidance or synaptic pruning. 

## Controlling the Brain and Steering Trajectories 

Many psychiatric conditions are associated with topological alterations of structural networks (Filippi et al., 2013; Fornito and Bullmore, 2015; Fornito et al., 2015; Hulshoff Pol and Bullmore, 2013). Interestingly, these alterations can have profound implications for brain dynamics (Deco et al., 2011, 2017; Honey et al., 2007, 2009), but they are rarely invoked to explain how psychopathology arises and unfolds. Control theory offers a unique perspective for understanding the functional consequences of altered structural networks, and it also provides a mechanistic explanation for how atypical patterns of functional connectivity, such as those observed in diseases like schizophrenia, arise as a consequence of structural features. The critical nature of the link between structure and function in the sense of state dynamics is in agreement with recent work demonstrating that the structure of the underlying network not only shapes passive dynamics, e.g., where control is not explicitly considered, but also has implications for evoked dynamics elicited by interventions informed by theories of network control (Gates and Rocha, 2016). Understanding these relationships would not only provide a link between brain circuits and cross-sectional psychopathology but also provide insight into the manner in which behavioral abnormalities manifest over time. Striking instability (as in bipolar disorder or emotion regulation in borderline personality disorder) and striking resistance to change (as in obsessive-compulsive disorder) are among the most salient features of mental illness that could be brought under the common explanatory paradigm of network control. 

A central idea regarding the dynamics of functional networks is that the brain transitions through various states, switching from one activity pattern to another as cognitive processes unfold (Shine et al., 2016b; Kaufman and Churchland, 2016). In the context of a mental illness such as schizophrenia, both theoretical and empirical accounts point toward an impaired ability to maintain stable activity patterns, switch between states, and transition through them in an appropriate fashion (Braun et al., 2016; Du et al., 2016; Durstewitz and Seamans, 2008). In principle, these theories and empirical observations align with recent findings of a subtle randomization of structural brain networks in schizophrenia (Lo et al., 2015a; Rubinov and Bullmore, 2013a, 2013b) accompanied by a less differentiated modular architecture and fewer hubs in functional networks (AlexanderBloch et al., 2014; Bassett et al., 2006; Yu et al., 2012). Emerging 

data from network control studies demonstrate that such a topological configuration is associated with less energetic state transitions (Betzel et al., 2016b), thereby offering a possible mechanistic explanation for how aberrations in the structural network architecture could lead to less stable functional states in schizophrenia. Examinations of state transitions in schizophrenia within the framework of control theory could offer a means of validating or falsifying such hypotheses. Moreover, they could offer a means of inferring which brain regions within these networks are most important in facilitating the transition between specific states, thereby identifying putative targets for interventions. 

To identify tractable targets for a translational approach, the next question would be, which intrinsic (molecular and neuronal) properties of brain regions influence their control properties? Theoretical and experimental accounts suggest that brain state transitions critically depend on glutamatergic and GABA-ergic signaling (Braun et al., 2016; Uhlhaas et al., 2010; Uhlhaas and Singer, 2012), while the general capability or readiness to switch to certain states may be critically modulated by more tonic monoaminergic processes (Uhlhaas and Singer, 2012), such as serotonergic, dopaminergic (Durstewitz and Seamans, 2008), and noradrenergic (Shine et al., 2016a, 2016b) signaling. Many drugs target these systems and thereby influence important order parameters of whole-brain dynamics in a way that network control theory can make computationally tractable. In addition, network control theory would, in principle, allow the identification of control hubs to which interventions could be targeted both (1) indirectly through, for example, cognitive-behavioral therapy; and (2) directly through, for example, deep brain stimulation (DBS) (Figure 3D). For example, in patients experiencing treatment-resistant depression, where deep brain stimulation protocols can deliver strong stimulation to a specific region with the aim of inducing plasticity in a distributed circuit, one could possibly in the future use control theory to identify such brain regions that would restore the brain trajectories to healthy states and use them as targets for fMRI-based biofeedback or in the far future even stimulation. Of course, extensive clinical validation is needed before such an effort can be attempted. 

In principle, network control theory could also be used to identify (potential) pharmacological targets. For example, a recent study combing several imaging datasets comprising information about vascular, functional, structural, metabolic, and amyloid deposition features of brains in healthy and Alzheimer’s disease patients sought to disentangle differential biological contributions and interventional strategies on controlled brain trajectories (Iturria-Medina et al., 2017). Interestingly, although the authors could identify vascular dysregulation as the initial pathologic event leading to late-onset Alzheimer’s, singular therapeutic options proved inefficient to the complex interplay among multiple pathological interactions. 

A different strategy for the multimodal assessment and identification of putative treatment targets could be to combine network control theory and bio-physical network models (BNMs) (Muldoon et al., 2016b). These whole-brain network models are becoming increasingly important tools to model and predict the dynamics of a human brain based on its underlying structural network (Deco et al., 2011, 2017; Deco and Kringelbach, 2014). The process of constructing a BNM requires two 

24 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

steps: a neural mass model reflecting the internal dynamics among populations of neurons and defined at the level of brain regions, and a structural network reflecting the coupling architecture that connects those regions. Recently, model construction has been dramatically simplified by automated processing pipelines such as The Virtual Brain (Schirner et al., 2015), which enables individual and personalized modeling of (aberrant) brain dynamics (Falcon et al., 2016). Studies applying BNMs to epilepsy (Jirsa et al., 2014, 2017; Proix et al., 2017), Parkinson’s disease (Saenger et al., 2017), schizophrenia (Yang et al., 2016), and other neuropsychiatric disorders (Deco and Kringelbach, 2014; Lord et al., 2017) have demonstrated their potential to uncover causal mechanisms of dysfunction and possible therapeutic targets. Moreover, these BNMs can also be used to study the impact of tuning regional characteristics, such as inhibitoryexcitatory balance implicated in mental disorders (Yang et al., 2016), and to predict the network-level impact of these focal perturbations in neurological disease (Saenger et al., 2017). Validation of such models in experimental pharmacological imaging datasets from healthy subjects could provide a valuable mechanistic description of how particular pharmacological interventions drive system-level brain dynamics. 

## Multi-dimensional Network Neuroscience Bridging Levels of Human Brain Function 

Although the strategies outlined above for identifying cross-disorder mechanisms of disease or aberrant function can provide evidence for system-level mechanisms of dysfunction based on neuroimaging, most mental disorders show aberrations across other spatial scales as well. For example, while alterations of NMDA receptor-dependent inhibitory and excitatory dysbalance can be assessed by combining imaging genetics, pharmaco-fMRI, and network neuroscience (Braun et al., 2016), studying the system-level impact of precise and reversible interventions on the cellular and molecular levels is not currently feasible in humans. Emerging experimental strategies to better understand the interactions between molecular and genetic alterations on system-level dysfunction in humans include the use of positron emission topography (PET)-fMRI and the combination of stem cells with (f)MRI as models of neuropsychiatric diseases (Falk et al., 2016; Werner et al., 2015). In addition, as previous research has revealed shared spatial and functional characteristics of the intrinsic network architecture of the brain across species, including mice, rats, and humans, crossspecies research on brain networks offers the unique opportunity to study interventional approaches on multiple levels (Becker et al., 2016; Smucny et al., 2014). Particularly, animal models allow for direct and precise manipulation of local brain circuits using optogenetics and CRISPR techniques, making them ideally suited to study the impact of local control properties on system-level dynamics. Translational imaging studies, combining such invasive tools in animals with imaging genetics and pharmacological approaches in humans targeting the same underlying neurotransmitter system, could contribute immensely to our cellular understanding of system-level control properties in health and their alterations in disease. 

Beyond the required progress in experimental and acquisition methods, a complementary strategy to link cellular, molecular, 

and neuronal alterations to large-scale connectivity variation lies in direct pharmacological manipulations in healthy subjects (Anticevic et al., 2015; Smucny et al., 2014). Candidate substances such as ketamine, a potent NMDA receptor antagonist, can be used to transiently and reversibly induce disorder-like symptoms in healthy subjects and thereby test, in a hypothesis-driven manner, the effects of a precise neurotransmitter perturbation (Becker et al., 2016; Grimm et al., 2015; Scheidegger et al., 2012). The first studies using ketamine have demonstrated that network approaches (Becker et al., 2016; Lv et al., 2016) are sensitive to network reconfigurations that occur in response to medication. However, to provide the greatest clinical utility, these pharmacological challenge studies need to be better couched in studies of disease mechanism to establish a converging link among cellular, molecular, and neural mechanisms of (patho)physiological brain function. 

The same point applies to bridging brain system-level function with output measures of behavior and emotion. Until recently, a common focus of neuroimaging studies has been in uncovering the neural basis of psychological functions in isolation. That is, researchers are interested in the extent to which the brain network architecture supporting one function, for example, working memory, adapts in response to external demands (Braun et al., 2015; Shine et al., 2016a, 2016b). However, in daily living, healthy humans continuously apply sequences of psychological functions from different domains, such as emotion regulation, executive functioning, or social interaction (Geschwind et al., 2010; Trull and Ebner-Priemer, 2014), thereby naturally transitioning through different states while accomplishing everyday tasks. Importantly, these state transitions could be profitably studied using network control theory, offering insight into how the brain navigates the transition between differential psychological functions. As altered state stability has been described in schizophrenia and other mental disorders (Braun et al., 2016; Uhlhaas and Singer, 2010; Yao et al., 2015), a natural next step would be to ask how the brain controls the transition between realistic brain states induced by different behaviorally relevant psychological functions and where and how these transitions fail in brain disorders. Using neuroimaging datasets that cover several domains of psychological functioning would enable us to study those brain state transitions and to link them to (most likely interrelated) psychological functions. Further extending current studies to capture psychological functions in everyday life using ambulatory assessment methods (Trull et al., 2015; Wenzel et al., 2016) would allow us to construct integrated network models of (dis)ordered human neural and psychological function that capture mechanisms of dysfunctional brain state transitions as they occur in everyday life. 

## Conclusions 

The methods introduced in this review constitute a limited selection from the broad field of network science. Many methods, such as annotated graphs (Newman and Clauset, 2015), dynamics on networks (Mi�sic� et al., 2015), and hypergraphs (Bassett et al., 2014; Davison et al., 2015) hold promise to further advance the field beyond mere mapping of brain networks. Further, computational whole-brain networks, as discussed briefly above and in detail here (Deco and Kringelbach, 

Neuron 97, January 3, 2018 25 

Neuron 

Review 

**==> picture [60 x 60] intentionally omitted <==**

2014), hold promise in offering complementary and necessary insights into dynamical, mechanistic aspects of brain function in health and disease. While we have come a long way in deriving a biologically rooted view of mental disorders and in disentangling the underlying neural processes, all network approaches presented here have an impressive potential to further advance our understanding of mental disorders toward a more mechanistic view. However, challenging technical, experimental, and conceptual problems remain to be addressed in order to establish their use as candidate clinical tools, and they will require close collaborations between clinicians and biomedical and computational researchers. 

Ashourvan, A., Gu, S., Mattar, M.G., Vettel, J.M., and Bassett, D.S. (2017). The energy landscape underpinning module dynamics in the human brain connectome. Neuroimage 157, 364–380. 

Barabasi, A.L., and Albert, R. (1999). Emergence of scaling in random networks. Science 286, 509–512. 

Barrat, A., Baronchelli, A., Dall’Asta, L., and Loreto, V. (2007). Agreement dynamics on interaction networks with diverse topologies. Chaos 17, 026111. 

Bassett, D.S., and Bullmore, E. (2006). Small-world brain networks. Neuroscientist 12, 512–523. 

Bassett, D.S., and Bullmore, E.T. (2009). Human brain networks in health and disease. Curr. Opin. Neurol. 22, 340–347. 

Bassett, D.S., and Bullmore, E.T. (2016). Small-world brain networks revisited. Neuroscientist. Published online September 21, 2016. https://doi.org/10. 1177/1073858416667720. 

## ACKNOWLEDGMENTS 

We thank David Lydon-Staley for helpful comments on an earlier version of this manuscript. D.S.B. and R.F.B. would also like to acknowledge support from the John D. and Catherine T. MacArthur Foundation, the Alfred P. Sloan Foundation, the Army Research Laboratory and the Army Research Office through contract numbers W911NF-10-2-0022 and W911NF-14-1-0679, the NIH (2-R01-DC-009209-11, 1R01HD086888-01, R01-MH107235, R01MH107703, and R21-M MH-106799), the Office of Naval Research, and the National Science Foundation (BCS-1441502, CAREER PHY-1554488, and BCS-1631550). A.M.-L. acknowledges support from the German Federal Ministry of Education and Research (BMBF, grants 01ZX1314G, 01GQ1003B and Collaborative Research Center 1158 subproject B09), the European Union’s Seventh Framework Programme (FP7, grants 602450, 115300, and 602805) and the Ministry of Science, Research and the Arts of the State of BadenWuerttemberg, Germany (MWK, grant 42-04HV.MED(16)/16/1). H.T. acknowledges support from the German Federal Ministry of Education and Research (BMBF, grant 01GQ1102) and the German Research Foundation (DFG, TO 539/3-1). The content is solely the responsibility of the authors and does not necessarily represent the official views of any of the funding agencies. 

A.M.-L. has received consultant fees from the American Association for the Advancement of Science, Atheneum Partners, Blueprint Partnership, Boehringer Ingelheim, Daimler und Benz Stiftung, Elsevier, F. Hoffmann-La Roche, ICARE Schizophrenia, K.G. Jebsen Foundation, L.E.K Consulting, Lundbeck International Foundation (LINF), R. Adamczak, Roche Pharma, Science Foundation, Sumitomo Dainippon Pharma, Synapsis Foundation – Alzheimer Research Switzerland, and System Analytics. A.M.-L. has received lecture fees including travel fees from Boehringer Ingelheim, Fama Public Relations, Institut d’investigacions Biome` diques August Pi i Sunyer (IDIBAPS), JansPsychiatrie,sen-Cilag, KlinikumLVR KlinikumChristophsbad,Dusseldorf,€ Go¨ ppingen,LWL PsychiatrieVerbundLilly Deutschland,Westfalen-Luzerner Lippe,of Psychiatry,Otsuka SPharmaceuticals,udwestrundfunk€ ReunionsFernsehen,i CienciaStern TV,S.L.,andSpanishVitos KlinikumSociety Kurhessen. 

## REFERENCES 

Achard, S., Salvador, R., Whitcher, B., Suckling, J., and Bullmore, E. (2006). A resilient, low-frequency, small-world human brain functional network with highly connected association cortical hubs. J. Neurosci. 26, 63–72. 

Akdeniz, C., Tost, H., Streit, F., Haddad, L., Wust, S., Sch€ afer, A., Schneider,€ M., Rietschel, M., Kirsch, P., and Meyer-Lindenberg, A. (2014). Neuroimaging evidence for a role of neural social stress processing in ethnic minority-associated environmental risk. JAMA Psychiatry 71, 672–680. 

Alexander-Bloch, A., Giedd, J.N., and Bullmore, E. (2013). Imaging structural co-variance between human brain regions. Nat. Rev. Neurosci. 14, 322–336. 

Alexander-Bloch, A.F., Reiss, P.T., Rapoport, J., McAdams, H., Giedd, J.N., Bullmore, E.T., and Gogtay, N. (2014). Abnormal cortical growth in schizophrenia targets normative modules of synchronized development. Biol. Psychiatry 76, 438–446. 

Anticevic, A., Corlett, P.R., Cole, M.W., Savic, A., Gancsos, M., Tang, Y., Repovs, G., Murray, J.D., Driesen, N.R., Morgan, P.T., et al. (2015). N-methyl-Daspartate receptor antagonist effects on prefrontal cortical connectivity better model early than chronic schizophrenia. Biol. Psychiatry 77, 569–580. 

Bassett, D.S., and Khambhati, A.N. (2017). A network engineering perspective on probing and perturbing cognition with neurofeedback. Ann. N Y Acad. Sci. 1396, 126–143. 

Bassett, D.S., and Sporns, O. (2017). Network neuroscience. Nat. Neurosci. 20, 353–364. 

Bassett, D.S., Meyer-Lindenberg, A., Achard, S., Duke, T., and Bullmore, E. (2006). Adaptive reconfiguration of fractal small-world human brain functional networks. Proc. Natl. Acad. Sci. USA 103, 19518–19523. 

Bassett, D.S., Brown, J.A., Deshpande, V., Carlson, J.M., and Grafton, S.T. (2011a). Conserved and variable architecture of human white matter connectivity. Neuroimage 54, 1262–1279. 

Bassett, D.S., Wymbs, N.F., Porter, M.A., Mucha, P.J., Carlson, J.M., and Grafton, S.T. (2011b). Dynamic reconfiguration of human brain networks during learning. Proc. Natl. Acad. Sci. USA 108, 7641–7646. 

Bassett, D.S., Wymbs, N.F., Rombach, M.P., Porter, M.A., Mucha, P.J., and Grafton, S.T. (2013). Task-based core-periphery organization of human brain dynamics. PLoS Comput. Biol. 9, e1003171. 

Bassett, D.S., Wymbs, N.F., Porter, M.A., Mucha, P.J., and Grafton, S.T. (2014). Cross-linked structure of network evolution. Chaos 24, 013112. 

Bassett, D.S., Yang, M., Wymbs, N.F., and Grafton, S.T. (2015). Learninginduced autonomy of sensorimotor systems. Nat. Neurosci. 18, 744–751. 

Becker, R., Braun, U., Schwarz, A.J., Gass, N., Schweiger, J.I., Weber-Fahr, W., Schenker, E., Spedding, M., Clemm von Hohenberg, C., Risterucci, C., et al. (2016). Species-conserved reconfigurations of brain network topology induced by ketamine. Transl. Psychiatry 6, e786. 

Betzel, R.F., and Bassett, D.S. (2016). Multi-scale brain networks. Neuroimage 160, 73–83. 

Betzel, R.F., Avena-Koenigsberger, A., Gon˜ i, J., He, Y., de Reus, M.A., Griffa,A., Ve´ rtes, P.E., Mi�sic, B., Thiran, J.P., Hagmann, P., et al. (2016a). Generative models of the human connectome. Neuroimage 124 (Pt A), 1054–1064. 

Betzel, R.F., Gu, S., Medaglia, J.D., Pasqualetti, F., and Bassett, D.S. (2016b). Optimally controlling the human connectome: the role of network topology. Sci. Rep. 6, 30770. 

Bollobas, B. (1985). Random Graphs London (Academic Press). 

Bollobas, B. (2012). Graph Theory: An Introductory Course, Volume 63 (Springer Science & Business Media). 

Borgatti, S.P., and Everett, M.G. (2000). Models of core/periphery structures. Soc. Networks 21, 375–395. 

Borsboom, D. (2017). A network theory of mental disorders. World Psychiatry 16, 5–13. 

Brady, K.T., Killeen, T.K., Brewerton, T., and Lucerini, S. (2000). Comorbidity of psychiatric disorders and posttraumatic stress disorder. J. Clin. Psychiatry 7, 22–32. 

Braun, U., Schafer, A., Walter, H., Erk, S., Romanczuk-Seiferth, N., Haddad, L.,€ Schweiger, J.I., Grimm, O., Heinz, A., Tost, H., et al. (2015). Dynamic 

26 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

reconfiguration of frontal brain networks during executive cognition in humans. Proc. Natl. Acad. Sci. USA 112, 11678–11683. 

Braun, U., Schafer, A., Bassett, D.S., Rausch, F., Schweiger, J.I., Bilek, E., Erk,€ S., Romanczuk-Seiferth, N., Grimm, O., Geiger, L.S., et al. (2016). Dynamic brain network reconfiguration as a potential schizophrenia genetic risk mechanism modulated by NMDA receptor function. Proc. Natl. Acad. Sci. USA 113, 12568–12573. 

Brookes, M.J., Tewarie, P.K., Hunt, B.A.E., Robson, S.E., Gascoyne, L.E., Liddle, E.B., Liddle, P.F., and Morris, P.G. (2016). A multi-layer network approach to MEG connectivity analysis. Neuroimage 132, 425–438. 

Buldyrev, S.V., Parshani, R., Paul, G., Stanley, H.E., and Havlin, S. (2010). Catastrophic cascade of failures in interdependent networks. Nature 464, 1025–1028. 

Bullmore, E., and Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. Nat. Rev. Neurosci. 10, 186–198. 

Bullmore, E., and Sporns, O. (2012). The economy of brain network organization. Nat. Rev. Neurosci. 13, 336–349. 

Byrge, L., Dubois, J., Tyszka, J.M., Adolphs, R., and Kennedy, D.P. (2015). Idiosyncratic brain activation patterns are associated with poor social comprehension in autism. J. Neurosci. 35, 5837–5850. 

Cabral, J., Kringelbach, M.L., and Deco, G. (2017). Functional connectivity dynamically evolves on multiple time-scales over a static structural connectome: models and mechanisms. Neuroimage 160, 84–96. 

Campbell, C., Ruths, J., Ruths, D., Shea, K., and Albert, R. (2015). Topological constraints on network control profiles. Sci. Rep. 5, 18693. 

Canolty, R.T., and Knight, R.T. (2010). The functional role of cross-frequency coupling. Trends Cogn. Sci. 14, 506–515. 

Canolty, R.T., Edwards, E., Dalal, S.S., Soltani, M., Nagarajan, S.S., Kirsch, H.E., Berger, M.S., Barbaro, N.M., and Knight, R.T. (2006). High gamma power is phase-locked to theta oscillations in human neocortex. Science 313, 1626–1628. 

Cantor-Graae, E., and Selten, J.P. (2005). Schizophrenia and migration: a meta-analysis and review. Am. J. Psychiatry 162, 12–24. 

Cao, H., Bertolino, A., Walter, H., Schneider, M., Schafer,€ A., Taurisano, P., Blasi, G., Haddad, L., Grimm, O., Otto, K., et al. (2016). Altered functional subnetwork during emotional face processing: a potential intermediate phenotype for schizophrenia. JAMA Psychiatry 73, 598–605. 

Caspi, A., Houts, R.M., Belsky, D.W., Goldman-Mellor, S.J., Harrington, H., Israel, S., Meier, M.H., Ramrakha, S., Shalev, I., Poulton, R., and Moffitt, T.E. (2014). The p factor: one general psychopathology factor in the structure of psychiatric disorders? Clin. Psychol. Sci. 2, 119–137. 

Chai, L.R., Mattar, M.G., Blank, I.A., Fedorenko, E., and Bassett, D.S. (2016). Functional network dynamics of the language system. Cereb. Cortex 26, 4148–4159. 

Ching, S., Purdon, P.L., Vijayan, S., Kopell, N.J., and Brown, E.N. (2012). A neurophysiological-metabolic model for burst suppression. Proc. Natl. Acad. Sci. USA 109, 3095–3100. 

Cohen Kadosh, K., Luo, Q., de Burca, C., Sokunbi, M.O., Feng, J., Linden, D.E.J., and Lau, J.Y.F. (2016). Using real-time fMRI to influence effective connectivity in the developing emotion regulation network. Neuroimage 125, 616–626. 

Cole, M.W., Bassett, D.S., Power, J.D., Braver, T.S., and Petersen, S.E. (2014). Intrinsic and task-evoked network architectures of the human brain. Neuron 83, 238–251. 

Cramer, A.O., Waldorp, L.J., van der Maas, H.L., and Borsboom, D. (2010). Comorbidity: a network perspective. Behav. Brain Sci. 33, 137–150. 

Craver, C.F., and Darden, L. (2013). In Search of Mechanisms: Discoveries across the Life Sciences (University of Chicago Press). 

Craver, C., and Tabery, J. (2015). Mechanisms in science. In The Stanford Encyclopedia of Philosophy, E.N. Zalta, ed. (Metaphysics Research Lab, Stanford University). 

Davison, E.N., Schlesinger, K.J., Bassett, D.S., Lynall, M.E., Miller, M.B., Grafton, S.T., and Carlson, J.M. (2015). Brain network adaptability across task states. PLoS Comput. Biol. 11, e1004029. 

De Domenico, M., Sasai, S., and Arenas, A. (2016a). Mapping multiplex hubs in human functional brain networks. Front. Neurosci. 10, 326. 

De Domenico, M., Granell, C., Porter, M.A., and Arenas, A. (2016b). The physics of spreading processes in multilayer networks. Nat. Phys. 12, 901–906. 

de Solla Price, D.J. (1965). Networks of scientific papers. Science 149, 510–515. 

Deco, G., and Kringelbach, M.L. (2014). Great expectations: using whole-brain computational connectomics for understanding neuropsychiatric disorders. Neuron 84, 892–905. 

Deco, G., Jirsa, V.K., and McIntosh, A.R. (2011). Emerging concepts for the dynamical organization of resting-state activity in the brain. Nat. Rev. Neurosci. 12, 43–56. 

Deco, G., Van Hartevelt, T.J., Fernandes, H.M., Stevner, A., and Kringelbach, M.L. (2017). The most relevant human brain regions for functional connectivity: evidence for a dynamical workspace of binding nodes from whole-brain computational modelling. Neuroimage 146, 197–210. 

Di Martino, A., Fair, D.A., Kelly, C., Satterthwaite, T.D., Castellanos, F.X., Thomason, M.E., Craddock, R.C., Luna, B., Leventhal, B.L., Zuo, X.N., and Milham, M.P. (2014). Unraveling the miswired connectome: a developmental perspective. Neuron 83, 1335–1353. 

Doron, K.W., Bassett, D.S., and Gazzaniga, M.S. (2012). Dynamic network structure of interhemispheric coordination. Proc. Natl. Acad. Sci. USA 109, 18661–18668. 

Du, Y., Pearlson, G.D., Yu, Q., He, H., Lin, D., Sui, J., Wu, L., and Calhoun, V.D. (2016). Interaction among subsystems within default mode network diminished in schizophrenia patients: a dynamic connectivity approach. Schizophr. Res. 170, 55–65. 

Durstewitz, D., and Seamans, J.K. (2008). The dual-state theory of prefrontal cortex dopamine function with relevance to catechol-o-methyltransferase genotypes and schizophrenia. Biol. Psychiatry 64, 739–749. 

Ecker, C., Bookheimer, S.Y., and Murphy, D.G. (2015). Neuroimaging in autism spectrum disorder: brain structure and function across the lifespan. Lancet Neurol. 14, 1121–1134. 

Eichler, K., Li, F., Litwin-Kumar, A., Park, Y., Andrade, I., Schneider-Mizell, C.M., Saumweber, T., Huser, A., Eschbach, C., Gerber, B., et al. (2017). The complete connectome of a learning and memory centre in an insect brain. Nature 548, 175–182. 

Ercsey-Ravasz, M., Markov, N.T., Lamy, C., Van Essen, D.C., Knoblauch, K., Toroczkai, Z., and Kennedy, H. (2013). A predictive network model of cerebral cortical connectivity based on a distance rule. Neuron 80, 184–197. 

Esslinger, C., Walter, H., Kirsch, P., Erk, S., Schnell, K., Arnold, C., Haddad, L., Mier, D., Opitz von Boberfeld, C., Raab, K., et al. (2009). Neural mechanisms of a genome-wide supported psychosis variant. Science 324, 605. 

Evans, A.C. (2013). Networks of anatomical covariance. Neuroimage 80, 489–504. 

Fair, D.A., Cohen, A.L., Power, J.D., Dosenbach, N.U., Church, J.A., Miezin, F.M., Schlaggar, B.L., and Petersen, S.E. (2009). Functional brain networks develop from a ‘‘local to distributed’’ organization. PLoS Comput. Biol. 5, e1000381. 

Falcon, M.I., Jirsa, V., and Solodkin, A. (2016). A new neuroinformatics approach to personalized medicine in neurology: The Virtual Brain. Curr. Opin. Neurol. 29, 429–436. 

Falk, A., Heine, V.M., Harwood, A.J., Sullivan, P.F., Peitz, M., Brustle, O., Shen,€ S., Sun, Y.M., Glover, J.C., Posthuma, D., and Djurovic, S. (2016). Modeling psychiatric disorders: from genomic findings to cellular phenotypes. Mol. Psychiatry 21, 1167–1179. 

Fatemi, S.H., and Folsom, T.D. (2009). The neurodevelopmental hypothesis of schizophrenia, revisited. Schizophr. Bull. 35, 528–548. 

Neuron 97, January 3, 2018 27 

Neuron 

Review 

**==> picture [60 x 60] intentionally omitted <==**

Fedorenko, E., and Thompson-Schill, S.L. (2014). Reworking the language network. Trends Cogn. Sci. 18, 120–126. 

Filippi, M., van den Heuvel, M.P., Fornito, A., He, Y., Hulshoff Pol, H.E., Agosta, F., Comi, G., and Rocca, M.A. (2013). Assessment of system dysfunction in the brain through MRI-based connectomics. Lancet Neurol. 12, 1189–1199. 

Fornito, A., and Bullmore, E.T. (2015). Connectomics: a new paradigm for understanding brain disease. Eur. Neuropsychopharmacol. 25, 733–748. 

Fornito, A., Zalesky, A., Pantelis, C., and Bullmore, E.T. (2012). Schizophrenia, neuroimaging and connectomics. Neuroimage 62, 2296–2314. 

Fornito, A., Zalesky, A., and Breakspear, M. (2015). The connectomics of brain disorders. Nat. Rev. Neurosci. 16, 159–172. 

Fortunato, S. (2010). Community detection in graphs. Phys. Rep. 486, 75–174. 

Frank, R., and Hargreaves, R. (2003). Clinical biomarkers in drug discovery and development. Nat. Rev. Drug Discov. 2, 566–580. 

Fried, E.I., and Cramer, A.O.J. (2017). Moving Forward: challenges and directions for psychopathological network theory and methodology. Perspect. Psychol. Sci. Published online August 1, 2017. https://doi.org/10.1177/ 1745691617705892. 

Fried, E.I., and Nesse, R.M. (2015). Depression is not a consistent syndrome: An investigation of unique symptom patterns in the STAR*D study. J. Affect. Disord. 172, 96–102. 

Friston, K.J. (2011). Functional and effective connectivity: a review. Brain Connect. 1, 13–36. 

Gala´ n, R.F., Ermentrout, G.B., and Urban, N.N. (2008). Optimal time scale for spike-time reliability: theory, simulations, and experiments. J. Neurophysiol. 99, 277–283. 

Galatzer-Levy, I.R., and Bryant, R.A. (2013). 636,120 ways to have posttraumatic stress disorder. Perspect. Psychol. Sci. 8, 651–662. 

Gates, A.J., and Rocha, L.M. (2016). Control of complex networks requires both structure and dynamics. Sci. Rep. 6, 24456. 

Geschwind, N., Peeters, F., Jacobs, N., Delespaul, P., Derom, C., Thiery, E., van Os, J., and Wichers, M. (2010). Meeting risk with resilience: high daily life reward experience preserves mental health. Acta Psychiatr. Scand. 122, 129–138. 

Giedd, J.N., Lenroot, R.K., Shaw, P., Lalonde, F., Celano, M., White, S., Tossell, J., Addington, A., and Gogtay, N. (2008). Trajectories of anatomic brain development as a phenotype. Novartis Found. Symp. 289, 101–112. 

Glennan, S.S. (1996). Mechanisms and the nature of causation. Erkenntnis 44, 49–71. 

Glennan, S. (2016). Mechanisms and Mechanical Philosophy: The Oxford Handbook of Philosophy of Science (Oxford University Press). 

Gon˜ i, J., van den Heuvel, M.P., Avena-Koenigsberger, A., Velez de Mendizabal, N., Betzel, R.F., Griffa, A., Hagmann, P., Corominas-Murtra, B., Thiran, J.-P., and Sporns, O. (2014). Resting-brain functional connectivity predicted by analytic measures of network communication. Proc. Natl. Acad. Sci. USA 111, 833–838. 

Grimm, O., Heinz, A., Walter, H., Kirsch, P., Erk, S., Haddad, L., Plichta, M.M., Romanczuk-Seiferth, N., Po¨ hland, L., Mohnke, S., et al. (2014). Striatal response to reward anticipation: evidence for a systems-level intermediate phenotype for schizophrenia. JAMA Psychiatry 71, 531–539. 

Grimm, O., Gass, N., Weber-Fahr, W., Sartorius, A., Schenker, E., Spedding, M., Risterucci, C., Schweiger, J.I., Bo¨ hringer, A., Zang, Z., et al. (2015). Acute ketamine challenge increases resting state prefrontal-hippocampal connectivity in both humans and rats. Psychopharmacology (Berl.) 232, 4231–4241. 

Gu, S., Pasqualetti, F., Cieslak, M., Telesford, Q.K., Yu, A.B., Kahn, A.E., Medaglia, J.D., Vettel, J.M., Miller, M.B., Grafton, S.T., and Bassett, D.S. (2015). Controllability of structural brain networks. Nat. Commun. 6, 8414. 

Gu, S., Cieslak, M., Baird, B., Muldoon, S.F., Grafton, S.T., Pasqualetti, F., and Bassett, D.S. (2016). The energy landscape of neurophysiological activity implicit in brain network structure. arXiv, arXiv:1607.01959, https://arxiv.org/abs/ 1607.01959. 

Gu, S., Betzel, R.F., Mattar, M.G., Cieslak, M., Delio, P.R., Grafton, S.T., Pasqualetti, F., and Bassett, D.S. (2017). Optimal trajectories of brain state transitions. Neuroimage 148, 305–317. 

Gutie´ rrez, R., Sendin˜ a-Nadal, I., Zanin, M., Papo, D., and Boccaletti, S. (2012). Targeting the dynamics of complex networks. Sci. Rep. 2, 396. 

Hagmann, P., Cammoun, L., Gigandet, X., Meuli, R., Honey, C.J., Wedeen, V.J., and Sporns, O. (2008). Mapping the structural core of human cerebral cortex. PLoS Biol. 6, e159. 

Hall, W., and Degenhardt, L. (2008). Cannabis use and the risk of developing a psychotic disorder. World Psychiatry 7, 68–71. 

Hamilton, J.P., Glover, G.H., Bagarinao, E., Chang, C., Mackey, S., Sacchet, M.D., and Gotlib, I.H. (2016). Effects of salience-network-node neurofeedback training on affective biases in major depressive disorder. Psychiatry Res. 249, 91–96. 

Hermundstad, A.M., Bassett, D.S., Brown, K.S., Aminoff, E.M., Clewett, D., Freeman, S., Frithsen, A., Johnson, A., Tipper, C.M., Miller, M.B., et al. (2013). Structural foundations of resting-state and task-based functional connectivity in the human brain. Proc. Natl. Acad. Sci. USA 110, 6169–6174. 

Hermundstad, A.M., Brown, K.S., Bassett, D.S., Aminoff, E.M., Frithsen, A., Johnson, A., Tipper, C.M., Miller, M.B., Grafton, S.T., and Carlson, J.M. (2014). Structurally-constrained relationships between cognitive states in the human brain. PLoS Comput. Biol. 10, e1003591. 

Hilgetag, C.C., and Kaiser, M. (2007). Organization and function of complex cortical networks. In Lectures in Supercomputational Neurosciences, P. beim Graben, C. Zhou, M. Thiel, and J. Kurths, eds. (Springer), pp. 107–133. 

Holme, P., and Saramaki,€ J. (2012). Temporal networks. Phys. Rep. 519, 97–125. 

Honey, C.J., Ko¨ tter, R., Breakspear, M., and Sporns, O. (2007). Network structure of cerebral cortex shapes functional connectivity on multiple time scales. Proc. Natl. Acad. Sci. USA 104, 10240–10245. 

Honey, C.J., Sporns, O., Cammoun, L., Gigandet, X., Thiran, J.P., Meuli, R., and Hagmann, P. (2009). Predicting human resting-state functional connectivity from structural connectivity. Proc. Natl. Acad. Sci. USA 106, 2035–2040. 

Hulshoff Pol, H., and Bullmore, E. (2013). Neural networks in psychiatry. Eur. Neuropsychopharmacol. 23, 1–6. 

Hutchison, R.M., Womelsdorf, T., Allen, E.A., Bandettini, P.A., Calhoun, V.D., Corbetta, M., Della Penna, S., Duyn, J.H., Glover, G.H., Gonzalez-Castillo, J., et al. (2013). Dynamic functional connectivity: promise, issues, and interpretations. Neuroimage 80, 360–378. 

Insel, T.R. (2010). Faulty circuits. Sci. Am. 302, 44–51. 

International Schizophrenia Consortium (2008). Rare chromosomal deletions and duplications increase risk of schizophrenia. Nature 455, 237–241. 

Iturria-Medina, Y., Carbonell, F.M., Sotero, R.C., Chouinard-Decorte, F., and Evans, A.C.; Alzheimer’s Disease Neuroimaging Initiative (2017). Multifactorial causal model of brain (dis)organization and therapeutic intervention: Application to Alzheimer’s disease. Neuroimage 152, 60–77. 

Jirsa, V.K., Stacey, W.C., Quilichini, P.P., Ivanov, A.I., and Bernard, C. (2014). On the nature of seizure dynamics. Brain 137, 2210–2230. 

Jirsa, V.K., Proix, T., Perdikis, D., Woodman, M.M., Wang, H., Gonzalez-Martinez, J., Bernard, C., Be´ nar, C., Guye, M., Chauvel, P., and Bartolomei, F. (2017). The Virtual Epileptic Patient: individualized whole-brain models of epilepsy spread. Neuroimage 145 (Pt B), 377–388. 

Kaiser, M. (2017). Mechanisms of Connectome Development. Trends Cogn. Sci. 21, 703–717. 

Kaiser, M., and Hilgetag, C.C. (2006). Nonoptimal component placement, but short processing paths, due to long-distance projections in neural systems. PLoS Comput. Biol. 2, e95. 

Kaiser, M., and Varier, S. (2011). Evolution and development of brain networks: from Caenorhabditis elegans to Homo sapiens. Network 22, 143–147. 

28 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

Kantrowitz, J.T., and Javitt, D.C. (2010). N-methyl-d-aspartate (NMDA) receptor dysfunction or dysregulation: the final common pathway on the road to schizophrenia? Brain Res. Bull. 83, 108–121. 

Kapur, S., Phillips, A.G., and Insel, T.R. (2012). Why has it taken so long for biological psychiatry to develop clinical tests and what to do about it? Mol. Psychiatry 17, 1174–1179. 

Kaufman, M.T., and Churchland, A.K. (2016). Many paths from state to state. Nat. Neurosci. 19, 1541–1542. 

Kessler, R.C., Birnbaum, H., Demler, O., Falloon, I.R., Gagnon, E., Guyer, M., Howes, M.J., Kendler, K.S., Shi, L., Walters, E., and Wu, E.Q. (2005). The prevalence and correlates of nonaffective psychosis in the National Comorbidity Survey Replication (NCS-R). Biol. Psychiatry 58, 668–676. 

Kim, J.Z., Soffer, J.M., Kahn, A.E., Vettel, J.M., Pasqualetti, F., and Bassett, D.S. (2017). Role of graph architecture in controlling dynamical networks with applications to neural systems. Nat. Phys. Published online September 25, 2017. https://doi.org/10.1038/nphys4268. 

Kivela, M., Arenas, A., Barthelemy, M., Gleeson, J.P., Moreno, Y., and Porter,€ M.A. (2014). Multilayer networks. J. Complex Netw. 2, 203–271. 

Korzeniewska, A., Franaszczuk, P.J., Crainiceanu, C.M., Ku�s, R., and Crone, N.E. (2011). Dynamics of large-scale cortical interactions at high gamma frequencies during word production: event related causality (ERC) analysis of human electrocorticography (ECoG). Neuroimage 56, 2218–2237. 

Krabbendam, L., and van Os, J. (2005). Schizophrenia and urbanicity: a major environmental influence–conditional on genetic risk. Schizophr. Bull. 31, 795–799. 

Krystal, J.H., and State, M.W. (2014). Psychiatric disorders: diagnosis to therapy. Cell 157, 201–214. 

Latora, V., and Marchiori, M. (2001). Efficient behavior of small-world networks. Phys. Rev. Lett. 87, 198701. 

Lederbogen, F., Kirsch, P., Haddad, L., Streit, F., Tost, H., Schuch, P., Wust,€ S., Pruessner, J.C., Rietschel, M., Deuschle, M., and Meyer-Lindenberg, A. (2011). City living and urban upbringing affect neural social stress processing in humans. Nature 474, 498–501. 

Lee, S.H., Ripke, S., Neale, B.M., Faraone, S.V., Purcell, S.M., Perlis, R.H., Mowry, B.J., Thapar, A., Goddard, M.E., Witte, J.S., et al.; Cross-Disorder Group of the Psychiatric Genomics Consortium; International Inflammatory Bowel Disease Genetics Consortium (IIBDGC) (2013). Genetic relationship between five psychiatric disorders estimated from genome-wide SNPs. Nat. Genet. 45, 984–994. 

Lee, W.C., Bonin, V., Reed, M., Graham, B.J., Hood, G., Glattfelder, K., and Reid, R.C. (2016). Anatomy and function of an excitatory network in the visual cortex. Nature 532, 370–374. 

Leonardi, N., and Van De Ville, D. (2015). On spurious and real fluctuations of dynamic functional connectivity during rest. Neuroimage 104, 430–436. 

Lieberman, J.A., Sheitman, B.B., and Kinon, B.J. (1997). Neurochemical sensitization in the pathophysiology of schizophrenia: deficits and dysfunction in neuronal regulation and plasticity. Neuropsychopharmacology 17, 205–229. 

Liu, Y.Y., Slotine, J.J., and Baraba´ si, A.L. (2011). Controllability of complex networks. Nature 473, 167–173. 

Lo, C.Y., Su, T.W., Huang, C.C., Hung, C.C., Chen, W.L., Lan, T.H., Lin, C.P., and Bullmore, E.T. (2015a). Randomization and resilience of brain functional networks as systems-level endophenotypes of schizophrenia. Proc. Natl. Acad. Sci. USA 112, 9123–9128. 

Lo, Y.P., O’Dea, R., Crofts, J.J., Han, C.E., and Kaiser, M. (2015b). A geometric network model of intrinsic grey-matter connectivity of the human brain. Sci. Rep. 5, 15397. 

Lord, L.D., Stevner, A.B., Deco, G., and Kringelbach, M.L. (2017). Understanding principles of integration and segregation using whole-brain computational connectomics: implications for neuropsychiatric disorders. Philos. Trans. A Math. Phys. Eng. Sci. 375, 2096. 

Lozano, A.M., Mayberg, H.S., Giacobbe, P., Hamani, C., Craddock, R.C., and Kennedy, S.H. (2008). Subcallosal cingulate gyrus deep brain stimulation for treatment-resistant depression. Biol. Psychiatry 64, 461–467. 

Lv, Q., Yang, L., Li, G., Wang, Z., Shen, Z., Yu, W., Jiang, Q., Hou, B., Pu, J., Hu, H., and Wang, Z. (2016). Large-scale persistent network reconfiguration induced by ketamine in anesthetized monkeys: relevance to mood disorders. Biol. Psychiatry 79, 765–775. 

Machamer, P., Darden, L., and Craver, C.F. (2000). Thinking about mechanisms. Philos. Sci. 67, 1–25. 

Markov, N.T., Ercsey-Ravasz, M., Lamy, C., Ribeiro Gomes, A.R., Magrou, L., Misery, P., Giroud, P., Barone, P., Dehay, C., Toroczkai, Z., et al. (2013a). The role of long-range connections on the specificity of the macaque interareal cortical network. Proc. Natl. Acad. Sci. USA 110, 5187–5192. 

Markov, N.T., Ercsey-Ravasz, M., Van Essen, D.C., Knoblauch, K., Toroczkai, Z., and Kennedy, H. (2013b). Cortical high-density counterstream architectures. Science 342, 1238406. 

Mattar, M.G., Cole, M.W., Thompson-Schill, S.L., and Bassett, D.S. (2015). A functional cartography of cognitive systems. PLoS Comput. Biol. 11, e1004533. 

Medaglia, J.D., Lynall, M.E., and Bassett, D.S. (2015). Cognitive network neuroscience. J. Cogn. Neurosci. 27, 1471–1491. 

Meunier, D., Achard, S., Morcom, A., and Bullmore, E. (2009). Age-related changes in modular organization of human brain functional networks. Neuroimage 44, 715–723. 

Meyer-Lindenberg, A. (2010). From maps to mechanisms through neuroimaging of schizophrenia. Nature 468, 194–202. 

Millan, M.J., Andrieux, A., Bartzokis, G., Cadenhead, K., Dazzan, P., FusarPoli, P., Gallinat, J., Giedd, J., Grayson, D.R., Heinrichs, M., et al. (2016). Altering the course of schizophrenia: progress and perspectives. Nat. Rev. Drug Discov. 15, 485–515. 

Mi�sic, B., Betzel, R.F., Nematzadeh, A., Gon˜ i, J., Griffa, A., Hagmann, P., Flam-� mini, A., Ahn, Y.Y., and Sporns, O. (2015). Cooperative and competitive spreading dynamics on the human connectome. Neuron 86, 1518–1529. 

Moore, T.H., Zammit, S., Lingford-Hughes, A., Barnes, T.R., Jones, P.B., Burke, M., and Lewis, G. (2007). Cannabis use and risk of psychotic or affective mental health outcomes: a systematic review. Lancet 370, 319–328. 

Motter, A.E. (2015). Networkcontrology. Chaos 25, 097621. 

Mucha, P.J., Richardson, T., Macon, K., Porter, M.A., and Onnela, J.P. (2010). Community structure in time-dependent, multiscale, and multiplex networks. Science 328, 876–878. 

Muldoon, S.F., and Bassett, D.S. (2016). Network and multilayer network approaches to understanding human brain dynamics. Philos. Sci. 83, 710–720. 

Muldoon, S.F., Soltesz, I., and Cossart, R. (2013). Spatially clustered neuronal assemblies comprise the microstructure of synchrony in chronically epileptic networks. Proc. Natl. Acad. Sci. USA 110, 3567–3572. 

Muldoon, S.F., Bridgeford, E.W., and Bassett, D.S. (2016a). Small-world propensity and weighted brain networks. Sci. Rep. 6, 22057. 

Muldoon, S.F., Pasqualetti, F., Gu, S., Cieslak, M., Grafton, S.T., Vettel, J.M., and Bassett, D.S. (2016b). Stimulation-based control of dynamic brain networks. PLoS Comput. Biol. 12, e1005076. 

Newman, M.E. (2003). The structure and function of complex networks. SIAM Rev. 45, 167–256. 

Newman, M.E. (2006). Modularity and community structure in networks. Proc. Natl. Acad. Sci. USA 103, 8577–8582. 

Newman, M. (2010). Networks: An Introduction (OUP Oxford). 

Newman, M., and Clauset, A. (2016). Structure and inference in annotated networks. Nat. Commun. 7, 11863. 

Newman, M., Baraba´ si, A.-L., and Watts, D.J. (2006). The Structure and Dynamics of Networks (Princeton University Press). 

Neuron 97, January 3, 2018 29 

Neuron 

Review 

**==> picture [60 x 60] intentionally omitted <==**

Nicodemus, K.K., Marenco, S., Batten, A.J., Vakkalanka, R., Egan, M.F., Straub, R.E., and Weinberger, D.R. (2008). Serious obstetric complications interact with hypoxia-regulated/vascular-expression genes to influence schizophrenia risk. Mol. Psychiatry 13, 873–877. 

O’Donovan, M.C., Craddock, N., Norton, N., Williams, H., Peirce, T., Moskvina, V., Nikolov, I., Hamshere, M., Carroll, L., Georgieva, L., et al.; Molecular Genetics of Schizophrenia Collaboration (2008). Identification of loci associated with schizophrenia by genome-wide association and follow-up. Nat. Genet. 40, 1053–1055. 

Olbert, C.M., Gala, G.J., and Tupler, L.A. (2014). Quantifying heterogeneity attributable to polythetic diagnostic criteria: theoretical framework and empirical application. J. Abnorm. Psychol. 123, 452–462. 

Paret, C., Ruf, M., Gerchen, M.F., Kluetsch, R., Demirakca, T., Jungkunz, M., Bertsch, K., Schmahl, C., and Ende, G. (2016). fMRI neurofeedback of amygdala response to aversive stimuli enhances prefrontal-limbic brain connectivity. Neuroimage 125, 182–188. 

Park, J., and Newman, M.E. (2004). Statistical mechanics of networks. Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 70, 066117. 

Pasqualetti, F., Zampieri, S., and Bullo, F. (2014). Controllability metrics, limitations and algorithms for complex networks. IEEE Transactions on Control of Network Systems 1, 40–52. 

Porter, M.A., Onnela, J.-P., and Mucha, P.J. (2009). Communities in networks. Not. Am. Math. Soc. 56, 1082–1097. 

Po´ sfai, M., Liu, Y.Y., Slotine, J.J., and Baraba´ si, A.L. (2013). Effect of correlations on network controllability. Sci. Rep. 3, 1067. 

Proix, T., Bartolomei, F., Guye, M., and Jirsa, V.K. (2017). Individual brain structure and modelling predict seizure propagation. Brain 140, 641–654. 

Puigdemont, D., Portella, M.J., Pe´ rez-Egea, R., de Diego-Adelin˜ o, J., Gironell, A., Molet, J., Duran-Sindreu, S., Alvarez, E., and Pe´ rez, V. (2009). Depressive relapse after initial response to subcallosal cingulate gyrus-deep brain stimulation in a patient with a treatment-resistant depression: electroconvulsive therapy as a feasible strategy. Biol. Psychiatry 66, e11–e12. 

Ripke, S., O’Dushlaine, C., Chambert, K., Moran, J.L., Kahler, A.K., Akterin, S.,€ Bergen, S.E., Collins, A.L., Crowley, J.J., Fromer, M., et al.; Multicenter Genetic Studies of Schizophrenia Consortium; Psychosis Endophenotypes International Consortium; Wellcome Trust Case Control Consortium 2 (2013). Genome-wide association analysis identifies 13 new risk loci for schizophrenia. Nat. Genet. 45, 1150–1159. 

Roberts, J.A., Perry, A., Lord, A.R., Roberts, G., Mitchell, P.B., Smith, R.E., Calamante, F., and Breakspear, M. (2016). The contribution of geometry to the human connectome. Neuroimage 124 (Pt A), 379–393. 

Rubinov, M., and Bullmore, E. (2013a). Fledgling pathoconnectomics of psychiatric disorders. Trends Cogn. Sci. 17, 641–647. 

Rubinov, M., and Bullmore, E. (2013b). Schizophrenia and abnormal brain network hubs. Dialogues Clin. Neurosci. 15, 339–349. 

Rubinov, M., Ypma, R.J., Watson, C., and Bullmore, E.T. (2015). Wiring cost and topological participation of the mouse brain connectome. Proc. Natl. Acad. Sci. USA 112, 10032–10037. 

Ruths, J., and Ruths, D. (2014). Control profiles of complex networks. Science 343, 1373–1376. 

Saenger, V.M., Kahan, J., Foltynie, T., Friston, K., Aziz, T.Z., Green, A.L., van Hartevelt, T.J., Cabral, J., Stevner, A.B.A., Fernandes, H.M., et al. (2017). Uncovering the underlying mechanisms and whole-brain dynamics of deep brain stimulation for Parkinson’s disease. Sci. Rep. 7, 9882. 

Salvador, R., Suckling, J., Coleman, M.R., Pickard, J.D., Menon, D., and Bullmore, E. (2005). Neurophysiological architecture of functional magnetic resonance images of human brain. Cereb. Cortex 15, 1332–1342. 

Samu, D., Seth, A.K., and Nowotny, T. (2014). Influence of wiring cost on the large-scale architecture of human cortical connectivity. PLoS Comput. Biol. 10, e1003557. 

Santaniello, S., Sherman, D.L., Thakor, N.V., Eskandar, E.N., and Sarma, S.V. (2012). Optimal control-based bayesian detection of clinical and behavioral state transitions. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 708–719. 

Satterthwaite, T.D., Wolf, D.H., Calkins, M.E., Vandekar, S.N., Erus, G., Ruparel, K., Roalf, D.R., Linn, K.A., Elliott, M.A., Moore, T.M., et al. (2016). Structural brain abnormalities in youth with psychosis spectrum symptoms. JAMA Psychiatry 73, 515–524. 

Scheidegger, M., Walter, M., Lehmann, M., Metzger, C., Grimm, S., Boeker, H., Boesiger, P., Henning, A., and Seifritz, E. (2012). Ketamine decreases resting state functional network connectivity in healthy subjects: implications for antidepressant drug action. PLoS ONE 7, e44799. 

Schiff, S.J. (2012). Neural Control Engineering (MIT Press Cambridge). 

Schirner, M., Rothmeier, S., Jirsa, V.K., McIntosh, A.R., and Ritter, P. (2015). An automated pipeline for constructing personalized virtual brains from multimodal neuroimaging data. Neuroimage 117, 343–357. 

Schlaepfer, T.E., and Lieb, K. (2005). Deep brain stimulation for treatment of refractory depression. Lancet 366, 1420–1422. 

Scholtens, L.H., Schmidt, R., de Reus, M.A., and van den Heuvel, M.P. (2014). Linking macroscale graph analytical organization to microscale neuroarchitectonics in the macaque connectome. J. Neurosci. 34, 12192–12205. 

Shine, J.M., Bissett, P.G., Bell, P.T., Koyejo, O., Balsters, J.H., Gorgolewski, K.J., Moodie, C.A., and Poldrack, R.A. (2016a). The dynamics of functional brain networks: integrated network states during cognitive task performance. Neuron 92, 544–554. 

Shine, J.M., Koyejo, O., and Poldrack, R.A. (2016b). Temporal metastates are associated with differential patterns of time-resolved connectivity, network topology, and attention. Proc. Natl. Acad. Sci. USA 113, 9888–9891. 

Siebenhuhner,€ F., Weiss, S.A., Coppola, R., Weinberger, D.R., and Bassett, D.S. (2013). Intra- and inter-frequency brain network structure in health and schizophrenia. PLoS ONE 8, e72351. 

Siegel, J.S., Ramsey, L.E., Snyder, A.Z., Metcalf, N.V., Chacko, R.V., Weinberger, K., Baldassarre, A., Hacker, C.D., Shulman, G.L., and Corbetta, M. (2016). Disruptions of network connectivity predict impairment in multiple behavioral domains after stroke. Proc. Natl. Acad. Sci. USA 113, E4367–4376. 

Sizemore, A.E., and Bassett, D.S. (2017). Dynamic graph metrics: tutorial, toolbox, and tale. Neuroimage, S1053-8119(17)30564-5. 

Smucny, J., Wylie, K.P., and Tregellas, J.R. (2014). Functional magnetic resonance imaging of intrinsic brain networks for translational drug discovery. Trends Pharmacol. Sci. 35, 397–403. 

Song, H.F., Kennedy, H., and Wang, X.J. (2014). Spatial embedding of structural similarity in the cerebral cortex. Proc. Natl. Acad. Sci. USA 111, 16580–16585. 

Sporns, O. (2010). Networks of the Brain (MIT press). 

Sporns, O. (2014). Contributions and challenges for network models in cognitive neuroscience. Nat. Neurosci. 17, 652–660. 

Sporns, O. (2015). Cerebral cartography and connectomics. Philos. Trans. R. Soc. Lond. B Biol. Sci. 370, 20140173. 

Sporns, O., and Betzel, R.F. (2016). Modular brain networks. Annu. Rev. Psychol. 67, 613–640. 

Stam, C.J. (2014). Modern network science of neurological disorders. Nat. Rev. Neurosci. 15, 683–695. 

Stefansson, H., Meyer-Lindenberg, A., Steinberg, S., Magnusdottir, B., Morgen, K., Arnarsdottir, S., Bjornsdottir, G., Walters, G.B., Jonsdottir, G.A., Doyle, O.M., et al. (2014). CNVs conferring risk of autism or schizophrenia affect cognition in controls. Nature 505, 361–366. 

Stephan, K.E., Friston, K.J., and Frith, C.D. (2009). Dysconnection in schizophrenia: from abnormal synaptic plasticity to failures of self-monitoring. Schizophr. Bull. 35, 509–527. 

Supekar, K., Musen, M., and Menon, V. (2009). Development of large-scale functional brain networks in children. PLoS Biol. 7, e1000157. 

30 Neuron 97, January 3, 2018 

Neuron Review 

**==> picture [60 x 60] intentionally omitted <==**

Tang, E., Giusti, C., Baum, G.L., Gu, S., Pollock, E., Kahn, A.E., Roalf, D.R., Moore, T.M., Ruparel, K., Gur, R.C., et al. (2017). Developmental increases in white matter network controllability support a growing diversity of brain dynamics. Nat. Commun. 8, 1252. 

Taylor, P.N., Thomas, J., Sinha, N., Dauwels, J., Kaiser, M., Thesen, T., and Ruths, J. (2015). Optimal control based seizure abatement using patient derived connectivity. Front. Neurosci. 9, 202. 

Telesford, Q.K., Lynall, M.-E., Vettel, J., Miller, M.B., Grafton, S.T., and Bassett, D.S. (2016). Detection of functional brain network reconfiguration during task-driven cognitive states. Neuroimage 142, 198–210. 

Trull, T.J., and Ebner-Priemer, U. (2014). The role of ambulatory assessment in psychological science. Curr. Dir. Psychol. Sci. 23, 466–470. 

Trull, T.J., Lane, S.P., Koval, P., and Ebner-Priemer, U.W. (2015). Affective dynamics in psychopathology. Emot. Rev. 7, 355–361. 

Uddin, L.Q. (2015). Idiosyncratic connectivity in autism: developmental and anatomical considerations. Trends Neurosci. 38, 261–263. 

Uddin, L.Q., Supekar, K., and Menon, V. (2013). Reconceptualizing functional brain connectivity in autism from a developmental perspective. Front. Hum. Neurosci. 7, 458. 

Uhlhaas, P.J. (2013). Dysconnectivity, large-scale networks and neuronal dynamics in schizophrenia. Curr. Opin. Neurobiol. 23, 283–290. 

Uhlhaas, P.J., and Singer, W. (2010). Abnormal neural oscillations and synchrony in schizophrenia. Nat. Rev. Neurosci. 11, 100–113. 

Uhlhaas, P.J., and Singer, W. (2012). Neuronal dynamics and neuropsychiatric disorders: toward a translational paradigm for dysfunctional large-scale networks. Neuron 75, 963–980. 

Uhlhaas, P.J., Roux, F., Rodriguez, E., Rotarska-Jagiela, A., and Singer, W. (2010). Neural synchrony and the development of cortical networks. Trends Cogn. Sci. 14, 72–80. 

van den Heuvel, M.P., Bullmore, E.T., and Sporns, O. (2016). Comparative connectomics. Trends Cogn. Sci. 20, 345–361. 

van Os, J., Rutten, B.P., and Poulton, R. (2008). Gene-environment interactions in schizophrenia: review of epidemiological findings and future directions. Schizophr. Bull. 34, 1066–1082. 

Ve´ rtes, P.E., and Bullmore, E.T. (2015). Annual research review: growth connectomics–the organization and reorganization of brain networks during normal and abnormal development. J. Child Psychol. Psychiatry 56, 299–320. 

Ve´ rtes, P.E., Alexander-Bloch, A.F., Gogtay, N., Giedd, J.N., Rapoport, J.L., and Bullmore, E.T. (2012). Simple models of human brain functional networks. Proc. Natl. Acad. Sci. USA 109, 5868–5873. 

Ve´ rtes, P.E., Rittman, T., Whitaker, K.J., Romero-Garcia, R., Va´ �sa, F., Kitzbichler, M.G., Wagstyl, K., Fonagy, P., Dolan, R.J., Jones, P.B., et al.; NSPN Consortium (2016). Gene transcription profiles associated with inter-modular hubs and connection distance in human functional magnetic resonance imaging networks. Philos. Trans. R. Soc. Lond. B Biol. Sci. 371, 20150362. 

Watanabe, T., Hirose, S., Wada, H., Imai, Y., Machida, T., Shirouzu, I., Konishi, S., Miyashita, Y., and Masuda, N. (2013). A pairwise maximum entropy model accurately describes resting-state human brain networks. Nat. Commun. 4, 1370. 

Watanabe, T., Masuda, N., Megumi, F., Kanai, R., and Rees, G. (2014). Energy landscape and dynamics of brain activity during human bistable perception. Nat. Commun. 5, 4765. 

Watts, D.J., and Strogatz, S.H. (1998). Collective dynamics of ‘small-world’ networks. Nature 393, 440–442. 

Wenzel, M., Kubiak, T., and Ebner-Priemer, U.W. (2016). Ambulatory assessment as a means of longitudinal phenotypes characterization in psychiatric disorders. Neurosci. Res. 102, 13–21. 

Werner, P., Barthel, H., Drzezga, A., and Sabri, O. (2015). Current status and future role of brain PET/MRI in clinical and research settings. Eur. J. Nucl. Med. Mol. Imaging 42, 512–526. 

Whitaker, K.J., Ve´ rtes, P.E., Romero-Garcia, R., Va´ �sa, F., Moutoussis, M., Prabhu, G., Weiskopf, N., Callaghan, M.F., Wagstyl, K., Rittman, T., et al.; NSPN Consortium (2016). Adolescence is associated with genomically patterned consolidation of the hubs of the human brain connectome. Proc. Natl. Acad. Sci. USA 113, 9105–9110. 

Wilson, D., and Moehlis, J. (2014). Locally optimal extracellular stimulation for chaotic desynchronization of neural populations. J. Comput. Neurosci. 37, 243–257. 

Yang, G.J., Murray, J.D., Wang, X.J., Glahn, D.C., Pearlson, G.D., Repovs, G., Krystal, J.H., and Anticevic, A. (2016). Functional hierarchy underlies preferential connectivity disturbances in schizophrenia. Proc. Natl. Acad. Sci. USA 113, E219–E228. 

Yao, Y., Palaniyappan, L., Liddle, P., Zhang, J., Francis, S., and Feng, J. (2015). Variability of structurally constrained and unconstrained functional connectivity in schizophrenia. Hum. Brain Mapp. 36, 4529–4538. 

Yu, Q., Plis, S.M., Erhardt, E.B., Allen, E.A., Sui, J., Kiehl, K.A., Pearlson, G., and Calhoun, V.D. (2012). Modular organization of functional network connectivity in healthy controls and patients with schizophrenia during the resting state. Front. Syst. Neurosci. 5, 103. 

Yuan, Z., Zhao, C., Di, Z., Wang, W.X., and Lai, Y.C. (2013). Exact controllability of complex networks. Nat. Commun. 4, 2447. 

Zalesky, A., and Breakspear, M. (2015). Towards a statistical test for functional connectivity dynamics. Neuroimage 114, 466–470. 

Zalesky, A., Fornito, A., Cocchi, L., Gollo, L.L., and Breakspear, M. (2014). Time-resolved resting-state brain networks. Proc. Natl. Acad. Sci. USA 111, 10341–10346. 

Zalesky, A., Pantelis, C., Cropley, V., Fornito, A., Cocchi, L., McAdams, H., Clasen, L., Greenstein, D., Rapoport, J.L., and Gogtay, N. (2015). Delayed development of brain connectivity in adolescents with schizophrenia and their unaffected siblings. JAMA Psychiatry 72, 900–908. 

Neuron 97, January 3, 2018 31 

