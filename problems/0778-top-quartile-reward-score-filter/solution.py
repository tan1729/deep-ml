import numpy as np

def top_quartile_mask(scores: list) -> list:
    """
    Return a boolean list marking scores in the top quartile (>= 75th percentile).
    """
    if len(scores) == 0:
        return []
    p75 = np.percentile(scores, 75)
    ans=[]
    for i in range(len(scores)):
        if(scores[i]>=p75):
            ans.append(True)
        else:
            ans.append(False)
    return ans