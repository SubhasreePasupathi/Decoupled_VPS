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


#bdd_to_city={0: 11, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}
img_path='/home/subha/Videos/Evaluate/format_conversion_for_inst_eval/gt_as_pred/city_gt_inst_map_uint16'
l=os.listdir(img_path)
l.sort()
print(len(l))


save_fol='cv_gt_as_pred_binary_masks'

for fname in l:
    arr=np.array(Image.open(os.path.join(img_path,fname))).astype(np.uint16)
    ids=np.unique(arr) 
    print(ids)
    

    for i,id in enumerate(ids):
        label=id//1000
        #iid=id%1000
        bm=np.zeros_like(arr)
        mask=arr==id
        bm[mask]=1
        im=Image.fromarray((bm).astype(np.uint8))
        im_fol=os.path.join(save_fol,fname.split('.')[0])
        if not os.path.isdir(im_fol):
           os.makedirs(im_fol)
        bm_path=os.path.join(im_fol,str(i)+'.png')
        im.save(bm_path)
        conf=1
        write_line_inst_eval(fname,bm_path,label,conf)        
        print(fname,id,conf,label)
       
        
