import os
import numpy as np
from PIL import Image

pcan_path='/home/subha/vpq_computation/pcan_track_result_mask_img_city_vps/'
psp_path='/home/subha/vpq_computation/psp_300_mask'

#pcan_files_path 
#psp_files_path

psp_fnames_list=os.listdir(psp_path)
pcan_fnames_list=[]
for (dirpath,dirnames,filenames) in os.walk(pcan_path):
  for filename in filenames:
    pcan_fnames_list.append(filename)
pcan_fnames_list.sort()
psp_fnames_list.sort()
#print(pcan_fnames_list)
#print(psp_fnames_list)
pcan_files_path=[]
for i,file in enumerate(pcan_fnames_list):
  m=file.split('_')
  s=os.path.join(pcan_path,m[0],file)
  #print(s)
  pcan_files_path.append(s)

psp_files_path=[]
for i,file in enumerate(psp_fnames_list):
  k=os.path.join(psp_path,file)
  psp_files_path.append(k)
 
#mask_file_path
mask_files_path=[]
mask_folder='/home/subha/vpq_computation/psp_pcan_masks'

for i,psp_im_path in enumerate(psp_files_path):
	psp_im=Image.open(psp_im_path)
	psp_im_arr=np.asarray(psp_im)
	pcan_im_path=pcan_files_path[i]
	pcan_im=Image.open(pcan_im_path)
	pcan_im_arr=np.array(pcan_im)	
	#change cat_ids of pcan with ref to vpsnet cat
	pcan_id_change_arr=pcan_im_arr.copy()
	cat_id_mapping_pcan_to_vpsnet={8:11,1:12,2:13,3:14,4:15,5:16,6:17,7:18}
	for key,value in cat_id_mapping_pcan_to_vpsnet.items():
		pcan_id_change_arr[:,:,0][pcan_id_change_arr[:,:,0]==key]=value	
	#create 3ch array for psp_pcan_mask
	psp_pcan_mask_arr=np.zeros((1024,2048,3),np.uint8)
	ids=np.unique(psp_im_arr)
	#Merge psp and pcan masks 
	for idx in ids:
		mask=psp_im_arr==idx
		if idx<=10:
			psp_pcan_mask_arr[:,:,0][mask]=idx
			psp_pcan_mask_arr[:,:,2][mask]=idx
		else:
			psp_pcan_mask_arr[:,:,0][mask]=255
			psp_pcan_mask_arr[:,:,2][mask]=0
	ids_0=np.unique(pcan_id_change_arr[:,:,0])
	ids_2=np.unique(pcan_id_change_arr[:,:,2])
	for idx in ids_0:
		if idx!=0:
			mask=pcan_id_change_arr[:,:,0]==idx
			psp_pcan_mask_arr[:,:,0][mask]=idx
	for idx in ids_2:
		if idx!=0:
			mask=pcan_id_change_arr[:,:,2]==idx
			psp_pcan_mask_arr[:,:,2][mask]=idx
	#fill whites with stuff
	pan_seg=psp_pcan_mask_arr[:,:,0].copy()
	pan_obj=psp_pcan_mask_arr[:,:,2].copy()

	while True:
		ids,cnts=np.unique(pan_seg,return_counts=True)
		if ids[-1]==255:
			prev_no_of_white=cnts[-1] 
		else:
			prev_no_of_white=0
		for i in range(1,pan_seg.shape[0]-1):
			for j in range(1,pan_seg.shape[1]-1):
				if pan_seg[i,j]==255:
					n = pan_seg[i-1:i+2, j-1:j+2].flatten()
					ids=[]
					cnts=[]
					id,cnt=np.unique(n,return_counts=True)
					for k,dd in enumerate(id):
						if (dd<=10):
							ids.append(dd)
							cnts.append(cnt[k])
					ids=np.array(ids)
					cnts=np.array(cnts)
					try:
						max=cnts[0]
						id_chosen=ids[0]
						for k,dd in enumerate(ids):
							if cnts[k]>max:
								max=cnts[k]
								id_chosen=dd
					except:
						continue
					pan_seg[i,j]=id_chosen
					pan_obj[i,j]=id_chosen
		ids,cnts=np.unique(pan_seg,return_counts=True)
		if ids[-1]==255:
			curr_no_of_white=cnts[-1] 
		else:
			curr_no_of_white=0
		print(prev_no_of_white,curr_no_of_white)
		if(prev_no_of_white==curr_no_of_white):
			break
	psp_pcan_mask_arr[:,:,0]=pan_seg
	psp_pcan_mask_arr[:,:,2]=pan_obj
	final_im=Image.fromarray((psp_pcan_mask_arr).astype(np.uint8))
	mask_file_path=os.path.join(mask_folder,os.path.basename(psp_im_path))
	final_im.save(mask_file_path)

	if i>2:
		break
