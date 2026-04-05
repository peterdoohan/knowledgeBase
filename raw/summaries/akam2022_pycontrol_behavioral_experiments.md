---
source_file: akam2022_pycontrol_behavioral_experiments.md
title: "Open-source, Python-based, hardware and software for controlling behavioural neuroscience experiments"
authors: Thomas Akam, Andy Lustig, James M Rowland, Sampath KT Kapanaiah, Joan Esteve-Agraz, Mariangela Panniello, Cristina Márquez, Michael M Kohl, Dennis Kätzel, Rui M Costa, Mark E Walton
year: 2022
journal: eLife
paper_type: empirical
contribution_type: methodological
---

### One-line summary

pyControl is an open-source Python-based hardware and software system for controlling behavioural neuroscience experiments, validated across timing performance benchmarks and three contrasting rodent behavioural paradigms.

---

### Background & motivation

Laboratory behavioural tasks are a cornerstone of neuroscience, yet existing tools present a persistent trade-off between flexibility and usability. Commercial systems are expensive, proprietary, and often non-extensible, while fully custom solutions require duplicated engineering effort and produce task code that is hard to share or replicate. Reproducibility of behavioural experiments is further hampered by the fact that published papers rarely specify task logic in sufficient detail, and publicly released code is only effective if it is readable and documented. pyControl was developed to address this gap: to make it quicker, cheaper, and easier to implement complex tasks at scale, while simultaneously improving communication and reproducibility across labs.

---

### Methods

- **System design**: pyControl comprises three integrated components — (1) a Python-based task definition framework running directly on a pyboard microcontroller (Arm Cortex M4, 168 MHz, 192 KB RAM) via MicroPython; (2) open-source hardware including a breakout board and a suite of behavioural devices (nose-pokes, audio boards, rotary encoders, stepper motor drivers, lickometers, LED drivers); (3) a graphical user interface (GUI) built in PyQt for configuring and running high-throughput parallel experiments.
- **Task formalism**: Tasks are defined as extended state machines — states, events, state-behaviour functions, timers — allowing arbitrary MicroPython code within state functions for maximum flexibility.
- **Framework performance validation**: Response latency and timing accuracy measured with a PicoScope 2204A USB oscilloscope at 50 kHz under low-load and high-load conditions (two additional analog inputs at 1 kHz + two Poisson digital inputs at 200 Hz average rate). Garbage collection effects on timers and digital inputs were also characterised.
- **Application examples** (three paradigms):
  - *5-Choice Serial Reaction Time Task (5-CSRTT)*: 8 male C57BL/6 mice in custom operant boxes; attention and impulsivity challenges validated; pharmacological validation with atomoxetine (2 mg/kg i.p.).
  - *Vibrissae-based object localisation task*: 3 female GCaMP6s-expressing head-fixed mice on a treadmill; Go/NoGo discrimination of pole position using whiskers.
  - *Social decision-making maze task*: 12 male C57BL/6J mice in a double T-maze; focal animal choices controlled reward delivery to both itself and a recipient animal.

---

### Key findings

- **Response latency** (low load): 556 ± 17 μs (mean ± SD); under high load: 859 ± 241 μs (mean ± SD), with 99.6% of latencies < 2 ms and maximum 3.3 ms.
- **Timing accuracy** (low load): errors approximately uniformly distributed across 1 ms (mean −220 μs, SD 282 μs), consistent with the framework's 1 ms clock resolution. Under high load: mean −10 μs, SD 353 μs; 99.5% of errors < 1 ms, maximum error 1.9 ms.
- **Garbage collection**: Timers that elapse during garbage collection are processed immediately afterwards; digital inputs are registered with correct timestamps, except when multiple edges on a single input occur within one garbage collection episode (only the last is processed).
- **Maximum continuous event rate**: approximately 960 Hz for digital inputs triggering state transitions; well above typical behavioural task requirements.
- **5-CSRTT validation**: Attention challenges (shorter stimulus duration, auditory distraction) selectively reduced accuracy and increased omissions without strongly affecting premature responses; impulsivity challenges (extended ITI) selectively increased premature responses. Atomoxetine (2 mg/kg) reduced premature responding and increased attentional accuracy (p<0.05, paired t-tests), replicating established pharmacological effects.
- **Vibrissae task**: Mice reached ≥75% correct performance within 5–9 training sessions; licking patterns before and after learning confirmed task acquisition.
- **Social decision-making**: Individual training produced appropriate behaviour in focal (no side bias; increasing trial rate) and recipient animals (~95% of pokes to active port by end of training); proof-of-concept social sessions demonstrated the task logic.
- Up to 24 setups have been run in parallel from a single computer without issue.

---

### Computational framework

Not applicable in the sense of a model of neural computation. pyControl implements a software engineering framework based on **extended finite state machines** — a classical formalism in computer science and control engineering. In this formalism, the system is always in one of a finite set of states; events (from hardware inputs or timers) trigger transitions between states; and state-behaviour functions containing arbitrary code (variables, conditionals, timers) extend the strict finite-state model to handle complex task logic. The key quantities are states, events, timers, and task variables. The framework assumes that task logic can be usefully decomposed into states and the transitions between them, which holds for the vast majority of operant and Pavlovian conditioning paradigms. Results from this paper constrain the design of behavioural control systems rather than models of neural computation.

---

### Prevailing model of the system under study

The paper does not investigate a neural system or mechanism — it addresses the methodological infrastructure for running behavioural experiments. The introduction frames the landscape as follows: commercial systems (e.g. Med Associates) are expensive and inflexible; DIY solutions (Arduino, Raspberry Pi, LabView) are flexible but require duplicated effort and produce poorly communicable code; existing open-source alternatives (Bpod, Bonsai) each have particular strengths and weaknesses. The implicit prior model is therefore that the field lacks a system that simultaneously achieves flexibility, low cost, high-throughput scalability, readable task syntax, and self-documenting reproducibility features. pyControl is positioned as filling this gap.

---

### What this paper contributes

pyControl establishes that it is possible to build a single open-source system that achieves sub-millisecond response latencies and millisecond-level timing accuracy, runs directly in high-level Python on low-cost microcontrollers, supports 24+ parallel setups from one computer, and automatically documents exact task versions and parameters with each dataset. The validation experiments demonstrate that performance is comparable or superior to commercial systems (explicitly benchmarked against Med Associates in the 5-CSRTT context) across three qualitatively distinct task types (operant attention, head-fixed sensory discrimination, social decision-making). The paper also provides a detailed conceptual comparison with the two closest alternatives (Bpod and Bonsai), clarifying the design trade-offs for prospective adopters. The primary contribution is a tool and a set of benchmarks that lower the barrier to implementing and sharing reproducible behavioural paradigms.

---

### Brain regions & systems

Not applicable. The paper is a methods/tool paper with no anatomical focus. The level of analysis is entirely behavioural and systems-level infrastructure: the unit of analysis is the task structure and the hardware/software system used to implement it. Three behavioural paradigms are validated — sustained attention and impulsivity (5-CSRTT), tactile sensory discrimination (vibrissae task), and social decision-making — but no neural recordings or imaging data are presented.

---

### Mechanistic insight

The paper does not meet the bar for this section. It presents no formalised algorithm of a neural computation, and provides no neural data (recordings, imaging, pharmacology beyond behavioural pharmacology as a task-validation tool). The atomoxetine experiment demonstrates that the pyControl 5-CSRTT implementation is sensitive to a known pharmacological manipulation, but this is used to validate the task rather than to test a mechanistic hypothesis. The paper operates purely at the level of methodology and behavioural phenotyping.

---

### Limitations & open questions

- MicroPython's automatic garbage collection can introduce brief pauses (a few milliseconds); if multiple edges arrive on a single digital input during garbage collection, only the last is processed. Users must manually manage garbage collection timing for the most latency-critical applications.
- The microcontroller's limited computational resources (no NumPy/SciPy, restricted RAM) preclude computationally intensive real-time processing (e.g. complex visual stimuli generation, online decoding).
- The system does not support direct access from task code to the host computer, though an API for this was in development at time of publication.
- Analogue audio playback is limited: one board uses the pyboard's internal DAC (simple waveforms only); the WAV-file board is limited to 44 kHz sample rate, which may be insufficient for some auditory neuroscience applications.
- The maximum number of parallel setups per computer has not been systematically characterised (24 confirmed without issue).
- Social decision-making behavioural results are presented only as a proof-of-concept; full analysis was planned for a separate publication.
- Bonsai comparison is acknowledged as incomplete — pyControl cannot perform real-time processing on high-dimensional data (video, high-rate analog), a regime where Bonsai is more capable.

---

### Connections & keywords

**Key citations**:
- Lopes et al., 2015 (Bonsai)
- Krakauer et al., 2017 (animal behaviour and brain function)
- Baker, 2016; International Brain Laboratory et al., 2021 (reproducibility)
- Carli et al., 1983; Bari et al., 2008 (5-CSRTT)
- O'Connor et al., 2010 (vibrissae object localisation task)
- Márquez et al., 2015 (social decision-making task in rats)
- Navarra et al., 2008; Paterson et al., 2011 (atomoxetine in 5-CSRTT)
- Grimm et al., 2018 (prior 5-CSRTT data from same group)
- Kapanaiah et al., 2021 (operant box design)

**Named models or frameworks**:
- pyControl (the system described)
- Bpod / PyBpod (comparison system)
- Bonsai (comparison system)
- Extended finite state machine (task formalism)
- 5-Choice Serial Reaction Time Task (5-CSRTT)
- Vibrissae-based object localisation task
- Social decision-making maze task

**Brain regions**: Not applicable.

**Keywords**: open-source behavioural neuroscience tools, extended state machine, MicroPython microcontroller, pyControl, high-throughput behavioural testing, task reproducibility, timing accuracy, 5-choice serial reaction time task, vibrissae object localisation, social decision-making, operant behaviour, behavioural hardware
