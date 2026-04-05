# Obsessive-Compulsive Disorder (OCD)

## Current understanding

OCD is proposed to arise from disrupted complex (model-based) reasoning systems embedded in frontostriatal loops, rather than from an over-dominant habitual (model-free) system. A neurocomputational meta-controller framework implicates dysfunction in three possible mechanisms: impaired construction or use of complex reasoning systems; faulty meta-confidence updating leading to over-reliance on simpler systems; or impaired arbitration by the meta-controller itself.

## Key evidence

- Juvenile OCD patients show consistent difficulties in complex decision making and set-shifting (extra-dimensional shifts, planning), but not in simple reward learning or basic reversal learning, distinguishing OCD from disorders such as depression and schizophrenia ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

- Evidence for an excessive habitual (model-free) system in juvenile OCD is absent or inconsistent; the observed reduction in model-based reasoning in adult OCD may be a *consequence* rather than a cause of OCD, with longitudinal data suggesting compulsive symptoms precede model-based deficits ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

- Indecisiveness — operationalised as excess information sampling and elevated decision thresholds — is a robust and early feature of both juvenile and adult OCD; computational modelling attributes it to a delayed urgency signal rather than general cognitive impairment ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

- Confidence impairments (underconfidence, reduced metacognitive accuracy) are well-established in adult OCD but are largely unstudied in juveniles; some evidence suggests low confidence is partially driven by anxiety/depression rather than compulsivity per se ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

- Neuroimaging consistently implicates frontostriatal circuits — particularly the dmPFC/dACC and orbitofrontal/striatal regions — with heightened prediction errors in the dACC and aberrant myelination trajectories in OCD adolescents ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

- Effect sizes are smaller in paediatric than adult OCD literature (meta-analyses: medium-to-large in adults vs. small in children), possibly reflecting shorter disease duration or that remitting patients are included in juvenile samples ([Loosen 2020](../../raw/summaries/loosen2020_computational_psychiatry_ocd.md))

## Computational framework

The paper adopts a hierarchical RL framework in which multiple parallel reasoning systems coexist:

- **Simple motor-outcome caches** (model-free RL): Fast, automatic, but inflexible
- **Sophisticated cognitive models** (model-based RL): Flexible, complex reasoning about task structure
- **Meta-controller**: Located in dmPFC/dACC, uses reliability signals (formed from absolute prediction errors) to arbitrate between competing action policies

**Three proposed pathomechanisms**:
1. Impaired construction or use of complex reasoning systems
2. Faulty meta-confidence updating leading to over-reliance on simpler systems
3. Impaired arbitration by the meta-controller itself

Assumptions: Functional complexity of reasoning systems increases along a posterior-to-anterior gradient in prefrontal cortex; a corresponding ventromedial-to-dorsolateral gradient exists in the striatum; complex systems mature late in adolescence.

## History of ideas

Before this review, OCD was predominantly framed as a disorder of habit learning — specifically, an imbalance between goal-directed and habitual control, with an over-dominant model-free (habitual) system driving compulsive behaviour. This view was supported by:
- Outcome-devaluation studies showing persistent behavior after reward removal
- Frontostriatal models attributing OCD to direct/indirect pathway imbalance
- Neuroimaging highlighting hyperactivation of caudate and OFC

The developmental dimension was largely absent: the dominant model did not account for why OCD peaks in adolescence or how developmental trajectories of specific neural circuits might create vulnerability.

## Open questions

- The computational framework is explicitly described as speculative; face validity has been established via simulation but not direct empirical validation
- The juvenile OCD literature remains small, cross-sectional, and methodologically heterogeneous; many conclusions are extrapolated from adult studies
- Longitudinal studies tracking cognitive and neural development in OCD from adolescence are largely absent
- The directionality question — whether neurocognitive impairments precede, coincide with, or follow symptom onset — remains open
- The precise developmental timing of when different frontostriatal loops mature, and how this interacts with OCD onset, is unknown
- It is unclear how anxiety and depression comorbidities modulate the core OCD-specific computational impairments
- The framework does not specify how to distinguish its three pathomechanisms behaviourally
- The role of the amygdala and its relationship to the frontostriatal framework remains unresolved

## Related pages

- [Orbitofrontal cortex](../brain_regions/orbitofrontal_cortex.md)
- [Dorsomedial prefrontal cortex](../brain_regions/dorsomedial_prefrontal_cortex.md)
- [Anterior cingulate cortex](../brain_regions/anterior_cingulate_cortex.md)
- [Striatum](../brain_regions/striatum.md)
- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Computational psychiatry](../methods/computational_psychiatry.md)
