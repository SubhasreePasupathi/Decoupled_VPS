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

from pathlib import Path

#bdd_to_city={0: 0, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}


path='bs_dm_w'
l=os.listdir(path)
l.sort()


#Timestep>(int), <Track ID>(int), <Class Number>(int), <Detection Confidence>(float), <Image Height>(int), <Image Width>(int), <Compressed RLE Mask>(string),



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
        write_fol='track_eval_format_full_panid'
        Path(write_fol).mkdir(parents=True,exist_ok=True)
        self.path=os.path.join(write_fol,sid+'.txt')
        
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
                

for i,fol in enumerate(l):
    sid=fol.split('_')[0]
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
            mask=pan_mask==id
            pan_inst[mask]=id
            

        ins_ids=np.unique(pan_inst)
        ins_ids=ins_ids[ins_ids>0]
        #print(ins_ids)
        for ins_id in ins_ids:
            obj_id=ins_id%1000
            class_id=ins_id//1000
            mask=pan_inst==ins_id
            bm=np.zeros_like(pan_inst)
            bm[mask]=1
            rle=binToRLE(bm)['counts']	
            write_line(sid,j,ins_id,class_id,str('0.7'),img.size[1],img.size[0],rle.decode('UTF-8'))
            
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




       
     
    
       


