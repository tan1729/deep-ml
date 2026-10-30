import numpy as np
def combined_quality_filter(rm_scores, llm_scores):
    """
    Return a boolean list marking high-quality samples by combined RM and LLM criteria.
    """
    if(len(rm_scores)==0 or len(llm_scores)==0):
        return []
    p75=np.percentile(rm_scores,75)
    ans=[]
    maxi=np.max(llm_scores)
    for i in range(len(rm_scores)):
        if(rm_scores[i]>=p75 or llm_scores[i]==maxi):
            ans.append(True)
        else:
            ans.append(False)
    return ans
