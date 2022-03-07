import openpyxl

path = "C:/Users/waidd/Desktop/School_Stuff/CS_495/script_testing/EL_Database.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

for i in range(1, 253):
    for j in range(1,31):
        cell_obj = sheet_obj.cell(row = i, column = j)
        print(cell_obj.value, end = " ")
    print("")