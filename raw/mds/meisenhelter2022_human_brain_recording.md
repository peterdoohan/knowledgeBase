**ll** 

**==> picture [46 x 35] intentionally omitted <==**

## Previews 

# Probing the human brain at single-neuron resolution with high-density cortical recordings 

Stephen Meisenhelter[1] and Ueli Rutishauser[1][,][2][,][3][,] * 

1Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA 90048, USA 

2Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA 91125, USA 

3Center for Neural Science and Medicine, Department of Biomedical Sciences, Cedars-Sinai Medical Center, Los Angeles, CA 90048, USA *Correspondence: ueli.rutishauser@cshs.org https://doi.org/10.1016/j.neuron.2022.07.014 

Recording in vivo from large numbers of neurons is a core neuroscience technique not typically possible in humans. In this issue of Neuron, Chung et al. (2022) show high-density acute recordings in human cortex using the Neuropixels probe. 

Using extracellular recordings to observe the spiking activity of neurons in vivo is one of the key tools of neuroscience. Recent studies have shown that recording simultaneously from multiple neurons can provide powerful insights into populationlevel representations and neural computation (Vyas et al., 2020) that could not have been discovered by only recording one cell at a time. The sophistication of extracellular recordings has increased substantially in recent decades, with the number of neurons being recorded simultaneously in animals doubling approximately every 7 years (Hong and Lieber, 2019). Newly developed semiconductorbased microfabrication, which enables tight packing of large numbers of miniscule recording pads onto a silicon electrode shaft, has been a major contributor to this development (Jun et al., 2017). A variety of electrodes made using this technique are now in routine use in animals. In rare cases, extracellular singleneuron recordings are performed in humans for clinical purposes or for research purposes alongside clinical procedures. However, these recordings have used either microwire brushes or the Utah array; high-density silicon probes have not been used in humans because of a variety of technical and clinical hurdles. 

The Neuropixels probe is a 960-channel electrode that was originally developed for acute high-density recordings in the rodent brain (Jun et al., 2017). Electrode pads are distributed along a 10-mmlong, 70-mm-wide, and 97-mm-thick elec- 

trode shank (note that this modified version is thicker than the version used in rodents). In rodents, this probe can routinely record dozens of neurons (‘‘units’’). These neurons can be isolated with high confidence because they are visible on multiple channels. Neuropixels probes have been widely used in studies that would not have been possible without the scale and recording density provided by this new technology (Siegle et al., 2021). 

In this issue of Neuron, Chung et al. (2022) present a new protocol for the use of the Neuropixels probe in intraoperative recordings from patients undergoing epilepsy surgery or brain tumor resection. Using this protocol, they obtained highquality simultaneous single-neuron recordings from up to 100 neurons in the human cortex for up to 20 min per session. Together with a simultaneously published study (Paulk et al., 2022), this work presents the challenges and successes of using this new electrode in humans alongside a characterization of spike sorting and unit stabilization tools that showcase the power of a dense electrode array for elucidating the fine spatial and temporal structure of micro-scale cortical activity. 

Safety is of paramount importance when introducing a new research or clinical tool for human use. For this reason, in the work by Chung et al., the probe was only inserted into tissue that was about to be resected. Probes were sterilized using standard medical-grade processes and were discarded after a single 

use. The study did not note any tissue compatibility problems as assessed by histology, although the devices were only inserted for a short time (up to 20 min). 

The authors overcame numerous obstacles to make the Neuropixels probe suitable for human use. The first problem was the fragility of the probe: it snapped in three of the early subjects. Each breakage resulted in a single fragment that could be removed with forceps. But tracking and removing probe fragments requires direct visibility of the probe throughout the experiment, which does not allow stabilization using fibrin sealants as is typically done to increase stability. It seems that this problem might resolve with practice: in both the studies by Chung et al. and Paulk et al. (where there were similar problems), the breakages were limited to early subjects. 

Recordings took place in the operating room, making contamination of the neural signal with electrical noise a significant challenge. Surgery requires the use of many electrical devices, including electrocautery tools and anesthesia equipment. The authors report that removing AC-powered devices from electrical contact with the subject and switching other devices to run on direct current power was effective in reducing electrical noise. After these mitigations, signal quality was high with a median signal-to-noise ratio of 4.2 and a noise floor of 6.81 mV in the 300–6,000 Hz band. This allowed Chung et al. to isolate large numbers of 

**==> picture [17 x 17] intentionally omitted <==**

Neuron 110, August 3, 2022 ª 2022 Elsevier Inc. 2353 

Previews 

## **ll** 

**==> picture [420 x 189] intentionally omitted <==**

Figure 1. Illustration of the Neuropixel probe layout relative to human cortical brain tissue (A) Schematic of the Neuropixels array overlaid on a NeuN-stained (showing most neurons) section of human prefrontal cortex (BA9). (B) Small section of the Neuropixels array overlaid on a SMI32-stained (showing pyramidal cells) section of human prefrontal cortex (BA9). (C) Reconstructed human spiny neuron (Cell ID 569844159 from middle temporal gyrus; see https://celltypes.brain-map.org/). Overlayed simulated extracellular action potentials recorded at different locations illustrate how the spikes of the same neuron are visible on multiple recording pads. Individual Neuropixels recording pads are shown as red squares to demonstrate scale. Modified with permission from Csercsa et al. (2010) (A and B) and Mosher et al. (2020) (C). 

units, with a median of 54.2 single units per probe. 

The activity of neurons is often suppressed immediately after insertion of a microelectrode. For this reason, recordings in animal studies are typically not attempted for several hours while the electrode ‘‘settles’’ and nearby neurons return to their typical firing patterns. If the Neuropixels probe caused the same problem, intraoperative recordings would be impractical. Fortunately, Chung et al. found that single units became active, on average, 8.8 s after probe insertion. Paulk et al. had similar findings—units began firing within minutes of probe insertion. 

The recordings were also limited by the use of anesthesia in the intraoperative environment. Anesthesia causes major changes in neuronal activity, which may limit the generalizability of studies conducted in anesthetized subjects. In some of the subjects, the recordings were performed after waking the patient during surgery (a common technique in neurosurgery). Even in this case, however, remaining amounts of anesthetics may have long-lasting effects that can affect both neuronal activity and patient behavior. Although these impacts can be somewhat mitigated through the use of other anesthetic agents, the clinical team 

must ensure that drug changes designed to improve the quality of research recordings do not affect the efficacy or safety of clinical practices (Feinsinger et al., 2022). 

The final major difficulty lies in keeping the electrode aligned with neuronal tissue as the brain pulsates throughout the cardiac cycle (Mosher et al., 2020). In this study, the probes were anchored to a head clamp and held stationary relative to the skull. As a result, the recorded single units slid along the electrode track as the brain moved within the skull. The authors used the dense geometry of the Neuropixels probe to track this movement. Additionally, they only inserted 7 mm (out of 10 mm) of the shank so that they could continuously measure the location of the air/brain boundary. They found that there was an average of 251 mm of vertical motion. While there was a significant negative correlation between motion amplitude and single unit yield, there was no correlation between motion amplitude and the proportion of the time during which each single unit could be detected. This is likely because the motion was principally along the long axis of the electrode and that most units were detected on electrodes close to the middle of the shank. This way, even when the brain moves, the units are always near an electrode. In addition to 

applying a motion-correction algorithm, the authors recommended minimizing pulsation by reducing positive end-expiratory pressure in intubated patients and by asking awake patients to avoid voluntary movements. 

The real strength of the Neuropixels probe is not the sheer number of units that can be recorded simultaneously. As impressive as that capability is, similar numbers of neurons have been recorded in humans with multiple Behnke-Fried electrodes (Mosher et al., 2020) and with the Utah array (Aflalo et al., 2015). What makes the Neuropixels probe truly distinct is the high density of its electrode array along the full 1 cm shaft length, with contacts every 20 mm. Each electrode pad is 12 mm by 12 mm in size, which is smaller than the typical human neuron (Figures 1A and 1B). With this electrode density, a single neuron is detectable on a median of 11 channels (Figure 1C), thereby greatly improving spike-sorting quality over less-dense arrays (Chung et al., 2022). Likewise, Paulk et al. found that 52% of units were present on multiple channels at 5 standard deviations above background noise. More fundamentally, this type of dense recording makes it uniquely possible to assess the activity of neurons within the same cortical column across the lamina of the cortex and 

2354 Neuron 110, August 3, 2022 

## Previews 

to provide a readily interpretable spatial map of the evolution of local field potentials in real time. This capability will also dramatically increase the likelihood of recording synaptically connected pairs of cells, opening the door for in vivo studies of synaptogenesis in humans. 

The overwhelming majority of those who participate in invasive electrophysiological research are people with epilepsy. Therefore, pathophysiology of epilepsy is ripe for investigation using this technology. In many cases, the epileptogenic focus can be a microscopic cortical dysplasia. With precise targeting, the Neuropixels probe could be used to examine the network dynamics within these areas of structural malformation. High-density recordings made possible by this new technology could reveal a more complete understanding of ictogenesis, potentially leading to new treatment options. 

As the Neuropixels probe continues to be developed, it seems plausible that there could soon be a version suitable for acute implantation during inpatient monitoring or even chronic implantation as part of a neurostimulation system. While the CMOS process used to manufacture the Neuropixels probe produces circuitry with fantastically small components, the rigid silicon substrate also means that the probe has a non-implantable ‘‘base,’’ which contains circuitry to 

amplify and digitize the brain signal, rigidly attached in the same plane as the probe’s shank. Critical technologies to create a free-floating probe with similar density, such as flexible polyimide substrates for photolithography applications, are already being studied for application in neuroscience. Through the combined efforts of neuroscientists, neurosurgeons, and engineers, the next several years may see another dramatic improvement in recording technology as profound as the Neuropixels probe. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

## REFERENCES 

Aflalo, T., Kellis, S., Klaes, C., Lee, B., Shi, Y., Pejsa, K., Shanfield, K., Hayes-Jackson, S., Aisen, M., Heck, C., et al. (2015). Decoding motor imagery from the posterior parietal cortex of a tetraplegic human. Science 348, 906–910. https:// doi.org/10.1126/science.aaa5417. 

Chung, J.E., Sellers, K.K., Leonard, M.K., Gwilliams, L., Xu, D., Dougherty, M.E., Kharazia, V., Metzger, S.L., Welkenhuysen, M., Dutta, B., and Chang, E.F. (2022). High-density single-unit human cortical recordings using the Neuropixels probe. Neuron 110, 2409–2421. https://doi.org/ 10.1016/j.neuron.2022.05.007. 

ErSzCsercsa,oss,}ucs,} L.,A.,R.,Entz,Kelemen,Dombova´ ri,L., So´ lyom,A.,B.,etFabo´ ,al.A.,(2010).D.,Ra´ sonyi,Wittner,LaminarG.,L., analysis of slow wave activity in humans. Brain 133, 2814–2829. https://doi.org/10.1093/brain/ awq169. 

## **ll** 

Feinsinger, A., Pouratian, N., Ebadi, H., Adolphs, R., Andersen, R., Beauchamp, M.S., Chang, E.F., Crone, N.E., Collinger, J.L., Fried, I., et al. (2022). Ethical commitments, principles, and practices guiding intracranial neuroscientific research in humans. Neuron 110, 188–194. https://doi.org/10. 1016/j.neuron.2021.11.011. 

Hong, G., and Lieber, C.M. (2019). Novel electrode technologies for neural recordings. Nat. Rev. Neurosci. 20, 330–345. https://doi.org/10.1038/ s41583-019-0140-6. 

Jun, J.J., Steinmetz, N.A., Siegle, J.H., Denman, D.J., Bauza, M., Barbarits, B., Lee, A.K., Anastassiou, C.A., Andrei, A., Aydın, C¸ ., et al. (2017). Fully integrated silicon probes for high-density recording of neural activity. Nature 551, 232–236. https://doi.org/10.1038/nature24636. 

Mosher, C.P., Wei, Y., Kaminski,� J., Nandi, A., Mamelak, A.N., Anastassiou, C.A., and Rutishauser, U. (2020). Cellular classes in the human brain revealed in vivo by heartbeat-related modulation of the extracellular action potential waveform. Cell Rep. 30, 3536–3551.e6. https:// doi.org/10.1016/j.celrep.2020.02.027. 

Paulk, A.C., Kfir, Y., Khanna, A.R., Mustroph, M.L., Trautmann, E.M., Soper, D.J., Stavisky, S.D., Welkenhuysen, M., Dutta, B., Shenoy, K.V., et al. (2022). Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex. Nat. Neurosci. 25, 252–263. https:// doi.org/10.1038/s41593-021-00997-0. 

Siegle, J.H., Jia, X., Durand, S., Gale, S., Bennett, C., Graddis, N., Heller, G., Ramirez, T.K., Choi, H., Luviano, J.A., et al. (2021). Survey of spiking in the mouse visual system reveals functional hierarchy. Nature 592, 86–92. https://doi.org/10.1038/ s41586-020-03171-x. 

Vyas, S., Golub, M.D., Sussillo, D., and Shenoy, K.V. (2020). Computation through neural population dynamics. Annu. Rev. Neurosci. 43, 249–275. https://doi.org/10.1146/annurev-neuro-092619094115. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, August 3, 2022 2355 

