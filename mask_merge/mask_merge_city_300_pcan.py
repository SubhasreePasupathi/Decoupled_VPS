#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:49:40 2022

@author: subha
"""

import os
from PIL import Image
import numpy as np


#According to mask created by subha
bdd_classes={'person':8, 'rider':1, 'car':2, 'truck':3, 'bus':4, 'train':5, 'motorcycle':6,  'bicycle':7}



#city_vps_things_classes
city_classes={0: "road", 1: "sidewalk", 2: "building", 3: "wall", 4: "fence", 5: "pole", 6: "traffic light", 7: "traffic sign", 8: "vegetation", 9: "terrain", 10: "sky", 11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

#pixel ids convertion dict
bdd_to_city={0: 0, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}



def maskmerge(psp_path,pcan_path,res_fol):
    
    psp_im=Image.open(psp_path)
    pcan_im=Image.open(pcan_path)
    
    pcan_arr=np.array(pcan_im)
    psp_arr=np.array(psp_im)
    
    #converting bdd ids to city ids in pcan mask
    pcan_id_conv_arr=np.zeros((pcan_arr.shape),np.uint8)
    pcan_seg_ids=np.unique(pcan_arr[:,:,0])
    print(pcan_seg_ids)
    for id in pcan_seg_ids:
        mask=pcan_arr[:,:,0]==id
        pcan_id_conv_arr[mask]=bdd_to_city[id]
        
    pcan_id_conv_arr[:,:,1] = pcan_arr[:,:,1]
    pcan_id_conv_arr[:,:,2] = pcan_arr[:,:,2]
    
    pcan_seg_ids=np.unique(pcan_id_conv_arr[:,:,0])
    print(pcan_seg_ids)
    
    #Mask merge
    pp_arr=np.zeros((pcan_arr.shape),np.uint8)
    pp_arr[:,:,0]=255
    
    psp_stuff_ids=np.unique(psp_arr)
    pcan_obj_ids=np.unique(pcan_id_conv_arr[:,:,2])
    
    for stuff_id in psp_stuff_ids:
        if stuff_id<=10:
            mask=psp_arr==stuff_id
            pp_arr[:,:,0][mask]=stuff_id
    
    for oid in pcan_obj_ids:
        if oid != 0:
           
            mask=pcan_id_conv_arr[:,:,2]==oid
            pp_arr[:,:,2][mask]=oid
            pp_arr[:,:,0][mask]=pcan_id_conv_arr[:,:,0][mask]
    
    
    #save
    print(np.unique(pp_arr[:,:,0]))
    print(np.unique(pp_arr[:,:,2]))
    
    
        
    pp_im=Image.fromarray(pp_arr.astype('uint8'))
    #pp_im.show()
    pp_im.save(os.path.join(res_fol,os.path.basename(pcan_path)))
    


if __name__ == '__main__':
    
    psp_root="/home/subha/Videos/Paper1_results/directly_from_nws/sseg/kitti_step_val_sseg/"
    pcan_root="/home/subha/Videos/Paper1_results/directly_from_nws/pcan/pcan_track_result_mask_val_kitti_step_with_bdd_pcan_cat_ids"
    
    psp_paths=[]
    pcan_paths=[]
    for dirpath,dirnames,filenames in os.walk(psp_root):
        for filename in filenames:
            if filename.endswith('.png'):
                psp_paths.append(os.path.join(dirpath,filename))
    psp_paths.sort()
    
    for dirpath,dirnames,filenames in os.walk(pcan_root):
        for filename in filenames:
            if filename.endswith('.png'):
                pcan_paths.append(os.path.join(dirpath,filename))
    pcan_paths.sort()
    
    
    for psp_path,pcan_path in (zip(psp_paths,pcan_paths)):
        res_fol=os.path.join("/home/subha/mask_merge/kitti_step/",'result',pcan_path.split('/')[-2])
        if not os.path.isdir(res_fol):
            os.mkdir(res_fol)
        print(psp_path, pcan_path)
        maskmerge(psp_path,pcan_path,res_fol)