import matplotlib.pyplot as plt

plt.plot([9.25,11,13.5,15,15.75],
         [2.54,4.1,1.21,3.9,4],
         linestyle='--',
         linewidth=5.0,
         marker='*',
         markersize=20.0,
         markeredgewidth=2.0,
         markerfacecolor='w')

plt.axis([8, 18, 0, 5])
plt.xticks([8, 10, 12, 14, 16, 18])

plt.xlabel('Decimal Hour in Day')
plt.ylabel('Power (mW)')

plt.title('Power vs Time')

plt.savefig('testplot.png', dpi=300)