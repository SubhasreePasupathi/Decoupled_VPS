
# Decoupled Approaches for Road Semantics-Inclusive Video Panoptic Segmentation in Autonomous Driving

## **Official Implementation for *Decoupled Approaches for Road Semantics-Inclusive Video Panoptic Segmentation in Autonomous Driving* submitted to the The Visual Computer Journal
## [[Modified Dataset](https://drive.google.com/drive/folders/1T2hEF7VbFGRytLEMxsbDKYg-ehi8NmUg?usp=sharing)] [[Original Cityscapes VPS Dataset](https://www.dropbox.com/scl/fi/th8t12uvalox9fopzlab1/cityscapes-vps-dataset-1.0.zip?rlkey=rfd1prz6jsn4kxi1nc04gqqsr&e=1&dl=0)]
The repo has the code and data of the novel Decoupled Video Panoptic Segmentation applied on SOTA VPS datasets such as Cityscapes VPS, KITTI STEP, and Waymo VPS datasets. The work is presented in the article titled


The Decoupled VPS is applied to the three datasets in which Cityscapes VPS is not subjected to any modification, while the other two datasets are subjected to the following modifications for the ground truth to get a common basis for comparision.

Renumbering of class ids
Eliminating the extra classes other than the ones considered
Reorganization of the instance mask representation to follow the Cityscapes VPS convention.
In this research work Cityscapes VPS is adopted as standard while the KITTI STEP and VPS masks form the Waymo dataset are converted to stadard format (Cityscaopes format). All the modified VPS masks of the KITTI STEP and Waymo dataset shall be found in the following link:T 

The original datasets particularly the RGB input images shall be downloaded from the respective link which is repeated here for reference: 

Cityscapes VPS Dataset: 

KITTI STEP Dataset: https://www.cvlibs.net/datasets/kitti/eval_step.php

Waymo VPS Dataset (PVPS only required):https://waymo.com/open/download

**MERGING APPROACHES**

The codes required for the mask merging of instance masks and segmentation masks along with tracking data in both MS and MIS approaches are presented in *mask_merge* folder.

**FORMAT CONVERSIONS**

The following  changes needs to be made in order to repeat the work presented in the article published.

Use the code from the folder *format_conversion_for_inst_eval* to generate instance masks based on (1) Deepmac and class id generated from object detection matching and (2) PCAN instance masks converted to a common convention for pixel level marking of class and instance ids.

Use the code from the folder *format_conversion_for_kittti_step_vpq* to convert the KITTI STEP data to the coomon format for applying video panoptic quality evaluation metrics for .

Use the code from the folder *formats_conversion_for_track_eval* to convert all the data to the coomon format for applying evaluation metrics related to tracking performance.

Use the codes in *modify_waymoids_to_cv_ids* to convert the instance ids of waymo masks to standard format used in the paper.

**EVALUATION**

All the codes related to evaluation metrics reported in the article are presented in the folder *eval*

Codes for VPQ metrics are presented in the vpq folder which will take care of the adoption required for the KITTI STEP and Waymo datasets.

