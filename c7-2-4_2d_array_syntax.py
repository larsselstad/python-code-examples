import numpy as np

air_temp = np.array([
    [7.9, 7.1, 5.7, 3.6, 2.3, 1.7, 1.0],
    [9.9, 8.5, 7.4, 5.7, 4.9, 4.5, 2.1],
    [12.8, 10.6, 9.1, 8.1, 8.8, 8.3, 4.0]
])

# dobler alle verdier
double_air_temp = air_temp * 2
print(double_air_temp)

# legger sammen verdiene i de 2 arrayene
combined_temp = air_temp + double_air_temp
print(combined_temp)

# finn laveste og høyeste tall i array
print(np.min(air_temp), np.max(air_temp))