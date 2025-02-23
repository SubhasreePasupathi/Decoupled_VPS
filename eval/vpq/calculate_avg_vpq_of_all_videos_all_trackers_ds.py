import os
from pprint import pprint
from pathlib import Path
paths=os.listdir('vpqs')
paths.sort()

write_path='vpqs_avg_check'
Path(write_path).mkdir(parents=True,exist_ok=True)
for path in paths:
    l=os.listdir(os.path.join('vpqs',path))
    l.sort()
    #l=l[:-1]
    list=[]
    for fol in l:
        ll=os.listdir(os.path.join('vpqs',path,fol))
        ll.sort()
        for file in ll:
            if file=='vpq-final.txt':
               list.append(os.path.join('vpqs',path,fol,file))
    
    
    all_vpq_all=[]
    all_vpq_thing=[]
    all_vpq_stuff=[]
    for file in list:
        with open (file,'r') as f:
             data=f.readlines()
        vpq_all=float(data[0].split(':')[1])
        vpq_thing=float(data[1].split(':')[1])
        vpq_stuff=float(data[2].split(':')[1])
        if vpq_thing==0.0:
           print(file)	
        all_vpq_all.append(vpq_all)
        all_vpq_thing.append(vpq_thing)
        all_vpq_stuff.append(vpq_stuff)
        print(vpq_all,vpq_thing,vpq_stuff)
    
    output_filename = os.path.join(write_path, path+'_vpq.txt')
    output_file = open(output_filename, 'w')
    output_file.write("vpq_all:%.4f\n"%(sum(all_vpq_all)/len(all_vpq_all)))
    output_file.write("vpq_thing:%.4f\n"%(sum(all_vpq_thing)/(len(all_vpq_thing)-1)))
    output_file.write("vpq_stuff:%.4f\n"%(sum(all_vpq_stuff)/len(all_vpq_stuff)))
    output_file.close()
    print(len(all_vpq_all))
