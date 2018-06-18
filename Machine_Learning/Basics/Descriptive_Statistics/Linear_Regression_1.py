# Simple Linear Regression for data of distance and time of a car. The velocitiy is estimated based
# of distance and time. The data is separated in train and test

# This example was based on: http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


time = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
distance = [10,22,29,41,52,57,70,81,89.5,100.1,111,120.2,133,139,151,160.3]

time_X_train = time[0:9] # The first ten numbers  
time_X_test = time[-7:]  # The last ten numbers

distance_y_train = distance[0:9] # The first ten numbers
distance_y_test = distance[-7:] # The last ten numbers

#print(time_X_train)
#print(time_X_test)

#print(distance_y_train)
#print(distance_y_test)


# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(np.reshape(time_X_train, (-1, 1)), np.reshape(distance_y_train, (-1, 1)))

# Make predictions using the testing set
distance_y_pred = regr.predict(np.reshape(time_X_test, (-1, 1)))

# The coefficients
print('Coefficients are:', regr.coef_)

# Plot outputs
plt.scatter(time_X_test, distance_y_test,  color='red')
plt.plot(np.reshape(time_X_test, (-1, 1)), np.reshape(distance_y_pred, (-1, 1)), color='blue', linewidth=3)

plt.title('Distance vs Time', fontsize=20)
plt.xlabel('time (s)')
plt.ylabel('distance (m)')

plt.show()
