'''
Explore a quadratic fucntion visually
If y = x^2 + 2x + 1
Calculate y for 10 different values of x
Show the relationship of y to x visually by using a graph
'''

import matplotlib.pyplot as plt

# Assume values of x
x_values = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
y_values = [(x**2+2*x+1) for x in x_values]

plt.plot(x_values, y_values, marker='o')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Y as a Function of X')
plt.show()
