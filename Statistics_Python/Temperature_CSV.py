# This example opens a CSV file and calculates the statistics of the data coming from a temperature sensor. Then, the data coming from sensor will be graphicated

import pandas
import numpy as np
import matplotlib.pyplot as plt

file_name = 'Temperature.csv'

data_temp = pandas.read_csv(file_name) # Read CSV (comma-separated) file into DataFrame

array = data_temp.values # The dtype will be a lower-common-denominator dtype

# separate array in X and Y

X = array[:,0]   # Time
Y = array[:,2]   # Temperature

day = []
hour = []

for n in range(0,len(X)):
    day.append(" ")
    hour.append(" ")

for n in range(0,len(X),20):
    day[n] = array[n,0].split(" ")[0]
    hour[n] = array[n,0].split(" ")[1]

mean_temperature = np.mean(Y)
var_temperature = np.var(Y)

print "The average mean of temperature is:", mean_temperature
print "The variance of temperature is:", var_temperature


plt.plot(X,Y)

plt.title('Temperature vs Time')

#plt.xticks(X, hour, rotation='vertical')

plt.xticks(X, hour)

plt.xlabel('Tiempo [s]')

plt.ylabel('Temperature [C]')

plt.show()



