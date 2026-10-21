
import numpy as np

def rmse(y_true, y_pred):
    s = np.mean((y_true - y_pred)**2)
    rmse_res = np.sqrt(s)
    return round(float(rmse_res), 3)
