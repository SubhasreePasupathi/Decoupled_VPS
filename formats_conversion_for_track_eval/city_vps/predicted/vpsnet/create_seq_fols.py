import os
import shutil
path='res_from_vpsnet/val_pans_unified/pan_2ch'

l=os.listdir(path)
l.sort()

for i, file in enumerate(l):
    outfol=file.split('_')[0]
    print(outfol)
    source=os.path.join(path,file)
    outpath=os.path.join('pan_2ch_seq',outfol,file)
    if not os.path.isdir(os.path.join('pan_2ch_seq',outfol)):
       os.makedirs(os.path.join('pan_2ch_seq',outfol))
    shutil.copyfile(source, outpath)
    

