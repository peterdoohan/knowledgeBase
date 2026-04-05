# Nucleus Accumbens (NAc)

The nucleus accumbens (NAc) is a region of the ventral striatum that plays a central role in reward processing, motivation, and reinforcement learning. It receives dopaminergic input from the ventral tegmental area (VTA) and forms a key node in the mesolimbic reward pathway.

## Current understanding

*No content yet — will be synthesised from Key evidence once sufficient facts are collected.*

## Key evidence

- D1-MSN stimulation in the nucleus accumbens drives VTA dopamine neurons via a hardwired biphasic linear filter that computes a temporal difference, demonstrating that TD error calculations are built into the dopamine-striatum microcircuit; optogenetic stimulation of lNAc D1-MSNs with 7 graded patterns produced dopamine responses matching TD error predictions including negative steady-state, with LTI model CV R^2 = 0.81 ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- The temporal discount factor gamma is hardwired in the D1-MSN to dopamine circuit and set by the balance of excitatory and inhibitory components; bootstrapped median gamma = 0.53 discount/sec from optotagged dopamine neurons, matching independent behavioral estimate of 0.56 from Masset et al. 2025; gamma = e^(-sigma) where sigma is LTI model pole; P/N ratio mathematically linked to gamma via exponential relationship ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- D1-MSNs in the nucleus accumbens acquire a value-like signal during opto-conditioning that is selectively potentiated by reward-predictive cues; lNAc D1-MSN calcium responses to odors were selectively potentiated by the CS+ over training (mean z-score difference = +0.62 ± 0.25, marginally significant, P = 0.0504 in D1 mice) while D2-MSNs showed no such potentiation (P = 0.84) ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- The lNAc carries a value signal necessary for TD RPE in natural reward tasks; muscimol inactivation of lNAc reduced CS+ dopamine responses (-2.30 %dF/F, P=0.0029) and increased predicted reward responses (+5.47 %dF/F, P=0.0013) without affecting unpredicted reward or omission responses, consistent with lNAc providing the value signal whose derivative is computed by VTA ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

## History of ideas

## Open questions

## Related pages

- [ventral_tegmental_area](ventral_tegmental_area.md)
- [striatum](striatum.md)
- [ventral_striatum](ventral_striatum.md)
- [temporal_difference_learning](../computational_frameworks/temporal_difference_learning.md)
- [reinforcement_learning](../behaviours/reinforcement_learning.md)
