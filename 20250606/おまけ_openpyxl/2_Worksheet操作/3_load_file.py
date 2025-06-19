import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
ws = wb["test1"] # シートの取得
