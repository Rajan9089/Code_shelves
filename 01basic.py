import pandas as pd;
import numpy as np;
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(type(iris))
print(iris)


df = iris.copy()      #shallow copy .. I think
# df me changes hoga usse iris pe koi fark ni padega



print(iris.head())
print()
print(df.head())


df.head(3)  #by default uper se 5 row show karega hai


df.tail()     #by default niche se 5 row show karega hai


print(iris.columns)
print(df.columns)


print(df.shape)    # 149 rows and 5 columns
print(iris.dtypes,'\n')
print(df.dtypes)


df.columns = ['sl' , 'sw' , 'pl' , 'pw' , 'flower_types']

df.describe()


df.sl    #df.column_name to acces data of particuar column
# df["sl"]      # another way


# df.isnull()      # it shows that there is no any null
df.isnull().sum()       # how many null entry we have in each columns


# iloc works on postion(index)
df.iloc[1:4 , 2:4]        # row [1 to 3] and col [2 to 3] to acces data of some row and some column
# df.[1:4 , 2:4] # can not directly do this


df.iloc[0]      #to acces data of particuar row


df.head()

# Manipulation of data in pandas
# df.drop(0)    # it makes a copy in which only data changes
# a = df.drop(0)
# a.head()         # it works fine

df.drop(0 , inplace = True)    #bydefault inplace is false .. we are saying remove the row which has (label) 0 not the 0th index(or position)
df.head()


df.drop(3 , inplace = True)    # we are saying remove the row which has (label) 3 not the 3rd index(or position)
df.head()           #here 3rd labeled row is removed


df.index          # label 0 and 3 are removed as shown below


# df.index[0]        # label of the 0th row
# df.index[2]        # label of the 3th row
df.index[0] , df.index[3]


#if you want to drop w.r.t postion instead of label
df.drop(df.index[0] , inplace=True)
df.head()


#if you want to drop first two row postion instead of label
df.drop(df.index[[0 , 1]] , inplace=True)
df.head()


df.sl > 5

df[df.sl > 5]  #here df.sl > 5 gives boolean value


df[df.flower_types == 'Iris-setosa']


df[df.flower_types == 'Iris-setosa'].describe()


# Add a row
#assuming there is no any 0 labeled row
df.loc[0] = [1 , 2, 3, 4, 'Iris-setosa']


# df.head()  # it doesn't show new added row
print(df.tail() , '\n')     # it shows new added row
df.loc[149] = [1 , 2, 3, 4, 'Iris-setosa']
print(df.tail())


print(df.index)           # it looks little weard like some are present some are not


# iloc vs loc
print(df.head())
print(df.iloc[0])    # oth position row
# print(df.loc[0])    # loc is labeled based so it will give error since we don't have 0 indexed row here
print(df.loc[8])



print(df.reset_index() , '\n\n')    # problem that it a new columns as index
print(df.reset_index(drop = True ))   # Above problem solved


df.reset_index(drop = True , inplace = True)  #on print it shows NONE
print(df.index)


# Remove a Column
# df.drop('sl')   gives error
df.drop('sl' , axis = 1 , inplace = True) # have to make inplace to make changes in df
df.head()

df.describe()


del df['sw']   # Another way deleting a column

print(df.describe())  # can't describe string type
df.head()



# Let's get all my data back
df = iris.copy()
df.columns = ['sl' , 'sw' , 'pl' , 'pw' , 'flower_types']
# df.describe()
df.tail()



# Add a new column
# column_name = 'diff_pl_pw' whuch is actually difference of 'pl' and 'pw'
df['diff_pl_pw'] = df['pl'] - df['pw']
df.tail()
# Add one more column ... names abc having only 1 as data
df['abc'] = 1;
df.head()



# How to deal with  'NaN' entries
# df.iloc[2:4 , 1:3] = 0
df.iloc[2:4 , 1:3] = np.nan
df.head()


df.describe()


df.dropna(inplace = True)



print(df.head())
df.reset_index(drop = True , inplace=True)
df.head()



# how to put other value in place of 'NaN'
# At first again put NaN Values
df.iloc[2:4 , 1:3] = np.nan
df.head()




# how to put other value(mean of sw) in place of 'NaN' in column names 'sw'
df.sw.fillna(df.sw.mean() , inplace= True)
df.pl.fillna(df.pl.mean() , inplace = True)
df.head()



# Handling String in panda dataframe
#let's add few column
df['Gender'] = 'Female'
df.iloc[0:5 , 7] = "Male"  # row [0,4] and col = [7] ... entries will be containing 'Male '
df.head(10)



# most of the cases we will be converting string to numeric value for easy calculation
def f(s):
    if s == 'Male':
        return 0
    else:
        return 1
df['sex'] = df.Gender.apply(f )   # we have new entry 'sex' having corresponding numeric value w.r.t 'Gender'
df.head(10)



del df['Gender']     # after converting string to numeric we deleted 'Gender' column



print(df.head(10))      # first 10 row
















