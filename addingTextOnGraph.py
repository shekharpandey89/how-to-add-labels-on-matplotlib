# addingTextOnGraph.py
import matplotlib.pyplot as plt
import numpy as np

plt.clf()
# using some dummy data for this example
x_value = np.arange(0,15,1)
print("x_value",x_value)
y_value = np.random.normal(loc=2.0, scale=0.9, size=15)
print("y_value",y_value)

plt.plot(x_value,y_value)

# default text will be left-aligned
plt.text(1,3,'This text starts at x=1 and y=3')

# this text will be right-aligned
plt.text(6,2,'This text ends at x=6 and y=2',horizontalalignment='right')

plt.show()