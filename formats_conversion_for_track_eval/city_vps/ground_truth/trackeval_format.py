import os
import csv
import json
from pprint import pprint
from rle_mask import annToRLE
import snoop
from pycocotools import mask
path='cv_gt_seq_modified_from_vpsnet'
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
        self.path=os.path.join('chumma',sid+'.txt')
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
                


def kkkk():

    for file in l:
        sid=file.split('.')[0]
        with open(os.path.join(path,file),'r')as ff:
             data=json.load(ff)
        fid=0
        masks=[]
        for keys,vals in data.items():#key 50025
            for i,els in enumerate(vals):
                rle=annToRLE(els)['counts']
                rle1={'size': [1024, 2048], 'counts': rle}
                masks.append(rle1)
                llll=mask.merge(masks)
                #print("subha")
                print(i,llll)
                #write_line(sid,fid,els['track_id'],els['category_id'],'1',els['height'],els['width'],rle)
                if(i>1):
                   break
            break
        break
        
    
kkkk()



       
     
    
       


