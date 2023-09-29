import matplotlib.pyplot as plt

plt.figure(3)
plt.plot([9.25,11,13.5,15,15.75],
         [2.54,4.1,1.21,3.9,4],
         marker='o')

plt.figure(4)
plt.plot([0.1, 0.2, 0.3, 0.4],
         [8, -2, 5.3, 4.2],
         linestyle='-.')

# make "figure3" the current plot again
plt.figure(3)
plt.title('Power vs Time')

plt.show()