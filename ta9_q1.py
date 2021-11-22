import matplotlib.pyplot as plt
import numpy as np

#generate a 1D array of random numbers of size=1000
x=np.random.rand(10000)

#bins denote number of columns
plt.hist(x, density=True, bins=100)  # `density=False` would make counts
plt.ylabel('Probability')
plt.xlabel('Data');

plt.show()