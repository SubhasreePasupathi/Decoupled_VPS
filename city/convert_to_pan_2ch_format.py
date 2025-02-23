import os
from pathlib import Path
import shutil
from PIL import Image
import numpy as np



pan_i_path='./pan_inst'
lbl_path='./lbl_map'

write_path='./pan_2ch'

l=os.listdir(pan_i_path)
l.sort()
for i,fol in enumerate(l):
    ll=os.listdir(os.path.join(lbl_path,fol))
    ll.sort()
    Path(os.path.join(write_path,fol)).mkdir(parents=True,exist_ok=True)
    for file in ll:
        arr=np.array(Image.open(os.path.join(pan_i_path,fol,file))).astype(np.uint16)
        ids=np.unique(arr)
        sem_ids=ids[ids<10000]
        #print(sem_ids)
        sem_im=np.zeros_like(arr).astype(np.uint8)
        ins_im=np.zeros_like(arr).astype(np.uint8)
        blank=np.zeros_like(arr).astype(np.uint8)
        for id in sem_ids:
            mask=arr==id            
            sem_im[mask]=id

        ins_ids=ids[ids>10500]
        #print(ins_ids)
        for id in ins_ids:
            mask=arr==id
            sem_id=id//1000
            ins_id=id%1000
            ins_im[mask]=ins_id
            sem_im[mask]=sem_id	
        pan_im=np.dstack((sem_im,blank,ins_im))
        img=Image.fromarray(pan_im)
        
        img.save(os.path.join(write_path,fol,file))
    print(fol)
    



'''	
print("***************")
l=os.listdir(lbl_path)
l.sort()
for fol in l:
    ll=os.listdir(os.path.join(lbl_path,fol))
    ll.sort()
    for file in ll:
        arr=np.array(Image.open(os.path.join(lbl_path,fol,file))).astype(np.uint16)
        ids=np.unique(arr)
        print(ids)
    exit()
'''
