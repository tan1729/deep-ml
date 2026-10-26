import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    # Your code here
    a=np.min(values)
    b=np.max(values)
    x=c+(d-c)/(b-a)*(values-a)
    return x