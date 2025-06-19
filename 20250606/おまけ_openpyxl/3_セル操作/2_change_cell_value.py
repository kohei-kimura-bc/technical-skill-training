import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
ws = wb["test1"] # シートの取得
cell = ws["A1"] # A1セルの取得
cell.value = "識別番号"
print(f"test1シートのAセルの値：{cell.value}")

wb.save("change_cell_value.xlsx") #test1シートのA1セルの値が「識別番号」に更新されたファイルが保存される