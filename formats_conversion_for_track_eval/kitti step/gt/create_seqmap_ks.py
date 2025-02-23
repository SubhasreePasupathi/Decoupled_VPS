import os
path='val'
l=os.listdir(path)
l.sort()
import csv
from PIL import Image
#h,w=375 ,1242

field_names=['fol','len','h','w']
with open('seqmap.txt','w') as f:
    writer = csv.DictWriter(f, fieldnames=field_names,delimiter=' ')
    for folder in l:
        print(folder)
        ll=os.listdir(os.path.join(path,folder))
        ll.sort()
        length=len(ll)
        for file in ll:
            img=Image.open(os.path.join(path,folder,file))
            w,h =img.size
        writer.writerow({'fol':folder,'len':length,'h':h,'w':w})
    
