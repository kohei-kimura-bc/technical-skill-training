import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
ws = wb["test1"] # シートの取得
cell = ws["A1"] # A1セルの取得
value = cell.value
print(f"test1シートのAセルの値：{value}")
