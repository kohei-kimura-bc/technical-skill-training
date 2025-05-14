"""
身長と体重からBMIを計算し、健康カテゴリと健康リスクを判定するプログラムです。空欄に適切な条件を記入してください。
"""

# 身長と体重を入力
height = float(input("身長をメートルで入力してください（例: 1.75）: "))
weight = float(input("体重をkgで入力してください: "))

# BMI計算
bmi = weight / (height * height)

# BMIカテゴリ判定
if ______:  # BMIが18.5未満
    category = "低体重"
    risk = "栄養不足のリスクがあります"
elif ______:  # BMIが18.5以上25未満
    category = "普通体重"
    risk = "健康的な範囲です"
elif ______:  # BMIが25以上30未満
    category = "過体重"
    if ______:  # BMIが27.5以上
        risk = "健康リスクが増加しています"
    else:
        risk = "軽度の健康リスクがあります"
elif ______:  # BMIが30以上35未満
    category = "肥満（クラス1）"
    risk = "中程度の健康リスクがあります"
elif ______:  # BMIが35以上40未満
    category = "肥満（クラス2）"
    risk = "高度な健康リスクがあります"
else:
    category = "肥満（クラス3）"
    risk = "非常に高い健康リスクがあります"

print(f"あなたのBMIは {bmi:.1f} です")
print(f"カテゴリ: {category}")
print(f"健康評価: {risk}")
