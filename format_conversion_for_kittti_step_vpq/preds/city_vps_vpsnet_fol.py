import os
from pathlib import Path
import shutil

path='/home/subha/Videos/Paper1_results/directly_from_nws/vpsnet/cityscape_vps_vpsnet_inference/val_pans_unified/pan_pred'
write_path='/home/subha/Videos/Evaluate/format_conversion_for_kittti_step_vpq/preds/city_vps_vpsnet_folder'
l=os.listdir(path)
l.sort()


for file in l:
    fol_name=file.split('_')[0]
    Path(os.path.join(write_path,fol_name,'pan_pred')).mkdir(parents=True,exist_ok=True)
    #os.rename(os.path.join(path,file),os.path.join(write_path,fol_name,file))
    shutil.copy(os.path.join(path,file),os.path.join(write_path,fol_name,'pan_pred',file))
