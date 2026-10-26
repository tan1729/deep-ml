import numpy as np

# Implement your function below.
def checkpoint_forward(funcs, input_arr):
    x = input_arr.astype(float)
    for func in funcs:
        x = func(x)
    return x.astype(float)
        