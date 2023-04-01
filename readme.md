# Cryo-EM data "Particle picker"

Cryo-electron microscopy (cryo-EM) is a powerful imaging technique used to study biological macromolecules at near-atomic resolution. In cryo-EM experiments, a beam of electrons is fired at a frozen sample, and the resulting images are used to reconstruct the 3D structure of the sample.

Particle picking is an important step in cryo-EM data processing, where individual particle images are identified from the raw cryo-EM images. The goal of particle picking is to extract high-quality images of individual particles for further processing.

### Building a pipeline for cryo-EM reconstruction
Machine learning-based methods: Train a machine learning model to classify particles into different categories based on their similarity to the manually selected ones.

##### Stages:
a) Provide the input data

b) A decision per image

c) Image clusterings

d) Clustering visualisation
[![cluster.png](Pictures%2Fcluster.png)]