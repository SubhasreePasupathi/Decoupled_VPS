import os

path='/datasets/Waymo_open_dataset/'
out_path='SSeg-master/scripts/demo_waymo_fol_subha.sh'

l=os.listdir(path)
l.sort()
l=l[:-4]

lines=[]
for fol in l:
    string='CUDA_VISIBLE_DEVICES=0 python demo_folder.py --demo-folder '+os.path.join(path,fol,'FRONT','rgb')+' --snapshot ./pretrained_models/kitti_best.pth --save-dir '+os.path.join('./output/waymo/with_kitti_best_weights',fol)
    lines.append(string)

with open(out_path,'w')as f:
     for line in lines:
         f.write(line)
         f.write("\n")
