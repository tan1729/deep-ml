def collect_rollouts(seeds: list[int], grid_size: int) -> list[int]:
	"""
	Collect optimal episode returns across procedurally generated gridworlds.

	Args:
		seeds: list of integer seeds, each defining one procedural environment.
		grid_size: side length of the square grid.

	Returns:
		A list of episode returns (one per seed).
	"""
	n=len(seeds)
	ans=[]
	for i in range(n):
		gx=seeds[i]%grid_size
		gy=(seeds[i]//grid_size)%grid_size
		if(gx==0 and gy==0):
			gx=grid_size-1
			gy=grid_size-1
		md=gx+gy 
		reward=10-md 
		ans.append(reward)
	return ans
