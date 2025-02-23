import os
import numpy as np
from PIL import Image
import shutil
from pathlib import Path


path='datasets/waymo'
write_path='datasets/waymo_modified'


waymo_to_city={0:255,1: 255, 2: 13, 3: 14, 4: 15, 5: 14, 6: 255, 7: 255, 8: 14, 9: 11, 10: 255, 11: 255, 12: 255, 13: 1, 14: 5, 15: 5, 16: 11, 17: 7, 18: 6, 19: 2, 20: 0, 21: 0, 22: 0, 23: 1, 24: 8, 25: 10, 26: 9, 27: 255, 28: 255, 255: 255}

print(waymo_to_city)

l=os.listdir(path)
l.sort()

for fol in l:
    fol_path=os.path.join(path,fol,'FRONT','pan')
    pan_write_fol_path=os.path.join(write_path,fol,'pan')
    pan_2ch_write_fol_path=os.path.join(write_path,fol,'pan_2ch')
    Path(pan_write_fol_path).mkdir(parents=True,exist_ok=True)
    Path(pan_2ch_write_fol_path).mkdir(parents=True,exist_ok=True)

    ll=os.listdir(fol_path)
    ll.sort()
    for file in ll:
        img=Image.open(os.path.join(fol_path,file))
        arr=np.array(img).astype(np.uint16)
        ids=np.unique(arr)

        pan_id_arr=np.zeros_like(arr).astype(np.uint16)
        pan_2ch_arr=np.zeros((arr.shape[0],arr.shape[1],3),np.uint8)

        for id in ids:
            sem_id=id//1000
            obj_id=id%1000

            mask=arr==id

            pan_id_arr[mask]=waymo_to_city[sem_id]*1000+obj_id
            pan_2ch_arr[:,:,0][mask]=waymo_to_city[sem_id]
            pan_2ch_arr[:,:,2][mask]=obj_id

        pan_im=Image.fromarray(pan_id_arr)
        pan_2ch_im=Image.fromarray(pan_2ch_arr)
        pan_im.save(os.path.join(pan_write_fol_path,file))
        pan_2ch_im.save(os.path.join(pan_2ch_write_fol_path,file))
        print(fol,file)
        
