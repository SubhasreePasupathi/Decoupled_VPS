import pickle
import pprint 
import sys
'''
with open('vpsnet_pickle_list.pkl','rb') as f:
	outputs=pickle.load(f)
with open('vpsnet_pickle_list.txt','w')as ff:
	pprint.pprint(outputs,stream=ff)

'''
fn=sys.argv[1]
k=fn.split('.')

ofn='.'.join((k[0],'txt'))
print(fn)
print(ofn)

with open(fn,'rb') as s:
	outputs=pickle.load(s)
with open(ofn,'w')as ss:
	pprint.pprint(outputs,stream=ss)
