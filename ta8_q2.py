#!/usr/bin/env python3
from math import exp

#define number of partitions for integration, lower limit, upper limit, step size
N = 10000
a=-10
b=10
h= (b-a)/N

#define value of ith x
def x(i):
    return a+i*h

#define function
def func(k):
    return exp(-k**2)

#function to integrate any function f
def integrator(f):
    sum = 0
    for i in range(N+1):
        if(i==0 or i==N):
            sum+=f(x(i))
        elif(i%2==0):
            sum+=2*f(x(i))
        else:
            sum+=4*f(x(i))
    sum = sum*h/3
    return sum

#finding value of 'A' using normalisation
A = 1/integrator(func)
print("value of A=", "%.5f" % A)

#define first moment and second moment
def first_moment(k):
    return k*A*exp(-k**2)

def second_moment(k):
    return k**2*A*exp(-k**2)

print("value of <x> =", "%.5f" % integrator(first_moment))
print("value of <x^2> =", "%.5f" % integrator(second_moment))
