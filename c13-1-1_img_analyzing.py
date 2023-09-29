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

img_highlight = img.copy()
img_highlight[:, :, 0] = np.where(condition, 1.0, img[:, :, 0])
img_highlight[:, :, 1] = np.where(condition, 0.0, img[:, :, 1])
img_highlight[:, :, 2] = np.where(condition, 1.0, img[:, :, 2])

plt.imsave('g004-A1_highlight.png', img_highlight)

percent_green = np.sum(condition) / np.size(condition) * 100
print('Percent "green":', percent_green)