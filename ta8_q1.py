#!/usr/bin/env python3
from math import sin


#define number of partitions for integration, lower limit, upper limit, step size
N = 10000
a=0
b=1
h= (b-a)/N

#define function sin(x)/x
def func(x):
    return 1 if x==0 else sin(x)/x

#define value of ith x
def x_i(i):
    return a+i*h


def trapezoidal_integral(f):
    #sum = h/2*( f(x(0))+2f(x(1))+..+2f(x(n-1))+f(n) )

    # in the fllowing code, we sum up f(x) based on value of i
    sum = 0
    for i in range(N+1):
        if (i==0 or i==N):
            sum+=f(x_i(i))
        else:
            sum+=2*f(x_i(i))
    sum = sum*h/2
    return sum


def simpson_integral(f):

    sum = 0
    for i in range(N+1):
        if(i==0 or i==N):
            sum+=f(x_i(i))
        elif(i%2==0):
            sum+=2*f(x_i(i))
        else:
            sum+=4*f(x_i(i))
    sum = sum*h/3
    return sum

def interpolation_rule(f):
    sum = 0
    for i in range(N+1):
        if(i==0 or i==N):
            sum+=f(x_i(i))
        elif(i%3==0 and i<=N-3):
            sum+=2*f(x_i(i))
        else:
            sum+=3*f(x_i(i))
    sum = sum*3*h/8
    return sum


print("value of integration using :")
print("trapezoidal rule ", "%.5f" % trapezoidal_integral(func))
print("simpson rule ", "%.5f" % simpson_integral(func))
print("interpolation method (n=3)", "%.5f" % interpolation_rule(func))