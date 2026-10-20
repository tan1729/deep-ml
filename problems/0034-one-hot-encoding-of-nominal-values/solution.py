
import numpy as np

def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = np.max(x) + 1

    output = np.zeros((len(x), n_col))

    rows = np.arange(len(x))
    cols = x

    output[rows, cols] = 1

    return output
