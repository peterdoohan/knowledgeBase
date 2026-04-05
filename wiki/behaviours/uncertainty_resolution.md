# Uncertainty Resolution in Prefrontal Cortex

## Current understanding

Distinct regions of prefrontal cortex implement specific computational functions for Bayesian decision-making under uncertainty. The anterior prefrontal cortex (APF, BA10) encodes uncertainty about hidden states, as measured by the entropy of the belief distribution over possible position states. The medial prefrontal cortex (mPFC, BA9/6) implements belief revision and error detection, with activity correlating with the likelihood of re-estimating position when predictions fail. This functional segregation provides a computational architecture where APF maintains uncertainty representations, mPFC handles belief revision, and lateral PFC/DLPF performs action selection. The framework formalizes decision-making under partial observability as a Partially Observable Markov Decision Process (POMDP) solved via Bayesian belief updating, with distinct PFC regions implementing specific algorithmic components.

## Key evidence

- Distinct regions of prefrontal cortex implement specific computational functions for Bayesian decision-making under uncertainty, with anterior prefrontal cortex (APF) encoding uncertainty about hidden states and medial prefrontal cortex (mPFC) mediating belief revision ([Yoshida 2006](../../raw/summaries/yoshida2006_resolution_uncertainty.md))

- Goal-search vs. visuomotor subtraction revealed activation in dorsolateral prefrontal cortex (DLPF; BA46), anterior cingulate cortex (ACC; BA32/8), bilateral posterior parietal cortex (PPC; BA40/7), thalamus, and basal ganglia (putamen, caudate, globus pallidus, substantia nigra) ([Yoshida 2006](../../raw/summaries/yoshida2006_resolution_uncertainty.md))

- mPFC (BA9/6) and bilateral PPC activity correlated with back-track probability; mPFC showed significantly higher activity during back-track mode vs. update mode (t = 4.20, p < 0.0001) ([Yoshida 2006](../../raw/summaries/yoshida2006_resolution_uncertainty.md))

- Bilateral anterior prefrontal cortex (APF; BA10 medial frontal gyrus and BA9 superior frontal gyrus) activity correlated with HCP entropy (positional uncertainty); mean correlation with HCP entropy: left r = 0.29 ± 0.22, right r = 0.27 ± 0.19; significantly positive for 10/13 subjects ([Yoshida 2006](../../raw/summaries/yoshida2006_resolution_uncertainty.md))

- HMM action prediction accuracy was 88.7% ± 2.9%, correlating significantly with task performance (r = 0.49, p < 0.00001); RT peaks coincided with BT peaks in 86.1% of trials, validating the model's cognitive state inference ([Yoshida 2006](../../raw/summaries/yoshida2006_resolution_uncertainty.md))

## History of ideas

Before this study, the field understood that prefrontal cortex broadly supports decision-making and executive function, but the specific computational roles of distinct PFC subregions in uncertain environments were not well delineated. The anterior prefrontal cortex (APF, particularly frontopolar BA10) had been implicated in complex cognitive tasks involving multiple competing rules, suggesting a role in handling internally-generated information and integrating lateral PFC representations. Medial PFC was associated with self-referential processing and performance monitoring based on reward prediction. The anterior cingulate was linked to error detection and conflict monitoring. However, how these regions specifically implement the computational demands of belief maintenance and updating under partial observability remained unclear. This paper demonstrated that distinct prefrontal subregions implement specific computational components of Bayesian decision-making under uncertainty: APF encodes uncertainty about hidden states, mPFC implements belief revision, and lateral PFC/DLPF performs action selection.

## Open questions

- The HMM parameters (action selection optimality α = 0.8, back-track depth n = 1) were fit to behavior rather than derived from first principles; individual variation was limited but not fully explored
- The fMRI analysis relies on correlational methods; the observed correlations between BOLD and model variables (entropy, back-track probability) do not establish causal necessity or sufficiency of these regions for the computational functions
- No direct neural evidence (e.g., single-unit recordings, lesions, stimulation) links the algorithmic variables to specific neural implementations; the localization remains at the level of macroscopic regions
- The maze task was highly structured (no dead-ends, symmetric topology); generalization to more complex, naturalistic environments with different uncertainty structures is not established
- The binary operant state model (proceed/update vs. re-evaluate/back-track) may oversimplify the continuous nature of belief revision processes
- The relationship between HCP entropy and the neural code for uncertainty remains unspecified—whether entropy is explicitly represented or emergent from population activity is not addressed

## Related pages

- [Prefrontal cortex](../brain_regions/prefrontal_cortex.md)
- [Anterior prefrontal cortex](../brain_regions/anterior_prefrontal_cortex.md)
- [Medial prefrontal cortex](../brain_regions/medial_prefrontal_cortex.md)
- [Dorsolateral prefrontal cortex](../brain_regions/dorsolateral_prefrontal_cortex.md)
- [Anterior cingulate cortex](../brain_regions/anterior_cingulate_cortex.md)
- [Posterior parietal cortex](../brain_regions/posterior_parietal_cortex.md)
- [Bayesian inference](../computational_frameworks/bayesian_inference.md)
- [Belief updating](belief_updating.md)
- [Decision making](decision_making.md)
- [Navigation](spatial_navigation.md)
