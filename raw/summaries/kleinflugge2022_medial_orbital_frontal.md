---
source_file: kleinflugge2022_medial_orbital_frontal.md
paper_id: kleinflugge2022_medial_orbital_frontal
title: "Medial and orbital frontal cortex in decision-making and flexible behavior"
authors:
  - "Miriam C. Klein-Flügge"
  - "Alessandro Bongioanni"
  - "Matthew F.S. Rushworth"
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
species:
  - rat
  - macaque
tasks:
  - foraging_task
methods:
  - optogenetics
  - electrophysiology
  - fmri
  - lesion
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - ventral_tegmental_area
  - substantia_nigra
frameworks:
  - attractor_networks
keywords:
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - anterior_cingulate_cortex
  - value_based_decision_making
  - explore_exploit
  - foraging
  - cognitive_map
  - grid_like_coding
  - attractor_network
  - multi_timescale_value
  - cost_benefit_integration
  - social_cognition
  - medial
  - orbital
  - frontal
  - cortex
  - decision
  - making
  - flexible
  - behavior
key_citations:
  - bongioanni2021_novel_choice_neural
  - behrens2018_cognitive_map_organizing_knowledge
  - whittington2020_tolman_eichenbaum_machine
---

### One-line summary

This review argues that the medial and orbital frontal cortex comprises at least five functionally distinct subregions — dACC, amFC, vmPFC/mOFC, pgACC, and dmPFC — each contributing a different computational role to flexible, value-guided decision-making, with a unifying theme that primate prefrontal cortex goes beyond reward distribution coding to represent the structure and causal relationships of the environment.

---

### Background & motivation

The orbitofrontal cortex (OFC) and medial frontal cortex (ACC, vmPFC) have long been implicated in decision-making and behavioral flexibility, with a dominant view that their core function is encoding the value of choices and environments. However, recent evidence challenges this picture: OFC lesions that spare adjacent white matter do not impair behavioral reversal in primates, and some researchers have argued that frontal areas may not hold the value representations previously attributed to them. A further problem is that subcortical systems (DA midbrain, DRN) also carry value and uncertainty signals, so the specific additional contribution of the frontal cortex has been unclear. This review synthesises evidence from humans, macaques, and rodents to propose a more differentiated account of frontal cortical function, distinguishing multiple subregions with distinct roles, and clarifying how these differ from subcortical counterparts.

---

### Methods

This is a narrative review covering primary empirical and computational studies in humans, macaques, and rodents.

- Scope: studies of dACC, amFC (medial area 10/14), vmPFC/mOFC (area 14m), pgACC, and dmPFC, plus relevant subcortical comparisons (DA midbrain, DRN, striatum, habenula).
- Methods included in reviewed studies: fMRI (BOLD), single-unit electrophysiology, lesion studies, TMS, transcranial ultrasound stimulation (TUS), optogenetics, intracranial EEG.
- Synthesis method: narrative, organised by subregion and functional theme; cross-species comparisons are explicitly addressed. Cytoarchitectonic maps (Wise, 2008) are used to anchor homology claims across rats, macaques, and humans.

---

### Key findings

- **dACC**: Encodes reward value at multiple simultaneous timescales (short and long), enabling detection of reward trajectories (whether the environment is improving or worsening). Also encodes the value of switching and exploring alternatives rather than persisting, and drives information-seeking behaviour. Neurons have the longest intrinsic autocorrelation timescales in the frontal lobe. Two dissociable microcircuits (dACC-SNpr for exploration initiation; dACC-striatum for post-decision persistence) were identified in rodents.

- **amFC** (primate-specific area 10/14): Represents the abstract structural relationships between environmental features, independently of their reward significance. Contains grid-like (hexagonal) representations of abstract task spaces, reminiscent of entorhinal grid cells. Supports inference about novel choices by simulating combinations of previously experienced features. Activity in amFC precedes the analogous signal in hippocampus/entorhinal cortex during spatial navigation. Disruption by TUS impairs integration of information across abstract value space.

- **vmPFC/mOFC**: Acts as a choice-option comparator, computing the difference between chosen and unchosen option values. Activity is consistent with a biophysical attractor network in which competing neural populations represent each option. Lesions or disruption increase choice stochasticity. Signals flip sign depending on behavioural policy (positive uncertainty coding during exploration, negative during exploitation). Opposite BOLD modulation directions in humans vs. macaques are reconciled by variation in time spent in the high-firing attractor state.

- **pgACC**: Integrates costs (effort, delay, aversive stimuli) with benefits to evaluate whether initiating an action is worthwhile. Microstimulation in macaques biases cost-benefit decisions toward avoidance. Projects to striosomes of the striatum; optogenetic manipulation of this pathway alters high-cost/high-benefit choices in rodents. Tracks one's own performance over multiple timescales and predicts whether actions will be initiated.

- **dmPFC**: Represents social structure and the positions of self and others within it. Tracks other individuals' actions and rewards; activity reflects "self-other mergence" — the inappropriate influence of others' performance on self-assessment and vice versa. TMS disruption augments self-other mergence, suggesting dmPFC normally disentangles individual agents. Also encodes others' beliefs in humans (intracranial recordings).

- **Rodent OFC vs. primate amFC/vmPFC**: Rodent OFC supports inference and structural-knowledge-based choice like primate amFC, but also resembles primate vmPFC and lateral OFC in some respects. The rodent OFC does not map cleanly onto any single primate area; primates appear to have differentiated a single ancestral region into multiple specialised circuits.

- **Subcortical comparisons**: DRN encodes mean environmental value; DA midbrain encodes prediction errors and, to a limited degree, distributional value. Frontal cortex is distinguished by representing distributions of opportunity over time, abstract environmental structure, and causal inference — capacities not yet demonstrated in subcortical regions.

---

### Computational framework

The review draws on several complementary frameworks:

1. **Foraging / optimal foraging theory** (marginal value theorem, Charnov 1976): dACC is framed as computing the opportunity cost of the current environment relative to available alternatives, driving explore-exploit switching.

2. **Multi-timescale value representation**: dACC neurons hold value estimates with different temporal integration windows, allowing detection of reward trajectories. Formalised as neurons with different exponential discount factors, analogous to metaplasticity (Farashahi et al., 2017; Schweighofer & Doya, 2003).

3. **Biophysical attractor network** (Wang 2002; Wong & Wang 2006): vmPFC/mOFC choice comparison is modelled as competition between two neural populations with recurrent excitation and mutual inhibition. The bulk signal (BOLD) reflects choice value difference because it captures time spent in the winning attractor state. This framework makes specific predictions about the sign of value modulation across species.

4. **Cognitive map / grid-cell coding** (Behrens et al. 2018; Whittington et al. 2020): amFC represents abstract task spaces with hexagonally-structured (grid-like) population codes, enabling vector-like inference across previously unexplored regions of state space.

Key variables across frameworks: subjective value, option-value difference, reward trajectory (short-term minus long-term average), transition probability, task structure (graph of state relationships), cost-benefit utility.

---

### Prevailing model of the system under study

Before this review's synthesis, the dominant view was that medial and orbital frontal cortex regions collectively encode the value of choices and environments to guide reward-maximising decisions — the "valuation system" account. OFC was primarily associated with representing the value of specific outcomes (including sensory-specific reward value) and enabling behavioral flexibility through reversal learning. ACC was linked to performance monitoring, conflict detection, and effort-reward trade-offs. vmPFC was associated with subjective value computation. This account was bolstered by lesion and neuroimaging studies showing impaired reward-guided decisions and reduced value-correlated neural activity after frontal damage.

The review's introduction signals tension with this view: OFC lesions sparing white matter leave reversal intact in primates; some researchers (Hayden & Niv, 2021) have challenged whether frontal areas hold genuine economic value representations at all. The authors note that subcortical systems provide many of the same signals (prediction error, average environmental value), raising the question of what is specifically frontal.

---

### What this paper contributes

The review establishes a differentiated functional map in which each medial/orbital frontal subregion contributes a distinct computation:

- dACC: not simply conflict or value, but multi-timescale distribution of environmental opportunity and explore-exploit arbitration
- amFC: not valuation but abstract structural knowledge enabling inference to novel situations; grid-like coding in non-spatial task dimensions
- vmPFC/mOFC: the locus of actual value comparison and choice commitment, consistent with an attractor network comparator — but flexible, with sign-flipping depending on current action policy
- pgACC: cost-benefit integration for action initiation, distinct from the comparison process in vmPFC
- dmPFC: social environmental structure, self-other disentanglement

This framework goes beyond the simple "valuation" account by arguing that primate frontal cortex's distinguishing contribution is structural knowledge and inference (not just reward prediction), and that different subregions support different stages from structure learning through to choice execution. It also clarifies the direction of species differences: rodents have a less parcellated frontal cortex that maps imperfectly onto multiple primate areas. The review also establishes the key claim that primate amFC and rodent OFC share some functional properties (structural inference, incidental associative learning) even while not being strict homologues.

---

### Brain regions & systems

- **dACC** (area 24 in primates; Cg1/Cg2 in rodents) — multi-timescale value coding, explore-exploit switching, information seeking
- **amFC** (areas 10v, 10r, 14, possibly anterior p32) — abstract task structure representation, grid-like coding of non-spatial spaces, simulation of novel choices; primate-specific (areas 10/14 absent in rodents)
- **vmPFC/mOFC** (area 14m in humans; medial OFC in macaques) — choice-option comparison and decision commitment; attractor network comparator
- **pgACC** (perigenual ACC, anterior to genu of corpus callosum) — cost-benefit integration, action initiation gating; projects to striosomes
- **dmPFC** (dorsomedial PFC) — social structure encoding, self-other disentanglement, tracking others' actions and beliefs
- **Lateral OFC / area 47/12o** — specific choice-outcome credit assignment; learning correct causal attribution of reward to choices
- **Area 13 (OFC)** — identity-selective offer-value neurons; causally implicated in value-guided decision-making in macaques
- **Posterior lateral OFC** — reward-reinforced sequence representations; more similar to rodent OFC cytoarchitecturally; slow-updating, robust
- **Striatum (striosomes and matrix)** — downstream target of pgACC (striosome) and dACC (matrix/striatum pathway); part of the subcortical reward circuit
- **DA midbrain (VTA/SNc)** — reward prediction errors; some distributional value coding; activity may precede vmPFC during simple choice
- **DRN** — mean environmental value, uncertainty; lacks multi-timescale or structural coding seen in dACC
- **Hippocampus / entorhinal cortex** — grid cells (entorhinal); complementary structural-knowledge representations; interacts with amFC for vector inference
- **Lateral habenula / GPh / RMTg** — ancestral subcortical reward circuit; present in lamprey; provides inhibitory control of DA/5HT

---

### Mechanistic insight

The paper partially meets the bar for mechanistic insight in a subset of its claims.

For **dACC explore-exploit microcircuits**, the review cites Tervo et al. (2021), who provide both an algorithmic account (two distinct pathways for initiation of exploration vs. post-decision persistence) and optogenetic evidence causally linking specific dACC-SNpr and dACC-striatum pathways to each function in rodents. This dissociates the algorithm at circuit level and constitutes a near-complete Marr analysis:
- **Computational**: identify when to switch vs. persist in the current foraging strategy
- **Algorithmic**: dACC computes exploration drive (via SNpr pathway) separately from persistence signals (via striatum pathway), timed differently within decision sequences
- **Implementational**: identified by pathway-specific optogenetic silencing in rats; the two pathways project to different subcortical targets

For **vmPFC attractor dynamics**, the biophysical attractor model (Wang 2002) provides an algorithmic account of choice comparison, and the review cites fMRI, electrophysiology, and lesion/TUS evidence linking vmPFC/mOFC to this computation. However, the reviewers acknowledge that the relationship between macaque and human activity-sign differences and the underlying neural population dynamics is not yet directly confirmed at the single-neuron level.

For **amFC grid-like coding**, the paper cites fMRI (hexagonal modulation) and causal TUS evidence in macaques (Bongioanni et al. 2021), but single-unit or population-level identification of actual grid cells in primate frontal cortex is not yet demonstrated — only aggregate fMRI signatures consistent with grid coding.

Overall, the mechanistic account is strongest for dACC microcircuits and moderate for vmPFC attractor dynamics; the grid-cell account of amFC remains at the algorithmic/computational level pending direct neural recordings.

---

### Limitations & open questions

- **Precise anatomical boundaries** between subregions (especially amFC/vmPFC, pgACC/amFC) remain contested; cytoarchitectonic parcellations are still evolving.
- **Rodent–primate homologies** are explicitly acknowledged as uncertain and likely non-one-to-one; the review cautions against direct mapping of rodent OFC onto any single primate area.
- **Subcortical contributions** to distributional value coding and structural inference are not ruled out; the review calls for direct comparisons of distributional coding between dACC and DA midbrain.
- **Grid-like coding in amFC** is inferred from fMRI BOLD hexagonal modulation; direct single-unit evidence of grid cells in primate frontal cortex is lacking.
- **Whether vmPFC/mOFC value signals cause or merely correlate with choice** — the review cites TUS and lesion evidence for causality but notes that as choices become familiar, vmPFC signals weaken, raising questions about when the region is necessary vs. optional.
- **The dmPFC** is hard to distinguish cleanly from amFC; some non-social structural tasks activate dmPFC, and its exclusive specialisation for social cognition is not established.
- **Interaction mechanisms** between frontal subregions (e.g., how amFC feeds into vmPFC for novel choices) are described conceptually but the temporal dynamics and connectivity are not fully resolved.
- **Curiosity vs. directed information seeking**: how curiosity (intrinsic desire to know) relates to dACC-mediated information seeking remains to be determined.
- **Mood and affect**: pgACC abnormalities are linked to mood and anxiety disorders, and self-other mergence relates to social-affective processing, but the review does not address clinical implications in depth.

---

### Connections & keywords

**Key citations:**
- Fouragnan et al. (2019) — dACC counterfactual value and TUS causal evidence
- Bongioanni et al. (2021) — amFC grid-like coding and TUS in macaques
- Klein-Flügge et al. (2019) — amFC structure encoding, dissociation from posterior OFC
- Tervo et al. (2021) — dACC microcircuit dissociation (exploration vs. persistence)
- Amemori & Graybiel (2012) — pgACC cost-benefit microstimulation
- Friedman et al. (2015) — pgACC-striosome pathway optogenetics
- Rudebeck et al. (2013) — OFC lesions and reversal task performance in primates
- Wang (2002); Wong & Wang (2006) — biophysical attractor network model
- Behrens et al. (2018) — cognitive map framework
- Hayden & Niv (2021) — challenge to economic value representations in OFC
- Kolling et al. (2012, 2018) — dACC foraging and explore-exploit signals
- Padoa-Schioppa & Conen (2017) — area 13 offer-value neurons

**Named models or frameworks:**
- Marginal value theorem (Charnov 1976) — foraging opportunity cost
- Biophysical attractor network / Wang model — vmPFC choice comparison
- Grid cell / cognitive map framework (Behrens et al. 2018; Whittington et al. 2020) — amFC abstract space coding
- Multi-timescale reward integration / metaplasticity (Farashahi et al. 2017)
- Self-other mergence (Wittmann et al. 2016b, 2021) — dmPFC social tracking

**Brain regions:**
dACC, amFC, vmPFC/mOFC, pgACC, dmPFC, lateral OFC (area 47/12o), area 13, posterior lateral OFC, striatum (striosomes), DA midbrain (VTA/SNc), DRN, hippocampus, entorhinal cortex, lateral habenula

**Keywords:**
medial prefrontal cortex, orbitofrontal cortex, anterior cingulate cortex, value-based decision-making, explore-exploit, foraging, cognitive map, grid-like coding, attractor network, multi-timescale value, cost-benefit integration, social cognition
