#!/usr/bin/env python3
import numpy as np

# define x limimts, y limits and step size
xl,xh,yh,dx,dy=0,4,6,0.002,0.002

# define lower y limit as function of x
def yl(x):
    return (x-2)**2

# integrand 
def func(x,y):
    return (542*y**2-12*x)

#double nested loop to go over each x,y pair and add f(x,y) to sum
sum = 0
for x in np.arange(xl,xh,dx):
    for y in np.arange(yl(x),yh,dy):
        sum = sum + func(x,y)

#multiple sum by dx*dy to get value of integration 
sum = sum*dx*dy

print("value of double integral is ", "%.3f" % sum)