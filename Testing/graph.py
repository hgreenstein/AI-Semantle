import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# create x-axis data
x = np.array([100*i for i in range(48)])

# create y-axis data
y = np.array([19, 26, 23, 29, 35, 28, 40, 43, 30, 30, 24, 34, 34, 37, 48, 47, 33, 29, 30, 31, 36, 27, 40, 34, 29, 33, 36, 43, 27, 40, 29, 41, 37, 43, 30, 31, 39, 40, 44, 32, 34, 31, 38, 43, 45, 41, 40, 30])

# define the function for the line of best fit
def linear_func(x, a, b):
    return a * x + b

# perform the curve fit
params, _ = curve_fit(linear_func, x, y)

# plot the data and line of best fit
plt.plot(x, y, 'o', label='data')
plt.plot(x, linear_func(x, *params), label='line of best fit')

# add labels and title
plt.xlabel("Range of games")
plt.ylabel("Number of games won")
plt.title("Trend of games won")

# display the graph
plt.legend()
plt.show()
