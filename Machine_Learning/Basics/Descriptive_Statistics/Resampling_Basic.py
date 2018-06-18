#Lesson 7: Algorithm Evaluation With Resampling Methods.

#This example is in: http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html

# Here we use resampling methods to split the training dataset up into subsets, some are used to train the model. The others are used to estimate the accuracy of the model.

import numpy as np

from sklearn.model_selection import KFold

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])

Y = np.array([1, 2, 3, 4])

print(X)

#print(Y)

kf = KFold(n_splits=5) # Number of folds. Must be at least 2

#print(kf)

print(kf.get_n_splits(X)) #Returns the number of splitting iterations in the cross-validator





















