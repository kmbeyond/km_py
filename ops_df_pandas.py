import pandas as pd
#from pandas import DataFrame, read_csv
import numpy as np

'''
1.Create dataframe from data of List, Arrays, Dictionaries
2.Create dataframe from clipboard

'''


#Simple List
list=['aa', 'bb', 'cc']

#Create DF
listDF = pd.DataFrame(list)
#>>> type(listDF) => <class 'pandas.core.frame.DataFrame'>

#with Column header name
listDF = pd.DataFrame(list, columns=['Title'])

#using DataFrame class directly
from pandas import DataFrame
listDF = DataFrame(list, columns=['Title'])
#OR using an alias
#from pandas import DataFrame as df
#listDF = df(list, columns=['Title'])

#Display top 5 rows
listDF.head(5)

numbersDF1 = pd.DataFrame(np.arange(16).reshape(4,4))
numbersDF1.head()

#DF from 2D matrix
dfeven = pd.DataFrame([[1,100],[2,200],[5,500]], columns=['small','big'])
dfeven.head()

#From Dictionary object: uses Key for column name
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}

type(raw_data)
#<class 'dict'>
df = pd.DataFrame(raw_data)

from pandas import DataFrame
rndDF = DataFrame({ 'k1': ['X', 'X', 'Y', 'Y', 'Z'],
    'k2':['alpha','beta','alpha','beta','alpha'],
    'dataset1':np.random.randint(5, size=5),
    'dataset2':np.random.randint(5, size=5)})

#----------------------Read from file-------------------------------
#2 ways:
#****1: using pd
datadf = pd.read_csv("/home/kiran/km/km_hadoop/data/data_loopback_date.tsv", delimiter='\t', header=0)
#Other options while file read
#header=None #by default first row as header
#delimiter='|' or '\t' : default delimiter is ','
#skipfooter=3 #Skips last 3 rows
#engine="python" #default engine
#na_values=['.']  #Specify what to use for null value

datadf.head(5)

#   userId               createDate  grade
#0       0  2016-05-08 22:00:49.673      2
#1       0  2016-07-23 12:37:11.570      7
#2       0  2017-01-03 12:05:33.060      7
#3    1009  2016-06-27 09:28:19.677      5
#4    1009  2016-07-23 12:37:11.570      8

#****2: using DataFrame class
datadf2 = DataFrame.from_csv("/home/kiran/km/km_hadoop/data/data_loopback_date.tsv", sep='\t') #from_csv() is deprecated
#Creates dataframe the default index with first column
datadf2.head(5)
#                     createDate  grade
#userId
#0       2016-05-08 22:00:49.673      2
#0       2016-07-23 12:37:11.570      7
#0       2017-01-03 12:05:33.060      7
#1009    2016-06-27 09:28:19.677      5
#1009    2016-07-23 12:37:11.570      8

#reset the default index
datadf2.reset_index()

#Sample data
#mem_num|name|addr1|city|state
#1345671|Kerry Johnson|123 Mains St.|Bellevue|WA
#1230504|Liliana Strauss|23000 Indian Rd.|Pasadena|CA
#
dfcust = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_customers.csv", delimiter='|' )


#file = r'/home/kiran/km/km_hadoop/data/data_rtl_customers.csv'
#df = pd.read_csv(file)

#Specify columns
dfcust = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_customers.csv", delimiter='|', names=['mem_num','name','addr1','city','state'])

#or specify column after creation
#df.columns = ['Mem Num','Name','Addr1','City','State']
dfcust.columns = ['mem_num','name','addr1','city','state']

dfcust.columns
dfcust.info()

#Get first or last (default=5) rows
dfcust.head() # or df.head(3)
dfcust.tail() # or df.tail(5)


#Specify index column
df2 = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], index_col=['c1','c2'])

#Specify null values
sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
df2 = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], na_values=sentinels)


#Read a column data
df2.c1
df2['c1'] #used if column name has spaces

df2[['c1','c2']]


df2.c1.head(4)
df2.head(4).c1

#skip bad rows if any
df3 = pd.read_csv("/home/kiran/km/km_hadoop/data/test_data_2.csv", delimiter=":", warn_bad_lines=False, error_bad_lines=False)


#Read from cipboard; NEEDS some additional libraries
#clipDF = pd.read_clipboard()


#Operations:
#filter by specific data
WADF = dfcust[ dfcust['state']=='WA' ]
WADF = dfcust[(dfcust['state']=='WA') & (dfcust['city']=='Bellevue')]

WADF = dfcust.loc[ dfcust['state']=='WA']
WADF = dfcust.loc[ (dfcust['state']=='WA') & (dfcust['city']=='Bellevue')]

dfcust.where( dfcust['state']=='WA' ) #BE AWARE: This returns NaN if not match


#data at an index
data5=dfcust.ix[5] #returns a series


df2['c1'].max()
#98.998372990400014

#Add new column / assign a value to existing column
df2['NewCol1']=1
df2['NewCol2']=2
df2['NewCol3']=3
#Add/update column based on data in other columns
df2['Mult23']=df2['c2']*df2['c3']
dfcust['WA User'] = dfcust['state']=='WA' #This returns True or False

df2['col_num']=np.arange(1, len(df2)+1)  #arange() : creates a range start index to end index (default with 0)



#Sample: Apply a function on a new column
#2,aa
#4,bb
#6,cc

#use apply
def isEven(num):
    return True if num%2==0 else False;


dfeven['iseven'] = dfeven['small'].apply(isEven)

dfeven['Mult']=dfeven.apply(lambda x: x[0]*x[1], axis=1)

#using a function in apply()
def mult13(row):
    return row[0]*row[1]
dfeven['Mult12']=dfeven.apply(mult13, axis=1)

#Find matching records from 2 dataframes
dfnum1 = pd.DataFrame([[1,100],[2,200],[5,500]], columns=['small','big'])
dfnum2 = pd.DataFrame([[3,300],[5,500],[6,600]], columns=['small','big'])

pd.merge(dfnum1, dfnum2, how='inner', on=['small'] )
#   small  big_x  big_y
#0      5    500    500

#drop column
#df2 = df.drop('NewCol1', 1) #2nd arg is axis; 0=rows, 1=columns
#OR use inplace
df2.drop('NewCol1', 1, inplace=True)

#Drop columns 3, 5 (Column count starts with 0)
df2.drop(df2.columns[[3,5]], axis=1, inplace=True)

#rename col
df2.rename(columns={'c3': 'c3', 'Mult12': 'Mult-12'}, inplace=True)
df2.columns = df2.columns.str.replace('$','')

#rename using zip()
old_names = ['$a', '$b', '$c', '$d', '$e']
new_names = ['a', 'b', 'c', 'd', 'e']
df2.rename(columns=dict(zip(old_names, new_names)), inplace=True)


#rename by sequence number
df2 = df2.rename(columns=lambda x: x[1:])
df2 = df2.rename(columns=lambda x: x.replace('$', ''))

#Save dataframe to csv
df.to_csv('/home/kiran/km/km_hadoop/data/data_2d_pandas_saved.csv')

print("--------------groupby--------------")
#groupby() & apply functions
txnsdf = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_txns.csv")
#total qty sold by sku (group by sku)
soldSkuDF = txnsdf.groupby('sku_id')['qty'].sum()
soldSkuDF = txnsdf.groupby('sku_id').agg({'qty' : ['size','sum', 'min', 'max', 'mean', 'std']})
soldSkuDF = txnsdf.groupby(['sku_id', 'store_id']).agg({'qty' : ['sum', 'min', 'max', 'mean', 'std']})

for sku, group in soldSkuDF.groupby('sku_id'):
    print("SKU: %s" %sku)
    print(group)
    print("\n")

soldSkuDF = txnsdf.groupby('sku_id').agg({'qty': 'sum'}).rename(columns={'qty': 'qty_total'})
#can also call sum() as: .agg({'qty': sum})

#Adds prefix to column title
txnsdf.groupby('sku_id').agg({'qty': sum}).add_prefix('total_')



strSkuQtyDF = txnsdf.groupby(['store_id', 'sku_id'], as_index=False)['qty'].sum()


#pivot() by store & sku
print("--------------Pivot--------------")
dfpivot = strSkuQtyDF.pivot('store_id', 'sku_id', 'qty')
dfpivot.head(5)

#groupby() on sample
