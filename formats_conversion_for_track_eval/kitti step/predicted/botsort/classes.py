
#According to mask created by subha
bdd_classes={'person':8, 'rider':1, 'car':2, 'truck':3, 'bus':4, 'train':5, 'motorcycle':6,  'bicycle':7}



#city_vps_things_classes
city_classes={0: "road", 1: "sidewalk", 2: "building", 3: "wall", 4: "fence", 5: "pole", 6: "traffic light", 7: "traffic sign", 8: "vegetation", 9: "terrain", 10: "sky", 11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

#pixel ids convertion dict
bdd_to_city={0: 0, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}





coco={1:'person', 2:'bicycle', 3:'car',	4:'motorcycle',5:'airplane', 6:'bus', 7:'train',8:'truck'}

coco_botsort={0:'person', 1:'bicycle', 2:'car',	3:'motorcycle',4:'airplane', 5:'bus', 6:'train',7:'truck'}
city_things={11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

coco_botsort_to_city={0:11, 1:18, 2:13, 3:17, 4:0, 5:15, 6:16, 7:14}
city_to_coco_botsort={11:0 , 12:0 , 13:2 ,14:7 , 15:5 ,16:6 ,17:3 ,18:1}

