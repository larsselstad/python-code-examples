import numpy as np

air_temp = np.array([
    [7.9, 7.1, 5.7, 3.6, 2.3, 1.7, 1.0],
    [9.9, 8.5, 7.4, 5.7, 4.9, 4.5, 2.1],
    [12.8, 10.6, 9.1, 8.1, 8.8, 8.3, 4.0]
])

# get item
print('air_temp[1,3] =', air_temp[1,3])

# change value
air_temp[1,3] = 2.2
print('new value for air_temp[1,3]', air_temp)

# slice array and array
print('air_temp[1:2, 0:2]', air_temp[1:2, 0:2])

# slice to just last array with last to items
print('air_temp[-1, -2:]')
print(air_temp[-1, -2:])