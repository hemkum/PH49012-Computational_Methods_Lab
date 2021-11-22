import matplotlib.pyplot as plt
xo,xf,h, yo = 1,2,0.1,5
N=int((xf-xo)/h)
y=[None]*(N+1)
x=[None]*(N+1)
x,y= [xo], [yo]
while xo <= xf:
	k1 = h*xo*yo
	k2 = h*(xo+h/2)*( yo+k1/2)
	k3 = h*(xo+h/2)*(yo+k2/2)
	k4 = h*(xo+h)*(yo+k3)
	yo += 1/6*(k1+2*k2+2*k3+k4)
	xo += h
	x.append(xo)
	y.append(yo)


plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)
plt.savefig('a3q13.png')
plt.show()


