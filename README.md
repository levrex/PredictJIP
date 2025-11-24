# PredictJIP
Repository featuring models for the prediction of Joint Involvement Patterns (JIP) in Rheumatoid arthrtitis

For more information on the clinical relevance of the JIPs read our study : https://www.nature.com/articles/s41746-025-01997-1

## Background
To make our clusters easier to use across different centers, we developed machine-learning surrogate models that can predict a patient’s JIP using a smaller set of variables. Because the primary axes of variation in our data are the *hand–feet differentiation* and the *oligo–poly joint involvement* (few vs. many affected joints), we found that JIP can be predicted reasonably well even with limited information.  
We therefore built two probabilistic models, each designed around the types of joint assessments that centers most commonly collect. These models output class probabilities, enabling users to choose decision thresholds that best fit their desired balance of precision, sensitivity, or overall accuracy. However, note that applying a very stringent cut-off may result in patients not being assigned to any cluster at all.

The two models—each validated on a hold-out set—are based on the following joint schemes (and ACPA, RF, Age & Sex):
- DAS44 (minimally required)
- DAS66/68 (ideal)

## Overview of JIP-related Github Repo's
![alt text](figures/md/Overview_JIP_related_git.png)

### Different ways to detect the JIPs
In order to identify JIPs, you have three options: 
1. (Re)clusering : run entire cluster analysis again, see our original clustering pipeline [EHR-clustering](https://github.com/levrex/EHR-Clustering-RA)
2. Projection : project patients on latent space [POODLE](https://github.com/levrex/Poodle) or use our client-based webtool [Rheumalyze](https://knevel-lab.github.io/Rheumalyze/)
3. Prediction : use a surrogate technique to predict the JIP cluster (This github repo!)

## Contact
If you experience difficulties with implementing the pipeline or if you have any other questions feel free to send me an e-mail. You can contact me on: t.d.maarseveen@lumc.nl 
