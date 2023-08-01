"""
PHY 241 Homework 6
github.com/akels/ComputationalPhysics was used as a resource
"""

from gaussxw import gaussxw
from numpy   import arange, array, tan, cos, pi, exp
from pylab   import plot, show, xlabel, ylabel, title

V      = 1000                     # volume in cm^3
rho    = 6.022 * 10**28           # number density of atoms
kB     = 1.38064852 * 10**(-23)   # Boltzmann’s constant
thetaD = 428                      # Debye temperature

N = 50    # Number of sample points
T = 5

x,w = gaussxw(N)


def f(x) :
    return (x**4 * exp(x))/(exp(x)-1)**2
    

def cv(T):
    a = thetaD/T
    b = 0
    
    C = 9*V*rho*kB*(T/thetaD)**3
    
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    s = sum(C*f(xp)*wp)
    
    return s


T  = arange(5, 500, 20)
CV = [cv(Ti) for Ti in T] 

plot(T, CV)

xlabel('Temperature, K')
ylabel('C_v')
show()
    


