import xlrd
import csv
#make sure that the file extention is correct. It is either xls or xlss or something
with xlrd.open_workbook('new.xlsx') as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open('spread.csv', 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))
        f.close()

#replace commas with spaces after this







