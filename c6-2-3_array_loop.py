import numpy as np

# line 4 is the same as line 8-9
lengths_in = np.array([2.3, 5.4, 12.9, 3.7, 8.8])
print(lengths_in * 2.54)

lengths_cm = np.zeros(5, dtype='d')
for i in range(5):
    lengths_cm[i] = lengths_in[i] * 2.54
print(lengths_cm)

# loop array with for and print item
precip = np.array([5, 3, 4, 2, 2, 1])
for iprecip in precip:
    print(iprecip)

# create and loop array with arange
precip_mean_size = np.size(precip) - 1
running_mean = np.zeros(precip_mean_size)
for i in np.arange(precip_mean_size):
    running_mean[i] = (precip[i+1] + precip[i]) / 2
print(running_mean)

# loop sliced array
sub_precip = precip[2:]
sub_precip_sum = 0.0
for iprecip in sub_precip:
    sub_precip_sum = sub_precip_sum + iprecip
print(sub_precip_sum)