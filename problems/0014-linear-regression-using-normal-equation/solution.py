import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	x=np.array(X)
	y=np.array(y)
	xt=x.T
	theta=np.linalg.inv(xt.dot(x)).dot(xt).dot(y)
	return [round(float(t), 4) for t in theta]