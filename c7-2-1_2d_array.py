import numpy as np

air_temp = np.array([
    [7.9, 7.1, 5.7, 3.6, 2.3, 1.7, 1.0],
    [9.9, 8.5, 7.4, 5.7, 4.9, 4.5, 2.1],
    [12.8, 10.6, 9.1, 8.1, 8.8, 8.3, 4.0]
])

# get shape of 2d array
print(np.shape(air_temp))
# returns (3,7) with 3 items with an array of 7 items in each

# size returns 3 * 7
print(np.size(air_temp))

# create similar of 2d array with zeros
air_temp_sim = np.zeros(np.shape(air_temp))
print(air_temp_sim)

# change 1d array to 2d
data = np.arange(12)
data_2d = np.reshape(data, (4,3))
print(data_2d)