---
source_file: reznikova2017_hunting_behavior_mouse.md
paper_id: reznikova2017_hunting_behavior_mouse
title: "Studying hunting behaviour in the striped field mouse using data compression"
authors:
  - "Zhanna Reznikova"
  - "Jan Levenets"
  - "Sofia Panteleeva"
  - "Boris Ryabko"
year: 2017
journal: "Acta Ethologica"
paper_type: empirical
contribution_type: methodological
species:
  - mouse
  - rat
tasks:
  - foraging_task
keywords:
  - hunting_behavior
  - predatory_behavior
  - striped_field_mouse
  - apodemus_agrarius
  - common_shrew
  - sorex_araneus
  - norway_rat
  - rattus_norvegicus
  - ethogram
  - data_compression
  - kolmogorov_complexity
  - behavioral_complexity
  - behavioral_stereotype
  - foraging_ecology
  - insect_predation
  - muridae
  - soricidae
  - comparative_ethology
  - behavioral_sequence_analysis
  - studying
---

### One-line summary

The striped field mouse (*Apodemus agrarius*) exhibits efficient, stereotyped hunting behavior toward insects that is comparable to specialized insectivores and distinct from generalist predators, as quantified using a novel data compression method applied to behavioral sequences.

---

### Background & motivation

Small rodents play central roles in ecosystems, yet their foraging ecology and behavioral adaptations for diet optimization remain understudied. While many rodents are omnivorous, the degree of carnivory and the nature of hunting adaptations in granivorous species like the striped field mouse are poorly understood. This study addresses the gap by comparing hunting behavior across species with different dietary specializations, using a novel quantitative method to assess behavioral complexity.

---

### Methods

- **Subjects**: 81 Norway rats (41F/40M), 26 striped field mice (13F/13M), 11 common shrews (7F/4M). Animals were housed in species-appropriate cages with controlled light/dark cycles (16:8).
- **Prey**: Lobster cockroach (*Nauphoeta cinerea*, ~28 mm) as live mobile prey.
- **Apparatus**: Noldus arenas (45×45×50 cm for rats; 30×30×35 cm for mice and shrews) with transparent lids.
- **Procedure**: Each animal placed in arena; cockroach introduced 5 min later. Three cockroaches presented sequentially. Video recorded at 25 fps (rats/mice) or 60 fps (shrews). Only complete hunting stereotypes (ending in killing and eating) were analyzed.
- **Behavioral encoding**: 19 behavioral elements coded from video, categorized into:
  - **Key elements**: bite (W), seizing with forepaws (E), pursuing (S/Q)
  - **Auxiliary elements**: handling (R), sniffing (D), carrying (G), nibbling legs (H), pinning (N/M)
  - **Noise elements**: freezing (C), turning (V/B/F), rearing (Y/I), backwards movement (U), grooming (X), jumping (J)
- **Analysis**: Data compression method using 7-zip (Bzip2 algorithm) applied to behavioral sequences. Compression ratios compared using Mann-Whitney U test. Correlation analysis (Pearson) between compression ratios and behavioral characteristics.

---

### Key findings

- **Hunting success rates**: 52% of rats (42/81), 65% of mice (17/26), and 100% of shrews (11/11) displayed complete hunting stereotypes.
- **Stereotype length**: Striped field mice had significantly longer hunting stereotypes (32.95 ± 2.81 elements) than rats (25.39 ± 2.57) and shrews (23.48 ± 3.05); Student's t-test: t = 1.984, P < 0.05 (mice vs rats); t = 2.281, P < 0.05 (mice vs shrews).
- **Species-specific behavioral elements**: 
  - Jumps (J) and free-standing rearing (I) observed only in mice and shrews, not rats.
  - Seizing with forepaws (E) and handling (R) observed only in rodents, not shrews.
  - Pinning prey with paws (N/M) observed only in shrews.
- **Proportion of behavioral elements in rats**: 66.7% key, 24.2% auxiliary, 7.1% noise.
- **Proportion of behavioral elements in mice**: 86% key, 8.3% auxiliary, 5.7% noise.
- **Proportion of behavioral elements in shrews**: 74.8% key, 19.5% auxiliary, 5.7% noise.
- **Statistical comparisons of element proportions**: Shrews had higher proportion of key elements than rats (Fisher's exact test, P < 0.005), but lower than mice. Shrews had lower proportion of auxiliary elements than rats (P < 0.005), but higher than mice. No significant difference in noise elements across species.
- **Hunting rates**: Shrews displayed greater hunting rate (elements per second) than rats (t = 9.075, P < 0.01) and mice (t = 2.197, P < 0.05). Rats had lower hunting rate than mice (t = 7.879, P < 0.01).
- **Compression ratios**: Striped field mice: 0.596; Common shrew: 0.59; Norway rat: 0.631. Mice and shrews did not differ significantly (Uemp. = 12.5, Ucr. = 1, P = 0.774), but both differed significantly from rats (rats vs shrews: Uemp. = 4, Ucr. = 5, P = 0.041; rats vs mice: Uemp. = 7, Ucr. = 8, P = 0.02).
- **Correlations with compression ratio**: Strong negative correlation with proportion of key elements (r = -0.693, P < 0.01) and bite proportion (r = -0.676, P < 0.01). Strong positive correlation with proportion of noise elements (r = 0.780, P < 0.01) and auxiliary elements (r = 0.527, P < 0.05).

---

### Computational framework

The study applies the **data compression method** based on **Kolmogorov complexity** (Ryabko et al. 2013) to analyze behavioral sequences (ethograms). The core formalism treats behavioral sequences as symbolic texts generated by stochastic processes. The complexity of a sequence is estimated by compressing it: the compression ratio (compressed length / original length) serves as a proxy for Kolmogorov complexity per symbol. Lower compression ratios indicate more regular, predictable sequences (lower complexity), while higher ratios indicate more variable, less predictable sequences (higher complexity). The method uses the Bzip2 compression algorithm (via 7-zip) and applies the Mann-Whitney-Wilcoxon test to compare complexity between groups. This approach assumes that behavioral sequences contain statistical regularities that a general-purpose compressor can capture, and that differences in compressibility reflect genuine differences in behavioral complexity rather than mere noise.

---

### Prevailing model of the system under study

Before this study, the striped field mouse (*Apodemus agrarius*) was considered primarily **granivorous** (seed-eating), with insects forming part of a diverse diet but without recognized specialized hunting adaptations. While skilled insect predation had been documented in Cricetidae (e.g., grasshopper mice, deer mice, golden hamsters), it was not known whether Muridae possessed comparable hunting capabilities. The common shrew (*Sorex araneus*) was well-established as a specialized insectivorous predator with efficient hunting behavior. The Norway rat (*Rattus norvegicus*) was characterized as a generalist with highly flexible, opportunistic foraging behavior. The prevailing view held that hunting behavior complexity and efficiency would correlate with dietary specialization: insectivores > generalists > granivores.

---

### What this paper contributes

This paper challenges the assumption that granivorous rodents lack sophisticated hunting capabilities by demonstrating that the striped field mouse exhibits hunting behavior comparable to specialized insectivores (common shrews) and distinct from generalist rats. The key contributions are:

1. **Empirical finding**: Striped field mice displayed efficient pursuit predation with surprisingly stereotyped hunting sequences, despite lacking morphological specializations for predation. Hunting efficiency (0.36 ants/minute in prior work) rivals specialized predators.

2. **Methodological innovation**: Applied the data compression method to ethograms for cross-species comparison, demonstrating that behavioral complexity can be quantified via compression ratios as a proxy for Kolmogorov complexity.

3. **Comparative insight**: The similarity in compression ratios between mice (0.596) and shrews (0.59) versus rats (0.631) suggests that highly stereotyped, low-complexity hunting patterns may reflect shared evolutionary roots in small mammals, with rats' flexible generalist strategy producing higher behavioral complexity.

4. **Theoretical implication**: The predominance of 'key' behavioral elements (86% in mice, 74.8% in shrews vs. 66.7% in rats) drives lower complexity, suggesting that efficient hunting relies on streamlined, predictable action sequences rather than behavioral flexibility.

---

### Brain regions & systems

Not applicable. This study focuses on behavioral analysis at the organismal level without neural recording or anatomical investigation. The findings constrain models of motor pattern generation and behavioral sequencing but do not directly implicate specific brain regions or circuits.

---

### Mechanistic insight

This paper does **not** meet the bar for mechanistic insight. It provides detailed behavioral characterization and applies a computational framework (data compression/Kolmogorov complexity) to quantify behavioral complexity, but it does not present an algorithmic model of how the brain generates hunting behavior, nor does it provide neural data linking specific mechanisms to the observed behaviors. The paper remains at the behavioral description level, though the compression-based approach offers a formal characterization of behavioral complexity that could constrain future algorithmic models.

---

### Limitations & open questions

- **Sample size imbalance**: Different numbers of subjects across species (81 rats, 26 mice, 11 shrews) and only 11 shrews total, which may limit statistical power for shrew comparisons.
- **Laboratory environment**: All experiments conducted in controlled laboratory settings with artificial prey (cockroach), which may not fully capture natural hunting behavior in the wild.
- **Single prey type**: Only one prey species (lobster cockroach) was used; hunting behavior may differ with different prey types.
- **No neural data**: The study provides behavioral characterization without neural mechanisms, leaving open how the brain generates these stereotyped sequences.
- **Evolutionary interpretation**: The similarity between mice and shrews is interpreted as shared evolutionary roots, but phylogenetic analysis was not performed.
- **Methodological constraints**: The compression method relies on a specific compressor (7-zip/Bzip2); different compressors might yield different absolute values, though relative comparisons should hold.

---

### Connections & keywords

**Key citations**:
- Ryabko et al. (2013) — foundational data compression method based on Kolmogorov complexity
- Panteleeva et al. (2013) — prior work demonstrating hunting efficiency in striped field mice
- Reznikova et al. (2012) — prior application of complexity measures to animal behavior
- Churchfield et al. (2012) — characterization of common shrew foraging ecology
- Timberlake & Washburne (1989) — predatory behavior in rodent species comparison

**Named models or frameworks**:
- Data compression method (Kolmogorov complexity-based)
- Ethogram analysis as biological texts
- Bzip2 compression algorithm

**Brain regions**:
- Not applicable

**Keywords**:
hunting behavior, predatory behavior, striped field mouse, Apodemus agrarius, common shrew, Sorex araneus, Norway rat, Rattus norvegicus, ethogram, data compression, Kolmogorov complexity, behavioral complexity, behavioral stereotype, foraging ecology, insect predation, Muridae, Soricidae, comparative ethology, behavioral sequence analysis
