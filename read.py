from openpyxl import workbook
import time

book = workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43

now = time.strftime('%x')
sheet['A3'] = now

book.save('Ashu.xlsx')