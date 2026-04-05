---
source_file: wen2024_entorhinal_maps_navigation_b.md
title: One-shot entorhinal maps enable flexible navigation in novel environments
authors: John H. Wen, Ben Sorscher, Emily A. Aery Jones, Surya Ganguli, Lisa M. Giocomo
year: 2024
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Grid cells in the medial entorhinal cortex form stable spatial maps in novel environments after a single exposure through fixed landmark inputs that weakly pin activity on a toroidal attractor, while flexible navigation is enabled by downstream plasticity implementing behavioural timescale synaptic plasticity.

---

### Background & motivation

Animals must navigate changing environments to find resources, yet how the brain rapidly incorporates novel or changing environmental features into neural spatial maps remains unknown. Two existing solutions have been proposed: (1) rigid path integration systems that accumulate error without landmarks, and (2) slower Hebbian plasticity that requires minutes to hours to integrate new landmarks. Neither mechanism fully explains previous observations that grid cells are sensitive to environmental boundaries and rewards while also exhibiting rapid remapping. This study investigates a third possibility: that fixed landmark-to-grid cell connectivity enables rapid map formation while allowing downstream plasticity to support flexible behaviour.

---

### Methods

**Experimental design:**
- Recorded 68,484 neurons (15,342 grid cells) from medial entorhinal cortex (MEC) using Neuropixels probes in head-fixed mice navigating virtual reality 1D tracks
- Three main experimental paradigms:
  1. **Build-up track**: 320-cm track where visual features (optic flow, tower landmarks) were cumulatively added across 9 blocks
  2. **Random environment track**: 100-cm track with 5 landmarks pseudo-randomly rearranged across 12 environments
  3. **Hidden reward task**: 200-cm track with 4 landmarks and unmarked reward zone; landmarks shifted forward/backward to test behavioural adaptation

**Analysis approaches:**
- Sorted co-modular grid cells onto 2D toroidal neural sheet based on firing phases
- Extracted moment-by-moment attractor state as centre of mass of activity bump
- Quantified anisometry (distance distortion) and geodesic curvature of bump trajectories
- Linear decoding of position from grid cell population activity
- Muscimol inactivation of MEC to assess causal role in behaviour

**Computational modelling:**
- 2D dynamical model of activity bump on toroidal sheet with landmark-induced pinning
- Velocity input with angular drift diffusion (D = 1.16 ± 0.07 deg² m⁻¹)
- Landmark inputs as weak pinning to fixed phases on neural sheet
- BTSP-based decoder for modelling downstream plasticity

---

### Key findings

- **Grid cell attractor dynamics in darkness**: Grid cells exhibit low-dimensional continuous attractor dynamics on a toroidal manifold. In darkness, the activity bump drifts diffusively (D = 1.16 ± 0.07 deg² m⁻¹) with stable grid scale (<5% drift over 100 m), consistent with accumulation of path integration error.

- **Landmarks induce one-shot remapping**: Visual landmarks rapidly entrain grid cells to periodic firing patterns. A single landmark exposure is sufficient to induce remapping (average 1.29 ± 0.07 trials to stabilize). Grid cells maintain high spatial correlation within blocks with landmarks but not across blocks (P < 1 × 10⁻¹⁰).

- **Remapping as bump trajectory changes**: Remapping corresponds to the activity bump taking a new trajectory on the toroidal attractor. Despite remapping, grid cells maintain continuous attractor dynamics with preserved temporal correlations between cells.

- **Landmarks cause weak pinning**: Landmarks do not strongly pin the bump to fixed neural sheet locations (history dependence observed). The trajectory in any environment is influenced by both landmarks and the bump's history from previous environments.

- **Grid distortions are predictable**: In random environments, grid cell firing patterns show significant anisometry (P < 1 × 10⁻¹⁰) and geodesic curvature (P < 1 × 10⁻¹⁰) with landmarks, unlike the straight geodesics in darkness. A computational model with fixed landmark-to-grid connectivity predicts held-out grid cell firing patterns (Pearson r significantly above shuffle, P = 3.58 × 10⁻¹⁸).

- **No plasticity in landmark-grid connections**: Incorporating Hebbian learning into the model revealed that a learning rate of zero best explains neural data, indicating fixed landmark-to-grid cell connectivity.

- **Behavioural adaptation despite distorted grid codes**: In the hidden reward task, landmark shifts permanently distort grid cell firing patterns (decoded position never recovers), yet animals adapt behaviourally within <10 trials.

- **MEC required for task performance**: Grid cell stability correlates with behavioural performance (Pearson r = −0.20, P < 1 × 10⁻¹⁰). Muscimol inactivation of MEC impairs performance (P = 0.0004) and reduces grid stability, confirming causal role.

- **Downstream plasticity enables flexibility**: A BTSP-based decoder rapidly adapts to landmark shifts and reliably predicts reward location, while a fixed decoder fails. This suggests downstream plasticity (possibly in CA1) compensates for fixed, distorted grid cell maps.

---

### Computational framework

**Continuous attractor networks**: The paper conceptualizes grid cells as forming a low-dimensional continuous attractor on a 2D toroidal manifold. The population activity is organized as a localized "bump" of activity that translates across a neural sheet as the animal moves through space.

**Dynamical systems model**: The computational model formalizes grid cell dynamics as:
- An activity bump moving on a periodic 2D sheet with toroidal topology
- Velocity input drives bump translation with angular drift diffusion (D = 1.16 deg² m⁻¹)
- Visual landmarks provide weak pinning inputs to fixed phases on the neural sheet
- The pinning function: when the animal is within 50 cm of a landmark, the bump is tugged toward the landmark's fixed pinning phase

**Key model assumptions**:
- Fixed landmark-to-grid connectivity (no Hebbian plasticity)
- Weak pinning strength (landmarks influence but don't fully determine bump trajectory)
- History dependence (bump trajectory influenced by previous environments)

The model successfully predicts grid cell firing patterns in held-out environments and captures anisometry and curvature distortions observed in neural data.

---

### Prevailing model of the system under study

Before this study, the field held two competing views of how grid cells adapt to novel environments:

1. **Rigid path integration system**: Grid cells rely primarily on idiothetic cues to encode distance travelled. This system operates instantly but accumulates error without external landmarks. Evidence supporting this view included the observation that grid cells maintain firing in darkness and the theoretical appeal of path integration models.

2. **Slow Hebbian plasticity system**: Grid cells integrate environmental features through synaptic plasticity mechanisms, allowing flexible adjustment of spatial maps. This system is accurate but requires time (minutes to hours) and repeated experience. Evidence came from studies in Drosophila showing Hebbian plasticity operates on the timescale of minutes to integrate novel landmarks.

Neither model fully explained prior observations that: (1) grid cells are sensitive to environmental boundaries and rewards (inconsistent with rigid path integration), (2) geometric perturbations cause persistent distortions lasting days (inconsistent with rapid Hebbian plasticity), and (3) grid cells can remap rapidly in novel environments. The field lacked a mechanistic understanding of how grid cell attractor dynamics evolve moment-by-moment as environmental features change.

---

### What this paper contributes

This paper establishes a hybrid mechanism for rapid spatial map formation that resolves the tension between speed and accuracy in navigation:

**Fixed landmark-grid architecture enables one-shot map formation**: The study demonstrates that grid cells form stable firing patterns in novel environments after a single exposure (one-shot remapping). This rapid stabilization occurs through fixed connections between visual landmarks and specific phases on the grid cell neural sheet. The landmark inputs "weakly pin" the activity bump, causing it to take distorted but stable trajectories. Importantly, the best-fitting model requires zero Hebbian plasticity in landmark-grid connections, indicating these connections are hard-wired or established through slow plasticity over long timescales.

**Distorted grid codes support spatial representation**: The fixed pinning architecture necessarily produces distorted grid cell firing patterns—distances in real space do not map proportionally to distances in neural space (anisometry), and bump trajectories curve rather than follow straight geodesics. These distortions are predictable from the model and persist indefinitely (grid cells never "un-distort" after landmark shifts). This challenges the assumption that regular grid patterns are required for accurate navigation.

**Downstream plasticity enables behavioural flexibility**: While grid cell maps remain distorted, animals adapt behaviourally to landmark shifts within <10 trials. The study identifies the mechanism: downstream regions (likely CA1) implement behavioural timescale synaptic plasticity (BTSP), which can rapidly learn to decode distorted grid cell activity. A BTSP-based decoder model successfully predicts reward location across shifted environments, while fixed decoders fail. MEC inactivation impairs performance, confirming that grid cells provide necessary spatial information even when their firing patterns are distorted.

**Unified framework for navigational flexibility**: The findings establish a computational principle: the brain balances rapidity and accuracy through a division of labour. Fixed connections enable rapid map formation (essential for novel environments), while downstream plasticity enables flexible behaviour (essential for changing environments). This framework predicts that any navigation system must have both stable upstream representations and plastic downstream decoders to function effectively.

---

### Brain regions & systems

**Medial entorhinal cortex (MEC)** — Primary brain region studied. Contains grid cells that form the neural spatial map. The study demonstrates that MEC grid cells:
- Form discrete modules with characteristic scale ratios (~1.4–1.7)
- Exhibit continuous attractor dynamics on a 2D toroidal manifold
- Rapidly remap to novel environments via fixed landmark inputs
- Maintain distorted but stable firing patterns after landmark shifts
- Are causally required for navigation (muscimol inactivation impairs performance)

**Hippocampus (CA1)** — Implicated as downstream region implementing behavioural adaptation. The study proposes that CA1 place cells use BTSP to rapidly learn to decode distorted MEC grid cell activity, enabling behavioural flexibility despite fixed upstream representations.

**Lateral entorhinal cortex (LEC)** — Mentioned as a region containing information about rewarded locations that could support flexible behaviour.

**Visual cortex (V1)** — Mentioned as a potential source of landmark input to grid cells.

**Subiculum** — Mentioned as containing boundary vector and corner cells that could provide landmark input.

---

### Mechanistic insight

This paper provides strong mechanistic insight by combining neural recordings, behavioural experiments, and computational modelling to reveal a two-level architecture for spatial navigation.

**Computational level (Marr's levels analysis):**

- **Computational**: The brain must solve the problem of rapidly forming stable spatial maps in novel environments while maintaining accurate navigation despite environmental changes. The solution balances rapidity (fixed connections) against accuracy (plastic downstream decoding).

- **Algorithmic**: Grid cells implement a continuous attractor network on a 2D toroidal manifold. The algorithm combines: (1) velocity integration (path integration) that drives bump translation with angular drift diffusion, and (2) weak landmark pinning that tugs the bump toward fixed neural sheet locations when landmarks are within 50 cm. The pinning is weak—landmarks influence but do not fully determine bump trajectory, which retains history dependence from previous environments.

- **Implementational**: The neural implementation involves discrete grid cell modules with characteristic scale ratios (~1.4–1.7). Grid cells within modules maintain phase relationships across long distances. The toroidal attractor is implemented through recurrent connectivity within MEC. Landmark inputs project to fixed phases on the neural sheet—no rapid Hebbian plasticity is required. Downstream, CA1 place cells likely implement BTSP to decode distorted grid activity, with muscimol inactivation confirming MEC's causal role in navigation.

**Evidence supporting the mechanism:**

1. **Fixed landmark-grid connectivity**: The best-fitting model learning rate was zero—Hebbian plasticity worsened rather than improved predictions. This indicates landmark inputs are hard-wired or established through slow plasticity over developmental timescales.

2. **Weak pinning**: Landmarks entrain but do not fully determine bump trajectories. The activity bump takes different paths in visually identical environments (history dependence), and landmarks produce distorted but stable maps.

3. **Distorted grid codes**: Grid cells show significant anisometry (P < 1 × 10⁻¹⁰) and geodesic curvature (P < 1 × 10⁻¹⁰) with landmarks, unlike the straight geodesics in darkness.

4. **Downstream plasticity required**: Fixed decoders fail to predict position across landmark shifts, but BTSP-based decoders succeed. Animals adapt behaviourally within <10 trials despite permanent grid distortions. MEC inactivation impairs navigation.

This paper thus meets the high bar for mechanistic insight: it presents a formal algorithm (continuous attractor with weak landmark pinning), provides neural data supporting that algorithm over alternatives (zero plasticity required, weak pinning evidenced by history dependence), and identifies the physical implementation (discrete grid modules, fixed landmark-MEC connectivity, BTSP in downstream CA1).

---

### Limitations & open questions

- **Nature of landmark inputs**: The specific neural source of landmark inputs to grid cells remains unknown. Candidates include MEC non-grid spatial cells, border cells, object vector cells, lateral entorhinal cortex neurons, V1 neurons, and subicular boundary vector/corner cells. The model assumes simple connectivity (one landmark → one pinning phase), but broader connectivity fields may exist.

- **Exact downstream plasticity mechanism**: While BTSP is proposed as the mechanism enabling behavioural flexibility, the exact plasticity mechanism requires further investigation. Alternative possibilities include Hebbian learning in associative networks or lateral entorhinal cortex involvement.

- **Temporal limits of fixed connectivity**: The study demonstrates fixed connectivity over minutes to hours. Whether landmark-grid connections remain fixed over longer timescales (days to weeks) or can eventually undergo plasticity remains unclear.

- **Generalization to 2D environments**: All experiments were conducted in 1D virtual reality environments. Whether the same principles apply to natural 2D navigation requires further study.

- **Coordination between grid modules**: The study finds that landmarks disrupt coordination between grid modules (which normally drift coherently in darkness). The functional implications of this discoordination remain unexplored.

- **Role of non-grid spatial cells**: While 56% of non-grid spatial cells exhibited landmark-tuned responses, their specific contribution to navigation and their relationship to grid cell activity remain unclear.

---

### Connections & keywords

**Key citations:**
- Hafting et al. (2005) — foundational discovery of grid cells
- Fyhn et al. (2007) — hippocampal remapping and grid realignment
- McNaughton et al. (2006) — path integration and cognitive maps
- Bittner et al. (2017) — behavioural timescale synaptic plasticity (BTSP)
- Gu et al. (2018) — map-like micro-organization of grid cells
- Gardner et al. (2022) — toroidal topology of grid cell population activity
- Yoon et al. (2013) — evidence for continuous attractor dynamics in grid cells
- Kim et al. (2019) & Fisher et al. (2019) — landmark plasticity in Drosophila heading system
- Ocko et al. (2018) — emergent elasticity in neural code for space

**Named models or frameworks:**
- Continuous attractor network (CAN) model of grid cells
- Toroidal attractor manifold framework
- 2D dynamical model with weak landmark pinning
- Path integration system
- Behavioural timescale synaptic plasticity (BTSP)
- Hebbian learning (as comparator)

**Brain regions:**
- Medial entorhinal cortex (MEC) — primary focus; contains grid cells, non-grid spatial cells, border cells, object vector cells
- Hippocampus CA1 — downstream region implementing BTSP for flexible decoding
- Lateral entorhinal cortex (LEC) — encodes object locations and rewarded locations
- Visual cortex (V1) — potential source of landmark input
- Subiculum — contains boundary vector and corner cells

**Keywords:**
grid cells, entorhinal cortex, spatial navigation, continuous attractor networks, toroidal manifold, remapping, visual landmarks, path integration, behavioural timescale synaptic plasticity (BTSP), virtual reality, Neuropixels, one-shot learning, neural population dynamics, hippocampus, cognitive map
