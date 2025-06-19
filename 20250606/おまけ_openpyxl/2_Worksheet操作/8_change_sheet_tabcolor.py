import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
ws = wb["test1"] # シートの取得
ws.sheet_properties.tabColor = "FF8C00" # シートの色設定

wb.save("change_sheet_tabcolor.xlsx")