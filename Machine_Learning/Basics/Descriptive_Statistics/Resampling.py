#Lesson 7: Algorithm Evaluation With Resampling Methods

# Here we use resampling methods to split the training dataset up into subsets, some are used to train the model. The others are used to estimate the accuracy of the model.


#In this case we obtain a dataset from URL:http://archive.ics.uci.edu/ml/datasets/Abalone

#Abstract: Predict the age of abalone from physical measurements


import pandas

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

characteristics = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = pandas.read_csv(url, names=characteristics) # Read CSV (comma-separated) file into DataFrame

array = data.values # The dtype will be a lower-common-denominator dtype

# separate array in X and Y

X = array[:,1:8]   #All rows in all columns (1 to 8)
Y = array[:,8]     #All rows in column 8
 
#print(X)
#print(Y)

# Kfold provides train/test indices to split data in train/test sets. Split dataset into k consecutive folds 

kfold = KFold(n_splits=10, random_state=7) 




















