from gaussxw import gaussxwab
from pylab   import plot,xlabel,ylabel,show,legend,ylim,title,imshow,contour,colorbar
from math    import pi,cos,sin,sqrt
from numpy   import zeros

#---- CONSTANTS ----

lmbda = 500             # light wavelenght in nm
k     = 2*pi /lmbda     # wave number


###########################################################
#               PART ONE: Calculate J(m,x)
###########################################################

def f(m, x, theta) :
    f = cos(m*theta-x*sin(theta))
    return f

"""           Gauss Quadrature Method
I chose to use the Gauss Quadrature method because of the 
high level of accuracy it provides.
This method assigns weights (w) mapped to components of the 
function (f[x]) and sums those combined values w[i]*f[x]
"""
def J(m,x):
    N = 20              # grid point number
    theta,w = gaussxwab(0,pi,N)
    
    j = 0.
    for i in range(N): 
        j += w[i]*f(m,x,theta[i])
    
    return j/pi

###########################################################
#      PART TWO: Plot J_0, J_1, J_2 from x = 0 to 20
###########################################################

j0 = []
j1 = []
j2 = []
x  = []
for i in range(21):
    j0.append(J(0,i))
    j1.append(J(1,i))
    j2.append(J(2,i))
    x.append(i)

plot(x,j0, label="j0")
plot(x,j1, label="j1")
plot(x,j2, label="j2")

title("J_0, J_1, J_2 for x in range (0,20)")
xlabel("x")
ylabel("J(m,x)")
legend()
show()

###########################################################
#               PART THREE: Density Plot
###########################################################

def I(r):
    I = (J(1,k*r)/(k*r))**2
    return I

N = 40

intensity = zeros([N,N],float)

for x in range(N):
    for y in range(N):
        if x == N/2 and y == N/2:
            intensity[x,y] = 1/2
        else:
            x_r = abs(x-N/2)*50
            y_r = abs(y-N/2)*50
            r = sqrt(x_r**2 + y_r**2)
            intensity[x,y] = I(r)

# note about the scale: the plot has 40x40 points with the x and y 
# values scaled by 50 nm to find the value of r
            
contour(intensity, cmap="Spectral")
imshow(intensity,vmax=0.01)
colorbar()
xlabel("x position (in 50 nm)") 
ylabel("y position (in 50 nm)")
show()











