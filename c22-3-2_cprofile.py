import cProfile
import numpy as np

arr = np.arange(1, 10)

# 1: use custom power function
def powb(x, exponent):
    p = 1
    for _ in range(exponent):
        p *= x
    return p

with cProfile.Profile() as pr:
    arr = np.arange(1, 10)
    cube_arr = arr ** 3

pr.print_stats()