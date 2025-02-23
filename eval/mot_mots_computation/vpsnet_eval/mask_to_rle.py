import pycocotools.mask as mask_util
import numpy as np
import pickle

def encode_mask_to_rle(mask):
    """Encode bitmap mask to RLE code.

    Args:
        track_results (list | tuple[list]): track results.
            In mask scoring rcnn, mask_results is a tuple of (segm_results,
            segm_cls_score).

    Returns:
        list | tuple: RLE encoded mask.
    """
    #for id, roi in track_results.items():
       #roi['segm'] = mask_util.encode(
            #np.array(roi['segm'][:, :, np.newaxis], order='F',
                     #dtype='uint8'))[0]  # encoded with RLE
    rle = mask_util.encode(np.array(mask,order='F',dtype='uint8'))
        
    
    return rle

with open('vpsnet_pickle.pkl','rb') as f:
	outputs=pickle.load(f)
'''
for result in outputs['track_result']:
    #result=encode_track_results(result)
    for id,roi in result.items():
        mask=roi['segm']['counts']
        rle=encode_mask_to_rle(mask)
        print(id)
        print(roi)
        print(rle)
        break
'''
mask=outputs['track_result'][0][1]['segm']['counts']
rle=encode_mask_to_rle(mask)
print(id)
print(mask)
print(rle)
#with open('vpsnet_pickle_rle.pkl','wb')as fff:
	#pickle.dump(outputs,fff)
