import xlrd

book = xlrd.open_workbook('test.xlsx')

for sheet in book.sheets():
    print(sheet.name)
    for row in range(sheet.nrows):
        for col in range(sheet.ncol):
            print(sheet.cell_value(row,col))
