import pandas as pd
import numpy as np

dict1 = {
    "name":["Manish Panwar", "Harry", "Ritika", "Gunjan"],
    "marks":[95, 92, 92, 89],
    "city":["Delhi", "Rampur", "Bhiwani", "Meerut"]
}

df = pd.DataFrame(dict1)
print(df)
#df.to_csv('Trains.csv')
print(df.head(2))
print(df.tail(2))
print(df.describe())

mannu = pd.read_csv('Trains.csv')
print(mannu)

mannu['Speed'][0] = 22
print(mannu)

mannu.index = ['first', 'second', 'third', 'fourth']
print(mannu)

ser = pd.Series(np.random.rand(34))
print(type(ser))
print(ser)

newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
print(newdf)
newdf[0][0] = 'Mannu'
print(newdf.head())
print(type(newdf))
print(newdf.dtypes)
print(newdf.describe())
print(newdf.index)
print(newdf.columns)
print(newdf.to_numpy())
print(newdf.sort_index(axis=0, ascending=False))
print(type(newdf[0]))

newdf2 = newdf #New copy won`t be created
#new copy will created in the following cases
newdf2 = newdf[:]
newdf2 = newdf.copy()
print(newdf2)
newdf.loc[0,0] = '654'
print(newdf.head())

newdf.columns = list('ABCDE')
print(newdf.head(2))
newdf.loc[0,'A'] = 666
print(newdf.head(2))

newdf.loc[0,0] = 666 # will create a new column 0 at the end and will fill all the values as NaN except 666
print(newdf.head(2))
newdf = newdf.drop(0, axis = 1)
print(newdf.head(2))

print(newdf.loc[[1,2], ['C', 'D']])
print(newdf.loc[:, ['C', 'D']])         #all rows, C and D columns
print(newdf.loc[[1,2], :])              #all columns, 1,2 rows

print(newdf.loc[(newdf['A'] < 0.3) & (newdf['C'] > 0.1)])

print(newdf.iloc[0,4])
print(newdf.iloc[[0,1], [1,2]])

newdf.reset_index(drop=True, inplace=True)
print(newdf.head(3))

print(newdf['B'].isnull())

newdf.loc[:, ['B']] = None
print(newdf['B'].isnull())

print(newdf.dropna(how='all')) 

print(newdf.drop_duplicates(subset=['A'], keep=False))

print(newdf.info())
print(newdf['B'].value_counts(dropna=True))