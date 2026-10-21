import numpy as np
def precision(y_true, y_pred):
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))

    if tp + fp == 0:
        return 0.0

    return tp / (tp + fp)

def recall(y_true, y_pred):
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fn = np.sum((y_pred == 0) & (y_true == 1))

    if tp + fn == 0:
        return 0.0

    return tp / (tp + fn)

def f_score(y_true, y_pred, beta):
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)

    denominator = beta**2 * p + r

    if denominator == 0:
        return 0.0

    f = (1 + beta**2) * p * r / denominator
    return round(f, 3)
