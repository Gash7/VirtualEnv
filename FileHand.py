'''

import openpyxl
wb = openpyxl.load_workbook('C:\\Users\AMIT_GORE\Desktop\Ash.xlsx')
print(type(wb))
sheet = wb.get_sheet_by_name(sheet1)
c = 'sheet['A1']
print(c)

'''
try:
    file = open(r'C:\Users\AMIT_GORE\Desktop')
except FileNotFoundError:
    print('File Not Found')
else:
    print('Please Enter Correct File')
finally:
    print('Must Print')