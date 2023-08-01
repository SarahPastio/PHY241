"""
PHY 241 Homework 5
"""

from numpy  import copy,array,zeros,exp,pi,arange,append
import numpy as np
from pylab  import plot, xlabel,ylabel,show,legend,ylim,title

# set up Constants and variables
# ------------------------------------
L  = 1.0                  # length of string
v  = 300                  # velocity in wave equation (m/s)
N  = 100                  # Number of divisions in grid along the string
                        
dx = L/N                  # Grid spacing along the string
dt = 0.5*dx/v                 # Time-step
r  = 1             # parameter combination
r1 = 1.0
r2 = 1.0

x  = arange(N+1)*dx       # array for x coordinates ranging from 0 to L.
#print(x[1],x[2])
# intial displacement of the string y0
# ------------------------------------

y01 = 0.26795*x
y02 = 0.17633*(1-x)

y0 = np.concatenate((y01[:41],y02[41:]))
y0[0] = y0[N] = 0.0

#y001 = np.array(y01[:41])
#y002 = np.array(y02[41:])

#y0 = [0.        0.0026795 0.005359  0.0080385 0.010718  0.0133975 0.016077 0.0187565 0.021436  0.0241155 0.026795  0.0294745 0.032154  0.0348335 0.037513  0.0401925 0.042872  0.0455515 0.048231  0.0509105 0.05359 0.0562695 0.058949  0.0616285 0.064308  0.0669875 0.069667  0.0723465 0.075026  0.0777055 0.080385  0.0830645 0.085744  0.0884235 0.091103 0.0937825 0.096462  0.0991415 0.101821  0.1045005 0.10718   0.1040347  0.1022714 0.1005081 0.0987448 0.0969815 0.0952182 0.0934549 0.0916916 0.0899283 0.088165  0.0864017 0.0846384 0.0828751 0.0811118 0.0793485 0.0775852 0.0758219 0.0740586 0.0722953 0.070532  0.0687687 0.0670054 0.0652421 0.0634788 0.0617155 0.0599522 0.0581889 0.0564256 0.0546623 0.052899  0.0511357 0.0493724 0.0476091 0.0458458 0.0440825 0.0423192 0.0405559 0.0387926 0.0370293 0.035266  0.0335027 0.0317394 0.0299761 0.0282128 0.0264495 0.0246862 0.0229229 0.0211596 0.0193963 0.017633  0.0158697 0.0141064 0.0123431 0.0105798 0.0088165 0.0070532 0.0052899 0.0035266 0.0017633 0.       ]
#print(y01[:41],y02[41:])


# create arrays to store displacements at threee steps
#-------------------------------------
yp    = copy(y0)                  # prevous step y(:, n-1)
yc    = zeros(N+1,float)          # current step y(:, n)
yn    = zeros(N+1,float)          # next    step y(:, n+1)

# calculate  first yc, use Euler method
yc[1:N] = y0[1:N] + 0.5*r**2*(y0[2:N+1]+y0[0:N-1]-2.0*y0[1:N])


# Main loop
#-------------------------------------

#1: check r value
print("r = ", r)

#2: plot the initial wave, i.e., @ t=0
plot(x,y0, 'k-', linewidth = 2.0, label="t = %5.2f s"%(0.))


#3: calculate and plot yn at the different times.

times = arange(10,150,15)*dt   # time array
#times = arange(2,5)*1.0e-4
nstep = int(times[-1]/dt)+1    # number of steps in time.

for n in range(1,nstep) :

    # Calculate the new values of yn
    # fixed ends
    yn[1:N] = 2.0*(1-r**2)*yc[1:N] - yp[1:N] + r**2*(yc[2:N+1] + yc[0:N-1]) 

    # makes plots at given times
    for i in range(len(times)) :
        if abs(n*dt-times[i]) < dt/2. :
           plot(x, yn-1.0*(i+1), linewidth = 2.0, label="t = %5.2f ms"%(n*dt*1000))

    # copy yc -> yp, yn -> yc
    yp = copy(yc)
    yc = copy(yn)


title("Waves on a string with fixed ends")
xlabel("x (m)",fontsize=14)
ylabel("displacements y (m)",fontsize=14)
legend(loc='lower right')
show()

