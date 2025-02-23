import os
import shutil
from pathlib import Path
import numpy as np
import re
import csv

out_path='vpq_avg_calc/vpqs'
paths=os.listdir(out_path)
paths.sort()

write_path='frame_avgs'
Path(write_path).mkdir(parents=True,exist_ok=True)


for path in paths:
    l=os.listdir(os.path.join(out_path,path))
    l.sort()
    
    for fol in l:
        ll=os.listdir(os.path.join(out_path,path,fol))
        ll.sort()       
        pqs_all,sqs_all,rqs_all=[],[],[]
        pqs_th,sqs_th,rqs_th=[],[],[]
        pqs_st,sqs_st,rqs_st=[],[],[]
        vpqs_all,vpqs_th,vpqs_st=[],[],[]
        for file in ll:
            if file!='vpq-final.txt':
               read_file=os.path.join(out_path,path,fol,file)
               with open (read_file,'r') as f:
                    for line in f:
                        if line.startswith('A'):
                        #if line.startswith('T'):
                        #if line.startswith('S'):
                           vals=[]                          
                           sline=line.split('  ')
                           
                           for el in sline:
                               if re.search("[0-9]",el):
                                  vals.append(el)
                               
                           vals=vals[:-1]
                           pq,sq,rq=vals                          
                           pqs_all.append(np.double(pq))
                           sqs_all.append(np.double(sq))
                           rqs_all.append(np.double(rq))
                        if line.startswith('T'):
                        #if line.startswith('S'):
                           vals=[]                          
                           sline=line.split('  ')
                           
                           for el in sline:
                               if re.search("[0-9]",el):
                                  vals.append(el)
                               
                           vals=vals[:-1]
                           pq,sq,rq=vals                          
                           pqs_th.append(np.double(pq))
                           sqs_th.append(np.double(sq))
                           rqs_th.append(np.double(rq))
                        if line.startswith('S'):
                           vals=[]                          
                           sline=line.split('  ')
                           
                           for el in sline:
                               if re.search("[0-9]",el):
                                  vals.append(el)
                               
                           vals=vals[:-1]
                           pq,sq,rq=vals                          
                           pqs_st.append(np.double(pq))
                           sqs_st.append(np.double(sq))
                           rqs_st.append(np.double(rq))

        pqs_all=np.array(pqs_all)
        sqs_all=np.array(sqs_all)
        rqs_all=np.array(rqs_all)

        pqs_th=np.array(pqs_th)
        sqs_th=np.array(sqs_th)
        rqs_th=np.array(rqs_th)

        pqs_st=np.array(pqs_st)
        sqs_st=np.array(sqs_st)
        rqs_st=np.array(rqs_st)
     

        fol_pqs_all_avg=sum(pqs_all)/len(pqs_all)
        fol_pqs_th_avg=sum(pqs_th)/len(pqs_th)
        fol_pqs_st_avg=sum(pqs_st)/len(pqs_st)

        fol_sqs_all_avg=sum(sqs_all)/len(sqs_all)
        fol_sqs_th_avg=sum(sqs_th)/len(sqs_th)
        fol_sqs_st_avg=sum(sqs_st)/len(sqs_st)
 
        fol_rqs_all_avg=sum(rqs_all)/len(rqs_all)
        fol_rqs_th_avg=sum(rqs_th)/len(rqs_th)
        fol_rqs_st_avg=sum(rqs_st)/len(rqs_st)
        for file in ll:
            if file=='vpq-final.txt':
               read_file=os.path.join(out_path,path,fol,file)
               with open (read_file,'r') as f:
                    for line in f:
                        print(line)
                        if line.startswith('vpq_all'):
                           vpq_all=float(line.split(':')[1].strip('\n'))  
                           print(vpq_all)
                        if line.startswith('vpq_thing'):
                           vpq_th=float(line.split(':')[1].strip('\n'))
                           print(vpq_th)
                        if line.startswith('vpq_stuff'):
                           vpq_st=float(line.split(':')[1].strip('\n'))
                           print(vpq_st)
                    vpqs_all.append(vpq_all)
                    vpqs_th.append(vpq_th)
                    vpqs_st.append(vpq_st)
        vpqs_all=np.array(vpqs_all)
        vpqs_th=np.array(vpqs_th)
        vpqs_st=np.array(vpqs_st)
        if len(vpqs_all)!=0:
           fol_vpqs_all_avg=sum(vpqs_all)/len(vpqs_all)
           fol_vpqs_th_avg=sum(vpqs_th)/len(vpqs_th)
           fol_vpqs_st_avg=sum(vpqs_st)/len(vpqs_st)
        
        with open(os.path.join(out_path,path,fol,'pq_sq_rq_avg.csv'),'w')as ff:
             fieldnames = ['cls','vpq','pq','sq','rq']
             writer = csv.DictWriter(ff, fieldnames=fieldnames)
             writer.writeheader()
             if len(vpqs_all)!=0:
                writer.writerow({'cls':'all','vpq':fol_vpqs_all_avg,'pq':fol_pqs_all_avg,'sq':fol_sqs_all_avg,'rq':fol_rqs_all_avg})
                writer.writerow({'cls':'things','vpq':fol_vpqs_th_avg,'pq':fol_pqs_th_avg,'sq':fol_sqs_th_avg,'rq':fol_rqs_th_avg})
                writer.writerow({'cls':'stuff','vpq':fol_vpqs_st_avg,'pq':fol_pqs_st_avg,'sq':fol_sqs_st_avg,'rq':fol_rqs_st_avg})
             
