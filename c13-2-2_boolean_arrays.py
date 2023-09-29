import numpy as np

# create array of boolean from expression
atomic_number = np.array([17, 2, 6, 8])
has_more_protons_than_carbon = atomic_number > 6
print(has_more_protons_than_carbon)


# to use and, or, not on array values
print(np.logical_and(atomic_number > 6, atomic_number < 10))
print(np.logical_or(atomic_number < 6, atomic_number > 10))
print(np.logical_not(atomic_number > 6))