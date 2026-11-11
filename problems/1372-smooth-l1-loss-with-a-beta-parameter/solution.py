
import numpy as np

def smooth_l1(pred, target, beta=1.0, reduction='mean'):

    if beta <= 0:
        raise ValueError("beta must be greater than 0")

    if reduction not in ['mean', 'sum', 'none']:
        raise ValueError("Invalid reduction")

    pred = np.array(pred)
    target = np.array(target)

    ans = np.abs(pred - target)

    f = np.where(
        ans < beta,
        0.5 * (ans ** 2) / beta,
        ans - 0.5 * beta
    )

    if reduction == 'none':
        return f
    elif reduction == 'sum':
        return float(np.sum(f))
    else:
        return float(np.mean(f))
