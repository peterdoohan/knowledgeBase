bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **The hippocampus as a small-world cognitive map** 

Jason Z. Kim,[1] _[,][†]_ James P. Sethna,[1] Itai Cohen,[1] _[,][†]_ and Weinan Sun[2] _[,][†]_ 

> 1 _Department of Physics, Cornell University, Ithaca, NY 14853, USA_ 

> 2 _Department of Neurobiology and Behavior, Cornell University, Ithaca, NY 14853, USA_ 

(Dated: February 8, 2026) 

## **Abstract** 

When a mouse perceives a hawk’s shadow, it may have only seconds to decide where to run, yet the safest refuge is often neither visible nor nearby. To survive, it must search its cognitive map quickly enough to choose among many possibilities, and accurately enough to avoid dead ends and hazards along the way. But what counts as “safe” changes over minutes to days as paths, refuges, and threats shift, so a cognitive map must be searchable not only over places but also over time. This highlights a core design problem: cognitive maps must preserve fine local structure for reliable action, yet remain globally searchable so that distant, useful solutions can be found efficiently in both space and time. The hippocampus is thought to support such maps, with population activity representing world states and their transitions—yet how these representations remain locally faithful while enabling efficient global search is not well understood. Here, we used a novel geometry-regularized autoencoder to model longitudinal calcium imaging from thousands of hippocampal CA1 neurons in mice learning a memory-guided navigation task. We discovered that the hippocampal population code achieves both local fidelity and global searchability through complementary mechanisms operating at different scales, yielding **small-world network structure** in the space of neural representations, with strong local clustering and a sparse set of long-range shortcuts that enable rapid access to distant states. At the population level, helical (rotation-plusdrift) dynamics of neural representations relative to past experience build new maps that preserve information about nearby positions in space and time while remaining distinguishable from earlier representations. At the cellular level, neurons with coordinated multi-field activity spanning distant representations create sparse, long-range shortcuts through the space of possible states. During synchronous population events in immobility, decoded activity often jumps to distant states in space, time, and task conditions, suggesting these shortcuts are engaged during offline processing. This functional organization, with implications for both neuroscience and artificial intelligence, sheds light on how hippocampal representations may be optimized for a fundamental challenge faced by intelligent systems: efficiently searching through accurate internal models of the world. 

## **1 Introduction** 

A fundamental challenge faced by intelligent agents, from foraging rodents to chess grandmasters, is how to search an internal model of the world to guide behavior. Consider a rat in a maze-like burrow network. To recover food cached weeks earlier, it must use memory to navigate among tunnels, exits, and chambers without physically checking each branch. Or consider a person planning a route through an unfamiliar city, mentally simulating turns and landmarks before taking a single step. This capacity for _mental navigation_ , the ability to efficiently search within an internal world model rather than through exhaustive physical exploration [1–3], is arguably what separates sophisticated cognition from simple reactive behavior. 

The notion of a _cognitive map_ , an internal representation that captures the relational structure of the environment, provides a conceptual framework for understanding how such mental navigation might be achieved [1]. An effective cognitive map must satisfy two fundamental requirements. First, it must accurately represent the structure of the environment, preserving the relationships between states so that mental traversal reflects real-world transitions. Second, for mental navigation to be useful, the map must support efficient search that scales gracefully as environments grow in size and complexity. Without such efficiency, mental simulation would not be fundamentally faster than physical exploration. 

The hippocampus offers a natural place to search for such organizational principles. It has long been implicated as the neural substrate supporting cognitive maps [4]. The landmark discovery of place cells, 

> †Correspondence: jk2557@cornell.edu (J.Z.K.), itai.cohen@cornell.edu (I.C.), ws467@cornell.edu (W.S.) 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

neurons that selectively fire at specific spatial locations, provided the first concrete evidence for neural encoding of an internal map [5]. Subsequent work has revealed that the hippocampus codes not only for spatial location but for a wide variety of experiences: temporal intervals [6], social identity [7, 8], conceptual categories [9, 10], and task-relevant abstract variables [11–13]. These findings support the broader conception of the hippocampus as encoding a general-purpose cognitive map [14]. 

Yet a critical question remains: **how is this map organized to support both accurate and efficient mental navigation?** Foundational work mapping single-neuron activity onto pre-selected variables such as position [5,15] established what the hippocampus encodes, but leaves open how the population code is organized to support computation. Focusing on individual neurons provides only a partial view of the collective code [16]. To model the collective code researchers have turned to nonlinear dimensionality reduction techniques such as UMAP [17] and isomap [18] that produce low-dimensional embeddings of neural data, where the embedding coordinates are meant to reflect systematic changes in population activity associated with encoded variables. These embeddings, however, often lack the geometric fidelity needed to characterize representational structure: small displacements in the embedding can correspond to large, irregular changes in the predicted neural activity [19,20], making it difficult to quantitatively study the organization of the map and how it supports navigation. 

Here, we address this issue by using Γ-autoencoder (Γ-AE), a novel technique that uses differential geometry to build manifold models that more faithfully preserve distances, angles, and directions when mapping between the latent embedding coordinates and neural population activity [20]. We apply this method to longitudinal calcium imaging from thousands of hippocampal CA1 neurons tracked across weeks in mice learning a memory-guided navigation task [13]. 

We discover that the hippocampal cognitive map has **small-world network structure** [21] in representational space, combining dense local neighborhoods with a limited set of long-range “wormhole” links between distant states. We trace this organization to two complementary features of the population code. First, helical representational dynamics, in which population activity systematically rotates through state space while drifting across experience, maintain local continuity while keeping representations from different days distinguishable. Second, generalized state fields, in which coordinated multi-field activity recurs across otherwise distant neighborhoods, create sparse long-range shortcuts. Together, these mechanisms suggest an organizational principle by which hippocampal representations can support efficient search through accurate internal world models. 

## **2 Quantitative model manifold of hippocampal cognitive maps** 

To study the collective representation of the mouse hippocampus, we use calcium imaging data of hippocampal CA1 neurons from a recently published study [13]. Briefly, the activity of thousands of neurons expressing the calcium indicator GCaMP6f was tracked across multiple days for 11 mice as they learned to navigate a virtual reality maze (Fig. 1A). The maze consisted of looped linear tracks with three zones: indicator, near reward 1 (R1), and far reward 2 (R2). Between trials a 2 s dark teleportation period was used to reset the track. For each trial, one of two indicator markers were randomly selected, which determined the location where the mouse needed to lick in order to receive a water reward (two-alternative cue-delay-choice (2ACDC) task) (Fig 1B). No penalty was applied for incorrect licking. Mice typically learned the task within 6-15 days across hundreds of trials. For all animals, cranial windows were implanted to image the neural activity of CA1 neurons in the dorsal hippocampus (Fig. 1C, Left), and the activity for each neuron was registered across days, allowing longitudinal tracking of activity across time (Fig. 1C, Right). 

We use these data across all days for each animal to model the cognitive map as a low-dimensional geometric manifold. Each image frame of _N_ neuron activations defines a point in an _N_ -dimensional space of population activity, whose _i_ -th coordinate is the measured activity of neuron _i_ (Fig. 1D). We model these data using a novel geometry-regularized autoencoder (Γ-AE) [20] that constructs a low-dimensional geometric manifold directly in the high-dimensional space of neuron activity (Fig. 1E, see Methods). In this framework, the latent variables define a coordinate system for the manifold, so that changes along latent dimensions correspond to movement along the manifold in data space. By explicitly preserving local distances, angles, and directions, Γ-AE yields a quantitative and interpretable map of population activity (Fig. 1F–H, see Methods). 

2 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 194] intentionally omitted <==**

Figure 1: **Constructing a quantitative model manifold of hippocampal cognitive maps** . ( **A** - **C** ) Experimental setup (panels adapted from Sun et al. [13]). ( **A** ) Schematic of the experimental setup comprising a mouse navigating a virtual reality maze atop an air-suspended ball with simultaneous calcium imaging of hippocampal CA1 neurons. ( **B** ) Diagram of the linear maze with different indicator markers and corresponding reward locations. ( **C** ) Image ROI (left) and time traces of activity for a subset of neurons (right). ( **D** ) Schematic of constructing a low-dimensional geometric manifold of high-dimensional neuron activity. ( **E** ) Architecture of the geometry preserving autoencoder. ( **F,G** ) Schematic of the latent-space coordinates (left), the corresponding manifolds from an autoencoder that does not preserve geometry in the space of neural activity (center), and from an autoencoder that does preserve geometry (right), demonstrating more accurate preservation of latent-space distances, angles, and direction. This geometry preservation results in a more quantitative and interpretable model, ( **H** ) which enables the principled study of how the map is structured to enable effective navigation. 

## **3 Emergent variables of position, task belief, and trial** 

To test the correspondence between the cognitive map models and the virtual maze we plot the projection of neural activity onto a 3-dimensional latent space learned by Γ-AE for a representative mouse in Figure 2 (see Methods). To identify the salient variables for which the hippocampus codes, we plot the embedding points for all frames on day 8, colored by the different track markers. For clarity, we plot the near trials opaque in Fig. 2A and far trials opaque in Fig. 2B. We observe that locally, data that vary along one direction in the latent space correspond to the mouse’s position along the track. We find that the cognitive map model arranges the neural firing patterns along the track in a manner that correctly organizes the maze marker sequence and topology for both task conditions. Additionally, we observe that, at each point, the data corresponding to the two tracks separate along a second direction throughout learning for the region spanning the indicator zone through the R2 zone (see Fig. 7 for the embeddings of the final day for all animals). 

Interestingly, we also observe trials where the cognitive map model starts along a trajectory associated with one task condition, but switches to the trajectory associated with the second task condition (Fig. 2C). Such switches often occur during error trials (licking at the wrong reward zone) or when the mouse is being inattentive (running without licking). This path switching on the manifold accompanied by incorrect licking behavior provides evidence that the mouse is confused about the task condition it thinks it is in. Collectively, these results indicate that each pathway on the manifold corresponds to the task condition in which the mouse believes itself to be and that the separation between these tracks, a second local direction in the latent space coordinates, represents how much the mouse believes each portion of the track belongs to each task condition (task belief). 

To identify an additional variable for which the hippocampus codes, we plot the embedding vectors for both days 7 and 8, and observe that all track markers and the track topology are strongly aligned between days (Fig. 2D), thereby largely preserving the first two dimensions of position and task condi- 

3 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 413] intentionally omitted <==**

Figure 2: **Low-dimensional geometry of neural representation along position, task, and trials** . ( **A** ) Low-dimensional embedding of hippocampal activity and evolution from _∼_ 5000 neurons in a 3-D latent space on day 8, colored by track marker, with data from the near trials opaque and the far trials transparent. ( **B** ) Same embedding with near trials transparent and far trials opaque. ( **C** ) Same embedding, with trials containing correct licking behavior transparent, and incorrect licking behavior during near trials opaque, showing most of the opaque points switching from the correct near trials to the correct far trials. ( **D** ) Embedding from days 7 and 8, colored by task marker showing near perfect overlap of track marker across days, and ( **E** ) rotated view showing a consistent direction of change in embedding coordinate within- and between-days, ( **F** ) which persists across all 9 days. ( **G** ) Embedding from all days colored by task marker with near trials opaque, and ( **H** ) far trials opaque, showing consistent alignment of task markers between all days. ( **I** ) Embedding data binned across position (3cm/bin) and trials (20 trials/bin) for near (transparent) and far (opaque) conditions. 

tion. By rotating the viewing angle and coloring the points now by the first- and second-half of trials on each of days 7 and 8 (Fig. 2E), we observe that the data consistently vary along a third geometric axis as a function of trial number, which is preserved within and between days. By plotting all of the points from all days and coloring the points by the trial number, we observe a consistent and continuous gradient along this third geometric axis that persists across a whole week (Fig. 2F). By plotting all of the points and instead coloring them by the task markers, we additionally observe that the data from the near task conditions (Fig. 2G, opaque) and the far task conditions (Fig. 2H, opaque) remain separated along a direction of task belief through trials, which can be decoded to and associated with 

4 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

a unique pattern of neural activity. Collectively, these analyses demonstrate that a specific point on our model’s latent-space corresponds to a mental state of track position, task belief, and trial number (time). This structure is consistent with prior work showing that hippocampal population activity can exhibit disentangled codes with approximately orthogonal components across task variables and that context-related structure can remain preserved along dimensions largely orthogonal to ongoing drift [22, 23]. Importantly, by preserving local distances, angles, and directions, our latent space captures and reveals the quantitative relationships between different coded variables on the manifold in the learned representational space. While our model of the cognitive map consists of three local directions, the vast majority of the mouse’s experienced mental state exists on two distinct task conditions (near, as in Figs. 2A,G, and far, as in Figs. 2B,H, rather than in between, as in portions of Fig. 2C), each of which predominantly occupies a 2-dimensional surface parameterized by position and trial (time). As such, for ease of analysis, we define the model of the mouse’s _experience_ on the cognitive map as the two surfaces formed by averaging the coordinates of the data points embedded in the latent space according to discrete bins of position (3cm) and time (20 trials) (Fig. 2I, see Methods). This representation allows us to quantitatively project the maze coordinates through time onto these surfaces (grid lines in Fig. 2I). 

## **4 Emergent manifold rotation and drift contextualize new representations relative to unique past experiences** 

These surfaces of experience provide insight into how the representation of the maze within the latent space is advanced across trials (Fig. 3A). Specifically, each point on the surface corresponds to a track position and trial number for a particular task condition. Interestingly, the grid lines are not perpendicular in the latent space coordinates but instead form an acute angle, _θ_ (Fig. 3A,B). A position 3 cm forward on the track is represented by a neighboring horizontal grid point to the right (Fig. 3B). The same position, 20 trials later is represented by a neighboring grid point to the upper right (Fig. 3B). Thus, the representation of the same position along the track in successive trials is shifted along the position direction in the latent space. This locally acute angle and the accompanying shift at most points on the surface produces a consistent global rotation of the mouse’s experience along the track position throughout the evolution of trials. We repeat the procedure of constructing the binned manifolds for all animals (see Methods), and compute the distribution of _θ_ for all positions, trials, and task conditions for all animals (Fig. 8, _n_ = 11). We find that this angle is statistically significantly acute (with an average angle of _θ ≈_ 77 _._ 2 _[◦] ±_ 2 _._ 7 _[◦]_ ; _p <_ 0 _._ 001). This angle, scaled by the lengths of the position vector and trial vectors, can be used to determine the advancement per trial. We find that the advancement was statistically positive with an average of _∼_ 0 _._ 43 mm/trial or 5 cm per day (Fig. 9, _p <_ 0 _._ 001). 

To provide intuition for this consistent global rotation of the manifold in the space of neural activity we consider the neural firing patterns associated with one task condition during one trial, which correspond to a ring in the space of neurons (Fig. 3C). If we consider fictive firing patterns from three individual neurons a, b, c, and their activity as a function of position along the track, a pure rotation would result in a translation of the firing pattern to earlier positions along the track. In other words, the collective firing pattern would simply shift backwards so that the same pattern of firing comes to represent positions further down the track (i.e. backshift [24, 25]). Thus, pure rotation would not result in any new firing patterns beyond those experienced during that trial. The vertical shift along the manifold of experience for different trials must therefore arise from new patterns of firing that are distinct from those used to represent earlier trials. We associate both changes in the neuronal patterns of activity over time with what is often referred to as representational drift [26–29]. Here, we designate the component of the change in activity aligned with positions as pure rotation, and the remaining component, which is orthogonal, as pure drift (Fig. 3D, top left). Together, rotation and drift produce a helical progression of representations across experience. Pure drift can arise from numerous sources including: changes in the shape of the place field, the formation or removal of place fields, and different rates of translation (Fig. 3D, bottom left). We find that all of these sources are observed in individual neuron recordings, and are captured by the decoded model activity (Fig. 3D, right, see Fig. 10 for more examples, and Fig. 6 for a single neuron decomposition). The fact that both rotation and drift exist implies that there is information from adjacent positions in previous trials that is preserved in 

5 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 244] intentionally omitted <==**

Figure 3: **Manifold rotation and drift contextualize current state relative to unique past experiences.** ( **A** ) Position- and trial-binned manifolds for the near (top) and far (bottom) task conditions, with each bin colored by whether the angle between the vectors along position and trial is acute (blue) or obtuse (green). ( **B** ) Zoomed-in view of one manifold section and schematic showing the angle, and the decomposition of the evolution across trials into a pure rotation and pure drift. ( **C** ) Schematic of the trajectory in the space of neuron activity for two consecutive trials undergoing pure rotation (top), associated with a consistent backshift of place fields (bottom). ( **D** ) Same schematic for two consecutive trials undergoing rotation and drift (top left), associated with a common component of backshift and a differential change in the place fields, respectively (bottom left), and example activity across position and trials for two neurons from the data and decoded from the 3D latent space model (right). ( **E** ) Calculation of the vectors of the change in activity over position (left) and trial (right) of three out of _∼_ 5000 neurons that visually co-vary. ( **F** ) Schematics detailing changes in activity across position and trials that are uncorrelated producing pure drift in the latent and data space (top), and perfectly correlated producing pure rotation (bottom). The empirical distribution at the specific position and trial in ( **E** ) is moderately correlated producing both rotation and drift (middle). 

(rotation), and also distinct from (drift) the current representation, thereby allowing past experiences to provide an explicit context for current representations. This encoding is reminiscent of successor representations previously observed in hippocampal CA1 neurons [30,31], but generalizes to the population code which we thus term _generalized condensed representation_ (GCR). Intuitively, GCR means that a state is represented together with a “compressed” imprint of its local neighborhood in task space. 

To quantify how the generalized condensed representation emerges from the population code we begin by plotting the decoded model activity of three neurons that are active along a _∼_ 100cm length of track. We then compute the change in activity with respect to position (Fig. 3E, left) and trials (Fig. 3E, right) at the midpoint of this track segment. For pure rotation, the activity profile for each neuron would translate by the same amount per trial, and the slope of the curve at the midpoint would be directly proportional to the change in activity at a later trial. The fact that the curves for different trials are not identical translations along position indicates that there is a component of pure drift (gray curves, Fig. 3E, right). We repeat this analysis for all the neurons at this midpoint and plot the slope (denoted ∆ _a/_ ∆ _p_ ) versus the observed change across trials (denoted ∆ _a/_ ∆ _t_ ) and connect their distribution to the components of pure rotation and pure drift on the manifold in Fig. 3F. A distribution that is uncorrelated (Fig. 3F, top) would correspond to pure drift, or _θ_ = 90 _[◦]_ . A distribution that is perfectly correlated (Fig. 3F, bottom) would correspond to pure rotation, or _θ_ = 0 _[◦]_ . For the distribution at the midpoint of this track segment, we find a strong but not perfect correlation (Fig. 3F, middle) 

6 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

indicating components of both rotation and drift. Interestingly, in this model, even if every neuron’s activity profile were simply shifting, if the shifts happen at different rates, then the distribution would not be perfectly correlated, and the collective representation would drift. This analysis demonstrates that a single neuron measurement is insufficient for studying the structure and evolution (e.g. rotation and drift) of the collective code. 

## **5 Small-World Architecture of the Hippocampal Cognitive Map** 

How, then, does the population code emerge from the activity patterns of individual neurons? To gain intuition, we plot the modeled activity patterns of individual neurons in the latent space. When we look at the activity of a single neuron (e.g. cell 2034) prior to binning, we find it can be active in multiple regions of the latent space (Fig. 4A, left). We represent the activity level of the model’s prediction of the neuron’s activity using iso-surfaces as shown in Fig. 4A, right. A similar analysis conducted on other neurons also shows multiple regions of localized activity in the latent space, which can be different for different neurons (Fig. 4B, left). This framework generalizes the idea of place fields, where neurons have localized activity in spatial coordinates that parametrize physical space, to one of generalized state fields (GSFs, see Methods), where neurons have localized activity and statistically significant local maxima of that activity (GSF peaks, see Methods) in the latent space that parametrizes the cognitive map. We also find that many cells exhibit multiple regions of activity (Fig. 4B, top right) that encompass a variety of the latent space volume (Fig. 4B, bottom right). The picture that emerges is of a code that arises from the firing of multiple neurons that have locally overlapping active regions within the latent space. As the manifold of experience moves through a particular coordinate within the latent space, the collective code consists of all the neurons that are active at that coordinate. 

Interestingly, we find that when multiple neurons are active at one latent space coordinate, they are statistically more likely than chance to also be active at different latent space coordinates (Fig. 4C, left), suggesting that the neural code may have additional structure that results from the co-firing of neurons. Specifically, we consider the peaks of all GSFs in the latent space, query them one by one (Fig. 4C, left red), identify the neurons associated with the _K_ = 200 nearest neighboring GSF peaks (Fig. 4C, left teal), and see whether the remaining GSF peaks of those neurons are (Fig. 4C, left green) or are not (Fig. 4C, left black) clustered in a statistically significant way (see Methods). In general, we observe that many neurons with peaks in the neighborhood of the query also have significantly clustered co-active peaks elsewhere in the latent space, and that these co-active peaks can be far from the query (Fig. 4C, right). This analysis provides evidence that the collective code contains additional structure where a statistically significant subset of the neurons representing one latent space coordinate are also collectively active at _different_ and _distant_ latent space coordinates, which sometimes correspond to very different spatial locations and are separated by many days. Viewed as a graph over latent-space neighborhoods, this combination of strong local clustering and a sparse set of long-range links yields a small-world organization [21] of the learned representational space (Fig. 4C, right; see Methods). 

To test whether long-range links exist not just in the model of the cognitive map, but also between distant regions of physical space and time, we return to the experimental data to determine if there are a statistically significant number of neurons that co-fire at multiple positions on the track. It is well known that a single neuron can fire at multiple positions over a single day (Fig. 4D, see Methods). Based on our model predictions (Fig. 4C), we hypothesize that neurons that co-fire at a specific query position, rather than firing randomly across positions and days (Fig. 4E, Hypothesis 1), will systematically co-fire at specific track positions and perhaps even other days (Fig. 4E, Hypothesis 2). Indeed, for neurons firing at one specific query position, we observe that a statistically significant subset of them also fire at different regions and on different days (Fig. 4F, see Methods, and Fig. 11 for raw unfiltered activity across single trials for these neurons). We repeat this analysis using each position and day bin as the query and compute the bins that contain a statistically significant number of neurons that co-fire. We plot a graph of bins across all positions, task conditions, and days, where edges exist from each query bin to other bins that have a significant number of co-firing neurons, and find that approximately 1% of the links in the graph are associated with long-range connections (Fig. 4G, left). We identify such links in the graphs of all animals, and further find that the vast majority of these long-range connections are not captured using the same procedure on a smaller subsample of neurons (Fig. 12). Thus, in 

7 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 390] intentionally omitted <==**

Figure 4: **Small-world architecture of the cognitive map from the model and data** . ( **A** ) Model activity of a single cell (2034) decoded from the embedded data points in the latent space (left), and isosurfaces of that same cell’s activity in the full latent space volume (right). ( **B** ) Isosurfaces of volumes with high single-cell activity for multiple neurons that tile the latent space we term Generalized State Fields (GSFs, left), and the distribution of GSF peak number (top right) and fraction of the latent space occupied by GSFs (bottom right). ( **C** ) Example of one query GSF peak (left, red), its nearest _k_ = 200 neighbors (teal), the other GSF peaks of the query and neighbor neurons (co-peaks, black and green dots), and the co-peaks that are significantly clustered (green). Adjacency matrix of the small-world graph with connections between GSF neighborhoods when the significant co-fields of one neighborhood overlap with another neighborhood (right). ( **D** ) Rate map across positions and days for one neuron with marked peaks (red, top), and example trace from one day (bottom). ( **E** ) Schematic of one hypothesis of peak organization where co-peaks of neurons that have peaks at the query are randomly dispersed within and between days (left), _versus_ another hypothesis where co-peaks are systematically organized (right). ( **F** ) Raster plot of neuron peaks for neurons that fire at the query, and with significant peak counts at different positions on the same day (left) and earlier day (right). ( **G** ) Connectogram where the nodes are position and day bins, and edges exist between the query bin and the statistically significant co-peak (left), and observed _versus_ degree-sequence preserving null distribution of small-world coefficient for all animals (right). 

accordance with the model prediction, we find significant nonlocal co-activity of neurons at multiple and distant locations. This connectivity map is reminiscent of, and is significantly characterized as, a small-world network (Fig. 4G, right, _p <_ 0 _._ 001 for all 11 animals, see Methods). 

8 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **6 Effective navigation** _**via**_ **accurate and efficient maps** 

**==> picture [488 x 362] intentionally omitted <==**

Figure 5: **Accurate and efficient maps built compositionally and leveraged during navigation** . ( **A** ) Schematic of compositionally reconstructing a decoded point on the surface of experience using decoded bins from past trials and other positions, while looking at different neuron subsets. ( **B** ) When all neurons are used, the reconstruction weights are skewed towards further positions on the track on earlier trials (left). Summing the weights over trials, and repeating this process for all positions on the same trial bin, we find that the weights are consistently skewed towards future positions on the track (right). ( **C** ) When only neurons with many GSF peaks are used, the weights are distributed in discrete and distant clusters throughout the surface (left), leading to jumps in decoded positions (right). ( **D** ) Schematic of compositionally decoding synchronized calcium events (SCEs) which are activity patterns when the mouse speed was zero and was not licking. ( **E** ) Examples of significant reconstruction coefficients (red boxes) from two SCEs that decode close to the animal’s true position (black box) and day. Other examples of significant SCE coefficients that decode ( **F** ) remotely to the other task but contiguously in position and day, ( **G** ) contiguously and remotely in all variables, ( **H** ) and distributed and remote in all variables. ( **I** ) Statistically significant overlap between significant SCE reconstruction coefficients and one step down the small-world graph (left), and observed _versus_ null distribution of the overlap score for all animals (right). 

This small-world network connectivity suggests avenues for the brain to modulate the neural code to emphasize different features, short _versus_ long-range connections of the cognitive map. One possible signature for mental navigation from one state to another is for the latter state to be associated with a pattern of activity that is strongly related to that of the former state. Using a compositional approach, we reconstruct the activity pattern at a specific state using a non-negative weighted sum of the patterns at other states, and use the weights as measures of the strength of relation between the 

9 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

states. Specifically, for a position and trial bin on our surface in the latent space, we decode that point to a pattern of neuron activity, and reconstruct that pattern using the decoded patterns of activity for other position and previous trial bins as a basis (Fig. 5A). Within this framework we find that different states can become strongly related when looking at different subsets of the neurons. 

When all of the neurons are used, we find that the strongest weights begin centered around the point to reconstruct for the same trial bin, and shift towards further positions along the track for earlier trials (Fig. 5B, left). Summing the weights across trial bins and repeating this procedure by reconstructing each position, we find that from any particular position to reconstruct, the vast majority of the weights (light blue points) lie immediately ahead and behind that position (Fig. 5B, top right), with a significant skew ahead (Fig. 5B, bottom right). This skew towards upcoming states is reminiscent of successor representation (SR, see Fig. 13 for simple example of SR population geometry), whereby an agent stores information not just about its current state, but also expectations of future states further down the track. In our analysis, this expectation emerges collectively from the previously described helical dynamics of manifold rotation and drift _via_ generalized condensed representation (Fig. 3) that condenses information with respect to the collective neural firing patterns associated with past states, which can represent more general information beyond simple physical variables. 

When instead we use a subset of neurons comprising those with greater number of GSF peaks for reconstruction, we find that the strongest weights no longer extend locally and continuously from the point to reconstruct, but rather in large clusters with discrete jumps in position and trial bins (Fig. 5C, left). Repeating this analysis by reconstructing all positions for the same trial bin and summing the weights across trials, we indeed find that there is much less weight locally immediately ahead and behind the current position, and much more weight distributed in clusters at distant positions (Fig. 5C, right). Hence, by looking at distinct subsets of neurons, different states can become strongly related, potentially enabling the brain to dynamically tune between modes of accurate local representations and efficient long-range search in the cognitive map architecture. 

Indeed, we find evidence that the mouse leverages such distinct modes when the animal pauses during the task, which is often associated with memory consolidation and planning rather than active task solving [32]. Specifically, we look at activity patterns called _synchronized calcium events (SCE)_ that occur when the mouse is stationary (speed = 0) and is not licking. Studies have shown that SCEs, recorded using calcium imaging, significantly co-occur with electrophysiologically measured sharp wave ripples (SWR) [33,34], which are fast sequential neuronal firing patterns associated with consolidation and planning [32]. To decode whether these SCEs contain some component of a previously experienced position and task condition, we again compositionally reconstruct each SCE as a non-negative weighted sum of the neuron activity patterns associated with each position and day bin (Fig. 5D), and only keep weights that are statistically significant under a shuffle test (see Methods). Similar to the local reconstruction on the surface of experience (Fig. 5B), we find that some SCEs decode to nearby states (Fig. 5E, red boxes) close to the animal’s actual position and day (black box). These SCEs that have locally decoded states resemble sequential reactivation patterns often observed in SWRs [32]. Similar to the nonlocal reconstruction on the surface of experience (Fig. 5C), we also observe SCEs that decode remotely and non-contiguously from the animal’s position on the same day (Fig. 5F), resembling recent findings of super-diffusive SWR [35,36]. Finally, we also observe SCEs that decode completely remotely in position, task condition, and across several days (Fig. 5G,H), consistent with recent findings that offline ensemble reactivation can link memories formed days apart [37]. 

Finally, we look for additional evidence that these SCEs are leveraging the small-world connectivity of the cognitive map (Fig. 4). One possible signature of this leveraging is for the significantly decoded bins of each SCE to be connected to each other along an edge of the small-world network of the cognitive map more often than by chance, indicating a significant alignment between the SCE and the map. To measure this alignment for each SCE, we compute an SCE overlap score as the correlation between the significantly decoded SCE bins (Fig. 5I, left, red boxes), and the bins that are one connection away from those significant bins on the small-world graph (Fig. 5I, left, purple squares). For SCEs containing four or more significant decoding weights, we find that all animals have a statistically significantly higher empirically measured overlap score than under a shuffle test (Fig. 5I, right, see Methods). Hence, not only does the architecture of the cognitive map support locally accurate representations and efficient search which can be accessed using different subsets of neurons, but we also provide evidence suggesting 

10 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

that these two modes are both used and leverage the small-world architecture in SCEs during offline processing. 

## **7 Discussion** 

In this study, we use Γ-AE [20] to obtain a low-dimensional and geometrically faithful model of the cognitive map in hippocampal CA1 population activity across weeks of learning [13], thereby capturing how task states are quantitatively related in population activity space. We find that this map has small-world organization [21,38]: strong local clustering preserves fine structure, and a small fraction of nonlocal bridges provides shortcut access between otherwise distant states. Crucially, this smallworld structure is not in the anatomical wiring, but in the functional space of representations: how population activity states relate to each other. We trace the local component to helical (rotationplus-drift) representational dynamics across experience, and the long-range component to coordinated multi-field structure captured by generalized state fields that tile the cognitive map. Immobilityassociated synchronous population events decode to remote states whose locations align with this bridge structure, connecting representational topology to offline population dynamics. Below we discuss these two mechanisms and their implications. 

## _7.1 Local structure from helical population dynamics_ 

The dense local neighborhoods of the cognitive map arise from helical population dynamics. Across experience, the population manifold rotates with respect to past experiences in a coherent low-dimensional way, coupling nearby states across trials so that each state carries structured information about its local neighborhood in task space. At the single-cell level, individual neurons exhibit a wide range of experience-dependent changes, including place-field backshift, skew, drift, and shifts in reliability [22,24–27,39–47]. Our framework provides a population-level lens on this diversity: heterogeneous single-neuron changes collectively reveal coherent low-dimensional structure that would be difficult to infer from any single cell. 

This structured coupling connects naturally to predictive-map ideas such as the successor representation (SR), in which each state is represented as a vector encoding expected future state occupancies, relative to the external environment, under the current behavioral policy [30, 31]. The SR provides a powerful framework for understanding how hippocampal representations support flexible planning, and recent work has shown that SR-like structure can emerge from biologically plausible learning rules, including spike-timing-dependent plasticity (STDP) operating within theta sequences and sequential predictive learning during behavior and replay [48–51]. Coherent rotation across experience generates what we term the _generalized condensed representation_ : a geometric arrangement of the population manifold on which each state’s position reflects its context not with respect to the external environment, but rather with respect to the population manifold from previous experiences. This provides a neural substrate through which predictive relationships, consistent with successor representation principles, could be read out from population geometry. 

Decomposing representational change into a rotational component and an orthogonal drift component clarifies the division of labor: rotation preserves and re-expresses structure from prior experience, whereas drift introduces new patterns that expand representational capacity and support context separation across days and task states. This functional role for drift is consistent with a growing body of work suggesting that representational drift serves multiple computational purposes, including continual learning, adaptation to changing environments, and robustness to synaptic perturbations [28, 29, 52]. Helical dynamics thus provide a locally navigable scaffold for the cognitive map. But local continuity alone does not support efficient search across distant states; for that, the map requires shortcuts. 

## _7.2 Long-range bridges from generalized state fields_ 

The sparse long-range bridges that complete the small-world architecture arise from generalized state fields. Localized “fields” have long been used to describe hippocampal coding of position and time, and have been extended to task-relevant abstract variables [5, 6, 12]. Our GSFs generalize this idea by defining fields directly in the geometry of the representational space: localized regions of latent 

11 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

coordinates with high decoded activity for a neuron, spanning variation across task position, condition, time, and any other physical and non-physical variable represented in the population code. This provides a compact description of localized structure even when the intrinsic dimensions of the code are difficult to specify a priori. 

Multi-field firing is commonly observed in hippocampal neurons, especially in extended environments and complex tasks [53, 54]. In our framework, multi-field structure becomes a computational feature because it can expose nonlocal links between distant states. The crucial observation is coordination across neurons: cells that co-fire in one neighborhood tend to co-fire again at specific distant neighborhoods, where “distant” can mean separated in physical space, across days of learning, or even in the representation space of neural activity comprising the cognitive map. These coordinated co-activations create statistically significant nonlocal overlaps that act as shortcut edges in representational space. The long-range bridges are sparse (roughly 1% of edges) and appear to be driven by a relatively small subset of neurons. Detecting such sparse structure likely requires the large-scale longitudinal recordings that have only recently become feasible (Fig. 12). 

Our observation that neurons with overlapping primary fields tend to exhibit _coordinated_ secondary fields (i.e., nonlocal co-firing structure) appears, at first glance, to differ from prior work arguing that multi-field structure is largely independent across cells. In particular, Rich _et al._ reported that in a very large, largely homogeneous linear environment, the number and locations of CA1 place fields were well explained by a stochastic model with minimal evidence for structured co-activation across distinct fields [53]. Subsequent studies have nevertheless highlighted conditions under which hippocampal coding exhibits additional structure, including experience-dependent coordination among neurons with _path-equivalent_ (repeated) fields across related locations in environments with repeating elements [55], non-random _anatomical_ clustering of CA1 neurons with similar field locations (often near salient task features and goals) [56], context-dependent structure in CA1 coactivity dynamics that carries information beyond single-cell tuning [57], and stronger correlated “cell-assembly” organization in CA3 consistent with recurrent-network mechanisms that can stabilize and bind distributed representations [58]. A parsimonious reconciliation is that the coordinated component of multi-field structure is sparse and state-/task-dependent: it may be weak or difficult to detect during continuous theta-dominated running on a feature-poor track (and with limited simultaneous sampling), yet becomes more apparent in tasks with repeated salient zones, memory-guided demands, and large-scale population recordings across days. Importantly, our chance-level controls explicitly account for the empirical inhomogeneity of peak density across positions by using, and subsequently standardizing by, multinomial null probabilities estimated from the observed peak-density profile (Eq. 10; Methods §8.11), so the excess secondary co-firing we report cannot be attributed solely to shared occupancy or common cue/reward locations. Together, these comparisons suggest that multi-field firing can reflect both (i) an approximately stochastic _background_ component that supports broad coverage once neuron- and location-specific propensities are accounted for, and (ii) an additional, sparse _coordinated_ component that may include a baseline prior of sparse long-range associations and that can be selectively expressed or amplified by behavioral/physiological state, providing long-range associational links in the cognitive map, including across time (e.g., across trials and days). 

It is important to clarify the relationship between these bridges and the underlying manifold structure. The Γ-AE embedding yields a smooth, continuous manifold that faithfully tiles task variables; this manifold does not itself contain topological shortcuts or discontinuities, and has a defined pattern of activity associated with each latent space coordinate. The wormhole connectivity we describe refers to the statistical structure of coordinated firing: certain subsets of neurons are active together at multiple distant locations in the latent space, corresponding to distant locations on the manifold in the representation space, creating the potential for shortcut-like associations. 

Our observation that synchronous population events align with this shortcut structure suggests that long-range associations can be engaged, but the mechanisms controlling when and how remain open. One possibility is that the hippocampal population code is reshaped in a state-dependent manner, such that neuromodulatory signals [59], shifts in excitation–inhibition balance [60, 61], or changes in oscillatory regime [32] alter which neurons participate in the active ensemble and thereby emphasize more local versus more nonlocal structure. Recent computational work further proposes that entorhinal input can tune hippocampal sequence generation between locally diffusive dynamics and regimes with 

12 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

occasional long jumps via spectral control of grid-cell components [62]. In our data, the CA1 representational space itself is organized into dense local neighborhoods together with a relatively sparse set of nonlocal associations arising from coordinated multi-field structure, providing a concrete map-level scaffold that such control signals could engage. A complementary possibility is that plasticity mechanisms can rapidly imprint or strengthen these associations; for example, behavioral time scale synaptic plasticity (BTSP) can assign credit over seconds and could help establish or reinforce sparse long-range links across locations and days [63]. Second, downstream circuits could implement flexible readout strategies. A readout that uniformly weights hippocampal output might follow the smooth local geometry of the manifold, whereas one that selectively weights subpopulations carrying multi-location associations could access long-range structure directly. Evidence that distinct hippocampal reactivation types are accompanied by distinct prefrontal modulation patterns supports the plausibility of such flexible readout [64]. Together, reshaping the code and selecting the readout provide complementary routes for flexibly engaging the small-world architecture, and identifying the circuits and conditions that govern this modulation is an important goal for future work. 

Together, helical dynamics and coordinated multi-field firing produce a representational architecture with both local fidelity and global reach. A natural question is whether this architecture is actually engaged during hippocampal computation. 

## _7.3 Synchronous events traverse the shortcut scaffold_ 

A central challenge in interpreting representational topology is establishing functional engagement: a shortcut scaffold is only meaningful if the system can and does traverse it. A large body of work has shown that hippocampal activity can express nonlocal representations both online and offline [3, 65, 66]. During behavior, prospective sweeps have been reported at decision points [67, 68] and during goal-directed navigation, where theta sequences reflect current goals and rapidly cycle among possible futures [65, 69–71]. During immobility and sleep, sharp-wave ripple (SWR) events support diverse forms of sequential reactivation [32], including forward and reverse sequences [72–74], reactivation of spatially and temporally remote experiences [66,75], construction of never-experienced trajectories [67], anticipatory sequences preceding novel exploration [76], and sequences linked to goal-directed planning [2,77]. 

In our calcium imaging data, immobility-associated synchronous population events provide a window into how the shortcut scaffold may be expressed. During these events, decoded activity patterns frequently land at remote states, and the locations of these decoded states are predicted by multi-field organization. This indicates that the shortcut scaffold is not merely a static property of representational geometry but an accessible feature of hippocampal population dynamics. Because calcium imaging does not directly measure ripple oscillations, we treat these events as population-level phenomena that may overlap with replay-associated dynamics under appropriate conditions, rather than equating them oneto-one with electrophysiologically defined SWRs. This approach is consistent with previous calcium imaging studies of SCEs and their relationship to hippocampal reactivation [33,34,78]. 

Recent work emphasizes that replay spans multiple dynamical phenotypes [79]: stationary replay, where decoded positions remain at a single location [80]; diffusive replay, where decoded positions spread gradually through nearby states like Brownian motion [81]; and super-diffusive replay, where abrupt transitions carry decoded positions farther than random diffusion would predict [35,36]. Super-diffusive trajectories with intermittent long jumps are reminiscent of heavy-tailed step statistics often described as L´evy walks in animal search behavior [82,83]. L´evy-walk-like dynamics have also been reported in neural population activity [84], and in our framework such statistics could arise naturally from mostly local traversal punctuated by rare wormhole hops. Consistent with this picture, the transitions we observe during synchronous events span the full range from smooth local progressions to abrupt jumps across distant locations and days, with the latter resembling super-diffusive dynamics expressed at the coarser temporal resolution of calcium imaging. Notably, events can also appear weakly decodable if one uses a decoder restricted to the current day’s task and state space; in our framework, such “nondecodable” events are naturally expected when activity traverses temporal wormholes to representations from other days or contexts that lie outside that decoder’s basis, and therefore look random in today’s coordinates. Our results suggest that the small-world scaffold provides a representational structure 

13 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

that supports these diverse transitions, consistent with the view that hippocampal circuits, together with associated regions such as entorhinal and prefrontal cortex, are organized for efficient traversal. More broadly, our framework offers a way to interpret and categorize heterogeneous ripple-associated and ripple-like population events by relating their decoded trajectories to an explicit representational scaffold, potentially helping to identify additional, previously uncharacterized event phenotypes. 

## _7.4 Implications for world models and artificial intelligence_ 

The organizational principles we identify may inform the design of artificial world models and reasoning systems. A central challenge in modern AI is building systems that can plan, reason, and generalize efficiently. Large language models have demonstrated remarkable capabilities, but often require extensive test-time computation (chain-of-thought reasoning, tree search, or iterative refinement) [85–90] to solve complex problems. World models that learn latent dynamics for planning [91–94] face similar challenges: rolling out trajectories step-by-step through a learned latent space can be computationally expensive, especially for long-horizon, complex tasks. Our results suggest a concrete architectural hypothesis: efficient search emerges when representations preserve reliable local neighborhoods and include sparse nonlocal bridges that reduce the number of intermediate steps needed to reach distant states. 

This idea aligns with world-model agents that plan by rolling out learned latent dynamics. A small-world prior suggests keeping latent dynamics locally smooth and predictive, while learning a sparse set of long-range associations that can reduce rollout depth while preserving local consistency. For retrieval-augmented systems that perform multi-hop access over large knowledge stores [95,96], it motivates regularizing learned graphs toward high local clustering with shorter global paths. 

The clone-structured causal graph (CSCG) [97–101] provides a compelling framework in this context. CSCG addresses perceptual aliasing by learning a graph where “clones” of sensory states represent the same observation in different temporal contexts, explaining phenomena like splitter cells and contextdependent place coding. Recent work has shown that CSCG uniquely reproduces not only the final orthogonalized state representations observed in mouse hippocampus during learning, but also the step-by-step learning trajectory itself, unlike sequence models such as LSTMs or transformers [13]. Schema-based extensions further suggest how such graphs can be reused and rapidly re-grounded under higher-level abstract structure [101,102]. Our results suggest targeted extensions for planning: add a separate sparse set of long-range “portal” edges between clones that reliably co-occur across distant contexts (analogous to coordinated multi-field structure), impose a small-world prior that preserves high local clustering while introducing a limited number of shortcuts, and gate portal influence based on task demands or uncertainty [99,100]. 

The generalized condensed representation offers a further architectural parallel. In transformers [103], each token embedding compresses information from a context window into a current representation, enabling downstream computation without explicit retrieval of every prior token. Similarly, manifold rotation yields a predictive organization where each state carries condensed information about its local temporal neighborhood. This can be viewed as a geometric “context window”: each point on the manifold implicitly represents not just a single state but a neighborhood of temporally related states, packaged in a form that downstream circuits can use directly. This structured and dynamic compression may enable efficient readout and computation in downstream areas without requiring explicit replay or retrieval of the full sequence. Artificial systems might benefit from similar architectural motifs: learning representations where each latent state implicitly encodes its local neighborhood, reducing the need for explicit multi-step rollouts or attention over long sequences. 

## _7.5 Outlook_ 

This work opens several directions for future research. A key open question is how shortcut structure is controlled during behavior. Efficient planning requires controlling when to exploit shortcuts versus when to favor smooth local traversal. Tasks can be designed to dissociate local accuracy from global access: for example, requiring choices among multiple remote candidates that are not locally distinguishable, or introducing latent contexts and multi-day contingencies that force links across time as well as space. Simultaneous recordings of hippocampus, entorhinal cortex, and prefrontal cortex can test 

14 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

whether shortcut engagement depends on available abstraction scale and whether prefrontal signals bias traversal toward locally continuous paths versus nonlocal transitions. Causal perturbations can target population-level structure, including closed-loop disruption of immobility-associated events [61,104] and manipulations that selectively weaken coordinated multi-field structure while preserving local decoding fidelity. 

Small-world wiring can do more than shorten paths: in the right regime it can also approximate a hierarchical graph, because tightly connected local neighborhoods act like modules (or subtrees) and a sparse set of longer-range shortcuts effectively provides higher-level links between modules, enabling coarse-to-fine routing. Work on decentralized navigation further suggests that this hierarchy-like efficiency depends on how shortcut lengths are distributed, with distance-dependent rules (often close to a power law matched to the underlying space) making simple local, greedy steps reliably find short routes [105]. The hippocampal-entorhinal system offers natural multiscale building blocks for such an organization: grid cells are arranged into modules with distinct spatial periods [106,107] and representational scale varies systematically along the hippocampal long axis, including gradients in place-field size [108–110]. Against this backdrop, our observation of small-world structure motivates a clear next question: do the long-range links in the cognitive map follow the distance-dependent statistics that would make the network effectively hierarchy-like and optimally navigable, and how might learning and interactions with entorhinal and neocortical circuits shape that wiring? Relatedly, hierarchical representations can emerge from learning dynamics in deep networks, pointing to general principles that may also apply to hippocampal-neocortical organization across scales [111]. 

More broadly, treating representational topology as a shared design variable offers a productive path forward for the continuing exchange between neuroscience and AI. In artificial systems, shortcut density and gating can be manipulated directly and evaluated for their effects on reasoning and robustness. On the neuroscience side, a rapidly maturing suite of manifold and latent-variable methods [47, 112–115] has made it possible to characterize population-level geometric structure with increasing precision, revealing that neural codes across brain regions are organized on low-dimensional manifolds whose topology reflects computational demands [16, 116–118]. Tightening this loop, by testing topological predictions in neural circuits and translating the resulting principles into world-model architectures, may yield insights in both directions. 

15 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **8 Methods** 

## _8.1 Experimental dataset and preprocessing_ 

All analyses were performed on a previously published, publicly available longitudinal two-photon calcium imaging dataset from hippocampal CA1 collected during learning of a memory-guided virtual navigation task [13]. In that study, male and female Thy1-GCaMP6f mice were head-fixed in a virtualreality setup and trained on the 2ACDC task, in which an indicator cue early in a 230 cm corridor signaled whether reward would be delivered at a near or far reward cue later in the trial. Imaging data are available via Figshare (https://doi.org/10.25378/janelia.27273552), and an interactive visualization is provided at `cognitivemap.janelia.org` . 

We used the neural and behavioral variables provided with the release, including session-aligned behavioral position and trial type, as well as the processed neural activity traces for CA1 neurons tracked across sessions as described in [13]. Briefly, in the original work neurons were recorded with a two-photon random access mesoscope at 10 Hz across multiple adjacent imaging regions, and cells were registered across days using image registration and clustering procedures, with fluorescence traces extracted using Suite2p [119]. All analyses used deconvolved calcium traces extracted by Suite2p. Unless otherwise noted, our analyses focus on the core near- and far-reward trial types from the standard 2ACDC task and use the author-provided preprocessing and cell tracking without re-segmentation. 

## _8.2_ Γ _-Autoencoder Architecture_ 

Like many other techniques, Γ-AE [20] constructs a low-dimensional nonlinear manifold of the data. Unlike other techniques, however, Γ-AE selectively penalizes all distortions involved in the manifold geometry. We provide a discussion about Γ-AE in comparison to other techniques below. 

An ambitious goal is to use an autoencoder to construct a low-dimensional and interpretable model of the mouse’s cognitive map that elucidates the most salient variables and accurately represents the quantitative relationships between them. A common failure mode of many deep neural networks is that they are universal function approximators that form latent spaces whose projections into the space of neuron activity are highly distorted [120, 121]. Therefore, in the models they produce, distances and angles in the latent space are not preserved on the manifold in the space of neuron activity, making it difficult to formalize quantitative relationships between the discovered variables (Fig. 1F, left, center). In addition, small changes along a latent space coordinate can lead to wildly fluctuating neural firing patterns (Fig. 1G, left, center), which makes it difficult to understand what moving along a latent space coordinate means in terms of changes to the neuron firing patterns. Our geometry-preserving autoencoder, Γ-AE, corrects these distortions by adding additional terms in the loss function that selectively penalizes excess manifold nonlinearities (see below). This procedure produces a model manifold with enough nonlinearity to quantitatively represent the data while locally preserving distances, angles, and directions when mapping latent coordinates to the manifold in data space. Preservation of distances ensures that small (large) changes in the latent space correspond to small (large) changes in the pattern of neuron activity (Fig. 1F, right). Preservation of angles ensures that directions that are orthogonal in the latent space correspond to changes in neural firing patterns that are maximally independent (Fig. 1F, right). Finally, preservation of direction ensures that moving along a particular direction in the latent space leads to regular and consistent changes of neuron activity (Fig. 1G, right). By including these costs in the autoencoder, we construct a model of the mouse’s cognitive map as a low-dimensional manifold that preserves the quantitative structure in the population activity, allowing us to study how the map is organized to support efficient search (Fig. 1H). 

We achieve this manifold model by completely and orthogonally decomposing all manifold nonlinearity into two curvatures: the extrinsic curvature that measures how quickly the direction of the collective variables changes along the manifold coordinates, and the parameter effects curvature that measures distortions in the distances and angles between the latent space and the data space. Hence, Γ-AE enables us to construct nonlinear manifolds that are interpretable—directions in the latent space correspond to consistent directions in data space—and quantitative—distances and angles in the latent space reflect those of the manifold in data space—even in regions with sparse or no data. As a result, Γ-AE builds a geometrically consistent manifold not just of the data, but of the entire nonlinear sub- 

16 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

space that the data inhabit. 

To build our model manifold of hippocampal CA1 neuron activity, we use a deep neural network called an autoencoder comprised of two feedforward multilayer perceptrons: the _encoder_ , _**fθ**_ : R _[N] →_ R _[k]_ , and the _decoder_ , _**hϕ**_ : R _[k] →_ R _[N]_ . The encoder architecture has four layers, where the layer dimensions are 200, 100, 50, 3, and the decoder architecture has four layers, where the layer dimensions are 3, 50, 100, 200. Hence, the function for the encoder follows 

**==> picture [364 x 12] intentionally omitted <==**

where the trainable parameters, _**θ**_ , are linear matrices _E_ 0 _, E_ 1 _, E_ 2 and bias terms _**e**_ **0** _,_ _**e**_ **1** _,_ _**e**_ **2** , and _**e**_ **3** . The activation function _s_ is softplus. The function for the decoder follows: 

**==> picture [367 x 12] intentionally omitted <==**

where the trainable parameters, _**ϕ**_ , are linear matrices _D_ 0 _, D_ 1 _, D_ 2, and _D_ 3 and bias terms _**d**_ **0** _,_ _**d**_ **1** _,_ _**d**_ **2** , and **ˆ** _**d**_ **3** . Passing an input vector of neuron activity _**x**_ produces the output of the autoencoder _**x**_ = _**h**_ ( _**f**_ ( _**x**_ )). 

## _8.3 Manifold Geometry_ 

Because deep neural networks are universal function approximators, the manifold formed by the decoder can, in principle, distort to pass through the data in any arbitrary order. According to [20], we orthogonally decompose and regularize all manifold nonlinearities to selectively choose which nonlinearities to allow. This decomposition is comprised of two components. 

First, to correct for distortions in the distances and angles between the latent-space coordinates and the manifold, we regularize the _parameter-effects curvature_ : 

**==> picture [351 x 30] intentionally omitted <==**

where _g[µν]_ is the inverse of the metric tensor, Γ _[κ] µν_[are the Christoffel symbols [122],][and Eq. 3 is written] in Einstein summation notation (repeated Greek indices are summed). The parameter-effects curvature given by Eq. 3 is the norm of the component of the second derivative of the manifold that lies tangent to the manifold at that point. Intuitively, Eq. 3 measures by how much a regular grid of points in latent space is distorted on the manifold by the decoder in data space. 

Second, to ensure that the manifold coordinates are interpretable such that consistent directions in the latent-space correspond to similar changes in the patterns of neuron activity, we enforce that straight lines in latent space correspond roughly to straight lines in data space by also regularizing the _extrinsic curvature_ at each point on the manifold, which we derive as 

**==> picture [403 x 34] intentionally omitted <==**

The extrinsic curvature is the norm of the component of the second derivative of the manifold that lies normal to the manifold at that point. Intuitively, Eq. 4 measures by how much the manifold tangent bends into new directions as we traverse the manifold. 

Additionally, even though Eq. 3 quantifies nonlinearities on the manifold tangents, there is still an arbitrariness to the absolute global scale between the latent-space coordinates and manifold tangents (e.g. how far one unit distance in the latent space is on the manifold). To fix an absolute scale, we include an additional loss on the scale of the manifold to be approximately uniform such that 

**==> picture [324 x 35] intentionally omitted <==**

17 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

where _gi_ is the metric tensor at sampled points _i_ in the latent space. Additionally, while Eq. 3 and Eq. 4 define the distortions of the manifold geometry through the decoder (Eq. 2), we additionally regularize distortions for the encoder _LE_ that maps points from the neuron space onto the latent space. 

Finally, the network also minimizes the standard autoencoder reconstruction loss, 

**==> picture [306 x 31] intentionally omitted <==**

which is the mean squared error of reconstructing the original data from the manifold. These losses combine to yield the final loss 

**==> picture [346 x 12] intentionally omitted <==**

In practice, we want our manifold to preserve distances and angles as well as possible, so we set _α_ = _β_ = _δ_ = 100 to be very large. Hence, the only nonlinearity we allow meaningful quantities of is the extrinsic curvature _γ_ = 0 _._ 5, which allows the manifold to bend gently along with the natural curvature of the data. 

## _8.4 Constructing the surfaces of experience_ 

Once Γ-AE is trained, we use the data points projected in the latent space to construct our surfaces of experience. To build each surface for each task condition, we average the latent space points corresponding to every 3 cm of track and every 20 trials for that task condition. Once the data are binned in a grid in the latent space, we smooth the surfaces using taubin smoothing [123] that avoids the artifact of shrinking the manifold experienced by Gaussian smoothing. We used _λ_ = 0 _._ 2 and _µ_ = _−_ 1 _._ 01 _λ_ , and iterated until the algorithm converged. 

## _8.5 Computing the generalized state fields_ 

In this work, we define a GSF for a neuron as localized regions of the latent space that have high decoded activity for that neuron. To compute GSFs, we first densely and uniformly sampled the latent space using a regularly spaced grid of points, _X_ , such that the grid extends slightly beyond the extent of the observed data embedded in the latent space. Then, we constructed a mask containing all grid points within the convex hull of the observed data. The points inside of the convex hull were decoded to patterns of neural activity, whereas the corresponding activity of points outside of the convex hull were set to 0 for all neurons. Then, each neuron’s activity on the grid was smoothed using a Gaussian convolution with a kernel standard deviation roughly 1/10th of the standard deviation of the observed embedded data. For clarity, we will call this Gaussian convolved activity for each neuron _n_ from the decoded latent space grid the _latent activity map_ , denoted _Ln_ ( _**x**_ ) _,_ _**x** ∈ X_ . For the visualization of the GSF isosurfaces, we threshold each isosurface to show activity above 98.5% of the activity for that neuron on the latent space grid. This threshold was used purely for visualization, and not for any quantitative analysis. 

## _8.6 Computing statistically significant GSF peaks_ 

To go beyond a thresholded visualization and define statistically significant peaks of the GSFs for further analysis, we begin with the latent activity map for one neuron, and identify candidate peaks as local maxima. Then for each peak, we use a merge-tree algorithm to compute its _prominence_ as the difference between that neuron’s activity at that peak and the highest saddle point on a path connecting to any higher peak. Said another way, the prominence for any peak is the minimum decrease in that neuron’s decoded activity to reach a higher point. The maximum peak is given a prominence of infinity. Given each peak _i_ of neuron _n_ , the decoded activity of that peak, _ai_ , and the prominence of that peak, _bi_ , we consider a candidate GSF peak to be a true significant GSF peak if both its activity relative to the minimum decoded activity in the latent activity map, and its prominence, satisfy 

**==> picture [477 x 12] intentionally omitted <==**

18 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

Here, MAD is the mean absolute deviation, and the factor 1.253 is the scale between the MAD and the standard deviation for normally distributed data. We define the set of all statistically significant peaks that pass these criteria as _P_ = _{p}_ with coordinates _**x** p_ and the corresponding neuron that produced that peak _np_ . 

## _8.7 Computing statistically significant GSF co-peaks_ 

Once we have the set of statistically significant GSF peaks, we turn to statistically testing for significant co-peaks. To do this, we take the set of all statistically significant GSF peaks across all neurons, _P_ , choose one peak at a time as the query peak, _pi ∈P_ , find the _k_ = 200 nearest neighbor peaks, _Kpi ⊂P_ , identify which neurons gave rise to those neighboring peaks, _Npi_ = _{np | p ∈Kpi}_ , and find all peaks produced by those neurons _Upi_ = _{pj | npj ∈Npi}_ . The candidate co-peaks, then, are the subset of peaks produced by those neighboring neurons excluding the neighboring peaks, _Cpi_ = _Upi_ `\` _Kpi_ , and _|Cpi|_ is the number of candidate co-peaks. 

To test whether the co-peaks are significantly clustered relative to chance, we perform a shuffle test and look at the distance from each co-peak to its _m_ = 30 nearest neighbor. Specifically, for each co-peak _cj ∈Cpi_ , we compute the distance to the _m_ -th nearest co-peak, _dj_ . Then, we select a random draw of _|Cpi|_ peaks from all significant peaks excluding the neighboring peaks, _Cp_[null] _i ⊂P_ `\` _Npi_ , and compute the distance from each true co-peak _cj_ to the _m_ -th nearest null co-peak, _d_[null] _j_ . Finally, we define a true co-peak _cj_ to be statistically significantly clustered to other true co-peaks than by chance if _d_ is smaller than _d_[null] for all of 5000 random draws of _C_[null][the][set][of][which][we][define][as] _j j pi_[,] _Spi_ = _{cj | cj ∈Cpi_ & _dj < d_[null] _j }_ . 

## _8.8 Defining small-worldness using latent-space co-peaks_ 

The procedure for defining statistically significant GSF co-peaks associates each query point _pi ∈P_ with the set of significantly clustered co-peaks _Spi ⊂P_ . To define small-worldness in this space, the fine-grained approach would be to consider each peak as a node and define an edge as existing from node _pi_ to _pj_ if the significant co-peaks _Spi_ overlapped with the neighborhood _Npj_ . This procedure would produce a graph of _|P|_ nodes. To produce a coarser graph, we take a subset of this graph where the nodes in that subset are chosen sequentially via a greedy set cover such that the neighborhoods of the chosen points maximally cover all of the peaks. It is this graph subset that is shown in the main text. 

## _8.9 Defining rate maps in position and day_ 

To identify place field peaks in the raw data across position for each day, we first build rate maps for each neuron’s activity. To build these rate maps, for each neuron _i_ , we first binned all frames into bins of 5cm and 1 day, such that for each position bin _b_ , we get the summed activity _ai_ ( _b_ ), and the number of frames in that bin _ni_ ( _b_ ). To avoid large fluctuations from bins with few frames, we compute the rate as the ratio of the convolved summed activity and frame count 

**==> picture [279 x 27] intentionally omitted <==**

where _∗_ denotes the convolution with the kernel _k_ , which is a Gaussian with a standard deviation of 5cm. This rate map is constructed for each day and each task condition. In the context of the rate maps and subsequent analyses of significant peaks, we consider each task condition separately as a circular track, such that these convolutions are taken on two periodic tracks, producing a rate map for each task condition. We then concatenate these two rate maps together, and for any analysis involving the rate maps and subsequent peaks, refer to the bin index along this concatenated rate map as position. 

## _8.10 Defining statistically significant rate map peaks_ 

To define statistically significant peaks in the raw data across position for each neuron and each day, we construct the rate map for that neuron and day across position, and identify candidate peaks as 

19 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

local maxima in the rate map. To test whether these local maxima are statistically significant and robust, we perform a shuffle test. Specifically, we take all of the raw activity data as a function of the frame number, and for the frames of each trial, circularly shift the frame index by a random uniform integer between 1 and the number of frames for that trial. We perform this random shift for each of all trials. Then, we use this randomly shifted data to construct a null rate map _rb_[null] as if the frame indices were not permuted (i.e., _ni_ ( _b_ ) does not change, and only the data that goes into _ai_ ( _b_ ) come from the shifted null). For each null rate map, we compute the maximum value of _rb_[null] , and repeat this null generation procedure 10,000 times. We define a rate map peak for each neuron and each day to be statistically significant if it is larger than 95% of the maximum null values, and also enforce a minimum peak distance of 2 bins. 

## _8.11 Defining statistically significant co-firing peaks in the rate maps_ 

To test for statistically significant co-firing peaks in the rate maps, we first construct a significant peak tensor _P ∈{_ 0 _,_ 1 _}_[#days] _[×]_[#position] _[×]_[#neurons] , where an index _Pijk_ is 1 if neuron _k_ had a statistically significant peak on day _i_ and position _j_ , and 0 otherwise. Then, for a query day and position bin ( _i, j_ ), we identify the neurons that fired in the immediate positional neighborhood of that query bin _Nij_ = _{k | Pitk_ = 1 _, t ∈{j −_ 1 _, j, j_ +1 _}}_ , and computed how many of those neurons had significant peaks for each position and day bin, _Cij_ =[�] _t∈Nij[P][ijt]_[,][where][we][set][the][counts][within][the][query][bin][and][im-] mediate positional neighborhood to 0. We refer to these counts as the empirically observed peak count. 

To test whether an empirically observed peak count _Cij_ was statistically significantly greater than by chance, we performed Monte Carlo sampling from a multinomial null distribution with empirically observed probabilities. Specifically, for each day _i_ and position _j_ , we compute the number of significant peaks across all neurons as _Dij_ =[�] _k[P][ijk]_[,][and][normalize][those][counts][as][the][multinomial][null] probabilities, 

**==> picture [280 x 29] intentionally omitted <==**

We then performed 10,000 draws from this multinomial distribution using _pij_ as the multinomial probabilities, and[�] _ij[C][ij]_[as][the][total][observed][counts,][and][for][each][multinomial][null][draw][computed][the] _C_ maximum standardized bin count,˜ _ij_ to be statistically significant if _C_[˜] it[null] was. We considered an empirically observed standardized bin countgreater than 95% of the maximum null draws _C_ ˜[null] . Hence, for each day and position bin, ( _i, j_ ), this procedure defines a set of bins _Sij_ where neurons that fire in the positional neighborhood of ( _i, j_ ) have statistically significantly more peaks than by chance. We convert these sets of significant co-firing bins into a matrix _S ∈{_ 0 _,_ 1 _}_[(#days] _[∗]_[#position)] _[×]_[(#days] _[∗]_[#position)] , where each row and each column corresponds to a day and position bin (i,j), and the entry _Smn_ = 1 if the query day and position bin ( _i, j_ ) corresponding to index _m_ has a significant bin in _Sij_ corresponding to index _n_ . 

## _8.12 Computing the small-world coefficient and generating the degree-preserving null model_ 

To test whether our graphs comprising nodes of bins of position (5cm) and time (1 day) and edges from query bins to other bins with statistically significantly higher co-peak counts, we compute the small-world coefficient [38], which takes the ratio of the graph’s clustering coefficient relative to a null, and the graph’s shortest path length relative to a null. To construct the null, we used the MaslovSneppen algorithm [124] that performs degree-preserving edge swaps to generate 1000 randomized null graphs using _∼_ 10 swaps per edge. From our empirically measured graph and the corresponding nulls, we computed the small-world coefficient by taking the fraction between the ratio of empirical _versus_ null clustering coefficient, and the empirical _versus_ null characteristic path length. We then computed the null distribution of small-world coefficient by computing the same ratio between each null re-wired graph’s clustering coefficient _versus_ that of the null ensemble and the null re-wired graph’s characteristic path length _versus_ that of the null ensemble. 

20 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## _8.13 Decoding and testing synchronized calcium events_ 

Synchronized calcium events (SCEs) were identified from stationary periods during the active task rather than during pre-session or post-session rest. This criterion captures moments when the animal has voluntarily paused mid-task during goal-directed navigation—brief pauses thought to be associated with memory consolidation and planning. We refer to these as SCEs rather than sharp-wave ripples (SWRs), as calcium imaging does not directly measure the underlying oscillatory dynamics, though previous work has established that such population events can co-occur with electrophysiologically measured SWRs. A frame was classified as an SCE if it satisfied the following criteria: (1) speed = 0 cm/s, (2) not during the inter-trial teleportation period, and (3) no licking at that frame or ±2 frames. Given the 10 Hz imaging rate, each frame corresponds to 100 ms. To ensure temporal separation between SCE frames and running frames used for manifold construction, SCE frames were required to be padded by at least two consecutive stationary frames on either side, while manifold frames required padding by at least two consecutive high-speed frames (speed _>_ 5 cm/s). This ensured a minimum separation of 500 ms between SCE and manifold frames, minimizing signal bleed-through. 

To decode the synchronized calcium events (SCEs), we first associated an averaged pattern of neuron activity with each position _j_ (5cm) and day _i_ by averaging the activity for the frames where the animal was at that particular position and day. This procedure gives us an average vector of activity _**a** ij_ , which we then normalize to yield _**b** ij_ = _**a** ij/|_ _**a** ij|_ . This procedure of defining bins is distinct from how we constructed the rate maps because the goal was not to identify robust peaks along the continuum of position, but rather to have an accurate and unbiased measurement of each position and day bin for decoding. 

To decode the activity of each SCE _m_ , we take the normalized vector of its pattern of activity, _**s** m_ , and reconstruct it using non-negative least squares with a ridge penalty 

**==> picture [385 x 26] intentionally omitted <==**

where we choose _β_ = 1. This procedure gives us the reconstruction coefficients _**v** m_ whose non-negative coefficient _vij_ is the amount of weight given to the position and day bin _**b** ij_ in the reconstruction. 

To test whether the weights are statistically significantly large, we perform a shuffle test by randomly permuting the elements of _**s** m_ , and recomputing the coefficients _**v** m_[null] using the same procedure in Eq. 11 for 2000 permutations. For each shuffle, we record the maximum decoded coefficient. For SCE _m_ , we call an empirically decoded coefficient statistically significant if it is larger than 95% of the distribution of 2000 maximum decoded coefficients from the null shuffles, giving us a thresholded vector _**t** m_ . 

## _8.14 Testing overlap between SCE decoded maps and the small-world graph_ 

To test whether the empirically decoded coefficients for the SCEs leverage the small-world graph more than by chance, we take the vector of significantly decoded coefficients for each SCE, _**t** m_ , and the matrix containing statistically significant co-firing peaks in the small-world graph _S_ , and define traversing one step down the graph as 

**==> picture [270 x 14] intentionally omitted <==**

The alignment score, then, is the correlation between _**t** m_ and _**t**_[ˆ] _m_ . 

To test whether this alignment is statistically significant, we construct a shuffle null where we take the decoded coefficients _**t** m_ which contains coefficients for each day and position bin, and circularly shift the position index by a random integer between 1 and the number of positions - 1, and recomputed the overlap score. This circular shift ensures we preserve any spatial correlations so that our null overlap score is not artificially low due to breaking up spatial correlation. We perform this null shift 1000 times, and find that our empirically measured overlap score is larger than the entire null distribution by a wide margin. 

21 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **Data availability** 

All data used in this study are publicly available as part of the dataset released in [13] on Figshare (https://doi.org/10.25378/janelia.27273552). An interactive visualization of the dataset is available at `cognitivemap.janelia.org` [13]. 

## **Code availability** 

Code used for analysis and figure generation will be released upon peer-reviewed acceptance. 

## **Acknowledgements** 

We thank Antonio Fernandez-Ruiz, Ian Ellwood, Chongxi Lai, Albert Lee, Melody X. Lim, Brett Mensh, and Nelson Spruston for valuable discussions and feedback on the manuscript. J.Z.K. was supported by postdoctoral fellowships from Bethe/KIC/Wilkins, Mong Neurotech, and the Eric and Wendy Schmidt AI in Science program of Schmidt Sciences, LLC. I.C. and J.Z.K. were supported in part by the NIH National Institute of Arthritis and Musculoskeletal and Skin Diseases (5R21AR08306402) and the Air Force Office of Scientific Research (FA9550-23-1-0722). W.S. was supported by Cornell University. 

22 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **References** 

- [1] Edward C Tolman. Cognitive maps in rats and men. _Psychological review_ , 55(4):189, 1948. 

- [2] Brad E Pfeiffer and David J Foster. Hippocampal place-cell sequences depict future paths to remembered goals. _Nature_ , 497(7447):74–79, 2013. 

- [3] Chongxi Lai, Shinsuke Tanaka, Timothy D Harris, and Albert K Lee. Volitional activation of remote place representations with a hippocampal brain–machine interface. _Science_ , 382(6670):566– 573, 2023. 

- [4] John O’keefe and Lynn Nadel. _The hippocampus as a cognitive map_ . Oxford university press, 1978. 

- [5] John O’Keefe and Jonathan Dostrovsky. The hippocampus as a spatial map: preliminary evidence from unit activity in the freely-moving rat. _Brain research_ , 1971. 

- [6] Christopher J MacDonald, Kyle Q Lepage, Uri T Eden, and Howard Eichenbaum. Hippocampal “time cells” bridge the gap in memory for discontiguous events. _Neuron_ , 71(4):737–749, 2011. 

- [7] Teruko Danjo, Taro Toyoizumi, and Shigeyoshi Fujisawa. Spatial representations of self and other in the hippocampus. _Science_ , 359(6372):213–218, 2018. 

- [8] Azahara Oliva. Ca2 physiology underlying social memory. _Current opinion in neurobiology_ , 77:102642, 2022. 

- [9] Robert E Hampson, Tim P Pons, Terrence R Stanford, and Sam A Deadwyler. Categorization in the monkey hippocampus: a possible mechanism for encoding information into memory. _Proceedings of the National Academy of Sciences_ , 101(9):3184–3189, 2004. 

- [10] R Quian Quiroga, Leila Reddy, Gabriel Kreiman, Christof Koch, and Itzhak Fried. Invariant visual representation by single neurons in the human brain. _Nature_ , 435(7045):1102–1107, 2005. 

- [11] Dmitriy Aronov, Rhino Nevers, and David W Tank. Mapping of a non-spatial dimension by the hippocampal–entorhinal circuit. _Nature_ , 543(7647):719–722, 2017. 

- [12] Edward H Nieh, Manuel Schottdorf, Nicolas W Freeman, Ryan J Low, Sam Lewallen, Sue Ann Koay, Lucas Pinto, Jeffrey L Gauthier, Carlos D Brody, and David W Tank. Geometry of abstract learned knowledge in the hippocampus. _Nature_ , 595(7865):80–84, 2021. 

- [13] Weinan Sun, Johan Winnubst, Maanasa Natrajan, Chongxi Lai, Koichiro Kajikawa, Arco Bast, Michalis Michaelos, Rachel Gattoni, Carsen Stringer, Daniel Flickinger, et al. Learning produces an orthogonalized state machine in the hippocampus. _Nature_ , 640(8057):165–175, 2025. 

- [14] James CR Whittington, David McCaffary, Jacob JW Bakermans, and Timothy EJ Behrens. How to build a cognitive map. _Nature neuroscience_ , 25(10):1257–1272, 2022. 

- [15] Robert U Muller, John L Kubie, and James B Ranck. Spatial firing patterns of hippocampal complex-spike cells in a fixed environment. _Journal of Neuroscience_ , 7(7):1935–1950, 1987. 

- [16] R Becket Ebitz and Benjamin Y Hayden. The population doctrine in cognitive neuroscience. _Neuron_ , 109(19):3055–3068, 2021. 

- [17] Leland McInnes, John Healy, and James Melville. Umap: Uniform manifold approximation and projection for dimension reduction. _arXiv preprint arXiv:1802.03426_ , 2018. 

- [18] Joshua B Tenenbaum, Vin de Silva, and John C Langford. A global geometric framework for nonlinear dimensionality reduction. _science_ , 290(5500):2319–2323, 2000. 

- [19] Tara Chari and Lior Pachter. The specious art of single-cell genomics. _PLOS Computational Biology_ , 19(8):e1011288, 2023. 

23 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [20] Jason Z Kim, Nicolas Perrin-Gilbert, Erkan Narmanli, Paul Klein, Christopher R Myers, Itai Cohen, Joshua J Waterfall, and James P Sethna. Γ-vae: Curvature regularized variational autoencoders for uncovering emergent low dimensional geometric structure in high dimensional data. _arXiv preprint arXiv:2403.01078_ , 2024. 

- [21] Duncan J Watts and Steven H Strogatz. Collective dynamics of ‘small-world’networks. _nature_ , 393(6684):440–442, 1998. 

- [22] Wenbo Tang, Hongyu Chang, Can Liu, Salma Perez-Hernandez, William Y Zheng, Jaehyo Park, Azahara Oliva, and Antonio Fernandez-Ruiz. A hippocampal population code for rapid generalization. _bioRxiv_ , pages 2025–03, 2025. 

- [23] Alexandra T Keinath, Coralie-Anne Mosser, and Mark P Brandon. The representation of context in mouse hippocampus is preserved despite neural drift. _Nature communications_ , 13(1):2415, 2022. 

- [24] Mayank R Mehta, Carol A Barnes, and Bruce L McNaughton. Experience-dependent, asymmetric expansion of hippocampal place fields. _Proceedings of the National Academy of Sciences_ , 94(16):8918–8921, 1997. 

- [25] Mayank R Mehta, Michael C Quirk, and Matthew A Wilson. Experience-dependent asymmetric shape of hippocampal receptive fields. _Neuron_ , 25(3):707–715, 2000. 

- [26] Yaniv Ziv, Laurie D Burns, Eric D Cocker, Elizabeth O Hamel, Kunal K Ghosh, Lacey J Kitch, Abbas El Gamal, and Mark J Schnitzer. Long-term dynamics of ca1 hippocampal place codes. _Nature neuroscience_ , 16(3):264–266, 2013. 

- [27] Laura N Driscoll, Noah L Pettit, Matthias Minderer, Selmaan N Chettih, and Christopher D Harvey. Dynamic reorganization of neuronal activity patterns in parietal cortex. _Cell_ , 170(5):986– 999, 2017. 

- [28] Laura N Driscoll, Lea Duncker, and Christopher D Harvey. Representational drift: Emerging theories for continual learning and experimental future directions. _Current opinion in neurobiology_ , 76:102609, 2022. 

- [29] Charles Micou and Timothy O’Leary. Representational drift as a window into neural and behavioural plasticity. _Current opinion in neurobiology_ , 81:102746, 2023. 

- [30] Peter Dayan. Improving generalization for temporal difference learning: The successor representation. _Neural computation_ , 5(4):613–624, 1993. 

- [31] Kimberly L Stachenfeld, Matthew M Botvinick, and Samuel J Gershman. The hippocampus as a predictive map. _Nature neuroscience_ , 20(11):1643–1653, 2017. 

- [32] Gy¨orgy Buzs´aki. Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. _Hippocampus_ , 25(10):1073–1188, 2015. 

- [33] Arnaud Malvache, Susanne Reichinnek, Vincent Villette, Caroline Haimerl, and Rosa Cossart. Awake hippocampal reactivations project onto orthogonal neuronal assemblies. _Science_ , 353(6305):1280–1283, 2016. 

- [34] Xin Liu, Satoshi Terada, Mehrdad Ramezani, Jeong-Hoon Kim, Yichen Lu, Andres Grosmark, Attila Losonczy, and Duygu Kuzum. E-cannula reveals anatomical diversity in sharp-wave ripples as a driver for the recruitment of distinct hippocampal assemblies. _Cell reports_ , 41(1), 2022. 

- [35] Brad E Pfeiffer and David J Foster. Autoassociative dynamics in the generation of sequences of hippocampal place cells. _Science_ , 349(6244):180–183, 2015. 

- [36] Alice Berners-Lee, Ting Feng, Delia Silva, Xiaojing Wu, Ellen R Ambrose, Brad E Pfeiffer, and David J Foster. Hippocampal replays appear after a single experience and incorporate greater detail with more experience. _Neuron_ , 110(11):1829–1842, 2022. 

24 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [37] Yosif Zaki, Zachary T Pennington, Denisse Morales-Rodriguez, Taylor R Francisco, Alexa R LaBanca, Zhe Dong, Sophia Lamsifer, Sim´on Carrillo Segura, Hung-Tu Chen, Zo´e Christenson Wick, et al. Aversive experience drives offline ensemble reactivation to link memories across days. _bioRxiv_ , 2023. 

- [38] Mark D Humphries and Kevin Gurney. Network ‘small-world-ness’: a quantitative method for determining canonical network equivalence. _PloS one_ , 3(4):e0002051, 2008. 

- [39] AD Ekstrom, J Meltzer, BL McNaughton, and CA Barnes. Nmda receptor antagonism blocks experience-dependent expansion of hippocampal “place fields”. _Neuron_ , 31(4):631–638, 2001. 

- [40] Inah Lee, Geeta Rao, and James J Knierim. A double dissociation between hippocampal subfields: differential time course of ca3 and ca1 place cells for processing changed environments. _Neuron_ , 42(5):803–815, 2004. 

- [41] Eric D Roth, Xintian Yu, Geeta Rao, and James J Knierim. Functional differences in the backward shifts of ca1 and ca3 place fields in novel and familiar environments. _PloS one_ , 7(4):e36035, 2012. 

- [42] Can Dong, Antoine D Madar, and Mark EJ Sheffield. Distinct place cell dynamics in ca1 and ca3 encode experience in new environments. _Nature communications_ , 12(1):2977, 2021. 

- [43] James B Priestley, John C Bowler, Sebi V Rolotti, Stefano Fusi, and Attila Losonczy. Signatures of rapid plasticity in hippocampal ca1 representations during novel experiences. _Neuron_ , 110(12):1978–1992, 2022. 

- [44] Jason R Climer, Heydar Davoudi, Jun Young Oh, and Daniel A Dombeck. Hippocampal representations drift in stable multisensory environments. _Nature_ , 645(8080):457–465, 2025. 

- [45] Clifford G Kentros, Naveen T Agnihotri, Samantha Streater, Robert D Hawkins, and Eric R Kandel. Increased attention to spatial context increases both place field stability and spatial memory. _Neuron_ , 42(2):283–295, 2004. 

- [46] Francesca Cacucci, Thomas J Wills, Colin Lever, Karl Peter Giese, and John O’Keefe. Experiencedependent increase in ca1 place cell spatial information, but not spatial reproducibility, is dependent on the autophosphorylation of the _α_ -isoform of the calcium/calmodulin-dependent protein kinase ii. _Journal of Neuroscience_ , 27(29):7854–7859, 2007. 

- [47] Ryan J Low, Sam Lewallen, Dmitriy Aronov, Rhino Nevers, and David W Tank. Probing variability in a cognitive map using manifold inference from neural dynamics. _BioRxiv_ , page 418939, 2018. 

- [48] Ching Fang, Dmitriy Aronov, LF Abbott, and Emily L Mackevicius. Neural learning rules for generating flexible predictions and computing the successor representation. _elife_ , 12:e80680, 2023. 

- [49] Tom M George, William de Cothi, Kimberly L Stachenfeld, and Caswell Barry. Rapid learning of predictive maps with stdp and theta phase precession. _Elife_ , 12:e80663, 2023. 

- [50] Jacopo Bono, Sara Zannone, Victor Pedrosa, and Claudia Clopath. Learning predictive cognitive maps with spiking neurons during behavior and replays. _Elife_ , 12:e80671, 2023. 

- [51] Daniel Levenstein, Aleksei Efremov, Roy Henha Eyono, Adrien Peyrache, and Blake Richards. Sequential predictive learning is a unifying theory for hippocampal representation and replay. _bioRxiv_ , pages 2024–04, 2024. 

- [52] Maanasa Natrajan and James E Fitzgerald. Stability through plasticity: Finding robust memories through representational drift. _Proceedings of the National Academy of Sciences_ , 122(45):e2500077122, 2025. 

- [53] P Dylan Rich, Hua-Peng Liaw, and Albert K Lee. Large environments reveal the statistical structure governing hippocampal representations. _Science_ , 345(6198):814–817, 2014. 

25 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [54] Jae Sung Lee, John J Briguglio, Jeremy D Cohen, Sandro Romani, and Albert K Lee. The statistical structure of the hippocampal code for space as a function of time, context, and value. _Cell_ , 183(3):620–635, 2020. 

- [55] Annabelle C Singer, Mattias P Karlsson, Ana R Nathe, Margaret F Carr, and Loren M Frank. Experience-dependent development of coordinated hippocampal spatial activity representing the similarity of related locations. _Journal of Neuroscience_ , 30(35):11586–11604, 2010. 

- [56] Hannah S Wirtshafter and John F Disterhoft. Place cells are nonrandomly clustered by field location in ca1 hippocampus. _Hippocampus_ , 33(2):65–84, 2023. 

- [57] Eliott Robert Joseph Levy, Sim´on Carrillo-Segura, Eun Hye Park, William Thomas Redman, Jos´e Rafael Hurtado, SueYeon Chung, and Andr´e Antonio Fenton. A manifold neural population code for space in hippocampal coactivity dynamics independent of place fields. _Cell reports_ , 42(10), 2023. 

- [58] L Sheintuch, N Geva, D Deitch, A Rubin, and Y Ziv. Organization of hippocampal ca3 into correlated cell assemblies supports a stable spatial code. cell rep. 42, 112119, 2023. 

- [59] Heng Zhou, Kevin R Neville, Nitsan Goldstein, Shushi Kabu, Naila Kausar, Rong Ye, Thuan Tinh Nguyen, Noah Gelwan, Bradley T Hyman, and Stephen N Gomperts. Cholinergic modulation of hippocampal calcium activity across the sleep-wake cycle. _elife_ , 8:e39777, 2019. 

- [60] S´ebastien Royer, Boris V Zemelman, Attila Losonczy, Jinhyun Kim, Frances Chance, Jeffrey C Magee, and Gy¨orgy Buzs´aki. Control of timing, rate and bursts of hippocampal place cells by dendritic and somatic inhibition. _Nature neuroscience_ , 15(5):769–775, 2012. 

- [61] Antonio Fern´andez-Ruiz, Azahara Oliva, Eliezyer Fermino de Oliveira, Florbela Rocha-Almeida, David Tingley, and Gy¨orgy Buzs´aki. Long-duration hippocampal sharp wave ripples improve memory. _Science_ , 364(6445):1082–1086, 2019. 

- [62] Daniel C McNamee, Kimberly L Stachenfeld, Matthew M Botvinick, and Samuel J Gershman. Flexible modulation of sequence generation in the entorhinal–hippocampal system. _Nature neuroscience_ , 24(6):851–862, 2021. 

- [63] Katie C Bittner, Aaron D Milstein, Christine Grienberger, Sandro Romani, and Jeffrey C Magee. Behavioral time scale synaptic plasticity underlies ca1 place fields. _Science_ , 357(6355):1033–1036, 2017. 

- [64] Jai Y Yu, Kenneth Kay, Daniel F Liu, Irene Grossrubatscher, Adrianna Loback, Marielena Sosa, Jason E Chung, Mattias P Karlsson, Margaret C Larkin, and Loren M Frank. Distinct hippocampal-cortical memory representations for experiences associated with movement versus immobility. _Elife_ , 6:e27621, 2017. 

- [65] Wenbo Tang, Xiyu Mei, Ryan E Harvey, Estrella Carbajal-Leon, Talia Netzer, Hongyu Chang, Azahara Oliva, and Antonio Fernandez-Ruiz. Goal-directed hippocampal theta sweeps during memory-guided navigation. _bioRxiv_ , pages 2025–08, 2025. 

- [66] Mattias P Karlsson and Loren M Frank. Awake replay of remote experiences in the hippocampus. _Nature neuroscience_ , 12(7):913–918, 2009. 

- [67] Anoopum S Gupta, Matthijs AA Van Der Meer, David S Touretzky, and A David Redish. Hippocampal replay is not a simple function of experience. _Neuron_ , 65(5):695–705, 2010. 

- [68] Adam Johnson and A David Redish. Neural ensembles in ca3 transiently encode paths forward of the animal at a decision point. _Journal of Neuroscience_ , 27(45):12176–12189, 2007. 

- [69] Andrew M Wikenheiser and A David Redish. Hippocampal theta sequences reflect current goals. _Nature neuroscience_ , 18(2):289–294, 2015. 

26 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [70] Kenneth Kay, Jason E Chung, Marielena Sosa, Jonathan S Schor, Mattias P Karlsson, Margaret C Larkin, Daniel F Liu, and Loren M Frank. Constant sub-second cycling between representations of possible futures in the hippocampus. _Cell_ , 180(3):552–567, 2020. 

- [71] Yuchen Zhou, Jeremie Sibille, and George Dragoi. Generative emergence of non-local representations in the hippocampus. _Nature Communications_ , 16(1):8012, 2025. 

- [72] Albert K Lee and Matthew A Wilson. Memory of sequential experience in the hippocampus during slow wave sleep. _Neuron_ , 36(6):1183–1194, 2002. 

- [73] Kamran Diba and Gy¨orgy Buzs´aki. Forward and reverse hippocampal place-cell sequences during ripples. _Nature neuroscience_ , 10(10):1241–1242, 2007. 

- [74] David J Foster and Matthew A Wilson. Reverse replay of behavioural sequences in hippocampal place cells during the awake state. _Nature_ , 440(7084):680–683, 2006. 

- [75] Hongyu Chang, Wenbo Tang, Annabella M Wulf, Thokozile Nyasulu, Madison E Wolf, Antonio Fernandez-Ruiz, and Azahara Oliva. Sleep microstructure organizes memory replay. _Nature_ , 637(8048):1161–1169, 2025. 

- [76] George Dragoi and Susumu Tonegawa. Preplay of future place cell sequences by hippocampal cellular assemblies. _Nature_ , 469(7330):397–401, 2011. 

- [77] Brian Lustig, Yingxue Wang, Sandro Romani, Eva Pastalkova, and Albert K Lee. Signatures of remote planning in hippocampal replay. _bioRxiv_ , pages 2025–12, 2025. 

- [78] Wan-Chen Jiang, Shengjin Xu, and Joshua T Dudman. Hippocampal representations of foraging trajectories depend upon spatial context. _Nature neuroscience_ , 25(12):1693–1705, 2022. 

- [79] Zilong Ji, Tianhao Chu, Xingsi Dong, Changmin Yu, Daniel Bush, Neil Burgess, and Si Wu. Dynamical modulation of hippocampal replay through firing rate adaptation. _Nature Communications_ , 2026. 

- [80] Eric L Denovellis, Anna K Gillespie, Michael E Coulter, Marielena Sosa, Jason E Chung, Uri T Eden, and Loren M Frank. Hippocampal replay of experience at real-world speeds. _Elife_ , 10:e64505, 2021. 

- [81] Federico Stella, Peter Baracskay, Joseph O’Neill, and Jozsef Csicsvari. Hippocampal reactivation of random trajectories resembling brownian diffusion. _Neuron_ , 102(2):450–461, 2019. 

- [82] Gandhimohan M Viswanathan, Vsevolod Afanasyev, Sergey V Buldyrev, Eugene J Murphy, Peter A Prince, and H Eugene Stanley. L´evy flight search patterns of wandering albatrosses. _Nature_ , 381(6581):413–415, 1996. 

- [83] David A Raichlen, Brian M Wood, Adam D Gordon, Audax ZP Mabulla, Frank W Marlowe, and Herman Pontzer. Evidence of l´evy walk foraging patterns in human hunter–gatherers. _Proceedings of the National Academy of Sciences_ , 111(2):728–733, 2014. 

- [84] Yuxi Liu, Xian Long, Paul R Martin, Samuel G Solomon, and Pulin Gong. L´evy walk dynamics explain gamma burst patterns in primate cerebral cortex. _Communications Biology_ , 4(1):739, 2021. 

- [85] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. _Advances in neural information processing systems_ , 35:24824–24837, 2022. 

- [86] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. _Advances in neural information processing systems_ , 35:22199–22213, 2022. 

27 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [87] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. _Advances in neural information processing systems_ , 36:11809–11822, 2023. 

- [88] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. _Advances in Neural Information Processing Systems_ , 36:46534–46594, 2023. 

- [89] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. _Advances in Neural Information Processing Systems_ , 36:8634–8652, 2023. 

- [90] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. _arXiv preprint arXiv:2501.12948_ , 2025. 

- [91] David Ha and J¨urgen Schmidhuber. World models. _arXiv preprint arXiv:1803.10122_ , 2(3), 2018. 

- [92] Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. Dream to control: Learning behaviors by latent imagination. _arXiv preprint arXiv:1912.01603_ , 2019. 

- [93] Danijar Hafner, Timothy Lillicrap, Ian Fischer, Ruben Villegas, David Ha, Honglak Lee, and James Davidson. Learning latent dynamics for planning from pixels. In _International conference on machine learning_ , pages 2555–2565. PMLR, 2019. 

- [94] Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, Karen Simonyan, Laurent Sifre, Simon Schmitt, Arthur Guez, Edward Lockhart, Demis Hassabis, Thore Graepel, et al. Mastering atari, go, chess and shogi by planning with a learned model. _Nature_ , 588(7839):604–609, 2020. 

- [95] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich K¨uttler, Mike Lewis, Wen-tau Yih, Tim Rockt¨aschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. _Advances in neural information processing systems_ , 33:9459–9474, 2020. 

- [96] Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval augmented language model pre-training. In _International conference on machine learning_ , pages 3929–3938. PMLR, 2020. 

- [97] Dileep George, Rajeev V Rikhye, Nishad Gothoskar, J Swaroop Guntupalli, Antoine Dedieu, and Miguel L´azaro-Gredilla. Clone-structured graph representations enable flexible learning and vicarious evaluation of cognitive maps. _Nature communications_ , 12(1):2392, 2021. 

- [98] Rajkumar Vasudeva Raju, J Swaroop Guntupalli, Guangyao Zhou, Carter Wendelken, Miguel L´azaro-Gredilla, and Dileep George. Space is a latent sequence: A theory of the hippocampus. _Science Advances_ , 10(31):eadm8470, 2024. 

- [99] Sivaramakrishnan Swaminathan, Antoine Dedieu, Rajkumar Vasudeva Raju, Murray Shanahan, Miguel Lazaro-Gredilla, and Dileep George. Schema-learning and rebinding as mechanisms of in-context learning and emergence. _Advances in neural information processing systems_ , 36:28785– 28804, 2023. 

- [100] Miguel Lazaro-Gredilla, Ishan Deshpande, Sivaramakrishnan Swaminathan, Meet Dave, and Dileep George. Fast exploration and learning of latent graphs with aliased observations. _arXiv preprint arXiv:2303.07397_ , 2023. 

- [101] J Swaroop Guntupalli, Rajkumar Vasudeva Raju, Shrinu Kushagra, Carter Wendelken, Danny Sawyer, Ishan Deshpande, Guangyao Zhou, Miguel L´azaro-Gredilla, and Dileep George. Graph schemas as abstractions for transfer learning, inference, and planning. _arXiv preprint arXiv:2302.07350_ , 2023. 

28 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [102] Toon Van de Maele, Tim Verbelen, Dileep George, and Giovanni Pezzulo. Schema-based active inference supports rapid generalization of experience and frontal cortical coding of abstract structure. _arXiv preprint arXiv:2601.18946_ , 2026. 

- [103] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, �Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. _Advances in neural information processing systems_ , 30, 2017. 

- [104] Can Liu, Ralitsa Todorova, Wenbo Tang, Azahara Oliva, and Antonio Fernandez-Ruiz. Associative and predictive hippocampal codes support memory-guided behaviors. _Science_ , 382(6668):eadi8237, 2023. 

- [105] Jon M Kleinberg. Navigation in a small world. _Nature_ , 406(6798):845–845, 2000. 

- [106] Hanne Stensola, Tor Stensola, Trygve Solstad, Kristian Frøland, May-Britt Moser, and Edvard I Moser. The entorhinal grid map is discretized. _Nature_ , 492(7427):72–78, 2012. 

- [107] Vegard Heimly Brun, Trygve Solstad, Kirsten Brun Kjelstrup, Marianne Fyhn, Menno P Witter, Edvard I Moser, and May-Britt Moser. Progressive increase in grid scale from dorsal to ventral medial entorhinal cortex. _Hippocampus_ , 18(12):1200–1212, 2008. 

- [108] Andrew P Maurer, Shea R VanRhoads, Gary R Sutherland, Peter Lipa, and Bruce L McNaughton. Self-motion and the origin of differential spatial scaling along the septo-temporal axis of the hippocampus. _Hippocampus_ , 15(7):841–852, 2005. 

- [109] Kirsten Brun Kjelstrup, Trygve Solstad, Vegard Heimly Brun, Torkel Hafting, Stefan Leutgeb, Menno P Witter, Edvard I Moser, and May-Britt Moser. Finite scale of spatial representation in the hippocampus. _Science_ , 321(5885):140–143, 2008. 

- [110] Bryan A Strange, Menno P Witter, Ed S Lein, and Edvard I Moser. Functional organization of the hippocampal longitudinal axis. _Nature reviews neuroscience_ , 15(10):655–669, 2014. 

- [111] Andrew M Saxe, James L McClelland, and Surya Ganguli. A mathematical theory of semantic development in deep neural networks. _Proceedings of the National Academy of Sciences_ , 116(23):11537–11546, 2019. 

- [112] John P Cunningham and Byron M Yu. Dimensionality reduction for large-scale neural recordings. _Nature neuroscience_ , 17(11):1500–1509, 2014. 

- [113] Chethan Pandarinath, Daniel J O’Shea, Jasmine Collins, Rafal Jozefowicz, Sergey D Stavisky, Jonathan C Kao, Eric M Trautmann, Matthew T Kaufman, Stephen I Ryu, Leigh R Hochberg, et al. Inferring single-trial neural population dynamics using sequential auto-encoders. _Nature methods_ , 15(10):805–815, 2018. 

- [114] Steffen Schneider, Jin Hwa Lee, and Mackenzie Weygandt Mathis. Learnable latent embeddings for joint behavioural and neural analysis. _Nature_ , 617(7960):360–368, 2023. 

- [115] Ding Zhou and Xue-Xin Wei. Learning identifiable and interpretable latent models of highdimensional neural activity using pi-vae. _Advances in neural information processing systems_ , 33:7234–7247, 2020. 

- [116] Mark M Churchland, John P Cunningham, Matthew T Kaufman, Justin D Foster, Paul Nuyujukian, Stephen I Ryu, and Krishna V Shenoy. Neural population dynamics during reaching. _Nature_ , 487(7405):51–56, 2012. 

- [117] Juan A Gallego, Matthew G Perich, Lee E Miller, and Sara A Solla. Neural manifolds for the control of movement. _Neuron_ , 94(5):978–984, 2017. 

- [118] Rishidev Chaudhuri, Berk Ger¸cek, Biraj Pandey, Adrien Peyrache, and Ila Fiete. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep. _Nature neuroscience_ , 22(9):1512–1520, 2019. 

29 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- [119] Marius Pachitariu, Carsen Stringer, Sylvia Schr¨oder, Mario Dipoppa, L Federico Rossi, Matteo Carandini, and Kenneth D Harris. Suite2p: beyond 10,000 neurons with standard two-photon microscopy. _BioRxiv_ , page 061507, 2016. 

- [120] Kurt Hornik, Maxwell Stinchcombe, and Halbert White. Multilayer feedforward networks are universal approximators. _Neural networks_ , 2(5):359–366, 1989. 

- [121] Georgios Arvanitidis, Lars Kai Hansen, and Søren Hauberg. Latent space oddity: on the curvature of deep generative models. _arXiv preprint arXiv:1710.11379_ , 2017. 

- [122] Michael David Spivak. _A comprehensive introduction to differential geometry_ . Publish or Perish, Inc., 2nd ed edition, 1979. 

- [123] Gabriel Taubin. Curve and surface smoothing without shrinkage. In _Proceedings of IEEE international conference on computer vision_ , pages 852–857. IEEE, 1995. 

- [124] Sergei Maslov and Kim Sneppen. Specificity and stability in topology of protein networks. _Science_ , 296(5569):910–913, 2002. 

- [125] Jason J Moore, Jesse D Cushman, Lavanya Acharya, Briana Popeney, and Mayank R Mehta. Linking hippocampal multiplexed tuning, hebbian plasticity and navigation. _Nature_ , 599(7885):442–448, 2021. 

30 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **9 Supplementary Information** 

## **10 Geometric decomposition and consolidation of single neuron place fields over trials** 

**==> picture [488 x 215] intentionally omitted <==**

Figure 6: **Individual place fields decompose consistently along rotation backshift and drift.** ( **a** ) Schematic of a single trajectory in the space of neuron activity with points colored by track markers that shift as the representation undergoes pure rotation/backshift (top), and 3 corresponding examples of single-neuron place fields undergoing pure backshift (bottom). ( **b** ) Schematic of a single trajectory undergoing both rotation/backshift and drift on the binned manifold (top), and 3 corresponding examples of single-neuron place fields undergoing a combination of backshift and drift (bottom). ( **c** ) model and data of a single neuron’s activity over position and trial (top), the change in activity across trial (blue) and from a pure rotation/backshift (orange) from the model (middle), where the change in activity over trials can be decomposed as a weighted sum of the pure rotation and a pure drift (bottom). ( **d** ) Model prediction (top) and data (bottom) of activity for single neurons displaying mostly rotation, but at different rates, leading to population-level drift. ( **e** ) Single neurons displaying a complex combination of rotation and drift. ( **f** ) Consolidation of rotation/backshift distribution for single neurons over time. ( **g** ) Rotation/backshift across all neurons averaged across all trials consistently positive for all animals. ( **h** ) Phase diagram of average rotation and drift component for each neuron and animal over all trials with two example model and data activity maps. 

To complement our population-level decomposition of collective backshift along rotation and drift, we seek a similar decomposition for the entire place fields of individual neurons. Traditionally, single neuron backshift has been quantified using scalar measures such as the neuron center of mass [41,42]. However, neuron tunings are often geometrically much more complex, exhibiting properties such as skew [25] and multiplex tuning [125], and drift [22, 26, 27], often violating the assumption that place fields can be thought of as uniquely coding for a specific position. Here we relax this assumption _via_ a functional approach by treating each neuron’s activity across an entire trial as a continuous function, and decomposing changes in that function over time along a component of pure backshift/rotation and pure drift. To build intuition, if the place fields of all neurons simultaneously backshift by the same amount, then there is no drift, and the evolution of the representation is constrained to a phase along a 1-dimensional line (Fig. 6A). If instead the place fields backshift at different rates or change shape, there emerges an additional component of drift (Fig. 6B). Hence, while not fully indicative of the population-level representation, here we extract the single-neuron component of backshift. 

To begin decomposing backshift and drift at the level of single neurons, we show the decoded activity of a single neuron across 50cm and _≈_ 100 trials from the model manifold, and the corresponding raw 

31 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

data (Fig. 6C, top). At a specific trial _t_ , we plot that neuron’s activity as a function of position, along with its activity at a later trial (Fig. 6C, middle blue), and its activity shifted in position indicating a pure rotation/backshift (Fig. 6, middle orange). We then decompose the place field change over trial (Fig. 6, bottom left) as a weighted sum of the pure rotational component (Fig. 6, bottom right, orange) and the residual which is the pure drift component (Fig. 6, bottom right, yellow). We further plot several examples of the model prediction and data for single neurons that largely contain a rotational component but backshift at different rates (Fig. 6D), thereby still resulting in a population-level drift. Additionally, while rotation/backshift is straightforward to characterize using statistics such as the center of activity for single place fields [42], our decomposition generalizes to arbitrarily complex fields. We plot additional examples of neurons that contain significant drift at the single-neuron level whether by changing field width, location, or relative spacing (Fig. 6E). 

To study the statistics and evolution of single-neuron rotation, we compute the average rotational component for each neuron in animal A7 for the first to fourth quarter segments of all trials, and plot the distribution of that average rotation for all neurons (Fig. 6F). We observe a statistically significantly positive rotation (backshift) across all trial segments, and a narrowing of the variance of rotation for later trials. We report a statistically significantly positive average single-neuron rotation for all animals (Fig. 6G). Finally, to broadly characterize the phase-space of single neuron behavior, we plot the average rotational and drift component across all trials for each neuron and each animal with two example place fields (Fig. 6H), showing an almost complete lack of neurons that purely rotate or have negative rotation on average. In sum, we demonstrate a per-neuron decomposition of representational drift into components of pure rotation and pure drift, report significant per-neuron rotation across all animals, and define a phase-space of single neuron behavior. 

32 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 635] intentionally omitted <==**

Figure 7: **Embedding of final day’s representation for all animals** . The embedding coordinates and vectors for the final day’s representation across all animals. Each vector is colored by the physical track marker of each mouse’s position on the linear maze, and the navy (orange) trace is the average trajectory for the near (far) trial on the final day. 

33 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 273] intentionally omitted <==**

Figure 8: **Distribution of angles between the position and trial vectors in the latent space for all animals, statistically tested using a 1-sided t-test against a null mean of** 90 _[◦]_ **.** 

34 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 274] intentionally omitted <==**

Figure 9: **Distribution of the advancement in positional representation per trial induced by the rotation in the surfaces of experience in the latent space for all animals, statistically tested using a 1-sided t-test against a null mean of 0mm/trial.** 

35 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 505] intentionally omitted <==**

Figure 10: **Data and model prediction of single neuron activity** . The activity of the 60 neurons with highest mean activity from the data and the corresponding model prediction decoded from the 3D latent space. Each bin is 30mm by 20 trials across all trials and all days for animal A7. 

36 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 677] intentionally omitted <==**

Figure 11: **Raw unfiltered time traces of activity for 264 neurons in the main text Figure 4 for a consecutive near and far trial on day 3 (left), and another consecutive near and far trial on day 2 (right), with the query region roughly marked in the dashed red box, and significant co-firing regions roughly marked in the dashed green boxes.** 

37 

bioRxiv preprint doi: https://doi.org/10.64898/2026.02.07.704615; this version posted February 8, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [488 x 345] intentionally omitted <==**

Figure 12: **Small-world graphs of significant co-firing cells for all animals using all neurons, and using 10% of neurons.** 

**==> picture [488 x 159] intentionally omitted <==**

Figure 13: **Geometry of single neuron place field under successor representation causes rotation and drift** . ( **A** ) Example of three artificial neurons coding for a circular track with initially unbiased position tuning (blue) and eventual direction-biased tuning (orange). ( **B** ) Plot of both the initial and final trajectories in the 3-dimensional state-space of neuron activity, showing how the geometry of the track changes and creates an acute angle. ( **C** ) Same state-space plot of the two trajectories viewed at a different angle from the side, showing that the change in the individual field shape induces a drift in representation. 

38 

