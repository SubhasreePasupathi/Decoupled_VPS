import json
from rle_mask  import annToRLE,annToMask

with open('city_vps_for_mots.json','r') as f:
	data=json.load(f)

ann=data['annotations'][0]

obj=annToRLE(ann)

print(obj)




