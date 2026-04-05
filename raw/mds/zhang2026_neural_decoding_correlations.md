Article 

## Exploiting correlations across trials and behavioral sessions to improve neural decoding 

## Highlights 

- Behaviorally relevant neural structures are shared across animals in low-dimensional space 

- Models exploiting shared structure improve prediction of behavior from neural activity 

- Linear models scale to large neural datasets across sessions and brain regions 

- Shared low-rank temporal patterns reveal brain-wide activation timescales 

## Authors 

Yizi Zhang, Hanrui Lyu, Cole Hurwitz, ..., Alexandre Pouget, Erdem Varol, Liam Paninski 

## Correspondence 

yz4123@columbia.edu (Y.Z.), liam@stat.columbia.edu (L.P.) 

## In brief 

Animals share common patterns of brain activity across trials and sessions. Exploiting this shared structure improves the prediction of behavior from neural activity, scales across many sessions and brain regions, and offers interpretable alternatives to deep-learning-based foundation models. 

**==> picture [17 x 17] intentionally omitted <==**

Zhang et al., 2026, Neuron _114_ , 536–551 February 4, 2026 © 2025 The Authors. Published by Elsevier Inc. https://doi.org/10.1016/j.neuron.2025.10.026 

**ll** 

**ll** OPEN ACCESS 

**==> picture [76 x 35] intentionally omitted <==**

## Article 

## **Exploiting correlations across trials and behavioral sessions to improve neural decoding** 

Yizi Zhang,[1][,][8][,][10][,] * Hanrui Lyu,[3][,][8] Cole Hurwitz,[2][,][6] Shuqi Wang,[4] Charles Findling,[6][,][7] Yanchen Wang,[2] Felix Hubert,[7] International Brain Laboratory,[6] Alexandre Pouget,[6][,][7] Erdem Varol,[5] and Liam Paninski[1][,][2][,][6][,][9][,] * 

1Department of Statistics, Columbia University, New York, NY, USA 

2Center for Theoretical Neuroscience, Columbia University, New York, NY, USA 

3Department of Statistics and Data Science, Northwestern University, Evanston, IL, USA 

4Department of Computer Science, E´ cole Polytechnique Fe´ de´ rale de Lausanne (EPFL), Lausanne, Switzerland 

5Department of Computer Science and Engineering, New York University, New York, NY, USA 

6The International Brain Laboratory 7Department of Basic Neurosciences, University of Geneva, Geneva, Switzerland 

8These authors contributed equally 

9Senior author 10Lead contact *Correspondence: yz4123@columbia.edu (Y.Z.), liam@stat.columbia.edu (L.P.) https://doi.org/10.1016/j.neuron.2025.10.026 

## SUMMARY 

Traditional neural decoders link neural activity to behavior within single trials of a session, overlooking correlations across trials and sessions. However, animals show similar neural patterns when performing the same task, and their behaviors are influenced by prior experiences. To capture these dependencies, we introduce two complementary models: a multi-session reduced-rank regression model that shares behaviorally relevant neural structure across sessions and a multi-session state-space model that captures behavioral structure across trials and sessions. On 433 sessions spanning 270 brain regions in the International Brain Laboratory (IBL) mouse Neuropixels dataset, our decoders outperform traditional approaches on four behaviors, with results generalizing across datasets, species, and tasks. Unlike deep learning methods, our models are efficient and interpretable, providing low-dimensional neural representations, task-related single-neuron contributions, and brain-wide timescales of neural activation. 

## INTRODUCTION 

Neural decoding is a critical tool for understanding the relationship between neural activity and behavior. Traditional neural decoders operate on a single-trial, single-session basis,[1][,][2] modeling neural-behavioral relationships within individual trials. However, they ignore correlations across trials and sessions in both neural and behavioral data, missing opportunities to exploit the rich structure of large-scale datasets spanning multiple sessions, animals, and brain regions. 

Similar neural activities emerge across experimental sessions when animals perform the same task.[3–6] Leveraging such intersession neural similarities offers an opportunity to improve single-session decoding,[7–9] but direct sharing is difficult since each session records different neurons. An alternative approach is to capture population-level variations via their correlation structures in neural latents across sessions. Previous unsupervised and self-supervised studies follow this strategy to estimate shared neural dynamics,[10–13] although the learned latents often lack behavioral relevance and thus require fine-tuning for decoding. Supervised approaches can instead learn behaviorally rele- 

vant neural representations across sessions, but existing methods[14][,][15] demand heavy computation and produce complex black-box models. A lightweight, interpretable model is therefore needed to share behaviorally relevant neural variations across sessions. 

Animal behavior depends not only on the current task but also on prior experiences. For example, Ashwood et al.[16] show that mouse decisions reflect internal states persisting across tens to hundreds of trials, well captured by hidden Markov models (HMMs). These latent states are reproducible across animals and sessions, and many experiments exhibit similar trial-to-trial correlations. Accounting for these behavioral correlations, alongside inter-session neural similarities, can potentially improve decoding. Moreover, inferring these latent states reveals the internal dynamics driving behavior and how animals transition between states during a task. Examining whether such latent states are shared across individuals can further distinguish common behavioral strategies from animal-specific ones. 

In this work, we develop two complementary methods to leverage neural and behavioral correlations for improved decoding. For neural data, we propose a multi-session reduced-rank 

**==> picture [16 x 17] intentionally omitted <==**

536 Neuron _114_ , 536–551, February 4, 2026 © 2025 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/). 

**ll** OPEN ACCESS 

## Article 

regression model (RRR) that captures shared temporal patterns across sessions while preserving session-specific differences in neural activity. For behavioral data, we introduce multi-session state-space models to infer latent states from trial-to-trial correlations. These representations are then used to improve singletrial, single-session decoders. Unlike deep learning approaches that rely on complex black-box models, our methods are simple, interpretable, and easy to fit. We evaluate the proposed approaches on International Brain Laboratory (IBL) mouse Neuropixels recordings[17][,][18] spanning 433 sessions and 270 brain regions, as well as on the Allen Institute Neuropixels visual coding dataset[19] and a primate random target-reaching task with Utah arrays.[20] Across datasets, species, and tasks, our models improve decoding accuracy. They are also computationally efficient, allowing us to create a brain-wide map of behaviorally relevant timescales and identify task-related neurons. 

## RESULTS 

## Formulation of the neural data-sharing model 

Our goal is to decode behavior _y_ ∈ ℝ _[P]_ from spike-sorted, temporally binned spike counts. For each trial _k_ , neural activity has size _N_ × _T_ , where _N_ is the number of neurons and _T_ the number of time steps. Recordings are split into 2-s trials, each divided into 20-ms bins, producing _T_ = 100 time steps. For each trial, we constructed _X_ ∈ ℝ _[N]_[×] _[T]_ by aggregating spike counts and used it to compute a decoder estimate _d_ ∈ ℝ _[P]_ of the true behavior _y_ ∈ ℝ _[P]_ . _y_ is constant within a trial (‘‘per-trial decoding’’); when _P_ = _T_ , _y_ varies across time (‘‘per-timestep decoding’’). For simplicity, we first present the model assuming _y_ is scalar ( _P_ = 1). 

Traditional single-session decoders use _full_ - _rank_ models with an unconstrained weight matrix _W_ ∈ ℝ _[N]_[×] _[T]_ : 

_d_ = _f_ (vec( _X_ )[⊤] vec( _W_ ) + _b_ ) _;_ (Equation 1) 

where vec( ⋅) denotes the vectorization (flattening) operator, and _b_ ∈ ℝ is a bias term. For large _N_ and _T_ , the number of parameters grows quickly, making such models prone to overfitting. 

To mitigate overfitting, we impose a low-rank constraint on the weight matrix by factorizing it into two smaller matrices: 

_d_ = _f_ (vec( _X_ )[⊤] vec( _UV_ ) + _b_ ) _;_ (Equation 2) 

where _U_ ∈ ℝ _[N]_[×] _[R]_ and _V_ ∈ ℝ _[R]_[×] _[T]_ are low-rank bases capturing neural and temporal components of _W_ . This RRR lowers the parameter count from _N_ × _T_ (Equation 1) to _R_ ( _N_ + _T_ ), with _R <_ min( _N; T_ ). The function _f_ may be linear or nonlinear, depending on the application. Note that the formulation in Equation 2 differs from standard reduced-rank regression previously applied to predict neural responses[21] ; see STAR Methods for details. 

The parameters _U_ , _V_ , and _b_ can be estimated via automatic differentiation or closed-form solutions. When _f_ is the identity function (linear model), closed-form solutions exist. In particular, _U_ defines a subspace that maximizes the correlation between neural activity _X_ and behavior _y_ while capturing the main variations in _y_ . Consequently, the RRR can be interpreted as a latent variable model, with rank _R_ specifying the number of latent variables needed to capture behaviorally relevant neural variations. 

See STAR Methods section ‘‘closed-form solution for reducedrank regression model’’ for details. 

Rather than manually aligning neurons across populations, based on firing or physical properties,[22][,][23] we aim to automatically learn a common neural representational space for decoding multiple populations. To achieve this, we introduce a multi-session RRR (RRR (M); Figure 1C) that captures shared neural representations and improves decoding. Given that neural populations within a region often exhibit similar activation patterns[3] (Figure 1B), we share the low-rank temporal basis _V_ across sessions while keeping session-specific neural bases _U[i]_ : 

**==> picture [204 x 13] intentionally omitted <==**

where _X[i]_ ∈ ℝ _[N][i]_[×] _[T]_ and _d[i]_ ∈ ℝ are the neural activity and predicted behavior for a single trial in session _i_ , corresponding to _X_ and _d_ in Equation 2. Sharing _V_ across sessions reduces the number of parameters, enabling more robust estimation from the same amount of data. 

The RRR (M) shares a temporal basis across sessions, assuming uniform neural activation patterns across regions. However, different brain regions may activate at different times within a trial due to functional differences[24–26] ; for example, sensory areas may respond earlier than cognition-related areas. To capture such regional temporal differences while retaining the benefits of a low-rank model across sessions, we introduce a multi-region RRR (RRR (MR); Figure 1D), which factorizes the across-session temporal basis _V_ into two low-rank matrices, enabling flexible temporal bases for regions indexed by _j_ : 

**==> picture [227 x 13] intentionally omitted <==**

where _X[ij]_ ∈ ℝ _[N][ij]_[×] _[T]_ is neural activity from region _j_ in session _i_ , and _d[ij]_ ∈ ℝ is the decoded behavior. Here, _A[j]_ ∈ ℝ _[L]_[×] _[R]_ captures region-specific temporal differences, _B_ ∈ ℝ _[L]_[×] _[T]_ captures shared temporal structure across regions, and _L_ is the rank of both _A[j]_ and _B_ . For _y[ij]_ ∈ ℝ, a RRR (M) (Equation 3) across _J_ regions and _I_ sessions learns an _R_ × _T_ temporal basis, whereas a RRR (MR) (Equation 4) increases this slightly to _L_ × ( _J_ × _R_ + _T_ ). We select _L_ and _R_ via hyperparameter tuning and empirically find _L; R <_ 10, allowing flexible region-specific temporal bases while leveraging shared structure. 

## Formulation of the behavioral data-sharing model 

In neuroscience experiments, animal behaviors often exhibit trial-to-trial correlations that can improve single-trial decoders. When neural activity from a single trial or session is limited, incorporating data from neighboring trials or additional sessions can boost decoding performance. 

For traditional decoders, we used neural activity _Xk_ in trial _k_ to predict the true behavior _yk_ and obtained a decoder estimate _dk_ . The index _k_ emphasizes that _Xk; yk_ , and _dk_ are single-trial quantities, with _Xk_ corresponding to _X_ in Equation 2 and _X[i]_ in Equation 3 and with _dk_ corresponding to _d_ in Equation 2 and _d[i]_ in Equation 3. (Here, we focus on per-trial decoded scalar quantities _dk_ ∈ ℝ, but this can be generalized.) Our goal is to improve _dk_ from the baseline decoder, which produces independent estimates per trial. For instance, a linear baseline captures correlations across neurons and time steps but not across trials, and in 

**==> picture [46 x 35] intentionally omitted <==**

Neuron _114_ , 536–551, February 4, 2026 537 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [490 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>OPEN ACCESS Article<br>A B C<br>D<br>E<br>F<br>G<br>H<br>**----- End of picture text -----**<br>


**Figure 1. Schematic illustration of neural and behavioral data-sharing models** (A) Mice indicate the location of a visual stimulus by rotating a wheel. 

(B) Neural activity consistently increases after stimulus onset (dashed line, t = 0 s) across four sessions. Each row shows a neuron’s peri-stimulus time histogram (PSTH), averaged over all trials. 

(C) Multi-session reduced-rank regression: neural activity _X[i]_ is projected onto a subject-specific basis _U[i]_ and multiplied by a shared temporal basis _V_ to predict behavior _d[i]_ . 

(D) Multi-region reduced-rank regression: for subject _i_ and region _j_ , activity is projected onto _U[i]_ and multiplied by a region-specific temporal basis _V[j]_ = _A[j] B_ to produce behavior _d[ji]_ . 

(E) Slowly changing prior beliefs _yk_ (dark purple) show trial-to-trial correlations ignored by single-trial decoders (light purple). Behavioral patterns are consistent across sessions. 

- (F) LG-AR1 model: latent behaviors _zk_ and observed decoder outputs _dk_ match the color-coded examples in (E). 

(G) Binary choices _yk_ (blue/green) show trial-to-trial correlations missed by single-trial decoders _dk_ gray). Similar behavioral patterns also occur across sessions. (H) BMM-HMM model: latent states _sk_ , latent behaviors _zk_ , and observed decoder outputs _dk_ match the color-coded examples in (G). 

reduced-rank regression, _U_ captures inter-neuronal dependencies while _V_ captures within-trial temporal structure. Neither models trial-to-trial dependencies, however. 

To improve _dk_ , we exploit trial-to-trial correlations across trials and the statistical structure in multiple sessions. We assume that the observations _dk_ are generated from latent variables _zk_ representing the underlying behavior, which evolve according to a latent dynamic process. For continuous behaviors (e.g., an animal’s prior belief about stimulus probability[27] ), we model _zk_ transitions with a first-order autoregressive process; each _zk_ depends on _zk_ − 1, and the continuous decoder _dk_ ∈ ℝ depends linearly on _zk_ in the same trial. This defines a linear Gaussian autoregressive model of order 1 (LG-AR1). Given the sequence[→] _d_ = ( _d_ 1 _; d_ 2 _;_ … _; dk_ ), we infer _zk_ via standard Kalman smoothing.[28] The inferred _zk_ serves as an improved decoder estimate, 

potentially closer to the true behavior _yk_ than the single-trial _dk_ , by incorporating information from neighboring trials and other sessions. See Figures 1E and 1F and STAR Methods section ‘‘LG-AR1: model details’’ for the data-generating mechanism. 

While the LG-AR1/Kalman smoother improves estimates of continuous _yk_ from noisy single-trial decoder outputs _dk_ , it is unsuitable for binary _yk_ ∈{0 _;_ 1}, such as an animal’s choice in IBL experiments.[17][,][18] In these experiments, mice indicate the location of a visual stimulus by rotating a wheel. The stimulus is initially equally likely on either side for the first 90 trials, then biased to one side in subsequent blocks. This creates a three-level data-generating process: (1) the animal forms an internal belief about the stimulus-generating state ( _sk_ ), (2) choices ( _zk_ ) are made based on the perceived state, and (3) the decoder estimate _dk_ is generated conditional on _zk_ . This hierarchical 

538 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

structure necessitates a modeling approach different from LG-AR1. 

For binary _yk_ ∈{0 _;_ 1}, the single-trial decoder output _dk_ ∈ [0 _;_ 1] represents the probability of _yk_ = 1. We assume _dk_ is generated from a mixture of beta distributions, with mixture assignment determined by a latent variable _zk_ . When the decoder accurately predicts behavior, the beta components are well separated; _dk_ is near 1 when _zk_ = 1 predicts _yk_ = 1 and near 0 when _zk_ = 0 predicts _yk_ = 0. Poor decoder performance leads to overlapping beta components. We further assume that _zk_ depends on behavioral states _sk_ , whose transitions follow an HMM with _H_ discrete states. In the IBL binary choice task, at least three hidden states exist: random switching (stimulus appears randomly), left biased, and right biased (stimulus predominantly appears on one side). The probability of _zk_ depends on the latent state via emission probabilities. We call this the beta mixture model HMM (BMM-HMM). Given the sequence[→] _d_ = ( _d_ 1 _; d_ 2 _;_ … _; dk_ ), we infer both _sk_ and _zk_ . The inferred _zk_ provides an improved decoder estimate, potentially closer to the true behavior _yk_ than _dk_ , by incorporating information from neighboring trials and other sessions. See Figures 1G and 1H and STAR Methods section ‘‘BMM-HMM: model details’’ for the data-generating mechanism. 

Single-session LG-AR1 and BMM-HMM models may output inaccurate parameter estimates when neural signals in the target session are insufficient. To address this, we propose multi-session versions of these models that utilize shared statistical structure across sessions to improve parameter estimation. Our multi-session approach learns empirical prior distributions of model parameters, using observed behaviors from training sessions, and applies these priors to constrain model parameter updates during inference on the test session. This method, which borrows from empirical Bayes literature,[29–31] pools data more effectively to constrain model parameters and improve characterization of underlying dynamics.[32][,][33] For more information on prior distribution choices and implementation details, see STAR Methods section ‘‘BMM-HMM: model details’’ and ‘‘LGAR1: model details.’’ 

## Learning behaviorally relevant neural variations across sessions 

We apply our models to 433 IBL sessions,[17] covering 270 brain regions and four behavioral variables: choice, prior, wheel speed, and whisker motion energy. While our main experiments focus on IBL data, the methods are broadly applicable to neural activity, with consistent temporal structure and behaviors exhibiting trial-to-trial correlations. In the IBL experiments, mice rotate a wheel to indicate the location of a visual stimulus, defined as their _choice_ (Figure 1A). For the first 90 trials, the stimulus appears randomly on either side with equal probability; in subsequent trials, it appears predominantly on one side in blocks.[17][,][18] Mice adapt their behavior to these changing probabilities, allowing estimation of each mouse’s trial-by-trial _prior belief_ ( _prior_ ) about stimulus location.[27] Additionally, _wheel speed_ and _whisker motion energy_ near the whisker pad are recorded. Whisker motion energy is computed as the mean absolute difference between adjacent video frames within a bounding box anchored between nose tip and eye.[34] Choice and prior are static within 

a trial, while wheel speed and whisker motion energy are timevarying signals sampled at 60 Hz. See STAR Methods sections ‘‘data processing’’ and ‘‘hyperparameter selection’’ for details. 

The RRR improves decoding by projecting neural activity onto a low-dimensional subspace that emphasizes behaviorally relevant variability. Unlike principal-component analysis (PCA),[35] which captures both relevant and irrelevant components,[36][,][37] RRR focuses on neural representations most predictive of behavior.[38] This supervised dimensionality reduction disentangles behaviorally relevant dynamics more effectively than unsupervised methods such as PCA or demixed PCA[38] (see STAR Methods). 

To illustrate, we compare PCA and RRR projections for decoding the binary choice variable. Figure 2A shows single-session projections, where RRR better separates behavioral classes than PCA. Using _k_ -means clustering and the adjusted Rand index (ARI),[39][,][40] we find that RRR (M) produces more discriminative neural representations by leveraging shared structure across sessions, reducing overfitting and enhancing generalizability. In Figures 2B and 2C, RRR (M) achieves higher ARI and decoding accuracy than single-session RRR ( _p <_ 0 _:_ 002 via bootstrap resampling; see STAR Methods), confirming the significance of these gains. 

The RRR also improves decoding of continuous behaviors— prior, wheel speed, and whisker motion energy—more accurately than ridge regression (Figures 2D and 2E). Prediction quality is evaluated both for reconstructing trial-averaged behavior across stimulus conditions and for capturing trial-specific variability. Figures 3A–3C and 3I–3K show reliable reconstruction of trial-averaged behavior, while Figures 3D, 3E, 3L, and 3M demonstrate accurate prediction of trial-specific deviations. Residual analysis (Figures 3F–3H and 3N–3P) shows minimal systematic error for whisker motion energy, with slight underestimation of extreme wheel speeds. Overall, RRR effectively decodes continuous behaviors by capturing both trial-averaged structure and trial-to-trial variability. 

## Learning latent behavioral dynamics across trials 

We next consider the behavioral data-sharing model, which learns latent behavioral states[→] _s_ to infer unknown behavior[→] _z_ (Equation 21) from neural activity _X_ , leveraging correlations across trials to improve single-session, single-trial decoder outputs[→] _d_ . Figure 4A illustrates latent state inference from a multi-session BMM-HMM applied to IBL binary decisions.[17] The stimulus probability switches among three states: right (R), left (L), and middle (M, stimulus randomly switching sides). These differ from the ‘‘engaged,’’ ‘‘disengaged,’’ and ‘‘biased’’ decision states described in Ashwood et al.[16] The model accurately infers these states using only single-trial decoder outputs, without prior knowledge of true choices or block timings (Figure 4B). Neural data from the decoded session alone is used to fit the model, while behavior from other sessions informs the multi-session model. 

When the single-trial decoder is accurate, the model can precisely infer states; when it makes errors, the model compensates by leveraging trial-to-trial correlations and behavioral patterns from other sessions. Figure 4C compares improved decoder outputs (Equation 21) from the multi-trial, multi-session BMM-HMM to baseline single-trial, single-session outputs. Baseline outputs 

**==> picture [46 x 35] intentionally omitted <==**

Neuron _114_ , 536–551, February 4, 2026 539 

**==> picture [76 x 35] intentionally omitted <==**

**ll** OPEN ACCESS 

**==> picture [47 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [481 x 305] intentionally omitted <==**

**----- Start of picture text -----**<br>
A PCA  B single-session RRR single-session RRR single-session RRR C effect size across sessions<br>(session 1) (session 2) (session 3) (session 4)<br>ARI<br>left trial  right trial<br>…<br>ARI: 0.06 ARI: 0.62 ARI: 0.75 ARI: 0.58 9% ↑<br>mul�-session RRR  mul�-session RRR  mul�-session RRR  mul�-session RRR  single-session RRR<br>(session 1) (session 2) (session 3) (session 4)<br>accuracy<br>…<br>ARI: 0.95 ARI: 0.67 ARI: 0.78 ARI: 0.71 2% ↑<br>D E single-session RRR<br>prior mul�-session RRR  ridge observed wheel speed<br>0.76 vs. 0.54 0.65 vs. 0.52<br>0.91 vs. 0.73<br>0.74 vs. 0.37 0.86 vs. 0.66<br>mo�on energy<br>0.55 vs. 0.51 0.70 vs. 0.56 0.60 vs. 0.55<br>0.80 vs. 0.52 0.51 vs. 0.51<br>mul�-session RRR<br>mul�-session RRR<br>**----- End of picture text -----**<br>


**Figure 2. The RRR achieves strong decoding performance by learning behaviorally relevant neural variations through multi-session learning** (A) Neural activity projected onto PCA and multi-session RRR subspace _U[i]_ , color coded by binary behavior. Light curves: single-trial projections; dark: trialaveraged projections. We apply _k_ -means (2 clusters) to separate projections in left and right trials, and use adjusted Rand index (ARI)[39][,][40] to quantify cluster similarity. Temporal basis _V_ is shown in Figure 7A. 

(B) Neural projections onto single- and multi-session RRR subspaces, color coded as in (A). _k_ -means and ARI measure left and right trial separation. 

(C) Scatterplot of ARI vs. decoding accuracy for multi- vs. single-session RRR across 10 sessions. Each point represents a session, and the green value shows the relative improvement of multi-session RRR over single-session RRR. 

(D) Decoded prior from multi-session RRR (purple) vs. ridge regression (green), compared with true prior (gray). Pearson correlation between the decoded and true prior is shown for each example. 

(E) Motion energy and wheel speed decoded by reduced-rank regression (purple) and ridge regression (green), with observed behavior shown in gray. 

are noisy and error-prone, while BMM-HMM outputs follow the smooth ‘‘block’’ structure by incorporating latent state knowledge. Quantitatively, the model achieves higher area under the curve (AUC) than the baseline, demonstrating the benefit of using trial-to-trial correlations and latent states. Decoder performance by block type is also shown, with baseline AUC in black and BMM-HMM in purple. 

We apply similar ideas to improve decoding of the continuous _prior_ , using the LG-AR1 model. This prior reflects a running estimate of stimulus-side probability[27] and changes smoothly over time. Like BMM-HMM, LG-AR1 infers the latent behavior (the unobserved prior) by exploiting trial-to-trial correlations in single-trial decoder outputs, borrowing information from other trials to correct errors. Figure 4D compares LG-AR1 outputs, _d_[~] _k_ (Equation 51), to baseline single-trial outputs, _dk_ . The baseline decoder struggles to track the prior, while LG-AR1 better aligns with the true prior, yielding higher Pearson correlation. Note that prior decoding is based on the full trial and may capture correlated variables such as reward or visual stimulus. 

We assess the impact of incorporating behavioral information from other sessions on BMM-HMM and LG-AR1 performance using three variants: _single-session_ , _multi-session_ , and _oracle_ , which uses true behaviors to learn parameters and improve decoder estimates (see STAR Methods). The oracle model assumes that the latent variable _zk_ is known and substitutes ground-truth behaviors _yk_ for _zk_ , but it still generates distinct outputs to avoid trivial decoding. It serves as an upper bound for measuring decoding performance. Figures 4E and 4F compare parameter estimates, showing that multi-session models align more closely with the oracle than single-session models. Figures 4G and 4H show that multi-session predictions better match the oracle outputs, highlighting the benefit of multi-session learning for parameter estimation and decoding accuracy. 

Benchmarking neural and behavioral data-sharing models with single- and multi-session baselines To measure decoding performance, we benchmark both single- and multi-session models. Single-session models include 

540 Neuron _114_ , 536–551, February 4, 2026 

**==> picture [491 x 416] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>Article OPEN ACCESS<br>A B C I J K<br>D L<br>E M<br>F N<br>G H O P<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**Figure 3. Qualitative evaluation of the RRR for decoding wheel speed and motion energy in a single IBL session** (A and I) Comparison of the RRR’s predicted whisker motion energy (A) and wheel speed (I) (dotted lines) with observed behavior (solid lines) across block conditions. For example, blue lines show the average predicted (dotted) and observed (solid) behavior for trials with a block value of 0.2. The gray vertical line indicates stimulus onset. 

(B, C, J, and K) Average predicted and observed whisker motion energy (B) and wheel speed (J) are shown by choice condition (right vs. left), and whisker motion energy (C) and wheel speed (K) are shown by reward outcome (rewarded vs. unrewarded). 

(D–F and L–N) Observed whisker motion energy (D) and wheel speed (L) from 96 example trials are displayed alongside model predictions (E and M) and residuals (F and N; observed minus predicted). Rows correspond to trials and columns to time steps. Both observed and predicted traces are mean-centered per trial to highlight variability and standardized for visualization. Spectral clustering group trials with similar patterns in the observed behavior. (G and O) Scatterplots of decoding performance for whisker motion energy (G) and wheel speed (O). Each point represents a single trial, comparing observed and predicted behaviors (trial-averaged subtracted) averaged across time steps. The diagonal line indicates perfect prediction, and predicted wheel speed often underestimates actual values. 

(H and P) Residual distributions over time indicate that whisker motion energy errors (H) are centered around zero, whereas wheel speed residuals (P) show systematic deviations, particularly at high speeds, suggesting some model bias. 

L2-regularized linear decoders; multi-layer perceptron (MLP) decoders[2] ; and single-session RRR, BMM-HMM, and LG-AR1. Multi-session models include RRR (M), RRR (MR), multi-session BMM-HMM, LG-AR1, and a ‘‘combined’’ decoder that refines initial RRR (M) predictions with multi-session BMM-HMM or LG-AR1. See STAR Methods for hyperparameters and model architectures. 

We decode choice, prior, wheel speed, and whisker motion energy using neural activity from five brain regions in the reproducible electrophysiology (RE) datasets[17] : posterior thalamic 

nucleus ( _PO_ ), lateral posterior nucleus ( _LP_ ), dentate gyrus ( _DG_ ), cornu ammonis ( _CA1_ ), and anterior visual cortex ( _VISa_ ). These regions were selected for high neuron yield and anatomical diversity. To avoid ceiling effects from using all regions, we decode each region separately, yielding more moderate, distinguishable performance across models. 

For choice decoding (Figure 5A), single-session RRR outperforms all other single-session baselines, including the MLP, which may not reach optimal performance despite hyperparameter tuning. RRR (M) further improves performance, with 

Neuron _114_ , 536–551, February 4, 2026 541 

**==> picture [76 x 35] intentionally omitted <==**

**==> picture [63 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>OPEN ACCESS<br>**----- End of picture text -----**<br>


**==> picture [47 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [481 x 417] intentionally omitted <==**

**----- Start of picture text -----**<br>
A neural activity  observed decoder output inferred behavioral state<br>decoder BMM-HMM<br>B<br>C<br>M: 0.51 vs. 0.56    L: 0.64 vs. 0.70    R: 0.69 vs. 0.89<br>D<br>E estimated transition prob. estimated emission prob. F oracle single-session multi-session<br>0.930 0.972<br>0.2290.275 0.255<br>0.149<br>0.015<br>0.003 0.012<br>G oracle single-session multi-session AUC: 0.72 vs. 0.66 vs. 0.79 H corr: 0.65 vs. 0.05 vs. 0.34<br>prob(R)<br>0       0.5     1<br>prior0           1<br>prior<br>prob(R)<br>**----- End of picture text -----**<br>


**Figure 4. The behavioral data-sharing model improves single-trial decoding by inferring latent behavioral states from trial-to-trial correlations within individual sessions and sharing behavioral information across sessions** 

(A) Schematic of BMM-HMM latent state inference. A single-trial decoder maps neural activity _Xk_ to outputs _dk_ , which the BMM-HMM uses to infer latent states _sk_ (left [L], right [R], and a random ‘‘middle’’ switching state [M]), producing improved decoder predictions. 

(B) Estimated latent states _sk_ show block structures switching between L, R, and M, mirroring the true block probabilities in the IBL task. These states are learned, not pre-defined, and their names are assigned post hoc. Color bar shows state probabilities; observed choices are green (right) and blue (left). → (C) Multi-trial, multi-session BMM-HMM decoder outputs _P zk_ = 1 _d_ (purple) overlaid on baseline single-trial outputs _dk_ (black), exploiting trial-to-trial cor( ⃒⃒⃒ ) relations for higher AUC. Performance is shown separately for M, L, and R blocks. Multi-session refers to borrowing behavioral information from multiple training sessions to improve neural state estimates in the test session. _dk_ is observed and _zk_ is latent. 

(D) Multi-trial, multi-session LG-AR1 outputs _d_[~] _k_ (purple) over baseline _dk_ and true prior (pink), achieving higher Pearson correlation. 

(E) Estimated transition and emission probabilities from oracle (pink), single-session (black), and multi-session (purple) BMM-HMM models. 

- (F) Parameter estimates from oracle, single-session, and multi-session LG-AR1: _ρ_ (AR autocorrelation), _θ_ and _μ_ (linear coefficient of Gaussian observation model); see STAR Methods section ‘‘LG-AR1: model details.’’ 

- (G) Decoded probabilities of choosing right from oracle (pink), single-session (black), and multi-session (purple) BMM-HMM models. 

- (H) Decoded priors from oracle (pink), single-session (black), and multi-session (purple) LG-AR1 models. 

(RRR (MR) providing a slight additional gain. The combined decoder achieves the highest performance across most regions. BMM-HMM models outperform linear baselines but show smaller gains than RRR. 

For prior decoding (Figure 5B), LG-AR1 models match or exceed the improvements of RRR. Single-session RRR outperforms other single-session baselines but lags behind RRR (M), with RRR (MR) slightly below the multi-session 

542 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

Article 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [428 x 601] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>C<br>D<br>E F<br>G<br>**----- End of picture text -----**<br>


_(legend on next page)_ 

Neuron _114_ , 536–551, February 4, 2026 543 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

variant. The combined decoder, integrating multi-session RRR and LG-AR1, achieves the highest performance. For wheel speed and whisker motion energy (Figures 5C and 5D), single-session RRR outperforms linear baselines and matches MLP decoders, while RRR (M) achieves the best overall performance and RRR (MR) performs slightly worse. 

Multi-session models consistently outperform single-session models, raising the following question: are the gains due to the RRR’s ability to capture shared temporal patterns or simply more training data? To test this, we compare RRR (M) with two multi-session baselines: full-rank linear and MLP decoders. For multi-session baselines, we employ session-specific linear read-in layers to project neural activity from sessions with varying neuron counts into a common latent space before feeding it into the linear or MLP backbone (Figure 5E). Figure 5F shows that RRR (M) outperforms the linear baseline for choice and prior; the results of the linear model are excluded for wheel speed and whisker motion energy owing to poor performance. Figure 5G shows that RRR (M) also outperforms multi-session MLP for choice, wheel speed, and whisker motion energy and matches it for prior. These results indicate that the performance improvement achieved by RRR arises from both multi-session training and its structured model design. 

## Identifying important neurons for decoding 

The RRR not only improves decoding but also provides intrinsic interpretability. Specifically, the neural basis _U_ quantifies each neuron’s contribution to decoding (see Equation 12). We validate this with a ‘‘neuron pruning’’ experiment, where the magnitude of _U_ ’s first rank reflects neuron importance. Starting with all neurons, we iteratively remove 5% per session, refit an L2-regularized logistic regression, and track AUC. We compare three strategies: removing least important neurons first, most important first, and random removal. Figures 6A–6E show that pruning least important neurons minimally affects decoding, while removing the most important ones causes a faster performance drop than random removal. Accurate decoding can still be achieved with only a small proportion of important neurons (green curves in Figures 6A–6E). Figures 6F–6J show trial-averaged activity of the most and least important neurons identified by _U_ in example sessions. The most important neurons display choice-selective firing patterns, whereas the least important ones show similar activity across left and right trials, indicating limited task responsiveness. 

## Mapping behaviorally relevant timescales across the brain 

Prior studies show that functionally distinct brain regions exhibit varying intrinsic timescales,[24–26] with motor and sensory areas operating faster than cognition-related regions. Yet, how these dynamics relate to behavior remains largely unexplored. To investigate, we fit the RRR (MR) on 433 sessions across 270 brain areas to decode choice and prior and use the first rank of the region-specific temporal basis _V[j]_ as each region’s timescale. Figure 7A shows distinct activation timescales across regions, including the gigantocellular reticular nucleus (GRN), motor cortex (MOp), nucleus accumbens (ACB), amygdala complex (CEA), CA1 in the hippocampus, basomedial amygdala (BMA), and VISa. Peak activation ( _peak_ ) is the highest point of the curve, and activation duration ( _width_ ) is the interval spanning 90% of the peak height. Although peak activation occurs at similar times following stimulus onset, ACB and BMA exhibit more prolonged activation, compared with other regions. 

We use each area’s peak activation time and duration (Figure 7A) to compare behaviorally relevant timescales. For choice decoding, most regions peak within 1.5 s of stimulus onset, consistent with the ‘‘reaction time’’ (stimulus onset to initial movement; see Figure 1C in IBL et al.[18] ). Figure 7B (top row) shows broadly similar peak times, except for the olfactory bulb and cerebellum, which may activate later upon receiving water reward. Figure 7C (top row) shows shorter activation durations in hindbrain regions, compared with forebrain and midbrain. For prior decoding, Figure 7B (bottom row) shows earlier cortical activation and delayed cerebellar activation, while Figure 7C (bottom row) shows longer activation durations in cortex and thalamus. White areas mark regions excluded from decoding because of missing behavioral data. 

In addition to showing activation timing and duration (Figures 7B and 7C), we analyze how much behavioral information is decodable from each region. While IBL et al.[18] map decoding accuracy using L2-regularized linear decoders, Figure 7D shows that the RRR (MR), a more constrained and interpretable linear decoder trained with more data, improves choice and prior decoding across most regions. This suggests that regularized linear decoders may not fully capture decision-related information in each region, potentially affecting interpretations based on them. 

In the STAR Methods, we confirm that the RRR (MR) improves information decoding from each region relative to the baseline linear decoder. To control for spurious correlations,[41] we generate null distributions using ‘‘imposter sessions.[18] ’’ Analysis of representative regions (PO, LP, DG, CA1, and VISa) in 

**Figure 5. Quantitative comparison of the proposed neural and behavioral data-sharing models against single- and multi-session baselines** (A–D) Decoding performance for choice (A), prior (B), wheel speed (C), and whisker motion energy (D), using neural activity from 5 brain regions across 10 IBL sessions. Bar plots show mean metrics; boxplots show median, quartiles, min, and max. For wheel speed and whisker motion energy, _R_[2] quantifies single-trial decoding accuracy. The multi-region RRR is labeled ‘‘RRR (MR).’’ For the combined model, estimates from multi-session RRR (RRR (M)) are further refined using multi-session BMM-HMM or LG-AR1 (BMMHMM/LGAR1 (M)). Percent improvement over the linear baseline is shown at the bottom of the panel; the combined model is not benchmarked for wheel speed or whisker motion energy, as BMM-HMM and LG-AR1 have not been applied to continuous vectorvalued behaviors. 

(E) Multi-session linear (full-rank) and MLP models serve as baselines. To accommodate sessions with different neuron counts, session-specific linear read-in matrices project activity to a common latent space before feeding the full-rank or MLP backbone. (F and G) Scatterplots compare RRR (M) to multi-session linear (F) and MLP (G) models across 30 sessions; each dot is a session. Green (or gray) values show relative improvement of RRR (M) over the multi-session baseline. Metrics for wheel speed and whisker motion energy are omitted for the linear baseline owing to poor performance. 

544 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [481 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
A PO B LP C DG D CA1 E VISa<br>most important<br>random<br>least important<br>F % neuron removed G % neuron removed H % neuron removed I % neuron removed J % neuron removed<br>most important most important most important most important most important<br>least important least important least important least important least important<br>�me (s) �me (s) �me (s) �me (s) �me (s)<br>**----- End of picture text -----**<br>


**Figure 6. RRRs identify important neurons for decoding choice in brain regions including PO, LP, DG, CA1, and VISa** (A–E) For brain regions PO (A), LP (B), DG (C), CA1 (D), and VISa (E), we show region-specific performance loss from the neuron pruning experiment using three removal strategies. Decoding accuracy (AUC) is averaged across 10 sessions per region. (F–J) Trial-averaged neural activity conditioned on choice for the most and least important choice-decoding neurons is shown for PO (F), LP (G), DG (H), CA1 (I), and VISa (J). Blue and black curves indicate mean spiking for left and right trials, with shaded ribbons showing ± 1 standard deviation. Stimulus onset is marked by a vertical dashed line. 

Figure S4 shows that while absolute decoding improvements differ slightly between original and adjusted scores, the relative ranking of regional improvements remains consistent. 

## Generalization across data structures, species, and behavior tasks 

In the previous sections, we focus on IBL trial-aligned Neuropixels recordings of mice performing visual decision-making tasks. To demonstrate the generalizability of our models across diverse data structures, species, and behavior tasks, we further applied them to three datasets: (1) IBL trial-unaligned data including both task-related (structured) and spontaneous neural activity; (2) the Allen Institute Neuropixels visual coding dataset, where mice are exposed to visual stimuli[19] distinct from IBL tasks; and (3) a primate random target-reaching task with self-paced, sequential movements and no repeated trials.[20] 

In earlier experiments, we segment recordings into 2-s trials aligned to task cues such as stimulus or movement onset. To test our methods on data without clear trial structure, we apply them to IBL trial-unaligned data, using 2-s snippets sampled both within and outside trials (Figure 8A). These snippets capture freely behaving periods without alignment to task events. We decode two continuous behaviors, wheel speed and whisker motion energy, comparing against ridge regression (linear regression), single-session reduced-rank regression, a single-session MLP, and our RRR (M). In Figure 8B, single-session reducedrank regression outperforms the linear baseline and matches the nonlinear MLP, while the multi-session model provides modest but consistent gains. Predicted behaviors in Figure 8C further show that the RRR (M) more closely tracks ground truth, reflecting improved decoding accuracy. 

To test generalizability across tasks, we apply our models to the Allen Institute visual coding dataset, which includes Neuropixels recordings from mouse visual cortex and thalamus during presentation of Gabors and static gratings (Figure 8D). This creates a multi-class classification task (three Gabor orientations and six grating orientations), alongside decoding of running 

speed, a continuous trial-unaligned variable spanning both stimulus and free-behavior periods. We compare performance with L2-regularized linear models, single-session RRR, a single-session MLP, and our RRR (M). In Figure 8E, single-session RRR outperforms the linear and MLP baselines, while the multi-session version yields modest further gains. Low-dimensional projections onto the reduced-rank subspace (Figure 8G) reveal clear separation of stimulus conditions, demonstrating that the model captures behaviorally relevant neural variation. Figure 8H compares predicted and actual running speed, showing that both single- and multi-session RRRs decode this trial-unaligned behavior accurately. 

The BMM-HMM infers latent internal states underlying observed behavioral outcomes, such as when a mouse perceives a stimulus and makes a decision. Since Gabors and gratings are stimuli rather than responses, BMM-HMM is less suitable here. Instead, we apply it to a ‘‘choice’’-related variable, _licks_ , the mouse’s response to visual stimulus changes. When the visual stimulus changes, the mouse is expected to respond with a lick, which is rewarded if correct. Mice, however, often produce consecutive licks to increase reward probability.[19] Figure 8I shows that BMM-HMM identifies distinct engaged and disengaged states: in the engaged state, licking is consistent, while in the disengaged state, it is infrequent. By capturing trial-to-trial correlations through latent states, BMM-HMM improves decoding over the linear baseline (Figure 8F). See STAR Methods section data processing and Figure S6 for data preprocessing details and additional examples. 

To test generalization across recording hardware and species, we also apply our method to a monkey random targetreaching task.[20] In this self-paced, sequential reaching task, the monkey moves between random grid elements (Figure 8J). The dataset includes single-session spiking activity from primary motor cortex recorded with Utah arrays, along with finger positions. We decode finger velocity and compare a single-session RRR against ridge regression and a single-session MLP, using 5-fold cross-validation. In Figure 8K, RRR outperforms 

Neuron _114_ , 536–551, February 4, 2026 545 

Article 

## **ll** 

OPEN ACCESS 

**==> picture [481 x 334] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>�me (s) �me (s) �me (s) �me (s)<br>B   peak (ms; rela�ve to s�mulus onset) C   width (ms) D % increase in accuracy<br>200                   250                  750 400                   1200                  2000 0                       5                       25<br>choice choice choice<br> not decoded<br>  peak (ms; rela�ve to s�mulus onset)   width (ms) % increase in correla�on<br>-550                   -350                  -200 50                   200                  450 0                     25                    150<br>prior prior prior<br>GRN ACB CA1 BMA<br>MOp CEA DG VISa<br>**----- End of picture text -----**<br>


**Figure 7. Mapping behaviorally relevant timescales and decoding quality improvement across the brain** 

(A) First rank of each region’s temporal basis _V[j]_ in the multi-region RRR model (Equation 4). The dashed line shows stimulus onset, the red cross indicates peak activation time (peak), and the yellow segment represents activation duration (width is defined as the interval covering 90% of the peak height). (B) Brain-wide map of relative peak activation times with respect to stimulus onset. 

(C) Brain-wide map of activation duration (width). Colors indicate choice (yellow) vs. prior (purple); intensity shows peak time or duration values. White: nondecoded regions. 

(D) Region-specific improvements in choice decoding accuracy and prior decoding correlation relative to L2-regularized linear baseline. Color intensity shows improvement magnitude. 

ridge regression but falls short of the nonlinear MLP. Figure 8L plots predicted vs. true finger velocity along the _x_ and _y_ axes. Although RRR does not always outperform nonlinear baselines, it provides clear improvements over the linear model. Importantly, decoding accuracy is not the only objective, as RRR also offers interpretability advantages over deep learningbased multi-session models. 

## DISCUSSION 

We introduce multi-session reduced-rank regression and statespace models that share neural and behavioral structure across sessions to improve decoding. Applied to large multi-region datasets, our models enhance decoding of several behavioral variables. Beyond performance, the approach is interpretable; it highlights task-relevant neurons, reveals behaviorally relevant timescales, and infers latent behavioral states. While extensible to nonlinear models, we focus here on an efficient, interpretable 

linear decoder that replaces full-rank regression and supports multi-session training. The reduced-rank structure offers clear interpretability through neural and temporal bases _U_ and _V_ , and it often matches or exceeds simple nonlinear MLPs, particularly when computational resources are limited. 

Our neural data-sharing model relates to several existing approaches.[42–47] Unlike prior work[3] that uses canonical correlation analysis (CCA) to align latent dynamics by maximizing neural and behavioral correlation, we replace CCA with reducedrank regression optimized for decoding accuracy. Compared to demixed PCA,[38] which prioritizes neural variability for reconstruction, our model emphasizes behavioral variation. Similarly, while preferential subspace identification (PSID)[37] extracts behaviorally relevant dynamics with state-space models, our reduced-rank regression provides a simpler latent-variable formulation without neural dynamics constraints. Finally, the factorization of the weight matrix into low-rank _U_ and _V_ resembles tensor component analysis[48][,][49] and tensor regression,[50][,][51] 

546 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [481 x 481] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>Unaligned  = Trial + Non-Trial      Wheel Speed                        Whisker Motion Energy<br>R2: 0.24 R2: 0.55<br>R2: 0.49 R2: 0.75<br>R2: 0.52 R2: 0.75<br>R2: 0.55 R2: 0.80<br>D E F Lick<br>Accuracy  ↑<br>Gabors Static Gratings<br>Linear<br>G Gabors Static Gratings H Running Speed I 0  No lick   1  Lick         — Linear    Accuracy: 0.71 — BMM-HMM<br>Orientation:  0 90 Orientation:  0 90 R2: 0.36<br>R2: 0.55<br>    Accuracy: 0.90<br>R2: 0.52<br>Prob.<br>1.0<br>R2: 0.69 0.5<br>0<br> 0             20          Trial          50           70<br>J K L<br>X Velocity        Y Velocity<br>R2: 0.01       X Velocity                                       Y VelocityR2: 0.44<br>R2: 0.36 R2: 0.56<br>R2: 0.16 R2: 0.71<br>Rank 2<br>Rank 1 Rank 2 Rank 1<br>BMMHMM<br>Rank 3<br>**----- End of picture text -----**<br>


**Figure 8. Generalization across data structures, species, and behavior tasks** 

(A) The IBL trial-unaligned dataset includes recording snippets both within and outside structured experimental trials. 

(B) Comparison of single-session (RRR) and multi-session RRR (RRR (M)) with linear and MLP baselines across 10 IBL sessions. RRR (M) is trained on 50 sessions. Bar plots show the mean decoding metric, and boxplots show the median, interquartile range, and full range. 

(C) Predicted wheel speed and whisker motion energy from an example session. RRR (M) aligns more closely with ground truth. 

(D) The Allen Institute visual coding dataset includes Neuropixels recordings from mice exposed to different visual stimuli. 

(E) Decoding performance across 10 Allen sessions, comparing single- and RRR (M) to baseline models. RRR (M) is trained on 58 Allen sessions. Bar plots show the mean decoding metric, while box plots show the median, quartiles, minimum, and maximum. 

(F) BMM-HMM vs. linear baseline predicting licks to visual stimulus changes across seven sessions. Each dot shows a session’s decoding accuracy. 

(G) Neural activity projected onto RRR latent space, color coded by stimulus orientation (two orientations shown) for Gabors and static gratings. 

- (H) Predicted running speed from an example session vs. ground truth; RRR (M) captures behavior more accurately. 

- (I) Side-by-side comparison of predicted and observed licks (BMM-HMM vs. linear baseline) with latent state probabilities shown as a heatmap. 

_(legend continued on next page)_ 

Neuron _114_ , 536–551, February 4, 2026 547 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

reflecting the shared goal of reducing overfitting and improving generalization through low-rank structure. 

Prior work has used HMMs to infer latent behavioral states from movement or decision-making data.[52][,][53] For example, Ashwood et al.[16] model mouse decisions using GLM-HMMs, which allow states to persist across trials and depend on stimuli and covariates. Unlike these behavior-only approaches, we also incorporate neural data. Other studies have applied HMMs to explain neural activity directly,[54–58] whereas we infer states that generate decoder estimates combining neural and behavioral information. Related work such as BehaveNet[59] integrates behavioral video data with autoregressive HMMs to smooth predictions. Our focus is on exploiting trial-to-trial correlations in IBL data, but similar history dependence is common across neuroscience experiments.[16][,][60][,][61] Incorporating task and behavioral history is therefore valuable not only for improving decoding but also for understanding learning and memory mechanisms. 

Technological advances now allow for the simultaneous collection of multiple data modalities, such as local field potentials and calcium imaging, in neuroscience experiments. RRRs extend beyond neural decoding to tasks like neural encoding[21][,][38][,][62] and inter-region activity prediction.[63] Future directions include incorporating additional data modalities, expanding the model to new tasks, and relaxing the assumption of shared temporal bases across sessions, which may not hold when animals are at different learning stages or performance levels. For multisession state-space models, nonlinear time series and dynamical systems[64–66] could better capture complex latent behavioral dynamics. Finally, all models are compatible with density-based decoding,[67] enabling decoding from unsorted spike features, which may further improve accuracy. 

## RESOURCE AVAILABILITY 

## Lead contact 

Requests for further information and resources should be directed to and will be fulfilled by the lead contact, Yizi Zhang (yz4123@columbia.edu). 

## Materials availability 

This study did not generate new reagents. 

## Data and code availability 

- Code to download the neural and behavioral data for reproducing this study is publicly available at https://docs.internationalbrainlab.org/ index.html as of the publication date. 

- All original code is publicly available at https://github.com/yzhang511/ neural_decoding with the DOI https://doi.org/10.5281/zenodo.1731 7498. 

- Additional information for analysis is available from the lead contact upon request. 

Simons Foundation, and the National Science Foundation and DoD OUSD (R&E) under Cooperative Agreement PHY-2229929 (The NSF AI Institute for Artificial and Natural Intelligence). We thank Matt Whiteway for many useful discussions, Peter Latham and Jonathan Pillow for helpful comments on the manuscript, and Chris Langfield for code review. 

## AUTHOR CONTRIBUTIONS 

Conceptualization, Y.Z., H.L., and L.P.; methodology, Y.Z., H.L., and L.P.; investigation, Y.Z., H.L., C.H., S.W., C.F., F.H., Y.W., A.P., E.V., and L.P.; writing – original draft, Y.Z. and H.L.; writing – review & editing, Y.Z., H.L., C.H., S.W., C.F., F.H., A.P., E.V., and L.P.; funding acquisition, L.P.; resources, L.P.; and supervision, C.H., E.V., and L.P. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

## DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES IN THE WRITING PROCESS 

ChatGPT was used for grammar correction, generating some plotting code, and documenting code. All AI-generated code was verified by the researchers. 

## STAR★METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

|•|KEY RESOURCES TABLE|||
|---|---|---|---|
|•|METHOD DETAILS|||
||○Closed-form solution for reduced-rank regression model|||
||○Derivation of V_=_G_−1_H_in Equation 8|||
||○Derivation of U_=_argminUTr_[ _U_⊤_StU_<br>(<br>)−1 _U_⊤_SbU_<br>(|)<br>1<br>2]in Equation 10||
||○Connection to PCA, CCA, demixed PCA and sliced TCA|||
||○BMM-HMM: Model details|||
||○EM algorithm for BMM-HMM|||
||○Oracle BMM-HMM|||
||○Learning empirical priors of state-space model parameters|||
||○Multi-session BMM-HMM|||
||○LG-AR1: Model details|||
|•|QUANTIFICATION AND STATISTICAL ANALYSIS|||
||○Data processing|||
||○Hyperparameter selection|||
||○Recording<br>hardwares,<br>task<br>structures<br>and||implementation|
||guidelines|||
||○Computation time comparison|||
||○Assessing statistical signifcance of decoding improvements via|||
||bootstrap resampling|||
||○Decoding frequency components of behavior|||
||○Assessing statistical signifcance of decoding improvements via null|||
||distribution|||
||○Relationship between LG-AR1 and post-hoc smoother, and across-|||
||session variability in BMM-HMM/LG-AR1 outputs|||
||○Scaling curves for multi-session reduced-rank|regression models||



## ACKNOWLEDGMENTS 

## SUPPLEMENTAL INFORMATION 

This work was funded by grants from the Wellcome Trust (209558 and 216324), the National Institutes of Health (1U19NS123716 and K99MH128772), the 

Supplemental information can be found online at https://doi.org/10.1016/j. neuron.2025.10.026. 

(J) Neural activity recorded via Utah arrays during a monkey random target-reaching task. 

(K) Decoding finger velocity ( _x_ and _y_ axes) with linear, MLP, and RRR models within a session via 5-fold cross-validation. Bar plots show the mean _R_[2] , while boxplots show the median, quartiles, min, and max. 

(L) Predicted finger velocities (along _x_ and _y_ axes) compared with true recorded velocities. 

548 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

Received: October 11, 2024 Revised: July 3, 2025 Accepted: October 22, 2025 Published: November 26, 2025 

## REFERENCES 

1. Paninski, L., Pillow, J., and Lewi, J. (2007). Statistical models for neural encoding, decoding, and optimal stimulus design. Prog. Brain Res. _165_ , 493–507. https://doi.org/10.1016/S0079-6123(06)65031-0. 

2. Glaser, J.I., Benjamin, A.S., Chowdhury, R.H., Perich, M.G., Miller, L.E., and Kording, K.P. (2020). Machine learning for neural decoding. eNeuro _7_ . ENEURO.0506-19.2020. https://doi.org/10.1523/ENEURO.0506-19.2020. 

3. Gallego, J.A., Perich, M.G., Naufel, S.N., Ethier, C., Solla, S.A., and Miller, L.E. (2018). Cortical population activity within a preserved neural manifold underlies multiple motor behaviors. Nat. Commun. _9_ , 4233. https://doi. org/10.1038/s41467-018-06560-z. 

4. Melbaum, S., Russo, E., Eriksson, D., Schneider, A., Durstewitz, D., Brox, T., and Diester, I. (2022). Conserved structures of neural activity in sensorimotor cortex of freely moving rats allow cross-subject decoding. Nat. Commun. _13_ , 7420. https://doi.org/10.1038/s41467-022-35115-6. 

5. Pellegrino, A., Cayco Gajic, N.A., and Chadwick, A. (2023). Low tensor rank learning of neural dynamics. Adv. Neural Inf. Process. Syst. _36_ , 11674– 11702. https://doi.org/10.5555/3666122.3666635. 

6. Safaie, M., Chang, J.C., Park, J., Miller, L.E., Dudman, J.T., Perich, M.G., and Gallego, J.A. (2023). Preserved neural dynamics across animals performing similar behaviour. Nature _623_ , 765–771. https://doi.org/10.1038/ s41586-023-06714-0. 

7. Herrero-Vidal, P., Rinberg, D., and Savin, C. (2021). Across-animal odor decoding by probabilistic manifold alignment. Adv. Neural Inf. Process. Syst. _34_ , 20360–20372. https://doi.org/10.1109/NeurIPS2021.00001. 

8. Schneider, S., Lee, J.H., and Mathis, M.W. (2023). Learnable latent embeddings for joint behavioural and neural analysis. Nature _617_ , 360–368. https://doi.org/10.1038/s41586-023-06031-6. 

9. Chen, C.S., Ebitz, R.B., Bindas, S.R., Redish, A.D., Hayden, B.Y., and Grissom, N.M. (2021). Divergent strategies for learning in males and females. Curr. Biol. _31_ , 39–50.e4. https://doi.org/10.1016/j.cub.2020.09.075. 

10. Turaga, S., Buesing, L., Packer, A.M., Dalgleish, H., Pettit, N., Hausser, M., and Macke, J.H. (2013). Inferring neural population dynamics from multiple partial recordings of the same neural circuit. In Advances in Neural Information Processing Systems 26 (NIPS 2013). https://doi.org/10.11 09/NeurIPS2013.00001. 

11. Pandarinath, C., O’Shea, D.J., Collins, J., Jozefowicz, R., Stavisky, S.D., Kao, J.C., Trautmann, E.M., Kaufman, M.T., Ryu, S.I., Hochberg, L.R., et al. (2018). Inferring single-trial neural population dynamics using sequential auto-encoders. Nat. Methods _15_ , 805–815. https://doi.org/10.1038/ s41592-018-0109-9. 

12. Ye, J., Collinger, J., Wehbe, L., and Gaunt, R. (2023). Neural data transformer 2: multi-context pretraining for neural spiking activity. Adv. Neural Inf. Process. Syst. _36_ , 80352–80374. https://doi.org/10.1101/2023.09.18. 558113. 

13. Zhang, Y., Wang, Y., Jime´ nez-Beneto´ , D.M., Wang, Z., Azabou, M., Richards, B., Tung, R., Winter, O., International Brain Laboratory, Dyer, E., and et al.. (2024). Towards a ‘‘universal translator’’ for neural dynamics at single-cell, single-spike resolution. Preprint at arXiv. https://doi.org/10. 48550/arXiv.2407.14668. 

14. Azabou, M., Arora, V., Ganesh, V., Mao, X., Nachimuthu, S., Mendelson, M., Richards, B., Perich, M., Lajoie, G., and Dyer, E. (2023). A unified, scalable framework for neural population decoding. Preprint at arXiv. https:// doi.org/10.48550/arXiv.2310.16046. 

15. Zhang, Y., Wang, Y., Azabou, M., Andre, A., Wang, Z., Lyu, H., International; Brain Laboratory, Dyer, E., Paninski, L., and Hurwitz, C. (2025). Neural encoding and decoding at scale. Preprint at arXiv. https:// doi.org/10.48550/arXiv.2504.08201. 

16. Ashwood, Z.C., Roy, N.A., Stone, I.R., International; Brain Laboratory, Urai, A.E., Churchland, A.K., Pouget, A., and Pillow, J.W. (2022). Mice alternate between discrete strategies during perceptual decision-making. Nat. Neurosci. _25_ , 201–212. https://doi.org/10.1038/s41593-021-01007-z. 

17. Banga, K., Benson, J., Bhagat, J., Biderman, D., Birman, D., Bonacchi, N., Bruijns, S.A., Buchanan, K., Campbell, R.A., Carandini, M., et al. (2025). Reproducibility of in vivo electrophysiological measurements in mice. eLife _13_ , RP100840. https://doi.org/10.7554/eLife.100840.3. 

18. International Brain Laboratory, Angelaki, D., Benson, B., Benson, J., Birman, D., Bonacchi, N., Bougrova, K., Bruijns, S.A., Carandini, M., Catarino, J.A., and et al.. (2025). A brain-wide map of neural activity during complex behaviour. Nature _645_ , 177–191. https://doi.org/10.1038/s415 86-025-09235-0. 

19. de Vries, S.E., Siegle, J.H., and Koch, C. (2023). Sharing neurophysiology data from the allen brain observatory. eLife _12_ , e85550. https://doi.org/10. 7554/eLife.85550. 

20. Pei, F., Ye, J., Zoltowski, D., Wu, A., Chowdhury, R.H., Sohn, H., O’Doherty, J.E., Shenoy, K.V., Kaufman, M.T., Churchland, M., et al. (2021). Neural latents benchmark’21: Evaluating latent variable models of neural population activity. Preprint at arXiv. https://doi.org/10.48550/ arXiv.2109.04463. 

21. Posani, L., Wang, S., Muscinelli, S.P., Paninski, L., and Fusi, S. (2025). Rarely categorical, always high-dimensional: how the neural code changes along the cortical hierarchy. Preprint at bioRxiv. https://doi.org/ 10.1101/2024.11.15.623878. 

22. Haxby, J.V., Guntupalli, J.S., Nastase, S.A., and Feilong, M. (2020). Hyperalignment: Modeling shared information encoded in idiosyncratic cortical topographies. eLife _9_ , e56601. https://doi.org/10.7554/eLife.56601. 

23. Busch, E.L., Slipski, L., Feilong, M., Guntupalli, J.S., di Oleggio Castello, M.V., Huckins, J.F., Nastase, S.A., Gobbini, M.I., Wager, T.D., and Haxby, J.V. (2021). Hybrid hyperalignment: A single high-dimensional model of shared information embedded in cortical patterns of response and functional connectivity. NeuroImage _233_ , 117975. https://doi.org/10. 1016/j.neuroimage.2021.117975. 

24. Kiebel, S.J., Daunizeau, J., and Friston, K.J. (2008). A hierarchy of timescales and the brain. PLoS Comp. Biol. _4_ , e1000209. https://doi.org/10. 1371/journal.pcbi.1000209. 

25. Scott, B.B., Constantinople, C.M., Akrami, A., Hanks, T.D., Brody, C.D., and Tank, D.W. (2017). Fronto-parietal cortical circuits encode accumulated evidence with a diversity of timescales. Neuron _95_ , 385–398.e5. https://doi.org/10.1016/j.neuron.2017.06.013. 

26. Zeraati, R., Shi, Y.L., Steinmetz, N.A., Gieselmann, M.A., Thiele, A., Moore, T., Levina, A., and Engel, T.A. (2023). Intrinsic timescales in the visual cortex change with selective attention and reflect spatial connectivity. Nat. Commun. _14_ , 1858. https://doi.org/10.1038/s41467-023-37613-7. 

27. Findling, C., Hubert, F., International Brain Laboratory, Acerbi, L., Benson, B., Benson, J., Birman, D., Bonacchi, N., Buchanan, E.K., Bruijns, S., and et al.. (2025). Brain-wide representations of prior information in mouse decision-making. Nature _645_ , 192–200. https://doi.org/10.1038/s41586025-09226-1. 

28. Welch, G., and Bishop, G. (1995). An Introduction to the Kalman Filter (Chapel Hill). 

29. Deely, J.J., and Lindley, D.V. (1981). Bayes empirical bayes. J. Am. Stat. Assoc. _76_ , 833–841. https://doi.org/10.1080/01621459.1981.10477731. 

30. Robbins, H.E. (1992). An empirical bayes approach to statistics. In Breakthroughs in Statistics, S. Kotz and N.L. Johnson, eds. (Springer), pp. 388–394. https://doi.org/10.1007/978-1-4612-0919-5_26. 

31. Efron, B. (1996). Empirical bayes methods for combining likelihoods. J. Am. Stat. Assoc. _91_ , 538–550. https://doi.org/10.1080/01621459.1996. 10476919. 

32. Allenby, G.M., and Rossi, P.E. (2006). Hierarchical bayes models. In The Handbook of Marketing Research: Uses, Misuses, and Future Advances (Sage), pp. 418–440. https://doi.org/10.4135/9781412973380.n20. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron _114_ , 536–551, February 4, 2026 549 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

33. Kruschke, J.K., and Vanpaemel, W. (2015). Bayesian Estimation in Hierarchical Models (Oxford University Press). https://doi.org/10.1093/oxfordhb/9780199957996.013.13. 

34. International Brain Laboratory, Birman, D., Bonacchi, N., Buchanan, K., Chapuis, G., Huntenburg, J., Meijer, G., Paninski, L., Schartner, M., Svoboda, K., et al. (2022). Video Hardware and Software for the International Brain Laboratory. Figshare. https://doi.org/10.6084/m9. figshare.19694452. 

35. Abdi, H., and Williams, L.J. (2010). Principal component analysis. WIREs Computational Stats. _2_ , 433–459. https://doi.org/10.1002/wics.101. 

36. Cunningham, J.P., and Yu, B.M. (2014). Dimensionality reduction for largescale neural recordings. Nat. Neurosci. _17_ , 1500–1509. https://doi.org/10. 1038/nn.3776. 

37. Sani, O.G., Abbaspourazad, H., Wong, Y.T., Pesaran, B., and Shanechi, M.M. (2021). Modeling behaviorally relevant neural dynamics enabled by preferential subspace identification. Nat. Neurosci. _24_ , 140–149. https:// doi.org/10.1038/s41593-020-00733-0. 

38. Kobak, D., Brendel, W., Constantinidis, C., Feierstein, C.E., Kepecs, A., Mainen, Z.F., Qi, X.L., Romo, R., Uchida, N., and Machens, C.K. (2016). Demixed principal component analysis of neural population data. eLife _5_ , e10989. https://doi.org/10.7554/eLife.10989. 

39. Hubert, L., and Arabie, P. (1985). Comparing partitions. J. Classif. _2_ , 193–218. https://doi.org/10.1007/BF01908075. 

40. Steinley, D. (2004). Properties of the hubert-arable adjusted rand index. Psychol. Methods _9_ , 386–396. https://doi.org/10.1037/1082-989X.9.3.386. 

41. Harris, K.D. (2020). Nonsense correlations in neuroscience. Preprint at bioRxiv. https://doi.org/10.1101/2020.11.29.402719. 

42. Mante, V., Sussillo, D., Shenoy, K.V., and Newsome, W.T. (2013). Contextdependent computation by recurrent dynamics in prefrontal cortex. Nature _503_ , 78–84. https://doi.org/10.1038/nature12742. 

43. Aoi, M.C., and Pillow, J.W. (2018). Model-based targeted dimensionality reduction for neuronal population data. In 32nd Conference on Neural Information Processing Systems (NeurIPS 2018). https://doi.org/10.11 09/NeurIPS2018.00001. 

44. Semedo, J.D., Zandvakili, A., Machens, C.K., Yu, B.M., and Kohn, A. (2019). Cortical areas interact through a communication subspace. Neuron _102_ , 249–259.e4. https://doi.org/10.1016/j.neuron.2019.01.026. 

45. Semedo, J.D., Gokcen, E., Machens, C.K., Kohn, A., and Yu, B.M. (2020). Statistical methods for dissecting interactions between brain areas. Curr. Opin. Neurobiol. _65_ , 59–69. https://doi.org/10.1016/j.conb.2020.09.009. 

46. Syeda, A., Zhong, L., Tung, R., Long, W., Pachitariu, M., and Stringer, C. (2023). Facemap: a framework for modeling neural activity based on orofacial tracking. Nat. Neurosci. _27_ , 187–195. https://doi.org/10.1038/s41 593-023-01490-6. 

47. Stringer, C., Pachitariu, M., Steinmetz, N., Carandini, M., and Harris, K.D. (2019). High-dimensional geometry of population responses in visual cortex. Nature _571_ , 361–365. https://doi.org/10.1038/s41586-019-1346-5. 

48. Williams, A.H., Kim, T.H., Wang, F., Vyas, S., Ryu, S.I., Shenoy, K.V., Schnitzer, M., Kolda, T.G., and Ganguli, S. (2018). Unsupervised discovery of demixed, low-dimensional neural dynamics across multiple timescales through tensor component analysis. Neuron _98_ , 1099–1115.e8. https:// doi.org/10.1016/j.neuron.2018.05.015. 

49. Pellegrino, A., Stein, H., and Cayco-Gajic, N.A. (2024). Dimensionality reduction beyond neural subspaces with slice tensor component analysis. Nat. Neurosci. _27_ , 1199–1210. https://doi.org/10.1038/s41593-024-01626-2. 

50. Guo, W., Kotsia, I., and Patras, I. (2012). Tensor learning for regression. IEEE Trans. Image Process. _21_ , 816–827. https://doi.org/10.1109/TIP.20 11.2165291. 

51. Zhou, H., Li, L., and Zhu, H. (2013). Tensor regression with applications in neuroimaging data analysis. J. Am. Stat. Assoc. _108_ , 540–552. https://doi. org/10.1080/01621459.2013.776499. 

52. Whoriskey, K., Auger-Me´ the´ , M., Albertsen, C.M., Whoriskey, F.G., Binder, T.R., Krueger, C.C., and Mills Flemming, J. (2017). A hidden mar- 

kov movement model for rapidly identifying behavioral states from animal tracks. Ecol. Evol. _7_ , 2112–2121. https://doi.org/10.1002/ece3.2795. 

53. Wang, G. (2019). Machine learning for inferring animal behavior from location and movement data. Ecol. Inform. _49_ , 69–76. https://doi.org/10.1016/ j.ecoinf.2018.12.002. 

54. Abeles, M., Bergman, H., Gat, I., Meilijson, I., Seidemann, E., Tishby, N., and Vaadia, E. (1995). Cortical activity flips among quasi-stationary states. Proc. Natl. Acad. Sci. USA _92_ , 8616–8620. https://doi.org/10.1073/pnas. 92.19.8616. 

55. Kemere, C., Santhanam, G., Yu, B.M., Afshar, A., Ryu, S.I., Meng, T.H., and Shenoy, K.V. (2008). Detecting neural-state transitions using hidden markov models for motor cortical prostheses. J. Neurophysiol. _100_ , 2441–2452. https://doi.org/10.1152/jn.00924.2007. 

56. Dano´ czy, M.G., and Hahnloser, R. (2005). Efficient estimation of hidden state dynamics from spike trains. In Advances in Neural Information Processing Systems 18 (NIPS 2005). https://doi.org/10.5555/2976248. 2976277. 

57. Rainer, G., and Miller, E.K. (2000). Neural ensemble states in prefrontal cortex identified using a hidden markov model with a modified em algorithm. Neurocomputing _32–33_ , 961–966. https://doi.org/10.1016/S09252312(00)00266-6. 

58. Radons, G., Becker, J.D., Du¨ lfer, B., and Kru¨ ger, J. (1994). Analysis, classification, and coding of multielectrode spike trains with hidden markov models. Biol. Cybern. _71_ , 359–373. https://doi.org/10.1007/BF00239623. 

59. Batty, E., Whiteway, M., Saxena, S., Biderman, D., Abe, T., Musall, S., Gillis, W., Markowitz, J., Churchland, A., Cunningham, J.P., et al. (2019). Behavenet: nonlinear embedding and bayesian neural decoding of behavioral videos. In Advances in Neural Information Processing Systems 32 (NeurIPS 2019). https://doi.org/10.1109/NeurIPS2019.00001. 

60. Foucault, C., Bounmy, T., Demortain, S., Thiririon, B., Eger, E., and Meyniel, F. (2024). A nonlinear code for event probability in the human brain. Preprint at bioRxiv. https://doi.org/10.1101/2024.02.28.582455. 

61. Sainburg, T., McPherson, T.S., Arneodo, E.M., Rudraraju, S., Turvey, M., Theilman, B.H., Tostado Marcos, P., Thielk, M., and Gentner, T.Q. (2025). Expectation-driven sensory adaptations support enhanced acuity during categorical perception. Nat. Neurosci. _28_ , 861–872. https://doi.org/ 10.1038/s41593-025-01899-1. 

62. Steinmetz, N.A., Zatka-Haas, P., Carandini, M., and Harris, K.D. (2019). Distributed coding of choice, action and engagement across the mouse brain. Nature _576_ , 266–273. https://doi.org/10.1038/s41586-019-1787-x. 

63. Semedo, J.D., Jasper, A.I., Zandvakili, A., Krishna, A., Aschner, A., Machens, C.K., Kohn, A., and Yu, B.M. (2022). Feedforward and feedback interactions between visual cortical areas use different population activity patterns. Nat. Commun. _13_ , 1099. https://doi.org/10.1038/s41467-022-28 552-w. 

64. Hochreiter, S., and Schmidhuber, J. (1997). Long short-term memory. Neural Comput. _9_ , 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735. 

65. Chen, R.T., Rubanova, Y., Bettencourt, J., and Duvenaud, D.K. (2018). Neural ordinary differential equations. Preprint at arXiv. https://doi.org/ 10.48550/arXiv.1806.07366. 

66. Rubanova, Y., Chen, R.T., and Duvenaud, D.K. (2019). Latent ordinary differential equations for irregularly-sampled time series. Preprint at arXiv. https://doi.org/10.48550/arXiv.1907.03907. 

67. Zhang, Y., He, T., Boussard, J., Windolf, C., Winter, O., Trautmann, E., Roth, N., Barrell, H., Churchland, M., Steinmetz, N.A., et al. (2023). Bypassing spike sorting: Density-based decoding using spike localization from dense multielectrode probes. In Advances in Neural Information Processing Systems 36 (NeurIPS 2023). https://doi.org/10.1101/2023.09. 21.558869. 

68. Izenman, A.J. (1975). Reduced-rank regression for the multivariate linear model. J. Multivariate Anal. _5_ , 248–264. https://doi.org/10.1016/0047-25 9X(75)90042-1. 

550 Neuron _114_ , 536–551, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

69. Zheng, S., Cai, X., Ding, C., Nie, F., and Huang, H. (2015). A closed form solution to multi-view low-rank regression. Preprint at arXiv. https://doi. org/10.48550/arXiv.1610.04668. 

70. Courant, R., and Hilbert, D. (1953). Methods of Mathematical Physics (Interscience Publishers). 

71. Fukunaga, K. (1990). Introduction to Statistical Pattern Recognition (Academic Press). 

72. Qin, S.J. (2006). An overview of subspace identification. Comput. Chem. Eng. _30_ , 1502–1513. https://doi.org/10.1016/j.compchemeng.2006.05.045. 

73. De la Torre, F. (2012). A least-squares framework for component analysis. IEEE Trans. Pattern Anal. Mach. Intell. _34_ , 1041–1055. https://doi.org/10. 1109/TPAMI.2011.184. 

74. Gruhl, C., and Sick, B. (2016). Variational bayesian inference for hidden markov models with multivariate gaussian output distributions. Preprint at arXiv. https://doi.org/10.48550/arXiv.1605.08618. 

75. Bassett, R., and Deride, J. (2019). Maximum a posteriori estimators as a limit of bayes estimators. Math. Program. _174_ , 129–144. https://doi.org/ 10.1007/s10107-018-1241-0. 

76. Brooks, S. (1998). Markov chain monte carlo method and its application. J. Royal Statistical Soc. D _47_ , 69–100. https://doi.org/10.1111/1467-98 84.00117. 

77. Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M., and Kenneth, D. (2016). Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels. Preprint at bioRxiv. https://doi.org/10.1101/ 061481. 

78. Warland, D.K., Reinagel, P., and Meister, M. (1997). Decoding visual information from a population of retinal ganglion cells. J. Neurophysiol. _78_ , 2336–2350. https://doi.org/10.1152/jn.1997.78.5.2336. 

79. Azabou, M., Pan, K.X., Arora, V., Knight, I.J., Dyer, E.L., and Richards, B.A. (2024). Multi-session, multi-task neural decoding from distinct cell-types and brain regions. Preprint at arXiv. https://doi.org/10.48550/arXiv.25 01.10368. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron _114_ , 536–551, February 4, 2026 551 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

## STAR★METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE<br>SOURCE|REAGENT or RESOURCE<br>SOURCE|IDENTIFIER|
|---|---|---|
|Deposited data|||
|Neural and behavioral data used to produce<br>all main text and supplementary fgures are<br>publicly available from the Brain Wide Map data<br>and Reproducible Electrophysiology data.<br>International Brain Laboratory||https://www.internationalbrainlab.com/data|
|Software and algorithms|||
|Python 3.9|python.org/downloads/|RRID: SCR_008394|
|SciPy1.11.4|scipy.org|RRID: SCR_008058|
|NumPy 1.23.1|numpy.org|RRID: SCR_008633|
|Pandas 2.1.3|pandas.pydata.org|RRID: SCR_018214|
|scikit-learn 1.3.2|scikit-learn.org|RRID: SCR_002577|
|matplotlib 3.8.2|matplotlib.org|RRID: SCR_008624|
|seaborn 0.13.0|seaborn.pydata.org|RRID: SCR_018132|
|Custom analysis code|https://github.com/yzhang511/<br>neural_decoding<br>https://doi.org/10.5281/zenodo.17317498||



## METHOD DETAILS 

## Closed-form solution for reduced-rank regression model 

In practice, the parameters of the reduced-rank regression model can be learned via automatic differentiation. In the special case of a linear model, a closed-form solution can be derived to improve computational efficiency and provide theoretical insight. For notational simplicity, we omit the session index _i_ and represent the neural activity and behavior across all trials as _X_ ∈ ℝ _[N]_[×] _[T]_ and _d_ ∈ ℝ _[P]_ , assuming there is only one trial in the data. To avoid dealing with the intercept term _b_ from Equation 2, we use the centered neural activity and behavior matrices _X[c]_ = _X_ − _X_ and _d[c]_ = _d_ − _d_ , where _X_ and _d_ represent the trial averages. 

Traditionally, a classical version of reduced-rank regression exists with a well-known closed-form solution.[68] This approach factorizes the full-rank regression weights into two lower-rank components: 

**==> picture [370 x 24] intentionally omitted <==**

where _F_ ∈ ℝ _[N]_[×] _[T]_[×] _[R]_ defines _R_ basis functions ( _F[r]_ ∈ ℝ _[N]_[×] _[T]_ ) over both the neural and temporal dimensions of the input neural activity _X[c]_ , while _E_ ∈ ℝ _[R]_[×] _[P]_ maps from the low-rank latent space to behavior _d[c]_ , with _E[r]_ ∈ ℝ _[P]_ denoting the rank- _r_ component. 

Our proposed formulation (Equation 6) follows the same principle of low-rank decomposition, but introduces additional structure to explicitly separate spatial (neural) and temporal components of the regression weights. Instead of learning unconstrained spatiotemporal bases _F[r]_ ∈ ℝ _[N]_[×] _[T]_[×] _[R]_ and behavior-specific bases _E_ ∈ ℝ _[R]_[×] _[P]_ , we decompose the regression weights into a low-rank neural basis _U_ ∈ ℝ _[N]_[×] _[R]_ and a low-rank temporal basis _V_ ∈ ℝ _[R]_[×] _[T]_[×] _[P]_ . This parameterization also allows us to share temporal structure across sessions via the temporal basis, while retaining session-specific variability through the neural basis. Specifically, our model solves the following objective: 

**==> picture [346 x 16] intentionally omitted <==**

2 where the operator vec( ⋅) flattens a matrix or tensor into a vector and ⃦⃦⋅⃦⃦ denotes the Frobenius norm. Regularization is included via 

_λ_ , though in practice it is applied as weight decay during optimization and is therefore not explicitly shown in Equations 1, 2, 3, and 4. To obtain the solution of _V_ , we differentiate LRRR (Equation 6) with respect to _V_ : 

**==> picture [348 x 19] intentionally omitted <==**

By setting the gradient in Equation 7 to 0, we obtain the closed-form solution of _V_ : 

~ _V_ = _G_[−][1] _H; G_ = _U_[⊤] ( _X[c] X[c]_[⊤] + _λI_ ) _U; H_ = ( _U_[⊤] _X[c]_ ) _d[c]_[⊤] _:_ (Equation 8) 

e1 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

**ll** 

OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

(Further details are provided below.) By substituting _V_ with _V_[~] in Equation 6,[69] the objective function simplifies to 

**==> picture [297 x 16] intentionally omitted <==**

The solution of _U_ is then derived by solving the following problem: 

**==> picture [320 x 21] intentionally omitted <==**

where 

**==> picture [325 x 10] intentionally omitted <==**

(Further details are provided below.) The resulting expression in Equation 10 constitutes a classical generalized Rayleigh quotient problem,[70][,][71] whose optimal solution is given by the top _R_ generalized eigenvectors of the matrix pair ( _Sb; St_ ). That is: 

**==> picture [47 x 9] intentionally omitted <==**

where the optimal columns of _U_[~] ∈ ℝ _[N]_[×] _[R]_ are formed from the eigenvectors _u_ associated with the top _R_ eigenvalues _μ_ . We can equivalently express Equation 10 as 

**==> picture [367 x 16] intentionally omitted <==**

where ∘ denotes element-wise matrix multiplication. This formulation suggests that _U_[~] captures directions in neural space that maximize a normalized version of the neural-behavioral covariance, after correcting for neuron-specific variance. As such, _U_[~] provides a principled way to quantify each neuron’s contribution to decoding behavior and identifies the most influential neurons for the task. Once the optimal _U_ and _V_ are obtained, neural activity _X_ is projected onto the learned low-rank subspace via _W_ = _X_[⊤] _U_ , which produces a low-dimensional representation that captures behaviorally relevant neural dynamics.[37][,][38][,][72] While this closed-form solution is limited to linear models, more flexible modeling frameworks using nonlinear decoders can be optimized using automatic differentiation. 

## Derivation of _**V**_[~] = _**G**_[−] **[1]** _**H**_ in Equation 8 

To find the optimal _V_ , we set the gradient in Equation 7 to 0 and obtain 

**==> picture [157 x 11] intentionally omitted <==**

This is a linear matrix equation of the form _GV_ = _H_ , where 

**==> picture [227 x 10] intentionally omitted <==**

Assuming _G_ is invertible, the solution is _V_[~] = _G_[−][1] _H_ as in Equation 8. 

**1** Derivation of _**U**_[~] = **arg** mi **n** _**U**_ Tr ( _**U**_[⊤] _**StU**_ )[−] **[1]** ( _**U**_[⊤] _**SbU**_ ) **2** in Equation 10 [ ] For notational clarity, we omit the vectorization operator vec( ⋅) in the remainder of this derivation. By substituting _V_ with _V_[~] = _G_[−][1] _H_ in Equation 6,[69] we now express the objective explicitly as a function of _U_ . We begin by expanding the first term in Equation 6: 

**==> picture [364 x 16] intentionally omitted <==**

The inner product can be rewritten using the trace operator: 

**==> picture [167 x 10] intentionally omitted <==**

The squared norm term becomes 

**==> picture [218 x 16] intentionally omitted <==**

The regularization term is 

**==> picture [95 x 11] intentionally omitted <==**

Combining these, the full loss in Equation 13 becomes 

**==> picture [359 x 13] intentionally omitted <==**

Neuron _114_ , 536–551.e1–e11, February 4, 2026 e2 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

Noting that the second and third trace terms in Equation 14 can be grouped using the definition _G_ = _U_[⊤] ( _X[c] X[c]_[⊤] + _λI_ ) _U_ , we write 

LRRR = ‖ _d[c]_ ‖[2] − 2Tr[ _Vd[c] X[c]_[⊤] _U_ ] + Tr[ _V_[⊤] _GV_ ] _:_ 

Substituting _H_ = ( _U_[⊤] _X[c]_ ) _d[c]_[⊤] and _V_ = _G_[−][1] _H_ into the expression yields: 

**==> picture [142 x 10] intentionally omitted <==**

**==> picture [136 x 9] intentionally omitted <==**

Therefore, the loss function becomes 

LRRR = ⃦⃦ _dc_ ⃦⃦2 − 2Tr[ _G_[−][1] _HH_[⊤][]] + Tr[ _H_[⊤] _G_[−][1] _H_ ] _:_ Since the two trace terms are equal (i.e., Tr _G_[−][1] _HH_[⊤][]] = Tr _H_[⊤] _G_[−][1] _H_ ), we simplify: [ [ ] LRRR = ‖ _d[c]_ ‖[2] − Tr[ _G_[−][1] _HH_[⊤][]] _:_ (Equation 15) As _dc_ |2 does not depend on _U_ , minimizing the loss in Equation 15 is equivalent to maximizing the trace term in Equation 8: ⃦⃦⃦ ⃒⃒⃒ arg min LRRR ⇔ arg max Tr _G_[−][1] _HH_[⊤][]] _: U U_ [ We can simplify _HH_[⊤] and _G_ further: _HH_[⊤] = _U_[⊤] _X[c] d[c]_[⊤] _d[c] X[c]_[⊤] _U_ = _U_[⊤] _SbU; G_ = _U_[⊤] ( _X[c] X[c]_[⊤] + _λI_ ) _U_ = _U_[⊤] _StU;_ where we have defined _Sb_ = _X[c] d[c]_[⊤] _d[c] X[c]_[⊤] _; St_ = _X[c] X[c]_[⊤] + _λI:_ Hence, the objective becomes arg max Tr ( _U_[⊤] _StU_ )[−][1] ( _U_[⊤] _SbU_ ) _: U_ [ ] 

where we have defined Hence, the objective becomes 

## Connection to PCA, CCA, demixed PCA and sliced TCA 

Our proposed RRR is similar to dimensionality reduction techniques like PCA and CCA, but with different objectives. As shown in Equation 12, the proposed RRR maximizes the correlation between the centered predictor _X_ and the centered response _d_ , as well as the variance of _d_ : 

RRR : Corr( _X; d_ )[2] Var( _d_ ) _:_ (Equation 16) 

According to De et al.,[73] PCA and CCA aim to maximize: 

PCA : Var( _X_ ) _;_ CCA : Corr( _X; d_ )[2] _:_ (Equation 17) 

PCA captures the major variations in neural activity _X_ but ignores the variations in behavior _d_ , while CCA considers the correlation between _X_ and _d_ but doesn’t prioritize modeling the variations in _d_ . The proposed RRR balances both the correlation between _X_ and _d_ and the variance of _d_ , making it more suitable for decoding tasks where capturing behavioral variations is crucial for prediction. The proposed RRR is also related to demixed-PCA,[38] which minimizes the loss 

**==> picture [321 x 12] intentionally omitted <==**

where _X_ is the centered data matrix, with each row representing the neural activity of each neuron across all trials and task conditions. The reconstruction target, _Xs_ , is a matrix of stimulus averages, with each data point replaced by the average neural activity for the corresponding stimulus. The solutions for _F_ and _E_ can be analytically obtained using the standard reduced-rank regression through singular value decompositions. The main difference is the reconstruction target: the behavior _d_ in our model (Equation 6) vs. the taskcondition averaged neural activity _Xs_ in demixed PCA. Intuitively, demixed-PCA maximizes the correlation between the neural activity _X_ and the task-condition averaged neural activity _Xs_ , while also maximizing the variance of _Xs_ . 

The decomposition of the full-rank weight matrix in Equation 2 resembles sliced TCA[49] when the behavior dimension _P >_ 1: 

(Equation 19) 

_W_ : _;_ : _;p_ = _UpVp_[⊤] _[;]_ 

e3 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

**ll** 

OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

where _W_ ∈ ℝ _[N]_[×] _[T]_[×] _[P]_ is the three-way regression tensor, and _Up_ ∈ ℝ _[N]_[×] _[R]_ and _Vp_ ∈ ℝ _[R]_[×] _[T]_ are the low-rank factors for the _p_ th slice along the behavior dimension. 

## BMM-HMM: Model details 

This section presents algorithms and implementation details for various BMM-HMM model variants (Figure S1). The BMM-HMM model consists of a dynamic process governing transitions among discrete latent states[→] _s_ and an observation process describing the generation of decoder estimates[→] _d_ given the latent state. The dynamic model, _P_ ( _sk_ | _sk_ − 1), describes the state transition from trial _k_ − 1 to _k_ , parameterized by a state transition matrix. The observation model, _p_ ( _dk_ | _sk_ ) = _p_ ( _dk_ | _zk_ ) _p_ ( _zk_ | _sk_ ), is characterized by a beta mixture model, where _p_ ( _zk_ | _sk_ ) is the emission probability at each state, _p_ ( _dk_ | _zk_ ) is the observation probability, and _zk_ controls the assignment of beta distributions in the mixture. 

Specifically, we assume the single-session, single-trial decoder output _dk_ = _P_ ( _yk_ = 1| _Xk_ ) ∈[0 _;_ 1] follows a mixture of beta distributions, with mixture assignment _zk_ depending on a latent state _sk_ , governed by an _H_ -state HMM. The data generation process for _dk_ is formulated as 

**==> picture [362 x 24] intentionally omitted <==**

where _azk_ and _bzk_ are parameters of a beta distribution. In each trial, the latent state _sk_ generates _zk_ with emission probability _ϕsk zk_ , and _dk_ is drawn from a beta mixture with observation probability _p_ ( _dk_ | _zk_ ), where _dk_ values cluster around 1 when _zk_ = 1 and around 0 when _zk_ = 0. 

The main idea is to substitute the single-session and single-trial decoder output _dk_ , which only considers information from the neural activity _Xk_ , with the inferred _zk_ . The inferred _zk_ contains information about the underlying behavioral states deduced from the trialto-trial correlations in[→] _d_ . Specifically, the improved decoder output is 

**==> picture [373 x 72] intentionally omitted <==**

where _f_ ( _dk_ | _sk_ ) =[∑][1] _zk_ = 0 _[p]_[(] _[d][k][;][z][k]_[|] _[s][k]_[)][, as defined in][ Equation 20][.] _[ α][k]_[(] _[s][k]_[)][ and] _[ β] k_[(] _[s][k]_[)][ are outputs from the forward and backward passes] in an Expectation-Maximization (EM) algorithm, described in more depth in the next section. We focus on inferring _zk_ because it reflects the true choices made by the mice during the visual decision-making task. In contrast, _dk_ represents noisy observations influenced by these latent choices. Since our goal is to fit a latent dynamical model that recovers these underlying decisions, _zk_ is the primary target of inference. 

## EM algorithm for BMM-HMM 

The EM (Baum–Welch) algorithm is used for iterative HMM parameter estimation. Each iteration consists of the following Expectation and Maximization steps: 

- **(E step)** Let _k_ index trial, _z_ ∈{0 _;_ 1} index the beta mixture component and _h; m_ ∈{1 _;_ … _; H_ } index the state. For all component and state pairs, we recursively compute the forward and backward probabilities _αk_ ( _h; z_ ) and _βk_ ( _h;z_ ), defined below. We then compute the component and state occupation probabilities _γk_ ( _h; z_ ) and _ξk_ ( _h; m_ ). 

- **(M step)** Using the estimated _γk_ ( _h_ ) and _ξk_ ( _h_ ), we then update the model parameters, including the transition probabilities _ηhm_ and the emission probabilities _ϕhz_ of the HMM, and the parameters of the beta mixture _az; bz_ . 

## _Forward pass_ 

We define the probability of observing the sequence of decoder outputs[→] _d_ being in state _h_ in trial _k_ as 

_αk_ ( _h_ ) : = _p_ ( _d_ 1 _; d_ 2 _;_ … _; dk; sk_ = _h_ ) _:_ (Equation 22) 

The pseudo-code for the iterative computation of _αk_ ( _h_ ) is: 

- _Initialization α_ 1( _h_ ) = _π_ 0( _h_ ) _f_ ( _d_ 1| _h_ ) ∀ _h_ ∈{1 _;_ … _; H_ } _._ 

- • _Recursion αk_ ( _h_ ) = _Hm_ = 1 _[α][k]_[ −][1][(] _[m]_[)] _[η] mh f_ ( _dk_ | _h_ ) ∀ _h; m_ ∈{1 _;_ … _; H_ } _; k_ ∈{1 _;_ … _; K_ }. ( ∑ ) 

- • _Termination p_[→] _d_[)] =[∑] _[H] h_ = 1 _[α][K]_[(] _[h]_[)][,] ( 

where _π_ 0 is a vector containing the initial probabilities for each of the _H_ hidden states. 

Neuron _114_ , 536–551.e1–e11, February 4, 2026 e4 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

_Backward pass_ 

The probability of future observations given that the HMM is in state _h_ in trial _k_ is 

**==> picture [306 x 10] intentionally omitted <==**

The pseudo-code for the iterative computation of _βk_ ( _h_ ) is: 

**==> picture [336 x 38] intentionally omitted <==**

_Forward-backward_ 

The state occupation probability _γk_ ( _h_ ) is 

**==> picture [361 x 34] intentionally omitted <==**

The component and state occupation probability _γk_ ( _h; z_ ) is the probability of component _z_ at state _h_ in trial _k_ given the whole observation sequence[→] _d_ : 

**==> picture [340 x 21] intentionally omitted <==**

We then estimate _ξk_ ( _h; m_ ), the probability of transitioning from state _h_ to _m_ given all observations[→] _d_ : 

**==> picture [361 x 33] intentionally omitted <==**

**==> picture [328 x 23] intentionally omitted <==**

For the M step, we update the transition and emission probabilities according to 

**==> picture [359 x 90] intentionally omitted <==**

We then update the parameters of the BMM ( _a_ 0 _; a_ 1 _; b_ 0 _; b_ 1) by maximizing the expected log-likelihood. First, we write down the likelihood of the BMM as 

**==> picture [386 x 25] intentionally omitted <==**

where _π_ ∞ represents the equilibrium probability for each of _H_ hidden states, which can be computed using the estimated transition probabilities. The conditional distribution is subsequently determined by 

**==> picture [312 x 60] intentionally omitted <==**

e5 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

OPEN ACCESS 

## Article 

## **ll** 

**==> picture [46 x 35] intentionally omitted <==**

Finally, the expected log-likelihood of the BMM is 

**==> picture [361 x 145] intentionally omitted <==**

In practice, we find ( _a_[∗] 0 _[;][ a]_ 1[∗] _[;][ b]_[∗] 0 _[;][ b]_ 1[∗] ) that maximize the quantity in Equation 36 through numerical optimization. 

## Oracle BMM-HMM 

In each session, the oracle BMM-HMM substitutes the ground truth observed behaviors[→] _y_ for[→] _z_ , treating[→] _z_ as a known quantity. This allows us to learn the underlying data-generating mechanism that produces the decoder outputs[→] _d_ . The process consists of the following steps: 

1. Train a discrete-state HMM on the ground truth observed behaviors[→] _y_ to estimate the oracle model parameters, including transition probabilities _ηhm_ and emission probabilities _ϕhz_ for each session. 

2. Apply a BMM to the decoder outputs[→] _d_ , treating the mixture assignment variable[→] _z_ as a known quantity by substituting[→] _z_ with the ground truth observed behaviors[→] _y_ . This step provides the correct assignment of mixture components. The learned oracle BMM parameters, ( _a_ 0 _; a_ 1 _; b_ 0 _; b_ 1), capture the true probabilistic relationship between[→] _d_ and[→] _z_ . 

3. Use the learned oracle model parameters to initialize and fit the BMM-HMM using the EM algorithm described in the section ‘‘EM algorithm for BMM-HMM’’ for the corresponding session. During model fitting, fix the oracle parameters ( _ηhm;ϕhz;a_ 0 _;a_ 1 _;b_ 0 _; b_ 1). Although the model parameters remain fixed, we infer the latent neural states _sk_ and the latent choices _zk_ based on the observed baseline decoder output _dk_ . 

This procedure allows us to deduce the latent behavioral states[→] _s_ and latent behaviors[→] _z_ as if we know the true data generation process. 

## Learning empirical priors of state-space model parameters 

To learn empirical priors for the multi-session BMM-HMM, we fit a variational HMM[74] to the ground truth observed behavior[→] _y_ from non-target sessions. This allows us to learn an empirical prior of the trial-to-trial correlations inherent in the true behavioral data. We impose Dirichlet priors on the initial state distribution _π_ 0, rows of the transition probability matrix _ηh_ ⋅, and rows of the emission probability matrix _ϕh_ ⋅ as follows: 

**==> picture [336 x 50] intentionally omitted <==**

**==> picture [320 x 24] intentionally omitted <==**

where ( _u_[(] _[π]_[0][)] _; u_[(] _[η]_[)] _; u_[(] _[ϕ]_[)][)] are the Dirichlet distribution concentration parameters, learned by fitting a variational HMM on the ground truth observed behaviors[→] _y_ from the training sessions using the Python package _hmmlearn_ . The resulting posterior distributions serve as priors for the multi-session BMM-HMM parameters, constraining their updates during the EM algorithm’s M step. To set empirical priors for the BMM parameters, we assume _dk_ follows a mixture of beta distributions from the exponential family, expressed as: 

**==> picture [345 x 11] intentionally omitted <==**

_h_ ( _d_ ) = 1 _; c_ ( _az; bz_ ) = 1 _= B_ ( _az; bz_ ) _;_ (Equation 41) 

Neuron _114_ , 536–551.e1–e11, February 4, 2026 e6 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

where 

_B_ ( _az; bz_ ) = _Γ_ ( _az_ ) _Γ_ ( _bz_ ) _= Γ_ ( _az_ + _bz_ ) _;_ (Equation 42) 

**==> picture [351 x 11] intentionally omitted <==**

For exponential family members, the conjugate prior is 

**==> picture [343 x 11] intentionally omitted <==**

Therefore, a suitable conjugate prior distribution for ( _az; bz_ ) is 

**==> picture [339 x 20] intentionally omitted <==**

Setting the natural conjugate prior _ψ_ parameter to zero yields independent exponential priors for ( _az;bz_ ), which have proven effective empirically. We apply a hierarchical BMM on the decoder outputs[→] _d_ , using the Python package _pymc3_ . We assume that the mixture assignment[→] _z_ can be empirically determined a priori, and substitute[→] _z_ with the observed behaviors[→] _y_ from the training sessions. The posterior distributions for ( _ν_[(] 1 _[z]_[)] _[;][ ν]_[(] 2 _[z]_[)] ) then serve as priors for the multi-session BMM-HMM parameters, constraining their updates during the EM algorithm’s M step. 

## Multi-session BMM-HMM 

Following the approach in Equations 37, 38, and 39, we impose Dirichlet priors on the BMM-HMM dynamic parameters ( _π_ 0 _;ηh_ ⋅ _;ϕh_ ⋅). We modify the EM algorithm in the section ‘‘EM algorithm for BMM-HMM’’ by using Maximum A Posteriori (MAP) estimation[75] to learn the posterior distributions of these parameters. The E step remains unchanged, while the M step incorporates the new prior terms when updating the HMM parameters with fixed latent _sk_ and _zk_ . The posterior means of the HMM parameters become 

**==> picture [356 x 63] intentionally omitted <==**

where ( ~ _u_ ( _π_ 0) _;_ ~ _u_ ( _η_ ) _;_ ~ _u_ ( _ϕ_ )) are the posterior concentration parameters from fitting the variational HMM on the training sessions. When updating BMM parameters, we add the Dirichlet prior term log _p_ ( _π_ 0 _; η; ϕ_ ) to the complete-data log-likelihood in Equation 33 and solve for ( _a_ 0 _; a_ 1 _; b_ 0 _; b_ 1) that maximize this new objective function. 

We constrain BMM parameters ( _a_ 0 _; a_ 1 _; b_ 0 _; b_ 1) _;_ using empirical priors 

**==> picture [69 x 13] intentionally omitted <==**

learned from the training sessions; see details in the section ‘‘learning empirical priors of state-space model parameters.’’ Incorporating the log-prior term (Equation 45) into the complete log-likelihood involves adding the following penalty to the right-hand side of Equation 36: 

**==> picture [369 x 24] intentionally omitted <==**

Numerically solving the penalized objective yields MAP estimates for the BMM parameters instead of the standard maximum likelihood estimation (MLE) solutions. 

## LG-AR1: Model details 

For scalar-valued _yk_ ∈ ℝ, we assume the decoder output _dk_ ∈ ℝ linearly depends on the latent behavior _zk_ ∈ ℝ. To incorporate trialto-trial correlations, the transitions of _zk_ between trials are modeled using a first-order autoregressive process. The objective aligns with that of a Kalman smoother,[28] which is to infer the state of a dynamical system ( _zk_ ) given a sequence of noisy observations ( _dk_ ). The formal data generating model is described as 

**==> picture [308 x 35] intentionally omitted <==**

e7 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

Intuitively, as the _first-order autocorrelation coefficient ρ_ approaches 1, _zk_ in the current trial is expected to exhibit minimal deviation from _zk_ − 1 in the preceding trial, as per Equation 50. As the _linear coefficient of the Gaussian observation model θ_ approaches 1, _dk_ is expected to closely track the pattern of _zk_ according to Equation 49. _μ_ is the _bias of the Gaussian observation model_ . In practice, the values of _θ_ and _ρ_ are determined by fitting the LG-AR1 model to the observed[→] _d_ . 

Similar to BMM-HMM, the main idea is to replace the original decoder estimate _dk_ , based solely on neural activity _Xk_ , with a smoothed estimate _d_[~] _k_ derived from the inferred latent state _zk_ . _d_[~] _k_ incorporates trial-to-trial correlations from[→] _d_ = { _d_ 1 _; d_ 2 _;_ … _; dk_ }, as[→] _d_ is used to infer the latent states[→] _z_ = { _z_ 1 _; z_ 2 _;_ … _; zk_ } .This process potentially improves _d_[~] _k_ ’s accuracy over the original _dk_ in estimating the true behavior. While[→] _d_ is used for model fitting and latent state inference, _d_[~] _k_ is the improved (smoothed) decoder estimate for the held-out trial _k_ given the entire[→] _d_ . To obtain _d_[~] _k_ , we sample from its posterior predictive distribution 

**==> picture [491 x 47] intentionally omitted <==**

In Equation 51, we use _d_[~] _k_ , the posterior mean of _dk_ , because empirically it leads to better recovery of the prior variable compared to using the inferred _zk_ . We believe this is due to the fact that the prior we aim to decode is itself the output of another model,[27] which estimates the ‘‘true’’ prior from data and thus contains noise. Ideally, we would compare the latent _zk_ directly to the true, unobserved prior, but since that is inaccessible, we rely on an estimated version from a statistical model.[27] In this context, _d_[~] _k_ serves as a proxy. To fit LG-AR1 on single-session data, we use a Bayesian approach, treating model parameters _Λ_ = ( _θ; μ; ρ; σ_[2] ϵ _[;][ σ]_[2] _τ_ ) as random variables with joint prior _p_ ( _Λ_ ): 

**==> picture [322 x 11] intentionally omitted <==**

In practice, we use the Python package _pymc3_ to fit the hierarchical LG-AR1 and learn the posterior distribution of session-specific parameters _Λ_ via MCMC sampling. 

To implement the multi-session LG-AR1, we begin by learning the dynamic model parameters ( _ρ;σ_[2] _τ_ ). This estimation is performed using the observed behaviors[→] _y_ from the training sessions, under the assumption that these dynamic model parameters can be empirically determined a priori. Next, we estimate observation model parameters ( _θ; μ; σ_[2] ϵ ) using decoder outputs[→] _d_ and corresponding observed[→] _y_ from training sessions. After estimating model parameters from the training data, we use the posterior means of these multi-session LG-AR1 parameters _Λ_ = ( _θ; μ; ρ; σ_[2] ϵ _[;][ σ]_[2] _τ_ ) to initialize the hierarchical LG-AR1 model (Equations 49 and 50) for the held-out session, with _Λ_ fixed during model fitting. For this held-out session, where true behaviors are unknown, we infer the latent behaviors _zk_ and obtain improved decoder outputs _d_[~] _k_ via MCMC sampling. 

We also implement an oracle LG-AR1 model to emulate the ground-truth data-generating process for[→] _d_ . This oracle model is constructed by estimating model parameters using the ground truth observed[→] _y_ from the target session, under the assumption that the true values of the variable[→] _z_ are known. For the oracle model, we learn dynamic AR1 parameters ( _ρ; σ_[2] _τ_ ) and observation model parameters ( _θ; μ; σ_[2] ϵ ) using true[→] _y_ and observed[→] _d_ from the test session. We initialize the hierarchical LG-AR1 model using these oracle solutions and hold them fixed while inferring the latent _zk_ and improved decoder outputs _d_[~] _k_ , as if we know the true data-generating mechanism. We summarize the differences among single-session, oracle, and multi-session LG-AR1 graphical models in Figure S1. 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

## Data processing 

## _IBL trial-aligned dataset_ 

For choice, we align trials to the stimulus onset, considering neural activity from 0.5 s before to 1.5 s post-onset. For prior, we also align trials to the stimulus onset, including neural activity from 0.6 s to 0.1 s pre-onset. The prior represents the mice’s estimate of the stimulus side probability. We use the same decoding window as in the previous study,[27] focusing on the period with minimal wheel movements. Within each trial, we segment neural activity into 50-ms non-overlapping time bins. For each time bin, we bin spike counts using all neurons, sorted by Kilosort 2.5,[77] from each session. For dynamic behaviors (wheel speed and whisker motion energy), we select the first movement onset as the alignment event, and decode the behavior starting at the alignment event and ending at 1 s after the alignment event. The neural activity within each trial is binned into non-overlapping 20 ms bins. For each time bin, we similarly bin spike counts using all neurons from each session. 

## _IBL trial-unaligned dataset_ 

We focus only on wheel speed and whisker motion energy, as variables like choice and prior are only defined during experimental trials, which are periods when stimuli are presented and mice respond for rewards. Unlike the trial-aligned dataset, we do not align neural activity and behavior to a specific event onset. Instead, we segment the continuous Neuropixels recordings into 2-s snippets to construct the trial-unaligned dataset for each session. These snippets cover intervals both during and outside experimental trials, capturing the repetitive, structured behaviors within trials as well as the more spontaneous behaviors outside of trials. 

Neuron _114_ , 536–551.e1–e11, February 4, 2026 e8 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

## _Allen dataset_ 

To use reduced-rank regression models, we decode 3 behavior variables: Gabors, static gratings, and running speed. The Gabors variable has 3 discrete orientation classes, while the static gratings variable has 6. Running speed, in contrast, is a continuous trialunaligned variable recorded during periods of spontaneous behavior. For Gabors and static gratings, we align trials to the respective stimulus onset and extract neural activity within a 200 ms window around the onset. For running speed, we divide the continuous recording into 1-s snippets. For all variables, we use a time bin size of 10 ms to bin neural activity. 

To apply BMM-HMM, we also decode the licks. In the Allen datasets, mice view a continuous stream of briefly presented visual stimuli and receive water rewards for correctly detecting changes in stimulus identity. To relate neural activity to behavior, the timing of behavioral responses, licks, is also recorded. Each Neuropixels recording session is divided into five stimulus blocks, but licking occurs exclusively during the ‘‘active’’ period, which lasts approximately 2000 to 3000 s. During this period, each visual stimulus is updated roughly every 0.2 s. We segment the active period into fixed 0.2-s intervals and labeled each interval as 1 if at least one lick occurred, and 0 otherwise. For each interval, we use a time bin size of 10 ms. For each session, we decode licks using neural activity from the recorded subset of regions of interest, DG, CA1, CA3, VISp, VISa, LP, and TH (the medial division of the posterior parahippocampal cortex). For example, if a session records from DG, CA1, and LP, all three are used in the decoder. Regions outside this set are excluded from the analysis, even if recorded. Region naming follows the IBL brain atlas conventions. _Primate random target dataset_ 

This dataset consists of 15 min of continuous reaching behavior, manually segmented into 1351 600 ms ‘‘trials.’’ It includes recordings from 130 neurons along with simultaneously tracked hand kinematics. We use the preprocessed version of the dataset provided by Pei et al.,[20] and apply a 20 ms bin size to discretize neural activity and behavior into 30 time bins per trial. Our decoding target is finger velocity, represented by velocity components along both the X and Y axes. 

## Hyperparameter selection 

For static variables (choice, prior, Gabors, static gratings), the target behavior in each trial is decoded using the full neural activity from that trial. For dynamic behaviors (wheel speed, whisker motion energy, running speed, finger velocity), the target behavior at each time bin _t_ is decoded using the entire neural activity across all time bins within the corresponding trial. For multi-session models applied to the IBL dataset, we use both multi-session and multi-region reduced-rank regression models to decode static and dynamic behaviors. In contrast, for the Allen and primate random target datasets, we do not include multi-region reduced-rank regression models, as our objective is not to perform region-specific decoding for these datasets. For discrete behavior variables (e.g., choice and licks), we employ both single- and multi-session BMM-HMM models. To decode prior, we use both single- and multi-session LG-AR1 models. Decoder performance is evaluated using accuracy and AUC for discrete variables, Pearson correlation for prior, and _R_[2] for dynamic behaviors. 

For our linear baselines, we use L2-regularized logistic regression for discrete-valued variables and ridge regression for prior and dynamic behavioral variables. Regularization strength is selected via _scikit-learn_ ’s GridSearchCV function, from the set {10 _[k]_[⃒⃒] _k_ = − 4 _;_ − 3 _;_ … _;_ 4}. Both reduced-rank regression models and MLPs are trained using gradient descent in PyTorch, with the AdamW optimizer and a cosine annealing learning rate scheduler. All models are trained for 2000 epochs with a batch size of 16, and the best model, determined by the lowest validation loss, is selected for test set decoding. For single-session MLP and reduced-rank regression models, hyperparameter search is performed over the value ranges in Table S2, using _Ray Tune_ in Python. We randomly sample 30 models from the specified range for this search. For multi-session and multi-region reduced-rank regression models, extensive hyperparameter tuning is not required as for the single-session models, since the model is less prone to overfitting. As a result, we only perform a search over the rank of the reduced-rank regression models, while fixing the learning rate at 0.01 and weight decay at 1, based on results from pilot studies. 

## Recording hardwares, task structures and implementation guidelines _Reduced-rank regression models_ 

These models are compatible with any electrophysiological recording hardwares that output single-spike data, including both highdensity Neuropixels probes and lower-density Utah arrays. Regardless of the number of recorded neurons, reduced-rank regression models consistently demonstrate strong decoding performance and serve as a reliable alternative to traditional linear models across datasets. For example, the IBL dataset contains an average of 676 neurons per session, ranging from approximately 300 to over 2000 neurons. In comparison, the Allen dataset has an average of 690 neurons per session, with a minimum of 415 and a maximum of 1005 neurons. Even in the primate random target dataset, which contains only 130 neurons, the reduced-rank regression model outperforms the linear baseline (Figures 8J and 8L). Importantly, these models are not constrained by task structure: they can be applied to both highly structured, trial-based paradigms as well as spontaneous, freely behaving tasks (Figures 8A and 8C). Reduced-rank regression models are capable of decoding both discrete and continuous static variables (e.g., choice and prior), as well as dynamic variables (e.g., wheel speed). When neuron count is not taken into account, model performance is generally robust to the choice of model rank, which is the main hyperparameter. This finding is consistent across both the IBL and Allen datasets (Figure S2). To account for neuron count, we further analyze the performance of the single-session reduced-rank regression model on IBL data as a function of neuron count and model rank. In Figure S8, we find that a rank of 2 generally yields better performance for decoding choice, prior, and whisker motion energy, whereas a larger rank performs better for decoding wheel speed. 

e9 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

**ll** OPEN ACCESS 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

## _BMM-HMM and LG-AR1 models_ 

These models can be used with the same electrophysiological recording hardwares as the reduced-rank regression models. The BMM-HMM is designed for decoding discrete-valued behavior variables, such as choice. While its default formulation is best suited for binary variables, it can be extended to multi-class variables using one-vs-all classification. In addition, users need to consider the nature of the behavior task, i.e., whether there is ‘‘block’’-like behavioral structure in the data to begin with. For example, previous studies have shown that choice probabilities can vary across trials within a session, either due to block-based stimulus sequences in the IBL task design,[17] or due to shifts in internal states.[16] Because BMM-HMM infers latent internal states underlying observed behavioral outcomes, such as when a mouse perceives a stimulus and responds with a choice, it is not applicable to visual stimuli like Gabors and static gratings, which are not behavioral responses. The LG-AR1 model is suited for scalar-valued variables like prior. However, both models are flexible: users can modify the latent dynamical and observation models to accommodate different types of behavior variables. For example, replacing the beta mixture model in the BMM-HMM with a Gaussian mixture model allows it to model scalar-valued variables. Similarly, the LG-AR1 model can be extended to vector-valued variables, such as wheel speed or whisker motion energy, by substituting the univariate Gaussian observation model with a multivariate Gaussian and using a vector autoregressive latent dynamical model. 

## Computation time comparison 

We evaluate the computational efficiency of the proposed reduced-rank regression model in comparison to baseline MLP models. Specifically, we measure the real-time training duration for both single-session and multi-session RRR and MLP using the Allen visual coding dataset. For single-session models, each model is trained on one of the 58 sessions, and the average computation time is calculated across all sessions. For multi-session models, a single model is trained jointly on all 58 sessions, and the total training time is recorded. To ensure a fair comparison, all models are trained for 2000 epochs on the same hardware: a single Nvidia RTX 3060 GPU. 

We observe that training the MLP model takes approximately 2.5 times longer than training the RRR model, in both single-session and multi-session settings. The single-session reduced-rank regression model is highly efficient, requiring only about 2 min to complete training for 2000 epochs on a single session using a single GPU. The multi-session RRR model is also highly efficient, requiring less than 2 h to train for 2000 epochs on the full 58-session dataset. While a direct comparison in terms of data size and experimental setup is not explored in this work, training a 100-session POYO model[14] using 8 NVIDIA A40 GPUs reportedly takes approximately 2 days for 400 epochs. This underscores the computational efficiency of the multi-session RRR model relative to more resourceintensive transformer-based approaches. 

## Assessing statistical significance of decoding improvements via bootstrap resampling 

In section ‘‘learning behaviorally relevant neural variations across sessions’’, we utilize a bootstrap resampling approach to assess the statistical significance of the decoding improvements achieved by the multi-session RRR compared to the single-session RRR. Specifically, we calculate the difference in Adjusted Rand Index (ARI) and decoding accuracy between the two models across the same set of 10 sessions. To evaluate whether this observed difference is statistically meaningful, we generate a null distribution by resampling the computed ARI and accuracy values with replacement. For each of 10,000 bootstrap samples, we randomly sample data points with replacement from the 10 sessions and compute the ARI and accuracy difference between the models on each resampled dataset. This results in empirical null distributions under the assumption that any metric difference arises from sampling variability. We then estimate a nonparametric _p_ value by calculating the proportion of bootstrap samples in which the absolute performance difference exceeds the observed one. 

## Decoding frequency components of behavior 

Observing that whisker motion energy exhibits higher-frequency fluctuations than the smoother wheel speed (Figures S3A and S3E), we hypothesize that decoders may still effectively capture slower behavioral components even if they fail to fully reconstruct the entire signal. To answer this question, we decompose the behavioral signals into orthogonal components using both Fourier analysis and PCA, and evaluate how well different baseline decoders reconstruct each component. 

To determine the amount of behavioral variance explained at each frequency, we compute the power spectral density (PSD) of the observed behavior, predicted behavior, and prediction error, following the approach from Warland et al.[78] As shown in Figures S3B and S3F, the PSDs for both observed and predicted behaviors, as well as the corresponding prediction error, drop off steeply at higher frequencies. Beyond 5 Hz, the decoder captures little to no behavioral information, and most of the variation in the behavioral signals lies in the lower frequency range. We also apply PCA to the observed behavior and project the observed, predicted, and error signals onto the resulting principal components (PCs). As shown in Figures S3B and S3F, the first 10 PCs account for most of the behavioral variance, and the reduced-rank regression model primarily captures information contained in these dominant components. 

A one-to-one correspondence between the first 5 PCs and the first 5 Fourier components (Figures S3C and S3G) suggests that the leading PCs capture low-frequency components of the behavior. To determine whether the decoders can capture both gradual and rapid fluctuations in behavior, we extract the first 10 PCs from the observed behavior and reconstruct the behavior using each PC. We then train each baseline decoder to predict these PC-specific reconstructions from neural activity. Figures S3D and S3H display the 

Neuron _114_ , 536–551.e1–e11, February 4, 2026 e10 

**ll** OPEN ACCESS 

Article 

**==> picture [76 x 35] intentionally omitted <==**

decoding _R_[2] for each PC across all baseline models. Most decoders perform similarly when decoding low-frequency components, with the reduced-rank regression model slightly outperforming others for wheel speed, which is inherently smoother. Overall, higher decoding performance is achieved primarily for lower-frequency components. 

## Assessing statistical significance of decoding improvements via null distribution 

In section ‘‘mapping behaviorally-relevant timescales across the brain,’’ we measure the increased information decoded from each region using the multi-region reduced-rank regression model compared to the baseline linear decoder. To control for potential spurious correlations, we conduct an additional experiment, following the approach in IBL et al.[18] We generate null distributions to test the significance of our decoding results according to the procedure described in the caption of Figure S4. To determine the significance of our decoding results, we analyze brain regions PO, LP, DG, CA1, and VISa as representative examples. Figure S4 displays the adjusted scores, with the original scores for choice and prior decoding corresponding to those in Figure 7D. While the percentage increase in decoding metrics varies slightly between original and adjusted scores, the relative ranking of brain regions, based on decoding improvement, remains largely consistent. For instance, DG shows the highest improvement in decodable information for choice, both before and after null distribution adjustment. This analysis demonstrates the reliability of the decoding improvement offered by our proposed model. 

## Relationship between LG-AR1 and post-hoc smoother, and across-session variability in BMM-HMM/LG-AR1 outputs 

In Figures 4D and 4H, we observe that the LG-AR1 models output a smoother version of the baseline model’s predictions. Although the LG-AR1 model is based on a latent variable framework, it can also be interpreted as a post-hoc smoother. To investigate whether applying a post-hoc smoother to denoise the baseline model’s predicted prior outperforms the LG-AR1 model, we use the SavitzkyGolay filter from the Python _scikit-learn_ package. This filter smooths the decoder output by fitting successive windows of the signal with low-degree polynomials using least-squares regression. We use a window length of 17 samples and a third-order polynomial. The smoothed signal preserves key features such as peaks and slopes while reducing high-frequency noise (Figure S5B). Together, Figures S5A and S5B demonstrate that the post-hoc smoother performs similarly to the single-session LG-AR1 model. 

Figure 4 illustrates how BMM-HMM and LG-AR1 models enhance decoder outputs, using examples of estimated model parameters and predictions from a single session. To examine their effects across multiple sessions, we train single-session, oracle, and multi-session BMM-HMM/LG-AR1 models over 10 sessions. In Figures S5C and S5D, we compare parameter estimation accuracy between the single- and multi-session models by evaluating their parameters against those of the oracle models. Using root mean squared error (RMSE) as the metric, we find that the multi-session BMM-HMM/LG-AR1 models consistently outperform the singlesession models in terms of lower estimation errors. In addition to the decoded choice probabilities and priors shown in Figures 4G and 4H, we present additional examples from four other sessions to examine variability in model predictions across sessions (Figures S5E and S5F). We observe that the ‘‘block’’ structure is more clear in the decoded choice probabilities for some sessions compared to others. However, even in sessions with less apparent ‘‘block’’ structure, the multi-session BMM-HMM models can still exploit across-session structure to generate predictions closer to oracle BMM-HMM than single-session BMM-HMM. 

## Scaling curves for multi-session reduced-rank regression models 

The empirical and theoretical success of scaling laws in multi-session neuro-foundation models[12–15][,][79] suggests that model performance improves predictably as the amount of data increases. These findings raise an important question: Do similar scaling laws apply to non-transformer-based, linear models, such as multi-session reduced-rank regression models? In this section, we present the results of our scaling experiments using the IBL dataset. For four behavior variables, choice, prior, wheel speed, and whisker motion energy, we train both single-session and multi-session reduced-rank regression models on data from 5, 10, 20, 40, and 73 sessions, and evaluate their performance on a fixed set of 5 test sessions. As shown in Figure S7, only whisker motion energy exhibits consistent improvement in decoding performance with additional training sessions. For choice, prior, and wheel speed, decoding performance improves up to approximately 20 ∼ 40 training sessions, after which it begins to decline. This pattern suggests that while increased training data can initially help prevent overfitting and uncover shared structure across sessions, the benefits plateau beyond a certain threshold. Overall, our findings indicate that scaling behavior in multi-session reduced-rank regression models is task-dependent, and their performance does not universally improve with more data. 

e11 Neuron _114_ , 536–551.e1–e11, February 4, 2026 

**Neuron, Volume** _**114**_ 

## **Supplemental information** 

## **Exploiting correlations across trials** 

## **and behavioral sessions to improve neural decoding** 

**Yizi Zhang, Hanrui Lyu, Cole Hurwitz, Shuqi Wang, Charles Findling, Yanchen Wang, Felix Hubert, International Brain Laboratory, Alexandre Pouget, Erdem Varol, and Liam Paninski** 

## **Table S1. Mathematical notation, related to Figures 1 and 4 and STAR Methods** 

Throughout the main text, STAR Methods section, and supplemental information, we use the mathematical notation defined in Table 1. 

|**Model**||**Notation**|**Dimensionality**|**Definition**|
|---|---|---|---|---|
|RRR|||_N x T_|Single-trial neural activity|
||||_P_|Single-trial ground truth behavior|
||||_P_|Single-trial predicted behavior (decoder estimate)|
||||_N x R_|RRR model’s neural basis set|
||||_R x T x P_|RRR model’s temporal basis set|
||||_P_|RRR model’s intercept term|
||||_L x R_|Multi-region RRR model’s neural basis set for each brain region|
||||_L x T x P_|Multi-region RRR model’s temporal basis set shared across all regions|
||||–|Number of neurons in a session|
||||–|Number of time bins in each trial|
||||–|Number of trials in a session|
||||–|Dimension of the behavior of interest|
||||–|Rank of the (multi-session) RRR model’s<br>and<br>bases|
||||–|Rank of the multi-region RRR model’s<br>and<br>bases|
|BMM-HMM|||1|True behavior in trial_k_|
||||1|Single-trial, single-session decoder estimate in trial_k_|
||||2|Latent mixture assignment of trial_k_in a beta-mixture model|
||||_H_|Hidden Markov model’s latent state in trial_k_|
||||1|Probability of past observations<br>at state_h_in trial_k_|
||||1|Probability of future observations<br>at state h in trial_k_|
||||1|Probability of_y_at state_h_in trial_k_given|
||||1|Transition probability from state_h_in trial_k_to state_m_in trial_k + 1_|
||||_H_|HMM’s initial state distribution|
||||_H x H_|HMM’s transition probability matrix|
||||_H x 2_|HMM’s emission probability matrix|



|||_H_|–|Number of latent states in an HMM|
|---|---|---|---|---|
|LG-AR1|||1|True behavior in trial_k_|
||||1|Single-trial, single-session decoder estimate in trial_k_|
||||1|LG-AR1’s latent state in trial_k_|
||||1|Improved decoder estimate in trial_k_given|
||||1|LG-AR1’s observation model parameter|
||||1|LG-AR1’s dynamic model parameter|
||||1|Intercept term of LG-AR1’s observation model|
||||1|Variance of LG-AR1’s noise term|
||||–|LG-AR1 model parameters ( , ,<br>,<br>)|



**Table S2. The range of possible model and optimizer hyperparameters from which** _**Ray Tune**_ **randomly samples combinations, related to STAR Methods** 

|**Hyperparameter**|**Value Range**|
|---|---|
|RRR Rank|Randint(2, 50)|
|MLP Depth|Randint(1, 6)|
|MLP Hidden Size|[16, 32, 64, 128, 256, 512]|
|MLP Dropout Ratio|Uniform(0.1, 0.3)|
|Weight Decay|Log-Uniform(0.001, 1)|
|Learning Rate|Log-Uniform(0.0001, 0.01)|



## **Table S3. Computation time for single- and multi-session reduced-rank regression (RRR) models and MLPs, related to STAR Methods** 

For single-session models, we report the mean and standard error of training times (in seconds) across 58 individual sessions. For multi-session models, we report the total time required to train a single model on all 58 sessions. 

|**Time (s)**|**RRR**|**MLP**|
|---|---|---|
|Single Session|129.10<br>4.33|297.91<br>29.14|
|58 Session|6610.70|16526.76|



**==> picture [480 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Single-Session LG-AR1 Learn Oracle Priors from  Test Session … Learn Empirical Priors from  Training Sessions …<br>Transition<br>Oracle LG-AR1 Multi-Session LG-AR1<br>Single-Session BMM-HMM<br>Transition<br>Learn Oracle Priors from  Test Session … Learn Empirical Priors from  Training Sessions …<br>Ground Truth Behavior<br>Decoder Output<br>Latent Behavior<br>Latent Behavioral State<br>Oracle BMM-HMM Multi-Session BMM-HMM<br>Observed<br>Latent<br>Learned From Training<br>Ground Truth Behavior<br>Learned From Test<br>Ground Truth Behavior<br>Emission<br>Emission<br>Emission<br>**----- End of picture text -----**<br>


## **Figure S1. Graphical models for single-session, oracle, and multi-session LG-AR1 and BMM-HMM models, related to STAR Methods** 

The single-session LG-AR1 and BMM-HMM models learn parameters directly from the test session. In contrast, the oracle LG-AR1 and BMM-HMM use a two-step learning process. They first derive oracle priors from the ground truth behavior in the test set, and then use these priors to guide parameter learning on the test data (shown by gray arrow). The multi-session LG-AR1 and BMM-HMM follow a similar approach to learn empirical priors from ground truth behaviors in the training data, which are then used to constrain parameter updates on the test set (shown by gray arrow). This approach allows the multi-session models to utilize information from multiple training sessions while adapting to the current test data. 

**==> picture [480 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Choice Prior Wheel Speed Whisker Motion Energy B Gabors Static Gratings Running Speed<br>1.0 1.0 0.8 0.6<br>0.7 0.8 1.0<br>0.6 0.45<br>0.6 0.7 0.5<br>R2 R2<br>AUC Corr<br>Acc Acc R2<br>0.2 0.15<br>0.4 0.5 -0.5<br>0 0<br>0.7 0.5 0.3 0.4 -1.0<br> 2     5     10   15  2     5     10   15  2     5     10   15  2     5     10   15  2     5     10   15  2     5     10   15  2     5     10   15<br>Rank Rank Rank Rank Rank Rank Rank<br>**----- End of picture text -----**<br>


**Figure S2. Effects of model rank on decoding performance across different behavior variables, related to STAR Methods** 

For each behavior task in the IBL (A) and Allen (B) datasets, the violin plots display performance metric distributions across 10 sessions when decoding using different model ranks. Although all behaviors can be captured using lower model ranks, wheel speed and static gratings exhibit improved decoding performance at higher ranks. 

1 

**==> picture [480 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
A E<br>Target<br>Pred<br>Time (s) Time (s)<br>B Fourier Decomp. PCA Decomp. D Linear MLP LSTM RRR (S) F Fourier Decomp. PCA Decomp. H Linear MLP LSTM RRR (S)<br>1.0<br>500 10 500 10<br>0.6<br>0.8<br>0 0           5 0 0           5 0.4 0 0           5 0 0           5 0.6<br>C Frequency (Hz) PC G Frequency (Hz) PC<br>PC1 0.2 PC1 0.4<br>PC2 0 PC2 0.2<br>PC3 PC3<br>-0.2 0<br>PC4 PC4<br>-0.2<br>PC5 -0.4 PC5<br>FC1    FC2     FC3    FC4   FC5 0           2          4           6          8          10PC FC1    FC2     FC3    FC4   FC5 0           2          4           6          8          10PC<br>Whisker<br>Wheel Speed Motion Energy<br>Variance Variance<br>Spectral Dens. Spectral Dens.<br>R2<br>R2<br>**----- End of picture text -----**<br>


**Figure S3. Evaluating the reduced-rank regression model against baseline decoders in capturing the primary components of the target behaviors, related to STAR Methods** 

Examples of actual (“Target”) and predicted (“Pred”) behaviors for wheel speed (A) and whisker motion energy (E) from the reduced-rank regression model across five selected trials. Whisker motion energy exhibits higherfrequency fluctuations compared to wheel speed. 

Power spectral density (PSD) as a function of frequency is shown for the observed (“target”) and predicted (“pred”) wheel speed (B) and whisker motion energy (F) from the reduced-rank regression model, and decoding error (“error,” defined as target minus pred), averaged over 10 sessions. In addition, the variance explained by each principal component (PC) is plotted for the target, pred, and error. Both the low-frequency Fourier components and leading PCs account for most of the variance in the behavior signals. 

Heatmap showing the Pearson correlation between the first 5 PCs and the first 5 Fourier components (FCs) of wheel speed (C) and whisker motion energy (G). A clear one-to-one correspondence is observed for the first two PCs and FCs, indicating that the leading PCs capture low-frequency components in the behavior. 

Model performance ( _R_[2] ) for decoding wheel speed (D) and whisker motion energy (H) reconstructed from each PC of the observed behavior using baseline decoders. Decoding _R_[2] is generally higher for the leading PCs, which are associated with low-frequency Fourier components. The mean and standard deviation of _R_[2] across 10 sessions are shown for the first 10 PCs. 

**==> picture [480 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
110 –<br>80 –<br>50 –<br>20 –<br>**----- End of picture text -----**<br>


**Figure S4. Assessing the decoding improvement achieved by multi-region reduced-rank regression model relative to null distributions generated from imposter sessions, related to Figure 7 and STAR Methods** For each session with probe insertions in PO, LP, DG, CA1, and VISa, we create 10 “imposter sessions” from behaviors (choice and prior) of other mice in different IBL sessions. These are generated by concatenating trials across all analyzed sessions, excluding the session under consideration, then randomly selecting a chunk of _N_ consecutive trials (where _N_ matches the original session length) from the concatenated sessions. We obtain the original score from the real session, while the adjusted score is calculated by subtracting the decoding accuracy (or correlation) of the imposter sessions from the original score. Each bar shows the mean score from 10 imposter sessions, with error bars indicating one standard deviation of these scores. 

2 

**==> picture [480 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B Corr: 0.27 Corr: 0.33 C Transition Prob. Emission Prob. D<br>Corr: 0.55 Corr: 0.66<br>Corr: 0.57 Corr: 0.68<br>Baseline   Smoother  LGAR1 BMMHMM BMMHMM (M) BMMHMM BMMHMM (M) LGAR1 LGAR1(M) LGAR1 LGAR1(M) LGAR1 LGAR1(M)<br>BMM-HMM LG-AR1<br>E F<br>Oracle Single-Session Multi-Session AUC: 0.84 vs. 0.79 vs. 0.84 Corr: 0.89 vs. 0.76 vs. 0.78 Oracle Single-Session Multi-Session<br>   0                           50                  85                    Trial                   165                 200                         250     0                       50                     Trial                    150                    200<br>AUC: 0.79 vs. 0.75 vs. 0.79 Corr: 0.83 vs. 0.62 vs. 0.64<br>   0                           50                  85                    Trial                   165                 200                         250    0                       50                    Trial                   150                    200<br>AUC: 0.83 vs. 0.79 vs. 0.81 Corr: 0.94 vs. 0.82 vs. 0.86<br>   0                           50                  85                    Trial                   165                 200                         250    0                       50                    Trial                   150                    200<br>AUC: 0.70 vs. 0.61 vs. 0.71 Corr: 0.92 vs. 0.79 vs. 0.80<br>   0                           50                  85                    Trial                   165                 200                         250    0                       50                    Trial                   150                    200<br>Prior<br>Prior<br>Prior<br>Prob(R) Prior<br>Prob(R) Prior<br>Prior<br>Prob(R)<br>Prob(R) Prior<br>**----- End of picture text -----**<br>


**Figure S5. Relationship between LG-AR1 and post-hoc smoother, and across-session variability in parameter estimation and predictions of BMM-HMM/LG-AR1 models, related to Figure 4 and STAR Methods** (A) Comparison of prior decoding performance, measured by correlation, across the linear baseline, single-session LG-AR1, and a post-hoc smoother. Box plots display the minimum, maximum, median, and quartiles over 10 sessions, while bar plots show the mean correlation. 

(B) Predicted priors from the linear baseline, single-session LG-AR1, and post-hoc smoother are compared to ground truth in two example sessions. 

Comparison of parameter estimation accuracy for BMM-HMM (C) and LG-AR1 (D) models, measured by root mean squared error (RMSE), between single-session models (BMMHMM, LGAR1) and multi-session models (BMMHMM (M), LGAR1 (M)). Box plots show the minimum, maximum, median, and quartiles across 10 sessions, while bar plots show the mean RMSE. For the BMM-HMM, RMSEs for the transition and emission probabilities are computed for each matrix entry in Figure 4E and then averaged. 

(E) Additional examples of decoded right-choice probabilities from the oracle (pink), single-session (black), and multi-session (purple) BMM-HMM models across 4 selected sessions. 

(F) Additional examples of decoded priors from the oracle (pink), single-session (black), and multi-session (purple) LG-AR1 models across 4 selected sessions. 

3 

**==> picture [480 x 270] intentionally omitted <==**

**----- Start of picture text -----**<br>
A 0 No Lick   1 Lick   — Linear — BMM-HMM B C<br>    Accuracy: 0.69     Accuracy: 0.74     Accuracy: 0.66<br>    Accuracy: 0.90     Accuracy: 0.88     Accuracy: 0.81<br>Prob. Prob. Prob.<br>1.0 1.0 1.0<br>0.5 0.5 0.5<br>0 0 0<br> 0             20          Trial          50           70  0             20          Trial          50           70  0             20          Trial          50           70<br>D E F<br>    Accuracy: 0.48     Accuracy: 0.64     Accuracy: 0.53<br>    Accuracy: 0.60     Accuracy: 0.84     Accuracy: 0.60<br>Prob. Prob. Prob.<br>1.0 1.0 1.0<br>0.5 0.5 0.5<br>0 0 0<br> 0             20          Trial          50           70  0             20          Trial          50           70  0             20          Trial          50           70<br>**----- End of picture text -----**<br>


**Figure S6. Additional examples of using BMM-HMM to infer latent states in licking behavior for better predictions in Allen datasets, related to Figure 8** Comparison of the BMM-HMM model and a linear baseline in predicting behavioral responses (licks) to visual stimulus changes across six sessions, complementing the example shown in Figure 8I. For each session, we decode using neural activity from a subset of brain regions (DG, CA1, CA3, VISp, VISa, LP and TH), depending on which regions were recorded in that session. The inferred latent states are visualized as heatmaps, color-coded by the probability of each state. 

**==> picture [480 x 119] intentionally omitted <==**

**Figure S7. Scaling curves of multi-session reduced-rank regression models, related to STAR Methods** For each behavioral variable, we train both single-session and multi-session reduced-rank regression models using data from 5, 10, 20, 40, and 73 sessions, and evaluate performance on a fixed set of 5 test sessions. Each panel shows how the average decoding score across these test sessions changes with the amount of training data. 

4 

**==> picture [480 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
Rank        2       5       10      30<br>**----- End of picture text -----**<br>


**Figure S8. Performance of single-session reduced-rank regression (RRR) model as a function of neuron count and model rank, related to STAR Methods** 

We train single-session RRR on 48 IBL sessions with varying neuron counts to predict choice, prior, wheel speed, and whisker motion energy. Decoding performance is plotted against neuron count after excluding sessions with outlier metrics, with each dot representing one session. Colors distinguish different model ranks. To visualize the trends, we fit a logistic regression for choice and a third-order polynomial regression for the other tasks. Shaded areas denote the 95% confidence interval. For choice decoding, rank 2 achieves the highest performance when the number of neurons is fewer than 1500. For prior decoding, rank 2 is consistently the best across all neuron counts. For whisker motion energy, rank 2 outperforms higher ranks when the neuron count exceeds 1500. For wheel speed, larger model ranks lead to better performance with lower neuron counts. 

5 

