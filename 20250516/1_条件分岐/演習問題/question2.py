"""
点数と出席率に基づいて成績を評価するプログラムです。空欄に適切な条件を記入してください。

"""

# 点数と出席率を入力
score = int(input("テストの点数（0-100）を入力してください: "))
attendance = int(input("出席率（0-100）を入力してください: "))

if ______:  # 点数が90以上かつ出席率が80%以上
    grade = "A"
elif ______:  # 点数が80以上90未満かつ出席率が70%以上
    grade = "B"
elif ______:  # 点数が70以上80未満または出席率が90%以上
    grade = "C"
elif ______:  # 点数が60以上70未満かつ出席率が60%以上
    grade = "D"
else:
    grade = "F"

print(f"あなたの成績は {grade} です")
