---
source_file: "olafsdottir2015_place_cells_reward.md"
paper_id: "olafsdottir2015_place_cells_reward"
title: "Hippocampal place cells construct reward related sequences through unexplored space"
authors: "H Freyja Olafsdottir, Caswell Barry, Aman B Saleem, Demis Hassabis, Hugo J Spiers"
year: 2015
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["t_maze"]
methods: ["tetrode_recording"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "prefrontal_cortex"]
frameworks: ["reinforcement_learning"]
keywords: ["hippocampal", "place", "cells", "construct", "reward", "related", "sequences", "through", "unexplored", "space"]
key_citations: ["davidson2009_hippocampal_replay_extended", "singer2009_reward_reactivation_hippocampus", "lee2002_memory_sequential_experience"]
---

### One-line summary

Viewing food delivered to an unvisited, visible arm of a maze is sufficient to trigger hippocampal place cell "preplay" — off-line pre-activation of spatial sequences representing that unrewarded-yet-motivationally-relevant space — whereas no such preplay is observed for an otherwise equivalent arm without reward.

---

### Background & motivation

Dominant theories of hippocampal function hold that place cell representations form during an animal's first physical encounter with an environment and are subsequently replayed during off-line states (sleep/rest) to support memory consolidation and future behaviour. Prior work on "preplay" (off-line activation of sequences before actual exploration) had focused on de novo preplay of entirely novel environments, leaving open whether motivational salience or visual access alone could drive the formation and pre-activation of a hippocampal spatial representation before any physical exploration. This paper asks whether the presence of an inaccessible but visible and rewarded goal is sufficient to elicit preplay of that unvisited space.

---

### Methods

- **Subjects**: 4 male lister-hooded rats implanted with tetrodes targeting hippocampal CA1 (37–66 place cells recorded per rat; 212 cells total).
- **Apparatus**: T-shaped raised track (stem 222 cm; arms 200 cm tip-to-tip). A transparent barrier blocked access to the arms throughout the initial run phase, allowing visual but not physical access.
- **Experimental phases**:
  1. REST1: ≥60 min pre-task rest recording.
  2. RUN1: 20 laps on the stem only; arms blocked by barrier.
  3. GOAL-CUE: experimenter baited one arm with food while the animal remained on the stem (~10 min); cued arm counterbalanced across animals.
  4. REST2: ≥60 min rest following goal-cueing.
  5. RUN2: barrier removed; animals ran alternate L-shaped laps covering both arms (20 laps per arm); place cell templates generated from this session.
- **Spiking events**: defined as periods ≤300 ms where ≥15% of cells were co-active, associated with elevated sharp-wave ripple power (80–250 Hz).
- **Preplay analysis (primary)**: Spearman rank-order correlation between cell firing sequences in rest events and future RUN2 place-cell templates (four templates: to/from each arm). Proportion of significant events compared to shuffle via binomial test.
- **Preplay analysis (secondary)**: Bayesian spatial reconstruction using a Poisson spiking framework; decoded posterior probability matrices fit with straight-line trajectories; significance assessed against cell-identity shuffle.
- **Behavioural measures**: dwell-time and head-direction bias towards cued vs uncued side of stem during GOAL-CUE and RUN1; arm preference on first lap of RUN2.

---

### Key findings

- During REST2, the cued arm was significantly preplayed (7.37% of spiking events; p < 0.001 binomial test vs chance); the uncued arm was not (4.41%, p = 0.33); the two arms differed significantly (p < 0.001).
- This effect replicated in all four animals individually.
- Cued arm preplay was absent during REST1 (4.74%, p = 0.34), confirming the effect was triggered by goal-cueing rather than by proximity to the upcoming RUN2 session.
- Preplay of the stem during REST1 was also non-significant (4.12%, p = 0.44), ruling out a general temporal-proximity artefact.
- Preplay of the cued arm emerged at the start of GOAL-CUE: cued arm cells showed a significantly elevated firing rate ratio relative to uncued arm cells during the early half of GOAL-CUE (ratio = 1.78, p = 0.01), persisting but attenuating into REST2 (early ratio = 1.30, p < 0.001; late ratio = 1.10, p < 0.01).
- Cued arm preplay events were equally forward and reverse (6.93% vs 7.80%, p = 0.18) and equally distributed to and from the arm (7.34% vs 7.40%, p = 0.49).
- Bayesian reconstruction independently confirmed selective preplay of the cued arm in REST2 (7.64%, p < 0.001) but not the uncued arm (4.78%, p = 0.55) or either arm in REST1.
- The amount of individual preplay correlated with each animal's behavioural interest in the cued arm during GOAL-CUE.
- All four animals preferentially turned toward the cued arm on the first lap of RUN2 (mean arm bias = 0.96).
- Preferential preplay was not explained by differences in cell number, spike-sorting quality, place field stability, or place field location on the two arms.

---

### Computational framework

Not applicable as a formal computational framework. The analysis uses two complementary data-analysis methods: (1) rank-order template matching (Spearman correlations between event spike sequences and RUN2 templates, with cell-identity shuffles), and (2) Bayesian spatial reconstruction under a Poisson spiking model, with position posteriors decoded using maximum-likelihood straight-line trajectory fitting. Neither constitutes a mechanistic model of hippocampal computation — they are decoding/analysis tools applied to neural recordings.

The results are interpreted in terms of preconfigured hippocampal cell assemblies ("charts"; McNaughton et al., 1996) that become bound to a motivationally salient environment before any physical exploration, and are discussed in relation to reinforcement-learning-adjacent ideas (temporal credit assignment, reverse replay as evaluation of action sequences). However, no formal RL or other computational model is fitted to the data.

---

### Prevailing model of the system under study

The paper's introduction situates itself against two major claims in the hippocampal literature. First, dominant theories hold that stable place cell representations form during an animal's *first encounter* with a novel environment (requiring physical exploration) and that subsequent off-line replay serves consolidation and future behaviour. Second, the prior "de novo preplay" literature (Dragoi & Tonegawa, 2011, 2013, 2014) proposed that preconfigured cell assemblies can be activated before exploration of a novel space, but these studies did not specifically manipulate motivational relevance or visual access. The baseline model is therefore that: (a) hippocampal spatial representations require direct physical experience to form; and (b) replay/preplay is modulated by reward (Cheng & Frank, 2008; Singer & Frank, 2009; Pfeiffer & Foster, 2013) but this modulation had not been extended to preplay of entirely unvisited spaces. The introduction is reasonably explicit about this theoretical landscape.

---

### What this paper contributes

The key finding is that physical exploration is not required for the hippocampus to form and pre-activate a spatial representation of an environment — visual access combined with motivational relevance (reward) is sufficient. This extends the modulatory influence of reward on hippocampal replay to the domain of preplay, and specifically to spaces the animal has never entered. The results constrain theories of hippocampal function in the following ways:

- Place cell sequences for unvisited environments can be constructed on the basis of visual information alone, provided the space is motivationally relevant.
- The hippocampal bias is goal-specific: an equally visible but unrewarded arm was not preplayed under identical conditions.
- Preplay begins during the goal-cueing epoch itself (not just during subsequent rest), implying rapid association of preconfigured cell assemblies with a motivationally relevant visible space.
- The findings are consistent with the "charts" or preconfigured assembly hypothesis (McNaughton et al., 1996), but do not distinguish between active simulation of goal-directed trajectories and passive capture of assemblies by motivational salience.
- The paper does not find de novo preplay of the stem during REST1, leaving open (without contradicting) whether de novo preplay exists independently of reward; the authors suggest environmental complexity may have suppressed it.

---

### Brain regions & systems

- **Hippocampus CA1** — primary recording site; locus of place cell sequences and sharp-wave ripple-associated preplay events. Central to the paper's entire argument.
- **Sharp-wave ripple complexes (CA1 LFP, 80–250 Hz)** — used to validate spiking events as candidate replay/preplay events; preplay events showed significantly elevated ripple power compared to non-significant spiking events and non-event periods.

No other brain regions are recorded or lesioned. The paper makes no direct claims about upstream inputs (e.g., entorhinal cortex, prefrontal cortex) though the discussion notes that place field formation could be driven by feed-forward cortical input (Hartley et al., 2000) as an alternative to the chart hypothesis.

---

### Mechanistic insight

The paper meets both criteria:

1. It proposes an algorithm: goal-triggered preplay as pre-activation of preconfigured hippocampal cell assemblies for motivationally relevant, visually accessible but physically unvisited spaces — offering a mechanism by which the hippocampus could prepare spatial representations for future experiences before they occur.
2. It provides neural data (CA1 single-unit recordings and LFP) that specifically support this mechanism over the null hypothesis that preplay requires prior physical exploration.

**Marr's three levels:**

- **Computational**: The brain is solving the problem of preparing for efficient spatial navigation to a reward-relevant goal before the animal is physically able to access it. The hippocampus constructs a prospective map of motivationally salient but unvisited spaces, supporting goal-directed navigation and potentially temporal credit assignment.
- **Algorithmic**: Preconfigured place cell assemblies (whose internal sequential structure is latent prior to experience) are selectively bound to the representation of the cued environment during the goal-cueing period. During subsequent rest, sharp-wave ripple events replay these sequences in both forward and reverse orders, analogous to the planning and evaluation functions proposed for post-exploration replay. The binding is rapid (detectable within ~5 min of goal-cueing) and reward-specific (absent for the unrewarded arm).
- **Implementational**: CA1 recordings with tetrodes; spiking events co-occurring with elevated sharp-wave ripple power (80–250 Hz). The paper does not address the specific circuit mechanism by which reward or goal information biases the activation of particular cell assemblies — this remains an open question. Cell types beyond putative CA1 pyramidal cells are not distinguished, and neuromodulatory mechanisms are not addressed.

**Bonus**: No specific cell types, connectivity patterns, or neuromodulators are identified as the implementational basis of the reward-driven bias.

---

### Limitations & open questions

- Only 4 rats; results are consistent across animals but statistical power is limited for some analyses (e.g., GOAL-CUE epoch preplay analysis was nominally non-significant at p = 0.052 for the proportion measure).
- The paper does not establish whether goal-biased preplay *causally* supports subsequent navigation to the goal. The correlation between behavioural interest and preplay amount is suggestive but not causal.
- Forward and reverse preplay occurred at equal rates, complicating a clean interpretation in terms of planning (forward) vs credit assignment (reverse); the paper acknowledges this but does not resolve it.
- The absence of de novo preplay (no significant preplay of the stem in REST1) is not fully explained; the authors speculate that environmental complexity may have suppressed it. This leaves the relationship between de novo preplay and goal-driven preplay unresolved.
- The mechanism by which reward/motivational salience biases which preconfigured cell assemblies become active is unaddressed — candidate mechanisms include dopaminergic neuromodulation, VTA-hippocampus projections, or prefrontal-hippocampal communication, but none are examined.
- Whether this phenomenon generalises to non-spatial or more abstract motivationally relevant representations is noted as a future direction (Kraus et al., 2013; Eichenbaum & Cohen, 2014).
- The paper cannot distinguish whether goal-biased preplay reflects active simulation of trajectories to the goal vs passive differential activation of cells near the cued location (though control analyses argued against a simple proximity confound).

---

### Connections & keywords

**Key citations**:
- Dragoi & Tonegawa (2011, 2013, 2014) — de novo preplay in novel environments
- Foster & Wilson (2006) — reverse replay; spiking event analysis methods
- Diba & Buzsaki (2007) — forward and reverse hippocampal sequences during ripples
- Pfeiffer & Foster (2013) — hippocampal place-cell sequences and future path planning to remembered goals
- Singer & Frank (2009) — reward modulation of hippocampal reactivation
- McNaughton et al. (1996) — preconfigured cell assembly / "charts" hypothesis
- Lee & Wilson (2002) — template-matching analysis of hippocampal replay
- Davidson et al. (2009) — Bayesian reconstruction of hippocampal replay
- Wilson & McNaughton (1994) — foundational hippocampal replay during sleep

**Named models or frameworks**:
- Rank-order template matching (Lee & Wilson, 2002; Foster & Wilson, 2006)
- Bayesian spatial reconstruction (Zhang et al., 1998; Davidson et al., 2009)
- Preconfigured cell assemblies / "charts" (McNaughton et al., 1996)
- De novo preplay (Dragoi & Tonegawa, 2011)

**Brain regions**:
- Hippocampus CA1
- Sharp-wave ripple complexes (CA1 LFP)

**Keywords**:
- hippocampal preplay
- place cells
- sharp-wave ripples
- reward-modulated replay
- spatial sequence reactivation
- goal-directed navigation
- preconfigured cell assemblies
- offline reactivation
- T-maze
- Bayesian spatial decoding
- motivational salience
- prospective coding
