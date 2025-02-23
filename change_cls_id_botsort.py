import os
import pandas
import csv

bs_cv_path='/home/subha/Videos/Paper1_results_nov4/directly_from_nws/BoT_SORT/city_vps_val_img_BoT_SORT_labels'
bs_ks_path='/home/subha/Videos/Paper1_results_nov4/directly_from_nws/BoT_SORT/kitti_step_Bot_SORT_labels'
write_path='/home/subha/Videos/ks_bs_class'
cv_l=os.listdir(bs_cv_path)
cv_l.sort()

ks_l=os.listdir(bs_ks_path)
ks_l.sort()

coco_botsort_to_city={0:11, 1:18, 2:13, 3:17, 4:0, 5:15, 6:16, 7:14}
cls=[]


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
        self.path=os.path.join(write_path,sid+'.txt')
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'x0':x0,'y0':y0,'x1':x1,'y1':y1})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'x0':x0,'y0':y0,'x1':x1,'y1':y1})



for i,file in enumerate(ks_l):
    with open (os.path.join(bs_ks_path,file))as f:
         lines=f.readlines()
    head=lines[0]
    lines=lines[1:]
    
    for ss in lines:
        line=ss.split(',')
        print(line)
        sid=file.split('.')[0]
        fid=line[0]
        tid=line[1]
        cls=int(float(line[2]))
        
        conf=line[7]
        x=float(line[3])
        y=float(line[4])
        w=float(line[5])
        h=float(line[6])
        x0,y0,x1,y1=tlwh_to_tlbr(x,y,w,h)
        #print(x,y,w,h)
        #print(x0,y0,x1,y1)
        #print(sid,fid,tid,city_cls,conf,x0,y0,x1,y1)
        print(sid)
        if cls!=8:
           city_cls=coco_botsort_to_city[cls]
           write_line(sid,fid,tid,city_cls,conf,x0,y0,x1,y1)
        
   
    
