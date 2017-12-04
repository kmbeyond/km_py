import pandas as pd
#from pandas import DataFrame, read_csv


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df

#From file
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", engine="python", header=None )
#Other options while file read
#header=None #by default first row as header
#skipfooter=3 #Skips last 3 rows
#na_values=['.']  #Specify what to use for null value

#file = r'highscore.csv'
#df = pd.read_csv(file)

#Specify columns
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", engine="python", header=None, names=['c1', 'c2', 'c3'])

#or specify after creation
df.columns = ['A1', 'A2', 'A3']

df.columns
df.info()

#Get first (default=5) rows
df.head()
df.head(10)
df.tail()

#Specify index column
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], index_col=['c1','c2'])

#Specify null values
sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_2d.csv", names=['c1', 'c2', 'c3'], na_values=sentinels)


#Read a column data
df.c1
df['c1']

df.C1.head(4)
df.head(4).c1

#skip bad rows if any
df = pd.read_csv("/home/kiran/km/km_hadoop/data/test_data_2.csv", delimiter=":", warn_bad_lines=False, error_bad_lines=False)


#Operations:
df['c1'].max()
#98.998372990400014

#Add new column
df['NewCol1']=1
df['Mult23']=df['c2']*df['c3']

#Sample: Apply a login on a new column
#2,aa
#4,bb
#6,cc
df = pd.read_csv("/home/kiran/km/km_hadoop/data/data_txns_cust.csv")

#use apply
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
