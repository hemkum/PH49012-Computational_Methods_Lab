import matplotlib.pyplot as plt
xo,xf,dx, yo = 1,2,0.1,5
N=int((xf-xo)/dx)
y=[None]*(N+1)
x=[None]*(N+1)
x,y= [xo], [yo]
while xo <= xf:
	k1 = dx*xo*yo
	k2 = dx*(xo+dx)*(yo+k1)
	yo += 1/2*(k1+k2)
	xo += dx
	x.append(xo)
	y.append(yo)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)
plt.savefig('a3q12.png')
plt.show()

