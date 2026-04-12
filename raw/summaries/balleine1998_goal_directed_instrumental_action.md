---
source_file: "balleine1998_goal_directed_instrumental_action.md"
paper_id: "balleine1998_goal_directed_instrumental_action"
title: "Goal-directed instrumental action: contingency and incentive learning and their cortical substrates"
authors: "Bernard W. Balleine, Anthony Dickinson"
year: 1998
journal: "Neuropharmacology"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["lesion"]
brain_regions: ["prefrontal_cortex", "prelimbic_cortex", "striatum"]
frameworks: ["reinforcement_learning"]
keywords: ["hammond_1980_original_contingency_degradation_procedure", "colwill_and_rescorla_1985a", "1985b", "1986", "1988_reward_devaluation_and_associative_structures_in_instrumental_learning", "adams_and_dickinson_1981", "adams_1982_reinforcer_devaluation_and_overtraining", "dickinson_and_balleine_1994", "1995_motivational_control_and_incentive_learning", "dickinson_et_al_1995_motivational_control_after_extended_training", "dickinson_et_al_1996_bidirectional_instrumental_conditioning", "balleine_and_dickinson_1998_incentive_learning_and_sensory_specific_satiety", "thorndike_1911", "hull_1943_sr_reinforcement_theory", "squire_1992_declarative_vs_procedural_memory", "goldman_rakic_1994", "frith_et_al_1991_prefrontal_cortex_and_voluntary_action", "named_models_or_frameworks", "sr_reinforcement_theory_law_of_effect", "contingency_learning"]
---

### One-line summary

Instrumental behaviour is controlled by three dissociable processes — contingency learning, incentive learning, and S–R habit — and lesion studies in rats implicate the prelimbic prefrontal cortex in contingency learning and the insular cortex in incentive learning.

---

### Background & motivation

Classical stimulus–response (S–R) reinforcement theory, formalised in Thorndike's Law of Effect, treats instrumental learning as the strengthening of a stimulus–response connection with no encoding of the response–reward relationship. This account fails to explain two well-established phenomena: sensitivity to the causal contingency between action and reward (beyond simple contiguity), and the selective modulation of performance by reward devaluation. A third puzzle is that motivational state changes do not always have a direct, immediate effect on performance, implying that animals must learn the incentive value of rewards through consummatory experience. The paper addresses all three gaps while also beginning to map these processes onto distinct cortical structures.

---

### Methods

- **Subjects**: Male rats, food-deprived; all experiments involved lever pressing and chain pulling for two distinct food rewards (pellets and starch solution), counterbalanced across responses.
- **Contingency sensitivity**: Non-contingent (unpaired) reward delivery was superimposed on one reward, degrading the action–outcome contingency for that response only; responding was compared across sessions and in a final extinction test.
- **Reward devaluation**: One reward was devalued via specific-satiety prefeeding (1 h); performance was assessed in an extinction test to isolate associative knowledge of the response–reward relationship from direct hedonic effects.
- **Incentive learning**: Animals received post-training consummatory experience with rewards in alternating hungry and sated states; performance was then assessed in extinction while sated, testing whether motivational-state-dependent value had been stored.
- **Overtraining manipulation**: A subset received 360 (vs. 120) reinforcers to induce habit-like, devaluation-insensitive performance.
- **Lesion experiments**: Bilateral neurotoxic lesions (quinolinic acid) of the prelimbic area (PL) of prefrontal cortex or the insular cortex (IC) were compared with sham controls on all three paradigms (contingency degradation, reward devaluation, incentive learning).

---

### Key findings

- **Contingency sensitivity**: Intact rats selectively reduced responding for the action whose paired reward was also delivered unpaired, demonstrating sensitivity to causal contingency beyond mere contiguity. This effect was replicated in sham controls across lesion experiments.
- **Reward devaluation**: Specific-satiety prefeeding selectively and profoundly reduced performance of the associated response in extinction in intact and sham-lesioned rats (all 8/8 animals in representative experiments).
- **Incentive learning**: Motivational state did not directly control performance after limited training (120 rewards); control required prior consummatory experience with the reward in the relevant state. After overtraining (360 rewards), the incentive learning manipulation was ineffective, consistent with S–R habit control.
- **PL lesions abolished contingency sensitivity**: PL-lesioned rats failed to discriminate the same vs. different reward actions under the non-contingent schedule. They also showed no reward-devaluation effect in extinction, consistent with behaviour being reduced to S–R habit. Importantly, these animals could learn a reward-based discrimination task, ruling out simple perceptual or motor deficits.
- **IC lesions preserved contingency sensitivity but abolished reward devaluation in extinction**: IC-lesioned rats showed normal contingency discrimination (all 8/8 performing correctly) but indiscriminate responding in the extinction devaluation test. Crucially, when the rewards were present during the devaluation test (reinforced test), IC-lesioned animals showed normal selective devaluation effects — suggesting the IC is required to store the updated incentive value for use in the absence of direct reward, not for computing the change in value per se.
- **IC lesions impaired incentive learning for motivational-state modulation**: IC rats failed to transfer motivational-state-dependent incentive learning to control of subsequent sated-state instrumental performance, consistent with the IC housing the incentive memory for food rewards.

---

### Computational framework

The paper is explicitly framed within an associative learning / reinforcement learning framework, drawing on distinctions between contiguity-based S–R reinforcement and contingency-sensitive action–outcome (A–O) learning. The core conceptual architecture involves three parallel processes:

1. **S–R/reinforcement**: A procedural mechanism that strengthens stimulus–response bonds on the basis of response–reward contiguity. No reward representation is encoded; performance is insensitive to reward identity or devaluation. Dominant after extended training.
2. **Contingency learning**: An associative process that encodes the causal relationship between a specific action and a specific reward. Allows performance to track whether an action is causally effective (i.e., sensitive to the action–outcome contingency, not just contiguity). Implemented (partially) via the PL cortex.
3. **Incentive learning**: A process that assigns current motivational significance to a reward representation through consummatory experience in a given motivational state. This learned incentive value, stored in the IC, then modulates instrumental performance via the A–O association.

The framework is not formalised mathematically but maps closely onto model-based vs. model-free distinctions in later reinforcement learning literature. Key variables: response identity, reward identity, reward contingency (paired vs. unpaired probabilities), current and experienced motivational state.

---

### Prevailing model of the system under study

The dominant theoretical account at the time was the S–R/reinforcement framework originating with Thorndike's Law of Effect and formalised by Hull. In this view, reward acts solely as a "stamp in" mechanism strengthening the S–R bond; no representation of the reward is stored, and performance is therefore insensitive to devaluation or contingency. Motivation was accounted for by general drive theory (Hull, 1943): any motivational state increases a non-specific drive that potentiates whatever S–R habit is dominant, with selectivity arising only via stimulus properties of motivational states. The authors note that mainstream conditioning theory in the 1970s–90s shifted focus to the Pavlovian paradigm, and that neurobiological work on reward (e.g., Robbins & Everitt) had not yet specified how reward processes interface with structures mediating instrumental action. The literature on brain mechanisms of conditioning was dominated by Pavlovian preparations (fear conditioning, eyeblink).

---

### What this paper contributes

The paper establishes, using a clean behavioural design with two actions and two rewards, that instrumental performance in rats is governed by at least three separable processes rather than a single S–R mechanism. The critical empirical advance over prior devaluation and contingency studies is the within-animal, response-specific design that controls for non-associative explanations (e.g., response competition, general drive).

The lesion data provide the first direct neural dissociation between contingency learning and incentive learning as distinct cortical functions: PL supports the encoding and use of action–outcome contingency relationships, while IC stores incentive value information that can be retrieved in the absence of direct reward contact. The finding that IC-lesioned rats show normal devaluation when rewards are present but not in extinction precisely localises the IC's role to memory storage of updated incentive value, rather than to on-line evaluation. Together, the results support a model in which purposive, goal-directed action requires cortical structures that supplement (and modulate) subcortical S–R habit systems, consistent with an evolutionary layering from archaic habit mechanisms to more flexible, cortex-dependent goal-directed control.

---

### Brain regions & systems

- **Prelimbic area (PL) of prefrontal cortex** — proposed site of contingency learning (encoding action–outcome associations); PL lesions render behaviour habit-like and insensitive to instrumental contingency and reward devaluation.
- **Insular cortex (IC)** — proposed site of incentive memory for food rewards; IC lesions abolish motivational-state-dependent incentive learning and block the off-line (extinction) expression of reward devaluation, while leaving on-line (reinforced) devaluation and contingency sensitivity intact.
- **Basal ganglia** — mentioned as a candidate locus for S–R learning (White, 1989; Wolpaw et al.) but not directly studied in this paper.
- **Spinal cord** — cited as evidence that S–R-like plasticity is widely distributed in the nervous system (Wolpaw et al.).

---

### Mechanistic insight

The paper meets the bar for mechanistic insight, with the following caveats and mapping:

**Criterion 1 (algorithm)**: The paper proposes a specific algorithmic account: contingency learning computes action–outcome associations sensitive to the probabilistic contingency between response and reward (not just contiguity); incentive learning computes a conjoint representation of reward identity and motivational state through consummatory experience, storing this as an incentive memory that is retrieved off-line to modulate performance.

**Criterion 2 (neural data supporting the algorithm)**: Neurotoxic lesions of PL and IC selectively impair each process respectively, and the double dissociation (PL impairs contingency but not gustatory IC functions; IC impairs incentive learning but not contingency detection) provides support for the two-process distinction over a single unified system.

**Marr's levels:**

- **Computational**: The problem is adaptive instrumental control — selecting actions whose consequences are relevant to current needs. Goal-directed action requires knowing both what an action causes (contingency) and whether that cause is currently desirable (incentive value).
- **Algorithmic**: Contingency learning tracks the conditional probability of reward given vs. not given the action, encoding the action–outcome association. Incentive learning updates a reward-value representation through direct consummatory experience and indexes it to the motivational state in which experience occurred.
- **Implementational**: PL cortex (rat homologue of dorsolateral prefrontal cortex) is required for contingency learning; IC (gustatory cortex) stores incentive value memories for food. Subcortical (basal ganglia / brainstem) structures are proposed to support S–R habit. The paper does not address specific cell types, neuromodulators, or biophysical mechanisms; the implementational level is characterised only at the level of cortical areas.

---

### Limitations & open questions

- The lesion work is described as "preliminary"; sample sizes (n = 8 per group) and the absence of histological detail in the main text limit strong causal inference.
- PL lesions could in principle impair working memory, attention, or response selection rather than specifically contingency learning; though the authors rule out basic perceptual/motor deficits via a discrimination control, more selective manipulations would be needed.
- The paper does not explain the mechanism by which PL and IC interact, or how their outputs modulate subcortical S–R systems.
- The transition point between goal-directed and habit control (120 vs. 360 rewards) is described but not mechanistically explained.
- Incentive learning in the IC is framed around gustatory processing; it is unclear whether the same structure mediates incentive learning for non-food rewards.
- The paper does not address the neural basis of the integration of contingency and incentive signals to produce action selection.
- The relationship of these cortical circuits to dopaminergic reward prediction error signals (a major parallel literature) is not discussed.

---

### Connections & keywords

**Key citations:**
- Hammond (1980) — original contingency degradation procedure
- Colwill & Rescorla (1985a, 1985b, 1986, 1988) — reward devaluation and associative structures in instrumental learning
- Adams & Dickinson (1981); Adams (1982) — reinforcer devaluation and overtraining
- Dickinson & Balleine (1994, 1995) — motivational control and incentive learning
- Dickinson et al. (1995) — motivational control after extended training
- Dickinson et al. (1996) — bidirectional instrumental conditioning
- Balleine & Dickinson (1998) — incentive learning and sensory-specific satiety
- Thorndike (1911); Hull (1943) — S–R/reinforcement theory
- Squire (1992) — declarative vs. procedural memory
- Goldman-Rakic (1994); Frith et al. (1991) — prefrontal cortex and voluntary action

**Named models or frameworks:**
- S–R/reinforcement theory (Law of Effect)
- Contingency learning
- Incentive learning
- Goal-directed vs. habitual action distinction
- Declarative vs. procedural learning (Dickinson, 1980; Squire, 1992)

**Brain regions:**
- Prelimbic area (PL) of prefrontal cortex
- Insular cortex (IC / gustatory cortex)
- Basal ganglia (discussed but not lesioned)

**Keywords:**
- goal-directed instrumental action
- habit learning
- contingency sensitivity
- reward devaluation
- incentive learning
- prelimbic cortex
- insular cortex
- action-outcome association
- stimulus-response reinforcement
- motivational control
- specific satiety
- cortical substrates of instrumental conditioning
