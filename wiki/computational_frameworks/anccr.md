# ANCCR (Adjusted Net Contingency for Causal Relations)

## Current understanding

ANCCR is a retrospective causal learning algorithm that computes whether stimuli reliably precede rewarding outcomes more than expected by chance. Unlike temporal difference reinforcement learning (TDRL), which maintains forward-looking value predictions over tiled temporal states, ANCCR tracks retrospective associations and converts them to prospective predictions via Bayes' rule. The framework proposes that mesolimbic dopamine release signals ANCCR values rather than TDRL reward prediction errors.

---

## Key evidence

- Mesolimbic dopamine release in the nucleus accumbens core tracks ANCCR rather than TDRL RPE across eleven distinct experimental tests. Dopamine responses to unpredicted rewards increase across sessions (inconsistent with RPE decrease), correlate positively with inter-reward intervals (opposite to RPE prediction), and emerge before behavioral learning (inconsistent with tight RPE-behavior coupling) ([Jeong 2022](../../raw/summaries/jeong2022_mesolimbic_dopamine_causal.md)).

- ANCCR predicts dopamine cue responses that survive extinction, unlike TDRL which predicts decay to zero. After behavioral extinction, NAcc dopamine cue responses remained significantly positive, consistent with ANCCR's maintenance of long-term retrospective associations ([Jeong 2022](../../raw/summaries/jeong2022_mesolimbic_dopamine_causal.md)).

- Sequential conditioning produces simultaneous emergence of dopamine responses to first-order and second-order cues in ANCCR, but ordered backpropagation in TDRL. Empirical data showed cue responses increased together early in learning before diverging, consistent with ANCCR and inconsistent with TDRL's RPE backpropagation prediction ([Jeong 2022](../../raw/summaries/jeong2022_mesolimbic_dopamine_causal.md)).

- Optogenetic inhibition of dopamine neurons during second-order cue-to-reward intervals does not prevent first-order cue learning, consistent with ANCCR's independence of dopamine during intervals, inconsistent with TDRL's prediction of no learning without RPE ([Jeong 2022](../../raw/summaries/jeong2022_mesolimbic_dopamine_causal.md)).

---

## History of ideas

The dominant theory of dopamine function has been the reward prediction error (RPE) hypothesis, formalized through temporal difference reinforcement learning (TDRL). This framework, established by Schultz, Dayan, and Montague (1997), proposed that dopamine neurons signal the difference between expected and received rewards, driving learning through synaptic plasticity. The TDRL RPE account became widely accepted as causally necessary for behavioral learning, supported by optogenetic stimulation and inhibition studies.

ANCCR emerged as an alternative framework proposing that animals learn by retrospectively inferring which stimuli cause meaningful outcomes, rather than maintaining forward-looking value predictions. This retrospective causal inference approach generates qualitatively different predictions about dopamine dynamics across multiple experimental paradigms, challenging the universality of the RPE account.

---

## Open questions

- Does ANCCR extend to instrumental (action-contingent) learning, including action-conditional cognitive maps?
- What is the relationship between ANCCR signaling in the mesolimbic system and RPE-like signals observed in dopaminergic cell body recordings (electrophysiology)?
- How does the brain set the appropriate timescale for the ANCCR computation (i.e., how it estimates the inter-reward interval)?
- Whether dopamine in other striatal subregions (e.g., NAcc shell, dorsal striatum) also tracks ANCCR rather than RPE remains open.

---

## Related pages

- [temporal_difference_learning](temporal_difference_learning.md)
- [reinforcement_learning](reinforcement_learning.md)
- [ventral_striatum](../brain_regions/ventral_striatum.md)
- [ventral_tegmental_area](../brain_regions/ventral_tegmental_area.md)
- [conditioning](../behaviours/conditioning.md)