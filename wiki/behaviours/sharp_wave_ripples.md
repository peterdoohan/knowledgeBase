# Sharp-Wave Ripples (SWRs)

## Current understanding

Sharp-wave ripples (SWRs) are high-frequency oscillations (150–250 Hz) in the hippocampal local field potential that occur during awake immobility and slow-wave sleep. SWRs serve as the physiological substrate for replay—the time-compressed reactivation of place cell sequences. SWR rates are modulated by reward, serving as a nonspecific marker of reward-related hippocampal activation, but the directional content (forward vs. reverse replay) within SWRs shows differential reward sensitivity.

---

## Key evidence

- Sharp-wave ripple (SWR) rates track reward magnitude changes, serving as a nonspecific marker of reward-related hippocampal activation ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). SWR rate increased significantly at 4× reward end (z = 5.24, p = 1.61 × 10⁻⁷) and decreased when reward removed (z = −6.66, p = 2.67 × 10⁻¹¹).

- Both SWR rates and overall replay rates track reward magnitude, but only reverse replay (not forward replay) shows directional selectivity for reward changes ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)).

- Awake hippocampal SWRs drive both coordinated excitation and inhibition of distinct prefrontal cortical ensembles, with approximately equal numbers of PFC neurons excited (18%) and inhibited (17%) during SWR events ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)). This differs from sleep SWRs which predominantly excite PFC.

- CA1 population activity precedes PFC responses during SWR events with distinct latencies: CA1 peaks at 54 ms, SWR-excited PFC at 100 ms, and SWR-inhibited PFC at 84 ms, establishing the directionality of hippocampal-prefrontal information flow during replay ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- SWR-modulated PFC neurons show stronger theta phase-locking during movement (77% of excited, 71% of inhibited) compared to unmodulated neurons (53%), indicating these cells participate in functional hippocampal-prefrontal circuits active during both theta and SWR states ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- SWR-excited and SWR-inhibited PFC cells form functionally distinct ensembles with different spatial properties: excited cells have diffuse spatial firing and higher rates at faster movement speeds, while inhibited cells have concentrated firing around reward sites and low speeds, suggesting content-specific functional specialization ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- Structured CA1-PFC correlations during SWRs are experience-dependent and mirror theta-period co-activity structure: 16% of CA1-PFC pairs show significant SWR correlations (vs. ~5% chance), predicted by theta-period cross-covariance (r = 0.39), and these correlations are absent during pre-task rest, establishing that coordination is built through experience rather than reflecting fixed connectivity ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)). This dissociation indicates that SWR rate reflects general reward-related hippocampal activation, while the directional content within SWRs carries specific computational signals.

- Sleep and awake sharp-wave ripples may have distinct functions, with sleep SWRs primarily supporting memory consolidation and awake SWRs supporting memory retrieval and working memory, suggesting state-dependent functional specialization ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Wilson & McNaughton (1994) discovered sleep reactivation; subsequent work revealed awake replay functions.

- Only 15–20% of SWRs contain detectable replay; the remaining SWRs may carry directional content not captured by standard Bayesian decoding methods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The authors argue random cell sampling should not bias direction, but this remains unverified.

- SWR rates track subjective value and trial value, with this value-coding dependent on intact mPFC; SWR rates were lowest at Least preferred and highest at Most preferred restaurants (F(3,147)=15.98, p=4.8e-9); Waiting SWR rates increased with trial value (Good deals > Difficult > Bad deals; F(2,96)=93.25, p<3e-23) ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- mPFC disruption with inhibitory DREADDs specifically impairs post-learning consolidation SWRs while sparing on-maze SWRs; SWR rate increase from pre-maze to post-maze rest was significantly reduced on CNO days (F(1,49)=8.36, p=.0057; interaction F(1,49)=10.9, p=.0018), while on-maze SWRs showed no effect (p=.21) ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- mPFC disruption alters the content of planning-related SWRs, increasing non-local representations; on CNO days, Waiting epoch SWRs showed increased non-local decoding compared to VEH, with reduced differentiation between Current and other restaurants ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- SWR-modulated mPFC neurons respond to hippocampal non-local replay content but do not drive prospective mPFC coding; SWR-excited mPFC neurons fired more during hippocampal representations of upcoming choice, while SWR-inhibited neurons fired more during representations of alternative choice; SWR modulation strength greater in ventral than dorsal mPFC (p=.038) ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

---

## History of ideas

Sharp-wave ripples were first identified as a distinct hippocampal phenomenon characterized by high-frequency oscillations during immobility and sleep. The link between SWRs and memory reactivation emerged from studies showing that place cell sequences experienced during behavior were reactivated during SWRs in a time-compressed manner. Singer and Frank (2009) demonstrated that reward presence modulates SWR rate, establishing a link between reward and SWR generation. Ambrose et al. (2016) refined this understanding by showing that while SWR rates track reward magnitude nonspecifically, the directional content within SWRs (forward vs. reverse replay) is differentially modulated, with only reverse replay being reward-sensitive.

---

## Open questions

- What is the content of the majority of SWRs that do not contain detectable replay sequences?
- How does the circuit mechanism for SWR generation interact with dopaminergic input from VTA to produce reward-modulated SWRs?
- Are there distinct SWR types that preferentially contain forward vs. reverse replay?

---

## Related pages

- [[hippocampal_replay]]
- [[reverse_replay]]
- [[forward_replay]]
- [[place_cells]]
- [[hippocampus_ca1]]
- [[memory_consolidation]]
