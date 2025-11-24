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
1. (Re)clustering : run entire cluster analysis again, see our original clustering pipeline [EHR-clustering](https://github.com/levrex/EHR-Clustering-RA)
2. Projection : project patients on latent space [POODLE](https://github.com/levrex/Poodle) or use our client-based webtool [Rheumalyze](https://knevel-lab.github.io/Rheumalyze/)
3. Prediction : use a surrogate technique to predict the JIP cluster (This github repo!)

## Directory Structure
* `README.md`: This file
* `requirements.txt`: Prerequisite python modules (with version numbers) to run code
* `figures/md`: Figures used for the readme
* `figures/das44`: Figures for the DAS44 model (i.e. SHAP feature importance plot)
* `models/*`: Contains the final models for predicting the JIP
  * `models/das44/JIP_xgb_pred_44.pk` : Pickle object containing DAS44 model (also needs age, sex, acpa & rf)
* `src/*`: Important functions for feature engineering
  * `src/DAS44_joints.py`: Contains lists of DAS44 joints for each anatomical location (based on Leiden EHR naming convention)
  * `src/DAS66_joints.py`: (WIP) Contains lists of DAS66 joints for each anatomical location (based on Leiden EHR naming convention) 
* `notebooks/*`: Example notebooks showing how to run the code
  * `notebooks/Example_notebook_das44.ipynb`: How to run DAS44 model (or retrain)
  * `notebooks/Example_KAN_encoder_optimization.ipynb`: How to train the ensemble KAN-encoder

## Contact
If you experience difficulties with implementing the pipeline or if you have any other questions feel free to send me an e-mail. You can contact me on: t.d.maarseveen@lumc.nl 
