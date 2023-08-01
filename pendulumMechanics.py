# Computations Physics Homework 3
# Sarah Rogers-Pastio


from math  import cos,sin,sqrt,pi,exp
from numpy import arange, array, ones, zeros
from pylab import plot, subplot, show, title, legend, \
                  xlim, ylim, xlabel, ylabel, semilogy, scatter

#  define constants and variables
g      = 9.8            # accelleration due to gravity
length = 1.0            # string length (m)
mass   = 1.0            # mass (kg)
q      = 0.5
omega_D= 2/3
theta0 = 0.2
                 
dt     = 0.04           # time interval
t_end  = 100000.0           # stopping time (s)

N    = int(t_end/dt)  
time = arange(N)*dt



def calc_thetas(theta0, q, omega_D, F_D) :
    
    thetas = ones(N, float)*theta0
    omegas = zeros(N, float)
    energy = zeros(N, float)
    
    
    for i in range(N-1):
        # calculate the 2nd derivative of thetas
        f2 = -g*sin(thetas[i])/length - q*omegas[i] + F_D*sin(omega_D*time[i])
        f2_star = -g*sin(thetas[i]+omegas[i]*dt/2)/length - q*omegas[i] + F_D*sin(omega_D*(time[i]+dt/2))
        
        thetas[i+1] = thetas[i] + (omegas[i+1]+f2*dt/2)*dt
        omegas[i+1] = omegas[i] + f2_star*dt
        
    for i in range(N-1):
        # calculate energy
        energy[i] = .5*mass*length**2*(omegas[i]**2 + g*thetas[i]**2/length)
    
    # plotting
    period = 2*pi*sqrt(length/g)        # period of the pendulum (s)
    
    subplot(121)
    title("Pendulum theta v time")
    xlabel("time  (s)")
    ylabel("Oscillating theta (degrees)")    
    ymin = min(thetas)-0.2*abs(min(thetas))
    ymax = max(thetas)+0.2*abs(max(thetas))
    for i in range(int(t_end/period)):
        plot([(i+1)*period,(i+1)*period],[ymin, ymax],"r:")
    plot(time,thetas,"b-")

    
    subplot(122)
    title("Pendulum energy v time")
    xlabel("time (s)")
    ylabel("Total energy (J)") 
    ymin = min(energy)-0.2*abs(min(energy)) 
    ymax = max(energy)+0.2*abs(max(energy))
    for i in range(int(t_end/period)):
        plot([(i+1)*period,(i+1)*period],[ymin, ymax],"r:")
    plot(time,energy,"b-")
    ylim(ymin,ymax)
    
    show()
    
    
    
def calc_theta_v_omega(theta0, q, omega_D, F_D):
   thetas = ones(N, float)*theta0
   omegas = zeros(N, float)

   for i in range(N-1):
       # calculate the 2nd derivative of thetas
       f2 = -sin(thetas[i]) - q*omegas[i] + F_D*sin(omega_D*time[i])
          

       # Euler-Cromer method
       omegas[i+1] = omegas[i] + f2*dt
       thetas[i+1] = thetas[i] + omegas[i+1]*dt
       
       
       # if angle is out of the range [-pi, pi], add or subtract 2pi to keep 
       # the angle in this range
       #
       if thetas[i+1] > pi :
          thetas[i+1] -= 2*pi
       if thetas[i+1] < -pi :
          thetas[i+1] += 2*pi
       
   return [thetas, omegas]



def draw_theta_v_omega():
    
    x1 = calc_theta_v_omega(theta0,q,omega_D, 0.5)   #F_D=0.5
    x2 = calc_theta_v_omega(theta0,q,omega_D, 1.2)   #F_D=1.2
     

    title("$\omega$ versus $\\theta$  Fd=0.5")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x1[0],x1[1],s=1)
    xlim(-1,1)
    ylim(-1,1)
    show()

    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x2[0],x2[1],s=1)
    ylim(-3,3)
    xlim(-4,4)
    

    show()
        


def poincare_plot():
    x1 = calc_theta_v_omega(theta0,q,omega_D, 0.5)
    x2 = calc_theta_v_omega(theta0,q,omega_D, 1.2)
    
    title("$\omega$ versus $\\theta$  Fd=0.5")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x1[0],x1[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()
    
    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x2[0],x2[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()



def poincare_plot_shifted():
    x1 = calc_theta_v_omega(theta0,q,omega_D, 0.5)
    x2 = calc_theta_v_omega(theta0,q,omega_D, 1.2)
    
    title("$\omega$ versus $\\theta$  Fd=0.5")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x1[0],x1[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()
    
    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x2[0],x2[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()



def chaotic_attractor():
    x0 = calc_theta_v_omega(0.0,q,omega_D, 0.5)
    x1 = calc_theta_v_omega(0.5,q,omega_D, 0.5)
    x2 = calc_theta_v_omega(0.7,q,omega_D, 0.5)
    x3 = calc_theta_v_omega(0.9,q,omega_D, 0.5)
    x4 = calc_theta_v_omega(1.0,q,omega_D, 0.5)
    
    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x0[0],x0[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()
    
    title("$\omega$ versus $\\theta$  Fd=0.5")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x1[0],x1[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()
    
    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x2[0],x2[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()

    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x3[0],x3[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()

    title("$\omega$ versus $\\theta$  Fd=1.2")
    xlabel("$\\theta$ (radians)")
    ylabel("$\omega$ (rad/s)")
    scatter(x4[0],x4[1],s=1)
    ylim(-2,1)
    xlim(-4,4)
    show()



chaotic_attractor()





