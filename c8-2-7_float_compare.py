import numpy as np

# this is False
print('3.1 == 3.1001', 3.1 == 3.1001)

# this is False
print('3.1 == 3.10000000001', 3.1 == 3.10000000001)

# this is could be True if your computer works that way
print('3.1 == 3.100000000000000000000001', 3.1 == 3.100000000000000000000001)

# we can check if the values are close
print('np.isclose(3.1, 3.10000000001)', np.isclose(3.1, 3.10000000001))
print('np.isclose(3.1, 3.100000000000000000000001', np.isclose(3.1, 3.100000000000000000000001))