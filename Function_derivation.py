# In this code we find the basic relations used in the paper Link: https://www.sciencedirect.com/science/article/pii/S0022407321002570
# We use sympy package to recalculate the expressions given in the paper.

import sympy as syp
import sys as s

# Assigning symbols
mu, A0, A1, omega = syp.symbols("mu A0 A1 omega")

# Following are the shifted legendre polynomials; shifting from mu to (2*mu-1) and orthogonal in the range of 0 to 1
P0 = syp.legendre_poly(0,x=2*mu-1)
P1 = syp.legendre_poly(1,x=2*mu-1)

# Legendre polynomial of second kind for Q_n(2*mu+1)
Q0 = 1./2 * syp.ln((mu +1)/mu) 
Q1 = 1./2 * (2*mu+1) * syp.ln((mu +1)/mu) - 1 

# Series expansion of S



S = A0 * Q0 - 3 * A1 * Q1



# Following is the equation satisfied by A0
integrand_0 = 1./(1 - omega * mu * S )
a0 = A0 - syp.integrate(integrand_0,(mu,0,1)) - 2

# Following is the equation satisfied by A1
integrand_1 = (2*mu + 1)/(1 - omega * mu * S )
a1 = A1 - syp.integrate(integrand_1,(mu,0,1))




