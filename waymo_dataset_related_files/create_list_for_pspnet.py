import os

path='datasets/Waymo_open_dataset/'
out_path1='/pspnet/semseg/list/waymo_val.txt'
out_path2='/datasets/waymo_val.txt'

l=os.listdir(path)
l.sort()
l=l[:-3] # --> 3 py files

files_list=[]
sem_list=[]
for fol in l:
    fol_path=os.path.join(path,fol,'FRONT','rgb')
    sem_path=os.path.join(path,fol,'FRONT','semseg')
    ll=os.listdir(fol_path)
    ll.sort()
    sl=os.listdir(sem_path)
    sl.sort()
    for fn in ll:
        file_path=os.path.join(fol_path,fn)       
        files_list.append(file_path)
    for sn in sl:
        sem_file_path=os.path.join(sem_path,sn)
        sem_list.append(sem_file_path)

with open(out_path1,'w')as f:
     for i,line in enumerate(files_list):
        f.write(line+" "+sem_list[i])
        f.write("\n")

with open(out_path2,'w')as ff:
     for i,line in enumerate(files_list):
        ff.write(line+" "+sem_list[i])
        ff.write("\n")

