import numpy as np

arr = np.arange(1, 10)

# 1: use custom power function
def powb(x, exponent):
    p = 1
    for _ in range(exponent):
        p *= x
    return p

cube_array = np.array([powb(a, 3) for a in arr])
print(cube_array)


# 2: use built in power operator
cube_array2 = np.array([a ** 3 for a in arr])
print(cube_array2)


# 3: use array syntax
cube_array3 = arr ** 3
print(cube_array3)


# 4: use numpy power function
cube_array4 = arr.copy()
np.power(cube_array4, 3, out=cube_array4)
print(cube_array4)