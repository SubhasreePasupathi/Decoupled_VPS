from mot_vpsnet import eval_mot
from mots_vpsnet import eval_mots 
import pycocotools.mask as mask_util
import pickle
import mmcv
import json
import numpy as np


def evaluate(    results,
                 metric=['bbox', 'segm', 'segtrack'],
                 logger=None,
                 classwise=True,
                 mot_class_average=True,
                 proposal_nums=(100, 300, 1000),
                 iou_thr=None,
                 metric_items=None):
    ann_file='city_vps_gt_for_mots.json'
    mot_class_average=True
    eval_results = dict()
    metrics = metric if isinstance(metric, list) else [metric]
    allowed_metrics = ['bbox', 'segm', 'track', 'segtrack']
    for metric in metrics:
        if metric not in allowed_metrics:
            raise KeyError(f'metric {metric} is not supported')
    if 'segtrack' in metrics:
        track_eval_results = eval_mots(mmcv.load(ann_file), results['track_result'], class_average=mot_class_average)
        eval_results.update(track_eval_results)
    elif 'track' in metrics:
        track_eval_results = eval_mot(mmcv.load(ann_file),results['track_result'], class_average=mot_class_average)
        eval_results.update(track_eval_results)
    return eval_results

with open('vpsnet_pickle_rle_1.pkl','rb') as f:
	outputs=pickle.load(f)
'''
res=[]
for i,ele in enumerate(outputs['track_result']):
	corrected_dict = { k-1: v for k, v in ele.items() }
	res.append(corrected_dict)
	#print(corrected_dict)
	print(i)
	
	for key,value in ele.items():
		print(key)
		print(ele[key])
		s=key-1
		ele[s]=ele[key]
		print('finish')
		
		
	print('img finish')
	

track_dict={'track_result':res}
with open('vpsnet_pickle_rle_1.pkl','wb') as ff:
	pickle.dump(track_dict,ff)

'''
#MOTS
eval_results=evaluate(outputs,metric=['bbox', 'segm', 'segtrack'])

#MOT
#eval_results=evaluate(outputs,metric=['bbox', 'segm', 'track'])


with open('mots_vspnet.txt','a') as ff:
	ff.write(str(eval_results))

