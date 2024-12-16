"""
=====================================
Convert slk exported laser data to csv
======================================
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from manchester_lab import slk_to_csv

# convert from .slk to .csv
path_slk = os.path.join("data", "test_laser.slk")
slk_to_csv(path_slk)

# read csv
path_csv = os.path.join("data", "test_laser.csv")
data = np.loadtxt(path_csv, delimiter=",")

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(data[:, 0], data[:, 1])
ax.set_xlabel("x [mm]")
ax.set_ylabel("y [mm]")
plt.show()
