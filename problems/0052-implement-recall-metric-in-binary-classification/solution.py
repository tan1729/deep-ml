import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    tp=np.sum((y_pred==1)&(y_true==1))
    tn=np.sum((y_pred==0)&(y_true==0))
    fn=np.sum((y_pred==0)&(y_true==1))
    rec=tp/(tp+fn)
    if(tp+fn == 0):
        rec=0.0
    return rec    
