from numpy import empty,zeros,max
from pylab import imshow,gray,show,colorbar,contour
import timeit

# Constants
M = 100		# Grid squres on a sid
target = 1e-6   # Target accuracy
alpha = 1.9     # SOR mixing parameter


eps0 = 1.0      # the permittivity of empty sapce
h = 100/M           # grid spacing

# Create arrays to hold potential values
phi     = zeros([M+1,M+1],float)


# Create array to hold charge density
rho = zeros([M+1,M+1], float)
for i in range(M+1) :
    for j in range(M+1) :
        if j == 20 and 20<i<80:
            rho[i][j] = 2.0
        if j == 80 and 20<i<80:
            rho[i][j] = -2.0

start = timeit.default_timer()

# Main loop
delta = 1.0
iterations = 1
while delta > target:
     
    delta_max = 0.0
    # Calculate new values of the potential
    for i in range(1,M):
        for j in range(1,M):
 
            phi_star = (phi[i+1,j] + phi[i-1,j] + \
                        phi[i,j+1] + phi[i,j-1])/4 + \
                        rho[i][j]*h**2/4./eps0
            delta_phi = alpha*(phi_star-phi[i,j])
            phi[i,j]  = delta_phi + phi[i,j]

            if abs(delta_phi) > delta_max :
                delta_max = abs(delta_phi)
                
    # Calculate maximum difference from old values
    delta = delta_max

  
    iterations += 1
    if iterations%100 == 0 :
       print("...  iteration #%d ..." %(iterations))

time = timeit.default_timer()-start
print("Total Computing Time:%7.2f seconds; Total iterations: %d" %(time, iterations))

# Make a plot
contour(phi)
imshow(phi)
colorbar()
show()
