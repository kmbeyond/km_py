
---------Write Pandas dataframe to Excel
--using any of these 2 engines
pip install openpyxl
pip install xlsxwriter

import xlsxwriter
import pandas as pd
data = [(1, 'aa', '2020-01-01'), (2, 'bb', '2021-01-01'), (3, 'cc', '2021-12-01')]
dataDF = pd.DataFrame(data, columns=['id', 'name', 'login_date'])
dataDF.to_excel('C:\km\km_test_xlsxwriter.xlsx', 'report', engine='xlsxwriter', index=False)

--using pandas excelwriter
from pandas.io.excel._base import ExcelWriter
writer = pd.ExcelWriter('C:\km\km_test_xlsxwriter2.xlsx', engine='xlsxwriter')
dataDF.to_excel(writer, sheet_name='Sheet1')
writer.close()

