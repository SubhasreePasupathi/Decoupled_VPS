import os
import pandas
import csv
from pprint import pprint
from PIL import Image,ImageDraw
import numpy as np
from rle_mask import binToRLE,annToMask
import pickle



class write_line_inst_eval:
   def __init__(self,fname,bm_path_abs,cid,conf):
       self.field_names=['bm_path','cid','conf']
       write_fol='bm_files_list'
       
       self.path=os.path.join(write_fol,fname.split('.')[0]+'.txt')
       if not os.path.isdir(write_fol):
           os.makedirs(write_fol)
       if not os.path.exists(self.path):
            with open(self.path,'w') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                self.writer.writerow({'bm_path':bm_path_abs,'cid':cid,'conf':conf})
       else:
            with open(self.path,'a') as f:            
                self.writer = csv.DictWriter(f, fieldnames=self.field_names,delimiter=' ')
                self.writer.writerow({'bm_path':bm_path_abs,'cid':cid,'conf':conf})


bdd_to_city={0: 11, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}

l=os.listdir('/home/subha/Videos/datasets/city_vps_val_after_running_scripts/val/img')
l.sort()
print(len(l))
with open ('city_vps_from_pcan.pkl','rb')as f:
     data=pickle.load(f)


data=data['track_result']
print(len(data))
save_fol='pcan_binary_masks'
for i,img in enumerate(data):
    fname=l[i]
    for j,obj in enumerate(img.items()):
       
        obj_id=obj[0]
        bbox = obj[1]['bbox'][:-1]
        conf=obj[1]['bbox'][-1]
        label=obj[1]['label']
        segm=obj[1]['segm']
        arr=np.zeros(segm['size'],np.uint8)
        segm_arr=annToMask(segm,segm['size'][0],segm['size'][1])
        #segm_arr=segm_arr*255
        im=Image.fromarray((segm_arr).astype(np.uint8))
        #im.show()
        im_fol=os.path.join(save_fol,fname.split('.')[0])
        if not os.path.isdir(im_fol):
           os.makedirs(im_fol)
        bm_path=os.path.join(im_fol,str(obj_id)+'.png')
        im.save(bm_path)
        write_line_inst_eval(fname,bm_path,bdd_to_city[label],conf)

        
        print(fname,obj_id,conf,label,bdd_to_city[label])
       
        
