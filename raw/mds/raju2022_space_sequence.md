_2022-12-6_ 

**==> picture [100 x 26] intentionally omitted <==**

## **Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus** 

**Rajkumar Vasudeva Raju, J. Swaroop Guntupalli, Guangyao Zhou, Miguel Lázaro-Gredilla and Dileep George** 

**Fascinating and puzzling phenomena, such as landmark vector cells, splitter cells, and event-specific representations to name a few, are regularly discovered in the hippocampus. Without a unifying principle that can explain these divergent observations, each experiment seemingly discovers a new anomaly or coding type. Here, we provide a unifying principle that the mental representation of space is an emergent property of latent higher-order sequence learning. Treating space as a sequence resolves myriad phenomena, and suggests that the place-field mapping methodology where sequential neuron responses are interpreted in spatial and Euclidean terms might itself be a source of anomalies. Our model, called Clone-structured Causal Graph (CSCG), uses a specific higher-order graph scaffolding to learn latent representations by mapping sensory inputs to unique contexts. Learning to compress sequential and episodic experiences using CSCGs result in the emergence of cognitive maps - mental representations of spatial and conceptual relationships in an environment that are suited for planning, introspection, consolidation, and abstraction. We demonstrate that over a dozen different hippocampal phenomena, ranging from those reported in classic experiments to the most recent ones, are succinctly and mechanistically explained by our model.** 

## **Introduction** 

The hippocampus is known for its role in episodic memory, map-like spatial representations, relational inference, and fast learning – a seemingly disparate set of requirements. Simultaneously, hippocampal cells are categorized into a wide variety of types based on their firing patterns ranging from place cells, splitter cells, time cells, lap cells, event specific representations and exhibit a variety of remapping phenomena in response to environmental changes (Kubie et al., 2020). These phenomena often get characterized using Euclidean spatial concepts such as object vector cells (Bicanski and Burgess, 2020), landmark vector cells (Deshmukh and Knierim, 2013), and distance coding (Deshmukh and Knierim, 2013; Sarel et al., 2017), without a coherent underlying explanation, and remain unresolved with other phenomena like splitter cells (Ainge et al., 2007a,b; Dudchenko and Wood, 2014) and event-specific representations (Sun et al., 2020). Could these divergent requirements and myriad phenomena be explained using a simple set of principles that are computationally grounded, implemented, and easy to understand? Here we show that treating _space as a sequence_ can resolve many of the divergent phenomena ascribed to spatial mapping, and help clarify the connections between spatial, temporal, abstract, and relational representations in the hippocampal complex. 

Treating space as a sequence is a necessity for humans and other animals because they do not have a global positioning system that enables direct sensing of location coordinates. Consequently, they need to acquire and abstract the concepts of locations and space from purely sensory-motor experience. However, sensations from the world are aliased and do not convey locations directly – identical sensations can occur at multiple locations or in different sequential contexts. To develop internal space-like maps from these aliased sensations (as illustrated in the sketch in Fig. 1A), the learning agent has to appropriately split or merge sensations based on sequential contexts (Niv, 2019; 

_Corresponding author(s): dileepgeorge@deepmind.com_ © 2022 DeepMind. All rights reserved 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

Plitt and Giocomo, 2021). Our model, clone-structured causal graph (CSCG), tackles this problem by learning different latent states (called clones) to represent the same observation in different sequential contexts (Dedieu et al., 2019; Eichenbaum, 2004; George et al., 2021), merging or splitting them as necessary. In CSCGs, allocentric "spatial" representations naturally arise from higher-order sequence learning on egocentric sensory inputs, without making any Euclidean assumptions, and without having locations as an input. An organism or an agent can utilize a CSCG for navigation, foraging, context-recognition, and shortcut finding without having to explicitly compute place fields, or having to decode locations. 

Importantly, our model suggests that place field maps need to be interpreted carefully because they overlay sequential responses on to Euclidean maps. Directly characterizing the place field maps in terms of spatial and Euclidean concepts could be a source of anomalies because the underlying phenomena are inherently sequential and dynamic (Warren, 2019). In contrast, CSCG explicates how the learning of sequential contexts gives rise to spatial representations that an agent can use to drive behavior without explicitly representing location coordinates. CSCGs predict the conditions under which place fields are expected to change in response to visible or invisible environmental changes, and when they do not, resolving a variety of phenomena with a simple principle. 

## **Model** 

We consider experimental setups where an agent moves around in an environment and receives local sensations which are aliased in the sense that they do not correspond uniquely to locations in the environment. The environment need not be Euclidean, the agent makes no Euclidean assumptions and does not have access to a map of the environment. If the sensations from the environment are vectors (for example, visual patterns) in a continuous space, they are discretized using a vector quantizer. From a sequence of discretized observations and actions, both of which could be egocentric, an agent has to discover the latent topology of its environment to vicariously evaluate different options for navigation. This is a difficult problem due to the aliasing of the observations and a lack of Euclidean assumptions. 

This can be formulated as the problem of learning a latent graph from aliased observations at its nodes. An agent performs a sequence of actions _𝑎_ 1 _, . . . , 𝑎𝑁_ (with discrete _𝑎𝑛_ ∈{1 _, . . . , 𝑁_ actions}) in an environment _𝐺_ , and as a result of each action, it receives an observation, obtaining the stream _𝑥_ 1 _, . . . , 𝑥𝑁_ (with discrete _𝑥𝑛_ ∈{1 _, . . . , 𝑁_ obs}). The goal is to recover the topology of the environment _𝐺_ from sequences of actions and observations. An environment is defined by a directed multigraph _𝐺_ ≡{ _𝑉, 𝐸_ } with nodes _𝑉_ ≡{ _𝑣_ 1 _, . . . 𝑣𝑁_ nodes } and edges _𝐸_ ≡{ _𝑒_ 1 _, . . . 𝑒𝑁_ edges }. Every node is labeled with a discrete observation. At each time step _𝑛_ , the agent will exist at a node and observe _𝑥𝑛_ to be its label. Multiple nodes can have the same label, so the observation does not identify the node. We use _𝐶_ ( _𝑥_ ) to refer to nodes with label _𝑥_ , also called the _clones_ of _𝑥_ . When an agent at node _𝑣𝑖_ executes an action _𝑎_ , it will transition to _𝑣𝑗_ with probability _𝑃_ ( _𝑣𝑗_ | _𝑣𝑖, 𝑎_ ). Whenever this probability is larger than 0, an associated directed edge from _𝑣𝑖_ to _𝑣𝑗_ is introduced in the graph, labeled with the corresponding action and probability. Note that this means that the graph can contain multiple edges with the same starting and ending node, but labeled with different actions. (This is what makes _𝐺_ a multigraph and not a simple graph). For consistency, all edges originating from the same node and labeled with the same action must have their probabilities sum up to 1. 

For a given sequence of actions, _𝐺_ encodes a distribution over sequences, establishing a connection between temporal sequences and arbitrary (not necessarily Euclidean) topologies. To do this effectively, requires a graph learning mechanism that can merge or split contexts appropriately (Niv, 2019). CSCG achieves this by creating a latent space of clones that has the flexibility to split or merge 

2 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

contexts, and having a smooth parameterization of the graph learning problem. Having the latent space allows the model to represent long-term temporal dependencies (Cormack and Horspool, 1987), and gives it the flexibility that is not available to models that purely concatenate temporal context in the observation space. 

**==> picture [360 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Learning a cognitive map from sequential experience in an environment<br>**----- End of picture text -----**<br>


**==> picture [466 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
allocentric map<br>egocentric<br>actions<br>time<br>B Flexible splitting and merging of states with clones<br>A A D E<br>E<br>A D E B<br>B D<br>F C D' F<br>B D E<br>C<br>first order cloned model with<br>Markov model appropriate merging &<br>training sequences C D F splitting of state  D<br>C Cloned HMM D Neural implementation E CSCG graphical<br>  of a cloned HMM   model<br>zn zn +1<br>latent states an<br>xn xn +1<br>z n z n +1<br>clones<br>observations<br>observations xn xn +1<br>observations<br>egocentric<br>observations<br>clones<br>**----- End of picture text -----**<br>


Figure 1 | **Clone-structured cognitive graph** . **A** . Learning cognitive maps from sequential sensory observations is challenging because observations do not identify locations uniquely. **B** . The cognitive map learning problem can be understood as learning a latent graph from observations emitted at every node, where two different nodes can emit the same observation. The challenge is to learn context-specific representations that will disambiguate sensory observations in the latent space. The observation _𝐷_ occurs in three different contexts in sequences _𝐴_ → _𝐷_ → _𝐸_ (purple), _𝐵_ → _𝐷_ → _𝐸_ (green), and _𝐶_ → _𝐷_ → _𝐹_ (orange) from the environment, a distinction that is not represented in a first-order Markov model. Two of these contexts (purple, and green) correspond to the same latent state, and the third (orange) to a different latent state. Cloning _𝐷_ into multiple latent states allows for flexible merging and splitting of contexts as appropriate. **C** . The cloning structure of dynamic Markov coding can be incorporated in an HMM with a structured emission matrix, the cloned HMM. **D** . Neural implementation of a cloned HMM. Neurons in each column are clones of each other that receive bottom-up input from the same observation. Arrow represent axons, and the lateral connections correspond to the cloned HMM transition matrix. Different sequences are in different colors. **E** . Probabilistic model for CSCG which extends cloned HMMs by including actions. 

3 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

The above definitions result in a precise, action-conditional probabilistic model for sequences. Using _𝑧𝑛_ to represent the (unobserved) node at step _𝑛_ , and adding a simple per-node policy _𝑃_ ( _𝑎𝑛_ | _𝑧𝑛_ ) to also model the actions, results in the CSCG model. The joint probability of a sequence of observations and actions is 

**==> picture [434 x 35] intentionally omitted <==**

depicted as a graphical model in Fig. 1E. Observe that in the action-conditional setting, this corresponds to a hidden Markov model in which the emission matrix is determined by the cloning structure and fixed, which improves its learnability. The model supports causal semantics (Pearl, 2009) and learning from interventions (Eaton and Murphy, 2007a; Peters et al., 2017). A learned transition matrix is a directed multi-graph, and reusing this transition matrix and the cloning structure to remap to a new environment can be considered as learning using soft interventions (Eaton and Murphy, 2007b). 

Inference and learning in CSCG can be achieved using biologically plausible mechanisms. The clones in CSCG can be represented by an assembly of neurons. Message-passing inference in CSCG is computationally cheap and biologically plausible using simple integrate-and-fire neurons (Rao, 2004). Learning is achieved using Expectation Maximization (EM) which maximizes the likelihood of the model using a local update mechanism analogous to spike timing dependent plasticity (Nessler et al., 2009, 2013). 

## **Results** 

|**Experiment**|**Phenomena**|**Publications**|
|---|---|---|
|Geometry changes|Place feld remaps as determined by<br>geometry|O’Keefe and Burgess(1996)|
|Visual cue rotation|Place feld rotates with cue card|Muller and Kubie (1987)|
|Barrier addition|Place feld disruption near barrier|Muller and Kubie (1987)|
|Landmark vector cells|Place feld remaps w.r.t a landmark|Deshmukh<br>and<br>Knierim<br>(2013)|
|Linear track|Place feld remaps w.r.t start and end<br>of the track|Sheehan et al.(2021)|
|Directional place felds|Place feld remapping is sensitive to<br>movement direction|O’Keefe and Burgess(1996)|
|Laps on a track|Event specifc rate remapping and lap<br>cells|Sun et al.(2020)|
|Four connected rooms|Place felds are unafected by closed<br>doors|Duvelle et al.(2021)|
|Two identical rooms|Place felds are repeated in two<br>rooms|Fuhs et al.(2005)|
|Hairpin maze|Direction specifc repetition of place<br>felds|Derdikman et al.(2009)|
|Room size expansion|Place felds expand or stretch based<br>on location w.r.t boundaries|Tanni et al.(2022)|



Table 1 | List of experiments, their observed phenomena, and related publications. 

We tested the CSCG model in a variety of experimental settings. The first set of experiments investigated the ability of a CSCG to learn latent topologies from perceptually aliased observation 

4 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

sequences, ability to represent multiple maps in the same model, and the ability to transitively stitch global maps from disjoint overlapping experiences. Furthermore, we investigated the ability of the model to use previously acquired structural knowledge to guide behavior in novel environments. All these properties are important for the performance of an animal. The second set of experiments investigated CSCG’s ability to reproduce and explain a broad set of well known experimental phenomena from the hippocampus (see Table 1). These phenomena can be broadly divided into spatial, geometry-related, and landmark-related remapping (Deshmukh and Knierim, 2013; Muller and Kubie, 1987; O’Keefe and Burgess, 1996; Sheehan et al., 2021), phenomena with both spatial and temporal components (O’Keefe and Burgess, 1996; Sun et al., 2020), and place field repetition, distortion, and changes with respect to environmental connectivity (Derdikman et al., 2009; Duvelle et al., 2021; Fuhs et al., 2005). In addition, we performed a set of experiments that serve as testable predictions for CSCG’s ability to explain the mechanisms underlying hippocampal phenomena. 

## **CSCG can construct maps from aliased egocentric observations in diverse environments.** 

CSCGs are successful in learning latent topologies in a variety of environments, including 2D and 3D layouts (Fig. 2A and B) and mazes, from purely sequential aliased random walk observations. In the uniform room example in Fig. 2A, the agent received egocentric visual observations quantized though a vector quantizer, and took egocentric actions, with four possible heading directions in each location. The visible input to the agent depended on its location as well as head direction. Learning in CSCG discovered the latent headings and locations and represented them using separate clones (Fig. 2A)(iii). Each node in the graph (Fig. 2A(iii)) corresponds to a clone, and its color represents the local observation it is attached to. Note that the learning of the transition graph discovered 4 clones per spatial location, this corresponds to the 4 possible headings that an agent can be in (see “Methods” for more details). CSCGs are also able to correctly learn the topology of 3D surfaces (bucky ball, cube) from sequential aliased egocentric observations (Fig. 2B), correctly inferring the latent local and global loop closures. 

While each clone in the transition graph in Fig. 2A(iii) is ‘bottom-up’ responding to the local sensation indicated by the color, that sensation needs to occur in the latent sequential context specified by the transition graph. By representing sequential contexts in the latent space, these clones come to represent variables like locations and heading that are not directly sensed. An experimenter can obtain the place field of a clone by creating a map representing the arena that the agent is moving in, and marking and accumulating the instantaneous activities of the clone at the present ground-truth location of the agent on that map. Examples of such place fields are shown in Fig. 2A(iv). The clones in Fig. 2A(iii) are also head direction sensitive, which corresponds well with the observation in Acharya et al. (2016) that place fields show head direction sensitivity when they are mapped conditioned on head direction. The head direction sensitivity will be strongest in those locations where the animal has very different visual inputs based on the head direction, compared to the locations in the middle where the animal receives the same visual input in all head directions, consistent with contemporary observations about view sensitivity of place fields (Acharya et al., 2016; Jercog et al., 2019; Moore et al., 2021; Muller et al., 1994). While the place field can give rise to the interpretation that the clone is responding to that particular location, this is purely an interpretive convenience for the experimenter. The agent itself has no mechanism by which it can derive a place field from the activity of its neurons. As we show in the next section, the agent does not need to compute place fields to locate itself, nor need to decode locations from the clones to make navigation decisions. 

CSCGs make complex latent transitive inferences during learning, and represent the learned information to enable novel transitive inferences (Eichenbaum et al., 1999). When different overlapping sections of an environment are exposed to the agent in disjoint episodes, CSCGs learn the underlying 

5 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [446 x 445] intentionally omitted <==**

**----- Start of picture text -----**<br>
A From sequential egocentric observations to an allocentric map<br>(i) room (ii) heading dependent observations (iii) learned transition graph (iv) place fields<br>max<br>100<br>heading 1 heading 2<br>heading 3 heading 4<br>sequence of<br>egocentric actions<br>1<br>0<br>sequence of<br>egocentric observations multiple clones per observation<br>B Example CSCGs learnt from random walks on 3D surfaces<br>bucky ball transition graph 4x4x4 cube  transition graph<br>C Latent transitive learning D CSCG learns separate maps in disjoint environments<br>room 1<br>A H G A H G<br>A G<br>B F B F<br>C E<br>C D E<br>C D E<br>room 3<br>learned transition graph<br>learned transition graph<br>observation index firing rate<br>clones<br>maze 1<br>maze 2<br>room 2 room 4<br>maze 3<br>maze 4<br>**----- End of picture text -----**<br>


Figure 2 | **CSCGs learn diverse latent topologies, transitively stitch them, and transfer structure to new environments** . **A** . CSCGs learn allocentric maps from aliased egocentric local observations from a room with uniform interiors (i) even with long runs of the same observation. (ii) Each sensation, shown by the color, is attached to a set of latent states (clones) through the emission matrix. Through learning of the transition matrix, these clones learn to represent different temporal contexts of that sensation. (iii) Learned transition graph among clones. Each clone’s color represents the observation it is attached to. (iv) Activations of the clones as the agent navigates the room can be used to compute their place fields, which reveal the spatial locations they represent. **B** . CSCGs are able to correctly learn the topology of 3D surfaces. Shown are the learned transition graphs with node colors indicating the observation that node is connected to. ( _continued on next page_ ) 

map that stitches together the whole environment (Fig. 2C), including the global loop closures. Even though the agent never experienced a transition from locations in segment _𝐴_ to locations in segment _𝐹_ during training, the learned map enables correct inferences between all pairs of such locations, such as the path from segment _𝐹_ to segment _𝐴_ being shorter via segment _𝐻_ as opposed to via segment 

6 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

Figure 2 ( _continued_ ) | **Properties of CSCGs** . **C** . An agent experiences four overlapping rooms in disjoint sequential episodes. _𝐴, 𝐶, 𝐸, 𝐺_ are the overlapping segments and _𝐵, 𝐷, 𝐹, 𝐻_ are exclusive to the rooms. CSCG learning stitches together the disjoint experience into a coherent global map. **D** . An agent experiences multiple sequential episodes sampled from four non-overlapping mazes. In this case, CSCG learning correctly learns separate maps for each maze. 

_𝐷_ . When environments are really disjoint, CSCGs learn to separate the maps, and simultaneously represent multiple maps in memory without being explicitly instructed about map boundaries during training (Fig. 2D). The appropriate map can then be recalled as hidden state inference (Sanders et al., 2020b), and used to guide behavior. 

## **Replay-based planning and schema-based transfer enable shortcut inference in dynamic settings** 

A behaving agent can keep track of its state as the most likely clone given past observations, without having to invoke any concepts about space or place fields. If the agent wants to navigate to a remembered goal of a visual sensation, the action sequences that achieve this can be inferred directly by clamping the corresponding clones and propagating messages. If the environment is learned correctly, this inference process is exact, and will recover the sequence of actions that will take the agent from the current state to the desired goal. Message-passing based planning in CSCGs is akin to replays in the hippocampus (Ólafsdóttir et al., 2018). A striking advantage of CSCG in comparison to models that purely predict, is that learned maps can be quickly reconfigured to reflect changes in the environment. When a previously passable route is blocked, the corresponding structural modification can be made in the latent graph, and message-passing based inference will utilize this updated information about the environment to navigate around obstacles. 

CSCGs can also transfer prior knowledge to new environments and infer novel shortcut paths through unobserved locations by treating the learned transition graph as a schema (Baraduc et al., 2019; Barry et al., 2006) and learning just the emission matrix. To demonstrate this ability, we first trained a CSCG using aliased observations from a random walk in a room (room 1, Fig. 3A). Next, we placed the agent in an unfamiliar room with the same structure (room 2, Fig. 3B). As the agent walks in the new room, we keep the transition matrix of the CSCG fixed and update the emission matrix with the EM algorithm. Just by walking along the periphery of room 2, the CSCG is able to infer the shortest path between visited locations through previously unvisited locations. Further, if we block the path with obstacles and a planned action fails, the CSCG is able to initiate replanning at the blocked location and reroute to the target (Fig. 3C). Thus, even with partial knowledge of a novel room, an agent can vicariously evaluate the sequence of actions to be taken to reach a destination by reusing the CSCG’s transition graph from a similar, previously experienced room. 

## **Remapping due to changes in overall geometry, visual cues, or landmarks can be explained using sequence learning** 

Changing the interpretation of place fields from explicitly representing spatial locations to representing the sequential context in which a sensation occurs explains a wide variety of place cell remapping phenomena. In the transition graph in Fig. 2A(iii), each state should be interpreted, not as responding to a specific location in the room, but as responding to the specific sequence of observations leading up to that location. As we demonstrate, sequential interpretation of spatial representations can explain a variety remapping driven by changes in geometry, visual cues, transparent or opaque barriers, 

7 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [460 x 463] intentionally omitted <==**

**----- Start of picture text -----**<br>
A   Learn CSCG in room 1 B   Schema reused in room 2 learned<br>room 1 learned transition graph reusable schema room 2 emission matrix<br>1<br>1<br>0<br>56<br>1 obs 9<br>action sequence<br>index<br>C   Shortcut finding with replanning when new obstacles are introduced in room 2<br>initial plan plan after finding obstacle 1 plan after finding obstacle 2 plan after finding obstacle 3<br>target initial start state subsequent start states inferred action failed action<br>D   Visualization of message propagation during planning and replanning<br>unaware of obstacles aware of obstacle 1 aware of obstacles 1,2 aware of obstacles 1,2,3<br>discovered obstacle 1 discovered obstacle 2 discovered obstacle 3 reached target!<br>start target blocked node<br>0 1 no. of steps from start 21<br>probability<br>clone index<br>planning<br>plan execution<br>**----- End of picture text -----**<br>


**==> picture [4 x 57] intentionally omitted <==**

Figure 3 | **Shortcut finding in a novel room** . The learned transition graph of a CSCG trained on one room ( **A** ) can be considered a reusable schema. Given partial observations in a second, novel room with an identical layout ( **B** ), the CSCG can re-use the previously learned latent structure to rapidly navigate around obstacles and find the shortest path to a target ( **C** ). ( **D** ) The graphs in the top row are a visualization of message propagation during planning and re-planning. Messages propagate outward from the starting clone. The first plan is unaware of the obstacles, and the agent discovers an obstacle only when the action sequence is executed (bottom row) and a planned action fails (at a node in black). This initiates re-planning from the new location, and the new plan routes around the obstacle. 

landmarks, distances to start or end locations etc. 

The classic experiments on geometry-change-driven remapping (O’Keefe and Burgess, 1996) can be explained using CSCGs as follows: changing the geometry of a room changes the locations 

8 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [469 x 498] intentionally omitted <==**

**----- Start of picture text -----**<br>
A O’Keefe & Burgess, 1996<br>clone 314 clone 161 clone 748<br>SS HR<br>max<br>VR LS<br>B Muller & Kubie, 1987 C Deshmukh & Knierim, 2013<br>clone 12 clone 145 clone 179<br>training<br>layout clone 326 clone 720<br>landmark moved 0<br>to a new location<br>D Sheehan et al., 2021<br>sliding start end sliding end start<br>box outbound box box inbound box<br>0 x 18 0 x 18<br>clone 3 clone 7 clone 8 clone 20 clone 18 clone 15<br>0<br>max<br>9<br>0<br>0<br>9<br>0 x 18 0 x 18 0 x 18 0 x 18 0 x 18 0 x 18<br>layout<br>training<br>firing rate<br>layout<br>training<br>cue<br>rotated<br>with<br>barrier<br>offset index<br>track referenced<br>firing rate<br>offset index<br>box referenced<br>**----- End of picture text -----**<br>


Figure 4 | **CSCG can reproduce several place field remapping phenomena** . **A** . Geometric determinants of place fields, O’Keefe and Burgess (1996). A CSCG was first trained using a random walk in the small square (SS) room. Place fields were computed in the training room as well as the horizontal rectangle (HR), vertical rectangle (VR), and large square (LS) rooms. For clone 314, the place field is anchored to the top-left corner and stays the same in all four rooms because the place field of this neuron is determined by the unique visual input at the boundary. Place fields anchored to an edge of the room, however, split into two components when the room is elongated along the corresponding axis - clones 161 and 748 along the horizontal and vertical axes, respectively. ( _continued on next page_ ) 

where similar sequential contexts will be observed. In these experiments, place fields that developed while the rat trained in an arena remapped in a geometry-dependent manner when the arena was 

9 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

Figure 4 ( _continued_ ) | **CSCG can reproduce several place field remapping phenomena** . **B** . Effects of changes in the environment on the spatial firing of hippocampal place cells, Muller and Kubie (1987). A CSCG was first trained using a random walk in a circular room with a cue at the 12 o’ clock position. Place fields were then computed in the training room, the room with the cue rotated by 90°, and the room with a barrier introduced. For each clone, we observe that the place fields also rotate by 90° when the cue is rotated. For most clones, the place fields completely disappear when the barrier is introduced. An exception is clone 179, where the place field in the original layout is sufficiently far away from the barrier. **C** . Landmark vector cells, Deshmukh and Knierim (2013). A CSCG was trained in a rectangular room with a landmark (depicted by a hexagon) on one side of the room. Place fields were then computed in the training room as well as a modified room in which the landmark was moved to a different location. For the modified layout, we observe that the place fields now have two components - one at the same location as the place field in the original layout, and another at the same vector displacement from the new location of the landmark. **D** . A compressed representation of spatial distance in the rodent hippocampus, Sheehan et al. (2021). A CSCG was trained on a linear track of length 18 steps using outbound (left to right) and inbound (right to left) walks. Place fields were computed using trials with different starting positions for the outbound trajectories and different end positions for the inbound trajectories. The top and bottom rows correspond to place fields in the reference frame of the track and the start box, respectively. We observe that most place cells coded for distance from the starting box. A few clones, e.g., clones 8 and 20, are anchored to the end box. Further, clones have gradually widening fields with distance from the starting or ending locations. 

elongated or widened. We demonstrate this by first training a CSCG on a small square (SS) room (size 9 × 9) and uniform interior and observing the place field changes of clones in test rooms that varied in size along the two dimensions (see Fig 4A). The activations of clones in a CSCG represents the posterior distribution over latent states given the past sequence of observations. As described earlier, the specific sequential context in which clones activate can be interpreted as coding for location. Since the interiors of a uniform room have undifferentiated local sequential context, the responses of clones in the center will be anchored with respect to the boundaries because of the relative uniqueness of the observations there. When navigating an elongated room using the CSCG learned from the smaller room, the internal states will reliably signal end-of-room states when the agent is near the boundaries of the new room. This effectively creates two loci for sequential contexts. The same clone that fired in the sequential context corresponding to a specific location in the original room will now fire at two different locations due to the splitting of the sequential contexts in the elongated room, as reflected in the remapped responses of clones 161 and 748 in Fig. 4A. In contrast, the response of clone 314 does not remap and remains the same in all four rooms. This is because this neuron’s sensory input already includes part of the boundary, and also because the sequence it represents has shorter undifferentiated segments from the boundary, making it strongly anchored. Although these results were originally characterized as boundary-vector coding, our results show that the major findings of O’Keefe and Burgess (1996) can be explained using sequence representation without using geometric concepts. As we describe later, the sequence perspective also naturally explains the temporal dependence of the remapped place fields. Of course, with further training in the new environment, the remapping will diminish because new place fields representing the new environment will develop with more experience in that environment. 

The classic Muller and Kubie experiments (Muller and Kubie, 1987) showing a variety of remapping phenomena can also be explained using CSCG, which we illustrate in Fig. 4B. In these experiments, rats were trained in a circular arena with a cue card placed on the wall. Researchers found a variety of remapping phenomena with respect to rotation of the cue card and introduction of opaque or 

10 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

transparent barriers. To investigate these phenomena, we first trained a CSCG in a circular arena with a cue card at the 12 o’ clock position. In this environment, the differentiated sequential contexts will develop with reference to the cue card. When we computed place fields with this CSCG in an arena where the cue was rotated, the place fields also rotated accordingly because they are always referenced to the context and not the absolute location. Placing a barrier in the arena has two effects that destroy the place field for some clones. One effect is that the barrier prevents the agent from taking some trajectories that are important for revealing the relevant sequential contexts for some clones. The second is that the presence of the barrier can change the visual sensation in its vicinity. Both these effects combine to explain why place fields are disrupted when a barrier is placed through its center, and not affected when the barrier is far away. 

CSCGs also explain why place cells can be seen as encoding a vector relationship to local landmarks (Deshmukh and Knierim, 2013). Just like cue cards, or boundaries, landmark objects placed in an environment act as disambiguating contexts with respect to which sensations at other locations are encoded. Thus, when a landmark is moved, some of sequential contexts also move in reference to that landmark. We illustrate this landmark vector remapping phenomenon in Fig. 4C. We first trained a CSCG in a rectangular layout with a landmark on one side of the room. We computed place fields in this layout as well as a modified version in which the landmark was moved to a different location. In the modified layout, the place fields now have two components - one at the same location as in the original layout, and the second at the same relative displacement from the new location of the landmark. 

In more recent experiments (Sheehan et al., 2021), rats were trained on outbound and inbound traversals on a linear track that could be changed in length. Responses to the appropriate sequential contexts in a CSCG naturally explain the remapping of place fields observed as the track length varies. To demonstrate this, we first trained a CSCG on a linear track of length 18 steps using both outbound (left to right) and inbound (right to left) walks. We then computed place fields separately on outbound and inbound trajectories, for various track lengths (Fig. 4D). We observed that most clones coded for distance from the starting position. The place fields gradually widened with distance from the starting position reflecting the growing uncertainty in the distance from the starting point. There were also clones anchored to the end point of the trajectories. 

## **Sequence representation can explain puzzling phenomena that mix spatial and temporal effects** 

Sequential contexts naturally explain the direction sensitivity of place field remapping reported in O’Keefe and Burgess (1996). When the room is elongated, some place fields that were unimodal in the original room remapped to produce two peaks, corresponding to two subcomponents in the elongated room. It was observed that these peaks were direction sensitive: the left subcomponent was active during rightward travel and vice versa. We tested CSCG for the same effects using the same settings as in Fig. 4A, by plotting the fields conditioned on the direction of travel. In the HR room, rightward and leftward trajectories of the agent strongly activated the left and right peaks of the place field, respectively, as shown in Fig. 5A. This is because only one of the sequential contexts that activate a clone occurs in a directional walk, which is a natural consequence of representing locations using sequential contexts. In contrast, a purely geometric model like the boundary vector model (Barry et al., 2006) does not offer an explanation for the direction sensitivity of place field remapping. 

CSCG can also explain recently discovered phenomena like event-specific rate remapping (ESR) cells (Sun et al., 2020), which signal a combination of location and lap number for different laps around a maze, without postulating special coding mechanisms. Fig. 5B shows a similar setting to an 

11 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [455 x 466] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Directional place fields, O ’Keefe & Burgess, 1996<br>random walk  random walk in<br>in training layout elongated layout directional random walk directional random walk<br>B  Sun et al., 2020 max<br>One trial during training One trial during test time<br>* *<br>lap 1 lap 2 lap 3 lap 1 lap 2 lap 3 lap 4<br>1 1<br>0<br>42 42<br>0 10 20 0 10 20 30<br>Unrolled position in trial Unrolled position in trial<br>clone 13<br>clone 40<br>firing rate<br>cell index cell index<br>**----- End of picture text -----**<br>


Figure 5 | **A** . We reproduce the directional place fields reported by O’Keefe and Burgess (1996). We first trained a CSCG in a square room. In an elongated rectangular room, place fields of clones of the CSCG elongate with two strong peaks (second column from the left). The left peak is located such that its distance from the left wall is the same as in the square room. The same holds true for the right peak relative to the right wall. Further, when we use directional random walks to compute place fields, the two independent subcomponents corresponding to these peaks are revealed. A particular subcomponent is stronger when the walk starts from the wall to which the location of the subcomponent is tied: left and right components in the → and ← walks, respectively. ( _continued on next page_ ) 

experiment in Sun et al. (2020) where a rat runs multiple laps in a looping rectangular track before receiving a reward. We trained a CSCG on trials comprising three laps of a rectangular track with a reward state at the end of the third lap. A CSCG exposed to the sequence of observations from such 

12 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

Figure 5 ( _continued_ ) | **B** . Lap-neurons and event-specific representations. A CSCG was trained on observations from laps in a rectangular maze similar to Sun et al. (2020). The training sequence consisted of three laps followed by a reward state (green ∗) at the end. We also considered test trials with four laps where the reward state was at the end of the fourth lap. We show the place fields computed using the training and test trials, respectively. Rows correspond to clones. The place fields on the training trials show that there are different clones that are maximally active for different laps. But most clones are also partially active at their corresponding location in other laps, similar to the neurophysiological observations in Sun et al. (2020). For the test trials, we observe that the lap three clones are significantly active in both the third and the fourth laps. This additional activation shifted precisely by one lap reflects the fact that the third lap is no longer rewarded and that an extra lap is needed to receive a reward. 

trials learned to distinguish the laps and to predict the reward at the end of the third lap, without the help of any explicit lap-boundary markers in the training sequence. This is reflected in the place fields of the clones for the training trials (left panel in Fig. 5B) - each clone is maximally active for an observation when it occurs in its specific lap. However, each clone also shows weak activations when its corresponding observation is encountered in other laps, a signature of ESR. This occurs naturally in the CSCG due to smoothing and the inference dynamics. CSCGs can also explain the remapping of ESR cells. We computed place fields on test trials comprising four laps, instead of three, in which the the reward was at the end of the fourth lap. The lap three clones were strongly activated in both the third and the fourth laps, reflecting the change in when the reward state is reached (right panel in Fig. 5B). 

## **CSCG can predict what kinds of changes in the environment lead to remapping** 

CSCGs show that environmental connectivity changes need not lead to place field remapping even when the agents’ behavior shows adaptation to the change, a phenomenon that researchers found puzzling. In Duvelle et al. (2021), rats ran in a 4-room maze where the doors connecting the rooms could be selectively locked to change the connectivity of the arena. The agent’s behavior reflected that it recognized the connectivity changes of the environment, but the place fields did not remap in response to these connectivity changes. The authors found this lack of remapping puzzling and argued that place cells do not encode a topological map. However, CSCGs show that place cells can encode global location in their activations, global topology in the cell-to-cell connectivity, and still not show remapping in response to the manipulations in Duvelle et al. (2021). 

To demonstrate this, we trained a CSCG using a random walk in an environment comprising four square rooms that are connected by two-way doors, similar to the experimental setting in Duvelle et al. (2021). Each room had visual cues that distinguished it from the other rooms. CSCG learned the global topology of the arena in the transition matrix, and the activation of clones corresponded to locations, as in previous experiments (Fig. 6A top row). We then tested for two environmental modifications used in Duvelle et al. (2021) - (i) one door was locked both ways effectively creating a blockade, and (ii) all doors were locked in one way allowing only an anti-clockwise direction of traversal in the environment. The corresponding modifications were made in the CSCG transition matrix by modifying the connections appropriately, and planning routes in this modified CSCG corresponded to the reported successful navigation. We then computed place fields using the appropriately modified CSCGs paired with the arena connectivity changes, and compared these to the fields from the original CSCG in the original arena. In Fig. 6A, we show that the place fields were the same across all three settings, consistent with the observations in Duvelle et al. (2021). 

13 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

The reason for lack of remapping can be understood by realizing that the connectivity change blocked paths without any change in the visual cues. The blocked path affected only a few of the potential sequences that were responsible for that place field, a change that is too small to be reflected in the aggregated sequential responses. However, the connectivity change can still lead to large changes in behavior, for example, in navigation between the two rooms. In CSCGs, those changes will be reflected in the replay messages used for planning, and in the computed shortest paths. 

## **Sequence learning explains place field repetition, size and shape variations.** 

Place fields distort along the boundaries, and increase in size systematically towards the center of an empty arena (Tanni et al., 2022). In very elongated rooms, place fields have multiple lobes. In some settings, place fields are known to repeat in identical rooms (Fuhs et al., 2005; Skaggs and McNaughton, 1998). While all these phenomena appear to be spatial, CSCGs provide cogent explanations for these in terms of sequence learning: all of them result from state aliasing due to the difficulty in creating different latent states for temporal contexts that are identical for long number of steps. 

To demonstrate place field repetition in visually identical environments, we trained a CSCG in a layout comprising two visually identical rooms in the same orientation and connected by a corridor, as shown in Fig. 6B, similar to the setting in Fuhs et al. (2005). Place fields computed in this layout show repetition, i.e., clones are active at the same location in both rooms. We also considered a layout in which the two rooms were abutted by rotating them such that their orientations differed by 180°. In Fuhs et al. (2005), it was reported that place field repetition disappears in the differentorientation setting. This was attributed to the rats potentially being able to maintain their inertial angular orientation. With CSCGs, in the absence of an external “compass”, we observe that place field repetition persists in the modified layout, even after the introduction of an asymmetric connection between the two rooms. However, when the CSCG was retrained on the different-orientation setting with an asymmetric connection between the rooms, it was able to partially split contexts in the two rooms. This resulted in unique place fields for most clones, as show in Fig. 6C. If the sensory input to CSCG is augmented with an external head direction input, then the different orientation setting results in unique place fields in CSCGs, similar to what is observed in Fuhs et al. (2005). 

In Fig. 6D, we reproduce the direction-dependent place field repetition reported in Derdikman et al. (2009). We trained a CSCG on a hairpin maze, with distinct end markers, using left to right ( _𝐿_ → _𝑅_ ) and right to left ( _𝑅_ → _𝐿_ ) walks. Place fields computed using this CSCG using only _𝐿_ → _𝑅_ or _𝑅_ → _𝐿_ walks reveal direction dependent place field repetition, as shown in Fig. 6D. For example, clone 17 is activated at the same location in all segments of the maze, but only in the _𝐿_ → _𝑅_ traversal. The two ends of the maze have different observations, which provides the CSCG enough context to disambiguate the two directions of travel. However, for each direction of traversal, the observations are the same in all segments of the maze resulting in the repetition of place fields. 

To study the effect of room size on place fields (Tanni et al., 2022), we trained three different CSCGs on square rooms, with uniform interiors, of side length 7, 9 and 11, respectively. As an agent moves away from the boundaries to the center of an empty room, different sequential trajectories start to look the same, making it difficult for the learning algorithm to split the contexts into different clones. This results in the same clone representing more contexts than it would in the periphery of the room where contexts can be easily distinguished. In place field mapping, this will appear as an enlargement of the place fields in the center of the room (“center” column in Fig. 6E). Similarly, the observations along the edge of a room might not all develop into distinct clones, resulting in multiple observations along the edge being aliased into the same clone. This aliasing, due to the elongation of the same evidence, will appear as an elongation of the place field (“edge” column in Fig. 6E). 

14 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [469 x 397] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Duvelle et al., 2021 B Fuhs et al., 2005<br>clone 311 clone 196 clone 77 clone 23<br>max<br>C Retrain with asymmetric connection<br>clone 65 clone 16<br>D Derdikman et al., 2009 E Room size experiments<br>corner edge center<br>L to R 0<br>clone 17 clone 43<br>R to L<br>layout<br>training<br>layout<br>training<br>rotated<br>both ways<br>1 door locked<br>rotated<br>w/ asym.<br>all doors<br>locked 1 way layout firing rate<br>training<br>7 x 7<br>9 x 9<br>11 x 11<br>**----- End of picture text -----**<br>


**==> picture [129 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
D Derdikman et al., 2009<br>**----- End of picture text -----**<br>


Figure 6 | **CSCG can reproduce various observations about place cells such as place field repetition and size, shape variations. A** . Hippocampal place cells encode global location but not connectivity in a complex space, Duvelle et al. (2021). A CSCG was first trained in a layout comprising four square rooms that are connected by two-way doors. Place fields were computed in the training layout and two modified layouts - (i) one door locked both ways, and (ii) all doors locked one way. We observe that place fields remain the same across all three settings. **B** . Place field repetition in visually identical environments. A CSCG was first trained on a layout comprising two identical rooms in the same orientation connected by a corridor. The behavior of the CSCG was then studied in a layout where the two rooms were abutted by rotating them such that their orientations differed by 180°. We also considered a second modification, where we introduced an asymmetery in the connection between the abutting rooms. In all these three layouts, we observed place field repetition across the two rooms. Note that these results are incongruent with those in Fuhs et al. (2005), where they observed place field repetition only in the same orientation layout. **C** . However, when we retrain a CSCG in the opposite orientation layout with asymmetric connectivity, we observe that the place field repetition disappears. ( _continued on next page_ ) 

Place field size expansion (Tanni et al., 2022) in an empty arena happens because of the same reason as place field repetition in two identical iso-oriented rooms. Both can be explained by the inability of the model to split very long-term temporal contexts into distinct latent clones with the 

15 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

Figure 6 ( _continued_ ) | **CSCG can reproduce various observations about place cells such as place field repetition and size, shape variations** . **D** . Direction dependent place field repetition in a hairpin maze, Derdikman et al. (2009). A CSCG was trained using _𝐿_ → _𝑅_ and _𝑅_ → _𝐿_ walks on a hairpin maze. Place fields were then computed using only _𝐿_ → _𝑅_ (top row) or _𝑅_ → _𝐿_ (bottom row) walks. We observe direction dependent repetition of place fields. **E** . Place field size and shape as a function of room size, Tanni et al. (2022). We trained three different CSCGs on square rooms, with uniform interiors, of side length 7 _,_ 9 and 11, respectively. The capability of a CSCG to learn the map of a room with uniform interior degrades as the room gets larger. This is reflected in the place fields. Place fields that are anchored to the corner of the room retain their size and shape across sizes. However, place fields at the edge and center of the room elongate and become larger as the room size increases. 

given amount of training. (Of course longer training will partially overcome this problem, which is observed in animals as well.) In that sense, larger place fields are the same as place field repetition, just happening in adjacent locations. 

**==> picture [467 x 295] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Place fields in rooms with random vs. checkerboard patterns<br>corner edge center<br>max<br>B Influence of local landmarks during room elongation 0<br>clone 15 clone 128<br>random<br>firing rate<br>checkerboard<br>layout<br>training<br>layout<br>elongated<br>**----- End of picture text -----**<br>


**B Influence of local landmarks during room elongation** 

Figure 7 | **CSCG based predictions about place fields** . **A** . What controls place field change is not the rate of visual field change, but the uniqueness of the visual context. We observe that a CSCG trained on the checkerboard room has more expanded place fields compared one trained on a room with a random pattern. **B** . Influence of local landmarks during a room elongation experiment. We first trained a CSCG on a rectangular room with local landmarks on one side of the room. We computed place fields in the training room and an elongated room in which the landmarks are in the same position as the training room. Place fields anchored to the landmark (clone 15) stay the same in both layouts, but place fields sufficiently far from the landmarks expand in the elongated layout (clone 128). 

16 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

## **Novel experiments and predictions** 

CSCGs can also make experimentally testable predictions for yet to be observed phenomena. One such prediction is the following. What controls how place fields change is not the rate of visual change, but the uniqueness of the visual context. To demonstrate this, we trained two CSCGs on square rooms with checkerboard and random patterns on the floor, respectively. We observed that the place fields in the checkerboard room were more expanded, as shown in Fig. 7A. This is because the same context repeats throughout the interior of the room, making it difficult for the learning to split the contexts 

CSCGs provide a mechanistic explanation for the question of when and why do place fields globally or partially remap? The answer: place cell responses are driven by their sequential contexts, and changes that significantly affect the sequential context of a neuron is what determines when and how its field will remap. Any change that makes the same sequential context occur in different parts of the room, will result in that field partially appearing in the new place. The organization and specificity of local context driving the responses of a cell will have a significant impact on its remapping. A cell that is tuned to sequences in the middle of a uniform room, will have its place fields anchored by the boundaries that are relatively more unique, causing the field to remap when when the boundaries are moved. However, if the cell had some other local cues, for example markings on the floor, that would provide it a unique sequential context, then the cell’s field will not remap when the boundary is moved. In Fig. 7B, clone 15 and clone 128 are two cells from the CSCG trained in the training layout. When the the room is elongated, the place field of clone 128 remaps as shown. This is because the local sequential context for clone 128 was anchored by the cyan marking on the left and the boundary on the right. These partial contexts occur in two different place in the elongated room. In contrast, the local sequential context for clone 15 is anchored by the blue marking on its left and the cyan marking on its right, and those did not change when the room was elongated. This means, locally, clone 15 will see the same sequential contexts after room elongation, resulting in a lack of remapping in its place field. 

## **Discussion** 

The discovery of place cells is a striking success of hippocampus research, and place field mapping has served as a valuable tool in revealing the representational properties of neurons in the HPC. However, anomalies have been accumulating over the simple view that place cells represent just locations (Acharya et al., 2016; Buzsáki and Llinás, 2017; Sun et al., 2020). Place fields distort around boundaries, and split along trajectories. They are direction sensitive (Acharya et al., 2016; Moore et al., 2021), and can even represent the lap count in running loops (Sun et al., 2020). In some cases, insertion of a boundary in between a place field clearly disrupts the place field, suggesting that fields are related to the connectivity of the underlying environment (Muller and Kubie, 1987). Yet, place fields can remain unchanged when the connectivity of the environment changes without any visible cues (Duvelle et al., 2021). If the environmental change is not reflected in place fields, how are the rats able to change their behavior in the new environment? In summary, many of these questions about the role of place cells – what they represent, how those representations are learned, how they are used, and how they change with respect to environmental manipulations remain unanswered in the location-centric description of hippocampal neurons. 

In this paper, we pursued the strong hypothesis that the hippocampus performs a singular algorithm that learns a sequential, relational, content-agnostic structure of its environment (Buzsáki and Llinás, 2017; Dabaghian et al., 2014), and demonstrated evidence for its validity. Our learning model, the CSCG, inverts the observation stream to learn a latent generative model that is producing the stream 

17 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

of sensations. With CSCGs, we demonstrated how a vast variety of experimental observations about hippocampal place cells can be explained by the singular key insight that spatial representation is an emergent property of latent higher-order sequence learning. We demonstrated this by first showing that pure temporal learning is sufficient to acquire cognitive maps that have locations, space, heading etc. We also showed how such latent graphs can transfer knowledge across environments. And finally, we showed that multiple phenomena that we observe are natural byproducts of sequence learning and inference, without having to directly model the phenomena itself. 

While CSCG draws up on many past and contemporary models of hippocampus (Uria et al., 2022), it is significantly different in many aspects. In contrast to temporal context models (TCM) (Howard and Kahana, 2002) that accumulate sequential context in the observation space, the sequential representation in CSCG is in the latent space, giving it the ability to model more complex and long duration temporal dependencies. The ability of CSCG to represent locations as sequences crucially depends up on having a latent representation. Although successor representations (Stachenfeld et al., 2017) can model temporal relations, they are not directly applicable in the aliased settings we consider here, and do not learn spatial representations from egocentric sensory inputs. Contemporary work on Tolman-Eichenbaum machines (TEM) (Whittington et al., 2018) have many similarities to CSCG in inspiration. However, unlike CSCG, TEMs do not learn latent graphs in aliased settings like ours. Instead, TEM focuses on learning general transitivity rules applicable to a single graph from multiple noisy realizations of that graph. Moreover, TEMs do not deal with multiple graphs at the same time (Sanders et al., 2020a), or do latent transitive stitching. In the context of learning spatial representations, TEMs have so far been demonstrated only in allocentric settings. More importantly, TEM is formulated purely as a predictive model and its internal representation does not learn a modifiable graph that corresponds to the environment. Therefore, TEM doesn’t have the same ability as CSCGs to deal with dynamic environments quickly by changing its graph connectivity, or to form hierarchies through community detection (Schapiro et al., 2016) on the latent graph. 

Unlike other computational models of place fields, CSCGs do not use grid fields to learn place fields and still explain varied remapping phenomena. Recent experimental evidence suggests that grid cells are not necessary for learning (Brandon et al., 2014; Tan et al., 2017) and continued functioning of place cells (Brandon et al., 2014). If grid cells outputs are available, CSCG can utilize those as additional sensations. This would speed up learning in the middle portions of empty arenas where unique sensations are not available, and it will also help stabilize the place fields away from the boundaries or other landmark cues (Mallory et al., 2018; Muessig et al., 2015), consistent with the idea of grid cells providing an optional scaffolding for place cells (Mulders et al., 2021). 

The most important message from our work is that many of the diverse fascinating hippocampal phenomena might be artifacts of Euclidean place field mapping. Hippocampal cells are usually interpreted by plotting their responses on to a 2D map corresponding to the environment, collapsing the sequential responses in to a static place field. Characterizing place field maps in terms of Euclidean concepts is akin to characterizing the effects rather than the underlying causes, and might be the source of new phenomena. Often these new phenomena are explained away invoking familiar, but ultimately unsatisfactory, answers like distributed coding, or mixed selectivity. These answers are unsatisfactory because instead of answering the questions they just shift the questions elsewhere. Our experiments show that phenomena that look extremely different – for example place-field expansion in a uniform room and event-specific responses in a lap running – can have the same underlying explanation which can be understood through the sequence learning model. We hope this opens up a new avenue of exploration that takes us away from the familiar questions centered on encoding and decoding locations. 

Much remains to be explored on this new path we have struck out on. We have only briefly touched 

18 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

up on replay based planning, and schemas, and both can be expanded in future research. Our work can also be expanded in the direction of active learning and inference. Reward mechanisms can be layered on top of CSCG. CSCGs have the ability for temporal abstractions via community detection (Schapiro et al., 2016) on the underlying graphs, an idea worthy of more exploration. Current models are learned using random walks. Potentially efficient exploration techniques can be developed as active learning on CSCGs. Most importantly, we hope our work gives a concrete tool that would help hippocampal researchers think beyond the place field paradigm. 

## **Methods** 

## **Expectation-Maximization learning of CSCGs** 

Cloned Hidden Markov Models (HMMs), first introduced in Dedieu et al. (2019), are a sparse restriction of overcomplete HMMs (Sharan et al., 2017) that can overcome many of the training shortcomings of dynamic Markov coding (Cormack and Horspool, 1987). Similar to HMMs, cloned HMMs assume the observed data _𝑥_ 1 _, . . . , 𝑥𝑁_ are generated from a hidden process _𝑧_ that obeys the Markovian property 

**==> picture [271 x 32] intentionally omitted <==**

Here _𝑃_ ( _𝑧_ 1) is the initial hidden state distribution, _𝑃_ ( _𝑧𝑛_ +1| _𝑧𝑛_ ) is the transition probability from _𝑧𝑛_ to _𝑧𝑛_ +1, and _𝑃_ ( _𝑥𝑛_ | _𝑧𝑛_ ) is the probability of emitting _𝑥𝑛_ from the hidden state _𝑧𝑛_ . 

In contrast to HMMs, cloned HMMs assume that each hidden state maps deterministically to a single observation. Further, cloned HMMs allow multiple hidden states to emit the same observation. All the hidden states that emit the same observation are called the _clones_ of that observation. 

CSCGs build on top of cloned HMMs by augmenting the model with the actions of an agent. In this section we first review the expection-maximization learning of cloned HMMs, before describing the learning of CSCGs. 

## _**Expectation-Maximization learning of Cloned HMMs**_ 

The standard algorithm to train HMMs is the expectation-maximization (EM) algorithm (Wu et al., 1983), which in this context is known as the Baum-Welch algorithm. Learning a cloned HMM using the Baum-Welch algorithm requires a few simple modifications: the sparsity of the emission matrix can be exploited to only use small blocks of the transition matrix both in the Expectation (E) and Maximization (M) steps. 

Learning a cloned HMM requires optimizing the vector of prior probabilities _𝜋_ : _𝜋𝑢_ = _𝑃_ ( _𝑧_ 1 = _𝑢_ ) and the transition matrix **T** : **T** _𝑢𝑣_ = _𝑃_ ( _𝑧𝑛_ +1 = _𝑣_ | _𝑧𝑛_ = _𝑢_ ). To this end, we assume the hidden states are indexed such that all the clones of the first emission appear first, all the clones of the second emission appear next, etc. Let _𝑁_ obs be the total number of emitted symbols. The transition matrix **T** can then be broken down into smaller submatrices **T** ( _𝑖, 𝑗_ ) _, 𝑖, 𝑗_ ∈{1 _, . . . , 𝑁_ obs}. The submatrix **T** ( _𝑖, 𝑗_ ) contains the transition probabilities _𝑃_ ( _𝑧𝑛_ +1| _𝑧𝑛_ ) for _𝑧𝑛_ ∈ _𝐶_ ( _𝑖_ ) and _𝑧𝑛_ +1 ∈ _𝐶_ ( _𝑗_ ), where _𝐶_ ( _𝑖_ ) and _𝐶_ ( _𝑗_ ) correspond to the hidden states (clones) of emissions _𝑖_ and _𝑗_ respectively. 

The standard Baum-Welch equations can then be expressed in a simpler form in the case of cloned HMM. The E-step recursively computes the forward and backward probabilities and then updates the posterior probabilities. The M-step updates the transition matrix via row normalization. 

19 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

## **E-Step** 

**==> picture [294 x 29] intentionally omitted <==**

**==> picture [154 x 56] intentionally omitted <==**

**==> picture [36 x 11] intentionally omitted <==**

**==> picture [181 x 52] intentionally omitted <==**

where ◦ and ⊘ denote the element-wise product and division, respectively (with broadcasting where needed). All vectors are _𝑀_ × 1 column vectors, where _𝑀_ is the number of clones per emission. We use a constant number of clones per emission for simplicity here, but the number of clones can be selected independently per emission. Cloned HMMs exploit the sparsity pattern in the emission matrix when performing training updates and inference, and achieve significant computational savings when compared with HMMs. 

## _**CSCGs: Action-augmented cloned HMMs**_ 

CSCGs are an extension of cloned HMMs in which an action happens at every timestep (conditional on the current hidden state) and the hidden state of the next timestep depends not only on the current hidden state, but also on the current action. The joint probability density function on the observations and the actions is given by 

**==> picture [361 x 34] intentionally omitted <==**

and the standard cloned HMM can be recovered by integrating out the actions. 

We group the actions with the next hidden state to remove loops, and create a chain that is amenable to exact inference. In other words, we rewrite the joint probability density function as 

**==> picture [323 x 34] intentionally omitted <==**

Learning a CSCG requires optimizing the vector of prior probabilities _𝜋_ : _𝜋𝑢_ = _𝑃_ ( _𝑧_ 1 = _𝑢_ ) and the action-augmented transition matrix **T** : **T** _𝑢𝑣𝑤_ = _𝑃_ ( _𝑧𝑛_ +1 = _𝑣, 𝑎𝑛_ = _𝑤_ | _𝑧𝑛_ = _𝑢_ ). Similar to cloned HMMs, we can break the action-augmented transition matrix **T** into smaller submatrices **T** ( _𝑖, 𝑘, 𝑗_ ) _, 𝑖, 𝑗_ ∈{1 _, . . . , 𝑁_ obs} _, 𝑘_ ∈{1 _, . . . , 𝑁_ actions}. The submatrix **T** ( _𝑖, 𝑘, 𝑗_ ) contains the transition probabilities _𝑃_ ( _𝑧𝑛_ +1 _, 𝑎𝑛_ = _𝑘_ | _𝑧𝑛_ ) for _𝑧𝑛_ ∈ _𝐶_ ( _𝑖_ ) _, 𝑧𝑛_ +1 ∈ _𝐶_ ( _𝑗_ ), where _𝐶_ ( _𝑖_ ) and _𝐶_ ( _𝑗_ ) correspond to the hidden states (clones) of emissions _𝑖_ and _𝑗_ respectively. All the previous considerations about cloned HMMs apply to CSCGs and the EM equations for learning are also very similar: 

20 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

## **E-Step:** 

**==> picture [304 x 28] intentionally omitted <==**

**==> picture [172 x 55] intentionally omitted <==**

## **M-Step:** 

**==> picture [201 x 52] intentionally omitted <==**

In George et al. (2021), it was observed that the convergence of EM for learning the parameters of a CSCG can be improved by using a smoothing parameter called the pseudocount. The pseudocount is a small constant that is added to the accumulated counts statistics matrix ([�] _𝑛[𝑁]_ =1 _[𝜉][𝑖𝑘𝑗]_[(] _[𝑛]_[)][),][which] ensures that any transition under any action has a non-zero probability. This ensures that the model does not have zero probability for any sequence of observations at test time. 

## **Egocentric actions and observations** 

To demonstrate how CSCGs can reproduce various experimental findings regarding the hippocampus, we consider experimental setups where an agent performs egocentric actions and makes egocentric observations. We assume that the agent is exploring a layout on an axis-aligned grid. At each time step, the agent can perform one of three actions: (i) go forward by one step along its current heading, (ii) turn left by 90°, and (iii) turn right by 90°. Note that the agent’s heading at any given time can only be one of four headings, which we denote by the four cardinal directions. 

The observation of the agent at any given time depends on its position in the layout and its current heading. We assume that the agent has a field of view of length _𝑓𝑙_ and width _𝑓𝑤_ . This field of view is such that the agent can see up to _𝑓𝑙_ − 1 steps in front and 1 step behind it, and is symmetric along the width axis. Fig. 8A shows the four heading dependent observations at the location marked by the black dot in an example 7 × 7 square layout. Inaccessible or invisible regions in the field of view are marked by gray slashes. Fig. 8B shows the set of all possible observations of size ( _𝑓𝑙_ = 4 _, 𝑓𝑤_ = 3) for this example layout. Each possible observation is also assigned a label/index. Fig. 9A (right panel) shows the observation index at each position, for all four possible headings, in the example layout. 

## _**CSCGs in allocentric vs. egocentric settings**_ 

For some of the results used to highlight the properties of a CSCG, we used allocentric actions and observations. In this setting, at each time step, the agent can perform one of four actions: go (i) left, (ii) right, (iii) up, or (iv) down. The observation at each time step is just the color/index of the current location in the layout. 

Here, we compare CSCGs trained using observations and actions in allocentric vs. egocentric settings. We use a square layout of size 7 × 7, as shown in Fig. 8A. For the egocentric setting we use a 

21 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [410 x 119] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Heading dependent observations<br>north east south west<br>102 82 3 84<br>B Set of unique observations<br>**----- End of picture text -----**<br>


**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 18] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [13 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

**==> picture [14 x 17] intentionally omitted <==**

Figure 8 | **Egocentric observations for an example** 7 × 7 **square layout. A** . The four heading dependent observations at the location denoted by the black dot, labeled by the corresponding observation indices. The observation window is of size _𝑓𝑙_ = 4, _𝑓𝑤_ = 3. **B** . The set of all unique observations for this example layout and their corresponding indices. The slashed areas correspond to regions outside the layout that are not visible to the agent. 

field of view of size _𝑓𝑙_ = 4 _, 𝑓𝑤_ = 3. The observation maps for both settings are shown in Fig. 9A. In the allocentric case, the no. of unique observations _𝑁_ obs = 9. In contrast, _𝑁_ obs = 117 for the egocentric setting. Fig. 9B illustrates the observation and action sequence for an example trajectory in both settings. 

In each setting, we collected a stream of 50 _,_ 000 action-observations pairs. We allocated 50 clones per observation, set the pseudocount to 5 × 10[−][4] , and ran EM for a maximum of 1000 iterations to train a CSCG. We then used Viterbi decoding to identify the relevant states/clones that are in use. Fig. 9C shows the learned transition graphs of the CSCGs learned in the two settings. In both cases, each node in the graph corresponds to a clone and its color corresponds to the observation the clone emits. The edges correspond to non-zero probability transitions between clones. In the allocentric case, each spatial location is represented by one clone in the graph. On the other hand, in the egocentric case, each location is represented by four clones corresponding to four possible headings. Importantly, a CSCG is able to learn a graph that correctly represents the topology of the environment in either setting, without any spatial information as inputs during learning. 

## 

Given a sequence of observations and actions, we define the activation of a clone _𝑖_ at time _𝑛_ as the following marginal posterior probability, 

**==> picture [181 x 11] intentionally omitted <==**

Since the CSCG model (with the action _𝑎𝑛_ −1 and hidden state _𝑧𝑛_ collapsed in a single variable) forms a chain, inference on it using belief propagation is exact. The marginal posterior distribution can be 

22 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

**==> picture [468 x 311] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Observation maps<br>Allocentric 9 Egocentric: heading dependent observations<br>100<br>1 north east south west 1<br>B Example random walks<br>Allocentric actions Egocentric actions<br>observations<br>observations<br>time time<br>C Learned transition graphs<br>observation index observation index<br>Allocentric Egocentric<br>**----- End of picture text -----**<br>


**==> picture [132 x 33] intentionally omitted <==**

**==> picture [139 x 38] intentionally omitted <==**

Figure 9 | **Allocentric vs. egocentric settings. A** . Observation maps for an example 7 × 7 square layout in the allocentric (left) and egocentric (right) settings. In the egocentric case, the maps specify the observation index at any given position and heading, for a field of view of size _𝑓𝑙_ = 4, _𝑓𝑤_ = 3. **B** . The sequence of observations and actions for an example trajectory in the two cases. For the egocentric case, the observations include the actual 4 × 3 observation patches (top row) and their corresponding indices (bottom row). **C** . The learned transition graphs for CSCGs trained on the example layout using allocentric (left) and egocentric (right) settings. In both cases, the learned graphs correctly correspond to a 7 × 7 grid. 

computed at each time step as follows, 

**==> picture [264 x 30] intentionally omitted <==**

where ¯ _𝑟_ ( _𝑛_ ) is the unnormalized distribution, _𝑥_ ˜ _𝑛_ is a one-hot encoding of the observation _𝑥𝑛_ , **T** ( _𝑎𝑛_ ) is the transition matrix corresponding to action _𝑎𝑛_ , and _𝐸_ is the clone-structured emission matrix. The ˜ unnormalized marginal distribution at the first time step is computed as ¯ _𝑟_ (1) = _𝜋_ ◦( _𝐸𝑥_ 1). In settings where the observations are noisy or uncertain, _𝑥_ ˜ _𝑛_ can be a distribution over all possible observations. 

To compute place fields, we first obtain activations of the clones from _𝑁_ trials random walks of the agent, each of length _𝑁_ seg, in an environment. We can then use the agent’s ground truth spatial information to compute the average activation of a clone at each spatial location in the environment, thus obtaining its place field. 

23 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

## **Acknowledgements** 

We thank Matt Botvinick, Kimberly Stachenfeld, Dharshan Kumaran, Charles Blundell, Murray Shanahan and Demis Hassabis for critically reading this manuscript and for insightful discussions. 

## **References** 

- L. Acharya, Z. M. Aghajan, C. Vuong, J. J. Moore, and M. R. Mehta. Causal influence of visual cues on hippocampal directional selectivity. _Cell_ , 164(1-2):197–207, 2016. 

- J. A. Ainge, M. Tamosiunaite, F. Woergoetter, and P. A. Dudchenko. Hippocampal CA1 place cells encode intended destination on a maze with multiple choice points. _J. Neurosci._ , 27(36):9769–9779, Sept. 2007a. 

- J. A. Ainge, M. A. A. van der Meer, R. F. Langston, and E. R. Wood. Exploring the role of contextdependent hippocampal activity in spatial alternation behavior. _Hippocampus_ , 17(10):988–1002, 2007b. 

- P. Baraduc, J.-R. Duhamel, and S. Wirth. Schema cells in the macaque hippocampus. _Science_ , 363 (6427):635–639, 2019. 

- C. Barry, C. Lever, R. Hayman, T. Hartley, S. Burton, J. O’Keefe, K. Jeffery, and N. Burgess. The boundary vector cell model of place cell firing and spatial memory. _Reviews in the Neurosciences_ , 17 (1-2):71, 2006. 

- A. Bicanski and N. Burgess. Neuronal vector coding in spatial cognition. _Nat. Rev. Neurosci._ , 21(9): 453–470, Sept. 2020. 

- M. P. Brandon, J. Koenig, J. K. Leutgeb, and S. Leutgeb. New and distinct hippocampal place codes are generated in a new environment during septal inactivation. _Neuron_ , 82(4):789–796, May 2014. 

- G. Buzsáki and R. Llinás. Space and time in the brain. _Science_ , 358(6362):482–485, 2017. 

- G. V. Cormack and R. N. S. Horspool. Data compression using dynamic Markov modelling. _The Computer Journal_ , 30(6):541–550, 1987. 

- Y. Dabaghian, V. L. Brandt, and L. M. Frank. Reconceiving the hippocampal map as a topological template. _Elife_ , 3:e03476, Aug. 2014. 

- A. Dedieu, N. Gothoskar, S. Swingle, W. Lehrach, M. Lázaro-Gredilla, and D. George. Learning higher-order sequential structure with cloned hmms. _arXiv preprint arXiv:1905.00507_ , 2019. 

- D. Derdikman, J. R. Whitlock, A. Tsao, M. Fyhn, T. Hafting, M.-B. Moser, and E. I. Moser. Fragmentation of grid cell maps in a multicompartment environment. _Nature neuroscience_ , 12(10):1325–1332, 2009. 

- S. S. Deshmukh and J. J. Knierim. Influence of local objects on hippocampal representations: Landmark vectors and memory. _Hippocampus_ , 23(4):253–267, 2013. 

- P. A. Dudchenko and E. R. Wood. Splitter cells: Hippocampal place cells whose firing is modulated by where the animal is going or where it has been. In D. Derdikman and J. J. Knierim, editors, _Space,Time and Memory in the Hippocampal Formation_ , pages 253–272. Springer Vienna, Vienna, 2014. 

24 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

- É. Duvelle, R. M. Grieves, A. Liu, S. Jedidi-Ayoub, J. Holeniewska, A. Harris, N. Nyberg, F. Donnarumma, J. M. Lefort, K. J. Jeffery, et al. Hippocampal place cells encode global location but not connectivity in a complex space. _Current Biology_ , 31(6):1221–1233, 2021. 

- D. Eaton and K. Murphy. Exact bayesian structure learning from uncertain interventions. In _Artificial intelligence and statistics_ , pages 107–114. PMLR, 2007a. 

- D. Eaton and K. Murphy. Exact bayesian structure learning from uncertain interventions. In M. Meila and X. Shen, editors, _Proceedings of the Eleventh International Conference on Artificial Intelligence and Statistics_ , volume 2 of _Proceedings of Machine Learning Research_ , pages 107–114, San Juan, Puerto Rico, 21–24 Mar 2007b. PMLR. URL `https://proceedings.mlr.press/v2/ eaton07a.html` . 

- H. Eichenbaum. Hippocampus: cognitive processes and neural representations that underlie declarative memory. _Neuron_ , 44(1):109–120, Sept. 2004. 

- H. Eichenbaum, P. Dudchenko, E. Wood, M. Shapiro, and H. Tanila. The hippocampus, memory, and place cells: is it spatial memory or a memory space? _Neuron_ , 23(2):209–226, 1999. 

- M. C. Fuhs, S. R. VanRhoads, A. E. Casale, B. McNaughton, and D. S. Touretzky. Influence of path integration versus environmental orientation on place cell remapping between visually identical environments. _Journal of neurophysiology_ , 94(4):2603–2616, 2005. 

- D. George, R. V. Rikhye, N. Gothoskar, J. S. Guntupalli, A. Dedieu, and M. Lázaro-Gredilla. Clonestructured graph representations enable flexible learning and vicarious evaluation of cognitive maps. _Nat. Commun._ , 12(1):2392, Apr. 2021. 

- M. W. Howard and M. J. Kahana. A distributed representation of temporal context. _Journal of mathematical psychology_ , 46(3):269–299, 2002. 

- P. E. Jercog, Y. Ahmadian, C. Woodruff, R. Deb-Sen, L. F. Abbott, and E. R. Kandel. Heading direction with respect to a reference point modulates place-cell activity. _Nat. Commun._ , 10(1):2333, May 2019. 

- J. L. Kubie, E. R. J. Levy, and A. A. Fenton. Is hippocampal remapping the physiological basis for context? _Hippocampus_ , 30(8):851–864, Aug. 2020. 

- C. S. Mallory, K. Hardcastle, J. S. Bant, and L. M. Giocomo. Grid scale drives the scale and long-term stability of place maps. _Nat. Neurosci._ , 21(2):270–282, Feb. 2018. 

- J. J. Moore, J. D. Cushman, L. Acharya, B. Popeney, and M. R. Mehta. Linking hippocampal multiplexed tuning, hebbian plasticity and navigation. _Nature_ , 599(7885):442–448, Nov. 2021. 

- L. Muessig, J. Hauser, T. J. Wills, and F. Cacucci. A developmental switch in place cell accuracy coincides with grid cell maturation. _Neuron_ , 86(5):1167–1173, June 2015. 

- D. Mulders, M. Y. Yim, J. S. Lee, A. K. Lee, T. Taillefumier, and I. R. Fiete. A structured scaffold underlies activity in the hippocampus. _bioRxiv_ , 2021. 

- R. U. Muller and J. L. Kubie. The effects of changes in the environment on the spatial firing of hippocampal complex-spike cells. _Journal of Neuroscience_ , 7(7):1951–1968, 1987. 

- R. U. Muller, E. Bostock, J. S. Taube, and J. L. Kubie. On the directional firing properties of hippocampal place cells. _J. Neurosci._ , 14(12):7235–7251, Dec. 1994. 

25 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

- B. Nessler, M. Pfeiffer, and W. Maass. Stdp enables spiking neurons to detect hidden causes of their inputs. _Advances in neural information processing systems_ , 22, 2009. 

- B. Nessler, M. Pfeiffer, L. Buesing, and W. Maass. Bayesian computation emerges in generic cortical microcircuits through spike-timing-dependent plasticity. _PLoS computational biology_ , 9(4), 2013. 

- Y. Niv. Learning task-state representations. _Nature neuroscience_ , 22(10):1544–1553, 2019. 

- J. O’Keefe and N. Burgess. Geometric determinants of the place fields of hippocampal neurons. _Nature_ , 381(6581):425–428, 1996. 

- H. F. Ólafsdóttir, D. Bush, and C. Barry. The role of hippocampal replay in memory and planning. _Current Biology_ , 28(1):R37–R50, 2018. 

- J. Pearl. _Causality_ . Cambridge university press, 2009. 

- J. Peters, D. Janzing, and B. Schölkopf. _Elements of causal inference: foundations and learning algorithms_ . The MIT Press, 2017. 

- M. H. Plitt and L. M. Giocomo. Experience-dependent contextual codes in the hippocampus. _Nat. Neurosci._ , 24(5):705–714, May 2021. 

- R. P. Rao. Bayesian computation in recurrent neural circuits. _Neural computation_ , 16(1):1–38, 2004. 

- H. Sanders, M. Wilson, M. Klukas, S. Sharma, and I. Fiete. Efficient inference in structured spaces. _Cell_ , 183(5):1147–1148, Nov. 2020a. 

- H. Sanders, M. A. Wilson, and S. J. Gershman. Hippocampal remapping as hidden state inference. _Elife_ , 9:e51140, 2020b. 

- A. Sarel, A. Finkelstein, L. Las, and N. Ulanovsky. Vectorial representation of spatial goals in the hippocampus of bats. _Science_ , 355(6321):176–180, Jan. 2017. 

- A. C. Schapiro, N. B. Turk-Browne, K. A. Norman, and M. M. Botvinick. Statistical learning of temporal community structure in the hippocampus. _Hippocampus_ , 26(1):3–8, 2016. 

- V. Sharan, S. M. Kakade, P. S. Liang, and G. Valiant. Learning overcomplete hmms. In _Advances in Neural Information Processing Systems_ , pages 940–949, 2017. 

- D. J. Sheehan, S. Charczynski, B. A. Fordyce, M. E. Hasselmo, and M. W. Howard. A compressed representation of spatial distance in the rodent hippocampus’. _bioRxiv_ , 2021. 

- W. E. Skaggs and B. L. McNaughton. Spatial firing properties of hippocampal ca1 populations in an environment containing two visually identical regions. _Journal of Neuroscience_ , 18(20):8455–8466, 1998. 

- K. L. Stachenfeld, M. M. Botvinick, and S. J. Gershman. The hippocampus as a predictive map. _Nature neuroscience_ , 20(11):1643, 2017. 

- C. Sun, W. Yang, J. Martin, and S. Tonegawa. Hippocampal neurons represent events as transferable units of experience. _Nature neuroscience_ , 23(5):651–663, 2020. 

- H. M. Tan, T. J. Wills, and F. Cacucci. The development of spatial and memory circuits in the rat. _Wiley Interdiscip. Rev. Cogn. Sci._ , 8(3), May 2017. 

- S. Tanni, W. De Cothi, and C. Barry. State transitions in the statistically stable place cell population correspond to rate of perceptual change. _Current Biology_ , 32(16):3505–3514, 2022. 

26 

Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus 

- B. Uria, B. Ibarz, A. Banino, V. Zambaldi, D. Kumaran, D. Hassabis, C. Barry, and C. Blundell. A model of egocentric to allocentric understanding in mammalian brains. _BioRxiv_ , pages 2020–11, 2022. 

- W. H. Warren. Non-Euclidean navigation. _J. Exp. Biol._ , 222(Pt Suppl 1), Feb. 2019. 

- J. Whittington, T. Muller, S. Mark, C. Barry, and T. Behrens. Generalisation of structural knowledge in the hippocampal-entorhinal system. In _Advances in neural information processing systems_ , pages 8484–8495, 2018. 

- C. J. Wu et al. On the convergence properties of the em algorithm. _The Annals of statistics_ , 11(1): 95–103, 1983. 

27 

