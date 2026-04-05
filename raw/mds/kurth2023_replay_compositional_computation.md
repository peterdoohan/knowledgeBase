**ll** 

## Perspective 

## Replay and compositional computation 

Zeb Kurth-Nelson,[1][,][2][,] * Timothy Behrens,[3][,][4] Greg Wayne,[1] Kevin Miller,[1][,][5] Lennart Luettgau,[2] Ray Dolan,[2][,][3] Yunzhe Liu,[6][,][7] and Philipp Schwartenbeck[8][,][9] 

1DeepMind, London, UK 

2Max Planck UCL Centre for Computational Psychiatry and Ageing Research, London, UK 

3Wellcome Centre for Human Neuroimaging, University College London, London, UK 

4Wellcome Centre for Integrative Neuroimaging, University of Oxford, Oxford, UK 

5Institute of Ophthalmology, University College London, London, UK 

6State Key Laboratory of Cognitive Neuroscience and Learning, IDG/McGovern Institute for Brain Research, Beijing Normal University, Beijing, China 

7Chinese Institute for Brain Research, Beijing, China 

8Max Planck Institute for Biological Cybernetics, Tubingen, Germany 9University of Tubingen, Tubingen, Germany *Correspondence: zebkurthnelson@gmail.com https://doi.org/10.1016/j.neuron.2022.12.028 

## SUMMARY 

Replay in the brain has been viewed as rehearsal or, more recently, as sampling from a transition model. Here, we propose a new hypothesis: that replay is able to implement a form of compositional computation where entities are assembled into relationally bound structures to derive qualitatively new knowledge. This idea builds on recent advances in neuroscience, which indicate that the hippocampus flexibly binds objects to generalizable roles and that replay strings these role-bound objects into compound statements. We suggest experiments to test our hypothesis, and we end by noting the implications for AI systems which lack the human ability to radically generalize past experience to solve new problems. 

## INTRODUCTION 

Replay in the brain was discovered in the context of spatial experiments on rodents. While the animal is moving, hippocampal neurons encode its current location in space. But when the animal rests or pauses, researchers noticed that the same neurons sometimes spontaneously sweep through a sequence of firing patterns, which repeat a path the animal recently traversed through space at an accelerated rate.[1–3] The phenomenon was fittingly termed ‘‘replay,’’ and is a major component of hippocampal function, comprising a large fraction of all spikes at rest.[4][,][5] It was hypothesized that the hippocampus rapidly stores new experiences and that replay is rehearsal to transfer this knowledge into a more stable form in the cortex,[6][,][7] a process called consolidation. 

However, over the past 20 years, our understanding of replay in the brain has grown. Although early experiments found replay sequences that directly repeated past experience, it gradually became clear that this is a special case of a much broader phenomenon. For example, Gupta et al.[8] measured replay sequences in rats who had experience running in a T-shaped maze. The animals always ran north up the central corridor and turned left or right at the T-junction. At rest, replay sequences traversed the entire width of the east-west corridor, stitching together segments of space that had only been experienced separately. Replay even synthesizes entirely novel sequences. In another experiment,[9] rats alternated between searching an open two-dimensional (2D) environment for a randomly placed reward and returning ‘‘home’’ (a fixed location) for another 

reward. The home location changed each day, creating many possible combinations of random location and home location. Spontaneous replay sequences formed trajectories ahead of the animal, predicting its future path, and this was true even when that particular path had never been physically traversed before. Similarly, when barriers are moved dynamically in a 2D environment, replay sequences quickly adapt to play trajectories that route around the new barrier locations.[10] When the only behavioral task is unstructured random foraging in an open environment, replays at rest play out diffusion-like trajectories that were never followed by the animal.[11] Most remarkably, replays can traverse areas of space that have never been visited. When rats are given full view, but only partial access, to a maze, and food is dropped into the inaccessible part, replay sequences spontaneously represent trajectories into the inaccessible part that has never physically been visited.[12] 

In light of an accumulating body of such data, the predominant view in neuroscience is that now sequences are not constrained to simply repeat past experience, but are informed by an internal model of the world.[13–18] This model could be used for online control of behavior (‘‘planning’’)[9][,][15][,][19][,][20] and for offline simulation to train a policy or value function (like Dyna).[21–23] 

## A NEW CONJECTURE 

The goal of this paper is to propose another update to how we think about replay. Our proposal is that replay in the brain instantiates a form of compositional computation. We will argue that a replay sequence constitutes a set of entities strung together into 

**==> picture [16 x 17] intentionally omitted <==**

454 Neuron 111, February 15, 2023 ª 2022 Elsevier Inc. 

**ll** 

## Perspective 

**==> picture [303 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D<br>**----- End of picture text -----**<br>


**==> picture [57 x 36] intentionally omitted <==**

**==> picture [116 x 43] intentionally omitted <==**

**==> picture [105 x 113] intentionally omitted <==**

**==> picture [46 x 35] intentionally omitted <==**

Figure 1. Two types of composability in replay 

(A) A structured compound, such as the concept ‘‘I am driving home from the airport,’’ can be described as a set of entities and the role each entity plays in the compound. Each entity, such as ‘‘driving,’’ is bound to a role, like ‘‘action.’’ The compound has a meaning that derives from the interaction of its parts but is not contained in any of the parts. (B) In our hypothesis, a replay sequence constitutes a set of entities, each tagged with the role of that entity, and is able to describe complex concepts. (C) One type of composability is that roles are independent of entities and are free to attach to new entities. (D) Another type of composability is that role-bound entities can be combined in many different ways to form new compounds. 

a compound. Each entity is transiently bound to a representation of its role in the compound, which specifies how that element functions as a part of the whole (Figures 1A and 1B). Thus, the replay sequence as a whole describes a structure whose meaning is an interaction of the parts and their relationships. Composing entities in this way allows replay to derive new knowledge. For example, if I already know that my laptop contains a processor and that the processor draws 30 W, then a replay sequence could derive the implication that the laptop draws at least 30 W. This is a speculative hypothesis, but it is a natural extension of recent neuroscientific discoveries about replay, which we will review. We will also offer experiments to test several predictions of the idea. 

The replay we envisage is built on two types of composability. The first type is a separation between entity and role (or, semantics and syntax): new entities can be bound to existing roles and vice versa (Figure 1C). The second type is that there are many ways to arrange role-bound entities into compounds (sequences), creating a potentially infinite space of compounds from a smaller number of elements (Figure 1D). We will use the idea of these two types of composability to organize the following sections. 

Our view agrees with the notion that replay draws on an internal model. However, in previous model-based accounts of replay, a replay event is a ‘‘rollout’’: a sequence of states predicted to occur sequentially in the world, with the model defining the transition probabilities between successive states. Our hypothesis relaxes this constraint, so that items in a replay event need not be successive states but instead may be a set of entities with arbitrary relationships to one another. Our hypothesis also relaxes the constraint that replays are used for online control of behavior or for updating a policy or value function. Instead, we suggest that replays can be used to derive new knowledge about the world by reasoning about the implications of combining existing pieces of knowledge. To forestall misunderstanding, our conjecture is not that all replay is best conceived as compositional computation. In simpler settings, replay does appear to recapitulate experience or to perform rollouts. Rather, we suggest that the machinery of replay—which likely evolved to solve 

simpler problems—gives rise to compositional computation when coupled with learning mechanisms and rich environments, and does so most dramatically in humans. 

## BINDING ENTITIES TO GENERALIZABLE ROLES IN HIPPOCAMPUS 

The first type of composability is binding new entities (role-fillers) to existing roles or vice versa.[24][,][25][,][26] In the example of Figure 1, the entity ‘‘airport’’ takes the role of ‘‘start point,’’ as part of a compound meaning ‘‘I am driving home from the airport.’’ The same role attached to a new entity, ‘‘aquarium,’’ would immediately have a different but interpretable meaning (‘‘aquarium as start point’’) and could be used to make new compounds. 

Our perspective is that the hippocampus has a general-purpose ability to bind entities to roles. This is an unproven idea, but experimental data from humans and animals make it an exciting possibility. We discuss these data in terms of three potential levels of generality of roles. At the first level, roles are constrained to be spatial (where something is relative to other things). At the second level, roles can be nonspatial but adhere to the Euclidean geometry of space (for example, a coordinate in the 1D space of auditory pitch). At the third level, roles can be nonspatial and non-Euclidean, potentially including arbitrary roles such as start point or ‘‘verb.’’ 

A large body of hippocampal literature on animals has primarily been concerned with studying spatial roles—our first level of generality. The hippocampus receives converging input from the brain’s ‘‘what’’ stream through the lateral entorhinal cortex, and its ‘‘where’’ stream through the medial entorhinal cortex.[27–30] The what stream carries representations that discriminate between different objects or sensory details but are invariant to how they are arranged in space. The where stream carries an abstract representation of space itself, providing a coordinate system that describes relative positions. These two streams combine in the hippocampus to form conjunctive codes, where the abstraction of space is joined with sensory specifics to code for a particular place or memory[24][,][31][,][32] (Figure 2A). For example, the medial entorhinal cortex contains object-vector 

Neuron 111, February 15, 2023 455 

## **ll** 

## Perspective 

**==> picture [481 x 415] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C D<br>E<br>**----- End of picture text -----**<br>


Figure 2. Binding of entities and roles in the hippocampus (A) A highly schematized depiction of two processing pathways in the cortex, adapted from Manns and Eichenbaum.[30] The ‘‘what’’ pathway, including the posterior parietal cortex and perirhinal cortex, extracts and transmits information about the identities and semantics of perceived entities (shown as geometric objects). The ‘‘where’’ pathway, including the inferior temporal cortex and parahippocampal cortex, extracts and transmits information about the relational roles of entities (shown as a repeating pattern representing an abstract code for space). After these pathways reach cells in the lateral and medial entorhinal cortex, respectively, they converge on cells in the hippocampus to produce conjunctive representations of ‘‘entity in role,’’ such as an episodic memory or a location in a particular environment. 

(B) Object-vector cells, in the medial entorhinal cortex, fire at a particular location relative to each object in the environment.[33] Landmark cells the in hippocampus show a similar pattern but are selective for particular objects.[34] 

(C) In the experiment of Sun et al.,[35] mice ran four identical laps around a track before receiving a reward. Some hippocampal cells (lap cells; three examples shown) were tuned not only to place but also to the lap index, firing selectively on particular laps. The x axis within each lap is the spatial location of the animal. The color axis shows the firing rate at that location, on that lap. Each row within each cell is a trial. 

(D) Each mouse performed the four-lap task in two different environments. Consistent with many prior experiments, hippocampal place cells remapped to new spatial locations between environments. Remapping can be explained as the same spatial role codes (medial entorhinal cortex; MEC) being conjoined with new sensory role-filler codes (lateral entorhinal cortex; LEC) in the new environment. Again, the x axis within each lap corresponds to the spatial location. The y axis represents the firing rate. 

(E) Lap cells did not remap to a different lap index between environments, which is explained by discrete role codes tuned to a particular lap.[32] 

cells (OVCs), which fire when the animal is at a particular location relative to any object in the environment[33] (Figure 2B). These cells code for a relational role, invariant to sensory specifics. Meanwhile, landmark cells in the hippocampus also fire at a 

particular location relative to an object, but restrict their firing to certain objects.[34] These cells code for a conjunction of role and sensory filler. In sum, the rodent spatial literature offers extensive evidence that hippocampal representations conjoin 

456 Neuron 111, February 15, 2023 

**ll** 

## Perspective 

abstract roles with sensory specific to describe role-bound entities. 

Newer experiments, in both humans and non-human animals, have started to broaden our understanding of the where pathway beyond physical space. Experimental data from the past decade,[36–40] aligning with older theories,[41][,][42] suggest that the where pathway carries information about nonspatial relational roles, ranging from social relationships to auditory pitch to configural stimulus spaces. Correspondingly, the hippocampus has conjunctive representations that go beyond space.[36][,][43][,][44] So far, experiments with nonspatial relations have mostly been limited to the second level of generality—Euclidean topologies such as 2D social relationships and 1D auditory pitch. 

However, there are hints that roles may even go beyond the Euclidean to the third level of generality. One point of supporting data is that non-Euclidean role representations appear in replay in humans,[45] which we discuss in more detail in the next section. Another piece of evidence comes from the representation of discrete states in the rodent hippocampus. In a task where a mouse had to complete four laps of a loop before reward became available,[35] hippocampal cells responded (as usual) at selective places in the lap. Some of these place cells were also ‘‘lap cells’’: they responded on a particular lap (Figure 2C). When the animal was asked to do the same task on a maze with different sensory cues, place cells that were not lap cells exhibited spatial remapping as usual[46] (Figure 2D). Lap cells also changed their spatial tunings but, crucially, they always fired on the same lap in both mazes (Figure 2E). This is exactly what is predicted by a system that has roles for spatial location and lap number, and fills them with the sensory particularities of each individual maze.[32] The different sensory input along each maze shifts the conjunctive cells in space, but this mechanism can never shift a cell between laps because each lap has the identical sensory input. Indeed, this same mechanism also explains open-field remapping experiments, where place cells preferentially remap to different peaks of the same grid cells. By remapping but staying at the same grid phase, a single place cell preserves its role input across different situations. Alternate accounts of these data, such as predicting reward or representing total distance traveled, are difficult to reconcile with the fact that they shift at random between different spatial locations (and different distances from the reward) in the two mazes. 

These hints of non-Euclidean role representations are limited to coding for an index within a sequence[35][,][45] or for a binary category.[45] But because roles can be learned from data,[24][,][32][,][47] there is potentially no limit to their richness and diversity. Future experiments are needed to probe a broader spectrum of roles, like "verb" (see section experimental predictions). Even if rodents represent some kinds of non-Euclidean roles, their repertoire is likely narrower than humans. But to the extent that the where pathway does carry information about general-purpose roles, conjunctive codes in the hippocampus may act as general-purpose bindings of entities to roles. 

## REPLAY AS COMPOSITIONAL COMPUTATION 

The central hypothesis of this paper is that replay sequences are made up of hippocampal representations of role-bound entities 

(first-level composition)—and by chaining these together into structures (second-level composition), sequences can express a huge variety of new compound meanings. Sequencing is a natural way to link entities because it interferes minimally with the spatial activity patterns that encode individual items. In other words, activating items in sequence keeps separate items separate. This is similar to how, in language, we put words in sequence instead of superimposing them. Continuing with the example of Figure 1, combining aquarium/start point with ‘‘a fish’s life/subject’’ makes a statement that is new yet interpretable. 

Our hypothesis builds on the idea of the hippocampus as a sequence generator,[48] where its function is to construct generic content-free sequences into which any content can be slotted. We add two things to this model. First, sequences do not have to be played in the order of experience; replay can assemble any set of things in any order. Second, each item in a sequence is bound to a representation of its role in the compound, allowing arbitrary compositional concepts to be constructed by putting together elements in complex ways. 

Compositional computation leverages the fact that the world itself is made up of more-or-less separate entities whose recombination in different ways is useful. Reassorting knowledge into meaningful new compounds brings the potential for strong generalization[49–53] and may underlie the flexibility of human imagination.[54–56] 

## Separate entities in replay 

The power of compositional systems comes from treating the world as made up of separate entities which can be recombined (Figure 3A). Reasoning about relationships between separate things is a potent form of abstraction, discarding everything except the relevant entities and relations.[49][,][57][,][58] For example, an animal might receive a reward due to an action it took an hour ago. This is a difficult credit assignment problem,[59] unless the animal abstracts away the continuum of sensory data between the action and the outcome. 

It is therefore interesting to view a replay sequence as a set of separate representations composed together into a unit. In nonspatial tasks with an inherently discrete structure, replay sequences jump abruptly between representations of the objects,[45][,][61][,][62] as we will describe in detail in the following sections. More surprisingly, replay also hops between discrete positions in spatial tasks[60] (Figure 3B). These hops are aligned with the gamma oscillation. At each peak in gamma, replay dwells at a stationary point in space, and at troughs, the representation jumps to a new point. Pfeiffer and Foster[60] suggest that peaks in gamma focus representation on a unit of information, and troughs allow transition to a different unit. This idea follows on from the large body of literature on pattern separation and pattern completion within hippocampal circuitry[63–65] as a mechanism for sharpening the differences between separate items. The Pfeiffer and Foster data are also consistent with longstanding theories that the gamma oscillation organizes neuronal spiking into discrete slots that correspond to cognitively relevant parcellations of information.[50][,][66–68] 

According to this view, it is plausible that both sharp wave ripple sequences and theta sequences form compositional 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, February 15, 2023 457 

Perspective 

## **ll** 

**==> picture [8 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [115 x 64] intentionally omitted <==**

**==> picture [115 x 64] intentionally omitted <==**

**==> picture [116 x 64] intentionally omitted <==**

**==> picture [97 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>**----- End of picture text -----**<br>


Figure 3. Discreteness in replay (A) Compositional systems divide the world into entities that can be recombined, like ‘‘pawn’’ or ‘‘c5 square.’’ These abstractions are only sensitive to key features that define each entity, with invariance to other features. The first and second images are both Caro-Kann, despite having almost no pixel similarity in the position of the c-pawn, while the third is Sicilian. (B) Replay sequences in a spatial task jump abruptly from point to point.[60] Animals ran around a 2D open field (black square), and replay was measured during subsequent rest. The image shows a single replay sequence, collapsing over 340 ms. Color at each pixel is the decoded probability that the replay sequence traversed that point in space. 

compounds. Most of the replay experiments we will discuss in this paper have investigated ripple-nested sequences, but a theta sequence also constitutes a set of conjunctive hippocampal representations. Theta sequences are associated with active behavior and may therefore perform compositional sampling for active control,[19][,][69][,][70] a topic we will return to later. 

## Replay beyond space 

For replay to implement general-purpose compositional computation, an obvious requirement is that it operates beyond the spatial domain measured in rodent replay experiments. Methodological advances have made it possible to detect replay in humans using magnetoencephalography (MEG), which enables the study of tasks with interesting nonspatial relationships that are difficult to explain to rodents.[61] In a nutshell, MEG replay experiments involve three stages. First, participants are presented with experimental stimuli (such as images of objects) in random order, with each stimulus repeated many times. The evoked MEG data are used to train decoding models that recognize the spatial pattern of MEG data coding for each stimulus. Second, participants perform a task in which they learn about some relationships between the stimuli (for example, chair always precedes ball). Third, during a time period of interest (such as a resting period), MEG data are analyzed using the trained decoding models to identify spontaneous reactivations of the stimulus representations. Replay is declared when spontaneous reactivations occur in fast sequences that adhere to the relationships learned about in the task. 

A number of experiments using this method have found replay in nonspatial tasks. Kurth-Nelson et al.[61] designed a directed graph of six nodes, where each node was defined by an object (cat, chair, etc.) (Figure 4A). Participants experienced trajectories through this graph, always seeing one object at a time, with the order of objects defined by the graph transitions. The graph itself had no natural spatial embedding, and subjects reported not conceiving of the objects in space, instead using conceptual mnemonics like ‘‘the cat sits on the chair.’’ After participants had learned about this implicit graph, MEG activity during rest periods spontaneously replayed sequences of object representations, in reverse order to the actual transitions of the graph (Figure 4B). Sequences were time-compressed approximately 

20-fold, so an entire sequence lasted about 120 ms. Nonspatial replay also matches several other identifying features of traditional spatial replay, including reward-dependent direction reversal and coincidence with sharp wave ripples.[45] 

Although these experiments used a simple set of visual objects, the hippocampus codes entities as diverse as social position,[40] state in abstract Markov decision processes (MDPs),[35][,][73] time,[74] sequence order,[75] evidence,[76] and auditory pitch.[36] Within the hippocampus’s switchboard,[48][,][64][,][77] we could imagine that replay sequences link together entities of different types— even from different levels of abstraction—such as hope and feathers, or equations and planetary orbits. 

## First type of composability in replay: Attaching objects to role representations 

We described the binding of entities to roles as the first type of composability. If I am given the set of words {attacked, alligator, python} without knowing the role of each item, I do not know who attacked whom. But if I bind each item to its role, as in {attacked/ action, alligator/patient, python/agent}, then I understand the meaning. 

Human MEG data indicate that replay sequences encode roles bound to objects. Liu et al.[45] trained human subjects on a nonspatial task designed to enable decoding of brain representations of roles separately from role-fillers. In the task, subjects learned about a set of eight objects that were arranged into two sequences of four items each. Each object’s role could therefore be described by two variables: which sequence it belonged to and which position (1st, 2nd, 3rd, or 4th) it occupied within that sequence (Figure 4C). Subjects performed this task in the MEG scanner, and Liu et al.[45] constructed two kinds of neural decoders. The first kind of decoder was trained to recognize each individual object (such as a house). The second was trained to recognize abstract representations of either position or sequence. Abstract position decoders predicted the category label of 1st, 2nd, 3rd, or 4th position, given the MEG data evoked by viewing either of the two objects having that position. Likewise, abstract sequence decoders predicted which sequence a viewed object belonged to, invariant to its position. The researchers validated these decoders by testing them with a special cross-validation technique where all instances of a particular 

458 Neuron 111, February 15, 2023 

## Perspective 

**==> picture [408 x 303] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D E<br>position-to-object lag (seconds) sequence-to-object lag (seconds)<br>G<br>F<br>**----- End of picture text -----**<br>


**==> picture [52 x 66] intentionally omitted <==**

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [21 x 22] intentionally omitted <==**

**==> picture [23 x 22] intentionally omitted <==**

**==> picture [46 x 47] intentionally omitted <==**

**==> picture [46 x 47] intentionally omitted <==**

**==> picture [7 x 19] intentionally omitted <==**

**==> picture [46 x 35] intentionally omitted <==**

Figure 4. Nonspatial replay and role representations 

(A) In Kurth-Nelson et al.,[61] subjects learned about the nonspatial relationships between six objects. 

(B) Replay sequences were detected with MEG and followed reverse paths in the graph.[61] Color axis shows the strength of spontaneous neural reactivations of four stimuli. (C) In Liu et al.,[45] subjects learned about a different nonspatial organization: eight objects comprising two sequences. The role of each object in the task could thus be described with two variables: position and sequence. 

(D) During a rest period,[45] replay spontaneously played out the learned sequences (not shown; similar to [B]). During these replay events, representations of the position and sequence variables also activated, with each role code slightly preceding the replayed representation of the corresponding object. The y axis is a measure of how consistently the position or sequence code precedes (positive) or follows (negative) the representation of the object. (E) Schematic of role tags in replay sequences.[45] Colored lines show decoding of spontaneous representations at rest, with the y axis representing the strength of decoding. Red lines correspond to concrete objects, which reactivated in fast sequences. Each object was accompanied by representations of the role it played: which sequence it belonged to, and which position it occupied within its sequence (blue lines). 

(F) Dragoi and Tonegawa[71] recorded replay sequences that formed trajectories through an environment before the animal’s first experience of that environment. Hippocampal cells spontaneously fired in sequences that played coherent trajectories through an as-yet-unvisited environment (left, each panel is a replay event recorded before experiencing the new environment). Those sequences were decoded by recording the spatial tunings that the cells subsequently adopted when the animal later experienced the new environment (right). 

(G) Replay is coordinated between place cells and grid cells.[72] Two example replay events are shown, with one place cell and one grid cell for each event. Color indicates probability of decoding at each spatial position; white lines are fit to the data. 

object were held out from training. For example, all instances of the 3rd item in the 2nd sequence might be held out from training. In testing, the position decoder successfully predicted that the held-out item was in the 3rd position, and the sequence decoder successfully predicted that the item was in the 2nd sequence. 

After constructing these decoding models, MEG activity was analyzed during a rest period that followed task learning. First, 

using object-specific decoders, spontaneous replay sequences were found to play out representations of the objects within a sequence. These replays coincided with transient increases in power in sharp wave ripple frequency. Second, using the abstract position and sequence decoders, the researchers found that each object in a replay sequence was accompanied (with a characteristic 50-ms lag) by a spontaneous reactivation of 

Neuron 111, February 15, 2023 459 

Perspective 

## **ll** 

that object’s abstract sequence and position (Figures 4D and 4E). In other words, each item in the replay sequence was tagged with its role. The effect is reminiscent of dynamic binding, where transient synchronous neural relationships bind roles to contents.[25][,][78][,][79] 

The same role tags that played in alignment with object replay sequences also played out in spontaneous sequences—even before the participants experienced the objects. This phenomenon, which the researchers called ‘‘transfer replay,’’ supports the idea that role representations exist separately from role-fillers and are subsequently bound to new role-fillers when they are learned. Transfer replay mirrors ‘‘preplay’’ in rodents, where spontaneous sequences play out coherent trajectories through an environment before that environment has been experienced[71] (although see Silva et al.[80] ) (Figure 4F). The sequences measured in the two experiments were of different kinds: Dragoi and Tonegawa[71] measured conjunctive place codes while Liu et al.[45] observed role codes. However, neither experiment was set up to detect the other kind of code. It is possible that role representations played out side-by-side with conjunctive representations in Dragoi and Tonegawa[71] but were not measured. Likewise, hypothetical sensory bindings may have played out along with roles in Liu et al.[45] Another unresolved question in both studies is whether the played structure (i.e., linear sequence) was hard-coded by evolution or learned from prior experiences. 

The experiments in Liu et al.[45] did not afford the anatomical precision to determine where role tags in replay are represented, but grid cells are a prime candidate. As discussed earlier, grid cells code for spatial relationships in spatial tasks and may code for more general relational roles in nonspatial tasks, while hippocampal cells putatively code for the conjunction of role with sensory specifics. In replay, hippocampal cells play out sequences of these conjunctive representations, while grid cells play out corresponding sequences in coordination[72] (Figure 4G). Given that Liu et al.[45] found representations of sensory information playing out in coordinated sequences with role-like representations, it is reasonable to think that replay events may include three kinds of representations in coordinated sequences: conjunctive codes in the hippocampus (including place cells in spatial tasks), role codes in the medial entorhinal cortex and other associated cortical areas, and sensory codes in the lateral entorhinal cortex and other associated cortical areas. Future experiments will be needed to test this prediction. 

Importantly, the roles investigated in Liu et al.[45] were limited to ‘‘which position’’ and ‘‘which sequence.’’ The perspective of this paper implies that replay sequences include more general roles such as verb or start point; future experiments will be required to test this prediction. It would be particularly interesting to test for the existence of role tags in replay that could support sophisticated computations. For example, if roles include operations such as ‘‘if,’’ ‘‘then,’’ and ‘‘else,’’ then perhaps rudimentary program fragments could be executed in replay sequences. Replay is therefore an intriguing candidate neurophysiological mechanism to implement symbolic computation in the brain.[81] 

Of course, in the real world, each entity plays different roles in different contexts. A car could be a way of getting to work, a source of scrap metal, or something to stand on. We suspect 

that replay sequences assemble entities bound to relevant roles according to the context, but understanding the mechanisms will require new experiments. 

## Second type of composability in replay: Stringing elements into sequences 

In spatial tasks, replay combines fragments of separate spatial experience to play out trajectories that are physically possible but were never experienced.[8–10] In nonspatial tasks, the scope for recombination of experience is vastly larger. 

Liu et al.[45] found that replay composes arbitrary objects into novel sequences using nonspatial relational knowledge. We described this experiment above but omitted one important detail. Participants experienced a set of eight objects: A, B, C, D, A[0] , B[0] , C[0] , D[0] . (The assignment of actual images, such as a chair, was randomized across participants.) Successful task performance required knowing that the objects were organized into two sequences: <A, B, C, D> and <A[0] , B[0] , C[0] , D[0] >. But the participants only experienced the objects in a scrambled order, such as <D[0] , B, C[0] , C, D, A[0] , A, B[0] >. They had previously learned a rule that allowed them to unscramble what they saw into the two true sequences. Behaviorally, subjects performed well at applying the unscrambling rule to derive the true sequences <A, B, C, D> and <A[0] , B[0] , C[0] , D[0] >. As described in the previous section, subjects had a rest period in the MEG scanner after experiencing the scrambled sequence, and object-specific decoders were used to detect spontaneous reactivations of the eight objects. Surprisingly, participants’ brains did not replay sequences in the order of experience. Instead, they played out in the never-seen rule-defined order (Figure 5A). It appears that replay strung a set of items together into a relevant novel compound. 

How is this reorganization achieved in the brain? As we saw in the previous section, replay of objects in Liu et al.[45] was accompanied by representations of which sequence and which position each object belonged to. Additionally, the position codes replayed spontaneously before the task objects were experienced (transfer replay). Taken together, these points of data suggest a potential mechanism for reorganization: the brain has an abstract template for ‘‘items in a sequence,’’[24][,][82] and when new items are encountered that fit this pattern, they are attached to the appropriate role in this template, allowing them to play in the correct sequence. However, for a general-purpose compositional system, it would be useful to not only fit new entities into a static template (like items in a sequence) but also to produce new compounds, where the roles themselves can be reorganized. For example, here is an English sentence in which not only are the words new but also the syntactic structure—the sentence diagram—is not a copy of any sentence I have previously written. 

In Schwartenbeck et al.,[62] in each trial, human participants were shown the silhouette of a complex 2D shape (Figure 5B) and given 3.5 s to think about how to assemble it from a set of four primitive building blocks they had previously learned about. Each solution involved exactly three blocks. Participants were aware that one particular building block would be present in all silhouettes. We call this block ‘‘stable.’’ The block that directly attaches to stable, in the ground truth solution for a given trial, we call ‘‘present.’’ The block attaching to present we call ‘‘distant 

460 Neuron 111, February 15, 2023 

**ll** 

## Perspective 

**==> picture [307 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B target<br>distant<br>present<br>present<br>object-to-object lag (seconds)  object-to-object lag (seconds) stable absent<br>**----- End of picture text -----**<br>


**==> picture [165 x 132] intentionally omitted <==**

**==> picture [46 x 35] intentionally omitted <==**

Figure 5. Replay sequences assemble entities into new compounds (A) Replay synthesizes novel sequences that are implied by an abstract rule.[45] Human subjects learned a rule that defined how a set of objects should be ordered. When they encountered a new set of objects (the eight objects shown) out-of-order, replay immediately began playing the items in the rule-defined order (true sequences). There was no replay in the actually experienced order (visual sequence). Each plot shows the strength of forward (positive y) or backward (negative y) sequences at every possible replay speed (x axis). 

(B) In a construction problem, sequences compose building blocks into candidate solutions.[62] In each trial of this task, subjects are presented a black silhouette (target) and given 3.5 s to consider how to build it from four component blocks they had previously learned about. The stable block is part of the solution for every target (in varying positions). Each other block can be present or absent in any given target. In the MEG signal, spontaneous representations of each block were decoded during the 3.5-s thinking period. The right panel shows the degree of consistent sequences (y axis) in the spontaneous activations at each moment relative to target onset (x axis). Tick labels are the start point of a 1-s sliding window used for sequence analysis. This plot zooms in on the most relevant time epoch. Early in the deliberation period, three kinds of replay sequences appeared (yellow, green, and blue traces), each involving the stable block and one other block. Soon after, sequences emerge that bidirectionally link the two present blocks (purple trace). Note that sequenceness here measures absolute rather than forward minus backward sequences, as plotted in (A). Negative A/B sequenceness occurs if A is followed by a reduced probability of B. Sequenceness is averaged over the range of element-to-element lags (10–200 ms) typically used for MEG replay analysis. 

present.’’ The fourth block is ‘‘absent.’’ To investigate replay signals underlying the mental construction process, the investigators trained classifiers on individual building blocks and measured pairwise sequences between spontaneous reactivations of those representations during the deliberation period, using similar methods to Liu et al.[45] They found a significant replay of several kinds of sequences of blocks. For example, detection of present/stable replay meant that the spontaneous reactivation of present was consistently followed by stable. Importantly, forming these replay sequences involved placing blocks into new arrangements, analogous to a new sentence diagram. 

Schwartenbeck et al.[62] also found that the content of the sequences changed dynamically during the deliberation period. Initially, sequences played out all combinations of stable with another block. In other words, there were independent sequences of present/stable, distant present/stable, and absent/stable. Shortly after, sequences appeared which combined distant present with present. The researchers argued that each replay sequence can be viewed as sampling a hypothesis about a partial solution of the target configuration in order to evaluate the hypothesis and gradually resolve uncertainty about the solution. The earliest sequences reflected all combinations of blocks compatible with the prior knowledge that the stable block exists somewhere in the solution. These sequences ostensibly discovered that present attaches to stable, after which sequences started to sample the combination of distant present with present, forming the remainder of the solution. 

The data from Schwartenbeck et al.[62] suggest that not only is replay not constrained to play out the actual order of experience but it that may also not even be constrained to play out succes- 

sive states in an MDP. After viewing each silhouette and thinking about how it could be built from blocks, participants were shown two blocks and asked a yes/no question about whether these blocks would have a particular relationship (such as ‘‘right of’’) in the solution. They never actually placed blocks to construct a solution. Thus, the task does not have an MDP in which the observed replay sequences are successive states. Of course, it is possible that participants could construct a fictive internal transition model and that replay consists of rollouts in the fictive model. This seems unlikely, given the observed pattern of replay, but would be difficult to fully rule out because nearly any pattern of data could, in principle, be explained by some fictive model. 

One interpretation of the Schwartenbeck data is that sequences traverse paths in a graph of entities, where edges are arbitrary relationships between entities. In fact, even constraining replay to traverse coherent paths might not be necessary if each item in a replay sequence is coupled to its role. However, order may provide extra information, for example, to de-alias ambiguous or repeated roles; order is apparently also a downstream consequence of the neural mechanisms that generate sequences. More work will be needed to understand the significance of order within sequences. 

## Planning with compositional replay 

Reorganization of knowledge in replay sequences may be a mechanism for planning. When animals face a spatial decision, spontaneous neural sequences rapidly sample multiple possible future trajectories,[19][,][69][,][83] likely as part of a planning and evaluation mechanism.[15][,][16][,][84–86] Planning in nonspatial tasks is thought to work similarly, sampling compositions of prior knowledge to search for solutions.[87–89] We suspect, then, that replay actively 

Neuron 111, February 15, 2023 461 

Perspective 

## **ll** 

**==> picture [377 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>**----- End of picture text -----**<br>


**==> picture [89 x 88] intentionally omitted <==**

**==> picture [89 x 88] intentionally omitted <==**

**==> picture [68 x 80] intentionally omitted <==**

**==> picture [105 x 85] intentionally omitted <==**

**==> picture [112 x 81] intentionally omitted <==**

Figure 6. Hybrid systems 

(A) Current goals bias replay sequences. In Wikenheiser and Redish,[70] rats ran in a circle, sometimes electing to pause at one of three equally spaced feeders (upper-left, upper-right, and bottom). Replay sequences (colored dots) traversed paths ahead of the animal. In trials when the rat would subsequently stop at a particular feeder, the prospective sequences also terminated at that feeder (left panel). When the rat did not plan to stop, sequences skipped the feeder (right panel). ‘‘X’’ is the animal’s location. 

(B) Blocking replay impairs learning. Replay sequences are nested within sharp wave ripples, the high frequency oscillation shown in blue trace and inset of red trace. Girardeau et al.[111] performed online detection of ripples during a rest period after each day’s learning session and injected current to disrupt replay events at their initiation (upper left panel). In the control condition (blue), current was injected 100 ms after the detected ripple (lower left panel). The calibration bars show 20 ms on the x axis and 0.2 mV on the y axis. Disrupting replay during rest impaired acquisition of the task (right panel; red disrupted learning curve below blue control and black no current injection). 

(C) Simplified diagram of AlphaGo,[112] which has a neural network component (red) and a discrete search component (black). The network predicts which moves are good in each board position. This constrains the search mechanism, reducing the combinatorial explosion of the game. The results of searches are ultimately used to train the neural network, creating a feedback loop. 

constructs new compounds (possibly in the form of program fragments) that represent potential partial solutions to a problem. Sampling compositional hypotheses in replay aligns with the brain’s widespread use of sampling for uncertainty representation and inference.[90–95] 

There is, of course, a continuum between online planning and offline processing of knowledge. When active behavior is required, replay samples the sequences relevant to that behavior.[9][,][70] Without task demands, sampling is less constrained,[11][,][96] presumably to prepare for a range of possible future scenarios. But the organism always has some information about upcoming decisions, so offline processing lies on a spectrum with planning.[97][,][98] When decisions are not needed imminently, we imagine that replay reviews the knowledge base, deriving new facts and identifying inconsistent beliefs requiring revision, akin to generalized path integration[99] in conceptual space. When a child learns ‘‘dolphins are mammals,’’[100][,][101] offline replay begins to explore and discover the implications, linking and cross-checking it with other knowledge. This takes a while, during which time contradictory beliefs will often be held. 

Is replay too noisy to do such intricate computations? Although statistically reliable, the magnitude of MEG sequence effects is often low in absolute terms.[45][,][61] However, our measurements of replay exaggerate the amount of noise. Not only are our decoders of neural activity far from perfect but the brain is also doing much besides dealing with the logic of the experimenter’s task. Additionally, noise is not all bad; for example, noise drives sampling and exploration.[102] 

## Replay’s bidirectional interactions with the cortex 

So far, we have focused on replay in the hippocampus, but hippocampal replay of course functions as part of the larger system of the brain. One very basic point of connection is that the representations in the hippocampus derive from the cortex. Thus, the compositional computations of replay are grounded[103] in 

cortical representations. (Ongoing replays may in fact help to maintain the tight coordination between the hippocampus and the cortex.[104] ) 

The contents of replay sequences are also shaped by the cortex. For example, when an auditory stimulus is played to rats during sleep, spontaneous reactivations in the hippocampus are biased toward places previously associated with that sound,[105] with the hippocampal activations immediately preceded by corresponding activations in the auditory cortex.[106] Although those experiments measured individual reactivations rather than sequences, replay sequences have also been observed where the cortex systematically leads hippocampal representations.[107] 

Additionally, the contents of replay sequences are influenced by the organism’s current goals[9][,][12][,][70][,][108] (Figure 6A). Liu et al.[45] found that spontaneous value representations localized to vmPFC were predictive of replay of a rewarded sequence, but not of an unrewarded sequence, following the general principle of frontal areas orchestrating hippocampal memory retrieval.[109][,][110] We conjecture that, if hippocampal memory is thought of as a probabilistic model of the large joint distribution of experience, the cortex may bias retrieval by conditioning that distribution on particular features (for example, reward) to obtain relevant samples. Of course, the degree to which the hippocampus itself encodes joint structure between items, versus this information coming from cortex, remains an open question. 

In the other direction, hippocampus-to-cortex, our proposal builds on the classic theory of systems consolidation,[6][,][7][,][113] where the hippocampus rapidly stores new experiences and later reactivates them to consolidate the knowledge into a more stable form in the cortex. A wealth of evidence indicates a role for replay in consolidation.[5][,][15][,][114] Sharp wave ripples, in which replays are nested, drive increased hippocampal-cortical communication and cortical plasticity, while disrupting ripples impairs learning (Figure 6B). 

462 Neuron 111, February 15, 2023 

**ll** 

## Perspective 

Consolidation theory also posits that replaying different experiences in close proximity allows the cortex to learn latent commonalities.[6][,][115–118] This semantic knowledge induced in the cortex by replay may itself have grammar-like structure.[119][,][120] The contents of replay are also optimized to cause the learning that will be most relevant for future tasks.[121–125] 

As described above, newer experiments have identified situations where replay does not strictly recapitulate past experience but instead generates new trajectories using a learned transition model, which itself is plausibly situated in the cortex.[8–12][,][45] Such model-based replays do not conform to the simplest models of consolidation because they do not faithfully reactivate actual past experiences. They may, nevertheless, support the transfer of knowledge from the hippocampus to the cortex by training the cortex on the statistics of possible trajectories, analogous to Dyna in machine learning.[23] Replaying actual experience can in fact be viewed as a special case of model-based replay using a nonparametric model.[126] There is some evidence that model-based replay has the additional function of contributing to online planning.[15] 

As model-based replay generalizes consolidation, our proposal further generalizes the idea of model-based replay. We have proposed that not only are replays not limited to playing back actual experience, they are also not even limited to playing out trajectories defined by a transition model. Instead, they play out sets of elements along with syntactic roles that define how the elements function together as a whole. Furthermore, instead of directly updating a value function or policy (as in Dyna), we suggest that replay discovers new knowledge of a more general form that does not necessarily have any immediate impact on the policy. An interesting implication is that consolidation mechanisms cause the cortex to learn about the new knowledge discovered by composing elements into sequences. 

The bidirectional interaction between replay and cortex sets up the possibility of a positive feedback loop.[117][,][127] According to our theory, replay composes existing entities into sequences, and new knowledge is derived from the meaning of the sequence as a whole. If that new knowledge is baked into the cortex,[128] it could subsequently function as a single element in higher-order replay sequences (i.e., sequences composed of pieces of knowledge that were previously derived from other sequences). The loop might produce a hierarchy of increasingly elaborate concepts. A similar feedback loop could operate at a faster timescale, too. Some neurons in the prefrontal cortex are tuned to specific replay sequences,[129] and if these neurons feed back into hippocampus as entities, then higher-order sequences could be composed within hundreds of milliseconds. 

## Experimental predictions 

Our perspective is that replay sequences sample structured compositions of existing elements to derive new knowledge. The most obvious experimental implication is that when replay is disrupted, the derivation of new knowledge through composition should be impaired. This could be tested using a task where subjects are taught about novel elements and how those elements work together. After teaching subjects about these elements, the experiment would require detecting the initiation of replay and immediately disrupting it,[84][,][111] with the prediction 

that disrupted individuals would subsequently demonstrate less knowledge about the implications of the rules. Such an experiment is challenging, because reasoning in rodents is limited, and disrupting replay in humans has never been attempted. Experiments in rodents would require the design of tasks to access compositional cognition, perhaps by training on a small set of conditional rules. Disruption in humans might be possible with ultrasound or transcranial magnetic stimulation, especially if replay initiation could be predicted slightly in advance using machine learning. In disruption experiments, careful controls for nonspecific effects, such as impaired memory for task-related information, would be essential. 

Disruption experiments will be vital for establishing whether replay has a causal function in compositional computation. Even when replay appears sophisticated, it is possible that this complexity is epiphenomenal, a kind of ‘‘exhaust fume’’ for computations actually performed elsewhere. However, there are reasons to be optimistic that compositional replay is in fact causal. First, as discussed in the previous section, disruption experiments in rodents have shown that replay is causally involved in learning and decision-making. Second, replay has pieces of the machinery—like the role codes in Liu et al.[45] —that would be useful for performing compositional computation. Third, replay that is relevant to a novel problem appears within hundreds of milliseconds of the onset of that problem, as in Schwartenbeck et al.[62] 

Aside from disruption experiments, another prediction is that after knowledge is derived by replay, it is subsequently available for use in other neural computations. For example, novice players could be tasked with solving a chess puzzle where the king is in check by a bishop (of course, a real experiment would be designed to eliminate the confounds inherent in chess). MEG decoding models would be trained to recognize representations of the pieces as well as their relational roles. As subjects consider the puzzle, we predict that replay sequences would explore various organized combinations of the pieces, examining the implications of their interactions. At some point during deliberation, a sequence is constructed that contains the king and bishop as elements and the bishop’s moving pattern as a relation. This sequence implies that the king is in check. After this sequence appears (but not before), the brain has knowledge of the king being in check, and this knowledge should manifest in several ways. It might be possible to decode the representation of ‘‘king in check’’ from the brain. Subsequent replay sequences might be constrained to evaluate only the moves that escape check. And, if forced to move, subjects might behaviorally reflect the knowledge of the king being in check. Although such a correlation would not prove a causal role for replay, it would be suggestive if the temporal relationship were consistent, with knowledge of the check appearing at a short, predictable delay after replay sequences containing the king and bishop. 

Finally, we have hypothesized that representations of items in a replay sequence are accompanied by representations of relational roles that describe how the items fit together to produce an overall meaning. As described earlier, Liu et al.[45] found a special case of these relational roles in replay: representations of ‘‘which sequence does this item belong to’’ and ‘‘which position does this item occupy.’’ Future experiments can test more general 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, February 15, 2023 463 

Perspective 

## **ll** 

roles. For example, if participants are asked to name the relationship between two distant relatives in a family tree, do replay sequences sample possible ways of linking them (like ‘‘mother’s father’s brother’’), and are replayed representations of individuals accompanied by representations of familial roles like ‘‘brother’’ or ‘‘stepdaughter’’? Again, a real experiment should use an appropriate grammar of relationships to reduce confounds. 

## REPLAY IN THE BRAIN AND AI 

In this final section, we consider the implications of our proposal for the relationship between hippocampal replay and machine learning. Replay has been a key point of connection between AI and neuroscience.[18][,][130–132] Replay in the brain is commonly compared with the technique of ‘‘experience replay,’’ where an agent stores its observations and later retrieves them for offline learning. This idea fits well with neuroscientific results where replay appeared to recapitulate actual experiences. It can also accommodate the observations, discussed in earlier sections, that replay generates novel sequences. A space of replay techniques in machine learning use experience to train a forward model of the world’s dynamics and then sample trajectories from the model to train a reactive policy.[23][,][133] 

But in this paper, we have proposed that replay in the brain has a more general function: deriving new knowledge through compositional computation. Therefore, how should we view the correspondence to AI? In this section, we suggest that replay, as compositional computation embedded in the larger brain system including the cortex (which behaves in many ways like a deep neural network[134–137] ), should be mapped to machine learning techniques that hybridize compositional computation with deep learning. 

Although humans learn new concepts or tasks from just a few examples, standard deep learning architectures cannot do this because they do not generalize effectively from their past experience.[138] At the same time, explicitly compositional AI systems without deep networks can reason about situations far outside their experience[57][,][58][,][138] but typically lack the abilities of neural networks to learn from raw data and scale to large problem sizes. Due to this complementarity, there have been many efforts to hybridize deep learning with compositional ingredients.[49][,][112][,][139–141] 

We outline a possible mapping between such hybrid machine learning systems and replay, following five principles: 

- (1) Neural networks are used to prune large compositional search spaces. 

- (2) New knowledge is discovered by search. 

- (3) A positive feedback loop results from networks informing search and search improving networks. 

- (4) Compositional operations live along a spectrum, from hard-coded to emergent. 

- (5) Entities are grounded in neural network representations. 

Consider the example of AlphaGo[112] (Figure 6C). Part of AlphaGo is a handcrafted algorithm that searches through trees of possible future moves in order to find move sequences most likely to lead to a win. Another part of the system is a neural network that predicts which moves are likely to be good. The 

search algorithm prioritizes moves that are preferred by the network, reducing combinatorial explosion, and drastically improving search efficiency. 

AlphaGo’s search is a special case of compositional computing because it is made up of discrete elements linked in organized ways to derive new knowledge. Viewing AlphaGo through this lens suggests a hypothesis for neuroscience: that the cortex predicts which combinatorial arrangements in replay sequences are useful and biases the hippocampus toward generating these sequences. Although the syntax of AlphaGo’s search only deals with board positions linked by moves, neurally guided search is also effective in many other machine learning contexts, such as searching through the space of programs expressed in a programming language.[140][,][142][,][143] 

AlphaGo uses the results of search both to make immediate decisions and to train its neural network. When playing a game, AlphaGo selects each move according to a search. But to train the neural network, AlphaGo plays millions of games against itself, and the network is trained to prefer moves that lead to winning outcomes. In this way, new knowledge discovered by the search process is gradually baked into the network. As AlphaGo’s network improves, the quality of searches rises, which further improves the network in a positive feedback loop. While the effect of search to improve AlphaGo’s network is indirect (via self-play), other related AI systems[140][,][144] train a neural network directly on knowledge discovered by search. 

Across the large family of methods that hybridize neural networks with compositional representation, there is a wide range of design choices about the degree to which the compositional component is handcrafted versus learned implicitly. At one extreme, AlphaGo uses a fully handcrafted search algorithm and searches through the space of idealized board positions. At the other extreme, training unstructured neural networks on certain distributions of data leads to the emergence of structured compositional operations within the dynamics of the network.[145–147] Between these endpoints, there are many compromises. 

MuZero[148] has a similar architecture to AlphaGo but is not endowed with knowledge of any game’s rules. Instead, it learns from experience to transform its inputs into useful representations and to predict the environment’s dynamics. Thus, like replay but unlike AlphaGo, MuZero grounds the elements that are recombined through search. However, unlike replay, neither AlphaGo nor MuZero have a rich syntax. Elements are combined only into chains of moves that follow one another in gameplay. An interesting direction in AI research is combining MuZero-style grounded entities and roles with syntactically rich composition. 

Neural networks with attention[149–151] form another midpoint. Attention mixes together multiple inputs according to a set of weights, such that the inputs with low weight are filtered out and those with high weight are retained. The weights are calculated on-the-fly as a learned function of data. Neural networks with attention have set new standards for performance in many areas of machine learning.[152–154] An important observation is that attention gives rise to role-filler binding.[26][,][155–158] This is because a role can induce weights that attend selectively to the filler, thereby accessing its contents. If the contents of the filler change, the weights attend to that new data. Or, to rephrase 

464 Neuron 111, February 15, 2023 

## Perspective 

in the language we have been using for replay, attention grants the first type of composability. In the context of replay, it is curious that attention-based neural networks, despite their amazing successes, often fail at structured reasoning,[159][,][160] which depends on composing elements into compounds. Another exciting project in AI research is adding replay-like composition mechanisms to attention-based neural networks. 

## Conclusions 

The world is too complex for an agent to force all its beliefs to be immediately consistent with one another—we still cannot reconcile gravity and quantum mechanics, for example, although having them as separate theories is highly useful. Real intelligence therefore requires understanding things in multiple ways, with a variety of metaphors or views on a problem that are kept separate from one another. But these different conceptualizations need to be sometimes put into contact with one another in order to find new symmetries and reach a deeper understanding. In many contexts, interesting structure arises from alternation between these two modes of a system, one where elements remain relatively separated and another where interactions are frequent.[161–163] Perhaps the hybridization of replay with the cortex serves this purpose. The compositional system of replay maintains separate pieces of knowledge, while the cortex extracts semantic abstractions. In this way, replay may contribute to the brain’s capacity for open-ended learning and creativity.[164] 

## ACKNOWLEDGMENTS 

We thank Zach Duer, Marc Guitart-Masip, Jess Hamrick, Kim Stachenfeld, and Steve Sullivan for insightful discussions and comments on a draft of the manuscript. Z.K.-N. was funded by DeepMind Technologies. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

## **ll** 

8. Gupta, A.S., van der Meer, M.A., Touretzky, D.S., and Redish, A.D. (2010). Hippocampal replay is not a simple function of experience. Neuron 65, 695–705. 

9. Pfeiffer, B.E., and Foster, D.J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. Nature 497, 74–79. 

10. Widloski, J., and Foster, D.J. (2022). Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping. Neuron 110, 1547–1558.e8. 

11. Stella, F., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). Hippocampal reactivation of random trajectories resembling brownian diffusion. Neuron 102, 450–461.e7. 

12. O[´ ] lafsdo´ ttir, H.F., Barry, C., Saleem, A.B., Hassabis, D., and Spiers, H.J. (2015). Hippocampal place cells construct reward related sequences through unexplored space. eLife 4, e06063. 

13. Dudai, Y. (2012). The restless engram: consolidations never end. Annu. Rev. Neurosci. 35, 227–247. 

14. Foster, D.J. (2017). Replay comes of age. Annu. Rev. Neurosci. 40, 581–602. 

15. O[´ ] lafsdo´ ttir, H.F., Bush, D., and Barry, C. (2018). The role of hippocampal replay in memory and planning. Curr. Biol. 28, R37–R50. 

16. Pezzulo, G., van der Meer, M.A., Lansink, C.S., and Pennartz, C.M. (2014). Internally generated sequences in learning and executing goaldirected behavior. Trends Cogn. Sci. 18, 647–657. 

17. Roscow, E.L., Chua, R., Costa, R.P., Jones, M.W., and Lepora, N. (2021). Learning offline: memory replay in biological and artificial reinforcement learning. Trends Neurosci. 44, 808–821. 

18. Wittkuhn, L., Chien, S., Hall-McMaster, S., and Schuck, N.W. (2021). Replay in minds and machines. Neurosci. Biobehav. Rev. 129, 367–388. 

19. Johnson, A., and Redish, A.D. (2007). Neural ensembles in ca3 transiently encode paths forward of the animal at a decision point. J. Neurosci. 27, 12176–12189. 

20. Mattar, M.G., and Lengyel, M. (2022). Planning in the brain. Neuron 110, 914–934. 

21. Johnson, A., and Redish, A.D. (2005). Hippocampal replay contributes to within session learning in a temporal difference reinforcement learning model. Neural Netw. 18, 1163–1171. 

22. Mattar, M.G., and Daw, N.D. (2018). Prioritized memory access explains planning and hippocampal replay. Nat. Neurosci. 21, 1609–1617. 

**==> picture [46 x 35] intentionally omitted <==**

## REFERENCES 

1. Louie, K., and Wilson, M.A. (2001). Temporally structured replay of awake hippocampal ensemble activity during rapid eye movement sleep. Neuron 29, 145–156. 

2. Na´ dasdy, Z., Hirase, H., Czurko´ , A., Csicsvari, J., and Buzsa´ ki, G. (1999). Replay and time compression of recurring spike sequences in the hippocampus. J. Neurosci. 19, 9497–9507. 

3. Skaggs, W.E., and McNaughton, B.L. (1996). Replay of neuronal firing sequences in rat hippocampus during sleep following spatial experience. Science 271, 1870–1873. 

4. Buzsa´ ki, G. (1989). Two-stage model of memory trace formation: a role for ‘‘noisy’’ brain states. Neuroscience 31, 551–570. 

5. Buzsa´ ki, G. (2015). Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. Hippocampus 25, 1073–1188. 

6. McClelland, J.L., McNaughton, B.L., and O’Reilly, R.C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychol. Rev. 102, 419–457. 

7. Wilson, M.A., and McNaughton, B.L. (1994). Reactivation of hippocampal ensemble memories during sleep. Science 265, 676–679. 

23. Sutton, R.S. (1991). Dyna, an integrated architecture for learning, planning, and reacting. SIGART Bull. 2, 160–163. 

24. Behrens, T.E.J., Muller, T.H., Whittington, J.C.R., Mark, S., Baram, A.B., Stachenfeld, K.L., and Kurth-Nelson, Z. (2018). What is a cognitive map? organizing knowledge for flexible behavior. Neuron 100, 490–509. 

25. Hummel, J.E., and Holyoak, K.J. (2003). A symbolic-connectionist theory of relational inference and generalization. Psychol. Rev. 110, 220–264. 

26. Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. Artif. Intell. 46, 159–216. 

27. Goodale, M.A., and Milner, A.D. (1992). Separate visual pathways for perception and action. Trends Neurosci. 15, 20–25. 

28. Keene, C.S., Bladon, J., McKenzie, S., Liu, C.D., O’Keefe, J., and Eichenbaum, H. (2016). Complementary functional organization of neuronal activity patterns in the perirhinal, lateral entorhinal, and medial entorhinal cortices. J. Neurosci. 36, 3660–3675. 

29. Knierim, J.J., Lee, I., and Hargreaves, E.L. (2006). Hippocampal place cells: parallel input streams, subregional processing, and implications for episodic memory. Hippocampus 16, 755–764. 

30. Manns, J.R., and Eichenbaum, H. (2006). Evolution of declarative memory. Hippocampus 16, 795–808. 

Neuron 111, February 15, 2023 465 

## **ll** 

## Perspective 

31. Komorowski, R.W., Manns, J.R., and Eichenbaum, H. (2009). Robust conjunctive item–place coding by hippocampal neurons parallels learning what happens where. J. Neurosci. 29, 9918–9929. 

32. Whittington, J.C.R., Muller, T.H., Mark, S., Chen, G., Barry, C., Burgess, N., and Behrens, T.E.J. (2020). The tolman-eichenbaum machine: unifying space and relational memory through generalization in the hippocampal formation. Cell 183, 1249–1263.e23. 

33. Høydal, Ø.A., Skytøen, E.R., Andersson, S.O., Moser, M.B., and Moser, E.I. (2019). Object-vector coding in the medial entorhinal cortex. Nature 568, 400–404. 

34. Deshmukh, S.S., and Knierim, J.J. (2013). Influence of local objects on hippocampal representations: landmark vectors and memory. Hippocampus 23, 253–267. 

35. Sun, C., Yang, W., Martin, J., and Tonegawa, S. (2020). Hippocampal neurons represent events as transferable units of experience. Nat. Neurosci. 23, 651–663. 

36. Aronov, D., Nevers, R., and Tank, D.W. (2017). Mapping of a non-spatial dimension by the hippocampal–entorhinal circuit. Nature 543, 719–722. 

37. Bongioanni, A., Folloni, D., Verhagen, L., Sallet, J., Klein-Flugge,€ M.C., and Rushworth, M.F.S. (2021). Activation and disruption of a neural mechanism for novel choice in monkeys. Nature 591, 270–274. 

38. Constantinescu, A.O., O’Reilly, J.X., and Behrens, T.E.J. (2016). Organizing conceptual knowledge in humans with a gridlike code. Science 352, 1464–1468. 

39. Killian, N.J., Jutras, M.J., and Buffalo, E.A. (2012). A map of visual space in the primate entorhinal cortex. Nature 491, 761–764. 

40. Tavares, R.M., Mendelsohn, A., Grossman, Y., Williams, C.H., Shapiro, M., Trope, Y., and Schiller, D. (2015). A map for social navigation in the human brain. Neuron 87, 231–243. 

41. Cohen, N.J., and Eichenbaum, H. (1993). Memory, Amnesia, and the Hippocampal System (MIT Press). 

42. Tolman, E.C. (1948). Cognitive maps in rats and men. Psychol. Rev. 55, 189–208. 

43. MacDonald, C.J., Lepage, K.Q., Eden, U.T., and Eichenbaum, H. (2011). Hippocampal "time cells" bridge the gap in memory for discontiguous events. Neuron 71, 737–749. 

44. Wood, E.R., Dudchenko, P.A., and Eichenbaum, H. (1999). The global record of memory in hippocampal neuronal activity. Nature 397, 613–616. 

45. Liu, Y., Dolan, R.J., Kurth-Nelson, Z., and Behrens, T.E.J. (2019). Human replay spontaneously reorganizes experience. Cell 178, 640–652.e14. 

46. Fyhn, M., Hafting, T., Treves, A., Moser, M.B., and Moser, E.I. (2007). Hippocampal remapping and grid realignment in entorhinal cortex. Nature 446, 190–194. 

47. Stachenfeld, K.L., Botvinick, M.M., and Gershman, S.J. (2017). The hippocampus as a predictive map. Nat. Neurosci. 20, 1643–1653. 

48. Buzsa´ ki, G., and Tingley, D. (2018). Space and time: the hippocampus as a sequence generator. Trends Cogn. Sci. 22, 853–869. 

49. Battaglia, P.W., Hamrick, J.B., Bapst, V., Sanchez-Gonzalez, A., Zambaldi, V., Malinowski, M., Tacchetti, A., Raposo, D., Santoro, A., Faulkner, R., et al. Relational inductive biases, deep learning, and graph networks. Preprint at arXiv, ArXiv:1806.01261. 

50. Buzsa´ ki, G. (2010). Neural syntax: cell assemblies, synapsembles, and readers. Neuron 68, 362–385. 

51. Goodman, N.D., Tenenbaum, J.B., and Gerstenberg, T. (2014). Concepts in a Probabilistic Languageof Thought (Center for Brains, Minds and Machines). Technical report. 

52. Van der Velde, F., and De Kamps, M. (2006). Neural blackboard architectures of combinatorial structures in cognition. Behav. Brain Sci. 29, 37–70 discussion 70. 

53. Zeithamova, D., Schlichting, M.L., and Preston, A.R. (2012). The hippocampus and inferential reasoning: building memories to navigate future decisions. Front. Hum. Neurosci. 6, 70. 

54. Buckner, R.L. (2010). The role of the hippocampus in prediction and imagination. Annu. Rev. Psychol. 61, 27–48. 

55. Frankland, S.M., and Greene, J.D. (2020). Concepts and compositionality: in search of the brain’s language of thought. Annu. Rev. Psychol. 71, 273–303. 

56. Hassabis, D., Kumaran, D., Vann, S.D., and Maguire, E.A. (2007). Patients with hippocampal amnesia cannot imagine new experiences. Proc. Natl. Acad. Sci. USA 104, 1726–1731. 

57. Newell, A., Shaw, J.C., and Simon, H.A. (1958). Elements of a theory of human problem solving. Psychol. Rev. 65, 151–166. 

58. Tsividis, P.A., Loula, J., Burga, J., Foss, N., Campero, A., Pouncy, T., Gershman, S.J., and Tenenbaum, J.B. (2021). Human-level reinforcement learning through theory-based modeling, exploration, and planning. Preprint at arXiv. arXiv:2107.12544. 

59. Hung, C.C., Lillicrap, T., Abramson, J., Wu, Y., Mirza, M., Carnevale, F., Ahuja, A., and Wayne, G. (2019). Optimizing agent behavior over long time scales by transporting value. Nat. Commun. 10, 5223. 

60. Pfeiffer, B.E., and Foster, D.J. (2015). PLACE CELLS. Autoassociative dynamics in the generation of sequences of hippocampal place cells. Science 349, 180–183. 

61. Kurth-Nelson, Z., Economides, M., Dolan, R.J., and Dayan, P. (2016). Fast sequences of non-spatial state representations in humans. Neuron 91, 194–204. 

62. Schwartenbeck, P., Baram, A., Liu, Y., Mark, S., Muller, T., Dolan, R., Botvinick, M., Kurth-Nelson, Z., and Behrens, T. (2021). Generative replay for compositional visual understanding in the prefrontal-hippocampal circuit. SSRN Journal. 

63. Leutgeb, J.K., Leutgeb, S., Moser, M.B., and Moser, E.I. (2007). Pattern separation in the dentate gyrus and ca3 of the hippocampus. Science 315, 961–966. 

64. Treves, A., and Rolls, E.T. (1994). Computational analysis of the role of the hippocampus in memory. Hippocampus 4, 374–391. 

65. Yassa, M.A., and Stark, C.E. (2011). Pattern separation in the hippocampus. Trends Neurosci. 34, 515–525. 

66. Harris, K.D., Csicsvari, J., Hirase, H., Dragoi, G., and Buzsa´ ki, G. (2003). Organization of cell assemblies in the hippocampus. Nature 424, 552–556. 

67. Lisman, J.E., and Idiart, M.A. (1995). Storage of 7±2 short-term memories in oscillatory subcycles. Science 267, 1512–1515. 

68. Lisman, J.E., and Jensen, O. (2013). The theta-gamma neural code. Neuron 77, 1002–1016. 

69. Kay, K., Chung, J.E., Sosa, M., Schor, J.S., Karlsson, M.P., Larkin, M.C., Liu, D.F., and Frank, L.M. (2020). Constant sub-second cycling between representations of possible futures in the hippocampus. Cell 180, 552– 567.e25. 

70. Wikenheiser, A.M., and Redish, A.D. (2015). Hippocampal theta sequences reflect current goals. Nat. Neurosci. 18, 289–294. 

71. Dragoi, G., and Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. Nature 469, 397–401. 

72. O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2016). Coordinated grid and place cell replay during rest. Nat. Neurosci. 19, 792–794. 

73. Zhou, J., Montesinos-Cartagena, M., Wikenheiser, A.M., Gardner, M.P.H., Niv, Y., and Schoenbaum, G. (2019). Complementary task structure representations in hippocampus and orbitofrontal cortex during an odor sequence task. Curr. Biol. 29, 3402–3409.e3. 

74. Eichenbaum, H. (2014). Time cells in the hippocampus: a new dimension for mapping memories. Nat. Rev. Neurosci. 15, 732–744. 

466 Neuron 111, February 15, 2023 

## Perspective 

75. Allen, T.A., Salz, D.M., McKenzie, S., and Fortin, N.J. (2016). Nonspatial sequence coding in ca1 neurons. J. Neurosci. 36, 1547–1563. 

76. Nieh, E.H., Schottdorf, M., Freeman, N.W., Low, R.J., Lewallen, S., Koay, S.A., Pinto, L., Gauthier, J.L., Brody, C.D., and Tank, D.W. (2021). Geometry of abstract learned knowledge in the hippocampus. Nature 595, 80–84. 

77. Teyler, T.J., and Rudy, J.W. (2007). The hippocampal indexing theory and episodic memory: updating the index. Hippocampus 17, 1158–1169. 

78. Engel, A.K., and Singer, W. (2001). Temporal binding and the neural correlates of sensory awareness. Trends Cogn. Sci. 5, 16–25. 

79. Hummel, J.E., and Biederman, I. (1992). Dynamic binding in a neural network for shape recognition. Psychol. Rev. 99, 480–517. 

80. Silva, D., Feng, T., and Foster, D.J. (2015). Trajectory events across hippocampal place cells require previous experience. Nat. Neurosci. 18, 1772–1779. 

81. Dehaene, S., Al Roumi, F.A.l., Lakretz, Y., Planton, S., and Sable´ -Meyer, M. (2022). Symbols and mental programs: a hypothesis about human singularity. Trends Cogn. Sci. 26, 751–766. 

82. Luyckx, F., Nili, H., Spitzer, B., and Summerfield, C. (2019). Neural structure mapping in human probabilistic reward learning. eLife 8, e42816. 

83. Ujfalussy, B.B., and Orban, G. (2021). Sampling motion trajectories during hippocampal theta sequences. Preprint at bioRxiv. https://doi.org/ 10.1101/2021.12.14.472575. 

84. Jadhav, S.P., Kemere, C., German, P.W., and Frank, L.M. (2012). Awake hippocampal sharp-wave ripples support spatial memory. Science 336, 1454–1458. 

85. Singer, A.C., Carr, M.F., Karlsson, M.P., and Frank, L.M. (2013). Hippocampal swr activity predicts correct decisions during the initial learning of an alternation task. Neuron 77, 1163–1173. 

86. Van Der Meer, M.A., and Redish, A.D. (2009). Covert expectation-ofreward in rat ventral striatum at decision points. Front. Integr. Neurosci. 3, 1. 

87. Hills, T.T., Todd, P.M., Lazer, D., Redish, A.D., and Couzin, I.D.; Cognitive Search Research Group (2015). Exploration versus exploitation in space, mind, and society. Trends Cogn. Sci. 19, 46–54. 

88. Hopfield, J.J. (2010). Neurodynamics of mental exploration. Proc. Natl. Acad. Sci. USA 107, 1648–1653. 

89. Hunt, L.T., Daw, N.D., Kaanders, P., MacIver, M.A., Mugan, U., Procyk, E., Redish, A.D., Russo, E., Scholl, J., Stachenfeld, K., et al. (2021). Formalizing planning and information search in naturalistic decisionmaking. Nat. Neurosci. 24, 1051–1064. 

90. Berkes, P., Orba´ n, G., Lengyel, M., and Fiser, J. (2011). Spontaneous cortical activity reveals hallmarks of an optimal internal model of the environment. Science 331, 83–87. 

91. Buesing, L., Bill, J., Nessler, B., and Maass, W. (2011). Neural dynamics as sampling: a model for stochastic computation in recurrent networks of spiking neurons. PLoS Comp. Biol. 7, e1002211. 

92. Echeveste, R., Aitchison, L., Hennequin, G., and Lengyel, M. (2020). Cortical-like dynamics in recurrent circuits optimized for sampling-based probabilistic inference. Nat. Neurosci. 23, 1138–1149. 

93. Griffiths, T.L., Vul, E., and Sanborn, A.N. (2012). Bridging levels of analysis for probabilistic models of cognition. Curr. Dir. Psychol. Sci. 21, 263–268. 

94. Orba´ n, G., Berkes, P., Fiser, J., and Lengyel, M. (2016). Neural variability and sampling-based probabilistic representations in the visual cortex. Neuron 92, 530–543. 

95. Rich, E.L., and Wallis, J.D. (2016). Decoding subjective decisions from orbitofrontal cortex. Nat. Neurosci. 19, 973–980. 

96. O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2017). Task demands predict a dynamic switch in the content of awake hippocampal replay. Neuron 96, 925–935.e6. 

## **ll** 

97. Daw, N.D., and Dayan, P. (2014). The algorithmic anatomy of modelbased evaluation. Philos. Trans. R. Soc. Lond. B Biol. Sci. 369, 20130478. 

98. Eldar, E., Lie` vre, G., Dayan, P., and Dolan, R.J. (2020). The roles of online and offline replay in planning. eLife 9, e56911. 

99. McNaughton, B.L., Battaglia, F.P., Jensen, O., Moser, E.I., and Moser, M.B. (2006). Path integration and the neural basis of the ‘cognitive map’. Nat. Rev. Neurosci. 7, 663–678. 

100. Griffiths, T.L., Chater, N., Kemp, C., Perfors, A., and Tenenbaum, J.B. (2010). Probabilistic models of cognition: exploring representations and inductive biases. Trends Cogn. Sci. 14, 357–364. 

101. McClelland, J.L., Botvinick, M.M., Noelle, D.C., Plaut, D.C., Rogers, T.T., Seidenberg, M.S., and Smith, L.B. (2010). Letting structure emerge: connectionist and dynamical systems approaches to cognition. Trends Cogn. Sci. 14, 348–356. 

102. McNamee, D.C., Stachenfeld, K.L., Botvinick, M.M., and Gershman, S.J. (2021). Flexible modulation of sequence generation in the entorhinal– hippocampal system. Nat. Neurosci. 24, 851–862. 

103. Harnad, S. (1990). The symbol grounding problem. Phys. D: Nonlinear Phenom. 42, 335–346. 

104. Ka´ li, S., and Dayan, P. (2004). Off-line replay maintains declarative memories in a model of hippocampalneocortical interactions. Nat. Neurosci. 7, 286–294. 

105. Bendor, D., and Wilson, M.A. (2012). Biasing the content of hippocampal replay during sleep. Nat. Neurosci. 15, 1439–1444. 

106. Rothschild, G., Eban, E., and Frank, L.M. (2017). A cortical–hippocampal–cortical loop of information processing during memory consolidation. Nat. Neurosci. 20, 251–259. 

107. Ji, D., and Wilson, M.A. (2007). Coordinated memory replay in the visual cortex and hippocampus during sleep. Nat. Neurosci. 10, 100–107. 

108. Xu, H., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). Assembly responses of hippocampal ca1 place cells predict learned behavior in goal-directed spatial tasks on the radial eight-arm maze. Neuron 101, 119–132.e4. 

109. McCormick, C., Barry, D.N., Jafarian, A., Barnes, G.R., and Maguire, E.A. (2020). vmPFC Drives Hippocampal Processing during Autobiographical Memory Recall Regardless of Remoteness. Cereb. Cortex 30, 5972–5987. 

110. Moscovitch, M. (1992). Memory and working-with-memory: A component process model based on modules and central systems. J. Cogn. Neurosci. 4, 257–267. 

111. Girardeau, G., Benchenane, K., Wiener, S.I., Buzsa´ ki, G., and Zugaro, M.B. (2009). Selective suppression of hippocampal ripples impairs spatial memory. Nat. Neurosci. 12, 1222–1223. 

112. Silver, D., Huang, A., Maddison, C.J., Guez, A., Sifre, L., Van Den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., et al. (2016). Mastering the game of go with deep neural networks and tree search. Nature 529, 484–489. 

113. Squire, L.R., and Alvarez, P. (1995). Retrograde amnesia and memory consolidation: a neurobiological perspective. Curr. Opin. Neurobiol. 5, 169–177. 

114. Squire, L.R., Genzel, L., Wixted, J.T., and Morris, R.G. (2015). Memory consolidation. Cold Spring Harbor Perspect. Biol. 7, a021766. 

115. Inostroza, M., and Born, J. (2013). Sleep for preserving and transforming episodic memory. Annu. Rev. Neurosci. 36, 79–102. 

116. O’Reilly, R.C., and Rudy, J.W. (2001). Conjunctive representations in learning and memory: principles of cortical and hippocampal function. Psychol. Rev. 108, 311–345. 

117. O’Reilly, R.C., Bhattacharyya, R., Howard, M.D., and Ketz, N. (2014). Complementary learning systems. Cogn. Sci. 38, 1229–1248. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, February 15, 2023 467 

## **ll** 

## Perspective 

118. Saxe, A.M., McClelland, J.L., and Ganguli, S. (2019). A mathematical theory of semantic development in deep neural networks. Proc. Natl. Acad. Sci. USA 116, 11537–11546. 

119. Battaglia, F.P., and Pennartz, C.M. (2011). The construction of semantic memory: grammar-based representations learned from relational episodic information. Front. Comp. Neurosci. 5, 36. 

120. Battaglia, F.P., Borensztajn, G., and Bod, R. (2012). Structured cognition and neural systems: from rats to language. Neurosci. Biobehav. Rev. 36, 1626–1639. 

121. Antonov, G., Gagne, C., Eldar, E., and Dayan, P. (2022). Optimism and pessimism in optimised replay. PLoS Comp. Biol. 18, e1009634. 

122. Barry, D.N., and Love, B.C. (2021). A neural network account of memory replay and knowledge consolidation. Preprint at bioRxiv. https://doi.org/ 10.1101/2021.05.25.445587. 

123. Deperrois, N., Petrovici, M.A., Senn, W., and Jordan, J. (2022). Learning cortical representations through perturbed and adversarial dreaming. eLife 11, e76384. 

124. Liu, Y., Mattar, M.G., Behrens, T.E.J., Daw, N.D., and Dolan, R.J. (2021). Experience replay is associated with efficient nonlocal learning. Science 372, eabf1357. 

125. Sun, W., Advani, M., Spruston, N., Saxe, A., and Fitzgerald, J.E. (2021). Organizing memories for generalization in complementary learning systems. Preprint at bioRxiv. https://doi.org/10.1101/2021.10.13.463791. 

126. van Hasselt, H.P., Hessel, M., and Aslanides, J. (2019). When to use parametric models in reinforcement learning? Adv. Neural Inf. Process. Syst. 32, 14322–14333. 

127. Lewis, P.A., Knoblich, G., and Poe, G. (2018). How memory replay in sleep boosts creative problemsolving. Trends Cogn. Sci. 22, 491–503. 

128. Tse, D., Langston, R.F., Kakeyama, M., Bethus, I., Spooner, P.A., Wood, E.R., Witter, M.P., and Morris, R.G. (2007). Schemas and memory consolidation. Science 316, 76–82. 

129. Berners-Lee, A., Wu, X., and Foster, D.J. (2021). Prefrontal cortical neurons are selective for non-local hippocampal representations during replay and behavior. J. Neurosci. 41, 5894–5908. 

130. Hassabis, D., Kumaran, D., Summerfield, C., and Botvinick, M. (2017). Neuroscience-inspired artificial intelligence. Neuron 95, 245–258. 

131. Lin, L.J. (1991). Programming robots using reinforcement learning and teaching. In AAAI’91: Proceedings of the ninth National conference on Artificial intelligence, pp. 781–786. 

132. Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.A., Veness, J., Bellemare, M.G., Graves, A., Riedmiller, M., Fidjeland, A.K., Ostrovski, G., et al. (2015). Human-level control through deep reinforcement learning. Nature 518, 529–533. 

133. Shin, H., Lee, J.K., Kim, J., and Kim, J. (2017). Continual learning with deep generative replay. In Advances in Neural Information Processing Systems (Curran Associates, Inc.). 

134. Kell, A.J.E., Yamins, D.L.K., Shook, E.N., Norman-Haignere, S.V., and McDermott, J.H. (2018). A task-optimized neural network replicates human auditory behavior, predicts brain responses, and reveals a cortical processing hierarchy. Neuron 98, 630–644.e16. 

135. Mante, V., Sussillo, D., Shenoy, K.V., and Newsome, W.T. (2013). Context-dependent computation by recurrent dynamics in prefrontal cortex. Nature 503, 78–84. 

136. Sussillo, D., Churchland, M.M., Kaufman, M.T., and Shenoy, K.V. (2015). A neural network that finds a naturalistic solution for the production of muscle activity. Nat. Neurosci. 18, 1025–1033. 

137. Yamins, D.L., Hong, H., Cadieu, C.F., Solomon, E.A., Seibert, D., and DiCarlo, J.J. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex. Proc. Natl. Acad. Sci. 111, 8619–8624. 

138. Lake, B.M., Ullman, T.D., Tenenbaum, J.B., and Gershman, S.J. (2017). Building machines that learn and think like people. Behav. Brain Sci. 40, e253. 

139. Diuk, C., Cohen, A., and Littman, M.L. (2008). An object-oriented representation for efficient reinforcement learning. In Proceedings of the 25th International Conference on Machine Learning, pp. 240–247. 

140. Ellis, K., Wong, C., Nye, M., Sable´ -Meyer, M., Morales, L., Hewitt, L., Cary, L., Solar-Lezama, A., and Tenenbaum, J.B. (2021). Dreamcoder: bootstrapping inductive program synthesis with wakesleep library learning. In Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation, pp. 835–850. 

141. Mao, J., Gan, C., Kohli, P., Tenenbaum, J.B., and Wu, J. The neuro-symbolic concept learner: interpreting scenes, words, and sentences from natural supervision. Preprint at arXiv, arXiv:1904.12584. 

142. Kalyan, A., Mohta, A., Polozov, O., Batra, D., Jain, P., and Gulwani, S. Neural-guided deductive search for real-time program synthesis from examples. Preprint at arXiv, arXiv:1804.01186. 

143. Parisotto, E., Mohamed, A.-r., Singh, R., Li, L., Zhou, D., and Kohli, P. Neuro-symbolic program synthesis. Preprint at arXiv, arXiv:1611.01855. 

144. Hamrick, J.B., Bapst, V., Sanchez-Gonzalez, A., Pfaff, T., Weber, T., Buesing, L., and Battaglia, P.W. (2019). Combining q-learning and search with amortized value estimates. Preprint at arXiv. arXiv:1912.02807. 

145. Guez, A., Mirza, M., Gregor, K., Kabra, R., Racaniere, S., Weber, T., Raposo, D., Santoro, A., Orseau, L., Eccles, T., et al. (2019). An investigation of model-free planning. In International Conference on Machine Learning, pp. 2464–2473. 

146. Ortega, P.A., Wang, J.X., Rowland, M., Genewein, T., Kurth-Nelson, Z., Pascanu, R., Heess, N., Veness, J., Pritzel, A., Sprechmann, P., et al. Meta-learning of sequential strategies. Preprint at arXiv, arXiv:1905. 03030. 

147. Wang, J.X., Kurth-Nelson, Z., Kumaran, D., Tirumala, D., Soyer, H., Leibo, J.Z., Hassabis, D., and Botvinick, M. (2018). Prefrontal cortex as a meta-reinforcement learning system. Nat. Neurosci. 21, 860–868. 

148. Schrittwieser, A., Antonoglou, I., Hubert, T., Simonyan, K., Sifre, L., Schmitt, S., Guez, A., Lock-hart, D., Hassabis, T., Graepel, T., et al. (2020). Mastering atari, go, chess and shogi by planning with a learned model. Nature 588, 604–609. 

149. Bahdanau, D., Cho, K., and Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. Preprint at arXiv. arXiv:1409.0473. 

150. Graves, A., Wayne, G., and Danihelka, I. (2014). Neural turing machines. Preprint at arXiv. arXiv:1410.5401. 

151. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., and Polosukhin, I. (2017). Attention is all you need. In Advances in Neural Information Processing Systems, pp. 5998–6008. 

152. Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901. 

153. Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O.,(2021).Tunyasuvunakool,Highly accurateK.,proteinBates,structureR., Zıdek,predictionA., Potapenko,with�alphafold.A., etNa-al. ture 596, 583–589. 

154. Vinyals, O., Babuschkin, I., Czarnecki, W.M., Mathieu, M., Dudzik, A., Chung, J., Choi, D.H., Powell, R., Ewalds, T., Georgiev, P., et al. (2019). Grandmaster level in starcraft ii using multi-agent reinforcement learning. Nature 575, 350–354. 

155. Botvinick, M., and Watanabe, T. (2007). From numerosity to ordinal rank: a gain-field model of serial order representation in cortical working memory. J. Neurosci. 27, 8636–8642. 

468 Neuron 111, February 15, 2023 

## Perspective 

156. O’Reilly, R.C., and Frank, M.J. (2006). Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia. Neural Comput. 18, 283–328. 

157. Schlag, I., Irie, K., and Schmidhuber, J. (2021). Linear transformers are secretly fast weight programmers. In International Conference on Machine Learning, pp. 9355–9366. 

158. Whittington, J.C., Warren, J., and Behrens, T.E. (2021). Relating transformers to models and neural representations of the hippocampal formation. Preprint at arXiv. arXiv:2112.04035. 

159. Lake, B.M., and Murphy, G.L. (2021). Word meaning in minds and machines. Psychol. Rev. https://doi.org/10.1037/rev0000297. 

160. Marcus, G., and Davis, E. (2020). Gpt-3, bloviator: Openai’s language generator has no idea what it’s talking about. MIT Technol. Rev. 

## **ll** 

https://www.technologyreview.com/2020/08/22/1007539/gpt3-openailanguage-generator-artificial-intelligence-ai-opinion/. 

161. Kitadai, N., and Maruyama, S. (2018). Origins of building blocks of life: a review. Geosci. Front. 9, 1117–1153. 

162. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., and Salakhutdinov, R. (2014). Dropout: a simple way to prevent neural networks from overfitting. J. Mach. Learn. Res. 15, 1929–1958. 

163. Zador, A.M. (2019). A critique of pure learning and what artificial neural networks can learn from animal brains. Nat. Commun. 10, 3770. 

164. Stanley, K.O., Lehman, J., and Soros, L. (2017). Open-Endedness: the Last Grand Challenge You’ve Never Heard Of (O’Reilly). 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 111, February 15, 2023 469 

