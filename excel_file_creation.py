
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





'''
Read excel file of format:
Arm_id      DSPName        DSPCode          HubCode          PinCode    PPTL
1            JaVAS            01              AGR             282001    1,2
2            JaVAS            01              AGR             282002    3,4
3            JaVAS            01              AGR             282003    5,6


'''
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('/home/kiran/km/km_hadoop/data/excel_data2.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()
