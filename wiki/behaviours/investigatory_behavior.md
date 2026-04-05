# Investigatory Behavior

Investigatory behavior is a fundamental behavioral mode in which organisms actively explore and gather information about stimuli in their environment. It encompasses a spectrum from brief, superficial inspection to sustained, committed engagement.

## Current understanding

*(Placeholder - to be written by synthesiser when sufficient evidence accumulates)*

## Key evidence

### State decomposition of investigation

- Investigatory behavior can be decomposed into latent states using Hidden Markov Models (HMM). Three states are identified: idle, shallow investigation, and deep investigation. The transition probabilities between these states differ based on stimulus familiarity, with the sniff-to-bite transition being the critical differentiator between familiar and novel objects ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

### Deep vs. shallow investigation

- **Shallow investigation**: Characterized by sniffing without subsequent engagement. In object investigation: sniff-without-bite. In social investigation: approach-investigation-without-grab. This represents superficial information gathering ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

- **Deep investigation**: Characterized by sustained engagement following initial inspection. In object investigation: sniff-followed-by-bite (and grab). In social investigation: approach-with-grab. This represents committed information gathering and is selectively amplified for novel stimuli ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

### Neural control of investigation depth

- A cortico-subcortical circuit specifically gates the transition from shallow to deep investigation: prelimbic cortex (PL) → zona incerta medial (ZIm) → periaqueductal gray (PAG). This circuit modulates investigation depth independently of general locomotion or approach behavior ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

- ZIm^GAD2 neurons show elevated activity specifically during deep investigation (Z-score ~4.1) compared to shallow investigation (Z-score ~0.8). This signal is present during both object and social investigation but absent during food interaction, suggesting selectivity for novelty-driven rather than consumatory investigation ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

- Chemogenetic silencing of PL→ZIm terminals abolishes deep investigation (investigation duration drops from ~73s to ~2s), demonstrating that prefrontal excitatory drive to ZIm is required for committed investigation ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

- Silencing ZIm^GAD2→PAG terminals strongly reduces investigation duration and deep investigation preference, while silencing ZIm→MLR or ZIm→PnO projections has no effect. This demonstrates that the ZIm→PAG projection specifically carries the investigation-gating signal ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

### Behavioral dissociations

- Deep investigation can be dissociated from general locomotion: inhibiting ZIm^GAD2 reduces investigation but does not reduce open-field travel distance ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

- Deep investigation can be dissociated from approach behavior: approach frequency is preserved when ZIm is manipulated; only the depth of engagement following approach is affected ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md)).

## History of ideas

*(To be written by synthesiser)*

## Open questions

- What is the computational role of the HMM-identified states? Are shallow and deep investigation truly discrete states or extremes of a continuous spectrum? ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md))

- How does the circuit integrate information about stimulus identity, value, and context to modulate investigation depth? ([Ahmadlou 2021](../../raw/summaries/ahmadlou2021_novelty_seeking_behavior.md))

## Related pages

- [novelty_seeking](novelty_seeking.md)
- [zona_incerta](../brain_regions/zona_incerta.md)
- [periaqueductal_gray](../brain_regions/periaqueductal_gray.md)
- [prelimbic_cortex](../brain_regions/prelimbic_cortex.md)
