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

from tools.config import config
from tools.base_dataset import BaseDataset


def colorize(gray, palette):
    # gray: numpy array of the label and 1*3N size list palette
    color = Image.fromarray(gray.astype(np.uint8)).convert('P')
    color.putpalette(palette)
    return color


#load psp_pcan_masks
im_path_list=os.listdir('psp_pcan_masks')
im_path_list.sort()
pred_pan_2ch=[]

for i,image in enumerate(im_path_list):
	im=Image.open(os.path.join('psp_pcan_masks',image))
	im_arr=np.asarray(im)
	pred_pan_2ch.append(im_arr)

#load image names and categories from json 
with open('panoptic_im_val_city_vps.json','r') as f:
        	im_jsons = json.load(f)
#names = [x['file_name'] for x in im_jsons['images']]
#names.sort()
categories = im_jsons['categories']
categories = {el['id']: el for el in categories}
color_generator = IdGenerator(categories)

names=[]
for i,fname in enumerate(im_path_list):
	names.append(fname)
names.sort()

vid_num=50
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

        dt = {"category_id": sem.item(), "iscrowd": 0, "id": int(rgb2id(color)), "bbox": [x.item(), y.item(), width.item(), height.item()], "area": mask.sum().item()}
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
with open('psp_pcan_annotaions.json','w') as ff:
	json.dump(anno_dict,ff)

save_path='psp_pcan_colour'
for i, image in enumerate(pan_all):
    if colors is not None:
        image = colorize(image, colors)
    else:
        image = Image.fromarray(image)
        #os.makedirs(os.path.dirname(name), exist_ok=True)
        image.save(os.path.join(save_path,names[i]))
    







