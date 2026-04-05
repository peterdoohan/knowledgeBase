# **Nonlinear Meta-learning Can Guarantee Faster Rates** 

Dimitri Meunier[∗] _[,]_[†] _dimitri.meunier.21@ucl.ac.uk_ 

Zhu Li[∗] _[,]_[‡] Arthur Gretton[†] Samory Kpotufe[§] _michael.lzy2013@gmail.com arthur.gretton@gmail.com samory@columbia.edu_ 

## **Abstract** 

Many recent theoretical works on _**meta-learning**_ aim to achieve guarantees in leveraging similar representational structures from related tasks towards simplifying a target task. The main aim of theoretical guarantees on the subject is to establish the extent to which convergence rates—in learning a common representation— _**may scale with the number** N_ _**of tasks**_ (as well as the number of samples per task). First steps in this setting demonstrate this property when both the shared representation amongst tasks, and task-specific regression functions, are linear. This linear setting readily reveals the benefits of aggregating tasks, e.g., via averaging arguments. In practice, however, the representation is often highly nonlinear, introducing nontrivial biases in each task that cannot easily be averaged out as in the linear case. In the present work, we derive theoretical guarantees for meta-learning with nonlinear representations. In particular, assuming the shared nonlinearity maps to an infinite dimensional reproducing kernel Hilbert space, we show that additional biases can be mitigated with careful regularization that leverages the smoothness of task-specific regression functions, yielding improved rates that scale with the number of tasks as desired. 

## **1 Introduction** 

Meta-learning refers colloquially to the problem of inferring a deeper internal structure—beyond a specific task at hand, e.g., a regression task—that may be leveraged towards speeding up other similar tasks. This arises for instance in practice with neural networks where, in pre-training, multiple apparently dissimilar tasks may be aggregated to learn a _**representation**_ that enables _**faster**_ training on unseen target tasks (i.e., requiring relatively fewer target data). 

Notwithstanding the popularity of meta-learning in practice, the theoretical understanding and proper formalism for this setting is still in its early stages. We consider a common approach in the context of regression, which posits an unknown target-task function of the form _f_ ( _x_ ) = _g_ (Γ( _x_ )) and _N_ unknown related task-functions of the form _fi_ ( _x_ ) = _gi_ (Γ( _x_ )) _,i_ ∈[ _N_ ], i.e., all sharing a common but unknown _**representation**_ Γ( _x_ ); it is assumed that all _link functions g_ and { _gi_ } _[N] i_ =1[are] _[simpler]_[—][for][instance][linear][or][at][least][lower-dimensional][—] than the corresponding regression functions _f_ and { _fi_ } _[N] i_ =1[.][As][all][these][objects][are][a][priori][unknown,][recent] research has aimed to establish how the target regression problem may benefit from the _N_ related tasks. In particular, if Γ( _x_ ) may be approximated by some Γ[ˆ] ( _x_ ) at a rate that scales with _N_ (and the number _n_ of samples per task), then presumably, the target regression function _f_ may be subsequently learned as _g_ ˆ(Γ[ˆ] ( _x_ )) at a faster rate commensurate with the _simplicity_ of _g_ . 

> ∗Equal Contribution. 

> †Gatsby Computational Neuroscience Unit, University College London, London. 

> ‡Department of Mathematics, Imperial College London, London. 

> §Department of Statistics, Columbia University, New York. 

1 

Recent theoretical results (Kong et al., 2020; Du et al., 2021; Tripuraneni et al., 2021; Tian et al., 2023; Niu et al., 2024) have provided significant new insights in this area by considering an idealized linear setting where _x_ ∈ R _[d]_ , _g_ and { _gi_ } _[N] i_ =1[are][linear][functions][in][R] _[s]_[(] _[s]_[≪] _[d]_[),][and][Γ][(] _[x]_[)][denotes][a][linear][projection][to][R] _[s]_[.][These] results show that Γ can be learned at a rate of _O_[˜] (√ _ds_ / _nN_ )—under suitable subspace-distance measures, and where _O_[˜] omits log terms —which then allows for the target task to be learned at a rate of _O_[˜] (√ _s_ / _n_ ) ≪ _O_[˜] (√ _d_ / _n_ ). Here, it is emphasized that the representation learning rate of _O_[˜] (√ _ds_ / _nN_ ) scales with the number of tasks _N_ rather than just with _n_ , establishing the benefit of related tasks in improving the target rate. 

In practice, however, the representation Γ is in general a nonlinear transformation of _x_ , as when _**reproducing kernel Hilbert space**_ (RKHS) or neural net representations are used. While the importance of the nonlinear setting is well understood, fewer works have so far addressed this more challenging scenario (Maurer et al., 2016; Du et al., 2021). 

In the present work, we consider the case where Γ maps _x_ , _**nonlinearly**_ , into an RKHS H, possibly of infinite dimension; more precisely, Γ _projects_ the feature maps _K_ ( _x,_ ⋅) into an _s_ -dimensional subspace H _s_ of H. The link functions _g_ and { _gi_ } _[N] i_ =1[are][assumed][to][be] _[simple]_[in][the][sense][that][they][are][linear][in][Γ][,][hence][we][also] have that _f_ and { _fi_ } _[N] i_ =1[belong to][H][.][In][other words,][if we knew][ Γ][ (or][ H] _[s]_[ = H] _[s]_[(][Γ][)][),][the target problem would] reduce to linear regression in R _[s] ,_ and therefore would admit ( _L_ 2) convergence rates of the form _O_[˜] (√ _s_ / _n_ ), significantly faster than usual nonparametric rates for regression over infinite dimensional H (see discussion after Theorem 1 and Corollary 1). As in the case of linear Γ discussed above, this improved rate will turn out to require estimating Γ at a fast rate scaling in both _N_ and _n_ . 

When moving from linear to nonlinear, nonparametric Γ, a significant new challenge arises due to the bias inherent in the learning procedure. For a high-level intuition, note that a main appeal of meta-learning is that the aggregate of _N_ tasks should help reduce _variance_ over using a single task, by carefully combining taskspecific statistics computed on each of the _N_ samples; _crucially, such statistics ought to introduce little bias, since bias cannot be averaged out_ . Task-specific biases are harder to avoid in nonparametric settings, however, if we wish to avoid overfitting task-specific statistics. This is in contrast to the case of linear projections in R _[d]_ , where we have unbiased statistics with no overfitting (one may think e.g., of OLS). 

Fortunately, as we show in this work, nonlinear meta-learning remains possible with rate guarantees improving in both _N_ and _n_ . Our approach relies on the following initial fact: if the links { _gi_ } _[N] i_ =1[are][linear][in][H][,][it][easily] follows that the individual regression functions { _fi_ } _[N] i_ =1[all live in the span][ H] _[s]_[ ⊂H][ of the shared representation][ Γ] (see setup Section 3.1). Thus, under a _richness assumption_ where { _fi_ } _[N] i_ =1[span][ H] _[s]_[ (extending usual assumptions] in the linear case, e.g. of Du et al., 2021), we may estimate H _s_ by estimating the span of regularized estimates _f_[ˆ] _i_ of _fi_ . In order to guarantee fast rates that scale with _N_ and _n_ , we need to _**under-regularize**_ , i.e., overfit taskspecific estimates { _f_[ˆ] _i_ } _[N] i_ =1[to suitably decrease bias, at the cost of increased task-specific (hence overall) variance.] Such under-regularization necessarily implies suboptimal regression in each task, but improves estimation of the representation defined by Γ. 

We demonstrate that these trade-offs may be satisfied, depending on the _smoothness_ level of regression functions { _fi_ } _[N] i_ =1[,][as captured by complementary regularity conditions on][ {] _[f][i]_[}] _[N] i_ =1[and the interaction between the kernel] and data distributions { _µi_ } _[N] i_ =1[defined][on][X][×][ R][(see][Section][4.1][),][where][we][view][X][and][R][as][the][input][and] output spaces, respectively. In the process, some interesting subtleties emerge: meta-learning benefits from _regularity beyond usual saturation points_ that were established in traditional RKHS regression (please refer to Remark 11). This further illustrates how the meta-learning goal of estimating Γ inherently differs from regression, even when relying on regression estimates. This is discussed in further detail in Section 4. Fast rates scaling in _N_ and _n_ for estimating H _s_ = H _s_ (Γ) from span{ _f_[ˆ] _i_ } are established in Theorem 2. This requires, among other tools, a basic variation on Wedin’s sin −Θ Theorem Wedin (1972) for infinite dimensional operators (Proposition 3). As a consequence, we show that by operating in H[ˆ] _s_ (the estimation of H _s_ ) for the target regression problem, we can achieve _**parametric**_ target _L_ 2 rates of _O_[˜] (√ _s_ / _n_ ) (see Corollary 1), which are much faster than the usual nonparametric rates for _f_ ∈H. This last step requires us to establish closeness 

2 

of projections onto the estimated H[ˆ] _s_ vs H _s_ . Moreover, when the feature map _K_ ( _x,_ ⋅) is finite dimensional, our results (see Example 1) recover the learning rates obtained in earlier studies (e.g. Du et al. (2021); Tripuraneni et al. (2021)), where Γ is a linear projection. 

Finally, although much of the analysis and involved operations pertain to infinite dimensional H space, the entire approach can be instantiated in input data space via suitable representation theorems (see Section 3.3). This realization supports our theoretical findings with complementary experiments on simulated data, as detailed in Section 5. 

## **Related Work** 

Meta-learning is an umbrella term for a rich variety of learning settings, where we are provided with a set of distributions pertaining to relevant training tasks, and obtain a functional to speed learning on a target task. In this work, we focus on the case where this functional defines _a representation_ Γ _of the data_ , and where the target regression function is of the form _f_ ( _x_ ) = _g_ (Γ( _x_ )). We begin this section with the closest work to our setting (namely linear and nonlinear projections Γ), then briefly touch on alternative meta-learning definitions for completeness (although these will be outside the scope of the present study). 

We start with works in the _linear setting_ , which study generalization error where Γ is a learned linear projection R _[d]_ → R _[s]_ , obtained from _N_ training tasks (Kong et al., 2020; Du et al., 2021; Tripuraneni et al., 2021; Thekumparampil et al., 2021; Konobeev et al., 2021; Tian et al., 2023; Yüksel et al., 2024; Niu et al., 2024). Tripuraneni et al. (2021) study low-dimensional linear representation learning under the assumption of isotropic inputs for all tasks, and obtain the learning rate of _O_[˜] (√ _ds_[2] / _nN_ + √ _s_ / _n_ ) on the target task. Du et al. (2021) achieve a similar rate while relaxing the isotropic assumption with a different algorithm. In the linear representation case, they obtain an _O_[˜] (√ _ds_ / _nN_ + √ _s_ / _n_ ) rate. Kong et al. (2020) study a somewhat different scenario, where the number of samples per task may differ (and is smaller than the dimension _d_ of the data); the aim is to determine how many tasks must be undertaken in order to achieve consistency. The work of Kong et al. (2020) is most closely related to our work, as our procedure, after linearization in H, is quite similar to their procedure in R _[d]_ , notably in its reliance on outer-products of regression estimates. However, many technical issues arise in the infinite dimensional setting considered here, both on the algorithmic and analytical fronts. These are detailed in Remark 5 of Section 3. Thekumparampil et al. (2021) consider an alternate gradient descent algorithm, where they jointly minimize the within task loss and the aggregate loss across all tasks. Under the assumption that the data is Gaussian with the same variance across all tasks, they obtain the learning rate of _O_[˜] (√ _ds_ / _nN_ + √ _s_ / _n_ ). Konobeev et al. (2021) consider a distribution dependent analysis of meta-learning in the setting of fixed design finite dimensional linear regression, with Gaussian noise and a Gaussian parameter distribution. In the case where the covariance matrix of the parameter is assumed to be known, the authors provide matching upper and lower bounds, which demonstrates a precise characterization of the benefit of meta-learning. While there is no theoretical analysis in the case where the covariance matrix is unknown, the authors provide a detailed description of how the EM algorithm can be employed to solve the meta-learning problem. Tian et al. (2023) consider a generalization where tasks share similar but not identical linear representations and account for outlier tasks. Niu et al. (2024); Yüksel et al. (2024) also study the linear representation setting and provide refined theoretical analysis on learning the common representation. 

We next consider the case where the representation Γ is nonlinear. Maurer et al. (2016) evaluate the performance of a method for learning a nonlinear representation Γ ∈F which is _s_ -dimensional, addressing in particular the case of a projection onto a subspace of a reproducing kernel Hilbert space. They focus on a _learning to learn_ (LTL) scenario, where excess risk is evaluated _in expectation over a distribution of tasks_ (Section 2.2 Maurer et al., 2016): we emphasize that this is a fundamentally different objective to the performance on a specific novel test task, as in our setting. The loss they propose to minimize (Eq. 1 Maurer et al., 2016) is an average over _N_ training tasks, where each task involves a different linear weighting of the common subspace projection (the work does not propose an algorithm, but concerns itself solely with the statistical analysis). 

3 

Theorem 5 in Maurer et al. (2016) shows that for an RKHS subspace projection, one can achieve an LTL excess risk for Lipschitz losses (in expectation over the task distribution) that decreases as _O_[˜] ( _s_ / ~~√~~ _N_ + √ _s_ / _n_ ). This requires _N_ ≥ _n_ in order to approach the parametric rate. Maurer et al. (2016, note 2, p. 8) demonstrate that the factor 1/ ~~√~~ _N_ is an unavoidable consequence of the LTL setting. 

Du et al. (2021) consider the case of nonlinear representation learning, using the same training loss as Maurer et al. (2016, Eq. 1), but with performance evaluation on a single test task, as in our setting. Again defining Γ ∈F, they obtain a learning rate of _O_[˜] (G(F)/ ~~√~~ _nN_ + √ _s_ / _n_ ) for the excess risk (Du et al., 2021, Theorem 5.1), where G(⋅) measures the Gaussian width of F (a data-dependent complexity measure, and consequently a function of _n,N_ ; see e.g., Maurer (2014), for further details). The instantiation of G(F) for specific instances of F was not pursued further in this work, however Maurer (2014) shows that the Gaussian width is of order ~~√~~ _nN_ in _n_ and _N_ , in the case where F is a projection onto a subspace of an RKHS with Lipschitz kernel. 

The problem of learning a “meaningful” low-dimensional representation Γ has also been addressed in the field of sufficient dimension reduction. Fukumizu et al. (2009); Li and Dong (2009); Yin et al. (2008) give different criteria for obtaining such Γ and establishing consistency, however they do not address the risk analysis of downstream learning algorithms that employ Γ. Li et al. (2011) introduce the so-called principal support vector machine approach for learning both linear and nonlinear Γ. The idea is to learn a set of support vector regression functions, each mapping to different “features” of the output _Y_ (e.g., restrictions to intervals, nonlinear transforms). The estimator Γ[ˆ] of Γ is then constructed from the principal components of these solutions. In the linear setting, the authors provide the ~~[√]~~ _n_ -consistency of Γ[ˆ] . Wu et al. (2007) provide a kernelization of sliced inverse regression, which yields a subspace Γ in an RKHS (the so-called effective dimension reduction space). Consistency of the projection by Γ[ˆ] of an RKHS feature map _ϕ_ ( _x_ ) is established; and an _O_ ( _n_[−][1][/][4] ) convergence rate is obtained, under the assumption that all Γ components can be expressed in terms of a finite number of covariance operator eigenfunctions. The learning risk of downstream estimators using Γ[ˆ] remains to be established, however. 

Outside of the regression setting, meta-learning has been studied for classification: Galanti et al. (2022) investigate the generalization error in this setting, with the representation Γ being a fully connected ReLU neural net of depth _Q_ , common to all tasks. Aliakbarpour et al. (2024) study the sample complexity per task when the task-specific classifiers are halfspaces in R _[s]_ and the samples per task are extremely low. Finally, there are analyses for other meta-learning schemes such as domain adaption Ben-David et al. (2006); Mansour et al. (2009), domain generalization Blanchard et al. (2021) and covariate shift Ma et al. (2023), as well as alternative gradient-based approaches to refine algorithms on novel test domains, e.g., Denevi et al. (2019); Finn et al. (2017, 2019); Khodak et al. (2019); Meunier and Alquier (2021). 

## **2 Background & Notations** 

**Function Spaces & Basic Operators.** Let _µ_ be a probability measure on X × R, _µ_ X denotes the marginal distribution of _µ_ on X , and _µ_ (⋅∣ _x_ ) the conditional distribution on R given _x_ ∈X . Let _K_ ∶X × X → R be a symmetric and positive definite kernel function and H be a vector space of X → R functions, endowed with a Hilbert space structure via an inner product ⟨⋅ _,_ ⋅⟩H. _K_ is a reproducing kernel of H if and only if: 1. ∀ _x_ ∈X _,ϕ_ ( _x_ ) ≐ _K_ (⋅ _,x_ ) ∈H; 2 _._ ∀ _x_ ∈X and ∀ _f_ ∈H _,f_ ( _x_ ) = ⟨ _f,ϕ_ ( _x_ )⟩H. A space H which possesses a reproducing kernel is called a reproducing kernel Hilbert space (RKHS) (Berlinet and Thomas-Agnan, 2011). _L_ 2(X _,µ_ X ), abbreviated _L_ 2( _µ_ ), denotes the Hilbert space of square-integrable functions with respect to (w.r.t.) _µ_ X .[1] 

∥ _A_ ∥ and ∥ _A_ ∥ _HS_ denote respectively the operator and Hilbert-Schmidt norm of a linear operator _A_ on H. For _f,g_ ∈H, _g_ ⊗ _f_ ≐⟨ _f,_ ⋅⟩H _g_ is the generalization of the Euclidean outer product. The covariance operator is 

> 1To simplify notations, when we integrate over _µ_ X a function defined on X , we use E _µ_ instead of E _µ_ X . 

4 

defined as Σ ≐ E _X_ ∼ _µ_ [ _K_ ( _X,_ ⋅) ⊗ _K_ ( _X,_ ⋅)]. 

We require some standard technical assumptions on the previously defined RKHS and kernel: 1. H is separable; this is satisfied if X is a Polish space and _K_ is continuous (Lemma 4.33 Steinwart and Christmann, 2008); 2. _ϕ_ ( _x_ ) is measurable for all _x_ ∈X ; 3. sup _x,x_ ′∈X _K_ ( _x,x_[′] ) ≐ _κ_[2] < ∞. Note that those assumptions are not restrictive in practice, as well-known kernels such as the Gaussian, Laplacian and Matérn kernels satisfy all of the above assumptions on R _[d]_ (Sriperumbudur et al., 2011). 

**Matrix Notation of Basic Operators.** For a set of vectors { _u_ 1 _,...,un_ } ∈H, _U_ ≐[ _u_ 1 _,...,un_ ] denotes the operator with the vectors as “columns”, formally _U_ ∶ R _[n]_ →H _,α_ ↦∑ _[n] i_ =1 _[u][i][α][i]_[.][Its][adjoint][is] _[U]_[ ∗][∶H][→][R] _[n][,u]_[ ↦] (⟨ _ui,u_ ⟩H) _[n] i_ =1[.] 

**Kernel Ridge Regression & Regularization.** Given a data set _D_ = {( _xi,yi_ )} _[n] i_ =1[independently][sampled] from _µ_ , kernel ridge regression aims to estimate the _regression function fµ_ = E _µ_ [ _Y_ ∣ _X_ ], with the following kernel-based regularized least-squares procedure 

**==> picture [333 x 26] intentionally omitted <==**

with _λ_ > 0 the regularization parameter. R _µ_ ( _f_ ) ≐ E _µ_ [( _Y_ − _f_ ( _X_ ))[2] ] is the squared expected risk and the excess 1/2 risk is given by E _µ_ ( _f_ ) ≐ √R _µ_ ( _f_ ) −R _µ_ ( _fµ_ ) = E _µ_ [( _f_ ( _X_ ) − _fµ_ ( _X_ ))[2] ] _._ We also introduce the population version of _f_[ˆ] _λ_ as _fλ_ = argmin {E _µ_ [( _Y_ − _f_ ( _X_ ))[2] ] + _λ_ ∥ _f_ ∥[2] H[}] _[.]_ (2) _f_ ∈H 

The normed difference _f_[ˆ] _λ_ − _fλ_ is referred to as the estimation error and is a central object for the study of kernel ridge regression (see e.g., Fischer and Steinwart (2020)). 

**Further Notations.** For _n,m_ ∈ N[∗] _,n_ ≤ _m,_ [ _n_ ] ≐{1 _,...,n_ } _,_ [ _n,m_ ] ≐{ _n,...,m_ }. For two real numbers _a_ and _b_ , we denote _a_ ∨ _b_ = max{ _a,b_ } and _a_ ∧ _b_ = min{ _a,b_ }. 

## **3 Nonlinear Meta-learning** 

## **3.1 Population Set-up** 

We consider a setting with _N_ source distributions { _µi_ } _i_ ∈[ _N_ ] defined on X × R, with corresponding regression functions of the form _fi_ ( _x_ ) = _gi_ (Γ( _x_ )). We are interested in minimizing the excess risk for a target distribution _µT_ , with regression function _fT_ ( _x_ ) = _gT_ (Γ( _x_ )). In the mostly common linear case, it is assumed that Γ _projects_ into a subspace of R _[d]_ = X . However, in this manuscript, we assume that Γ is a projection of nonlinear feature maps in an infinite dimensional space. 

**Assumption 1.** _We let_ Γ ∶X ↦H _be a map from x_ ∈X _to a subspace_ H _s of dimension s_ ≥ 1 _of an RKHS_ H _as follows: given a projection operator P onto_ H _s,_ Γ( _x_ ) ≐ _PK_ ( _x,_ ⋅) _. Furthermore, all link functions gT ,_ { _gi_ } _[N] i_ =1 _are assumed linear_ H ↦ R _, i.e.,_ ∃ _wT ,wi_ ∈H _s s.t. gT_ (Γ( _x_ )) = ⟨ _wT ,_ Γ( _x_ )⟩H _, and gi_ (Γ( _x_ )) = ⟨ _wi,_ Γ( _x_ )⟩H _._ 

**Remark 1.** _Given an orthonormal basis (ONB) V_ = [ _v_ 1 _,...,vs_ ] _of_ H _s, we may rewrite gT_ (Γ( _x_ )) = _αT_[⊺] _[V]_[∗] _[K]_[(] _[x,]_[⋅)] _[,][i.e.,][for][α][T]_[∈][R] _[s][,][for][an][s][-dimensional][(nonlinear)][representation][V]_[∗][Γ][(] _[x]_[)][=] _[V]_[∗] _[K]_[(] _[x,]_[⋅)] _[of][x][.] The same is true for_ { _gi_ } _[N] i_ =1 _[with][respective]_[{] _[α][i]_[}] _[N] i_ =1 _[.][The][representations][are][non-unique,][although][their][corre-] sponding regression functions and_ H _s are unique (see Remark 3 below)._ 

**Remark 2.** _Since P is self-adjoint, we have fT_ ( _x_ ) ≐⟨ _PwT ,K_ ( _x,_ ⋅)⟩H _, hence by the reproducing property, fT_ = _PwT_ ∈H _s. Similarly, we have that all_ { _fi_ } _[N] i_ =1 _[are][in]_[H] _[s][.]_ 

5 

Remark 2 indicates that span ({ _fi_ } _i_ ∈[ _N_ ]) ⊆H _s_ . We therefore need the following _richness condition_ , similar to previous works on meta-learning in the linear representation case (Du et al., 2021), without which we cannot hope to learn H _s_ . 

**Assumption 2** (Source Richness) **.** _We have that_ span ({ _fi_ } _i_ ∈[ _N_ ]) = H _s._ 

**Remark 3.** _For any projection P onto some complete subspace_ H _s,_ ⟨⋅ _,PK_ ( _x,_ ⋅)⟩H _evaluates every function in_ H _s at x, and in fact is well-known as the kernel of the sub-RKHS defined by_ H _s. The same fact implies uniqueness of_ H _s and in particular that it equals_ span ~~{~~ Γ( _x_ ) ≐ _PK_ ( _x,_ ⋅)} _._ 

## **3.2 Learning Set-up** 

In this section we present the high level ideas of our meta-learning strategy with nonlinear representation. The first step is to learn a subspace approximation H[ˆ] _s_ ≈H _s_ from source tasks. This process aims to find a suitable representation that facilitates the learning of the target task. We refer to this step as **pre-training** . The second step involves directly learning the target task within the subspace H[ˆ] _s_ . We refer to this step as **inference** . 

**Source Tasks - pre-training.** Our approach to approximate H _s_ is inspired by Kong et al. (2020), who focused on finite-dimensional linear meta-learning. We extend this strategy to encompass (potentially infinite dimensional) nonlinear meta-learning. Under the source richness assumption (Assumption 2), H _s_ is equal to the range of the rank- _s_ operator (see Proposition 5 in Appendix) 

**==> picture [319 x 26] intentionally omitted <==**

Therefore, we estimate H _s_ via the range of 

**==> picture [293 x 26] intentionally omitted <==**

where _f_[ˆ] _i,λ_[′] _[,][f]_[ˆ] _[i,λ]_[are][i.i.d][copies][of][a][ridge][regression][estimator][for][source][task] _[i]_[∈[] _[N]_[]][.][Here,][we][use][a][data-] splitting strategy to obtain the following 

**==> picture [153 x 26] intentionally omitted <==**

This property plays a crucial role in deriving approximation rates for H _s_ . Data-splitting is similarly employed in Kong et al. (2020). Avoiding data-splitting remains an open problem even in the finite-dimensional linear representation setting. 

Each source task is learned from a dataset D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][of][i.i.d][observations][sampled][from] _[µ][i]_[,] via regularized kernel regression as in Eq. (1), 

**==> picture [439 x 27] intentionally omitted <==**

For task _i_ ∈[ _N_ ], let _Ki,Li_ ∈ R _[n]_[×] _[n]_ be the Gram matrices such that ( _Ki_ ) _j,l_ = _K_ ( _xi,j,xi,l_ ), ( _j,l_ ) ∈[ _n_ ] and ( _Li_ ) _j,l_ = _K_ ( _xi,j,xi,l_ ), ( _j,l_ ) ∈[ _n_ + 1 ∶ 2 _n_ ]. Then for all _x_ ∈X _,_ 

**==> picture [391 x 15] intentionally omitted <==**

where _ki,x_ = ( _K_ ( _xi,_ 1 _,x_ ) _,...,K_ ( _xi,n,x_ ))[⊺] ∈ R _[n]_ , _ℓi,x_ = ( _K_ ( _xi,n_ +1 _,x_ ) _,...,K_ ( _xi,_ 2 _n,x_ ))[⊺] ∈ R _[n]_ , _Yi_ = ( _yi,_ 1 _,...,yi,n_ )[⊺] ∈ R _[n]_ and _Yi_[′][= (] _[y][i,n]_[+][1] _[,...,y][i,]_[2] _[n]_[)][⊺][∈][R] _[n]_[.] 

6 

After obtaining _C_[ˆ] _N,n,λ_ , we cannot directly compare ran _CN_ to ran _C_[ˆ] _N,n,λ_ , since the latter is not guaranteed to be of rank _s_ . We therefore consider the singular value decomposition of _C_[ˆ] _N,n,λ_ : 

**==> picture [131 x 26] intentionally omitted <==**

where _γ_ ˆ1 ≥⋅⋅⋅≥ _γ_ ˆ _N_ ≥ 0 are the singular values and stored in the diagonal matrix _D_[ˆ] ∈ R _[N]_[×] _[N]_ . The right and left ˆ ˆ singular vectors are stored as _V_[ˆ] = [ _v_ 1 _,...,_ ˆ _vN_ ] and _U_[ˆ] = [ _u_ 1 _,...,_ ˆ _uN_ ], respectively. We use the right singular vectors to construct the approximation of H _s_ as follows (note that a similar approach can be applied to the left singular vectors), 

**==> picture [96 x 13] intentionally omitted <==**

We define the orthogonal projection onto H[ˆ] _s_ as _P_[ˆ] . 

**Remark 4.** _In nonparametric regression, as employed in this approach, regularization becomes necessary. This leads to biased estimators since_ E[ _f_[ˆ] _i,λ_ ] ≠ _fi. For subspace approximation, it is crucial to effectively control this bias since it cannot be averaged out._ 

**Target task - inference.** We are given a target task dataset D _T_ = {( _xT,j,yT,j_ ) _[n] j_ = _[T]_ 1[} ∈(X ×][R][)] _[n][T]_[sampled from] _µT_ in order to approximate _fT_ . As mentioned in Remark 3, H[ˆ] _s_ = _P_[ˆ] (H) ⊆H forms a RKHS on X having the same inner product as H and with reproducing kernel _K_[ˆ] ( _x,y_ ) = ⟨ _Pϕ_[ˆ] ( _x_ ) _,ϕ_ ( _y_ )⟩H _,_ ( _x,y_ ) ∈X[2] . Consequently, we can estimate _fT_ via regularized kernel regression within H[ˆ] _s_ , as shown in Eq. (1). For _λ_ ∗ > 0, 

**==> picture [345 x 26] intentionally omitted <==**

Since H[ˆ] _s_ is _s_ −dimensional, it can be treated as a standard regularized regression in R _[s]_ (see Section 3.3). The following remark highlights the main technical difficulties over the linear case. 

**Remark 5** (Differences from Linear Case) **.** _We point out that, while the algorithm used in our meta-learning approach draws inspiration from Kong et al. (2020), there are significant differences due to the complexities of the nonlinear setting, as opposed to the linear one, as outlined below._ 

_— First, from the algorithmic perspective, proper regularization is crucial in an infinite dimensional space to prevent overfitting. Kong et al. (2020) did not employ a regularization scheme, but instead relied on OLS regression, which does not directly extend to infinite dimension where some form of regularization is needed to control a learner’s capacity. A second algorithmic difference arises in the instantiation of the procedure in input space_ R _[d] : while our procedure appears similar to Kong et al. (2020)’s when described in the RKHS_ H _i.e., after embedding, its instantiating in_ R _[d] is nontrivial, as it involves translating operations in_ H _—e.g., projections onto subspaces of_ H _—into operations in_ R _[d] . Section 3.3 below addresses such technicality in depth._ 

_— Second, many crucial difficulties arise in the analysis of the infinite dimensional setting, which are not present in the finite-dimensional case. Importantly, in infinite dimensional space, the analysis effectively concerns two separate spaces: the RKHS_ H _which encodes the nonlinear representation, and the L_ 2 _regression space. Thus a main technical difficulty is to relate rates of convergence in_ H _(where all operations are taking place) to rates in L_ 2 _, in particular via the_ _**covariance operator** which links the two norms_ ∥⋅∥H _and_ ∥⋅∥ _L_ 2 _; this is relatively easy in finite dimension by simply assuming an identity covariance (or bounds on its eigenvalues) as done in Kong et al. (2020); Du et al. (2021); Tripuraneni et al. (2021), but such assumptions do not extend to infinite dimension where concepts such as "identity covariance" are not defined. Namely, an infinite dimensional covariance operator must be compact, which implies that its eigenvalues decay to zero. Our analysis reveals that the speed of that decay (encoded in Assumptions 3 and 4) determines the rate at which we can learn. Furthermore, unlike in Kong et al. (2020); Du et al. (2021); Tripuraneni et al. (2021), where there was no need to regularize the task-specific regressors, much of our analysis focuses on understanding the bias-variance_ 

7 

_trade-offs induced by the choice of regularizers. This is nontrivial but is crucial for guaranteeing gains in our nonlinear case, as explained in the paper’s introduction. Thus, in the present infinite dimensional setting, as we will see, such crucial trade-offs will depend on specific measures of smoothness—of the RKHS_ H _and the regression functions therein—as introduced in the main results Section 4.2 (see Assumptions 3, 4, 5)._ 

## **3.3 Instantiation in Data Space** 

In this section, we describe in detail the steps outlined in Section 3.2 to offer a comprehensive understanding of the computational process. In particular, we focus on the computation of the right singular vectors of _C_[ˆ] _N,n,λ_ , which plays a crucial role in constructing H[ˆ] _s_ . Additionally, we provide insights into the projection of new data points onto H[ˆ] _s_ , which is essential during the inference stage. We emphasize that such instantiations were not provided for kernel classes in the nonlinear settings addressed by Maurer et al. (2016); Du et al. (2021); given the nonconvexity of the loss (Eq. (1) in both papers), this task is nontrivial. 

**Singular Value Decomposition of** _C_[ˆ] _N,n,λ_ **.** We start by explaining how we can compute the SVD of _C_[ˆ] _N,n,λ_ in closed form from data. Let { _v_ ˆ _i_ } _[s] i_ =1[and][{] _[u]_[ˆ] _[i]_[}] _[s] i_ =1[be][the][right][and][left][singular][vectors][corresponding][to][the] ˆ ˆ largest _s_ singular values, and denote _V_[ˆ] _s_ = [ _v_ 1 _,...,_ ˆ _vs_ ] and _U_[ˆ] _s_ = [ _u_ 1 _,...,_ ˆ _us_ ]. The next proposition shows that ( _U_[ˆ] _s, V_[ˆ] _s_ ) can be obtained through the solution of a generalized eigenvalue problem associated to the matrices _J,Q_ ∈ R _[N]_[×] _[N]_ where for ( _i,j_ ) ∈[ _N_ ][2] 

**==> picture [260 x 32] intentionally omitted <==**

**Proposition 1.** _Consider the generalized eigenvalue problem which consists of finding generalized eigenvectors_ ( _α_[⊺] _,β_[⊺] )[⊺] ∈ R[2] _[N] and generalized eigenvalues γ_ ∈ R _such that_ 

**==> picture [135 x 27] intentionally omitted <==**

_Define A_ ≐[ _f_[ˆ] 1[′] _[,...,][f]_[ˆ] _N_[ ′][]] _[and][B]_[≐[] _[f]_[ ˆ][1] _[,...,][f]_[ˆ] _[N]_[]] _[and][let]_[{(] _[α]_[ˆ] _i_[⊺] _[,]_[ ˆ] _[β] i_[⊺][)][⊺][}] _i[s]_ =1 _[be][the][generalized][eigenvectors][associated] to the s_ − _largest generalized eigenvalues of the above problem and re-normalized such that αi_[⊺] _[Qα][i]_[=] _[β] i_[⊺] _[Jβ][i]_[=] ˆ 1 _,i_ ∈[ _s_ ] _. The following two families of vectors_ { _ui_ } _[s] i_ =1 _[and]_[{] _[v]_[ˆ] _[i]_[}] _[s] i_ =1 _[are][orthonormal][systems,][and][correspond] to top-s left and right singular vectors of C_[ˆ] _N,n,λ:_ 

**==> picture [237 x 27] intentionally omitted <==**

_In other words, we can define the projection onto the subspace_ H[ˆ] _s via_ { _v_ ˆ _i_ } _[s] i_ =1 _[:]_ 

**==> picture [194 x 13] intentionally omitted <==**

**Projection onto** H[ˆ] _s_ **and inference.** Next, we explain how we can project a new point onto H[ˆ] _s_ and perform inference on such representations. The projection onto H[ˆ] _s_ satisfies _P_[ˆ] = _V_[ˆ] _sV_[ˆ] _s_[∗][.][A][new][point] _[x]_[∈X][can][be] projected into H[ˆ] _s_ as _Pϕ_[ˆ] ( _x_ ) and identified to R _[s]_ via 

**==> picture [395 x 13] intentionally omitted <==**

By Proposition 1, _x_ ˜ can be computed as 

**==> picture [265 x 13] intentionally omitted <==**

8 

where _B_[∗] _ϕ_ ( _x_ ) ≐( _f_[ˆ] 1( _x_ ) _,..., f_[ˆ] _N_ ( _x_ ))[⊺] ∈ R _[N]_ . Recall that after pre-training, at inference, we receive a target task todatasetEq. (D8), _T_ = {(and _x_ by _T,j,yXT,jT_ )}≐[ _[n] j_ = _[T] x_ ˜1 _T,_[.] 1[We] _,...,_[denote] ˜ _xT,nT_ ][by] ∈ _[x]_[˜] R _[T,j][s]_[×] _[n]_[∈] _[T]_[R] _[s]_ the[the] data[embedding] matrix[of] that[the] collects[covariate] the _[x][T,j]_ embedded[into][H][ˆ] _[s]_[according] points as columns, _KT_ ≐ _XT_[⊺] _[X][T]_[∈][R] _[n][T]_[ ×] _[n][T]_[is][the][associated][Gram][matrix][and] _[n]_[−] _T_[1] _[X][T][ X] T_[⊺][∈][R] _[s]_[×] _[s]_[the][associated][empirical] covariance. 

**Proposition 2.** _f_[ˆ] _T,λ_ ∗ = _V_[ˆ] _sβT,λ_ ∗ _, where_ 

**==> picture [401 x 52] intentionally omitted <==**

## **4 Main Results** 

## **4.1 Regularity Assumptions** 

Our first two assumptions are related to the eigensystem of the covariance operator. For _i_ ∈[ _N_ ] ∪{ _T_ }, the covariance operator for task _i_ , Σ _i_ ≐ E _µi_ [ _ϕ_ ( _X_ ) ⊗ _ϕ_ ( _X_ )], is positive semi-definite and trace-class, and thereby admits an eigenvalue decomposition with eigenvalues _λi,_ 1 ≥ _λi,_ 2 ≥ _..._ ≥ 0 and eigenvectors {√ _λi,jei,j_ } _j_ ≥1 (Lemma 2.12 Steinwart and Scovel, 2012). 

**Assumption 3.** _For i_ ∈[ _N_ ] _, the eigenvalues of the covariance operator_ Σ _i from the_ ( _K,µi_ ) _pair satisfy a polynomial decay of order_ 1/ _p, i.e., for some constant c_ > 0 _and_ 0 < _p_ ≤ 1 _, and for all j_ ≥ 1 _, λi,j_ ≤ _cj_[−][1][/] _[p] . When the covariance operator has finite rank, we have p_ = 0 _._ 

The assumption on the decay rate of the eigenvalues is typical in the risk analysis for kernel ridge regression (see e.g., Fischer and Steinwart, 2020; Caponnetto and De Vito, 2007). 

**Assumption 4.** _There exist α_ ∈[ _p,_ 1] _and kα,_ ∞ > 0 _, such that, for any task i_ ∈[ _N_ ] _and µi_ − _almost all x_ ∈X _,_ ∑ _j_ ≥1 _λ[α] i,j[e]_[2] _i,j_[(] _[x]_[) ≤] _[k] α,_[2] ∞ _[.]_ 

This assumption is known as an _embedding property_ (into _L_ ∞, see Fischer and Steinwart (2020)), and is a regularity condition on the pair ( _K,µi_ ). In particular, let _TK,i_ ≐∑ _j λi,j ei,j_ ⊗ _L_ 2( _µi_ ) _ei,j_ denote the _integral operator L_ 2( _µi_ ) ↦ _L_ 2( _µi_ ) induced by _K_ , then the assumption characterizes the smallest _α_ such that the range of _TK,i[α]_[/][2][may][be][continuously][embedded][into] _[L]_[∞][(] _[µ][i]_[)][.][As][it][is][well-known][for][continuous][kernels,][ran] _[T]_[ 1] _K,i_[/][2][≡H][,] thus the assumption holds for _α_ = 1 whenever _K_ is bounded. Note that the _interpolation spaces_ ran _TK,i[α]_[/][2][only] get larger as _α_ → 0, eventually coinciding with the closure of span{ _ei,j_ } _j_ ≥1 in _L_ 2( _µi_ ). Additionally, it can be shown that Assumption 4 implies Assumption 3 with _p_ = _α_ (Lemma 10 Fischer and Steinwart, 2020). 

As alluded to in the introduction, _α_ has no direct benefit for regression in our _well-specified_ setting with _fi_ ∈H, but is beneficial in meta-learning (see Corollary 1 and Remark 11 thereafter). 

**Assumption 5.** _There exist r_ ∈[0 _,_ 1] _and R_ ≥ 0 _, such that for i_ ∈[ _N_ ] _, the regression function fi associated with µi is an element of_ H _and satisfies_ ∥Σ[−] _i[r][f][i]_[∥][H][ ≐] _[R]_[ < ∞] _[.]_ 

This assumption, imposing smoothness on each source task regression function, is standard in the statistical analysis of regularized least-squares algorithms (Caponnetto and De Vito, 2007). 

9 

**Remark 6.** _Assumptions 3, 4, and 5 only concern the source tasks towards nonlinear meta-learning. We will see in Section 4.2 that they are complementary in ensuring enough_ _**smoothness** of the source regression functions to allow for sufficient_ _**under-regularization** to take advantage of the aggregation of N source tasks. Thus, the main assumption on the target task is simply that it shares the same nonlinear representation as the source tasks._ 

Finally, to control the noise we assume the following. 

**Assumption 6.** _There exists a constant Y_ ∞ ≥ 0 _such that for all Y_ ∼ _µi,i_ ∈[ _N_ ] ∪{ _T_ } _:_ ∣ _Y_ ∣< _Y_ ∞ _._ 

## **4.2 Main Theorems** 

**Theorem 1.** _Under Assumptions 1, 2 and 6 with s_ ≥ 1 _, for τ_ ≥ 2 _._ 6 _,_ 0 < _λ_ ∗ ≤ 1 _and_ 

**==> picture [110 x 13] intentionally omitted <==**

_with probability not less than_ 1 − 3 _e_[−] _[τ] and conditionally on_ {D _i_ } _[N] i_ =1 _[,]_ 

**==> picture [222 x 26] intentionally omitted <==**

_where P_[ˆ] ⊥ ≐ _I_ H − _P_[ˆ] _and c_ 0 _is a constant that depends only on Y_ ∞ _,_ ∥ _fT_ ∥H _, and κ. Hence, treating τ as a constant, if we take λ_ ∗ = 12 _κ_[2] (log( _s_ )∨ _τ_ ) _n_[−] _T_[1] _[,][conditionally][on]_[{D] _[i]_[}] _[N] i_ =1 _[,][for][n][T]_[≥][12] _[κ]_[2][(][log][(] _[s]_[)][∨] _[τ]_[)] _[,][we][get][that]_[E] _[µ] T_[(][ ˆ] _[f][T,λ]_ ∗[)] _is of the order_ 

**==> picture [70 x 26] intentionally omitted <==**

Theorem 1 reveals that the excess risk for the target task consists of two components: √ _s_ / _nT_ due to the inference stage, and ∥ _P_[ˆ] ⊥ _P_ ∥ in the pre-training stage. In the upcoming Theorem 2, we will see that the pretraining error ∥ _P_[ˆ] ⊥ _P_ ∥ decays with _n_ and _N_ . In other words, if either _N_ (number of tasks) or _n_ (number of data within each task) is sufficiently large, we can guarantee that the excess risk decays at the parametric rate _O_ (√ _s_ / _nT_ ), an optimal rate achieved only by performing linear regression in a space of dimension _s_ . ∥ _P_[ˆ] ⊥ _P_ ∥ is the sin-Θ distance between H _s_ and H[ˆ] _s_ Stewart and Sun (1990). We can relate this distance to the difference between _CN_ and _C_[ˆ] _N,n,λ_ using classic perturbation theory for singular vectors. Proposition 3 is a basic generalization of Wedin’s sin −Θ Theorem Wedin (1972). 

**Proposition 3** (Wedin’s sin −Θ Theorem) **.** _Given CN and C_[ˆ] _N,n,λ defined in Eqs._ (3) _and_ (4) _, with γs smallest nonzero eigenvalues of CN . We have,_ 

**==> picture [302 x 14] intentionally omitted <==**

We refer to Section A.2 in the Appendix for the proof. Note that the operator norm ∥ _C_[ˆ] _N,n,λ_ − _CN_ ∥ is dominated by the Hilbert-Schmidt norm ∥ _C_[ˆ] _N,n,λ_ − _CN_ ∥ _HS_ . The following theorem provides high probability bounds on this quantity. 

**Theorem 2.** _Let Assumptions 3, 4, 5 and 6 hold with parameters_ 0 < _p_ ≤ _α_ ≤ 1 _and r_ ∈[0 _,_ 1] _. Let τ_ ≥ log(2) _, N_ ≥ _τ and_ 0 < _λ_ ≤ 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _. Define the following terms:_ 

**==> picture [170 x 30] intentionally omitted <==**

10 

_where c only depends on kα,_ ∞ _,D,κ. We require n_ ≥ _Aλ if r_ ∈(0 _,_ 1/2] _or n_ ≥ _Bλ if r_ ∈(1/2 _,_ 1] _. Under both scenarios, with probability greater than_ 1 − 2 _e_[−] _[τ]_ − _o_ (( _nN_ )[−][10] ) _over the randomness in the source tasks we have_ 

**==> picture [362 x 30] intentionally omitted <==**

_where C_ 1 _only depends on Y_ ∞ _, R, κ, p and kα,_ ∞ _._ 

We highlight two key aspects of Theorem 2. First, the bound is comprised of two terms that come from a bias-variance decomposition (refer to Section 6 for details): 

**==> picture [294 x 28] intentionally omitted <==**

The first and second terms in Eq. (10) correspond to bounds on the variance and on the bias respectively. Secondly, while we obtain the same upper bound in Eq. (10) for the two distinct scenarios _r_ ∈(0 _,_ 1/2] and _r_ ∈(1/2 _,_ 1], the requirement on the number of training samples per task is different. In particular, _Bλ_ ≥ _Aλ_ , since _λ_ ≤ 1 and _p_ + 1 ≥ _α_ . This means that we can benefit from further smoothness _r_ > 1/2, but at the cost of a higher number of samples per source task. Our analysis in Theorem 9 implies that the difference comes from bounding the bias term. We specifically shows that uniformly bounding the bias from each task when _r_ ∈(1/2 _,_ 1] (require _n_ ≥ _Bλ_ ) is strictly harder than when _r_ ∈(0 _,_ 1/2] (require _n_ ≥ _Aλ_ ). As such, our results reveal the inherent difficulty of nonlinear meta-learning: analyzing the bias is more involved than analyzing the variance, a fact which cannot be seen in the linear representation case. 

**Remark 7** (Further Smoothness and the Well-specified Regime) **.** _While in usual analyses, consistency in L_ 2 _norm is assured for r_ = 0 _(implying that the regression function is in_ H _), we require further smoothness on source regression functions (i.e., r_ > 0 _) to guarantee consistency in our setting. The requirement for additional smoothness stems from the fact that the result depends on convergence of regression estimates in_ _**the stronger RKHS norm** rather than in L_ 2 _norm, as the above_ ∥⋅∥ _HS and projections are defined w.r.t. the RKHS itself._ 

_We point out that in kernel learning literature (see e.g., Caponnetto and De Vito (2007); Fischer and Steinwart (2020)), one often observes the Tikhonov saturation effect, where the learning rate does not improve for r_ > 1/2 _. However, we remark that this saturation happens only when the L_ 2 _norm is used. In particular, Eq._ (10) _demonstrates that our learning rate can be improved up to r_ = 1 _. This reflects the fact that, if the RKHS norm is employed, the Tikhonov saturation effect happens for r_ > 1 _. A similar phenomenon is observed by Blanchard and Mücke (2018)._ 

Combining Theorem 1, Proposition 3, and Eq. (10) from Theorem 2, we obtain the following results on the meta-learning excess risk. 

**Corollary 1.** _Under the assumptions of Theorem 1 and Theorem 2, for τ_ ≥ 2 _._ 6 _and λ_ ∗ = 12 _κ_[2] (log( _s_ )∨ _τ_ ) _n_[−] _T_[1] _[,] with probability_ 1 − 5 _e_[−] _[τ]_ − _o_ (( _nN_ )[−][10] ) _over the randomness in both the source and target tasks, we have the following regimes of rates for a constant C_ 3 _that only depends on Y_ ∞ _, R, κ, γ_ 1 _, p, c,_ ∥ _fT_ ∥H _and kα,_ ∞ _._ 

_A._ **Small number of tasks.** _In this regime, with the number of tasks N being small, the variance is significant compared to the bias. Therefore, we must choose λ to balance the order of the bias with that of the variance. If N_ ≤ _n_ 2 _r_ + _α_ 1+ _p_ −1 _and r_ ∈(0 _,_ 1/2] _or N_ ≤ _n_ 2 _rp_ ++11+ _p_ −1 _and r_ ∈(1/2 _,_ 1] _, for a choice of λ_ = (log2( _nN_ )/( _nN_ )) 2 _r_ +11+ _p ,_ 

**==> picture [344 x 31] intentionally omitted <==**

_B._ **Large number of tasks.** _In this regime, we consider larger N (see B._ 1 _and B._ 2 _below), so that the variance term becomes negligible compared to the bias. Therefore the rates below correspond to the choices of_ 

11 

_λ that minimize the bias, in Eq._ (10) _(under the constraints n_ ≥ _Aλ,Bλ). In what follows, ω_ > 2 _is a free parameter._ 

**==> picture [352 x 56] intentionally omitted <==**

**==> picture [358 x 56] intentionally omitted <==**

**Remark 8** (Saturation effect on large _N_ ) **.** _Corollary 1 shows no further improvement from larger N once N_ ≥ _n_ 2( _r_ ∧1 _α_ /2)+1+ _p_ −1 _, since the rates then only depend on n (as outlined in case B). This is due to a saturation effect from the bias-variance trade-off, i.e., N only helps decrease the variance term below the best achievable bias; at that point the bias (within each task) can only be further improved by larger per-task sample size n._ 

**Remark 9** (Regime _N_ ≳ exp( _n_ )) **.** _The regimes presented in Corollary 1 only cover settings where N_ ≲ exp( _n_ ) _, which is in fact the only regime covered by previous works (see, for instance Du et al. (2021); Tripuraneni et al. (2020)). This is due to the constraints n_ ≥ _Aλ,Bλ, that prevents N_ ≳ exp( _n_ ) _. However, at the cost of a less tight rate we can obtain a bound on the pre-training error that is free of any constraint on n (see Section A.6). As a corollary of this theorem, when N_ ≳ exp( _n_ ) _, choosing λ_ = _n_[−] 2[1] _, results in the nontrivial rate_ 

**==> picture [114 x 26] intentionally omitted <==**

_Notice that this is a slower rate than shown for smaller N in regime B of Corollary 1. Tightening the rates in the regime of N_ ≳ exp( _n_ ) _appears difficult, and is left as an open problem. We emphasize, as stated earlier, that this regime is in fact not addressed by previous works, even under the stronger assumption of linear representations._ 

**Regimes of Gain.** We want to contrast our results in the meta-learning setting with the rates obtainable on the target task without the benefits of source tasks. Since no regularity condition is imposed on the target distribution, the best target rate, absent any source tasks, is of the form _O_ ( _n_[−] _T_[1][/][4] ) (see e.g., Caponnetto and De Vito, 2007)[2] ; thus we gain from the source tasks whenever E _µT_ ( _f_[ˆ] _T,λ_ ∗ ) = _o_ ( _n_[−] _T_[1][/][4] ). Our interest, however, is in _regimes where the gain is greatest_ , in that the source tasks permit a final metalearning rate of E _µT_ ( _f_[ˆ] _T,λ_ ∗ ) ≲ √ _s_ / _nT_ ; Corollary 1 displays such regimes according to the number of source samples _N_ and _n_ , and the parameters _r_ , _α_ and _p_ , denoting the difficulty of the sources tasks. While it is clear that larger _r_ indicates _**smoother**_ source regression functions _fi_ as viewed from within the RKHS H, smaller parameters _α_ and _p_ can be understood as a _**smoothness level**_ of the RKHS H itself—e.g., consider a Sobolev space H of _m_ -smooth functions, then we may take _α,p_ ∝ 1/ _m_ (see Example 3). Thus the smoother the source tasks, viewed under _r_ , _α_ and _p_ , the faster the rates we can expect, since our approach aims at reducing the bias in each individual task (which is easiest under smoothness see Remark 10 below). Focusing on the situation where the number of samples per task is roughly the same across source and target, i.e., _n_ ∝ _nT_ , the conditions for meta-learning to provide the greatest gain, i.e., achieving _O_ ( _n_[−][1][/][2] ) rate, under various regimes are listed in Table 1. 

> 2Note that the assumption that _fT_ is in some subspace H _s_ is irrelevant for usual kernel ridge regression, since it is always true once we know that _f_ belongs to H. 

12 

Table 1: Conditions for meta-learning to reach the parametric rate _O_ (√ _s_ / _n_ ), log terms are removed for clarity. 

|ons for me|ta-learning to reach the para|ta-learning to reach the para|ta-learning to reach the para|metric rate_O_ (<br>|_s_/_n_), log terms are re|
|---|---|---|---|---|---|
|**Cases**|**Range of Source Tasks**|||**Choice of** _λ_|**Regimes of Gain**|
|A|_n_|2|_r_+1+_p_<br>2_r_<br>−1≤_N_ ≤_n_<br>2_r_+1+_p_<br>_α_<br>−1|(_nN_)−<br>1<br>2_r_+1+_p_|_α_<br>2 ≤_r_≤1<br>2|
|||||||
|A|_n_|2|_r_+1+_p_<br>2_r_<br>−1≤_N_ ≤_n_<br>2_r_+1+_p_<br>_p_+1<br>−1|(_nN_)−<br>1<br>2_r_+1+_p_|_p_+1<br>2<br>≤_r_≤1|
|||||||
|B.1||_n_|2_r_+1+_p_<br>_α_<br>−1≤_N_ ≤_o_(_en_)|_n_−_r_<br>_α_|_α_<br>2 ≤_r_≤1<br>2|
|B.2||_n_|2_r_+1+_p_<br>_p_+1<br>−1≤_N_ ≤_o_(_en_)|_n_−<br>_r_<br>_p_+1|_p_+1<br>2<br>≤_r_≤1|



**Remark 10** (Under-regularization/Overfitting) **.** _In order for meta-learning to provide gain, in particular for n_ ∝ _nT , we have to_ _**overfit** the regression estimates in each source task, i.e., set λ lower than would have been prescribed for optimal regression (choices of λ for the different regimes of gain are summarized in Table 1)._ 

_Overfitting is essential because, as highlighted in the introduction, the bias inherent in each task during metalearning cannot be averaged out. Deliberate under-regularization reduces this bias at the expense of increased variance within each task. However, the variance in the target task may subsequently be mitigated by aggregating across multiple tasks._ 

_More specifically, in the regimes of gain discussed earlier, the choices of λ in Corollary 1 are consistently lower than the optimal regression choice of λKRR_ ≍ _n_ − 2( _r_ ~~∧~~ 1/12)+1+ _p (see e.g., Fischer and Steinwart, 2020, Theorem 1) in the well-specified regime. This deviation from the optimal regression setting indicates overfitting, which again reveals that understanding nonlinear meta-learning is fundamentally more difficult than the linear setting due to the bias term. This effect is similarly observed in nonparametric kernel regression when splitting the dataset and averaging estimators trained on each split of the dataset Zhang et al. (2015)._ 

**Remark 11** (Regularity beyond regression) **.** _Notice that the choice of the regularization parameter in kernel ridge regression λKRR_ ≍ _n_ − 2( _r_ ~~∧~~ 1/12)+1+ _p has no direct dependence on α: lower values of_ 0 < _α_ ≤ 1 _yield no further benefit in regression once we assume fi_ ∈H _, as opposed to the misspecified setting where fi lies outside_ H[3] _. By contrast, in meta-learning, we do benefit from considering α, as α governs both the threshold level at which the saturation effect on large N kicks in (see Remark 8) and the level of smoothness required for meta-learning to provide the greatest gain (See Table 1 and associated discussion). Ultimately, if α_ → 0 _, there is no saturation effect, and the rates always match the parametric rate O_ ( _n_[−][1][/][2] ) _. This indicates that subspace learning is a fundamentally different problem to ridge regression._ 

**Characterizing** _α_ **,** _p_ **and** _r_ **.** As discussed above, smaller parameters _α_ and _p_ and higher parameter _r_ yield faster meta-learning rates. The next examples yield insights on these situations. Throughout, recall that by Lemma 10 Fischer and Steinwart (2020), we have _p_ ≤ _α_ , i.e., _p_ = _α_ is always admissible. **Example 1** (Finite-dimensional kernels) **.** _Suppose_ H _is finite dimensional, i.e., the covariance operators_ Σ _i each admit a finite number of eigenfunctions ei,j,j_ = 1 _,_ 2 _,...k for some k_ ≥ 1 _. Then clearly as the eigenfunctions_ { _ei,j_ } _are bounded_[4] _and Assumptions 3-4 hold for α,p_ = 0 _. Furthermore, Assumption 5 holds for any value of r. In this regime,_ 

**==> picture [327 x 27] intentionally omitted <==**

_See Remark 13 in the Appendix for the detailed derivations. As an example, for polynomial kernels K_ ( _x,x_[′] ) ≐ ( _x_[⊺] _x_[′] + _b_ ) _[m] on compact domains_ X ⊂ R _[d] , we obtain k_ = _d[m] . Note that, since polynomial regression converges_ 

> 3Note, however, that _p_ ≤ _α_ , and therefore a small _α_ implies that we are in the small _p_ regime (and the rates do depend on _p_ ). 

> 4As we employ a bounded kernel, every function in the RKHS is bounded (Lemma 4.23 Steinwart and Christmann (2008)). 

13 

_at rate O_ (√ _d[m]_ / _nT_ ) _(see e.g., Ghorbani et al., 2021; Chen and Meka, 2020; Andoni et al., 2014; Zippel, 1979), we can gain in meta-learning whenever the representation_ H _s is of dimension s_ ≪ _d[m] ._ 

**Remark 12** (Subspace learning guarantees in the linear setting) **.** _In the meta learning model with linear representations, with d the dimension of the input points and s the dimension of the subspace, Tripuraneni et al. (2021) (Theorem 5) provide an information-theoretic lower bound on the_ sin −Θ _distance_ ∥ _P_[ˆ] ⊥ _P_ ∥ _of the order_ √ _nNds[valid][for][estimators][that][are][functions][of][the][ nN][data][points.][Assuming][that][the][eigenvalues][of][ C][N] are well-conditioned (γs_ ≍ _s_[−][1] _), estimators with matching guarantees on the_ sin −Θ _distance are obtained in Du et al. (2021); Niu et al. (2024). By the previous example, if we employ a linear kernel on_ R _[d] and under the ds_[2] _assumption γs_ ≍ _s_[−][1] _, we obtain a subspace learning error (up to a log term) of_ √ _nN[,][recovering][the][learning] rate obtained in Tripuraneni et al. (2021). Generalizing the result of Tripuraneni et al. (2021) to the nonlinear setting with a lower bound depending on the parameters_ ( _N,n,s,p,r,α_ ) _represents a significant and valuable direction for future research._ 

**Example 2** (Gaussian kernel) **.** _Let_ X ⊂ R _[d] be a bounded set with Lipschitz boundary_[5] _, µ a distribution supported on_ X × R _, with marginal distribution uniform on_ X _and let K be a Gaussian kernel. Then by (Corollary 4.13 Kanagawa et al., 2018), Assumption 4 is satisfied with any α_ ∈(0 _,_ 1] _, implying that Assumption 3 is also satisfied with any p_ ∈(0 _,_ 1] _._ 

**Example 3** (Sobolev spaces and Matérn kernels) **.** _Let_ X ⊂ R _[d] , be a non-empty, open, connected, and bounded set with a C_ ∞− _boundary. Let µ be a distribution supported on_ X × R _, with marginal equivalent to the Lebesgue measure on_ X _. Choose a kernel which induces a Sobolev space H[m] of smoothness m_ ∈ N _with m_ > _d_ /2 _, such as the Matérn kernel (see e.g., Kanagawa et al. (2018) Examples 2.2 and 2.6). Then by Fischer and Steinwart d (Corollary 5 2020), Assumption 3 is satisfied with p_ = 2 _m[and][Assumption][4][is][satisfied][for][every][α]_[ ∈(] 2 _[d] m[,]_[1][]] _[.] Furthermore, it can be shown that Assumption 5 is satisfied if and only if the_ { _fi_ } _[N] i_ =1 _[belong][to][a][Sobolev][space] (with fractional smoothness) of smoothness m_ (2 _r_ + 1) _(see Fischer and Steinwart (2020))._ 

## **5 Experimental Results** 

In this section, we report the results of experiments on simulated data to test the two main theoretical predictions of our paper: 1) with the proper number of tasks it is possible to learn at the parametric rate; 2) overfitting is beneficial for meta learning. Consider the Sobolev space H = { _f_ ∶[0 _,_ 1] → R _,f_ absolutely continuous _,f_[′] ∈ 1 _L_[2] ([0 _,_ 1]) _,f_ (0) = 0} _,_ equipped with the inner product ⟨ _f,g_ ⟩H = ∫0 _[f]_[ ′][(] _[x]_[)] _[g]_[′][(] _[x]_[)] _[dx.]_[H][is][the][RKHS][associated] to the kernel _K_ ∶[0 _,_ 1] × [0 _,_ 1] → R _,_ ( _x,x_[′] ) ↦ min( _x,x_[′] ) Gu and Gu (2013). For a fixed parameter _s_ ∈ N, we consider an orthonormal system (with respect to ⟨⋅ _,_ ⋅⟩H) of _s_ splines of degree 2 (i.e. piecewise quadratic functions with continuous derivative) ( _ψ_ 1 _,...,ψs_ ) as shown in Figure 1. We then take H _s_ = span{ _ψ_ 1 _,...,ψs_ } and _P_ = ∑ _[s] j_ =1 _[ψ][j]_[⊗] _[ψ][j]_[the][projection][onto][H] _[s]_[.][Note][that] _[P]_[=] _[ V V]_[∗][with] _[V]_[= [] _[ψ]_[1] _[,...,ψ][s]_[]][.][Any] _[ω]_[ ∈][R] _[s]_[leads][to] an element of H _s_ as, 

**==> picture [478 x 57] intentionally omitted <==**

**==> picture [240 x 13] intentionally omitted <==**

Throughout the experiments, _σ_ is fixed to 0.1. In Figure 1, we display an example of generated task for _s_ = 10. Given an estimator _f_[ˆ] for the target task, we evaluate its performance by approximating the squared excess risk E _µT_ [( _f_[ˆ] ( _X_ ) − _fT_ ( _X_ ))[2] ] on independent samples, where _µT_ is the Lebesgue measure on [0 _,_ 1]. 

> 5For the definition of Lipschitz boundary see (Definition 3 Kanagawa et al., 2020). 

14 

**==> picture [144 x 91] intentionally omitted <==**

**==> picture [144 x 91] intentionally omitted <==**

**==> picture [143 x 91] intentionally omitted <==**

Figure 1: (Left)-(Center) Orthonormal system in H spanning H _s_ for respectively _s_ = 3 (Left) and _s_ = 10 (Center). (Right) Example of sampled task for _s_ = 10 with 300 datapoints, the blue solid line represents the ground truth. 

**Parameter values:** _p_ **,** _α_ **and** _r_ **.** As the marginal probability distribution is the uniform measure on [0 _,_ 1] and _K_ induces a Sobolev space of smoothness _m_ = 1, by Remark 3, Assumption 3 is satisfied with _p_ = 2[1][and] Assumption 4 is satisfied with every _α_ ∈( 2[1] _[,]_[1][]][.][Finally,][tasks][functions][are][generated][as][linear][combinations] of order 2 splines and therefore belong to _H[m]_ (0 _,_ 1) for every _m_ <[5] 2[(and][do][not][belong][to] _[H][m]_[(][0] _[,]_[1][)][for][any] _m_ ≥[5][By Remark][ 3][, Assumption][ 5][ is therefore satisfied for every] _[ r]_[ ∈[][0] _[,]_[3] 2[).] 4[)][ (and Assumption][ 5][ is not satisfied] for any _r_ ≥[3] 4[).][In][the][experiments,][we][set] _[r]_[ =][1] 2[.] 

**Choice of regularization.** We focus on the **small number of tasks regime** , Corollary 1-(A), where _N_ ≤ _n_ 2 _r_ + _α_ 1+ _p_ −1 = _n_ 4. According to Case A, we set _λ_ = ( _nN_ )− 2 _r_ +11+ _p_ = ( _nN_ )[−] 5[2] and _λ_ ∗ = _n_[−] _T_[1][.][By][Corollary][1][,][the] excess risk on the target task is upper bounded (up to constants and log terms) by √ _s_ / _nT_ + ( _nN_ )[−] 5[1] . 

**Learning at the parametric rate.** We have shown in Table 1 that given enough source tasks and samples per source task it is possible to learn at the parametric rate √ _s_ / _nT_ . To illustrate this fact, we compare our meta learning approach to an oracle estimator accessing the true subspace. The oracle estimator has access to ( _ψ_ 1 _,...,ψs_ ) and is trained with linear ridge regression. For _x_ ∈[0 _,_ 1], define its transform _x_ ˜ _[s]_ ≐ ( _ψ_ 1( _x_ ) _,...,ψs_ ( _x_ ))[⊺] ∈ R _[s]_ . Then, _f_[ˆ] oracle( _x_ ) ≐ _β_[ˆ][⊺] _x_ ˜ _[s]_ , with 

**==> picture [206 x 25] intentionally omitted <==**

For _λ_ oracle = _n_[−] _T_[1][,][E] _[µ] T_[(] _[f]_[ ˆ][oracle][)][is][of][the][order] √ _s_ / _nT_ Mourtada and Rosasco (2022). In Figure 2-(Left), for _s_ = 25 and _n_ = 300 we show the evolution of the squared excess risk as we vary _nT_ for the oracle estimator and our meta learning estimator trained with different values of _N_ . Results are averaged over 100 runs, where for each run we sample new source and target tasks. For _N_ = 250, the performance of the meta learning is identical to the oracle. It demonstrates that our meta learning strategy successfully leverages the source tasks and that given enough source tasks, it learns at a similar rate of the oracle estimator, leading to a parametric rate of convergence. We refer to Section D for additional results. 

**Effect of overfitting.** To assess the effect of overfitting (see Remark 10), we compare our meta learning approach trained with _λ_ 1 = ( _nN_ )[−] 5[2] and _λ_ 2 = _n_[−] 5[2] . In Figure 2-(Right), for _s_ = 25, _n_ = 300 and _nT_ = 5000, we plot the evolution of the squared excess risk as we increase _N_ for _λ_ 1 (red dotted line) and _λ_ 2 (blue solid line). Results are averaged over 100 runs. It confirms the message of Remark 10 that overfitting (with respect to the usual regularization of kernel ridge regression) on each source task is beneficial for meta learning. We refer to Section D for additional results. 

15 

**==> picture [215 x 130] intentionally omitted <==**

**==> picture [216 x 130] intentionally omitted <==**

Figure 2: **(Left)** Meta Learning versus Oracle: Comparison of the squared excess risk on the target task for the oracle estimator _f_[ˆ] oracle (dotted red line) and the meta learning estimator _f_[ˆ] _T,λ_ ∗ trained with different number of tasks _N_ (solid lines). _x_ −axis represents the size of the dataset for the target task ( _nT_ ). **(Right)** Effect of under-regularization: Comparison of the squared excess risk of the meta learning estimator trained with _λ_ = ( _nN_ )[−] 5[2] (red dotted line) and _λ_ = _n_[−] 5[2] (blue solid line). _x_ −axis represents the number of source tasks ( _N_ ). For both figures _n_ = 300, _s_ = 25 and results are averaged over 100 generations of the source and target tasks. 

## **6 Analysis Outline** 

To prove Theorem 2, we proceed with a bias-variance decomposition: 

**==> picture [371 x 27] intentionally omitted <==**

where _C_[¯] _N,n,λ_ ≐ _N_[1][∑] _[i]_[ E][(][ ˆ] _[f][i,λ]_[) ⊗][E][(][ ˆ] _[f][i,λ]_[)][.][Next][we][consider][both][of][these][terms][separately.] 

● The variance term can be written as follows 

**==> picture [161 x 28] intentionally omitted <==**

with _ξi_ ≐ _f_[ˆ] _i,λ_[′][⊗] _[f]_[ˆ] _[i,λ]_[ −][E][(][ ˆ] _[f][i,λ]_[) ⊗][E][(][ ˆ] _[f][i,λ]_[)] _[,i]_[∈[] _[N]_[]][.][Thus,][the][variance][term][being][an][average][with][mean][0][,][we] would naturally want to bound it via a concentration inequality. However, this requires _ξi_ to be well behaved, e.g., bounded or subgaussian. A naive upper bound on ∥ _ξi_ ∥ _HS_ is of the order ∥ _f_[ˆ] _i,λ_[′][∥][H][⋅∥] _[f]_[ˆ] _[i,λ]_[∥][H][≤] _[λ]_[−][1][(see] Proposition 10); however this would lead to a loose concentration bound on the variance term, in particular, such a bound would not go down with the per-task’s sample size _n_ . 

Therefore, we first establish a high probability bound on ∥ _ξi_ ∥ _HS_ in terms of _n_ and _λ_ as follows. First, recall _fi,λ_ from Eq. (2), and let _ηi_ ≐ _f_[ˆ] _i,λ_[′][⊗] _[f]_[ˆ] _[i,λ]_[ −] _[f][i,λ]_[ ⊗] _[f][i,λ]_[whereby] _[ξ][i]_[ =] _[ η][i]_[ −][E][[] _[η][i]_[]][.][With][some][algebra][we][can][get] 

**==> picture [324 x 14] intentionally omitted <==**

From existing results on kernel ridge regression (see e.g., Fischer and Steinwart, 2020), we can bound ∥ _f_[ˆ] _i,λ_ − _fi,λ_ ∥H in terms of both _n_ and _λ_ , in high-probability. This leads to a high probability bound on ∥ _ξi_ ∥ _HS_ that takes the form P (∥ _ξi_ ∥ _HS_ ≤ _V_ ( _δ,n,λ_ )) ≥ 1 − 2 _e_[−] _[δ]_ for all _δ_ ≥ 0 and _i_ ∈[ _N_ ] (see Theorem 8 in Section A.3 for details). Define the event _EN,δ,n,λ_ = ∩ _i_ ∈[ _N_ ] _Ei,δ,n,λ_ where _Ei,δ,n,λ_ ≐{∥ _ξi_ ∥ _HS_ ≤ _V_ ( _δ,n,λ_ )}. We then have 

**==> picture [376 x 28] intentionally omitted <==**

16 

For the first term on the r.h.s, we can now apply Hoeffding inequality (Theorem 15) since _ξi_ conditionally on _EN,δ,n,λ_ is bounded. However, conditioning on _EN,δ,n,λ_ , the variable _ξi_ may no longer have zero mean, a requirement for usual concentration arguments. We therefore proceed by first centering _ξi_ around E( _ξi_ ∣ _EN,δ,n,λ_ ) = E ( _ξi_ ∣ _Ei,δ,n,λ_ ) (by independence of the source tasks), and upper-bounding this expectation as 

**==> picture [367 x 14] intentionally omitted <==**

where we used the upper bound _λ_[−][1] on ∥ _ξi_ ∥ _HS_ . Then, applying Hoeffding inequality to the first term, we obtain with probability greater than 1 − 2 _e_[−] _[τ]_ − 2 _Ne_[−] _[δ]_ , 

**==> picture [290 x 28] intentionally omitted <==**

by choosing _δ_ (a free parameter) as 12log( _nN_ ). In that way, for our choices of _λ_ (see Corollary 1), ( _λN_[12] _n_[12] )[−][1] is always of lower order and 2 _Ne_[−] _[δ]_ = _o_ (( _nN_ )[−][10] ). Our choice of _V_ ( _δ,n,λ_ ) is given in Theorem 13 (leading to Eq. (10)), with the constraint that _n_ ≥ _Aλ_ (see Theorem 2 for the definition of _Aλ_ ). For the detailed proof of the variance bound, please refer to Theorem 8 in Section A.3. 

● To bound the bias, we first notice that it can be decomposed in the following way 

**==> picture [181 x 26] intentionally omitted <==**

The key is therefore to obtain a good control on ∥ _fi_ − E( _f_[ˆ] _i,λ_ )∥H. We consider two different ways of bounding this term, commensurate with regimes of _r_ . 

— When _r_ ∈(0 _,_ 1/2], we proceed as follows, 

**==> picture [424 x 100] intentionally omitted <==**

For _n_ ≥ _Aλ_ , with probability over 1 − 2 _e_[−] _[δ]_ —where _δ_ is chosen as discussed for the variance bound—we can show that ∥( _I_ + Σ _i,λ_[−][1][/][2][(][ˆΣ] _[i]_[ −][Σ] _[i]_[Σ][−] _i,λ_[1][/][2][)][−][1][∥≤][3][,][whereby][we][get][with][the][same][probability][∥] _[f][i]_[ −][E][(][ ˆ] _[f][i,λ]_[)∥][H][≤][3] _[λ][r]_[.] Thus, conditioning on this event, we get a final bound 

**==> picture [147 x 14] intentionally omitted <==**

**==> picture [333 x 15] intentionally omitted <==**

— When _r_ ∈(1/2 _,_ 1], we proceed as follows, 

**==> picture [258 x 50] intentionally omitted <==**

We then use the following derivation 

**==> picture [303 x 17] intentionally omitted <==**

We are left with bounding the term E∥( _I_ −(Σ _i_ − Σ[ˆ] _i_ )Σ[−] _i,λ_[1][)][−][1][∥][which can be obtained by using a Neumann series.] For a detailed analysis of the bias, see Theorem 9 of Section A.3 

17 

## **7 Conclusion** 

We address the problem of meta-learning with nonlinear representations, providing theoretical guarantees for its effectiveness. Our study focuses on the scenario where the shared representation maps inputs nonlinearly into an infinite dimensional RKHS. By leveraging the smoothness of task-specific regression functions and employing careful regularization techniques, the paper demonstrates that biases introduced in the nonlinear representation can be mitigated. Importantly, the derived guarantees show that the convergence rates in learning the common representation can scale with the number of tasks, in addition to the number of samples per task. The analysis extends previous results obtained in the linear setting, and highlights the challenges and subtleties specific to the nonlinear case. The findings presented in this work open up several avenues for future research, which include: exploration of different types of nonlinear representations beyond RKHS, alternative subspace estimation techniques, and further refinement of trade-offs between bias and variance. 

## **Acknowledgements** 

Dimitri Meunier, Zhu Li, and Arthur Gretton were supported by the Gatsby Charitable Foundation. Zhu Li is also funded by Imperial College London through the Chapman Fellowship. Samory Kpotufe is thankful for support from NSF CNS-2334997, and a Sloan 2021 Fellowship over the bulk of this study. 

## **References** 

- Maryam Aliakbarpour, Konstantina Bairaktari, Gavin Brown, Adam Smith, Nathan Srebro, and Jonathan Ullman. Metalearning with very few samples per task. In _**The Thirty Seventh Annual Conference on Learning Theory**_ , pages 46–93. PMLR, 2024. 

- Alexandr Andoni, Rina Panigrahy, Gregory Valiant, and Li Zhang. Learning sparse polynomial functions. In _**Proceedings of the twenty-fifth annual ACM-SIAM symposium on Discrete algorithms**_ , pages 500–510. SIAM, 2014. 

- Shai Ben-David, John Blitzer, Koby Crammer, and Fernando Pereira. Analysis of representations for domain adaptation. _**Advances in Neural Information Processing Systems**_ , 19, 2006. 

- Alain Berlinet and Christine Thomas-Agnan. _**Reproducing kernel Hilbert spaces in probability and statistics**_ . Springer Science & Business Media, 2011. 

- Gilles Blanchard and Nicole Mücke. Optimal rates for regularization of statistical inverse learning problems. _**Foundations of Computational Mathematics**_ , 18(4):971–1013, 2018. 

- Gilles Blanchard, Aniket Anand Deshmukh, Ürun Dogan, Gyemin Lee, and Clayton Scott. Domain generalization by marginal transfer learning. _**Journal of Machine Learning Research**_ , 22(1):46–100, 2021. 

- Andrea Caponnetto and Ernesto De Vito. Optimal rates for the regularized least-squares algorithm. _**Foundations of Computational Mathematics**_ , 7(3):331–368, 2007. 

- Sitan Chen and Raghu Meka. Learning polynomials in few relevant dimensions. In _**Conference on Learning Theory**_ , pages 1161–1227. PMLR, 2020. 

- Giulia Denevi, Carlo Ciliberto, Riccardo Grazzi, and Massimiliano Pontil. Learning-to-learn stochastic gradient descent with biased regularization. In _**International Conference on Machine Learning**_ , pages 1566– 1575. PMLR, 2019. 

18 

- Simon Shaolei Du, Wei Hu, Sham M. Kakade, Jason D. Lee, and Qi Lei. Few-shot learning via learning the representation, provably. In _**International Conference on Learning Representations**_ , 2021. 

- Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-agnostic meta-learning for fast adaptation of deep networks. In _**International Conference on Machine Learning**_ , pages 1126–1135. PMLR, 2017. 

- Chelsea Finn, Aravind Rajeswaran, Sham Kakade, and Sergey Levine. Online meta-learning. In _**International Conference on Machine Learning**_ , pages 1920–1930. PMLR, 2019. 

- Simon Fischer and Ingo Steinwart. Sobolev norm learning rates for regularized least-squares algorithms. _**Journal of Machine Learning Research**_ , 21:205–1, 2020. 

- Kenji Fukumizu, Francis R. Bach, and Michael I. Jordan. Kernel dimension reduction in regression. _**The Annals of Statistics**_ , 37(4):1871–1905, 2009. 

- Tomer Galanti, András György, and Marcus Hutter. Generalization bounds for transfer learning with pretrained classifiers. _**arXiv preprint arXiv:2212.12532**_ , 2022. 

- Benyamin Ghojogh, Fakhri Karray, and Mark Crowley. Eigenvalue and generalized eigenvalue problems: Tutorial. _**arXiv preprint arXiv:1903.11240**_ , 2019. 

- Behrooz Ghorbani, Song Mei, Theodor Misiakiewicz, and Andrea Montanari. Linearized two-layers neural networks in high dimension. _**The Annals of Statistics**_ , 49(2), 2021. 

- Chong Gu and Chong Gu. _**Smoothing spline ANOVA models**_ , volume 297. Springer, 2013. 

- Daniel Hsu, Sham M Kakade, and Tong Zhang. Random design analysis of ridge regression. In _**Conference on Learning Theory**_ , pages 9–1. JMLR Workshop and Conference Proceedings, 2012. 

- Motonobu Kanagawa, Philipp Hennig, Dino Sejdinovic, and Bharath K Sriperumbudur. Gaussian processes and kernel methods: A review on connections and equivalences. _**arXiv preprint arXiv:1807.02582**_ , 2018. 

- Motonobu Kanagawa, Bharath K Sriperumbudur, and Kenji Fukumizu. Convergence analysis of deterministic kernel-based quadrature rules in misspecified settings. _**Foundations of Computational Mathematics**_ , 20:155–194, 2020. 

- Mikhail Khodak, Maria-Florina F Balcan, and Ameet S Talwalkar. Adaptive gradient-based meta-learning methods. _**Advances in Neural Information Processing Systems**_ , 32, 2019. 

- Weihao Kong, Raghav Somani, Zhao Song, Sham Kakade, and Sewoong Oh. Meta-learning for mixed linear regression. In _**International Conference on Machine Learning**_ , pages 5394–5404. PMLR, 2020. 

- Mikhail Konobeev, Ilja Kuzborskij, and Csaba Szepesvári. A distribution-dependent analysis of meta learning. In _**International Conference on Machine Learning**_ , pages 5697–5706. PMLR, 2021. 

- Bing Li and Yuexiao Dong. Dimension reduction for nonelliptically distributed predictors. _**The Annals of Statistics**_ , 37(3):1272–1298, 2009. 

- Bing Li, Andreas Artemiou, and Lexin Li. Principal support vector machines for linear and nonlinear sufficient dimension reduction. _**The Annals of Statistics**_ , 39(6):3182–3210, 2011. 

- Cong Ma, Reese Pathak, and Martin J Wainwright. Optimally tackling covariate shift in rkhs-based nonparametric regression. _**The Annals of Statistics**_ , 51(2):738–761, 2023. 

- Yishay Mansour, Mehryar Mohri, and Afshin Rostamizadeh. Domain adaptation: Learning bounds and algorithms. In _**Conference on Learning Theory**_ . PMLR, 2009. 

- Andreas Maurer. A chain rule for the expected suprema of gaussian processes. In _**Proc. 25th International Conference on Algorithmic Learning Theory**_ , 2014. 

19 

- Andreas Maurer, Massimiliano Pontil, and Bernardino Romera-Paredes. The benefit of multitask representation learning. _**Journal of Machine Learning Research**_ , 17(81):1–32, 2016. 

- Dimitri Meunier and Pierre Alquier. Meta-strategy for learning tuning parameters with guarantees. _**Entropy**_ , 23(10):1257, 2021. 

- Mattes Mollenhauer. _**On the statistical approximation of conditional expectation operators**_ . Freie Universitaet Berlin (Germany), 2021. 

- Jaouad Mourtada and Lorenzo Rosasco. An elementary analysis of ridge regression with random design. _**Comptes Rendus. Mathématique**_ , 360(G9):1055–1063, 2022. 

- Xiaochun Niu, Lili Su, Jiaming Xu, and Pengkun Yang. Collaborative learning with shared linear representations: Statistical rates and optimal algorithms. _**arXiv preprint arXiv:2409.04919**_ , 2024. 

Beresford N Parlett. _**The symmetric eigenvalue problem**_ . SIAM, 1998. 

- Iosif Pinelis. Optimum bounds for the distributions of martingales in banach spaces. _**The Annals of Probability**_ , pages 1679–1706, 1994. 

- Iosif F Pinelis and Aleksandr Ivanovich Sakhanenko. Remarks on inequalities for large deviation probabilities. _**Theory of Probability & Its Applications**_ , 30(1):143–148, 1986. 

- Steve Smale and Ding-Xuan Zhou. Learning theory estimates via integral operators and their approximations. _**Constructive Approximation**_ , 26(2):153–172, 2007. 

- Bharath K Sriperumbudur, Kenji Fukumizu, and Gert RG Lanckriet. Universality, characteristic kernels and rkhs embedding of measures. _**Journal of Machine Learning Research**_ , 12(7), 2011. 

- Ingo Steinwart and Andreas Christmann. _**Support vector machines**_ . Springer Science & Business Media, 2008. 

- Ingo Steinwart and Clint Scovel. Mercer’s theorem on general domains: On the interaction between measures, kernels, and rkhss. _**Constructive Approximation**_ , 35(3):363–417, 2012. 

- Gilbert W Stewart and Ji-guang Sun. _**Matrix perturbation theory**_ . Academic press, 1990. 

- Kiran K Thekumparampil, Prateek Jain, Praneeth Netrapalli, and Sewoong Oh. Statistically and computationally efficient linear meta-representation learning. _**Advances in Neural Information Processing Systems**_ , 34:18487–18500, 2021. 

- Ye Tian, Yuqi Gu, and Yang Feng. Learning from similar linear representations: Adaptivity, minimaxity, and robustness. _**arXiv preprint arXiv:2303.17765**_ , 2023. 

- Nilesh Tripuraneni, Michael Jordan, and Chi Jin. On the theory of transfer learning: The importance of task diversity. _**Advances in Neural Information Processing Systems**_ , 33:7852–7862, 2020. 

- Nilesh Tripuraneni, Chi Jin, and Michael Jordan. Provable meta-learning of linear representations. In _**International Conference on Machine Learning**_ , pages 10434–10443. PMLR, 2021. 

- Per-Åke Wedin. Perturbation bounds in connection with singular value decomposition. _**BIT Numerical Mathematics**_ , 12:99–111, 1972. 

- Qiang Wu, F Liang, and S Mukherjee. Regularized sliced inverse regression for kernel models. Technical report, Citeseer, 2007. 

- Xiangrong Yin, Bing Li, and R Dennis Cook. Successive direction extraction for estimating the central subspace in a multiple-index regression. _**Journal of Multivariate Analysis**_ , 99(8):1733–1757, 2008. 

20 

- Oğuz Kaan Yüksel, Etienne Boursier, and Nicolas Flammarion. First-order anil provably learns representations despite overparametrisation. In _**The Twelfth International Conference on Learning Representations**_ , 2024. 

- Yuchen Zhang, John Duchi, and Martin Wainwright. Divide and conquer kernel ridge regression: A distributed algorithm with minimax optimal rates. _**Journal of Machine Learning Research**_ , 16(1):3299–3340, 2015. 

- Richard Zippel. Probabilistic algorithms for sparse polynomials. In _**International symposium on symbolic and algebraic manipulation**_ , pages 216–226. Springer, 1979. 

21 

## **Appendix** 

In Section A we present the proofs of the main results: 

- A.1: proof of Theorem 1; 

- A.2: proof of Proposition 3; 

- A.3: proofs of Theorem 2 and Example 1; 

- A.4: proof of Corollary 1; 

- A.5: proofs Section 3.3; 

- A.6: proof of Remark 9. 

In Section B, we present auxiliary results used for the main proofs. In Section C, we list concentration inequalities used in the different proofs. Finally, in Section D, we present additional results from our experimental results. 

## **A Proofs of the Main Results** 

## **A.1 Proof of Theorem 1** 

Before embarking on the proof of Theorem 1 we need a few preliminary results and definitions. We first introduce the empirical counterpart of the covariance operator, for _i_ ∈[ _N_ ] ∪{ _T_ } and _m_ = _n_ if _i_ ∈[ _N_ ], _m_ = _nT_ if _i_ = _T_ , 

**==> picture [321 x 26] intentionally omitted <==**

where Φ _i_ = [ _ϕ_ ( _xi,_ 1) _,...,ϕ_ ( _xi,m_ )] is defined as 

**==> picture [86 x 37] intentionally omitted <==**

and admits as adjoint the sampling operator for task _i_ , 

**==> picture [114 x 23] intentionally omitted <==**

The Gram matrix for each task is _Ki_ ≐ Φ[∗] _i_[Φ] _[i]_[ ∈][R] _[m]_[×] _[m]_[.][For][any][linear][operator] _[F]_[∶H →H][and][scalar] _[γ]_[>][ 0][,][we] define _Fγ_ ≐ _F_ + _γI_ H. With those notations and taking derivatives with respect to _f_ in Eq. (1), we can derive a closed-form expression for _f_[ˆ] _i,λ_ , for _i_ ∈[ _N_ ], 

**==> picture [337 x 22] intentionally omitted <==**

Recall that H[ˆ] _s_ is a RKHS with canonical feature map _Pϕ_[ˆ] (⋅) equipped with the same inner product as H. Hence, the covariance operator in that space equipped with the marginal distribution _µT_ on X is defined as 

**==> picture [331 x 14] intentionally omitted <==**

22 

which is a positive semi-definite self-adjoint operator. The counterpart of Eq. (15) in H[ˆ] _s_ is 

**==> picture [57 x 30] intentionally omitted <==**

1 Then Σ[ˆ] ˆ _P_[=] _nT_[Φ][ ˆ] _P_[Φ][∗] _P_ ˆ[is][the][empirical][covariance][in][H][ˆ] _[s]_[for][the][target][task.][Therefore,][since] _[f]_[ˆ] _[T,λ]_[∗][is][the][ridge] estimator in H[ˆ] _s_ (see Eq. (7)), in light of Eq. (16), we have 

**==> picture [360 x 23] intentionally omitted <==**

Theˆ next technicalˆ lemmata ˆare ˆusefulˆ for theˆ proofˆ of Theoremˆ 1ˆ. Recall that _P_[ˆ] is the projection onto H _s_ = span{ _v_ 1 _,...,_ ˆ _vs_ }, hence _P_ = _V V_[∗] where _V_ = [ _v_ 1 _,...,_ ˆ _vs_ ] and _V_[∗] _V_ = _Is_ with _Is_ the identity in R _[s]_[×] _[s]_ . ˆ ˆ ˆ **Lemma 3.** _P_[ˆ] Σ[ˆ] _T,λ_ ∗ _P_[ˆ] = _V_[ˆ] ( _V_[ˆ][∗] Σ[ˆ] _T V_[ˆ] + _λ_ ∗ _Is_ ) _V_[ˆ][∗] _and_ Σ[ˆ][−] _P ,λ_ ˆ[1] ∗ _P_ ˆΣ _T,λ_ ∗ _P_ = _P ._ 

_Proof._ The first identity is obtained by plugging _P_[ˆ] = _V_[ˆ] _V_[ˆ][∗] and using _V_[ˆ][∗] _V_[ˆ] = _Is_ . For the second identity, we have 

**==> picture [274 x 65] intentionally omitted <==**

where in the second equality, we used the matrix inversion lemma. 

ˆ ˆ ˆ ˆ ˆ ˆ **Lemma 4.** _P_[ˆ] − Σ[ˆ][−] _P ,λ_ ˆ[1] ∗ _P_ ˆΣ _T_ = _λ_ ∗ˆΣ[−] _P ,λ_ ˆ[1] ∗ _P_ − ˆΣ[−] _P ,λ_ ˆ[1] ∗ _P_ ˆΣ _T,λ_ ∗ _P_ ⊥ _, where P_ ⊥ ≐ _I_ H − _P . Proof._ 

**==> picture [240 x 54] intentionally omitted <==**

where the last equality follows from Lemma 3. 

ˆ **Lemma 5.** Σ[−] ˆ[1][/][2] _P_ ˆΣ[1][/][2] ∥[ˆ] _P ,λ_ ∗ _T,λ_ ∗[∥∈{][0] _[,]_[1][}] _[.]_ 

ˆ ˆ ˆ ˆ _Proof._ First, note that _hλ_ ∗ ≐ Σ[ˆ][−] _P ,λ_ ˆ[1] ∗ _P_ = _V_ ( ˆ _V_[∗] ˆΣ _T,λ_ ∗ _V_ )[−][1] _V_[∗] . Secondly, note that 

**==> picture [156 x 50] intentionally omitted <==**

Thirdly, 

**==> picture [286 x 62] intentionally omitted <==**

23 

Hence, using that for any bounded linear operator _F_ ∶H →H, ∥ _F_ ∥[2] = ∥ _F_[∗] _F_ ∥, 

**==> picture [198 x 106] intentionally omitted <==**

**==> picture [342 x 20] intentionally omitted <==**

**==> picture [198 x 21] intentionally omitted <==**

_Proof of Theorem 1._ Under Assumptions 1 and 2 with _s_ ≥ 1, we have the following excess risk decomposition 

**==> picture [396 x 14] intentionally omitted <==**

where we used _P_[ˆ] ⊥ + _P_[ˆ] = _I_ H and _fT_ = _PfT_ since _fT_ ∈H _s_ . Instead of working with the _L_ 2−norm we can work with the H norm as for any _f_ ∈ H[ˆ] _s_ , 

**==> picture [341 x 83] intentionally omitted <==**

where in the second equality we used the reproducing property in H[ˆ] _s_ and in the fourth equality we used the definition of Σ ˆ _P_[in][Eq.][(][17][).][Similarly,][for][any] _[f]_[∈H][,] 

**==> picture [288 x 15] intentionally omitted <==**

Therefore, we have 

**==> picture [398 x 15] intentionally omitted <==**

where we used that for a bounded kernel (here sup _x,x_ ′∈X _K_ ( _x,x_[′] ) ≐ _κ_[2] < ∞), for any marginal distribution, the trace norm (and hence the operator norm) of the associated covariance operator is bounded by _κ_ (see 

24 

Steinwart and Christmann, 2008, Theorem 4.27). On the other hand, by Eq. (20) and Eq. (18), we have 

**==> picture [414 x 137] intentionally omitted <==**

where in the last equality we used Φ ˆ _P_[Φ] _T_[∗][=] _[P]_[ˆ][Φ] _[T]_[ Φ][∗] _T_[=] _[ n][T][P]_[ˆ][ ˆΣ] _[T][ .]_ **Term A.** For term A, we have 

**==> picture [260 x 76] intentionally omitted <==**

where in the last inequality, we used 

**==> picture [463 x 44] intentionally omitted <==**

**==> picture [317 x 21] intentionally omitted <==**

ˆ where _BT,λ_ ∗ ≐ Σ[−] ˆ[1][/][2] _P_ (Σ _T_ − ˆΣ _T_ ) ˆ _P_ Σ[−] ˆ[1][/][2][We][control] _[B][T,λ]_[∗][in][operator][norm][with][a][Bernstein-type][concentra-] _P ,λ_ ∗ _P ,λ_ ∗[.] tion inequality for Hilbert-Schmidt operator valued random variables. By Proposition 12, for _λ_ ∗ > 0, _τ_ ≥ 2 _._ 6 and _nT_ ≥ 1, the following operator norm bound is satisfied with _µ[n] T[T]_[-probability][not][less][than][1][ −] _[e]_[−] _[τ]_ 

**==> picture [347 x 82] intentionally omitted <==**

conditionally on D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][.][Therefore,][if] _[n][T]_[≥][6][(] _[τ]_[+][ log][(] _[s]_[))] _[κ]_[2] _[λ]_[−] ∗[1][,][Proposition][12][yields] 

with _µ[n] T[T]_[-probability][not][less][than][1][ −] _[e]_[−] _[τ]_[.][Consequently,][the][inverse][of] _[I]_[ −] _[B][T,λ]_[∗][can][be][represented][by][the] Neumann series. In particular, the Neumann series gives us the following bound 

**==> picture [380 x 25] intentionally omitted <==**

with _µ[n] T[T]_[-probability not less than][ 1][−] _[e]_[−] _[τ]_[.][Hence, for] _[ λ]_[∗][>][ 0][,] _[ τ]_[≥][2] _[.]_[6][ and] _[ n][T]_[≥][6][(] _[τ]_[ +][log][(] _[s]_[))] _[κ]_[2] _[λ]_[−] ∗[1][, conditionally] on D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][with] _[µ][n] T[T]_[-probability][not][less][than][1][ −] _[e]_[−] _[τ]_[,] 

**==> picture [320 x 24] intentionally omitted <==**

25 

To deal with the remaining term in term A, note that 

**==> picture [374 x 24] intentionally omitted <==**

where 

**==> picture [158 x 28] intentionally omitted <==**

We can bound this quantity in probability using a Bernstein concentration inequality for Hilbert space valued random variables (Theorem 14). First note that 

**==> picture [315 x 19] intentionally omitted <==**

Consequently, to apply Theorem 14, it remains to bound the _m_ -th moment of _ξ_ , for _m_ ≥ 2, 

**==> picture [341 x 20] intentionally omitted <==**

The inner integral can be bounded by Assumption 6, for _µT_ -almost all _x_ ∈X , for _m_ ≥ 2, 

**==> picture [218 x 22] intentionally omitted <==**

Then, by Lemma 11, and since dim(H[ˆ] _s_ ) = _s_ , 

**==> picture [206 x 22] intentionally omitted <==**

Since ∥ _P_[ˆ] ∥≤ 1 and sup _x,x_ ′∈X _K_ ( _x,x_[′] ) ≐ _κ_[2] < ∞, we have for all _x_ ∈X , 

**==> picture [205 x 22] intentionally omitted <==**

Therefore, 

**==> picture [332 x 60] intentionally omitted <==**

Applying Theorem 14 and Proposition 11 with _v_[2] = (2 _Y_ ∞)[2] _s_ and _b_ = 2 _Y_ ∞ _κλ_[−] ∗[1][/][2] _,_ we get that for _τ_ ≥ 1 and _nT_ ≥ 1, with probability at least 1 − 2 _e_[−] _[τ]_ , 

**==> picture [294 x 28] intentionally omitted <==**

conditionally on D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][.][Therefore,][merging][with][Eq.][(][26][)][and][using][a][union][bound,][for] _λ_ ∗ > 0, _τ_ ≥ 2 _._ 6 and _nT_ ≥ 6( _τ_ + log( _s_ )) _κ_[2] _λ_[−] ∗[1][, conditionally on][ D] _[i]_[= {(] _[x][i,j][,y][i,j]_[)][2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][, with] _[ µ][n] T[T]_[-probability] not less than 1 − 3 _e_[−] _[τ]_ 

**==> picture [306 x 31] intentionally omitted <==**

**Term B.** By Lemma 4, we have 

**==> picture [373 x 32] intentionally omitted <==**

26 

For B.1, 

**==> picture [174 x 39] intentionally omitted <==**

We encountered the first term when we bounded Term A (see Eqs. (24) and (25))). For _λ_ ∗ > 0, _τ_ ≥ 2 _._ 6 with _nT_ ≥ 6( _τ_ + log( _s_ )) _κ_[2] _λ_[−] ∗[1][,][with][probability][at][least][1][ −] _[e]_[−] _[τ]_[,] 

**==> picture [92 x 18] intentionally omitted <==**

conditionally on D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][.][Hence,] 

**==> picture [285 x 14] intentionally omitted <==**

For term B.2., for _λ_ ∗ > 0, _τ_ ≥ 2 _._ 6 with _nT_ ≥ 6( _τ_ + log( _s_ )) _κ_[2] _λ_[−] ∗[1][,][with][probability][at][least][1][ −] _[e]_[−] _[τ]_ 

**==> picture [230 x 36] intentionally omitted <==**

where we used Lemma 5 and Eqs. (24) and (25) again. Putting together Eq. (19), Eq. (22), Eq. (23), Eq. (27) and Eq. (28), for _λ_ ∗ > 0, _τ_ ≥ 2 _._ 6 and 

_nT_ ≥ 6 _κ_[2] _λ_[−] ∗[1][(] _[τ]_[+][ log][ (] _[s]_[))] _[,]_ 

conditionally on D _i_ = {( _xi,j,yi,j_ )[2] _j_ = _[n]_ 1[}] _[,i]_[ ∈[] _[N]_[]][with] _[µ][n] T[T]_[-probability][not][less][than][1][ −][3] _[e]_[−] _[τ]_[,] 

**==> picture [336 x 31] intentionally omitted <==**

where _c_ is a universal constant. 

## **A.2 Proof of Proposition 3** 

We prove the following infinite dimensional version of Wedin’s sin −Θ Theorem. 

**Theorem 6.** _Let A_ ∶ _H_ → _H and A_[̂] ∶ _H_ → _H be compact operators on a separable Hilbert space H with nonincreasingly ordered singular values_ ( _γi_ ) _i_ ≥1 _and_ ( _γ_ ˆ _i_ ) _i_ ≥1 _respectively. Let s_ ≤ min{rank( _A_ ) _,_ rank( _A_[̂] )} _and assume γs_ > _γs_ +1 _. Let furthermore P and P_[̂] _be the projections on the span of the top-s left singular vectors for A and A_[̂] _respectively. Then we have,_ 

**==> picture [104 x 27] intentionally omitted <==**

_where the result also holds in Hilbert-Schmidt norm. Both bounds also hold when we replace the top-s left singular vectors with the sets of top-s right singular vectors._ 

_Proof._ In this proof, ∥⋅∥ denotes either the operator norm or the Hilbert-Schmidt norm. First note that ∥( _I_ − _P_[̂] ) _P_ ∥≤ 1, therefore if 2∥ _A_ − _A_[̂] ∥≥ _γs_ − _γs_ +1, the bound is trivially obtained. Let us now consider 2∥ _A_ − _A_[̂] ∥≤ _γs_ − _γs_ +1. We start by assuming that _A_ and _A_[̂] are rectangular _n_ × _m_ matrices. By Wedin’s sin −Θ Theorem, if _γs_ − _γ_ ˆ _s_ +1 > 0, 

**==> picture [291 x 26] intentionally omitted <==**

27 

By Weyl’s inequality for singular values, 

**==> picture [144 x 20] intentionally omitted <==**

This implies, by the assumption _γs_ > _γs_ +1, that 

**==> picture [106 x 19] intentionally omitted <==**

Therefore, combining Eq. (29) and 2∥ _A_ − _A_[̂] ∥≤ _γs_ − _γs_ +1, we obtain 

**==> picture [315 x 27] intentionally omitted <==**

Let us now assume that _A_ and _A_[̂] are compact operators. Let _U_ and _U_[̂] be the sets of first left _s_ + 1 eigenvectors of _A_ and _A_[̂] , respectively and let Π _U_ ∪̂ _U_[be][the][projection][on][the][union][of][their][spans.][Let] _[V]_[and] _[V]_[̂][be][the] sets of first right _s_ + 1 eigenvectors of _A_ and _A_[̂] , respectively and let Π _V_ ∪̂ _V_ be the projection on the union of their spans. We define the operators _A_ 0 ≐ Π _U_ ∪̂ _U[A]_[Π] _V_ ∪ _V_[̂][and] _A_[̂] 0 ≐ Π _U_ ∪̂ _U A_[̂] Π _V_ ∪̂ _V_ . By construction, the first _s_ + 1 singular values and left-right eigenvectors of _A_ 0 and _A_[̂] 0 coincide with the first _s_ + 1 singular values and left-right eigenvectors of _A_ and _A_[̂] , respectively. By choosing some orthonormal basis of the finite-dimensional spaces span( _U_ ∪ _U_[̂] ) and span( _V_ ∪ _V_[̂] ) and expressing _A_ 0 and _A_[̂] 0 in terms of matrices, we can apply the previous Eq. (30) to conclude the proof. 

The extension of the original Wedin’s sin −Θ Theorem Wedin (1972) to Hilbert spaces is taken from the proof technique used in Theorem A.4.4 Mollenhauer (2021). 

_Proof of Proposition 3._ We apply Theorem 6 to _CN_ and _C_[ˆ] _N,n,λ_ . As _CN_ has rank _s_ , _γs_ +1 = 0. 

## **A.3 Proof of Theorem 2** 

Before proving Theorem 2, we provide some intermediate results. 

**Lemma 7.** _For all i_ ∈[ _N_ ] _, we have_ 

**==> picture [258 x 14] intentionally omitted <==**

_Proof._ For all _i_ ∈[ _N_ ], we define _Yi_ ≐( _yi,_ 1 _,...,yi,n_ )[⊺] ∈ R _[n]_ and _ϵi_ ≐[ _ϵi,_ 1 _,...,ϵi,n_ ][⊺] ∈ R _[n]_ where _ϵi,j_ ≐ _yi,j_ − _fi_ ( _xi,j_ ), _j_ ∈[ _n_ ]. For all _i_ ∈[ _N_ ], using _ϵi_ = _Yi_ − Φ[∗] _i_[(] _[f][i]_[)][,][we][get][from][Eq.][(][16][)][that] _[f]_[ˆ] _[i,λ]_[can][be][decomposed][as] 

**==> picture [163 x 22] intentionally omitted <==**

Since E[ _ϵi_ ∣ _xi,_ 1 _,...,xi,n_ ] = 0, it yields 

**==> picture [352 x 22] intentionally omitted <==**

It gives us the following bound on ∥E[ _f_[ˆ] _i,λ_ ]∥H 

**==> picture [284 x 15] intentionally omitted <==**

where in the last inequality we used the fact that the eigenvalues of _I_ − _λ_ Σ[ˆ][−] _i,λ_[1][are][in][the][interval][[][0] _[,]_[1][]][,][hence] its operator norm is bounded by 1. 

28 

For each source task _i_ ∈[ _N_ ], we introduce the regularized population regression function 

**==> picture [181 x 21] intentionally omitted <==**

It admits the closed-form expression 

**==> picture [306 x 14] intentionally omitted <==**

Therefore, we have the following bound for its H−norm 

**==> picture [358 x 15] intentionally omitted <==**

Furthermore, we have 

**==> picture [147 x 14] intentionally omitted <==**

This quantity is the statistical bias of the estimator _f_[ˆ] _i,λ_ . To prove Theorem 2, we use the following decomposition, 

**==> picture [262 x 28] intentionally omitted <==**

where 

**==> picture [141 x 26] intentionally omitted <==**

and _CN_ , _C_[ˆ] _N,n,λ_ are defined in Eqs. (3) and (4) respectively. 

**Theorem 8** (Bounds on the variance term) **.** _Suppose Assumption 5 and Assumption 6 hold. Define_ **Var**[(] _λ[N,n]_[)] ≐ ∥ _C_[ˆ] _N,n,λ_ − _C_[¯] _N,n,λ_ ∥ _HS. For λ_ ∈(0 _,_ 1] _,τ,δ_ ≥ log(2) _and N,n_ ≥ 1 _, with probability greater than_ 1 − 2 _e_[−] _[τ]_ − 4 _Ne_[−] _[δ] ,_ 

**==> picture [347 x 27] intentionally omitted <==**

_with c_ 1 _a constant depending on Y_ ∞ _,_ max _i_ ∈[ _N_ ] ∥ _fi_ ∥H _, κ and R._ 

_Alternatively, suppose Assumptions 3, 4, 5 and 6 hold. For_ 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _, δ_ ≥ 1 _, τ_ ≥ log(2) _, N_ ≥ 1 _and n_ ≥ _c_ 0 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α] , with probability greater than_ 1 − 2 _e_[−] _[τ]_ − 8 _Ne_[−] _[δ] ,_ 

**==> picture [423 x 36] intentionally omitted <==**

_with c_ 0 _a constant depending on kα,_ ∞ _,D and c a constant depending on Y_ ∞ _,kα,_ ∞ _,D and R._ 

We use the second variance bound to prove Theorem 2. The first bound is used to prove Remark 9. 

_Proof._ For _i_ ∈[ _N_ ], we let _ξi_ ≐ _f_[ˆ] _i,λ_[′][⊗] _[f]_[ˆ] _[i,λ]_[−][E][(][ ˆ] _[f][i,λ]_[)⊗][E][(][ ˆ] _[f][i,λ]_[)][ and] _[ η][i]_[ ≐] _[f]_[ˆ] _i,λ_[ ′][⊗] _[f]_[ˆ] _[i,λ]_[−] _[f][i,λ]_[⊗] _[f][i,λ]_[such that] _[ ξ][i]_[ =] _[ η][i]_[−][E][[] _[η][i]_[]][.] We start with the following decomposition, for _i_ ∈[ _N_ ] 

**==> picture [303 x 67] intentionally omitted <==**

29 

We now use Eq. (32), 

**==> picture [333 x 33] intentionally omitted <==**

In the following we assume that we have access to a function _g_ ( _n,λ,δ_ ) such that for all _δ_ ≥ 0 and _i_ ∈[ _N_ ], with probability at least 1 − _Je_[−] _[δ]_ 

∥ _f_[ˆ] _i,λ_ − _fi,λ_ ∥H ≤ _g_ ( _n,λ,δ_ ) _,_ (35) 

for some constant _J_ ≥ 1. We will use either Theorem 12: for _λ_ > 0 _,δ_ ≥ log(2) _,n_ ≥ 1, with probability at least 1 − 2 _e_[−] _[δ]_ 

**==> picture [85 x 24] intentionally omitted <==**

or Theorem 13: for _δ_ ≥ 1, _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥, and _n_ ≥ _c_ 0 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ , with probability not less than 1 − 4 _e_[−] _[δ]_ 

**==> picture [145 x 29] intentionally omitted <==**

with _c_ 0 a constant depending on _kα,_ ∞ _,D_ and _c_ a constant depending on _Y_ ∞ _,kα,_ ∞ _,D_ and _R_ . We fix _g_ a function satisfying Eq. (35) and define the events 

**==> picture [379 x 24] intentionally omitted <==**

By independence of the _f_[ˆ] _i,λ_ and _f_[ˆ] _i,λ_[′][,][we][have][for][all] _[i]_[ ∈[] _[N]_[]] 

**==> picture [180 x 30] intentionally omitted <==**

where we used Bernoulli’s inequality. We then have 

**==> picture [200 x 14] intentionally omitted <==**

For any _ϵ_ > 0, 

**==> picture [294 x 105] intentionally omitted <==**

For each _i_ ∈[ _N_ ], E[ _ξi_ ] = 0, therefore by Proposition 10, 

**==> picture [373 x 22] intentionally omitted <==**

30 

**==> picture [456 x 14] intentionally omitted <==**

**==> picture [363 x 121] intentionally omitted <==**

By Proposition 10 again, 

**==> picture [378 x 97] intentionally omitted <==**

where we used that by Assumption 5: for _i_ ∈[ _N_ ] 

**==> picture [189 x 11] intentionally omitted <==**

Hence ∥ _ζi_ ∥ _HS_ ≤ 2 _V_ ( _n,λ,δ_ ). We now use Hoeffding’s inequality (Theorem 15) on _H_ = _HS_ for the centered and bounded random variables { _ζi_ } _i_ ∈[ _N_ ]. As long as _ϵ_ ≥ 2 _c_ 1 _λ_[−][1] _Je_[−] _[δ]_ , 

**==> picture [352 x 81] intentionally omitted <==**

Therefore, combining the results, we obtain 

Solving for _ϵ_ , we have for all _τ_ ∈(2 _JNe_[−] _[δ] ,_ 1), 

**==> picture [220 x 26] intentionally omitted <==**

Finally, we obtain that for all _τ_ ∈(2 _JNe_[−] _[δ] ,_ 1) with probability greater than 1 − _τ_ , 

**==> picture [273 x 29] intentionally omitted <==**

Alternatively we can write, for all _τ_ ≥ log(2) with probability greater than 1 − 2 _e_[−] _[τ]_ − 2 _JNe_[−] _[δ]_ , 

**==> picture [316 x 29] intentionally omitted <==**

_δ_ is a free parameter that we will adjust as a function of _N,n_ such that _Ne_[−] _[δ]_ and _e_[−] _[δ] λ_[−][1] converge to 0 with _N_ →+∞ or _n_ →+∞. 

31 

**Theorem 9** (Bounds on the bias term) **.** _Suppose Assumptions 3, 4 and 5 hold with_ 0 < _p_ ≤ _α_ ≤ 1 _and r_ ∈[0 _,_ 1] _. For any δ_ ≥ 1 _and λ_ ∈(0 _,_ 1] _if n_ ≥ _c_ 1 _δλ_[−] _[p]_[−][1] _then_ 

**==> picture [316 x 26] intentionally omitted <==**

_where c_ 1 _is a constant depending only on D, κ, and kα,_ ∞ _and c_ 2 _is a constant depending only on R, κ. Furthermore, for any δ_ ≥ 1 _and_ 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _, if n_ ≥ _c_ 3 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α] then_ 

**==> picture [320 x 14] intentionally omitted <==**

_where c_ 3 _only depends on kα,_ ∞ _,D and c_ 4 _only depends on R,κ._ 

_Proof._ 

**==> picture [344 x 119] intentionally omitted <==**

where we used Lemma 7 and Assumption 5: for _i_ ∈[ _N_ ] 

**==> picture [189 x 11] intentionally omitted <==**

For the first bound, by Proposition 8, we have for _λ_ ∈(0 _,_ 1], _δ_ ≥ 1 and _n_ ≥ _c_ 1 _δλ_[−][1][−] _[p]_ , 

**==> picture [143 x 26] intentionally omitted <==**

where _c_ 1 is a constant depending only on _D_ , _κ_ , and _kα,_ ∞ and _c_ 5 is a constant depending only on _R_ , _κ_ , which proves the second bound. For the second bound, by Proposition 9, we have for 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥, _δ_ ≥ 1 and _n_ ≥ _c_ 6 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ , 

**==> picture [151 x 14] intentionally omitted <==**

where _c_ 6 only depends on _kα,_ ∞ _,D_ and _c_ 7 only depends on _R,κ_ . 

_Proof of Theorem 2._ **Bound in Eq. (10).** We first notice that the bias bounds in Eq. (36) and Eq. (37) can be combined as follows: for any _δ_ ≥ 1, 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ and _n_ ≥ _c_ 1 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ if _r_ ≤ 1/2 or _n_ ≥ _c_ 2 _δλ_[−] _[p]_[−][1] if _r_ ∈(1/2 _,_ 1], 

**==> picture [151 x 27] intentionally omitted <==**

where we used _λ_ ≤ 1. _c_ 1 is a constant depending only on _D_ , _kα,_ ∞, _c_ 2 is a constant depending only on _D_ , _κ_ , and _kα,_ ∞ and _C_ 0 is a constant depending only on _R_ , _κ_ . We now combine this bias bound with Eq. (34) for the variance. Note that both bounds have a free parameter _δ_ that we take as the same value _δ_ 1 for each bound. Since 0 < _λ_ ≤ 1 by assuming _n_ large enough so that √ _nλ_ 1+2 _p_ √1 + _nλ[α]_[−] _[p]_[≤][1][,][we][obtain] 

32 

that for all 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥, _τ_ ≥ log(2), _δ_ ≥ 1, _N_ ≥ _τ_ and _n_ ≥ _c_ 1 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ if _r_ ≤ 1/2 or _n_ ≥ _δ_ max{ _c_ 2 _λ_[−] _[p]_[−][1] _,c_ 1 (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ } if _r_ ∈(1/2 _,_ 1], with probability greater than 1 − 2 _e_[−] _[τ]_ − 8 _Ne_[−] _[δ]_ , 

**==> picture [262 x 31] intentionally omitted <==**

with _C_ 1 a constant depending on _Y_ ∞ _,kα,_ ∞ _,D,κ_ and _R_ . As _δ_ is a free parameter, we pick _δ_ = 12log( _Nn_ ) with _N,n_ large enough such that _δ_ ≥ 1. We obtain that for _n_ ≥ 12 _c_ 0 log( _Nn_ )(1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α]_ if _r_ ≤ 1/2 or 

**==> picture [230 x 14] intentionally omitted <==**

if _r_ ∈(1/2 _,_ 1], with probability greater than 1 − 2 _e_[−] _[τ]_ − _o_ (( _nN_ )[−][10] ): 

**==> picture [393 x 31] intentionally omitted <==**

When we optimise for _λ_ in Corollary 1, we notice that the term _λ_ ( _nN_ 1 )[12][is][always][of][lower][order,][therefore][we] do not include it in the presentation of Theorem 2. Finally, since _λ_ ≤ 1 and we always have _p_ + 1 ≥ _α_ , when _r_ ∈(1/2 _,_ 1], we can simplify the constraint on _n_ as _n_ ≥ _c_ 3 log( _Nn_ )(1 + _p_ log( _λ_[−][1] )) _λ_[−] _[p]_[−][1] , with _c_ 3 a constant depending on _D_ , _κ_ , and _kα,_ ∞. 

**Remark 13** (Proof of Example 1) **.** _In the finite dimensional case, we use the same steps as the previous proof with g_ ( _n,λ,δ_ ) = _cδ_ √ _nk[from][Eq.]_[(][45][)] _[in][Theorem][13][.][Furthermore,][for][the][bias,][we][let][r]_[=][1] _[since] Assumption 5 is satisfied for any value of r when the RKHS is finite dimensional. This leads to the following bound. For n_ ≳ _k_ log( _nN_ ) _, with probability greater than_ 1 − 2 _e_[−] _[τ]_ − _o_ (( _nN_ )[−][10] ) _:_ 

**==> picture [372 x 27] intentionally omitted <==**

_We obtain Eq._ (12) _, by plugging λ_ =[lo][g][2] _nN_[(] _[nN]_[)] _._ 

## **A.4 Proof of Corollary 1** 

In the following, we ignore constants as only the orders of _n_ and _N_ matter for the proof of the corollary. By Theorem 2, under the assumption that _n_ ≥ log( _Nn_ ) log( _λ_[−] _[p]_ ) _λ_[−] _[α]_ for _r_ ≤ 1/2 or _n_ ≥ log( _Nn_ ) log( _λ_[−] _[p]_ ) _λ_[−] _[p]_[−][1] for _r_ ∈(1/2 _,_ 1], with high probability, ∥ _C_[ˆ] _N,n,λ_ − _CN_ ∥ _HS_ is bounded by a term of the order (see Eq. (10) and Eq. (38)), 

**==> picture [175 x 25] intentionally omitted <==**

Let _a_ > 0 be defined as _a_ ≐ log( _N_ )/ log( _n_ ), then _N_ = _n[a]_ . Plugging _N_ = _n[a]_ , we get the following upper bounds on ∥ _C_[ˆ] _N,n,λ_ − _CN_ ∥ _HS_ : 

**==> picture [348 x 48] intentionally omitted <==**

**Case A:** To optimize this bound, we start by matching _λ[r]_ with 1 . 

**==> picture [225 x 26] intentionally omitted <==**

33 

2 _r_ We need to make sure that the matched term _n_[−] 2 _[r] r_[(] + _[a]_ 1[+] +[1] _p_[)] log( _n_[1][+] _[a]_ ) 2 _r_ +1+ _p_ is the slowest term. 

**==> picture [466 x 37] intentionally omitted <==**

b) 1 ≥ 3 is always satisfied. 

We then need to check the constraint on _n_ for both _r_ ≤ 1/2 ( _n_ ≥ _Aλ_ ) and _r_ ∈(1/2 _,_ 1] ( _n_ ≥ _Bλ_ ). Plugging 1 2 back _a_ = log( _N_ )/ log( _n_ ), we get _λ_ = ( _nN_ )[−] 2 _r_ +1+ _p_ log( _nN_ ) 2 _r_ +1+ _p_ . Let us start with _r_ ≤ 1/2. Recall that _Aλ_ = log( _nN_ ) log( _λ_[−] _[p]_ ) _λ_[−] _[α]_ (where we ignore constant as only the orders of _n_ and _N_ matter here). Hence, plugging the value of _λ_ , 

**==> picture [337 x 17] intentionally omitted <==**

To satisfy this condition, it is sufficient that _N_ ≤ _n_ 2 _r_ + _αp_ +1 −1, i.e. _a_ ≤[2] _[r]_[+] _α[p]_[+][1] − 1. Notice that _a_ ≤[2] _[r]_[+] _α[p]_[+][1] − 1 ≤ 2 _rα_ +− _pp_ +1 − 1, therefore if _a_ ≤[2] _[r]_[+] _α[p]_[+][1] − 1 we have 1 ≥ 2 and under this condition, the obtained upper bound is of the order 

_r_ 2 _r_ ( _nN_ )[−] 2 _r_ +1+ _p_ log( _nN_ ) 2 _r_ +1+ _p_ (41) 

Let us now move to the constraint _n_ ≥ _Bλ_ for _r_ ∈(1/2 _,_ 1]. Recall that 

**==> picture [125 x 12] intentionally omitted <==**

To satisfy _n_ ≥ _Bλ_ , it is sufficient that _a_ ≤[2] _[r] p_[+] + _[p]_ 1[+][1] − 1 _,_ i.e. _N_ ≤ _n_ 2 _rp_ ++ _p_ 1+1 −1. Notice that 2 _rp_ ++ _p_ 1+1 − 1 ≤[2] _[r] α_[+] − _[p] p_[+][1] − 1, therefore if _a_ ≤[2] _[r] p_[+] + _[p]_ 1[+][1] − 1 we have 1 ≥ 2 and under this condition, the obtained upper bound is the same as in Eq. (41) with _r_ ∈(1/2 _,_ 1]. It concludes the proof of Eq. (11). 

**Case B:** In that regime, we further increase _N_ beyond the constraints in case A. As a result, the variance become negligible and we only need to minimize the bias. 

● B.1. _r_ ∈(0 _,_ 1/2]. We focus on bounding the risk with Eq. (10) under the constraint _n_ ≥ _Aλ_ . We choose the minimum _λ_ such that _n_ ≥ _Aλ_ is satisfied. This gives us _λ_ = (log _[ω]_ ( _nN_ )/ _n_ )[1][/] _[α]_ for _ω_ > 2. This choice of _λ_ leads to the final rate of 

_ωr_ log( _nN_ ) _α_ ⋅ _n_[−] _α[r]_ 

1 _p_ +1 ● B.2. _r_ ∈(1/2 _,_ 1]. We now choose the minimum _λ_ such that _n_ ≥ _Bλ_ is satisfied. This gives us _λ_ = ([lo][g] _[ω] n_[(] _[nN]_[)] ) for _ω_ > 2. This choice of _λ_ leads to the final rate of 

**==> picture [81 x 13] intentionally omitted <==**

## **A.5 Proofs of Section 3.3** 

**Definition 1.** _Let A,B_ ∈ R _[n]_[×] _[n] be two real symmetric matrices, the generalized eigenvalue problem solves for_ ( _v,γ_ ) ∈ R _[n]_ × R _,_ 

( _A_ − _γB_ ) _v_ = 0 _._ 

_A solution_ ( _v,γ_ ) _is called a generalized eigenpair where v is called a generalized eigenvector and γ a generalized eigenvalue. Note that if B_ = _In we retrieve the standard eigenvalue problem._ 

34 

For a comprehensive treatment of the generalized eigenvalue problem see Parlett (1998). Before proving Proposition 1, we need the following lemma. 

**Lemma 10.** _Let_ ( _U,_[ˆ] _V_[ˆ] ) _be the top_ − _s left and right singular vectors of C_[ˆ] _N,n,λ._ ( _U,_[ˆ] _V_[ˆ] ) _is solution of_ 

**==> picture [299 x 48] intentionally omitted <==**

_Proof._ For all _U,V_ ∶ R _[s]_ →H such that _U_[∗] _U_ = _V_[∗] _V_ = _Is_ , let us write _U_ = [ _u_ 1 _,...,us_ ], _V_ = [ _v_ 1 _,...,vs_ ]. Plugging the SVD _C_[ˆ] _N,n,λ_ = ∑ _[N] i_ =1 _[γ]_[ˆ] _[i][u]_[ˆ] _[i]_[⊗] _[v]_[ˆ] _[i]_[in][the][objective,][we][have] 

**==> picture [188 x 26] intentionally omitted <==**

In that form, the objective is separable in the _s_ variables {( _ui,vi_ )} _[s] i_ =1[.][For] _[i]_[ =][ 1][,][we][have] 

**==> picture [284 x 30] intentionally omitted <==**

ˆ ˆ and the upper bound is achieved for _u_ 1 = _u_ 1 and _v_ 1 = _v_ 1. For _i_ = 2, incorporating the constraint ⟨ _u_ 2 _,u_ 1⟩H = ⟨ _v_ 2 _,v_ 1⟩H = 0 and plugging _u_ 1 = _u_ ˆ1 and _v_ 1 = ˆ _v_ 1, we have 

**==> picture [225 x 26] intentionally omitted <==**

ˆ ˆ and the upper bound is again achieved for _u_ 2 = _u_ 2 and _v_ 2 = _v_ 2. Iterating up to _i_ = _s_ , we obtain that the solution of Eq. (42) is ( _U,_[ˆ] _V_[ˆ] ). 

From this formulation of ( _U,_[ˆ] _V_[ˆ] ) we can further relate it to a generalized eigenvalue problem and prove Proposition 1. 

_Proof of Proposition 1._ We omit the subscript _λ_ for clarity. We have 

**==> picture [191 x 26] intentionally omitted <==**

hence the columns of _U_ and _V_ can be restricted to span{ _f_[ˆ] 1[′] _[,...,][f]_[ˆ] _N_[ ′][}][ and][ span][{] _[f]_[ ˆ][1] _[,...,][f]_[ˆ] _[N]_[}][ respectively.][There-] fore every solution of Problem (42) can be written _U_ = _AR,V_ = _BS_ where _R,S_ ∈ _R[N]_[×] _[s]_ . The objective can then be re-written 

**==> picture [224 x 14] intentionally omitted <==**

and the constraints 

**==> picture [276 x 11] intentionally omitted <==**

Therefore Problem (42) is equivalent to 

**==> picture [101 x 48] intentionally omitted <==**

35 

with solution ( _R,_[ˆ] _S_[ˆ] ) linked to the solution ( _U,_[ˆ] _V_[ˆ] ) of Eq. (42) through _U_[ˆ] = _AR,_[ˆ] _V_[ˆ] = _BS_[ˆ] . The Lagrangian for this problem is 

**==> picture [301 x 12] intentionally omitted <==**

where Λ _,_ Γ ∈ R _[s]_[×] _[s]_ are diagonal matrices whose entries are the Lagrange multipliers (for a proof that Λ _,_ Γ can be taken as diagonal matrices see Appendix B in Ghojogh et al. (2019)). Equating the derivative of L with respect to the primal variables gives us 

**==> picture [163 x 10] intentionally omitted <==**

Multiplying on the left respectively by _R_[⊺] and _S_[⊺] and subtracting gives us 

**==> picture [80 x 11] intentionally omitted <==**

Plugging the constraints _R_[⊺] _QR_ = _S_[⊺] _JS_ = 1 implies Λ = Γ. Therefore we are looking for the largest diagonal real matrix Γ that solves the following expression with respect to _R,S_ : 

**==> picture [309 x 26] intentionally omitted <==**

with constraints _R_[⊺] _QR_ = _S_[⊺] _JS_ = 1. This is the generalized eigenvalue problem stated in Proposition 1. Denoting by {( _α_ ˆ _i_[⊺] _[,]_[ ˆ] _[β] i_[⊺][)][⊺][}] _i[s]_ =1[the][generalized][eigenvectors][associated][to][the] _[s]_[−][largest][generalized][eigenvalues,] ˆ the solution ( _R,_[ˆ] _S_[ˆ] ) of Eq. (43) is _R_[ˆ] = [ _α_ 1 _,..._ ˆ _αs_ ] _, S_[ˆ] = [ _β_[ˆ] 1 _,... β_[ˆ] _s_ ] ∈ R _[N]_[×] _[s]_ . 

_Proof of Proposition 2._ Recall that _f_[ˆ] _T,λ_ ∗ is defined as the solution of 

**==> picture [174 x 26] intentionally omitted <==**

For _f_ ∈ H[ˆ] _s_ , we define _β_ ≐ _V_[ˆ][∗] _f_ = (⟨ _f,_ ˆ _v_ 1⟩H _,...,_ ⟨ _f,_ ˆ _vs_ ⟩H)[⊺] ∈ R _[s]_ (those are the coordinates of _f_ in the basis ˆ { _v_ 1 _,...,_ ˆ _vs_ } of H[ˆ] _s_ . For _x_ ∈X we define 

**==> picture [310 x 13] intentionally omitted <==**

those are the coordinates of _ϕ_ ( _x_ ) in the basis { _v_ ˆ1 _,...,_ ˆ _vs_ } of H[ˆ] _s_ . We then have 

**==> picture [238 x 13] intentionally omitted <==**

Furthermore, 

**==> picture [173 x 13] intentionally omitted <==**

hence we can re-frame Eq. (7) as 

**==> picture [341 x 26] intentionally omitted <==**

with _f_[ˆ] _T,λ_ ∗ = _P_[ˆ] _f_[ˆ] _T,λ_ ∗ = _V_[ˆ] _V_[ˆ][∗] _f_[ˆ] _T,λ_ ∗ = _V β_[ˆ] _T,λ_ ∗ . Solving for Eq. (44) gives 

**==> picture [152 x 13] intentionally omitted <==**

**==> picture [326 x 34] intentionally omitted <==**

We can choose one form or the other depending if _nT_ ≤ _s_ or _nT_ > _s_ . 

36 

## **A.6 Proof of Remark 9** 

To get a bound that can handle the case where _N_ is exponential in _n_ we need bounds on the bias and variance that are free of constraints of the type _n_ ≥ _Aλ_ . We start with the bias. 

**Proposition 4.** _Suppose Assumption 5 holds with r_ ∈[0 _,_ 1] _. For λ_ ∈(0 _,_ 1] _and n_ ≥ 1 _,_ 

**==> picture [161 x 26] intentionally omitted <==**

_where J_ 1 _depends on κ and R._ 

_Proof._ We proved in the proof of Theorem 9 that 

**==> picture [189 x 25] intentionally omitted <==**

We then use the following decomposition 

**==> picture [213 x 16] intentionally omitted <==**

By Proposition 7, the first term is bounded by _Rλ[r]_ . By Lemma 7 and Eq. (31), 

**==> picture [304 x 15] intentionally omitted <==**

where we used Jensen’s inequality. Using the first order decomposition 

**==> picture [126 x 13] intentionally omitted <==**

we have 

**==> picture [274 x 32] intentionally omitted <==**

To bound this term, we use Proposition 13 with _A_ = _I_ H, _B_ = Σ _[r] i,λ_[−][1][,] _[C][A]_[=] _[κ]_[,] _[C][B]_[=] _[κλ][r]_[−][1][and] _[σ]_[2][=] _[κ]_[2] _[λ][r]_[−][1][,] and convert the high probability bound to a bound in expectation with Proposition 11. There is a universal constant _C_ > 0 such that 

hence, 

**==> picture [357 x 74] intentionally omitted <==**

where _J_ depends on _κ_ and _R_ . Putting it together, we obtain 

**==> picture [161 x 26] intentionally omitted <==**

where _J_ 1 depends on _κ_ and _R_ , which concludes the proof. 

For the variance part, we use the bound obtained in Theorem 8. For _λ_ ∈(0 _,_ 1] _,τ,δ_ ≥ log(2) and _N,n_ ≥ 1, with probability greater than 1 − 2 _e_[−] _[τ]_ − 4 _Ne_[−] _[δ]_ , 

**==> picture [265 x 27] intentionally omitted <==**

37 

with _c_ 1 a constant depending on _Y_ ∞, max _i_ ∈[ _N_ ] ∥ _fi_ ∥H, _κ_ and _R_ . Combining the bias and variance bound, we obtain that for all _λ_ ∈(0 _,_ 1], _δ,τ_ ≥ log(2), _N_ ≥ _τ_ and _n_ ≥ 1 large enough so that ~~√~~ _δnλ_[≤][1][,][with][probability] greater than 1 − 2 _e_[−] _[τ]_ − 4 _Ne_[−] _[δ]_ 

**==> picture [243 x 27] intentionally omitted <==**

with _C_ 2 a constant that depends on _Y_ ∞ _,κ,R_ and max _i_ ∈[ _N_ ] ∥ _fi_ ∥H. Plugging _δ_ = 12log( _Nn_ ), leads to 

**==> picture [289 x 26] intentionally omitted <==**

with probability greater than 1 − 2 _e_[−] _[τ]_ − _o_ (( _nN_ )[−][10] ). When _N_ is exponential in _n_ , the bias term dominates and it is minimized with _λ_ = _n_[−][1][/][2] _,_ leading to the bound in Remark 9. 

## **B Auxiliary Results** 

**Proposition 5.** _Under Assumption 2,_ 

**==> picture [81 x 25] intentionally omitted <==**

_is such that_ ran _CN_ = H _s._ 

_Proof. CN_ = _SS_[∗] where _S_ ∶ R _[N]_ →H _,α_ ↦∑ _[N] i_ =1 _[α][i][f][i]_[,][hence][ran] _[C][N]_[=][ ran] _[SS]_[∗][=][ ran] _[S]_[=][ span][{] _[f]_[1] _[,...,f][N]_[} = H] _[s]_[,] where the last equality follows from Assumption 2. 

**Proposition 6.** _Let_ H _be a Hilbert space, let C and D be two bounded self-adjoint positive semidefinite linear operators and λ_ > 0 _, then_ 

_and_ 

**==> picture [210 x 59] intentionally omitted <==**

_Proof._ First note that 

**==> picture [263 x 40] intentionally omitted <==**

Hence, 

**==> picture [280 x 45] intentionally omitted <==**

**Lemma 11.** _Let_ H _be a separable RKHS on_ X _w.r.t. a bounded and measurable kernel K, and µ be a probability distribution on_ X _._ Σ _µ_ ≐ E _X_ ∼ _µ_ [ _K_ ( _X,_ ⋅) ⊗ _K_ ( _X,_ ⋅)] _is the covariance operator associated to_ (H _,µ_ ) _. For all λ_ > 0 _:_ 

**==> picture [264 x 20] intentionally omitted <==**

38 

N( _λ_ ) = Tr ((Σ _µ_ + _λI_ H)[−][1] Σ _µ_ ) _is the effective dimension associated to_ (H _,µ_ ) _. Under Assumption 3 with c_ > 0 _and_ 0 < _p_ ≤ 1 _,_ 

**==> picture [62 x 11] intentionally omitted <==**

_with D_ ≐ _c_ /(1 − _p_ )1 _p_ <1 + Tr(Σ _µ_ )1 _p_ =1 _. Furthermore, under Assumption 4 with kα,_ ∞ > 0 _and_ 0 < _α_ ≤ 1 _,_ 

**==> picture [164 x 21] intentionally omitted <==**

_Proof._ The first inequality is proven in Caponnetto and De Vito (2007) for _p_ < 1 and in Lemma 11 Fischer and Steinwart (2020) for _p_ = 1. The second inequality is proven in Lemma 13 Fischer and Steinwart (2020). 

The forthcoming result provides a bound on the approximation error _fi,λ_ − _fi_ . While similar bounds can be found in Theorem 4 Smale and Zhou (2007) (with the correspondence _r_[′] = _r_ + 1/2) and Lemma 14 Fischer and Steinwart (2020) (with the correspondence _β_ = 2 _r_ + 1), it is worth noting that these references assert that the bound saturates at _r_ = 1/2 when measuring the approximation error in both the _L_ 2-norm and the H-norm. In contrast, our result reveals that the saturation point occurs at _r_ = 1 when utilizing the H-norm. Notably, we are aware of only one reference, Blanchard and Mücke (2018), that acknowledges the saturation point for _r_ exceeding 1/2 when the approximation is measured in norms stronger than the _L_ 2−norm. As they consider a setting with abstract spectral regularization techniques, we offer our own proof. 

**Proposition 7.** _For i_ ∈[ _N_ ] _and ω_ ∈{0 _,_ 1/2} _, let_ ∥⋅∥ _ω be_ ∥⋅∥H _if ω_ = 0 _and_ ∥⋅∥ _L_ 2( _µi_ ) _if ω_ = 1/2 _. Then if Assumption 5 is satisfied with_ 0 ≤ _r_ ≤ 1 − _ω we have_ 

**==> picture [90 x 12] intentionally omitted <==**

_Proof._ Fix _i_ ∈[ _N_ ] and _ω_ ∈{0 _,_ 1/2}. With the same argument as in Eq. (21) we have that if _f_ ∈H, then ∥ _f_ ∥ _L_ 2( _µi_ ) = ∥Σ _i_[1][/][2] _f_ ∥H. Therefore, by Eq. (31), 

**==> picture [148 x 93] intentionally omitted <==**

where in the last inequality we used _r_ + _ω_ ≤ 1. 

Analysis of the estimation error _f_[ˆ] _i,λ_ − _fi,λ_ in kernel ridge regression is an important part of our theory. Below we provide two different results on this analysis. 

**Theorem 12** (Theorem 1 Smale and Zhou (2007)) **.** _Let f_[ˆ] _i,λ be the solution from Eq._ (5) _and fi,λ its population version as defined in Eq._ (31) _. Suppose Assumption 6 holds with Y_ ∞ ≥ 0 _. For i_ ∈[ _N_ ] _, δ_ ≥ log(2) _and λ_ > 0 _, the following bound is satisfied with probability not less than_ 1 − 2 _e_[−] _[δ]_ 

**==> picture [103 x 24] intentionally omitted <==**

Theorem 16 Fischer and Steinwart (2020) provides a refined bound on the estimation error at the cost of an additional constraint on the relationship between _λ_ and _n_ . The following result is a simple extension of this result. 

39 

**Theorem 13.** _Let f_[ˆ] _i,λ be the solution from Eq._ (5) _and fi,λ its population version as defined in Eq._ (31) _. Suppose Assumptions 3, 4 and 6 hold with c_ > 0 _,_ 0 < _p_ ≤ 1 _, α_ ∈[ _p,_ 1] _, kα,_ ∞ ≥ 0 _and Y_ ∞ ≥ 0 _. For δ_ ≥ 1 _, λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _, and n_ ≥ _c_ 0 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α] , the following bound is satisfied with probability not less than_ 1 − 4 _e_[−] _[δ]_ 

**==> picture [166 x 29] intentionally omitted <==**

_where c_ 0 _depends on kα,_ ∞ _,D and c_ 1 _depends on Y_ ∞ _,kα,_ ∞ _,D and R. Furthermore, if_ Σ _i has finite rank k with eigensystem_ {( _ei,j,λi,j_ )} _[k] j_ =1 _[such][that]_ √ _λi,jei,j is an orthonormal basis of_ range(Σ _i_ ) _. Then for δ_ ≥ 1 _,_ 0 < _λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _, and n_ ≥ _c_ 2 _δk_ (1 + _p_ log( _λ_[−][1] )) _, the following bound is satisfied with probability not less than_ 1 − 4 _e_[−] _[δ]_ 

**==> picture [291 x 27] intentionally omitted <==**

_where c_ 2 _depends D,κ,_ min _i_ ∈[ _N_ ]{ _λi,d_ } _and c_ 3 _depends on Y_ ∞ _,κ,_ max _i_ ∈[ _N_ ]{ _λi,_ 1} _,_ min _i_ ∈[ _N_ ]{ _λi,d_ } _and R._ 

_Proof._ Define the following two terms for _i_ ∈[ _N_ ]: 

**==> picture [134 x 43] intentionally omitted <==**

Apply Theorem 16 in Fischer and Steinwart (2020) (by letting _γ_ = 1 in their result), for _τ_ ≥ 1, with probability over 1 − 4 _e_[−] _[δ]_ for _n_ ≥ _Ai,λ,δ_ , 

**==> picture [382 x 32] intentionally omitted <==**

By Lemma 11, under Assumption 3, we have N _i_ ( _λ_ ) ≤ _Dλ_[−] _[p]_ ; and by Proposition 7, under Assumption 5, we have ∥ _fi_ − _fi,λ_ ∥[2] _L_ 2[≤] _[R]_[2] _[λ]_[2] _[r]_[+][1][(plug] _[ω]_[ =][ 1][/][2][in][Proposition][7][).][In][addition,][by][Assumption][4][,][we][have] 

**==> picture [141 x 26] intentionally omitted <==**

where the second last step follows from Proposition 7 with _ω_ = 0 and the last step uses _λ_ ≤ 1. As such, denote _YR_ ≐ max{ _Y_ ∞ _,kα,_ ∞ _R_ } we have 

**==> picture [277 x 61] intentionally omitted <==**

where _b_ 0 is a constant that depends on _Y_ ∞ _,kα,_ ∞ _,D_ and _R_ . We obtain the desired bound by noticing that _α_ ≤ 1 ≤ 2 _r_ + _p_ + 1 and _λ_ ≤ 1. 

Next, let us simplify the constraint _n_ ≥ _Ai,λ,δ_ . Let us fix some lower bound 0 < _c_ ≤ 1 with _c_ ≤ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥. _λ_ will be chosen as a function of ( _n,N_ ) or _n_ only with the property that _λ_ → 0 when _n_ →∞. We choose an index bound _n_ 0 ≥ 1 such that _λ_ ≤ _c_ ≤ min {1 _,_ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥} for all _n_ ≥ _n_ 0. Using the definition _qi,λ_ , _λ_ ≤ _c_ ≤ min _i_ ∈ _N_ ∥Σ _i_ ∥, N _i_ ( _λ_ ) ≤ _Dλ_[−] _[p]_ from Lemma 11, we get, for _n_ ≥ _n_ 0, 

**==> picture [213 x 65] intentionally omitted <==**

40 

For the second bound, since Σ _i_ has finite rank _k_ , let us show that Assumption 4 holds with _α_ = 0. We have, 

**==> picture [353 x 27] intentionally omitted <==**

where we used ∥√ _λi,jei,j_ ∥H = 1, and ∥ _ϕ_ ( _x_ )∥[2] H[=] _[ K]_[(] _[x,x]_[) ≤] _[κ]_[2][.][As][such,][the][constant][for][Assumption][4][can][be] taken as _k_ 0[2] _,_ ∞[=] _[ kκ]_[2][/] _[λ][i,k]_[.][Apply][Theorem][16][in][Fischer][and][Steinwart][(][2020][)][(by][letting] _[γ]_[=][ 0][this][time)][and] let _α_ = 0, with probability over 1 − 4 _e_[−] _[δ]_ for _n_ ≥ _Ai,λ,δ_ , 

**==> picture [363 x 28] intentionally omitted <==**

We have N _i_ ( _λ_ ) = Tr (Σ _i_ Σ[−] _i,λ_[1][) = ∑] _j[k]_ =1 _λλi,ji,j_ + _λ_[≤] _[k]_[.][Furthermore,][since] _[K]_[is][bounded][by] _[κ]_[2][,][we][have] 

**==> picture [367 x 19] intentionally omitted <==**

Therefore, 

**==> picture [383 x 31] intentionally omitted <==**

Finally, we obtain the result using _λ_[−] _i,k_[1][≤(][min] _[i]_[∈[] _[N]_[]][{] _[λ][i,k]_[})][−][1][,] _[λ][i,]_[1][≤][max] _[i]_[∈[] _[N]_[]][{] _[λ][i,]_[1][}][and][(since] _[λ]_[≤][1][)] ∥ _fi_ − _fi,λ_ ∥ _L_ 2 ≤ _Rλ[r]_[+][1][/][2] ≤ _R_ . Note that plugging _α_ = 0 and _k_ 0[2] _,_ ∞[=] _[ kκ]_[2][/] _[λ][i,k]_[in] _[ A][i,λ,δ]_[gives the constraint] _[ n]_[ ≥][8] _[δkκ]_[2] _[q][i,λ]_[/] _[λ][i,k]_[.][We can similarly] simplify it to _n_ ≥ 8 _δkκ_[2] (log(4 _eD_ ) + _p_ log( _λ_[−][1] ))(min _i_ ∈[ _N_ ]{ _λi,k_ })[−][1] for 0 < _λ_ < min {1 _,_ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥}. 

The next results provide bounds on the bias _fi_ − E( _f_[ˆ] _i,λ_ ) in kernel ridge regression. 

**Proposition 8.** _Let f_[ˆ] _i,λ be the solution from Eq._ (5) _. Suppose Assumptions 3 and 5 hold with_ 0 < _p_ ≤ 1 _and r_ ∈[0 _,_ 1] _. We have, for any λ_ ∈(0 _,_ 1] _, δ_ ≥ 1 _, and n_ ≥ _c_ 1 _δλ_[−] _[p]_[−][1] _,_ 

**==> picture [139 x 27] intentionally omitted <==**

_where c_ 1 _is a constant depending only on D, κ, and c_ 2 _is a constant depending only on R, κ._ 

_Proof._ By Lemma 7 we have 

**==> picture [231 x 86] intentionally omitted <==**

To bound E ∥Σ _i,λ_ Σ[ˆ][−] _i,λ_[1][∥][,][we][notice][that] 

**==> picture [233 x 14] intentionally omitted <==**

As a result, we have, 

**==> picture [279 x 23] intentionally omitted <==**

41 

where in the second step we used Neumann series, provided ∥(Σ _i_ − Σ[ˆ] _i_ )Σ[−] _i,λ_[1][∥<][1][.] We are left to bound ∥(Σ _i_ − Σ[ˆ] _i_ )Σ[−] _i,λ_[1][∥][.][By][Proposition][5.3][Blanchard][and][Mücke][(][2018][),][for][any] _[n]_[ ≥][1][,] _[λ]_[ ∈(][0] _[,]_[1][]][and] _[δ]_[≥][log][(][2][)][,][it] holds with probability at least 1 − 2 _e_[−] _[δ]_ , 

**==> picture [354 x 31] intentionally omitted <==**

where we used Lemma 11 and _c_ 0 depends on _κ,D_ . Note that on one hand, 

and on the other hand, 

**==> picture [138 x 66] intentionally omitted <==**

Note that _p_ + 1 ≥ 1, therefore, since _λ_ ≤ 1, for _n_ ≥ _δ_ max(9 _c_[2] 0 _[,]_[3] _[c]_[0][)] _[λ]_[−] _[p]_[−][1] _[,]_[we][have][with][probability][over][1][ −][2] _[e]_[−] _[δ]_ ∥(Σ _i_ − Σ[ˆ] _i_ )Σ[−] _i,λ_[1][∥≤][1][/][3][ +][ 1][/][3][ =][ 2][/][3] _[.]_ 

This further implies that with probability over 1 − 2 _e_[−] _[δ]_ , 

**==> picture [202 x 26] intentionally omitted <==**

Moreover, we have 

**==> picture [151 x 24] intentionally omitted <==**

As such, we have 

**==> picture [268 x 57] intentionally omitted <==**

**Proposition 9.** _Let f_[ˆ] _i,λ be the solution from Eq._ (5) _. Suppose Assumptions 3, 4, 5 hold with_ 0 < _p_ ≤ _α_ ≤ 1 _and r_ ∈(0 _,_ 1] _. We have, for any δ_ ≥ 1 _, λ_ < 1∧ min _i_ ∈[ _N_ ] ∥Σ _i_ ∥ _, and n_ ≥ _c_ 0 _δ_ (1 + _p_ log( _λ_[−][1] )) _λ_[−] _[α] ,_ 

**==> picture [151 x 14] intentionally omitted <==**

_where c_ 0 _depends on kα,_ ∞ _,D and c_ 1 _depends on R,κ._ 

_Proof._ By Lemma 7, for all _i_ ∈[ _N_ ], 

Notice that we have 

**==> picture [111 x 43] intentionally omitted <==**

Furthermore by Proposition 6, we have 

**==> picture [95 x 16] intentionally omitted <==**

−1 where _β_[ˆ] _i,λ_ ≐( _I_ − Σ[−] _i,λ_[1][/][2][(][Σ] _[i]_[ −][ˆΣ] _[i]_[)][Σ][−] _i,λ_[1][/][2][)] . By Lemma 17 Fischer and Steinwart (2020), for all _i_ ∈[ _N_ ], _δ_ ≥ 1, _λ_ > 0 and _n_ ≥ 1 with probability at least 1 − 2 _e_[−] _[δ]_ 

**==> picture [244 x 27] intentionally omitted <==**

42 

with 

**==> picture [129 x 27] intentionally omitted <==**

Therefore, if _n_ ≥ max _i_ ∈[ _N_ ] 8 _kα,_[2] ∞ _[δq][i,λ][λ]_[−] _[α]_[,][with][probability][at][least][1][ −][2] _[e]_[−] _[δ]_ 

**==> picture [189 x 26] intentionally omitted <==**

Consequently, _β_[ˆ] _i,λ_ can be represented by the Neumann series. In particular, the Neumann series gives us the following bound 

**==> picture [479 x 106] intentionally omitted <==**

On the other hand, 

**==> picture [325 x 93] intentionally omitted <==**

where we used _λ_ ≤ 1. Finally the constraint _n_ ≥ 8 _kα,_[2] ∞ _[δq][i,λ][λ]_[−] _[α]_[, can be simplified to] _[ n]_[ ≥] _[c]_[0] _[δ]_[ (][1][ +] _[ p]_[log][(] _[λ]_[−][1][))] _[λ]_[−] _[α]_[,] where _c_ 0 depends on _kα,_ ∞ _,D_ as in the proof of Theorem 13. 

**Proposition 10.** _For all i_ ∈[ _N_ ] _and_ 0 < _λ_ ≤ 1 _it holds almost surely that_ 

**==> picture [174 x 33] intentionally omitted <==**

_with c_ ≐ _Y_ ∞[2][+][ max] _i_ ∈[ _N_ ][∥] _[f][i]_[∥][2] H _[.]_ 

_Proof._ By definition of _f_[ˆ] _i,λ_ in Eq. (5), we have 

**==> picture [196 x 102] intentionally omitted <==**

43 

where in the second inequality we plugged _f_ = 0 and in the last inequality we used the bound ∣ _yi,j_ ∣≤ _Y_ ∞ for all _i_ ∈[ _N_ ] and _j_ ∈[ _n_ ]. We therefore have ∥ _f_[ˆ] _i,λ_ ∥H ≤ _Y_ ∞/ ~~√~~ _λ_ and the same bound holds for ∥ _f_[ˆ] _i,λ_[′][∥][H][.][Using] Lemma 7, we then have 

**==> picture [278 x 97] intentionally omitted <==**

where the last inequality follows from _λ_ ∈(0 _,_ 1]. Similarly, using Eq. (32) we have 

**==> picture [232 x 70] intentionally omitted <==**

## **C Concentration inequalities** 

**Proposition 11.** _Let X be a random variable taking values in_ R+ _such that_ 

**==> picture [128 x 27] intentionally omitted <==**

_v,b_ > 0 _, c_ ≥ 1 _, then for all τ_ ≥ 0 

**==> picture [71 x 12] intentionally omitted <==**

_with probability at least_ (1 − _ce_[−] _[τ]_ )+ _, where x_ + = max(0 _,x_ ) _, x_ ∈ R _._ 

_Proof._ Solving for _τ_ =[1] 2 _v_[2] _t_ +[2] _bt_[we][get][as][positive][solution] _[t]_[ =] ~~√~~ 2 _τv_[2] + _τ_[2] _b_[2] + _τb_ . Observing that 

**==> picture [66 x 12] intentionally omitted <==**

gives the bound. 

The next proposition provides a high probability bound on the “whitened” difference between the population and empirical covariance on H[ˆ] _s_ in operator norm. 

**Proposition 12.** _For λ_ ∗ > 0 _, τ_ ≥ 2 _._ 6 _and nT_ ≥ 1 _, the following operator norm bound is satisfied with µ[n] T[T][-] probability not less than_ 1 − _e_[−] _[τ]_ 

**==> picture [385 x 50] intentionally omitted <==**

44 

_Proof._ We apply Lemma 24 from Hsu et al. (2012) to H[ˆ] _s_ and _µT_ . ∆ _λ_ , _n_ and _x_ in their setting corresponds to ˆ Σ[−] ˆ[1][/][2] _P_ (Σ _T_ − ˆΣ _T_ ) ˆ _P_ Σ[−] ˆ[1][/][2] _[n][T]_[and] _[Pϕ]_[ˆ][(] _[X]_[)][in][our][setting.][As][H][ˆ] _[s]_[is][finite-dimensional,][their][“Condition][1”][is] _P ,λ_ ∗ _P ,λ_ ∗[,] automatically satisfied and we have 

**==> picture [158 x 29] intentionally omitted <==**

where { _λ_[ˆ] 1 _,..., λ_[ˆ] _s_ } are the eigenvalues of Σ ˆ _P_[.][For][their][“Condition][2”,][we][have][for][all] _[x]_[ ∈X][,][since][∥] _[P]_[ˆ][∥≤][1][and] the kernel is bounded, 

**==> picture [205 x 22] intentionally omitted <==**

Hence we take _ρλ_ ∗ = _κ_ ( _d_[˜] _λ_ ∗ _λ_ ∗)[−][1][/][2] and we have _ρ_[2] _λ_ ∗ _[d]_[˜] _[λ]_ ∗[=] _[ κ]_[2][/] _[λ]_[∗] _[.]_[ We conclude by Lemma 24][ Hsu et al.][ (][2012][).] 

In the next two propositions we omit the index _i_ ∈[ _N_ ] as it applies for any task source task. Let F _,_ G be separable Hilbert spaces. Let _A_ ∶H →F, _B_ ∶H →G be bounded operator. The next result provides a high probability bound on 

**==> picture [82 x 14] intentionally omitted <==**

**Proposition 13.** _Let CA,CB,σ_ > 0 _be constants such that_ E∥ _Aϕ_ ( _X_ )∥F ∥ _Bϕ_ ( _X_ )∥G ≤ _σ_[2] _,_ ∥ _Aϕ_ ( _X_ )∥F ≤ _CA and_ ∥ _Bϕ_ ( _X_ )∥G ≤ _CB almost surely, then_ 

**==> picture [238 x 26] intentionally omitted <==**

_Alternatively, we get for all τ_ ≥ 0 _, with probability at least_ (1 − 2 _e_[−] _[τ]_ )+ _,_ 

**==> picture [206 x 26] intentionally omitted <==**

_where C is a universal constant._ 

_Proof._ 

**==> picture [190 x 25] intentionally omitted <==**

where _hx_ ≐ _Aϕ_ ( _x_ ) and _lx_ ≐ _Bϕ_ ( _x_ ). One one hand, almost surely 

**==> picture [150 x 11] intentionally omitted <==**

On the other hand, 

**==> picture [206 x 12] intentionally omitted <==**

Hence exploiting Corollary 2 in the Hilbert space _HS_ with _b_ = _CACB_ and _v_[2] = _σ_[2] _CACB_ , we get 

**==> picture [238 x 26] intentionally omitted <==**

Then by Proposition 11, for all _τ_ ≥ 0, with probability at least (1 − 2 _e_[−] _[τ]_ )+, 

**==> picture [206 x 27] intentionally omitted <==**

45 

As a special case we obtain a high probability bound on the “whitened” difference between the population and empirical covariance on H in Hilbert-Schmidt norm. 

The following bound is a Bernstein-like concentration inequality for Hilbert space-valued random variables. It can be deduced from Corollary 1 Pinelis and Sakhanenko (1986). 

**Theorem 14.** _Let H be a separable Hilbert space and X_ 1 _,...,Xn be independent random variables with values in H. If for some constants v,b_ > 0 _, for all j_ ∈[ _n_ ] 

**==> picture [208 x 137] intentionally omitted <==**

_Then_ 

**Corollary 2.** _Let H be a separable Hilbert space and X_ 1 _,...,Xn be independent random variables with values in H. If for some constants v,b_ > 0 _, for all j_ ∈[ _n_ ] _,_ ∥ _Xj_ ∥ _H_ ≤ _b almost surely and_ E∥ _Xj_ ∥[2] _H_[≤] _[v]_[2] _[,]_ 

_Proof._ For all _j_ ∈[ _n_ ] 

**==> picture [357 x 22] intentionally omitted <==**

hence using Theorem 14 with _v_[2] = 4 _v_[2] and _b_ = 2 _b_ gives the result. 

**Theorem 15** (Bounded concentration in Hilbert spaces) **.** _Suppose that_ ( _Xi_ ) _[n] i_ =1 _[are][zero-mean][independent] random variables with values in a Hilbert space_ ( _H,_ ⟨⋅ _,_ ⋅⟩) _and such that_ max _i_ =1 _,...,n_ ∥ _Xi_ ∥≤ _C_ < ∞ _. Then for all t_ ≥ 0 _,_ 

**==> picture [121 x 26] intentionally omitted <==**

_Proof._ The inequality can be deduced from Theorem 3.5 Pinelis (1994). Their result applies to martingales ( _Zj_ ) _j_ ≥0 of Bochner-integrable random vectors in a (2 _,D_ )−smooth separable Banach space (X _,_ ∥⋅∥). A Banach space (X _,_ ∥⋅∥) is (2 _,D_ )−smooth if for all ( _x,y_ ) ∈X[2] , 

**==> picture [160 x 13] intentionally omitted <==**

In particular, any Hilbert space is (2 _,_ 1)−smooth by the parallelogram identity. Theorem 3.5 Pinelis (1994) states that if the increments of the martingale ( _Zj_ ) _j_ ≥0 are such that ∑[∞] _j_ =1[∥] _[Z][j]_[−] _[Z][j]_[−][1][∥][2] ∞[≤] _[b]_[2] ∗[for][some] _[b]_[∗][>][0][.] Then for all _r_ ≥ 0, 

**==> picture [317 x 26] intentionally omitted <==**

Let us fix _n_ ≥ 1, and consider a sequence ( _Xi_ ) _[n] i_ =1[of][zero-mean][independent][random][variables][with][values][in][a] Hilbert space ( _H,_ ⟨⋅ _,_ ⋅⟩) such that ∥ _Xi_ ∥∞ ≤ _C_ < ∞ for all _i_ = 1 _,...,n_ . Then ( _Zj_ ) _j_ ≥0 such that 

**==> picture [226 x 26] intentionally omitted <==**

is a martingale on _H_ and its increments _dj_ ≐ _Zj_ − _Zj_ −1 satisfies 

**==> picture [163 x 11] intentionally omitted <==**

46 

hence, 

**==> picture [125 x 26] intentionally omitted <==**

Therefore, applying Eq. (46) to ( _Zj_ ) _j_ ≥0 with X = _H_ , _D_ = 1 and _b_[2] ∗[=] _[ nC]_[2][leads][to,][for][all] _[t]_[ ≥][0][,] 

**==> picture [291 x 26] intentionally omitted <==**

Rescaling by 1/ _n_ gives the final result. 

## **D Additional Experimental Results** 

**==> picture [215 x 129] intentionally omitted <==**

**==> picture [216 x 129] intentionally omitted <==**

Figure 3: **(Left)** Meta Learning versus Oracle: Comparison of the squared excess risk on the target task for the oracle estimator _f_[ˆ] oracle (dotted red line) and the meta learning estimator _f_[ˆ] _T,λ_ ∗ trained with different number of tasks _N_ (solid lines). _x_ −axis represents the size of the dataset for the target task ( _nT_ ). **(Right)** Effect of under-regularization: Comparison of the squared excess risk of the meta learning estimator trained with _λ_ = ( _nN_ )[−] 5[2] (red dotted line) and _λ_ = _n_[−] 5[2] (blue solid line). _x_ −axis represents the number of source tasks ( _N_ ). For both figures _n_ = 500, _s_ = 50 and results are averaged over 20 generations of the source and target tasks. 

47 

