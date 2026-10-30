
import numpy as np

def macro_average_accuracy(subtask_results: dict) -> float:
    if len(subtask_results) == 0:
        return 0.0

    ac = []

    for key in subtask_results:
        s = 0
        n = len(subtask_results[key])

        for j in subtask_results[key]:
            if j[0] == j[1]:
                s += 1

        if n == 0:
            ac.append(0.0)
        else:
            ac.append(s / n)

    ans = np.mean(ac)
    return round(float(ans), 4)
