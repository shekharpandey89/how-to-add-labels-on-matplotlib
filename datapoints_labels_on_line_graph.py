# datapoints_labels_on_line_graph.py

# import the required packages
import matplotlib.pyplot as plt
import numpy as np

# import the clf () method to draw the another graph on the same graph window
plt.clf()

# dummy dataset from numpy
x_values = np.arange(0,10,1)
y_values = np.random.normal(loc=2, scale=0.2, size=10)

plt.plot(x_values,y_values,marker='D', mfc='green', mec='yellow',ms='7')

# zip joins x and y coordinates in pairs
for x,y in zip(x_values,y_values):

    label = "{:.3f}".format(y)

    plt.annotate(label, # this is the value which we want to label (text)
                 (x,y), # x and y is the points location where we have to label
                 textcoords="offset points",
                 xytext=(0,10), # this for the distance between the points
                 # and the text label
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))

plt.show()