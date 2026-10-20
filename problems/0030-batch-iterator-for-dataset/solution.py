import numpy as np

def batch_iterator(X, y=None, batch_size=32):
    batches = []
    n = X.shape[0]

    for start in range(0, n, batch_size):
        end=start + batch_size
        X_batch = X[start:end]

        if y is not None:
            y_batch = y[start:end]
            batches.append([X_batch.tolist(), y_batch.tolist()])
        else:
            batches.append(X_batch.tolist())

    return batches