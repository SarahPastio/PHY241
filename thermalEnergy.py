"""
PHY 241 Homework 7
"""

from gaussxw import gaussxwab, gaussxw
from numpy   import pi, exp, arange
from pylab   import plot, scatter, show, xlabel, ylabel, title


k = 1.38064852 * 10**-23    # Boltzman constant
c = 299792458               # speed of light
h = 1.054571817 * 10**-34   # hbar


# Perform the integral
def W(T,N) :
    # T = temperature, N = sampling grid number
    x,w = gaussxw(N)
    s = 0.0
    for i in range(N) :
        s += w[i] * (k * T)**4 * x[i] / (4 * (pi*c*h)**2 * (exp(x[i])-1))
    return s


# Plot W as a function of N
Npoints = []
Wpoints = []
for i in range(10,1000,10):
    Npoints.append(i)
    Wpoints.append(W(300,i))
    
scatter(Npoints,Wpoints)
xlabel("N number of chosen grid")
ylabel("W total thermal energy")
show()


# Plot W as a function of T
Tpoints = arange(10,1000,10)
WpointsT = []
for i in range(len(Tpoints)):
    WpointsT.append(W(Tpoints[i],100))

scatter(Tpoints,WpointsT)
xlabel("T temperature")
ylabel("W total thermal energy")
show()




