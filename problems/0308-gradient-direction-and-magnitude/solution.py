import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    gradient = np.array(gradient, dtype=float)
    magnitude = np.sqrt(np.sum(gradient**2))

    if magnitude == 0:
        direction = np.zeros_like(gradient)
        desc = np.zeros_like(gradient)
    else:
        direction = gradient / magnitude
        desc = -direction

    return {
        'magnitude': float(magnitude),
        'direction': direction.tolist(),
        'descent_direction': desc.tolist()
    }