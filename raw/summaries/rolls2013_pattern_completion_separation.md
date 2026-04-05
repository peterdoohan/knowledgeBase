---
source_file: rolls2013_pattern_completion_separation.md
title: The mechanisms for pattern completion and pattern separation in the hippocampus
authors: Edmund T. Rolls
year: 2013
journal: Frontiers in Systems Neuroscience
paper_type: review
contribution_type: theoretical
---

### One-line summary

A theoretical review proposing that the hippocampal CA3 system operates as an autoassociation/attractor network enabling pattern completion for episodic memory recall, while the dentate gyrus performs pattern separation through competitive learning to produce sparse, decorrelated representations.

### Background & motivation

Understanding how the hippocampus supports episodic memory requires explaining two fundamental computational properties: pattern completion (retrieving a complete memory from a partial cue) and pattern separation (storing distinct memories for similar experiences without interference). This paper synthesizes a quantitative theory of hippocampal function developed over decades, specifying the neural mechanisms that implement these computations in different hippocampal subregions.

### Methods

- Theoretical synthesis and computational modeling review
- Quantitative analysis of hippocampal connectivity (synapse counts from anatomical data)
- Mathematical derivation of memory storage capacity in autoassociation networks
- Review of empirical studies testing specific predictions of the theory
- Simulation studies of attractor network dynamics with integrate-and-fire neurons

### Key findings

- **CA3 as autoassociation network**: The CA3 region operates as a single attractor network via extensive recurrent collateral connections (~12,000 synapses per neuron, 2% connectivity), enabling arbitrary associations between spatial and object information and pattern completion from partial cues.

- **Storage capacity**: The maximum number of retrievable memories (p_max) is proportional to the number of recurrent collateral synapses per neuron (C_RC) and inversely proportional to sparseness (a): approximately p_max ≈ 0.2-0.3 × C_RC / a. For CA3 with C_RC = 12,000 and a = 0.02, capacity is ~36,000 memories.

- **Diluted connectivity advantage**: The sparse connectivity (0.04 in rats) minimizes multiple synapses between neuron pairs, which would otherwise distort energy landscapes and reduce memory capacity. Dilution also reduces spiking-related noise and enhances recall stability.

- **Pattern separation in dentate gyrus**: Dentate granule cells perform pattern separation via competitive learning, converting correlated grid cell inputs into sparse, decorrelated place cell representations. Key mechanisms include: sparse mossy fiber connectivity (~46 synapses per CA3 neuron), expansion recoding (1 million dentate cells vs. 300,000 CA3 cells), and sparse firing activity.

- **Dual route to CA3**: The mossy fiber pathway (strong, sparse) dominates during learning to force new random representations, while the perforant path (weaker, more numerous) initiates recall and provides pattern generalization. This separation is necessary because the perforant path alone cannot drive efficient CA3 firing for storage.

- **Backprojection recall**: Hippocampo-cortical backprojections implement a reverse hierarchy of pattern associators that retrieve complete neocortical representations from hippocampal episodic memories, with each stage performing pattern completion to reconstruct the original cortical activity patterns.

- **Temporal order memory**: Rate encoding by "time cells" (neurons firing at different times within a delay period) combined with synaptic adaptation enables sequential attractor transitions that could implement temporal order memory within episodic events.

### Computational framework

The paper employs **attractor network theory** and **autoassociation memory** as the core computational framework. The CA3 network is modeled as a recurrent neural network with Hebbian-modifiable synapses where memory storage occurs through synaptic weight changes according to: δw_ij = k × r_i × r_j'. Pattern completion emerges from the attractor dynamics: the network converges to stored memory states from partial cues by evolving toward energy minima. The framework also incorporates **continuous attractor networks (CANNs)** for spatial representations, where activity packets can be maintained at any location, and **competitive learning** for pattern separation in the dentate gyrus. The theory is quantitative, deriving memory capacity limits and connectivity requirements from statistical mechanics of neural networks.

### Prevailing model of the system under study

Before this paper's synthesis, the hippocampus was understood as critical for episodic memory and spatial processing, with CA3 recognized as having extensive recurrent connectivity suitable for associative memory. Theoretical work by Marr (1971), McNaughton and Morris (1987), and others had proposed autoassociative functions for CA3. However, a comprehensive quantitative theory specifying how different hippocampal subregions contribute distinct computational operations (pattern separation vs. pattern completion), the role of specific anatomical features (mossy fiber sparsity, connectivity dilution), and explicit capacity calculations had not been fully synthesized. The paper builds on prior work by Rolls, Treves, and colleagues developing these theoretical foundations throughout the 1990s and 2000s.

### What this paper contributes

This paper provides a comprehensive theoretical synthesis that:

1. **Unifies hippocampal function** under a quantitative framework where CA3 acts as an autoassociation network for pattern completion and episodic storage, while the dentate gyrus performs competitive learning for pattern separation.

2. **Specifies anatomical mechanisms** linking particular connectivity features (diluted recurrent collaterals, sparse mossy fibers, expansion recoding) to computational functions, with quantitative predictions about synapse numbers and sparseness values.

3. **Derives capacity limits** mathematically, showing how the number of storable memories depends on synaptic counts and sparseness, providing testable predictions (e.g., ~36,000 memories for rat CA3).

4. **Explains why connectivity is diluted** rather than complete, showing that dilution reduces noise, prevents multiple synapse distortions, and maximizes capacity while maintaining attractor stability.

5. **Integrates backprojections** into the theory, specifying how hippocampal recall reconstructs neocortical activity through a hierarchy of pattern associators.

6. **Extends the theory to temporal order memory**, proposing how attractor dynamics with adaptation can encode sequences within episodic memories.

### Brain regions & systems

- **Hippocampal CA3**: Core autoassociation network for episodic memory storage and pattern completion; contains ~300,000 neurons (rat) with ~12,000 recurrent collateral synapses per neuron; operates as a single attractor network enabling arbitrary associations between spatial and object information.

- **Dentate gyrus (granule cells)**: Pattern separation via competitive learning; ~1 million neurons providing expansion recoding; converts correlated grid cell inputs to sparse, decorrelated place-like representations; sparse firing activity enhances CA3 storage capacity.

- **Entorhinal cortex**: Source of inputs to hippocampus; layer 2 projects via perforant path to dentate and CA3; layer 3 projects to CA1; contains grid cells for spatial representation; provides forward projections during encoding and receives backprojections during recall.

- **Hippocampal CA1**: Transforms CA3 outputs for recall to neocortex; performs competitive learning to combine episodic sub-parts; provides efficient retrieval cues for backprojection pathways; may contribute to temporal order memory (though this remains unclear).

- **Parahippocampal gyrus / perirhinal cortex**: Intermediate stage in hippocampal-cortical communication; part of the backprojection pathway for memory recall to neocortex.

- **Neocortical association areas**: Ultimate target of hippocampal recall; includes multimodal areas (superior temporal sulcus), unimodal areas (inferior temporal cortex), prefrontal cortex, and parietal cortex; original encoding activity is reinstated during recall via backprojections.

### Mechanistic insight

The paper presents a **mechanistic theory spanning Marr's three levels**:

**Computational level**: The hippocampus solves the problem of rapid episodic memory formation and retrieval. The computational goal is to store arbitrary associations between arbitrary cortical inputs (e.g., objects with places) and later retrieve complete memories from partial cues. This requires maximizing storage capacity while minimizing interference between similar memories.

**Algorithmic level**: Pattern separation (decorrelation of similar inputs) is implemented by competitive learning in the dentate gyrus, producing sparse, randomized representations. Pattern completion (retrieval from partial cues) is implemented by attractor dynamics in CA3, where recurrent collateral connections with Hebbian-modified weights converge to stored memory states. The perforant path provides pattern generalization during recall initiation, while mossy fibers force new random representations during learning. Backprojections to neocortex implement a reverse hierarchy of pattern associators for cortical reinstatement.

**Implementational level**: The theory specifies concrete biological implementations: sparse mossy fiber connectivity (~46 synapses per CA3 neuron, dilution 0.000046) with large synapses near the soma produces powerful but sparse activation; diluted recurrent collateral connectivity (12,000 synapses, 2% connectivity) minimizes multiple synapse distortions while maintaining attractor dynamics; expansion recoding via 1 million dentate granule cells vs. 300,000 CA3 cells; heterosynaptic LTD for preventing saturation and enabling forgetting; NMDA receptor-dependent LTP at recurrent collateral synapses; graded firing rate distributions (exponential/gamma) increasing sparseness; and neurogenesis providing new random dentate representations.

The paper provides **neural data supporting the algorithm**: CA3 lesions impair one-trial object-place learning and completion from partial cues (Kesner et al., 2008); dentate lesions impair pattern separation for similar spatial locations (Gilbert et al., 2001; McHugh et al., 2007); voltage-sensitive dye imaging shows pattern completion in CA3 slices (Jackson, 2013); CA3 NMDA receptor knockouts impair associative recall (Nakazawa et al., 2002, 2003); and young vs. old dentate granule cells show differential pattern separation vs. completion contributions (Nakashiba et al., 2012).

### Limitations & open questions

- The theory predicts that some effects (e.g., pattern separation requirements) may only manifest when the hippocampus is well-loaded with thousands of memories, which is difficult to test in typical behavioral experiments that use only a few memories.

- The role of CA1 in temporal order memory remains unclear—some evidence implicates CA1, but the theory naturally places temporal sequence storage in the CA3 recurrent collateral network.

- Whether the primate hippocampus operates as a single continuous network (as the theory suggests) or has more modular organization remains to be fully established, though evidence indicates more extensive longitudinal connections in primates than rodents.

- The functional role of adult neurogenesis in the dentate gyrus, while hypothesized to facilitate pattern separation for new memories, requires further experimental validation to establish its quantitative contribution.

- Whether information transfer from hippocampus to neocortex occurs primarily during waking (as proposed) or during sleep remains debated, with different predictions for semantic memory consolidation.

### Connections & keywords

- Key citations: Marr (1971), McNaughton and Morris (1987), O'Keefe and Nadel (1978), Treves and Rolls (1991, 1992, 1994), McClelland et al. (1995), Rolls and Kesner (2006), Nakazawa et al. (2002, 2003), Wills et al. (2005), Leutgeb et al. (2007), McHugh et al. (2007), Kesner (2007, 2013), Hunsaker and Kesner (2008, 2013), Nakashiba et al. (2012), Clelland et al. (2009), Day et al. (2003), Gilbert et al. (2001), Jackson (2013), Jezek et al. (2011), MacDonald et al. (2011), Killian et al. (2012), Jacobs et al. (2013), Battaglia and Treves (1998), Samsonovich and McNaughton (1997), Amit (1989), Hopfield (1982), Hertz et al. (1991), Cerasti and Treves (2010, 2013), Cheng (2013), Lassalle et al. (2000), Lee and Kesner (2004), Rolls and Treves (1998), Rolls and Deco (2002, 2010), Rolls and Stringer (2005), Rolls and Webb (2012), Rolls and Xiang (2005, 2006), Rolls et al. (1997a, 1997b, 1998, 2002, 2005, 2006, 2013), Schultz and Rolls (1999), Schultz et al. (2000), Simmen et al. (1996), Stringer and Rolls (2002, 2006), Stringer et al. (2002a, 2002b, 2004, 2005), Walters et al. (2013), Webb et al. (2011), Deco and Rolls (2003, 2005, 2006), Deco et al. (2005, 2013), Franco et al. (2007), Faisal et al. (2008), Fyhn et al. (2004), Hafting et al. (2005), Hasselmo et al. (1995), Giocomo et al. (2011), Giocomo and Hasselmo (2007), Georges-François et al. (1999), Goodrich-Hunsaker et al. (2008), Gold and Kesner (2005), Gilbert and Kesner (2003), Barkas et al. (2010), Bonelli et al. (2010), Sidhu et al. (2013), Brun et al. (2002), Daumas et al. (2009), De Araujo et al. (2001), Hoge and Kesner (2007), Kesner et al. (2002, 2008, 2012), Lehn et al. (2009), Leutgeb and Leutgeb (2007), Lynch (2004), Markov et al. (2013), Miller (1956), Miller and Wang (2006), Morris (1989, 2003), Morris et al. (2003), Moscovitch et al. (2005), Nakazawa et al. (2004), O'Keefe (1979), O'Keefe and Speakman (1987), Pitkanen et al. (2002), Rajji et al. (2006), Rondi-Reig et al. (2001), Schwindel and McNaughton (2011), Stefanacci et al. (1996), Tonegawa et al. (2003), Treves (1990, 1991, 1995), Van Haeften et al. (2003), Van Hoesen (1982), Wills et al. (2005), Witter (1993, 2007), Witter et al. (2000a, 2000b), Amaral (1987, 1993), Amaral et al. (1990, 1992), Amaral and Witter (1989, 1995), Acsady et al. (1998), Andersen et al. (2007), Lavenex et al. (2004), Lavenex and Amaral (2000), Kondo et al. (2009), Naber et al. (2001), Storm-Mathiesen et al. (1990), Carmichael and Price (1995), Delatour and Witter (2002), Henze et al. (2002), Kropff and Treves (2008), Zilli (2012), Amit and Brunel (1997), Battaglia and Treves (1998), Brown et al. (1989, 1990), Clelland et al. (2009), Day et al. (2003), Fazeli and Collingridge (1996), Fyhn et al. (2004), Giocomo and Hasselmo (2007), Giocomo et al. (2011), Gold and Kesner (2005), Goodrich-Hunsaker et al. (2008), Hafting et al. (2005), Hasselmo et al. (1995), Hoge and Kesner (2007), Hunsaker and Kesner (2008, 2013), Hunsaker et al. (2008), Jackson (2013), Jacobs et al. (2013), Jezek et al. (2011), Jung and McNaughton (1993), Kesner (2007, 2013), Kesner et al. (2002, 2008, 2012), Killian et al. (2012), Lassalle et al. (2000), Lehn et al. (2009), Leutgeb and Leutgeb (2007), Leutgeb et al. (2007), Lee and Kesner (2004), Lynch (2004), McHugh et al. (2007), MacDonald et al. (2011), McNaughton and Morris (1987), McNaughton et al. (1983, 2006), Morris (1989, 2003), Morris et al. (2003), Nakashiba et al. (2012), Nakazawa et al. (2002, 2003, 2004), O'Keefe (1979), O'Keefe and Nadel (1978), O'Keefe and Speakman (1987), Rajji et al. (2006), Rolls (1987, 1989a, 1989b, 1989c, 1990a, 1990b, 1991, 1995, 1996a, 1996b, 1999, 2008, 2010a, 2010b, 2012a, 2012b, 2013, 2014a, 2014b), Rolls and Deco (2002, 2010), Rolls and Kesner (2006), Rolls and Stringer (2000, 2005), Rolls and Treves (1990, 1998, 2011), Rolls and Webb (2012), Rolls and Xiang (2005, 2006), Rolls et al. (1997a, 1997b, 1998, 2002, 2005, 2006, 2013), Simmen et al. (1996), Stringer and Rolls (2002, 2006), Stringer et al. (2002a, 2002b, 2004, 2005), Treves (1990, 1991, 1995), Treves and Rolls (1991, 1992, 1994), Walters et al. (2013), Wang and Morris (2010), Wills et al. (2005), Witter (1993, 2007), Witter et al. (2000a, 2000b), Zhang (1996), Zilli (2012), Amit (1989), Hopfield (1982), Hertz et al. (1991), Kohonen (1977, 1984), Marr (1971), McClelland et al. (1995), Miller (1956), Miller and Wang (2006), Moscovitch et al. (2005), Naber et al. (2001), Amaral (1987, 1993), Amaral et al. (1990, 1992), Amaral and Witter (1989, 1995), Andersen et al. (2007), Lavenex et al. (2004), Lavenex and Amaral (2000), Kondo et al. (2009), Storm-Mathiesen et al. (1990), Acsady et al. (1998), Carmichael and Price (1995), Delatour and Witter (2002), Henze et al. (2002), Kropff and Treves (2008), Faisal et al. (2008), Amit and Brunel (1997), Battaglia and Treves (1998), Brown et al. (1989, 1990), Cerasti and Treves (2010, 2013), Cheng (2013), Clelland et al. (2009), Daumas et al. (2009), Day et al. (2003), De Araujo et al. (2001), Deco and Rolls (2003, 2005, 2006), Deco et al. (2005, 2013), Fazeli and Collingridge (1996), Fyhn et al. (2004), Giocomo and Hasselmo (2007), Giocomo et al. (2011), Gold and Kesner (2005), Goodrich-Hunsaker et al. (2008), Hafting et al. (2005), Hasselmo et al. (1995), Hoge and Kesner (2007), Hunsaker and Kesner (2008, 2013), Hunsaker et al. (2008), Jackson (2013), Jacobs et al. (2013), Jezek et al. (2011), Jung and McNaughton (1993), Kesner (2007, 2013), Kesner et al. (2002, 2008, 2012), Killian et al. (2012), Lassalle et al. (2000), Lehn et al. (2009), Leutgeb and Leutgeb (2007), Leutgeb et al. (2007), Lee and Kesner (2004), Lynch (2004), McHugh et al. (2007), MacDonald et al. (2011), McNaughton and Morris (1987), McNaughton et al. (1983, 2006), Morris (1989, 2003), Morris et al. (2003), Nakashiba et al. (2012), Nakazawa et al. (2002, 2003, 2004), O'Keefe (1979), O'Keefe and Nadel (1978), O'Keefe and Speakman (1987), Rajji et al. (2006), Rondi-Reig et al. (2001), Samsonovich and McNaughton (1997), Schultz and Rolls (1999), Schultz et al. (2000), Simmen et al. (1996), Stringer and Rolls (2002, 2006), Stringer et al. (2002a, 2002b, 2004, 2005), Treves (1990, 1991, 1995), Treves and Rolls (1991, 1992, 1994), Walters et al. (2013), Wang and Morris (2010), Wills et al. (2005), Witter (1993, 2007), Witter et al. (2000a, 2000b), Zhang (1996), Zilli (2012)

- Named models or frameworks: Autoassociation memory, Attractor neural networks, Continuous attractor networks (CANNs), Pattern association networks, Competitive learning networks, Hopfield networks, Marr's hippocampal theory, Treves-Rolls theory of hippocampal function, Complementary learning systems theory

- Brain regions: Hippocampus, CA3, CA1, dentate gyrus, entorhinal cortex, subiculum, parahippocampal gyrus, perirhinal cortex, neocortex (association areas, prefrontal cortex, temporal lobe, parietal cortex, orbitofrontal cortex)

- Keywords: hippocampus, pattern completion, pattern separation, episodic memory, attractor network, autoassociation, competitive learning, dentate gyrus, CA3, recurrent collateral, mossy fibers, perforant path, spatial memory, place cells, spatial view cells, grid cells, memory capacity, diluted connectivity, backprojections, temporal order memory, one-trial learning, NMDA receptors, long-term potentiation, heterosynaptic depression, neurogenesis
