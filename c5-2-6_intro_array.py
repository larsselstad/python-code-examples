import numpy as np

# arrays må inneholde samme type?

test = np.array(['sdf', 3])

print('test is type', type(test))
print(test)


# arrays kan ikke endre størrelse

# arrays har endel innebygde funksjoner som er nyttige

# sum
ydata = np.array([2.54, 4.1, 1.21, 3.9, 4])
print('sum =', np.sum(ydata))

# lengde
print('lengde =', np.size(ydata))

# legg sammen verdiene i arrayer
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print('array[1,2,3,4] + array[5,6,7,8] =', arr1 + arr2)

# samme kan gjøres med alle matte operatorene
print('array[1,2,3,4] - array[5,6,7,8] =', arr1 - arr2)
print('array[1,2,3,4] * array[5,6,7,8] =', arr1 * arr2)

# plusse på alle verdiene i en array
print('array[1,2,3,4] + 1 = ', arr1 + 1)

# regn ut "magniteude of a velocity"
vx = np.array([0.2, 1.4, -1.9, 7.8])
vy = np.array([-0.3, 2.1, 3.2, 1.7])
magnitudes = ((vx ** 2) + (vy ** 2)) ** 0.5
print(magnitudes)
