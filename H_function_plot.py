# This code will plot the H(mu) function with respect to mu in case of isotropic scattering.

import numpy as np, matplotlib.pyplot as plt
import sys as s
from H_isotropic_values import*


# Defining the value of single scattering albedo
omega_0 = 0.1
omega_1 = 1.0
title=["$\omega_0=0.1$","$\omega_0$=1"]
# Tabulating the values of mu
mu = np.arange(0.0,1.05,0.05)
# The values of H(mu) given in Chandrasekhar (1960) pg. 125
H_omg_pt1 = np.array([1.0, 1.00783, 1.01238, 1.01584, 1.01864, 1.02099, 1.02300, 1.02475, 1.02630, 1.02768, 1.02892, 1.03004, 1.03106, 1.03199, 1.03284, 1.03363, 1.03436, 1.03504, 1.03567, 1.03626, 1.03682])

H_omg_1 = np.array([1.0, 1.1368, 1.2474, 1.3508, 1.4503, 1.5473, 1.6425, 1.7364, 1.8293, 1.9213, 2.0128, 2.1037, 2.1941, 2.2842, 2.3740, 2.4635, 2.5527, 2.6417, 2.7306, 2.8193, 2.9078])

#print H_omg_1; s.exit(1)
#=======================================================
H_calc_omg_pt1 = H_iso(omega_0)
H_calc_omg_1 = H_iso(omega_1)
#=======================================================
fig, axes = plt.subplots(2,1)
plt.subplot(2,1,1)
plt.plot(mu,H_omg_pt1,".k",mu,H_calc_omg_pt1,"r-")
plt.gca().title.set_text(title[0])
plt.subplot(2,1,2)
plt.plot(mu,H_omg_1,".k",mu,H_omg_1,"r-")
plt.gca().title.set_text(title[1])
fig.tight_layout()
plt.xlabel("$\mu$")
plt.savefig("Isotrpic_H-Funtion_plot.jpg")
plt.show()
