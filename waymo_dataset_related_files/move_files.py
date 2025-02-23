import os
import shutil

path="Datasets/Waymo Open Dataset/Val Files with Seg"

l=os.listdir(path)
l.sort()
#print(l)

new_fols_names=[]
for fols in l:
    new_fol_name='_'.join(fols.split('_')[:2])
    if not os.path.isdir(new_fol_name):
       new_fols_names.append(new_fol_name)
       os.makedirs(new_fol_name)
       
#print(new_fols_names)

for i,fol in enumerate(l):
    ll=os.listdir(os.path.join(path,fol))
    #print(fol)
    for camerafol in ll:        
        if camerafol=='FRONT':
           for f in os.listdir(os.path.join(path,fol,camerafol)):
               if f=='ins':
                  kk=os.listdir(os.path.join(path,fol,camerafol,f))
                  print(len(kk))
'''
           src=os.path.join(path,fol,camerafol)
           
           dest=os.path.join(('_'.join(fol.split('_')[:2])),camerafol)
           shutil.copytree(src,dest)
'''
