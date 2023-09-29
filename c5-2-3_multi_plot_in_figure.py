import matplotlib.pyplot as plt

plt.figure(1)
plt.plot([0, 1, 2, 3], [1, 2, 3, 4], '--o',
         [1, 3, 5, 9], [8, -2, 5.3, 4.2], '-D')

plt.title('2 plots in one figure')

plt.figure('legend')

plt.plot([0, 1, 2, 3], [1, 2, 3, 4], 'r--o', label='Sensor 1')
plt.plot([1, 3, 5, 9], [8, -2, 5.3, 4.2], 'b-D', label='Sensor 2')

plt.legend()

plt.title('2 plots in one figure with legend')

plt.show()