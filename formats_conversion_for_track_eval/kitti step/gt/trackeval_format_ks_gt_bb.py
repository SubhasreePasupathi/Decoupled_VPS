import os
import csv
import json
from pprint import pprint
from rle_mask import annToRLE,annToMask
from PIL import Image
import numpy as np
import imageio
from rle_mask import binToRLE

from pycocotools import mask as  maskUtils
import os
from collections import defaultdict
import sys
PYTHON_VERSION = sys.version_info[0]
if PYTHON_VERSION == 2:
    from urllib import urlretrieve
elif PYTHON_VERSION == 3:
    from urllib.request import urlretrieve






path='val'
l=os.listdir(path)
l.sort()


def tlwh_to_tlbr(x1,y1,w,h):
    #ret = np.asarray(tlwh).copy()
    #ret[2:] += ret[:2]
    x2=x1+w
    y2=y1+h
    return x1,y1,x2,y2

#Timestep>(int), <Track ID>(int), <Class Number>(int), <Detection Confidence>(float), <Image Height>(int), <Image Width>(int), <Compressed RLE Mask>(string),



class write_line:
    
    def __init__(self,sid,fid,tid,cid,conf,x0,y0,x1,y1):
        self.sid=sid
        self.fid=fid
        self.tid=tid
        self.cid=cid
        self.conf=conf
        self.h=h
        self.w=w
        #self.mask=mask
        self.field_names=['fid','tid','cid','conf','x0','y0','x1','y1']
        self.path=os.path.join('chumma_bb',sid+'.txt')
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'x0':x0,'y0':y0,'x1':x1,'y1':y1})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'x0':x0,'y0':y0,'x1':x1,'y1':y1})
                

for i,fol in enumerate(l):
    sid=fol
    print(i)
    ll=os.listdir(os.path.join(path,fol))
    ll.sort()
    for j,img_name in enumerate(ll):
        img=Image.open(os.path.join(path,fol,img_name))
        arr=np.array(img)
        pan_mask=(arr[:,:,0]*1000+arr[:,:,2]).astype('uint16')
        pan_inst=np.zeros_like(pan_mask)
        ids=np.unique(pan_mask)
        for id in ids:
            if(id>10500 and id<20000):
               mask=pan_mask==id
               pan_inst[mask]=id
            

        ins_ids=np.unique(pan_inst)
        ins_ids=ins_ids[ins_ids>0]
        #print(ins_ids)
        for ins_id in ins_ids:
            obj_id=ins_id%1000
            class_id=ins_id//1000
            mask=pan_inst==ins_id
            index = np.where(mask)
            x = index[1].min()
            y = index[0].min()
            width = index[1].max() - x
            height = index[0].max() - y
            x,y,w,h=x.item(), y.item(), width.item(), height.item()
            x0,y0,x1,y1=tlwh_to_tlbr(x,y,w,h)
            
            write_line(sid,j,ins_id,class_id,str('1'),x0,y0,x1,y1)
            
            #print(sid,j	,obj_id,class_id,'1',img.size[1],img.size[0])
         
        #imageio.imwrite(os.path.join('out',img_name),pan_inst)
        
        
        
       
'''

for file in l:
    sid=file.split('.')[0]
    with open(os.path.join('seq',file),'r')as ff:
        data=json.load(ff)
    fid=0
    for keys,vals in data.items():#key 50025
        for els in vals:
            rle=annToRLE(els)['counts']
            write_line(sid,fid,els['track_id'],els['category_id'],'1',els['height'],els['width'],rle)
            #for k,v in els.items():#k 0,1,2
            #    print(k,v)
            
                #write_line(sid,fid,k['track_id'],k['category_id'],str('1'),k['height'],k['width'])
        fid+=1
            #pprint(data[k])
        
'''   




       
     
    
       


