
import numpy as np

def batch_iterator(X, y=None, batch_size=32):
    batches = []
    n = len(X)

    for start in range(0, n, batch_size):
        X_batch = X[start:start + batch_size]

        if y is not None:
            y_batch = y[start:start + batch_size]
            batches.append([X_batch.tolist(), y_batch.tolist()])
        else:
            batches.append(X_batch.tolist())

    return batches
