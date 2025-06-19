import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
ws = wb["test1"] # シートの取得
ws.title = "テスト名変更" # 新しいシート名

wb.save("rename_title.xlsx") #シート名が変更されたファイルが保存される