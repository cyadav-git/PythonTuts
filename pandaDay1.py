import pandas as pd
import numpy as np

#created a series with random numbers
s = pd.Series(np.random.randn(4))
print("Is the object empty?")
print(s.empty)
#s = pd.Series()
#print(s.empty)
print(s)
print(s.ndim)
print("the dimension of the object:")
#create a dictionary of series
d = {'Name':pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
     'Age':pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating':pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
#create a dataframe
df = pd.DataFrame(d)
print("our data series is: ")
print(df)
print(df.shape)
#tranpose the above series dictionary
print("the transpose of the given table")
print(df.T)
#print(df.shape)
#total number of size
print("the size of the series")
print(df.size)
print("display the data from head or from top ")
print(df.head(7))
print("display the data from the tail or bottom")
print(df.tail(4))
#sum the data in the series
print(df.sum())
#used to mean the series
print(df.mean())
#describe the series
print(df.describe(include='all'))
#sort the elements in the series in descending
print(df.sort_index(ascending=False, axis=1))
#sort the elements in the series with name format
print(df.sort_values(by='Name', ascending=True))