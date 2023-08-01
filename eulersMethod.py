"""
Created on Tue Feb  8 19:27:04 2022

@author: Sarah Rogers-Pastio
"""

from math  import cos,sin,sqrt,pi,exp
from numpy import arange, array
from pylab import plot, subplot, show, title, legend, xlim, ylim, xlabel, ylabel


# constants

a = 0.0065      # Temp in K/m
T0 = 300        # Ground temperature
alpha = 2.5

R = 0.08        # Radius in meters
C = 0.47        # Coefficient of drag
rho = 1.22      # Air density
m  = 1                 # mass in kg

B = pi * R**2 * rho * C / (2 * m)

g  = 9.8               # gravity acceleration (m/s2)
dt = 0.01              # time interval in seconds


# define variables
t = 0
rx = []                # array storing x-positions
ry = []                # array storing y-positions

x,y = 0.0, 0.0         # initial position

theta *= pi/180        # unit converting: degree to radian
vx = v0 * cos(theta)   # calculate the intitial velocity along x 
vy = v0 * sin(theta)   # calculate the intitial velocity along y

# Euler's method
while y >= 0:
    
    rx.append(x)
    ry.append(y)
    
    v = sqrt(vx**2+vy**2)
    
    vx = vx - B * v * vx * dt / m
    x  = rx[-1] + vx*dt
    
    vy = vy - g*dt - B * v * vx * dt / m
    y  = ry[-1] + vy*dt

    t  = t + dt

print( [rx, ry]  )
