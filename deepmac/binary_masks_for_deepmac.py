import os
from PIL import Image
import numpy as np

path='deepmac'
mask_fol_path='deepmac_mask'

l=os.listdir(path)
l.sort()

for i,img in enumerate(l):
    fol_path=os.path.join(mask_fol_path,img.split('.')[0])
    #if not os.path.isdir(fol_path):
    #   os.makedirs(fol_path)
    image=Image.open(os.path.join(path,img))
    arr=np.array(image)
    inst_ids=np.unique(arr)
    inst_ids=inst_ids[inst_ids>0]
    print(fol_path , len(inst_ids))
    
    for id in inst_ids:
        arr1=np.zeros_like(arr)
        mask=arr==id
        arr1[mask]=1
        img1=Image.fromarray(arr1.astype('uint8'))
        mask_name=os.path.join(fol_path,os.path.basename(fol_path)+'_'+str(id)+'.png')
        img1.save(mask_name)
    
