# Lesson 6. Modelin Basics.

# Standardize data (0 mean, 1 stdev).
# Standardization of a dataset is a common requirement for many machine learning estimators: they might behave badly if the individual #feature do not more or less look like standard normally distributed data (e.g. Gaussian with 0 mean and unit variance).

#This example is obtained from: http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html 



from sklearn.preprocessing import StandardScaler


data = [[0, 3], [0, 3], [1, 1], [1, 1]] 

scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance

#print(data)

#print(scaler)

print(scaler.fit(data))

print(scaler.mean_) # The mean come from each column. In the example, the second column is: (3+3+1+1)/4 = 2

print(scaler.transform(data)) # Perform standardization by centering and scaling
                              # Show the variance data from the mean 0. The mean 0 is the center of the mean of scaler.mean


 


