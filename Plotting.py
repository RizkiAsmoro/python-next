'''
Plotting - Basic Pyplot

'''
#Plotting using x and y points
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0,6])
ypoint = np.array([0,50])

plt.plot(xpoint, ypoint)
plt.show()