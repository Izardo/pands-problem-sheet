# This program creates a plot of the following 3 functions:
# f(x) = x, g(x) = x^2, h(x) = x^3

# Author: Isabella Doyle

# imports numpy and matplotlib for creating an array and plot respectively
import numpy as np
import matplotlib.pyplot as plt

# selects graphical style for plot
plt.style.use('ggplot')

# x-axis value range
x = np.array([0, 1, 2, 3])  # uses numpy to create a multi-dimensional array of x-axes values

# y-axis values
y1 = x          # f(x) = x
y2 = x ** 2     # g(x) = x^2
y3 = x ** 3     # h(x) = x^3

# plots the values on the y-axes
plt.plot(y1,label='f(x) = x')
plt.plot(y2,label='g(x) = x^2')
plt.plot(y3,label='h(x) = x^3')

# add labels for x and y axes and sets font-size
plt.xlabel('x-axis', fontsize=8)
plt.ylabel('y-axis', fontsize=8)

# adds a plot title and sets font-size
plt.title('Plot of functions: f(x) = x, g(x) = x^2, h(x) = x^3', fontsize=10)

# adds legend to plot and sets padding
plt.legend(loc='upper left', borderaxespad=2)

# saves the plot figure
plt.savefig('myPlot.jpg')

# displays the plot figure
plt.show()