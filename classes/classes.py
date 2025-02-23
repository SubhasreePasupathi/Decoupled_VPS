from deepdiff import DeepDiff as dd
from pprint import pprint
#According to mask created 
bdd_classes={'person':8, 'rider':1, 'car':2, 'truck':3, 'bus':4, 'train':5, 'motorcycle':6,  'bicycle':7}



#city_vps_things_classes
city_classes={0: "road", 1: "sidewalk", 2: "building", 3: "wall", 4: "fence", 5: "pole", 6: "traffic light", 7: "traffic sign", 8: "vegetation", 9: "terrain", 10: "sky", 11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

#pixel ids convertion dict
bdd_to_city={0: 0, 8: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18}





coco={1:'person', 2:'bicycle', 3:'car', 4:'motorcycle',5:'airplane', 6:'bus', 7:'train',8:'truck'}

coco_botsort={0:'person', 1:'bicycle', 2:'car',3:'motorcycle',4:'airplane', 5:'bus', 6:'train',7:'truck'}
city_things={11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

coco_botsort_to_city={0:11, 1:18, 2:13, 3:17, 4:0, 5:15, 6:16, 7:14}
city_to_coco_botsort={11:0 , 12:0 , 13:2 ,14:7 , 15:5 ,16:6 ,17:3 ,18:1}


waymo_classes={0: 'unknown(sdc)', 1: 'car', 2: 'truck', 3: 'bus', 4: 'other_large_vehicle', 5: 'bicycle', 6: 'motorcycle', 7: 'trailer', 8: 'person', 9: 'cyclist', 10: 'motorcyclist', 11: 'bird', 12: 'ground_animal', 13: 'construction_cone_pole', 14: 'pole', 15: 'other_pedestrian_object', 16: 'sign', 17: 'traffic light', 18: 'building', 19: 'road', 20: 'lane_marker', 21: 'road_marker', 22: 'sidewalk', 23: 'vegetation', 24: 'sky', 25: 'ground', 26: 'dynamic', 27: 'static', 255: 'ignore_label'}

waymo_things={ 1: 'car', 2: 'truck', 3: 'bus', 4: 'other_large_vehicle',  7: 'trailer', 8: 'person', 9: 'cyclist', 10: 'motorcyclist'}
city_things={11: "person", 12: "rider", 13:"car", 14: "truck", 15: "bus", 16: "train", 17: "motorcycle", 18: "bicycle"}

waymo_stuff={0: 'unknown(sdc)', 5: 'bicycle',6: 'motorcycle',11: 'bird',12: 'ground_animal',13: 'construction_cone_pole',14: 'pole',15: 'other_pedestrian_object',16: 'sign', 17: 'traffic_light',18: 'building',19: 'road',20: 'lane_marker',21: 'road_marker',22: 'sidewalk',23: 'vegetation',24: 'sky',25: 'ground',26: 'dynamic',27: 'static',255: 'ignore_label'}
city_stuff={0: "road", 1: "sidewalk", 2: "building", 3: "wall", 4: "fence", 5: "pole", 6: "traffic light", 7: "traffic sign", 8: "vegetation", 9: "terrain", 10: "sky"}


city_inv={v: k for k, v in city_classes.items()}
waymo_inv={v: k for k, v in waymo_classes.items()}


diff=dd(city_inv,waymo_inv)
pprint(diff)

city_to_waymo={     'bicycle': {18: 5},
                    'building': {2: 18},
                    'bus': {15: 3},
                    'car': {13: 1},
                    'motorcycle': {17: 6},
                    'person': {11: 8},
                    'pole': {5: 14},
                    'road': {0: 19},
                    'sidewalk': {1: 22},
                    'sky': {10: 24},
                    'truck': {14: 2},
                    'vegetation': {8: 23},
                    'traffic light':{6,17}
                    }
       
waymo_to_city={
                    'bicycle': {5: 18},
                    'building': {18: 2},
                    'bus': {3: 15},
                    'car': {1: 13},
                    'motorcycle': {6: 17},
                    'person': {8: 11},
                    'pole': {14: 5},
                    'road': {19: 0},
                    'sidewalk': {22: 1},
                    'sky': {24: 10},
                    'truck': {2: 14},
                    'vegetation': {23: 8}
                    'traffic light':{17,6}
                    
                    }

extra_in_city={ 'wall', 'fence',  'traffic sign', 'terrain', 'rider', 'train'}

extra_in_waymo={'unknown(sdc)', 'other_large_vehicle', 'trailer', 'cyclist', 'motorcyclist', 'bird', 'ground_animal', 'construction_cone_pole', 'other_pedestrian_object', 'sign',  'lane_marker', 'road_marker', 'ground', 'dynamic', 'static', 'ignore_label'}




waymo_extra_classes_ids_assigned_by_subha={'unknown(sdc)': 255,
'other_large_vehicle':		'truck',
'trailer':			'truck',
'cyclist':			'rider',
'motorcyclist':			'rider',
'bird':				'sky',
'ground_animal':		'sidewalk',
'construction_cone_pole':	'pole',
'other_pedestrian_object':	'pedestrian',
'sign': 			'traffic sign',		
'lane_marker': 			'road',
'road_marker':			'road',
'ground':			'terrain',
'dynamic':			255,
'static':			255,													
'ignore_label':			255,	
'bicycle':			255, 
'motocycle': 			255
}



waymo_to_city:{ 1:255,
2:13,
3:14,
4:15,
5:14,
6:255,
7:255,
8:14,
9:11,
10:255,
11:255,
12:255
13:1,
14:5,
15:5,
16:11,
17:7,
18:6,
19:2,
20:0,
21:0,
22:0,
23:1,
24:8,
25:10,
26:9,
27:255,
28:255,
255:255

}

















