import numpy as np
def precision(y_true,y_pred):
	y_true=np.array(y_true)
	y_pred=np.array(y_pred)
	tp=np.sum((y_true==1) & (y_pred==1))
	fp=np.sum((y_true==0) & (y_pred==1))
	if((tp+fp)==0):
		return 0.0
	rec=tp/(tp+fp)
	return rec 
def recall(y_true,y_pred):
	y_true=np.array(y_true)
	y_pred=np.array(y_pred)
	tp=np.sum((y_true==1) & (y_pred==1))
	fn=np.sum((y_true==1) & (y_pred==0))
	if((tp+fn)==0):
		return 0.0
	rec=tp/(tp+fn)
	return rec 
def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	p=precision(y_true,y_pred)
	r=recall(y_true,y_pred)
	if((p+r) == 0):
		return 0.0
	f1=2*p*r/(p+r)
	return round(f1,3)