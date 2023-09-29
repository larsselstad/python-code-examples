import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

#- Define data:
hour_in_day = np.arange(11) + 7
duck_count = np.array([5, 3, 4, -999, 2, 3, 6, -999, 7, 6, 7])
duck_count_masked = ma.masked_values(duck_count, -999)

print(type(duck_count_masked))
print(duck_count_masked)
print(duck_count_masked.mask)
print(duck_count_masked.fill_value)
print(duck_count_masked.filled())

#- Calc mean:
print("Mean:", ma.mean(duck_count_masked))

#- Get ducks per minute
print('Ducks per minute:', duck_count_masked / 60)

#- Plot graph:
plt.figure()
plt.plot(hour_in_day, duck_count_masked, 'ko-')
plt.title('Masked arrays to count ducks')
plt.xlabel('Hours in the day')
plt.ylabel('Count')
plt.show()