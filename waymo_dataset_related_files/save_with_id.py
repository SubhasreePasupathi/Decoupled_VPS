import os
import shutil
from PIL import Image
import numpy as np


path="."

l=os.listdir(path)
l.sort()
#print(l)


for i,fol in enumerate(l):
    ll=os.listdir(os.path.join(path,fol))
    #print(fol)
    for camerafol in ll:        
        if camerafol=='FRONT':
           for f in os.listdir(os.path.join(path,fol,camerafol)):
               if f=='sem' :
                  print(f)
                  kk=os.listdir(os.path.join(path,fol,camerafol,f))
                  
                  if not os.path.isdir(os.path.join(path,fol,camerafol,'semseg')):
                         os.makedirs(os.path.join(path,fol,camerafol,'semseg'))
                  for file in kk:
                      im=Image.open(os.path.join(path,fol,camerafol,f,file))
                      arr=np.array(im)
                      ids=np.unique(arr)
                      new_arr=np.zeros_like(arr)
                      for id in ids:
                          mask=arr==id
                          new_arr[mask]=id
                      new_im=Image.fromarray((new_arr).astype(np.uint8))
                      
                      new_im.save(os.path.join(path,fol,camerafol,'semseg',file))
                  print(len(kk))
               #elif f=='sem':
'''
           src=os.path.join(path,fol,camerafol)
           
           dest=os.path.join(('_'.join(fol.split('_')[:2])),camerafol)
           shutil.copytree(src,dest)
'''
