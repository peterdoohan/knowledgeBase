## Replay and compositional computation 

Zeb Kurth-Nelson[1] _[,]_[2] , Timothy Behrens[3] _[,]_[4] , Greg Wayne[1] , Kevin Miller[1] _[,]_[5] , Lennart Luettgau[2] , Ray Dolan[2] _[,]_[3] , Yunzhe Liu[6,7] , Philipp Schwartenbeck[8,9] 

1DeepMind, London, UK 

2Max Planck UCL Centre for Computational Psychiatry and Ageing Research, London, UK 

3Wellcome Centre for Human Neuroimaging, University College London, London, UK 

4Wellcome Centre for Integrative Neuroimaging, University of Oxford, Oxford, UK 

5Institute of Ophthalmology, University College London, London, UK 

6State Key Laboratory of Cognitive Neuroscience and Learning, IDG/McGovern Institute for Brain Research, Beijing Normal University, Beijing, China 

7Chinese Institute for Brain Research, Beijing, China 

8Max Planck Institute for Biological Cybernetics, Tubingen, Germany 

9University of Tubingen, Tubingen, Germany 

It is still a mystery how the human brain radically generalizes from previous experiences to solve new problems with very little data, an ability that far surpasses deep learning. Here, we propose a speculative hypothesis: that ‘replay’ in the brain implements a form of compositional computation where entities are assembled into meaningful structures. We review recent advances in the neuroscience of replay, highlighting how the hippocampus flexibly binds objects to generalizable roles and how replay strings these role-bound objects into compound statements. We suggest new experiments to test this hypothesis. We end by noting the bidirectional interactions between replay and other brain systems and their relationship to AI methods that hybridize neural networks with compositional computation. 

Replay in the brain was discovered in the context of spatial experiments on rodents. While the animal is moving, hippocampal neurons encode its current location in space. But when the animal rests or pauses, researchers noticed that the same neurons sometimes spontaneously sweep through a sequence of firing patterns which repeat a path the animal recently traversed through space, at an accelerated rate (Louie and Wilson, 2001; Nadasdy et al., 1999; Skaggs and McNaughton, 1996). The phenomenon was fittingly termed ‘replay’, and is a major component of hippocampal function, comprising a large fraction of all spikes at rest (Buzsaki, 1989, 2015). It was hypothesized that hippocampus rapidly stores new experiences, and that replay is rehearsal to transfer this knowledge into a stabler form in cortex (McClelland et al., 1995; Wilson and McNaughton, 1994), a process called consolidation. 

However, over the past 20 years, our understanding of replay in the brain has grown. Although early experiments found replay sequences that directly repeat past experience, it gradually became clear that this is a special case of a much broader phenomenon. For example, Gupta et al. (2010) measured replay sequences in rats who had experience running in a T-shaped maze. The animals always ran north up the central corridor and turned left or right at the T-junction. At rest, replay sequences traversed the entire width of the east-west corridor, stitching together 

1 

segments of space that had only been experienced separately. Replay even synthesizes entirely novel sequences. In the experiment of Pfeiffer and Foster (2013), rats alternated between searching an open 2D environment for a randomly placed reward, and returning ‘home’ (a fixed location) for another reward. The home location changed each day, creating many possible combinations of random location and home location. Spontaneous replay sequences formed trajectories ahead of the animal, predicting its future path, and this was true even when that particular path had never been physically traversed before. Similarly, when barriers are moved dynamically in a 2D environment, replay sequences quickly adapt to play trajectories that route around the new barrier locations (Widloski and Foster, 2022). When the only behavioral task is unstructured random foraging in an open environment, replays at rest play out diffusion-like trajectories which were never followed by the animal (Stella et al., 2019). Most remarkably, replays can traverse areas of space that have never been visited. When rats are given full view but only partial access to a maze, and food is dropped into the inaccessible part, replay sequences spontaneously represent trajectories into the inaccessible part that has never physically been visited (Olafsdottir et al., 2015). 

In light of an accumulating body of such data, the predominant view in neuroscience is now that sequences are not constrained to simply repeat past experience, but are informed by an internal model of the world (Dudai, 2012; Foster, 2017; Olafsdottir et al., 2018; Pezzulo et al., 2014; Roscow et al., 2021; Wittkuhn et al., 2021). The use of an internal model opens the door for replay to describe hypothetical scenarios based on the causal structure of the world (Behrens et al., 2018; Pearl, 2009; Sutton and Barto, 1998). This model could be used for online control of behavior (‘planning’) (Johnson and Redish, 2007; Olafsdottir et al., 2018; Pfeiffer and Foster, 2013) and for offline simulation to train a policy or value function (like ‘Dyna’) (Johnson and Redish, 2005; Mattar and Daw, 2018; Mattar and Lengyel, 2022; Sutton, 1991). 

## **A new conjecture** 

The goal of this paper is to propose another update to how we think about replay. Our proposal is that replay in the brain instantiates a form of compositional computation. We will argue that a replay sequence constitutes a set of entities strung together into a compound. Each entity is transiently bound to a representation of its role in the compound, which specifies how that element functions as a part of the whole. Thus, the replay sequence as a whole describes a complicated structure whose meaning is more than the sum of its parts. Composing entities in this way allows replay to derive new knowledge. For example, if it is already known that _p > q_ and _q > r_ , then a replay sequence could derive the implication that _p > r_ . This is a speculative hypothesis, but it is a natural extension of recent neuroscientific discoveries about replay, which we will review. We will also offer experiments to test several predictions of the idea. 

The replay we envisage is built on two types of composability (Figure 1). The first type is a separation between entity and role (or, semantics and syntax): new entities can be bound to existing roles and vice versa. The second type is that there are many ways to arrange role-bound entities into compounds (sequences), creating a potentially infinite space of compounds from a smaller number of elements. We will use the idea of these two types of composability to organize the following sections. 

2 

Figure 1 

b 

a 

## A statement: 

“I am driving home from the airport” **`I subject I as subject driving action driving as action airport start point airport as start point home end point home as end point entities roles conjunctions`** 

First type of composability: Binding a new entity to an existing role 

## Encoded as a replay sequence 

c 

**`end point home home as end point aquar`** ~~**`ium`**~~ **`start point aquarium as start point start point airport airport as start point`** d **`action`** Second type of composability: Recombining role-bound entities to generate a new statement **`driving driving as action subject a fish’s life subject a fish’s life as subject I I as subject aquarium start point aquarium as start point`** Time 

Our view agrees with the notion that replay draws on an internal model. However, in previous model-based accounts of replay, a replay event is a ‘rollout’: a sequence of states predicted to occur sequentially in the world, with the model defining the transition probabilities between successive states. Our hypothesis relaxes this constraint, so that items in a replay event need not be successive states, but instead may have a more general set of relationships to one another. Our hypothesis also relaxes the constraint that replays are used for online control of behavior or for updating a policy or value function. Instead, we suggest that replays can be used to derive new knowledge about the world by reasoning about the implications of combining existing pieces of knowledge. To forestall misunderstanding, our conjecture is not that all replay sequences are best conceived as compositional computation. In simpler settings, replay does appear to recapitulate experience or to perform rollouts. Rather, we suggest that the machinery of replay – which likely evolved to solve simpler problems – gives rise to compositional computation when coupled with learning mechanisms and rich environments, particularly in humans. 

## **Binding entities to generalizable roles in hippocampus** 

The first type of composability is binding new entities (role-fillers) to existing roles or vice versa (Behrens et al., 2018; Hummel and Holyoak, 2003; Smolensky, 1990). In the example of Figure 1, the entity _airport_ takes the role of _start point_ , as part of a compound meaning ‘I’m driving home from the airport’. The same role attached to a new entity, _aquarium_ , would immediately have a different but interpretable meaning (‘aquarium as start point’) and could be used to make new compounds. 

Our perspective is that hippocampus has a general-purpose ability to bind entities to roles. This is an unproven idea, but experimental data from humans and animals make it an exciting possibility. We discuss these data in terms of three potential levels of generality of roles. At the first level, roles are constrained to be spatial (where something is relative to other things). At the second level, roles can be nonspatial but adhere to the Euclidean geometry of space (for example, a coordinate in the 1D space of auditory pitch). At the third level, roles can be nonspatial and non-Euclidean, potentially including arbitrary roles like _start point_ or _verb_ . 

The large hippocampal literature in animals has studied primarily spatial roles. Hippocampus receives converging input from the brain’s ‘what’ stream (through lateral entorhinal cortex) and ‘where’ stream (through medial entorhinal cortex) (Goodale and Milner, 1992; Keene et al., 2016; Knierim et al., 2006; Manns and Eichenbaum, 2006). The ‘what’ stream carries representations that discriminate between different objects or sensory details but are invariant to how they are arranged in space. The ‘where’ stream carries an abstract representation of space itself, providing a coordinate system that describes relative positions. These two streams combine in hippocampus to form conjunctive codes, where the abstraction of space is joined with sensory specifics to code for a particular place or memory (Figure 2a). The rodent spatial literature thus offers extensive evidence that hippocampal representations act as role-bound entities at the first level of generality – the special case of spatial relations. 

Newer experiments, in both humans and non-human animals, have started to broaden our understanding of the ‘where’ pathway beyond physical space. Experimental data from the past 

3 

Figure 2 

b 

a 

## **‘what’ cortical pathway** 

## **‘where’ cortical pathway** 

**==> picture [151 x 83] intentionally omitted <==**

**==> picture [151 x 83] intentionally omitted <==**

**==> picture [318 x 84] intentionally omitted <==**

**==> picture [725 x 301] intentionally omitted <==**

**----- Start of picture text -----**<br>
lateral medial<br>entorhinal entorhinal<br>cortex (LEC) cortex (MEC) c<br>hippocampus (HC)<br>**----- End of picture text -----**<br>


decade (Aronov et al., 2017; Bongioanni et al., 2021; Constantinescu et al., 2016; Killian et al., 2012; Tavares et al., 2015), aligning with older theories (Cohen and Eichenbaum, 1993; Tolman, 1948), suggest that the ‘where’ pathway carries information about nonspatial relational roles, ranging from social relationships to auditory pitch to configural stimulus spaces. Theory implies these roles can be arbitrarily rich because they derive from learning algorithms operating on the real world (Behrens et al., 2018; Stachenfeld et al., 2017; Whittington et al., 2020). So far, experiments with nonspatial relations have mostly been limited to the second level of generality – Euclidean topologies such as 2D social relationships and 1D auditory pitch. 

However, there are hints that roles may even go beyond Euclidean to the third level of generality. One point of supporting data is that non-Euclidean role representations appear in replay in humans (Liu et al., 2019), which we discuss in more detail in the next section. Another piece of evidence comes from the representation of discrete states in rodent hippocampus. In a task where a mouse had to complete four laps of a loop before reward became available (Sun et al., 2020), hippocampal cells responded (as usual) at selective places in the lap. Some of these place cells were also ‘lap cells’: they responded on a particular lap. When the animal was asked to do the same task on a maze with different sensory cues, place cells that were not lap cells exhibited spatial remapping as usual (Fyhn et al., 2007) (Figure 2b). Lap cells also changed their spatial tunings, but crucially they always fired on the same lap in both mazes (Figure 2c). This is exactly what is predicted by a system that has roles for spatial location and lap number, and fills them with the sensory particularities of each individual maze (Whittington et al., 2020). The different sensory input along each maze shifts the conjunctive cells in space, but this mechanism can never shift a cell between laps because each lap has the identical sensory input. Indeed, this same mechanism also explains open-field remapping experiments, where place cells preferentially remap to different peaks of the same grid cells. By remapping, but staying at the same grid phase, a single place cell preserves its role input across different situations. Alternate accounts of these data, such as predicting reward or representing total distance travelled, are difficult to reconcile with the fact that they shift at random between different spatial locations (and different distances from the reward) in the two mazes. 

These hints of non-Euclidean role representations are limited to coding for an index within a sequence (Sun et al. (2020) and ‘position’ codes in Liu et al. (2019)) or for a binary category (‘sequence’ codes in Liu et al. (2019)). Future experiments are needed to probe a broader spectrum of roles, like _verb_ . Even if rodents represent some kinds of non-Euclidean roles, their repertoire is likely narrower than humans. But to the extent that the ‘where’ pathway does carry information about general-purpose roles, conjunctive codes in hippocampus may act as generalpurpose bindings of entities to roles. 

## **Replay as compositional computation** 

The second type of composability is stringing together role-bound entities into a huge variety of compounds with different overall meanings. This kind of composition leverages the fact that the world itself is made up of more-or-less separate entities whose recombination in different ways is useful. Continuing with the example of Figure 1, combining _aquarium/start point_ with _a fish’s life/subject_ makes a statement that is new yet interpretable. Reassorting knowledge into meaningful new compounds brings the potential for strong generalization (Battaglia et al., 2018; 

4 

Buzsaki, 2010; Goodman et al., 2014; Zeithamova et al., 2012; Van der Velde and De Kamps, 2006) and may underlie the flexibility of human imagination (Buckner, 2010; Frankland and Greene, 2020; Hassabis et al., 2007). 

We hypothesize that replay sequences express this type of compositionality by chaining the hippocampal representations of role-bound entities together into structures with new compound meanings. Time is a natural axis of composition because it interferes minimally with the activity patterns that encode individual items. Activating items in sequence keeps separate items separate. This is similar to how, in language, we put words in sequence instead of superimposing them. 

Our hypothesis builds on the idea of hippocampus as a sequence generator (Buzsaki and Tingley, 2018), where its function is to construct generic content-free sequences into which any content can be slotted. We add two things to this model. First, sequences don’t have to be played in the order of experience; replay can assemble any set of things in any order. Second, each item in a sequence is bound to a representation of its role in the compound, allowing arbitrary compositional concepts to be constructed by putting together elements in complex ways. 

## **Replay beyond space** 

For replay to implement general-purpose compositional computation, an obvious requirement is that it operates beyond the spatial domain measured in rodent replay experiments. Methodological advances have made it possible to detect replay in humans using magnetoencephalography (MEG), which enables the study of tasks with interesting nonspatial relationships that are difficult to explain to rodents (Kurth-Nelson et al., 2016). In a nutshell, MEG replay experiments involve three stages. First, participants are presented with experimental stimuli (such as images of objects) in random order, each stimulus repeated many times. The evoked MEG data are used to train decoding models that recognize the spatial pattern of MEG data coding for each stimulus. Second, participants perform a task in which they learn about some relationships between the stimuli (for example, chair always precedes ball). Third, during a time period of interest (such as a resting period), MEG data are analyzed using the trained decoding models to identify spontaneous reactivations of the stimulus representations. Replay is declared when spontaneous reactivations occur in fast sequences which adhere to the relationships learned about in the task. 

A number of experiments using this method have found replay in nonspatial tasks. Kurth-Nelson et al. (2016) designed a directed graph of six nodes, where each node was defined by an object (cat, chair, etc) (Figure 3a). Participants experienced trajectories through this graph, always seeing one object at a time, with the order of objects defined by the graph transitions. The graph itself had no natural spatial embedding, and subjects reported not conceiving of the objects in space, instead using conceptual mnemonics like ‘the cat sits on the chair’. After participants had learned about this implicit graph, MEG activity during rest periods spontaneously replayed sequences of object representations, in reverse order of the actual transitions of the graph (Figure 3b). Sequences were time-compressed approximately 20-fold, so an entire sequence lasted about 120 ms. Nonspatial replay also matches several other identifying features of 

5 

**==> picture [618 x 486] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure 3<br>Spontaneous sequential reactivations<br>a b c<br>of object representations<br>Sequence 1<br>Sequence 2<br>0 ms 50 ms 100 ms 150 ms<br>d e<br>Position code systematically Sequence code systematically<br>preceeds object code preceeds object code seq1,pos4 seq2,pos4<br>seq1,pos3 seq2,pos3<br>seq1,pos2 seq2,pos2<br>seq1,pos1 seq2,pos1<br>Time Time<br>f Pre-task rest Task g Place cell 1 Grid cell 1<br>Place cell 2 Grid cell 2<br>Time Time<br>Position 1Position 2Position 3Position 4<br>Decoded position<br>Cell id<br>Decoding probability<br>Decoded position<br>**----- End of picture text -----**<br>


traditional spatial replay, including reward-dependent direction reversal and coincidence with sharp wave ripples (Liu et al., 2019). 

Although these experiments used a simple set of visual objects, hippocampus codes entities as diverse as social position (Tavares et al., 2015), state in abstract MDPs (Sun et al., 2020; Zhou et al., 2019), time (Eichenbaum, 2014), sequence order (Allen et al., 2016), evidence (Nieh et al., 2021) and auditory pitch (Aronov et al., 2017). Within hippocampus’s switchboard (Buzsaki and Tingley, 2018; Teyler and Rudy, 2007; Treves and Rolls, 1994), we could imagine that replay sequences link together entities of different type, even from different levels of abstraction. Hope and feathers; equations and planetary orbits. 

## **First type of composability in replay: attaching objects to role representations** 

We described the binding of entities to roles as the first type of composability. If I’m given the set of words { _attacked, alligator, python_ } without knowing the role of each item, I don’t know who attacked whom. But if I bind each item to its role – { _attacked/action, alligator/patient, python/agent_ } – then I understand the meaning. Human MEG data indicate that replay sequences encode roles bound to objects much like in this example. 

Liu et al. (2019) trained human subjects on a nonspatial task designed to enable decoding of brain representations of roles separately from role-fillers. In the task, subjects learned about a set of eight objects that were arranged into two sequences of four items each. Each object’s role could therefore be described by two variables: which sequence it belonged to, and which position (1st, 2nd, 3rd or 4th) it occupied within that sequence (Figure 3c). Subjects performed this task in the MEG scanner, and Liu et al. (2019) constructed two kinds of neural decoders. The first kind of decoder was trained to recognize each individual object (such as a house). The second was trained to recognize abstract representations of either position or sequence. Abstract position decoders predicted the category label of 1st, 2nd, 3rd or 4th position, given the MEG data evoked by viewing either of the two objects having that position. Likewise, abstract sequence decoders predicted which sequence a viewed object belonged to, invariant to its position. The researchers validated these decoders by testing them with a special crossvalidation technique where all instances of a particular object were held out from training. For example, all instances of the 3rd item in the 2nd sequence might be held out from training. In testing, the position decoder successfully predicted that the held-out item was in the 3rd position, and the sequence decoder successfully predicted that the item was in the 2nd sequence. 

After constructing these decoding models, MEG activity was analyzed during a rest period that followed task learning. First, using object-specific decoders, spontaneous replay sequences were found to play out representations of the objects within a sequence. These replays coincided with transient increases in power in sharp wave ripple frequency. Second, using the abstract position and sequence decoders, the researchers found that each object in a replay sequence was accompanied (with a characteristic 50 ms lag) by a spontaneous reactivation of that object’s abstract sequence and position (Figure 3d,e). In other words, each item in the replay sequence was tagged with its role. The effect is reminiscent of theories like dynamic binding where 

6 

transient synchronous neural relationships bind roles to contents (Engel and Singer, 2001; Hummel and Biederman, 1992; Hummel and Holyoak, 2003). 

The same role tags that played in alignment with object replay sequences also played out in spontaneous sequences even before the participants experienced the objects. This phenomenon, which the researchers called ‘transfer replay’, supports the idea that role representations exist separately from role-fillers and are subsequently bound to new role-fillers when they are learned. Transfer replay mirrors ‘preplay’ in rodents, where spontaneous sequences play out coherent trajectories through an environment before that environment has been experienced (Dragoi and Tonegawa, 2011)[1 ] (Figure 3f). The sequences measured in the two experiments were of different kind: Dragoi and Tonegawa (2011) measured conjunctive place codes while Liu et al. (2019) observed role codes. However, neither experiment was set up to detect the other kind of code. It is possible that role representations played out side-by-side with conjunctive representations in Dragoi and Tonegawa (2011) but were not measured. Likewise, hypothetical sensory bindings may have played out along with roles in Liu et al. (2019). Another unresolved question in both studies is whether the played structure (i.e., linear sequence) was hard-coded by evolution or learned from prior sequential experiences. 

The experiments in Liu et al. (2019) did not afford the anatomical precision to determine where role tags in replay are represented, but grid cells are a prime candidate. As discussed earlier, grid cells code for spatial relationships in spatial tasks and may code for more general relational roles in nonspatial tasks, while hippocampal cells putatively code for the conjunction of role with sensory specifics. In replay, hippocampal cells play out sequences of these conjunctive representations, while grid cells play out corresponding sequences in coordination (Olafsdottir et al., 2016) (Figure 3g). Given that Liu et al. (2019) found representations of sensory information playing out in coordinated sequences with role-like representations, it is reasonable to think that replay events may include three kinds of representation in coordinated sequences: conjunctive codes in hippocampus (which are place cells in a spatial task), role codes in medial entorhinal cortex and other associated cortical areas, and sensory codes in lateral entorhinal cortex and other associated cortical areas. Future experiments will be needed to test this prediction. 

Such experiments could also look for roles generalized even further beyond ‘position’ and ‘sequence’, such as _verb_ or _start point_ . It would be particularly interesting to test for the existence of role tags in replay that could support sophisticated computations. For example, if roles include operations such as _if_ , _then_ and _else_ , then perhaps rudimentary program fragments could be executed in replay sequences. 

## **Second type of composability in replay: stringing elements into sequences** 

In spatial tasks, replay combines fragments of separate spatial experience to play out trajectories that are physically possible but were never experienced (Gupta et al., 2010; Pfeiffer and Foster, 2013; Widloski and Foster, 2022). In nonspatial tasks, the scope for recombination of experience is vastly larger. 

> 1 Although see (Silva et al., 2015) 

7 

Liu et al. (2019) found that replay composes arbitrary objects into novel sequences using nonspatial relational knowledge. We described this experiment above but omitted one important detail. Participants experienced a set of eight objects: A, B, C, D, A’, B’, C’, D’. (The assignment of actual images, such as a chair, was randomized across participants.) Successful task performance required knowing that the objects were organized into two sequences: _<_ A, B, C, D _>_ and _<_ A’, B’, C’, D’ _>_ . But the participants only experienced the objects in a scrambled order, such as _<_ D’, B, C’, C, D, A’, A, B’ _>_ . They had previously learned a rule which allowed them to unscramble what they saw into the two true sequences. Behaviorally, subjects performed well at applying the unscrambling rule to derive the true sequences _<_ A, B, C, D _>_ and _<_ A’, B’, C’, D’ _>_ . As described in the previous section, subjects had a rest period in the MEG scanner after experiencing the scrambled sequence, and object-specific decoders were used to detect spontaneous reactivations of the eight objects. Surprisingly, participants’ brains did not replay sequences in the order of experience. Instead, they played out in the never-seen rule-defined order (Figure 4a). It appears that replay strung a set of items together into a relevant novel compound. 

How is this reorganization achieved in the brain? As we saw in the previous section, replay of objects in Liu et al. (2019) was accompanied by representations of which sequence and which position each object belongs to. Additionally, the position codes replayed spontaneously before the task objects were experienced (‘transfer replay’). Taken together, these points of data suggest a potential mechanism for reorganization: the brain has an abstract template for ‘items in a sequence’ (Behrens et al., 2018; Luyckx et al., 2019), and when new items are encountered that fit this pattern, they are attached to the appropriate role in this template, allowing them to play in the correct sequence. However, for a general-purpose compositional system, it would be useful to not only fit new entities into a static template (like ‘items in a sequence’), but also to produce new compounds where the roles themselves can be reorganized. For example, here is an English sentence in which not only are the words new, but the syntactic structure – the sentence diagram – is not a copy of any sentence I’ve previously written. 

In Schwartenbeck et al. (2021), in each trial human participants were shown the silhouette of a complex two dimensional shape (Figure 4b) and given 3.5 seconds to think about how to assemble it from a set of four primitive building blocks they had previously learned about. Each solution involved exactly three blocks. Participants were aware that one particular building block would be present in all silhouettes. We call this block ‘Stable’. The block that directly attaches to Stable, in the ground truth solution for a given trial, we call ‘Present’. The block attaching to ‘Present’ we call ‘Distant Present’. The fourth block is ‘Absent’. To investigate replay signals underlying the mental construction process, the investigators trained classifiers on individual building blocks and measured pairwise sequences between spontaneous reactivations of those representations during the deliberation period, using similar methods as Liu et al. (2019). They found significant replay of several kinds of sequences of blocks. For example, detection of Present→Stable replay meant that spontaneous reactivation of Present was consistently followed by Stable. Importantly, forming these replay sequences involved placing blocks into new relational arrangements (like ‘the L-shaped block goes _on top_ of the horizontal block’), analogous to a new sentence diagram. Another interesting feature of this study is that there was no temporal ordering between blocks, meaning that replay played out sequences constituting a set of elements rather than successive states in an MDP. 

8 

**==> picture [146 x 54] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure 4 D’ B C’ C<br>a<br>Visual<br>Sequence D A’ A B’<br>**----- End of picture text -----**<br>


**==> picture [165 x 153] intentionally omitted <==**

**==> picture [502 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>b Target<br>True 0.04<br>Sequences A’ B’ C’ D’<br>0.02<br>0<br>Distant<br>Present<br>-0.02 ‘Distant present’ to ‘stable’<br>Present<br>‘Present’ to ‘stable’<br>‘Absent’ to ‘stable’<br>-0.04<br>‘Present’ to ‘present’<br>200 400 600 800 1000<br>Stable<br>Absent Time from Target onset<br>Sequenceness<br>**----- End of picture text -----**<br>


Schwartenbeck et al. (2021) also found that the content of the sequences changed dynamically during the deliberation period. Initially, sequences played out all combinations of Stable with another block. In other words, there were independently sequences of Present→Stable, Distant Present→Stable and Absent→Stable. Shortly after, sequences appeared which combined Distant Present with Present. The researchers argued that each replay sequence can be viewed as sampling a hypothesis about a partial solution of the target configuration, in order to evaluate the hypothesis and gradually resolve uncertainty about the solution. The earliest sequences reflected all combinations of blocks compatible with the prior that the Stable block exists somewhere in the solution. These sequences ostensibly discovered that Present attaches to Stable, after which sequences started to sample the combination of Distant Present with Present, forming the remainder of the solution. 

## **Planning with compositional replay** 

Reorganization of knowledge in replay sequences may be a mechanism for planning. When animals face a spatial decision, spontaneous neural sequences rapidly sample multiple possible future trajectories (Johnson and Redish, 2007; Kay et al., 2020; Ujfalussy and Orban, 2021), likely as part of a planning and evaluation mechanism (Jadhav et al., 2012; Olafsdottir et al., 2018; Pezzulo et al., 2014; Singer et al., 2013; Van Der Meer and Redish, 2009). Planning in nonspatial tasks is thought to work similarly, sampling compositions of prior knowledge to search for solutions (Hills et al., 2015; Hopfield, 2010; Hunt et al., 2021). We suspect, then, that replay actively constructs new compounds (possibly in the form of program fragments) which represent potential partial solutions to a problem. Sampling compositional hypotheses in replay aligns with the brain’s widespread use of sampling for uncertainty representation and inference (Berkes et al., 2011; Buesing et al., 2011; Echeveste et al., 2020; Griffiths et al., 2012; Orban et al., 2016; Rich and Wallis, 2016). 

There is of course a continuum between online planning and offline processing of knowledge. When active behavior is required, replay samples sequences relevant to that behavior (Pfeiffer and Foster, 2013; Wikenheiser and Redish, 2015)[2] . Without task demands, sampling is less constrained (Olafsdottir et al., 2017; Stella et al., 2019), presumably to prepare for a range of possible future scenarios. But the organism always has some information about upcoming decisions, so offline processing lies on a spectrum with planning (Daw and Dayan, 2014; Eldar et al., 2020). When decisions are not needed imminently, we imagine that replay reviews the knowledge base, deriving new facts and identifying inconsistent beliefs requiring revision, like generalized path integration (McNaughton et al., 2006) in conceptual space. When a child learns ‘dolphins are mammals’ (Griffiths et al., 2010; McClelland et al., 2010), offline replay begins to explore and discover the implications, linking and cross-checking it with other knowledge. This takes a while, during which time contradictory beliefs will often be held. 

## **Separate entities in replay** 

> 2 We will not discuss the important differences between theta sequences and replay in sharp wave ripples. 

9 

Figure 5 

a 

**==> picture [279 x 280] intentionally omitted <==**

## b 

**==> picture [368 x 205] intentionally omitted <==**

pawn on e4 pawn on c6 

Description in terms of entities: 

**==> picture [367 x 205] intentionally omitted <==**

pawn on e4 pawn on c6 

**==> picture [368 x 205] intentionally omitted <==**

pawn on e4 pawn on c5 

A fascinating property of replay sequences is that they string together a small set of discretely separated representations. In nonspatial tasks with inherently discrete structure, replay sequences jump abruptly between representations of the objects, as described above (KurthNelson et al., 2016; Liu et al., 2019; Schwartenbeck et al., 2021) (cf Figure 3a,b). More surprisingly, replay also hops between discrete positions in spatial tasks (Pfeiffer and Foster, 2015) (Figure 5a). These hops are aligned with the gamma oscillation. At each peak in gamma, replay dwells at a stationary point in space, and at troughs, the representation jumps to a new point. Pfeiffer and Foster (2015) suggest that peaks in gamma focus representation on a unit of information, and troughs allow transition to a different unit. This idea follows from the large literature on pattern separation and pattern completion within hippocampal circuitry (Leutgeb et al., 2007; Treves and Rolls, 1994; Yassa and Stark, 2011) as a mechanism for sharpening the differences between separate items. The data are also consistent with longstanding theories that the gamma oscillation organizes neuronal spiking into discrete slots which correspond to cognitively relevant parcellations of information (Buzsaki, 2010; Harris et al., 2003; Lisman and Idiart, 1995; Lisman and Jensen, 2013). It is therefore inviting to view a replay sequence as being composed of a small number of separate ‘units’ of representation. 

Dividing the world into separate entities, which can be recombined, gives compositional systems their power (Figure 5b). Reasoning about relationships between separate things is a potent form of abstraction: discarding everything except the relevant entities and relations (Battaglia et al., 2018; Newell et al., 1958; Tsividis et al., 2021). For example, an animal might receive a reward due to an action it took an hour ago. This is a difficult credit assignment problem (Hung et al., 2019) unless the animal abstracts away the continuum of sensory data between the action and the outcome. 

## **Replay’s bidirectional interactions with cortex** 

So far we have focused on replay in hippocampus, but hippocampal replay of course functions as part of the larger system of the brain. One very basic point of connection is that the representations in hippocampus derive from cortex. Thus the compositional computations of replay are grounded (Harnad, 1990) in cortical representations. (Ongoing replays may in fact help to maintain the tight coordination between hippocampus and cortex (Kali and Dayan, 2004).) 

The contents of replay sequences are also shaped by cortex. For example, when an auditory stimulus is played to rats during sleep, spontaneous reactivations in hippocampus are biased toward places previously associated with that sound (Bendor and Wilson, 2012), with the hippocampal activations immediately preceded by corresponding activations in auditory cortex (Rothschild et al., 2017). Although those experiments measured individual reactivations rather than sequences, replay sequences have also been observed where cortex systematically leads hippocampal representations (Ji and Wilson, 2007). 

Additionally, the contents of replay sequences are influenced by the organism’s current goals (Olafsdottir et al., 2015; Pfeiffer and Foster, 2013; Wikenheiser and Redish, 2015; Xu et al., 2019) (Figure 6a). Liu et al. (2019) found that spontaneous value representations localized to vmPFC were predictive of replay of a rewarded sequence, but not of an unrewarded sequence – 

10 

Figure 6 a 

Search 

**==> picture [152 x 152] intentionally omitted <==**

b 

**==> picture [115 x 136] intentionally omitted <==**

c No stimulation Control stimulation Replay disruption Neural network Day of learning 

**==> picture [113 x 132] intentionally omitted <==**

following the general principle of frontal areas orchestrating hippocampal memory retrieval (McCormick et al., 2020; Moscovitch, 1992). We conjecture that, if hippocampal memory is thought of as a probabilistic model of the large joint distribution of experience, cortex may bias retrieval by conditioning that distribution on particular features (for example, reward) to obtain relevant samples. 

In the other direction, hippocampus-to-cortex, our proposal builds on the classic theory of systems consolidation (McClelland et al., 1995; Squire and Alvarez, 1995; Wilson and McNaughton, 1994), where hippocampus rapidly stores new experiences and later reactivates them to consolidate the knowledge into a more stable form in cortex. A wealth of evidence indicates a role for replay in consolidation (Buzsaki, 2015; Olafsdottir et al., 2018; Squire et al., 2015). Sharp wave ripples, in which replays are nested, drive increased hippocampal-cortical communication and cortical plasticity; while disrupting ripples impairs learning (Figure 6b). 

Consolidation theory also posits that replaying different experiences in close proximity allows cortex to learn latent commonalities (Inostroza and Born, 2013; McClelland et al., 1995; O’Reilly and Rudy, 2001; O’Reilly et al., 2014; Saxe et al., 2019). This semantic knowledge induced in cortex by replay may itself have grammar-like structure (Battaglia and Pennartz, 2011; Battaglia et al., 2012). The contents of replay are also optimized to cause the learning that will be most relevant for future tasks (Antonov et al., 2022; Barry and Love, 2021; Liu et al., 2021; Sun et al., 2021). 

As described above, newer experiments have identified situations where replay does not strictly recapitulate past experience, but instead generates plausible new trajectories using a learned transition model (Gupta et al., 2010; Olafsdottir et al., 2015; Pfeiffer and Foster, 2013; Stella et al., 2019; Widloski and Foster, 2022). Such model-based replays do not conform to the simplest models of consolidation because they do not faithfully reactivate actual past experiences. They may nevertheless support transfer of knowledge from hippocampus to cortex by training cortex on the statistics of possible trajectories, analogous to Dyna in machine learning (Sutton, 1991). Replaying actual experience can in fact be viewed as a special case of model-based replay using a nonparametric model (van Hasselt et al., 2019). There is some evidence that model-based replay has the additional function of contributing to online planning (Olafsdottir et al., 2018). 

As model-based replay generalizes consolidation, our proposal further generalizes the idea of model-based replay. We have proposed that not only are replays not limited to playing back actual experience, they are not even limited to playing out trajectories defined by a transition model. Instead, they play out sets of elements along with syntactic roles that define how the elements function together as a whole. Furthermore, instead of directly updating a value function or policy (as in Dyna), we suggest that replay discovers new knowledge of a more general form that does not necessarily have any immediate impact on the policy. An interesting implication is that consolidation mechanisms cause cortex to learn about the new knowledge discovered by composing elements into sequences. 

The bidirectional interaction between replay and cortex sets up the possibility for a positive feedback loop (Lewis et al., 2018; O’Reilly et al., 2014). According to our theory, replay composes existing entities into sequences, and new knowledge is derived from the meaning of the sequence as a whole. If that new knowledge is baked into cortex (Tse et al., 2007), it could 

11 

subsequently function as a single element in higher-order replay sequences (i.e., sequences composed of pieces of knowledge which were previously derived from other sequences). The loop might produce a hierarchy of increasingly elaborate concepts. A similar feedback loop could operate at a faster timescale, too. Some neurons in prefrontal cortex are tuned to specific replay sequences (Berners-Lee et al., 2021), and if these neurons feed back into hippocampus as entities, then higher-order sequences could be composed within hundreds of milliseconds. 

## **Experimental predictions** 

Our perspective is that replay sequences sample structured compositions of existing elements to derive new knowledge. The most obvious experimental implication is that when replay is disrupted, the derivation of new knowledge through composition should be impaired. This could be tested using a task where subjects are taught about novel elements and how those elements work together. After teaching subjects about these elements, the experiment would require detecting the initiation of replay and immediately disrupting it (Girardeau et al., 2009; Jadhav et al., 2012), with the prediction that disrupted individuals would subsequently demonstrate less knowledge about implications of the rules. Such an experiment is challenging because reasoning in rodents is limited, and disrupting replay in humans has never been attempted. Experiments in rodents would require design of tasks to access compositional cognition, perhaps by training on a small set of conditional rules. Disruption in humans might be possible with ultrasound or TMS, especially if replay initiation could be predicted slightly in advance using machine learning. In disruption experiments, careful controls for nonspecific effects such as impaired memory for task-related information would be essential. If done correctly, disruption experiments will be vital for establishing the causal role of replay. 

Short of disruption experiments, another prediction is that after knowledge is derived by replay, it is subsequently available for use in other neural computations. For example, novice players could be tasked with solving a chess puzzle where the king is in check by a bishop[3] . MEG decoding models would be trained to recognize representations of the pieces as well as their relational roles. As subjects consider the puzzle, we predict that replay sequences explore various organized combinations of the pieces, examining the implications of their interactions. At some point during deliberation, a sequence is constructed that contains the king and bishop as elements and the bishop’s moving pattern as a relation. This sequence implies that the king is in check. After this sequence appears (but not before), the brain has knowledge of the king being in check, and this knowledge should manifest in several ways. It might be possible to decode the representation of ‘king in check’ from the brain. Subsequent replay sequences might be constrained to evaluate only moves that escape check. And if forced to move, subjects might behaviorally reflect the knowledge of the king being in check. Although such a correlation would not prove a causal role for replay, it would be suggestive if the temporal relationship were consistent, with knowledge of ‘king in check’ appearing at a short predictable delay after replay sequences containing the king and bishop. 

## **Replay in the brain and AI** 

> 3 Of course a real experiment would be designed to eliminate the confounds inherent to chess. 

12 

In this final section, we consider the implications of our proposal for the relationship between hippocampal replay and machine learning. Replay has been a key point of connection between AI and neuroscience (Lin, 1991; Hassabis et al., 2017; Mnih et al., 2015; Wittkuhn et al., 2021). Replay in the brain is commonly compared to the technique of ‘experience replay’, where an agent stores its observations and later retrieves them for offline learning. This idea fits well with neuroscientific results where replay appeared to recapitulate actual experience. It can also accommodate the observations, discussed in earlier sections, that replay generates novel sequences. A space of techniques in machine learning use experience to train a forward model of the world’s dynamics, and then sample trajectories from the model to train a reactive policy (Sutton, 1991; Shin et al., 2017). 

But in this paper we have proposed that replay in the brain has a more general function: deriving new knowledge through compositional computation. So how should we view the correspondence to AI? In this section we suggest that replay, as a kind of compositional computation embedded in the larger brain system including cortex (which behaves in many ways like a deep neural network (Kell et al., 2018; Mante et al., 2013; Sussillo et al., 2015; Yamins et al., 2014)), should be mapped to machine learning techniques that hybridize compositional computation with deep learning. 

While humans learn new concepts or tasks from just a few examples, standard deep learning architectures cannot do this because they do not generalize effectively from their past experience (Lake et al., 2017). At the same time, explicitly compositional AI systems without deep networks reason about situations far outside their experience (Lake et al., 2017; Newell et al., 1958; Tsividis et al., 2021) but typically lack the abilities of neural networks to learn from raw data and scale to large problem sizes. Due to this complementarity, there have been many efforts to hybridize deep learning with compositional ingredients (Battaglia et al., 2018; Diuk et al., 2008; Ellis et al., 2021; Mao et al., 2019; Silver et al., 2016). 

We outline a possible mapping between such hybrid machine learning systems and replay, following five principles: 

- (1) The use of neural networks to prune large compositional search spaces. 

- (2) The discovery of new knowledge in search. 

- (3) The positive feedback loop that results from using networks to inform search and using search results to improve networks. 

- (4) The varying degree to which compositional operations are hard-coded versus emergent. 

- (5) The grounding of entities in neural network representations. 

Consider the example of AlphaGo (Silver et al., 2016), which has two parts[4 ] (Figure 6c). One is a handcrafted algorithm that searches through trees of possible future moves, in order to find move sequences most likely to lead to a win. The other is a neural network that predicts which moves are likely to be good. The search algorithm prioritizes moves that are preferred by the network, reducing combinatorial explosion and drastically improving search efficiency. 

AlphaGo’s search is a special case of compositional computing, because it is made up of discrete elements linked in organized ways to derive new knowledge. Viewing AlphaGo through this lens 

> 4 We describe elements of both AlphaGo and AlphaZero and elide some important features like value prediction. 

13 

suggests a hypothesis for neuroscience: that cortex predicts which combinatorial arrangements in replay sequences are useful and biases hippocampus toward generating these sequences. Although the syntax of AlphaGo’s search only deals with board positions linked by moves, neurally-guided search is also effective in many other machine learning contexts, such as searching through the space of programs expressed in a programming language (e.g., Ellis et al. (2021); Kalyan et al. (2018); Parisotto et al. (2016)). 

AlphaGo uses the results of search both to make immediate decisions and to train its neural network. When playing a game, AlphaGo selects each move according to a search. But to train the neural network, AlphaGo plays millions of games against itself, and the network is trained to prefer moves that lead to winning outcomes. In this way, new knowledge discovered by the search process is gradually baked in to the network. As AlphaGo’s network improves, the quality of searches rises, which further improves the network in a positive feedback loop. While the effect of search to improve AlphaGo’s network is indirect (via self-play), other related AI systems (e.g., Ellis et al. (2021); Hamrick et al. (2019)) train a neural network directly on knowledge discovered by search. 

Across the large family of methods that hybridize neural networks with compositional representation, there is a wide range of design choices about the degree to which the compositional component is handcrafted versus learned implicitly. At one extreme, AlphaGo uses a fully handcrafted search algorithm and searches through the space of idealized board positions. At the other extreme, training unstructured neural networks on certain distributions of data leads to the emergence of structured compositional operations within the dynamics of the network (Guez et al., 2019; Ortega et al., 2019; Wang et al., 2018). Between these endpoints there are many compromises. 

MuZero (Schrittwieser et al., 2020) has a similar architecture to AlphaGo but is not endowed with knowledge of any game’s rules. Instead, it learns from experience to transform its inputs into useful representations and to predict the environment’s dynamics. Thus, like replay but unlike AlphaGo, MuZero grounds the elements that are recombined through search. However, unlike replay, neither AlphaGo nor MuZero have a rich syntax. Elements are combined only into chains of moves that follow one another in gameplay. An interesting direction in AI research is combining MuZero-style grounded entities and roles with syntactically rich composition. 

Neural networks with attention (Bahdanau et al., 2014; Graves et al., 2014; Vaswani et al., 2017) form another midpoint. Attention mixes together multiple inputs according to a set of weights, such that the inputs with low weight are filtered out and those with high weight are retained. The weights are calculated on-the-fly as a learned function of data. Neural networks with attention have set new standards for performance in many areas of machine learning (Brown et al., 2020; Jumper et al., 2021; Vinyals et al., 2019). An important observation is that attention gives rise to role-filler binding (Schlag et al., 2021; Whittington et al., 2021; Botvinick and Watanabe, 2007; Smolensky, 1990; O’Reilly and Frank, 2006). This is because a role can induce weights that attend selectively to the filler, thereby accessing its contents. If the contents of the filler change, the weights attend to that new data. Or, to rephrase in the language we’ve been using for replay, attention grants the first type of composability. In the context of replay, it’s curious that attention-based neural networks, despite their amazing successes, often fail at structured reasoning (Lake and Murphy, 2021; Marcus and Davis, 2020), which depends on 

14 

composing elements into compounds. Another exciting project in AI research is adding replaylike composition mechanisms to attention-based neural networks. 

## **Conclusion** 

The world is too complex for an agent to force all its beliefs to be immediately consistent with one another – we still can’t reconcile gravity and quantum mechanics, for example, while having them as separate theories is highly useful. Real intelligence therefore requires understanding things in multiple ways, with a variety of metaphors or views on a problem that are kept separate from one another. But these different conceptualizations need to be sometimes put into contact in order to find new symmetries and deeper understanding. In many contexts, interesting structure arises from alternation between these two modes of a system, one where elements remain relatively separated and another where interactions are frequent (Kitadai and Maruyama, 2018; Srivastava et al., 2014; Zador, 2019). We like the idea that the hybridization of replay with cortex serves this purpose. The compositional system of replay maintains separate pieces of knowledge while cortex extracts semantic abstractions. In this way replay may contribute to the brain’s capacity for open-ended learning and creativity (Stanley et al., 2017). 

**Acknowledgements.** We thank Zach Duer, Marc Guitart-Masip, Jess Hamrick, Kim Stachenfeld and Steve Sullivan for insightful discussions and comments on a draft of the manuscript. 

## **Figure Captions** 

**Figure 1: Two types of composability in replay. a,** A structured compound, such as the concept ‘I am driving home from the airport’, can be described as a set of entities and the role each entity plays in the compound. Each entity, like _driving_ , is bound to a role, like _action_ . The compound has a meaning that derives from the interaction of its parts but is not contained in any of the parts. **b,** In our hypothesis, a replay sequence constitutes a set of entities, each tagged with the role of that entity, and can describe complex concepts. **c,** One type of composability is that roles are independent of entities and are free to attach to new entities. **d,** Another type of composability is that role-bound entities can be combined in many different ways to form new compounds. 

**Figure 2: Binding of entities and roles in hippocampus. a,** A highly schematized depiction of two processing pathways in cortex, adapted from Manns and Eichenbaum (2006). The ‘what’ pathway, including posterior parietal cortex and perirhinal cortex, extracts and transmits information about the identities and semantics of perceived entities (shown as geometric objects). The ‘where’ pathway, including inferior temporal cortex and parahippocampal cortex, extracts and transmits information about relational roles of entities (shown as a repeating pattern representing an abstract code for space). After these pathways reach cells in lateral and medial entorhinal cortex, respectively, they converge on cells in hippocampus to produce conjunctive representations of ‘entity in role’, such as an episodic memory or a location in a particular environment. **b,** In the experiment of Sun et al. (2020), mice ran four identical laps (two are shown in this schematic) around a track before getting reward. Each mouse performed the four-lap task in two different environments. Consistent with many prior experiments, 

15 

hippocampal place cells remapped to new spatial locations between environments. Remapping can be explained as the same spatial role codes (MEC) being conjoined with by new sensory rolefiller codes (LEC) in the new environment. **c,** Some place cells were tuned not only to space but also to lap index, for example firing only on lap 2 of 4. Lap tuning did not remap between environments, which is explained by discrete role codes tuned to a particular lap (Whittington et al., 2020). 

**Figure 3: Nonspatial replay and role representations. a,** In Kurth-Nelson et al. (2016), subjects learned about the nonspatial relationships between six objects. **b,** Replay sequences were detected with MEG and followed reverse paths in the graph (Kurth-Nelson et al., 2016). Color axis shows strength of spontaneous neural reactivations of four stimuli. **c,** In Liu et al. (2019), subjects learned about a different nonspatial organization: eight objects comprising two sequences. The role of each object in the task could thus be described with two variables: position and sequence. **d,** During a rest period (Liu et al., 2019), replay spontaneously played out the learned sequences (not shown; similar to panel b). During these replay events, representations of the position and sequence variables also activated, with each role code slightly preceding the replayed representation of the corresponding object. The y-axis is a measure of how consistently the position or sequence code precedes (positive) or follows (negative) the representation of the object. **e,** Schematic of role tags in replay sequences (Liu et al., 2019). Colored lines show decoding of spontaneous representations at rest. Red and green lines correspond to concrete objects, which reactivated in fast sequences. Each object was accompanied by representations of the role it played: which sequence it belonged to, and which position it occupied within its sequence (blue lines). **f,** Dragoi and Tonegawa (2011) recorded hippocampal cells before the animal’s first experience of a new environment. The cells spontaneously fired in sequences which formed coherent trajectories (left) when viewed through the lens of the spatial tunings they would subsequently adopt in the new environment (right). **g,** Replay is coordinated between place cells and grid cells  (Olafsdottir et al., 2016). Two example replay events are shown, with one place cell and one grid cell for each event. Color indicates probability of decoding at each spatial position; white lines are fit to the data. 

**Figure 4: Replay sequences assemble entities into new compounds. a,** Replay synthesizes novel sequences that are implied by an abstract rule (Liu et al., 2019). Human subjects learned a rule that defined how a set of objects should be ordered. When they encountered a new set of objects (the eight objects shown) out-of-order, replay immediately began playing the items in the rule-defined order (True Sequences). There was no replay in the actually-experienced order (Visual Sequence). Each plot shows the strength of forward (positive y) or backward (negative y) sequences at every possible replay speed (x-axis). **b,** In a construction problem, sequences compose building blocks into candidate solutions (Schwartenbeck et al., 2021). In each trial of this task, subjects are presented a black silhouette (Target) and given 3.5 seconds to consider how to build it from four component blocks they previously learned about. The Stable block is part of the solution for every Target (in varying positions). Each other block can be Present or Absent in any given Target. In the MEG signal, spontaneous representations of each block were decoded during the 3.5 second thinking period. The right panel shows the degree of consistent sequences (y-axis) in the spontaneous activations at each moment relative to Target onset (xaxis). Tick labels are the start point of a 1 s sliding window used for sequence analysis. This plot zooms in on the most relevant time epoch. Early in the deliberation period, three kinds of replay sequences appeared (yellow, green and blue traces), each involving the Stable block and one 

16 

other block. Soon after, sequences emerge that link the two Present blocks. Note that sequenceness here measures absolute rather than forward minus backward sequences as plotted in a. Sequenceness is averaged over the range of element-to-element lags (10-200 ms) typically used for MEG replay analysis. 

**Figure 5: Discreteness in replay. a,** Replay sequences in a spatial task jump abruptly from point to point (Pfeiffer and Foster, 2015). Animals ran around a 2D open field (black square), and replay was measured during subsequent rest. Image shows a single replay sequence, collapsing over 340 milliseconds. Color at each pixel is the decoded probability that the replay sequence traversed that point in space. **b,** Compositional systems divide the world into entities that can be recombined, like ‘pawn’ or ‘c5 square’. These abstractions are only sensitive to key features that define each entity, with invariance to other features. The first and second images are both Caro-Kann despite having almost no pixel similarity in the position of the c-pawn, while the third is Sicilian. 

**Figure 6: Hybrid systems. a,** Current goals bias replay sequences. In Wikenheiser and Redish (2015), rats ran in a circle, sometime electing to pause at one of three equally-spaced feeders. Replay sequences (colored dots) traversed paths ahead of the animal. In trials when the rat would subsequently stop at a particular feeder, the prospective sequences also terminated at that feeder (left panel). When the rat did not plan to stop, sequences skipped the feeder (right panel). **b,** Blocking replay impairs learning. Replay sequences are nested within sharp wave ripples, the high frequency oscillation shown in blue trace and inset of red trace. Girardeau et al. (2009) performed online detection of ripples during a rest period after each day’s learning session, and injected current to disrupt replay events at their initiation (upper left panel). In the control condition (blue), current was injected 100 ms after the detected ripple (lower left panel). The calibration bars show 20 ms on the x-axis and 0.2 mV on the y-axis. Disrupting replay during rest impaired acquisition of the task (right panel; red disrupted learning curve below blue control and black no current injection). **c,** Simplified diagram of AlphaGo (Silver et al., 2016), which has a neural network component (red) and a discrete search component (black). The network predicts which moves are good in each board position. This constrains the search mechanism, reducing the combinatorial explosion of the game. The results of searches are ultimately used to train the neural network, creating a feedback loop. 

## **References** 

T. A. Allen, D. M. Salz, S. McKenzie, and N. J. Fortin. Nonspatial sequence coding in ca1 neurons. _Journal of Neuroscience_ , 36(5):1547–1563, 2016. 

G. Antonov, C. Gagne, E. Eldar, and P. Dayan. Optimism and pessimism in optimised replay. _PLOS Computational Biology_ , 18(1):e1009634, 2022. 

D. Aronov, R. Nevers, and D. W. Tank. Mapping of a non-spatial dimension by the hippocampal– entorhinal circuit. _Nature_ , 543(7647):719–722, 2017. 

D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate. _arXiv preprint arXiv:1409.0473_ , 2014. 

D. N. Barry and B. C. Love. A neural network account of memory replay and knowledge consolidation. _bioRxiv_ , 2021. 

17 

F. P. Battaglia and C. M. Pennartz. The construction of semantic memory: grammar-based representations learned from relational episodic information. _Frontiers in computational neuroscience_ , 5:36, 2011. 

F. P. Battaglia, G. Borensztajn, and R. Bod. Structured cognition and neural systems: from rats to language. _Neuroscience & Biobehavioral Reviews_ , 36(7):1626–1639, 2012. 

P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner, et al. Relational inductive biases, deep learning, and graph networks. _arXiv preprint arXiv:1806.01261_ , 2018. 

T. E. Behrens, T. H. Muller, J. C. Whittington, S. Mark, A. B. Baram, K. L. Stachenfeld, and Z. KurthNelson. What is a cognitive map? organizing knowledge for flexible behavior. _Neuron_ , 100(2):490–509, 2018. 

D. Bendor and M. A. Wilson. Biasing the content of hippocampal replay during sleep. _Nature neuroscience_ , 15(10):1439–1444, 2012. 

P. Berkes, G. Orban, M. Lengyel, and J. Fiser. Spontaneous cortical activity reveals hallmarks of an optimal internal model of the environment. _Science_ , 331(6013):83–87, 2011. 

A. Berners-Lee, X. Wu, and D. J. Foster. Prefrontal cortical neurons are selective for non-local hippocampal representations during replay and behavior. _Journal of Neuroscience_ , 41(27): 5894–5908, 2021. 

A. Bongioanni, D. Folloni, L. Verhagen, J. Sallet, M. C. Klein-Flu¨gge, and M. F. Rushworth. Activation and disruption of a neural mechanism for novel choice in monkeys. _Nature_ , 591 (7849):270–274, 2021. 

M. Botvinick and T. Watanabe. From numerosity to ordinal rank: a gain-field model of serial order representation in cortical working memory. _Journal of Neuroscience_ , 27(32):8636–8642, 2007. 

T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33:1877–1901, 2020. 

R. L. Buckner. The role of the hippocampus in prediction and imagination. _Annual review of psychology_ , 61:27–48, 2010. 

L. Buesing, J. Bill, B. Nessler, and W. Maass. Neural dynamics as sampling: a model for stochastic computation in recurrent networks of spiking neurons. _PLoS computational biology_ , 7(11):e1002211, 2011. 

G. Buzsaki. Two-stage model of memory trace formation: a role for “noisy” brain states. _Neuroscience_ , 31(3):551–570, 1989. 

G. Buzsaki. Neural syntax: cell assemblies, synapsembles, and readers. _Neuron_ , 68(3):362–385, 2010. 

G. Buzsaki. Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. _Hippocampus_ , 25(10):1073–1188, 2015. 

G. Buzsaki and D. Tingley. Space and time: The hippocampus as a sequence generator. _Trends in cognitive sciences_ , 22(10):853–869, 2018. 

N. J. Cohen and H. Eichenbaum. _Memory, amnesia, and the hippocampal system_ . MIT press, 1993. A. O. Constantinescu, J. X. O’Reilly, and T. E. Behrens. Organizing conceptual knowledge in humans with a gridlike code. _Science_ , 352(6292):1464–1468, 2016. 

N. D. Daw and P. Dayan. The algorithmic anatomy of model-based evaluation. _Philosophical Transactions of the Royal Society B: Biological Sciences_ , 369(1655):20130478, 2014. 

18 

C. Diuk, A. Cohen, and M. L. Littman. An object-oriented representation for efficient reinforcement learning. In _Proceedings of the 25th international conference on Machine learning_ , pages 240–247, 2008. 

G. Dragoi and S. Tonegawa. Preplay of future place cell sequences by hippocampal cellular assemblies. _Nature_ , 469(7330):397–401, 2011. 

Y. Dudai. The restless engram: consolidations never end. _Annual review of neuroscience_ , 35: 227– 247, 2012. 

R. Echeveste, L. Aitchison, G. Hennequin, and M. Lengyel. Cortical-like dynamics in recurrent circuits optimized for sampling-based probabilistic inference. _Nature neuroscience_ , 23(9): 1138–1149, 2020. 

H. Eichenbaum. Time cells in the hippocampus: a new dimension for mapping memories. _Nature Reviews Neuroscience_ , 15(11):732–744, 2014. 

E. Eldar, G. Lievre, P. Dayan, and R. J. Dolan. The roles of online and offline replay in planning. _ELife_ , 9:e56911, 2020. 

K. Ellis, C. Wong, M. Nye, M. Sable-Meyer, L. Morales, L. Hewitt, L. Cary, A. Solar-Lezama, and J. B. Tenenbaum. Dreamcoder: Bootstrapping inductive program synthesis with wakesleep library learning. In _Proceedings of the 42nd acm sigplan international conference on programming language design and implementation_ , pages 835–850, 2021. 

A. K. Engel and W. Singer. Temporal binding and the neural correlates of sensory awareness. _Trends in cognitive sciences_ , 5(1):16–25, 2001. 

D. J. Foster. Replay comes of age. _Annual review of neuroscience_ , 40:581–602, 2017. 

S. M. Frankland and J. D. Greene. Concepts and compositionality: in search of the brain’s language of thought. _Annual review of psychology_ , 71:273–303, 2020. 

M. Fyhn, T. Hafting, A. Treves, M.-B. Moser, and E. I. Moser. Hippocampal remapping and grid realignment in entorhinal cortex. _Nature_ , 446(7132):190–194, 2007. 

G. Girardeau, K. Benchenane, S. I. Wiener, G. Buzsaki, and M. B. Zugaro. Selective suppression of hippocampal ripples impairs spatial memory. _Nature neuroscience_ , 12(10):1222–1223, 2009. M. A. Goodale and A. D. Milner. Separate visual pathways for perception and action. _Trends in neurosciences_ , 15(1):20–25, 1992. 

N. D. Goodman, J. B. Tenenbaum, and T. Gerstenberg. Concepts in a probabilistic languageof thought. Technical report, Center for Brains, Minds and Machines (CBMM), 2014. 

A. Graves, G. Wayne, and I. Danihelka. Neural turing machines. _arXiv preprint arXiv:1410.5401_ , 2014. 

T. L. Griffiths, N. Chater, C. Kemp, A. Perfors, and J. B. Tenenbaum. Probabilistic models of cognition: Exploring representations and inductive biases. _Trends in cognitive sciences_ , 14 (8):357–364, 2010. 

T. L. Griffiths, E. Vul, and A. N. Sanborn. Bridging levels of analysis for probabilistic models of cognition. _Current Directions in Psychological Science_ , 21(4):263–268, 2012. 

A. Guez, M. Mirza, K. Gregor, R. Kabra, S. Racaniere, T. Weber, D. Raposo, A. Santoro, L. Orseau, T. Eccles, et al. An investigation of model-free planning. In _International Conference on Machine Learning_ , pages 2464–2473. PMLR, 2019. 

A. S. Gupta, M. A. van der Meer, D. S. Touretzky, and A. D. Redish. Hippocampal replay is not a simple function of experience. _Neuron_ , 65(5):695–705, 2010. 

J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, T. Pfaff, T. Weber, L. Buesing, and P. W. Battaglia. Combining q-learning and search with amortized value estimates. _arXiv preprint arXiv:1912.02807_ , 2019. 

19 

S. Harnad. The symbol grounding problem. _Physica D: Nonlinear Phenomena_ , 42(1-3):335–346, 1990. 

K. D. Harris, J. Csicsvari, H. Hirase, G. Dragoi, and G. Buzsaki. Organization of cell assemblies in the hippocampus. _Nature_ , 424(6948):552–556, 2003. 

D. Hassabis, D. Kumaran, S. D. Vann, and E. A. Maguire. Patients with hippocampal amnesia cannot imagine new experiences. _Proceedings of the National Academy of Sciences_ , 104(5): 1726– 1731, 2007. 

D. Hassabis, D. Kumaran, C. Summerfield, and M. Botvinick. Neuroscience-inspired artificial intelligence. _Neuron_ , 95(2):245–258, 2017. 

T. T. Hills, P. M. Todd, D. Lazer, A. D. Redish, I. D. Couzin, C. S. R. Group, et al. Exploration versus exploitation in space, mind, and society. _Trends in cognitive sciences_ , 19(1):46–54, 2015. 

J. J. Hopfield. Neurodynamics of mental exploration. _Proceedings of the National Academy of Sciences_ , 107(4):1648–1653, 2010. 

J. E. Hummel and I. Biederman. Dynamic binding in a neural network for shape recognition. _Psychological review_ , 99(3):480, 1992. 

J. E. Hummel and K. J. Holyoak. A symbolic-connectionist theory of relational inference and generalization. _Psychological review_ , 110(2):220, 2003. 

C.-C. Hung, T. Lillicrap, J. Abramson, Y. Wu, M. Mirza, F. Carnevale, A. Ahuja, and G. Wayne. Optimizing agent behavior over long time scales by transporting value. _Nature communications_ , 10(1):1–12, 2019. 

L. Hunt, N. Daw, P. Kaanders, M. MacIver, U. Mugan, E. Procyk, A. Redish, E. Russo,J. Scholl, K. Stachenfeld, et al. Formalizing planning and information search in naturalistic decision-making. _Nature neuroscience_ , pages 1–14, 2021. 

M. Inostroza and J. Born. Sleep for preserving and transforming episodic memory. _Annual review of neuroscience_ , 36:79–102, 2013. 

S. P. Jadhav, C. Kemere, P. W. German, and L. M. Frank. Awake hippocampal sharp-wave ripples support spatial memory. _Science_ , 336(6087):1454–1458, 2012. 

D. Ji and M. A. Wilson. Coordinated memory replay in the visual cortex and hippocampus during sleep. _Nature neuroscience_ , 10(1):100–107, 2007. 

A. Johnson and A. D. Redish. Hippocampal replay contributes to within session learning in a temporal difference reinforcement learning model. _Neural Networks_ , 18(9):1163–1171, 2005. 

A. Johnson and A. D. Redish. Neural ensembles in ca3 transiently encode paths forward of the animal at a decision point. _Journal of Neuroscience_ , 27(45):12176–12189, 2007. 

J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O. Ronneberger, K. Tunyasuvunakool, R. Bates, A. Zıdek, A. Potapenko, et al. Highly accurate protein structure prediction withˇ alphafold. _Nature_ , 596(7873):583–589, 2021. 

S. Kali and P. Dayan. Off-line replay maintains declarative memories in a model of hippocampalneocortical interactions. _Nature neuroscience_ , 7(3):286–294, 2004. 

A. Kalyan, A. Mohta, O. Polozov, D. Batra, P. Jain, and S. Gulwani. Neural-guided deductive search for real-time program synthesis from examples. _arXiv preprint arXiv:1804.01186_ , 2018. 

K. Kay, J. E. Chung, M. Sosa, J. S. Schor, M. P. Karlsson, M. C. Larkin, D. F. Liu, and L. M. Frank. Constant sub-second cycling between representations of possible futures in the hippocampus. _Cell_ , 180(3):552–567, 2020. 

C. S. Keene, J. Bladon, S. McKenzie, C. D. Liu, J. O’Keefe, and H. Eichenbaum. Complementary functional organization of neuronal activity patterns in the perirhinal, lateral entorhinal, and medial entorhinal cortices. _Journal of Neuroscience_ , 36(13):3660–3675, 2016. 

20 

A. J. Kell, D. L. Yamins, E. N. Shook, S. V. Norman-Haignere, and J. H. McDermott. A task-optimized neural network replicates human auditory behavior, predicts brain responses, and reveals a cortical processing hierarchy. _Neuron_ , 98(3):630–644, 2018. 

N. J. Killian, M. J. Jutras, and E. A. Buffalo. A map of visual space in the primate entorhinal cortex. _Nature_ , 491(7426):761–764, 2012. 

N. Kitadai and S. Maruyama. Origins of building blocks of life: A review. _Geoscience Frontiers_ , 9(4):1117–1153, 2018. 

J. J. Knierim, I. Lee, and E. L. Hargreaves. Hippocampal place cells: parallel input streams, subregional processing, and implications for episodic memory. _Hippocampus_ , 16(9):755–764, 2006. 

Z. Kurth-Nelson, M. Economides, R. J. Dolan, and P. Dayan. Fast sequences of non-spatial state representations in humans. _Neuron_ , 91(1):194–204, 2016. 

B. M. Lake and G. L. Murphy. Word meaning in minds and machines. _Psychological review_ , 2021. 

B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershman. Building machines that learn and think like people. _Behavioral and brain sciences_ , 40, 2017. 

J. K. Leutgeb, S. Leutgeb, M.-B. Moser, and E. I. Moser. Pattern separation in the dentate gyrus and ca3 of the hippocampus. _science_ , 315(5814):961–966, 2007. 

P. A. Lewis, G. Knoblich, and G. Poe. How memory replay in sleep boosts creative problemsolving. _Trends in cognitive sciences_ , 22(6):491–503, 2018. 

L. J. Lin. Programming robots using reinforcement learning and teaching. In _AAAI_ , pages 781– 786, 1991. 

J. E. Lisman and M. A. Idiart. Storage of 7±2 short-term memories in oscillatory subcycles. _Science_ , 267(5203):1512–1515, 1995. 

J. E. Lisman and O. Jensen. The theta-gamma neural code. _Neuron_ , 77(6):1002–1016, 2013. Y. Liu, R. J. Dolan, Z. Kurth-Nelson, and T. E. Behrens. Human replay spontaneously reorganizes experience. _Cell_ , 178(3):640–652, 2019. 

Y. Liu, M. G. Mattar, T. E. Behrens, N. D. Daw, and R. J. Dolan. Experience replay is associated with efficient nonlocal learning. _Science_ , 372(6544), 2021. 

K. Louie and M. A. Wilson. Temporally structured replay of awake hippocampal ensemble activity during rapid eye movement sleep. _Neuron_ , 29(1):145–156, 2001. 

F. Luyckx, H. Nili, B. Spitzer, and C. Summerfield. Neural structure mapping in human probabilistic reward learning. _Elife_ , 8:e42816, 2019. 

J. R. Manns and H. Eichenbaum. Evolution of declarative memory. _Hippocampus_ , 16(9):795– 808, 2006. 

V. Mante, D. Sussillo, K. V. Shenoy, and W. T. Newsome. Context-dependent computation by recurrent dynamics in prefrontal cortex. _nature_ , 503(7474):78–84, 2013. 

J. Mao, C. Gan, P. Kohli, J. B. Tenenbaum, and J. Wu. The neuro-symbolic concept learner: Interpreting scenes, words, and sentences from natural supervision. _arXiv preprint arXiv:1904.12584_ , 2019. 

G. Marcus and E. Davis. Gpt-3, bloviator: Openai’s language generator has no idea what it’s talking about. _MIT Technology Review_ , 2020. 

M. G. Mattar and N. D. Daw. Prioritized memory access explains planning and hippocampal replay. _Nature neuroscience_ , 21(11):1609–1617, 2018. 

M. G. Mattar and M. Lengyel. Planning in the brain. _Neuron_ , 2022. 

21 

J. L. McClelland, B. L. McNaughton, and R. C. O’Reilly. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. _Psychological review_ , 102(3):419, 1995. 

J. L. McClelland, M. M. Botvinick, D. C. Noelle, D. C. Plaut, T. T. Rogers, M. S. Seidenberg, and L. B. Smith. Letting structure emerge: connectionist and dynamical systems approaches to cognition. _Trends in cognitive sciences_ , 14(8):348–356, 2010. 

C. McCormick, D. N. Barry, A. Jafarian, G. R. Barnes, and E. A. Maguire. vmpfc drives hippocampal processing during autobiographical memory recall regardless of remoteness. _Cerebral Cortex_ , 30(11):5972–5987, 2020. 

B. L. McNaughton, F. P. Battaglia, O. Jensen, E. I. Moser, and M.-B. Moser. Path integration and the neural basis of the ‘cognitive map’. _Nature Reviews Neuroscience_ , 7(8):663–678, 2006. 

V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, et al. Human-level control through deep reinforcement learning. _nature_ , 518(7540):529–533, 2015. 

M. Moscovitch. Memory and working-with-memory: A component process model based on modules and central systems. _Journal of cognitive neuroscience_ , 4(3):257–267, 1992. 

Z. Nadasdy, H. Hirase, A. Czurko, J. Csicsvari, and G. Buzsaki. Replay and time compression of recurring spike sequences in the hippocampus. _Journal of Neuroscience_ , 19(21):9497–9507, 1999. 

A. Newell, J. C. Shaw, and H. A. Simon. Elements of a theory of human problem solving. _Psychological review_ , 65(3):151, 1958. 

E. H. Nieh, M. Schottdorf, N. W. Freeman, R. J. Low, S. Lewallen, S. A. Koay, L. Pinto, J. L. Gauthier, C. D. Brody, and D. W. Tank. Geometry of abstract learned knowledge in the hippocampus. _Nature_ , 595(7865):80–84, 2021. 

H. F. Olafsdottir, C. Barry, A. B. Saleem, D. Hassabis, and H. J. Spiers. Hippocampal place cells construct reward related sequences through unexplored space. _Elife_ , 4:e06063, 2015. 

H. F. Olafsdottir, F. Carpenter, and C. Barry. Coordinated grid and place cell replay during rest. _Nature neuroscience_ , 19(6):792–794, 2016. 

H. F. Olafsdottir, F. Carpenter, and C. Barry. Task demands predict a dynamic switch in the content of awake hippocampal replay. _Neuron_ , 96(4):925–935, 2017. 

H. F. Olafsdottir, D. Bush, and C. Barry. The role of hippocampal replay in memory and planning. _Current Biology_ , 28(1):R37–R50, 2018. 

G. Orban, P. Berkes, J. Fiser, and M. Lengyel. Neural variability and sampling-based probabilistic representations in the visual cortex. _Neuron_ , 92(2):530–543, 2016. 

R. C. O’Reilly and M. J. Frank. Making working memory work: a computational model of learning in the prefrontal cortex and basal ganglia. _Neural computation_ , 18(2):283–328, 2006. 

R. C. O’Reilly and J. W. Rudy. Conjunctive representations in learning and memory: principles of cortical and hippocampal function. _Psychological review_ , 108(2):311, 2001. 

P. A. Ortega, J. X. Wang, M. Rowland, T. Genewein, Z. Kurth-Nelson, R. Pascanu, N. Heess, J. Veness, 

A. Pritzel, P. Sprechmann, et al. Meta-learning of sequential strategies. _arXiv preprint arXiv:1905.03030_ , 2019. 

R. C. O’Reilly, R. Bhattacharyya, M. D. Howard, and N. Ketz. Complementary learning systems. _Cognitive science_ , 38(6):1229–1248, 2014. 

E. Parisotto, A.-r. Mohamed, R. Singh, L. Li, D. Zhou, and P. Kohli. Neuro-symbolic program synthesis. _arXiv preprint arXiv:1611.01855_ , 2016. 

J. Pearl. _Causality_ . Cambridge university press, 2009. 

22 

G. Pezzulo, M. A. van der Meer, C. S. Lansink, and C. M. Pennartz. Internally generated sequences in learning and executing goal-directed behavior. _Trends in cognitive sciences_ , 18 (12):647–657, 2014. 

B. E. Pfeiffer and D. J. Foster. Hippocampal place-cell sequences depict future paths to remembered goals. _Nature_ , 497(7447):74–79, 2013. 

B. E. Pfeiffer and D. J. Foster. Autoassociative dynamics in the generation of sequences of hippocampal place cells. _Science_ , 349(6244):180–183, 2015. 

E. L. Rich and J. D. Wallis. Decoding subjective decisions from orbitofrontal cortex. _Nature neuroscience_ , 19(7):973–980, 2016. 

E. L. Roscow, R. Chua, R. P. Costa, M. W. Jones, and N. Lepora. Learning offline: memory replay in biological and artificial reinforcement learning. _Trends in Neurosciences_ , 2021. 

G. Rothschild, E. Eban, and L. M. Frank. A cortical–hippocampal–cortical loop of information processing during memory consolidation. _Nature neuroscience_ , 20(2):251–259, 2017. 

A. M. Saxe, J. L. McClelland, and S. Ganguli. A mathematical theory of semantic development in deep neural networks. _Proceedings of the National Academy of Sciences_ , 116(23):11537– 11546, 2019. 

I. Schlag, K. Irie, and J. Schmidhuber. Linear transformers are secretly fast weight programmers. In _International Conference on Machine Learning_ , pages 9355–9366. PMLR, 2021. 

A. Schrittwieser, I. Antonoglou, T. Hubert, K. Simonyan, L. Sifre, S. Schmitt, A. Guez, E. Lock-hart, 

D. Hassabis, T. Graepel, et al. Mastering atari, go, chess and shogi by planning with a learned model. _Nature_ , 588(7839):604–609, 2020. 

P. Schwartenbeck, A. Baram, Y. Liu, S. Mark, T. Muller, R. Dolan, M. Botvinick, Z. Kurth-Nelson, and T. Behrens. Generative replay for compositional visual understanding in the prefrontalhippocampal circuit. _bioRxiv_ , 2021. 

H. Shin, J. K. Lee, J. Kim, and J. Kim.  Continual  learning  with  deep  generative  replay. _Advances in neural information processing systems_ , 30, 2017. 

D. Silva, T. Feng, and D. J. Foster. Trajectory events across hippocampal place cells require previous experience. _Nature neuroscience_ , 18(12):1772–1779, 2015. 

D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. Van Den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, et al. Mastering the game of go with deep neural networks and tree search. _nature_ , 529(7587):484–489, 2016. 

A. C. Singer, M. F. Carr, M. P. Karlsson, and L. M. Frank. Hippocampal swr activity predicts correct decisions during the initial learning of an alternation task. _Neuron_ , 77(6):1163–1173, 2013. W. E. Skaggs and B. L. McNaughton. Replay of neuronal firing sequences in rat hippocampus during sleep following spatial experience. _Science_ , 271(5257):1870–1873, 1996. 

P. Smolensky. Tensor product variable binding and the representation of symbolic structures in connectionist systems. _Artificial intelligence_ , 46(1-2):159–216, 1990. 

L. R. Squire and P. Alvarez. Retrograde amnesia and memory consolidation: a neurobiological perspective. _Current opinion in neurobiology_ , 5(2):169–177, 1995. 

L. R. Squire, L. Genzel, J. T. Wixted, and R. G. Morris. Memory consolidation. _Cold Spring Harbor perspectives in biology_ , 7(8):a021766, 2015. 

N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. _The journal of machine learning research_ , 15(1):1929–1958, 2014. 

K. L. Stachenfeld, M. M. Botvinick, and S. J. Gershman. The hippocampus as a predictive map. _Nature neuroscience_ , 20(11):1643–1653, 2017. 

23 

K. O. Stanley, J. Lehman, and L. Soros. Open-endedness: The last grand challenge you’ve never heard of. _O’Reilly_ , 2017. 

F. Stella, P. Baracskay, J. O’Neill, and J. Csicsvari. Hippocampal reactivation of random trajectories resembling brownian diffusion. _Neuron_ , 102(2):450–461, 2019. 

C. Sun, W. Yang, J. Martin, and S. Tonegawa. Hippocampal neurons represent events as transferable units of experience. _Nature neuroscience_ , 23(5):651–663, 2020. 

W. Sun, M. Advani, N. Spruston, A. Saxe, and J. E. Fitzgerald. Organizing memories for generalization in complementary learning systems. _BioRxiv_ , 2021. 

D. Sussillo, M. M. Churchland, M. T. Kaufman, and K. V. Shenoy. A neural network that finds a naturalistic solution for the production of muscle activity. _Nature neuroscience_ , 18 (7):1025– 1033, 2015. 

R. S. Sutton. Dyna, an integrated architecture for learning, planning, and reacting. _ACM Sigart Bulletin_ , 2(4):160–163, 1991. 

R. S. Sutton and A. G. Barto. _Reinforcement learning: An introduction_ . MIT press, 1998. 

R. M. Tavares, A. Mendelsohn, Y. Grossman, C. H. Williams, M. Shapiro, Y. Trope, and 

D. Schiller. A map for social navigation in the human brain. _Neuron_ , 87(1):231–243, 2015. 

T. J. Teyler and J. W. Rudy. The hippocampal indexing theory and episodic memory: updating the index. _Hippocampus_ , 17(12):1158–1169, 2007. 

E. C. Tolman. Cognitive maps in rats and men. _Psychological review_ , 55(4):189, 1948. 

A. Treves and E. T. Rolls. Computational analysis of the role of the hippocampus in memory. _Hippocampus_ , 4(3):374–391, 1994. 

D. Tse, R. F. Langston, M. Kakeyama, I. Bethus, P. A. Spooner, E. R. Wood, M. P. Witter, and R. G. Morris. Schemas and memory consolidation. _Science_ , 316(5821):76–82, 2007. 

P. A. Tsividis, J. Loula, J. Burga, N. Foss, A. Campero, T. Pouncy, S. J. Gershman, and J. B. Tenenbaum. Human-level reinforcement learning through theory-based modeling, exploration, and planning. _arXiv preprint arXiv:2107.12544_ , 2021. 

B. B. Ujfalussy and G. Orban. Sampling motion trajectories during hippocampal theta sequences. _bioRxiv_ , 2021. 

M. A. Van Der Meer and A. D. Redish. Covert expectation-of-reward in rat ventral striatum at decision points. _Frontiers in integrative neuroscience_ , 3:1, 2009. 

F. Van der Velde and M. De Kamps. Neural blackboard architectures of combinatorial structures in cognition. _Behavioral and Brain Sciences_ , 29(1):37–70, 2006. 

H. P. van Hasselt, M. Hessel, and J. Aslanides. When to use parametric models in reinforcement learning? _Advances in Neural Information Processing Systems_ , 32:14322–14333, 2019. 

A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L . Kaiser, and I. Polosukhin. Attention is all you need. _Advances in neural information processing systems_ , pages 5998–6008, 2017. 

O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung, D. H. Choi, R. Powell, T. Ewalds, P. Georgiev, et al. Grandmaster level in starcraft ii using multi-agent reinforcement learning. _Nature_ , 575(7782):350–354, 2019. 

J. X. Wang, Z. Kurth-Nelson, D. Kumaran, D. Tirumala, H. Soyer, J. Z. Leibo, D. Hassabis, and M. Botvinick. Prefrontal cortex as a meta-reinforcement learning system. _Nature neuroscience_ , 21(6):860–868, 2018. 

J. C. Whittington, T. H. Muller, S. Mark, G. Chen, C. Barry, N. Burgess, and T. E. Behrens. The tolman-eichenbaum machine: Unifying space and relational memory through generalization in the hippocampal formation. _Cell_ , 183(5):1249–1263, 2020. 

24 

J. C. Whittington, J. Warren, and T. E. Behrens. Relating transformers to models and neural representations of the hippocampal formation. _arXiv preprint arXiv:2112.04035_ , 2021. 

J. Widloski and D. J. Foster. Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping. _Neuron_ , 110(9):1547–1558, 2022. 

A. M. Wikenheiser and A. D. Redish. Hippocampal theta sequences reflect current goals. _Nature neuroscience_ , 18(2):289–294, 2015. 

M. A. Wilson and B. L. McNaughton. Reactivation of hippocampal ensemble memories during sleep. _Science_ , 265(5172):676–679, 1994. 

L. Wittkuhn, S. Chien, S. Hall-McMaster, and N. W. Schuck. Replay in minds and machines. 2021. H. Xu, P. Baracskay, J. O’Neill, and J. Csicsvari. Assembly responses of hippocampal ca1 place cells predict learned behavior in goal-directed spatial tasks on the radial eight-arm maze. _Neuron_ , 101(1):119–132, 2019. 

D. L. Yamins, H. Hong, C. F. Cadieu, E. A. Solomon, D. Seibert, and J. J. DiCarlo. 

Performance-optimized hierarchical models predict neural responses in higher visual cortex. _Proceedings of the national academy of sciences_ , 111(23):8619–8624, 2014. 

M. A. Yassa and C. E. Stark. Pattern separation in the hippocampus. _Trends in neurosciences_ , 34(10):515–525, 2011. 

A. M. Zador. A critique of pure learning and what artificial neural networks can learn from animal brains. _Nature communications_ , 10(1):1–7, 2019. 

D. Zeithamova, M. L. Schlichting, and A. R. Preston. The hippocampus and inferential reasoning: building memories to navigate future decisions. _Frontiers in human neuroscience_ , 6: 70, 2012. J. Zhou, M. Montesinos-Cartagena, A. M. Wikenheiser, M. P. Gardner, Y. Niv, and G. Schoenbaum. Complementary task structure representations in hippocampus and orbitofrontal cortex during an odor sequence task. _Current Biology_ , 29(20):3402–3409, 2019. 

25 

