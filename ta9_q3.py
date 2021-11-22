import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

t0=0    #initial time
tn=5   #final time
n=500  #steps 
dt=(tn-t0)/n    #step size
D=1     #diffusion constant

# initialise (rx,ry) as (0,0)
rx=[0]  
ry=[0]

# rx(i+1) = rx(i) + sqrt(D) * dt * G(i)
for i in range(n):
    rx.append(rx[i]+sqrt(D)*dt*np.random.randn())
    ry.append(ry[i]+sqrt(D)*dt*np.random.randn())
plt.title("brownian particle diffusing in fluid medium")
plt.plot(rx,ry, marker=">", linestyle="--")
plt.show()