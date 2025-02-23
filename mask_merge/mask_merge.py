import os
from PIL import Image
import numpy as np


#According to mask created by subha
bdd_classes={'person':8, 'rider':1, 'car':2, 'truck':3, 'bus':4, 'train':5, 'motorcycle':6,  'bicycle':7}



#city_vps_things_classes
city_classes={0: "road", 1: "sidewalk", 2: "building", 3: "wall", 4: "fence", 5: "pole", 6: "traffic light", 7: "traffic sign", 8: "vegetation", 9: "terrain", 10: "sky", 11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

#pixel ids convertion dict
bdd_to_city={0: 0, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}


psp_path="/home/subha/mask_merge/city_vps/0005_0025_frankfurt_000000_001736_newImg8bit_psp.png"
pcan_path="/home/subha/mask_merge/city_vps/0005_0025_frankfurt_000000_001736_newImg8bit_pcan.png"

psp_im=Image.open(psp_path)
pcan_im=Image.open(pcan_path)

pcan_arr=np.array(pcan_im)
psp_arr=np.array(psp_im)

#converting bdd ids to city ids in pcan mask
pcan_id_conv_arr=np.zeros((pcan_arr.shape),np.uint8)
pcan_seg_ids=np.unique(pcan_arr[:,:,0])
print(pcan_seg_ids)
for id in pcan_seg_ids:
    mask=pcan_arr[:,:,0]==id
    pcan_id_conv_arr[mask]=bdd_to_city[id]
    
pcan_id_conv_arr[:,:,1] = pcan_arr[:,:,1]
pcan_id_conv_arr[:,:,2] = pcan_arr[:,:,2]

pcan_seg_ids=np.unique(pcan_id_conv_arr[:,:,0])
print(pcan_seg_ids)

#Mask merge
pp_arr=np.zeros((pcan_arr.shape),np.uint8)
pp_arr[:,:,0]=255

psp_stuff_ids=np.unique(psp_arr)
pcan_obj_ids=np.unique(pcan_id_conv_arr[:,:,2])

for stuff_id in psp_stuff_ids:
    if stuff_id<=10:
        mask=psp_arr==stuff_id
        pp_arr[:,:,0][mask]=stuff_id

for oid in pcan_obj_ids:
    if oid != 0:
       
        mask=pcan_id_conv_arr[:,:,2]==oid
        pp_arr[:,:,2][mask]=oid
        pp_arr[:,:,0][mask]=pcan_id_conv_arr[:,:,0][mask]


#save
print(np.unique(pp_arr[:,:,0]))
print(np.unique(pp_arr[:,:,2]))


    
pp_im=Image.fromarray(pp_arr.astype('uint8'))
pp_im.show()
pp_im.save(os.path.join("/home/subha/mask_merge/city_vps/",'result','p_im.png'))
