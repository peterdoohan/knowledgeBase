PSYCHOLOGICAL AND COGNITIVE SCIENCES **RESEARCH ARTICLE |** BIOPHYSICS AND COMPUTATIONAL BIOLOGY 

**==> picture [30 x 29] intentionally omitted <==**

## **Expert navigators deploy rational complexity–based decision precaching for large- scale real- world planning** 

Pablo Fernandez Velasco[a,b,1] , Eva - Maria Griesbauer[a,1] , Iva K. Brunec[c] , Jeremy Morley[d] , Ed Manley[e,f] , Daniel C. McNamee[g,2,3] , and Hugo J. Spiers[a,2,3] 

Affiliations are included on p. 8. 

Edited by Peter Dayan, Max Planck Institute for Biological Cybernetics; received April 22, 2024; accepted October 25, 2024 by Editorial Board Member Elizabeth A. Buffalo 

**Efficient planning is a distinctive hallmark of intelligence in humans, who routinely make rapid inferences over complex world contexts. However, studies investigating how humans accomplish this tend to focus on naive participants engaged in simplistic tasks with small state spaces, which do not reflect the intricacy, ecological validity, and human specialization in real** - **world planning. In this study, we examine the street** - **by** - **street route planning of London taxi drivers navigating across more than 26,000 streets in London (United Kingdom). We explore how planning unfolded dynamically over different phases of journey construction and identify theoretic principles by which these expert human planners rationally precache decisions at prioritized environment states in an early phase of the planning process. In particular, we find that measures of path complexity predict human mental sampling prioritization dynamics independent of alternative measures derived from the real spatial context being navigated. Our data provide real** - **world evidence for complexity** - **driven remote state access within internal models and precaching during human expert route planning in very large structured spaces.** 

efficient planning | large - scale | real - world | navigation | human expertise 

In the novel _Invisible Cities_ , the author Italo Calvino plays on an analogy between navigating through an urban street network and making moves in a game of chess. Both require the consideration of future actions and their outcomes in order to decide which way to move, that is, planning ( 1 ). This analogy between the real and the abstract is a common presupposition in the study of cognitive mechanisms of expert human reasoning ( 2 ). Indeed, to date, computational modeling studies of human planning have relied on abstract games such as chess, or Go, or the Tower of Hanoi problem for experimental verification ( 3 ). Thus, the degree to which theoretic principles developed in the fields of cognitive science and AI can be extrapolated to the cognitive computations of human domain experts solving - large scale planning problems in the real world is largely unknown. 

The classic approach to planning, both in the cognitive sciences ( 4 – 6 ) and in AI ( 7 – 9 ), is to implement a tree search algorithm. This approach involves a representation of possible trajectories across a state space, with potential actions as branching points. Each sampled trajectory along the decision tree results in an estimated total expected reward or probability of goal achievement, and action plans are decided on based on maximizing such estimated quantities ( 10 – 12 ). The fundamental difficulty with algorithms based on tree search is that they become computationally intractable in large state spaces. This so-called curse of dimensionality ( 13 ) presents a puzzle for modeling human cognition, given that humans have the capability to plan in vast state spaces in which humans operate under substantial time pressures and with limited working memory capacity ( 14 ,  15 ). 

And yet, humans routinely defy the curse of dimensionality, by planning successfully in extremely complex environments such as cities ( 16 ). Recent approaches in theoretical modeling have sought to specify how humans do this. Existing studies have modeled how people allocate limited computational resources ( 17 ,  18 ), modulate the depth of their planning ( 6 ,  19 ), prune initially unpromising paths ( 5 ), and identify how much planning to perform ( 20 ). Some of this work has also investigated possible modifications of the problem representation itself, through different forms of simplified representations ( 21 ) and task decomposition ( 22 – 24 ) leading to hierarchical planning ( 14 ,  25 – 30 ). 

Efficient planning has been studied in a broad range of experimental and theoretic settings, - such as problem solving games ( 31 ,  32 ), regionalized virtual environments ( 33 ,  34 ) examining the linguistic impact of semantics and preferences for regional crossings ( 35 ,  36 ), latent graphs governing transitions between object stimuli ( 22 ,  37 ,  38 ) or a virtual subway network task ( 39 ). Evidence from these studies suggests not only the existence of regionalized representations of different environments but also that humans exploit such state-space structure to 

## **Significance** 

Humans can plan efficiently in incredibly complex situations. Existing work has looked at naive participants in simple tasks, which might not be representative of how experts plan in the real world. Here, we study the real - world planning process of London taxi drivers – famous for their expert knowledge of London. By analyzing their response times as a proxy for thinking times, we reveal that at an early stage in their thought process, they store decisions at key street junctions to keep them in mind for later planning. Using computational modeling, we show that taxi drivers prioritize inference at street junctions according to normative metrics measuring how critical a particular decision is for reducing the complexity of planning across the entire city. 

Author contributions: E. - M.G., J.M., and H.J.S. designed research; E. - M.G. performed research; I.K.B. and E.M. contributed new reagents/analytic tools; P.F.V. and D.C.M. analyzed data; and P.F.V., D.C.M., and H.J.S. wrote the paper. 

The authors declare no competing interest. 

This article is a PNAS Direct Submission. P.D. is a guest editor invited by the Editorial Board. 

Copyright © 2025 the Author(s). Published by PNAS. This article is distributed under Creative Commons Attribution - NonCommercial - NoDerivatives License 4.0 (CC BY - NC - ND). 

Although PNAS asks authors to adhere to United Nations naming conventions for maps (https://www.un.org/ geospatial/mapsgeo), our policy is to publish maps as provided by the authors. 

> 1P.F.V. and E. - M.G. contributed equally to this work. 

2D.C.M. and H.J.S. contributed equally to this work. 

3To whom correspondence may be addressed. Email: daniel.mcnamee@research.fchampalimaud.org or h.spiers@ ucl.ac.uk. 

This article contains supporting information online at https://www.pnas.org/lookup/suppl/doi:10.1073/pnas. 2407814122/- /DCSupplemental. 

Published January 23, 2025. 

https://doi.org/10.1073/pnas.2407814122 **1 of 9** 

**PNAS** 2025  Vol. 122  No. 4 e2407814122 

prioritize particular states in their inference process in order to minimize planning demands ( 14 ,  24 ,  35 ,  39 ). However, most studies to - date have employed either virtual, small scale, or abstract environments ( 33 – 35 ,  40 ,  41 ). As a result, it remains unclear how humans process and exploit state-space structure in large, real-world environments. Cities epitomize the intricacy of planning in real-world environments. If we considered planning a path across a large city that between start and destination involved 30 streets, using a minimal tree-search algorithm would involve an evaluation of over 1 billion potential street sequences ( 5 ). The complexity of cities also lies in the fact that they lack definitive regional segregation. For example, in London (UK) there is no definite boundary between _Farringdon_ and _City of London_ , despite both regions being well known to Londoners ( 42 ). In contrast, the state spaces used in experimental work are often designed so as to accentuate particular state-space structure such as hierarchical decompositions ( 33 – 35 ,  39 ,  43 ). A case in point is the study by Balaguer and colleagues ( 39 ), in which a virtual subway network was divided into subway lines, which facilitated hierarchically organized planning. Expert human planning in - large real world environments, such as London ( Fig. 1 ), without - exogenously imposed state space structure or other cognitive structural representations, remains to be studied. 

A general quantitative indicator of efficient planning, which may be applied to many such modeling techniques, and may be indexed via the analysis from human reaction times, is the order in which states are processed during planning ( 44 ). For example, a simple forward tree search strategy processes states in an ordered fashion directly related to the relative order of those states in the state space. In contrast, we consider strategies for efficient planning which may result in states being processed out-of-order with - respect to the state space structure. For example, efficient planning with hierarchical representations leverages bottleneck states, which - connect contiguous state space clusters, to be prioritized, and results in a disordered index of states being evaluated with respect to the state-space structure ( 28 ). Overall, this approach can reduce the number of states which may need to be evaluated. Our analysis approach is based on identifying evidence for such discontiguous state prioritization from expert human reaction time data and - relating this estimate to information theoretically motivated var- iables computed from the state space graph. In particular, we investigate the influence of two measures of planning complexity on expert human planning which, respectively, measure how likely and how connected a given state is ( 14 ). The first measure is quantified by the successor representation (SR) ( 45 ), while the second is measured by the local transition entropy (LTE) in the state-space graph. It can be shown that the product of these two quantities is the contribution of any given state to the _path entropy_ . The path entropy is the entropy of the distribution of all paths in the state space and measures the information-theoretic cost of specifying a particular path, e.g., an optimal route to a particular goal. It has been proposed as a measure of planning complexity in large state spaces and related to neural and behavioral signatures of internal representations for efficient planning ( 14 ). Our normative framework proposes that expert humans structure their mental search process by prioritizing states in order to maximally decrease path entropy—a principle we refer to as _planning description length minimization_ . 

- Here, we sought real world evidence of such theoretic principles - underlying human expert planning in ecologically valid, large scale, state spaces. This effort faces two key challenges, one from an analysis perspective, and the other from an experimental perspective. From an analysis perspective, the size of the state space presents a significant challenge for fitting and evaluating mechanistic planning models, thus, in this work, we pursued a descriptive 

statistical approach based on prior normative theoretic analyses of planning efficiency ( 14 ). Indeed, this approach was previously used to infer the existence of hierarchical representations in electrophysiological recordings of neural activity and also human sensitivity to critical bottleneck states in laboratory experiments - involving the mental simulation of real world routes ( 43 ,  46 ). A recent successful approach to testing spatial planning has been to - - examine the reaction times of choices when navigating step by step in a fictitious subway network ( 39 ). In this approach, increased reaction times imply higher computational demands on the brain to make the next choice and can be employed to infer the computational mechanisms underlying a planning process. Here, we extend this approach from a state space of 35 states to a state space of over 26,000 states: the street network of London (UK). To our knowledge, this is the largest graph structure ever completely enumerated in a human psychological experiment. 

From an experimental perspective, the challenge was to identify - a large and ecologically valid real world state space, and then to recruit a human participant population with expert domain knowledge thereof. To explore how people navigate, ideally participants - - would tell you their planned route step by step. The issue is that the larger the street network, the harder it will be to find participants who can plan routes and recall the names of all the streets between any two points. We propose that licensed London taxi drivers provide an exceptional opportunity to meet this challenge. London taxi drivers are exceptional in the world for their knowledge of street networks and navigational expertise ( 16 ). They are unique with respect to their vast experience and standardized expert training of the London street network ( 47 ), and they have been well characterized in prior studies exploring cognition, brain function, and structural changes as a result of expertise ( 48 – 56 ) and taxi drivers may be at less risk of Alzheimer’s disease than the general population ( 57 ). Indeed, in order to obtain their license, London taxi drivers are specifically examined on their ability to mentally navigate through London by naming all the streets and turns in a planned route between a given origin and destination. This familiar task paradigm forms the basis of our experimental approach ( 47 ). Participants were - asked to plan routes between a set of origin destination pairs, and then “call out” the routes step by step. The collected verbal data of the route call-outs were transcribed with regard to street names and to response times. We then employed information-theoretic models to provide predictor variables for the statistical analysis of data col- lected from forty three taxi drivers. Specifically, we used general linear models (GLM) to examine the effect of environmental, cognitive, and theoretical metrics on route planning, with the aim of testing for efficient planning by examining the inferred order in which states are processed. More generally, we assess the impact of different variable classes, such as environmental, spatial, and theoretic, on real-world large-scale expert planning. With response times serving as the behavioral measure, we employed a multivariate linear regression analysis to explore how these variables impacted planning. 

## **Results** 

**Data Extraction, Preparation, and Characterization.** Response times were extracted from transcribed verbal reports of London routes (Fig. 1 and Movie S1). Participants were given an origin and a destination, and they had to call out the run (i.e., the route) step by step (Fig. 2 _A_ ). For each route, the response time data consisted of an _OFF- TT_ (OFF- TT, the time from task presentation to the - first call out which characterizes the offline phase while the taxi driver silently considers the route) and subsequent _COT_ (COT, the times between each call- out corresponding to the online phase). We refer to the sum of COT for a particular route as the _online_ 

**2 of 9** https://doi.org/10.1073/pnas.2407814122 

pnas.org 

## A 

**==> picture [392 x 324] intentionally omitted <==**

B 

**==> picture [127 x 55] intentionally omitted <==**

**==> picture [127 x 56] intentionally omitted <==**

**==> picture [127 x 56] intentionally omitted <==**

**==> picture [127 x 56] intentionally omitted <==**

**==> picture [127 x 56] intentionally omitted <==**

**==> picture [127 x 55] intentionally omitted <==**

C D 

**==> picture [156 x 76] intentionally omitted <==**

**==> picture [98 x 100] intentionally omitted <==**

**==> picture [66 x 100] intentionally omitted <==**

**Fig. 1.** Route planning task. London taxi drivers received prerecorded audio instructions of the origin and destination locations and called out the names of all the streets they would navigate between the two points, after which they were presented with the next origin - destination pair. All instructions and route plans were audio recorded and transcribed to extract response times. The time lapsed between the instructions and the first recalled street was defined as the offline thinking time (OFF - TT, corresponding to an offline phase of planning). Time lapses between called - out streets of the route were considered as the response times in the online planning phase. ( _A_ ) An overlay of the responses from all participants for all routes. For the same origin - destination pair, different participants called different routes. ( _B_ ) An example of route 8 (Joe Allen’s restaurant to Courthouse Hotel) for a single participant. The taxi driver “called” the “run” (i.e., route) turn by turn. In the map is the resulting route as it evolved, indicating the corresponding trial times ( _Top_ - _Right_ of each map) and streets called ( _Left_ ). See also Movie S1. ( _C_ ) The whole route is mapped for the example route shown in _B_ . The circumference size of the circle markers corresponds to the length of the time lapses between recalled streets. ( _D_ ) The call - out times (COT) (Response times, average z - score values). Note the long pause before Shaftesbury Avenue that is consistent across all taxi drivers (corresponding to the largest circle in C). See Movie S1 for an audio recording of a taxi driver calling out route 8 and an animation of the corresponding route evolving turn - by - turn. 

https://doi.org/10.1073/pnas.2407814122 **3 of 9** 

**PNAS** 2025  Vol. 122  No. 4 e2407814122 

A 

**==> picture [171 x 135] intentionally omitted <==**

**==> picture [14 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>**----- End of picture text -----**<br>


**==> picture [192 x 162] intentionally omitted <==**

**Fig. 2.** Anticorrelation between offline and online thinking times. ( _A_ ) We schematize the trial structure distinguishing the relevant response time variables. In particular, we distinguish OFF - TT from the COT in different phases of the trial. The sum of COT is referred to as the ON - TT for the route. ( _B_ ) For each run called out by a taxi driver, we normalized the OFF - TT and ON - TT by the streetwise distance of the route. There was a strong negative correlation as measured by Spearman rank correlation _𝜌_ = − 0.348, _p <_ 10[−][9] . This indicates that longer periods spent thinking offline before the call - outs begin, reduces the burden of planning online. Notably, this correlation was not significant if normalized by the number of steps along each route. This suggests that the physical structure of London was a relevant factor in determining taxi driver planning dynamics. 

_thinking time_ (ON- TT). Mean OFF- TT was M = 13.83s ( _SD_ = 13.40) over N = 315 routes. On average, taxi drivers recalled 84.02% of routes. The average total response duration across tasks was M = 17.53s ( _SD_ = 16.47). The total number of pauses between two consecutively named streets was 3,398, with a mean call- out time of M = 1.82s ( _SD_ = 3.24). For more details of the task, see ref. 58. All procedures were approved by the UCL research ethics committee (CPB/2013/150 and EP/2018/008). Informed consent was obtained from all participants. 

**Relating Thinking Times Across Different Route Planning Phases.** In order to examine the relationship between OFF- TT and ON- TT across routes, we first normalized these data by the streetwise distance on a per- route basis in order to account for the large variability in route length. We then computed the Spearman rank correlation coefficient between OFF- TT and ON- TT (distance normalized) resulting in a strongly significant anticorrelation _휌_ = − 0.348 ( _p <_ 10[−][9] , Fig. 2 _B_ ). This indicates that time spent thinking offline reduced the ON- TT required to plan the route. We then tested whether the length of the offline phase differentially impacted online thinking on short versus long timescales. We performed a mediansplit of our data according to the step number along each route thus defining an EARLY phase of online planning and a LATE online planning phase. There was no significant difference in COT in the early versus late online planning phases ( _t_ = − 1.43, _p_ = 0.15 ) and longer OFF- TT did not modulate COTs differently in the early versus late online phase ( _t_ = − 0.436, _p_ = 0.663 ). This suggests that offline planning operated across the entirety of the route in a global fashion rather than considering streets local to the start position of the route. 

**Linear Regression Analysis of COT.** We then sought to understand which environmental and theoretic variables influence the modulation of ON- TT via a fixed- effects multivariate linear regression analysis of the COT. This revealed that the following variables had significant effects on COT: _Euclidean distance, segment length, remaining streetwise distance- to- destination, remaining direct distance- to- destination, SR, segment angular deviation, destination angular deviation,_ and _OFFTT × SR and OFF- TT × LTE interactions_ (Table 1, SR is successor representation, LTE is local transition entropy). See Fig. 3 _A_ and _B_ for graphical illustrations of the SR and LTE variables. A multivariate 

correlation analysis was performed which indicated that the theoretic SR and LTE predictor variables were relatively independent of the environmental predictor variables (Fig. 3 _C_ ). A model comparison analysis was performed to compare GLMs expressing distinct hypotheses regarding the interactions between the theoretic variables and taxi driver thinking times (Fig. 3 _D_ ). Table 1 reports the best fitting GLM3 which contains OFF- TT x SR and OFF- TT x LTE interactions. GLM0 included only environmental predictors, GLM1 included environmental and theoretic predictors, and GLMs 2- 5 included several distinct combinations of interactions. Notably, the subset of GLMs containing OFF- TT interactions performed much better than the subset of GLMs without OFF- TT interactions thus providing strong evidence for an influence of OFF- TT in determining subsequent COT. 

Since the combination of SR and LTE determines a normative localized metric of planning complexity ( Fig. 3 _B_ ), we review in detail how they impacted COT ( 14 ). There was a highly significant and negative main effect of SR on COT such that more predictable states were associated with faster COTs. This effect did not interact with the planning step number ( _P_ = 0.16) indicating that it was consistently present through the planning process rather than being related to, e.g., cognitive fatigue. The main effect of LTE trended strongly toward slowing COTs but did not reach significance ( _P_ = 0.066). 

**Multiphase Dynamics in Response Times Consistent with Efficient Discontiguous State Access During Planning.** In our experiment, planning can take place before the first call- out (the offline phase) and then, may continue in parallel while the route is verbally reported (Fig. 2 _A_ ). We sought to examine how SR and LTE influence behavioral response times from a dynamic multiphase perspective over the course of planning. LTE measures the local processing cost at a particular street segment, and it is weighted by SR in determining its contribution to global planning complexity according to the planning description length perspective (see _Methods_ , Eq. **1** ). In a state space as complex as London, there are inevitably too many states to consider and search through assuming limited availability of memory capacity and time. Given this, our theoretic analysis prescribes a rational strategy whereby high SR and high LTE states are prioritized for planning (Fig. 4 _C_ ). 

In order to test this, we focused on the relationship between the length of the offline planning phase and the subsequent effects of 

**4 of 9** https://doi.org/10.1073/pnas.2407814122 

pnas.org 

**Table 1.   Regression results for general linear model 3 relating OFF** - **TT to COT via interactions between OFF** - **TT and SR, LTE** 

|<br>**SR, LTE**||
|---|---|
|Variable<br>Coef.<br>SE<br>t<br>P >|t||CI|
||[0.025<br>0.975]|
|_Intercept_<br>0.0248<br>0.051<br>0.490<br>0.624<br> _OFF-TT_<br>−0.0197<br>0.023<br>−0.858<br>0.391<br> _Plan step number_<br>0.0025<br>0.001<br>1.752<br>0.080<br> _Number of planning steps_<br>−0.0069<br>0.005<br>−1.348<br>0.178<br> _Direct distance-to-destination_<br> _[route total]_<br>0.1778<br>0.122<br>1.454<br>0.146<br> _Direct distance-to-destination_<br> _[remaining]_<br>−0.1382<br>0.105<br>−1.320<br>0.187<br> **_Streetwise distance-to-destination_**<br> **_[route total]_**<br> **−0.5128**<br> **0.156**<br> **−3.296**<br> **0.001**<br> **_Streetwise distance-to-destination_**<br>**_[remaining]_**<br> **0.3452**<br> **0.107**<br> **3.237**<br> **0.001**<br> **_Street segment length_**<br> **0.1963**<br> **0.025**<br> **7.802**<br> **0.000**<br> _Segment angular deviation_<br>0.0076<br>0.060<br>0.127<br>0.899<br> **_Destination angular deviation_**<br> **0.2128**<br> **0.086**<br> **2.461**<br> **0.014**<br> **_SR_**<br> **−0.3781**<br> **0.119**<br> **−3.186**<br> **0.001**<br> _LTE_<br>0.0411<br>0.022<br>1.841<br>0.066<br> **OFF-TT x SR**<br> **0.3801**<br>**0.124**<br> **3.075**<br> **0.002**<br> **OFF-TT x LTE**<br> **−0.0481**<br> **0.023**<br> **−2.137**<br> **0.033**|−0.075<br>0.124<br>−0.065<br>0.025<br>−0.000<br>0.005<br>−0.017<br>0.003<br>−0.062<br>0.418<br>−0.344<br>0.067<br> **−0.818**<br> **−0.208**<br> **0.136**<br> **0.554**<br> **0.147**<br> **0.246**<br>−0.110<br>0.125<br> **0.043**<br> **0.382**<br> **−0.611**<br> **−0.145**<br>−0.003<br>0.085<br> **0.138**<br> **0.622**<br> **−0.092**<br> **−0.004**|



The dependent variable is the log-transformed and z-standardized COT. Variables that reached significance are highlighted in bold. Consistent with the theoretic analysis of planning complexity based on path entropy, the theoretic variables, namely SR and LTE, significantly impacted COT independent of environmental variables which characterize the veridical spatial context of the London routes. 

SR and LTE on COT. We reasoned that a longer offline planning phase should be optimized to prospectively plan specifically at high SR and high LTE states and to precache the associated decisions leading to a reduction in the subsequent COT at these states ( Fig. 4 _A_ and _B_ ). Indeed, our model comparison ( Fig. 3 _D_ ) identified significant interactions between the amount of time the taxi drivers deployed to think offline and the SR and LTE variables in determining subsequent COT. Furthermore, this hypothesis was directly - tested using median splits of the data according to the length of the offline thinking period and comparing high and low SR (LTE) call-outs across this split. For longer offline planning periods, we found a significant and selective reduction in call-out time for both the SR ( Fig. 4 _A_ ) and LTE ( Fig. 4 _B_ ) variables. In contrast, a planning - process based on sequential state roll outs, e.g., tree search, whereby states are prioritized in the order they occur along the route, would predict an interaction effect of planning step number and the length of the offline planning period ( Fig. 4 _C_ ). In particular, the COT would be relatively reduced for states closer to the origin; however, such an effect was not present in the data ( _P_ = 0.648, t (43) =−0.457). Importantly, we verified that there were no robust autocorrelations - - in the SR (1 lag autocorrelation = 0.0) and LTE (1 lag autocorrelation = 0.1) variables along the evaluated routes in order to rule out a confound whereby the SR and LTE variables were structured in a spatially consistent manner with respect to the London state space. 

## **Discussion** 

In the present study, we set out to examine expert planning in a - large scale, ecologically valid, setting by testing licensed taxi drivers engaged in navigation tasks across London. London taxi drivers are uniquely positioned for this investigation because they undergo - rigorous training and have vast, first hand experience of the street - network. In our study, we asked forty three taxi drivers to mentally - plan routes between a set of origin destination pairs while verbally 

describing those routes street by street. We then transcribed their responses and measured the response times before and while calling out the names of streets and turns along routes through the city. Using a multivariate linear regression analysis, we examined how a range of spatial, environmental, and theoretic variables impacted planning with response times serving as the behavioral measure. This approach exposed three principles of efficient expert - planning, namely predictive mapping, complexity based prioritization, and global nonsequential decision precaching. 

We sought to determine how planning dynamically unfolded over different phases of each trial. Specifically, by examining the influence of the time length of the offline planning period on COT, we aimed to identify how expert planners rationally organize their planning process in time by selectively targeting potentially remote environment states for decision precaching. This involves retrieving the relevant state information for prioritized offline planning, and storing the resulting local plan for that state, thus enabling faster plan retrieval during the online planning phase. In order to minimize planning description length, states should be accessed according to the SR and LTE measures as knowledge of the correct transitions at such states provides the maximal reduction in the overall uncertainty regarding a particular route ( 14 ,  59 ). In accordance with this idea, the data we collected from expert London taxi drivers reflected selective reductions in online response times at high SR and high LTE states for longer offline planning periods. The SR and LTE measures in our theory ( 14 ) are, respectively, analogous to the so-called need and gain terms described in theoretic work based on the Q-DYNA variant of model-based RL based on sequential state rollouts for planning ( 60 ). In this model, the gain term refers to the amount of reward that can be gained by implementing a Bellman backup update to the policy. This requires that a particular reward function - be specified ( 61 ). Given that our task, and the real world experience of taxi drivers, corresponds to the multitask RL setting with different starts and goals defining a huge number of possible reward functions, 

https://doi.org/10.1073/pnas.2407814122 **5 of 9** 

**PNAS** 2025  Vol. 122  No. 4 e2407814122 

**==> picture [13 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [172 x 167] intentionally omitted <==**

**==> picture [13 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>**----- End of picture text -----**<br>


## C 

**==> picture [232 x 170] intentionally omitted <==**

**==> picture [223 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
D<br>**----- End of picture text -----**<br>


**Fig. 3.** ( _A_ ) Graphical depictions of the SR and LTE variables. Intuitively, the SR quantitatively captures how common or likely a particular state is while LTE reflects the complexity of a decision at an environmental state. ( _B_ ) Environmental and theoretic predictor variables are schematized along an origin - destination route from local and global perspectives. SR and LTE jointly specify the local decision complexity along a run. Path entropy is the global sum of these local complexity measurements. ( _C_ ) This predictor variable correlation matrix demonstrates that the theoretic predictors, the SR and LTE, varied independently with respect to each other and the environmental predictor variables. ( _D_ ) Using the Akaike information criterion (AIC) for model comparison (a lower AIC value indicates a better explanatory model), the best explanatory model of the taxi driver COT was GLM3 (starred) containing main effects of the environmental and theoretic predictors as well as interaction terms between OFF - TT and the SR and LTE variables. Using the Bayesian information criterion instead of AIC led to the same result. This indicates that the SR and LTE variables influence state prioritization during the offline planning phase before the taxi driver starts calling out the route. 

we suggest that the LTE measure provides an appropriate analogous measure in the multitask setting agnostic to any particular reward function. Indeed, the conceptual usage of LTE in our model is consistent with a number of information-theoretic studies investi- gating efficient generic state space representations for exploration and planning in artificial agents ( 22 ,  62 – 65 ). An important distinction with respect to meta-optimized models based on Q-DYNA and tree search ( 6 ,  60 ), is the apparent global nonsequential, spatially discontiguous, nature of the prioritization effect we observe. In our data, the effect of route step number did not reach significance and the associated coefficient was very weak. Therefore, states were apparently not accessed in the order they could be sequentially generated from the origin but out-of-order with respect depending on their SR and LTE values. We suggest that such a global reorganization of planning from local simulations to nonsequential decision precaching for critical states throughout the London state space may reflect extremely refined planning strategies for expert planners. This predicts alternative forms of neural replay in the brain which may be testable in data and motivates the investigation of possible generative models of planning which exhibit such memory access dynamics ( 66 ,  67 ). 

High LTE states tend to form critical junction states which interface between adjacent clusters and thus the relatively slow call-outs at these states may be caused by internal switches between distinct local state-space representations ( 14 ). An illustrative example is the turn at Shaftesbury Avenue in  Fig. 1 , a critical junction state that corresponds to a very slow reaction time. This is consistent with our theoretical perspective given that the LTE for the Shaftesbury Avenue state in the London state space is in the 95th percentile of the LTE distribution across the entire city. Thus, expert navigators, such as taxi drivers, may exploit segmentations of London into hierarchically organized regions in order to optimize for planning - demands ( 35 ,  39 ). This result provides real world support to previous theories of hierarchical planning coming from both computational and laboratory work ( 14 ,  26 – 30 ). 

In our analysis, we included a range of environmental variables focusing on those highlighted in studies on human psychology in urban environments ( 33 ,  68 ). Some of these variables, such as distances-to-destination, may reflect a navigation strategy based on “counting down” distance to a target location as observed in homing - animals and insects, after apparently approximately path integrating outbound trajectories ( 69 ). Notably, only distance-to-destination 

**6 of 9** https://doi.org/10.1073/pnas.2407814122 

pnas.org 

**==> picture [336 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>**----- End of picture text -----**<br>


**==> picture [161 x 117] intentionally omitted <==**

**Fig. 4.** The local complexity of the street network, measured by SR and LTE, interacts with OFF - TT in predicting variability in taxi driver COT. ( _A_ ) COT specifically for highly predictive states were faster if the taxi driver spent more time thinking offline prior to beginning to verbally report the route (two - sided _t_ test between median splits, _P_ = 0.02, t = 2.565). ( _B_ ) Furthermore, the OFF - TT interacted with the theoretic LTE variable, measuring local decision complexity, in a similar manner (two - sided _t_ test between median splits, _P_ = 0.005, t = 3.045). Specifically, a longer period of offline thinking resulted in significantly decreased online COT for complex local transition structures (high LTE). ( _C_ ) Our data point to a spatially discontiguous global prioritization of remote states as planning evolves whereby high SR and high LTE states are accessed expeditiously offline and the associated local decision precached (solid - line arrows). This stands in contrast to an ordered sequential structure to London - contiguous state sampling in simulation - based models of planning such as tree search (dashed - line arrows). 

metrics measured along the traversed streets modulated the taxi drivers’ COT. Direct distances-to-destination, which ignore the street structure, did not. This suggests that taxi drivers have internally metrized London based on their natural behavioral affordances, i.e., driving through the streets, rather than absolute Euclidean distance. The theoretic predictor variables in our model were selected based on the mathematical definition of planning description length. However, this does not rule out the possibility that variables derived from other planning models may explain some of the variance in the taxi driver thinking times or provide alternative interpretations. For example, a taxi driver entering a very familiar region of London may use a regional representation with SR values conditioned on the entrance state to this region providing a better individualized fit to his or her thinking. In general, we expect this unique experimental population of human experts to provide further opportunities to test a range of models. 

Another environmental measure that has a significant effect on response times is segment length, i.e., the length of the current segment at the state level. This effect means that taxi drivers are slower at transitioning through physically longer segments. A potential explanation for this effect is that taxi drivers employ some form of mental visualization of streets along the route based on an internal model of the physical properties of London ( 59 , 70 ). This is consistent with existing work suggesting that taxi - drivers imagine in street views of the trajectory when computing route plans ( 47 ). Further evidence supporting the hypothesis that taxi drivers planned using internal representations which reflected the embodied spatial structure of London comes from the fact that destination angular deviation (i.e., angular deviation with respect to the final destination) also has an effect on response times. We can see this metric as a measure of the curvature of the route within a real-world spatial embedding as opposed to a pure - graph based representation of the state space which lacks angular relationships. Within this framework, the slowing down of response times as a function of this variable is consistent with vector-based navigation ( 71 ). Using deep reinforcement learning (RL), Banino and colleagues provided support for the idea that entorhinal grid cells contribute the spatial metric enabling the calculation of vectors between the current location and the goal ( 72 ). Another recent computational approach employed a hybrid - model that combined a map based strategy reliant on boundary cells and place cells and a vector-based strategy reliant on grid-cells ( 73 ,  74 ). Future work could investigate how the use of vector-based 

navigation, predictive maps, nonsequential precaching, and hierarchical planning vary from task to task, from environment to environment, and from participant to participant. Indeed, regarding the latter, factors which presumably influence interindividuality in the behavior and planning processes of taxi drivers are route preferences, regional familiarity, and prior distributions of routes navigated. In future work, we aim to investigate such variability in human expert planning using large-scale databases of taxi driver route distributions and demand indicators. 

## **Methods** 

**Experimental Protocol.** Taxi drivers were presented with an origin- destination pair and then were required to verbally describe a route from the origin to the destination within London. These verbal descriptions of the routes were recorded and transcribed from the taxi drivers (58). Response times were calculated as pauses between two consecutively named streets (see Fig. 1). The response time to the first named street, which tended to be significantly longer, is referred to as the _OFF- TT_ while the subsequent response times are referred to as _COT_ . The former is conceptualized as characterizing the _offline_ planning phase before the driver begins announcing the route whereas the latter corresponds to the _online_ planning phase while the driver verbally navigates the route. The sum of COT for a particular route is referred to as the _ON- TT_ . Response times were log- transformed prior to linear regression analyses and presentation. Furthermore, these data were standardized via z- scoring on a per- participant basis. 

Origin- destination combinations were selected such that the corresponding routes varied in their environmental and structural properties (e.g., Euclidean distance, path length, direction of travel, and planning complexity). The experimental data were collected in two phases. In the first phase, tasks consisted of 12 origin- destination pairs. In the second data collection phase, tasks consisted of 8 origin- destination pairs, including two origin- destination pairs from the original set to allow for a comparison across the two groups. To keep traffic conditions consistent, participants were asked to imagine they were carrying out the planning task at 11.00 AM on a typical Monday. The data from both experiments were treated as one dataset because the Wilcoxon signed- rank test indicated no group differences between the two sets of taxi drivers for tasks 7 and 8 for log- transformed COT (Mdn(S1) = −0.22, IQR = 1.18, Mdn(S2) = −0.16, IQR = 1.24, _P_ = .252, r = .046) or z- standardized COT (Mdn(S1) = −0.29, IQR = 1.11, Mdn(S2) = −0.33, IQR = 1.24, _P_ = .688, r = .016). 

**Environmental Measures of London Spatial Context.** To test the impact of spatial features of the street network on route planning behavior, COT were analyzed in association with the following environmental metrics: direct _distance- todestination, streetwise distance- to- destination, segment length, remaining direct distance- to- destination, remaining streetwise distance- to- destination, segment_ 

https://doi.org/10.1073/pnas.2407814122 **7 of 9** 

**PNAS** 2025  Vol. 122  No. 4 e2407814122 

_angular deviation,_ and _destination angular deviation. Direct distance- to- destination_ corresponds to the Euclidean distance from origin to destination as the crow flies, at the route level. _Streetwise distance- to- destination_ corresponds to the distance from origin to destination along the shortest path, at the route level. _Segment length_ corresponds to the length of the current segment, at the state level. _Remaining streetwise (direct) distance- to- destination_ corresponds to the remaining streetwise (direct) distance to the destination. _Segment angular deviation_ corresponds to the angular deviation with respect to the next segment in a route. _Destination angular deviation_ corresponds to the angular deviation with respect to the destination of the route. See Fig. 3 _B_ for a schematic illustration of these environmental measures. 

**Planning Description Length: A Normative Measure of Planning Complexity.** We use path entropy as an information- theoretic measure of planning complexity under a stochastic search model (14). This quantifies how much information must be generated on average in order to specify a route from an origin state to a destination state. The matrix H( _휏_ |o) of path entropy for all possible trajectories _휏_ emanating from an origin state _o_ in London can be expressed as a matrix- vector product of the _SR_ M and the LTE H (75, 76): 

**==> picture [166 x 14] intentionally omitted <==**

where s is an arbitrary London state. The _SR_ is defined as 

**==> picture [151 x 10] intentionally omitted <==**

where T is the transition matrix defining the probability of transitioning between states of the environment under a random walk (i.e., exploratory) policy. Specifically, T (s, s[′] ) is the probability moving to state s[′] from state s . The SR measures how likely different states (in our case, street segments) are to be sampled under a given transition policy and a model of the environment (45). To a state s , we associate the SR measure M(o, s) where o is the origin state for a particular route task. Note that the SR definition Eq. ( **2** ) does not depend on a particular goal state in contrast to previous work where a goal- absorbing SR was computed for every goal state (14). Given that any location in London may be a goal state for a taxi driver, then this goal- agnostic SR serves as a close approximation but obviates the need to compute a distinct SR for every goal state. _LTE_ is defined as 

**==> picture [181 x 15] intentionally omitted <==**

In our analyses, the SR and LTE values associated with a reported London position are computed with respect to the transition structure at the previously reported position. That is, for a transition s → s[′] then the LTE H(s) is aligned with the callout time for s[′] as this is expected to reflect the complexity of the planning process which produced state s[′] (Fig. 1). Since the overall complexity of planning may be expressed as a product of SR and LTE, we reasoned that these variables should determine the mental labor of planning and, consequently, guide how planning is efficiently structured in expert planners under resource limitations (77–79). From a normative perspective, we suggest that plans are processed at states in the order by which they reduce the overall uncertainty in the route trajectory (14). We refer to this as a _planning description length minimization_ strategy. For example, taxi drivers may establish an approximate transition plan for a critical junction such as Charing Cross before establishing the subroute from the origin to Charing Cross. 

**Theoretic Variables and State - Space Network Structure.** The SR and LTE variables have graphical interpretation in terms of the structure of the state space (Fig. 3 _A_ ) (14, 80). For example, from the graph- theoretic perspective, high SR- LTE 

1. I. Calvino, _Invisible Cities_ (Houghton Mifflin Harcourt, 1978). 

2. A. Newell, H. A. Simon, _Human Problem Solving_ (Prentice- Hall, 1972). 

3. K. R. Allen _et al._ Using games to understand the mind. https://doi.org/10.31234/osf.io/hbsvj. Accessed 10 September 2024. 

4. N. D. Daw, Y. Niv, P. Dayan, Uncertainty- based competition between prefrontal and dorsolateral striatal systems for behavioral control. _Nat. Neurosci._ 8, 1704–1711 (2005). 

5. Q. J. M. Huys _et al._ , Bonsai trees in your head: How the pavlovian system sculpts goal- directed choices by pruning decision trees. _PLOS Comput. Biol._ 8, e1002410 (2012). 

6. B. van Opheusden _et al._ , Expertise increases planning depth in human gameplay. _Nature_ 618, 1000–1005 (2023). 

7. C. E. Shannon, Programming a computer for playing chess. _Lond. Edinb. Dublin Philos. Mag. J. Sci._ 41, 256–275 (1950). 

states tend to form critical junction states (Fig. 3 _A_ , _Bottom Right_ ) while high SR low LTE correspond to highly connected states that may be concatenated into subroutes (Fig. 3 _A_ , _Top Right_ ) as in the options framework in hierarchical RL (28, 81). The network structure interpretation of SR and LTE is related to their role as normative metrics of planning complexity. Indeed, the correspondence between the network structure motifs described by these theoretic variables and their normative computational implications has been studied previously (22, 65) and their interactions explain call- out time variability ( _SI Appendix_ , Fig. S1 _A_ ). Taken together, these complementary perspectives suggest resource- rational principles by which planning may be reorganized from a localized serial search approach to a globalized multiscale process guided by SR and LTE metrics in extremely large state spaces (Fig. 4 _C_ ). 

**Statistical Analysis.** To test the effects of variables from the street network on route planning, we employed multivariate linear regression models assuming fixed effects across taxi drivers (82). The dependent variable was the logtransformed response times from the route call- outs (COTs) which was z- scored on a per- driver basis. We explored thirteen independent variables. These included the spatial metrics outlined above: _Euclidean distance- to- destination, streetwise distance- to- destination, segment length, remaining streetwise distance- todestination, segment angular deviation_ , and _destination angular deviation_ . The independent variables in the models also included the following: _OFF- TT_ , _plan step number, number of planning steps, SR measurement, LTE_ , and _SR- LTE interaction. Plan step number_ corresponded to the call- outs number within a route, at the state level. _Number of planning steps_ corresponded to the total number of call- outs in a route, at the route level. 

**Model Comparison.** We fitted several GLM to predict taxi driver COT. Each GLM had a qualitatively distinct set of predictor variables examining a specific relationship between the OFF- TT and the theoretic predictors SR and LTE in predicting COT. GLM0 contained only spatial predictor variables while GLM1 contained both spatial and theoretically predicted variables (Fig. 3 _C_ ). GLMs 2- 5 contained interaction terms involving the theoretic SR and LTE variables and OFF- TT. The best fitting model included interaction terms between OFF- TT and each of the SR and LTE theoretic variables. The nature of these significant interactions is further investigated in Fig. 4. Notably, this model comparison serves to provide strong evidence of interactions between the SR and LTE variables and OFF- TT given that the class of models containing interactions (GLMs 3 to 5) provides a much stronger fit than the model class without (GLMs 0 to 2). 

**Data, Materials, and Software Availability.** Data and the analysis code can be found at https://github.com/dmcnamee/taxi-driver-planning (82). 

**ACKNOWLEDGMENTS.** PFV’s work was supported by the British Academy (PFSS23\230053). DM’s work was supported by the Champalimaud Foundation. We thank Francesco Trapani, Margarida Sousa, and the anonymous reviewers for their feedback. 

Author affiliations: aInstitute of Behavioural Neuroscience, Department of Experimental Psychology, University College London, London WC1H 0AP, United Kingdom;[b] Department of Philosophy, University of York, York YO10 5DD, United Kingdom;[c] Department of Psychology, University of Pennsylvania, Philadelphia, PA 19104;[d] Ordnance Survey Ltd, Southampton SO16 0AS, United Kingdom;[e] School of Geography, University of Leeds, Leeds LS2 9JT, United Kingdom;[f] Centre for Advanced Spatial Analysis, University College London, London W1T 4TJ, United Kingdom; and gNeuroscience Programme, Champalimaud Research, Centre for the Unknown, Lisbon 1400 - 038, Portugal 

8. D. Silver _et al._ , Mastering the game of Go with deep neural networks and tree search. _Nature_ 529, 484–489 (2016). 

9. S. Russell, P. Norvig, _Artificial Intelligence: A Modern Approach_ (University of California, Berkeley, CA, ed. 4, 2021). 

10. L. A. Streeter, D. Vitello, A Profile of Drivers’ Map- Reading Abilities. _Hum. Factors_ 28, 223–239 (1986). 

11. R. J. Elliott, M. E. Lesk “Route finding in street maps by computers and people” in _Proceedings of the Second AAAI Conference on Artificial Intelligence_ (AAAI Press, 1982), pp. 258–261. 

12. K. J. Miller, S. J. C. Venditto, Multi- step planning in the brain. _Curr. Opin. Behav. Sci._ 38, 29–39 (2021). 

13. R. Bellman, _Dynamic programming_ (Princeton University Press, 1957). 

**8 of 9** https://doi.org/10.1073/pnas.2407814122 

pnas.org 

14. D. McNamee, D. M. Wolpert, M. Lengyel, “Efficient state- space modularization for planning: Theory” in _Behavioral and Neural Signatures in Advances in Neural Information Processing Systems_ (Curran Associates Inc, 2016). 

15. T. L. Griffiths, Understanding human intelligence through human limitations. _Trends Cogn. Sci._ 24, 873–883 (2020). 

16. P. Fernandez Velasco, H. J. Spiers, Wayfinding across ocean and tundra.what traditional cultures teach us about navigation. _Trends Cogn. Sci._ 28, 56–71 (2024). 

17. J. Snider, D. Lee, H. Poizner, S. Gepshtein, Prospective optimization with limited resources. _PLoS Comput. Biol._ 11, e1004501 (2015). 

18. F. Callaway _et al._ , “A resource- rational analysis of human planning” in _Proceedings of the 40th Annual Meeting of the Cognitive Science Society, CogSci 2018_ (The Cognitive Science Society, 2018), pp. 178–183. 

19. M. Keramati, P. Smittenaar, R. J. Dolan, P. Dayan, Adaptive integration of habits into depth- limited planning defines a habitual- goal–directed spectrum. _Proc. Natl. Acad. Sci. U.S.A._ 113, 12868–12873 (2016). 

20. E. Russek, D. Acosta- Kane, B. van Opheusden, M. G. Mattar, T. Griffiths Time spent thinking in online chess reflects the value of computation. https://doi.org/10.31234/osf.io/8j9zx. Accessed 10 September 2024. 

21. M. K. Ho _et al._ , People construct simplified mental representations to plan. _Nature_ 606, 129–136 (2022). 

22. A. Solway _et al._ , Optimal behavioral hierarchy. _PLoS Comput. Biol._ 10, e1003779 (2014). 

23. Q. J. M. Huys _et al._ , Interplay of approximate planning strategies. _Proc. Natl. Acad. Sci. U.S.A._ 112, 3098–3103 (2015). 

24. C. G. Correa, M. K. Ho, F. Callaway, N. D. Daw, T. L. Griffiths, Humans decompose tasks by trading off utility and computational cost. _PLoS Comput. Biol._ 19, e1011087 (2023). 

25. K. S. Lashley, “The problem of serial order in behavior” in _Cerebral Mechanisms in Behavior; the Hixon Symposium_ (Wiley, 1951), pp. 112–146. 

26. M. M. Botvinick, Hierarchical reinforcement learning and decision making. _Curr. Opin. Neurobiol._ 22, 956–962 (2012). 

27. J. P. O’Doherty, S. W. Lee, D. McNamee, The structure of reinforcement- learning mechanisms in the human brain. _Curr. Opin. Behav. Sci._ 1, 94–100 (2015). 

28. M. M. Botvinick, Y. Niv, A. G. Barto, Hierarchically organized behavior and its neural foundations: A reinforcement learning perspective. _Cognition_ 113, 262–280 (2009). 

29. M. S. Tomov, S. Yagati, A. Kumar, W. Yang, S. J. Gershman, Discovery of hierarchical representations for efficient planning. _PLoS Comput. Biol._ 16, e1007594 (2020). 

30. H. Bast _et al._ , “Route Planning in Transportation Networks, Lecture Notes in Computer Science” in _Algorithm Engineering: Selected Results and Surveys_ , L. Kliemann, P. Sanders, Eds. (Springer International Publishing, 2016), pp. 19–80. 

31. G. Ward, A. Allport, Planning and problem solving using the five disc tower of london task. _Q. J. Exp. Psychol. Sect. A_ 50, 49–78 (1997). 

32. C. A. Knoblock, “A Theory of abstraction for hierarchical planning” in _Change of Representation and Inductive Bias, The Kluwer International Series in Engineering and Computer Science_ , D. P. Benjamin, Ed. (Springer, US, 1990), pp. 81–104. 

33. J. M. Wiener, H. A. Mallot, “Fine- to- Coarse” route planning and navigation in regionalized environments. _Spat. Cogn. Comput._ 3, 331–358 (2003). 

34. J. M. Wiener, A. Schnee, H. A. Mallot, Use and interaction of navigation strategies in regionalized environments. _J. Environ. Psychol._ 24, 475–493 (2004). 

35. W. Schick, M. Halfmann, G. Hardiess, F. Hamm, H. A. Mallot, Language cues in the formation of hierarchical representations of space. _Spat. Cogn. Comput._ 19, 252–281 (2019). 

36. W. Schick, Acquisition and consolidation of hierarchical representations of space. https://doi. org/10.15496/publikation- 23395. 

37. J. M. Wiener, S. J. Büchner, C. Hölscher, Taxonomy of human wayfinding tasks: A knowledge- based approach. _Spat. Cogn. Comput._ 9, 152–165 (2009). 

38. B. Hommel, J. Gehrke, L. Knuf, Hierarchical coding in the perception and memory of spatial layouts. _Psychol. Res._ 64, 1–10 (2000). 

39. J. Balaguer, H. Spiers, D. Hassabis, C. Summerfield, Neural mechanisms of hierarchical planning in a virtual subway network. _Neuron_ 90, 893–903 (2016). 

40. S. Büchner _et al._ “Path choice heuristics for navigation related to mental representations of a building” in _Proceedings of the European Cognitive Science Conference_ (Taylor and Francis Delphi, Greece, 2007), pp. 504–509. 

41. D. Badre, A. S. Kayser, M. D’Esposito, Frontal cortex and the discovery of abstract action rules. _Neuron_ 66, 315–326 (2010). 

42. E.- M. Griesbauer, E. Manley, D. McNamee, J. Morley, H. Spiers, What determines a boundary for navigating a complex street network: Evidence from London taxi drivers. _J. Navig._ 75, 15–34 (2022). 

43. A. E. G. F. Arnold, G. Iaria, A. D. Ekstrom, Mental simulation of routes during navigation involves adaptive temporal compression. _Cognition_ 157, 14–23 (2016). 

44. M. G. Mattar, M. Lengyel, Planning in the brain. _Neuron_ 110, 914–934 (2022). 

45. P. Dayan, Improving generalization for temporal difference learning: The successor representation. _Neural Comput._ 5, 613–624 (1993). 

46. K. Bonasia, J. Blommesteyn, M. Moscovitch, Memory and navigation: Compression of space varies with route length and turns. _Hippocampus_ 26, 9–12 (2016). 

47. E.- M. Griesbauer, E. Manley, J. M. Wiener, H. J. Spiers, London taxi drivers: A review of neurocognitive studies and an exploration of how they build their cognitive map of London. _Hippocampus_ 32, 3–20 (2022). 

48. E. A. Maguire _et al._ , Navigation- related structural change in the hippocampi of taxi drivers. _Proc. Natl. Acad. Sci. U.S.A._ 97, 4398–4403 (2000). 

49. E. A. Maguire, K. Woollett, H. J. Spiers, London taxi drivers and bus drivers: A structural MRI and neuropsychological analysis. _Hippocampus_ 16, 1091–1101 (2006). 

50. E. A. Maguire, R. Nannery, H. J. Spiers, Navigation around London by a taxi driver with bilateral hippocampal lesions. _Brain_ 129, 2894–2907 (2006). 

51. H. J. Spiers, E. A. Maguire, Spontaneous mentalizing during an interactive real world task: an fMRI study. _Neuropsychologia_ 44, 1674–1682 (2006). 

52. H. J. Spiers, E. A. Maguire, Thoughts, behaviour, and brain dynamics during navigation in the real world. _Neuroimage_ 31, 1826–1840 (2006). 

53. H. J. Spiers, E. A. Maguire, The neuroscience of remote spatial memory: a tale of two cities. _Neuroscience_ 149, 7–27 (2007). 

54. H. J. Spiers, E. A. Maguire, Neural substrates of driving behaviour. _Neuroimage_ 36, 245–255 (2007). 

55. H. J. Spiers, E. A. Maguire, A navigational guidance system in the human brain. _Hippocampus_ 17, 618–626 (2007). 

56. H. J. Spiers, E. A. Maguire, The dynamic nature of cognition during wayfinding. _J. Environ. Psychol._ 28, 232–249 (2008). 

57. V.- R. Patel, M. Liu, C.- M. Worsham, A.- B. Jena, Alzheimer’s disease mortality among taxi and ambulance drivers: Population based cross sectional study. _BMJ_ , 10.1136/bmj-2024-082194 (2024). 

58. E.- M. Griesbauer _et al._ London taxi drivers exploit neighbourhood boundaries for hierarchical route planning. _Cognition_ 256, 106014 (2024). 

59. D. McNamee, D. M. Wolpert, Internal models in biological control. _Annu. Rev. Control Robot. Auton. Syst._ 2, 339–364 (2019). 

60. M. G. Mattar, N. D. Daw, Prioritized memory access explains planning and hippocampal replay. _Nat. Neurosci._ 21, 1609–1617 (2018). 

61. R. S. Sutton, Dyna, an integrated architecture for learning, planning, and reacting. _ACM SIGART Bull._ 2, 160–163 (1991). 

62. C. Salge, C. Glackin, D. Polani Empowerment - - an Introduction _._ arXiv [Preprint] (2013). http://arxiv. org/abs/1310.1863 (Accessed 4 December 2023). 

63. K. Gregor, D. J. Rezende, D. Wierstra Variational Intrinsic Control _._ arXiv [Preprint] (2016). http://arxiv. org/abs/1611.07507 (Accessed 4 December 2023). 

64. A. Goyal _et al._ InfoBot: Transfer and exploration via the information Bottleneck _._ arXiv [Preprint] (2023). http://arxiv.org/abs/1901.10902 (Accessed 22 March 2024). 

65. K. Archer, N. C. Volpi, F. Bröker, D. Polani A space of goals: The cognitive geometry of informationally bounded agents _._ arXiv [Preprint] (2022). http://arxiv.org/abs/2111.03699 (Accessed 4 December 2023). 

66. A. E. Comrie _et al._ , Hippocampal representations of alternative possibilities are flexibly generated to meet cognitive demands _._ bioRxiv [Preprint] (2024). 10.1101/2024.09.23.613567 (Accessed 10 October 2024). 

67. D. C. McNamee, The generative neural microdynamics of cognitive processing. _Curr. Opin. Neurobiol._ 85, 102855 (2024). 

68. D. Yesiltepe _et al._ , Entropy and a sub- group of geometric measures of paths predict the navigability of an environment. _Cognition_ 236, 105443 (2023). 

69. M. Müller, R. Wehner, Path integration in desert ants. Cataglyphis fortis. _Proc. Natl. Acad. Sci. U.S.A._ 85, 5287–5290 (1988). 

70. P. W. Battaglia, J. B. Hamrick, J. B. Tenenbaum, Simulation as an engine of physical scene understanding. _Proc. Natl. Acad. Sci. U.S.A._ 110, 18327–18332 (2013). 

71. F. Le Moël, T. Stone, M. Lihoreau, A. Wystrach, B. Webb, The central complex as a potential substrate for vector based navigation. _Front. Psychol._ 10, 690 (2019). 

72. A. Banino _et al._ , Vector- based navigation using grid- like representations in artificial agents. _Nature_ 557, 429–433 (2018). 

73. V. Edvardsen, A. Bicanski, N. Burgess, Navigating with grid and place cells in cluttered environments. _Hippocampus_ 30, 220–232 (2020). 

74. N. Nyberg, É. Duvelle, C. Barry, H. J. Spiers, Spatial goal coding in the hippocampal formation. _Neuron_ 110, 394–422 (2022). 

75. L. Ekroot, T. M. Cover, The entropy of Markov trajectories. _IEEE Trans. Inf. Theory_ 39, 1418–1421 (1993). 

76. M. Kafsi, M. Grossglauser, P. Thiran, The entropy of conditional markov trajectories. _IEEE Trans. Inf. Theory_ 59, 5577–5583 (2013). 

77. S. J. Gershman, E. J. Horvitz, J. B. Tenenbaum, Computational rationality: A converging paradigm for intelligence in brains, minds, and machines. _Science_ 349, 273–278 (2015). 

78. W. Kool, M. Botvinick, Mental labour. _Nat. Hum. Behav._ 2, 899–908 (2018). 

79. F. Lieder, T. L. Griffiths, Resource- rational analysis: Understanding human cognition as the optimal use of limited computational resources. _Behav. Brain Sci._ 43, e1 (2020). 

80. K. L. Stachenfeld, M. M. Botvinick, S. J. Gershman, The hippocampus as a predictive map. _Nat. Neurosci._ 20, 1643–1653 (2017). 

81. Y. Jinnai, D. Abel, D. Hershkowitz, M. Littman, G. Konidaris, “Finding Options that Minimize Planning Time” in _Proceedings of the 36th International Conference on Machine Learning_ (PMLR, 2019), pp. 3120–3129. 

82. D. McNamee, Data from “taxi- driver- planning.” Github. https://github.com/dmcnamee/taxi- driverplanning. Deposited 19 November 2024. 

https://doi.org/10.1073/pnas.2407814122 **9 of 9** 

**PNAS** 2025  Vol. 122  No. 4 e2407814122 

