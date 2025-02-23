
import numpy as np
from PIL import Image

vps_ids=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
vps_classes=['Road','Sidewalk','Building','Wall','Fence','Pole','Traffic light','Traffic sign','Vegetation','Terrain','Sky','Person','Rider','Car','Truck','Bus','Train','Motorcycle','Bicycle']


#vps_dict={vps_keys[i]:vps_values[i] for i in range(len(vps_keys))}


vps_colour=[[128,64,128],[244,35,232],[70,70,70],[102,102,156],[190,153,153],[153,153,153],[250,170,30],[220,220,0],[107,142,35], [152,251,152],[70,130,180],[220,20,60],[255,0,0],[0,0,142],[0,0,70],[0,60,100],[0,80,100],[0,0,230],[119,11,32]]
#print(len(vps_colour),len(vps_ids),len(vps_classes))
l=zip(vps_classes,vps_colour)
li=list(l)
print(li)





for i,key in enumerate(vps_ids):
	rgbArray = np.zeros((512,512,3), 'uint8')
	rgb=vps_colour[i]
	print(rgb[0],rgb[1],rgb[2])
	
	rgbArray[..., 0] = rgb[0]
	rgbArray[..., 1] = rgb[1]
	rgbArray[..., 2] = rgb[2]
	img = Image.fromarray(rgbArray)
	im_name=str(vps_ids[i])+"_"+str(vps_classes[i])+'.jpeg'
	img.save(im_name)
		
	
