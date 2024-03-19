import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def time2deg(hour, minute, second):
    return 360 * ((hour / 24) + (minute / (24 * 60)) + (second / (24 * 60 * 60)))


def time2rad(hour, minute, second):
    return np.deg2rad(time2deg(hour, minute, second))


data = pd.read_csv('lab3wedge.csv')

velocities = data['Vr']
declinations = time2rad(data['Hours'], data['Minutes'], data['Seconds'])
declinations = (declinations * 2) - time2rad(14, 0, 0)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(declinations, velocities, s=25)
ax.set_theta_offset(time2rad(16, 0, 0))
ax.set_xticks(np.linspace(np.pi, 3 * np.pi / 2, 4))
ax.set_rmax(12000)
ax.set_rticks([2000, 4000, 6000, 8000, 10000, 12000])

radial_tick_labels = ['2000km/s', '4000km/s', '6000km/s', '8000km/s', '10000km/s', '12000km/s']
ax.set_yticklabels(radial_tick_labels)

ax.grid(True)

ax.set_thetamin(time2deg(10, 0, 0))
ax.set_thetamax(time2deg(18, 0, 0))

theta_ticks = np.linspace(time2deg(10, 0, 0), time2deg(18, 0, 0), 5)
theta_labels = ['12H', '13H', '14H', '15H', '16H']
ax.set_xticks(np.deg2rad(theta_ticks))
ax.set_xticklabels(theta_labels)


plt.savefig('wedge.png', dpi=200)
plt.show()