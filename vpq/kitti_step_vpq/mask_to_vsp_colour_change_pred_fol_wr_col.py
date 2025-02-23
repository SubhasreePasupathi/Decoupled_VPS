from __future__ import print_function
from PIL import Image
import os
import os.path as osp
import numpy as np
import json
from panopticapi.utils import rgb2id
from panopticapi.utils import IdGenerator
from pprint import pprint



import sys
#import torch
#import torch.multiprocessing as multiprocessing
import pickle
import time

#from tools.config import config
#from tools.base_dataset import BaseDataset


def colorize(gray, palette):
    # gray: numpy array of the label and 1*3N size list palette
    color = Image.fromarray(gray.astype(np.uint8)).convert('P')
    color.putpalette(palette)
    return color


#load sseg_pcan_masks

#/sseg_pcan_0002_pans_unified'
def for_fol(fol):
    pred_fol_type=os.path.join('pred/sseg_pcan/sseg_pcan_ks_bi_pan_map_fol/',fol)
    pred_fol='pan_2ch'
    path=os.path.join(pred_fol_type,pred_fol)
    print(path)
    im_path_list=os.listdir(path)
    im_path_list.sort()
    pred_pan_2ch=[]
    
    for i,image in enumerate(im_path_list):
    	im=Image.open(os.path.join(path,image))
    	im_arr=np.asarray(im)
    	pred_pan_2ch.append(im_arr)
    
    #load image names and categories from json 
    #with open('categories.json','r') as f:
    #        	data = json.load(f)
    #names = [x['file_name'] for x in im_jsons['images']]
    #names.sort()
    #categories = data['categories']
    categories=[{"id": 0, "name": "road", "supercategory": "flat", "isthing": 0, "instance_eval": 0, "trainid": 0, "ori_id": 7, "color": [128, 64, 128]}, {"id": 1, "name": "sidewalk", "supercategory": "flat", "isthing": 0, "instance_eval": 0, "trainid": 1, "ori_id": 8, "color": [244, 35, 232]}, {"id": 2, "name": "building", "supercategory": "construction", "isthing": 0, "instance_eval": 0, "trainid": 2, "ori_id": 11, "color": [70, 70, 70]}, {"id": 3, "name": "wall", "supercategory": "construction", "isthing": 0, "instance_eval": 0, "trainid": 3, "ori_id": 12, "color": [102, 102, 156]}, {"id": 4, "name": "fence", "supercategory": "construction", "isthing": 0, "instance_eval": 0, "trainid": 4, "ori_id": 13, "color": [190, 153, 153]}, {"id": 5, "name": "pole", "supercategory": "object", "isthing": 0, "instance_eval": 0, "trainid": 5, "ori_id": 17, "color": [153, 153, 153]}, {"id": 6, "name": "traffic light", "supercategory": "object", "isthing": 0, "instance_eval": 0, "trainid": 6, "ori_id": 19, "color": [250, 170, 30]}, {"id": 7, "name": "traffic sign", "supercategory": "object", "isthing": 0, "instance_eval": 0, "trainid": 7, "ori_id": 21, "color": [220, 220, 0]}, {"id": 8, "name": "vegitation", "supercategory": "nature", "isthing": 0, "instance_eval": 0, "trainid": 8, "ori_id": 21, "color": [107, 142, 35]}, {"id": 9, "name": "terrain", "supercategory": "nature", "isthing": 0, "instance_eval": 0, "trainid": 9, "ori_id": 22, "color": [152, 251, 152]}, {"id": 10, "name": "sky", "supercategory": "sky", "isthing": 0, "instance_eval": 0, "trainid": 10, "ori_id": 23, "color": [70, 130, 180]}, {"id": 11, "name": "person", "supercategory": "human", "isthing": 1, "instance_eval": 1, "trainid": 11, "ori_id": 24, "color": [220, 20, 60]}, {"id": 12, "name": "rider", "supercategory": "human", "isthing": 1, "instance_eval": 1, "trainid": 12, "ori_id": 25, "color": [255, 0, 0]}, {"id": 13, "name": "car", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 13, "ori_id": 26, "color": [0, 0, 142]}, {"id": 14, "name": "truck", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 14, "ori_id": 27, "color": [0, 0, 70]}, {"id": 15, "name": "bus", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 15, "ori_id": 28, "color": [0, 60, 100]}, {"id": 16, "name": "train", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 16, "ori_id": 31, "color": [0, 80, 100]}, {"id": 17, "name": "motorcycle", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 17, "ori_id": 32, "color": [0, 0, 230]}, {"id": 18, "name": "bicycle", "supercategory": "vehicle", "isthing": 1, "instance_eval": 1, "trainid": 18, "ori_id": 33, "color": [119, 11, 32]}]

    categories = {el['id']: el for el in categories}
    color_generator = IdGenerator(categories)
    
    names=[]
    for i,fname in enumerate(im_path_list):
    	names.append(fname)
    names.sort()
    
    #vid_num=50
    OFFSET = 1000
    VOID = 255
    annotations, pan_all = [], []
    # reference dict to used color
    inst2color = {}
    for idx in range(len(pred_pan_2ch)):
        pan_2ch = np.uint32(pred_pan_2ch[idx])
        pan = OFFSET * pan_2ch[:, :, 0] + pan_2ch[:, :, 2]
        pan_format = np.zeros((pan_2ch.shape[0], pan_2ch.shape[1], 3), dtype=np.uint8)
        l = np.unique(pan)
        # segm_info = []
        segm_info = {}
        for el in l:
            sem = el // OFFSET
            if sem == VOID:
                continue
            mask = pan == el
            #### handling used color for inst id
            if el % OFFSET > 0:
            # if el > OFFSET:
                # things class
                if el in inst2color:
                    color = inst2color[el]
                else:
                    color = color_generator.get_color(sem)
                    inst2color[el] = color
            else:
                # stuff class
                color = color_generator.get_color(sem)
    
            pan_format[mask] = color
            index = np.where(mask)
            x = index[1].min()
            y = index[0].min()
            width = index[1].max() - x
            height = index[0].max() - y
            #pred.json
            dt = {"category_id": sem.item(), "iscrowd": 0, "id": int(rgb2id(color)), "color":[int(x) for x in color],"bbox": [x.item(), y.item(), width.item(), height.item()], "area": mask.sum().item(),"fname":names[idx]}
            
            segment_id = int(rgb2id(color))
            segm_info[segment_id] = dt
        
        # annotations.append({"segments_info": segm_info})
        pan_all.append(pan_format)
        
        gt_pan = np.uint32(pan_format)
        pan_gt = gt_pan[:, :, 0] + gt_pan[:, :, 1] * 256 + gt_pan[:, :, 2] * 256 * 256      
        labels, labels_cnt = np.unique(pan_gt, return_counts=True)
        for label, area in zip(labels, labels_cnt):
            if label == 0:
                continue
            if label not in segm_info.keys():
                print('label:', label)
                raise KeyError('label not in segm_info keys.')
    
            segm_info[label]["area"] = int(area)
        segm_info = [v for k,v in segm_info.items()]
    
        annotations.append({"segments_info": segm_info})
    
    anno_dict={'annotations':annotations}
    colors=None
    print(len(annotations))
    with open(os.path.join(pred_fol_type,'pred.json'),'w') as ff:
    	json.dump(anno_dict,ff)
    
    save_path=os.path.join(pred_fol_type,'pan_pred')
    if not os.path.isdir(save_path):
       os.makedirs(save_path)
    for i, image in enumerate(pan_all):
        if colors is not None:
            image = colorize(image, colors)
        else:
            image = Image.fromarray(image)
            #os.makedirs(os.path.dirname(name), exist_ok=True)
            image.save(os.path.join(save_path,names[i]))
        
outer_path='/home/subha/Videos/Evaluate/kitti_step_vpq/pred/sseg_pcan/sseg_pcan_ks_bi_pan_map_fol'

l=os.listdir(outer_path)
l.sort()
for fol in l:
    print(fol)
    for_fol(fol)





