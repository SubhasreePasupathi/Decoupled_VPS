import os
import json
from pprint import pprint

path='/home/subha/Videos/Paper1_results/directly_from_nws/vpsnet/cityscape_vps_vpsnet_inference/val_pans_unified/pred.json'

with open (path,'r')as f:
     data=json.load(f)
print(len(data['annotations']))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


data_split=list(split(data['annotations'], 50))
pprint(data_split)

fol_path='/home/subha/Videos/Evaluate/format_conversion_for_kittti_step_vpq/preds/city_vps_vpsnet_folder'
l=os.listdir(fol_path)
l.sort()
for i,sp in enumerate(data_split):
    with open(os.path.join(fol_path,l[i],'pred.json'),'w')as ff:
         json.dump({'annotations':sp},ff)
