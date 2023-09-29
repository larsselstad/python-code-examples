import numpy as np

# create array with 5 floating point zeroes
fiveZeros = np.zeros(5)
print(fiveZeros)

# create array with 5 int zeroes
# l means long integer
fiveIntZeros = np.zeros(5, dtype='l')
print(fiveIntZeros)

# crete array with 5 floating point ones
fiveOnes = np.ones(5)
print(fiveOnes)

# create array with 5 floating point 100´s
five100s = np.ones(5) * 100.0
print(five100s)

# create array with 5 items from int 0 to int 4
zeroToFour = np.arange(5)
print(zeroToFour)

# create array with 5 items from float 0 to float 4
zeroToFour = np.arange(5, dtype='d')
print(zeroToFour)

# create array with 5 item incremented by 0.25
zeroToOne = np.arange(5) / 4
print(zeroToOne)

# alt: create array with 5 item incremented by 0.25
# start = 0
# stop = 1.1 (excluded)
# increment = 0.25
zeroToOne = np.arange(0, 1.1, 0.25)
print(zeroToOne)

# get type of items in array
print('zeroToOne.dtype =', zeroToOne.dtype, 'zeroToOne.dtype.char =', zeroToOne.dtype.char)

# create a new array with the same size and type
zeroToOneSizeAndType = np.zeros(np.size(zeroToOne), dtype=zeroToOne.dtype.char)
print(zeroToOneSizeAndType)