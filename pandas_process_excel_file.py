
'''
Read excel file of format:
Arm_id      DSPName        DSPCode          HubCode          PinCode    PPTL
1            JaVAS            01              AGR             282001    1,2
2            JaVAS            01              AGR             282002    3,4
3            JaVAS            01              AGR             282003    5,6


'''


import pandas
df = pandas.read_excel('/home/kiran/km/km_hadoop/data/excel_data.xls')

#print the column names
print(df.columns)

#get the values for a given column into array
values = df['Arm_id'].values

#get a dataframe with selected columns
FORMAT = ['Arm_id', 'DSPName', 'PinCode']
df_selected = df[FORMAT]

df_selected.head(5)




#-----------------------Write to excel-------------
import pandas as pd

# Create a Pandas Excel writer using XlsxWriter as the engine.
fileName="/home/kiran/km/km_hadoop/data/excel_data_cr_pandas.xls"
writer = pd.ExcelWriter(fileName, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_selected.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
