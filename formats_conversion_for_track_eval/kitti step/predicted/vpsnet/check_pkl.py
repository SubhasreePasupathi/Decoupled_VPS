import os
import pickle
import glob


path='kitti_step_vpsnet_inference'
l=os.listdir(path)
l.sort()

for fol in l:
    print(fol)
    if fol.endswith('.pkl'):

       print(fol)
    

