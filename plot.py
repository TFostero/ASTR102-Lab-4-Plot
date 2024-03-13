import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def hourToDeg(hour):
    return hour * (360 / 24)

def hourToRad(hour):
    return np.deg2rad(hourToDeg(hour))


data = pd.read_csv('lab3wedge.csv')

velocities = data['Vr']
declinations = hourToRad(data['Dec'])
declinations = (declinations * 2) - hourToRad(14)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(declinations, velocities)
ax.set_theta_offset(hourToRad(16))
ax.set_xticks(np.linspace(np.pi, 3 * np.pi / 2, 4))
ax.set_rmax(12000)
ax.set_rticks([2000, 4000, 6000, 8000, 10000, 12000])

radial_tick_labels = ['2000km/s', '4000km/s', '6000km/s', '8000km/s', '10000km/s', '12000km/s']
ax.set_yticklabels(radial_tick_labels)

ax.grid(True)

ax.set_thetamin(hourToDeg(10))
ax.set_thetamax(hourToDeg(18))

theta_ticks = np.linspace(hourToDeg(10), hourToDeg(18), 5)
theta_labels = ['12H', '13H', '14H', '15H', '16H']
ax.set_xticks(np.deg2rad(theta_ticks))
ax.set_xticklabels(theta_labels)

plt.savefig('wedge.png', dpi=200)
plt.show()

