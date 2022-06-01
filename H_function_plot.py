# This code will plot the H(mu) function with respect to mu in case of isotropic scattering.

import numpy as np, matplotlib.pyplot as plt
import sys as s
from H_isotropic_values import*


# Defining the value of single scattering albedo
omega_0 = 0.1
# Tabulating the values of mu
mu = np.arange(0.0,1.05,0.05)
# The values of H(mu) given in Chandrasekhar (1960) pg. 125
H_mu = np.array([1.0, 1.00783, 1.01238, 1.01584, 1.01864, 1.02099, 1.02300, 1.02475, 1.02630, 1.02768, 1.02892, 1.03004, 1.03106, 1.03199, 1.03284, 1.03363, 1.03436, 1.03504, 1.03567, 1.03626, 1.03682])

#=======================================================
H_mu_calc = H_iso(omega_0)

plt.plot(mu,H_mu,".k");
plt.plot(mu,H_mu_calc,"r-")
plt.xlabel("$\mu$");plt.ylabel("$H(\mu)$")
plt.legend(["Chandrasekhar(1960)","oztruck (2021)"])
plt.title("$\omega_0$= "+str(omega_0))
plt.show()
