---------Write Pandas dataframe to Excel
#--using ANY of these 2 engines
#python pip install xlsxwriter
#python pip install openpyxl

import pandas as pd
data = [(1, 'aa', '2020-01-01'), (2, 'bb', '2021-01-01'), (3, 'cc', '2021-12-01')]
dataDF = pd.DataFrame(data, columns=['id', 'name', 'login_date'])

import xlsxwriter
dataDF.to_excel('C:\km\km_test_xlsxwriter2.xlsx', 'report', engine='xlsxwriter', index=False)

import openpyxl
dataDF.to_excel('C:\km\km_test_openpyxl2.xlsx', 'report', engine='openpyxl', index=False)


#--using pandas excelwriter : REQUIRES any of above engines
from pandas.io.excel._base import ExcelWriter
writer = pd.ExcelWriter('C:\km\km_test_xlsxwriter2.xlsx', engine='xlsxwriter')
dataDF.to_excel(writer, sheet_name='Sheet1')
writer.close()
