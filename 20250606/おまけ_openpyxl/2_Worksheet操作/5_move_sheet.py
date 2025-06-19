import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
wb.move_sheet("test1", offset=1) # シートの移動

wb.save("move_sheet.xlsx") #「test1」sheetが右に移動したファイルが保存される