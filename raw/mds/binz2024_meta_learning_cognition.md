META-LEARNED MODELS OF COGNITION 

1 

# **Meta-Learned Models of Cognition** 

Marcel Binz[1] , Ishita Dasgupta[2] , Akshay Jagadish[1] , Matthew Botvinick[2] , Jane X. Wang[2] , 

and Eric Schulz[1] 

> 1Max Planck Institute for Biological Cybernetics 

2DeepMind 

## **Author Note** 

Correspondence concerning this article should be addressed to Marcel Binz, MPRG Computational Principles of Intelligence, Max Planck Institute for Biological Cybernetics, Max Planck Ring 8, 72076 Tübingen, Germany. E-mail: marcel.binz@tue.mpg.de 

Marcel Binz https://orcid.org/0000-0001-8872-8386 

META-LEARNED MODELS OF COGNITION 

2 

## **Abstract** 

**Short** : Meta-learning has established itself as a promising tool for building models of human cognition in the recent years. Yet, a coherent research program around meta-learned models of cognition is still missing. The purpose of the present article is to develop such a research program. We accomplish this by pointing out that meta-learning can be used to construct Bayes-optimal learning algorithms, allowing us to draw strong connections to the rational analysis of cognition. We then discuss several advantages of the meta-learning framework over traditional Bayesian methods and reexamine prior work in the context of these new insights. 

**Long** : Meta-learning is a framework for learning learning algorithms through repeated interactions with an environment as opposed to designing them by hand. In recent years, this framework has established itself as a promising tool for building models of human cognition. Yet, a coherent research program around meta-learned models of cognition is still missing. The purpose of this article is to synthesize previous work in this field and establish such a research program. We rely on three key pillars to accomplish this goal. We first point out that meta-learning can be used to construct Bayes-optimal learning algorithms. This result not only implies that any behavioral phenomenon that can be explained by a Bayesian model can also be explained by a meta-learned model but also allows us to draw strong connections to the rational analysis of cognition. We then discuss several advantages of the meta-learning framework over traditional Bayesian methods. In particular, we argue that meta-learning can be applied to situations where Bayesian inference is impossible and that it enables us to make rational models of cognition more realistic, either by incorporating limited computational resources or neuroscientific knowledge. Finally, we reexamine prior studies from psychology and neuroscience that have applied meta-learning and put them into the context of these new insights. In summary, our work highlights that meta-learning considerably extends the scope of rational analysis and thereby of cognitive theories more generally. 

META-LEARNED MODELS OF COGNITION 

3 

_Keywords:_ meta-learning, rational analysis, Bayesian inference, cognitive modeling, 

neural networks 

META-LEARNED MODELS OF COGNITION 

4 

## **Meta-Learned Models of Cognition** 

It is hard to imagine cognitive psychology and neuroscience without computational – models they are invaluable tools to study, analyze, and understand the human mind. Traditionally, such computational models have been hand-designed by expert researchers. In a cognitive architecture, for instance, researchers provide a fixed set of structures and a definition of how these structures interact with each other (Anderson, 2013b). In a Bayesian model of cognition, researchers instead specify a prior and a likelihood function – – which in combination with Bayes’ rule fully determine the model’s behavior (L Griffiths, Kemp, & B Tenenbaum, 2008). The framework of meta-learning (Bengio, Bengio, & Cloutier, 1991; Schmidhuber, 1987; Thrun & Pratt, 1998) offers a radically different approach for constructing computational models by learning them through repeated interactions with an environment instead of requiring an a priori specification from a researcher. 

Recently, psychologists have started to apply meta-learning to the study of human learning (Griffiths et al., 2019). It has been shown that meta-learned models can capture a wide range of empirically observed phenomena that could not be explained otherwise. They, amongst others, reproduce human biases in probabilistic reasoning (Dasgupta, Schulz, Tenenbaum, & Gershman, 2020), discover heuristic decision-making strategies used by people (Binz, Gershman, Schulz, & Endres, 2022), and generalize compositionally on complex language tasks in a human-like manner (Lake, 2019). The goal of the present article is to develop a research program around meta-learned models of cognition and, in doing so, offer a synthesis of previous work and outline new research directions. 

To establish such a research program, we will make use of a recent result from the machine learning community showing that meta-learning can be used to construct Bayes-optimal learning algorithms (Mikulik, Delétang, et al., 2020; Ortega et al., 2019; Rabinowitz, 2019). This correspondence is interesting from a psychological perspective because it allows us to connect meta-learning to another already well-established 

META-LEARNED MODELS OF COGNITION 

5 

framework: the rational analysis of cognition (Anderson, 2013a; Chater & Oaksford, 1999). In a rational analysis, one first has to specify the goal of an agent along with a description of the environment the agent interacts with. The Bayes-optimal solution for the task at hand is then derived based on these assumptions and tested against empirical data. If needed, assumptions are modified and the whole process is repeated. This approach for constructing cognitive models has had a tremendous impact on psychology because it explains “why cognition works, by viewing it as an approximation to ideal statistical inference given the structure of natural tasks and environments” (Tenenbaum, 2021). The observation that meta-learned models can implement Bayesian inference implies that a meta-learned model can be used as a replacement for the corresponding Bayesian model in a rational analysis and thus suggests that any behavioral phenomenon that can be captured by a Bayesian model can also be captured by a meta-learned model. 

We start our article by presenting a simplified version of an argument originally formulated by Ortega et al. (2019) and thereby make their result accessible to a broader audience. Having established that meta-learning produces models that can simulate Bayesian inference, we go on to discuss what additional explanatory power the meta-learning framework offers. After all, why should one not just stick to the tried-and-tested Bayesian approach? We answer this question by providing four original arguments in favor of the meta-learning framework (see Figure 1 for a visual synopsis): 

1. Meta-learning can produce approximately optimal learning algorithms even if exact Bayesian inference is computationally intractable. 

2. Meta-learning can produce approximately optimal learning algorithms even if it is not possible to phrase the corresponding inference problem in the first place. 

3. Meta-learning makes it easy to manipulate a learning algorithm’s complexity and can therefore be used to construct resource-rational models of learning. 

4. Meta-learning allows us to integrate neuroscientific insights into the rational analysis 

META-LEARNED MODELS OF COGNITION 

6 

## **Argument 1** 

## **Argument 2** 

**==> picture [440 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
Possible even if exact Bayesian inference Possible even if it is impossible to phrase<br>is computationally intractable. the corresponding inference problem.<br>p (H) =<br>?<br>p ( D| H) =<br>?<br>**----- End of picture text -----**<br>


## **Argument 3** 

Makes it easy to manipulate a learning algorithm’s complexity. 

**==> picture [213 x 134] intentionally omitted <==**

## **Argument 4** 

**==> picture [213 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
Integrates neuroscientific insights into the<br>rational analysis of cognition.<br>[D] [)]<br>p (H |D ) = [p] [(][H] [,]<br>p ( D )<br>**----- End of picture text -----**<br>


**Figure 1** 

_Visual synopsis of the four different arguments for meta-learning over Bayesian inference put forward in this article._ 

of cognition by incorporating these insights into model architectures. 

The first two points highlight situations in which meta-learned models can be used for rational analysis but traditional Bayesian models cannot. The latter two points provide examples of how meta-learning enables us to make rational models of cognition more realistic, either by incorporating limited computational resources or neuroscientific insights. Taken together, these arguments showcase that meta-learning considerably extends the scope of rational analysis and thereby of cognitive theories more generally. 

META-LEARNED MODELS OF COGNITION 

7 

We will discuss each of these four points in detail and provide illustrations to highlight their relevance. We then reexamine prior studies from psychology and neuroscience that have applied meta-learning and put them into the context of our newly-acquired insights. For each of the reviewed studies, we highlight how it relates to the four presented arguments, and discuss why its findings could not have been obtained using a classical Bayesian model. Following that, we describe under which conditions traditional models are preferable to those obtained by meta-learning. We finish our article by speculating what the future holds for meta-learning. Therein, we focus on how meta-learning could be the key to building a domain-general model of human cognition. 

## **1. Meta-Learned Rationality** 

The prefix _meta_ - is generally used in a self-referential sense: a meta-rule is a rule about rules, a meta-discussion is a discussion about discussions, and so forth. 

Meta-learning, consequently, refers to learning about learning. We, therefore, need to first establish a common definition of _learning_ before covering meta-learning in more detail. For the present article, we adopt the following definition from Mitchell (1997): 

## **Definition: Learning** 

“For a given task, training experience, and performance measure, an algorithm is said to learn if its performance at the task improves with experience.” 

To illustrate this definition, consider the following example which we will return to throughout the text: you are a biologist who has just discovered a new insect species and now set yourself the task of predicting how large members of this species are. You have already observed three exemplars in the wild with lengths of 16cm, 12cm, and 15cm respectively. This data amounts to your training experience. Ideally, you can use this experience to make better predictions about the length of the next individual you encounter. You are said to have learned something if your performance is better after seeing the data than it was before. Typical performance measures for this example problem 

META-LEARNED MODELS OF COGNITION 

8 

include the mean squared error or the (negative) log-likelihood. 

## **1.1. Bayesian Inference for Rational Analyses** 

In a rational analysis of cognition, researchers are trying to compare human behavior to that of an optimal learning algorithm. However, it turns out that no learning algorithm is better than another when averaged over all possible problems (Wolpert, 1996; Wolpert & Macready, 1997), which means that we first have to make additional assumptions about the to-be-solved problem to obtain a well-defined notion of optimality. For our running example, one may make the following – somewhat unrealistic – assumptions: 

1. Each observed insect length _xk_ is sampled from a normal distribution with mean _µ_ and standard deviation _σ_ . 

2. An insect species’ mean length _µ_ cannot be observed directly, but the standard deviation _σ_ is known to be 2cm. 

3. Mean lengths across all insect species are distributed according to a normal distribution with a mean of 10cm and a standard deviation of 3cm. 

An optimal way of making predictions about new observations under such assumptions is specified by Bayesian inference. Bayesian inference requires access to a prior distribution _p_ ( _µ_ ) that defines an agent’s initial beliefs about possible parameter values before observing any data and a likelihood _p_ ( _x_ 1: _t|µ_ ) that captures the agent’s knowledge about how data is generated for a given set of parameters. In our running example, the prior and the likelihood can be identified as follows: 

**==> picture [336 x 53] intentionally omitted <==**

META-LEARNED MODELS OF COGNITION 

9 

where _x_ 1: _t_ = _x_ 1 _, x_ 2 _, . . . , xt_ denotes a sequence of observed insect lengths and the product in Equation 2 arises due to the additional assumption that observations are independent given the parameters. 

The outcome of Bayesian inference is a posterior predictive distribution _p_ ( _xt_ +1 _|x_ 1: _t_ ), which the agent can use to make probabilistic predictions about a hypothetical future observation. To obtain this posterior predictive distribution, the agent first combines prior and likelihood into a posterior distribution over parameters by applying Bayes’ theorem: 

**==> picture [309 x 29] intentionally omitted <==**

In a subsequent step, the agent then averages over all possible parameter values weighted by their posterior probability to get the posterior predictive distribution: 

**==> picture [328 x 23] intentionally omitted <==**

Multiple arguments justify Bayesian inference as a normative procedure, and thereby its use for rational analyses (Corner & Hahn, 2013). This includes dutch book arguments (Lewis, 1999; M. Rescorla, 2020), free energy minimization (Friston, 2010; Hinton & Van Camp, 1993), and performance-based justifications (Aitchison, 1975; Rosenkrantz, 1992). For this article, we are mainly interested in the latter class of – performance-based justifications because these can be used as we will demonstrate later on – to derive meta-learning algorithms that learn approximations to Bayesian inference. 

Performance-based justifications are based on the notion of frequentist statistics. They assert that no learning algorithm can be better than Bayesian inference on a certain performance measure. Particularly relevant for this article is a theorem first proved by Aitchison (1975). It states that the posterior predictive distribution is the distribution (from the set of all possible distributions _Q_ ) that maximizes the log-likelihood of hypothetical future observations when averaged over the data-generating distribution 

META-LEARNED MODELS OF COGNITION 

10 

**==> picture [149 x 13] intentionally omitted <==**

**==> picture [358 x 21] intentionally omitted <==**

Equation 5 implies that if an agent wants to make a prediction about the length of a still unobserved exemplar from a particular insect species and measures its performance using – – the log-likelihood, then averaged across all possible species that can be encountered there is no better way of doing it than using the posterior predictive distribution. We decided to include a short proof of this theorem within Box 1 for the curious reader as it does not appear in popular textbooks on probabilistic machine learning (Bishop, 2006; Murphy, 2012) nor in survey articles on Bayesian models of cognition. Note that, while the theorem itself is central to our later argument, working through its proof is not required to follow the remainder of this article. 

## **1.2. Meta-Learning** 

Having summarized the general concepts behind Bayes-optimal learning, we can now start to describe meta-learning in more detail. Formally speaking, a meta-learning algorithm is defined as any algorithm that “uses its experience to change certain aspects of a learning algorithm, or the learning method itself, such that the modified learner is better than the original learner at learning from additional experience” (Schaul & Schmidhuber, 2010). 

To accomplish this, one first decides on an inner-loop (or base) learning algorithm and determines which of its aspects can be modified. We also refer to these modifiable aspects as meta-parameters. In an outer-loop (or meta-learning) process, the system is then trained on a series of learning problems such that the inner-loop learning algorithm gets better at solving the problems that it encounters. We provide a high-level overview of this framework in Figure 2. 

The previous definition is quite broad and includes a variety of methods. It is, for 

META-LEARNED MODELS OF COGNITION 

11 

**==> picture [468 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
Meta-Learning<br>Learning<br>15cm . . . 16cm = 15.5cm<br>Base Learner p ( xt +1  | x 1: t )<br>22cm . . . 20cm<br>3cm . . . 3cm<br>15cm . . . 16cm<br>Meta-Parameters Performance Measure<br>**----- End of picture text -----**<br>


## **Figure 2** 

_High-level overview of the meta-learning process. A base learner (green rectangle) receives data and performs some internal computations that improve its predictions on future data-points. A meta-learner (blue rectangle) encompasses a set of meta-parameters that can be adapted to create an improved learner. This is accomplished by training the learner on a distribution of related learning problems._ 

example, possible to meta-learn: 

- Hyperparameters for a base learning algorithm, such as learning rates, batch sizes, or the number of training epochs (Doya, 2002; Feurer & Hutter, 2019; Li, Zhou, Chen, & Li, 2017). 

- Initial parameters of a neural network that is trained via stochastic gradient descent (Finn, Abbeel, & Levine, 2017; Nichol, Achiam, & Schulman, 2018). 

- Prior distributions in a probabilistic graphical model (Baxter, 1998; Grant, Finn, Levine, Darrell, & Griffiths, 2018). 

- Entire learning algorithms (Hochreiter, Younger, & Conwell, 2001; Santoro, 

META-LEARNED MODELS OF COGNITION 

12 

Bartunov, Botvinick, Wierstra, & Lillicrap, 2016). 

While all these methods have their own merits, we will be primarily concerned with the latter approach. Learning entire learning algorithms from scratch is arguably the most general and ambitious type of meta-learning, and it is the focus of this article because it is the only one among the aforementioned approaches leading to Bayes-optimal learning algorithms that can be utilized for rational analyses. 

## **1.3. Meta-Learned Inference** 

It may seem like a daunting goal to learn an entire learning algorithm from scratch, but the core idea behind the approach we discuss in the following is surprisingly simple: instead of using Bayesian inference to obtain the posterior predictive distribution, we teach a general-purpose function approximator to do this inference. Previous work has mostly focused on using recurrent neural networks as function approximators in this setting and – – thus we will without loss of generality focus our upcoming exposition on this class of models. 

Like the posterior predictive distribution, the recurrent neural network processes a sequence of observed length from a particular insect species and produces a predictive distribution over the lengths of potential future observations from the same species. More concretely, the meta-learned predictive distribution takes a predetermined functional form whose parameters are given by the network outputs. If we had, for example, decided to use a normal distribution as the functional form of the meta-learned predictive distribution, outputs of the network would correspond to a expected length _mt_ +1 and its standard deviation _st_ +1. Figure 3a illustrates this setup graphically. 

Initially, the recurrent neural network implements a randomly initialized learning algorithm.[1] The goal of the meta-learning process is then to turn this system into an 

> 1 Based on our earlier definition, it is at this point strictly speaking not a learning algorithm at all as it does not improve with additional data. 

META-LEARNED MODELS OF COGNITION 

13 

## **(a) Meta-Learning Setup** 

## **(b) Pseudocode** 

**==> picture [278 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
Forward ( mt +1 , st +1) ∇ Θ  log  q ( xt +1 |x 1: t,  Θ )<br>Backward<br>Θ Θ . . . Θ<br>x 1 x 2 xt<br>**----- End of picture text -----**<br>


initialize **Θ while** not converged **do** _▷_ sample data _µ ∼ p_ ( _µ_ ), _x_ 1: _t_ +1 _∼ p_ ( _x_ 1: _t_ +1 _|µ_ ) _▷_ forward pass _q_ ( _xt_ +1 _|x_ 1: _t,_ **Θ** ) _←_ model( _x_ 1: _t_ ) _▷_ backward pass and update **Θ** _←_ **Θ** + _α∇_ **Θ** log _q_ ( _xt_ +1 _|x_ 1: _t,_ **Θ** ) **end while** 

## **(c) Meta-Learning Loss** 

## **(d) Predictive Distributions** 

**==> picture [473 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
t = 0 t = 10000<br>4.0<br>meta-learned<br>0.6 Bayesian<br>3.5<br>3.0 0.4<br>2.5<br>0.2<br>Bayes-optimal<br>2.0<br>0.0<br>0 5000 10000 0 10 0 10<br>Iteration Insect Length Insect Length<br>Loss<br>Probability Density<br>**----- End of picture text -----**<br>


**Figure 3** 

_Meta-learning illustration. (a) A recurrent neural network processes a sequence of observations and produces a predictive distribution at the final time-step. (b) Pseudocode for a simple meta-learning algorithm. (c) Loss during meta-learning with shaded contours corresponding to the standard deviation across 30 runs. (d) Posterior and meta-learned predictive distributions for an example sequence at beginning and end of meta-learning. The dotted grey line denotes the (unobserved) mean length._ 

improved learning algorithm. The final result is a learning algorithm that is _learned_ or trained rather than specified by a practitioner. To create a learning signal to do this training, we need a performance measure that can be used to optimize the network. Equation 5 suggests a straightforward strategy for designing such a measure by replacing the maximization over all possible distributions with a maximization over meta-parameters 

META-LEARNED MODELS OF COGNITION 

14 

**Θ** (in our case, the weights of the recurrent neural network): 

**==> picture [338 x 53] intentionally omitted <==**

– To turn this expression into a practical meta-learning algorithm, we will as common – practice when training deep neural networks maximize a sample-based version using stochastic gradient ascent: 

**==> picture [338 x 56] intentionally omitted <==**

Figure 3b presents pseudocode for a simple gradient-based procedure that maximizes Equation 7. The entire meta-learning algorithm can be implemented in just around 30 lines of self-contained `PyTorch` code (Paszke et al., 2019). We provide an annotated reference implementation on this article’s accompanying github repository.[2] 

## **1.4. How Good Is a Meta-Learned Algorithm?** 

We have previously shown that the global optimum of Equation 7 is achieved by the posterior predictive distribution. Thus, by maximizing this performance measure, the network is actively encouraged to implement an approximation to exact Bayesian inference. Importantly, after the completion of meta-learning, producing an approximation to the posterior predictive distribution does not require any further updates to the network weights. To perform an inference, we simply have to query the network’s outputs after providing it with a particular sequence of observations. 

If we want to use the fully optimized network for rational analyses, we have to ask 

> 2 `https://github.com/marcelbinz/meta-learned-models` 

META-LEARNED MODELS OF COGNITION 

15 

ourselves: how well does the resulting model approximate Bayesian inference? Two aspects have to be considered when answering this question. First, the network has to be sufficiently expressive to produce the exact posterior predictive distribution for all input sequences. Neural networks of sufficient width are universal function approximators (Hornik, Stinchcombe, & White, 1989), meaning that they can approximate any continuous function to arbitrary precision. Therefore, this aspect is not too problematic for the optimality argument. The second aspect is a bit more intricate: assuming that the network is powerful enough to represent the global optimum of Equation 7, the employed optimization procedure also has to find it. While we are not aware of any theorem that could provide such a guarantee, in practice, it has been observed that meta-learning procedures similar to the one discussed here often lead to networks that closely approximate Bayesian inference (Mikulik, Delétang, et al., 2020; Rabinowitz, 2019). We provide a visualization demonstrating that the predictions of a meta-learned model closely resemble those of exact Bayesian inference for our insect length example in Figure 3c-d. 

While our exposition in this section focused on the supervised learning case, the same ideas can also be readily extended to the reinforcement learning setting (Duan et al., 2016; Wang et al., 2016). Box 2 outlines the general ideas behind the meta-reinforcement learning framework. 

## **1.5. Tool or Theory?** 

It is often not so trivial to separate meta-learning from normal learning. We believe that part of this confusion arises from an underspecification regarding what is being studied. In particular, the meta-learning framework provides opportunities to address two distinct research questions: 

1. It can be used to study how people improve their learning abilities over time. 

2. It can be used as a methodological tool to construct learning algorithms with the properties of interest (and thereafter compare the emerging learning algorithms to 

META-LEARNED MODELS OF COGNITION 

16 

## human behavior). 

Historically, behavioral psychologists have been mainly interested in the former aspect (Doya, 2002; Harlow, 1949). In the 1940s, for example, Harlow (1949) already studied how learning in monkeys improves over time. He found that they adapted their learning strategies after sufficiently many interactions with tasks that shared a common structure, thereby showing a learning-to-learn effect. By now, examples of this phenomenon have – – been found in many different species including humans across nature (Wang, 2021). 

More recently, psychologists have started to view meta-learning as a methodological tool to construct approximations to Bayes-optimal learning algorithms (Binz et al., 2022; Kumar, Dasgupta, Cohen, Daw, & Griffiths, 2020a), and subsequently utilize the resulting algorithms to study human cognition. The key difference from the former approach is that, in this setting, one abstracts away from the process of meta-learning and instead focuses on its outcome. From this perspective, only the fully converged model is of interest. Importantly, this approach allows us to investigate human learning from a rational perspective since we have demonstrated that meta-learning can be used to construct approximations to Bayes-optimal learning. 

We place an emphasis on the second aspect in the present article and advocate for – using fully converged meta-learned algorithms as replacements for the corresponding – Bayesian models for rational analyses of cognition.[3] In the next section, we will outline several arguments that support this approach. However, it is important to mention that we believe that meta-learning can also be a valuable tool to understand the process of learning-to-learn itself. In this context, several intriguing questions arise: at what time scale does meta-learning take place in humans? How much of it is due to task-specific 

> 3 There has been a longstanding conceptual debate in cognitive psychology on whether to view Bayesian models as normative standards or descriptive tools. We believe that this debate is beyond the scope of the current article and thus refer the reader to earlier work for an in-depth discussion (Griffiths, Chater, Norris, & Pouget, 2012; Jones & Love, 2011; Tauber, Navarro, Perfors, & Steyvers, 2017; Zednik & Jäkel, 2016). We only want to add that the framework outlined here is agnostic to this issue – meta-learned models may serve as both normative standards and descriptive tools. 

META-LEARNED MODELS OF COGNITION 

17 

adaptations? How much of it is based on evolutionary or developmental processes? While we agree that these are important questions, they are not the focus of this article. 

## **2. Why Not Bayesian Inference?** 

We have just argued that it is possible to meta-learn Bayes-optimal learning algorithms. What are the implications of this result? If one has access to two different theories that make identical predictions, which of them should be preferred? Bayesian inference has already established itself as a valuable tool for building cognitive models in the recent decades. Thus, the burden of proof is arguably on the meta-learning framework. In this section, we provide four different arguments that highlight the advantages of meta-learning for building models of cognition. Many of these arguments are novel and have not been put forward explicitly in previous literature. The first two arguments highlight situations in which meta-learned models can be used for rational analysis but traditional Bayesian models cannot. The latter two provide examples of how meta-learning enables us to make rational models of cognition more realistic, either by incorporating limited computational resources or neuroscientific insights. 

## **2.1. Intractable Inference** 

## **Argument 1** 

Meta-learning can produce approximately optimal learning algorithms even if exact Bayesian inference is computationally intractable. 

Bayesian inference becomes intractable very quickly because the complexity of computing the normalization constant that appears in the denominator grows exponentially with the number of unobserved parameters. In addition, it is only possible to find a closed-form expression of the posterior distribution for certain combinations of prior and likelihood. In our running example, we assumed that both prior and likelihood follow a normal distribution, which, in turn, leads to a normally-distributed posterior. However, if 

META-LEARNED MODELS OF COGNITION 

18 

one would instead assume that the prior over mean length follows an exponential – distribution which is arguably a more sensible assumption as it enforces lengths to be – positive it becomes already impossible to find an analytical expression for the posterior distribution. 

Researchers across disciplines have recognized these challenges and have, in turn, developed approaches that can approximate Bayesian inference without running into computational difficulties. Prime examples of this are variational inference (Jordan, Ghahramani, Jaakkola, & Saul, 1999) and Markov chain Monte-Carlo (MCMC) methods (Geman & Geman, 1984). In variational inference, one phrases inference as an optimization problem by positing a variational approximation whose parameters are fitted to minimize a divergence measure to the true posterior distribution. MCMC methods, on the other hand, draw samples from a Markov chain that has the posterior distribution as its equilibrium distribution. Previous research in cognitive science indicates that human learning shows characteristics of such approximations (Courville & Daw, 2008; Dasgupta, Schulz, & Gershman, 2017; Daw, Courville, & Dayan, 2008; A. N. Sanborn, Griffiths, & Navarro, 2010; A. N. Sanborn & Silva, 2013). 

Meta-learned inference also never requires an explicit calculation of the exact posterior or posterior predictive distribution. Instead, it performs approximately optimal inference via a single forward pass through the network. Inference, in this case, is approximate because we had to determine a functional form for the predictive distribution. The chosen form may deviate from the true form of the posterior predictive distribution, which, in turn, leads to approximation errors.[4] In some sense, this type of approximation is similar to variational inference: both approaches involve optimization and require one to define a functional form of the respective distribution. However, the optimization process in both approaches uses a different loss function and happens at different time scales. 

> 4 In principle, one could select arbitrarily flexible functional forms, such as mixtures of normal distributions or discretized distributions with small bin sizes, which would reduce the accompanying approximation error. 

META-LEARNED MODELS OF COGNITION 

19 

While variational inference employs the negative evidence lower bound as its loss function, meta-learning directly maximizes for models which can be expected to generalize well to unseen observations (using the performance-based measure from Equation 5). Furthermore, meta-learned inference only involves optimization during the outer-loop meta-learning process but not during the actual learning itself. To update how a meta-learned model makes predictions in the light of new data, we only have to perform a simple forward pass through the network. In contrast to this, standard variational inference requires us to rerun the whole optimization process from scratch every time a new data point is observed.[5] 

In summary, it is possible to meta-learn an approximately Bayes-optimal learning algorithm. If exact Bayesian inference is not tractable, such models are our best option for performing rational analyses. Yet, many other methods for approximate inference, such as variational inference and MCMC methods, also share this feature, and it will thus ultimately be an empirical question which of these approximations provides a better description of human learning. 

## **2.2. Unspecified Problems** 

## **Argument 2** 

Meta-learning can produce optimal learning algorithms even if it is not possible to phrase the corresponding inference problem in the first place. 

Bayesian inference is hard, but posing the correct inference problem can be even harder. What exactly do we mean by that? To perform Bayesian inference, we need to specify a prior and a likelihood. Together, these two objects fully specify the assumed data-generating distribution, and thus the inference problem. Ideally, the specified data-generating distribution should match how the environment actually generates its data. It is fairly straightforward to fulfill this requirement in artificial scenarios, but for many 

> 5 This only holds for standard variational inference but not for more advanced methods that involve amortization such as variational autoencoders (Kingma & Welling, 2013). 

META-LEARNED MODELS OF COGNITION 

20 

real-world problems, it is not. Take for instance our running example: Does the prior over mean length really follow a normal distribution? If yes, what are the mean and variance of this distribution? Are the underlying parameters actually time-invariant or do they, for example, change based on seasons? None of these questions can be answered with certainty. 

In his seminal work on Bayesian decision theory, Savage (1972) made the distinction between small and large world problems. A small world problem is one “in which all relevant alternatives, their consequences, and probabilities are known” (Gigerenzer & Gaissmaier, 2011). A large world problem, on the other hand, is one in which the prior, the likelihood, or both cannot be identified. Savage’s distinction between small and large worlds is relevant for the rational analysis of human cognition as its critics have pointed out that Bayesian inference only provides a justification for optimal reasoning in small world problems (Binmore, 2007) and that “very few problems of interest to the cognitive, behavioral, and social sciences can be said to satisfy [this] condition” (Brighton & Gigerenzer, 2012). 

Identifying the correct set of assumptions becomes especially challenging once we deal with more complex problems. To illustrate this, consider a study conducted by Lucas, Griffiths, Williams, and Kalish (2015) who attempted to construct a Bayesian model of human function learning. Doing so required them to specify a prior over functions that people expect to encounter. Without direct access to such a distribution, they instead opted for a heuristic solution: 98 _._ 8% of functions are expected to be linear, 1 _._ 1% are expected to be quadratic, and 0 _._ 1% are expected to be non-linear. Empirically, this choice led to good results, but it is hard to justify from a rational perspective. We simply do not know the frequency with which these functions appear in the real world, nor whether the given selection fully covers the set of functions expected by participants. 

There are also inference problems in which it is not possible to specify or compute the likelihood function. These problems have been studied extensively in the machine learning community under the names of simulation-based or likelihood-free inference 

META-LEARNED MODELS OF COGNITION 

21 

(Cranmer, Brehmer, & Louppe, 2020; Lueckmann, Boelts, Greenberg, Goncalves, & Macke, 2021). In this setting, it is typically assumed that we can sample data from the likelihood for a given parameter setting but that computing the corresponding likelihood is impossible. Take, for instance, our insect length example. It should be clear that an insect’s length does not only depend on its species’ mean but on many other factors such as climate, genetics, and the individual’s age. Even if all these factors were known, mapping them to a likelihood function does seem close to impossible. But, we can generate samples easily by observing insects in the wild. If we had access large database of insect length measurements for different species, this could be directly used to meta-learn an approximately Bayes-optimal learning algorithm for predicting their length, while circumventing an explicit definition of a likelihood function. 

In cases where we do not have access to a prior or a likelihood, we can neither apply exact Bayesian inference nor approximate inference schemes such as variational inference or MCMC methods. In contrast to this, meta-learned inference does not require us to define the prior or the likelihood explicitly. It only demands samples from the data-generating – distribution to meta-learn an approximately Bayes-optimal learning algorithm a much weaker requirement (Müller, Hollmann, Arango, Grabocka, & Hutter, 2021). The ability to construct Bayes-optimal learning algorithms for large worlds problems is a unique feature of the meta-learning framework, and we believe that it could open up totally new avenues for constructing rational models of human cognition. To highlight one concrete example, it – would be possible to take a collection of real-world decision-making tasks such as the ones presented by Czerlinski, Gigerenzer, Goldstein, et al. (1999) – and use them to obtain a meta-learned agent that is adapted to the decision-making problems that people actually encounter in their everyday lives. This algorithm could then serve as a normative standard against which we can compare human decision-making. 

META-LEARNED MODELS OF COGNITION 

22 

## **2.3. Resource Rationality** 

## **Argument 3** 

Meta-learning makes it easy to manipulate a learning algorithm’s complexity and can therefore be used to construct resource-rational models of learning. 

Bayesian inference has been successfully applied to model human behavior across a number of domains, including perception (Knill & Richards, 1996), motor control (Körding & Wolpert, 2004), everyday judgments (Griffiths & Tenenbaum, 2006), and logical reasoning (Oaksford, Chater, et al., 2007). Notwithstanding these success stories, there are also well-documented deviations from the notion of optimality prescribed by Bayesian inference. People, for example, underreact to prior information (Kahneman & Tversky, 1973), ignore evidence (Benjamin, 2019), and rely on heuristic decision-making strategies (Gigerenzer & Gaissmaier, 2011). 

– The intractability of Bayesian inference together with empirically observed – deviations from it has led researchers to conjecture that people only attempt to approximate Bayesian inference. Many different notions of what constitutes a computational resource have been suggested, such as memory (Dasgupta & Gershman, 2021), thinking time (Ratcliff & McKoon, 2008), or physical effort (Hoppe & Rothkopf, 2016). 

Cover (1999) put forward a dichotomy that will be useful for our following discussion. He refers to the algorithmic complexity of an algorithm as the number of bits needed to _implement_ it. In contrast, he refers to the computational complexity of an algorithm as the space, time, or effort required to _execute_ it. It is possible to cast many approximate inference schemes as resource-rational algorithms (A. N. Sanborn, 2017). The resulting models typically consider some form of computational complexity. In MCMC methods, computational complexity can be measured in terms of the number of drawn samples: drawing fewer samples leads to faster inference at the cost of introducing a bias (Courville & Daw, 2008; A. N. Sanborn et al., 2010). In variational inference, on the other 

META-LEARNED MODELS OF COGNITION 

23 

hand, it is possible to introduce an additional parameter that allows to trade-off performance against the computational complexity of transforming the prior into the posterior distribution (Binz & Schulz, 2022b; Ortega, Braun, Dyer, Kim, & Tishby, 2015). Likewise, other frameworks for building resource-rational models, such as rational meta-reasoning (Lieder & Griffiths, 2017), also only target computational complexity. 

The prevalence of resource-rational models based on computational complexity is likely due to the fact that building similar models based on algorithmic complexity is much harder. Measuring algorithmic complexity historically relies on the notion of Kolmogorov complexity, which is the size of the shortest computer program that produces a particular data sequence (Chaitin, 1969; Kolmogorov, 1965; Solomonoff, 1964). Kolmogorov complexity is in general uncomputable, and, therefore, of limited practical interest.[6] 

Meta-learning provides us with a straightforward way to manipulate both algorithmic and computational complexity in a common framework by adapting the size of the underlying neural network model. Limiting the complexity of network weights places a constraint on algorithmic complexity (as reducing the number of weights decreases the amount of bits needed to store them, and hence also the amount of bits needed to store the learning algorithm). Limiting the complexity of activations, on the other hand, places a constraint on computational complexity (reducing the number of hidden units, for example, decreases the memory needed for executing the meta-learned model). 

Previously, both forms of complexity constraints have been realized in meta-learned models. Dasgupta et al. (2020) decreased the number of hidden units of a meta-learned inference algorithm, effectively reducing its computational complexity. In contrast, Binz et al. (2022) placed a constraint on the description length of neural network weights, which implements a form of algorithmic complexity. To the best of our knowledge, no other class 

> 6 Having said that, it is possible to approximate it under certain circumstances and different authors have applied such approximations to study both human and animal cognition (Chater & Vitányi, 2003; Gauvrit, Zenil, Delahaye, & Soler-Toscano, 2014; Gauvrit, Zenil, & Tegnér, 2017; Griffiths, Daniels, Austerweil, & Tenenbaum, 2018; Zenil, Marshall, & Tegnér, 2015). 

META-LEARNED MODELS OF COGNITION 

24 

of resource-rational models exists that allows us to take both algorithmic and computational complexity into account, making this ability a unique feature of the meta-learning framework. 

## **2.4. Neuroscience** 

## **Argument 4** 

Meta-learning allows us to integrate neuroscientific insights into the rational analysis of cognition by incorporating these insights into model architectures. 

In addition to providing a framework for understanding many aspects of behavior, meta-learning offers a powerful lens through which to view brain structure and function. For instance, Wang et al. (2018) presented observations supporting the hypothesis that prefrontal circuits may constitute a meta-reinforcement learning system. From a computational perspective, meta-learning strives to learn a faster inner-loop learning algorithm via an adjustment of neural network weights in a slower outer-loop learning process. Within the brain, an analogous process plausibly occurs when slow, 

dopamine-driven synaptic change gives rise to reinforcement learning processes that occur within the activity dynamics of the prefrontal network, allowing for adaptation on much faster timescales. This perspective recontextualized the role of dopamine function in reward-based learning and was able to account for a range of previously puzzling neuroscientific findings. To highlight one example, Bromberg-Martin, Matsumoto, Hong, and Hikosaka (2010) found that dopamine signaling reflected updates in not only _experienced_ but also _inferred_ values of targets. Notably, a meta-reinforcement learning agent trained on the same task also recovered this pattern. Having a mapping of meta-reinforcement learning components onto existing brain regions furthermore allows us to apply experimental manipulations that directly perturb neural activity, for example by using optogenetic techniques. Wang et al. (2018) used this idea to modify their original meta-reinforcement learning architecture to mimic the blocking or enhancement of 

META-LEARNED MODELS OF COGNITION 

25 

dopaminergic reward prediction error signals, in direct analogy with optogenetic stimulation delivered to rats performing a two-armed bandit task (Stopper, Maric, Montes, Wiedman, & Floresco, 2014). 

Importantly, the direction of exchange can also work in the other direction, with neuroscientific findings constraining and inspiring new forms of meta-learning architectures. Bellec, Salaj, Subramoney, Legenstein, and Maass (2018), for example, showed that recurrent networks of spiking neurons are able to display convincing learning-to-learn behavior, including in the realm of reinforcement learning. Episodic meta-reinforcement learning (Ritter et al., 2018) architectures are also heavily inspired by neuroscientific accounts of complementary learning systems in the brain (McClelland, McNaughton, & O’Reilly, 1995). Both of these examples demonstrate that meta-learning can be used to build more biologically plausible learning algorithms, and thereby highlight that it can act as a bridge between Marr’s computational and implementational level (Marr, 2010). 

Finally, the meta-learning perspective not only allows us to connect machine learning and neuroscience via architectural design choices but also via the kinds of tasks that are of interest. Dobs, Martinez, Kell, and Kanwisher (2022), for instance, suggested that functional specialization in neural circuits, which has been widely observed in biological brains, arises spontaneously as a consequence of task demands. In particular, they found that convolutional neural networks trained on both face and object recognition depicted emergent segregation on the basis of these tasks. Likewise, G. R. Yang, Joglekar, Song, Newsome, and Wang (2019) found that training a single recurrent neural network to perform a wide range of cognitive tasks yielded units that were clustered along different functional cognitive processes. Put another way, it seems plausible that functional specialization emerges by training neural networks on multiple tasks. While this has not been tested so far, we speculate that this also holds in the meta-learning setting, as it involves training on multiple tasks by design. If this were true, we could look at the emerging areas inside a meta-learned model, and use the resulting insights to generate 

META-LEARNED MODELS OF COGNITION 

26 

novel predictions about the processes happening in individual brain areas (Kanwisher, Khosla, & Dobs, 2023). 

## **3. Previous Research** 

Meta-learned models are already starting to transform the cognitive sciences today. They allow us to model things that are hard to capture with traditional models such as compositional generalization, language understanding, and model-based reasoning. In this section, we provide an overview of what has been achieved with the help of meta-learning in previous work. We arranged this review into various thematic subcategories. For each of them, we summarize which key findings have been obtained by meta-learning and discuss why these results would have been difficult to obtain using traditional models of learning by appealing to the insights from the previous section. 

## **3.1. Heuristics and Cognitive Biases** 

Meta-learning has been previously used to discover algorithms with a limited computational budget that show human-like cognitive biases as we have already alluded to earlier. Dasgupta et al. (2020) trained a neural network on a distribution of probabilistic inference problems while controlling for the number of its hidden units. They found that – – their model when restricted to just a single hidden unit captured many biases in human reasoning, including a conservatism bias and base rate neglect. Likewise, Binz et al. (2022) trained a neural network on a distribution of decision-making problems while controlling for the number of bits needed to represent the network. Their model discovered two previously suggested heuristics in specific environments and made precise prognoses about when these heuristics should be applied. In particular, knowing the correct ranking of features led to one reason decision-making, knowing the directions of features led to an equal weighting heuristic, and not knowing about either of them led to strategies that use weighted combinations of features (also see Figure 4a-b). 

META-LEARNED MODELS OF COGNITION 

27 

## **(a)** 

**==> picture [468 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
Model Simulations Model Fit (Posterior Probabilities)<br>0.75 single cue Guessing 1<br>Ideal Observer<br>Equal Weighting<br>Single Cue<br>Strategy Selection<br>Feedforward Network<br>0.00 0<br>equal weighting<br>Participant<br>(b)<br>Model Simulations Model Fit (Posterior Probabilities)<br>0.75 single cue Guessing 1<br>Ideal Observer<br>Equal Weighting<br>Single Cue<br>Strategy Selection<br>Feedforward Network<br>0.00 0<br>equal weighting<br>Participant<br>Gini coefficients<br>Gini coefficients<br>**----- End of picture text -----**<br>


## **(c)** 

**==> picture [462 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
Model-Free Model-Based Meta-Learned<br>common rare common rare common rare<br>1.0 1.0 1.0<br>Start<br>0.5 0.5 0.5<br>Planet Y Planet X<br>0.0 0.0 0.0<br>rY rX<br>Rewarded Unrewarded Rewarded Unrewarded Rewarded Unrewarded<br>Stay Probability<br>**----- End of picture text -----**<br>


**Figure 4** 

_Example results obtained using meta-learned models. (a) In a paired comparison task, a meta-learned model identified a single-cue heuristic as the resource-rational solution when information about the feature ranking was available. Follow-up experiments revealed that people indeed apply this heuristic under the given circumstances. (b) If information about feature directions was available, the same meta-learned model identified an equal weighting heuristic as the resource-rational solution. People also applied this heuristic in the given context (Binz et al., 2022). (c) Wang et al. (2016) showed that meta-learned models can exhibit model-based learning characteristics in the two-step task (Daw, Gershman, Seymour, Dayan, & Dolan, 2011) even when they were purely trained through model-free approaches. The plots on the right illustrate the probability of repeating the previous action for different agents (model-free, model-based, meta-learned) after a common or uncommon transition and after a received or omitted reward._ 

In both of these studies, meta-learned models offered a novel perspective on results that were previously viewed as contradictory. This was in part possible because 

META-LEARNED MODELS OF COGNITION 

28 

meta-learning enabled us to easily manipulate the complexity of the underlying learning algorithm. While doing so is, at least in theory, also possible within the Bayesian framework, no Bayesian model that captures the full set of findings from Dasgupta et al. (2020) and Binz et al. (2022) has been discovered so far. We hypothesize that this could be because traditional rational process models struggle to capture that human strategy selection is context-dependent even before receiving any direct feedback signal (Mercier & Sperber, 2017). The meta-learned models of Dasgupta et al. (2020) and Binz et al. (2022), on the other hand, were able to readily show context-specific biases when trained on an appropriate task distribution. 

## **3.2. Language Understanding** 

Meta-learning may also help us to answer questions regarding how people process, understand, and produce language. Whether the inductive biases needed to acquire a language are learned from experience or are inherited is one of these questions (Y. Yang & Piantadosi, 2022). McCoy, Grant, Smolensky, Griffiths, and Linzen (2020) investigated how to equip a model with a set of linguistic inductive biases that are relevant to human cognition. Their solution to this problem builds upon the idea of model-agnostic meta-learning (Finn et al., 2017). In particular, they meta-learned the initial weights of a neural network such that the network can adapt itself quickly to new languages using standard gradient-based learning. When being trained on a distribution over languages, these initial weights can be interpreted as universal factors that are shared across all languages. They showed that this approach identifies inductive biases (e.g. a bias for treating certain phonemes as vowels) that are useful for acquiring a language’s syllable structure. While their work focused on various modeling aspects, they suggested that their framework “could [ _. . ._ ] be used to empirically investigate the effects that those inductive biases have.” They additionally argued that a Bayesian modeling approach would only be able to consider a restrictive set of inductive biases as it needs to commit to a particular 

META-LEARNED MODELS OF COGNITION 

29 

representation and inference algorithm. In contrast, the meta-learning framework made it easy to implement the intended inductive biases by simply manipulating the distribution of encountered languages. 

The ability to compose simple elements into complex entities is at the heart of human language. The property of languages to “make infinite use of finite means” (Chomsky, 2014) is what allows us to make strong generalizations from limited data. For example, people readily understand what it means to “dax twice” or to “dax slowly” after learning about the meaning of the verb “dax.” How to build models with a similar proficiency, however, remains an open research question. Lake (2019) showed that a transformer-like neural network can be trained to make such compositional generalizations through meta-learning. Importantly, during meta-learning, his models were adapted to problems that required compositional generalization, and could thereby acquire the skills needed to solve entirely new problems. Lake (2019) argued that meta-learning “has implications for understanding how people generalize compositionally.” In particular, it highlights the importance of “tackling a series of changing learning problems rather than iterating through a static data-set”, as it is done in traditional neural network training schemes. 

## **3.3. Inductive Biases** 

Human cognition comes with many useful inductive biases beyond the ability to reason compositionally. The preference for simplicity is one of these biases (Chater & Vitányi, 2003; Feldman, 2016). We readily extract abstract low-dimensional rules that allow us to generalize entirely new situations. Meta-learning is an ideal tool to build models with similar preferences because we can easily generate tasks based on simple rules and use them for meta-learning, thereby enabling an agent to acquire the desired inductive bias from data. 

Towards this end, Kumar, Dasgupta, Cohen, Daw, and Griffiths (2020b) tested 

META-LEARNED MODELS OF COGNITION 

30 

humans and meta-reinforcement agents on a family of structured tasks generated by a grammar and compared their performance to those trained on a non-structured version of the same task with matched statistics. They expanded these results to a larger suite of tasks generated from simple abstract rules in Kumar, Dasgupta, et al. (2022). Humans found it easier to learn in structured tasks, confirming that they have strong priors towards simple abstract rules (Schulz, Tenenbaum, Duvenaud, Speekenbrink, & Gershman, 2017). However, their analysis also indicated that meta-learning is easier on non-structured tasks than on structured tasks. In follow-up work, they found that this result also holds for agents that were trained purely on the structured version of their task but evaluated on – both versions (Kumar, Correa, et al., 2022) a quite astonishing finding considering that one would expect an agent to perform better on the task distribution it was trained on. The authors addressed this mismatch between humans and meta-learned agents by guiding agents during training to reproduce natural language descriptions that people provided to describe a given task. They found that grounding meta-learned agents in natural language descriptions not only improved their performance but also led to more human-like inductive biases, demonstrating that natural language can serve as a source for abstractions within human cognition. 

Their line of work utilizes another interesting technique for training meta-learning agents (Kumar, Correa, et al., 2022; Kumar, Dasgupta, et al., 2022). It does not rely on a hand-designed task distribution but instead involves sampling tasks from the prior distribution of human participants using a technique known as Gibbs sampling with people (Harrison et al., 2020; A. Sanborn & Griffiths, 2007). While doing so provides them with a data-set of tasks, no expression of the corresponding prior distribution over them is accessible and, hence, it is non-trivial to define a Bayesian model for the given setting. A meta-learned agent, on the other hand, was readily obtained by training on the collected samples. 

META-LEARNED MODELS OF COGNITION 

31 

## **3.4. Model-Based Reasoning** 

Many realistic scenarios afford two distinct types of learning: model-free and model-based. Model-free learning algorithms directly adjust their strategies using observed outcomes. Model-based learning algorithms, on the other hand, learn about the transition and reward probabilities of an environment, which are then used for downstream reasoning tasks. People are generally thought to be able to perform model-based learning, at least to some extent, and assuming that the problem at hand calls for it (Daw et al., 2011; Kool, Cushman, & Gershman, 2016). Wang et al. (2016) showed that a meta-learned algorithm can display model-based behavior, even if it was trained through a pure model-free reinforcement learning algorithm (see Figure 4c). 

Having a model of the world also acts as the basis for causal reasoning. Traditionally, making causal inferences relies on the notion of Pearl’s do-calculus (Pearl, 2009). Dasgupta et al. (2019), however, showed that meta-learning can be used to create models that draw causal inferences from observational data, select informative interventions, and make counterfactual predictions. While they have not related their model to human data directly, it could in future work serve as the basis to study how people make causal judgments in complex domains and explain why and when they deviate from normative causal theories (Bramley, Dayan, Griffiths, & Lagnado, 2017; Gerstenberg, Goodman, Lagnado, & Tenenbaum, 2021). 

Together, these two examples highlight that model-based reasoning capabilities can emerge internally in a meta-learned model if they are beneficial for solving the encountered problem. While there are already many traditional models that can perform such tasks, these models are often slow at run-time as they typically involve Bayesian inference, planning, or both. Meta-learning, on the other hand, “shifts most of the compute burden from inference time to training time [which] is advantageous when training time is ample but fast answers are needed at run-time” (Dasgupta et al., 2019), and may therefore explain how people can perform such intricate computations within a reasonable time-frame. 

META-LEARNED MODELS OF COGNITION 

32 

While model-based reasoning is an emerging property of meta-learned models, it may also be integrated explicitly into such models should it be desired. Jensen, Hennequin, and Mattar (2023) have taken this route, and augmented a standard meta-reinforcement learning agent with the ability to perform temporally extended planning using imagined rollouts. In each time-step, their agent can decide to perform a planning operation instead of directly interacting with the environment (in this case, a spatial navigation task). Their meta-learned agents opted to perform this planning operation consistently after training. Importantly, the model showed striking similarities to patterns of human deliberation by performing more planning early on and with an increased distance to the goal. 

Furthermore, they found that patterns of hippocampal replays resembled the rollouts of their model. 

## **3.5. Exploration** 

People do not only have to integrate observed information into their existing knowledge, but they also have to actively determine what information to sample. They constantly face situations that require them to decide whether they should explore something new or whether they should rather exploit what they already know. Previous research suggests that people solve this exploration-exploitation dilemma using a combination of directed and random exploration strategies (Gershman, 2018; Schulz & Gershman, 2019; Wilson, Geana, White, Ludvig, & Cohen, 2014; Wu, Schulz, Speekenbrink, Nelson, & Meder, 2018). Why do people use these particular strategies and not others? Binz and Schulz (2022a) hypothesized that they do so because human exploration follows resource-rational principles. To test this claim, they devised a family of resource-rational reinforcement learning algorithms by combining ideas from meta-learning and information theory. Their meta-learned model discovered a diverse set of exploration strategies, including random and directed exploration, that captured human exploration better than alternative approaches. In this domain, meta-learning offered a direct path 

META-LEARNED MODELS OF COGNITION 

33 

towards investigating the hypothesis that people try to explore optimally but are subject to limited computational resources, whereas designing hand-crafted models for studying the same question would have been more intricate. 

It is not only important to decide how to explore, but also to decide whether exploration is worthwhile in the first place. Lange and Sprekeler (2020) studied this question using the meta-learning framework. Their meta-learned agents are able to flexibly interpolate between implementing exploratory learning behaviors and hard-coded, non-learning strategies. Importantly, which behavior was realized crucially depended on environmental properties, such as the diversity of the task distribution, the task complexity, and the agent’s lifetime. They showed, for instance, that agents with a short lifetime should opt for small rewards that are easy to find, while agents with an extended lifetime should spend their time exploring the environment. The study of Lange and Sprekeler (2020) clearly demonstrates that meta-learning makes it conceptually easy to iterate over different environmental assumptions inside a rational analysis of cognition. They only had to modify the environment as desired, followed by rerunning their meta-learning procedure. In contrast, traditional modeling approaches would require hand-designing a new optimal agent each time an environmental change occurs. 

## **3.6. Cognitive Control** 

Humans are remarkable at adapting to task-specific demands. The processes behind this ability are collectively referred to as cognitive control (Botvinick, Braver, Barch, Carter, & Cohen, 2001). Cohen (2017) even argues that “the capacity for cognitive control is perhaps the most distinguishing characteristic of human behavior.” It should therefore come as no surprise that cognitive control has received a significant amount of attention from a computational perspective (Botvinick & Cohen, 2014; Collins & Frank, 2013). Recently, some of these computational investigations have been extended to the meta-learning framework. 

META-LEARNED MODELS OF COGNITION 

34 

The ability to adjust computational resources as needed is one hallmark of cognitive control. Moskovitz, Miller, Sahani, and Botvinick (2022) proposed a meta-learned model – with such characteristics. Their model learns a simple default policy similar to the model – of Binz and Schulz (2022a) that can be overwritten by a more complex one if necessary. They demonstrate that this model is not only able to capture behavioral phenomena from the cognitive control literature but also known effects in decision-making and reinforcement learning tasks, thereby linking the three domains. Importantly, their study highlights that the meta-learning framework offers the means to account for multiple computational costs – instead of just a single one in this case, a cost for implementing the default policy and one for deviating from it. 

Taking contextual cues into consideration is another vital aspect of cognitive control. Dubey, Grant, Luo, Narasimhan, and Griffiths (2020) implemented this idea in the meta-learning framework. In their model, contextual cues determine the initialization of a task-specific neural network that is then trained using model-agnostic meta-learning. They showed that such a model captures “the context-sensitivity of human behavior in a simple but well-studied cognitive control task.” Furthermore, they demonstrated that it scales well to more complex domains (including tasks from the MuJoCo (Todorov, Erez, & Tassa, 2012), CelebA Liu, Luo, Wang, and Tang (2015) and MetaWorld (Yu et al., 2020) benchmarks), thereby opening up new opportunities for modeling human behavior in naturalistic scenarios. 

## **4. Why Is Not Everything Meta-Learned?** 

We have laid out different arguments that make meta-learning a useful tool for constructing cognitive models, but it is important to note that we do not claim that meta-learning is the ultimate solution to every modeling problem. Instead, it is essential to understand when meta-learning is the right tool for the job and when not. 

META-LEARNED MODELS OF COGNITION 

35 

## **4.1. Lack of Interpretability** 

Perhaps its most significant detriment is that meta-learning never provides us with analytical solutions that we can inspect, analyze and reason about. In contrast to this, some Bayesian models have analytical solutions. Take as an example the data-generating distribution that we encountered earlier (Equations 1-2). For these assumptions, a closed-form expression of the posterior predictive distribution is available. By looking at this closed-form expression, researchers have generated new predictions and subsequently tested them empirically (Daw et al., 2008; Dayan & Kakade, 2000; Gershman, 2015). Performing the same kind of analysis with a meta-learned model is not as straightforward. We do not have access to an underlying mathematical expression, which makes a structured exploration of theories much harder. 

That being said, there are still ways to analyze a meta-learned model’s behavior. For one, it is possible to use model architectures that facilitate interpretability. Binz et al. (2022) relied on this approach and designed a neural network architecture that produced weights of a probit regression model which were then used to cluster applied strategies into different categories. Doing so enabled them to identify which strategy was used by their meta-learned model in a particular situation. 

Recently, researchers have also started to use tools from cognitive psychology to analyze the behavior of black-box models (Rich & Gureckis, 2019; Ritter, Barrett, Santoro, & Botvinick, 2017; Schulz & Dayan, 2020). For example, it is possible to treat such models just like participants in a psychological experiment and use the collected data to analyze their behavior similar to how psychologists would analyze human behavior (Binz & Schulz, 2023; Dasgupta et al., 2022; Rahwan et al., 2019; Schramowski, Turan, Andersen, Rothkopf, & Kersting, 2022). We believe that this approach has great potential for analyzing increasingly capable and opaque artificial agents, including those obtained via meta-learning. 

META-LEARNED MODELS OF COGNITION 

36 

## **4.2. Intricate Training Processes** 

When using the meta-learning framework, one also has to deal with the fact that training neural networks is complex and takes time. Neural network models contain many moving parts, like weight initializations or the used optimizer, that have to be chosen appropriately such that training can take off in the first place, and training itself may take hours or days until it is finished. When we want to modify assumptions in the data-generating distribution, we have to retrain the whole system from scratch altogether. Thus, although the process of iterating over different environmental assumptions is conceptually straightforward in the meta-learning framework, it may be time-consuming. Bayesian models can, in comparison, sometimes be more quickly adapted to changes in environmental assumptions. To illustrate this, let us assume that you wanted to explain human behavior through a meta-learned model that was trained on the data-generating distribution from Equations 1-2, but found that the resulting model does not fit the observed data well. Next, you want to consider the alternative hypothesis that people assume a non-stationary environment. While this modification could be done quickly in the corresponding Bayesian model, the meta-learning framework requires retraining on newly generated data. 

There is, furthermore, no guarantee that a fully converged meta-learned model actually implements a Bayes-optimal learning algorithm. While we were able to compare to analytical solutions for simple cases like our insect length example, it is in general impossible to verify that a meta-learned algorithm is optimal. Indeed, there are reported cases in which meta-learning failed to find the Bayes-optimal solution (Wang et al., 2021). We believe that this issue can be somewhat mitigated by validating meta-learned models in various different ways. But, ultimately future work should come up with techniques to verify meta-learned models. 

META-LEARNED MODELS OF COGNITION 

37 

## **4.3. Meta-Learned or Bayesian Inference?** 

— – In summary, both frameworks meta-learning and Bayesian inference have their unique strengths and weaknesses. The meta-learning framework does and will not replace Bayesian inference but complement it. It broadens our available toolkit and enables researchers to study questions that were previously out of reach. However, there are certainly situations in which traditional Bayesian inference is a more appropriate modeling choice as we have outlined in this section. 

## **5. The Role of Neural Networks** 

Most of the points we have discussed so far are agnostic regarding the function approximator implementing the meta-learned algorithm. However, at the same time, we have appealed to neural networks at various points throughout the text. When one looks at prior work, it can also be observed that neural networks are the predominant model class in the meta-learning setting. Why is that the case? In addition to their universality, neural networks offer one big opportunity: they provide a flexible framework for engineering different types of inductive biases into a computational model (Goyal & Bengio, 2022). In the following section, we will highlight three examples of how previous work has accomplished this. For each of these examples, we take a concept from psychology, and show how it can be readily accommodated in a meta-learned model. 

Perhaps one of the most persuasive idea in cognitive modeling is that of – gradient-based learning. It is not only at the heart of one of the most influential models – the Rescorla-Wagner model (Gershman, 2015; R. A. Rescorla, 1972) but also features prominently in many other theories of human learning, such as connectionist models (Rumelhart, McClelland, Group, et al., 1988). Even though the earlier outlined meta-learning procedure relies on gradient-based learning in the outer loop, the resulting inner-loop dynamics must bear no resemblance to gradient descent. However, it is possible to construct meta-learned models whose inner-loop updates rely on gradient-based 

META-LEARNED MODELS OF COGNITION 

38 

learning. Finn et al. (2017) proposed a meta-learning technique known as model-agnostic meta-learning that finds optimal initial parameters of a feedforward neural network that is subsequently trained via gradient descent. The idea is that these optimal initial parameters allow the feedforward network to generalize to multiple tasks in a minimal number of gradient steps. While their general setup is similar to the one we discussed, it leads to models that learn via gradient descent instead of models that implement a learning algorithm inside the dynamics of a recurrent neural network. Kirsch and Schmidhuber (2021) recently brought these two approaches together into a single model. Their proposed architecture consists of multiple recurrent neural networks that interact with each other. Importantly, they showed that one particular configuration of these networks could implement backpropagation in the forward pass, thereby being able to perform gradient-based learning in a memory-based system. 

– – Exemplar-based models like the generalized category model (Nosofsky, 2011) are one of the most prominent approaches for modeling how people categorize items into different classes (Kruschke, 1990; Shepard, 1987). They categorize a new instance based on the estimated similarity between that instance and previously seen examples. Recently, meta-learned models with exemplar-based reasoning abilities have been proposed for the task of few-shot classification, in which a classifier must generalize based on a training set containing only a few examples. Matching networks (Vinyals, Blundell, Lillicrap, Wierstra, et al., 2016) accomplish this by classifying a new data-point using a similarity-weighted combination of categories in the training set. Importantly, similarity is computed over a learned embedding space, thereby ensuring that the model can scale to high-dimensional stimuli. Follow-up work has taken inspiration from another hugely influential model of human category learning and replaced the exemplar-based mechanism used in matching networks with one based on category prototypes (Snell, Swersky, & Zemel, 2017). 

Finally, making inferences using similarities to previous experiences is not only useful for supervised learning but also in the reinforcement learning setting. In the 

META-LEARNED MODELS OF COGNITION 

39 

reinforcement learning literature, the ability to store and recollect states or trajectories for later use is studied under the name of episodic memory (Lengyel & Dayan, 2007). It has been argued that episodic memory could be the key to explaining human performance in naturalistic environments (Gershman & Daw, 2017). Episodic memory also plays a crucial role in neuroscience, with studies showing that highly rewarding instances are stored in the hippocampus and made available for recall as and when required Blundell et al. (2016). Ritter et al. (2018) build upon the neural episodic control idea from Pritzel et al. (2017) and utilize a differential neural dictionary for episodic recall in the context of 

meta-learning. Their dictionary stores encodings from previously experienced tasks, which can then be later queried as needed. With this addition, their meta-learned model is able to recall previously discovered policies, retrieve memories using category examples, handle compositional tasks, re-instate memories while traversing the environment, and recover a learning strategy people use in a neuroscience-inspired task. 

In summary, human cognition comes with a variety of inductive biases and neural networks provide flexible ways to easily incorporate them into meta-learned models of cognition. We have outlined three such examples in the section, demonstrating how to integrate gradient-based learning, exemplar- and prototype-based reasoning, and episodic memory into a meta-learned model. There are, furthermore, many other inductive biases for neural network architectures that could be utilized in the context of meta-learning but have not been yet. Examples include networks that perform differentiable planning (Farquhar, Rocktäschel, Igl, & Whiteson, 2017; Tamar, Wu, Thomas, Levine, & Abbeel, 2016), extract object-based representations (Piloto, Weinstein, Battaglia, & Botvinick, 2022; Sancaktar, Blaes, & Martius, 2022), or modify their own connections through synaptic plasticity (Miconi, Rawal, Clune, & Stanley, 2020; Schlag, Irie, & Schmidhuber, 2021). 

META-LEARNED MODELS OF COGNITION 

40 

## **6. Towards a Domain-General Model of Human Learning** 

What does the future hold for meta-learning? The current generation of meta-learned models of cognition is almost exclusively trained on the data-generating distribution of a specific problem family. While this training process enables them to generalize to new tasks inside this problem family, they are unlikely to generalize to completely different domains. We would, for example, not expect a meta-learned algorithm to perform a challenging maze navigation task if it was only trained to predict the lengths of insect species. 

While domain-specific models have (and will continue to) provide answers to important research questions, we agree with Newell (1992) that “unified theories of cognition are the only way to bring this wonderful, increasing fund of knowledge under intellectual control.” Ideally, such a unified theory should manifest itself in a 

domain-general cognitive model that cannot only solve prediction tasks but is also capable of human-like decision-making (Gigerenzer & Gaissmaier, 2011), category learning (Ashby, Maddox, et al., 2005), navigation (Montello, 2005), problem-solving (Newell, Simon, et al., 1972) and so on. We consider the meta-learning framework the ideal tool for accomplishing this goal as it allows us to compile arbitrary assumptions about an agent’s beliefs of the world (arguments 1 and 2) and its computational architecture (arguments 3 and 4) into a cognitive model. 

To obtain such a domain-general cognitive model via meta-learning, however, a few challenges need to be tackled. First of all, there is the looming question of how a data-generating distribution that contains many different problems should be constructed. Here, we may take inspiration from the machine learning community, where researchers have devised generalist agents by training neural networks on a large set of problems (Reed et al., 2022). (A. A. Team et al., 2023) have recently shown that this is a promising path for scaling up meta-learning models. They trained a meta-reinforcement learning agent on a vast open-ended world with over 10[40] possible tasks. The resulting agent can adapt to 

META-LEARNED MODELS OF COGNITION 

41 

held-out problems as quickly as humans, and “displays on-the-fly hypothesis-driven exploration, efficient exploitation of acquired knowledge, and can successfully be prompted with first-person demonstrations.” In the same vein, we may come up with a large collection of tasks that are more commonly used to study human behavior (Miconi, 2023; Molano-Mazon et al., 2022; G. R. Yang et al., 2019), and use them to train a meta-learned model of cognition. 

Language will likely play an important role in future meta-learning systems. We do not want a system that learns every task from scratch via trial and error but one that can be provided with a set of instructions similar to how a human subject would be instructed in a psychological experiment. Having agents capable of language will not only enable them to understand new tasks in a zero-shot manner but may also facilitate their cognitive abilities. It, for example, allows them to decompose tasks into sub-tasks, learn from other agents, or generate explanations (Colas, Karch, Moulin-Frier, & Oudeyer, 2022). 

Fortunately, our current best language models (Brown et al., 2020; Chowdhery et al., 2022) and meta-learning systems are both based on neural networks. Thus, integrating language – – capabilities into a meta-learned model of cognition should at least conceptually be fairly straightforward. Doing so would furthermore enable such models to harvest the compositional nature of language to make strong generalizations to tasks outside of the meta-learning distribution. The potential for this was highlighted in a recent study of (Riveland & Pouget, 2022) which found that language-conditioned recurrent neural network models can perform entirely novel psychophysical tasks with high accuracy. 

Moreover, a sufficiently general model of human cognition must not only be able to select amongst several given options, like in a decision-making or category learning setting, but it also needs to maneuver within a complex world. For this, it needs to perceive and process high-dimensional visual stimuli, it needs to control a body with many degrees of freedom, and it needs to actively engage with other agents. Many of these problems have been at the heart of the deep learning community (Hill et al., 2020; McClelland, Hill, 

META-LEARNED MODELS OF COGNITION 

42 

Rudolph, Baldridge, & Schütze, 2020; Strouse, McKee, Botvinick, Hughes, & Everett, 2021; O. E. L. Team et al., 2021), and it will be interesting to see whether the solutions developed there can be integrated into a meta-learned model of cognition. 

Finally, there are also some challenges on the algorithmic side that need to be taken into account. In particular, it is unclear how far currently used model architectures and outer-loop learning algorithms scale. While contemporary meta-learning algorithms are able to find approximately Bayes-optimal solutions to simple problems, they sometimes struggle to do so on more complex ones (e.g. as in the earlier discussed work of Wang et al. (2021)). Therefore, it seems likely that simply increasing the complexity of the – meta-learning distribution will not be sufficient we will also need model architectures and outer-loop learning algorithms that can handle increasingly complex data-generating distributions. The transformer architecture (Vaswani et al., 2017), which has been very successful at training large language models (Brown et al., 2020; Chowdhery et al., 2022), provides one promising candidate, but there could be countless other (so far undiscovered) alternatives. 

Thus, taken together, there are still substantial challenges involved in creating a domain-general meta-learned model of cognition. In particular, we have argued in this section that we need to (1) meta-learn on more diverse task distributions, (2) develop agents that can parse instructions in form of natural language, (3) embody these agents in realistic problem settings, and (4) find model architectures that scale to these complex problems. Figure 5 summarizes these points graphically. 

## **7. Conclusion** 

Most computational models of human learning are hand-designed, meaning that at some point a researcher sat down and defined how they behave. Meta-learning starts with an entirely different premise. Instead of designing learning algorithms by hand, one trains a system to achieve its goals by repeatedly letting it interact with an environment. While 

META-LEARNED MODELS OF COGNITION 

43 

**==> picture [468 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
Meta-Learning<br>Learning<br>Find as many apples as possible.<br>Base Learner π ( at | ht )<br>15cm . . . 16cm<br>Meta-Parameters Performance Measure<br>**----- End of picture text -----**<br>


**Figure 5** 

_Illustration of how a domain-general meta-learned model of cognition could look like. Modifications include training on more diverse task distributions, providing natural language instructions as additional inputs, and relying on scalable model architectures._ 

this seems quite different from traditional models of learning on the surface, we have highlighted that the meta-learning framework actually has a deep connection to the idea of Bayesian inference, and thereby to the rational analysis of cognition. Using this connection as a starting point, we have highlighted several advantages of the meta-learning framework for constructing rational models of cognition. Together, our arguments demonstrate that meta-learning cannot only be applied in situations where Bayesian inference is impossible but also facilitates the inclusion of computational constraints and neuroscientific insights into rational models of human cognition. Earlier criticisms of the rational analysis of cognition have repeatedly pointed out that “rational Bayesian models are significantly unconstrained” and that they should be “developed in conjunction with mechanistic considerations to offer substantive explanations of cognition” (Jones & Love, 2011). We believe that the meta-learning framework provides the ideal opportunity to do so as it 

META-LEARNED MODELS OF COGNITION 

44 

allows for a painless integration of flexible computational mechanisms. 

It is worth pointing out that meta-learning can be also motivated by taking neural networks as a starting point. From this perspective, it bridges two of the most popular – – theories of cognition Bayesian models and connectionism by bringing the scalability of neural network models into the rational analysis of cognition. We, therefore, believe that meta-learning provides a powerful tool to scale up psychological theories to more complex settings. However, at the same time, meta-learning has not delivered on this promise yet. Existing meta-learned models of cognition are typically applied to classical scenarios where established models already exist. Thus, we have to ask: what prevents the application to more complex and general paradigms? First, such paradigms themselves have to be developed. Fortunately, there is currently a trend toward measuring human behavior on more naturalistic tasks (Brändle, Stocks, Tenenbaum, Gershman, & Schulz, 2022; Brändle, Binz, & Schulz, 2022; Schulz et al., 2019), and it will be interesting to see what role meta-learning will play in modeling behavior in such settings. Furthermore, meta-learning can be intricate and time-consuming. We hope that the present article – together with the – accompanying code examples makes this technique less opaque and more accessible to a wider audience. Future advances in hardware will likely make the meta-learning process quicker and we are therefore hopeful that meta-learning can ultimately fulfill its promise of identifying plausible models of human cognition in situations that are out of reach for hand-designed algorithms. 

META-LEARNED MODELS OF COGNITION 

45 

## **Acknowledgements** 

The authors would like to thank Sreejan Kumar, Tobias Ludwig, Dominik Endres, and 

Adam Santoro for their valuable feedback on an earlier draft. 

## **Funding statement** 

This work was funded by the Max Planck Society, the Volkswagen Foundation, as well as the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy–EXC2064/1–390727645. 

## **of Interest statement** 

The author(s) declare none. 

META-LEARNED MODELS OF COGNITION 

46 

**Box 1.** We proof that the posterior predictive distribution _p_ ( _xt_ +1 _|x_ 1: _t_ ) maximizes the loglikelihood of future observations averaged over the data-generating distribution: 

**==> picture [342 x 19] intentionally omitted <==**

The essence of this proof is to show that the posterior predictive distribution is superior to any other reference distribution _r_ ( _xt_ +1 _|x_ 1: _t_ ) in terms of log-likelihood: 

**==> picture [250 x 13] intentionally omitted <==**

or equivalently that: 

**==> picture [146 x 27] intentionally omitted <==**

Proofing this conjecture is straight-forward (Aitchison, 1975): 

**==> picture [278 x 333] intentionally omitted <==**

definition of expectation 

change order of summation 

Bayes’ rule 

factor out _p_ ( _x_ 1: _t_ ) 

change order of summation 

factor out log-term 

Equation 4 

definition of KL divergence ■ 

Note that while we used sums in our proof, thereby assuming that relevant quantities take discrete values, the same ideas can be readily applied to continuous-valued quantities by replacing sums with integrals. 

META-LEARNED MODELS OF COGNITION 

47 

**Box 2.** The main text has focused on tasks in which an agent receives direct feedback about which response would have been correct. In the real world, however, people do not always receive such explicit feedback. They, instead, often have to deal with partial information – taking the form of rewards, utilities, or costs – that merely informs them about the quality of their response. 

Problems that fall into this category are often modeled as Markov decision processes (MDPs). In an MDP, an agent repeatedly interacts with an environment. In each time-step, it observes the state of the environment _st_ and can take an action _at_ that leads to a reward signal _rt_ sampled from a reward distribution _p_ ( _rt|st, at, µr_ ). Executing an action furthermore influences the environment state at the next time-step according to a transition distribution _p_ ( _st_ +1 _|st, at, µs_ ). 

The goal of a Bayes-optimal reinforcement learning agent is to find a policy, which is a mapping from a history of observations _ht_ = _s_ 1 _, a_ 1 _, r_ 1 _, . . . , st−_ 1 _, at−_ 1 _, rt−_ 1 _, st_ to a probability distribution over actions _π[∗]_ ( _at|ht_ ), that maximizes the total amount of obtained rewards across a finite horizon _H_ averaged over all problems that may be encountered: 

**==> picture [388 x 32] intentionally omitted <==**

MDPs with unknown reward and transition distributions are substantially more challenging to solve optimally compared to supervised problems as there is no teacher informing the agent about which actions are right or wrong. Instead, the agent has to figure out the most rewarding course of action solely through trial and error. Finding an analytical solution to Equation 9 is extremely challenging and indeed only possible for a few special cases (Duff, 2003; Gittins, 1979), which made it historically near impossible to investigate such problems within the framework of rational analysis. 

Even though finding an analytical expression of the Bayes-optimal policy is often impossible, it is straightforward to meta-learn an approximation to it (Duan et al., 2016; Wang et al., 2016). The general concept is almost identical to the supervised learning case: parameterize the to-be-learned policy with a recurrent neural network and replace the maximization over the set of all possible policies from Equation 9 with a sample-based approximation that maximizes over neural network parameters. The resulting problem can then be solved using any standard deep reinforcement learning algorithm. 

Like in the supervised learning case, the resulting recurrent neural network implements a free-standing reinforcement learning algorithm after meta-learning is completed. Learning is once again implemented via a simple forward pass through the network, i.e., by conditioning the model on an additional data-point. The meta-learned reinforcement learning algorithm approximates the Bayes-optimal policy under the same conditions as in the supervised learning case: a sufficiently expressive model and an optimization procedure that is able to find the global optimum. 

META-LEARNED MODELS OF COGNITION 

48 

## 8. References 

Aitchison, J. (1975). Goodness of prediction fit. _Biometrika_ , _62_ (3), 547–554. Anderson, J. R. (2013a). _The adaptive character of thought_ . Psychology Press. Anderson, J. R. (2013b). _The architecture of cognition_ . Psychology Press. 

- Ashby, F. G., Maddox, W. T., et al. (2005). Human category learning. _Annual review of psychology_ , _56_ (1), 149–178. 

- Baxter, J. (1998). Theoretical models of learning to learn. In _Learning to learn_ (pp. 71–94). Springer. 

- Bellec, G., Salaj, D., Subramoney, A., Legenstein, R., & Maass, W. (2018). Long short-term memory and learning-to-learn in networks of spiking neurons. _Advances in neural information processing systems_ , _31_ . 

- Bengio, Y., Bengio, S., & Cloutier, J. (1991). Learning a synaptic learning rule. In _Ijcnn-91-seattle international joint conference on neural networks_ (Vol. 2, pp. 969–vol). 

- Benjamin, D. J. (2019). Errors in probabilistic reasoning and judgment biases. _Handbook of Behavioral Economics: Applications and Foundations 1_ , _2_ , 69–186. 

- Binmore, K. (2007). Rational decisions in large worlds. _Annales d’Economie et de Statistique_ , 25–41. 

- Binz, M., Gershman, S. J., Schulz, E., & Endres, D. (2022). Heuristics from bounded meta-learned inference. _Psychological review_ . 

- Binz, M., & Schulz, E. (2022a). Modeling human exploration through resource-rational reinforcement learning. In A. H. Oh, A. Agarwal, D. Belgrave, & K. Cho (Eds.), _Advances in neural information processing systems._ Retrieved from `https://openreview.net/forum?id=W1MUJv5zaXP` 

- Binz, M., & Schulz, E. (2022b). Reconstructing the einstellung effect. _Computational Brain & Behavior_ , 1–17. 

- Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand gpt-3. 

META-LEARNED MODELS OF COGNITION 

49 

_Proceedings of the National Academy of Sciences_ , _120_ (6), e2218523120. 

Bishop, C. M. (2006). _Pattern recognition and machine learning_ . springer. 

- Blundell, C., Uria, B., Pritzel, A., Li, Y., Ruderman, A., Leibo, J. Z., . . . Hassabis, D. (2016). Model-free episodic control. _arXiv preprint arXiv:1606.04460_ . 

- Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. _Psychological review_ , _108_ (3), 624. 

- Botvinick, M. M., & Cohen, J. D. (2014). The computational and neural basis of cognitive control: charted territory and new frontiers. _Cognitive science_ , _38_ (6), 1249–1285. 

- Bramley, N. R., Dayan, P., Griffiths, T. L., & Lagnado, D. A. (2017). Formalizing neurath’s ship: Approximate algorithms for online causal learning. _Psychological review_ , _124_ (3), 301. 

- Brändle, F., Stocks, L. J., Tenenbaum, J. B., Gershman, S. J., & Schulz, E. (2022). Intrinsically motivated exploration as empowerment. _PsyArXiv. January_ , _14_ . 

- Brighton, H., & Gigerenzer, G. (2012). Are rational actor models “rational” outside small worlds. _Evolution and Rationality: Decisions, Co-operation, and Strategic Behavior_ , 84–109. 

- Bromberg-Martin, E. S., Matsumoto, M., Hong, S., & Hikosaka, O. (2010). A 

   - pallidus-habenula-dopamine pathway signals inferred stimulus values. _Journal of neurophysiology_ , _104_ (2), 1068–1076. 

- Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., . . . others (2020). Language models are few-shot learners. _Advances in neural information processing systems_ , _33_ , 1877–1901. 

- Brändle, F., Binz, M., & Schulz, E. (2022). Exploration beyond bandits. In 

   - I. Cogliati Dezza, E. Schulz, & C. M. Wu (Eds.), _The drive for knowledge: The science of human information seeking_ (p. 147–168). Cambridge University Press. doi: 10.1017/9781009026949.008 

- Chaitin, G. J. (1969). On the simplicity and speed of programs for computing infinite sets 

META-LEARNED MODELS OF COGNITION 

50 

   - of natural numbers. _Journal of the ACM (JACM)_ , _16_ (3), 407–422. 

- Chater, N., & Oaksford, M. (1999). Ten years of the rational analysis of cognition. _Trends in cognitive sciences_ , _3_ (2), 57–65. 

- Chater, N., & Vitányi, P. (2003). Simplicity: A unifying principle in cognitive science? _Trends in cognitive sciences_ , _7_ (1), 19–22. 

- Chomsky, N. (2014). _Aspects of the theory of syntax_ (Vol. 11). MIT press. 

- Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A., . . . others (2022). Palm: Scaling language modeling with pathways. _arXiv preprint arXiv:2204.02311_ . 

- Cohen, J. D. (2017). Cognitive control: Core constructs and current considerations. _The Wiley handbook of cognitive control_ , 1–28. 

- Colas, C., Karch, T., Moulin-Frier, C., & Oudeyer, P.-Y. (2022). Language and culture internalization for human-like autotelic ai. _Nature Machine Intelligence_ , _4_ (12), 1068–1076. 

- Collins, A. G., & Frank, M. J. (2013). Cognitive control over learning: creating, clustering, and generalizing task-set structure. _Psychological review_ , _120_ (1), 190. 

- Corner, A., & Hahn, U. (2013). Normative theories of argumentation: are some norms better than others? _Synthese_ , _190_ (16), 3579–3610. 

- Courville, A. C., & Daw, N. D. (2008). The rat as particle filter. In _Advances in neural information processing systems_ (pp. 369–376). 

- Cover, T. M. (1999). _Elements of information theory_ . John Wiley & Sons. 

- Cranmer, K., Brehmer, J., & Louppe, G. (2020). The frontier of simulation-based 

   - inference. _Proceedings of the National Academy of Sciences_ , _117_ (48), 30055–30062. 

- Czerlinski, J., Gigerenzer, G., Goldstein, D. G., et al. (1999). How good are simple heuristics. _Simple heuristics that make us smart_ , 97–118. 

- Dasgupta, I., & Gershman, S. J. (2021). Memory as a computational resource. _Trends in Cognitive Sciences_ , _25_ (3), 240–251. 

META-LEARNED MODELS OF COGNITION 

51 

- Dasgupta, I., Lampinen, A. K., Chan, S. C., Creswell, A., Kumaran, D., McClelland, J. L., & Hill, F. (2022). Language models show human-like content effects on reasoning. _arXiv preprint arXiv:2207.07051_ . 

- Dasgupta, I., Schulz, E., & Gershman, S. J. (2017). Where do hypotheses come from? _Cognitive psychology_ , _96_ , 1–25. 

- Dasgupta, I., Schulz, E., Tenenbaum, J. B., & Gershman, S. J. (2020). A theory of learning to infer. _Psychological review_ , _127_ (3), 412. 

- Dasgupta, I., Wang, J., Chiappa, S., Mitrovic, J., Ortega, P., Raposo, D., . . . 

   - Kurth-Nelson, Z. (2019). Causal reasoning from meta-reinforcement learning. _arXiv preprint arXiv:1901.08162_ . 

- Daw, N. D., Courville, A. C., & Dayan, P. (2008). Semi-rational models of conditioning: The case of trial order. _The probabilistic mind_ , 431–452. 

- Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans’ choices and striatal prediction errors. _Neuron_ , _69_ (6), 1204–1215. 

- Dayan, P., & Kakade, S. (2000). Explaining away in weight space. _Advances in neural information processing systems_ , _13_ . 

- Dobs, K., Martinez, J., Kell, A. J., & Kanwisher, N. (2022). Brain-like functional specialization emerges spontaneously in deep neural networks. _Science advances_ , _8_ (11), eabl8913. 

- Doya, K. (2002). Metalearning and neuromodulation. _Neural networks_ , _15_ (4-6), 495–506. 

- Duan, Y., Schulman, J., Chen, X., Bartlett, P. L., Sutskever, I., & Abbeel, P. (2016). Rl[2] : Fast reinforcement learning via slow reinforcement learning. _arXiv preprint arXiv:1611.02779_ . 

- Dubey, R., Grant, E., Luo, M., Narasimhan, K., & Griffiths, T. (2020). Connecting context-specific adaptation in humans to meta-learning. _arXiv preprint arXiv:2011.13782_ . 

META-LEARNED MODELS OF COGNITION 

52 

- Duff, M. O. (2003). Optimal learning: Computational procedures for bayes-adaptive markov decision processes. 

- Farquhar, G., Rocktäschel, T., Igl, M., & Whiteson, S. (2017). Treeqn and atreec: Differentiable tree-structured models for deep reinforcement learning. _arXiv preprint arXiv:1710.11417_ . 

- Feldman, J. (2016). The simplicity principle in perception and cognition. _Wiley Interdisciplinary Reviews: Cognitive Science_ , _7_ (5), 330–340. 

- Feurer, M., & Hutter, F. (2019). Hyperparameter optimization. In _Automated machine learning_ (pp. 3–33). Springer, Cham. 

- Finn, C., Abbeel, P., & Levine, S. (2017). Model-agnostic meta-learning for fast adaptation of deep networks. In _International conference on machine learning_ (pp. 1126–1135). 

- Friston, K. (2010). The free-energy principle: a unified brain theory? _Nature reviews neuroscience_ , _11_ (2), 127–138. 

- Gauvrit, N., Zenil, H., Delahaye, J.-P., & Soler-Toscano, F. (2014). Algorithmic complexity for short binary strings applied to psychology: a primer. _Behavior research methods_ , _46_ (3), 732–744. 

- Gauvrit, N., Zenil, H., & Tegnér, J. (2017). The information-theoretic and algorithmic approach to human, animal, and artificial cognition. In _Representation and reality in humans, other living organisms and intelligent machines_ (pp. 117–139). Springer. 

- Geman, S., & Geman, D. (1984). Stochastic relaxation, gibbs distributions, and the bayesian restoration of images. _IEEE Transactions on pattern analysis and machine intelligence_ (6), 721–741. 

- Gershman, S. J. (2015). A unifying probabilistic view of associative learning. _PLoS computational biology_ , _11_ (11), e1004567. 

- Gershman, S. J. (2018). Deconstructing the human algorithms for exploration. _Cognition_ , _173_ , 34–42. 

- Gershman, S. J., & Daw, N. D. (2017). Reinforcement learning and episodic memory in 

META-LEARNED MODELS OF COGNITION 

53 

humans and animals: an integrative framework. _Annual review of psychology_ , _68_ , 101. 

- Gerstenberg, T., Goodman, N. D., Lagnado, D. A., & Tenenbaum, J. B. (2021). A counterfactual simulation model of causal judgments for physical events. _Psychological review_ , _128_ (5), 936. 

- Gigerenzer, G., & Gaissmaier, W. (2011). Heuristic decision making. _Annual review of psychology_ , _62_ , 451–482. 

- Gittins, J. C. (1979). Bandit processes and dynamic allocation indices. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 148–177. 

- Goyal, A., & Bengio, Y. (2022). Inductive biases for deep learning of higher-level cognition. _Proceedings of the Royal Society A_ , _478_ (2266), 20210068. 

- Grant, E., Finn, C., Levine, S., Darrell, T., & Griffiths, T. (2018). Recasting 

   - gradient-based meta-learning as hierarchical bayes. In _6th international conference on learning representations, iclr 2018._ 

- Griffiths, T. L., Callaway, F., Chang, M. B., Grant, E., Krueger, P. M., & Lieder, F. (2019). Doing more with less: meta-reasoning and meta-learning in humans and machines. _Current Opinion in Behavioral Sciences_ , _29_ , 24–30. 

- Griffiths, T. L., Chater, N., Norris, D., & Pouget, A. (2012). How the bayesians got their beliefs (and what those beliefs actually are): comment on bowers and davis (2012). 

- Griffiths, T. L., Daniels, D., Austerweil, J. L., & Tenenbaum, J. B. (2018). Subjective randomness as statistical inference. _Cognitive psychology_ , _103_ , 85–109. 

- Griffiths, T. L., & Tenenbaum, J. B. (2006). Optimal predictions in everyday cognition. _Psychological science_ , _17_ (9), 767–773. 

- Harlow, H. F. (1949). The formation of learning sets. _Psychological review_ , _56_ (1), 51. 

- Harrison, P., Marjieh, R., Adolfi, F., van Rijn, P., Anglada-Tort, M., Tchernichovski, O., . . . Jacoby, N. (2020). Gibbs sampling with people. _Advances in Neural Information Processing Systems_ , _33_ , 10659–10671. 

META-LEARNED MODELS OF COGNITION 

54 

- Hill, F., Lampinen, A., Schneider, R., Clark, S., Botvinick, M., McClelland, J. L., & Santoro, A. (2020). Environmental drivers of systematicity and generalization in a situated agent. In _International conference on learning representations._ Retrieved from `https://openreview.net/forum?id=SklGryBtwr` 

- Hinton, G. E., & Van Camp, D. (1993). Keeping the neural networks simple by minimizing the description length of the weights. In _Proceedings of the sixth annual conference on computational learning theory_ (pp. 5–13). 

- Hochreiter, S., Younger, A. S., & Conwell, P. R. (2001). Learning to learn using gradient descent. In _International conference on artificial neural networks_ (pp. 87–94). 

- Hoppe, D., & Rothkopf, C. A. (2016). Learning rational temporal eye movement strategies. _Proceedings of the National Academy of Sciences_ , _113_ (29), 8332–8337. 

- Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. _Neural networks_ , _2_ (5), 359–366. 

- Jensen, K. T., Hennequin, G., & Mattar, M. G. (2023). A recurrent network model of planning explains hippocampal replay and human behavior. _bioRxiv_ , 2023–01. 

- Jones, M., & Love, B. C. (2011). Bayesian fundamentalism or enlightenment? on the explanatory status and theoretical contributions of bayesian models of cognition. _Behavioral and brain sciences_ , _34_ (4), 169. 

- Jordan, M. I., Ghahramani, Z., Jaakkola, T. S., & Saul, L. K. (1999). An introduction to variational methods for graphical models. _Machine learning_ , _37_ (2), 183–233. 

- Kahneman, D., & Tversky, A. (1973). On the psychology of prediction. _Psychological review_ , _80_ (4), 237. 

- Kanwisher, N., Khosla, M., & Dobs, K. (2023). Using artificial neural networks to ask ‘why’questions of minds and brains. _Trends in Neurosciences_ . 

- Kingma, D. P., & Welling, M. (2013). Auto-encoding variational bayes. _arXiv preprint arXiv:1312.6114_ . 

- Kirsch, L., & Schmidhuber, J. (2021). Meta learning backpropagation and improving it. 

META-LEARNED MODELS OF COGNITION 

55 

_Advances in Neural Information Processing Systems_ , _34_ . 

- Knill, D. C., & Richards, W. (1996). _Perception as bayesian inference_ . Cambridge University Press. 

- Kolmogorov, A. N. (1965). Three approaches to the quantitative definition ofinformation’. _Problems of information transmission_ , _1_ (1), 1–7. 

- Kool, W., Cushman, F. A., & Gershman, S. J. (2016). When does model-based control pay off? _PLoS computational biology_ , _12_ (8), e1005090. 

- Körding, K. P., & Wolpert, D. M. (2004). Bayesian integration in sensorimotor learning. _Nature_ , _427_ (6971), 244–247. 

- Kruschke, J. (1990). Alcove: A connectionist model of human category learning. _Advances in Neural Information Processing Systems_ , _3_ . 

- Kumar, S., Correa, C. G., Dasgupta, I., Marjieh, R., Hu, M., Hawkins, R. D., . . . Griffiths, T. L. (2022). Using natural language and program abstractions to instill human inductive biases in machines. In A. H. Oh, A. Agarwal, D. Belgrave, & K. Cho 

   - (Eds.), _Advances in neural information processing systems._ Retrieved from `https://openreview.net/forum?id=buXZ7nIqiwE` 

- Kumar, S., Dasgupta, I., Cohen, J., Daw, N., & Griffiths, T. (2020b). Meta-learning of structured task distributions in humans and machines. In _International conference on learning representations._ 

- Kumar, S., Dasgupta, I., Cohen, J. D., Daw, N. D., & Griffiths, T. L. (2020a). Meta-learning of structured task distributions in humans and machines. _arXiv preprint arXiv:2010.02317_ . 

- Kumar, S., Dasgupta, I., Marjieh, R., Daw, N. D., Cohen, J. D., & Griffiths, T. L. (2022). Disentangling abstraction from statistical pattern matching in human and machine learning. _arXiv preprint arXiv:2204.01437_ . 

- Lake, B. M. (2019). Compositional generalization through meta sequence-to-sequence 

   - learning. _Advances in Neural Information Processing Systems_ , _32_ , 9791–9801. 

META-LEARNED MODELS OF COGNITION 

56 

- Lange, R. T., & Sprekeler, H. (2020). Learning not to learn: Nature versus nurture in silico. _arXiv preprint arXiv:2010.04466_ . 

- Lengyel, M., & Dayan, P. (2007). Hippocampal contributions to control: the third way. _Advances in neural information processing systems_ , _20_ . 

- Lewis, D. (1999). Why conditionalize? In _Papers in metaphysics and epistemology_ (Vol. 2, p. 403–407). Cambridge University Press. doi: 10.1017/CBO9780511625343.024 

- L Griffiths, T., Kemp, C., & B Tenenbaum, J. (2008). Bayesian models of cognition. 

- Li, Z., Zhou, F., Chen, F., & Li, H. (2017). Meta-sgd: Learning to learn quickly for few-shot learning. _arXiv preprint arXiv:1707.09835_ . 

- Lieder, F., & Griffiths, T. L. (2017). Strategy selection as rational metareasoning. _Psychological review_ , _124_ (6), 762. 

- Liu, Z., Luo, P., Wang, X., & Tang, X. (2015, December). Deep learning face attributes in the wild. In _Proceedings of international conference on computer vision (iccv)._ 

- Lucas, C. G., Griffiths, T. L., Williams, J. J., & Kalish, M. L. (2015). A rational model of function learning. _Psychonomic bulletin & review_ , _22_ (5), 1193–1215. 

- Lueckmann, J.-M., Boelts, J., Greenberg, D., Goncalves, P., & Macke, J. (2021). Benchmarking simulation-based inference. In _International conference on artificial intelligence and statistics_ (pp. 343–351). 

- Marr, D. (2010). _Vision: A computational investigation into the human representation and processing of visual information_ . MIT press. 

- McClelland, J. L., Hill, F., Rudolph, M., Baldridge, J., & Schütze, H. (2020). Placing language in an integrated understanding system: Next steps toward human-level performance in neural language models. _Proceedings of the National Academy of Sciences_ , _117_ (42), 25966–25974. 

- McClelland, J. L., McNaughton, B. L., & O’Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. 

META-LEARNED MODELS OF COGNITION 

57 

_Psychological review_ , _102_ (3), 419. 

- McCoy, R. T., Grant, E., Smolensky, P., Griffiths, T. L., & Linzen, T. (2020). Universal linguistic inductive biases via meta-learning. _arXiv preprint arXiv:2006.16324_ . 

- Mercier, H., & Sperber, D. (2017). _The enigma of reason_ . Harvard University Press. 

- Miconi, T. (2023). A large parametrized space of meta-reinforcement learning tasks. _arXiv preprint arXiv:2302.05583_ . 

- Miconi, T., Rawal, A., Clune, J., & Stanley, K. O. (2020). Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity. _arXiv preprint arXiv:2002.10585_ . 

- Mikulik, V., Delétang, G., McGrath, T., Genewein, T., Martic, M., Legg, S., & Ortega, P. A. (2020). Meta-trained agents implement bayes-optimal agents. _arXiv preprint arXiv:2010.11223_ . 

- Mikulik, V., Delétang, G., McGrath, T., Genewein, T., Martic, M., Legg, S., & Ortega, P. (2020). Meta-trained agents implement bayes-optimal agents. In H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, & H. Lin (Eds.), _Advances in neural_ 

   - _information processing systems_ (Vol. 33, pp. 18691–18703). Curran Associates, Inc. Retrieved from `https://proceedings.neurips.cc/paper/2020/file/ d902c3ce47124c66ce615d5ad9ba304f-Paper.pdf` 

- Mitchell, T. M. (1997). _Machine learning_ (Vol. 1) (No. 9). 

- Molano-Mazon, M., Barbosa, J., Pastor-Ciurana, J., Fradera, M., Zhang, R.-Y., Forest, J., . . . others (2022). Neurogym: An open resource for developing and sharing neuroscience tasks. 

- Montello, D. R. (2005). _Navigation._ Cambridge University Press. 

- Moskovitz, T., Miller, K., Sahani, M., & Botvinick, M. M. (2022). A unified theory of dual-process control. _arXiv preprint arXiv:2211.07036_ . 

- Müller, S., Hollmann, N., Arango, S. P., Grabocka, J., & Hutter, F. (2021). Transformers can do bayesian inference. _arXiv preprint arXiv:2112.10510_ . 

META-LEARNED MODELS OF COGNITION 

58 

- Murphy, K. P. (2012). _Machine learning: a probabilistic perspective_ . MIT press. 

- Newell, A. (1992). Unified theories of cognition and the role of soar. In _Soar: A cognitive architecture in perspective_ (pp. 25–79). Springer. 

- Newell, A., Simon, H. A., et al. (1972). _Human problem solving_ (Vol. 104) (No. 9). Prentice-hall Englewood Cliffs, NJ. 

- Nichol, A., Achiam, J., & Schulman, J. (2018). On first-order meta-learning algorithms. _arXiv preprint arXiv:1803.02999_ . 

- Nosofsky, R. M. (2011). The generalized context model: An exemplar model of classification. _Formal approaches in categorization_ , 18–39. 

- Oaksford, M., Chater, N., et al. (2007). _Bayesian rationality: The probabilistic approach to human reasoning_ . Oxford University Press. 

- Ortega, P. A., Braun, D. A., Dyer, J., Kim, K.-E., & Tishby, N. (2015). Information-theoretic bounded rationality. _arXiv preprint arXiv:1512.06789_ . 

- Ortega, P. A., Wang, J. X., Rowland, M., Genewein, T., Kurth-Nelson, Z., Pascanu, R., . . . others (2019). Meta-learning of sequential strategies. _arXiv preprint arXiv:1905.03030_ . 

- Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., . . . Chintala, S. (2019). Pytorch: An imperative style, high-performance deep learning library. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, & R. Garnett (Eds.), _Advances in neural information processing systems 32_ (pp. 8024–8035). Curran Associates, Inc. Retrieved from `http://papers.neurips.cc/paper/9015` 

   - `-pytorch-an-imperative-style-high-performance-deep-learning-library.pdf` 

- Pearl, J. (2009). _Causality_ . Cambridge university press. 

- Piloto, L. S., Weinstein, A., Battaglia, P., & Botvinick, M. (2022). Intuitive physics learning in a deep-learning model inspired by developmental psychology. _Nature human behaviour_ , _6_ (9), 1257–1267. 

META-LEARNED MODELS OF COGNITION 

59 

- Pritzel, A., Uria, B., Srinivasan, S., Badia, A. P., Vinyals, O., Hassabis, D., . . . Blundell, C. (2017). Neural episodic control. In _International conference on machine learning_ (pp. 2827–2836). 

- Rabinowitz, N. C. (2019). Meta-learners’ learning dynamics are unlike learners’. _arXiv preprint arXiv:1905.01320_ . 

- Rahwan, I., Cebrian, M., Obradovich, N., Bongard, J., Bonnefon, J.-F., Breazeal, C., . . . others (2019). Machine behaviour. _Nature_ , _568_ (7753), 477–486. 

- Ratcliff, R., & McKoon, G. (2008). The diffusion decision model: theory and data for two-choice decision tasks. _Neural computation_ , _20_ (4), 873–922. 

- Reed, S., Zolna, K., Parisotto, E., Colmenarejo, S. G., Novikov, A., Barth-Maron, G., . . . others (2022). A generalist agent. _arXiv preprint arXiv:2205.06175_ . 

- Rescorla, M. (2020). An improved dutch book theorem for conditionalization. _Erkenntnis_ , 1–29. 

- Rescorla, R. A. (1972). A theory of pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. _Current research and theory_ , 64–99. 

- Rich, A. S., & Gureckis, T. M. (2019). Lessons for artificial intelligence from the study of natural stupidity. _Nature Machine Intelligence_ , _1_ (4), 174–180. 

- Ritter, S., Barrett, D. G., Santoro, A., & Botvinick, M. M. (2017). Cognitive psychology for deep neural networks: A shape bias case study. In _International conference on machine learning_ (pp. 2940–2949). 

- Ritter, S., Wang, J., Kurth-Nelson, Z., Jayakumar, S., Blundell, C., Pascanu, R., & Botvinick, M. (2018). Been there, done that: Meta-learning with episodic recall. In _International conference on machine learning_ (pp. 4354–4363). 

- Riveland, R., & Pouget, A. (2022). Generalization in sensorimotor networks configured with natural language instructions. _bioRxiv_ , 2022–02. 

- Rosenkrantz, R. D. (1992). The justification of induction. _Philosophy of Science_ , _59_ (4), 527–539. 

META-LEARNED MODELS OF COGNITION 

60 

- Rumelhart, D. E., McClelland, J. L., Group, P. R., et al. (1988). _Parallel distributed processing_ (Vol. 1). IEEE New York. 

- Sanborn, A., & Griffiths, T. (2007). Markov chain monte carlo with people. _Advances in neural information processing systems_ , _20_ . 

- Sanborn, A. N. (2017). Types of approximation for probabilistic cognition: Sampling and variational. _Brain and cognition_ , _112_ , 98–101. 

- Sanborn, A. N., Griffiths, T. L., & Navarro, D. J. (2010). Rational approximations to rational models: alternative algorithms for category learning. _Psychological review_ , _117_ (4), 1144. 

- Sanborn, A. N., & Silva, R. (2013). Constraining bridges between levels of analysis: A computational justification for locally bayesian learning. _Journal of Mathematical Psychology_ , _57_ (3-4), 94–106. 

- Sancaktar, C., Blaes, S., & Martius, G. (2022). Curious exploration via structured world models yields zero-shot object manipulation. In A. H. Oh, A. Agarwal, D. Belgrave, & K. Cho (Eds.), _Advances in neural information processing systems._ Retrieved from `https://openreview.net/forum?id=NnuYZ1el24C` 

- Santoro, A., Bartunov, S., Botvinick, M., Wierstra, D., & Lillicrap, T. (2016). Meta-learning with memory-augmented neural networks. In _International conference on machine learning_ (pp. 1842–1850). 

- Savage, L. J. (1972). _The foundations of statistics_ . Courier Corporation. 

- Schaul, T., & Schmidhuber, J. (2010). Metalearning. _Scholarpedia_ , _5_ (6), 4650. (revision #91489) doi: 10.4249/scholarpedia.4650 

- Schlag, I., Irie, K., & Schmidhuber, J. (2021). Linear transformers are secretly fast weight programmers. In _International conference on machine learning_ (pp. 9355–9366). 

- Schmidhuber, J. (1987). _Evolutionary principles in self-referential learning, or on learning how to learn: the meta-meta-... hook_ (Unpublished doctoral dissertation). Technische Universität München. 

META-LEARNED MODELS OF COGNITION 

61 

- Schramowski, P., Turan, C., Andersen, N., Rothkopf, C. A., & Kersting, K. (2022). Large pre-trained language models contain human-like biases of what is right and wrong to do. _Nature Machine Intelligence_ , _4_ (3), 258–268. 

- Schulz, E., Bhui, R., Love, B. C., Brier, B., Todd, M. T., & Gershman, S. J. (2019). Structured, uncertainty-driven exploration in real-world consumer choice. _Proceedings of the National Academy of Sciences_ , _116_ (28), 13903–13908. 

- Schulz, E., & Dayan, P. (2020). Computational psychiatry for computers. _Iscience_ , _23_ (12), 101772. 

- Schulz, E., & Gershman, S. J. (2019). The algorithmic architecture of exploration in the human brain. _Current opinion in neurobiology_ , _55_ , 7–14. 

- Schulz, E., Tenenbaum, J. B., Duvenaud, D., Speekenbrink, M., & Gershman, S. J. (2017, December). Compositional inductive biases in function learning. _Cogn. Psychol._ , _99_ , 44–79. doi: 10.1016/j.cogpsych.2017.11.002 

- Shepard, R. N. (1987). Toward a universal law of generalization for psychological science. _Science_ , _237_ (4820), 1317–1323. 

- Snell, J., Swersky, K., & Zemel, R. (2017). Prototypical networks for few-shot learning. _Advances in neural information processing systems_ , _30_ . 

- Solomonoff, R. J. (1964). A formal theory of inductive inference. part i. _Information and control_ , _7_ (1), 1–22. 

- Stopper, C. M., Maric, T., Montes, D. R., Wiedman, C. R., & Floresco, S. B. (2014). Overriding phasic dopamine signals redirects action selection during risk/reward decision making. _Neuron_ , _84_ (1), 177–189. 

- Strouse, D., McKee, K., Botvinick, M., Hughes, E., & Everett, R. (2021). Collaborating with humans without human data. _Advances in Neural Information Processing Systems_ , _34_ , 14502–14515. 

- Tamar, A., Wu, Y., Thomas, G., Levine, S., & Abbeel, P. (2016). Value iteration networks. _Advances in neural information processing systems_ , _29_ . 

META-LEARNED MODELS OF COGNITION 

62 

- Tauber, S., Navarro, D. J., Perfors, A., & Steyvers, M. (2017). Bayesian models of cognition revisited: Setting optimality aside and letting data drive psychological theory. _Psychological review_ , _124_ (4), 410. 

- Team, A. A., Bauer, J., Baumli, K., Baveja, S., Behbahani, F., Bhoopchand, A., . . . others (2023). Human-timescale adaptation in an open-ended task space. _arXiv preprint arXiv:2301.07608_ . 

- Team, O. E. L., Stooke, A., Mahajan, A., Barros, C., Deck, C., Bauer, J., . . . others (2021). Open-ended learning leads to generally capable agents. _arXiv preprint arXiv:2107.12808_ . 

- Tenenbaum. (2021). _Joshua Tenenbaum’s homepage._ 

`http://web.mit.edu/cocosci/josh.html` . ([Online; accessed 9-November-2021]) 

- Thrun, S., & Pratt, L. (1998). Learning to learn: Introduction and overview. In _Learning to learn_ (pp. 3–17). Springer. 

- Todorov, E., Erez, T., & Tassa, Y. (2012). Mujoco: A physics engine for model-based control. In _2012 ieee/rsj international conference on intelligent robots and systems_ (pp. 5026–5033). 

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., . . . Polosukhin, I. (2017). Attention is all you need. _Advances in neural information processing systems_ , _30_ . 

- Vinyals, O., Blundell, C., Lillicrap, T., Wierstra, D., et al. (2016). Matching networks for one shot learning. _Advances in neural information processing systems_ , _29_ . 

- Wang, J. X. (2021). Meta-learning in natural and artificial intelligence. _Current Opinion in Behavioral Sciences_ , _38_ , 90–95. 

- Wang, J. X., King, M., Porcel, N., Kurth-Nelson, Z., Zhu, T., Deck, C., . . . Botvinick, M. (2021). Alchemy: A structured task distribution for meta-reinforcement learning. _CoRR_ , _abs/2102.02926_ . Retrieved from `https://arxiv.org/abs/2102.02926` 

- Wang, J. X., Kurth-Nelson, Z., Kumaran, D., Tirumala, D., Soyer, H., Leibo, J. Z., . . . 

META-LEARNED MODELS OF COGNITION 

63 

Botvinick, M. (2018). Prefrontal cortex as a meta-reinforcement learning system. _Nature neuroscience_ , _21_ (6), 860–868. 

- Wang, J. X., Kurth-Nelson, Z., Tirumala, D., Soyer, H., Leibo, J. Z., Munos, R., . . . Botvinick, M. (2016). Learning to reinforcement learn. _arXiv preprint arXiv:1611.05763_ . 

- Wilson, R. C., Geana, A., White, J. M., Ludvig, E. A., & Cohen, J. D. (2014). Humans use directed and random exploration to solve the explore–exploit dilemma. _Journal of Experimental Psychology: General_ , _143_ (6), 2074. 

- Wolpert, D. H. (1996). The lack of a priori distinctions between learning algorithms. _Neural computation_ , _8_ (7), 1341–1390. 

- Wolpert, D. H., & Macready, W. G. (1997). No free lunch theorems for optimization. _IEEE transactions on evolutionary computation_ , _1_ (1), 67–82. 

- Wu, C. M., Schulz, E., Speekenbrink, M., Nelson, J. D., & Meder, B. (2018). Generalization guides human exploration in vast decision spaces. _Nature human behaviour_ , _2_ (12), 915–924. 

- Yang, G. R., Joglekar, M. R., Song, H. F., Newsome, W. T., & Wang, X.-J. (2019). Task representations in neural networks trained to perform many cognitive tasks. _Nature neuroscience_ , _22_ (2), 297–306. 

- Yang, Y., & Piantadosi, S. T. (2022). One model for the learning of language. _Proceedings of the National Academy of Sciences_ , _119_ (5). 

- Yu, T., Quillen, D., He, Z., Julian, R., Hausman, K., Finn, C., & Levine, S. (2020). Meta-world: A benchmark and evaluation for multi-task and meta reinforcement learning. In _Conference on robot learning_ (pp. 1094–1100). 

- Zednik, C., & Jäkel, F. (2016). Bayesian reverse-engineering considered as a research strategy for cognitive science. _Synthese_ , _193_ (12), 3951–3985. 

- Zenil, H., Marshall, J. A., & Tegnér, J. (2015). Approximations of algorithmic and structural complexity validate cognitive-behavioural experimental results. _arXiv_ 

META-LEARNED MODELS OF COGNITION 

64 

_preprint arXiv:1509.06338_ . 

