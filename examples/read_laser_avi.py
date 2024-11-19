"""
=======================
Read the laser avi data
=======================
"""

import matplotlib.pyplot as plt
from manchester_lab import laseravi_to_npy

file_path = "TestExperiment.avi"
data = laseravi_to_npy(file_path)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(data[10, :, 0], data[10, :, 1])
ax.plot(data[200, :, 0], data[200, :, 1])
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
