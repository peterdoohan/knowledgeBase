---
source_file: "maggi2022_activity_subspaces_prefrontal.md"
paper_id: "maggi2022_activity_subspaces_prefrontal"
title: "Activity Subspaces in Medial Prefrontal Cortex Distinguish States of the World"
authors: "Silvia Maggi, Mark D. Humphries"
year: 2022
journal: "The Journal of Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["y_maze"]
methods: ["tetrode_recording", "behavioral_analysis"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex", "infralimbic_cortex"]
frameworks: ["reinforcement_learning", "mixed_selectivity"]
keywords: ["activity", "subspaces", "medial", "prefrontal", "cortex", "distinguish", "states", "world"]
key_citations: ["fusi2016_mixed_selectivity_cognition", "ito2015_prefrontal_thalamic_hippocampus"]
---

### One-line summary

In rats learning rules on a Y-maze, medial prefrontal cortex (mPfC) population activity occupies distinct, linearly separable low-dimensional subspaces for the trial (present state) and intertrial interval (past state), with near-orthogonal decoding axes between phases, allowing downstream targets to independently read out different world states and enabling differential reactivation during post-training sleep.

---

### Background & motivation

The medial prefrontal cortex is known to represent both the immediate past (working memory) and the current state of the world (ongoing decisions and sensory context), but how a single mPfC population can simultaneously encode multiple distinct states without catastrophic interference has been unclear. Prior studies showed past and upcoming choices can both modulate activity of neurons in the same mPfC population, yet none had compared how different world states are represented at the population level or explained how downstream readouts could distinguish them. This paper addresses the interference problem directly by asking whether, and through what geometric arrangement, the same mPfC population can represent two temporally distinct states of the world.

---

### Methods

- **Subjects and data**: Reanalysis of tetrode recordings from 4 male Long-Evans rats (Peyrache et al., 2009); 49 sessions used (from 53 total), recorded from prelimbic and infralimbic mPfC.
- **Task**: Y-maze rule-learning task. Rats self-initiated trials (run to arm end; ~6.5 s), followed by a self-paced intertrial interval (return to start; ~55.6 s). Four sequential rules tested (go right, go to lit arm, go left, go to dark arm); rule switch after 10 correct (or 11/12).
- **Population vectors**: Firing rate vectors (N active neurons per session; 4–22 neurons) constructed for each trial and each intertrial interval.
- **Subspace separability**: PCA applied to concatenated trial and ITI vectors; linear SVM used to classify trial vs. ITI activity in 1–4 principal dimensions.
- **Decoding**: Logistic regression (leave-one-out cross-validation) to decode direction choice, light position, and outcome from trial and ITI activity; also tested linear discriminant analysis, linear SVM, and nearest-neighbour classifiers for robustness.
- **Position-dependent decoding**: Maze divided into 5 sections; population vectors computed per position.
- **Decoding axis angles**: Cosine angle between logistic regression weight vectors for the same feature decoded from trials vs. ITI; also within-phase angles between features.
- **Cross-decoding**: Classifier trained on trial activity tested on ITI activity (and vice versa) to quantify independence of representations.
- **Sleep reactivation**: Spearman's rank correlation between feature-specific mean population vectors (from waking) and 1-s binned population activity during pre- and post-training slow-wave sleep; bin sizes varied from 100 ms to 10 s.
- **Session grouping**: Split by rule type (direction vs. cue) and learning type (putative learning session vs. Other, based on step-change in performance).

---

### Key findings

- Population activity in mPfC is linearly separable between trials and ITIs in as few as 1 principal dimension; using 2 dimensions achieves above-chance separation in all 49 sessions (median classification error near 0).
- Separation between phases (trial vs. ITI) was substantially larger and more discontinuous than separation within phases (between adjacent maze sections), indicating a true subspace shift rather than a gradual drift.
- From trial activity: direction choice, light position, and outcome of the current trial could be decoded significantly above chance; features of the preceding trial could not (at or near chance).
- From ITI activity: direction choice, light position, and outcome of the immediately preceding trial could be decoded significantly above chance; features of the upcoming trial were at chance.
- Decoding axes for the same feature between trial and ITI were near-orthogonal (median angles clustered at or close to π/2 for all three features; median departure from π/2 was 0.067π for direction and 0.045π for light position).
- Cross-decoding (training on trial activity, testing on ITI) was at chance for outcome and light position; significant but weak for direction — consistent with the near-orthogonal decoding axes.
- Within each phase, decoding axes for different features were not near-orthogonal, ruling out that the inter-phase orthogonality is a trivial consequence of random high-dimensional vectors.
- Mean activity vectors representing each feature were more closely aligned across phases than were the corresponding decoding axes, showing that the orthogonality is a property of the coding geometry, not of the population activity per se.
- Decoding results were robust across rule types (direction-based vs. cue-based) and session types (learning vs. Other).
- Post-training slow-wave sleep: trial activity was preferentially reactivated in post-training vs. pre-training sleep, and this was consistent specifically in putative learning sessions; correlation with post-training sleep correlated with the change in reward rate (Spearman ρ ≈ 0.35, p = 0.01 for direction; ρ ≈ 0.34, p = 0.01 for outcome).
- ITI activity also showed some preferential post-training reactivation, but this was not consistently above pre-training sleep after learning sessions and did not correlate with performance improvement.
- Trial activity reactivation was more correlated between pre- and post-training sleep (CC ≈ 0.82–0.84 across features) than ITI reactivation (CC ≈ 0.60–0.67), and this difference was consistent across time scales (100 ms–10 s bins).
- These reactivation differences were consistent across all tested bin sizes, and preferential reactivation of trial activity was stronger at shorter bin sizes.

---

### Computational framework

The paper is framed within the **dynamical systems / population geometry** view of neural coding, specifically the concept of **activity subspaces** (low-dimensional manifolds occupied by population activity in different conditions). The core formalism is as follows:

- Population activity is represented as a vector in N-dimensional firing-rate space (N = number of neurons).
- PCA is used to identify a low-dimensional projection in which activity from different task phases (trial vs. ITI) is linearly separable.
- Decoding axes — the weight vectors of linear classifiers — are used to characterise how task features are encoded. Near-orthogonality of these axes between phases is the key geometric property asserted.
- The framework assumes that downstream populations reading out mPfC activity use linear input weights (a standard assumption in population coding theory), so orthogonal decoding axes imply independent readout.

The paper also invokes the concept of the **interference problem**: in a population jointly encoding multiple world states, how can downstream populations disambiguate them? The subspace/orthogonality solution is proposed as a mechanism, referencing related work on rotational dynamics (Libby and Buschman, 2021) and communication subspaces (Semedo et al., 2019).

No formal mathematical model is derived; the framework is primarily analytical (PCA + linear decoding applied to neural data).

---

### Prevailing model of the system under study

The introduction frames mPfC as a region with established, parallel roles in (1) working memory — maintaining representations of the immediate past during delay periods — and (2) representing the current state of the world to guide ongoing decisions. Multiple prior single-unit studies had documented both past- and present-dependent activity in the same mPfC neurons (e.g., Baeg et al., 2003; Ito et al., 2015), and global shifts in mPfC population activity had been linked to strategy switching (Durstewitz et al., 2010; Karlsson et al., 2012). However, the prevailing model left open how these two types of representation coexist in the same population without interfering with each other, and no prior study had explicitly compared the geometric relationship between past- and present-encoding representations at the population level. The implicit prior assumption was that mixed selectivity (single neurons responding to multiple task variables) provided flexibility, but the problem of downstream disambiguation had not been mechanistically addressed.

---

### What this paper contributes

The paper provides direct empirical evidence that the same mPfC population resolves the interference problem via a population-geometric mechanism: trial (present state) and ITI (past state) activity occupy distinct, linearly separable low-dimensional subspaces, and the decoding axes for the same task feature are near-orthogonal between phases. This means:

1. A downstream population with linear input weights tuned to the trial subspace can read out present-state information without contamination from past-state signals, and vice versa.
2. Upstream inputs can selectively drive the population into either subspace (the sequential decoding, inbound-outbound analysis, and differential sleep reactivation all suggest independent addressability of the two subspaces).
3. Preferential reactivation of trial-phase activity in post-training sleep — but not ITI activity — correlates with learning, suggesting that the trial subspace is selectively targeted for memory consolidation.

These findings move beyond prior demonstrations of mixed selectivity in single PfC neurons to provide a population-level geometric account of how multiple world states can be independently represented and read out.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPfC) — prelimbic and infralimbic cortex**: Primary region of interest. Proposed locus of orthogonal activity subspaces for present and past world states; site of the selective post-learning sleep reactivation.
- **Hippocampus (region CA1)**: Discussed in the context of providing potential upstream input to mPfC that could drive the transition between subspaces (theta-coherent hippocampal-prefrontal interactions at the time of the arm-end / heading-direction change); invoked as a likely driver of the subspace shift but not directly recorded in this study.

---

### Mechanistic insight

This paper partially meets the bar. It presents a clear **algorithm** (near-orthogonal activity subspaces enabling independent linear readout of distinct world states by downstream populations) and provides **neural data** (tetrode recordings from mPfC) that specifically support this mechanism — including decoding accuracy, decoding axis angles, cross-decoding failure, and differential sleep reactivation. The evidence that cross-decoding is at or near chance despite robust within-phase decoding directly supports the orthogonality claim over a simpler alternative (e.g., a single shared representation with amplitude modulation).

However, the paper does not reach the **implementational level**. The mechanism by which the subspace shift is initiated is unknown — candidates discussed include reaching the arm end, changing heading direction, or hippocampal input, but these are not experimentally dissociated. No specific cell types, connectivity patterns, or neuromodulatory mechanisms are identified.

Mapping onto Marr's three levels:

- **Computational**: The brain must represent multiple distinct states of the world in the same population without downstream confusion — i.e., the interference problem must be solved.
- **Algorithmic**: Population activity occupies distinct low-dimensional subspaces for each world state; decoding axes for the same feature are near-orthogonal across subspaces; linear downstream readout with subspace-matched weights can independently access each state's representation.
- **Implementational**: Unresolved. The transition mechanism (what drives the shift from trial to ITI subspace) is unknown; specific cell types and connectivity are not examined. Hippocampal input is a suggested but untested candidate.

---

### Limitations & open questions

- The dataset is small (4 rats, 49 sessions, 4–22 neurons per session) and reanalysed from a single prior study (Peyrache et al., 2009), limiting generalisation.
- The precise timing and cause of the subspace shift (arm-end arrival vs. heading-direction change) cannot be resolved with existing data; further experiments are needed.
- The light cue was extinguished during the ITI, but the exact timing is unknown, leaving some ambiguity in interpreting light-position decoding during that phase.
- The study cannot rule out that ITI activity also encodes some present-state features during that interval, since the task structure does not provide a strong dissociation between past and present during the return trip.
- The paper does not identify which upstream inputs drive the mPfC population into each subspace; hippocampal CA1 input is hypothesised but not tested.
- The functional significance of the different reactivation dynamics of trial vs. ITI activity in sleep remains to be established causally.
- The findings are specific to the Y-maze sequential-rule-learning paradigm; tasks where past and future choices are more entangled (e.g., delayed non-match to place, multi-arm sequence mazes) may disrupt the clean subspace separation observed here.

---

### Connections & keywords

**Key citations**:
- Peyrache et al. (2009) — original dataset; mPfC replay of rule-learning patterns in sleep
- Maggi et al. (2018) — prior work by same group showing ITI decoding of preceding trial in the same dataset
- Libby and Buschman (2021) — rotational dynamics as a mechanism to reduce interference between sensory and memory representations
- Semedo et al. (2019) — communication subspaces between cortical areas
- Rigotti et al. (2013) — mixed selectivity in prefrontal cortex
- Fusi et al. (2016) — high-dimensional mixed selectivity for cognition
- Singh et al. (2019) — mPfC population activity plasticity and sleep reactivation
- Durstewitz et al. (2010) — abrupt transitions in mPfC ensemble states during rule learning
- Benchenane et al. (2010) — hippocampal-prefrontal theta coherence at learning
- Wang et al. (2018) — prefrontal cortex as a meta-reinforcement learning system

**Named models or frameworks**:
- Activity subspaces (population geometry framework)
- Linear decoding / logistic regression decoder
- Interference problem (in neural population coding)
- Communication subspaces (Semedo et al., 2019)

**Brain regions**:
- Medial prefrontal cortex (mPfC) — prelimbic and infralimbic cortex
- Hippocampus (CA1) — hypothesised upstream input

**Keywords**:
- activity subspaces
- population geometry
- linear decoding
- orthogonal coding axes
- medial prefrontal cortex
- world state representation
- interference problem
- intertrial interval
- sleep reactivation
- rule learning
- mixed selectivity
- working memory
