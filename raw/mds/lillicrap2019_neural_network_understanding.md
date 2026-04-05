# What does it mean to understand a neural network? 

# Timothy P. Lillicrap & Konrad P. Kording 

July 2019 

## **Abstract** 

We can define a neural network that can learn to recognize objects in less than 100 lines of code. However, after training, it is characterized by millions of weights that contain the knowledge about many object types across visual scenes. Such networks are thus dramatically easier to understand in terms of the code that makes them than the resulting properties, such as tuning or connections. In analogy, we conjecture that rules for development and learning in brains may be far easier to understand than their resulting properties. The analogy suggests that neuroscience would benefit from a focus on learning and development. 

## **Introduction** 

When we build networks that solve image recognition at human-like performance [18] or are strong at playing the game of Go [30] we ended up using a few computer screens worth of high-level computer code. We undeniably understand these lines of code, and we teach how these systems works to students in our deep learning courses who also obtain a meaningful understanding. After training we have the full set of weights and elementary operations. We can also compute and inspect any aspect of the representations formed by the trained network. In this sense we can have a complete description of the network and its computations. And yet, neither we, nor anyone we know feels that they grasp how processing in these networks truly works. Said another way, besides gesturing to a network’s weights and elementary operations, we cannot say how it classifies an image as a cat or a dog, or how it chooses one Go move over another. For neural networks there is no doubt that the understanding that we can currently have about their properties after learning is massively more shallow than the understanding that we have about the code used to train it: the rules for its development and learning. 

One day, we may develop ways of compactly describing how neural networks work after training. There may be an intermediate language in which we could meaningfully describe how these systems work. A useful intermediate language would allow us to write high-level computer code to directly construct powerful neural networks for image recognition or playing Go without resorting to iterative construction of the network via a learning procedure. However, we can not currently offer such an intermediate description for our artificial networks, which we have arbitrarily better access to than 

1 

**==> picture [386 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Unbeatable Tic-Tac-Toe B Unbeatable Go (Hypothesized) C<br>?<br>Number of Rules Needed<br>2) If you can, stoptheir win<br>1) If you can, win 3) Take a corner 1) If you can win, win2) If you can stop theirwin, stop it 100) Some obscure rule 1000,000) Seriously rare rule<br>Variance Explained Variance Explained<br>**----- End of picture text -----**<br>


Figure 1: **The notion of compressability.** (A) Unbeatable performance at tic-tac-toe can be obtained with just three rules. These rules can be ordered by their importance (B) Unbeatable performance at the game of Go needs many rules. So many, in fact, that we can not know that number. Importantly, the rules are heavy tailed. If we have any small number of rules, the remaining rules will generally still carry a lot information about how to further improve on the task. Humans have long tried to distill the game of Go into instructional books and have, to a large extent, been unsuccessfully at doing so. (C) The question is where on this axis the brain is situated. The brain might be easier than Go to compactly describe. Or the brain may be much harder than Go, affording no compact description under any realistic assumption. 

brains. As such, even if meaningful descriptions exist, for the moment we best understand neural networks in terms of their mechanisms for development and learning. 

In this paper, we will discuss issues of complexity as applied to neural networks and other artificial systems. These systems are fully observed, we have a total description of all the involved functions, and nonetheless we have trouble producing a meaningful “understanding”. We will use this consideration as a backdrop to ask what we mean when we talk about understanding neural computation. We will argue that the brain’s generative process is not that unlike that of neural networks, since it obtains information from a world which it stores as a distributed pattern of weight changes, a pattern that is remarkably hard to wrap one’s head around. We will conclude by suggesting that, at least for the moment, neuroscience should focus on understanding development and learning. 

## **Can an artificial system that is as good as humans at a broad range of tasks be compactly expressed?** 

The learning rules in artificial systems are compactly expressed, in the sense that they can be written in a few pages of high-level (e.g. Pytorch) code. And at least to us practitioners of machine learning it feels like having such a compact description is necessary for meaningful understanding. Having such a compact description offers us leverage: we can produce variants of the same kind of ideas and use them to solve a broad range of useful and interesting machine learning problems. 

2 

Maybe humans or other intelligent beings can figure out ways of meaningfully arguing about noncompact systems, but, at least so far, compactness is necessary for what we would call a meaningful understanding. 

Central to our arguments is the idea of compressibility. We will introduce it with with a simple scenario: the game of tic-tac-toe. While there are 255,168 potential games, we can have a policy of just three rules (see Figure 1), that allows unbeatable tic-tac-toe performance. In the game of Go, in which computers have recently started beating world champions [29, 30], there is no known compact way of expressing the instantaneous valuation of a position. This is at least in part due to the fact that there can be exponentially many games of Go ( _>_ 10[10][48] games) although the set of reasonably probable games is probably much lower, say 800 moves, 100 possibilities each (10[1600] games). In such a domain, knowledge that lowers the number of allowable games by a factor of two (hypothesis testing) will be essentially useless (we will still have 10[10][48] _[−]_[log10(2)] games left). Neural networks that capture effective policies and value functions for Go reflect the complexity of the game. Systems that solve a broad range of interesting problems at human levels should be less compressible than specialized systems that play Go [29, 30] or neural networks that recognize visual categories [18]. After all, humans can do both. In complex domains, approximate systems that are more compressed tend to have poor performance and so do not truly represent a way of avoiding the problem. We may thus expect broadly applicable intelligent systems to be hard (or impossible) to compress into a small size. 

Computer scientists have worked extensively on the problem of compressing large neural networks into simpler and more describable systems. With the rise in popularity of distillation techniques [12, 13, 14, 15, 28, 35] and renewed interest in the field of computational complexity we are starting to understand more about compressability. From distillation techniques we know that networks trained on ImageNet, a popular 2012 machine learning benchmark that requires the classification of natural images, cannot readily be compressed to fewer than about 100k free parameters [13, 20, 32] (though see [35]). We want to emphasize that these compressions, even of the ImageNet case, are not in any meaningful sense human understandable. Even the famous and somewhat trivial networks that solve the MNIST character recognition problem can not readily be compressed into a format that humans find readable [8]. Moreover, human performance includes knowledge of roughly 30,000 categories of objects [3] - and arguably they, on average, know a lot of information about each of them, possibly megabytes thereof, and certainly more than a few bytes. Humans also appear to know more than a megabyte worth of information about their own language [21]. Human-like performance seems exceptionally hard to compress into a compact representation. 

How are neural network scientists trying to understand their networks? They primarily look for phenomena relevant for optimization, such as vanishing and exploding gradients, or exploding global dynamics during the process of generating a system. Perhaps most common in practice is looking at histograms of the unit activations and derivatives [2, 10, 23] to see whether learning is halting or being slowed for a trivial reason – offering clues as to how to adjust learning rates or other hyperparameters. However, such analyses are used almost exclusively to diagnose problems in the engineering process that arise during the construction of the system. They do not provide a path to a meaningful understanding of the computations done by the systems they build. 

Ongoing work in the deep learning field aims at more intuitive understanding of the computations in neural networks. Scientists study the sensitivity of outputs to changes in the system to ask what 

3 

matters [9, 31, 33]. They ask which stimuli can fool a system [1, 11, 31]. They visualize elements of a network [33, 34]. They analyze what happens if a system is perturbed, e.g. by removing units [12, 19, 22]. However, no one who is familiar with these approaches would say that they offer a good understanding of models like AlexNet, AlphaGo, or GPT2 [18, 24, 30]. These approaches remain far from offering practitioners enough understanding to be useful to improve networks for task performance. 

Returning to the question of compressibility, we may ask why we should expect neural networks that exhibit human-like performance to be hard to compress? The world in which humans live is undeniably complicated; much of our world is built of peculiarities which are obviously incompressible. Let us choose balloons as an example. Adult humans know a lot about balloons. For example, they are made of rubber or aluminum foil, often held by kids or clowns, are red in a famous song, etc. And yet, it seems unlikely that we are born with knowledge of balloons. We have similar incompressible knowledge about any of the many categories of objects people know about. Estimates of how much humans know vary widely but suggest that compressibility is limited. The important result is that _the bulk_ of the information we need to specify a working model comes from the world, which is complicated and (arguably) not compressible. There are domains where the world is simple and then we should be good at building models (e.g. for the vestibuloocular reflex [26]) and there are domains where the world is truly complicated (e.g. image recognition) and it is presumably hopeless to communicate a working model of such behaviors. 

Given just the architecture and weights of an already functioning system is not very useful except with respect on the exact task that it already solves. (Imagine giving an ImageNet trained network to someone who had no idea how the learning process worked!). Knowing the learning rules, architectures, and loss functions used to train such a system are far more useful for future alterations and interventions one might want to make. 

## **Analogy to neuroscience** 

Humans are not neural networks. And yet, the brain has ubiquitous plasticity [17]. Specifically, we know that plasticity allows changes in the brain to enable good performance across new tasks [7]. As such, it is hard to see how the arguments we made above about artificial neural networks would not carry over to the human brain. To the level that this insight holds, this may suggest that understanding representations, which may be viewed like an artificial neural network after training, may be outstandingly hard. We concluded above that for artificial neural networks a focus on objectives, learning rules, and architectures is most promising. We do not see why the same argument does not carry over to neuroscience: itt may currently be prohibitively hard to understand connection strengths and representations, even if architectures, learning, and development can be meaningfully characterized and communicated. 

4 

## **Where to now?** 

However, while we may not be very hopeful about communicating a working model of the dynamics, we can still hope to communicate how biology, nature, sets up the brain (including its anatomy and learning rules, see Figure 2). After all, the complexity from our DNA is upper limited by 6 _·_ 10[9] bits of DNA. And that information is hugely redundant, largely non-coding, and only effects change through some 20k genes, most of which undoubtedly do not code information for brains. That being said, we can not know the amount of information effectively communicated by non-coding parts of the DNA. With the increased availability of genetic tools we might be able to get closer to such principles. The basic biochemistry of cells, is somewhat bounded in complexity – there are only so many types of neurotransmitters or channels that appear relevant. The developmental processes setting up our anatomy as well as cell types (or computational primitives) promise to produce the backbone for our learning. We may hope that we can understand them. While learned information is unlikely to be compressible, we may at least hope that biological information is, e.g. learning rules and anatomy. 

The breakdown into parameters (nurture) and principles (nature) is precisely the breakdown that the AlphaGo and AlexNet papers use in practice: they offer pointers to tasks and related data sources (from which the vast majority of the incompressible & non-communicable parameters will be extracted), and then document the architectures (Convnets / ResNets), loss functions (L2 / cross entropy), learning rule (SGD / Adam), and optimization (MCTS) approaches used. These last four pieces are all easily expressed in small human understandable equations, and formal recipes. We can not communicate the data sources in any straightforward sense - while we could read the contents of the images and their labels to another person, they would not meaningfully understand their totality. And yet, we do understand the generation of the neural networks. Not only do these recipes offer replicable means of producing working systems, they also offer the kind of understanding that affords ways of pursuing useful and interesting interventions and predictions. 

There is a widespread belief in neuroscience that there can be a meaningful mid-level model of the dynamics of the brain that both can be communicated and work for complex tasks. The idea is in analogy to physics: In quantum mechanics, the state of e.g. a gas can not be meaningfully communicated since every gas atom may exist in a high dimensional space and there are many atoms. But in statistical physics, the state of the gas may be compactly described in terms of a few variables like temperature, pressure, etc. And these mid-level descriptions can afford high accuracy predictions and control. From this analogy it is sometimes argued that a compact midlevel description should exist for neuroscience. And, indeed, a lossy model of how e.g. eye movement is computed in humans might enable us to better predict movements for some practical purpose. Such mid-level lossy descriptions of the computations carried out by brains may thus be interesting. However, for the more complicated problems we discuss in this paper, the analogy quickly breaks down: in the gas case, all atoms are the same, are exchangeable, and have short memory while in brains each cell may be unique and have a memory that effectively goes back to the birth of the animal. Moreover, the argument we made here suggests that such a compact mid-level model of computation can not have the property of actually working in the domains of brain performance where the environment can not be compactly communicated. Thus the analogy to physics may be misleading in the context of neuroscience. 

5 

## **Outlook** 

**==> picture [388 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Data: Brain:<br>B Potential Principles:<br>Systems Neuroscience Machine Learning<br>Anatomy: Architecture:<br>Plasticity Rules: Learning Rules:<br>pre post<br>**----- End of picture text -----**<br>


Figure 2: **Dividing theories of brain functions into principles and data.** (A) If the brain is not compressable, we can at best divide our description of it into a set of compact principles and a set of non compressable data. We may then hope that the way the brain converts the data into computation may be understandable. (B) A very natural division is to ask for an understanding of anatomy and plasticity rules, which jointly may allow understanding how (uncompressable) stimuli convert into computation. This could be in analogy to machine learning where architectures along with learning rules and loss functions give rise to the relevant computation. 

History is full of seemingly impossible things that ended up being possible [4]. It may thus eventually be possible to meaningfully understand a network trained on ImageNet. Importantly, there can be no doubt that doing so is arbitrarily easier than understanding a human brain - after all, for a network trained on ImageNet we have all the information and can run any experiment we might possibly want to run. We thus may want to try and start trying to understand such networks, in tight analogy with microprocessors [16]. Despite a thriving community aiming at understanding trained neural networks [e.g. 6, 12] there are worries about general feasibility [25]. It is possible that real brains have aspects, e.g. strong modularity, approximate linearity, or high noise that make them easier to understand than artificial neural networks, in which case we should be precise about which factors make the task doable. Alternatively, it may be impossible to meaningfully understand 

6 

a network after training on a complex tasks and we may want to start looking for ways of proving that. Or maybe humans can never understand such a network but, potential super-human entities, e.g. those built by future AI technologies, may be able to understand it. In any of these cases, neuroscience should be informed by this consideration and a lot of approaches currently deployed to understand brains may be rather transparently unable to deliver the results neuroscientists are looking for. 

The popular approaches used to study brains can readily be focused on studying the nature component as opposed to nurture component. Behaviorally, we may ask how learning changes the choice of actions. When we study representations, we can ask which loss function, architecture, and learning dynamics would have given rise to the measured representations. Alternatively, we may ask about the representation of learning signals. When we study connectomics, we can focus on the large scale anatomy and circuit motifs [5, 27], which likely are genetically specified, instead of which exact neuron connects to which other exact neuron, which is likely to be learned. Perturbation approaches such as optogenetics can be focused on perturbing the signals that matter for learning. Even within molecular research we may focus on the cascades that set up the computation, e.g. synaptic plasticity, versus those involved in the computation per se. Instead of asking _how the brain works_ we should, arguably, ask _how it learns to work_ . 

## **1 Acknowledgements** 

We are thankful to many people for discussion and inspiration. Of particular importance were John Krakauer, Neil Rabinowitz, the MILA group, and Adam Marblestone. We want to thank NIH (R01MH103910) for funding. 

## **References** 

- [1] Anish Athalye, Logan Engstrom, Andrew Ilyas, and Kevin Kwok. Synthesizing robust adversarial examples. _arXiv preprint arXiv:1707.07397_ , 2017. 

- [2] Yoshua Bengio, Patrice Simard, Paolo Frasconi, et al. Learning long-term dependencies with gradient descent is difficult. _IEEE transactions on neural networks_ , 5(2):157–166, 1994. 

- [3] Irving Biederman. Recognition-by-components: a theory of human image understanding. _Psychological review_ , 94(2):115, 1987. 

- [4] Michael Dickinson. Solving the mystery of insect flight. _Scientific American_ , 284(6):48–57, 2001. 

- [5] Rodney J Douglas and KA Martin. A functional microcircuit for cat visual cortex. _The Journal of physiology_ , 440(1):735–769, 1991. 

- [6] Matthew S Farrell, Stefano Recanatesi, Guillaume Lajoie, and Eric Shea-Brown. Dynamic compression and expansion in a classifying recurrent network. _bioRxiv_ , page 564476, 2019. 

7 

- [7] Eberhard E Fetz. Operant conditioning of cortical unit activity. _Science_ , 163(3870):955–958, 1969. 

- [8] Nicholas Frosst and Geoffrey Hinton. Distilling a neural network into a soft decision tree. _arXiv preprint arXiv:1711.09784_ , 2017. 

- [9] Leon A Gatys, Alexander S Ecker, and Matthias Bethge. Image style transfer using convolutional neural networks. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 2414–2423, 2016. 

- [10] Xavier Glorot and Yoshua Bengio. Understanding the difficulty of training deep feedforward neural networks. In _Proceedings of the thirteenth international conference on artificial intelligence and statistics_ , pages 249–256, 2010. 

- [11] Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining and harnessing adversarial examples. _arXiv preprint arXiv:1412.6572_ , 2014. 

- [12] Song Han, Huizi Mao, and William J Dally. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. _arXiv preprint arXiv:1510.00149_ , 2015. 

- [13] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. _arXiv preprint arXiv:1503.02531_ , 2015. 

- [14] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, and Hartwig Adam. Mobilenets: Efficient convolutional neural networks for mobile vision applications. _arXiv preprint arXiv:1704.04861_ , 2017. 

- [15] Forrest N Iandola, Song Han, Matthew W Moskewicz, Khalid Ashraf, William J Dally, and Kurt Keutzer. Squeezenet: Alexnet-level accuracy with 50x fewer parameters and¡ 0.5 mb model size. _arXiv preprint arXiv:1602.07360_ , 2016. 

- [16] Eric Jonas and Konrad Paul Kording. Could a neuroscientist understand a microprocessor? _PLoS computational biology_ , 13(1):e1005268, 2017. 

- [17] Eric R Kandel, James H Schwartz, Thomas M Jessell, Department of Biochemistry, Molecular Biophysics Thomas Jessell, Steven Siegelbaum, and AJ Hudspeth. _Principles of neural science_ , volume 4. McGraw-hill New York, 2000. 

- [18] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural networks. In _Advances in neural information processing systems_ , pages 1097–1105, 2012. 

- [19] Yann LeCun, John S Denker, and Sara A Solla. Optimal brain damage. In _Advances in neural information processing systems_ , pages 598–605, 1990. 

- [20] Chunyuan Li, Heerad Farkhoor, Rosanne Liu, and Jason Yosinski. Measuring the intrinsic dimension of objective landscapes. _arXiv preprint arXiv:1804.08838_ , 2018. 

- [21] Francis Mollica and Steven T Piantadosi. Humans store about 1.5 megabytes of information during language acquisition. _Royal Society Open Science_ , 6(3):181393, 2019. 

8 

- [22] Julian D Olden and Donald A Jackson. Illuminating the “black box”: a randomization approach for understanding variable contributions in artificial neural networks. _Ecological modelling_ , 154(1-2):135–150, 2002. 

- [23] Razvan Pascanu, Tomas Mikolov, and Yoshua Bengio. On the difficulty of training recurrent neural networks. In _International conference on machine learning_ , pages 1310–1318, 2013. 

- [24] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. _OpenAI Blog_ , 1(8), 2019. 

- [25] Venkatakrishnan Ramaswamy. An algorithmic barrier to neural circuit understanding. _bioRxiv_ , page 639724, 2019. 

- [26] DA Robinson. Adaptive gain control of vestibuloocular reflex by the cerebellum. _Journal of Neurophysiology_ , 39(5):954–969, 1976. 

- [27] Mikail Rubinov and Olaf Sporns. Complex network measures of brain connectivity: uses and interpretations. _Neuroimage_ , 52(3):1059–1069, 2010. 

- [28] Michael Schmidt and Hod Lipson. Distilling free-form natural laws from experimental data. _science_ , 324(5923):81–85, 2009. 

- [29] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of go with deep neural networks and tree search. _nature_ , 529(7587):484, 2016. 

- [30] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al. Mastering the game of go without human knowledge. _Nature_ , 550(7676):354, 2017. 

- [31] Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, and Rob Fergus. Intriguing properties of neural networks. _arXiv preprint arXiv:1312.6199_ , 2013. 

- [32] Xundong Wu, Yong Wu, and Yong Zhao. Binarized neural networks on the imagenet classification task. _arXiv preprint arXiv:1604.03058_ , 2016. 

- [33] Jason Yosinski, Jeff Clune, Anh Nguyen, Thomas Fuchs, and Hod Lipson. Understanding neural networks through deep visualization. _arXiv preprint arXiv:1506.06579_ , 2015. 

- [34] Matthew D Zeiler and Rob Fergus. Visualizing and understanding convolutional networks. In _European conference on computer vision_ , pages 818–833. Springer, 2014. 

- [35] Wenda Zhou, Victor Veitch, Morgane Austern, Ryan P Adams, and Peter Orbanz. Nonvacuous generalization bounds at the imagenet scale: a pac-bayesian compression approach. _ICLR_ , 2018. 

9 

