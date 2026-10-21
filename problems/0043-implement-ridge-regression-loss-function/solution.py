import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	s=0
	n=X.shape[0]
	for i in range(n):
		s+=(y_true[i]-X[i].dot(w))*(y_true[i]-X[i].dot(w))
	s=(1/n)*s
	d=w.shape[0]
	s2=0
	for i in range(d):
		s2+=w[i]*w[i]
	s2=alpha*s2 
	L=s+s2 
	return L
