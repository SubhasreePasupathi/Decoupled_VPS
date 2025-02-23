from PIL import Image, ImageDraw
import os
import pandas as pd
from collections import defaultdict
from pprint import pprint
import numpy as np 

bot_path='bot_sort_with_filenames'
deep_path='deepmac_binary_mask'
ind_frames_path='bot_sort_ind_frames'
overlay_path='bb_mask_overlay'

bl=os.listdir(bot_path)
bl.sort()

dl=os.listdir(deep_path)
dl.sort()

def xywh2xyxy(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2

for i,seq_file in enumerate(bl):
    df = pd.read_csv(os.path.join(bot_path,seq_file))
    cols=list(df.columns)    
    frame_ids=np.unique(df['frame_id']) 
    
    for j,f_id in enumerate(frame_ids):
        dff=pd.DataFrame()
        mask= df['frame_id']==f_id
        dff=df[mask]
        name=dff['file_names'].tolist()[0]
        print(dff)
        dff.to_csv(os.path.join(ind_frames_path,name+'.csv'),index=False)
        
        print('\n.........................\n')
        


'''
im_path='000000.png'
img = Image.open(im_path)

boxes=[[ 421.66992,  186.00003,  555.24207,  285.9817 ],
	[ 889.5222 ,  170.4285 ,  902.2972 ,  206.66005],
	[1128.1084 ,  142.6732 , 1172.7382 ,  226.94936],
	[ 845.57117,  178.49657,  860.38666,  200.92165]]
img1 = ImageDraw.Draw(img)  
for bb in boxes:
    
    img1.rectangle(bb, outline ="red")
    img.show()
'''
