import pandas as pd
#from pandas import DataFrame, read_csv
import numpy as np
'''
1.Create dataframe from data of List, Arrays, Dictionaries
2.Create dataframe from clipboard

'''
#Simple List
list=['aa', 'bb', 'cc']

listDF = pd.DataFrame(list)
#>>> type(listDF) => <class 'pandas.core.frame.DataFrame'>

#Create DF with Column header name
listDF = pd.DataFrame(list, columns=['Title'])

#using DataFrame class
from pandas import DataFrame
listDF = DataFrame(list, columns=['Title'])


#Display top 5 rows
listDF.head(5)

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
datadf2 = DataFrame.from_csv("/home/kiran/km/km_hadoop/data/data_loopback_date.tsv", sep='\t')
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
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_customers.csv", delimiter='|' )


#file = r'/home/kiran/km/km_hadoop/data/data_rtl_customers.csv'
#df = pd.read_csv(file)

#Specify columns
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_customers.csv", names=['mem_num','name','addr1','city','state'])

#or specify column after creation
df.columns = ['Mem Num','Name','Addr1','City','State']

df.columns
df.info()

#Get first or last (default=5) rows
df.head() # or df.head(3)
df.tail() # or df.tail(5)


#Specify index column
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], index_col=['c1','c2'])

#Specify null values
sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], na_values=sentinels)


#Read a column data
df.c1
df['c1'] #used if column name has spaces

df[['c1','c2']]


df.C1.head(4)
df.head(4).c1

#skip bad rows if any
df = pd.read_csv("/home/kiran/km/km_hadoop/data/test_data_2.csv", delimiter=":", warn_bad_lines=False, error_bad_lines=False)


#Read from cipboard; NEEDS some additional libraries
#clipDF = pd.read_clipboard()


#Operations:
#filter by specific data
WADF = df[df['state']=='WA' ]
WADF = df[(df['state']=='WA') & (df['city']=='Bellevue')]

WADF = df.loc[df['state']=='WA']
WADF = df.loc[(df['state']=='WA') & (df['city']=='Bellevue')]

df.where( df['state']=='WA' ) #BE AWARE: This returns NaN if not match


#data at an index
data5=df.ix[5] #returns a series


df['c1'].max()
#98.998372990400014

#Add new column / assign a value to existing column
df['NewCol1']=1

#Add/update column based on data in other columns
df['Mult23']=df['c2']*df['c3']
df['WA User'] = df['state']=='WA' #This returns True or False

df['col_num']=np.arange(1, len(df)+1)  #arange() : creates a range start index to end index (default with 0)



#Sample: Apply a function on a new column
#2,aa
#4,bb
#6,cc

#use apply
def isEven(num):
    return True if num%2==0 else False;

df = pd.DataFrame([[1,100],[2,200],[5,500]], columns=['small','big'])
df['iseven'] = df['small'].apply(isEven)

df['Mult']=df.apply(lambda x: x[0]*x[1], axis=1)

#using a function in apply()
def mult13(row):
    return row[0]*row[1]
df['Mult12']=df.apply(mult13, axis=1)


#drop column
df = df.drop('NewCol1', 1) #2nd arg is axis; 0=rows, 1=columns
#OR use inplace
df.drop('NewCol1', 1, inplace=True)

#Drop columns 3, 5 (Column count starts with 0)
df.drop(df.columns[[3,5]], axis=1, inplace=True)

#rename col
df.rename(columns={'C3': 'c3', 'Mult12': 'Mult-12'}, inplace=True)
df.columns = df.columns.str.replace('$','')

#rename using zip()
old_names = ['$a', '$b', '$c', '$d', '$e']
new_names = ['a', 'b', 'c', 'd', 'e']
df.rename(columns=dict(zip(old_names, new_names)), inplace=True)


#rename by sequence number
df2 = df.rename(columns=lambda x: x[1:])
df2 = df.rename(columns=lambda x: x.replace('$', ''))

#Save dataframe to csv
df.to_csv('/home/kiran/km/km_hadoop/data/data_2d_pandas_saved.csv')

#groupby() & apply functions
txnsdf = pd.read_csv("/home/kiran/km/km_hadoop/data/data_rtl_txns.csv")
#total qty sold by sku (group by sku)
soldSkuDF = txnsdf.groupby('sku_id')['qty'].sum()
soldSkuDF = txnsdf.groupby('sku_id').agg({'qty' : ['size','sum', 'min', 'max', 'mean', 'std']})
soldSkuDF = txnsdf.groupby(['sku_id', 'store_id']).agg({'qty' : ['sum', 'min', 'max', 'mean', 'std']})

for sku, group in soldSkuDF.groupby('sku_id'):
    print("SKU: %s" %sku)
    print(group[0])
    print("\n")

soldSkuDF = txnsdf.groupby('sku_id').agg({'qty': 'sum'}).rename(columns={'qty': 'qty_total'})
#can also call sum() as: .agg({'qty': sum})

#Adds prefix to column title
txnsdf.groupby('sku_id').agg({'qty': sum}).add_prefix('total_')



strSkuQtyDF = txnsdf.groupby(['store_id', 'sku_id'], as_index=False)['qty'].sum()

txnsdf['qty'].groupby(['store_id', 'sku_id'], as_index=False).sum()

#pivot() by store & sku
strSkuQtyDF.pivot('store_id', 'sku_id', 'qty')


#groupby() on sample
