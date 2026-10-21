
import numpy as np

def r_squared(y_true, y_pred):
    y_mean = np.mean(y_true)
    num = 0
    den = 0
    n = y_true.shape[0]

    for i in range(n):
        num += (y_true[i] - y_pred[i])**2
        den += (y_true[i] - y_mean)**2

    ans = 1 - num / den
    return ans
