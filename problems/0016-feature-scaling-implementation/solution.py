import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data=(data-data.mean(axis=0))/data.std(axis=0)
	normalized_data=(data-data.min(axis=0))/(data.max(axis=0)-data.min(axis=0))
	return np.round(standardized_data,4), np.round(normalized_data,4)