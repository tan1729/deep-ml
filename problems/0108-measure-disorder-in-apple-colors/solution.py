
import numpy as np

def disorder(y: list) -> float:
    colors, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)

    s = 0
    for i in range(len(colors)):
        s += probabilities[i]**2

    return 1 - s
