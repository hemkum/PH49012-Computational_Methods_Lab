#!/usr/bin/env python3

import sys

print("  ---enter value of a,b,c,d separated by spaces---  ")
for i in range(1, len(sys.argv)):
	sys.argv[i]=float(sys.argv[i])
[null,a,b,c,p,q,r]=sys.argv
x=(b*r-c*q)/(p*b-q*a)
y=(p*c-a*r)/(p*b-q*a)
print("solution for equations ax+by=c and px+qy=r")
print("x=",x)
print("y=",y)

