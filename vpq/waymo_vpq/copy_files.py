import os
import numpy as np
from PIL import Image
import shutil
from pathlib import Path

path='/home/subha/Videos/datasets/waymo_gt_modified_with_cv_ids'
write_path='gt/pan_map_fol'

l=os.listdir(path)
l.sort()

for fol in l:
    fol_path=os.path.join(path,fol,'pan_2ch')
    write_path_fol=os.path.join(write_path,fol)

    Path(write_path_fol).mkdir(parents=True,exist_ok=True)

    ll=os.listdir(fol_path)
    ll.sort()
    for file in ll:
        shutil.copy(os.path.join(fol_path,file),os.path.join(write_path_fol,file))
        	
