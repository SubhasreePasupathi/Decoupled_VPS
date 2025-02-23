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
                



for file in l:
    sid=file.split('.')[0]
    with open(os.path.join(path,file),'r')as ff:
        data=json.load(ff)
    fid=0
    
    for keys,vals in data.items():#key 50025
        for els in vals:
            rle=annToRLE(els)['counts']
            
            
            write_line(sid,fid,els['track_id'],els['category_id'],'1',els['height'],els['width'],rle.decode('UTF-8'))
            #for k,v in els.items():#k 0,1,2
            #    print(k,v)
            
                #write_line(sid,fid,k['track_id'],k['category_id'],str('1'),k['height'],k['width'])
        fid+=1
            #pprint(data[k])
        
        
    




       
     
    
       


