import numpy as np

def bernoulli_mask_schedule(seq_len: int, t: float, schedule: str, seed: int) -> list:
    if schedule == 'linear':
        p = t
    else:
        p = 1 - np.cos((np.pi * t) / 2)

    p = np.clip(p, 0, 1)

    np.random.seed(seed)
    s = np.random.rand(seq_len)

    ans = (s < p).astype(int).tolist()

    return ans