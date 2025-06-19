import openpyxl
wb = openpyxl.load_workbook("test.xlsx") # Excelファイルの読み込み
sheet_names = wb.sheetnames # シート名一覧取得
print(sheet_names)
