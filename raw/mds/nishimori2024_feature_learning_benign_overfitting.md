Information Geometry https://doi.org/10.1007/s41884-024-00142-3 ~~**RESEARCH PAPER**~~ 

**==> picture [29 x 29] intentionally omitted <==**

## **Feature learning and generalization error analysis of two-layer linear neural networks for high-dimensional inputs** 

## **Hayato Nishimori[1] · Taiji Suzuki[1,2]** 

Received: 10 September 2023 / Revised: 15 June 2024 / Accepted: 12 July 2024 © The Author(s) 2024 

## **Abstract** 

It is well known that a model can generalize even when it completely interpolates the training data, which is known as the benign overfitting. Indeed, several work have theoretically revealed that the minimum-norm interpolator can exhibit the benign overfitting. On the other hand, deep learning models such as two-layer neural networks have been reported to outperform “shallow” learning models such as kernel methods under appropriate model sizes by adaptively learning the basis functions to the data. This mechanism is called feature learning, and it is known empirically to be beneficial even when the model size is large. However, it is generally difficult to show that benign overfitting occurs in learning models with feature learning especially for regression problems. In this study, we then analyze the predictive error of the estimator after one step feature learning in a two-layer linear neural network optimized by gradient descent methods and study the effect of feature learning on benign overfitting. The results show that feature learning reduces bias compared to a one-layer linear regression model without feature learning, especially when the eigenvalues of the covariance of input decay slowly. On the other hand, we clarify that the variance is hardly changed by feature learning. This differs significantly from the results for benign overfitting in the situation without feature learning and indicates the usefulness of feature learning. 

**Keywords** Neural network · Feature learning · Benign overfitting · Error analysis 

Communicated by Noboru Murata. 

> B Hayato Nishimori benzene-ring-78@g.ecc.u-tokyo.ac.jp 

Taiji Suzuki taiji@mist.i.u-tokyo.ac.jp 

- 1 The University of Tokyo, Bunkyo City, Japan 

- 2 Center for Advanced Intelligence Project, RIKEN, Chuo City, Japan 

**==> picture [133 x 12] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

## **1 Introduction** 

In a standard learning theory, it is usually recommended not to overfit to the training data because overfitting leads to poor predictive performance. Then, several regularization or variable selection are usually applied to restrict the degrees of freedom of the model. 

However, it has been reported for various models experimentally that overparametrized models generalize very well even when no regularization is applied [5, 16, 21]. This phenomenon is called benign overfitting and has been the subject of significant research in recent years. Theoretical analyses that explain benign overfitting are carried out as Bartlett et al. [4, 19], Hastie et al. [10], Xu and Hsu [20] in the one-layer linear regression model, and Li et al. [15], Louart et al. [14], Mei and Montanari [13] in the random feature model of the two-layer nonlinear neural network. 

By the way, it has been reported in various situations that “deep” learning models such as two-layer neural networks outperform “shallow” learning models such as kernel methods under appropriate model sizes [11, 18]. This is considered to be because deep learning models can adaptively learn basis functions, which is known as feature learning. On the other hand, deep learning models show good generalization performance in practice without necessarily choosing an appropriate model size. In particular, the model size for deep learning is often larger than the sample size. 

Ba et al. [3] gives an analysis of the predictive error of the estimators after one step feature learning of a two-layer neural network, and shows that the model with feature learning generalizes beyond the lower bound of the predictive error of the linear models such as kernel methods, especially when the sample size is larger than the model size. However, the analysis is given in the proportional limit, and finitedimensional analysis has not been carried out. In another study, Damian et al. [8] analyzed the learning ability of a one step feature learning model in the setting that the output depends only a low dimensional subspace with dimensionality _r_ in the _d_ - dimensional input space. According to Damian et al. [8], the one-step gradient feature learning makes the model generalize even when _n_ ≍ _d_[2] _r_ + _dr[p]_ while random feature models require larger sample size _n_ ≳ _d[p]_ where _p_ is the degrees of polynomial to be estimated. However, the effect of feature learning in a situation where _n < d_ is not reported. Therefore, it is an important question to study whether a model with feature learning achieves benign overfitting when the sample size is smaller than the input dimension. 

In this study, we investigate three different feature learning procedures and their effect to the predictive performance in the interpolation regime where the model is the two-layer linear neural network. Specifically, the three procedures we investigate are (i) training the first layer by one-step vanilla gradient descent, (ii) that by natural gradient descent and (iii) that by linear regression; and on top of that, we obtain the minimum norm interpolator using the second layer. The predictive performances of the three procedures are analyzed in the finite-dimensional overparametrized regime, where the dimension of the input data is larger than the sample size, and then we compare the performances between the three procedures so that we reveal what kind offeaturelearningmethodiseffectiveforbenignoverfitting.Asasummary,weprovide the following contributions in this paper: 

123 

Feature learning and generalization error analysis of… 

First, we analyze a situation where the step size for the feature learning is small. We give an explicit formula of the difference between the predictive errors with and without feature learning. Then, we characterize when the feature learning can reduce the predictive error. We also confirm that our theoretical evaluation is consistent with numerical experiments. As a consequence, we see that, in “difficult” instances where the true signal is not well aligned to the input, the NGD can reduce the bias while the GD cannot. This indicates the effectiveness of NGD in the interpolation regime. 

Second, we evaluate the generalization error when we employ a larger step size for feature learning. Then, we see that the generalization error after feature learning does not deteriorate compared with that of the non-feature learned linear interpolator. We also give a detailed theoretical analysis that characterizes the differences of predictive errors between the three approaches. 

In the former, we find that the reduction of predictive errors induced by feature learning becomes larger as the eigenvalues of the covariance of the input decays more slowly, i.e., the regression problem becomes more difficult. Though it is known that when the eigenvalues are polynomially decaying with _λi_ = _i_[−] _[(]_[1][+] _[α)] (α >_ 0 _)_ , the optimal minimax rate can be achieved by one-layer linear regression, we show theoretically and experimentally that feature learning significantly reduces the bias while feature learning does not change the variance when _α <_ 0. 

Amari et al. [1] which studied the predictive error of linear interpolator with preconditioning reported a tradeoff in which the bias is reduced by preconditioning while the variance is increased. However, in this study, we show that only the bias decreases and the variance hardly increases. This significant difference is because we deal with a linear interpolator computed after feature learning while Amari et al. analyzed only a linear interpolator without feature learning. In addition, Ba et al. [3] analyzed the predictive error after one gradient step feature learning, however, they considered the proportional limit where _n_ and _d_ are taken limit to ∞ where their ratio converges to a positive constant _n_ ≍ _d_ . On the other hand, our analysis does not take the proportional limit and is valid in a general finite sample and finite dimensional setting. As a consequence, the reduction of the predictive error can be shown even in a setting of _d_ = _ω(n)_ . 

## **1.1 Notations** 

Throughout this paper, for a vector _**v**_ ∈ R _[n]_ and a positive definite symmetric matrix _�_ ∈ R _[n]_[×] _[n]_ , we let ∥ _**v**_ ∥[2] _�_[:=] _**[v]**_[⊤] _[�]_ _**[v]**_[and][∥] _**[v]**_[∥] _[�]_[:=] �∥ _**v**_ ∥[2] _�_[.][For][a][square][matrix] _[A]_[∈] R _[n]_[×] _[n]_ , its operator norm is denoted by ∥ _A_ ∥op and the _i_ -th largest eigenvalue of _A_ , allowingforties,isdenotedbyby _μi (A)_ .Also,foramatrix _B_ ∈ R _[n]_[×] _[m]_ ,let _B_ 0: _k_ ∈ R _[n]_[×] _[k]_ denote the submatrix of _B_ from which the left _k_ columns are taken and _Bk_ :∞ ∈ R _[n]_[×] _[m]_[−] _[k]_ denotes the submatrix of _B_ consisting of the other columns. Similarly, for _**v**_ ∈ R _[n]_ , let _**v**_ 0: _k_ ∈ R _[k]_ be a vector consisting of the upper _k_ components of _**v**_ and _**v** k_ :∞ ∈ R _[n]_[−] _[k]_ be a vector consisting of the other components. Let _O(_ · _)_ and _o(_ · _)_ denote the Landau’s asymptotic big-O and little-o notations respectively, and when these notations are used for fixed finite demensional matrices and vectors, assume that the asymptotic property holds for each component. In addition, for a sequence of random 

123 

N. Hayato, S. Taiji 

def variables _Xn_ , _Xn_ = _o_ P _(_ 1 _)_ ⇐⇒ for every _ε >_ 0, lim _n_ →∞ _P(_ | _Xn_ | ≤ _ε)_ = 1 and def def _Xn_ = _o_ P _( f (n))_ ⇐⇒ _Xn/ f (n)_ = _o_ P _(_ 1 _)_ . Similarly, _Xn_ = _O_ P _(_ 1 _)_ ⇐⇒ for every _ε >_ 0, there exist a constant _K (ε)_ and an integer _N (ε)_ such that if _n_ ≥ _N (ε)_ then def _P(_ | _Xn_ | ≤ _K (ε))_ ≥ 1 − _ε_ , and _Xn_ = _O_ P _( f (n))_ ⇐⇒ _Xn/ f (n)_ = _O_ P _(_ 1 _)_ . 

## **1.2 Related work** 

**Benign overfitting of linear estimator.** Recent works provided analyses of linear models under high demensional input [1, 4, 10, 19, 20]. In particular, feature learning in the two-layer linear neural network can be regarded as a kind of preconditioning analyzed in Amari et al. [1]. However this result cannot be applied to this study because it considered only diagonalizable preconditioning. Benign overfitting was also analysed in the random feature model of the two-layer nonlinear neural network [13–15]. 

All of these estimator are linear estimators, that is, they are linear to the output data. However, the estimator we consider in this study is not linear because feature learning in the first layer induced nonlinearity to the output data. 

**Two-layer neural network model.** Two-layer neural network with feature learning is one of the simplest deep learning models. It is known theoretically that appropriately sized deep learning estimators outperform linear estimators for certain classes of functions [11, 18]. However deep learning estimators perform well even when the appropriate model size is not chosen and then some works analyzed such situation [2, 3, 6, 8, 9]. In particular, it has been pointed out that the transition trajectories of the parameters in the learning process are highly dependent on the initial stage of learning [12], and Ba et al. [3] showed that the estimator with one step feature learning outperform linear estimators where sample size is larger than input dimension. On the other hand, we consider the estimators with one step feature learning where input dimension is larger than sample size. In addition, this study performs analysis on finite data while Ba et al. [3] did in proportional limit. The importance of analysis with finite data has been pointed out in detail by Cheng and Montanari [7]. 

## **1.3 Paper organization** 

Section 2 describes the learning model and input–output data setup that is the subject of theoretical analysis in this study, and provides an interpretation of the proposed model. In Sect. 3, we give an analysis of the predictive errors given by these learning methods and also refer to a brief note and discussion of the results. In Sect. 4, we perform numerical experiments related to the main results of Sect. 3 and discussion based on these results. Section 5 again summarizes this study and its results, and mentions future works. The proof of the analyses are performed in Sects. 6 and 7. Section 8 contains numerical experiments on facts not directly related to the analytical results of this study. Section 9 summarizes the perturbation theory of matrices necessary for the analysis. 

123 

Feature learning and generalization error analysis of… 

## **2 Problem setup and training procedure** 

The goal of this study is to construct an estimator based on training data and theoretically evaluate the predictive error of this estimator. In Sect. 2.1, we describe the problem setting and assumptions on the underlying distribution in this study, which is consistent with Tsigler and Bartlett [19]. In Sect. 2.2, we explain the two-layer linear network we consider in this study and introduce the feature learning procedure. 

## **2.1 Setting of input and output data** 

1. Suppose that we observe an i.i.d. sequence of input _(_ _**x** i )i[n]_ =1[∈][R] _[d]_[whose mean is] zero and covariance matrix is _�_ . Without loss of generality, _�_ can be transformed into a diagonal matrix with eigenvalues arranged in descending order by an appropriate change of basis, and then we assume that _�_ = diag _(λ_ 1 _, λ_ 2 _, . . . , λd )_ with _λ_ 1 ≥ _λ_ 2 ≥· · · ≥ _λd_ . In addition, we assume that the random variable _�_[−] 2[1] _**x** i_ (if _λk_ , diag) follows a sub-Gaussian distribution with sub-Gaussian norm _σx_ .[1] 

2. The output data _(yi )i[n]_ =1[∈][R][ are assumed to be observed as the value of a linear] function _f_[∗] _(_ _**x** i )_ = _**x** i_[⊤] _**[a]**_[∗][with additive observation noise:] 

**==> picture [132 x 13] intentionally omitted <==**

Here, _(ϵi )i[n]_ =1[follow][a][Gaussian][distribution][with][mean][0][and][variance] _[σ] ϵ_[ 2][inde-] i _._ i _._ d _._ pendently: _ϵi_ ∼ _N (_ 0 _, σϵ_[2] _[)]_[. Furthermore, we assume][ ∥] _**[a]**_[∗][∥][2] _�_[=][1 without loss of] generality. 

ˆ In this study, we construct an estimator of a linear model _f_[ˆ] _(_ _**x** )_ = _**x**_[⊤] _**a**_ from the training data _(_ _**x** i , yi )i[n]_ =1[that satisfy the above conditions and evaluate the predictive] error measured by the _L_[2] -norm: E _**x**_ [ _( f_[∗] _(_ _**x** )_ − _f_[ˆ] _(_ _**x** ))_[2] ] where the expectation of _x_ is taken over the unseen test data which is independent of the training data. Here, note that the predictive error can be expressed as follows: 

**==> picture [285 x 63] intentionally omitted <==**

> 1 A random variable _X_ is sub-gaussian if it has a finite sub-gaussian norm ∥ _X_ ∥ _ψ_ 2 := inf { _t >_ 0|E[exp _(X_[2] _/t_[2] _)_ ] ≤ 2}. 

123 

N. Hayato, S. Taiji 

## **2.2 Training procedure** 

In this study, we consider a fully-connected two-layer linear neural network with _N_ neurons. The input and output of the network are represented as follows: 

**==> picture [161 x 13] intentionally omitted <==**

Next, we describe how to train the parameters _W ,_ _**a**_ of this model. 

1. First, we randomly initialized the parameters _W_ = _W_ 0 and _**a**_ = _**a**_ 0 as i.i.d. realization of Gaussian random variables: √ _N Wi j_ ∼ _N (_ 0 _,_ 1 _),_ ~~√~~ _N a j_ ∼ _N (_ 0 _,_ 1 _) (i_ ∈ [ _d_ ] _, j_ ∈[ _N_ ] _)_ . 

2. Second, the first-layer parameter _W_ 0 is updated by one-step gradient descent to _n_ 

reduce the training error _L_ = _n_[1] � _i_ =1 _[(][y][i]_[−] _[f][ (]_ _**[x]**[i][))]_[2][. More precisely, it is updated] as 

**==> picture [115 x 13] intentionally omitted <==**

Here, _P(λ[(]_[1] _[)] )_ is a _d_ × _d_ matrix that depends on the regularization parameter _λ[(]_[1] _[)]_ ≥ 0, and _η_ ≥ 0 represents the step size. 

3. Third, _**a**_ 0 isupdatedbyperformingtheridgeregressionwithindependentrealization of the training data _(_ _**x**_ ˜ _i , y_ ˜ _i )i[n]_ =1[which have the same distribution as those used to] train the first layer: 

**==> picture [214 x 31] intentionally omitted <==**

Here, we give some remark on the training procedure described above. In the follow˜ ˜ ing, we write _X_ := _(_ _**x**_ 1 _, . . . ,_ _**x** n)_[⊤] _, X_[˜] := _(_ _**x**_ 1 _, . . . ,_ ˜ _**x** n)_[⊤] _,_ _**y**_ = _(y_ 1 _, . . . , yn)_[⊤] _,_ _**y**_ = _(_ ˜ _y_ 1 _, . . . , y_ ˜ _n)_[⊤] . We first note that the matrix ∇ _W_ 0 _L_ of the update equation of the first-layer is represented as 

**==> picture [255 x 25] intentionally omitted <==**

This shows that the update from _W_ 0 to _W_ 1 is given by a rank-1 matrix. Therefore, we may write 

where _a_ ˜ is given by 

**==> picture [250 x 75] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

In this study, we primarily analyze the situation where the number of neurons _N_ is infinitely large while keeping _d, n_ finite. In this case, we can see that _**a**_ ˜ _a_ → _.s. P(λ[(]_[1] _[)] ) n_[1] _[X]_[⊤] _**[y]**[ (][N]_[→∞] _[)]_[ because the second term of (][4][) converges to a zero matrix.] Next, in this study, we analyze three choices of the matrix of _P(λ[(]_[1] _[)] )_ : 

**==> picture [323 x 27] intentionally omitted <==**

Here, _�_ is not necessarily a non-singular matrix and _X_[⊤] _X_ is not a non-singular matrix because _X_ ∈ R _[n]_[×] _[d]_ and _n < d_ . In this case, if _λ[(]_[1] _[)]_ = 0, _(�_ + _λ[(]_[1] _[)] Id )_[−][1] and � _n_ 1 _[(][X]_[⊤] _[X]_[+] _[ λ][(]_[1] _[)][I][d][)]_ �−1 don’t exist. However, even in this case, lim _λ(_ 1 _)_ →0 _Pi (λ[(]_[1] _[)] ) n_[1] _[X]_[⊤][�] _**y**_ − ~~√~~ 1 _N[XW]_[0] _**[a]**_ � _(i_ = 2 _,_ 3 _)_ exists. So, we define _Pi (_ 0 _)_ := lim _λ(_ 1 _)_ →0 _Pi (λ[(]_[1] _[)] ) (i_ = 2 _,_ 3 _)_ for convenience. 

The following is an interpretation of each _P(λ[(]_[1] _[)] )_ 

1. When _P_ = _P_ 1, the update of _W_ corresponds to just the vanilla gradient descent. 

2. When we use _P_ = _P_ 2, then the update of _W_ 0 can be seen as the mixture of the natural gradient descent (NGD) and the gradient descent (GD). Indeed, if _λ[(]_[1] _[)]_ = 0, it is exactly NGD, and as _λ[(]_[1] _[)]_ goes to ∞, it approaches to GD. In that sense, _λ[(]_[1] _[)]_ is a parameter that controls the mixture proportion of NGD and GD. The difference of NGD and GD is crucial especially when we consider the one-step update. Indeed, by noticing that E _X ,ϵ_ [ _n_[1] _[X]_[⊤] _[X]_ _**[ y]**_[]][=] _[�]_ _**[a]**_[∗][since][ E] _[ϵ]_[[] _**[y]**_[]][=] _[X]_ _**[a]**_[∗][, the] update direction of NGD _(λ[(]_[1] _[)]_ = 0 _)_ is exactly same as the true signal _**a**_[∗] , which means that the NGD can efficiently capture the true signal in average. On the other hand, the inverse of the small eigenvalue of _�_ is large, so the noise component in _n_[1] _[X]_[⊤] _[X]_ _**[ y]**_[is amplified by] _[ �]_[−][1][. Therefore] _[ λ][(]_[1] _[)]_[can be seen as a regularizer that] uniformly terminates small eigenvalue components of _�_ at the value of _λ[(]_[1] _[)]_ and suppresses the amplification of noise. 

3. Third, since 

**==> picture [308 x 43] intentionally omitted <==**

we can see that the direction of the update is a ridge regression where _P(λ[(]_[1] _[)] )_ = _P_ 3 _(λ[(]_[1] _[)] )_ . The derivation of (5) is described in Sect. 6. 

Next, we discuss the optimization of the second layer. This is a one-layer linear ridge regression on the data _XW_ 1 passing through the first-layer. However, as we have already seen, _W_ 1 and _X_ are not independent. In our analysis, we then optimize the second layer _**a**_ 1 based on the same size data _X_[˜] sampled again independently of _X_ and suppress the stochastic behavior of _X_ and _X_[˜] in two parts. This is an approximate setup for the analysis, but the qualitative behavior is consistent with that of actual models that are learned with unsplit data (Fig. 11). In a situation where data are split, as in (5), _**a**_ 1 can be written explicitly with _W_ 1 and _X_[˜] : 

123 

N. Hayato, S. Taiji 

**==> picture [440 x 290] intentionally omitted <==**

**Fig. 1** The relationship between _k_[∗] and the bias 

**==> picture [169 x 13] intentionally omitted <==**

Therefore, the estimator of the two-layer linear model in this study is given by ˆ _**a**_ = _W_ 1 _**a**_ 1 = _W_ 1 _W_ 1[⊤] _[X]_[˜][⊤] _[(]_[ ˜] _[XW]_[1] _[W]_[ ⊤] 1 _[X]_[˜][⊤][+] _[λ][(]_[2] _[)][I][n][)]_[−][1][ ˜] _**[y]**_[. This estimator][ ˆ] _**[a]**_[ can be regarded] as a kind of preconditioned estimators analyzed in Amari et al. [1]. In general, preconditioned estimators is given by 

**==> picture [207 x 12] intentionally omitted <==**

ˆ with a matrix _P_ . Therefore _**a**_ is a variant of a preconditioned estimator where _P_ = _a.s. W_ 1 _W_ 1[⊤][in][(][6][).][In][particular,][since] _[W]_[0] _[W]_[ ⊤] 0 → _Id (N /d_ →∞ _)_ , the random feature model is consistent with a one-layer linear regression model when _N_ is sufficiently large(Fig. 9).Aswehavementionedabove,weconsiderasettingwhere _N_ istakentobe ∞ so that _W_ 0 _W_ 0[⊤][=] _[I][d]_[because our goal is to compare the respective predictive errors] of the estimator obtained by the one-step feature learning model and one obtained by the one-layer linear regression model. 

123 

Feature learning and generalization error analysis of… 

**==> picture [440 x 139] intentionally omitted <==**

**Fig. 2** The relationship between _d_ and the bias 

## **3 Main results** 

In this section, we first give the Bias-Variance decomposition of the predictive error, and then derive upper-bounds on the Bias and Variance for the general step size. We next explicitly compare the predictive errors between a feature learning method and a non-feature learning method in two different regimes of the step size: small step size setting and large step size setting. 

The predictive error given in (1) is decomposed into Bias and Variance as 

**==> picture [303 x 59] intentionally omitted <==**

The following theorem enables us to reduce evaluation of the Bias and Variance of the two layer neural network to that of the vanilla (one-layer) ridge regression. 

> 1 ˜ **Theorem 1** _V_ ˜[⊤] _W_ 1[⊤] _[�][W]_[1] _Denote the right singular vectors of[V]_[˜] _[is a diagonal matrix such that][ �]_[=] _�[ diag]_ 2 _W_ 1 _[(][λ]_[˜] _by_[1] _[, . . . ,] V_ ∈[ ˜] _[λ]_ R _[N][N][)]_[×] _[ with][N] . Here,[λ]_[˜][1][≥˜] _�[λ]_[2] :=[≥] · · · ≥ _λ_[˜] _N . Then, it holds that_ 

**==> picture [323 x 46] intentionally omitted <==**

_Here, let W_ 1 _[⋆][be any matrix satisfying W]_[1] _[W][ ⋆]_ 1[=] _[I][d][. Since W]_[1] _[ is row full rank, we can] easily check that W_ 1 _[⋆][exists. Indeed, W]_[ †] 1 _[satisfies W]_[1] _[W]_[ †] 1[=] _[I][d][.]_ 

_**Remark 1**_ Since _W_ 1 ∈ R _[d]_[×] _[N]_ and _N > d_ , _λ_[˜] _d_ +1 = · · · = _λ_[˜] _N_ = 0. 

123 

N. Hayato, S. Taiji 

Once the first layer’s parameter is fixed, the predictive error of the two-layer network can be evaluated through the usual analysis on the one-layer network. The following theorem gives upper bounds of the Bias and Variance of the two-layer network through the analysis on the usual ridge regression in the interpolation regime [19]. With this theorem, we can evaluate the effect of feature learning on the predictive error. From E[ _V_[˜][⊤] _W_ 1[⊤] _**[xx]**_[⊤] _[W]_[1] _[V]_[˜][ ] =] _[V]_[˜][ ⊤] _[W]_[ ⊤] 1 _[�][W]_[1] _[V]_[˜][ ,theproofisobtainedimmediatelybyapplying] Theorem 1 of Tsigler and Bartlett [19] to Theorem 1. 

**Theorem 2** _Suppose λ[(]_[2] _[)]_ ≥ 0 _. There exist constants cx and Cx depending only on σx such that, for any δ <_ 1 − 4 _e_[−] _[n][/][c]_[2] _x , (1) the condition number of XW_ 1 _Vk_ :∞ _Vk_[⊤] :∞ _[W]_[ ⊤] 1 _[X]_[⊤][+] _[ λ][(]_[2] _[)][I][N][is][at][most][L][with][probability]_[1][ −] _[δ][where][L][is][a] constant such that_ 

**==> picture [98 x 28] intentionally omitted <==**

_and (2) for any k_ ≤ _n/cx , t_ ∈ _(_ 1 _, n/cx ) , we have_ 

**==> picture [316 x 65] intentionally omitted <==**

_with probability_ 1 − _δ_ − 20 _e_[−] _[t][/][c][x] ._ 

Here, from the note on the random feature model in Sect. 2, the evaluation of the Bias and Variance with _η_ = 0 follows that of a one-layer ridge regression, namely, the following corollary holds. 

**Corollary 1** _Letting η_ = 0 _under the same conditions as in Theorem_ 2 _, there exists N_ 0 ∈ Z _such that, for any N_ ≥ _N_ 0 _, the following inequalities hold:_ 

**==> picture [268 x 64] intentionally omitted <==**

_**Remark 2** B_[¯] 0 and _V_[¯] 0 given in Corollary 1 match the evaluation of Bias and Variance in Theorem 1 of Tsigler and Bartlett [19]. 

We then present some additional lemmas on Theorem 2. 

**Lemma 1** _The second term of B_[¯] 1 _is represented as follows:_ 

**==> picture [167 x 20] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

1 _where, U_[˜] ∈ R _[d]_[×] _[d] are the left singular vectors of �_ 2 _W_ 1 _._ 

_**Remark 3**_ The value of _B_[¯] 1 does not depend on the choice of _W_ 1[∗][.] 

## **3.1 Error analysis of sufficiently small step feature learning** 

In this subsection, we give a first-order perturbation of the predictive error by considering a small step size regime: _η_ 1. We first note that the step size need to be appropriately reduced as _N_ increases to performe perturbation analysis. 

Now, for given _**a**_ ˜ , _W_ 1 _W_ 1[⊤][=] _[I][d]_[+] _[ η]_[2][ ˜] _**[a][a]**_[˜][⊤][+] _[ η(][W]_[0] _**[a][a]**_[˜][⊤][+] _**[a]**_[˜] _[(][W]_[0] _**[a]**[)]_[⊤] _[)]_[ +] _[ (][W]_[0] _[W]_[ ⊤] 0[−] _Id )_ holds from (3). As _W_ 0 _W_ 0[⊤] = _Id_ + _O_ P _(_[√] _d/N )_ and ∥ _W_ 0 _**a**_ ∥= _O_ P _(_[√] _d/N )_ , when _η_ = _N[γ] (γ_ ∈ _(_ −1 _/_ 2 _,_ 0 _))_ and _N_ is sufficiently large, _W_ 1 _W_ 1[⊤][is represented as] 1 _W_ 1 _W_ 1[⊤][=] _[I][d]_[+] _[ η]_[2][ ˜] _**[a][a]**_[˜][⊤][+] _[ o]_[P] _[(η]_[2] _[)]_[. The singular values and singular vectors of] _[ �]_ 2 _W_ 1 can be evaluated from the expansion. Under this assumption, we give the predictive error after feature learning below. Let _η_[2] = _ε_ . 

**Theorem 3** _Let B_[¯] 1 _and V_[¯] 1 _be those given in Theorem_ 2 _, and let k and λ[(]_[2] _[)] satisfy the same assumptions as in Theorem_ 2 _. Furthermore, let W_ 1 _W_ 1[⊤][=] _[I][d]_[ +] _[ε]_ _**[a]**_[˜] _**[a]**_[˜][⊤][+] _[o]_[P] _[(ε)][ and] assume that the eigenvalues of � are not degenerate. Then, B_[¯] 1 _and V_[¯] 1 _are represented as follows:_ 

**==> picture [336 x 329] intentionally omitted <==**

N. Hayato, S. Taiji 

_Here,_ _**a** i_[2][:=] _[ (]_ _**[a]**[i][)]_[2] _[for any vector]_ _**[ a]**[.]_ 

Let each term in the right hand side of the bias _B_[¯] 1 in Theorem 3 be _b_ 1 to _b_ 6 respectively, that is, 

**==> picture [336 x 141] intentionally omitted <==**

Each term has the following meaning. First, _b_ 1 and _b_ 5 are the same terms as _B_[¯] 0. Then, _b_ 2 and _b_ 3 are the terms that mainly increase or decrease _B_[¯] 1 from _B_[¯] 0 because _b_ 4 and _b_ 6 are zeros in the setting of sparse signal. Next, we give a corollary below to analyze the effect of _b_ 4 and _b_ 6 in detail. 

˜ **Corollary 2** _Let k satisfy the same assumptions as in Theorem_ 2 _and let_ _**a**_ = _P_[−][1] _X_[⊤] _**y** /n with a diagonal matrix P_ = _diag( p_ 1 _, . . . , pd ). Then, the following equations hold:_ 

**==> picture [331 x 70] intentionally omitted <==**

_Remember that P_ = _� and P_ = _Id correspond to the NGD and GD update respectively._ 

From Corollary 2, we have the following observations. First, _b_ 4 represents the interaction among the first _k_ components of _**a**_[∗] . In the summand, the terms with smaller _λi_ − _λ j_ have greater impact on the whole bias because _λi_ − _λ j_ appears in the denominator in each term. Since the first term is always negative, it makes _B_[¯] 1 smaller on average, while the second term makes _B_[¯] 1 larger on average. _b_ 6 represents the interaction between the first _k_ components of _**a**_[∗] and the rest components of _**a**_[∗] . Because E _X ,ϵ_ [ _b_ 6] is always positive, _b_ 6 makes _B_[¯] 1 larger on average. However, its effect is relatively small because _λi_ − _λ j_ in the denominator tends to be large as they are from different components; i.e., _i_ is from the first _k_ components and _j_ is from the rest. 

123 

Feature learning and generalization error analysis of… 

_**Sparse signal**_ In practice, signals are often sparse under high dimensional inputs, namely, most components of the _**a**_[∗] are zero. Then, in the following, we derive a more detailed evaluation of Theorem 3 where _**a**_[∗] is completely sparse, that is, _**a**_[∗] _k_[∗][=] 1 _/_[√] _λk_[∗] _,_ _**a** i_[∗][=][0] _[ (]_[∀] _[i]_[̸=] _[k]_[∗] _[)]_[ for] _[ k]_[∗][∈[] _[d]_[]][. In this case, since] _[ b]_[4][=] _[b]_[6][=][0, we obtain] the following corollaries where each term in the bias is due to _b_ 2 and _b_ 3. 

**Corollary 3** _Let B_[¯] 1 _and V_[¯] 1 _be given in Theorem_ 3 _and let k and λ[(]_[2] _[)] satisfy the same assumptions in Theorem_ 2 _. If_ _**a** i_[∗][=] _[ λ] i_[−][1] _[/]_[2] _(i_ = _k_[∗] _),_ _**a** i_[∗][=][ 0] _[ (][i]_[̸=] _[ k]_[∗] _[)][, for k]_[∗][≤] _[k][and]_ ˜ _**a**_ = _(�_ + _λ[(]_[1] _[)] Id )_[−][1] _X_[⊤] _**y** /n, the following equations hold:_ 

**==> picture [295 x 120] intentionally omitted <==**

_In particular, if λ[(]_[1] _[)]_ = 0 _, we have following evaluations:_ 

**==> picture [333 x 69] intentionally omitted <==**

Corollary 3 shows how NGD affects the bias through feature learning. On the other hand, the following corollary gives the effect of GD. 

**Corollary 4** _Let B_[¯] 1 _and V_[¯] 1 _be given in Theorem_ 3 _and let k, and λ[(]_[2] _[)] satisfy the same assumptions in Theorem_ 2 _. If_ _**a** i_[∗][=] _[ λ] i_[−][1] _[/]_[2] _(i_ = _k_[∗] _),_ _**a** i_[∗][=][ 0] _[ (][i]_[̸=] _[ k]_[∗] _[)][, for k]_[∗][≤] _[k][and]_ ˜ _**a**_ = _X_[⊤] _**y** /n, the following equations hold:_ 

**==> picture [340 x 77] intentionally omitted <==**

In the following, we discuss in more detail the effect of feature learning with NGD and with GD. 

123 

N. Hayato, S. Taiji 

˜ ˜ For _**a**_ = _�_[−][1] _X_[⊤] _**y** /n_ , while _**a**_ is an unbiased estimator of _**a**_[∗] (E _X ,_ _**ϵ**_ [˜ _**a**_ ] = _**a**_[∗] ), its variance is far away from zero. Indeed, E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] _�_[]][is][approximately] _[d][(]_[1][+] _n[σ] ϵ_[ 2] _[)]_ from (11). Therefore, in the case where _d_ is larger than _n_ , the estimation accuracy of the first-layer is quite poor. However, Corollary 3 suggests that feature learning can improve predictive error even in such a case. In fact, the following corollary holds for the situation where the bias is reduced. 

**Corollary 5** _Let k, and λ[(]_[2] _[)] satisfy the same assumptions in Theorem_ 2 _and let λi_ = _i_[−] _[(]_[1][+] _[α)] (_ −1 _< α, α_ ̸= 0 _). Then, the following holds:_ 

**==> picture [294 x 28] intentionally omitted <==**

_Especially, letting k_ = _o(d), λ[(]_[2] _[)]_ = 0 _, and_ −1 _< α <_ 0 _, we have that_ 

**==> picture [234 x 26] intentionally omitted <==**

_Hence, if k_[∗][1][+] _[α] >_[|] _[α]_[|] _[(]_[1] _n_[+] _[σ] ϵ_[ 2] _[)] d_[1][+] _[α] , then it holds that_ 

**==> picture [139 x 27] intentionally omitted <==**

_and moreover B_[¯] 1 _< B_[¯] 0 _holds._ 

Corollary 5 tells that the threshold of _k_[∗] yielding better generalization by feature learning is _k_[∗][1][+] _[α]_ =[|] _[α]_[|] _[(]_[1] _n_[+] _[σ] ϵ_[ 2] _[)] d_[1][+] _[α]_ if _α <_ 0. Especially if _d_ = _o(n_ 1+1 _α )_ , the improvement of the bias is _k_[∗][1][+] _[α]_ . On the other hand, if _d_ is larger than _n_ and the eigenvalue decay rate is fast, feature learning worsens bias though one-layer linear regression may generalize even in the case where _d_ = ∞ and _n <_ ∞ from Bartlett et al. [4]. In this regime, it is shown that ridge regression exhibits good predictive performance. For _**a**_ ˜ = _X_[⊤] _**y** /n_ , decrease in the bias _λk_[∗] −[1][+] _n[σ] ϵ_[ 2] _λ[(]_[2] � _[)]_ + _i_ ~~[�]~~ _>ki>[λ] i_[2] _k[λ][i][<][λ][k]_[∗][=] _[k]_[∗−] _[(]_[1][+] _[α)]_ in the same case as Corollary 5. Therefore, as _k_[∗] →∞, the improvement of bias converges to zero. 

Therefore, when _k_[∗] is large and exeeds the threshold and the eigenvalue decay rate is slow, feature learning with NGD improves the bias while feature learning with GD does not, and then NGD is superior to GD. 

## **3.2 Error analysis of sufficiently large step feature learning** 

In this subsection, we give an evaluation of the predictive error when the step size _η_ is sufficiently large. 

Ba et al. [3] shows that, when _η_ = _O(N )_ , one-step gradient feature learning can outperform the kernel method as _n, d, N_ →∞. It is also reported that, if _η_ = _O(_ 1 _)_ , 

123 

Feature learning and generalization error analysis of… 

feature learning does not improve the predictive error, and _η_ = _ω(_ ~~√~~ _N )_ is still not enough. 

In this study, we analyze the predictive error in the case where _N_ is sufficiently large while _n_ and _d_ are finite. Here, we assume that the step size _η_ is within the range of _N[γ] (γ_ ∈ _(_ 0 _,_ 2[1] _[))]_[ for the following reasons. As we have seen in Sect.][3.1][,] _[ W]_[1] _[W]_[ ⊤] 1[=] _Id_ + _η_[2] _**a**_ ˜ _**a**_ ˜[⊤] + _η(W_ 0 _**aa**_ ˜[⊤] + _**a**_ ˜ _(W_ 0 _**a** )_[⊤] _)_ and _η(W_ 0 _**aa**_ ˜[⊤] + _**a**_ ˜ _(W_ 0 _**a** )_[⊤] _)_ = _O_ P _(η_ ~~�~~ _Nd[)]_[.] Therefore, when _η_ = _N[γ] (γ_ ∈ _(_ 0 _,_ 2[1] _[))]_[,] _[W]_[1] _[W]_[ ⊤] 1[=] _[I][d]_[+] _[ η]_[2][ ˜] _**[a][a]**_[˜][⊤][+] _[ O]_[P] _[(]_ ~~√~~ _dη_[1][−][1] _[/]_[2] _[γ] )_ . Then, for large _η_ , _W_ 1 _W_ 1[⊤][=] _[I][d]_[+] _[ η]_[2][ ˜] _**[a][a]**_[˜][⊤][+] _[ o]_[P] _[(]_[1] _[)]_[ and following theorem holds.] 1 1 We let _U_[˜] = lim _η_ →∞ _U_[˜] _(η)_ where _U_[˜] _(η)_ is the eigenvectors of _�_ 2 _W_ 1 _W_ 1[⊤] _[�]_ 2 = _�_ + _η_[2] _�_ 21 _**a**_ ˜ _**a**_ ˜[⊤] _�_ 21 . Now we can easily check that the limit exists and _U_ ˜ is an orthogonal matrix. Here, note that the first eigenvector of _U_[˜] is _�_ 21 _**a**_ ˜ and the others are vectors orthogonal to _�_ 21 _**a**_ ˜ . **Theorem 4** _Let B_[¯] 1 _and V_[¯] 1 _be given in Theorem_ 2 _and let k and λ[(]_[2] _[)] satisfy the_ ˜ ˜ _same assumption as Theorem_ 2 _. Then, letting_ _**b**_ = _**a**_ − _(_ _**a**_[⊤] _�_ _**a**_[∗] _)_ _**a**_[∗] _and if W_ 1 _W_ 1[⊤][=] _Id_ + _η_[2] _**a**_ ˜ _**a**_ ˜[⊤] + _o_ P _(_ 1 _), the following holds._ 

**==> picture [336 x 32] intentionally omitted <==**

_As for the variance, since_[�] _i>k[λ][i]_[≤][�] _i>k[λ]_[˜] _[i]_[≤][�] _i>k[λ][i]_[+] _[ λ]_[1] _[in]_[(][13][)] _[,][it holds] that_ 

**==> picture [165 x 28] intentionally omitted <==**

_from Theorem_ 2 _. It is expected that_[�] _i>k[λ]_[˜] _i_[2] _[also approximately equals to]_[ �] _i>k[λ] i_[2] _[.]_ 

In Theorem 4, if ˜ _**a**_ approximates _**a**_[∗] , ˜ _**a**_[⊤] _�_ _**a**_[∗] approximately equals to 1. Then, ∥ _**b**_ ∥[2] _�_ matches ∥ _**a**_[∗] −˜ _**a**_ ∥[2] _�_[. Therefore, Theorem][ 4][ can be regarded as a formula evaluating the] approximation error of the first-layer estimator _**a**_ ˜ with _**a**_[∗] by dividing it by _U_[˜] into the first _k_ components and the rest of them. However it is difficult to explicitly characterize the distribution of _U_[˜] . Hence, we consider two concrete situations in the following so that we explicitly evaluate Theorem 4. 

(1) The first one is the case where the distribution of _U_[˜] is the worst. Since _U_[˜] is an orthogonal matrix, it holds that ��� _U_ ˜ ⊤1: _k[�]_ 21 _**a**_ ˜[⊤] _�_ _**b a**_[∗] ���2 _�_ 1[−] : _k_[2] ≤ _[λ]_ _**a**_ ˜ _k_[−][⊤][2] _�_[∥] _**[b] a**_[∥][∗] _�_[2][.][Here,][even][in] the worst case setting, that is, ��� _U_ ˜ ⊤1: _k[�]_ 21 _**a**_ ˜[⊤] _�_ _**b a**_[∗] ���2 _�_ 1[−] : _k_[2] = _[λ]_ _**a**_ ˜ _k_[−][⊤][2] _�_[∥] _**[b] a**_[∥][∗] _�_[2][, following evaluation] holds. 

**Corollary 6** _Let B be given in_ (7) _. There exists a large constant cx that only depends on σx such that_ 

123 

N. Hayato, S. Taiji 

_1. If there exists a constant Cx that only depends on σx and nλk_ +1 ≥ _Cx_ � _i>k[λ][i] holds for some k < n/cx , then by letting λ[(]_[2] _[)]_ = _nλ_[˜] _k_ +1 _in Theorem 4, we have that for any t_ ∈ _(cx , n/cx )_ 

**==> picture [68 x 26] intentionally omitted <==**

_with probability at least_ 1 − 26 _e_[−] _[t][/][c][x] . Here, Dx is a constant that only depends on σx ._ 

_2. If_[�] _i>k[λ][i]_ ≥ _cx nλk_ +1 _holds for some k < n/cx , then by letting λ[(]_[2] _[)]_ = −[�] _i>k[λ][i]_[+] _[ ξ]_ � _nλ_ 1 + ~~�~~ _n_ ~~[�]~~ _i>k[λ] i_[2] � _for some constant ξ > cx , we have that for any t_ ∈ _(cx , n/cx )_ 

**==> picture [140 x 31] intentionally omitted <==**

_with probability at least_ 1 − 20 _e_[−] _[t][/][c][x] . Especially, if λi_ = _i_[−] _[(]_[1][+] _[α)] (_ −0 _._ 5 _< α_ ≤ 0 _), we have B_ ≤ _Dx_ _**a**_ ˜∥[⊤] _**b** �_ ∥[2] _�_ _**a**_[∗] _[.]_ 

Corollary 6 shows that _B_[¯] 1 is bounded by a constant multiple of the estimation error in the first layer even in the case where ��� _U_ ˜ ⊤1: _k[�]_ 21 _**a**_ ˜[⊤] _�_ _**b a**_[∗] ���2 _�_ 1[−] : _k_[2] = _[λ]_ _**a**_ ˜ _k_[−][⊤][2] _�_[∥] _**[b] a**_[∥][∗] _�_[2][. Especially,] for the learning model with _P_ 3 _(λ_ 1 _)_ = � _n_ 1 _[(][X]_[⊤] _[X]_[+] _[ λ][(]_[1] _[)][I][d][)]_ �−1 in the first-layer update, the predictive error for the entire second layer is at most a constant multiple of the one-layer ridge regression model. Here, ��� _U_ ˜ ⊤1: _k[�]_ 21 _**a**_ ˜[⊤] _�_ _**b a**_[∗] ���2 _�_ 1[−] : _k_[2] = _[λ]_ _**a**_ ˜ _k_[−][⊤][2] _�_[∥] _**[b] a**_[∥][∗] _�_[2][holds when] ˜ 1 ˜ 1 _U_ 1[⊤] : _k[�]_ 2 _**b**_ ∝ _**e** k_ . However, since _U_ is left singular vectors of the matrix which is _�_ 2 _W_ 0 addedarank-1matrixandleftsingularvectorsof _�_ 21 _W_ 0 are _Id_ , ��� _U_ ˜ ⊤1: _k[�]_ 21 _**a**_ ˜[⊤] _�_ _**b a**_[∗] ���2 _�_ 1[−] : _k_[2] = 

_λ_[−] _k_[2][∥] _**[b]**_[∥] _�_[2] _**a**_ ˜[⊤] _�_ _**a**_[∗][does not hold and feature learning decreases the bias experimentally (Fig.][ 6][).] (2) The second one is the case where the true signal is sparse and the estimation error of the first-layer is sufficiently small. 

**Corollary 7** _Let k satisfy the same assumption as Theorem_ 2 _and U be given in Theorem_[˜] 4 _._ { _**e**_ 1 _, . . . ,_ _**e** d_ } _denotes the standard basis of_ R _[d] and we assume that the eigenvalues of � are not degenerate. In Theorem_ 4 _, if_ _**a**_[∗] = _λ_ − _k_[∗] 2[1] _**[e]**[k]_[∗] _[(][k]_[∗][≤] _[k][)][ and]_ _**a**_ ˜∥[⊤] _**b** �_ ∥[2] _�_ _**a**_[∗] _[is sufficiently]_ ˜ _small, we have that for U_[˜] 1:∞ = _(_ _**u**_ 2 _, . . . ,_ ˜ _**u** d )_ 

**==> picture [175 x 64] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

**==> picture [440 x 139] intentionally omitted <==**

**Fig. 3** The relationship between _σϵ_[2] and the bias 

_In this case, it holds that_ 

**==> picture [331 x 33] intentionally omitted <==**

## **4 Numerical experiments** 

In this section, we present numerical experiments and discuss the validity of our theoretical results we provided in Sect. 3. 

## **4.1 Experimental setting** 

In this subsection, we describe the overall experimental settings in Sect. 4. We assume that _�_ = diag _(λ_ 1 _, . . . , λd )_ satisfies _λi_ = _i_[−] _[(]_[1][+] _[α)] (α >_ −1 _)_ (recall that _�_ is the covariance matrix of input data _**x**_ ). Namely, we suppose that the distribution of eigenvalues polynomially decay and _α_ determines the decay rate. Here, note that _d d_ lim _d_ →∞ � _i_ =1 _[λ][i][<]_[ ∞][when] _[ α][>]_[ 0, and lim] _[d]_[→∞] � _i_ =1 _[λ][i]_[= ∞][when][ −][1] _[ < α]_[≤][0.] Furthermore, we asuume that input data _**x**_ and noise independently follow Gaussian i.i.d. i.i.d. distributions: _**x**_ ∼ _N (_ 0 _, �), ϵ_ ∼ _N (_ 0 _, σϵ_[2] _[)]_[.] 

In Sect. 3, for ease of analysis, we constructed the theory in a setting where the data were split into sampled data _(X ,_ _**y** )_ and resampled data _(X_[˜] _,_ ˜ _**y** )_ . In this section, however, experiments are conducted in a setting where the data are not split, which is closer to the real setting. To be more precisely, we compute _W_ 1 from data _(X ,_ _**y** )_ according to (2) and then compute _**a**_ ˆ FL _,_ _**a**_ ˆ RF _,_ and _**a**_ ˆ LR from the same data in the following way: 

**==> picture [188 x 44] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

Here, _**a**_ ˆ FL _,_ _**a**_ ˆ RF and _**a**_ ˆ LR represent the ridge estimators corresponding to the one-step feature learning method, the random feature model and the vanilla linear regression. In Sect. 8, we present some comparisons of the experimental results with and without splitting. The qualitative behavior of the results is largely the same, throughout the experiment, regardless of the splitting setting. 

We approximate the bias and variance of the predictive error given by these estimators with numerical calculation. The way how to calculate them is as follows. For ES ∈{FL _,_ RF _,_ LR}, we calculate _B_[ˆ] ES and _V_[ˆ] ES _M_ times over _M_ independent realizations of the training data. For the _i_ -th realization of _Xi_ and _**ϵ** i_ of the training data, we calculate the bias _B_[ˆ] ES _[(][i][)]_[and variance] _V_[ˆ] ES _[(][i][)][(][i]_[∈[] _[M]_[]] _[)]_[ as] 

**==> picture [221 x 31] intentionally omitted <==**

where 

**==> picture [117 x 43] intentionally omitted <==**

Then, we calculate their average _M_[1] � _iM_ =1 _B_[ˆ] ES _[(][i][)]_[and] _M_[1] � _iM_ =1 _V_[ˆ] ES _[(][i][)]_[as estimates of their] true expectation E _X_ [ _B_ ES] and E _X_ [ _V_ ES] respectively. In the following, unless otherwise mentioned, each parameter is set as follows: Sample size _n_ = 100, dimension of input data _d_ = 200, number of neurons in the middle layer _N_ = 1000 _, α_ = −0 _._ 5 _, k_[∗] = 100 _, σϵ_[2][=][ 0] _[.]_[01 and] _[ λ][(]_[1] _[)]_[=] _[ λ][(]_[2] _[)]_[=][ 0] _[.]_ 

## **4.2 Experiments for small step size** 

Inthissubsection,weperformexperimentsforthesmallstepsizesettingcorresponding to Sect. 3.1. Although the smaller the step size the more accurate our analysis is, we employ rather large step size _η_ = 1 because the improvement of the predictive error is hidden behind the numerical errors. Here, we let _M_ = 1000. 

We observe the relationship between each parameter and the bias where _**a**_[∗] _k_[∗][=] 1 _/_[√] _λk_[∗] _,_ _**a** i_[∗][=][ 0] _[ (]_[∀] _[i]_[̸=] _[ k]_[∗] _[)]_[ for] _[ k]_[∗][∈[] _[d]_[]][. Here, we calculate] _[B]_[FL] _B_[−] LR _[B]_[LR] and _[B]_[FL] _B_[−] RF _[B]_[RF] to compare the bias given by GD and NGD feature learning methods with those given by linear regression model or random feature model. According to Corollaries 3 and 4, the change in the bias due to feature learning consists of the first term which makes the bias smaller and the second term which makes it larger. 

In Fig. 1, we see that feature learning decreases the relative bias well when _**a**_ ˜ is aligned on _**a**_[∗] well. In Figs. 2 and 3, we see that when _d_ and _σϵ_[2][is][increased,][the] variance E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] ] becomes larger and the relative bias is increased especially due to feature learning with NGD. In Fig. 4, we see that proper regularization can reduce the bias further. 

Figure 1 shows the relationship between _k_[∗] and the bias for some specific _α_ . 

123 

Feature learning and generalization error analysis of… 

**==> picture [440 x 139] intentionally omitted <==**

**Fig. 4** The relationship between _λ[(]_[1] _[)] , λ[(]_[2] _[)]_ and the bias 

**==> picture [440 x 139] intentionally omitted <==**

**Fig. 5** The relationship between _α_ and the variance 

**==> picture [440 x 139] intentionally omitted <==**

**Fig. 6** The change in each bias when _η_ is varied 

123 

N. Hayato, S. Taiji 

**Fig. 7** _α_ = −0 _._ 5 

**==> picture [216 x 157] intentionally omitted <==**

**Fig. 8** The change in each overall Predictive Error when _η_ is varied 

**==> picture [216 x 182] intentionally omitted <==**

When _k_[∗] is small, the relative bias is increased due to feature learning with NGD. Especially, as _α_ gets larger, the relative bias gets larger except for _k_[∗] = 1 in (d). This is because, when _k_[∗] is small, the first term of Corollary 3 which reduces the bias is small and the second term which increases it is large. In contrast, the relative bias is reduced due to feature learning with GD where _k_[∗] is small. Especially, the reduction is large when _α_ is large. This is because, when _k_[∗] is small, _**a**_ **[∗]** is aligned on input and _**a**_ ˜ in (4) with GD estimates the signal well while _**a**_ ˜ with NGD does not due to the large variance E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] ]. Here, the comparisons with linear regression model behave differently from that with random feature model where feature learning is GD. This is simply because the difference between _**a**_ ˆ RF and _**a**_ ˆ LR is huge for finite _N /d_ where _α_ is large or _k_[∗] is small (Fig. 10). 

We next see that the relative bias for NGD feature learning decreases as _k_[∗] is increased because the decrease depending on _k_[∗] is _λ_ 1 _k_ ∗[=] _[k]_[∗] _[(]_[1][+] _[α)]_[.][Moreover,][the] rate of decreasing with increasing _k_[∗] is fast when _α_ is large. In general, regression 

123 

Feature learning and generalization error analysis of… 

is difficult when _k_[∗] is large because the principle component of _**x**_ is different from the direction of _**a**_[∗] . This means one step feature learning with NGD is beneficial for difficult instances. On the contrary, as _k_[∗] gets larger, the decrease in the relative bias due to feature learning with GD gets small because the decrease depending on _k_[∗] is _k_[∗−] _[(]_[1][+] _[α)]_ . Furthermore, for larger _α_ , the decrease in bias approaches zero more quickly with increasing _k_[∗] . Hence, the benefit of one step feature learning with GD is approximately zero for difficult instances though that is large for easy instances. 

Figure 2 shows how the bias changes against different _d_ when _k_[∗] = 100 is fixed. In both (a) and (b), the bias with NGD increases as _d_ is increased. This is because the second term of Corollary 3 is monotonically increases with respect to _d_ ; indeed, we 1 see that _[d]_[−] _n[k]_ ~~�~~ _i>k[λ][i]_[=] _[ O][(]_ ~~√~~ _d)_ for _α_ = −0 _._ 5. This matches the empirical observation in the graph. In contrast, the bias with GD decreases slowly because of the second � _i>k[λ] i_[2] term of Corollary 4. In fact, the term _λ[(]_[2] _[)]_ + ~~[�]~~ _i>k[λ][i]_[=] _[ O][(]_[log] _[ d][/]_ √ _d)_ for _α_ = −0 _._ 5 and it decreases slowly as _d_ gets larger. The second term of Corollaries 3 and 4 intuitively gets larger wheremeans that the bias is increased when _**a**_ ˜ consists of NGD feature learning while this gets smaller as ratio E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] _�_[]][ is large. This gets larger as] _[ d] k_[∗] _/d_ gets smaller where _**a**_ ˜ consists of GD feature learning. Figure 3 shows how the bias changes against _σϵ_[2][. Here, let] _[M]_[=][ 10000 in order to] suppress bias fluctuation when _σϵ_[2][is increased.] The relative bias with NGD feature learning is linearly increasing with respect to _σϵ_[2][.] This is because _[d]_[−] _n[k]_ ~~�~~ _i>_ 1 _k[λ][i]_[which is the coefficient of] _[ σ] ϵ_[ 2][is positive. In contrast, the] relative bias with GD feature learning is flat against increasing _σϵ_[2][.][This][is][because] _n_ 1 _λ[(]_[2] � _[)]_ + _i_ ~~[�]~~ _>ki>[λ] i_[2] _k[λ][i]_[which is also coefficient of] _[ σ] ϵ_[ 2][is almost zero.] 

Figure 4a, b show how the bias changes against positive _λ[(]_[1] _[)]_ and _λ[(]_[2] _[)]_ respectively. Here, as _λ[(]_[1] _[)]_ is increased, the step size is effectively smaller and the estimator of the feature learning model approaches that of a random feature model. Therefore, let the step size be _η(_ 1 + _λ[(]_[1] _[)] )_ to compensate for this. 

Note that _λ[(]_[1] _[)]_ = 0 corresponds to a situation where the feature learning is performed by NGD, and _λ[(]_[1] _[)]_ = ∞ corresponds to that where GD is used. In Fig. 4a, we set _k_[∗] = 60 where the relative bias with NGD and that with GD are equal, and indeed the values of the bias at _λ[(]_[1] _[)]_ = 0 and _λ[(]_[1] _[)]_ = 9 are approximately equal. We can also see that feature learning decreases the relative bias the most where _λ[(]_[1] _[)]_ = 0 _._ 2. This indicates that one step feature learning to the intermediate gradient direction between NGD and GD reduces the bias better than just NGD or GD. This can be explained as follows. When feature learning is performed with NGD, E _X ,_ _**ϵ**_ [˜ _**a**_ ] = _**a**_[∗] and the first term of Corollary 3 which decreases the bias is large while E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] ] is large and the second term of Corollary 3 which increases the bias is also large. In contrast, when feature learning is performed with GD, ∥E _X ,_ _**ϵ**_ [˜ _**a**_ ] − _**a**_[∗] ∥[2] is large and the first term of Corollary 3 which decreases the bias is small while E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] ] is small and the second term of Corollary 3 which increases the bias is also small. Therefore, by setting a value of _λ[(]_[1] _[)]_ appropriately, feature learning between NGD and GD balances ∥E _X ,_ _**ϵ**_ [˜ _**a**_ ] − _**a**_[∗] ∥[2] and E _X ,_ _**ϵ**_ [∥˜ _**a**_ − _**a**_[∗] ∥[2] ] and then reduce the bias better. 

Next, as for (b), the relative bias with NGD decreases with increasing _λ[(]_[2] _[)]_ . This is because 1[is][the][second][term][of][Corollary][3][is][decreasing][with] _λ[(]_[2] _[)]_ + ~~[�]~~ _i>k[λ][i]_[which] 

123 

N. Hayato, S. Taiji 

**==> picture [440 x 254] intentionally omitted <==**

**Fig. 9** The difference between _**a**_ ˆ RF and _**a**_ ˆ LR 

increasing _λ[(]_[2] _[)]_ . On the other hand, the gleen plot which is the relative bias with GD hardly decreases. This is because _λ[(]_[2] � _[)]_ + _i_ ~~[�]~~ _>ki>[λ] i_[2] _k[λ][i]_[which increases the bias is already small] even where _λ[(]_[2] _[)]_ = 0. Here, the reason why the blue plot decreases is simply that the bias with linear regression model is larger than that with random feature model when _λ[(]_[2] _[)]_ is small. 

We will now discuss the variance of Corollaries 3 and 4. In Fig. 5, we plot _[V]_[FL] _V_[−] LR _[V]_[LR] and _[V]_[FL][−] _[V]_[RF] for several _α_ . _V_ RF (a) shows that the variance of estimators with feature learning is almost the same as that with random features (i.e., no feature learning). Though it appears that the variance of feature learning models is worse than that of the linear regression in (b), this is simply because the variance of the random feature model is larger than that of the linear regression model. The fact that feature learning makes the variance almost no worse can be explained as follows. The variance given by linear regression is mostly determined by the decay rate of the eigenvalues of the covariance matrix E[ _**xx**[T]_ ]. Here, in feature learning models, the decay rates of the covariance matrix of the data passing through the first layer E[ _**x** W_ 1 _W_ 1[⊤] _**[x]**_[⊤][]][is][almost][the][same][as][that][of][E][[] _**[xx]**[T]_[ ]] because _W_ 1 is given by adding just a rank-1 matrix to _W_ 0 which approximately satisfies _W_ 0 _W_ 0[⊤][=] _[I]_[. Therefore, the variance is not changed much by one step feature learning.] 

123 

Feature learning and generalization error analysis of… 

**==> picture [440 x 136] intentionally omitted <==**

**Fig. 10** The relationship between _α, k_[∗] and _BRF /BL R_ 

## **4.3 Experiments for large step size** 

In this subsection, we perform experiments for the large step size setting which corresponds to our theoretical analysis in Sect. 3.2. In updating first layer, we write ˆ ˆ ˆ the feature learning model as _**a**_ FLGD, _**a**_ FLNGD and _**a**_ FLWLR corresponding to _W_ 1 = _W_ 0 + _η P_ 1 _(λ[(]_[1] _[)] )_ ∇ _W_ 0 _L_ , _W_ 1 = _W_ 0 + _η P_ 2 _(λ[(]_[1] _[)] )_ ∇ _W_ 0 _L_ and _W_ 1 = _W_ 0 + _η P_ 3 _(λ[(]_[1] _[)] )_ ∇ _W_ 0 _L_ respectively. 

Figure 6 depicts the bias _B_ ES corresponding to each _**a**_ ˆ ES for ES ∈ {FLGD _,_ FLNGD _,_ FLWLR _,_ RF _,_ LR} against the step size _η_ where _**a**_[∗] _k_[∗][=][ 1] _[/]_[√] _λk_[∗] _,_ _**a** i_[∗][=] 0 _(_ ∀ _i_ ̸= _k_[∗] _)_ . We observe that _B_ FLWLR and _B_ FLGD decrease as _η_ gets larger while _B_ FLNGD hardly changes. This can be explained as follows. When _**a**_[∗] is sparse and ∥ _**b**_ ∥[2] _�_[is tiny, from] Corollary 7, the bias of the upper _k_ components is decreased to less than the estimation error in the first layer while that of the rest of components are the same. Therefore, ˜ if the weights of the difference _**a**_ − _**a**_[∗] are concentrated in the upper components, the bias can be further reduced by increasing _η_ . In contrast, if the weights are distributed more widely after _k_ , increasing _η_ does not reduce the bias much. Then, from the proof of Corollary 3, the error between _**a**_ ˜ updated by NGD and _**a**_[∗] is isotropically distributed ˜ throughout the whole space. Hence, since _k_ = _o(d)_ , the weights of _**a**_ − _**a**_[∗] are mostly distributed over the components after _k_ and _B_ FLNGD does not decrease even if _η_ is increased. On the other hand, the weights of the error between _**a**_ ˜ updated by GD and WLR and _**a**_[∗] are distributed to the upper _k_ components and the components after _k_ . Thus, _B_ FLWLR and _B_ FLGD decrease with increasing _η_ . 

Next, we discuss the effect of the step size _η_ to the variance. Figure 7 shows that the variance of each estimator as a function of the step size _η_ . From Fig. 7 , we can see that the variance of any feature learning method is almost the same as that of the random feature model. This is in accordance with the note of 1 1 Theorem 4 that the eigenvalues of _�_ 2 _W_ 1 _W_ 1[⊤] _[�]_[are almost the same as] _[ �]_ 2 _W_ 0 _W_ 0[⊤] _[�]_ even though _W_ 0 is updated with a rank-1 matrix to _W_ 1. 

Finally, we show the predictive error of each estimator as a function of the step size _η_ in Fig. 8. Note that the predictive error is the sum of the bias and variance _B_ ES + _V_ ES, 

123 

N. Hayato, S. Taiji 

**==> picture [440 x 290] intentionally omitted <==**

**Fig. 11** The relative bias with and without data splitting 

which can be obtained as the sum of the graphs in Figures 6 and 7. 

Figure 8 shows that the estimator of the feature learning model outperforms that of the one-layer linear regression model not only in terms of bias but also in terms of overall predictive error, especially with NGD feature learning. Here, in this experiment, the variance is about one order of magnitude smaller than the bias, and thus the behavior of the predictive error in Fig. 8 is almost dominated by the bias. However, if we multiply _σϵ_[2][by][10][and][let][the][bias][and][variance][to][the][same][magnitude,][the][behavior][of][the] predictive error will still follow the bias approximately. This is because, from Figs. 6 and 7, the difference of bias induced by feature learning is about two orders of magnitude larger than that of the variances. 

## **5 Conclusion and future work** 

_**Summary**_ We analyzed the effect of one-step feature learning for the two-layer linear neural network to its predictive error in a high dimensional regression setting and gave detailed evaluations of the bias and variance in two step size regimes (small step size and large step size). In particular, for the small step size, we gave the comparison 

123 

Feature learning and generalization error analysis of… 

between the predictive error of the estimator obtained by feature learning and that given by one-layer linear regression in a concrete form, and confirmed the correspondence with numerical experiments. Theoretical and experimental results showed that feature learning is more effective when the decay rate is slow _α <_ 0 in both cases. 

_**Future Work**_ In this study, we gave the analysis of a one step feature learning model for the case where the number of neurons is sufficiently large, but the analysis with a finite width network is important because a neural network with a finite number of neurons is used in practice. In addition, this study analyzed a linear neural network without a nonlinear activation function in the intermediate layer, so the estimator of this model has serious limitations as it can only represent linear functions on input data. Therefore, the analysis of feature learning models including a nonlinear activation function is an extremely important issue. 

## **6 Proof of Sect. 2** 

## **6.1 Proof of (5)** 

Since 

∥ _X_ _**a**_ − _**y**_ ∥[2] + _λ[(]_[1] _[)]_ ∥ _**a**_ ∥[2] = _**a**_[⊤] _(X_[⊤] _X_ + _λ[(]_[1] _[)] Id )_ _**a**_ − 2 _**y**_[⊤] _X_ _**a**_ + const. = _(_ _**a**_ − _(X_[⊤] _X_ + _λ[(]_[1] _[)] Id )_[−][1] _X_[⊤] _**y** )_[⊤] _(X_[⊤] _X_ + _λ[(]_[1] _[)][I][d] )(_ _**a**_ − _(X_[⊤] _X_ + _λ[(]_[1] _[)] Id )_[−][1] _X_[⊤] _**y** )_ +const. _,_ 

the first equation holds. Here, const. denotes a term independent of _**a**_ . 

Next, we prove the second equation. This can be directly derived from Appendix A of Tsigler and Bartlett [19]. Applying Sherman-Morrison formula yields 

**==> picture [238 x 22] intentionally omitted <==**

Therefore, 

**==> picture [274 x 76] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

## **7 Proof of Sect. 3** 

## **7.1 Proof of Theorem 1** 

As for the Bias, we have the statement from 

**==> picture [283 x 58] intentionally omitted <==**

Similarly, one can easily obtain the variance equation. 

## **7.2 Proof of Lemma 1** 

> 1 ˜ ˜ 1 ˜ From singular value decomposition, note that _�_ 2 _W_ 1 = _U_ � _�_ 2 _Od,N_ − _d_ � _V_[⊤] . Here, ˜ 1 1 _�_ is a diagonal matrix of the eigenvalues of _�_ 2 _W_ 1 _W_ 1[⊤] _[�]_ 2 in increasing order. From this, 

**==> picture [278 x 185] intentionally omitted <==**

holds. Hence, we have the result from 

**==> picture [338 x 70] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

## **7.3 Proof of Lemma 3** 

From Corollary 1, it is clear that the second term of Theorem 2 does not depend on _W_ 1 _[⋆]_[.][As][for][the][first][term,][note][that] _[�]_[0][:] _[k]_[is][not][singular,] _[k]_[columns][of] _[V]_[0][:] _[k]_[span] Im _(W_ 1[⊤] _[)]_[ ⊂][R] _[N]_[. Here, the set of all] _[ W][ ⋆]_ 1[is given as][ {] _[W]_[ †] 1[+] _[A]_[∈][R] _[N]_[×] _[d]_[|][ each column] of A is in Ker _(W_ 1 _)_ }. Because R _[N]_ = Im _(W_ 1[⊤] _[)]_[ ⊕][Ker] _[(][W]_[1] _[)]_[,] _[V]_ 0[ ⊤] : _k[A]_[=] _[O][k][,][d]_[holds and] the value of _V_ 0[⊤] : _k[W][ ⋆]_ 1[is constant for any] _[ W][ ⋆]_ 1[.] 

## **7.4 Proof of Theorem 3** 

In this proof, we usually omit _o(ε)_ . 

1 1 1 ˜ ˜ 1 ˜ Let _�_ 2 _W_ 0 = _U_ � _�_ 2 _Od,N_ − _d_ � _V_[⊤] and _�_ 2 _W_ 1 = _U_ � _�_ 2 _Od,N_ − _d_ � _V_[⊤] . Here, from _W_ 0 _W_ 0[⊤] = _Id_ , note that _U_ = _Id_ and _V_ 0: _d_ = _W_ 0[⊤][.][Furthermore,][letting] _[�]_[˜][=] diag _(λ_[˜] 1 _, . . . , λ_[˜] _d )_ does not contradict the notation of Theorem 1. Now, because _�_ 21 _W_ 1 _W_ 1[⊤] _[�]_ 21 = _�_ + _ε�_ 21 _**a**_ ˜ _**a**_ ˜[⊤] _�_ 21 holds and the eigenvalues of _�_ are not degenerate, 

**==> picture [100 x 46] intentionally omitted <==**

holds from Theorem 6. In the following, let _U_[˜] = _U_ + _δU_ and _�_[˜] = _�_ + _δ�_ . Here, note that _δU_ is an alternating matrix. 

Then, we calculates perturbation expansion of each term of _B_[¯] 1 and _V_[¯] 1 by using above equations. First, as for ∥ _V_[˜] 0[⊤] : _k[W][ ⋆]_ 1 _**[a]**_[∗][∥][2] _�_[−] 0:[1] _k_ , because 

**==> picture [209 x 30] intentionally omitted <==**

1 1 we can let _W_ 1 _[⋆]_[=] _[ (�]_ 2 _W_ 1 _)_[†] _�_ 2 . Hence, 

**==> picture [235 x 80] intentionally omitted <==**

Thus, 

**==> picture [338 x 42] intentionally omitted <==**

N. Hayato, S. Taiji 

**==> picture [275 x 52] intentionally omitted <==**

holds. As for the third term of (8), 

**==> picture [265 x 115] intentionally omitted <==**

holds. Here, when _**a**_ ˜ almost approximates _**a**_[∗] and _**a**_ ˜ _i_ _**a** i_[∗] _[>]_[0] _[,]_[ ˜] _**[a]**[ j]_ _**[ a]**_[∗] _j[>]_[0 holds for any] _i, j_ , the former term is positive and the latter term is negative. Furthermore, when _**a**_[∗] 1 is sparse, the third term is zero because diagonal components of _�_[−] 2[1] _δU �_ 2 are zero. 

2 _λ[(]_[2] _[)]_ +[�] _i>k[λ]_[˜] _[i]_ Next, as for _n_ , � � 

**==> picture [330 x 69] intentionally omitted <==**

holds. 

From the above, the first term of _B_[¯] 1 is represented as follows: 

**==> picture [273 x 133] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

Next, we analyze the second term of _B_[¯] 1. First, 

**==> picture [335 x 166] intentionally omitted <==**

holds. Here, let _δU_ = _δUk,k δUk,d_ − _k_ and we use the fact that _δU_ is an � _δUd_ − _k,k δUd_ − _k,d_ − _k_ � alternating matrix to derive the above identity. 

From that, by using Corollary 1, the second term is represented as follows: 

**==> picture [304 x 43] intentionally omitted <==**

Here, the second term of (9) implies the effect of mixing the first _k_ components and the rest of the components, and then this is represented as follows: 

**==> picture [247 x 38] intentionally omitted <==**

Similarly to the third term of (8), this is positive when _**a**_ ˜ _i_ _**a** i_[∗] _[>]_[0] _[,]_[ ˜] _**[a]**[ j]_ _**[ a]**_[∗] _j[>]_[0 for any] _i, j_ . 

From the above, we obtain the desired result of the bias. 

Next, as for the variance, 

**==> picture [306 x 76] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

**==> picture [263 x 31] intentionally omitted <==**

holds. Hence, we also obtain the results of the variance. 

## **7.5 Proof of Theorem 2** 

The proof of Theorem 2 is clear if we show 

**==> picture [82 x 12] intentionally omitted <==**

for any _i, j (i_ ̸= _j)_ . First, the following holds: 

**==> picture [281 x 53] intentionally omitted <==**

Now, as for the second term, noting that _X_ and _ϵ_ are independent, 

**==> picture [277 x 66] intentionally omitted <==**

holds. Similarly, the expectation of the third term is also zero. As for the fourth term, noting that each component of _X_ and _**ϵ**_ is all independent of each other, 

**==> picture [313 x 118] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

holds. Here, (10) holds from the fact that E _X ,ϵ_ [ _**ϵ** j_ _**ϵ** j_ ′] = E _X ,ϵ_ [ _**ϵ** j_ ]E _X ,ϵ_ [ _**ϵ** j_ ′] = 0 for _j, j_[′] _( j_ ̸= _j_[′] _)_ . Finally, as for the first term, 

**==> picture [339 x 192] intentionally omitted <==**

holds. From the above, we have the desired result. 

## **7.6 Proof of Corollary 3** 

When _**a**_[∗] is sparse, _B_[¯] 0 − _B_[¯] 1 is represented as follows: 

**==> picture [338 x 224] intentionally omitted <==**

Hence, when _k_[∗] ≤ _k_ , 

123 

N. Hayato, S. Taiji 

˜ holds. Now, from _**a**_ = _(�_ + _λ[(]_[1] _[)] Id )_[−][1] _X_[⊤] _**y** /n_ , noting that 

**==> picture [258 x 69] intentionally omitted <==**

we have 

**==> picture [218 x 152] intentionally omitted <==**

˜ Next, we evaluate E _X ,ϵ_ [ _(_ _**a** i_ − _**a** i_[∗] _[)]_[2][]][. Noting that] _**[ a]** i_[∗][=][ 0 for] _[ i][>][ k]_[, we get] 

**==> picture [272 x 61] intentionally omitted <==**

Hence, 

**==> picture [265 x 123] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

**==> picture [231 x 58] intentionally omitted <==**

holds. Therefore, 

**==> picture [296 x 43] intentionally omitted <==**

holds. From the above, we obtain the desired result. As for the variance, note that 

**==> picture [275 x 58] intentionally omitted <==**

for _i > k_ . Then, we have 

**==> picture [330 x 77] intentionally omitted <==**

## **7.7 Proof of Corollary 5** 

From the evaluation of series with the piecewise quadrature, 

**==> picture [157 x 82] intentionally omitted <==**

holds. And then, we get the result. 

123 

N. Hayato, S. Taiji 

## **7.8 Proof of Theorem4** 

1 1 Similarly to the proof of Theorem 3, we can let _W_ 1 _[⋆]_[=] _[ (�]_ 2 _W_ 1 _)_[†] _�_ 2 . Then, similarly 1 to the above, letting _U_[˜] , _V_[˜] , and _�_[˜] 2 be left singular vectors, right singular vectors, and 1 singular values of _�_ 2 _W_ 1, 

**==> picture [150 x 75] intentionally omitted <==**

holds. 

Here, we let _W_ 1 _(η)_ = _W_ 0 + _η_ _**aa**_ ˜[⊤] and _U_[˜] _(η)_ be left singular vectors of _�_ 21 _W_ 1 _(η)_ . 1 1 Noting that _U_[˜] _(η)_ are also eigenvectors of _�_ 2 _W_ 1 _(η)W_ 1 _(η)_[⊤] _�_ 2 _/η_[2] = _�/η_[2] + _�_ 21 _**a**_ ˜ _**a**_ ˜[⊤] _�_ 21 , _U_ ˜ := lim _η_ →∞ _U_ ˜ _(η)_ exists from Corollary 4.3 of Sun and Sun [17]. In this case, from _λ_[˜] 1 →∞ _(_ as _η_ →∞ _)_ , _λ_[˜] −1 2[1] _**u**_ ˜[⊤] 1 _[�]_ 21 _**a**_[∗] → 0 _._ . So, in the following, we analyze _**u**_ ˜ _i_[⊤] _[�]_ 21 _**a**_[∗] for _i >_ 1. First, we let 

**==> picture [346 x 48] intentionally omitted <==**

Next, we expand _**u**_ ˜ _i_ with { _**u** i_ } _i[d]_ =1[which is eigenvectors of] _[ A]_[:] _**[u]**_[˜] _[i]_[=][ �] _[d] j_ =1 _[d][i j]_ _**[ u]**[ j]_[. Then,] _**u**_ ˜ _i_[⊤] _[�]_ 21 _**a**_[∗] → _di_ 1 _(_ as _η_ →∞ _)_ holds. This is because _**u**_ 1 → _�_ 21 _**a**_[∗] from the fact that 1 1 1 _A_ = _�_ + _η_[2] _c_[2] _�_ 2 _**a**_[∗] _(�_ 2 _**a**_[∗] _)_[⊤] and ∥ _�_ 2 _**a**_[∗] ∥[2] = ∥ _**a**_[∗] ∥[2] _�_[=][ 1. Thus, we analyze] _[ d][i]_[1][in] the following. 

˜ Now, noting that _(A_ + _B)_ _**u** i_ = _λ_[˜] _i_ ˜ _**u** i_ , we have 

**==> picture [238 x 70] intentionally omitted <==**

Here, denote _λ[A] j_[to be the] _[j]_[-th largest eigenvalues of] _[A]_[. Multiplying (][12][) by] _**[ u]**_[⊤] 1[from] the left, we get 

**==> picture [65 x 28] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

**==> picture [71 x 29] intentionally omitted <==**

As for _**u**_[⊤] 1 _[B][/η]_[2][,] 

**==> picture [278 x 49] intentionally omitted <==**

holds. Then, as for _λ_ 1 _[A]_[,] 

**==> picture [297 x 16] intentionally omitted <==**

holds. Hence, _λ_ 1 _[A][/η]_[2][→] _[c]_[2] _[ (]_[as] _[ η]_[→∞] _[).]_[Furthermore,][as][shown][later,] _[λ]_[˜] _[i][/η]_[2][→] 0 _(_ as _η_ →∞ _)._ holds. Therefore we obtain 

**==> picture [91 x 22] intentionally omitted <==**

Next, we derive the evaluation of eigenvalues. From Corollary 2, _λi_ ≤ _λ_[˜] _i_ holds for any _i_ ∈[ _d_ ]. As for[�] _i>k[λ]_[˜] _[i]_[,][�] _i>k[λ]_[˜] _[i]_[=][�] _i[d]_ = _k_ +1 _[λ]_[˜] _[i]_[holds][because] _[λ]_[˜] _[i]_[=][0][for][any] _i > d_ . Here, noting that the trace is linear mapping: tr _(A_ + _B)_ = tr _(A)_ + tr _(B)_ , 

**==> picture [142 x 84] intentionally omitted <==**

olds. Furthermore, note that 

**==> picture [165 x 66] intentionally omitted <==**

From the above, we have 

**==> picture [130 x 31] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

**==> picture [232 x 68] intentionally omitted <==**

**Lemma 2** _Suppose A_ ∈ R _[n]_[×] _[n] is a real symmetric matrix and B_ ∈ R _[n]_[×] _[n] is a positivesemidefinite matrix. Then, for any i_ ∈[ _n_ ] _, μi (A)_ ≤ _μi (A_ + _B) holds._ 

_**Proof**_ Without loss of generality, we can assume that _A_ is a diagonal matrix with eigenvalues arranged in descending order. Note that, for any real symmetric matrix _C_ and _i_ ∈[ _n_ ], 

**==> picture [114 x 23] intentionally omitted <==**

holds. Then, 

**==> picture [301 x 129] intentionally omitted <==**

holds. Here, define R _[i]_ ⊕{ **0** _n_ − _i_ } := { _**v**_ ∈ R _[n]_ | _**v** i_ +1 = _**v** i_ +2 = · · · = _**v** n_ = 0}. From the above, we have the desired result. ⊓⊔ 

## **7.9 Proof of Corollary 6** 

Noting Theorem 1, the following holds from Theorem 7 of [19]. First, as for the case 1, 

1. If there exists some constants _C_[˜] _x_ that only depend on _σx_ and _nλ_[˜] _k_ +1 ≥ _C_[˜] _x_ � _i>k[λ]_[˜] _[i]_ for some _k < n/cx_ , then for _λ[(]_[2] _[)]_ = _nλ_[˜] _k_ +1 and for any _t_ ∈ _(cx , n/cx )_ , with probability at least 1 − 26 _e_[−] _[t][/][c][x]_ 

**==> picture [186 x 23] intentionally omitted <==**

123 

Feature learning and generalization error analysis of… 

holds. Then, from Corollary 1 and Theorem 4, 

**==> picture [320 x 36] intentionally omitted <==**

Furthermore, from remarks of Theorem 4, noting that _λ_[˜] _i_ − _λi_ = _o(_ 1 _)_ , _nλk_ +1 ≥ _Cx_ � _i>k[λ][i]_[holds if] _[ n][λ]_[˜] _[k]_[+][1][≥˜] _[C][x]_ � _i>k[λ]_[˜] _[i]_[.] Similarly, as for the case 2, 

**==> picture [339 x 47] intentionally omitted <==**

**==> picture [269 x 98] intentionally omitted <==**

holds. Especially, if _λi_ = _i_[−] _[(]_[1][+] _[α)] (_ −0 _._ 5 _< α <_ 0 _)_ , � _ni>λk_[2] _k[λ] i_[2] ≤ _nk[<]_[1][holds] because _λ_[2] _[(β][>]_[ 0] _[)]_[.] _i_[=] _[ i]_[−] _[(]_[1][+] _[β)]_ 

## **7.10 Proof of Theorem 7** 

˜ Define _**b**_[∗] = _**b** /_ _**a**_[⊤] _�_ _**a**_[∗] . First, define orthogonal matrices _P_ = _(_ _**p**_ 1 _, . . . ,_ _**p** d )_ ∈ R _[d]_ as follows: 

**==> picture [238 x 89] intentionally omitted <==**

Then, 

**==> picture [70 x 15] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

1 1 _�_ 2 _**a**_[∗] + _�_ 2 _**b**_[∗] = ~~�~~ ∥ _**a**_[∗] ∥[2] _�_[+ ∥] _**[b]**_[∗][∥][2] _�_ = _**e** k_[∗] + _O(_ ∥ _**b**_[∗] ∥ _�)._ 

Thus, for any _i_ ∈[ _d_ ], the sum part of _**p** i_ is bounded by _O(_ ∥ _**b**_[∗] ∥ _�)_ . Now, the second term of _P_[⊤] _�_ 21 _W_ 1 _W_ 1[⊤] _[�]_ 21 _P_ = _P_[⊤] _� P_ + _η_[2] _P_[⊤] _�_ 21 _**a**_ ˜ _**a**_ ˜[⊤] _�_ 21 _P_ is a matrix where only the (1,1) component is _η_[2] ∥˜ _**a**_ ∥[2] _�_[and the rest is zero. Further-] 1 1 more,non-diagonalcomponentsare _O(_ ∥ _**b**_[∗] ∥ _�)_ .Hence, _P_[⊤] _�_ 2 _W_ 1 _W_ 1[⊤] _[�]_ 2 _P_ isamatrix 1 1 which is a diagonal matrix added a _O(_ ∥ _**b**_[∗] ∥ _�)_ matrix. Thus _P_[⊤] _�_ 2 _W_ 1 _W_ 1[⊤] _[�]_ 2 _P_ can be diagonalized by an orthogonal matrix _Q_ where _Q_ = _Id_ + _O(_ ∥ _**b**_[∗] ∥ _�)_ from Theorem 6. 

1 Therefore, because _U_[˜] = _P Q_ for left singular vectors of _�_ 2 _W_ 1 : _U_ ˜ , we have desired result. 

## **8 Additional experiments** 

This section contains numerical experiments on facts mentioned in the text that are not directly related to the results of this study. 

We first see that _**a**_ ˆ RF →ˆ _**a**_ LR _(N /d_ →∞ _)_ holds as noted in Sect. 3. Figure 9a–c show ∥ˆ _**a**_ RF −ˆ _**a**_ LR∥[2] averaged over 100 times when _N /d_ is increased from 1 to 100. Although the value of ∥ˆ _**a**_ RF −ˆ _**a**_ LR∥[2] is different in each graph, in any _**a**_[∗] , ∥ˆ _**a**_ RF −ˆ _**a**_ LR∥[2] converges to 0 when _N /d_ is increased. 

We next see that when the decay rate of the eigenvalues is fast and _k_[∗] is small, the discrepancy between the estimator of the random feature model and that of the onelayer linear regression model is large. Figure 10 shows _BRF /BL R_ with _N /d_ = 10 fixed and _α_ and _k_[∗] changed respectively. 

From Fig. 10, when _α_ is large and _k_[∗] is small, _BRF /BL R_ is significantly large and _**a**_ ˆ RF and _**a**_ ˆ LR are highly divergent. This is because when _α_ is large and _k_[∗] is small, the bias of one-layer linear regression is very small. 

We lastly present some comparisons of the experimental results with and without data splitting. Figure 11a, c shows the relative bias in settings where data are split, while Fig. 11b, d shows that in settings without data splitting. 

Although each plot except blue plots shows qualitatively the same behavior, the bias values for the settings where data are split are uniformly about 0.3 smaller than that without data splitting. This means the bias improves more with feature learning in settings where the model is trained on split data. This is just because feature learning models use twice as much data for training as random feature models and linear regression models in such situations. 

123 

Feature learning and generalization error analysis of… 

## **9 Perturbation theory of matrices** 

This section presents various theorems on perturbations of matrices that are necessary for the analysis in Sect. 4. 

Theorem 5 characterizes the condition that a matrix’s eigenvalues respond in the first order when it is subjected to a first-order perturbation. This is not always trivial, as can be seen from the matrix below: 

**==> picture [32 x 25] intentionally omitted <==**

**Theorem 5** _Let A_ ∈ R _[n]_[×] _[n] be a diagonalizable square matrix and B_ ∈ R _[n]_[×] _[n] be any λ(ε)square_ ˜ _of matrix.A_ + _ε B is represented byIn this case, for anyλ(ε)_ ˜ _real_ = _λnumberi_ + _cε_ + _ε Osufficiently(ε_[2] _), given a constant c and thesmall, the eigenvalue eigenvalue λi of A._ 

_**Proof**_ Without loss of generality, let _A_ be a diagonal matrix. So, define _A_ := diag˜ _(A_ 1 _, A_ 2 _, . . . , Am)_ and _Ai_ := _λi Idi_ .Then,det _(x I_ − _(A_ + _ε B))_ = _f (x)_ + _g(x, ε)_ =: _f (x, ε)_ holds with _f (x)_ := det _(x I_ − _A)_ . Now, since _g(x, ε)_ is obviously a polynomial of high _n_ degree in _x_ and _ε_ and _A_ is a diagonal matrix, all terms in _g_ have _ε_ factors. 

We first prove the zeroth order expansion factor of _λ(ε)_[˜] . That is, lim _ε_ →0 _λ(ε)_[˜] = _λi_ holds for some _i_ ∈[ _m_ ]. Since _λ(ε)_[˜] is an eigenvalue of _A_ + _ε B_ , _f_[˜] _(λ(ε), ε)_[˜] = 0 holds. Therefore, noting that _A_ is a diagonal matrix, 

**==> picture [236 x 29] intentionally omitted <==**

holds. 

Now, note that _λ(ε)_[˜] ≤∥ _A_ + _ε B_ ∥op ≤∥ _A_ ∥op +∥ _B_ ∥op _<_ ∞ when _ε_ ≤ 1 and each term of _g(x, ε)_ contains a factor of _ε_ . Then lim _ε_ →0 _g(λ(ε), ε)_[˜] = 0 holds. Therefore, if lim _ε_ →0 _λ(ε)_[˜] = _λi_ does not hold for any _i_ ∈[ _m_ ], then the left side of (14) is not zero in the limit of _ε_ → 0, and this is a contradiction. Hence, lim _ε_ →0 _λ(ε)_[˜] = _λi_ holds for some _i_ ∈[ _m_ ]. 

We next prove that there exists a first-order perturbative expansion of _λ(ε)_[˜] . Hereafter, _i_ ∈[ _m_ ] is assumed to satisfy lim _ε_ →0 _λ(ε)_[˜] = _λi_ . This proof is almost clear by showing that the polynomial _g(λi , ε)_ for _ε_ contains a factor _ε[d][i]_ in every term. Thus, we first prove this. 

_g(λi , ε)_ = _f (λi )_ + _g(λi , ε)_ = det _((λi I_ − _A)_ − _ε B)_ , but the matrix _(λi I_ − _A)_ − _ε B)_ contains only _ε B_ components in the _di_ row where the diagonal matrix _Ai_ is stored. Thus, all nonzero terms in the determinant det _((λi I_ − _A)_ − _ε B)_ involve a factor of _ε[d][i]_ . 

Now, because _λ(ε)_[˜] ̸= _λ j (i_ ̸= _j)_ for a sufficiently small _ε_ , we have 

**==> picture [164 x 33] intentionally omitted <==**

123 

N. Hayato, S. Taiji 

from (14). 

Considering the limit of _ε_ → 0 on the right-hand side, for the numerator lim _ε_ →0 _g(λ(ε), ε)/ε_[˜] _[d][i]_ = lim _ε_ →0 _g(λi , ε)/ε[d][i] <_ ∞ holds. The first equality is understood from the fact that each term of _g(λ(ε), ε)_[˜] is a polynomial consisting of the product of _λ(ε)_[˜] and _ε_ , and the limit can be decomposed for the product. The second inequality is as noted that the polynomial _g(λi , ε)_ in _ε_ begins with the term _ε[d][i]_ . For the denominator limit, lim _ε_ →0 � _j_ ̸= _i[(][λ(ε)]_[˜][ −] _[λ][ j][)][d][ j]_[=][ �] _j_ ̸= _i[(λ][i]_[−] _[λ][ j][)][d][ j]_[̸=][ 0 holds.] From the above, letting _c_ = lim _ε_ →0 − _(g(λ(ε), ε)/ε_[˜] _[d][i] )/_[�] _j_ ̸= _i[(][λ(ε)]_[˜][ −] _[λ][ j][)][d][ j][<]_[ ∞][,] we have _λ(ε)_[˜] = _λi_ + _cε_ + _O(ε_[2] _)_ . ⊓⊔ 

From here, we show that the eigenvectors respond in first order when perturbed to a matrix whose eigenvalues are not degenerate. In general, when eigenvalues are degenerate, even if the eigenvalues are diagonalizable, there are degrees of freedom in how the eigenspace is grounded, making perturbation analysis of the eigenvectors 

**Corollary 8** _If the matrix A_ ∈ R _[n]_[×] _[n] has no degenerate eigenvalues, then for any sufficiently small real number ε and any matrix B_ ∈ R _[n]_[×] _[n] , A_ + _ε B has no degenerate eigenvalues._ 

_**Proof**_ Fix a sufficiently small _ε_ . Assume the existence of degenerate eigenvalues _λ_[˜] of _A_ + _ε B_ . From Theorem 5, there exists _i_ ∈[ _n_ ] and _λ_[˜] = _λi_ + _O(ε)_ holds. Now, from the assumption, 

**==> picture [131 x 25] intentionally omitted <==**

holds. On the other hand, 

**==> picture [337 x 81] intentionally omitted <==**

Therefore, _A_ + _ε B_ has no degenerate eigenvalues. ⊓⊔ 

From Theorem 5 and Corollary 8, we have the following corollary. 

**Corollary 9** _If the matrix A_ ∈ R _[n]_[×] _[n] has n distinct eigenvalues_ { _λ_ 1 _, . . . , λn_ } _, then for any sufficiently small real number ε and any square matrix B_ ∈ R _[n]_[×] _[n] , the matrix A_ + _ε B has n different eigenvalues_ { _λ_[˜] 1 _, . . . , λ_[˜] _n_ } _and each is represented as λ_[˜] _i_ = _λi_ + _ci ε_ + _O(ε_[2] _) with constants c_ 1 _, . . . , cn._ 

**Lemma 3** _Let A_ ∈ R _[n]_[×] _[n] be a matrix whose eigenvalues are not degenerate and U_ ∈ R _[n]_[×] _[n] be its basis matrix. That is, U_[−][1] _AU is diagonal matrix. Then, for any_ 

123 

Feature learning and generalization error analysis of… 

_sufficiently small real number ε and any square matrix B_ ∈ R _[n]_[×] _[n] , there exists a basis matrix U_[˜] _(ε) of A_ + _ε B and_ lim _ε_ →0 _U_[˜] _(ε)_ = _U holds._ 

˜ _**Proof**_ ˜ Define _U_ = _(_ _**u**_ 1 _, . . . ,_ _**u** n)_ and _U_[˜] ˜ _(ε)_ = _(_ _**u**_ 1 _(ε), . . . ,_ ˜ _**u**_ ˜ _n(ε))_ . The existence of _U (ε)_ is clear from Corollary 9. Then, _(λi (ε)I_ − _(A_ + _ε B))_ _**u** i (ε)_ = **0** holds for each ˜ _i_ ∈[ _n_ ] with any small _ε_ . Now, assume that lim _ε_ →0 _**u** (ε)_ = _**v**_ ̸= _**u** i_ . Then, we have 

**==> picture [279 x 31] intentionally omitted <==**

However, each eigenspace is one-dimensional, since any eigenvalue of _A_ is not degenerate. Therefore, _(λi I_ − _A)_ _**v**_ ̸= **0** from _(λi I_ − _A)_ _**u** i_ = **0** _,_ _**v**_ ̸= _**u** i_ . This is a contradiction. Then, eigenvectors are continuous. ⊓⊔ 

Theorem 6 shows that the eigenspace has a first-order response for perturbation when the eigenvectors form an orthonormal basis. Furthermore, we give explicit form for first-order perturbations of eigenvalues and eigenvectors. 

**Theorem 6** _Let A_ ∈ R _[n]_[×] _[n] be a normal matrix whose eigenvalues are not degenerate and B_ ∈ R _[n]_[×] _[n] be any square matrix. Let U_ = _(_ _**u**_ 1 _, . . . ,_ _**u** n) be eigenvectors and λ_ 1 _, . . . , λn be eigenvalues of A, then for a sufficiently small real number ε, (A_ + _ε B)’s_ ˜ _eigenvectors U_[˜] = _(_ _**u**_ 1 _(ε), . . . ,_ ˜ _**u** n(ε)) and eigenvalues_ { _λ_[˜] 1 _(ε), . . . , λ_[˜] _n(ε)_ } _are given by_ 

**==> picture [155 x 48] intentionally omitted <==**

_**Proof**_ Note that since _A_ is normal, _U_ is an orthogonal matrix, i.e. _U_[⊤] _U_ = _I_ . If we ˜ represent _λ_[˜] _i (ε)_ = _λi_ + _δλi (ε)_ and _**u** i (ε)_ = _**u** i_ + _**δu** i (ε)_ , then we have 

**==> picture [221 x 10] intentionally omitted <==**

If we represent _λ_[˜] _i (ε)_ = _λi_ + _δλi (ε)_ and _**u**_ ˜ _i (ε)_ = _**u** i_ + _**δu** i (ε)_ , then we have 

**==> picture [221 x 10] intentionally omitted <==**

From Lemma 3, lim _ε_ →0 _ci j (ε)_ = 0. Then, since 1 + _cii (ε)_ ̸= 0 for sufficiently small _ε_ , letting _di j (ε)_ = _ci j (ε)/(_ 1 + _cii (ε))_ , we have 

**==> picture [307 x 56] intentionally omitted <==**

N. Hayato, S. Taiji 

Then, we have 

**==> picture [313 x 31] intentionally omitted <==**

Thus, noting _εdi j (ε)_ = _o(ε)_ and multiplying both sides by _**u** i_[⊤][from the left, we get] 

**==> picture [106 x 13] intentionally omitted <==**

Then multiplying by _**u**_[⊤] _j[(][i]_[̸=] _[j][)]_[ from the left, we get] 

**==> picture [109 x 29] intentionally omitted <==**

**==> picture [8 x 6] intentionally omitted <==**

**Corollary 10** _In particular, when A is a symmetric matrix, the eigenvalues and eigenvectors of A_ + _ε B are given in the above form._ 

**Acknowledgements** HN was partially supported by JST CREST (JPMJCR2115). TS was partially supported by JSPS KAKENHI (20H00576) and JST CREST (JPMJCR2015). 

**Funding** Open Access funding provided by The University of Tokyo. 

**Data availability** The authors declare that the data supporting the findings of this study are available within this paper. 

## **Declarations** 

**Conflict of interest** The corresponding author states that there is no Conflict of interest. 

**OpenAccess** ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

## **References** 

1. Amari, S., Ba, J., Grosse, R.B., Li, X., Nitanda, A., Suzuki, T., Wu, D., Xu, J.: When does preconditioning help or hurt generalization? In: International Conference on Learning Representations (2021). https://openreview.net/forum?id=S724o4_WB3 

2. Azulay, S., Moroshko, E., Nacson, M.S., Woodworth, B.E., Srebro, N., Globerson, A., Soudry, D.: On the implicit bias of initialization shape: beyond infinitesimal mirror descent. In: International Conference on Machine Learning, pp. 468–477. PMLR (2021) 

123 

Feature learning and generalization error analysis of… 

3. Ba, J., Erdogdu, M.A., Suzuki, T., Wang, Z., Wu, D., Yang, G.: High-dimensional asymptotics of featurelearning:howonegradientstepimprovestherepresentation.In:AdvancesinNeuralInformation Processing Systems (2022). https://openreview.net/forum?id=akddwRG6EGi 

4. Bartlett, P.L., Long, P.M., Lugosi, G., Tsigler, A.: Benign overfitting in linear regression. Proc. Natl. Acad. Sci. **117** (48), 30063–30070 (2020) 

5. Belkin, M., Hsu, D., Ma, S., Mandal, S.: Reconciling modern machine-learning practice and the classical bias-variance trade-off. Proc. Natl. Acad. Sci. **116** (32), 15849–15854 (2019) 

6. Chatterji, N.S., Long, P.M., Bartlett, P.L.: The interplay between implicit bias and benign overfitting in two-layer linear networks. J. Mach. Learn. Res. **23** (263), 1–48 (2022) 

7. Cheng, C., Montanari, A.: Dimension free ridge regression (2022). arXiv preprint arXiv:2210.08571 

8. Damian, A., Lee, J., Soltanolkotabi, M.: Neural networks can learn representations with gradient descent. In: Conference on Learning Theory, pp. 5413–5452. PMLR (2022) 

9. Frei, S., Chatterji, N.S., Bartlett, P.: Benign overfitting without linearity: neural network classifiers trained by gradient descent for noisy linear data. In: Conference on Learning Theory, pp. 2668–2703. PMLR (2022) 

10. Hastie, T., Montanari, A., Rosset, S., Tibshirani, R.J.: Surprises in high-dimensional ridgeless least squares interpolation. Ann. Stat. **50** (2), 949–986 (2022) 

11. Imaizumi, M., Fukumizu, K.: Deep neural networks learn non-smooth functions effectively. In: International Conference on Artificial Intelligence and Statistics, pp. 869–878. PMLR (2019) 

12. Jastrzebski, S., Szymczak, M., Fort, S., Arpit, D., Tabor, J., Cho, K., Geras, K.: The break-even point on optimization trajectories of deep neural networks. In: International Conference on Learning Representations (2020). https://openreview.net/forum?id=r1g87C4KwB 

13. Li, Z., Zhou, Z.-H., Gretton, A.: Towards an understanding of benign overfitting in neural networks (2021). arXiv preprint arXiv:2106.03212 

14. Louart, C., Liao, Z., Couillet, R.: A random matrix approach to neural networks. Ann. Appl. Probab. **28** (2), 1190–1248 (2018) 

15. Mei, S., Montanari, A.: The generalization error of random features regression: precise asymptotics and the double descent curve. Commun. Pure Appl. Math. **75** (4), 667–766 (2022) 

16. Neyshabur, B., Li, Z., Bhojanapalli, S., LeCun, Y., Srebro, N.: The role of over-parametrization in generalization of neural networks. In: International Conference on Learning Representations (2019). https://openreview.net/forum?id=BygfghAcYX 

17. Sun, D., Sun, J.: Strong semismoothness of eigenvalues of symmetric matrices and its application to inverse eigenvalue problems. SIAM J. Numer. Anal. **40** (6), 2352–2367 (2002) 

18. Suzuki, T.: Adaptivity of deep ReLU network for learning in Besov and mixed smooth Besov spaces: optimal rate and curse of dimensionality. In: International Conference on Learning Representations (2019). https://openreview.net/forum?id=H1ebTsActm 

19. Tsigler, A., Bartlett, P.L.: Benign overfitting in ridge regression (2020). arXiv preprint arXiv:2009.14286 

20. Xu, J., Hsu, D.J.: On the number of variables to use in principal component regression. In: Advances in Neural Information Processing Systems, vol. 32, pp. 5095–5104 (2019) 

21. Zhang, C., Bengio, S., Hardt, M., Recht, B., Vinyals, O.: Understanding deep learning (still) requires rethinking generalization. Commun. ACM **64** (3), 107–115 (2021) 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps 

123 

