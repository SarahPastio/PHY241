from math import exp
from random import random
from pylab import plot,subplot,bar,show, \
     xlabel, ylabel, xlim,ylim,fill_between
from numpy import arange, array, linspace

N = 1000000

def f(x):
    return x**(-.5)/(exp(x)+1)

def p():
	x = 2*random()
	return 1/(2*x**.5)

def mcint(N) :
    count = 0
    for i in range(N):
        # define points using random
        x = 2*random()
        y = random()
        if  y < f(x) :
            count += 1

    return 2*count/N


"""
 main
"""

x = []
for i in range(N):
    x.append(p())
x.sort()
y = list(map(f,x))

plot(x,y)
xlim(0,10)
fill_between(x,y, color='green', alpha=0.3)
show()

I = mcint(1000000)
print(I)

