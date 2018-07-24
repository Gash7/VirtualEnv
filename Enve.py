import openpyxl
#file = open()
wb = openpyxl.load_workbook('D:\Python\Ash.xlsx')
sheet = wb.get_sheet_names()
wb1 = wb.get_active_sheet

print(wb)

listofrow = []

for items in listofrow:
    data =[sheet.cell_valur(items,col) for col in range(sheet.ncols)] #[sheet.cell_value(items,col) for col in range(sheet.ncols)]
    listofrow.append(data)

print(listofrow)
