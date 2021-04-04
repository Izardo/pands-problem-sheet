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


'''
REFERENCES:

[1] "matplotlib.pyplot.plot" - matplotlib 
Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html [Accessed: 26/3/2021]
[2] "Style sheets reference" - matplotlib 
Available at: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html [Accessed: 30/3/2021]
[3] "Matplotlib Pyplot" - w3schools 
Available at: https://www.w3schools.com/python/matplotlib_pyplot.asp [Accessed: 26/3/2021]
[4] "Python Plotting With Matplotlib (Guide)" - Brad Solomon 
Available at: https://realpython.com/python-matplotlib-guide/ [Accessed: 28/3/2021]
[5] "How to change the font size on a matplotlib plot" - Herman Schaaf
Available at: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot [Accessed: 30/3/2021]
'''