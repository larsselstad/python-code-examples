import numpy as np

precip = np.array([5.58, 3.54, 4.54, 2.93, 2.10, 1.47, 0.49, 1.03, 1.72, 4.31, 6.50, 5.41])

#- adjust all numbers under 1.1 by 0.82
# create array of Boolean
is_need_adjust = precip < 1.1
# create array with new adjusted values
zero_or_adjusted_precip = is_need_adjust * precip * 0.82
# add adjusted precip to precip
adjusted_precip = zero_or_adjusted_precip + np.logical_not(is_need_adjust) * precip
print(adjusted_precip)

# OR use np.where
adjusted_precip2 = np.where(is_need_adjust, precip * 0.82, precip)
print(adjusted_precip2)


#- return adjusted items from 2D array in a array
precip_2d = np.reshape(precip, (4, 3))
print('precip_2d:', precip_2d)
# get location of values under 1.1
pts = np.where(precip_2d < 1.1)
print('pts:', pts)
print('precip_2d[pts]:', precip_2d[pts])
print('precip_2d[pts] * 0.82:', precip_2d[pts] * 0.82)


#- get sum of values under 1.1
mask = precip < 1.1
print('mask', mask)
print('sum of values under 1.1:', np.sum(mask * precip))

# OR use np.where
print('np.sum(precip_2d[pts]):', np.sum(precip_2d[pts]))