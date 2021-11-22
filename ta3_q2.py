import matplotlib.pyplot as plt
import math
def Dy(t,y): # derivative of y wrt to t
    return y-t**2+1

def rk4(Dy=Dy, y0=0.5, t0=0, tf=2, h=0.1): #rk4 function
    t,y=[t0],[y0] #initialsing lists with first x0,y0 pair
    while t0<=tf: 
        k1 = h*Dy(t0, y0)
        k2 = h*Dy(t0+h/2, y0+k1/2)
        k3 = h*Dy(t0+h/2, y0+k2/2)
        k4 = h*Dy(t0+h, y0+k3)
        y0 += (1/6)*(k1+2*k2+2*k3+k4)     
        t0+=h
        t.append(t0)
        y.append(y0)
    return t, y

def analytical_solution(t0=0,tf=2,h=0.1):# function to find y(t) at interval of h steps
    y_actual=[]
    while t0 <=tf:
        y0= t0**2+2*t0+1-0.5*math.exp(t0)
        t0+=h
        y_actual.append(y0)
    return y



t,y = rk4()
y_actual = analytical_solution()

plt.xlabel('t')
plt.ylabel('y')
plt.plot(t,y,'g^',t,y_actual,'r--') # plot t,y with -- and plot t, y_actual with triangles
plt.savefig('a3q2.png')
plt.show()

