---
source_file: hasz2020_spatial_encoding_deliberation.md
paper_id: hasz2020_spatial_encoding_deliberation
title: "Spatial encoding in dorsomedial prefrontal cortex and hippocampus is related during deliberation"
authors:
  - "Brendan M. Hasz"
  - "A. David Redish"
year: 2020
journal: Hippocampus
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - prelimbic_cortex
keywords:
  - hippocampal_prefrontal_interaction
  - deliberation
  - prospective_spatial_encoding
  - vicarious_trial_and_error
  - bayesian_population_decoding
  - theta_oscillations
  - reward_encoding
  - non_local_representation
  - spatial_contingency_switching
  - place_cells
  - decision_making
  - prefrontal_executive_function
  - spatial
  - encoding
  - dorsomedial
  - prefrontal
  - cortex
  - hippocampus
  - related
  - during
key_citations:
  - redish2016_vicarious_trial_error_b
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

### One-line summary

Simultaneous recordings in rat dmPFC and CA1 during a spatial contingency-switching task reveal that dmPFC predicts whether hippocampus enters a prospective (non-local) encoding mode on a broad, seconds-long timescale, while hippocampal goal-location representations in turn drive fast, theta-cycle-locked increases in reward encoding in dmPFC.

---

### Background & motivation

Deliberation — the internal simulation and valuation of candidate actions prior to choice — is known to depend on both prefrontal cortex and hippocampus, but the precise nature of information exchange between these regions during deliberation remains unclear. Hippocampal ensembles are known to represent non-local (prospective) spatial information at decision points, yet what triggers these representations and how they feed back into prefrontal value computations is not well understood. The paper asks specifically: does dmPFC predict when hippocampus will enter a prospective mode, and does hippocampal prospective encoding reciprocally modulate reward representations in dmPFC?

---

### Methods

- **Subjects**: 6 FBNF-1 rats (4 male, 2 female), ages 8–14 months at experiment start.
- **Task**: Spatial contingency-switching maze with a single high-cost left/right choice point; contingency (Left, Right, or Alternate) switched every 30 ± 5 laps within a session. Rats ran ~138 laps per session (mean ± SD: 137.7 ± 31.7).
- **Recordings**: Simultaneous chronic tetrode arrays targeting CA1 of dorsal hippocampus (bilateral, 24 tetrodes) and 32-site silicon probe targeting right dmPFC (prelimbic/cingulate cortex area 1), recorded with an Intan RHD2000 system.
- **Spike sorting**: CA1 units sorted manually with MClust; dmPFC units sorted with Kilosort followed by manual refinement in Phy. Only sessions with ≥10 cells per area included.
- **Deliberation measure**: Vicarious trial and error (VTE) quantified with zIdPhi (z-scored integrated angular head velocity at the choice point).
- **Analysis**: Cross-validated Bayesian decoding of spatial position from ensemble activity in each area separately, using hippocampal theta cycle time bins (LFP band-passed 6–11 Hz). Decoded posteriors projected onto three zones (choice point, left reward zone, right reward zone). A separate Bayesian classifier trained on dmPFC firing rates predicted whether CA1 was in a local or prospective state. Lag analyses examined the temporal specificity of dmPFC-to-HPC and HPC-to-dmPFC relationships. Reward decoding from dmPFC trained on post-reward-zone-entry epochs (1–3 s) and applied to choice-point periods.

---

### Key findings

- Both CA1 and dmPFC decoded positions further ahead of the rat during VTE than non-VTE passes (CA1: p = .0156; dmPFC: p = .0469, one-sided Wilcoxon signed-rank, N = 6 rats), confirming prospective encoding in both areas during deliberation.
- Spatial representations in CA1 and dmPFC were correlated at the theta-cycle level: the two areas tended to represent either local (choice point) or prospective (reward zone) information within the same theta cycle (median Spearman's rho = .129, p = .0313), but the identity of the reward site being encoded was not significantly correlated between areas (p = .156).
- A Bayesian classifier trained on dmPFC firing rates predicted whether CA1 was in a prospective vs. local state above chance (AUROCs generally 0.6–0.8; >20 SDs above shuffle at zero lag). However, the classifier's performance was broad across lags (± several theta cycles and beyond), consistent with a seconds-long rather than cycle-precise relationship. Within-lap shuffles degraded performance more than between-lap shuffles, implicating a strategy-level signal in dmPFC.
- Reward encoding in dmPFC (decoded probability) increased significantly during hippocampal theta cycles in which CA1 represented the reward zone (increase of ~1.02% per theta cycle, p = .0021, Wilcoxon signed-rank, N = 40 sessions), but this effect was tightly locked to the zero-lag theta cycle — no other lags were significant after Bonferroni correction (α = .05 / N lags).
- The increase in dmPFC reward encoding during hippocampal prospective cycles was not significant in the first 10 laps of a contingency block (p = .202), but was significant and larger in the last 10 laps (2.2% per theta cycle, p = .00285), suggesting the effect is contingent on the animal having a confident model of the current contingency.
- No significant difference was found in dmPFC reward encoding between theta cycles when CA1 represented the chosen vs. unchosen goal location (p = .158).

---

### Computational framework

The paper uses **Bayesian population decoding** as its primary analytic framework. The key operation is cross-validated maximum-likelihood Bayesian decoding of continuous spatial variables (2D position) and binary outcome variables (reward vs. no-reward) from ensemble firing rates. Spatial posteriors are projected onto defined zones to yield per-theta-cycle estimates of what location each area is "representing." A classifier variant of the same framework is used to predict HPC state (local vs. prospective) from dmPFC activity at varying time lags.

The underlying process model is the **deliberative decision-making loop** (following Redish 2016): hippocampus generates prospective spatial representations corresponding to simulated candidate outcomes; prefrontal cortex both instigates these simulations (via top-down influence) and integrates the resulting value signals (via bottom-up hippocampal input) to support action selection. No formal computational model is fit; the framework is analytic rather than mechanistic.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view held that HPC and dmPFC form a bidirectional information-processing loop supporting deliberative decision-making. Hippocampal ensembles were known to represent non-local, prospective spatial information at decision points (Johnson & Redish, 2007; Kay et al., 2020), interpreted as internal simulation of candidate action outcomes. dmPFC was implicated in conflict detection, working memory, executive control, and the possible initiation of internal simulations (Hassabis & Maguire, 2009; van der Meer et al., 2012). Value signals associated with candidate outcomes were thought to be generated in ventral striatum and orbitofrontal cortex. Theta oscillation coherence between HPC and mPFC was established as a correlate of spatial working memory and deliberation (Benchenane et al., 2010; Jones & Wilson, 2005). What remained unclear was (a) what specific information passes between HPC and dmPFC, (b) the direction and timescale of any causal influence, and (c) whether dmPFC genuinely initiates hippocampal prospective representations or merely co-activates with them.

---

### What this paper contributes

The paper establishes two dissociable relationships between dmPFC and CA1 during deliberation, with different temporal signatures:

1. **dmPFC → HPC influence is temporally diffuse (seconds-scale)**: dmPFC firing rates predict whether CA1 will be in a prospective state, but this predictability is stable across many theta cycles before and after the event, consistent with dmPFC encoding a slow strategic state (deliberate vs. automatic mode) rather than triggering individual simulation events.

2. **HPC → dmPFC influence is temporally precise (single theta-cycle)**: When CA1 represents a goal location, reward encoding in dmPFC increases, but only within the same theta cycle — the effect does not persist to adjacent cycles. This suggests fast, within-cycle feed-forward influence from hippocampal spatial recall to prefrontal value representations.

Together these findings refine the prevailing loop model: dmPFC may set the context for deliberation broadly (whether to simulate) rather than triggering specific simulations cycle-by-cycle; and goal-location information retrieved by HPC updates prefrontal reward estimates rapidly, on the timescale of a single theta cycle (~100 ms). The asymmetric timescales argue against a simple synchronised co-representation model and suggest the two areas play functionally distinct roles within the same deliberative episode.

---

### Brain regions & systems

- **CA1 of dorsal hippocampus** — primary locus of prospective (non-local) spatial encoding during deliberation; encodes candidate goal locations during VTE; provides fast feed-forward spatial information to dmPFC within single theta cycles.
- **Dorsomedial prefrontal cortex (dmPFC)**, specifically overlapping prelimbic cortex, cingulate cortex area 1, and portions of secondary motor cortex — encodes both spatial position (prospective and local) and reward/outcome information; predicts HPC prospective state on a slow, strategy-level timescale; receives and integrates hippocampal goal-location signals into reward representations on a fast theta-cycle timescale.
- **Nucleus reuniens and thalamic relay nuclei** — discussed in the introduction as a bisynaptic bidirectional anatomical pathway between CA1 and dmPFC, providing a candidate substrate for the rapid HPC-to-PFC information transfer identified in the results (not directly recorded).

---

### Mechanistic insight

The paper partially meets the bar. It proposes an algorithmic account (dmPFC sets a slow deliberative context; HPC-recalled goal representations update dmPFC reward encoding within theta cycles) and provides neural recordings from both areas that are consistent with this account. However, it does not provide data that selectively support the proposed algorithm over alternatives. Specifically:

- The slow, broad temporal profile of dmPFC predicting HPC state is consistent with a strategic context signal, but could equally reflect shared common input (e.g., from nucleus reuniens or basal ganglia) or non-causal co-modulation.
- The fast, theta-cycle-locked increase in dmPFC reward encoding during hippocampal prospective cycles is correlational; no manipulation (optogenetics, inactivation, disconnection) is used to test whether the HPC signal causally drives the PFC change.
- The implementational level is not addressed: the paper does not resolve which cell types, synaptic pathways, or oscillatory mechanisms mediate the identified interactions.

**Computational**: The brain is solving the problem of selecting the action with the highest expected value during spatial deliberation, requiring internal simulation of candidate outcomes and their valuations.
**Algorithmic**: dmPFC maintains a strategy-level state determining whether the system is in a deliberative mode (slow signal, seconds-long); within that mode, each theta cycle in which HPC recalls a goal location transiently updates prefrontal reward expectations.
**Implementational**: Not resolved. Anatomical pathways (monosynaptic CA1→dmPFC and bisynaptic CA1→reuniens→dmPFC) are discussed as candidate substrates but not tested.

---

### Limitations & open questions

- All findings are correlational; no causal manipulation of dmPFC or HPC is performed to test the directionality of the identified relationships.
- The broad temporal profile of dmPFC predicting HPC state could reflect common input rather than true top-down control; the paper acknowledges this but cannot adjudicate between these accounts.
- Only 6 rats were used, which limits statistical power for between-rat comparisons and generalisability.
- Only CA1 was recorded from the hippocampus; the roles of CA3, dentate gyrus, or subiculum in the deliberative loop are not assessed.
- The increase in dmPFC reward encoding during hippocampal prospective cycles was not significantly greater than local cycles at the population level (p = .12), qualifying the claimed fast HPC-to-PFC influence.
- The paper cannot distinguish between the hypothesis that HPC drives the change in PFC reward encoding versus both areas co-modulating in response to a third signal.
- The functional significance of the dissociation between chosen and unchosen goal representations for actual choice behaviour is not resolved (p = .158, non-significant trend).
- Recordings were confined to right hemisphere dmPFC; lateralisation effects were not assessed.

---

### Connections & keywords

**Key citations**:
- Johnson & Redish (2007) — hippocampal non-local representations at decision points
- Kay et al. (2020) — sub-second cycling between hippocampal future representations
- Redish (2016) — vicarious trial and error review
- van der Meer et al. (2012) — deliberative decision-making systems
- Zielinski, Shin, & Jadhav (2019) — coherent spatial coding in HPC-PFC via theta oscillations
- Hasz & Redish (2020) — companion paper on strategic context encoding in dmPFC and HPC
- Schmidt, Duin, & Redish (2019) — dmPFC disruption alters hippocampal deliberative sequences
- Benchenane et al. (2010) — theta coherence and learning in HPC-PFC network
- Rich & Wallis (2016) — value switching in orbitofrontal cortex

**Named models or frameworks**:
- Vicarious trial and error (VTE) / zIdPhi metric
- Cross-validated Bayesian population decoding
- Contingency switching task (spatial reversal)
- Drift-diffusion / sequential sampling models (discussed in relation to value-based decisions)
- CRAMS hypothesis (Wang, Cohen, & Voss, 2015) — covert rapid action-memory simulation

**Brain regions**:
- CA1 (dorsal hippocampus)
- Dorsomedial prefrontal cortex (dmPFC; prelimbic cortex, cingulate cortex area 1)
- Nucleus reuniens (discussed as anatomical relay)

**Keywords**:
- hippocampal-prefrontal interaction
- deliberation
- prospective spatial encoding
- vicarious trial and error
- Bayesian population decoding
- theta oscillations
- reward encoding
- non-local representation
- spatial contingency switching
- place cells
- decision-making
- prefrontal executive function

### Related wiki pages
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]
