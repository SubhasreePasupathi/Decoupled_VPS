# Decoupled_VPS
The repo has the code and data of the novel Decoupled Video Panoptic Segmentation applied on SOTA VPS datasets such as Cityscapes VPS, KITTI STEP, and Waymo VPS datasets.


The Decoupled VPS is applied to the three datasets in which Cityscapes VPS is not subjected to any modification, while the other two datasets are subjected to the following modifications for the ground truth to get a common basis for comparision.

Renumbering of class ids
Eliminating the extra classes other than the ones considered
Reorganization of the instance mask representation to follow the Cityscapes VPS convention.
All the modified VPS masks of the KITTI STEP and Waymo dataset shall be found in the following link:T https://drive.google.com/drive/folders/1T2hEF7VbFGRytLEMxsbDKYg-ehi8NmUg?usp=sharing

The original datasets shall be downloaded from the respective link which is repeated here for reference: Cityscapes VPS Dataset: KITTI STEP Dataset Waymo VPS Dataset
