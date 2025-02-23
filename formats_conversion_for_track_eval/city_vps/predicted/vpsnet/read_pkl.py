import pickle
from pprint import pprint

with open('res_from_vpsnet/val_pred_pans_2ch.pkl','rb') as f:
     print('gkhgjhghghj')
     #data=pickle.load(f)
     unpickler = pickle.Unpickler(f)
     # if file is not empty scores will be equal
     # to the value unpickled
     data = unpickler.load()

	
			
		

with open('test_mask.txt','w') as ff:
	#ff.write(str(data))
	pprint(data,stream=ff)
