Neuroscience and Biobehavioral Reviews 118 (2020) 631–642 

**==> picture [61 x 66] intentionally omitted <==**

Contents lists available at ScienceDirect 

## Neuroscience and Biobehavioral Reviews 

journal homepage: www.elsevier.com/locate/neubiorev 

**==> picture [57 x 73] intentionally omitted <==**

## Review article 

## Towards a computational psychiatry of juvenile obsessive-compulsive disorder 

**==> picture [29 x 29] intentionally omitted <==**

## Alisa M. Loosen[a][,][b][,] *, Tobias U. Hauser[a][,][b][,] * 

> a _Max Planck UCL Centre for Computational Psychiatry and Ageing Research, United Kingdom_ 

> b _Wellcome Centre for Human Neuroimaging, University College London, United Kingdom_ 

|A R T I C L E I N F O <br>_Keywords:_<br>Juvenile obsessive-compulsive disorder<br>Adolescence<br>Neuropsychology<br>Computational psychiatry<br>Neuroimaging|A B S T R A C T|
|---|---|
||Obsessive-Compulsive Disorder (OCD) most often emerges during adolescence, but we know little about the<br>aberrant neural and cognitive developmental mechanisms that underlie its emergence during this critical de-<br>velopmental period. To move towards a computational psychiatry of juvenile OCD, we review studies on the<br>computational, neuropsychological and neural alterations in juvenile OCD and link these fndings to the adult<br>OCD and cognitive neuroscience literature. We fnd consistent difculties in tasks entailing complex decision<br>making and set shifting, but limited evidence in other areas that are altered in adult OCD, such as habit and<br>confdence formation. Based on these fndings, we establish a neurocomputational framework that illustrates<br>how cognition can go awry and lead to symptoms of juvenile OCD. We link these possible aberrant neural<br>processes to neuroimaging fndings in juvenile OCD and show that juvenile OCD is mainly characterised by<br>disruptions of complex reasoning systems.|



## **1. Introduction** 

Most mental health conditions emerge early in life. About half of all psychiatric disorders manifest themselves before the age of 14 and three-quarters by the age of 24 (Kessler et al., 2005). This developmental period is also characterised by significant growth and reorganisation of the brain (Whitaker et al., 2016; Ziegler et al., 2019). Protracted maturation, particularly in areas involved in higher-order cognition, characterises this important developmental stage (Giedd et al., 1999; Tamnes et al., 2017). However, the precise nature of these changes and how they might drive and interact with the maturation of cognitive functions is unclear. Likewise, how a derailing of neurocognitive development may lead to psychiatric disorders such as obsessivecompulsive disorder (OCD) remains unknown. 

The incidence pattern of OCD has a characteristic developmental trajectory that suggests a close link with ongoing neurocognitive maturation (Kessler et al., 2005). By the age of 14, a quarter of all patients express a manifest disorder and only a few develop OCD later in life (American Psychiatric Association, 2013). This highlights the importance of a developmental perspective in order to understand the inner workings of the disorder. 

A thorough investigation of the mechanisms underlying the emergence of OCD is vital for its understanding and treatment. However, 

current OCD research is facing three key problems. Firstly, despite substantial research on adults with OCD, far fewer studies have investigated neurocognitive deficits in juvenile OCD. Secondly, the link between brain, cognition and OCD symptoms is unclear. Several neuroimaging studies have provided insight into abnormalities in frontostriatal loops (e.g. Brem et al., 2012; Hauser et al., 2017b; Menzies et al., 2008) but while links to cognition and symptoms have been made in the adult literature (e.g. van den Heuvel et al., 2009; Kwon et al., 2003; Mataix-Cols et al., 2004) these links are still underdeveloped in juvenile OCD. It is thus unclear how impairments in these neural circuits drive aberrant cognition and give rise to OCD. Thirdly, inconsistent neuropsychiatric findings can be observed both in the adult and Abramovitch paediatric literature, as well as between these two fields ( et al., 2015; Abramovitch et al., 2013; Abramovitch and Cooperman, 2015). 

In this paper, we will address these challenges directly. We will tackle the first problem by projecting well-established findings in adult OCD onto the smaller body of juvenile OCD research, explaining discrepancies and commonalities from a developmental perspective. We will argue that it is possible to close the gap between brain, cognition, and symptoms using methods of computational psychiatry ( _cf._ Box 1), thus addressing the second problem. Lastly, we will present a computational framework that illustrates how the heterogeneity and diversity 

⁎ Corresponding authors at: Max Planck UCL Centre for Computational Psychiatry and Ageing Research, University College London, 10-12 Russell Square, London WC1B 5EH. 

_E-mail addresses:_ a.loosen.17@ucl.ac.uk (A.M. Loosen), t.hauser@ucl.ac.uk (T.U. Hauser). 

https://doi.org/10.1016/j.neubiorev.2020.07.021 

Received 10 January 2020; Received in revised form 14 July 2020; Accepted 18 July 2020 Available online 14 September 2020 0149-7634/ © 2020 Elsevier Ltd. All rights reserved. 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

## **Box 1** 

From neuropsychology to developmental computational psychiatry 

Computational psychiatry uses models from machine learning to understand how aberrant brain processes can lead to mental illness (Adams et al., 2016; Huys et al., 2016). These models describe how a task can be solved algorithmically and which cognitive processes may occur. The processes are often formalised using reinforcement learning (RL; _cf._ Box 2) and/or Bayes’ rule, principles of which many have been found to be implemented in the brain (Parr et al., 2018; Schultz et al., 1997). A key advantage over descriptive, psychological concepts (e.g. cognitive flexibility) is the generative nature of these computational models. This means they make concrete, testable predictions about cognitive processes and behaviour. Using simulations and model fitting, one can predict behaviour and cognitive patterns, which in turn can be used to understand the neurocomputational groundings of mental illness. The computational models help to link aberrant neural processes to cognitive biases and psychiatric symptoms (cf. Fig. 1). After determining the specific computations of brain areas and whether they are altered in patients, we can use the models to investigate how a derailing of such processes may alter cognition and drive psychiatric symptoms. The emerging field of developmental computational psychiatry (Hauser et al., 2019) extends the current efforts and focuses on how computational capacity develops during youth. It investigates how deviation from canonical developmental trajectories can lead to imminent or protracted neurocognitive impairments. 

**==> picture [241 x 341] intentionally omitted <==**

**Fig. 1.** Computational psychiatry allows us to infer mechanisms which generate brain activity, cognition and behaviour in psychiatric patients. It helps us to bridge the gaps between neural implementation (e.g. altered neural systems), cognition (e.g. decision making) and symptoms (e.g. indecisiveness). 

of cognitive deficits (third problem) can be reconciled. 

In what follows, we will review areas of research related to computational psychiatry and examine the current state of research on juvenile OCD and how it relates to adult OCD. Lastly, we will present a computational framework summarising current neurocognitive evidence that provides testable hypotheses and can guide future research. 

## **2. General decision making and reward learning** 

OCD is often cast as a disorder of learning and decision making, but it is unclear whether OCD is characterised by fundamental cognitive 

biases, or whether underperformance is only manifest in more complex tasks and situations. 

The symptomatology of trying to avoid negative outcomes even at high costs (e.g. carrying out compulsions for hours to prevent an unlikely catastrophe) suggests that OCD patients overestimate the likelihood that negative things will happen, or value negative events more negatively (i.e. increased loss/punishment avoidance). While some studies report an increased risk aversion in adult OCD patients (Admon et al., 2012; Sip et al., 2018; Sip et al., 2016), other studies, inter alia in juvenile OCD patients, did not find this (Drechsler et al., 2015; Hauser et al., 2017d; Starcke et al., 2010; Zhang et al., 2015). In particular, computational modelling in juvenile and adult OCD patients found no evidence for altered loss and gain processing, but for altered (value independent) choice perseveration in patients (Hauser et al., 2017b). This suggests these decision-making biases are more complex than simple heightened loss avoidance (Nord et al., 2018). Selective findings showing impaired reward processing may potentially be driven by specific subtypes and/or additional OCD-related psychiatric components such as anhedonia (Abramovitch et al., 2014). However, overall studies in adult OCD patients show more subtle biases, such as a reduced reward sensitivity (Aranovich et al., 2017), or increased randomness for gains (i.e. a violation of subjective-value maximization resulting from choosing an uncertain over a certain option; Pushkarskaya et al., 2017), with some of them replicating in juvenile OCD patients (Norman et al., 2018). This is in contrast to other disorders such as attention-deficit/hyperactivity disorder (ADHD) and depression that have shown a clearer imbalance in reward and punishment sensitivity (Gotlib et al., 2010; Masunami et al., 2009; Tripp and Alsop, 1999). 

Many OCD-related clinical behaviours, such as heightened threat perception that induces compulsions, are often based on experienced, rather than explicitly stated stimulus-outcome associations (e.g. compulsions relieving distress). It has thus been speculated whether patients with OCD suffer from a learning impairment, often investigated using reversal learning tasks. In fact, adult patients have been seen to take longer to perform these tasks on a similar performance level as healthy controls (Chamberlain et al., 2008; Remijnse et al., 2009; Valerius et al., 2008). In juvenile OCD, however, reversal learning studies are more inconsistent (Gottwald et al., 2018; Hauser et al., 2017b; Hybel et al., 2017). 

This heterogeneity is not limited to reversal learning findings, but is also present in other studies reporting on procedural learning (Beers et al., 1999; Ornstein et al., 2010). A key challenge of these tasks is to capture how learning is impaired. Many require complex learning strategies which can go wrong in many different ways. Dissecting the learning mechanisms using computational models may help identify the exact processes that are altered and may help to explain some of the heterogeneity in findings and increase effect sizes. 

A consistent finding in the adult literature is that OCD patients 

632 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

struggle with implicit learning tasks while mastering tasks with explicit instructions (Deckersbach et al., 2002; Rauch et al., 1995; Soref et al., 2018). Implicit learning involves the acquisition and expression of information without awareness (Rauch et al., 1995) and has been seen to rely on brain circuits typically impaired in OCD (Rauch et al., 1995, 2001). Findings show an overtake of explicit learning systems leading to deficiencies in dual-task paradigms (Deckersbach et al., 2002). Thus, the impairment may result from an imbalance in implicit versus explicit systems. 

In line with this, OCD patients seem to consistently struggle with problems of increased complexity without explicit guidelines that require the participant to build a representation of the task structure. Difficulties seem to arise when tasks draw upon certain (learning) processes to master set-shifting and other unpredicted changes in the Chamberlain environment. Such deficits have been found both in adult ( et al., 2006; Gu et al., 2008) and juvenile OCD patients (Britton et al., 2010a,b; Drechsler et al., 2015; Gottwald et al., 2018; Kim et al., 2019; Wolff et al., 2017; Wolff et al., 2018), although not ubiquitously (Beers et al., 1999; Hybel et al., 2017; Ornstein et al., 2010). Most recent work showed that planning seems to be a pre-existing trait marker for paediatric OCD (Negreiros et al., 2020), which underpins the hypothesis that models may not be used or constructed adequately by patients. 

Moreover, deficiencies in adult OCD have mainly been found in the most challenging aspects of learning processes (e.g. extra-dimensional, but not intra-dimensional shifts; Chamberlain et al., 2007b; Chamberlain et al., 2006). In contrast, other patient groups, e.g. schizophrenia and depressed patients, show more consistent difficulties in earlier, simpler stages of such tasks (Ceaser et al., 2008; Jazbec et al., 2007; Nord et al., 2018; Purcell et al., 1997). Recent work has contrasted children with OCD with children with generalized anxiety disorder showing that OCD patients had greater difficulties completing complex planning tasks while patients with general anxiety disorder made more simple reversal learning errors than OCD patients giving insight into the unique difficulties (Kim et al., 2019). 

In summary, OCD (primarily juvenile) patients do not express a clear deficiency in simple decision making or learning but seem to show altered behaviours when completing complex learning problems involving the construction or adaptation of mental task spaces. This specificity of alterations further speaks against an explanation on the basis of cognitive capacity models (e.g. Eysenck and Keane, 2000; Kahneman, 1973), which would predict impairments in all highly 

demanding and complex task. 

## **3. Habits** 

A key domain that is often thought to be aberrant in OCD is (excessive) habitual behaviour. The clinical manifestation of compulsions in OCD are often described as habits (American Psychiatric Association, 2013), behaviours automatically prompted by stimuli and formed through stimulus-action association learning (Andrews, 1903). These can be contrasted with ‘goal-directed’ behaviour that involves complex reasoning and planning to attain a set goal. 

Evidence for a predisposition toward habit formation mainly comes from overtraining studies, that suggest that adult (Gillan et al., 2014a; Gillan et al., 2011; Gillan et al., 2014b) as well as juvenile (Gottwald et al., 2018) OCD patients’ learned behaviour persists in the face of outcome devaluation. In these paradigms, participants first learn a stimulus-action association, which is then removed after overtraining. The habitual system is thereby assumed to only slowly adapt to such changes and thus stick to the previously learned stimulus-response sequence. However, the ability of these paradigms to induce dominant habitual behaviour in humans has been questioned lately suggesting the explanation of the cited findings might rather be an impaired complex reasoning system (de Wit et al., 2018). Moreover, a different line of research has proposed that instead of an overly dominant habitual or impaired goal-directed system, OCD patients might have difficulties arbitrating between systems (Gruner et al., 2016). This hypothesis has been underpinned by neuroimaging findings showing impaired connectivity in the inferior lateral prefrontal cortex (ilPFC) in OCD, an area that plays an important role in cognitive control and complex decisionmaking, and alterations in the frontopolar cortex (FPC) and the anterior cingulate cortex (ACC; Anticevic et al., 2014; Fitzgerald et al., 2005; Harrison et al., 2009; Lee et al., 2014). 

In the context of RL, habitual behaviour is often linked to an excessive model-free learning system, which stands in contrast to a modelbased learning system ( _cf._ Box 2; Dolan and Dayan, 2013). While the latter uses a model of the task and is thus able to learn quickly, the former system relies on experienced rewards and learns slower. The impact of these systems has been studied in adult OCD using a task that allows a dissociation between these two systems by introducing a probabilistic transition structure between different states (Daw et al., 2011). Adult OCD patients have consistently exhibited a relative 

## **Box 2** 

Reinforcement learning as a tool for computational psychiatry 

RL formalises how human and non-human agents take actions to maximise rewarding outcomes (Sutton & Barto, 1988). The agent thereby finds itself in a specific **state** , in a physical or virtual world that is associated with distinct properties (e.g. what was before and what will come next) and possibilities to act (e.g. going left or right). The agent aims to transition to states associated with the highest **rewards** . To do so, it can act upon the world by executing an **action** , which might lead it to another state at the following time step. The optimal action to take is thereby determined by the maximisation of future outcomes, formalised as **state-action values** . Consequently, the agent develops a policy that guides its behaviour. 

A wealth of evidence has shown that humans and other animals exhibit similar behaviours to the ones predicted by RL models (Daw et al., 2011; O’Doherty et al., 2003; Yin et al., 2004, 2005). This makes the algorithms well suited to study (aberrant) decision making and learning in humans. Moreover, brain activity has been found to align well with predictions from RL. The most prominent example is the encoding of reward PEs in firing patterns of the dopaminergic midbrain (Schultz et al., 1997). Here, we use RL to describe and understand cognitive and behavioural differences found in OCD and to speculate about their neurobiological underpinnings, i.e. how and where these processes are embedded. **Model-based and Model-free Reinforcement Learning.** In the present paper, we heavily rely on the premise that the brain incorporates multiple, parallel reasoning systems. These systems’ representation of the world (e.g. a task structure), span a wide range of complexity, from simple motor-outcome associations to complex cognitive models with many unobservable states and state transition. 

Most previous work has been focused on distinguishing only two of these RL systems: **model-based** and **model-free** RL ( _cf._ Fig. 2) (Daw et al., 2005). Model-based RL incorporates a (complex) model of the world, which allows to learn and guide actions most accurately, at the expense of high computing/energy costs. Model-free RL has a very limited model of the world and forms predictions based on experienced outcomes. It caches encountered rewards and slowly builds up expectations about actions and outcomes. While it demands only little computational and memory resources, it is inflexible, generalises poorly and its ability to react to sudden changes in the environment is limited. These two systems can be regarded as extreme prototypes, while recent evidence shows that it is likely that many intermediate systems are embedded in the brain and contribute to our behaviour (Russek et al., 2017; Shahar et al., 2019). 

633 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

**==> picture [361 x 132] intentionally omitted <==**

**Fig. 2.** Complex (model-based) and simple (model-free) reasoning system. The systems represent the world as states (S1-5), actions (taking the bus, cycling, running, looking at the phone, and reading a book) and rewards (R1-3). **The complex reasoning system** (left) incorporates a complex model of the world, which represents the transitions between states and the actions causing the transitions. For a known current state, the system can calculate the likely outcome (R1-3 on the left) of simulated actions in each state. **The simple reasoning system** (right) reduces the representational and computational demands, mirroring a cache rather than a tree system. It only re- 

presents the expected value as a scalar (R1-3 on the right) for each action in each state. It does not take into account the actual transition structure (i.e. action-state sequence) leading to the outcome. 

Gillan deficiency in the model-based system across several studies ( et al., 2011, 2020; Gillan et al., 2016; Gillan and Robbins, 2014; Voon et al., 2015). Recent work by Gillan and colleagues has further shown that factors such as trait and state anxiety failed to explain the consistently observed goal-directed impairments in OCD (Gillan et al., 2016,2020b), suggesting the impairment in these paradigms might be a characteristic of OCD beyond the effects of other important psychiatric dimensions such as anxiety. 

While this association appears to be reliable in adult OCD, research on juvenile OCD patients seems to be inexistent. This research gap is of particular significance because of two reasons. Firstly, current research is unclear on whether excessive habit learning is a cause or consequence of OCD. An excessive habitual system may drive the emergence of compulsive symptoms (Robbins et al., 2012), but it could also be that chronic illness and/or a pre-occupation with OCD-related symptoms drains cognitive resources at the expense of a complex model-based reasoning system. Secondly, the model-based system only matures in late adolescence (Decker et al., 2016; Potter et al., 2017). Hence, it is important to understand whether adolescents with OCD show an intact system compared to peers, or whether an impairment is already manifest. Understanding the developmental trajectories of both OCDsymptoms and the model-based system could thus provide great insight into the directionality of the association. 

First longitudinal findings by Vaghi et al. (in press) in adolescents show that compulsive symptoms precede and drive the emergence of a model-based system deficiency. This suggests that the reduction in model-basedness in adult OCD might be a consequence of obsessivecompulsive (OC) behaviour rather than a driver. It remains to be determined whether the effect is primarily driven by a disorder-related draining on cognitive resources, as increased cognitive load from other sources can reduce the degree to which an individual uses model-based decision making (Otto et al., 2013). Alternatively, an overload of symptoms (e.g. obsession) might also lead to a draining of complex control systems and consequently to observed cognitive and behavioural alterations (Abramovitch et al., 2012; for further critical discussion of the habit theory also see Kalanthroff et al., 2016). Taken together, these findings suggest that reduced model-based reasoning might be a consequence rather than a cause of altered neurocognitive development in OCD during adolescence. 

## **4. Indecisiveness** 

Following insights from clinical observation, several other cognitive symptoms have been investigated, for example indecisiveness (the inability to commit to a decision) which is often reported by OCD patients. One way to experimentally capture indecisiveness is to use tasks in which participants are free to sample as much information as they desire before committing to a choice. In these sequential informationgathering tasks, adult OCD patients have been found to sample more 

information (Fear and Healy, 1997; Pélissier and O’Connor, 2002; Volans, 1976; Voon et al., 2017), although not ubiquitously (Chamberlain et al., 2007a; Grassi et al., 2015). 

Indecisiveness seems to be a feature present early on in the disorder. Information gathering and thus indecisiveness, was found to be exaggerated in juvenile OCD patients (Erhan et al., 2017; Hauser et al., 2017d). Moreover, indecisiveness seems to be a marker of compulsivity as a dimension. Non-clinical subjects with high obsessive-compulsive traits have shown a level of indecisiveness intermediate to the level associated with OCD patients and low compulsive subjects (Hauser et al., 2017c). 

The cognitive mechanisms underlying this indecisiveness have recently been investigated using computational modelling. Hauser et al. (2017d) found that the excess in information sampling was associated with lower subjective costs for sampling information. These costs can be cast as an urgency signal (Cisek et al., 2009), which is delayed in high compulsive subjects and juvenile OCD patients (Hauser et al., 2017d; Hauser et al., 2017c). This signal modulates a decision threshold and thus explains why OCD patients were less inclined to commit to a decision earlier. Importantly, participants along the compulsivity spectrum were matched on other psychiatric dimensions such as anxiety and depression (Hauser et al., 2017c). Thus, these findings were characteristic for compulsivity independent from alternative psychiatric dimensions, indicating that there may be factors contributing to OCD that go beyond the factors contributing to e.g. anxiety and depression. 

It is not entirely clear whether and how a similar indecisiveness mechanism is driving differences observed in perceptual decision making. Several studies showed that adult OCD patients and high compulsive subjects need to accumulate more perceptual evidence to arrive at a decision (Banca et al., 2015; Hauser et al., 2017c). Erhan et al. (2017) found that juvenile OCD patients accumulated more sensory evidence for a longer time before making a decision to achieve a certain performance level. This could at least in part be driven by elevated decision thresholds that collapse more slowly (Erhan et al., 2017; Hauser et al., 2017d), similar to above-mentioned information gathering findings. 

Thus, there is relatively consistent evidence for elevated indecisiveness, both in juvenile and adult OCD patients. This cognitive bias seems to be characteristic of OCD and further differentiates it from other disorders such as schizophrenia, which show the opposite behaviour (Ermakova et al., 2019; Evans et al., 2015). 

## **5. Confidence** 

A separate line of research in adult OCD has focused on confidence. When external feedback is unavailable, the feeling of confidence serves as an internal appraisal signal. Confidence is often operationalised as the evidence strength in favour of a decision (Kiani et al., 2014). A miscalibration of this signal (i.e. overconfidence or underconfidence) is 

634 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

assumed to contribute to aberrant decision making and has been suggested to drive OCD symptoms, such as repetitive checking (Cuttler et al., 2013). 

Multiple studies showed lowered confidence ratings in patients with OCD, but to our knowledge only in adult patient populations. Low confidence in OCD has been found across multiple cognitive domains, such as general knowledge (Dar, 2004; Dar et al., 2000), memory (Boschen and Vuksanovic, 2007; Moritz et al., 2007; Tuna et al., 2005), and perception tasks (Sarig et al., 2012), as well as in the evaluation of internal states (Lazarov et al., 2014). Impaired confidence processing further seems to be a potential root for specific OCD symptoms (Boschen and Vuksanovic, 2007; Zitterl et al., 2001). For instance, diminishing confidence in a task via false feedback was predictive of doubt and checking urges (Cuttler et al., 2013). In turn, repeated checking reduced confidence but not performance (Radomsky et al., 2014). This suggests there might be a bidirectional link between low confidence, decision making and OCD symptoms that could constitute a driving force in the development of the disorder. 

However, investigating confidence along the compulsivity spectrum, while excluding the factor of anxiety and depression, Rouault et al. (2018) as well as Seow and Gillan (2020), showed that high compulsivity was associated with increased confidence ratings. This is not in contradiction to mentioned findings of lowered confidence, but rather adds new detailed insight suggesting that lowered confidence in OCD might in fact be driven by anxious and depressive symptoms and related comorbidities. 

A key function of confidence is to track one’s performance and to inform subsequent decision-making processes. It is therefore critical to assess the relationship between performance and confidence. It could well be that OCD patients solely display a lowered average confidence (i.e. confidence bias), but accurately track their performance (i.e. display lower confidence when they are wrong and higher confidence when they are correct). Alternatively, the mapping of performance onto confidence could be corrupted (i.e. metacognitive impairment), which would be detrimental for their decision making (Fleming and Lau, 2014). 

To our knowledge, only two studies have investigated metacognition in adult compulsive subjects so far. Both found that subjects with high obsessive-compulsive symptoms had reduced metacognitive ability. This means their confidence was less indicative of their actual performance (Hauser et al., 2017a; Rouault et al., 2018). Metacognitive impairments have also been shown in compulsivity independently of anxiety or depression (Hauser et al., 2017a) suggesting it might be a characteristic of OCD beyond other psychiatric dimensions. Interestingly, a mismatch between action and confidence was also found during learning in studies with OCD patients (Vaghi et al., 2017) and along the compulsivity dimension (Seow and Gillan, 2020). These findings provide an extended understanding of previously observed under-confidence relative to actual performance compared to controls (e.g. Dar, 2004; Dar et al., 2000) that already indicated a dissociation of subjective beliefs and behaviour. 

This observed dissociation of beliefs and actions docks onto a thought and action fusion seen as a common clinical symptom. Thought and action fusion (TAF) entails the belief that thinking something is equivalent to carrying out that action and that a thought of event is more likely to happen in the future (Shafran and Rachman, 2004; Shafran et al., 1996). The observed action-confidence misappropriation might be a mechanism related to TAF. Furthermore, ‘insight’ which is often assessed in clinical settings (e.g. Eisen et al., 1998) and may be understood as the awareness of a patient that their mental experiences are not based on external reality, is a relevant aspect of metacognition. It has been seen to be predictive of therapeutic success in children (e.g. Garcia et al., 2010) and adults with OCD (e.g. Foa et al., 1999) and thereby underlines the importance of metacognitive evaluations. 

In summary, these findings suggest a relatively consistent confidence impairment in adult OCD patients. This impairment is likely to 

be at least partially driven by a mismatch between actual, objective performance and the patients’ confidence (i.e. metacognitive deficit). However, there is a notable lack of studies on metacognition in juvenile OCD. This might partially be because little is known about the normative maturation of metacognitive skills. First studies indicate that metacognition matures during late adolescence (Fandakova et al., 2017; Moses-Payne et al., 2020; Weil et al., 2013). An indication that metacognition might already be impaired in juvenile OCD comes from a questionnaire study that showed that adolescents with high OC symptoms have altered metacognitive beliefs (Mather and CartwrightHatton, 2004). Whether observed lowered levels of insight in children with OCD (e.g. Lewin et al., 2010) is linked to deficits in metacognitive tasks needs to be determined. It is therefore most critical to better understand aberrant and normative development of metacognition. An early impairment may foster the feeling of internal uncertainty and could contribute to the development of checking compulsions that themselves increase uncertainty. 

## **6. Multiple systems in the brain** 

So far, we have discussed several different domains in which (juvenile) OCD patients show altered behaviour. In what follows we will present a schematic framework that brings these findings together and illustrates how deficits may arise from one or multiple aberrant neurodevelopmental mechanisms. This will then be underpinned by simulations of the framework that are freely accessible online ( _cf_ . supplementary material). Potential relevance for other psychiatric disorders such as ADHD or depression may further result from the frameworks overarching computational and neural foundation. 

Here, we rely on the premise that multiple reasoning systems coexist in the brain (Daw et al., 2011; Dolan and Dayan, 2013). These systems predict the value of specific actions in specific states and differ in their sophistication, i.e. level of complexity. We propose that the simplest models learn about the outcome of specific motor actions (based on simple feedback learning), ignoring other sensory inputs (e.g. type of stimuli on the screen). The most complex models, however, have access to a sophisticated representation (or cognitive model) of the task structure, including various hidden states and transitions between them. These reasoning systems are likely to differ in their demands: a complex system relies on slow and demanding computations, while a simple model is fast and needs only little neural computations. In general, more complex models are likely to make more accurate predictions, unless they are overly complex in which case their performance may be reduced (Gershman and Niv, 2015). It is thus of critical importance that actions are guided by the reasoning system that makes the best predictions with minimal complexity (Friston, 2013). 

The majority of current empirical studies reduce this framework to a well-established dichotomous systems theory ( _cf._ Box 2; Daw et al., 2005). However, recent findings from Shahar et al. (2019) prove the existence of multiple reasoning systems with a motor-spatial system complementing model-based and model-free systems. We propose that these different systems are embedded in separate, parallel feedback loops, referred to as fronto-striatal loops. These loops are known to play an important role in learning and decision making connecting frontal regions to the striatum in a topographically organised manner (Haber, 2016). It is likely that the functional complexity of the reasoning systems increases from the posterior to the anterior regions of the frontal lobe (Miller and Cohen, 2001), ranging from the motor cortex to regions involved in complex reasoning i.e. the orbitofrontal cortex (OFC; Schuck et al., 2016) and surrounding areas ( _cf._ Fig. 3; Miller and Cohen, 2001; O’Doherty et al., 2015; Schoenbaum et al., 1998). This assumption is founded in human neuroimaging studies that have shown that anterior regions represent complex, sometimes hidden task-structures (Chan et al., 2016; Schuck et al., 2016; Schuck and Niv, 2019; Wilson et al., 2014), while simpler action-outcome associations are mainly represented in more posterior areas (for review see work by Domenech 

635 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

**==> picture [241 x 190] intentionally omitted <==**

**Fig. 3.** Schematic framework illustrating how cognitive deficits in OCD may arise from aberrant neurodevelopmental mechanisms. Different reasoning systems may be embedded in separate fronto-striatal loops (arrows). Functional complexity of the systems is likely to increase from the posterior to the anterior regions of the frontal lobe. A meta-controller in the dmPFC/dACC may arbitrate and select between competing actions. The cortex was visualised using the BrainNet Viewer (http://www.nitrc.org/projects/bnv/; Xia et al., 2013). 

and Koechlin, 2015). This is also in line with animal literature prescribing goal-directed learning to the prelimbic area (Coutureau and Killcross, 2003) and state representations to the OFC (Baltz et al., 2018). 

We speculate that such a topographical alignment is also preserved in the basal ganglia following a ventromedial to dorsolateral gradient. Areas of the anterior prefrontal cortex (aPFC) project to medial, and posterior areas to lateral striatal regions via topographically organised fronto-striatal loops (Di Martino et al., 2008; Jarbo and Verstynen, 2015). While ventromedial regions are often associated with complex, ‘future-oriented’ values (Burton et al., 2015; Yin et al., 2005), dorsolateral regions are involved in simpler motor, associative and habitual actions (Burton et al., 2015; Yin et al., 2004). 

If these (partially) independent systems do exist, how do they learn and how does arbitration between them take place? Dopaminergic prediction errors (PEs; Schultz et al., 1997; Schultz, 2016) may act as teaching signals for most systems. Recent advances suggest dopamine does not carry a unified PE signal, but rather multiple distinct PE signals (Dabney et al., 2020; Takahashi et al., 2011, 2017). This is in line with findings showing that dopaminergic activity is area- and circuitryspecific and that separate fronto-striatal loops are associated with distinct dopaminergic signals supporting different value learning mechanisms (Lammel et al., 2011; Morris et al., 2016). Therefore each loop may be associated with different dopaminergic PEs that update the specific predictions of each reasoning system. 

We propose that a meta-controller selects between competing action policies to arbitrate between the systems and determine the best action (Lieder and Griffiths, 2017). A straightforward mechanism to base the arbitration on would be to track each systems’ predictive accuracy over time and to form individual systems’ confidence signals. Such a ‘metaconfidence’ (or reliability) could be formed from the (absolute) PEs of each system (Alexander and Brown, 2011; Silvetti et al., 2011), and subsequently, help to weight the predictions of each system for action selection. The relative difference between these meta-confidences might not only determine the executed action but also feed into the selfreport of confidence. However, the meta-controller itself and the arbitration mechanism may not be conscious. How exactly confidence, as well as insight into disorder relate to this framework therefore remains to be explored. 

We propose that the dorsal medial prefrontal cortex (dmPFC), encompassing the dorsal anterior cingulate cortex (dACC), could constitute a critical node of the meta-controller. The dmPFC has extensive connections to the striatum, other prefrontal and motor regions (Haber, 2016). It resides in an ideal position to collect, integrate, and select conflicting decision-related signals (Alexander and Brown, 2011). Previous work suggests that the dmPFC integrates multiple, conflicting signals into a single decision output (Alexander and Brown, 2011; Shenhav et al., 2016). Many functions necessary for a meta-controller involve the dACC. The dACC has not only been found relevant for simple error monitoring and behavioural control (Amiez et al., 2005; Brown and Braver, 2005; Heilbronner and Hayden, 2016; van Veen and Carter, 2002), but also seems to encode multiple decision variables (Heilbronner and Hayden, 2016) and control switches between different behavioural strategies (Kerns et al., 2004; Lee et al., 2014). Whether the dmPFC indeed fulfils all functions of a meta-controller needs further investigation. 

Given this framework, we can now speculate how the observed cognitive biases in juvenile OCD might arise from a single altered neural process and how multiple deficits might surface in similar symptomologies, but with different underlying mechanisms. 

## **7. Potential pathomechanisms** 

Assuming that the multiple-systems framework approximately describes what happens in the brain, one can propose at least three different ways of how such processes can go awry and lead to deficits found in OCD. These potential impairments can guide our research pursuits by taking into account the possibility that distinct OCD subgroups might suffer from different symptomologies. Neurocognitive deficiencies could arise from (i) impaired (complex) reasoning systems, (ii) an impaired formation of meta-confidence for functioning systems, and/or (iii) an impaired arbitration process of the meta-controller. 

Complex reasoning systems rely on cognitive models of a task (/the world) that are often high-dimensional and challenging to learn. If these complex mental maps are not constructed or updated adequately, symptoms associated with OCD could arise. A failure in complex systems predicts that tasks necessitating such maps will not be completed adequately. For example, complex extra-dimensional shifts need an expansion of mental models (i.e. taking a previously irrelevant feature dimension into account). If such a model cannot be constructed or exploited, then subjects might be able to perform more simple learning aspects of the task, but no extra-dimensional shifts. The failure of these systems then affects their meta-confidence, which in turn leads to a decreased reliance on these systems. This again can explain why (at least over time) an over-reliance on simpler, model-free systems emerges, leading to habit-like behaviours. Similarly, faulty complex systems can also lead to indecisiveness and corrupt information gathering processes that critically rely on complex systems in order to plan into the future (Fradkin et al., 2020). Lastly, if confidence reports primarily rely on complex systems as indicated by recent neuroimaging work (e.g. Bang and Fleming, 2018; Fleming and Dolan, 2012) and simple action exertion on less complex systems, dissociative learning rates in belief and action updating could arise. 

Faulty meta-confidence updating can have similar consequences, but the inner workings are different. If meta-confidence is not updated adequately, it can lead to an over-reliance on a not-so-good system, ignoring better systems. Assuming that the brain is developmentally programmed to rely on simpler reasoning systems ( _cf._ below), this means that more complex reasoning systems will have less influence in a decision-making process, which in turn can lead to excessive use of simple systems leading to habit-like behaviour. Likewise, this process could also impair the completion of complex tasks such as set-shifting, by ignoring adequate predictions of complex systems. 

Lastly, a faulty meta-controller may also account for some of the observed alterations. Concretely, if the controller does not take 

636 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

individual meta-confidence accurately into account, it will base its action selection on suboptimal models and thus make inadequate decisions. Such a deficiency is in line with previous accounts suggesting arbitration difficulties between habitual and goal-directed systems (Gruner et al., 2016). It can further explain both an over-habitual behaviour as well as a failure to solve complex task aspects, such as planning, set-shifting or information gathering. How such an ignorance towards meta-confidence affects confidence reports depends on the concrete implementation, but it is likely that the erratic behaviour of the meta-controller will also interfere with the updating of meta-confidence. 

Regardless of which one(s) of the suggested three pathomechanisms may be present, the imbalance between systems may further explain the prominent clinical chain of “obsession- distress- compulsion- relieve”. If a simple model dominates behaviour intrusive thoughts may lead to a simple compulsive reaction leading to a momentary relieve of distress. More complex systems may be able to take transition probabilities of events into account and thus acknowledge the unrealistic character of these thoughts and the ineffectiveness of compulsions. However, if these complex systems do not exert any power over executed behaviours and thought patterns the named chain of symptoms is likely to prevail and potentially even worsen the systems’ imbalance. 

Our algorithmic framework can be expanded to an implementation level. Previous models prescribe OCD-symptoms to an imbalance of the direct (excitatory) and indirect (inhibitory) cortico-striatal pathways (Maia and Frank, 2011; Saxena et al., 2001). Such an imbalance can explain why a single system can go awry and become unable to adapt. In fact, previous work has highlighted the role of different frontostriatal networks attributing OCD-like symptoms to impairments in different circuits (Maia et al., 2008; Rolls et al., 2008). This is in line with our framework assigning concrete cognitive functions to the different fronto-striatal loops. Furthermore, all three pathomechanisms could explain observed heightened dACC PEs (Hauser et al., 2017b) as well as error-related negativity (ERN; Hajcak et al., 2008). A wrong model of the world resulting in inaccurate predictions and/or a faulty behaviour-selection mechanism leading to actions that are not in line with the original predictions could explain faulty predicted values of rewards, which in turn modulates and determines behavioural output. It could further lead to an increase in uncertainty mirrored in increased anxiety and lowered confidence shown in OCD. This is in line with work suggesting that increased ERNs may be a potential marker for anxietyrelated phenotypes (e.g. Gillan et al., 2017) and may constitute an important marker in OCD-related anxiety. Moreover, anxiety and the cognitive load that comes with it may further foster an imbalance between systems and/or a misallocation of behavioural influence by the meta-controller. 

In summary, we propose three potential mechanisms that can go awry and lead to underperformances consistently observed in OCD patients. Whilst several of these mechanistic disruptions suggested here make similar predictions about the behavioural consequences, their neural implementation is likely to differ. Therefore, they could be dissociated using computational modelling and neural probing. In what follows, we will thus review the known neural alterations in OCD, and end by highlighting why a developmental perspective on these is essential. 

## **8. Neural alterations in OCD** 

Evidence for structural and functional differences in juvenile OCD has been accumulated for more than two decades, revealing effects primarily in the frontal-striatal circuitry (Brem et al., 2012; Hauser et al., 2017b; Maia et al., 2008; Marzuki et al., 2020; Menzies et al., 2008). 

A key area altered in (juvenile) OCD is the dmPFC, including the dACC (Maia et al., 2008). Grey matter (Szeszko et al., 2008) as well as functional activity in the ACC (e.g. Carrasco et al., 2013; Hajcak et al., 

2008) has been seen to be increased in juvenile OCD patients. Recently, heightened PEs were found in the dACC in juvenile patients (Hauser et al., 2017b), which supports the idea that processing of a meta-controller could be compromised. Interestingly, this was replicated in adult OCD, and it was shown that this effect could be normalized by altering dopamine functioning (Murray et al., 2019). Similar evidence comes from electrophysiological studies showing that ERN in this area is more pronounced in juvenile OCD patients (Carrasco et al., 2013; Hajcak et al., 2008). As part of the action monitoring system, altered ACC activity has further been associated with symptom severity in adult OCD (e.g. Fitzgerald et al., 2005; Ursu et al., 2003). It should be noted that the direction of an altered activation (i.e. hyper- vs hypo-activity), may depend on the specific task used, and may flip in resting-state studies (He, 2013). 

Similarly important for these cognitive functions, other frontostriatal areas besides the dmPFC also express functional and structural abnormalities in juvenile OCD. These alterations are focused on striatal as well as orbitofrontal and adjacent regions (Hauser et al., 2017b; Woolley et al., 2008; Norman et al., 2017; Jayarajan et al., 2015; Fitzgerald et al., 2011) and have been linked to cognitive alterations such as limited inhibitory control (Woolley et al., 2008) and indecisiveness (Hauser et al., 2017b). 

All of these areas are known to undergo pronounced maturation during adolescence (Blakemore and Choudhury, 2006; Giedd et al., 1999 ). It is therefore critical to understand when and how these deficits in juvenile OCD arise. A recent longitudinal study showed that adolescents exhibit widespread myelin-related growth across the entire prefrontal cortex (Ziegler et al., 2019). However, this growth was substantially reduced in ACC and striatum in adolescents with high OCD symptoms. Further support for such development-dependent alterations was seen in cross-sectional patient studies. For instance, while grey matter in the ACC has been found to increase in healthy adolescents, this increase was absent in juvenile OCD patients, who in turn exhibited larger baseline volumes (Rosenberg and Keshavan, 1998; Ziegler et al., 2019). Likewise, Fitzgerald et al. (2011) found reduced connectivity in fronto-striatal loops encompassing the dACC and striatum that was specific to children with OCD, while excessive connectivity of dorsal striatum regions to the ventromedial PFC (vmPFC) was present in all age groups. How myelin-related growth integrates with functional connectivity during development, however, remains unclear. Together, these findings suggest that different fronto-striatal loops follow distinct (aberrant) developmental trajectories. 

Due to the prominence of anxiety in OCD, the amygdala has also been proposed to play an important role in OCD. Its exact involvement has however been a matter of debate and past research in adult OCD has shown under-, hyper- as well as normal amygdala activity (Milad and Rauch, 2012). While some studies in the adult OCD literature suggested an alteration in the fronto-amygdala connectivity (Subirà et al., 2016), other studies could not find changes in amygdala activity during threat learning (Apergis-Schoute et al., 2017). Szeszko et al. (2004) found (asymmetric) volume differences in juvenile patients and Britton et al. (2010b) an amygdala under-activation in response to facial expressions. However, a recent meta-analysis on emotional processing pointed out the small number of studies on paediatric OCD (Thorsen et al., 2018). The same study further showed increased amygdala activity during emotional processing in adult OCD and indicated that uncontrolled variables such as medication status, comorbidities, and symptom severity seem to have led to inconsistencies in the field. Thus, while the amygdala is likely to play an influential role in OCD the current literature on amygdala activity in (juvenile) OCD is scarce and inconsistent. It further remains to explore whether other OCD-like alterations might drive certain amygdala responses, or the other way around or whether these changes come about in a more synchronic matter. 

In summary, it is critical to investigate neural alterations of OCD in the context of neurocognitive development. Understanding how and 

637 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

## **Box 3** 

Outstanding questions 

Our knowledge about the neural and cognitive mechanisms that underlie juvenile OCD is still limited. It is thus critical to conduct longitudinal studies that track the development of cognitive skills and brain maturation. Such approaches can help to get an understanding of the neural and cognitive factors that contribute to the emergence of OCD: 

- [How does the development of OCD symptoms relate to the development of cognitive markers (e.g. indecisiveness)? Does cognition precede ] symptoms or vice versa? 

- [When do different fronto-striatal loops mature and how are they related to cognition and symptoms?  ] 

- [Do juvenile OCD and other psychiatric disorders express similar or distinct neurocognitive developmental trajectories?  ] 

- [Can we identify different at-risk stages before the development of OCD (][Fineberg et al., 2019][; similar to schizophrenia) and if so, what are ] their cognitive and neural markers? 

when a specific neural alteration arises and how it relates to cognitive impairments and OCD symptoms helps us trace the derailing that promotes the emergence of the disorder ( _cf._ Box 3 on open questions). 

## **9. A derailed development in OCD** 

We have proposed that the emergence of OCD can be understood in the context of a meta-controller framework and that areas implicated in this framework show specific developmental trajectories in OCD patients. 

A key developmental contribution is that different reasoning systems appear to develop at different times. Structural brain development studies show that areas where complex reasoning systems are likely to reside mature last in adolescence (Toga et al., 2006). This is mirrored by a late development in model-based reasoning during adolescence (Decker et al., 2016). The consequence of this slow maturation is that earlier in life, we are more likely to rely on simpler reasoning systems (Vaghi et al., in press). This could even be reflected in the meta-confidence of complex systems. As long as a complex system is immature, it may make faulty predictions and thus have low meta-confidence. Only once the predictions become more accurate, meta-confidence will increase, and adolescents will rely more on these systems. However, if complex systems never fully mature, one will never rely on these complex reasoning systems. The above findings of altered orbitofrontal/ vmPFC regions and connectivity support a notion of impaired development of complex reasoning systems in OCD. 

It is also important to note that the emergence of the meta-controller itself may be perturbed in juvenile OCD. In particular, the findings on altered structure and function in the dmPFC in juvenile OCD support this notion. The altered maturation of the dmPFC could impact the arbitration between the reasoning systems, perhaps even prevent the complex system from fully maturing. 

The proposed pathomechanisms may further account for the observed bi-phasic onset seen in OCD (for more details see Hauser, 2020). A misled development of complex systems may lead to a so-called ‘early-onset’ (i.e. onset around puberty) of OCD which is also associated with higher heritability (Chabane et al., 2005; Taylor, 2011). If an entire complex system or meta-controller fails to mature however, a later onset in early adulthood (‘late-onset’; Taylor, 2011) could result. Adult OCD may similarly be explained by the present framework. Described pathomechanisms may not only lay the foundation at disorder onset but also exacerbate over time. Resulting neural alterations may look different in adult OCD as a simple consequence of the investigation taking place at different stages of development. Symptom and cognitive portrayals may further differ as a consequence of longer exposure to the disorder which could also lead to e.g. even higher differences in metaconfidence across systems. 

It is also important to note that effect sizes seem to differ between the paediatric and adult OCD literature. While meta-analyses on neuropsychological functioning have on average shown medium to large effect sizes in adults (Abramovitch and Cooperman, 2015; Shin et al., 2008; Snyder et al., 2015), the only meta-analysis paediatric OCD 

literature has found small effects (Abramovitch et al., 2015). One reason for this could be that effect sizes increase as a disorder becomes more chronic. Differences may get larger with further neurodevelopmental derailing and a longer disease duration. Alternatively, smaller effect sizes in children may be indicative of their long-term disease progress, so that patients that will remit show fewer impairments (e.g. Abramovitch, 2017). Research showing that pre-treatment executive functioning was predictive of treatment success is in line with this hypothesis (D’Alcante et al., 2012). These essential questions need to be addressed in longitudinal developmental investigations. 

## **10. Limitations and future research** 

In the present paper, we brought together the current state of research on juvenile OCD and considered the possible computational mechanisms that could drive observed difficulties. Our computational framework proposes how computations could go awry and lead to the observed problems. Despite having established face validity of our framework, it remains speculative at the current stage. Further computational and neuroimaging research is now needed to test and examine it in more detail, based on the specific predictions that our framework makes (also see Box 3. Outstanding questions). 

Our review further highlights a relative lack of developmental and especially longitudinal studies in juvenile OCD. While there is a growing body of research on adult OCD, our inferences about juvenile OCD are still limited and concerted efforts are needed to further deepen our computational understanding of juvenile OCD. Using longitudinal and computational studies will enable us to investigate how brain and cognitive functions dynamically change over development, and help to identify the mechanisms that underlie the emergence of OCD symptoms during development. 

## **11. Conclusion** 

In conclusion, we provided a review of the cognitive and neural alterations in (juvenile) OCD. We highlighted the commonalities, differences and research gaps between adult and juvenile OCD. Based on these findings we formulated a meta-controller framework and showed how different impairments can give rise to OCD symptoms. It is now critical to verify this framework, by examining the normative development of its components and to assess when and how it goes awry in OCD. 

## **Declaration of competing interest** 

The authors declare no conflict of interest. 

## **Acknowledgements** 

Alisa M. Loosen is a pre-doctoral fellow of the International Max Planck Research School on Computational Methods in Psychiatry and Ageing Research (IMPRS COMP2PSYCH). The participating institutions 

638 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

are the Max Planck Institute for Human Development Berlin, Germany, and University College London, London, UK. For more information, see https://www.mps-ucl-centre.mpg.de/en/comp2psych. Tobias U. Hauser is supported by a Wellcome Sir Henry Dale Fellowship (211155/ Z/18/Z), a grant from the Jacobs Foundation (2017-1261-04), the Medical Research Foundation, and Brain & Behavior Research Foundation NARSAD Young Investigator grant (27023). The Max Planck UCL Centre is a joint initiative supported by UCL and the Max Planck Society. The Wellcome Centre for Human Neuroimaging is supported by core funding from the Wellcome Trust (203147/Z/16/Z). 

## **Appendix A. Supplementary data** 

Supplementary material related to this article can be found, in the online version, at doi:https://doi.org/10.1016/j.neubiorev.2020.07. 021. 

## **References** 

Abramovitch, A., 2017. Neuropsychological Function in OCD. Obsessive-Compulsive Disorder: Phenomenology, Pathophysiology, and Treatment. Oxford University Press. Abramovitch, A., Abramowitz, J.S., Mittelman, A., 2013. The neuropsychology of adult obsessive-compulsive disorder: a meta-analysis. Clin. Psychol. Rev. 33 (8), 1163–1171. 

Abramovitch, A., Abramowitz, J.S., Mittelman, A., Stark, A., Ramsey, K., Geller, D.A., 2015. Research review: neuropsychological test performance in pediatric obsessivecompulsive disorder–a meta-analysis. J. Child Psychol. Psychiatry Allied Disciplines 56 (8), 837–847. 

Abramovitch, A., Cooperman, A., 2015. The cognitive neuropsychology of obsessivecompulsive disorder: a critical review. J. Obsessive-Compulsive Related Disord. 5, 24–36. 

Abramovitch, A., Dar, R., Hermesh, H., Schweiger, A., 2012. Comparative neuropsychology of adult obsessive-compulsive disorder and attention deficit/hyperactivity disorder: implications for a novel executive overload model of OCD. J. Neuropsychol. 6 (2), 161–191. 

Abramovitch, A., Pizzagalli, D.A., Reuman, L., Wilhelm, S., 2014. Anhedonia in obsessivecompulsive disorder: beyond comorbid depression. Psychiatry Res. 216 (2), 223–229. Adams, R.A., Huys, Q.J.M., Roiser, J.P., 2016. Computational Psychiatry: Towards a mathematically informed understanding of mental illness. J. Neurol. Neurosurg. Psychiatry 87 (1), 53–63. 

Admon, R., Bleich-Cohen, M., Weizmant, R., Poyurovsky, M., Faragian, S., Hendler, T., 2012. Functional and structural neural indices of risk aversion in obsessive–compulsive disorder (OCD). Psychiatry Res.: Neuroimaging 203 (2–3), 207–213. 

Alexander, W.H., Brown, J.W., 2011. Medial prefrontal cortex as an action-outcome predictor. Nat. Neurosci. 14 (10), 1338–1344. 

American Psychiatric Association, 2013. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition. American Psychiatric Association. 

Amiez, C., Joseph, J.-P., Procyk, E., 2005. Anterior cingulate error-related activity is modulated by predicted reward. Eur. J. Neurosci. 21 (12), 3447–3452. 

Andrews, B.R., 1903. Habit. Am. J. Psychol. 14 (2), 121–149. 

Anticevic, A., Hu, S., Zhang, S., Savic, A., Billingslea, E., Wasylink, S., Repovs, G., et al., 2014. Global resting-state functional magnetic resonance imaging analysis identifies frontal cortex, striatal, and cerebellar dysconnectivity in obsessive-compulsive disorder. Biol. Psychiatry 75 (8), 595–605. 

Apergis-Schoute, A.M., Gillan, C.M., Fineberg, N.A., Fernandez-Egea, E., Sahakian, B.J., Robbins, T.W., 2017. Neural basis of impaired safety signaling in Obsessive Compulsive Disorder. Proceedings of the National Academy of Sciences of the United States of America 114 (12), 3216–3221. 

Aranovich, G.J., Cavagnaro, D.R., Pitt, M.A., Myung, J.I., Mathews, C.A., 2017. A modelbased analysis of decision making under risk in obsessive-compulsive and hoarding disorders. J. Psychiatr. Res. 90, 126–132. 

Baltz, E.T., Yalcinbas, E.A., Renteria, R., Gremel, C.M., 2018. Orbital frontal cortex updates state-induced value change for decision-making. eLife 7, e35988. 

Banca, P., Vestergaard, M.D., Rankov, V., Baek, K., Mitchell, S., Lapa, T., Castelo-Branco, M., et al., 2015. Evidence accumulation in obsessive-compulsive disorder: the role of uncertainty and monetary reward on perceptual decision-making thresholds. Neuropsychopharmacology 40 (5), 1192–1202. 

Bang, D., Fleming, S.M., 2018. Distinct encoding of decision confidence in human medial prefrontal cortex. Proc. Natl. Acad. Sci. U. S. A. 115 (23), 6082–6087. Beers, S.R., Rosenberg, D.R., Dick, E.L., Williams, T., O’Hearn, K.M., Birmaher, B., Ryan, C.M., 1999. Neuropsychological study of frontal lobe function in psychotropic-naive children with obsessive-compulsive disorder. Am. J. Psychiatry 156 (5), 777–779. 

Blakemore, S.-J., Choudhury, S., 2006. Development of the adolescent brain: implications for executive function and social cognition. J. Child Psychol. Psychiatry 47 (3–4), 296–312. 

Boschen, M.J., Vuksanovic, D., 2007. Deteriorating memory confidence, responsibility perceptions and repeated checking: comparisons in OCD and control samples. Behav. Res. Ther. 45 (9), 2098–2109. 

Brem, S., Hauser, T.U., Iannaccone, R., Brandeis, D., Drechsler, R., Walitza, S., 2012. 

Neuroimaging of cognitive brain function in paediatric obsessive compulsive disorder: a review of literature and preliminary meta-analysis. J. Neural Transm. 119 (11), 1425–1448. 

Britton, J.C., Rauch, S.L., Rosso, I.M., Killgore, W.D.S., Price, L.M., Ragan, J., Chosak, A., et al., 2010a. Cognitive inflexibility and frontal-cortical activation in pediatric obsessive-compulsive disorder. J. Am. Acad. Child Adolesc. Psychiatry 49 (9), 944–953. Britton, J.C., Stewart, S.E., Killgore, W.D., Rosso, I.M., Price, L.M., Gold, A.L., Pine, D.S., Wilhelm, S., Jenike, M.A., Rauch, S.L., 2010b. Amygdala activation in response to facial expressions in pediatric obsessive-compulsive disorder. Depress. Anxiety 27 (7), 643–651. 

Brown, J.W., Braver, T.S., 2005. Learned predictions of error likelihood in the anterior cingulate cortex. Science 307 (5712), 1118–1121. 

Burton, A.C., Nakamura, K., Roesch, M.R., 2015. From ventral-medial to dorsal-lateral striatum: neural correlates of reward-guided decision-making. Neurobiol. Learn. Memory 117, 51–59. 

Carrasco, M., Hong, C., Nienhuis, J.K., Harbin, S.M., Fitzgerald, K.D., Gehring, W.J., Hanna, G.L., 2013. Increased error-related brain activity in youth with obsessivecompulsive disorder and other anxiety disorders. Neurosci. Lett. 541, 214–218. 

Ceaser, A.E., Goldberg, T.E., Egan, M.F., McMahon, R.P., Weinberger, D.R., Gold, J.M., 2008. Set-shifting ability and schizophrenia: a marker of clinical illness or an intermediate phenotype? Biol. Psychiatry 64 (9), 782–788. 

Chabane, N., Delorme, R., Millet, B., Mouren, M.-C., Leboyer, M., Pauls, D., 2005. Earlyonset obsessive-compulsive disorder: a subgroup with a specific clinical and familial pattern? J. Child Psychol. Psychiatry, Allied Disciplines 46 (8), 881–887. Chamberlain, S.R., Fineberg, N.A., Blackwell, A.D., Clark, L., Robbins, T.W., Sahakian, B.J., 2007a. A neuropsychological comparison of obsessive-compulsive disorder and trichotillomania. Neuropsychologia 45 (4), 654–662. Chamberlain, S.R., Fineberg, N.A., Blackwell, A.D., Robbins, T.W., Sahakian, B.J., 2006. Motor inhibition and cognitive flexibility in obsessive-compulsive disorder and trichotillomania. Am. J. Psychiatry 163 (7), 1282–1284. 

Chamberlain, S.R., Fineberg, N.A., Menzies, L.A., Blackwell, A.D., Bullmore, E.T., Robbins, T.W., Sahakian, B.J., 2007b. Impaired cognitive flexibility and motor inhibition in unaffected first-degree relatives of patients with obsessive-compulsive disorder. Am. J. Psychiatry 164 (2), 335–338. 

Chamberlain, S.R., Menzies, L., Hampshire, A., Suckling, J., Fineberg, N.A., del Campo, N., Aitken, M., Craig, K., Owen, A.M., Bullmore, E.T., Robbins, T.W., Sahakian, B.J., 2008. Orbitofrontal dysfunction in patients with obsessive-compulsive disorder and their unaffected relatives. Science (New York, N. Y.) 321 (5887), 421–422. 

Chan, S.C.Y., Niv, Y., Norman, K.A., 2016. A probability distribution over latent causes, in the orbitofrontal cortex. J. Neurosci. 36 (30), 7817–7828. 

Cisek, P., Puskas, G.A., El-Murr, S., 2009. Decisions in changing conditions: the urgencygating model. J. Neurosci. 29 (37), 11560–11571. 

Coutureau, E., Killcross, S., 2003. Inactivation of the infralimbic prefrontal cortex reinstates goal-directed responding in overtrained rats. Behav. Brain Res. 146 (1–2), 167–174. 

Cuttler, C., Sirois-Delisle, V., Alcolado, G.M., Radomsky, A.S., Taylor, S., 2013. Diminished confidence in prospective memory causes doubts and urges to check. J. Behav. Ther. Exp. Psychiatry 44 (3), 329–334. 

Dabney, W., Kurth-Nelson, Z., Uchida, N., Starkweather, C.K., Hassabis, D., Munos, R., Botvinick, M., 2020. A distributional code for value in dopamine-based reinforcement learning. Nature 577 (7792), 671–675. 

D’Alcante, C.C., Diniz, J.B., Fossaluza, V., Batistuzzo, M.C., Lopes, A.C., Shavitt, R.G., Deckersbach, T., et al., 2012. Neuropsychological predictors of response to randomized treatment in obsessive–compulsive disorder. Prog. Neuro-Psychopharmacol. Biol. Psychiatry 39 (2), 310–317 New Drugs of Abuse. 

Dar, R., 2004. Elucidating the mechanism of uncertainty and doubt in obsessive-compulsive checkers. J. Behav. Ther. Exp. Psychiatry 35 (2), 153–163. 

Dar, R., Rish, S., Hermesh, H., Taub, M., Fux, M., 2000. Realism of confidence in obsessive-compulsive checkers. J. Abnorm. Psychol. 109 (4), 673–678. 

Daw, N.D., Gershman, S.J., Seymour, B., Dayan, P., Dolan, R.J., 2011. Model-based influences on humans’ choices and striatal prediction errors. Neuron 69 (6), 1204–1215. 

Daw, N.D., Niv, Y., Dayan, P., 2005. Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. Nat. Neurosci. 8 (12), 1704–1711. 

Decker, J.H., Otto, A.R., Daw, N.D., Hartley, C.A., 2016. From creatures of habit to goaldirected learners. Psychol. Sci. 27 (6), 848–858. 

Deckersbach, T., Savage, C.R., Curran, T., Bohne, A., Wilhelm, S., Baer, L., Jenike, M.A., et al., 2002. A study of parallel implicit and explicit information processing in patients with obsessive-compulsive disorder. Am. J. Psychiatry 159 (10), 1780–1782. 

Di Martino, A., Scheres, A., Margulies, D.S., Kelly, A.M.C., Uddin, L.Q., Shehzad, Z., Biswal, B., et al., 2008. Functional connectivity of human striatum: a resting state FMRI study. Cerebral Cortex (N.Y.: 1991) 18 (12), 2735–2747. 

Dolan, R.J., Dayan, P., 2013. Goals and habits in the brain. Neuron 80 (2), 312–325. Domenech, P., Koechlin, E., 2015. Executive control and decision-making in the prefrontal cortex. Curr. Opin. Behav. Sci. 1, 101–106. 

Drechsler, R., Hauser, T.U., Iannaccone, R., Brandeis, D., Walitza, S., Brem, S., 2015. Dealing with uncertainty—Decision-making, executive function and cognitive style in adolescents with ADHD compared to adolescents with OCD. Presented at the Eunethydis. 

Eisen, J.L., Phillips, K.A., Baer, L., Beer, D.A., Atala, K.D., Rasmussen, S.A., 1998. The brown assessment of beliefs scale: reliability and validity. Am. J. Psychiatry 155 (1), 102–108 US: American Psychiatric Assn. 

Erhan, C., Bulut, G.Ç., Gökçe, S., Ozbas, D., Turkakin, E., Dursun, O.B., Yazgan, Y., et al., 2017. Disrupted latent decision processes in medication-free pediatric OCD patients. J. Affect. Disord. 207, 32–37. 

639 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

Ermakova, A.O., Gileadi, N., Knolle, F., Justicia, A., Anderson, R., Fletcher, P.C., Moutoussis, M., et al., 2019. Cost evaluation during decision-making in patients at early stages of psychosis. Comput. Psychiatry (Cambridge, Mass.) 3, 18–39. Evans, S.L., Averbeck, B.B., Furl, N., 2015. Jumping to conclusions in schizophrenia. Neuropsychiatr. Dis. Treat. 11, 1615–1624. 

Eysenck, M.W., Keane, M.T., 2000. Cognitive psychology: a student’s handbook. Psychology Press, Hove. 

Fandakova, Y., Selmeczy, D., Leckey, S., Grimm, K.J., Wendelken, C., Bunge, S.A., Ghetti, S., 2017. Changes in ventromedial prefrontal and insular cortex support the development of metamemory from childhood into adolescence. Proc. Natl. Acad. Sci. U. S. A. 114 (29), 7582–7587. 

Fear, C.F., Healy, D., 1997. Probabilistic reasoning in obsessive–compulsive and delusional disorders. Psychol. Med. 27 (1), 199–208. 

Fineberg, N.A., Dell’Osso, B., Albert, U., Maina, G., Geller, D.A., Carmi, L., Sireau, N., et al., 2019. Early intervention for obsessive compulsive disorder: an expert consensus statement. Eur. Neuropsychopharmacol. 29 (4), 549–565. 

Fitzgerald, K.D., Welsh, R.C., Gehring, W.J., Abelson, J.L., Himle, J.A., Liberzon, I., Taylor, S.F., 2005. Error-related hyperactivity of the anterior cingulate cortex in obsessive-compulsive disorder. Biol. Psychiatry 57 (3), 287–294. 

Fitzgerald, K.D., Welsh, R.C., Stern, E.R., Angstadt, M., Hanna, G.L., Abelson, J.L., Taylor, S.F., 2011. Developmental alterations of frontal-striatal-thalamic connectivity in obsessive compulsive disorder. J. Am. Acad. Child Adolesc. Psychiatry 50 (9) 938948.e3. 

Fleming, S.M., Dolan, R.J., 2012. The neural basis of metacognitive ability. Philos. Transact. R. Soc. B: Biol. Sci. 367 (1594), 1338–1349. 

Fleming, S.M., Lau, H.C., 2014. How to measure metacognition. Frontiers Hum. Neurosci. 8, 443. 

Foa, E.B., Abramowitz, J.S., Franklin, M.E., Kozak, M.J., 1999. Feared consequences, fixity of belief, and treatment outcome in patients with obsessive-compulsive disorder. Behav. Ther. 30 (4), 717–724. 

Fradkin, I., Adams, R.A., Parr, T., Roiser, J.P., Huppert, J.D., 2020. Searching for an anchor in an unpredictable world: a computational model of obsessive compulsive disorder. Psychol. Rev. Advance online publication. 

Friston, K., 2013. Life as we know it. J. R. Soc. Interface 10 (86) 20130475. 

Garcia, A.M., Sapyta, J.J., Moore, P.S., Freeman, J.B., Franklin, M.E., March, J.S., Foa, E.B., 2010. Predictors and moderators of treatment outcome in the Pediatric Obsessive Compulsive Treatment Study (POTS I). J. Am. Acad. Child Adolesc. Psychiatry 49 (10), 1024–1086. 

Gershman, S.J., Niv, Y., 2015. Novelty and inductive generalization in human reinforcement learning. Topics Cognitive Sci. 7 (3), 391–415. 

Giedd, J.N., Blumenthal, J., Jeffries, N.O., Castellanos, F.X., Liu, H., Zijdenbos, A., Paus, T., et al., 1999. Brain development during childhood and adolescence: a longitudinal MRI study. Nat. Neurosci. 2 (10), 861–863. 

Gillan, C.M., Robbins, T.W., 2014. Goal-directed learning and obsessive-compulsive disorder. Philos. Transact. R. Soc. B: Biol. Sci. 369 (1655) 20130475. 

Gillan, C.M., Papmeyer, M., Morein-Zamir, S., Sahakian, B.J., Fineberg, N.A., Robbins, T.W., de Wit, S., 2011. Disruption in the balance between goal-directed behavior and habit learning in obsessive-compulsive disorder. Am. J. Psychiatry 168 (7), 718–726. Gillan, C.M., Apergis-Schoute, A.M., Morein-Zamir, S., Urcelay, G.P., Sule, A., Fineberg, N.A., Sahakian, B.J., et al., 2014a. Functional neuroimaging of avoidance habits in obsessive-compulsive disorder. Am. J. Psychiatry 172 (3), 284–293. 

Gillan, C.M., Morein-Zamir, S., Urcelay, G.P., Sule, A., Voon, V., Apergis-Schoute, A.M., Fineberg, N.A., et al., 2014b. Enhanced avoidance habits in obsessive-compulsive disorder. Biolog. Psychiatry 75 (8), 631–638. 

Gillan, C.M., Kosinski, M., Whelan, R., Phelps, E.A., Daw, N.D., 2016. Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. Frank, M.J. (Ed.), eLife 5, e11305. 

Gillan, C.M., Fineberg, N.A., Robbins, T.W., 2017. A trans-diagnostic perspective on obsessive-compulsive disorder. Psychol. Med. 47 (9), 1528–1548. 

Gillan, C.M., Kalanthroff, E., Evans, M., Weingarden, H.M., Jacoby, R.J., Gershkovich, M., Snorrason, I., et al., 2020a. Comparison of the association between goal-directed planning and self-reported compulsivity vs obsessive-compulsive disorder diagnosis. JAMA Psychiatry 77 (1), 77–85. 

Gillan, C.M., Vaghi, M.M., Hezemans, F.H., van Ghesel Grothe, S., Dafflon, J., Brühl, A.B., Savulich, G., Robbins, T.W., 2020b. Experimentally induced and real-world anxiety have no demonstrable effect on goal-directed behaviour. Psychol. Med. 1–12 Advance online publication. 

Gotlib, I.H., Hamilton, J.P., Cooney, R.E., Singh, M.K., Henry, M.L., Joormann, J., 2010. Neural processing of reward and loss in girls at risk for major depression. Arch. Gen. Psychiatry 67 (4), 380–387. 

Gottwald, J., de Wit, S., Apergis-Schoute, A.M., Morein-Zamir, S., Kaser, M., Cormack, F., Sule, A., et al., 2018. Impaired cognitive plasticity and goal-directed control in adolescent obsessive–compulsive disorder. Psychol. Med. 48 (11), 1900–1908. 

Grassi, G., Pallanti, S., Righi, L., Figee, M., Mantione, M., Denys, D., Piccagliani, D., et al., 2015. Think twice: impulsivity and decision making in obsessive–compulsive disorder. J. Behav. Addict. 4 (4), 263–272. 

- Gruner, P., Anticevic, A., Lee, D., Pittenger, C., 2016. Arbitration between action strategies in obsessive-compulsive disorder. Neurosci. Rev. J. Bring. Neurobiol. Neurol. Psychiatry 22 (2), 188–198. 

- Gu, B.M., Park, J.Y., Kang, D.H., Lee, S.J., Yoo, S.Y., Jo, H.J., Choi, C.H., et al., 2008. Neural correlates of cognitive inflexibility during task-switching in obsessive-compulsive disorder. Brain 131 (Pt 1), 155–164. 

Haber, S.N., 2016. Corticostriatal circuitry. Dialogues Clin. Neurosci. 18 (1), 7–21. Hajcak, G., Franklin, M.E., Foa, E.B., Simons, R.F., 2008. Increased error-related brain activity in pediatric obsessive-compulsive disorder before and after treatment. Am. J. Psychiatry 165 (1), 116–123. 

Harrison, B.J., Soriano-Mas, C., Pujol, J., Ortiz, H., López-Solà, M., Hernández-Ribas, R., Deus, J., et al., 2009. Altered corticostriatal functional connectivity in obsessivecompulsive disorder. Arch. Gen Psychiatry 66 (11), 1189–1200. 

Hauser, T.U., 2020. On the development of OCD. In: Fineberg, N.A., Robbins, T.W. (Eds.), Future Trends in Obsessive-Compulsive Disorder. Springer Nature. Hauser, T.U., Allen, M., Rees, G., Dolan, R.J., 2017a. Metacognitive impairments extend perceptual decision making weaknesses in compulsivity. Sci. Rep. 7 (1), 6614. 

Hauser, T.U., Iannaccone, R., Dolan, R.J., Ball, J., Hättenschwiler, J., Drechsler, R., Rufer, M., Brandeis, D., Walitza, S., Brem, S., 2017b. Increased fronto-striatal reward prediction errors moderate decision making in obsessive-compulsive disorder. Psychol. Med. 47 (7), 1246–1258. 

Hauser, T.U., Moutoussis, M., Dayan, P., Dolan, R.J., 2017c. Increased decision thresholds trigger extended information gathering across the compulsivity spectrum. Transl. Psychiatry 7, 1296. 

Hauser, T.U., Moutoussis, M., Iannaccone, R., Brem, S., Walitza, S., Drechsler, R., Dayan, P., et al., 2017d. Increased decision thresholds enhance information gathering performance in juvenile Obsessive-Compulsive Disorder (OCD). PLoS Comput. Biol. 13 (4), e1005440. 

Hauser, T.U., Will, G.-J., Dubois, M., Dolan, R.J., 2019. Annual Research Review: developmental computational psychiatry. J. Child Psychol. Psychiatry 60 (4), 412–426. He, B.J., 2013. Spontaneous and task-evoked brain activity negatively interact. J. Neurosci. 33 (11), 4672–4682. 

Heilbronner, S.R., Hayden, B.Y., 2016. Dorsal anterior cingulate cortex: a bottom-up view. Ann. Rev. Neurosci. 39, 149–170. 

van den Heuvel, O.A., Remijnse, P.L., Mataix-Cols, D., Vrenken, H., Groenewegen, H.J., Uylings, H.B., van Balkom, A.J., Veltman, D.J., 2009. The major symptom dimensions of obsessive-compulsive disorder are mediated by partially distinct neural systems. Brain 132 (Pt 4), 853–868. 

Huys, Q.J.M., Maia, T.V., Frank, M.J., 2016. Computational psychiatry as a bridge from neuroscience to clinical applications. Nat. Neurosci. 19 (3), 404–413. 

Hybel, K.A., Mortensen, E.L., Lambek, R., Thastum, M., Thomsen, P.H., 2017. Cool and hot aspects of executive function in childhood obsessive-compulsive disorder. J. Abnorm. Child Psychol. 45 (6), 1195–1205. 

Jarbo, K., Verstynen, T.D., 2015. Converging structural and functional connectivity of orbitofrontal, dorsolateral prefrontal, and posterior parietal cortex in the human striatum. J. Neurosci. 35 (9), 3865–3878. 

Jayarajan, R.N., Agarwal, S.M., Viswanath, B., Kalmady, S.V., Venkatasubramanian, G., Srinath, S., Chandrashekar, C.R., et al., 2015. A voxel based morphometry study of brain gray matter volumes in juvenile obsessive compulsive disorder. J. Can. Acad. Child Adolesc. Psychiatry 24 (2), 84–91. 

Jazbec, S., Pantelis, C., Robbins, T.W., Weickert, T., Weinberger, D.R., Goldberg, T.E., 2007. Intra-dimensional/extra-dimensional set-shifting performance in schizophrenia: impact of distractors. Schizophr. Res. 89 (1), 339–349. 

Kahneman, D., 1973. Attention and effort. Prentice-Hall, Englewood Cliffs, N.J. Kalanthroff, E., Abramovitch, A., Steinman, S.A., Abramowitz, J.S., Simpson, H.B., 2016. The chicken or the egg: what drives OCD? J. Obsessive-Compulsive Relat. Disorders 11, 9–12. 

Kerns, J.G., Cohen, J.D., MacDonald, A.W., Cho, R.Y., Stenger, V.A., Carter, C.S., 2004. Anterior cingulate conflict monitoring and adjustments in control. Science 303 (5660), 1023–1026. 

Kessler, R.C., Berglund, P., Demler, O., Jin, R., Merikangas, K.R., Walters, E.E., 2005. Lifetime prevalence and age-of-onset distributions of DSM-IV disorders in the national comorbidity survey replication. Arch. Gen. Psychiatry 62 (6), 593–602. Kiani, R., Corthell, L., Shadlen, M.N., 2014. Choice certainty is informed by both evidence and decision time. Neuron 84 (6), 1329–1342. 

Kim, K.L., Christensen, R.E., Ruggieri, A., Schettini, E., Freeman, J.B., Garcia, A.M., Flessner, C., et al., 2019. Cognitive performance of youth with primary generalized anxiety disorder versus primary obsessive–compulsive disorder. Depress. Anxiety 36 (2), 130–140. 

Kwon, J.S., Kim, J.-J., Lee, D.W., Lee, J.S., Lee, D.S., Kim, M.-S., Lyoo, I.K., et al., 2003. Neural correlates of clinical symptoms and cognitive dysfunctions in obsessive–compulsive disorder. Psychiatry Res.: Neuroimaging 122 (1), 37–47. Lammel, S., Ion, D.I., Roeper, J., Malenka, R.C., 2011. Projection-specific modulation of dopamine neuron synapses by aversive and rewarding stimuli. Neuron 70 (5), 855–862. 

Lazarov, A., Liberman, N., Hermesh, H., Dar, R., 2014. Seeking proxies for internal states in obsessive–compulsive disorder. J. Abnorm. Psychol. 123 (4), 695–704. 

Lee, S.W., Shimojo, S., O’Doherty, J.P., 2014. Neural computations underlying arbitration between model-based and model-free learning. Neuron 81 (3), 687–699. Lewin, A.B., Caporino, N., Murphy, T.K., Geffken, G.R., Storch, E.A., 2010. Understudied clinical dimensions in pediatric obsessive compulsive disorder. Child Psychiatry Hum. Dev. 41 (6), 675–691. 

Lieder, F., Griffiths, T.L., 2017. Strategy selection as rational metareasoning. Psychol. Rev. 124 (6), 762–794. 

Maia, T.V., Cooney, R.E., Peterson, B.S., 2008. The neural bases of obsessive-compulsive disorder in children and adults. Dev. Psychopathol. 20 (4), 1251–1283. Maia, T.V., Frank, M.J., 2011. From reinforcement learning models to psychiatric and neurological disorders. Nat. Neurosci. 14 (2), 154–162. 

Marzuki, A.A., Pereira de Souza, A.M.F.L., Sahakian, B.J., Robbins, T.W., 2020. Are candidate neurocognitive endophenotypes of OCD present in paediatric patients? A systematic review. Neurosci. Biobehav. Rev. 108, 617–645. 

Masunami, T., Okazaki, S., Maekawa, H., 2009. Decision-making patterns and sensitivity to reward and punishment in children with attention-deficit hyperactivity disorder. Int. J. Psychophysiol. 72 (3), 283–288. 

Mataix-Cols, D., Wooderson, S., Lawrence, N., Brammer, M.J., Speckens, A., Phillips, M.L., 2004. Distinct neural correlates of washing, checking, and hoarding symptom 

640 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

dimensions in obsessive-compulsive disorder. Arch. Gen. Psychiatry 61 (6), 564–576. 

Mather, A., Cartwright-Hatton, S., 2004. Cognitive predictors of obsessive-compulsive symptoms in adolescence: a preliminary investigation. J. Clin. Child Adolesc. Psychol. 33 (4), 743–749 American Psychological Association, Division 53. 

Menzies, L., Chamberlain, S.R., Laird, A.R., Thelen, S.M., Sahakian, B.J., Bullmore, E.T., 2008. Integrating evidence from neuroimaging and neuropsychological studies of obsessive-compulsive disorder: the orbitofronto-striatal model revisited. Neurosci. Biobehav. Rev. 32 (3), 525–549. 

- Milad, M.R., Rauch, S.L., 2012. Obsessive-compulsive disorder: beyond segregated cortico-striatal pathways. Trends Cognitive Sci. 16 (1), 43–51. 

Miller, E.K., Cohen, J.D., 2001. An integrative theory of prefrontal cortex function. Ann. Rev. Neurosci. 24 (1), 167–202. 

Moritz, S., Wahl, K., Zurowski, B., Jelinek, L., Hand, I., Fricke, S., 2007. Enhanced perceived responsibility decreases metamemory but not memory accuracy in obsessivecompulsive disorder (OCD). Behav. Res. Ther. 45 (9), 2044–2052. Morris, L.S., Kundu, P., Dowell, N., Mechelmans, D.J., Favre, P., Irvine, M.A., Robbins, T.W., Daw, N., Bullmore, E.T., Harrison, N.A., Voon, V., 2016. Fronto-striatal organization: defining functional and microstructural substrates of behavioural flexibility. Cortex 74, 118–133. Moses-Payne, M.E., Habicht, J., Bowler, A., Steinbeis, N., Hauser, T.U., 2020. I Know Better! Emerging Metacognition Allows Adolescents to Ignore False Advice. . 

Murray, G.K., Knolle, F., Ersche, K.D., Craig, K.J., Abbott, S., Shabbir, S.S., Fineberg, N.A., et al., 2019. Dopaminergic drug treatment remediates exaggerated cingulate prediction error responses in obsessive-compulsive disorder. Psychopharmacology 236 (8), 2325–2336. 

Negreiros, J., Belschner, L., Best, J.R., Lin, S., Yamin, D.F., Joffres, Y., Selles, R.R., et al., 2020. Neurocognitive risk markers in pediatric obsessive–compulsive disorder. J. Child Psychol. Psychiatry 61 (5), 605–613. 

- Nord, C.L., Lawson, R.P., Huys, Q.J.M., Pilling, S., Roiser, J.P., 2018. Depression is associated with enhanced aversive Pavlovian control over instrumental behaviour. Sci. Rep. 8 (1), 12582. 

Norman, L.J., Carlisi, C.O., Christakou, A., Chantiluke, K., Murphy, C., Simmons, A., Giampietro, V., et al., 2018. Neural dysfunction during temporal discounting in paediatric attention-deficit/hyperactivity disorder and obsessive-compulsive disorder. Psychiatry Res. Neuroimaging 269, 97–105. 

Norman, L.J., Carlisi, C.O., Christakou, A., Murphy, C.M., Chantiluke, K., Giampietro, V., Simmons, A., Brammer, M., Mataix-Cols, D., Rubia, K., 2018. Frontostriatal dysfunction during decision making in attention-deficit/hyperactivity disorder and obsessive-compulsive disorder. Biolog. Psychiatry 3 (8), 694–703. 

O’Doherty, J.P., Dayan, P., Friston, K., Critchley, H., Dolan, R.J., 2003. Temporal difference models and reward-related learning in the human brain. Neuron 38 (2), 329–337. 

O’Doherty, J.P., Lee, S.W., McNamee, D., 2015. The structure of reinforcement-learning mechanisms in the human brain. Curr. Opin. Behav. Sci. 1, 94–100. Ornstein, T.J., Arnold, P., Manassis, K., Mendlowitz, S., Schachar, R., 2010. 

- Neuropsychological performance in childhood OCD: a preliminary study. Depress. Anxiety 27 (4), 372–380. 

Otto, A.R., Gershman, S.J., Markman, A.B., Daw, N.D., 2013. The curse of planning: dissecting multiple reinforcement-learning systems by taxing the central executive. Psychol. Sci. 24 (5), 751–761. 

Parr, T., Rees, G., Friston, K.J., 2018. Computational neuropsychology and Bayesian inference. Frontiers Hum. Neurosci. 12, 61. 

Pélissier, M.-C., O’Connor, K.P., 2002. Deductive and inductive reasoning in obsessivecompulsive disorder. Br. J. Clin. Psychol. 41 (Pt 1), 15–27. 

Potter, T.C.S., Bryce, N.V., Hartley, C.A., 2017. Cognitive components underpinning the development of model-based learning. Dev. Cognitive Neurosci. 25, 272–280. Purcell, R., Maruff, P., Kyrios, M., Pantelis, C., 1997. Neuropsychological function in young patients with unipolar major depression. Psychol. Med. 27 (6), 1277–1285. Pushkarskaya, H., Tolin, D., Ruderman, L., Henick, D., Kelly, J.M., Pittenger, C., Levy, I., 2017. Value-based decision making under uncertainty in hoarding and obsessivecompulsive disorders. Psychiatry Res. 258, 305–315. 

Radomsky, A.S., Dugas, M.J., Alcolado, G.M., Lavoie, S.L., 2014. When more is less: doubt, repetition, memory, metamemory, and compulsive checking in OCD. Behav. Res. Ther. 59, 30–39. 

Rauch, S.L., Savage, C.R., Brown, H.D., Curran, T., Alpert, N.M., Kendrick, A., Fischman, A.J., et al., 1995. A PET investigation of implicit and explicit sequence learning. Hum. Brain Mapp. 3 (4), 271–286. Rauch, S.L., Whalen, P.J., Curran, T., Shin, L.M., Coffey, B.J., Savage, C.R., McInerney, S.C., et al., 2001. Probing striato-thalamic function in obsessive-compulsive disorder and Tourette syndrome using neuroimaging methods. Adv. Neurol. 85, 207–224. Remijnse, P.L., Nielen, M.M., van Balkom, A.J., Hendriks, G.J., Hoogendijk, W.J., Uylings, H.B., Veltman, D.J., 2009. Differential frontal-striatal and paralimbic activity during reversal learning in major depressive disorder and obsessive-compulsive disorder. Psychol. Med. 39 (9), 1503–1518. 

Robbins, T.W., Gillan, C.M., Smith, D.G., de Wit, S., Ersche, K.D., 2012. Neurocognitive endophenotypes of impulsivity and compulsivity: towards dimensional psychiatry. Trends Cognitive Sci. 16 (1), 81–91 Special Issue: Cognition in Neuropsychiatric Disorders. 

Rolls, E.T., Loh, M., Deco, G., 2008. An attractor hypothesis of obsessive-compulsive disorder. Eur. J. Neurosci. 28 (4), 782–793. 

Rosenberg, D.R., Keshavan, M.S., 1998. Toward a neurodevelopmental model of obsessive-compulsive disorder. Biol. Psychiatry 43 (9), 623–640. 

Rouault, M., Seow, T., Gillan, C.M., Fleming, S.M., 2018. Psychiatric symptom dimensions are associated with dissociable shifts in metacognition but not task performance. Biol. Psychiatry 84 (6), 443–451. 

Russek, E.M., Momennejad, I., Botvinick, M.M., Gershman, S.J., Daw, N.D., 2017. 

Predictive representations can link model-based reinforcement learning to model-free mechanisms. PLoS Comput. Biol. 13 (9), e1005768. 

Sarig, S., Dar, R., Liberman, N., 2012. Obsessive-compulsive tendencies are related to indecisiveness and reliance on feedback in a neutral color judgment task. J. Behav. Ther. Exp. Psychiatry 43 (1), 692–697. 

Saxena, S., Bota, R.G., Brody, A.L., 2001. Brain-behavior relationships in obsessivecompulsive disorder. Semin. Clin. Neuropsychiatry 6 (2), 82–101. 

Schoenbaum, G., Chiba, A.A., Gallagher, M., 1998. Orbitofrontal cortex and basolateral amygdala encode expected outcomes during learning. Nat. Neurosci. 1 (2), 155–159. Schuck, N.W., Cai, M.B., Wilson, R.C., Niv, Y., 2016. Human orbitofrontal cortex represents a cognitive map of state space. Neuron 91 (6), 1402–1412. 

Schuck, N.W., Niv, Y., 2019. Sequential replay of nonspatial task states in the human hippocampus. Science (New York, N.Y.) 364 (6447) eaaw5181. 

Schultz, W., Dayan, P., Montague, P.R., 1997. A neural substrate of prediction and reward. Science (New York, N.Y.) 275 (5306), 1593–1599. 

Schultz, Wolfram, 2016. Dopamine reward prediction error coding. Dialogues Clin. Neurosci. 18 (1), 23–32. 

Seow, T., Gillan, C.M., 2020. Transdiagnostic phenotyping reveals a host of metacognitive deficits implicated in compulsivity. Sci. Rep. 10 (1), 2883. Shafran, R., Rachman, S., 2004. Thought-action fusion: a review. J. Behav. Ther. Exp. Psychiatry 35 (2), 87–107. 

- Shafran, Roz, Thordarson, D.S., Rachman, S., 1996. Thought-action fusion in obsessive compulsive disorder. J. Anxiety Disorders 10 (5), 379–391. 

Shahar, N., Moran, R., Hauser, T.U., Kievit, R.A., McNamee, D., Moutoussis, M., Consortium, N.S.P.N., et al., 2019. Credit assignment to state-independent task representations and its relationship with model-based decision making. Proc. Natl. Acad. Sci. U. S. A. 116 (32), 15871–15876. 

- Shenhav, A., Cohen, J.D., Botvinick, M.M., 2016. Dorsal anterior cingulate cortex and the value of control. Nat. Neurosci. 19 (10), 1286–1291. 

- Shin, M.-S., Choi, H., Kim, H., Hwang, J.-W., Kim, B.-N., Cho, S.-C., 2008. A study of neuropsychological deficit in children with obsessive-compulsive disorder. Eur. Psychiatry 23 (7), 512–520. 

Silvetti, M., Seurinck, R., Verguts, T., 2011. Value and prediction error in medial frontal cortex: integrating the single-unit and systems levels of analysis. Frontiers Hum. Neurosci. 5, 75. 

Sip, K.E., Gonzalez, R., Taylor, S.F., Stern, E.R., 2018. Increased loss aversion in unmedicated patients with obsessive-compulsive disorder. Frontiers Psychiatry 8, 309. Sip, K.E., Muratore, A.F., Stern, E.R., 2016. Effects of context on risk taking and decision times in obsessive-compulsive disorder. J. Psychiatr. Res. 75, 82–90. 

Snyder, H.R., Kaiser, R.H., Warren, S.L., Heller, W., 2015. Obsessive-compulsive disorder is associated with broad impairments in executive function: a meta-analysis. Clin. Psychol. Sci. 3 (2), 301–330. 

Soref, A., Liberman, N., Abramovitch, A., Dar, R., 2018. Explicit instructions facilitate performance of OCD participants but impair performance of non-OCD participants on a serial reaction time task. J. Anxiety Disorders 55, 56–62. 

Starcke, K., Tuschen-Caffier, B., Markowitsch, H.J., Brand, M., 2010. Dissociation of decisions in ambiguous and risky situations in obsessive–compulsive disorder. Psychiatry Res. 175 (1), 114–120. 

Subirà, M., Cano, M., de Wit, S.J., Alonso, P., Cardoner, N., Hoexter, M.Q., Kwon, J.S., Nakamae, T., Lochner, C., Sato, J.R., Jung, W.H., Narumoto, J., Stein, D.J., Pujol, J., Mataix-Cols, D., Veltman, D.J., OCD Brain Imaging Consortium, Menchón, J.M., van den Heuvel, O.A., Soriano-Mas, C., 2016. Structural covariance of neostriatal and limbic regions in patients with obsessive-compulsive disorder. J. Psychiatry Neurosci. 41 (2), 115–123. 

- Sutton, R.S., Barto, A.G., 1988. Reinforcement learning: an introduction. IEEE Transact. Neural Netw. 16, 285–286. 

- Szeszko, P.R., Christian, C., MacMaster, F., Lencz, T., Mirza, Y., Taormina, S.P., Easter, P., et al., 2008. Gray matter structural alterations in psychotropic drug-naive pediatric obsessive-compulsive disorder: an optimized voxel-based morphometry study. Am. J. Psychiatry 165 (10), 1299–1307. 

Szeszko, P.R., MacMillan, S., McMeniman, M., Lorch, E., Madden, R., Ivey, J., Banerjee, S.P., Moore, G.J., Rosenberg, D.R., 2004. Amygdala volume reductions in pediatric patients with obsessive-compulsive disorder treated with paroxetine: preliminary findings. Neuropsychopharmacology 29 (4), 826–832. 

Takahashi, Y.K., Batchelor, H.M., Liu, B., Khanna, A., Morales, M., Schoenbaum, G., 2017. Dopamine neurons respond to errors in the prediction of sensory features of expected rewards. Neuron 95 (6) 1395-1405.e3. 

Takahashi, Y.K., Roesch, M.R., Wilson, R.C., Toreson, K., O’Donnell, P., Niv, Y., Schoenbaum, G., 2011. Expectancy-related changes in firing of dopamine neurons depend on orbitofrontal cortex. Nat. Neurosci. 14 (12), 1590–1597. 

- Tamnes, C.K., Herting, M.M., Goddings, A.-L., Meuwese, R., Blakemore, S.-J., Dahl, R.E., Güroğlu, B., et al., 2017. Development of the Cerebral Cortex across adolescence: a multisample study of inter-related longitudinal changes in cortical volume, surface area, and thickness. J. Neurosc. 37 (12), 3402–3412. 

- Taylor, S., 2011. Early versus late onset obsessive-compulsive disorder: evidence for distinct subtypes. Clin. Psychol. Rev. 31 (7), 1083–1100. 

- Thorsen, A.L., Hagland, P., Radua, J., Mataix-Cols, D., Kvale, G., Hansen, B., van den Heuvel, O.A., 2018. Emotional processing in obsessive-compulsive disorder: a systematic review and meta-analysis of 25 functional neuroimaging studies. Biol. Psychiatry: Cog. Neurosci. Neuroimaging, Interoception Mental Health 3 (6), 563–571. 

Toga, A.W., Thompson, P.M., Sowell, E.R., 2006. Mapping brain maturation. Trends Neurosci. 29 (3), 148–159. 

Tripp, G., Alsop, B., 1999. Sensitivity to reward frequency in boys with attention deficit hyperactivity disorder. J. Clin. Child Psychol. 28 (3), 366–375. Tuna, S., Tekcan, A.I., Topçuoğlu, V., 2005. Memory and metamemory in obsessive- 

641 

_Neuroscience and Biobehavioral Reviews 118 (2020) 631–642_ 

_A.M. Loosen and T.U. Hauser_ 

compulsive disorder. Behav. Res. Ther. 43 (1), 15–27. 

Ursu, S., Stenger, V.A., Shear, M.K., Jones, M.R., Carter, C.S., 2003. Overactive action monitoring in obsessive-compulsive disorder: evidence from functional magnetic resonance imaging. Psychol. Sci. 14 (4), 347–353 SAGE Publications Inc. 

- Vaghi, M., Luyckx, F., Sule, A., Fineberg, N.A., Robbins, T.W., De Martino, B., 2017. Compulsivity reveals a novel dissociation between action and confidence. Neuron 96 (2) 348-354.e4. 

- Vaghi, M., Moutoussis, M., Vaša, F., Kievit, R., Hauser, T. U., Vértes, P., Shahar, N., Romero-Garcia, R., Kitzbichler, M. G., NSPN Consortium, Dolan, R., (in press). Compulsivity is linked to reduced adolescent development of goal-directed control and fronto-striatal functional connectivity. _Proceedings of the National Academy of Sciences of the United States of America_ . 

- Valerius, G., Lumpp, A., Kuelz, A.-K., Freyer, T., Voderholzer, U., 2008. Reversal learning as a neuropsychological indicator for the neuropathology of obsessive compulsive disorder? A behavioral study. J. Neuropsychiatry Clin. Neurosci. 20 (2), 210–218. 

- van Veen, V., Carter, C.S., 2002. The anterior cingulate as a conflict monitor: FMRI and ERP studies. Physiol. Behavior 77 (4), 477–482. 

- Volans, P.J., 1976. Styles of decision-making and probability appraisal in selected obsessional and phobic patients. Br. J. Soc. Clin. Psychol. 15 (3), 305–317. 

- Voon, V., Derbyshire, K., Rück, C., Irvine, M.A., Worbe, Y., Enander, J., Schreiber, L.R.N., et al., 2015. Disorders of compulsivity: a common bias towards learning habits. Mol. Psychiatry 20 (3), 345–352. 

- Voon, Valerie, Droux, F., Morris, L., Chabardes, S., Bougerol, T., David, O., Krack, P., et al., 2017. Decisional impulsivity and the associative-limbic subthalamic nucleus in obsessive-compulsive disorder: stimulation and connectivity. Brain 140 (2), 442–456. 

- Weil, L.G., Fleming, S.M., Dumontheil, I., Kilford, E.J., Weil, R.S., Rees, G., Dolan, R.J., et al., 2013. The development of metacognitive ability in adolescence. Conscious. Cog. 22 (1), 264–271. 

- Whitaker, K.J., Vértes, P.E., Romero-Garcia, R., Váša, F., Moutoussis, M., Prabhu, G., Weiskopf, N., et al., 2016. Adolescence is associated with genomically patterned consolidation of the hubs of the human brain connectome. Proc. Natl. Acad. Sci. U. S. A. 113 (32), 9105–9110. 

Wilson, R.C., Takahashi, Y.K., Schoenbaum, G., Niv, Y., 2014. Orbitofrontal cortex as a cognitive Map of Task Space. Neuron 81 (2), 267–279. 

- de Wit, S., Kindt, M., Knot, S.L., Verhoeven, A.A.C., Robbins, T.W., Gasull-Camos, J., Evans, M., et al., 2018. Shifting the balance between goals and habits: five failures in experimental habit induction. J. Exp. Psychol.: Gen. 147 (7), 1043–1065. 

- Wolff, N., Buse, J., Tost, J., Roessner, V., Beste, C., 2017. Modulations of cognitive flexibility in obsessive compulsive disorder reflect dysfunctions of perceptual categorization. J. Child Psychol. Psychiatry 58 (8), 939–949. 

- Wolff, N., Giller, F., Buse, J., Roessner, V., Beste, C., 2018. When repetitive mental sets increase cognitive flexibility in adolescent obsessive–compulsive disorder. J. Child Psychol. Psychiatry 59 (9), 1024–1032. 

- Woolley, J., Heyman, I., Brammer, M., Frampton, I., McGuire, P.K., Rubia, K., 2008. Brain activation in paediatric obsessive-compulsive disorder during tasks of inhibitory control. B. J. Psychiatry 192 (1), 25–31. 

- Xia, M., Wang, J., He, Y., 2013. BrainNet viewer: a network visualization tool for human brain connectomics. PLoS One 8 (7), e68910. 

- Yin, H.H., Knowlton, B.J., Balleine, B.W., 2004. Lesions of dorsolateral striatum preserve outcome expectancy but disrupt habit formation in instrumental learning. Eur. J. Neurosci. 19 (1), 181–189. 

- Yin, H.H., Ostlund, S.B., Knowlton, B.J., Balleine, B.W., 2005. The role of the dorsomedial striatum in instrumental conditioning. Eur. J. Neurosci. 22 (2), 513–523. 

- Zhang, L., Dong, Y., Ji, Y., Zhu, C., Yu, F., Ma, H., Chen, X., et al., 2015. Dissociation of decision making under ambiguity and decision making under risk: a neurocognitive endophenotype candidate for obsessive–compulsive disorder. Prog. NeuroPsychopharmacol. Biol. Psychiatry 57, 60–68. 

- Ziegler, G., Hauser, T.U., Moutoussis, M., Bullmore, E.T., Goodyer, I.M., Fonagy, P., Jones, P.B., NSPN Consortium, Lindenberger, U., Dolan, R.J., 2019. Compulsivity and impulsivity traits linked to attenuated developmental frontostriatal myelination trajectories. Nat. Neurosci. 22 (6), 992–999. 

- Zitterl, W., Urban, C., Linzmayer, L., Aigner, M., Demal, U., Semler, B., Zitterl-Eglseer, K., 2001. Memory deficits in patients with DSM-IV obsessive-compulsive disorder. Psychopathology 34 (3), 113–117. 

642 

