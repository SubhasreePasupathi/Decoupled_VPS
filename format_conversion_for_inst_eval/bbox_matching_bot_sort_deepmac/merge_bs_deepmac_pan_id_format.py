import os
import pandas
import csv
from pprint import pprint
from PIL import Image,ImageDraw
import numpy as np
from rle_mask import binToRLE

bs_cv_path='cv_bs_class'
deep_path="deepmac_29nov22/policy_02_SMALLEST FIRST/deepmac_instance_tracking_masks"


l=os.listdir(deep_path)
l.sort()




class write_line_inst_eval:
   def __init__(self,fname,bm_path_abs,cid,conf):
       self.field_names=['bm_path','cid','conf']
       write_fol='botsort_deepmac_sf_trackeval_format'
       
       self.path=os.path.join(write_fol,fname.split('.')[0]+'.txt')
       if not os.path.isdir(write_fol):
           os.makedirs(write_fol)
       if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                self.writer.writerow({'bm_path':bm_path_abs,'cid':cid,'conf':conf})
       else:
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                self.writer.writerow({'bm_path':bm_path_abs,'cid':cid,'conf':conf})


sequence={}

seq='0005'
i=0
s={}
for file in l:
    sid=file.split('_')[0]
    
    #print(sid)
    if seq==sid:
       i=i+1
       fid=i
       #print(sid,fid,file,'if')
       s.update({fid:file})
       #pprint(s)
    else :
       sequence.update({seq:s})
       s={}
       seq=sid
       i=1
       fid=i
       #print(sid,fid,file,'else')
       s.update({fid:file})       
       #pprint(s)
sequence.update({seq:s})

deepmac_dict=sequence
#pprint(deepmac_dict)

path=bs_cv_path
ll=os.listdir(path)
ll.sort()
#check_fol='bb_mask_check'
save_fol='botsort_deepmac_sf_predictions'
if not os.path.isdir(save_fol):
   os.makedirs(save_fol)
for i,file in enumerate(ll):
    with open (os.path.join(path,file))as f:
         lines=f.readlines()
    #head=lines[0]
    #lines=lines[1:]
    
    for j,ss in enumerate(lines):
        line=ss.split(' ')
        #print(line)
        sid=file.split('.')[0]
        fid=int(float(line[0]))
        tid=int(float(line[1]))
        cls=int(float(line[2]))        
        conf=line[3]
        x1=float(line[4])
        y1=float(line[5])
        x2=float(line[6])
        y2=float(line[7])
        box=[x1,y1,x2,y2]
        #print(sid,fid,tid,cls,conf)
        fname=deepmac_dict[sid][fid]
        im=Image.open(os.path.join(deep_path,fname))
        arr=np.array(im).astype(np.uint8)
        bm=np.zeros_like(arr)  
        arr1=np.zeros_like(arr)    
        mask=arr==tid
        bm[mask]=1
        bm_im=Image.fromarray(bm.astype(np.uint8))
        bm_fol=os.path.join(save_fol,fname.split('.')[0])
        if not os.path.isdir(bm_fol):
           os.makedirs(bm_fol)
        bm_path=os.path.join(bm_fol,str(tid)+'.png')
        bm_im.save(bm_path)
        write_line_inst_eval(fname,bm_path,cls,conf)
        #write_line(sid,fid-1,tid,cls,conf,im.size[1],im.size[0],rle.decode('UTF-8'))

    print(i)    
