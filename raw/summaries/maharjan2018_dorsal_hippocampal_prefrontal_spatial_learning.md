---
source_file: "maharjan2018_dorsal_hippocampal_prefrontal_spatial_learning.md"
paper_id: "maharjan2018_dorsal_hippocampal_prefrontal_spatial_learning"
title: "Disruption of dorsal hippocampal \u2013 prefrontal interactions using chemogenetic inactivation impairs spatial learning"
authors: "Dennis M. Maharjan, Yu Y. Dai, Ethan H. Glantz, Shantanu P. Jadhav"
year: 2018
journal: "Neurobiology of Learning and Memory"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["optogenetics", "lesion"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex", "infralimbic_cortex", "ventral_hippocampus"]
frameworks: ["reinforcement_learning"]
keywords: ["disruption", "dorsal", "hippocampal", "prefrontal", "interactions", "chemogenetic", "inactivation", "impairs", "spatial", "learning"]
key_citations: ["jadhav2016_hippocampal_prefrontal_swr"]
---

### One-line summary

Chemogenetic contralateral inactivation of dorsal hippocampus (dHPC) and prefrontal cortex (PFC) in rats selectively impairs learning of a spatial working memory task but not a spatial reference memory task, establishing that dHPC–PFC interactions are necessary for rapid spatial alternation learning.

---

### Background & motivation

The hippocampus and prefrontal cortex are both necessary for spatial learning and memory-guided behavior, and physiological evidence — including theta oscillation coherence and sharp-wave ripple (SWR)-mediated reactivation — strongly implicates coordinated activity between dorsal HPC (dHPC) and PFC during spatial memory tasks. However, prior functional disconnection studies using contralateral inactivation focused exclusively on ventral and intermediate hippocampus (vHPC, iHPC) to PFC projections, leaving open whether dHPC–PFC interactions are causally required for spatial learning. This paper tests that causal requirement directly, motivated by evidence that direct dHPC–PFC projections exist and that dHPC SWR-mediated reactivation in PFC is especially prominent during initial novel task acquisition.

---

### Methods

- **Subjects**: Adult Long Evans rats (n = 46, 6–8 months old).
- **Task**: W-track continuous spatial alternation task with two components: (1) outbound — spatial working memory, requiring animals to alternate between outer arms (must remember previous arm visited); (2) inbound — spatial reference memory, requiring animals to return to the center arm from any outer arm.
- **Learning paradigm**: Single-day rapid learning protocol comprising eight 15-min run sessions interleaved with 15–20 min rest sessions in a sleep box.
- **Chemogenetic inactivation**: Inhibitory DREADDs (hM4Di) expressed via AAV8 under CaMKIIα promoter injected into target regions 21–24 days before testing; systemic CNO injections (3–5 mg/kg i.p.) 30 min before sessions 1 and 5 to activate DREADDs.
- **Experiment 1 groups** (n=34): Contralateral+CNO (experimental, n=9), Contralateral+Vehicle (n=8), Ipsilateral+CNO (n=7), Naïve controls (n=10). Contralateral inactivation targeted dHPC (left hemisphere CA1) and PFC (right hemisphere prelimbic/infralimbic cortex).
- **Experiment 2 groups** (n=12): Bilateral PFC+CNO (n=7), Bilateral PFC+Vehicle (n=5); naïve controls from Experiment 1 used as reference.
- **Analysis**: State-space model of learning to estimate per-trial probability of correct choice; mixed two-factor ANOVA with repeated measures; post-hoc Bonferroni correction. Histological verification of DREADD expression by fluorescence quantification.

---

### Key findings

- Contralateral dHPC–PFC inactivation (Experiment 1) produced a significant impairment in learning the **outbound (spatial working memory)** component of the W-track task compared to all control groups (main effect of group: F(3,30)=7.33, p=0.001; post-hoc p=0.012 vs. vehicle, p=0.024 vs. ipsilateral, p=0.001 vs. naïve).
- Significant differences between the experimental group and controls emerged by **Session 3** (p<0.05 vs. all controls).
- The experimental group had significantly higher fraction of outbound error trials over the full 8-session learning period and during the first 100 trials (p<0.01 vs. all controls for the first 100 trials).
- **Inbound (spatial reference memory)** learning was **not significantly impaired** by contralateral inactivation (F(3,30)=1.77, p=0.174); all groups showed similar inbound error rates.
- **Ipsilateral inactivation** showed no deficit in either task component, ruling out non-specific effects of unilateral inactivation or systemic CNO.
- Experiment 2: **Bilateral PFC inactivation** also selectively impaired outbound but not inbound learning (F(2,19)=7.80, p=0.003 for outbound across sessions; inbound not significant).
- Viral expression levels (fluorescence intensity) did not differ across groups, ruling out expression differences as a confound.
- Total trial numbers were similar across groups, ruling out differences in behavioral engagement.

---

### Computational framework

Not applicable. The paper is purely empirical with no explicit computational framework. The results constrain models of hippocampal–prefrontal interaction, particularly those positing that SWR-mediated replay transmitted from dHPC to PFC supports working memory updating and rapid novel-task learning. The selective working-memory deficit is consistent with models in which the hippocampus maintains trial-unique spatial context that must be communicated to PFC for integration across trials — a process that could be formalised within reinforcement learning or Bayesian memory consolidation frameworks.

---

### Prevailing model of the system under study

The field's baseline understanding, as framed by the paper's introduction, holds that HPC and PFC have complementary and overlapping roles in memory: the hippocampus is critical for encoding and retrieval of new spatial memories, while PFC supports working memory, executive function, and long-term storage. Direct anatomical projections from **ventral and intermediate CA1/subiculum (vHPC, iHPC) to PFC** were considered the primary route through which hippocampal memory signals reach prefrontal circuits, and prior functional disconnection studies using contralateral inactivation confirmed the causal necessity of vHPC–PFC and iHPC–PFC interactions for spatial working memory and navigation learning. Multiple physiological mechanisms — theta coherence, theta-gamma coupling, and SWR-mediated coordinated reactivation — had been observed between **dorsal** HPC and PFC, implicating dHPC–PFC interactions in memory. However, the causal necessity of dHPC–PFC interactions specifically had not been tested with inactivation; the field could not determine whether these physiological signatures reflected functionally necessary communication or merely epiphenomenal coactivation. Newly reported direct anatomical dHPC→PFC projections had been described but their behavioral relevance to spatial learning was not established.

---

### What this paper contributes

This paper provides the first direct causal evidence that **dorsal hippocampal–prefrontal interactions are necessary for rapid spatial alternation learning**, specifically for the working memory component. Before this study, functional disconnection evidence implicated only vHPC and iHPC in spatial memory, leaving the relevance of dHPC–PFC interactions — despite extensive physiological evidence — unresolved. The results now establish that: (1) dHPC–PFC ipsilateral projections are a functionally required pathway for novel spatial working memory acquisition; (2) this requirement is selective — spatial reference memory (inbound) is spared, mirroring the pattern seen after disruption of awake hippocampal SWRs (Jadhav et al., 2012); (3) this deficit cannot be attributed to non-specific effects of surgery, viral expression, or CNO. The findings strongly support the hypothesis that SWR-mediated dHPC–PFC reactivation during novel task learning is the physiological substrate through which hippocampal spatial information is communicated to prefrontal circuits for working memory updating.

---

### Brain regions & systems

- **Dorsal hippocampus (dHPC), CA1 region** — primary site of DREADD inactivation; provides high-precision spatial maps and SWR-mediated reactivation signals hypothesized to communicate spatial context to PFC.
- **Medial prefrontal cortex (PFC), prelimbic (PrL) and infralimbic (IL) cortex** — second inactivation target; proposed locus of working memory integration and executive function receiving hippocampal input.
- **Ventral/intermediate hippocampus (vHPC, iHPC)** — not directly manipulated; discussed as the previously established source of direct hippocampal projections to PFC; distinguished from dHPC as the focus of prior functional disconnection studies.
- **Nucleus reuniens (NR)** — mentioned as an indirect PFC-to-HPC pathway; not manipulated but discussed as a route supporting memory flexibility.

---

### Mechanistic insight

The paper partially meets the bar. It proposes an algorithm (dHPC communicates trial-unique spatial context to PFC via ipsilateral projections, with SWR-mediated replay as the likely substrate) and provides neural data (chemogenetic inactivation) that causally implicates the dHPC–PFC circuit. However, it does not directly record neural activity (place cells, SWRs, PFC ensembles) during the inactivation, so it cannot map the specific mechanistic variables (e.g., whether SWR rate, content, or PFC coupling is disrupted) onto the behavioral deficit.

- **Computational**: The brain must maintain a representation of the previously visited spatial location across multiple trials to guide correct alternation choices (spatial working memory); this requires communication between the hippocampal cognitive map and prefrontal executive systems.
- **Algorithmic**: The dHPC encodes high-precision spatial context; this information is transmitted to PFC via ipsilateral direct projections (and possibly indirectly); coordinated SWR reactivation events during rest periods are proposed as the mechanism transferring trial-specific hippocampal representations to PFC for consolidation into working memory. The ipsilateral specificity (contralateral inactivation disrupts; ipsilateral inactivation does not) identifies the relevant anatomical substrate.
- **Implementational**: The paper does not characterise specific cell types, synaptic mechanisms, or biophysical properties. DREADDs suppress excitatory neurons (CaMKIIα-expressing) in CA1 and PFC, but the downstream circuit effects on SWRs, theta coupling, or PFC ensemble dynamics are not measured.

---

### Limitations & open questions

- The chemogenetic inactivation suppresses excitatory cells broadly within the targeted regions; it cannot distinguish contributions of different projection pathways (e.g., direct dHPC→PFC vs. dHPC→vHPC→PFC indirect routes).
- No simultaneous electrophysiology was performed, so whether the inactivation disrupts SWR generation, SWR-mediated PFC reactivation, theta coherence, or other physiological interactions is unknown.
- The partial (not complete) inactivation afforded by DREADDs may explain why inbound (simpler) learning is spared — residual circuitry may be sufficient for reference memory but not working memory. This interpretation is plausible but unverified.
- The early transient increase in inbound perseverative errors in the experimental group (significant vs. naïve only, not vs. vehicle or ipsilateral controls) is ambiguous — could reflect partial hippocampal disruption or surgical/injection effects.
- Whether dHPC–PFC interactions are necessary for performance (retrieval) of a fully learned task, or only for acquisition, remains untested.
- The relative contributions of the direct dHPC→PFC projection versus indirect routes (dHPC→vHPC→PFC; PFC→NR→HPC) are not dissociable in this design.
- Generalisability is limited to male Long Evans rats in a specific W-track paradigm; open questions remain about whether findings extend to other spatial tasks, sex differences, or other species.

---

### Connections & keywords

**Key citations**:
- Jadhav et al. (2012) — awake hippocampal SWRs support spatial memory; SWR disruption selectively impairs outbound learning on W-track.
- Jadhav et al. (2016) — coordinated dHPC–PFC excitation/inhibition during SWRs.
- Tang et al. (2017) — dHPC–PFC reactivation during learning stronger in awake vs. sleep states.
- Tang & Jadhav (2018) — SWRs as signature of hippocampal–prefrontal reactivation.
- Kim & Frank (2009) — hippocampal lesions impair W-track alternation learning.
- Wang & Cai (2006, 2008) — vHPC–PFC disconnection impairs spatial working memory.
- Churchwell et al. (2010) — iHPC–PFC interactions in spatial encoding/retrieval.
- Floresco et al. (1997) — vHPC–PFC disconnection in radial-arm maze.
- DeNardo et al. (2015); Hoover & Vertes (2007); Ye et al. (2017) — direct dHPC→PFC anatomical projections.
- Roth (2016) — DREADDs methodology.

**Named models or frameworks**:
- DREADDs (Designer Receptors Exclusively Activated by Designer Drugs) — chemogenetic inactivation tool.
- W-track continuous spatial alternation task.
- Contralateral inactivation / functional disconnection approach.
- State-space model of learning (Smith et al., 2004).

**Brain regions**:
- Dorsal hippocampus (dHPC), CA1
- Medial prefrontal cortex (PFC), prelimbic (PrL), infralimbic (IL)
- Ventral hippocampus (vHPC), intermediate hippocampus (iHPC)
- Nucleus reuniens (NR)

**Keywords**:
- dorsal hippocampus–prefrontal cortex interactions
- chemogenetic inactivation, DREADDs
- spatial working memory
- spatial reference memory
- W-track alternation task
- contralateral disconnection
- sharp-wave ripples (SWRs)
- hippocampal–prefrontal reactivation
- novel task learning
- spatial cognitive map
- theta oscillations and memory
- hippocampal place cells
