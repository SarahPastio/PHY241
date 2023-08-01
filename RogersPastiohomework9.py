from random import random
from math   import log
from numpy  import arange, sort, empty, arange
from pylab  import plot,xlabel,ylabel,show,legend


tauPb = 3.3*60           # Half life of lead in seconds
tauTl = 3.053*60         # Half life of thallium in seconds
tauBi = 46*60            # Half life of Bismoth in seconds

h = 1.0                  # Size of time-step in seconds

pPb = 1 - 2**(-h/tauPb)  # Probability of decay of Pb in one step
pTl = 1 - 2**(-h/tauTl)  # Probability of decay of Tl in one step
pBi = 1 - 2**(-h/tauBi)  # Probability of decay of Bi in one step

tmax = 25000             # Total time seconds

muPb    = log(2)/tauPb
muTl    = log(2)/tauTl
muBi213 = log(2)/tauBi

NBi213 = 10000           # Number of Bi 213 atoms
NPb    = 0               # Number of lead atoms
NTl    = 0               # Number of thallium atoms
NBi209 = 0               # Number of Bi 209 atoms

tpoints = arange(0.0,tmax,h)
Bi213points = []
Tlpoints    = []
Pbpoints    = []
Bi209points = []


for t in tpoints:
    Bi209points.append(NBi209)
    Pbpoints.append(NPb)
    Tlpoints.append(NTl)
    Bi213points.append(NBi213)
    
    # Calculate the number of atoms that decay from Lead
    decay = 0
    for i in range(NPb):
        if random() < pPb:
            decay += 1
    
    NPb    -= decay
    NBi209 += decay
    
    # Calculate the number of atoms that decay from Thallium
    decay = 0
    for i in range(NTl):
        if random() < pTl:
            decay += 1
    
    NTl -= decay
    NPb += decay
    
    # Calculate the number of atoms that decay from Bismoth
    decayTl = 0
    decayPb = 0
    for i in range(NBi213):
        if random() < pBi:
            if random() >= 0.0209:
                decayTl += 1
            else:
                decayPb += 1
    
    NBi213 -= decayTl
    NTl    += decayTl
    
    NBi213 -= decayPb
    NPb    += decayPb
    


#    
# Generate Plots
#

plot(tpoints, Bi209points, label="Bi 209")
plot(tpoints, Pbpoints, label="Pb 209")
plot(tpoints, Tlpoints, label="Tl 209")
plot(tpoints, Bi213points, label="Bi 213")



xlabel("Time")
ylabel("Number of atoms")
legend()
show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        