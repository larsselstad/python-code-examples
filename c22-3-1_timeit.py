import timeit
import numpy as np

arr = np.arange(1, 10)

# 1: use custom power function
def powb(x, exponent):
    p = 1
    for _ in range(exponent):
        p *= x
    return p

custom_function = timeit.timeit('np.array([powb(a, 3) for a in arr])', number=10000, globals=globals())
print(custom_function, 'timeit custom function')


# 2: use built in power operator
power_operator = timeit.timeit('np.array([a ** 3 for a in arr])', number=10000, globals=globals())
print(power_operator, 'timeit built in power operator')


# 3: use array syntax
array_syntax = timeit.timeit('arr ** 3', number=10000, globals=globals())
print(array_syntax, 'timeit array syntax')


# 4: use numpy power function
cube_array4 = arr.copy()
numpy_power = timeit.timeit('np.power(cube_array4, 3, out=cube_array4)', number=10000, globals=globals())
print(numpy_power, 'timeit numpy power function')