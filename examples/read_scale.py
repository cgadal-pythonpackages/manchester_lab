"""
=======================
Read the scale data
=======================
"""

import os

import matplotlib.pyplot as plt
from manchester_lab import read_scalefile_gtkterm
from scipy.ndimage import gaussian_filter1d

file_path = os.path.join("data", "test_scale.dat")
time, mass_data = read_scalefile_gtkterm(file_path)

fig, axarr = plt.subplots(2, 1, layout="constrained", sharex=True)
axarr[0].plot(time, mass_data)
axarr[1].plot(time, gaussian_filter1d(mass_data, sigma=5, order=1) / (time[1] - time[0]))
axarr[0].set_ylabel("mass [g]")
axarr[1].set_ylabel("mass flux [g/s]")
axarr[1].set_xlabel("time [s]")

plt.show()
