import matplotlib.pyplot as plt
import numpy as np

# define gaussian distribution parameters sigma= standard ddeviation and mu = mean
sigma = 0
mu = 1

#generate 5*10^4 random numbers from gaussian distribution
x=np.random.normal(sigma, mu, size=5*10**4)

# generate a histogram using x and store it as an array of 100 bins in bins variable
count, bins, ignored = plt.hist(x,100,density=True)

# plot the density funtion after defining it as a function of mu, sigma and bins
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp( -(bins-mu)**2 / (2*sigma**2) ), linewidth=2, color='r' )
plt.title("Gaussian probability distributions")
plt.show()