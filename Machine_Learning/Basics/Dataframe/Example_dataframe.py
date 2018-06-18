# This is an example of Dataframe

import numpy
import pandas

my_datas = numpy.array([[32, 20, 'None', 23, 45],[7, 9, 'None',20, 90]])

row_names = ['Payment', 'Debit']

col_names = ['Thuesday', 'Wensday','Thursday','Friday','Saturday']

my_DataFrame = pandas.DataFrame(my_datas, index=row_names, columns=col_names)

print(my_DataFrame)



