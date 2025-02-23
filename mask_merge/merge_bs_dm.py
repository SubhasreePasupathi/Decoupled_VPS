import os
import numpy as np
from PIL import Image
from pathlib import Path
from collections import defaultdict
from pprint import pprint
import json


bs_path='/home/subha/Videos/Paper1_results/modified/kitty_step/kitti_step_BoT_SORT_with_kitti_step_cls_ids/ks_bs_class'
dm_path='/home/subha/Videos/Paper1_results/directly_from_nws/deepmac/kitti_step_deepmac/policy_01_HIGHEST PIXEL CONFIDENCE'


write_path='/home/subha/Videos/bs_dm/'
Path(write_path).mkdir(parents=True,exist_ok=True)

bs_l=os.listdir(bs_path)
bs_l.sort()

dm_l=os.listdir(dm_path)
dm_l.sort()
#pprint(list(zip(bs_l,dm_l)))



class write_merged_image:
    
    def __init__(self,frame_list,fol):
        dmac_fol=os.path.join(dm_path,fol)
        write_fol=os.path.join(write_path,fol)
        Path(write_fol).mkdir(parents=True,exist_ok=True)
        dmac_ll=os.listdir(dmac_fol)
        dmac_ll.sort()
        #pprint(frame_list[232])
        for k,frame in enumerate(frame_list):   
            dmac_file_path=os.path.join(dmac_fol,dmac_ll[k])
            write_file_path=os.path.join(write_fol,dmac_ll[k])
            #print(dmac_file_path,write_file_path)
            obj=np.array(Image.open(dmac_file_path))
            ins=np.zeros_like(obj)
            sem=np.zeros_like(obj)
            #print(obj.shape,sem.shape)
            #print(np.unique(obj))
            for el in frame:
                for key,val in el.items():                    
                    for keys,vals in val.items():
                        print(keys)
                        mask=obj==int(vals['tid'])
                        sem[mask]=int(vals['cid'])
            pan_2ch=np.zeros((obj.shape[0],obj.shape[1],3))
            
            pan_2ch[:,:,0]=sem
            pan_2ch[:,:,2]=obj
            pan_im=Image.fromarray(pan_2ch.astype(np.uint8))
            pan_im.save(write_file_path)
                    
for i,file in enumerate(bs_l):
    with open (os.path.join(bs_path,file))as f:
         lines=f.readlines()
    head=lines[0]
    #lines=lines[1:]
    ll=os.listdir(os.path.join(dm_path,dm_l[i]))
    ll.sort()

    frame_list=[[] for i in range(0,len(ll))]
    #print(len(frame_list))
    for j,ss in enumerate(lines):
        line=ss.split(' ')
        #print(line)
        sid=file.split('.')[0]
       
        fid=int(line[0])
        tid=int(line[1])
        cls=int(float(line[2]))
        
        conf=line[7]
        x0=float(line[3])
        y0=float(line[4])
        x1=float(line[5])
        y1=float(line[6])
        
        
        line_dict={str(sid)+'_'+str(fid)+'_'+str(tid):{'sid':sid,'fid':fid,'tid':tid,'cid':cls,'conf':conf,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'fname':ll[fid] } }
        frame_list[fid].append({fid:line_dict})
    write_merged_image(frame_list,dm_l[i])
    print(i)
    
   
