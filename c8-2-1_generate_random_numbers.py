import numpy as np

# random int number beetween 0 and 40
print(np.random.randint(0, 40))

# array with 5 random ints beetween 0 and 40
print(np.random.randint(0, 40, size=5))

# 2D array with 5 by 4 random ints beetween 0 and 40
print(np.random.randint(0, 40, size=(5, 4)))

# random float number beetween 0 and 1
print(np.random.uniform())

# random float number beetween 0 and 40
print(np.random.uniform(0, 40))

# array with 5 random floats beetween 0 and 40
print(np.random.uniform(0, 40, size=5))

# 2D array with 5 by 4 random floats beetween 0 and 40
print(np.random.uniform(0, 40, size=(5, 4)))