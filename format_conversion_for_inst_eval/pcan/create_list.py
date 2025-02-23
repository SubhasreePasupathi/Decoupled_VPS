import os

l=os.listdir('city_gt_inst_map_uint16')
l.sort()
ll=[]
for els in l:
    els=os.path.abspath(els)
    ll.append(els)

with open('gt_list.txt','w') as f:
     f.write('\n'.join(ll))

