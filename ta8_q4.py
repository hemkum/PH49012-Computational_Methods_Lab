#!/usr/bin/env python3
import numpy as np
from math import cos

# define x limimts, y limits and step size
yl,yh,xl,dx,dy=0,2,0,0.001,0.001

# define lower y limit as function of x
def xh(y):
    return 2*pow(y,0.5)

# integrand 
def func(x,y):
    return 5*x**3*cos(y**3)

#double nested loop to go over each x,y pair and add f(x,y) to sum
sum = 0
for y in np.arange(yl,yh,dy):
    for x in np.arange(xl,xh(y),dx):
        sum = sum + func(x,y)

#multiple sum by dx*dy to get value of integration 
sum = sum*dx*dy

print("value of double integral is ", "%.3f" % sum)