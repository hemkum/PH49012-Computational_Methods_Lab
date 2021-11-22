import matplotlib.pyplot as plt
a,b,dx, y0 = 1,2,0.1,5 # intilise bounds are a,b, intial value of y is y0 and step size is dx
N=int((b-a)/dx) # find number of iterations
y=[None]*(N+1) #initilise empty array of fixed size
x=[None]*(N+1)
y[0]=5 # define first element of y 
x[0]=a
    
for i in range(1,N+1): #loop over all x(i)
	x[i-1]=a+dx*(i-1)
	y[i]=y[i-1]+dx*x[i-1]*y[i-1]
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)
plt.savefig('a3q11.png')
plt.show()
