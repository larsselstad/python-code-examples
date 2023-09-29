import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('g004-A1.png')

tresh = 0.58
offset = 0.05
tresh_diff = tresh - offset
is_pixel_not_red = img[:, :, 0] < tresh_diff
is_pixel_green = img[:, :, 1] > tresh
is_pixel_not_blue = img[:, :, 2] < tresh_diff
condition = np.logical_and(
    np.logical_and(is_pixel_green, is_pixel_not_red),
    is_pixel_not_blue)

print('condition:', condition)

# show use of reduce
condition2 = np.logical_and.reduce((is_pixel_green, is_pixel_not_red, is_pixel_not_blue))

print('condition2:', condition2)
