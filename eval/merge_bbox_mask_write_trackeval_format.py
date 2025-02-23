import os
import pandas
import csv
from pprint import pprint
from PIL import Image,ImageDraw
import numpy as np
from rle_mask import binToRLE

bs_cv_path='cv_bs_class'
deep_path="/root/deepmac_instance_tracking_masks"


l=os.listdir(deep_path)
l.sort()



class write_line:
    
    def __init__(self,sid,fid,tid,cid,conf,h,w,mask):
        self.sid=sid
        self.fid=fid
        self.tid=tid
        self.cid=cid
        self.conf=conf
        self.h=h
        self.w=w
        #self.mask=mask
        self.field_names=['fid','tid','cid','conf','h','w','mask']
        write_fol='chumma'
        self.path=os.path.join(write_fol,sid+'.txt')
        if not os.path.isdir(write_fol):
           os.makedirs(write_fol)
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
                


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
check_fol='bb_mask_check'
if not os.path.isdir(check_fol):
   os.makedirs(check_fol)
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
        #check bb_mask_correctness  
        #arr1[mask]=tid
        #im1=Image.fromarray(arr1.astype(np.uint8))
        #img1 = ImageDraw.Draw(im1)  
        #img1.rectangle(box, outline ="red")
        #im1.save(os.path.join(check_fol,str(i)+'_'+str(j)+'.png'))
        rle=binToRLE(bm)['counts']	
        #write_line(sid,j,obj_id,class_id,str('0.7'),img.size[1],img.size[0],rle.decode('UTF-8'))
        write_line(sid,fid-1,tid,cls,conf,im.size[1],im.size[0],rle.decode('UTF-8'))

    print(i)    
