---
source_file: "coutrot2022_entropy_street_navigation.md"
paper_id: "coutrot2022_entropy_street_navigation"
title: "Entropy of city street networks linked to future spatial navigation ability"
authors: "A. Coutrot, E. Manley, S. Goodroe, C. Gahnstrom, G. Filomena, D. Yesiltepe, R. C. Dalton, J. M. Wiener, C. H\u00f6lscher, M. Hornberger, H. J. Spiers"
year: 2022
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["navigation_task"]
keywords: ["entropy", "city", "street", "networks", "linked", "future", "spatial", "navigation", "ability"]
---

### One-line summary

People who grew up in cities with more complex (higher entropy) street networks develop better spatial navigation skills for complex environments, while those raised in grid-like cities excel at simpler, regular layouts.

### Background & motivation

Environmental factors deeply influence cognition and mental health, but how the environment in which one grew up affects later cognitive abilities remains poorly understood. This study addresses the gap by examining how urban design—specifically street network complexity—shapes spatial navigation ability across diverse global populations.

### Methods

- **Task**: Wayfinding task embedded in the mobile video game "Sea Hero Quest" (SHQ), where participants navigate a boat to find checkpoints in a virtual environment after viewing a map
- **Participants**: 397,162 participants from 38 countries who completed at least 11 game levels and provided full demographics
- **Key metric**: Street Network Entropy (SNE) computed from Shannon entropy of street orientation distributions in the 10 largest cities per country, weighted by population
- **Control variables**: Age, gender, education level, video gaming skill
- **Validation**: Follow-up experiment with 599 USA participants using "City Hero Quest" (city-themed version of SHQ)

### Key findings

- People who grew up outside cities had better navigation skills than city-dwellers (Hedge's g = 0.09, 95% CI = [0.09, 0.10]), with effect size varying dramatically across countries (from near-null in Romania to g = 0.19 in USA)
- Country-level street network entropy (SNE) negatively correlated with the environment effect size (Pearson's r = -0.60, P < 0.001, 95% CI = [-0.78, -0.30]): countries with grid-like cities (low SNE) showed larger city vs. non-city navigation differences
- Participants from low-SNE countries performed better at low-entropy (regular layout) game levels, while participants from high-SNE countries excelled at high-entropy (complex layout) game levels
- Key navigational demands in high-SNE cities: accommodating turns deviating from 90°, navigating more streets, and crossing more neighborhood partitions
- The environment effect remained stable across age groups, suggesting early exposure creates lasting cognitive adaptations
- City Hero Quest replication confirmed results transfer to urban navigation contexts (SHQ: g = 0.27; CHQ: g = 0.34)

### Computational framework

The study uses information theory (Shannon entropy) to quantify environmental complexity. Street Network Entropy (SNE) measures the distribution of street orientations—a grid city has low entropy (streets align to few orientations), while organic cities have high entropy (streets follow many orientations). The framework assumes that navigating high-entropy environments requires enhanced cognitive strategies: maintaining goal direction despite irregular angles, prospective memory for street names and turns, and hierarchical planning across neighborhoods.

### Prevailing model of the system under study

Prior to this study, the field understood that: (1) environmental enrichment enhances hippocampal neurogenesis and cognition in rodents; (2) living near green spaces benefits human mental health; (3) urban residence associates with higher psychiatric disorder risk; (4) spatial navigation activates the hippocampus and complex city navigation increases posterior hippocampal volume. However, whether childhood environment type shapes later spatial cognitive abilities remained unclear, with limited empirical evidence linking specific urban design features to navigation skill development.

### What this paper contributes

This paper establishes that the topology of one's childhood environment—specifically street network entropy—shapes spatial navigation ability in a lasting, environment-specific manner. People develop navigation strategies optimized for their developmental environment: those raised in grid cities excel at regular layouts but struggle with complex ones, while those raised in organic cities or rural areas show the opposite pattern. This demonstrates that human spatial cognition adapts to environmental structure during development, creating specialized rather than generalizable navigation abilities. The findings have implications for urban design, suggesting that city layouts influence cognitive development at population scales.

### Brain regions & systems

Not applicable — this is a behavioral study using a mobile video game. However, the paper discusses hippocampal involvement in spatial navigation based on prior literature (Maguire et al., 2006; Spiers & Maguire, 2006), noting that complex navigation increases posterior hippocampal volume in taxi drivers. The study constrains what types of environmental demands (orientation tracking, prospective memory, hierarchical planning) would engage hippocampal and prefrontal systems, but does not directly measure neural activity.

### Mechanistic insight

The paper does not meet the mechanistic insight bar. While it proposes that specific navigational demands (tracking goal direction with varying angles, prospective memory for streets/turns, hierarchical planning across neighborhoods) enhance navigation skill, it does not formalize these as a computational algorithm or provide neural data supporting one algorithm over alternatives. The framework is descriptive rather than formalized: it identifies correlations between environmental entropy and navigation performance, and correlates SNE with specific route demands (deviation from 90° turns, unique streets, partitions crossed), but does not specify the representations or processes that transform environmental structure into navigation behavior. The study is purely behavioral with no neural recordings.

### Limitations & open questions

- Causality cannot be established from this cross-sectional design; the results show association, not that growing up in specific environments causes navigation differences
- Self-reported home environment (city vs. non-city) may not capture the full complexity of actual developmental environments
- SHQ participants only reported home country, not finer-grained regional information, requiring country-level averaging of SNE
- The game-based measure, while validated, may not fully capture real-world navigation complexity
- The mechanism by which early exposure creates lasting effects (neural plasticity, strategy crystallization) remains unproven
- Whether the effects persist across the entire lifespan or are modifiable by later environment exposure is unknown
- Whether grid city navigation deficits in complex environments represent true impairment or simply lack of practice is unclear

### Connections & keywords

**Key citations**: Kempermann et al. 1997 (environmental enrichment and neurogenesis), Maguire et al. 2006 (London taxi drivers hippocampal volume), Coutrot et al. 2018 (SHQ initial validation), Spiers et al. 2021 (worldwide navigation variation), Boeing 2017 (OSMnx), Lynch 1960 (Image of the City), Tversky 1981 (map memory distortions)

**Named models or frameworks**: Sea Hero Quest (wayfinding task), Shannon entropy (information theory), Street Network Entropy (SNE), agent-based route simulation, linear mixed models (LMM)

**Brain regions**: Hippocampus (posterior, discussed in context of prior literature), prefrontal cortex (discussed for planning), posterior parietal cortex (discussed for angular deviation processing)

**Keywords**: spatial navigation, wayfinding, street network entropy, urban design, environmental enrichment, cognitive development, Sea Hero Quest, Shannon entropy, city topology, hippocampus, cross-cultural, mobile game, citizen science