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
                

def tlwh_to_tlbr(x1,y1,w,h):
    #ret = np.asarray(tlwh).copy()
    #ret[2:] += ret[:2]
    x2=x1+w
    y2=y1+h
    return x1,y1,x2,y2


for file in l:
    sid=file.split('.')[0]
    with open(os.path.join(path,file),'r')as ff:
        data=json.load(ff)
    fid=0
    
    for keys,vals in data.items():#key 50025
        for els in vals:
            rle=annToRLE(els)['counts']
            
            x,y,w,h=els['bbox']
            x0,y0,x1,y1=tlwh_to_tlbr(x,y,w,h)
            write_line(sid,fid,els['track_id'],els['category_id'],'1',x0,y0,x1,y1)
            #for k,v in els.items():#k 0,1,2
            #    print(k,v)
            
                #write_line(sid,fid,k['track_id'],k['category_id'],str('1'),k['height'],k['width'])
        fid+=1
            #pprint(data[k])
        
        
    




       
     
    
       


