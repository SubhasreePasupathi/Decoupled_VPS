import os
import shutil
path='/home/subha/Videos/Evaluate/waymo_vpq/gt/pan_map_fol'
l=os.listdir(path)
l.sort()

for fol in l:
    ll=os.listdir(os.path.join(path,fol))
    ll.sort()    
    for i,on in enumerate(ll):
        if i==3:
           last_part='_leftImg8bit.png'
        else:
           last_part='_newImg8bit.png'
        nn=os.path.join(fol.split('_')[0]+'_'+on.split('.')[0]+'_waymo_'+fol.split('_')[0]+'_'+on.split('.')[0]+last_part)
        print(os.path.join(path,fol,nn))
        #os.rename(os.path.join(path,fol,on),os.path.join(path,fol,nn))
        
       
