# -*- coding: utf-8 -*-

#In the following example, we construct a NeighborsClassifier class from an array representing our data set and ask who’s the closest point to [1,1,1]. 

#It returns [[0.5]], and [[2]], which means that the element is at distance 0.5 and is the third element of samples (indexes start at 0). 

#The next example is: http://scikit-learn.org/stable/modules/generated/#sklearn.neighbors.KNeighborsClassifier.html



from sklearn.neighbors import  NearestNeighbors

samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]

neigh = NearestNeighbors(n_neighbors=1)

neigh.fit(samples) 

print(neigh.kneighbors([[0.1, 0.1, 0.1]])) 

