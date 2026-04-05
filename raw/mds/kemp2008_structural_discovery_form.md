## **The discovery of structural form** 

## **Charles Kemp*[†] and Joshua B. Tenenbaum[‡]** 

*Department of Psychology, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, PA 15213; and[‡] Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, MA 02139 

Edited by Richard M. Shiffrin, Indiana University, Bloomington, IN, and approved May 30, 2008 (received for review March 17, 2008) 

**Algorithms for finding structure in data have become increasingly important both as tools for scientific data analysis and as models of human learning, yet they suffer from a critical limitation. Scientists discover qualitatively new forms of structure in observed data: For instance, Linnaeus recognized the hierarchical organization of biological species, and Mendeleev recognized the periodic structure of the chemical elements. Analogous insights play a pivotal role in cognitive development: Children discover that object category labels can be organized into hierarchies, friendship networks are organized into cliques, and comparative relations (e.g., ‘‘bigger than’’ or ‘‘better than’’) respect a transitive order. Standard algorithms, however, can only learn structures of a single form that must be specified in advance: For instance, algorithms for hierarchical clustering create tree structures, whereas algorithms for dimensionality-reduction create low-dimensional spaces. Here, we present a computational model that learns structures of many different forms and that discovers which form is best for a given dataset. The model makes probabilistic inferences over a space of graph grammars representing trees, linear orders, multidimensional spaces, rings, dominance hierarchies, cliques, and other forms and successfully discovers the underlying structure of a variety of physical, biological, and social domains. Our approach brings structure learning methods closer to human abilities and may lead to a deeper computational understanding of cognitive development.** 

## cognitive development � structure discovery � unsupervised learning 

**D** fundamentaliscovering the underlyingforstructurescientistsof aandset ofchildrenentitiesalikeis a 

challenge (1–7). Scientists may attempt to understand relationships between biological species or chemical elements, and children may attempt to understand relationships between category labels or the individuals in their social landscape, but both must solve problems at two distinct levels. The higher-level problem is to discover the form of the underlying structure. The entities may be organized into a tree, a ring, a dimensional order, a set of clusters, or some other kind of configuration, and a learner must infer which of these forms is best. Given a commitment to one of these structural forms, the lower-level problem is to identify the instance of this form that best explains the available data. 

The lower-level problem is routinely confronted in science and cognitive development. Biologists have long agreed that tree structures are useful for organizing living kinds but continue to debate which tree is best—for instance, are crocodiles better grouped with lizards and snakes or with birds (8)? Similar issues arise when children attempt to fit a new acquaintance into a set of social cliques or to place a novel word in an intuitive hierarchy of category labels. Inferences like these can be captured by standard structure-learning algorithms, which search for structures of a single form that is assumed to be known in advance (Fig. 1 _A_ ). Clustering or competitive-learning algorithms (9, 10) search for a partition of the data into disjoint groups, algorithms for hierarchical clustering (11) or phylogenetic reconstruction (12) search for a tree structure, and algorithms for dimensionality reduction (13, 14) or multidimensional scaling (15) search for a spatial representation of the data. 

Higher-level discoveries about structural form are rarer but more fundamental, and often occur at pivotal moments in the development of a scientific field or a child’s understanding (1, 2, 4). For centuries, the natural representation for biological species was held to be the ‘‘great chain of being,’’ a linear structure in which every living thing found a place according to its degree of perfection (16). In 1735, Linnaeus famously proposed that relationships between plant and animal species are best captured by a tree structure, setting the agenda for all biological classification since. Modern chemistry also began with a discovery about structural form, the discovery that the elements have a periodic structure. Analogous discoveries are made by children, who learn, for example, that social networks are often organized into cliques, that temporal categories such as the seasons and the days of the week can be arranged into cycles, that comparative relations such as ‘‘longer than’’ or ‘‘better than’’ are transitive (17, 18) and that category labels can be organized into hierarchies (19). Structural forms for some cognitive domains may be known innately, but many appear to be genuine discoveries. When learning the meanings of words, children initially seem to organize objects into nonoverlapping clusters, with one category label allowed per cluster (20); hierarchies of category labels are recognized only later (19). When reasoning about comparative relations, children’s inferences respect a transitive ordering by the age of 7 but not before (21). In both of these cases, structural forms appear to be learned, but children are not explicitly taught to organize these domains into hierarchies or dimensional orders. 

Here, we show that discoveries about structural form can be understood computationally as probabilistic inferences about the organizing principles of a dataset. Unlike most structurelearning algorithms (Fig. 1 _A_ ), the model we present can simultaneously discover the structural form and the instance of that form that best explain the data (Fig. 1 _B_ ). Our approach can handle many kinds of data, including attributes, relations, and measures of similarity, and we show that it successfully discovers the structural forms of a diverse set of real-world domains. 

Any model of form discovery must specify the space of structural forms it is able to discover. We represent structures using graphs and use graph grammars (22) as a unifying language for expressing a wide range of structural forms (Fig. 2). Of the many possible forms, we assume that the most natural are those that can be derived from simple generative processes (23). Each of the first six forms in Fig. 2 _A_ can be generated by using a single context-free production that replaces a parent node with two child nodes and specifies how to connect the children to each other and to the neighbors of 

Author contributions: C.K. and J.B.T. designed research; C.K. performed research; and C.K. and J.B.T. wrote the paper. 

This article is a PNAS Direct Submission. 

†To whom correspondence should be addressed. E-mail: ckemp@cmu.edu. 

Freely available online through the PNAS open access option. 

See Commentary on page 10637. 

This article contains supporting information online at www.pnas.org/cgi/content/full/ 0802631105/DCSupplemental. 

© 2008 by The National Academy of Sciences of the USA 

PNAS � **August 5, 2008** � vol. 105 � no. 31 � **10687–10692** 

www.pnas.org�cgi�doi�10.1073�pnas.0802631105 

**==> picture [427 x 232] intentionally omitted <==**

**----- Start of picture text -----**<br>
A ostrich bat gorilla robin crocodile gorilla B<br>robin crocodile ostrich snake turtle bat Form Tree<br>turtle snake<br>Circumplex Clustering gorilla<br>gorilla models gorilla bat<br>bat f  [ 1 ] f  [ 2 ] f  [ 3 ] f  [ 4 ] f  [ 5 ] . . . f  [100 ] bat turtle<br>turtle Hierarchical gorilla  . . . Unidimensional<br>clustering bat  scaling ostrich Structure snake<br>snake turtle<br>snake  robin crocodile<br>crocodilerobin crocodile ostrich robi n  . . . crocodileturtle ostrichrobin<br>ostrich<br>snake<br>PCA, Minimum<br>MDS spanning<br>tree<br>f  [ 1 ] f  [ 2 ] f  [ 3 ] f  [ 4 ] f  [ 5 ] . . . f  [100 ]<br>crocodile gorilla  . . .<br>snake snake gorilla Data turtle bat<br>gorilla snake<br>crocodile ostrich crocodile<br>bat turtle robi n<br>turtle bat ostric h  . . .<br>robin ostrich robin<br>**----- End of picture text -----**<br>


**Fig. 1.** Finding structure in data. ( _A_ ) Standard structure learning algorithms search for representations of a single form that is fixed in advance. Shown here are methods that discover six different kinds of structures given a matrix of binary features. ( _B_ ) A hierarchical model that discovers the form _F_ and the structure _S_ that best account for the data _D_ . The model searches for the form and structure that jointly maximize _P_ ( _S_ , _F_ � _D_ ) � _P_ ( _D_ � _S_ ) _P_ ( _S_ � _F_ ) _P_ ( _F_ ). 

the parent node. Fig. 2 _B_ – _D_ shows how three of these productions generate chains, orders, and trees. More complex forms, including multidimensional spaces and cylinders, can be generated by combining these basic forms or by using more complex productions. 

It is striking that the simple grammars in Fig. 2 _A_ generate many of the structural forms discussed by psychologists (24) and assumed by algorithms for unsupervised learning or exploratory data analysis. Partitions (9, 25), chains (26), orders (1, 25, 27), rings (28, 29), trees (1, 12, 30), hierarchies (31, 32) and grids (33) recur again and again in formal models across many different literatures. To highlight just one example, Inhelder and Piaget (1) suggest that the elementary logical operations in children’s thinking are founded on two forms: a classification structure that can be modeled as a tree and a seriation structure that can be modeled as an order. The popularity of the forms in Fig. 2 suggests that they are useful for describing the world, and that they spring to mind naturally when scientists seek formal descriptions of a domain. 

The problem of form discovery can now be posed. Given data _D_ about a finite set of entities, we want to find the form _F_ and the structure _S_ of that form that best capture the relationships between these entities. We take a probabilistic approach, and define a hierarchical generative model (34) that specifies how the data are generated from an underlying structure, and how this structure is generated from an underlying form (Fig. 1 _B_ ). We then search for the structure _S_ and form _F_ that maximize the posterior probability 

**==> picture [184 x 10] intentionally omitted <==**

_P_ ( _F_ ) is a uniform distribution over the forms under consideration (Fig. 2). Structure _S_ is a cluster graph, an instance of one of the forms in Fig. 2, where the nodes represent clusters of entities (Fig. 4 _A_ shows a cluster graph with the form of an order). The prior _P_ ( _S_ � _F_ ) favors graphs where _k_ , the number of clusters, is small: _P_ ( _S_ � _F_ ) � � _[k]_ if _S_ is compatible with _F_ , and _P_ ( _S_ � _F_ ) � 0 otherwise [see supporting information (SI) _Appendix_ for the definition of compatibility]. The parameter � determines the 

**==> picture [247 x 248] intentionally omitted <==**

**----- Start of picture text -----**<br>
A St ru ctur al Fo rm  Generativ e p  rocess  B<br>⇒<br>Pa rt itio n  ⇒<br>⇒<br>Chai n  ⇒ ⇒<br>Orde r  ⇒<br>C ⇒<br>Ring  ⇒ ⇒<br>Hierarch y  ⇒ ⇒<br>⇒<br>Tr ee  ⇒<br>D ⇒<br>Gr id  Chai n  ∏ Chai n<br>⇒<br>Cylinder  Chai n  ∏ Ring  ⇒<br>**----- End of picture text -----**<br>


**Fig. 2.** A hypothesis space of structural forms. ( _A_ ) Eight structural forms and the generative processes that produce them. Open nodes represent clusters of objects: A hierarchy has objects located internally, but a tree may only have objects at its leaves. The first six processes are node-replacement graph grammars. Each grammar uses a single production, and each production specifies how to replace a parent node with two child nodes. The seed for each grammar is a graph with a single node (in the case of the ring, this node has a self-link). ( _B_ – _D_ ) Growing chains, orders, and trees. At each step in each derivation, the parent and child nodes are shown in gray. The graph generated at each step is often rearranged before the next step. In _B_ , for instance, the right side of the first step and the left side of the second step are identical graphs. The red arrows in each production represent _all_ edges that enter or leave a parent node. When applying the order production, all nodes that previously sent a link to the parent node now send links to both children. 

**10688** � www.pnas.org�cgi�doi�10.1073�pnas.0802631105 

Kemp and Tenenbaum 

**==> picture [411 x 352] intentionally omitted <==**

**----- Start of picture text -----**<br>
D<br>A Salmon Trout Alligator<br>Eagle<br>Robin Penguin<br>Iguana<br>Finch Whale Ant<br>Chicken<br>Ostrich Dolphin Cockroach<br>Seal<br>Butterfly<br>Rhino Wolf Bee<br>Horse<br>Elephant Cow Dog<br>Deer Cat<br>GiraffeCamel Lion<br>Gorilla<br>Chimp Squirrel  [Tiger]<br>Mouse<br>B E Lima<br>Mexico City<br>MarshallBlackmun Stevens SouterBreyer WhiteO'ConnorRehnquistScalia Los Angeles Bogota Santiago<br>Brennan Ginsburg Thomas Honolulu Buenos Aires<br>Kennedy Chicago<br>Wellington VancouverToronto<br>C Anchorage New Sao Paulo<br>York<br>Sydney Dakar<br>Tokyo Madrid<br>Vladivostok London Kinshasa<br>Perth Berlin Cape Town<br>Irkutsk Moscow<br>Budapest<br>Jakarta Manila Nairobi<br>Cairo<br>Shanghai<br>Teheran<br>Bangkok<br>Bombay<br>**----- End of picture text -----**<br>


**Fig. 3.** Structures learned from biological features ( _A_ ), Supreme Court votes ( _B_ ), judgments of the similarity between pure color wavelengths ( _C_ ), Euclidean distances between faces represented as pixel vectors ( _D_ ), and distances between world cities ( _E_ ). For _A_ – _C_ , the edge lengths represent maximum _a posteriori_ edge lengths under our generative model. 

extent to which graphs with many clusters are penalized, and is fixed for all of our experiments. The normalizing constant for _P_ ( _S_ � _F_ ) depends on the number of structures compatible with a given form, and ensures that simpler forms are preferred when- 

ever possible. For example, any chain _S_ c is a special case of a grid, but _P_ ( _S_ c� _F_ � chain) � _P_ ( _S_ c� _F_ � grid) because there are more possible grids than chains given a fixed number of entities. It follows that _P_ ( _S_ c, _F_ � chain� _D_ ) � _P_ ( _S_ c, _F_ � grid� _D_ ) for any 

**==> picture [325 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B Rumsfeld Myers C D 1<br>1 Feith<br>Wolfowitz<br>2 Rice<br>3 Bush Powell Armitage<br>Ashcroft<br>4 5 Cheney Libby<br>6 Card<br>Whitman<br>1 123 B R M FWR P A A C L C W 1<br>2 B 1<br>3 RM<br>F<br>W<br>R<br>P<br>A<br>A<br>C<br>L<br>C<br>W<br>**----- End of picture text -----**<br>


**Fig. 4.** Structureslearnedfromrelationaldata( _Upper_ )andtherawdataorganizedaccordingtothesestructures( _Lower_ ).( _A_ )Dominancerelationshipsamongatroop of sooty mangabeys. The sorted data matrix has most of its entries above the diagonal, indicating that animals tend to dominate only the animals below them in the order. ( _B_ ) A hierarchy representing interactions between members of the Bush administration. ( _C_ ) Social cliques representing friendship relations between prisoners. The sorted matrix has most of its entries along the diagonal, indicating that prisoners tend only to be friends with prisoners in the same cluster. ( _D_ ) The Kula ring representing armshell trade between New Guinea communities. The relative positions of the communities correspond approximately to their geographic locations. 

PNAS � **August 5, 2008** � vol. 105 � no. 31 � **10689** 

Kemp and Tenenbaum 

dataset _D_ , and that the grid form will only be chosen if the best grid is substantially better than the best chain. 

The remaining term in Eq. **1** , _P_ ( _D_ � _S_ ), measures how well the structure _S_ accounts for the data _D_ . Suppose that _D_ is a feature matrix like the matrix in Fig. 1. _P_ ( _D_ � _S_ ) will be high if the features in _D_ vary smoothly over the graph _S_ , that is, if entities nearby in _S_ tend to have similar feature values. For instance, feature **f**[1] is smooth over the tree in Fig. 1 _B_ , but **f**[100] is not. Even though Fig. 1 shows binary features, we treat all features as continuous features and capture the expectation of smoothness by assuming that these features are independently generated from a multivariate Gaussian distribution with a dimension for each node in graph _S_ . As described in _SI Appendix_ , the covariance of this distribution is defined in a way that encourages nearby nodes in graph _S_ to have similar feature values, and the term _P_ ( _D_ � _S_ ) favors graphs that meet this condition. 

In principle, our approach can be used to identify the form _F_ that maximizes _P_ ( _F_ � _D_ ), but we are also interested in discovering the structure _S_ that best accounts for the data. We therefore search for the structure _S_ and form _F_ that jointly maximize the scoring function _P_ ( _S_ , _F_ � _D_ ) (Eq. **1** ). To identify these elements, we run a separate greedy search for each candidate form. Each search begins with all entities assigned to a single cluster, and the algorithm splits a cluster at each iteration, using the production for the current form (Fig. 2). After each split, the algorithm attempts to improve the score, using several proposals, including proposals that move an entity from one cluster to another and proposals that swap two clusters. The search concludes once the score can no longer be improved. A more detailed description of the search algorithm is provided in _SI Appendix_ . 

We generated synthetic data to test this algorithm on cases where the true structure was known. The _SI Appendix_ shows graphs used to generate five datasets, and the structures found by fitting five different forms to the data. In each case, the model recovers the true underlying form of the data. 

Next, we applied the model to several real-world datasets, in each case considering all forms in Fig. 2. The first dataset is a matrix of animal species and their biological and ecological properties. It consists of human judgments about 33 species and 106 features and amounts to a larger and noisier version of the dataset shown schematically in Fig. 1. The best scoring form for this dataset is the tree, and the best tree (Fig. 3 _A_ ) includes subtrees that correspond to categories at several levels of resolution (e.g., mammals, primates, rodents, birds, insects, and flying insects). The second dataset is a matrix of votes from the United States Supreme Court, including 13 judges and their votes on 1,596 cases. Some political scientists (35) have argued that a unidimensional structure best accounts for variation in Supreme Court data and in political beliefs more generally, although other structural forms [including higher-dimensional spaces (36) and sets of clusters (37)] have also been proposed. Consistent with the unidimensional hypothesis, our model identifies the chain as the best-scoring form for the Supreme Court data. The best chain (Fig. 3 _B_ ) organizes the 13 judges from liberal (Marshall and Brennan) to conservative (Thomas and Scalia). 

If similarity is assumed to be a measure of covariance, our model can also discover structure in similarity data. Under our generative model for features, the expression for _P_ ( _D_ � _S_ ) includes only two components that depend on _D_ : the number of features observed and the covariance of the data. As long as both components are provided, Eq. **1** can be used even if none of the features is directly observed. We applied the model to a matrix containing human judgments of the similarity between all pairs of 14 pure-wavelength hues (38). The ring in Fig. 3 _C_ is the best structure for these data and corresponds to the color circle described by Newton. Next, we analyzed a similarity dataset where the entities are faces that vary along two dimensions: 

**==> picture [217 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
Eagle Finch Bee Ant Wolf Dog Cat<br>Ostrich<br>Chicken Robin Cockroach Lion Tiger<br>Butterfly<br>5 features Alligator Elephant Giraffe Gorilla<br>SalmonDolphin Iguana Cow Camel<br>Whale Deer HorseSquirrel<br>Trout Chimp Rhino<br>Penguin Seal Mouse<br>Chicken Eagle<br>Ostrich Robin Bee<br>Finch Butterfly<br>Ant<br>20 features Tiger Lion DogCat Cockroach<br>Wolf Iguana<br>Gorilla<br>Chimp<br>Horse Alligator<br>Cow Trout<br>Elephant Mouse Salmon<br>CamelRhino GiraffeDeerSquirrel DolphinSeal Whale<br>Penguin<br>Salmon Trout Alligator<br>Eagle<br>Robin Penguin<br>Iguana<br>Finch Whale Ant<br>Chicken<br>110 features Ostrich Dolphin Cockroach<br>Seal<br>Butterfly<br>Rhino Wolf Bee<br>Elephant HorseCow Dog<br>Deer Cat<br>GiraffeCamel Lion<br>Gorilla Tiger<br>Chimp Squirrel<br>Mouse<br>**----- End of picture text -----**<br>


**Fig. 5.** Developmental changes as more data are observed for a fixed set of objects. After observing only five features of each animal species, the model chooses a partition, or a set of clusters. As the number of observed features grows from 5 to 20, the model makes a qualitative shift between a partition and a tree. As the number of features grows even further, the tree becomes increasingly complex, with subtrees that correspond more closely to adult taxonomic intuitions: For instance, the canines (dog, wolf) split off from the other carnivorous land mammals; the songbirds (robin, finch), flying birds (robin, finch, eagle), and walking birds (chicken, ostrich) form distinct subcategories; and the flying insects (butterfly, bee) and walking insects (ant, cockroach) form distinct subcategories. More information about these simulations can be found in _SI Appendix_ . 

masculinity and race. The model chooses a grid structure that recovers these dimensions (Fig. 3 _D_ ). Finally, we applied the model to a dataset of distances between 35 world cities. Our model chooses a cylinder where the chain component corresponds approximately to latitude, and the ring component corresponds approximately to longitude. 

The same algorithm can be used to discover structure in relational data, but we must modify the distribution _P_ ( _D_ � _S_ ). Suppose that _D_ is a square frequency matrix, where _D_ ( _i_ , _j_ ) indicates the number of times a certain relation has been observed between entities _i_ and _j_ (Fig. 4). We define a model where _P_ ( _D_ � _S_ ) is high if the large entries in _D_ correspond to edges in the graph _S_ . A similar model can be defined if _D_ is a binary relation rather than a frequency matrix. Given a relation _D_ , it is important to discover whether the relation tends to hold between elements in the same cluster or only between different clusters, and whether the relation is directed or not. The forms in Fig. 2 _A_ all have directed edges and nodes without self-links, and we 

**10690** � www.pnas.org�cgi�doi�10.1073�pnas.0802631105 

Kemp and Tenenbaum 

expanded this collection to include forms with self-links, forms with undirected edges, and forms with both of these properties. 

First, we applied the model to a matrix of interactions among a troop of sooty mangabeys. The model discovers that the order is the most appropriate form, and the best order found (Fig. 4 _A_ ) is consistent with the dominance hierarchy inferred by primatologists studying this troop (39). Hierarchical structure is also characteristic of human organizations, although tree-structured hierarchies are perhaps more common than full linear orders. We applied the model to a matrix of interactions between 13 members of George W. Bush’s first-term administration (40). The best form is an undirected hierarchy, and the best hierarchy found (Fig. 4 _B_ ) closely matches an organizational chart built by connecting individuals to their immediate superiors. Next, we analyzed social preference data (41) that represent friendships between prison inmates. Clique structures are often claimed to be characteristic of social networks (42), and the model discovers that a partition (a set of cliques) gives the best account of the data. Finally, we analyzed trade relations between 20 communities in New Guinea (43). The model discovers the Kula ring, an exchange structure first described by Malinowski (44). 

We have presented an approach to structure discovery that provides a unifying description of many structural forms, discovers qualitatively different representations for a diverse range of datasets, and can handle multiple kinds of data, including feature data, relational data, and measures of similarity. Our hypothesis space of forms (Fig. 2) includes some of the most common forms, but does not exhaust the set of cognitively natural or scientifically important forms. Ultimately, psychologists should aim to develop a ‘‘Universal Structure Grammar’’ (compare with ref. 45) that characterizes more fully the representational resources available to human learners. This universal grammar might consist of a set of simple principles that generate all and only the cognitively natural forms. We can only speculate about how these principles might look, but one starting place is a metagrammar (46) for generating graph grammars. For instance, all of the forms shown in Fig. 2 _A_ can be generated by a metagrammar shown in _SI Appendix_ . 

Our framework may be most readily useful as a tool for data analysis and scientific discovery, but should also be explored as a model of human learning. Our model helps to explain how adults discover structural forms in controlled behavioral experiments (40), and is consistent with previous demonstrations that adults can choose the most appropriate representation for a given problem (47). Our model may also help to explain how children learn about the structure of their world. The model shows developmental shifts as more data are encountered, and 

1. Inhelder B, Piaget J (1964) _The Early Growth of Logic in the Child_ (Routledge & Kegan Paul, London). 

2. Carey, S (1985) _Conceptual Change in Childhood_ (MIT Press, Cambridge, MA). 

3. Gopnik, A, Meltzoff, AN (1997) _Words, Thoughts, and Theories_ (MIT Press, Cambridge, MA). 

4. Kuhn, TS (1970) _The Structure of Scientific Revolutions_ (Univ of Chicago Press, Chicago), 2nd Ed. 

5. Whewell W (1840) _The Philosophy of the Inductive Sciences: Founded Upon Their History_ (J. W. Parker, London). 

6. Jaynes ET (2003) _Probability Theory: The Logic of Science_ (Cambridge Univ Press, Cambridge, UK). 

7. Spirtes P, Glymour C, Scheines R (1993) _Causation, Prediction and Search_ (Springer, New York). 

8. Purves WK, Sadava D, Orians GH, Heller HC (2001) _Life: The Science of Biology_ (Sinauer, Sunderland, MA), 6th Ed. 

9. Anderson JR (1991) The adaptive nature of human categorization. _Psychol Rev_ 98:409– 429. 

10. Rumelhart D, Zipser D (1986) Feature discovery by competitive learning. _Parallel Distributed Processing: Explorations in the Microstructure of Cognition_ , eds Rumelhart D, McClelland J, and the PDP research group (MIT Press, Cambridge, MA), Vol 1. 

11. Duda RO, Hart PE, Stork DG (2000) _Pattern Classification_ (Wiley, New York), 2nd Ed. 

12. Huelsenbeck JP, Ronquist F (2001) MRBAYES: Bayesian inference of phylogenetic trees. _Bioinformatics_ 17:754–755. 

often moves from a simple form to a more complex form that more faithfully represents the structure of the domain (Fig. 5 and _SI Appendix_ ). Identifying the best form for a domain provides powerful constraints on inductive inference, constraints that may help to explain how children learn new word meanings, concepts, and relations so quickly and from such sparse data (48–51). Discovering the clique structure of social networks can allow a child to predict the outcome of interactions between individuals who may never have interacted previously. Discovering the hierarchical structure of category labels allows a child to predict that a creature called a ‘‘chihuahua’’ might also be a dog and an animal, but cannot be both a dog and a cat. 

As examples like these suggest, form discovery provides a way of acquiring domain-specific constraints on the structure of mental representations, a possibility that departs from two prominent views of cognition. A typical nativist view recognizes that inductive inference relies on domain-specific constraints but assumes that these constraints are innately provided (52–54). Chomsky (52), for instance, has suggested that ‘‘the belief that various systems of mind are organized along quite different principles leads to the natural conclusion that these systems are intrinsically determined, not simply the result of common mechanisms of learning or growth.’’ A typical empiricist view emphasizes learning but assumes no domain-specific representational structure. Standard methods for learning associative networks (55) and neural networks (56) use the same generic class of representations for every task, instead of attempting to identify the distinctive kinds of structures that characterize individual domains. Without these constraints, empiricist methods can require unrealistically large quantities of training data to learn even very simple concepts (57). Our framework offers a third view that combines insights from both these approaches and shows how domain-specific structural constraints can be acquired by using domain-general probabilistic inference. As children learn about the structure of different domains, they make discoveries as impressive as those of Linnaeus and Mendeleev, and approaches like ours may help to explain how these discoveries are possible. 

**ACKNOWLEDGMENTS.** We thank P. Gunkel, E. Newport, A. Perfors, and W. Richards for valuable discussions and D. Casasanto, M. Frank, N. Goodman, V. Mansinghka, R. Saxe, J. M. Tenenbaum, D. Tymoczko, the editor, and two anonymous reviewers for helpful suggestions. This work was supported in part by the William Asbjornsen Albert memorial fellowship (to C.K.), the Paul E. Newton career development chair (J.B.T.), the James S. McDonnell Foundation Causal Learning Research Collaborative, Air Force Office of Scientific Research Grant FA9550-07-1-0075, and the NTT Communication Sciences Laboratory. 

13. Pearson K (1901) On lines and planes of closest fit to systems of points in space. _Philos Mag_ 2:559–572. 

14. Spearman CE (1904) ‘‘General intelligence’’ objectively determined and measured. _Am J Psychol_ 5:201–293. 

15. Torgeson WS (1965) Multidimensional scaling of similarity. _Psychometrika_ 30:379–393. 

16. Lovejoy AO (1970) _The Great Chain of Being_ (Harvard Univ Press, Cambridge, MA). 

17. Piaget J (1965) _The Child’s Conception of Number_ (Norton, New York). 

18. Shultz TR (2003) _Computational Developmental Psychology_ (MIT Press, Cambridge, MA). 

19. Rosch E (1978) Principles of categorization. _Cognition and Categorization_ , eds Rosch E, Lloyd BB (Lawrence Erlbaum, New York), pp 27–48. 

20. Markman, E (1989) _Naming and Categorization in Children_ (MIT Press, Cambridge, MA). 

21. Shultz, TR, Vogel, A (2004) A connectionist model of the development of transitivity. _Proceedings of the 26th Annual Conference of the Cognitive Science Society_ , eds Forbus K, Gentner D, Regier T (Lawrence Erlbaum, Cambridge, MA) pp 1243–1248. 

22. Engelfriet J, Rozenberg G (1997) Node replacement graph grammars. _Handbook of Graph Grammars and Computing by Graph Transformation_ , ed Rozenberg G (World Scientific, Singapore), Vol 1. 

23. Leyton M (1992) _Symmetry, Causality, Mind_ (MIT Press, Cambridge, MA). 

24. Shepard RN (1980) Multidimensional scaling, tree-fitting, and clustering. _Science_ 210:390–398. 

25. Fiske AP (1992) The four elementary forms of sociality: Framework for a unified theory of social relations. _Psychol Rev_ 99:689–723. 

26. Guttman L (1944) A basis for scaling qualitative data. _Am Soc Rev_ 9:139–150. 

PNAS � **August 5, 2008** � vol. 105 � no. 31 � **10691** 

Kemp and Tenenbaum 

27. Bradley RA, Terry ME (1952) Rank analysis of incomplete block designs. 1. The method of paired comparisons. _Biometrika_ 39:324–345. 

28. Guttman L (1954) A new approach to factor analysis: The radex. _Mathematical Thinking in the Social Sciences_ , ed Lazarsfeld PF (Free Press, Glencoe, IL), pp 258–348. 

29. Wiggins JS (1996) An informal history of the interpersonal circumplex tradition. _J Personality Assessment_ 66:217–233. 

30. Sneath PH, Sokal RR (1973) _Numerical Taxonomy: The Principles and Practice of Numerical Classification_ (Freeman, San Francisco). 

31. Collins AM, Quillian MR (1969) Retrieval time from semantic memory. _J Verbal Learn Verbal Behav_ 8:240–247. 

32. Carroll JD (1976) Spatial, nonspatial and hybrid models for scaling. _Psychometrika_ 41:439–463. 

33. Kohonen T (1997) _Self_ - _Organizing Maps_ (Springer, New York). 

34. Gelman, A, Carlin JB, Stern HS, Rubin DB (2003) _Bayesian Data Analysis_ (Chapman & Hall, New York), 2nd Ed. 

35. Grofman B, Brazill T (2002) Identifying the median justice on the Supreme Court through multidimensional scaling: Analysis of ‘‘natural courts’’ 1953–1991. _Public Choice_ 112:55–79. 

36. Wilcox C, Clausen A (1991) The dimensionality of roll-call voting reconsidered. _Legislative Stud Q_ 16:393–406. 

37. Fleishman JA (1986) Types of political attitude structure: Results of a cluster analysis. _Public Opin Q_ 50:371–386. 

38. Ekman G (1954) Dimensions of color vision. _J Psychol_ 38:467–474. 

39. Range F, Noe¨ R (2002) Familiarity and dominance relations among female sooty mangabeys in the Tai national park. _Am J Primatol_ 56:137–153. 

40. Kemp C (2008) PhD Thesis (Massachusetts Institute of Technology, Cambridge, MA). 

41. MacRae J (1960) Direct factor analysis of sociometric data. _Sociometry_ 22:360–371. 

42. Girvan M, Newman MEJ (2002) Community structure in social and biological networks. _Proc Natl Acad Sci USA_ 99:7821–7826. 

43. Hage, P, Harary, F (1991) _Exchange in Oceania: A Graph Theoretic Analysis_ (Oxford Univ Press, Oxford). 

44. Malinowski, B (1922) _Argonauts of the Western Pacific: An Account of Native Enterprise and Adventure in the Archipelagoes of Melanesian New Guinea_ (G. Routledge & Sons, London). 

45. Chomsky, N (1965) _Aspects of the Theory of Syntax_ (MIT Press, Cambridge, MA). 

46. Nagl M (1986) Set theoretic approaches to graph grammars. _Proceedings of the 3rd International Workshop on Graph_ - _Grammars and their Application to Computer Science_ (Springer, London, UK), pp 41–54. 

47. Novick LR, Hurley SM (2001) To matrix, network or hierarchy: That is the question. _Cognit Psych_ 42:158–216. 

48. Carey S, Bartlett E (1978) Acquiring a single new word. _Pap Rep Child Lang Dev_ 15:17–29. 

49. Keil FC (1979) _Semantic and Conceptual Development_ (Harvard Univ Press, Cambridge, MA). 

50. Keil FC (1981) Constraints on knowledge and cognitive development. _Psychol Rev_ 88:197–227. 

51. Tenenbaum JB, Griffiths TL, Kemp C (2006) Theory-based Bayesian models of inductive learning and reasoning. _Trends Cognit Sci_ 10:309–318. 

52. Chomsky N (1980) _Rules and Representations_ (Basil Blackwell, Oxford). 

53. Atran S (1998) Folk biology and the anthropology of science: Cognitive universals and cultural particulars. _Behavioral and Brain Sciences_ 21:547–609. 

54. Kant I, trans Smith NK (2003) _Critique of Pure Reason_ (Palgrave Macmillan, New York). 

55. Rescorla, RA, Wagner, AR (1972) A theory of pavlovian conditioning: Variations on the effectiveness of reinforcement and non-reinforcement. _Classical Conditioning II: Current Research and Theory_ , eds Black, AH, Prokasy, WF (Appleton-Century-Crofts, New York), pp 64–99. 

56. Rogers, TT, McClelland, JL (2004) _Semantic Cognition: A Parallel Distributed Processing Approach_ (MIT Press, Cambridge, MA). 

57. Geman S, Bienenstock E, Doursat R (1992) Neural networks and the bias-variance dilemma. _Neural Computation_ 4:1–58. 

**10692** � www.pnas.org�cgi�doi�10.1073�pnas.0802631105 

Kemp and Tenenbaum 

