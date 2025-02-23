from mot import eval_mot
from mots import eval_mots 
import pickle
import mmcv
import json



def evaluate(    results,
                 metric=['bbox', 'segm', 'segtrack'],
                 logger=None,
                 classwise=True,
                 mot_class_average=True,
                 proposal_nums=(100, 300, 1000),
                 iou_thr=None,
                 metric_items=None):
        # evaluate for detectors without tracker
        #mot_class_average=False
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


with open('city_vps_from_pcan.pkl','rb') as f:
	outputs=pickle.load(f)




#only for pcan. Not for vpsnet
for lisele in outputs['track_result']:
	for key,value in lisele.items():
		#print(value['label'])
		value['label']+=10
		#print(value['label'])

		
#MOTS
eval_results=evaluate(outputs,metric=['bbox', 'segm', 'segtrack'])

#MOT
#eval_results=evaluate(outputs,metric=['bbox', 'segm', 'track'])


print(eval_results)
with open('mots_psp_pcan.txt','a') as ff:
	ff.write(str(eval_results))


