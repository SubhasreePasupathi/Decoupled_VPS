import os
from pprint import pprint
path='data'
out_path='data1'
l=os.listdir(path)
l.sort()
import pandas as pd
import csv


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
        self.path=os.path.join('data1',sid+'.txt')
        if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                #self.writer.writeheader()
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
        else:            
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')                
                self.writer.writerow({'fid':fid,'tid':tid,'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
                






for j,file in enumerate(l):
    i=0
    dictionary={}
    with open(os.path.join(path,file),'r') as f:
         lines=[line.strip() for line in f]
         print(len(lines))
    for k,line in enumerate(lines):       
        line_data=line.split(' ')        
        fid,tid,cid,conf,h,w,mask=line_data  
        sid=file.split('.')[0]      
        if tid in dictionary.keys():
           print(tid,dictionary[tid])
        else:
           i=i+1
           dictionary.update({tid:i})
        print(j)
        write_line( sid,fid,dictionary[tid],cid,conf,h,w,mask)  
   

pprint(dictionary)
'''
frame_list=[]

for file in l:    
    with open(os.path.join(path,file),'r') as f:
         lines=[line.strip() for line in f]
         print(len(lines))
    for line in lines:       
        line_data=line.split(' ')        
        fid,tid,cid,conf,h,w,mask=line_data        
        frame_list.append({'fid':fid,'tid':dictionary[tid],'cid':cid,'conf':conf,'h':h,'w':w,'mask':mask})
        sid=file.split('.')[0]
        write_line( sid,fid,tid,cid,conf,h,w,mask)  

'''


