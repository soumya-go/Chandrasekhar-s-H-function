"""# This code is developed according to the formalism given in https://www.sciencedirect.com/science/article/pii/S0022407321002570
# This is to determine the value of H(mu) numerically.
# The final results show the values of H-function according to different mu and omega. 
# N express the upper limit of the expansion of the summation given in eqn.(17) in the paper.
"""


import numpy as np
import sys


# Defining omega
omega1 = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.8,0.9,1.0])

def H_iso(omega): 
        # Determining A_0(omega)
        def A0(omg):
                return (2./omg)*(1-np.sqrt(1-omg))  # Eqn. (21) of the paper.

        # Legendre function of second kind Q_0 
        def Q0(x):
                y = (x+1)/float(x-1) # this is followed from Arfken
                return 0.5*np.log(y)
                
        # Legendre function of second kind Q_0 
        def Q1(x):
                y = (x+1)/float(x-1)
                return 0.5*x*np.log(y) - 1



        mu = np.arange(0.0,1.05,0.05)        
        x= 2*mu+1

        ####### Calculation for N=0 #########
        n=0
        def S0(m,omg):
                return (2*n+1)*(-1)**n*A0(omg)*Q0(2*m+1)        # Eqn.(17) for N=0

        def H(m,omg):
                return 1./(1-omg*m*S0(m,omg))                    # Eqn.(18)   

        ####### Calculation for N=1 #########
        def A1(omg):
                R = 100-200*omg*(3-4*np.log(2))*A0(omg) + 10*omg**2*(185-532*np.log(2)+384*(np.log(2))**2)*A0(omg)**2
                a = 10.*(omg*A0(omg)*(3-4*np.log(2))-1)+np.sqrt(R)
                b = 6*omg*(28*np.log(2)-19)
                return  a/float(b)         # Eqn. (A7) of the paper.

        def S1(m,omg):
                return S0(m,omg)-3*A1(omg)*Q1(2*m+1)        # Eqn.(17) for N=1


        def H1(m,omg):
                return 1./(1-omg*m*S1(m,omg))                    # Eqn.(18) 
                
        H1 = np.vectorize(H1)
        return np.array([1.00000]+list(H1(mu[1:],omega))) # Here we manually add H(mu=0) = 1.0000 as mu=0 gives a zero division error.
                  
        """    
        for j in range(len(omega)):
                print "omega=",omega[j]
                print "mu\t\tH(N=0)\t\tH(N=1)\n"
                for i in range(1,len(mu)):
                        print np.round(mu[i],2),"\t\t",np.round(H(mu[i],omega[j]),5),"\t",np.round(H1(mu[i],omega[j]),5)     
                print "-"*60
        """

if __name__ == "__main__":
        omega=omega1[0]
        print H_iso(omega)
#for i in range(1,len(mu)):
#                print np.round(mu[i],2),"\t\t\t",np.round(H1(mu[i],omega),5)     




