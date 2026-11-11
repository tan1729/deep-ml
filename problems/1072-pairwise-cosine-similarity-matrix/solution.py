
import numpy as np

def pairwise_cosine_similarity(X: np.ndarray) -> list:
    X = np.array(X, dtype=float)
    n = X.shape[0]

    norms = np.linalg.norm(X, axis=1)

    ans = []

    for i in range(n):
        row = []

        for j in range(n):
            if norms[i] == 0 or norms[j] == 0:
                sim = 0.0
            else:
                sim = np.dot(X[i], X[j]) / (norms[i] * norms[j])

            row.append(round(float(sim), 4))

        ans.append(row)

    return ans
