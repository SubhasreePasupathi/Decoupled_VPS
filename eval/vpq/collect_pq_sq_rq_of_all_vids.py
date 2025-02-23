import os
import shutil
from pathlib import Path
import numpy as np
import re

out_path='vpqs'
paths=os.listdir(out_path)
paths.sort()

write_path='vid_avgs'
'''
for path in paths:
    l=os.listdir(os.path.join(out_path,path))
    l.sort()
    for fol in l:
        ll=os.listdir(os.path.join(out_path,path,fol))
        ll.sort()       
        Path(os.path.join(write_path,path,'vpq_finals')).mkdir(parents=True,exist_ok=True)
        shutil.copy(os.path.join(out_path,path,fol,ll[-1]),os.path.join(write_path,path,'vpq_finals',fol+'_'+ll[-1]))
'''
for path in paths:
    l=os.listdir(os.path.join(out_path,path))
    l.sort()
    for fol in l:
        ll=os.listdir(os.path.join(out_path,path,fol))
        ll.sort()       
        Path(os.path.join(write_path,path,'vpq_pq_sq_rq_all')).mkdir(parents=True,exist_ok=True)
        #Path(os.path.join(write_path,path,'vpq_pq_sq_rq_th')).mkdir(parents=True,exist_ok=True)
        #Path(os.path.join(write_path,path,'vpq_pq_sq_rq_st')).mkdir(parents=True,exist_ok=True)
        pqs,sqs,rqs=[],[],[]
        for file in ll:
            if file!='vpq-final.txt':
               read_file=os.path.join(out_path,path,fol,file)
               with open (read_file,'r') as f:
                    for line in f:
                        if line.startswith('A'):
                        #if line.startswith('T'):
                        #if line.startswith('S'):
                           vals=[]
                           #sline=line.split('|')
                           sline=line.split('  ')
                           
                           for el in sline:
                               if re.search("[0-9]",el):
                                  vals.append(el)
 
                               
                           vals=vals[:-1]
                           pq,sq,rq=vals
                           print(line)
                           print(sline)
                           print(vals)
                           print(pq,sq,rq)
                           pqs.append(float(pq))
                           sqs.append(float(sq))
                           rqs.append(float(rq))
                           
        pqs=np.array(pqs)
        sqs=np.array(sqs)
        rqs=np.array(rqs)
        for file in ll:
            if file=='vpq-final.txt':
               read_file=os.path.join(out_path,path,fol,file)
               with open (read_file,'r') as f:
                    for line in f:
                        if line.startswith(''):
        with open(os.path.join(write_path,path,'vpq_all_vals',fol+'.txt'),'w')as ff:
        ##with open(os.path.join(write_path,path,'vpq_pq_sq_rq_all',fol+'_pq_sq_rq_all_avg.txt'),'w')as ff:
        #with open(os.path.join(write_path,path,'vpq_pq_sq_rq_th',fol+'_pq_sq_rq_th_avg.txt'),'w')as ff:
        #with open(os.path.join(write_path,path,'vpq_pq_sq_rq_st',fol+'_pq_sq_rq_st_avg.txt'),'w')as ff:
             ff.write('pq:'+ str(np.average(pqs)))
             ff.write('\n')
             ff.write('s :'+ str(np.average(sqs)))
             ff.write('\n')
             ff.write('rq:'+ str(np.average(rqs)))
        
        
