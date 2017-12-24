
'''
Read excel file of format:
Arm_id      DSPName        DSPCode          HubCode          PinCode    PPTL
1            JaVAS            01              AGR             282001    1,2
2            JaVAS            01              AGR             282002    3,4
3            JaVAS            01              AGR             282003    5,6


'''

from xlrd import open_workbook


class Arm(object):
    def __init__(self, id, dsp_name, dsp_code, hub_code, pin_code, pptl):
        self.id = id
        self.dsp_name = dsp_name
        self.dsp_code = dsp_code
        self.hub_code = hub_code
        self.pin_code = pin_code
        self.pptl = pptl

    def __str__(self):
        return("Arm object:\n"
               "  Arm_id = {0}\n"
               "  DSPName = {1}\n"
               "  DSPCode = {2}\n"
               "  HubCode = {3}\n"
               "  PinCode = {4} \n"
               "  PPTL = {5}"
               .format(self.id, self.dsp_name, self.dsp_code,
                       self.hub_code, self.pin_code, self.pptl))

def print_sheet(items):
    for item in items:
        print("DSPName: {0}".format(item.dsp_name))
        print(item)
        print()

wb = open_workbook('/home/kiran/km/km_hadoop/data/excel_data.xls')

for sheet in wb.sheets():
    print("Reading Sheet : {}".format(sheet.name))
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(*values)
        items.append(item)
    print_sheet(items)
