**comment** 

## Redefine statistical significance 

We propose to change the default _P_ -value threshold for statistical significance from 0.05 to 0.005 for claims of new discoveries. 

Daniel J. Benjamin, James O. Berger, Magnus Johannesson, Brian A. Nosek, E.-J. Wagenmakers, Richard Berk, Kenneth A. Bollen, Björn Brembs, Lawrence Brown, Colin Camerer, David Cesarini, Christopher D. Chambers, Merlise Clyde, Thomas D. Cook, Paul De Boeck, Zoltan Dienes, Anna Dreber, Kenny Easwaran, Charles Efferson, Ernst Fehr, Fiona Fidler, Andy P. Field, Malcolm Forster, Edward I. George, Richard Gonzalez, Steven Goodman, Edwin Green, Donald P. Green, Anthony Greenwald, Jarrod D. Hadfield, Larry V. Hedges, Leonhard Held, Teck Hua Ho, Herbert Hoijtink, Daniel J. Hruschka, Kosuke Imai, Guido Imbens, John P. A. Ioannidis, Minjeong Jeon, James Holland Jones, Michael Kirchler, David Laibson, John List, Roderick Little, Arthur Lupia, Edouard Machery, Scott E. Maxwell, Michael McCarthy, Don Moore, Stephen L. Morgan, Marcus Munafó, Shinichi Nakagawa, Brendan Nyhan, Timothy H. Parker, Luis Pericchi, Marco Perugini, Jeff Rouder, Judith Rousseau, Victoria Savalei, Felix D. Schönbrodt, Thomas Sellke, Betsy Sinclair, Dustin Tingley, Trisha Van Zandt, Simine Vazire, Duncan J. Watts, Christopher Winship, Robert L. Wolpert, Yu Xie, Cristobal Young, Jonathan Zinman and Valen E. Johnson 

he lack of reproducibility of scientific studies has caused growing concern Tover the credibility of claims of new discoveries based on ‘statistically significant’ findings. There has been much progress toward documenting and addressing several causes of this lack of reproducibility (for example, multiple testing, _P_ -hacking, publication bias and under-powered studies). However, we believe that a leading cause of non-reproducibility has not yet been adequately addressed: statistical standards of evidence for claiming new discoveries in many fields of science are simply too low. Associating statistically significant findings with _P_ < 0.05 results in a high rate of false positives even in the absence of other experimental, procedural and reporting problems. 

For fields where the threshold for defining statistical significance for new discoveries is _P_ < 0.05, we propose a change to _P_ < 0.005. This simple step would immediately improve the reproducibility of scientific research in many fields. Results that would currently be called significant but do not meet the new threshold should instead be called suggestive. While statisticians have known the relative weakness of using _P_ ≈ 0.05 as a threshold for discovery and the proposal to lower it to 0.005 is not new[1][,][2] , a critical mass of researchers now endorse this change. 

We restrict our recommendation to claims of discovery of new effects. We do 

not address the appropriate threshold for confirmatory or contradictory replications of existing claims. We also do not advocate changes to discovery thresholds in fields that have already adopted more stringent standards (for example, genomics and high-energy physics research; see the ‘Potential objections’ section below). 

We also restrict our recommendation to studies that conduct null hypothesis significance tests. We have diverse views about how best to improve reproducibility, and many of us believe that other ways of summarizing the data, such as Bayes factors or other posterior summaries based on clearly articulated model assumptions, are preferable to _P_ values. However, changing the _P_ value threshold is simple, aligns with the training undertaken by many researchers, and might quickly achieve broad acceptance. 

## **Strength of evidence from** _**P**_ **values** 

In testing a point null hypothesis _H_ 0 against an alternative hypothesis _H_ 1 based on data _x_ obs, the _P_ value is defined as the probability, calculated under the null hypothesis, that a test statistic is as extreme or more extreme than its observed value. The null hypothesis is typically rejected — and the finding is declared statistically significant — if the _P_ value falls below the (current) type I error threshold _α_ = 0.05. 

From a Bayesian perspective, a more direct measure of the strength of evidence for _H_ 1 relative to _H_ 0 is the ratio of their 

probabilities. By Bayes’ rule, this ratio may be written as: 

**==> picture [139 x 64] intentionally omitted <==**

where BF is the Bayes factor that represents the evidence from the data, and the prior odds can be informed by researchers’ beliefs, scientific consensus, and validated evidence from similar research questions in the same field. Multiple-hypothesis testing, _P_ -hacking and publication bias all reduce the credibility of evidence. Some of these practices reduce the prior odds of _H_ 1 relative to _H_ 0 by changing the population of hypothesis tests that are reported. Prediction markets[3] and analyses of replication results[4] both suggest that for psychology experiments, the prior odds of _H_ 1 relative to _H_ 0 may be only about 1:10. A similar number has been suggested in cancer clinical trials, and the number is likely to be much lower in preclinical biomedical research[5] . 

There is no unique mapping between the _P_ value and the Bayes factor, since the Bayes factor depends on _H_ 1. However, the connection between the two quantities can be evaluated for particular test statistics under certain classes of plausible alternatives (Fig. 1). 

**Nature HumaN BeHaviour** | VOL 2 | JANUARY 2018 | 6–10 | www.nature.com/nathumbehav 

**6** 

© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved. 

**comment** 

**==> picture [328 x 196] intentionally omitted <==**

**----- Start of picture text -----**<br>
100.0 100.0<br>Power<br>Likelihood ratio bound<br>50.0 UMPBT 50.0<br>Local− H 1 bound<br>25.7<br>20.0 20.0<br>13.9<br>10.0 10.0<br>5.0 5.0<br>3.4<br>2.4<br>2.0 2.0<br>1.0 1.0<br>0.5 0.5<br>0.3 0.3<br>0.0010 0.0025 0.0050 0.0100 0.0250 0.0500 0.1000<br>P  value<br>Bayes factor<br>**----- End of picture text -----**<br>


**Fig. 1 | relationship between the** _**P**_ **value and the Bayes factor.** The Bayes factor (BF) is defined as _f_ ( _x_ obs _H_ 1) . The figure assumes that observations are independent and identically distributed _f_ ( _x_ obs _H_ 0) (i.i.d.) according to _x_ ~ _N_ ( _μ_ , _σ_[2] ), where the mean _μ_ is unknown and the variance _σ_[2] is known. The _P_ value is from a two-sided _z_ -test (or equivalently a one-sided _χ_ 12-test) of the null hypothesis _H_ 0: _μ_ = 0. Power (red curve): BF obtained by defining _H_ 1 as putting ½ probability on _μ_ = ± _m_ for the value of _m_ that gives 75% power for the test of size _α_ = 0.05. This _H_ 1 represents an effect size typical of that which is implicitly assumed by researchers during experimental design. Likelihood ratio bound (black curve): BF obtained by defining _H_ 1 as putting ½ probability on _μ_ = ± _x_ , where _x_ is approximately equal to the mean of the observations. These BFs are upper bounds among the class of all _H_ 1 terms that are symmetric around the null, but they are improper because the data are used to define _H_ 1. UMPBT (blue curve): BF obtained by defining _H_ 1 according to the uniformly most powerful Bayesian test[2] that places ½ probability on _μ_ = ± _w_ , where _w_ is the alternative hypothesis that corresponds to a one-sided test of size 0.0025. This curve is indistinguishable from the ‘Power’ curve that would be obtained if the power used in its definition was 80% rather than 75%. Local-upper bound on the BF from among all unimodal alternative hypotheses that have a mode at the null and _H_ 1 bound (green curve): BF = − _ep_ 1ln _p_[, where ] _[p]_[ is the ] _[P]_[ value, is a large-sample ] satisfy certain regularity conditions[15] . The red numbers on the _y_ axis indicate the range of Bayes factors that are obtained for _P_ values of 0.005 or 0.05. For more details, see the Supplementary Information. 

evidence according to conventional Bayes factor classifications[6] . 

A two-sided _P_ value of 0.05 corresponds to Bayes factors in favour of _H_ 1 that range from about 2.5 to 3.4 under reasonable assumptions about _H_ 1 (Fig. 1). This is weak evidence from at least three perspectives. First, conventional Bayes factor categorizations[6] characterize this range as ‘weak’ or ‘very weak’. Second, we suspect many scientists would guess that _P_ ≈ 0.05 implies stronger support for _H_ 1 than a Bayes factor of 2.5 to 3.4. Third, using equation (1) and prior odds of 1:10, a _P_ value of 0.05 corresponds to at least 3:1 odds (that is, the 1 reciprocal of the product 10 × 3 4. ) in favour of the null hypothesis! 

Second, in many fields the _P_ < 0.005 standard would reduce the false positive rate to levels we judge to be reasonable. If we let _ϕ_ denote the proportion of null hypotheses that are true, 1 – _β_ the power of tests in rejecting false null hypotheses, and _α_ the type I error/significance threshold, then as the population of tested hypotheses becomes large, the false positive rate (that is, the proportion of true null effects among the total number of statistically significant findings) can be approximated by: 

**==> picture [155 x 20] intentionally omitted <==**

## **Why 0.005** 

The choice of any particular threshold is arbitrary and involves a trade-off between type I and type II errors. We propose 0.005 for two reasons. First, a two-sided _P_ value of 0.005 corresponds to Bayes factors between approximately 14 and 26 in favour of _H_ 1. This range represents ‘substantial’ to ‘strong’ 

For different levels of the prior odds that there is a true effect, 1 − _ϕ_ , and for _ϕ_ significance thresholds _α_ = 0.05 and _α_ = 0.005, Fig. 2 shows the false positive rate as a function of power 1− _β_ . 

In many studies, statistical power is low[7] . Figure 2 demonstrates that low statistical power and _α_ = 0.05 combine to produce high false positive rates. 

For many, the calculations illustrated by Fig. 2 may be unsettling. For example, the false positive rate is greater than 33% with prior odds of 1:10 and a _P_ value threshold of 0.05, regardless of the level of statistical power. Reducing the threshold to 0.005 would reduce this minimum false positive rate to 5%. Similar reductions in false positive rates would occur over a wide range of statistical powers. 

Empirical evidence from recent replication projects in psychology and experimental economics provide insights into the prior odds in favour of _H_ 1. In both projects, the rate of replication (that is, significance at _P_ < 0.05 in the replication in a consistent direction) was roughly double for initial studies with _P_ < 0.005 relative to initial studies with 0.005 < _P_ < 0.05: 50% versus 24% for psychology[8] , and 85% versus 44% for experimental economics[9] . Although based on relatively small samples of studies (93 in psychology, and 16 in experimental economics, after excluding initial studies with _P_ > 0.05), these numbers are suggestive of the potential gains in reproducibility that would accrue from the new threshold of _P_ < 0.005 in these fields. In biomedical research, 96% of a sample of recent papers claim statistically significant results with the _P_ < 0.05 threshold[10] . However, replication rates were very low[5] for these studies, suggesting a potential for gains by adopting this new standard in these fields as well. 

## **Potential objections** 

We now address the most compelling arguments against adopting this higher standard of evidence. 

## **The false negative rate would become** 

**unacceptably high.** Evidence that does not reach the new significance threshold should be treated as suggestive, and where possible further evidence should be accumulated; indeed, the combined results from several studies may be compelling even if any particular study is not. Failing to reject the null hypothesis does not mean accepting the null hypothesis. Moreover, the false negative rate will not increase if sample sizes are increased so that statistical power is held constant. 

For a wide range of common statistical tests, transitioning from a _P_ value threshold of _α_ = 0.05 to _α_ = 0.005 while maintaining 80% power would require an increase in sample sizes of about 70%. Such an increase means that fewer studies can be conducted using 

**Nature HumaN BeHaviour** | VOL 2 | JANUARY 2018 | 6–10 | www.nature.com/nathumbehav 

**7** 

© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved. 

## **comment** 

**==> picture [321 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.0<br>Prior odds = 1:40<br>Prior odds = 1:10<br>Prior odds = 1:5<br>0.8<br>0.6<br>P  < 0.05 threshold<br>0.4<br>0.2<br>P  < 0.005 threshold<br>0.0<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Power<br>False positive rate<br>**----- End of picture text -----**<br>


**Fig. 2 | relationship between the** _**P**_ **value threshold, power, and the false positive rate.** Calculated according to equation (2), with prior odds defined as 1 − _ϕ_ = Pr( _H_ 1) _ϕ_ Pr( _H_ 0)[. For more details, see ] the Supplementary Information. 

type II errors, and other factors that vary by research topic. For exploratory research with very low prior odds (well outside the range in Fig. 2), even lower significance thresholds than 0.005 are needed. Recognition of this issue led the genetics research community to move to a ‘genome-wide significance threshold’ of 5 × 10[–8] over a decade ago. And in high-energy physics, the tradition has long been to define significance by a ‘5-sigma’ rule (roughly a _P_ value threshold of 3 × 10[–7] ). We are essentially suggesting a move from a 2-sigma rule to a 3-sigma rule. 

current experimental designs and budgets. But Fig. 2 shows the benefit: false positive rates would typically fall by factors greater than two. Hence, considerable resources would be saved by not performing future studies based on false premises. Increasing sample sizes is also desirable because studies with small sample sizes tend to yield inflated effect size estimates[11] , and publication and other biases may be more likely in an environment of small studies[12] . We believe that efficiency gains would far outweigh losses. 

Our recommendation applies to disciplines with prior odds broadly in the range depicted in Fig. 2, where use of _P_ < 0.05 as a default is widespread. Within those disciplines, it is helpful for consumers of research to have a consistent benchmark. We feel the default should be shifted. 

**The proposal does not address multiplehypothesis testing,** _**P**_ **-hacking, publication bias, low power, or other biases (for example, confounding, selective reporting, and measurement error), which are arguably the bigger problems.** We agree. Reducing the _P_ value threshold complements — but does not substitute for — solutions to these other problems, which include good study design, ex ante power calculations, pre-registration of planned analyses, replications, and transparent reporting of procedures and all statistical analyses conducted. 

**Changing the significance threshold is a distraction from the real solution, which is to replace null hypothesis significance testing (and bright-line thresholds) with more focus on effect sizes and confidence intervals, treating the** _**P**_ **value as a continuous measure, and/or a Bayesian method.** Many of us agree that there are better approaches to statistical analyses than null hypothesis significance testing, but as yet there is no consensus regarding the appropriate choice of replacement. For example, a recent statement by the American Statistical Association addressed numerous issues regarding 

**The appropriate threshold for statistical significance should be different for different research communities.** We agree that the significance threshold selected for claiming a new discovery should depend on the prior odds that the null hypothesis is true, the number of hypotheses tested, the study design, the relative cost of type I versus 

the misinterpretation and misuse of _P_ values (as well as the related concept of statistical significance), but failed to make explicit policy recommendations to address these shortcomings[13] . Even after the significance threshold is changed, many of us will continue to advocate for alternatives to null hypothesis significance testing. 

## **Concluding remarks** 

Ronald Fisher understood that the choice of 0.05 was arbitrary when he introduced it[14] . Since then, theory and empirical evidence have demonstrated that a lower threshold is needed. A much larger pool of scientists are now asking a much larger number of questions, possibly with much lower prior odds of success. 

For research communities that continue to rely on null hypothesis significance testing, reducing the _P_ value threshold for claims of new discoveries to 0.005 is an actionable step that will immediately improve reproducibility. We emphasize that this proposal is about standards of evidence, not standards for policy action nor standards for publication. Results that do not reach the threshold for statistical significance (whatever it is) can still be important and merit publication in leading journals if they address important research questions with rigorous methods. This proposal should not be used to reject publications of novel findings with 0.005 < _P_ < 0.05 properly labelled as suggestive evidence. We should reward quality and transparency of research as we impose these more stringent standards, and we should monitor how researchers’ behaviours are affected by this change. Otherwise, science runs the risk that the more demanding threshold for statistical significance will be met to the detriment of quality and transparency. 

Journals can help transition to the new statistical significance threshold. Authors and readers can themselves take the initiative by describing and interpreting results more appropriately in light of the new proposed definition of statistical significance. The new significance threshold will help researchers and readers to understand and communicate evidence more accurately. ❐ 

Daniel J. Benjamin[1] *, James O. Berger[2] , Magnus Johannesson[3] *, Brian A. Nosek[4,5] , E.-J. Wagenmakers[6] , Richard Berk[7,10] , Kenneth A. Bollen[8] , Björn Brembs[9] , Lawrence Brown[10] , Colin Camerer[11] , David Cesarini[12,13] , Christopher D. Chambers[14] , Merlise Clyde[2] , Thomas D. Cook[15,16] , Paul De Boeck[17] , Zoltan Dienes[18] , Anna Dreber[3] , 

**Nature HumaN BeHaviour** | VOL 2 | JANUARY 2018 | 6–10 | www.nature.com/nathumbehav 

**8** 

© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved. 

**comment** 

Kenny Easwaran[19] , Charles Efferson[20] , Ernst Fehr[21] , Fiona Fidler[22] , Andy P. Field[18] , Malcolm Forster[23] , Edward I. George[10] , Richard Gonzalez[24] , Steven Goodman[25] , Edwin Green[26] , Donald P. Green[27] , Anthony G. Greenwald[28] , Jarrod D. Hadfield[29] , Larry V. Hedges[30] , Leonhard Held[31] , Teck Hua Ho[32] , Herbert Hoijtink[33] , Daniel J. Hruschka[34] , Kosuke Imai[35] , Guido Imbens[36] , John P. A. Ioannidis[37] , Minjeong Jeon[38] , James Holland Jones[39,40] , Michael Kirchler[41] , David Laibson[42] , John List[43] , Roderick Little[44] , Arthur Lupia[45] , Edouard Machery[46] , Scott E. Maxwell[47] , Michael McCarthy[48] , Don A. Moore[49] , Stephen L. Morgan[50] , Marcus Munafó[51,52] , Shinichi Nakagawa[53] , Brendan Nyhan[54] , Timothy H. Parker[55] , Luis Pericchi[56] , Marco Perugini[57] , Jeff Rouder[58] , Judith Rousseau[59] , Victoria Savalei[60] , Felix D. Schönbrodt[61] , Thomas Sellke[62] , Betsy Sinclair[63] , Dustin Tingley[64] , Trisha Van Zandt[65] , Simine Vazire[66] , 

Duncan J. Watts[67] , Christopher Winship[68] , Robert L. Wolpert[2] , Yu Xie[69] , Cristobal Young[70] , Jonathan Zinman[71] and Valen E. Johnson[72] * 

_1 Center for Economic and Social Research and Department of Economics, University of Southern California, Los Angeles, CA 90089-3332, USA._ 

_2 Department of Statistical Science, Duke University, Durham, NC 27708-0251, USA.[3] Department of Economics, Stockholm School of Economics, Stockholm SE-113 83, Sweden.[4] University of Virginia, Charlottesville, VA 22908, USA.[5] Center for Open Science, Charlottesville, VA 22903, USA. 6 Department of Psychology, University of Amsterdam, Amsterdam 1018 VZ, The Netherlands.[7] School of Arts and Sciences and Department of Criminology, University of Pennsylvania, Philadelphia, PA 19104-6286, USA.[8] Department of Psychology and Neuroscience, Department of Sociology, University of North Carolina Chapel Hill, Chapel Hill, NC 27599-3270, USA.[9] Institute of Zoology — Neurogenetics, Universität Regensburg, Universitätsstrasse 31, 93040 Regensburg, Germany. 10 Department of Statistics, The Wharton School, University of Pennsylvania, Philadelphia, PA 19104, USA.[11] Division of the Humanities and Social Sciences, California Institute of Technology, Pasadena, CA 91125, USA.[12] Department of Economics, New York University, New York, NY 10012, USA.[13] The Research Institute of Industrial Economics (IFN), Stockholm SE-102 15, Sweden. 14 Cardiff University Brain Research Imaging Centre (CUBRIC), Cardiff CF24 4HQ, UK.[15] Northwestern University, Evanston, IL 60208, USA.[16] Mathematica Policy Research, Washington, DC 20002-4221, USA. 17 Department of Psychology, Quantitative Program, Ohio State University, Columbus, OH 43210, USA. 18 School of Psychology, University of Sussex, Brighton BN1 9QH, UK.[19] Department of Philosophy, Texas A&M University, College Station, TX 77843-4237, USA.[20] Department of Psychology, Royal Holloway_ 

_University of London, Egham Surrey TW20 0EX, UK.[21] Department of Economics, University of Zurich, 8006 Zurich, Switzerland.[22] School of BioSciences and School of Historical & Philosophical Studies, University of Melbourne, Parkville, VIC 3010, Australia.[23] Department of Philosophy, University of Wisconsin — Madison, Madison, WI 53706, USA.[24] Department of Psychology, University of Michigan, Ann Arbor, MI 48109-1043, USA. 25 Stanford University, General Medical Disciplines, Stanford, CA 94305, USA.[26] Department of Ecology, Evolution and Natural Resources SEBS, Rutgers University, New Brunswick, NJ 08901-8551, USA. 27 Department of Political Science, Columbia University in the City of New York, New York, NY 10027, USA.[28] Department of Psychology, University of Washington, Seattle, WA 98195-1525, USA. 29 Institute of Evolutionary Biology School of Biological Sciences, The University of Edinburgh, Edinburgh EH9 3JT, UK.[30] Weinberg College of Arts & Sciences Department of Statistics, Northwestern University, Evanston, IL 60208, USA.[31] Epidemiology, Biostatistics and Prevention Institute (EBPI), University of Zurich, 8001 Zurich, Switzerland._ 

_32 National University of Singapore, Singapore 119077, Singapore.[33] Department of Methods and Statistics, Universiteit Utrecht, Utrecht 3584 CH, The Netherlands.[34] School of Human Evolution and Social Change, Arizona State University, Tempe, AZ 85287-2402, USA.[35] Department of Politics and Center for Statistics and Machine Learning, Princeton University, Princeton, NJ 08544, USA. 36 Stanford University, Stanford, CA 94305-5015, USA.[37] Departments of Medicine, of Health Research and Policy, of Biomedical Data Science, and of Statistics and Meta-Research Innovation Center at Stanford (METRICS), Stanford University, Stanford, CA 94305, USA.[38] Advanced Quantitative Methods, Social Research Methodology, Department of Education, Graduate School of Education & Information Studies, University of California, Los Angeles, CA 90095-1521, USA.[39] Department of Life Sciences, Imperial College London, Ascot SL5 7PY, UK.[40] Department of Earth System Science, Stanford, CA 94305-4216, USA.[41] Department of Banking and Finance, University of Innsbruck and University of Gothenburg, Innsbruck A-6020, Austria.[42] Department of Economics, Harvard University, Cambridge, MA 02138, USA._ 

_43 Department of Economics, University of Chicago, Chicago, IL 60637, USA.[44] Department of Biostatistics, University of Michigan, Ann Arbor, MI 48109-2029, USA.[45] Department of Political Science, University of Michigan, Ann Arbor, MI 48109-1045, USA.[46] Department of History and Philosophy of Science, University of Pittsburgh, Pittsburgh, PA 15260, USA.[47] Department of Psychology, University of Notre Dame, Notre Dame, IN 46556, USA. 48 School of BioSciences, University of Melbourne, Parkville, VIC 3010, Australia.[49] Haas School of Business, University of California at Berkeley, Berkeley, CA 94720-1900A, USA.[50] Johns Hopkins University, Baltimore, MD 21218, USA.[51] MRC Integrative Epidemiology Unit, University of Bristol,_ 

_Bristol BS8 1TU, UK.[52] UK Centre for Tobacco and Alcohol Studies, School of Experimental Psychology, University of Bristol, Bristol BS8 1TU, UK._ 

_53 Evolution & Ecology Research Centre and School of Biological, Earth and Environmental Sciences, University of New South Wales, Sydney, NSW 2052, Australia.[54] Department of Government, Dartmouth College, Hanover, NH 03755, USA.[55] Department of Biology, Whitman College, Walla Walla, WA 99362, USA.[56] Department of Mathematics, University of Puerto Rico, Rio Piedras Campus, San Juan, PR 00936-8377, Puerto Rico.[57] Department of Psychology, University of Milan-Bicocca, Milan 20126, Italy.[58] Department of Cognitive Sciences, University of California, Irvine, CA 92617, USA. 59 Université Paris Dauphine, 75016, Paris, France. 60 Department of Psychology, The University of British Columbia, Vancouver V6T 1Z4 BC, Canada._ 

_61 Department Psychology, Ludwig-MaximiliansUniversity Munich, Leopoldstraβ e 13, 80802 Munich, Germany.[62] Department of Statistics, Purdue University, West Lafayette, IN 47907-2067, USA. 63 Department of Political Science, Washington University in St. Louis, St. Louis, MO 63130-4899, USA.[64] Government Department, Harvard University, Cambridge, MA 02138, USA. 65 Department of Psychology, Ohio State University, Columbus, OH 43210, USA.[66] Department of Psychology, University of California, Davis, CA 95616, USA.[67] Microsoft Research, 641 Avenue of the Americas, 7th Floor, New York, NY 10011, USA. 68 Department of Sociology, Harvard University, Cambridge, MA 02138, USA.[69] Department of Sociology, Princeton University, Princeton, NJ 08544, USA.[70] Department of Sociology, Stanford University, Stanford, CA 94305-2047, USA.[71] Department of Economics, Dartmouth College, Hanover, NH 03755-3514, USA.[72] Department of Statistics, Texas A&M University, College Station, TX 77843, USA. *e-mail: daniel.benjamin@gmail.com; magnus.johannesson@hhs.se; vejohnson@exchange.tamu.edu_ 

Published online: 1 September 2017 DOI: 10.1038/s41562-017-0189-z 

## References 

1. Greenwald, A. G. et al. _Psychophysiology_ **33** , 175–183 (1996). 

2. Johnson, V. E. _Proc. Natl Acad. Sci. USA_ **110** , 19313–19317 (2013). 

3. Dreber, A. et al. _Proc. Natl Acad. Sci. USA_ **112** , 15343–15347 (2015). 

4. Johnson, V. E. et al. _J. Am. Stat. Assoc._ **112** , 1–10 (2016). 

5. Begley, C. G. & Ioannidis, J. P. A. _Circ. Res._ **116** , 116–126 (2015). 

6. Kass, R. E. & Raftery, A. E. _J. Am. Stat. Assoc._ **90** , 773–795 (1995). 

7. Szucs, D. & Ioannidis, J. P. A. _PLoS Biol._ **15** , e2000797 (2017). 

8. Open Science Collaboration. _Science_ **349** , aac4716 (2015). 

9. Camerer, C. F. et al. _Science_ **351** , 1433–1436 (2016). 

10. Chavalarias, D. et al. _JAMA_ **315** , 1141–1148 (2016). 

11. Gelman, A. & Carlin, J. _Perspect. Psychol. Sci._ **9** , 641–651 (2014). 

12. Fanelli, D., Costas, R. & Ioannidis, J. P. A. _Proc. Natl Acad. Sci. USA_ **114** , 3714–3719 (2017). 

13. Wasserstein, R. L. & Lazar, N. A. _Am. Stat._ **70** , 129–133 (2016). 

14. Fisher, R. A. _Statistical Methods for Research Workers_ (Oliver & Boyd, Edinburgh, 1925). 

**Nature HumaN BeHaviour** | VOL 2 | JANUARY 2018 | 6–10 | www.nature.com/nathumbehav 

**9** 

© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved. 

## **comment** 

15. Sellke, T., Bayarri, M. J. & Berger, J. O. _Am. Stat._ **55** , 62–71 (2001). 

## Acknowledgements 

We thank D. L. Lormand, R. Royer and A. T. Nguyen Viet for excellent research assistance. 

## Competing interests 

One of the 72 authors, Christopher Chambers, is a member of the Advisory Board of _Nature Human Behaviour_ . Christopher Chambers was not a corresponding author and did not communicate with the editors regarding the 

publication of this article. The other authors declare no competing interests. 

## Additional information 

Supplementary information is available for this paper at doi:10.1038/s41562-017-0189-z. 

**Nature HumaN BeHaviour** | VOL 2 | JANUARY 2018 | 6–10 | www.nature.com/nathumbehav 

**10** 

© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved. 

