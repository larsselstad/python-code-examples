import numpy as np

air_temp = np.array([
    [7.9, 7.1, 5.7, 3.6, 2.3, 1.7, 1.0],
    [9.9, 8.5, 7.4, 5.7, 4.9, 4.5, 2.1],
    [12.8, 10.6, 9.1, 8.1, 8.8, 8.3, 4.0]
])

for i in range(3):
    for j in range(7):
        print('(i,j) = (' + str(i) + ',' + str(j) + \
              ') value: ' + str(air_temp[i,j]))