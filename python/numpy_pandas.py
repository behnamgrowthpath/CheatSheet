
#! NumPy:
import numpy as np

# ndarray is the name of numpy n-dimensional arrays

x = np.array([1, 2, 3, 4]) 
# NumPy arrays are faster and more compact than lists. 
# this arrays can contain only a single data type

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
print(x.ndim) # 2 --> returns the number of dimensions of the array.
print(x.size) # 9 --> returns the total number of elements of the array.
print(x.shape) # (3, 3) --> returns a tuple of integers that indicate the number of elements stored along each dimension of the array. 

# each element of array should be in same type - Homogeneous
typeOfArray = x.dtype

x = np.array([2, 1, 3])
x = np.append(x, 4) # add an element
x = np.delete(x, 0) # remove at index
x = np.sort(x) # 

y = np.arange(2, 14 ,3) # (same as range() in python) allows you to create an array that contains a range of evenly spaced intervals sort the array
# y is [2, 5, 8, 11]

y = y.flatten() # same as y.reshaope(1,-1) --> change n-dimensional aray to 1-dimensional

y = y.reshape(2, 2) # this method allows us to change 1-dimensional arrays to an 2/3-dimensional or vice versa

y1 = y[: , -1] # whole last column
y2 = y[0,:] # whole first row
y = y[-3:-2] # can be sliced just like lists

x = np.arange(1, 10)
x = x[(x>5) & (x%2==0)] # x is [6, 8] # &: and, |: or
# You can provide a condition as the index to select the elements that fulfill the given condition. 

res = ((x[:]>5) & (x[:]%2==0)).sum()
# true is 1 and false is 0

# masking:
heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))
heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))
mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)
tall_presidents = height_age_arr[mask, ] # --> tall_presidents is [[183  49], [183  43], [188  46], [185  47]]
# mask only has True and False item but its is known by the creator array.
# Masking is used to extract, modify, count, or otherwise manipulate values in an array based on some criterion.

# sum(), min(), max(), mean(), median(), var()[variance], std()[standard deviation]
z = np.median(y)
rowSums = x.sum(axis=1)
rcolumnsSums = x.sum(axis=0)

verticallyAdded = np.vstack((x,y)) # rows numbers are same
horizentallyAdded = np.hstack((x,y)) # columns numbers are same # these could be happend for more than 2 arrays
verticallyAdded = np.concatenate((x,y), axis=1) # --> vstack
horizentallyAdded = np.concatenate((x,y), axis=0) # --> hstack

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))

#matrix functions:
x = np.array([[1,0],[0,1]])
y = np.array([[1,2],[3,4]])
a = np.dot(x,y)
b = x.transpose()
c = np.linalg.inv(x)
d = x.trace()
e = np.linalg.det(x)

#! Pandas:

import pandas as pd

# A Series is essentially a column, and a DataFrame is a multi-dimensional table made up of a collectiondf[(df['ages']>18) & (df['heights']>180)] of Series.
# You can think of a Series as a one-dimensional array, while a DataFrame is a multi-dimensional array.
# every dataframe has an index and multiple columns.
data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}
pd.set_option('max_rows', 10)

df = pd.DataFrame(data) # each key is a column name and value represent the array of data
#1. The DataFrame automatically creates a numeric index for each row. We can specify a custom index, when creating the DataFrame:
df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
#2. We also see that Pandas has added an auto generated index. We can set our own index column by using the set_index() function:
df.set_index('ages', inplace=True) # inplace means to save changes in this dataframe or not
# 1: to add name of indexes but 2: to change a simillar column to the index of dataframe then it wont be a serie anymore

print(df.columns)
sample = pd.DataFrame({ 'Bob': ['I liked it.', 'It was awful.'], 
                        'Sue': ['Pretty good.', 'Bland.']},
                        index=['Product A', 'Product B'])

# When selecting a single column from a Pandas DataFrame, we use single square brackets. When selecting multiple columns, we use double square brackets.
sample = df[['ages','heghts']]
is_tall = df['heights'] >= 180
elementsNumber = df.size # like np
dimension = df.shape[0] # like np --> num of rows
dimension = df.shape[1] # like np --> num of columns

#The values attribute of a Pandas Series give the data as a numpy array.
# np.array([[14,165], [18,180], [24,176], [42,184]]) === df['ages','heights'].values

# A Pandas Series is a single column from a Pandas DataFrame.
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s = pd.Series({'a': 1, 'b': 2, 'c':3})
s = pd.Series(np.array([1, 2, 3])) #indexes form 0 to n-1
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


someRow = df.loc['amy':'Bob'] # accessing to special rows from a to b
# we can use a conditional statement with loc[] or we can use a boolean array
someRows = df.iloc[1:-1] # just for numeric index

df['ages'].head(n=3) # accessing to special series (1 or more)
someColumn = df.loc[:,'heights']
df['index_backwards'] = range(len(df), 0, -1)

specialPerson = df[(df['ages']>18) & (df['heights']>180)] # condition with & and | 

readingFile = pd.read_csv("fileName.csv", index_col= 0) # or False to force pandas for generating the index by itself
readingFile = pd.read_csv("fileName.csv", index_col='indexColumn') # Pandas also supports reading from JSON files, as well as SQL databases
'''for kaggle competitions:
output = pd.DataFrame({ 'Id': X.Id,
                        'outputPrediction': model.predict(y)})
output.to_csv('submission.csv', index=False)'''

firstRows = readingFile.head(n=10) # return 'n' first rows of a dataframe
lastRows = readingFile.tail(n=9) # return 'n' last rows of a dataframe

#? df.column1.isin(['1', '2'])
#? df.column2.isnull()
#? df.column3.notnull()

# The info() function is used to get essential information about your dataset, such as number of rows, columns, data types, etc:
df.info()

# dropna drops missing values (think of na as "not available")
filtered = df.dropna(axis=0)

df.drop(24, axis=0, inplace=True) 
# drop() deletes rows and columns.
# axis=1 specifies that we want to drop a column.
# axis=0 will drop a row. """

df['date'] = [2701.20, 2802.20, 3103.20] # adding new column
df['month'] = pd.to_datetime(df['date'], format="%d%m.%y").dt.month_name() # two usefull function about date

countMeanStdMin255075Max = df.describe() # return usefull information for numeric columns also nan-value ones
df['height'].describe() # We can also get the summary stats for a single column

# for numerical features:
dividedInRange = df['heghits'].quantile([0.25, 0.5, 0.75, 1]) # return 4 answer like box plot
# we also have sunm(), mean(), median(), std(), min(), max() and ext.

no_duplocated = df.month.unique()
# for categorial features
repeats = df['month'].value_counts() # it shows that each item of 'month' column repeated how many times.
each_duplicate = df.month.value_counts()
# we can also use this code:
repeats = df.groupby('month').month.count()

grouped = df.groupby('month')['height'].max() # shows the maximum height of each month
grouped = df.groupby('party')['height'].agg([min, np.median, max]) # lets you run a bunch of different functions on your DataFrame simultaneously
grouped = df.groupby('party').agg({'height':[np.median, np.mean], 'age':[min, max]})

reviewed = df.groupby(['month', 'ages']).height.agg([len])
# if we use different columns for groupby, we have a multiindexes in pandas. so we can use this code to convert the data:
grouped.reset_index()

function_for_column_values = df.age.map(lambda f : f+1)
def f():
    pass
function_for_column_values = df.age.apply(f ,axis='columns')
'''
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')
'''
'''
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
'''

best_growth_ratio = (df.height / df.ages).idxmax()

sorted_data = reviewed.sort_values(by=['month', 'ages'] , ascending=False)# you can ignore by=
sorted_data = reviewed.sort_index() # sorted by index

decemberCases = df[df['month']==12]['cases', 'deaths']

a = df.ages.dtype
b = df.dtypes
c = df.height.astype('float64')
d = df.index.dtype

missing_values = df[pd.isnull(df.date)]
df.date.fillna("Unknown") # fillna() provides a few different strategies for mitigating such data.
df.month.replace("december", "last_month")

df.rename(columns={'date': 'tarikh'} ,index={0: 'firstEntry', 1: 'secondEntry'})
df.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

#* combining two dataframe or serie:
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
pd.concat([canadian_youtube, british_youtube])
# This is useful when we have data in different DataFrame or Series objects but having the same fields (columns)
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')
# this lets you combine different DataFrame objects which have an index in common

