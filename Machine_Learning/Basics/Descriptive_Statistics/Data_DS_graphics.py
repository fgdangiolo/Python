# Lesson 5. This data will be shape in a Graphics

# The variable "description" obtain the Description Statistics.


#In this case we obtain a dataset from URL:http://archive.ics.uci.edu/ml/datasets/Abalone


import pandas
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

characteristics = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = pandas.read_csv(url, names=characteristics)

scatter_matrix(data, alpha=0.8)

plt.show()
