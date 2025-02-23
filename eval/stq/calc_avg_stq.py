import os
import json
from pathlib import Path
import numpy as np
path='stq'
l=os.listdir(path)
l.sort()
#l=l[1:]

#print(l)


for fol in l:
    ll=os.listdir(os.path.join(path,fol))
    ll.sort()
    stq_vid,aq_vid,iou_vid=[],[],[]
    for file in ll:
        with open(os.path.join(path,fol,file),'r')as f:
             data=json.load(f)
             
             for el in data:
                 stq_vid.append(el['STQ'])
                 aq_vid.append(el['AQ'])
                 iou_vid.append(el['IoU'])
    stq_fol=np.average(np.array(stq_vid))
    aq_fol=np.average(np.array(aq_vid))
    iou_fol=np.average(np.array(iou_vid))
    write_file=os.path.join('avgs','_'.join(ll[0].split('_')[:-1])+'.txt')
    with open (write_file,'w') as ff:
         ff.write("stq : "+str(stq_fol))
         ff.write("\n")
         ff.write("aq : "+str(aq_fol))
         ff.write("\n")
         ff.write("iou : "+str(iou_fol))
         ff.write("\n")
