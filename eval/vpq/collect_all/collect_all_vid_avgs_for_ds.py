import os
import shutil
from pathlib import Path
import numpy as np
import re
import csv
import pandas as pd
import glob
from pprint import pprint


path='/home/subha/Videos/work_area/vpq_avg_calc/vpqs/vpq_waymo_vpsnet'
l=os.listdir(path)
l.sort()
csv_files=[]
for fol in l:
    #ll=os.listdir(os.path.join(path,fol))
    
    csv_files.append(glob.glob(os.path.join(path,fol) + '/*.csv'))

pprint(len(csv_files))

cf=[]
for el in csv_files:
    for e in el:
        cf.append(e)

df_concat = pd.concat([pd.read_csv(f) for f in cf ], axis=0,ignore_index=True)
df_concat.sort_values(by=['cls'],ascending=True)
df_concat.to_csv(os.path.join(path,'metrics.csv'))



