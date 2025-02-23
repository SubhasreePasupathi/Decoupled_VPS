import os
from pathlib import Path
import shutil

path='/home/subha/Videos/datasets/city_vps_val_after_running_scripts/val/panoptic_video'
write_path='/home/subha/Videos/Evaluate/format_conversion_for_kittti_step_vpq/gt/city_vps_gt_folder'
l=os.listdir(path)
l.sort()


for file in l:
    fol_name=file.split('_')[0]
    Path(os.path.join(write_path,fol_name)).mkdir(parents=True,exist_ok=True)
    #os.rename(os.path.join(path,file),os.path.join(write_path,fol_name,file))
    shutil.copy(os.path.join(path,file),os.path.join(write_path,fol_name,file))
