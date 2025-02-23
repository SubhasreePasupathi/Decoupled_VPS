import os
import numpy as np
from PIL import Image
from pprint import pprint
import random
from pathlib import Path


#pprint(city_classes)
path='datasets/waymo'

ins_files=[]
sem_files=[]
pan_files=[]

for (root,dirnames,filenames) in os.walk(path):
    for file in filenames:
        if 'ins' in (os.path.join(root,file)).split('/'):
            ins_files.append(os.path.join(root,file))
        if 'pan' in (os.path.join(root,file)).split('/'):
            pan_files.append(os.path.join(root,file))
        if 'sem' in (os.path.join(root,file)).split('/'):
            sem_files.append(os.path.join(root,file))

#print(len(pan_files))

sel_ins=random.choices(ins_files,k=10)	
sel_sem=random.choices(sem_files,k=10)	
sel_pan=random.choices(pan_files,k=10)	
#pprint(sel_ins)
#pprint(sel_pan)
#pprint(sel_sem)
#th_ids=[id for id in waymo_things.keys()]
th_ids=[1, 2, 3, 4, 7, 8, 9, 10]
#st_ids=[id for id in waymo_stuff.keys()]
st_ids=[0, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 255]

waymo_extra_ids=[0,4,7,9,10,11,12,13,15,16,20,21,25,26,27]
#print(th_ids,st_ids)
for file in pan_files:
    arr=np.array(Image.open(file)).astype(np.uint16)
    ids=np.unique(arr)
    data_fol_name=file.split('/')[-4]
    #exit()
    for i,id in enumerate(ids):
        sem_id=id//1000
        ins_id=id%1000
        #k=[11,110]
        if sem_id-1 in waymo_extra_ids:
           
           mask=arr==id
           bm=np.zeros_like(arr,np.uint8)
           bm[mask]=255
           bm_im=Image.fromarray(bm)
           
           rgb_im=Image.open(file.replace('pan','rgb'))
           write_path=os.path.join('check',str(sem_id))
           Path(write_path).mkdir(parents=True,exist_ok=True)
           fn=file.split('/')[-1].replace('pan','rgb')
           rgb_im.save(os.path.join(write_path,data_fol_name+'_'+fn))
           #print(os.path.join(write_path,fn))
           
           fnn=file.split('/')[-1].split('.')[0]+'_'+str(id)+'.png'
           bm_im.save(os.path.join(write_path,data_fol_name+'_'+fnn))
           print(id , os.path.join(write_path,data_fol_name+'_'+fnn))
           #rgb_im.show()
           #bm_im.show()
       


