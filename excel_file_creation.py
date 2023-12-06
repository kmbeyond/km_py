
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
