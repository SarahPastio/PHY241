"""
PHY 241 Homework 10
"""

from numpy import loadtxt
from numpy.fft import rfft,irfft
from scipy.fft import dct,idct
from pylab import plot,show,subplot,legend

cutoff = 0.02

# Load and plot the data 
y = loadtxt("dow2.txt",float)

#subplot: unaltered dow2 file
plot(y,"c-", label="Dow (original file)") 


#-------- Fourier --------


# Calculate Fourier transform 
transform = rfft(y)

# Smoothing
ncut = int(cutoff * len(y))
transform[ncut:] = 0.0

# inverse FT 
ynewFT = irfft(transform)

plot(ynewFT,"r-", label="Fast Fourier")
legend()
show()


#-------- Cosine --------


#subplot: unaltered dow2 file
plot(y,"c-", label="Dow (original file)")

# Calculate Cosine Transform 
transform = dct(y)

# Smoothing
ncut = int(cutoff * len(y))
transform[ncut:] = 0.0

# inverse CT 
ynewCT = idct(transform)

plot(ynewCT,"b-", label="Fast Cosine")
legend()
show()
