# Lesson 4. DataFrame will be shape in a Graphics

# The variable "description" obtain the Description Statistics.


#Load text file from URL. The variable "description" obtain the Description Statistics

#In this case we obtain a dataset from URL:http://archive.ics.uci.edu/ml/datasets/Abalone


import pandas

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

characteristics = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = pandas.read_csv(url, names=characteristics)

description = data.describe()

print(description)


