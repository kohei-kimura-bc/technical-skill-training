"""
点数と出席率に基づいて成績を評価するプログラムです。空欄に適切な条件を記入してください。

"""

score = int(input("テストの点数（0-100）を入力してください: "))
attendance = int(input("出席率（0-100）を入力してください: "))

if score >= 90 and attendance >= 80:
    grade = "A"
elif score >= 80 and score < 90 and attendance >= 70:
    grade = "B"
elif (score >= 70 and score < 80) or attendance >= 90:
    grade = "C"
elif score >= 60 and score < 70 and attendance >= 60:
    grade = "D"
else:
    grade = "F"
