import openpyxl


file = openpyxl.load_workbook('D:\Python\Ash.xlsx')
data = file.sheetnames
print(data)

for line in file:
    print('Line Print', line)
print('file.get_active_sheet',file.get_active_sheet)
print('file.read_only',file.read_only)
