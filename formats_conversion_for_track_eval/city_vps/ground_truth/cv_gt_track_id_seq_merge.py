import os
import numpy as np
from PIL import Image
import json
from pprint import pprint

with open ('gt/panoptic_gt_val_city_vps.json','r')as f:
     ids_data=json.load(f)


with open('gt/instances_val_city_vps_rle.json','r') as ff:
     inst_data=json.load(ff)



#For Image id to frame name conversion
image_ids_annos = inst_data['images']

image_id_to_frame={}
w=image_ids_annos[0]['width']
h=image_ids_annos[0]['height']

for img in image_ids_annos:
    id=img['id']
    name='_'.join(img['file_name'].split('_')[:-1])
    image_id_to_frame.update({id:name})

image_frame_to_id={v: k for k, v in image_id_to_frame.items()}

frame_keys=[k for k, v in image_id_to_frame.items()]


#For Track_ids extraction
ids_annos=ids_data['annotations']
#print(len(ids_annos))
cnt=0
frames_pan={}
for i, id in enumerate(frame_keys):
    single_frame_annos=[]
    for frame_annos in ids_annos:
        if frame_annos['image_id']==image_id_to_frame[id]:
           for anno in frame_annos['segments_info']:               
               if anno['category_id']>10:
                  anno['image_id']=id
                  anno['frame_name']=frame_annos['image_id']
                  single_frame_annos.append(anno)
    cnt+=len(single_frame_annos)
    frames_pan.update({id:single_frame_annos})           
pprint(len(frames_pan))
print(cnt)

        
#Instances

inst_annos=inst_data['annotations']



keys = ['frame_id','track_id','class_id','dconfidence', 'h','w','mask']

full_list=[]
#extract instances of individual frames

cnt=0
frames_inst={}
for i,id in enumerate(frame_keys):
    single_frame_annos=[]
    for anno in inst_annos:  
        if anno['image_id']==id:
           frame_name=image_id_to_frame[anno['image_id']]
           anno['frame_name']= frame_name
           single_frame_annos.append(anno)
    cnt+=len(single_frame_annos)
    frames_inst.update({id:single_frame_annos})
pprint(len(frames_inst))
print(cnt)
'''
k=[]
for i, frame in enumerate(frames_inst):
    
    k.append(len(frames_inst[frame]))
print(k)     
v=[]
for i, frame in enumerate(frames_pan):
    v.append(len(frames_pan[frame]))
print(v)

for i in range(len(k)):
    print(k[i],v[i])
print(np.array(k).sum())
print(np.array(v).sum())
'''

#print(len(frames_inst.keys()))
#print(len(frames_pan.keys()))

#print(frames_pan.keys())

for i,key in enumerate(frames_pan.keys()):    
    #print(i,key,len(frames_pan[key]),len(frames_inst[key]))
    for j in range(len(frames_pan[key])):
        #pprint(frames_pan[key][j])
        #pprint(frames_inst[key][j])
        assert frames_pan[key][j]['area']==frames_inst[key][j]['area']
        frames_inst[key][j]['track_id']=frames_pan[key][j]['id']
        #pprint(frames_inst[key][j])
        


with open('city_vps_val_gt_with_things_track_id.json','w') as f:
     json.dump(frames_inst,f)

#video sequence

#print(np.unique(frames_inst.keys()))


chumma=  np.unique(   [   int(str(f"{key:08}")[:4])  for key in frames_inst.keys()   ]    )
vid_ids=[f"{el:04}" for el in chumma]
print(vid_ids)
print(chumma)
vid_ids=np.unique(   [   f"{int(str(key)[:3]):04}" for key in frames_inst.keys()   ]    )
#vid_ids.sort()

#print(len(vid_ids))
print(vid_ids)

vid_list=[]

print(vid_ids)

for i,vid in enumerate(vid_ids):
    single_vid_frames=[]
    for key in frames_inst.keys():
        if vid==f"{int(str(key)[:3]):04}":#int(str(key)[:3]): 
           print(key)
           single_vid_frames.append({key:frames_inst[key]})
           if vid=='0285':
              video_id=f"{285:04}"
              #video_id=285
           else:
              video_id=f"{int(frames_inst[key][0]['frame_name'].split('_')[0]):04}"#int(frames_inst[key][0]['frame_name'].split('_')[0])
           print(video_id)
    vid_list.append({video_id : single_vid_frames})


#pprint(vid_list)   
           
with open('city_vps_val_gt_Vid_seq_with_things_track_id.json','w') as f:
     json.dump(vid_list,f)  
    
    
   
    
    







    
