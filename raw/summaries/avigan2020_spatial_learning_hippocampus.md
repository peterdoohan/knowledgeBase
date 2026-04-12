---
source_file: avigan2020_spatial_learning_hippocampus.md
paper_id: avigan2020_spatial_learning_hippocampus
title: "Flexible spatial learning requires both the dorsal and ventral hippocampus and their functional interactions with the prefrontal cortex"
authors:
  - "Philip D. Avigan"
  - "Katharine Cammack"
  - "Matthew L. Shapiro"
year: 2020
journal: Hippocampus
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - morris_water_maze
methods:
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - striatum
  - dorsolateral_striatum
  - thalamus
  - ventral_hippocampus
keywords:
  - hippocampal_longitudinal_axis
  - dorsal_ventral_hippocampus_dissociation
  - spatial_reversal_learning
  - muscimol_inactivation
  - crossed_disconnection
  - mpfc_hippocampus_interaction
  - cognitive_flexibility
  - perseveration
  - proactive_interference
  - place_cells
  - egocentric_response_strategies
  - nucleus_reuniens
  - flexible
  - spatial
  - learning
  - requires
  - both
  - dorsal
  - ventral
  - hippocampus
key_citations:
  - ito2015_prefrontal_thalamic_hippocampus
  - jadhav2016_hippocampal_prefrontal_swr
  - jones2005_theta_hippocampal_prefrontal
---

### One-line summary

Temporary inactivation of dorsal or ventral hippocampus each profoundly impaired spatial learning in rats, and crossed (contralateral) co-inactivation with medial prefrontal cortex disrupted both discrimination and reversal learning, demonstrating that flexible spatial memory depends on both hippocampal subregions and their functional interactions with mPFC.

---

### Background & motivation

The hippocampus (HPC) is essential for episodic and spatial memory, and the medial prefrontal cortex (mPFC) is essential for behavioral flexibility, but the circuit mechanisms linking these structures remain unclear. A prevailing dorsal/ventral dissociation held that the dorsal HPC (dHPC) supports spatial memory while the ventral HPC (vHPC) supports emotional/anxiety-related processing, with the vHPC providing the primary monosynaptic input to mPFC. The specific contributions of each HPC subregion to flexible spatial memory — and whether mPFC-HPC interactions require both subregions — had not been directly tested using temporary, targeted inactivation in a task dissociating initial learning from reversal. This study fills that gap by systematically inactivating mPFC, dHPC, and vHPC individually and in combination, using unilateral crossed versus ipsilateral designs to probe circuit interactions.

---

### Methods

- **Subjects**: 25 male Long-Evans rats implanted with bilateral cannulae targeting mPFC and either dHPC or vHPC.
- **Task**: Spatial win-stay discrimination and reversal task in a plus maze; rats learned an initial spatial discrimination (ID) then a series of contingency reversals (R1, R2, …), with a 10/12-trial criterion triggering each reversal.
- **Drug**: Muscimol (GABAA agonist; mPFC: 0.1 mg/ml; HPC: 1 mg/ml, 0.5 µl) or saline microinjections 20 min before testing, in an ABBA order across four daily sessions per experiment.
- **Inactivation conditions tested** (7 total): bilateral mPFC (n=19), bilateral dHPC (n=9), bilateral vHPC (n=11), ipsilateral mPFC-dHPC (n=11), crossed mPFC-dHPC (n=11), ipsilateral mPFC-vHPC (n=8), crossed mPFC-vHPC (n=8).
- **Key measures**: Choice accuracy (% correct), trials performed, error counts; goal arm versus start arm error analysis to distinguish recent versus long-term memory impairments; perseveration index; egocentric body-turn strategy analysis using binomial testing and Fisher's method.
- **Analysis**: Repeated-measures ANOVA with drug, learning block, HPC subregion, and hemisphere as factors; histological verification of cannula placements.

---

### Key findings

- **Bilateral dHPC or vHPC inactivation** severely impaired initial discrimination learning: reduced choice accuracy (F(1,18)=41.7, p<.001), increased trials and errors, with no significant difference between subregions. Both subregions also impaired reversal learning in rats that progressed to R1.
- vHPC inactivation produced somewhat stronger early ID impairment than dHPC (drug × subregion interaction over first 10 trials: F(1,18)=6.25, p=.022).
- Both dHPC and vHPC inactivation increased start arm errors (entries to never-rewarded arms; p=.024), indicating impairment of long-term spatial memory, as well as goal arm errors (recent memory).
- **Bilateral mPFC inactivation** preferentially impaired reversal over discrimination learning (block × drug accuracy interaction: F(1,18)=9.54, p=.006) and increased perseverative errors at reversal onset (p=.049); it selectively increased goal arm errors (p<.001) without affecting start arm errors, suggesting mPFC specifically supports flexible use of recent memory.
- **Crossed mPFC-HPC inactivation** (mPFC in one hemisphere + dHPC or vHPC in the opposite hemisphere) impaired both ID and R1 learning: reduced accuracy (F(1,17)=38.2, p<.001), increased trials and errors. **Ipsilateral inactivation did not impair learning** (accuracy: F(1,17)=0.91, p=.35), confirming that impairment requires disabling mPFC-HPC interactions in both hemispheres simultaneously.
- Crossed inactivation increased goal arm but not start arm errors, suggesting mPFC-HPC interactions support recent but not long-term memory.
- Muscimol to bilateral dHPC, vHPC, or crossed mPFC-dHPC induced egocentric body-turn repetition strategies during the task (group p-values: dHPC: 6.98×10⁻⁸; vHPC: 1.05×10⁻⁵; crossed mPFC-dHPC: 1.59×10⁻⁵), suggesting that loss of hippocampal spatial processing allows default striatum-dependent egocentric strategies to emerge.

---

### Computational framework

Not applicable in a formal sense — no explicit computational model is developed or fit to data.

The paper is framed at a systems and circuit level rather than a computational/algorithmic one. Results constrain circuit-level frameworks for hippocampal-prefrontal interaction. Informally, the paper is consistent with models in which the mPFC resolves proactive interference by differentiating or selecting among competing hippocampal spatial codes (prospective coding), and the vHPC relays spatial/contextual signals to mPFC while mPFC feeds back rule information via the nucleus reuniens thalamic relay. This is related to frameworks involving attractor-based spatial representations in hippocampus and top-down prefrontal gating of memory retrieval.

---

### Prevailing model of the system under study

The dominant pre-existing view was a functional dissociation along the hippocampal longitudinal axis: the dHPC supports precise spatial mapping (consistent with small place fields, water maze impairments after dHPC but not vHPC lesions), while the vHPC is more closely tied to emotional processing and anxiety (supported by anxiety effects of vHPC but not dHPC lesions and by vHPC's stronger behavioral anxiety phenotype). Under this view, spatial learning in intact animals would be expected to depend primarily on dHPC circuits. Separately, the mPFC was known to support cognitive flexibility and reversal learning, and to communicate with HPC — particularly via the dense monosynaptic input from vHPC (ventral CA1 / subiculum) to mPFC and via disynaptic mPFC-to-HPC pathways through the nucleus reuniens — but the degree to which flexible spatial memory required bidirectional mPFC interactions with both dHPC and vHPC specifically had not been established. The prevailing assumption was that vHPC-mPFC connectivity made the vHPC the relevant hippocampal node for mPFC-dependent flexible memory.

---

### What this paper contributes

The results challenge the strict dorsal/ventral functional dissociation for spatial memory: extensive prior training appears to distribute spatial memory representations across the entire hippocampal longitudinal axis, such that either subregion is individually necessary. This updates the prevailing model by showing that the vHPC is not simply an "emotional" structure — it is required for spatial learning and memory even in well-trained animals. The crossed inactivation design provides causal evidence that flexible spatial memory depends on functional interactions between mPFC and both HPC subregions (not just the vHPC-mPFC monosynaptic pathway), and that a single hemisphere containing intact mPFC-HPC circuitry is sufficient for normal performance. The pattern of error types (goal arm errors for crossed/mPFC inactivation; both goal and start arm errors for bilateral HPC inactivation) further dissects recent versus long-term memory contributions of these structures and their interactions.

---

### Brain regions & systems

- **Dorsal hippocampus (dHPC, primarily dorsal CA1)** — required for spatial learning and memory including both recent and long-term memory; supports precise spatial representations; interacts with mPFC via disynaptic thalamic (nucleus reuniens) pathways.
- **Ventral hippocampus (vHPC, primarily ventral CA1)** — required for spatial learning and memory (contrary to strict dissociation models); primary source of direct monosynaptic hippocampal input to mPFC; relays spatial/contextual signals to mPFC.
- **Medial prefrontal cortex (mPFC, prelimbic/infralimbic)** — required for cognitive/behavioral flexibility; specifically impairs reversal learning and promotes perseveration when inactivated; supports flexible use of recent memory; proposed to signal current rules to HPC via nucleus reuniens.
- **Nucleus reuniens of the thalamus** — key relay for disynaptic mPFC-to-HPC communication (discussed as mechanistic intermediary, not directly manipulated in this study).
- **Dorsolateral striatum** — mentioned as substrate for egocentric response strategies that emerge when HPC function is disrupted.

---

### Mechanistic insight

The paper does not fully meet the high bar: it provides causal neural data (inactivation manipulations) that establish necessity of specific circuits, but it does not present a formalised algorithm or provide direct neural recordings linking a specific computational process (e.g., prospective coding or rule representation) to measured activity. It infers algorithmic-level mechanisms from behavioral deficits.

Partial mapping onto Marr's levels:
- **Computational**: The brain must flexibly update spatial goals when reward contingencies change while suppressing proactive interference from previously learned associations. This requires both a spatial map (maintained by HPC) and a rule/context signal (maintained by mPFC) that modulates which spatial memory is retrieved or expressed.
- **Algorithmic**: vHPC transmits spatial/contextual signals to mPFC; mPFC encodes the current rule and differentiates competing hippocampal prospective codes; mPFC feeds rule information back to dHPC and vHPC via nucleus reuniens, enabling selection of correct prospective codes. Impairment of this circuit causes perseveration and egocentric fallback strategies.
- **Implementational**: The paper does not provide recordings, pharmacological specificity beyond GABA-A agonism, or cell-type-level data. The proposed implementation (vHPC→mPFC monosynaptic projection; mPFC→reuniens→HPC disynaptic feedback; theta/gamma oscillatory coordination) is cited from other studies rather than demonstrated here.

---

### Limitations & open questions

- Muscimol spreads beyond the targeted area and has unknown off-target effects; it eliminates local spiking but may spare passing fibres or produce rebound excitation.
- The study used only male rats, limiting generalisability.
- The prelimbic and infralimbic subregions of mPFC were not separately targeted; their distinct contributions to discrimination versus reversal remain unresolved.
- Extensive pre-surgical training may have altered the structure of hippocampal memory representations (e.g., establishing vHPC spatial codes that would not be present after minimal training), limiting comparison to lesion studies with limited training.
- The crossed inactivation approach assumes that ipsilateral mPFC-HPC circuits are functionally redundant across hemispheres — this is not directly verified.
- The study does not record neural activity, so proposed mechanisms (prospective coding, rule differentiation) are inferred rather than directly observed.
- The role of the nucleus reuniens and thalamic relays in mediating the mPFC-HPC interactions evidenced here remains to be tested directly in this preparation.
- It is unclear whether the spatial memory gradient along the hippocampal axis is task-specific (plus maze) or generalises to other spatial paradigms.

---

### Connections & keywords

**Key citations**:
- Guise & Shapiro (2017) — prior mPFC inactivation study using the same plus maze task; mPFC modulates HPC encoding to reduce interference
- Ferbinteanu & Shapiro (2003) — prospective/retrospective coding in HPC; plus maze paradigm origin
- Spellman et al. (2015) — vHPC-mPFC input supports spatial working memory; ventral CA1 terminal inactivation in mPFC
- Ito et al. (2015) — prefrontal-thalamo-hippocampal circuit; nucleus reuniens role; mPFC inactivation degrades prospective coding in dCA1
- Bannerman et al. (2004) — dorsal/ventral HPC dissociation review (spatial vs. emotional)
- Fanselow & Dong (2010) — dorsal/ventral hippocampus functional distinction
- Floresco et al. (1997) — crossed disconnection methodology for hippocampal-prefrontal circuits
- Moser et al. (1995); Moser & Moser (1998) — spatial memory gradient along hippocampal axis; water maze dHPC/vHPC lesion studies
- Jones & Wilson (2005) — theta coordination of mPFC-HPC during spatial memory
- Jadhav et al. (2016) — sharp-wave ripples and prefrontal-HPC coordination

**Named models or frameworks**:
- Spatial win-stay discrimination and reversal task (plus maze)
- Crossed disconnection design (Floresco et al., 1997)
- Hippocampus as cognitive map (O'Keefe & Nadel, 1978)
- Prospective/retrospective coding framework

**Brain regions**:
- Dorsal hippocampus (dHPC, dorsal CA1)
- Ventral hippocampus (vHPC, ventral CA1)
- Medial prefrontal cortex (mPFC, prelimbic/infralimbic)
- Nucleus reuniens of the thalamus
- Dorsolateral striatum

**Keywords**:
- hippocampal longitudinal axis
- dorsal-ventral hippocampus dissociation
- spatial reversal learning
- muscimol inactivation
- crossed disconnection
- mPFC-hippocampus interaction
- cognitive flexibility
- perseveration
- proactive interference
- place cells
- egocentric response strategies
- nucleus reuniens
