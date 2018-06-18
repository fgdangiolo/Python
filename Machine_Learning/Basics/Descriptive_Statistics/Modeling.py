# Lesson 6. Prepare For Modeling by Pre-Processing Data

# Standardize data (0 mean, 1 stdev).
# Standardization of a dataset is a common requirement for many machine learning estimators: they might behave badly if the individual #feature do not more or less look like standard normally distributed data (e.g. Gaussian with 0 mean and unit variance).

#In this case we obtain a dataset from URL:http://archive.ics.uci.edu/ml/datasets/Abalone

#Abstract: Predict the age of abalone from physical measurements


import pandas
import numpy

from sklearn.preprocessing import StandardScaler


url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

characteristics = ['Sex','Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = pandas.read_csv(url, names=characteristics) # Read CSV (comma-separated) file into DataFrame

array = data.values # The dtype will be a lower-common-denominator dtype

# separate array in X and Y

X = array[:,1:8]   #All rows in all columns (1 to 8)
Y = array[:,8]     #All rows in column 8
 
#print(X)
#print(Y)

#print(data)

scaler = StandardScaler().fit(X) # Standardize features by removing the mean and scaling to unit variance

#print(scaler.mean_) # The mean come from each column. 

mean_center=scaler.mean_  # The mean value for each feature in the training set.

rescalerX = scaler.transform(X)  # Perform standardization by centering and scaling

#print(rescalerX)

numpy.set_printoptions(precision=3) # These options determine the way floating point numbers, arrays and other NumPy objects are displayed.


print('Mean_center')
print(mean_center)

print('Variance')
print(rescalerX[0:8,:])

print('Data')
print(array[0:8,1:])








