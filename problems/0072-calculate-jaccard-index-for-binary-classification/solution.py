
import numpy as np

def jaccard_index(y_true, y_pred):
	n=y_true.shape[0]
	c1=np.sum((y_true==1) & (y_pred==1))
	c2=np.sum((y_true==1) | (y_pred==1))
	if(c2==0):
		return 0.0
	result=c1/c2
	return round(result, 3)
