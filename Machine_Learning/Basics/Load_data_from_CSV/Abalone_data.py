#Load text file from URL

#In this case we obtain a dataset from URL:http://archive.ics.uci.edu/ml/datasets/Abalone

#Abstract: Predict the age of abalone from physical measurements


import pandas

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

characteristics = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = pandas.read_csv(url, names=characteristics)

print(data)


