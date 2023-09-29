#- Module imports:

import numpy as np
import matplotlib.pyplot as plt


#- Set random seed, number of positions, and domain parameters:

np.random.seed(31493293)
n_positions = 5001
domain_shape = (200, 200)
food = np.zeros(domain_shape) + 5.0
N = np.zeros(domain_shape)
N_crit = 0


#- Set parameteres and arrays for walker:

max_eat_rate = 0.1
use_energy = 0.05

energy = np.zeros(n_positions, dtype='d')
x = np.zeros(n_positions, dtype='l')
y = np.zeros(n_positions, dtype='l')

energy[0] = 0.3
x[0] = domain_shape[1] // 2
y[0] = domain_shape[0] // 2

step_x = np.array([ 0,  1, 1, 1, 0, -1, -1, -1])
step_y = np.array([-1, -1, 0, 1, 1,  1,  0, -1])
#- Take steps:

i = 1
while i < n_positions:
    step_idx = np.random.randint(0, np.size(step_x))
    xtrial = x[i - 1] + step_x[step_idx]
    ytrial = y[i - 1] + step_y[step_idx]

    if (xtrial >= domain_shape[1]) or (xtrial < 0):
        continue
    if (ytrial >= domain_shape[0]) or (ytrial < 0):
        continue

    if N[ytrial, xtrial] < N_crit:
        N[ytrial, xtrial] += 1
        x[i] = x[i - 1]
        y[i] = y[i - 1]
    else:
        if energy[i - 1] > 0.0:
            x[i] = xtrial
            y[i] = ytrial
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1]

    energy_from_eat = np.min([ max_eat_rate, food[y[i - 1], x[i - 1]] ])
    energy[i] = energy[i - 1] + energy_from_eat - use_energy
    food[y[i - 1], x[i - 1]] -= energy_from_eat

    if energy[i] < 0.0:
        energy[i] = 0.0

    if food[y[i - 1], x[i - 1]] < 0.0:
        food[y[i - 1], x[i - 1]] = 0.0

    i += 1

plot_t_index = [11, 501, 1001, 5001]
plt.figure()

for j in range(4):
    plt.subplot(2, 2, j + 1)
    plt.plot(x[:plot_t_index[j]], y[:plot_t_index[j]], '-')
    plt.plot(x[0], y[0], 'og')
    plt.plot(x[plot_t_index[j] - 1], y[plot_t_index[j] - 1], 'xr')
    plt.title('Path after ' + str(plot_t_index[j] - 1) + ' steps')
    plt.axis([0, domain_shape[1], domain_shape[0], 0])

    if j >= 2:
        plt.xlabel('X-direction index')
    else:
        plt.xticks([])

    if (j % 2) == 0:
        plt.ylabel('Y-direction index')
    else:
        plt.yticks([])

plt.show()
