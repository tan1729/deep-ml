import numpy as np
def compute_inference_metrics(timestamps: list[float]) -> dict:
	"""
	Compute LLM inference performance metrics from token timestamps.
	
	Args:
		timestamps: List of floats where timestamps[0] is the request start time
		            and timestamps[1:] are the times when each output token was generated.
	
	Returns:
		Dictionary with keys 'ttft', 'tps', 'itl' containing the metric values.
	"""
	timestamps=np.array(timestamps)
	ttft=timestamps[1]-timestamps[0]
	n=timestamps.shape[0]
	diff=timestamps[n-1]-timestamps[0]
	tps = (n - 1) / diff
	if(n==2):
		itl=0.0
	else:
	    a=[]
	    for i in range(1,n-1):
	    	a.append(timestamps[i+1]-timestamps[i])
	    itl=np.mean(a)
	return {'ttft': ttft, 'tps': tps, 'itl': itl}

