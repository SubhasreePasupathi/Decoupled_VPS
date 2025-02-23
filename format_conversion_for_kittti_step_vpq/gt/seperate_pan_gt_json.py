import os
import json
from pprint import pprint

path='/home/subha/Videos/datasets/city_vps_val_after_running_scripts/panoptic_gt_val_city_vps.json'

with open (path,'r')as f:
     data=json.load(f)
print(len(data['annotations']))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


anno_split=list(split(data['annotations'], 50))
images_split=list(split(data['images'], 50))
categories=data['categories']
#pprint(data_split)

fol_path='/home/subha/Videos/Evaluate/format_conversion_for_kittti_step_vpq/gt/city_vps_gt_folder'         
write_path='/home/subha/Videos/Evaluate/format_conversion_for_kittti_step_vpq/gt/gt_annotations_jsons'
l=os.listdir(fol_path)
l.sort()
for i,sp in enumerate(images_split):
    dictionary={'images':images_split[i],'annotations':anno_split[i],'categories':categories}
    with open(os.path.join(write_path,'pan_gt_cv_annotations_'+l[i]+'.json'),'w')as ff:
         json.dump(dictionary,ff)




