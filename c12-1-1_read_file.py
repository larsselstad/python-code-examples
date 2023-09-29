#- Import modules
import numpy as np

#- Read in datafile and reshape into 3-D array
air_temp_2d = np.genfromtxt('surf_temp_n-d_midwest.csv', delimiter=',')
air_temp = np.reshape(air_temp_2d, (4, 5, 7))


#- Create array of zeros to hold 24-hour average:
air_temp_24h_avg = np.zeros(np.shape(air_temp)[-2:], dtype=air_temp.dtype.char)


#- Calculate 24-hr average at each location
avg_shape = np.shape(air_temp_24h_avg)
for i in range(avg_shape[0]):
    for j in range(avg_shape[1]):
        air_temp_24h_avg[i, j] = np.mean(air_temp[:, i, j])
print(air_temp_24h_avg)

#- Convert air_temp to K and print maxium value:
air_temp_K = air_temp + 273.15
print("Maximum temp in K:", np.max(air_temp_K))