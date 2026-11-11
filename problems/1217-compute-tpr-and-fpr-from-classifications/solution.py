import numpy as np

def compute_tpr_fpr(y_true, y_pred):
    """
    Compute TPR and FPR from true and predicted binary labels.

    Args:
        y_true (array-like): Ground-truth labels (0 or 1).
        y_pred (array-like): Predicted labels (0 or 1).

    Returns:
        tuple: (tpr, fpr) as Python floats.
    """
    # TODO: compute TP, FN, FP, TN then TPR and FPR
    tp=sum((y_pred==1) & (y_true==1))
    fp=sum((y_pred==1) & (y_true==0))
    tn=sum((y_true==0) & (y_pred==0))
    fn=sum((y_true==1) & (y_pred==0))
    if((tp+fn)==0.0):
        tpr=0.0
    else:
        tpr=tp/(tp+fn)
    if((fp+tn)==0.0):
        fpr=0.0
    else:
        fpr=fp/(fp+tn)
    return (tpr,fpr)
    
