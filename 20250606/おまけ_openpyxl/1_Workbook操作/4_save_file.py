import openpyxl
wb = openpyxl.load_workbook("test.xlsx")

wb.save("out.xlsx") # Excelファイルの保存
