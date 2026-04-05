# LEARNING GRID CELLS BY PREDICTIVE CODING 

## **Mufeng Tang, Helen Barron & Rafal Bogacz** 

MRC Brain Network Dynamics Unit, University of Oxford 

_{_ mufeng.tang, helen.barron, rafal.bogacz _}_ @bndu.ox.ac.uk 

## ABSTRACT 

Grid cells in the medial entorhinal cortex (MEC) of the mammalian brain exhibit a strikingly regular hexagonal firing field over space. These cells are learned after birth and are thought to support spatial navigation but also more abstract computations. Although various computational models, including those based on artificial neural networks, have been proposed to explain the formation of grid cells, the process through which the MEC circuit _learns_ to develop grid cells remains unclear. In this study, we argue that predictive coding, a biologically plausible plasticity rule known to learn visual representations, can also train neural networks to develop hexagonal grid representations from spatial inputs. We demonstrate that grid cells emerge robustly through predictive coding in both static and dynamic environments, and we develop an understanding of this grid cell learning capability by analytically comparing predictive coding with existing models. Our work therefore offers a novel and biologically plausible perspective on the learning mechanisms underlying grid cells. Moreover, it extends the predictive coding theory to the hippocampal formation, suggesting a unified learning algorithm for diverse cortical representations. 

## 1 INTRODUCTION 

Our brain contains a rich set of neural representations of space that help us navigate in an everchanging world. These include hippocampal place cells (O’Keefe, 1976), which fire when an animal is at a specific spatial position, and grid cells observed in the medial entorhinal cortex (MEC) (Hafting et al., 2005), which fire when an animal occupies multiple positions on a hexagonal or triangular grid. Grid cells have been observed across various species (Fyhn et al., 2008; Yartsev et al., 2011; Doeller et al., 2010), and their remarkable regularity has raised extensive interest in the computational mechanism underlying their emergence. Earlier models have focused on how mechanisms, such as membrane potential oscillation (O’Keefe & Burgess, 2005; Hasselmo et al., 2007) and specialized recurrent connectivity, can generate grid-like firing patterns (Fuhs & Touretzky, 2006; Burak & Fiete, 2009). More recently, research has shown that grid cells can emerge in recurrent neural networks (RNNs) trained using backpropagation through time (BPTT) for path integration tasks. The models are trained to predict their current location by integrating velocity inputs (Cueva & Wei, 2018; Banino et al., 2018; Whittington et al., 2020; Sorscher et al., 2023), providing a normative, task-driven account of the computational problem that the MEC grid cells address. However, the process by which the MEC circuit acquires, or _learns_ the grid cells in a biologically plausible way has been largely neglected, despite the fact that grid cells are known to be learned, rather than hardwired at birth (Langston et al., 2010; Wills et al., 2010). Existing learning models (e.g. Weber & Sprekeler (2018)) are highly specialized for grid cells, and it is unclear whether plasticity rules for only one specific cell type exist in the brain. 

In this paper, we directly tackle the learning problem underlying the emergence of grid cells using _predictive coding_ , an algorithm modeling the plasticity rules for a variety of cortical functions and representations (Rao & Ballard, 1999; Friston, 2005). Our approach to modeling grid cell emergence through predictive coding is motivated by three key factors: Firstly, the predictive coding algorithm can be implemented in predictive coding networks (PCNs) with local computations and Hebbian plasticity (Bogacz, 2017), making it more biologically plausible than learning rules such as backpropagation. Secondly, PCNs have been successful in replicating representations in other regions of the brain, such as the visual cortex (Rao & Ballard, 1999; Olshausen & Field, 1996; Millidge et al., 

1 

2024). Thirdly, PCNs have demonstrated the ability to perform hippocampus-related functions, such as associative and sequential memories (Salvatori et al., 2021; Tang et al., 2023; 2024). 

The primary contribution of this work is to demonstrate for the first time that grid cells naturally emerge in PCNs trained to represent spatial inputs with biologically plausible plasticity rules. In this work we: 

- show that hexagonal grid cells develop as the latent representations of place cells in classical PCNs (Rao & Ballard, 1999; Olshausen & Field, 1996) with sparse and non-negative constraints; 

- train a dynamical extension of classical PCNs, called temporal predictive coding network (tPCN) (Millidge et al., 2024), in path integration tasks and observe that the latent activities of the tPCN develop hexagonal, grid-like representations, similar to what has been discovered in RNNs; 

- develop an understanding of grid cell emergence in tPCN, by showing analytically that the Hebbian learning rule of tPCN implicitly approximates truncated BPTT (Williams & Peng, 1990); 

- show that tPCN can robustly develop grid cells under different architectural choices, and even without velocity inputs in path integration. 

Overall, our results present an effective and plausible learning rule for hexagonal grid cells in the MEC based on predictive coding. We offer a novel extension of predictive coding theory, which has traditionally been used to model visual representations (Rao & Ballard, 1999; Olshausen & Field, 1996), to encompass spatial representations in the MEC. Our findings therefore offer a novel understanding of how a single, unified learning algorithm can be employed by different brain regions to represent inputs of various levels of abstraction. 

## 2 RELATED WORK 

**Computational Models of Grid Cells** The periodicity of grid cells inspired early models of grid cells based on membrane potential oscillations, where the periodic firing of grid cells results naturally from the interference between somatic and dendritic oscillators in MEC pyramidal neurons (O’Keefe & Burgess, 2005; Hasselmo et al., 2007). These models were subsequently extended to incorporate multiple networks of oscillatory neurons (Zilli & Hasselmo, 2010). However, these models lack biological plausibility as they require an unrealistically large number of networks (Giocomo et al., 2011). Another major family of models leverages the recurrent attractor networks and obtains grid firing patterns (Fuhs & Touretzky, 2006; Burak & Fiete, 2009; Ocko et al., 2018) by hand-tuning the recurrent connectivity to form a center-surround structure. These networks perform robust and accurate path integration (Burak & Fiete, 2009) and can explain experimental observations such as the deformation of grid cells in irregular environments (Ocko et al., 2018). However, as pointed out by Sorscher et al. (2023), these models lack an explanation for the underlying spatial task that gives rise to the specific recurrent connectivity. 

To address this gap, recent studies have explored the question _‘If grid cell is the answer, what is the question?’_ . Dordek et al. (2016) showed that grid cells emerge as the non-negative principal components of place cells, while Stachenfeld et al. (2017) proposed that grid cells form a basis for predicting future observations. Other studies have focused on the multi-modularity of grid cells by optimizing biologically constrained objective functions (Dorrell et al., 2022; Schaeffer et al., 2024). Notably, multiple research tracks have found that RNNs trained to perform path integration tasks will develop hexagonal grid representations in their latent states (Cueva & Wei, 2018; Banino et al., 2018; Whittington et al., 2020), suggesting that grid cells emerge as a result of successful navigation. These findings were further reinforced by Sorscher et al. (2023), who analytically demonstrated that path integration with certain implementation choices, such as non-negativity, is a sufficient condition for the emergence of grid cells, clarifying earlier controversies (Schaeffer et al., 2022). However, none of these works have addressed how the MEC/hippocampal network learns the grid cells. The RNN models are trained by BPTT, a learning rule unlikely to be employed by the brain (Lillicrap & Santoro, 2019). Even though the principal component model by Dordek et al. (2016) can be learned with the plausible Sanger’s rule (Sanger, 1989), it has been shown that principal component analysis (PCA) cannot be applied to other brain regions such as the visual areas (Olshausen & Field, 1996), and Sanger’s rule cannot be generalized to dynamical tasks such as path integration. Earlier models of the learning process of grid cells have explored plausible learning rules such as 

2 

**==> picture [386 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>Entorhinal Cortex Hippocampus<br>ReLU<br>error value interneuron excitatory inhibitory<br>**----- End of picture text -----**<br>


Figure 1: **Architecture and circuit implementation of PCNs.** A: Sparse, non-negative PCN as a generative model. During learning, **p** is given and the latent **g** and **W** are inferred and learned through a type of EM algorithm. B: Simlar to A, but with dynamic inputs **p** _t_ and recurrent weights **W** r. The dashed velocity inputs are optional (see Section 4.4). C: Circuit implementation of tPCN, adapted from Tang et al. (2024) with a mapping to MEC and hippocampus. 

spike time-dependent plasticity (Widloski & Fiete, 2014) and variants of Hebbian learning rules (Kropff & Treves, 2008) within networks of excitatory and inhibitory neurons (Weber & Sprekeler, 2018). However, these learning rules are highly specialized, and have not been shown to reproduce representations from other brain regions with non-spatial tasks. Recent works have also modeled the hippocampal formation using generative models with plausible learning rules similar to predictive coding (George et al., 2024; Bredenberg et al., 2021), though these studies did not address 2D spatial learning. 

**Predictive Coding** Predictive coding has been an influential theory in understanding cortical computations (Friston, 2005; Rao & Ballard, 1999; Bogacz, 2017) and has been applied to modeling various cortical functions (see Millidge et al. (2021) for a review). Specifically, in the visual cortex, PCNs develop realistic visual representations such as Gabor-like receptive fields in response to both static (Rao & Ballard, 1999; Olshausen & Field, 1996) and moving stimuli (Millidge et al., 2024). Recently, theories have been developed to describe hippocampo-neocortical interactions using predictive coding (Barron et al., 2020), and PCNs have demonstrated the ability to memorize and retrieve static and dynamic visual patterns, a key function of the hippocampus (Salvatori et al., 2021; Tang et al., 2023; 2024). Our work explores whether the representational learning capabilities of predictive coding can be extended to the hippocampal formation, which has so far only been functionally modeled by PCNs. 

The computations of PCNs use only local neural dynamics and Hebbian plasticity, making it biologically more plausible than backpropagation (Whittington & Bogacz, 2017). It has also been shown that predictive coding approximates backpropagation both in theory and practice (Whittington & Bogacz, 2017; Song et al., 2024; Pinchetti et al., 2024). Unlike many other Hebbian learning rules, predictive coding can be extended to temporal predictive coding networks (tPCNs), which use recurrent connections to process dynamic stimuli (Millidge et al., 2024). However, while Millidge et al. (2024) demonstrated that tPCNs approximate Kalman filtering, the relationships between tPCNs and RNNs remain unclear. In this work, we train tPCNs for path integration and compare their performance with RNNs both analytically and experimentally in this context. 

## 3 MODELS 

**Non-negative Sparse PCN** We first investigate the classical PCN (Rao & Ballard, 1999) for its ability to form grid representations. Assuming a place cell input **p** _∈_ R _[N][p]_ that represents a location in 2D space as an _Np_ -dimensional vector, a simple 2-layer PCN generates predictions of **p** using its latent activities **g** _∈_ R _[N][g]_ (which will develop grid-like representations) and a weight matrix **W** (Fig 1A). The generative model minimizes the following loss function subject to two constraints: _L_ PCN = _∥_ **p** _−_ **Wg** _∥_ 2[2][+] _[ ∥]_ **[g]** _[∥]_[2] 2[+ 2] _[λ][∥]_ **[g]** _[∥]_[1] (1) 

3 

where _∥_ **g** _∥_ 2[2][constrains the] _[ l]_[2 norm of the latent] **[ g]**[ and] _[ λ][∥]_ **[g]** _[∥]_[1][enforces sparsity, similar to the sparse] coding model (Olshausen & Field, 1996). This loss function is minimized via an expectationmaximization (EM) algorithm, alternating between the optimization over **g** (inference) and **W** (learning) (see Appendix A.1 for the training algorithm): 

**==> picture [341 x 31] intentionally omitted <==**

where _**ϵ**_ **[p]** := **p** _−_ **Wg** and we apply a ReLU to the inference dynamics to constrain the latent activities to be non-negative. The inference and learning dynamics can be implemented in a plausible circuit (Bogacz, 2017). After convergence, we examine the firing fields of the latent activities **g** . 

**Path Integrating tPCN** To account for the learning of spatial representations in moving animals, we also investigate tPCN that extends the classical PCNs to the temporal domain (Millidge et al., 2024; Tang et al., 2024) in path integration tasks (Fig. 1B). The model receives a series of place cell activities **p** 1 _, ...,_ **p** _T_ and velocity inputs **v** 1 _, ...,_ **v** _T_ that represent the trajectory of an agent moving in a 2D space, and minimizes the following loss function at each time step _t_ : 

**==> picture [328 x 12] intentionally omitted <==**

where _f_ and _h_ are both nonlinear activation functions, and **W** in, **W** r and **W** out are weight matrices projecting the predictions. We define _**ϵ**_ **[p]** _t_[:=] **[ p]** _[t][−][f]_[(] **[W]**[out] **[g]** _[t]_[)][,] _**[ϵ]**_ **[g]** _t_[:=] **[ g]** _[t][−][h]_[(] **[W]**[r] **[g]**[ˆ] _[t][−]_[1][+] **[W]**[in] **[v]** _[t]_[)][.][The] model learns by first optimizing the loss function with respect to **g** _t_ via gradient descent: 

**==> picture [301 x 13] intentionally omitted <==**

and then optimizing weights by: 

**==> picture [350 x 27] intentionally omitted <==**

˜ ˆ where _f[′]_ and _h[′]_ are Jacobians of the nonlinear functions _f_ and _h_ , and **g** _t_ := **W** r **g** _t−_ 1 + **W** in **v** _t_ . After the inference (Equation 5) converges, we set **g** ˆ _t_ to the converged value of **g** _t_ , which will be used for optimizing the objective function at the next time step i.e., _L_ tPCN _,t_ +1. The model is trained on a large number of trajectories _{_ **v** _t,_ **p** _t}_ and after training, a set of velocity inputs from unseen trajectories is presented to the model. The model then performs a forward pass through time and layers to predict the positions encoded by place cells (see Appendix A.1 for the training and testing algorithms of tPCN): 

**==> picture [295 x 11] intentionally omitted <==**

The model is evaluated on 1) the accuracy of path integration position prediction ˆ **p** _t_ and 2) the firing fields of the latent **g** . When both _f_ and _h_ are linear, these computations can be plausibly implemented in a neural circuit shown in Figure 1C, with local inference computations (Equation 5) and Hebbian learning rules (Equation 6) (Millidge et al., 2024). When the activation functions involve only local nonlinearity, such as tanh or ReLU, the Jacobians are diagonal and the inference and learning rules remain local and Hebbian (Millidge et al., 2022), and additional circuitry components can be included to plausibly implement the nonlinearities (Whittington & Bogacz, 2017). Within the context of spatial representation learning, this circuit implementation can be naturally mapped to the circuitry of the hippocampal formation. We discuss the relationship of this circuit implementation to existing and potential experimental evidence in the Discussion section. 

**Input of the Model** In models discussed in this work, we assume that grid cells are inferred as latent representations of place cells. Although previous models have followed the opposite direction of the relationship, several strands of experimental evidence have suggested the emergence of grid cells as a result of place cells, including the earlier development of place cells (Bush et al., 2014; Langston et al., 2010; Wills et al., 2010). In both PCN and tPCN models, the place cell inputs are constructed as 2D difference-of-softmaxed-Gaussian (DoS) curves flattened into 1D vectors, which have been shown to yield hexagonal grid representations in RNNs (Schaeffer et al., 2022; Sorscher et al., 2023). The firing centers of the place cells are uniformly distributed across a 2D environment. For PCN, the inputs are _Nx_ evenly distributed locations in the environment ( _Nx_ large enough to cover the whole environment) represented by the _Np_ place cells. For tPCN, the trajectories for 

4 

**==> picture [393 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B E<br>C D<br>**----- End of picture text -----**<br>


Figure 2: **Grid cells developed in PCN.** A: Latent representations of a sparse, non-negative PCN, resembling hexagonal grid cells in the MEC. Numbers in the title reflect the grid scores. B: Grid cells obtained via the pattern formation theory/non-negative PCA discussed in Sorscher et al. (2023); Dordek et al. (2016). C, D: Latent representations without sparsity or non-negativity, respectively. E: Distribution of grid scores of the representations in A and B. 

the path integration task are obtained by simulating an agent performing a smooth random walk in the square environment. At each point in time, the _Np_ place cells will be uniquely activated, representing the agent’s current location. The velocity inputs **v** _t_ are 2D vectors representing the speed of the simulated agent on the _x_ and _y_ coordinates at time step _t_ . The effect of boundaries is simulated by slowing down the agent and reverting its moving direction near the borders of the environment. We sample a large number of trajectories to cover the whole simulated environment for training. 

## 4 RESULTS 

## 4.1 SPARSE NON-NEGATIVE PCN DEVELOPS LATENT GRID CELLS 

Here we examine whether the sparse non-negative PCN can develop hexagonal, grid-like latent representations of the space after training, by plotting each latent neuron’s responses to the _Nx_ = 900 locations in the 2D space. We use _Np_ = 512 and _Ng_ = 256. The “gridness” of the 2D latent representations is evaluated using the _grid score_ metric, commonly employed in both experimental and computational studies (Sargolini et al., 2006; Banino et al., 2018) (see A.3 for grid score calculation). We found that this simple, 2-layer PCN can develop hexagonal grid cells similar to those observed in the MEC (Figure 2A). For comparison, we reproduce the results from Dordek et al. (2016) and Sorscher et al. (2023), which show theoretically that performing non-negative PCA on the place cell inputs is guaranteed to produce hexagonal grid representations as the principal components of the _Nx × Np_ place cell input matrix. The visual results of the reproduction are shown in Figure 2B, and we compare the distribution of grid scores of the PCN’s latent neuron firing fields with those of the non-negative principal components in Figure 2E. The grid scores between our sparse non-negative PCN and non-negative PCA are similarly distributed. 

Why does the sparse, non-negative PCN develop hexagonal grid cells? While a precise analytical explanation is left for future work, we offer an intuitive hypothesis here. When presented with a batch _Nx_ of place cell inputs, the objective of PCN (Equation 1) can be written compactly as: 

**==> picture [302 x 14] intentionally omitted <==**

where **P** _∈_ R _[N][x][×][N][p]_ is the place cell activities across _Nx_ locations, and **G** _∈_ R _[N][x][×][N][g]_ represents grid cell responses. On the other hand, the objective function of PCA is: 

**==> picture [288 x 13] intentionally omitted <==**

where **M** is the _Ng × Np_ readout matrix. The constraint **GG** _[⊤]_ = _**I** Nx_ in Equation 9 enforces orthonormality of the grid cell matrix **G** columns, meaning they are orthogonal and have unit norm. 

5 

**==> picture [395 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>1.4m<br>D F<br>E G<br>1.4m<br>**----- End of picture text -----**<br>


Figure 3: **tPCN in path integration** . A: Visual demonstration of the performance of tPCN and RNN in path integration. B: RMSEs between the decoded and ground-truth 2D positions by tPCN and RNN with different agent moving speed. C: Grid score distributions of tPCN and RNN with different agent moving speed. D, E: Firing fields of latent neurons in a tPCN and an RNN respectively, when _dt_ = 0 _._ 02. F, G: Firing fields of latent neurons in a tPCN and an RNN respectively, when _dt_ = 0 _._ 1. 

We hypothesize that the constraint _∥_ **g** _i∥_ 2[2][+ 2] _[λ][∥]_ **[g]** _[i][∥]_[1][for our sparse PCN achieves this orthonormal-] ity implicitly: while the constraints are imposed on the rows of **G** , the overall sparsity of entries in **G** could induce orthogonality among its columns, with the _l_ 2 term constraining the norm of the columns to achieve normality implicitly. Indeed, Figure 2C shows that if we remove the sparsity constraint, the latent neurons’ firing fields will no longer be hexagonal. Similarly, without ReLU i.e., non-negativity applied to the inference dynamics, we also could not obtain hexagonal grid cells (Figure 2D). It is worth noting that although (non-negative) PCA can be learned with the biologically plausible Sanger’s rule (Sanger, 1989), it lacks PCN’s generalizability to different architectures (Salvatori et al., 2022) and to other brain regions such as the visual cortex (Olshausen & Field, 1996; Rao & Ballard, 1999). However, it can be noticed that the grid cells by PCN lack the multi-modularity of the grid cells by non-negative PCA i.e., grid cells with different firing periods. We suspect that although sparse PCNs can approximate the orthonormality of latent variables, they lack PCA’s ability to extract latent variables ordered by the amount of explained variance in data, with higher variance naturally corresponding to larger spatial scales and vice versa. 

## 4.2 TPCN DEVELOPS GRID CELLS BY PATH INTEGRATION 

Although training a static PCN with a large number of place cell activations can already give rise to brain-like hexagonal grid cells, the emergence of grid cells is known to rely on dynamic motion of animals (McNaughton et al., 2006; Winter et al., 2015). Therefore, we investigate tPCN in a path integration task, where the simulated agent uses dynamic velocity inputs to determine its current position. As a reference, we compare tPCN with RNNs trained in path integration, which have been shown to develop hexagonal grid cells (Cueva & Wei, 2018; Banino et al., 2018; Sorscher et al., 2023) and share the same graphical structure as tPCN (Figure 1B). However, it is important to note that RNNs are trained with the biologically implausible backpropagation-though-time (BPTT) algorithm, which requires “unrolling” of the network through time, a process unlikely to occur in the brain (Lillicrap & Santoro, 2019). 

We first evaluate whether tPCN can learn to perform the path integration task using local and Hebbian learning rules. We trained a tPCN model with _Ng_ = 2048 latent neurons on trajectories within a 1 _._ 4m _×_ 1 _._ 4m environment represented by _Np_ = 512 place cells. After training, we tested the model on a set of unseen trajectories with velocity input **v** _t_ , and assessed whether the tPCN and RNN models could predict the correct positions using Equation 7. As the output of the networks is by averaging the center positions of thethe _Np_ -dimensional population activity 3of most active place cells in the outputthe place cells, we calculate the predicted **p** ˆ _t_ , and calculate the2D positions 

6 

**==> picture [396 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
A C<br>Dependency Forward propagation D<br>B<br>**----- End of picture text -----**<br>


Figure 4: **Comparing tPCN and tBPTT.** A: Dependencies of latent grid cells in tPCN and RNN trained with 1-step tBPTT. Black arrows indicate the flow of computations during a forward pass and red arrows indicate the dependency of latent variables. B: Firing fields of the latent neurons of an RNN trained by 1-step tBPTT. C, D: Path integration RMSE and grid score distributions of 1-step tBPTT, BPTT and tPCNs with different inference iterations. “tPCNk” indicates tPCN trained with k inference iterations. 

root mean square error (RMSE) between the decoded and ground-truth 2D positions. The visual and numerical results are shown in Figure 3A and B, where we also varied a scaling factor _dt_ of the simulated agent’s speed, sampled from a Rayleigh distribution with mean 1, to test the robustness of the results. Note that we do not intend to model physiologically realistic speed of animals with these values. The performance of tPCN is comparable to that of the RNN, though it slightly deteriorates when the agent moves at higher speeds. 

Next, we examine whether the tPCN model develops grid-like representations in its latent layer during path integration. We plot the firing fields of the 2048 latent neurons given an unseen set of trajectories covering the entire space. The neurons with the highest grid scores are shown in Figure 3C, which reveals a grid-like, hexagonal firing pattern with high grid scores. Visually, these grid cells are similar to those in a trained RNN with the same architecture shown in Figure 3E, replicating the results from (Sorscher et al., 2023). To systematically compare the grid cells in tPCN and RNN, we plot the distribution of grid scores in both models as a function of the movement speed of the agent in the environment in Figure 3C. When the movement is slow, the grid score distributions are similar between tPCN and RNN. However, as the _dt_ increases to 0 _._ 05 and 0 _._ 1, tPCN tends to have higher grid scores than RNN. This is visually reflected in Figure 3F (tPCN) and G (RNN), which shows the latent representations developed by tPCN largely retain the grid-like pattern whereas firing centers of many of the RNN neurons no longer form a grid when _dt_ = 0 _._ 1. Interestingly, the band-like representations present in both models in this case are observed in MEC (Krupic et al., 2012), although their existence is controversial (Navratilova et al., 2016). 

## 4.3 TPCN APPROXIMATES TRUNCATED BPTT 

Next, we asked why hexagonal grid representations emerge both when training a tPCN using a BPTT-free Hebbian learning rule and when training an RNN using BPTT. We provide an analytical comparison between the learning rules of tPCN and RNN. Assuming a vanilla, sequenceto-sequence RNN with exactly the same graphical structure as in Figure 1A, its dynamics can be recursively described as: 

**==> picture [294 x 11] intentionally omitted <==**

The loss that this RNN is trained to minimize is the cumulative prediction error: 

**==> picture [286 x 13] intentionally omitted <==**

7 

Suppose BPTT is performed at every step _t_ to update weights in this RNN, the learning rule for **W** r at step _t_ can be expressed as (see Appendix A.2 for derivations): 

**==> picture [307 x 16] intentionally omitted <==**

where _**ϵ**_ **[p]** _t_[denotes the prediction error] **[ p]** _[t][−]_ **[p]**[ˆ] _[t]_[and the] _∂[∂]_ **g[g]** _k[t]_[terms correspond to the unrolling in BPTT,] which can be factorized into a chain of partial derivatives (Bellec et al., 2020). On the other hand, for tPCN, if we assume that the inference dynamics in Equation 5 has fully converged (∆ **g** _t_ = 0) at the time of weight update, the learning rule of tPCN can be written as (see Appendix A.2 for derivations): 

**==> picture [285 x 12] intentionally omitted <==**

Two key differences between these learning rules stand out. First, tPCN does not involve the recursive unrolling term, thereby avoiding the need to maintain a perfect memory of all preceding hidden states. Second, instead of using the forward-propagated **g** _t−_ 1 as in Equation 10, tPCN employs the ˆ inferred **g** _t−_ 1 from Equation 5 (underlined). The first difference suggests an equivalence between tPCN and RNN trained with truncated BPTT (tBPTT) with a truncation window of size 1 (1-step tBPTT) (Williams & Peng, 1990), where the RNN does not backpropagate _any_ hidden states through time when updating the weights. This characteristic could potentially harm the RNN’s performance as it cannot effectively perform temporal credit assignment. However, the second difference parˆ tially solves this problem, as **g** _t−_ 1 is inferred following Equation 5, which includes the term _**ϵ**_ **[p]** _t−_ 1 that communicates the place cell prediction error at step _t −_ 1. Therefore, when **W** r is updated at step _t_ , the **g** ˆ _t[⊤] −_ 1[term in][ ∆] **[W]** r[tPCN] will effectively form an eligibility trace (Bellec et al., 2020) that allows the model to access historical prediction errors on the place cell level. Figure 4A illustrates this difference between tPCN and RNN trained by 1-step tBPTT, highlighting the dependency of tPCN hidden states on past place cell activations. In Appendix A.2 we also discuss the relationship between the update rules for **W** in and **W** out in these two models. 

To verify this theoretical difference, we compare tPCN with RNNs trained by tBPTT in the path inˆ tegration task. Since ˆ **g** _t_ in tPCN is initialized by a forward pass _f_ ( **W** r **g** _t−_ 1) and then updated by the iterative inference (Appendix A.1), the behavior of 1-step tBPTT, which computes its latent states via a forward pass at each time step, should be closer to tPCN with fewer inference iterations. Therefore, we evaluate tPCN with various inference iterations. Figure 4B shows the grid cells learned by an RNN trained with 1-step tBPTT, which still exhibit hexagonal grid firing fields, though with lower grid scores than those from full BPTT. This suggests that backpropagating the error through all time steps is not entirely necessary for RNNs to generate grid cell-like representations. In Figure 4C we show the path integration performance of RNN by 1-step tBPTT and BPTT, as well as tPCNs with different inference iterations from 1 to 50. As can be seen, tPCN with a single inference iteration has identical performance to RNN trained by tBPTT, and its performance will improve as we increase the number of inference iterations but will saturate around 20 iterations. Overall, this graph suggests that tPCN with 5 or more inference iterations can effectively perform temporal credit assignment that improves upon tPCN1 or 1-step tBPTT, potentially due to the eligibility trace. However, this eligibility trace arises from local inference dynamics (Equation 5) rather than from unrolling the RNN graph as in Bellec et al. (2020). This improvement is also reflected in the grid scores (Figure 4D), although increasing the inference iterations does not necessarily result in better grid score representations. We suspect that although the gridness of latent representations is somewhat related to path integration performance, their relationship is not linear. It is also worth noting that to fully evaluate the similarities and differences between BPTT and tPCN, an in-depth comparison is needed across different tasks and versions of tBPTT. We aim to investigate this question in future works as it is beyond the scope of this paper. 

## 4.4 ROBUSTNESS OF GRID CELL REPRESENTATIONS IN TPCN 

Inspired by Schaeffer et al. (2022), we examine the robustness of our results against different architectural choices of the tPCN model, to understand what contributes to the emergence of grid cells within tPCN. Specifically, we vary the following components of the model: 1) Encoding of the place cell activities; 2) Output nonlinearity _f_ ; 3) Recurrent nonlinearity _h_ ; 4) Environment sizes; 5) Latent sizes and 6) Velocity input to the model. The baseline model has DoS place cell encodings, _h_ = ReLU, _f_ = softmax, 1 _._ 4m _×_ 1 _._ 4m environment and latent size 2048 with velocity inputs. 

8 

**==> picture [279 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
A C<br>D<br>E<br>F<br>B<br>G<br>H<br>I<br>**----- End of picture text -----**<br>


**==> picture [109 x 229] intentionally omitted <==**

Figure 5: **Robust emergence of grid cells in tPCN.** A, B: Path integration RMSE and grid scores of tPCN in different setups. “Stationary baseline” refers to a model that always predicts the initial position regardless of movement. C-I: Firing fields of latent neurons in tPCNs with C: Gaussian place cells; D: _f_ =tanh; E: _h_ =tanh; F: 1 _._ 8m _×_ 1 _._ 8m environment; G: 1 _._ 2m _×_ 1 _._ 2m environment; H: 256 latent neurons; I: tPCN without velocity input. 

We first examine whether replacing the place encoding with Gaussian curves affects the model’s performance. As shown in Figure 5A, B and C, the Gaussian place cells do not affect the path integration performance, but the latent representations are no longer hexagonal. This is consistent with earlier findings that the DoS place cell encoding is necessary for hexagonal grid cells (Dordek et al., 2016; Sorscher et al., 2023; Schaeffer et al., 2022). 

The choices of _f_ and _h_ are particularly interesting: as discovered by earlier works (Dordek et al., 2016; Sorscher et al., 2023), a choice of _h_ that imposes non-negativity constraint on the latent activities, such as ReLU, is necessary for the emergence of hexagonal grid cells. In our tPCN model, the activation functions are also important for biological plausibility: in both Equation 5 and Equation 6, the multiplication with the Jacobians _h[′]_ and _f[′]_ can be reduced to local, element-wise multiplications if _h_ and _f_ are element-wise nonlinearities such as ReLU and tanh. Although it is possible to design a circuit to perform the computations in softmax (Snow & Orchard, 2022), it is unclear how the Jacobian matrix of softmax can be computed in a biological circuit. Therefore, we first replace _f_ with a tanh function in our tPCN model and evaluate the model’s performance in both path integration and its latent representations. As shown in Figure 5A, replacing _f_ with tanh results in slightly worse path integration performance and lower grid scores than the softmax baseline. However, visually, the latent representations are hexagonal and grid-like (Figure 5D), suggesting that using a biologically more plausible _f_ would not significantly affect the emergence of grid cells within tPCN. On the other hand, replacing the non-negative constraint (ReLU) on the latent activities with _h_ = tanh results in the amorphous latent representations (Figure 5E), which is consistent with Sorscher et al. (2023). 

We next investigate the impact of the size of the environment, by training tPCN within a square environment of size 1 _._ 8m _×_ 1 _._ 8m (big) and an environment of size 1 _._ 2m _×_ 1 _._ 2m (small). Changing environment sizes does not affect the path integration performance, and does not affect tPCN’s capability of developing grid cells either (Figure 5F for big environment and G for small environment). We also vary the number of latent neurons in the model from 256 to 512 and 1024, which does not affect the grid cell representations (Figure 5H shows the latent representations learned by a tPCN with 256 latent neurons). However, with fewer latent neurons, the performance in path integration becomes worse as the model has fewer number of parameters to perform the task (Figure 5A). 

9 

Earlier studies using PCNs to model visual representations have mostly used unsupervised PCNs (Rao & Ballard, 1999; Olshausen & Field, 1996; Millidge et al., 2024), which corresponds to blocking the velocity input **v** _t_ into tPCN in Figure 1B. Here we asked how removing velocity input would affect the path integration performance˜ andˆ grid cell emergence of tPCN. Mathematically, this is achieved simply by re-defining **g** _t_ := **W** r **g** _t−_ 1 without changing any inference or learning dynamics. It can be seen from Figure 5A that the path integration performance is significantly affected by the absence of velocity input, with an RMSE even higher than the stationary baseline, where the model does not predict any movement at all. Intriguingly, the latent representations developed by this unsupervised tPCN are still grid cell-like (Figure 5I) with a similar grid score distribution to the baseline model. This result demonstrates that grid cells can still emerge even in a model unable to perform path integration at all. Therefore, our model predicts that path integration is not a sufficient condition for the emergence of grid cells, which resonates with Schaeffer et al. (2022). In other words, it predicts that animals unable to navigate due to impaired velocity encoding may still develop grid cells as a result of self-motion. 

## 5 DISCUSSION 

**Relationship to Experimental Observations** Here, we highlight properties of the biologically plausible circuit in Figure 1C, including those consistent with experimental observations, and those generating prediction about the hippocampal formation. This circuit can be naturally divided into a MEC layer and a hippocampal layer. The MEC layer contains velocity-encoding neurons ( **v** ) and grid cells ( **g** ), which aligns with experimental findings of the conjunctive representations of velocity and grids in the entorhinal cortex (Sargolini et al., 2006). In our model, grid cells in the ˆ MEC layer are recurrently connected through a specialized circuit involving interneurons **g** _t−_ 1 that inhibit the output signal from the grid cells, allowing the error neurons _**ϵ**_ **[g]** _t_[to compute the temporal] prediction errors. Experimental evidence suggests that lateral interactions in layer II of the MEC are predominantly inhibitory (Witter & Moser, 2006) and are mediated by interneurons such as basket cells (Jones & B¨uhl, 1993). Our model also predicts that these interneurons encode an eligibility ˆ trace **g** _t−_ 1 from the immediate past. While recent studies have reported grid cells representing prospective locations (Ouchi & Fujisawa, 2024), it remains to be verified whether these cells are mechanistically supported by such “past” cells. Additionally, neurons in the entorhinal cortex are known to encode errors (Ku et al., 2021), suggesting a possible error-driven learning mechanism similar to that in tPCN. 

In our model, the MEC and hippocampus are bidirectionally connected, a well-documented characteristic of entorhinal-hippocampal connectivity (Canto et al., 2008). Crucially, the circuit also posits the existence of error neurons _**ϵ**_ **[p]** _t_[in the hippocampus, which encode the discrepancy between place] cell activities and inputs from MEC grid cells. The CA1 sub-region of the hippocampus has been shown to serve as a mismatch detector between the hippocampus and cortex (Lisman, 1999; Duncan et al., 2012). Our model predicts that in spatial navigation, the error neurons _**ϵ**_ **[p]** _t_[in the hippocampus,] whose existence has been supported by Wirth et al. (2009) and Ku et al. (2021), can encode exactly this mismatch signal between the two regions. 

**Conclusion** In this work, we have demonstrated a biologically plausible learning rule for grid cells based on predictive coding. We have shown that with sparsity and non-negative constraints, classical PCNs can develop grid cell-like representations of batched place cell inputs. With inputs representing trajectories of moving agents, tPCN can also develop grid cell activations while performing path integration. We have developed a theoretical understanding of this property of tPCN by deriving and comparing its learning dynamics with that of BPTT, showing that unrolling a recurrent network is unnecessary for it to learn grid cells, and a more plausible approach with recursive inference dynamics should suffice. Furthermore, we have examined the robustness of our results by varying hyper-parameters of the model, and found that grid cells can be learned even without velocity inputs. Overall, our work demonstrates that predictive coding can serve as an effective and biologically plausible plasticity rule for neural networks to learn grid cells observed in the MEC. Importantly, compared with earlier learning rules specialized for grid cells, predictive coding is a general learning rule able to reproduce many other cortical functions and representations. Thus, our findings suggest that a single, unified plausible learning rule can be employed by the brain to find the most appropriate representation of cortical inputs in different regions. 

10 

## ACKNOWLEDGEMENT 

This work has been supported by Medical Research Council UK grant MC ~~U~~ U ~~0~~ 0003/1 to RB, an E.P. Abraham Scholarship in the Chemical, Biological/Life and Medical Sciences to MT, and UKRI Future Leaders Fellowship to HB (MR/W008939/1). The authors would like to acknowledge the use of the University of Oxford Advanced Research Computing (ARC) facility in carrying out this work. http://dx.doi.org/10.5281/zenodo.22558 

## REPRODUCIBILITY STATEMENT 

The code used for the experiments in this paper can be found at https://github.com/C16Mftang/placecell-pred-coding. All hyperparameters for training are detailed in the appendix. Additionally, proofs for the theoretical results discussed in the paper are also included in the appendix for verification. 

## REFERENCES 

- Andrea Banino, Caswell Barry, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski, Alexander Pritzel, Martin J Chadwick, Thomas Degris, Joseph Modayil, et al. Vector-based navigation using grid-like representations in artificial agents. _Nature_ , 557(7705):429–433, 2018. 

- Helen C Barron, Ryszard Auksztulewicz, and Karl Friston. Prediction and memory: A predictive coding account. _Progress in neurobiology_ , 192:101821, 2020. 

- Guillaume Bellec, Franz Scherr, Anand Subramoney, Elias Hajek, Darjan Salaj, Robert Legenstein, and Wolfgang Maass. A solution to the learning dilemma for recurrent networks of spiking neurons. _Nature communications_ , 11(1):3625, 2020. 

- Rafal Bogacz. A tutorial on the free-energy framework for modelling perception and learning. _Journal of mathematical psychology_ , 76:198–211, 2017. 

- Colin Bredenberg, Benjamin Lyo, Eero Simoncelli, and Cristina Savin. Impression learning: Online representation learning with synaptic plasticity. _Advances in Neural Information Processing Systems_ , 34:11717–11729, 2021. 

- Yoram Burak and Ila R Fiete. Accurate path integration in continuous attractor network models of grid cells. _PLoS computational biology_ , 5(2):e1000291, 2009. 

- Daniel Bush, Caswell Barry, and Neil Burgess. What do grid cells contribute to place cell firing? _Trends in neurosciences_ , 37(3):136–145, 2014. 

- Cathrin B Canto, Floris G Wouterlood, and Menno P Witter. What does the anatomical organization of the entorhinal cortex tell us? _Neural plasticity_ , 2008(1):381243, 2008. 

- Christopher J Cueva and Xue-Xin Wei. Emergence of grid-like representations by training recurrent neural networks to perform spatial localization. _arXiv preprint arXiv:1803.07770_ , 2018. 

- Christian F Doeller, Caswell Barry, and Neil Burgess. Evidence for grid cells in a human memory network. _Nature_ , 463(7281):657–661, 2010. 

- Yedidyah Dordek, Daniel Soudry, Ron Meir, and Dori Derdikman. Extracting grid cell characteristics from place cell inputs using non-negative principal component analysis. _Elife_ , 5:e10094, 2016. 

- William Dorrell, Peter E Latham, Timothy EJ Behrens, and James CR Whittington. Actionable neural representations: Grid cells from minimal constraints. _arXiv preprint arXiv:2209.15563_ , 2022. 

- Katherine Duncan, Nicholas Ketz, Souheil J Inati, and Lila Davachi. Evidence for area ca1 as a match/mismatch detector: A high-resolution fmri study of the human hippocampus. _Hippocampus_ , 22(3):389–398, 2012. 

11 

- Karl Friston. A theory of cortical responses. _Philosophical transactions of the Royal Society B: Biological sciences_ , 360(1456):815–836, 2005. 

Mark C Fuhs and David S Touretzky. A spin glass model of path integration in rat medial entorhinal cortex. _Journal of Neuroscience_ , 26(16):4266–4276, 2006. 

- Marianne Fyhn, Torkel Hafting, Menno P Witter, Edvard I Moser, and May-Britt Moser. Grid cells in mice. _Hippocampus_ , 18(12):1230–1238, 2008. 

- Tom M George, Kimberly L Stachenfeld, Caswell Barry, Claudia Clopath, and Tomoki Fukai. A generative model of the hippocampal formation trained with theta driven local learning rules. _Advances in Neural Information Processing Systems_ , 36, 2024. 

Lisa M Giocomo, May-Britt Moser, and Edvard I Moser. Computational models of grid cells. _Neuron_ , 71(4):589–603, 2011. 

- Torkel Hafting, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I Moser. Microstructure of a spatial map in the entorhinal cortex. _Nature_ , 436(7052):801–806, 2005. 

- Michael E Hasselmo, Lisa M Giocomo, and Eric A Zilli. Grid cell firing may arise from interference of theta frequency membrane potential oscillations in single neurons. _Hippocampus_ , 17(12): 1252–1271, 2007. 

- RSG Jones and EH B¨uhl. Basket-like interneurones in layer ii of the entorhinal cortex exhibit a powerful nmda-mediated synaptic excitation. _Neuroscience letters_ , 149(1):35–39, 1993. 

- Emilio Kropff and Alessandro Treves. The emergence of grid cells: Intelligent design or just adaptation? _Hippocampus_ , 18(12):1256–1269, 2008. 

- Julija Krupic, Neil Burgess, and John O’Keefe. Neural representations of location composed of spatially periodic bands. _Science_ , 337(6096):853–857, 2012. 

- Shih-pi Ku, Eric L Hargreaves, Sylvia Wirth, and Wendy A Suzuki. The contributions of entorhinal cortex and hippocampus to error driven learning. _Communications biology_ , 4(1):618, 2021. 

- Rosamund F Langston, James A Ainge, Jonathan J Couey, Cathrin B Canto, Tale L Bjerknes, Menno P Witter, Edvard I Moser, and May-Britt Moser. Development of the spatial representation system in the rat. _Science_ , 328(5985):1576–1580, 2010. 

- Timothy P Lillicrap and Adam Santoro. Backpropagation through time and the brain. _Current opinion in neurobiology_ , 55:82–89, 2019. 

- John E Lisman. Relating hippocampal circuitry to function: recall of memory sequences by reciprocal dentate–ca3 interactions. _Neuron_ , 22(2):233–242, 1999. 

- Bruce L McNaughton, Francesco P Battaglia, Ole Jensen, Edvard I Moser, and May-Britt Moser. Path integration and the neural basis of the’cognitive map’. _Nature Reviews Neuroscience_ , 7(8): 663–678, 2006. 

- Beren Millidge, Anil Seth, and Christopher L Buckley. Predictive coding: a theoretical and experimental review. _arXiv preprint arXiv:2107.12979_ , 2021. 

- Beren Millidge, Alexander Tschantz, and Christopher L Buckley. Predictive coding approximates backprop along arbitrary computation graphs. _Neural Computation_ , 34(6):1329–1368, 2022. 

- Beren Millidge, Mufeng Tang, Mahyar Osanlouy, Nicol S Harper, and Rafal Bogacz. Predictive coding networks for temporal prediction. _PLOS Computational Biology_ , 20(4):e1011183, 2024. 

- Zaneta Navratilova, Keith B Godfrey, and Bruce L McNaughton. Grids from bands, or bands from grids? an examination of the effects of single unit contamination on grid cell firing fields. _Journal of neurophysiology_ , 115(2):992–1002, 2016. 

- Samuel A Ocko, Kiah Hardcastle, Lisa M Giocomo, and Surya Ganguli. Emergent elasticity in the neural code for space. _Proceedings of the National Academy of Sciences_ , 115(50):E11798– E11806, 2018. 

12 

John O’Keefe. Place units in the hippocampus of the freely moving rat. _Experimental neurology_ , 51 (1):78–109, 1976. 

- John O’Keefe and Neil Burgess. Dual phase and rate coding in hippocampal place cells: theoretical significance and relationship to entorhinal grid cells. _Hippocampus_ , 15(7):853–866, 2005. 

- Bruno A Olshausen and David J Field. Emergence of simple-cell receptive field properties by learning a sparse code for natural images. _Nature_ , 381(6583):607–609, 1996. 

Ayako Ouchi and Shigeyoshi Fujisawa. Predictive grid coding in the medial entorhinal cortex. _Science_ , 385(6710):776–784, 2024. 

- Luca Pinchetti, Chang Qi, Oleh Lokshyn, Gaspard Olivers, Cornelius Emde, Mufeng Tang, Amine M’Charrak, Simon Frieder, Bayar Menzat, Rafal Bogacz, et al. Benchmarking predictive coding networks–made simple. _arXiv preprint arXiv:2407.01163_ , 2024. 

- Rajesh PN Rao and Dana H Ballard. Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. _Nature neuroscience_ , 2(1):79–87, 1999. URL https://www.nature.com/articles/nn0199_79. 

- Tommaso Salvatori, Yuhang Song, Yujian Hong, Lei Sha, Simon Frieder, Zhenghua Xu, Rafal Bogacz, and Thomas Lukasiewicz. Associative memories via predictive coding. _Advances in Neural Information Processing Systems_ , 34:3874–3886, 2021. 

- Tommaso Salvatori, Luca Pinchetti, Beren Millidge, Yuhang Song, Tianyi Bao, Rafal Bogacz, and Thomas Lukasiewicz. Learning on arbitrary graph topologies via predictive coding. _Advances in neural information processing systems_ , 35:38232–38244, 2022. 

- Terence D. Sanger. Optimal unsupervised learning in a single-layer linear feedforward neural network. _Neural Networks_ , 2(6):459–473, 1989. ISSN 0893-6080. doi: https://doi.org/ 10.1016/0893-6080(89)90044-0. URL https://www.sciencedirect.com/science/ article/pii/0893608089900440. 

- Francesca Sargolini, Marianne Fyhn, Torkel Hafting, Bruce L McNaughton, Menno P Witter, MayBritt Moser, and Edvard I Moser. Conjunctive representation of position, direction, and velocity in entorhinal cortex. _Science_ , 312(5774):758–762, 2006. 

- Rylan Schaeffer, Mikail Khona, and Ila Fiete. No free lunch from deep learning in neuroscience: A case study through models of the entorhinal-hippocampal circuit. _Advances in neural information processing systems_ , 35:16052–16067, 2022. 

- Rylan Schaeffer, Mikail Khona, Tzuhsuan Ma, Cristobal Eyzaguirre, Sanmi Koyejo, and Ila Fiete. Self-supervised learning of representations for space generates multi-modular grid cells. _Advances in Neural Information Processing Systems_ , 36, 2024. 

Mallory A Snow and Jeff Orchard. Biological softmax: Demonstrated in modern hopfield networks. In _Proceedings of the Annual Meeting of the Cognitive Science Society_ , volume 44, 2022. 

- Yuhang Song, Beren Millidge, Tommaso Salvatori, Thomas Lukasiewicz, Zhenghua Xu, and Rafal Bogacz. Inferring neural activity before plasticity as a foundation for learning beyond backpropagation. _Nature neuroscience_ , 27(2):348–358, 2024. 

- Ben Sorscher, Gabriel C Mel, Samuel A Ocko, Lisa M Giocomo, and Surya Ganguli. A unified theory for the computational and mechanistic origins of grid cells. _Neuron_ , 111(1):121–137, 2023. 

- Kimberly L Stachenfeld, Matthew M Botvinick, and Samuel J Gershman. The hippocampus as a predictive map. _Nature neuroscience_ , 20(11):1643–1653, 2017. 

- Mufeng Tang, Tommaso Salvatori, Beren Millidge, Yuhang Song, Thomas Lukasiewicz, and Rafal Bogacz. Recurrent predictive coding models for associative memory employing covariance learning. _PLoS computational biology_ , 19(4):e1010719, 2023. 

13 

Mufeng Tang, Helen Barron, and Rafal Bogacz. Sequential memory with temporal predictive coding. _Advances in Neural Information Processing Systems_ , 36, 2024. 

- Simon Nikolaus Weber and Henning Sprekeler. Learning place cells, grid cells and invariances with excitatory and inhibitory plasticity. _Elife_ , 7:e34560, 2018. 

- James CR Whittington and Rafal Bogacz. An approximation of the error backpropagation algorithm in a predictive coding network with local hebbian synaptic plasticity. _Neural computation_ , 29(5): 1229–1262, 2017. 

- James CR Whittington, Timothy H Muller, Shirley Mark, Guifen Chen, Caswell Barry, Neil Burgess, and Timothy EJ Behrens. The tolman-eichenbaum machine: unifying space and relational memory through generalization in the hippocampal formation. _Cell_ , 183(5):1249–1263, 2020. 

- John Widloski and Ila R Fiete. A model of grid cell development through spatial exploration and spike time-dependent plasticity. _Neuron_ , 83(2):481–495, 2014. 

- Ronald J Williams and Jing Peng. An efficient gradient-based algorithm for on-line training of recurrent network trajectories. _Neural computation_ , 2(4):490–501, 1990. 

- Tom J Wills, Francesca Cacucci, Neil Burgess, and John O’Keefe. Development of the hippocampal cognitive map in preweanling rats. _science_ , 328(5985):1573–1576, 2010. 

- Shawn S Winter, Max L Mehlman, Benjamin J Clark, and Jeffrey S Taube. Passive transport disrupts grid signals in the parahippocampal cortex. _Current Biology_ , 25(19):2493–2502, 2015. 

- Sylvia Wirth, Emin Avsar, Cindy C Chiu, Varun Sharma, Anne C Smith, Emery Brown, and Wendy A Suzuki. Trial outcome and associative learning signals in the monkey hippocampus. _Neuron_ , 61(6):930–940, 2009. 

- Menno P Witter and Edvard I Moser. Spatial representation and the architecture of the entorhinal cortex. _Trends in neurosciences_ , 29(12):671–678, 2006. 

- Michael M Yartsev, Menno P Witter, and Nachum Ulanovsky. Grid cells without theta oscillations in the entorhinal cortex of bats. _Nature_ , 479(7371):103–107, 2011. 

- Eric A Zilli and Michael E Hasselmo. Coupled noisy spiking neurons as velocity-controlled oscillators in a model of grid cell spatial firing. _Journal of Neuroscience_ , 30(41):13850–13860, 2010. 

14 

## A APPENDIX 

A.1 ALGORITHMS 

Below is the training algorithm for a sparse, non-negative PCN given spatial inputs **p** . We obtain the grid cells shown in the main text directly by taking the converged latent activities **g** after training. 

**Algorithm 1** Learning latent representations of space with a PCN 

1: _▷ Training_ 2: **while W** not converged **do** 3: Initialize **g** randomly; 4: Input: **p** 5: **while g** not converged **do** 6: **g** _←_ ReLU( **g** _t_ + ∆ **g** _t_ ) (Eq. 2) 7: **end while** 8: Update **W** (Eqs. 3) 9: **end while** 

Below is the training algorithm for tPCN in path integration tasks. The testing performance and grid cells shown in the main text are obtained by performing a forward pass through the model after training, given an unseen trajectory _{_ **v** _t,_ **p** _t}_ . 

**Algorithm 2** Path integration with tPCN 

|**Alg**|**orithm 2**Path integration with tPCN|||
|---|---|---|---|
|1:|_▷Training_|11:|ˆ**g**_t ←_**g**_t_|
|2:|**while W**out,**W**r,**W**innot converged**do**|12:|**end for**|
|3:|Initializeˆ**g**0randomly or from**p**0via a|13: **end while**||
||PCN;|||
|4:|**for**_t_= 1_, ..., T_ **do**|14: _▷Testing_||
|5:|Input: **p**_t_,ˆ**g**_t−_1and optionally**v**_t_|15: Initialize**g**0randomly or from**p**0via a||
|6:|Initialize**g**_t_ =_f_(**W**rˆ**g**_t−_1)|PCN;||
|7:|**for**_k_ = 1_, ..., K_ **do**|16:<br>**for**_t_= 1_, ..., T_ **do**||
|8:|**g**_t ←_**g**_t_+ ∆**g**_t_(Eq. 5)|17:|Input: **g**_t−_1and optionally**v**_t_|
|9:|**end for**|18:|Obtain**g**_t_, ˆ**p**_t_via Eq. 7|
|10:|Update**W**out,**W**r,**W**in(Eqs. 6)|19: **end for**||



15 

## A.2 DERIVATIONS OF LEARNING DYNAMICS 

Here we derive the recurrent weight update rules for **W** r[RNN] (Equation 12) and **W** r[tPCN] (Equation 13). For RNN, we assume that the weights are updated at each time step and therefore **W** r[RNN] is updated following the chain rule: 

**==> picture [283 x 23] intentionally omitted <==**

We first look at the term _d[d]_ **W[g]** _[t]_ r[, which, following the rule of partial derivatives, can be written as:] 

**==> picture [302 x 101] intentionally omitted <==**

due to the recursive and implicit dependency of **g** _t_ on **g** _t−_ 1 and **g** _t−_ 1 on **W** r[RNN] for all _t_ . Thus, the update rule can be written as: 

**==> picture [274 x 29] intentionally omitted <==**

Since **g** _k_ = _h_ (˜ **g** _k_ ) = _h_ ( **W** r **g** _k−_ 1 + **W** in **v** _k_ ), and _L_ RNN _,t_ = _∥_ **p** _t − f_ ( **W** out **g** _t_ ) _∥_ 2[2][the update rule can] be written as: 

**==> picture [302 x 30] intentionally omitted <==**

concluding our proof for Equation 12. The derivation for **W** in[RNN] is similar: 

**==> picture [286 x 23] intentionally omitted <==**

and 

**==> picture [305 x 101] intentionally omitted <==**

Therefore, the update rule for **W** in in an RNN can be written as: 

**==> picture [297 x 30] intentionally omitted <==**

Finally, the update rule for **W** out[RNN] can be straightforwardly expressed as: 

**==> picture [259 x 66] intentionally omitted <==**

16 

as there is no recursive dependency. 

For tPCN, at each time step _t_ the following loss is minimized with respect to **W** r: 

**==> picture [327 x 13] intentionally omitted <==**

ˆ Since **g** _t−_ 1 is inferred through Equation 5, rather than forward-propagated by **W** r, the recursive dependency on **W** r disappears, and thus the update rule for **W** r can be locally derived as: 

**==> picture [279 x 23] intentionally omitted <==**

If we also assume that the inference dynamics in Equation 5 have converged when the weights are updated, namely: 

**==> picture [276 x 13] intentionally omitted <==**

the update rule can be written as: 

**==> picture [286 x 13] intentionally omitted <==**

which concludes our proof for Equation 13. Similarly, following the same assumption of converged inference and Equation 6, the update rule ∆ **W** in[tPCN] can be written as: 

**==> picture [281 x 12] intentionally omitted <==**

It can be seen that it differs from ∆ **W** in[RNN] only in the absence of the unrolling term _∂[∂]_ **g[g]** _k[t]_[.][On][the] other hand, the update rules ∆ **W** out[RNN] and ∆ **W** out[tPCN] are exactly the same. 

17 

## A.3 EXPERIMENTAL SETUPS AND HYPERPARAMETERS 

**Place cell and trajectory parameters** We use DoS place cell encodings throughout most of our experiments. Formally, the activity of the _i_ th place cell with this encoding, given a particular location _x_ can be written as: 

**==> picture [292 x 56] intentionally omitted <==**

where _Ci_ is the center of the place cell’s firing field, and _τ_ and _ξ_ define the width of the firing field’s center and surround. The table below specifies parameters defining the place cells and trajectories: 

**==> picture [292 x 24] intentionally omitted <==**

Specifically, at time step _t_ = 0, a 2D position and a head direction scalar in [0 _,_ 2 _π_ ] are randomly initialized. At each of the subsequent time steps, a random turn angle is sampled from a normal distribution and a random speed is sampled from a Rayleigh distribution. Both values are then multiplied by _dt_ mentioned in the main text. If the simulated agent hits a border wall at this time step, its speed is slowed and its turn angle is inverted. The position of the agent is updated according to the speed and turn angle at this time step. The trajectories are simulated using parameters adapted from the code provided in Sorscher et al. (2023). 

**Model and training hyperparameters** In our experiments, we have used three models: sparsity and non-negativity constrained PCN, RNN and tPCN. The table below specifies parameters of model architectures: 

|**Model**|_Np_|_Ng_|_h_|_f_|
|---|---|---|---|---|
|sparse,non-neg. PCN|512|256|N/A|N/A|
|tPCN|512|_{_256,512,1024,2048_}_|_{_ReLU_,_tanh_}_|_{_softmax_,_tanh_}_|
|RNN|512|2048|ReLU|softmax|



The table below specifies hyperparameters used in training RNN and tPCN. We use Adam optimizer for all weight updates, and plain SGD for inference dynamics in tPCN. We found that in general, RNNs take more epochs to converge in the path integration task. 

|**Model**|_Nx_|**batch size**|**learning rate**|**inference step size**|**epochs**|**inference iters**|**weight decay**|
|---|---|---|---|---|---|---|---|
|tPCN|50000|500|10_−_4|10_−_2|150|20|10_−_4|
|RNN|50000|500|10_−_4|N/A|200|N/A|10_−_4|



The table below specifies hyperparameters used in training the sparse, non-negative PCN. We use Adam optimizer for all weight updates, and plain SGD for inference dynamics. 

|_Nx_|**batch size**|**learning rate**|**inference step size**|**epochs**|**inference iters**|**weight decay**|_λ_|
|---|---|---|---|---|---|---|---|
|900|100|2_×_10_−_3|10_−_2|600|20|10_−_5|0.05|



**Calculation of grid scores** The following grid score calculation process is adapted from Sargolini et al. (2006) and the code of Sorscher et al. (2023). It is summarized below for completeness and clarity: 

- Get the rate map of latent neurons (potentially hexagonal grid cells); 

- Place one copy of the rate map on top of the other, and start moving the top copy by _δ ∈_ R[2] . If the rate maps are hexagonal grids, for particular _δ_ ’s that make the firing peaks overlap, the autocorrelation between the stationary and moved maps will be 1; otherwise, the autocorrelation will be 0. We will then have a hexagonal autocorrelation map if the rate map itself is hexagonal; 

18 

- We then rotate the autocorrelation map and compute the correlation between each rotated map and the original map. If the rate maps are hexagonal, the correlation as a function of rotated degrees will be sinusoidal, with 60 and 120 degrees as peaks and 30, 90 and 150 degrees as troughs. 

- Grid score is calculated as the minimum difference between the peak and trough correlation, which in theory is a real value in range [ _−_ 2 _,_ 2]. 

All experiments were performed on a single Tesla V100 GPU. 

19 

