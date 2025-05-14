"""
学生のテスト点数や出席率などから成績を判定するシステムです。空欄に適切な条件を記入してください。
"""

# 学生の情報を入力
score_midterm = int(input("中間テストの点数（0-100）を入力: "))
score_final = int(input("期末テストの点数（0-100）を入力: "))
homework_completed = int(input("提出した宿題の数（0-10）を入力: "))
attendance_rate = int(input("出席率（0-100）を入力: "))
extra_credit = (
    input("特別課題を提出しましたか？(yes/no): ").lower() == "yes"
)  # lower()は全ての文字を小文字に変更する関数

# 合否判定の初期値
passed = False
grade = "F"


avg_score = (score_midterm + score_final) / 2


# 基本条件（中間・期末の平均が60以上かつ宿題が7つ以上かつ出席率が80%以上）を満たす
if ______:
    passed = True

    # 成績判定
    if ______:  # 平均90以上かつ宿題10個かつ出席率95%以上
        grade = "A+"
    elif ______:  # 平均90以上
        grade = "A"
    elif ______:  # 平均80以上
        grade = "B"
    elif ______:  # 平均70以上
        grade = "C"
    else:
        grade = "D"
else:
    # 救済条件：特別課題を提出していて、他の条件が少し足りない場合
    if extra_credit and ______:  # 平均が55以上かつ宿題が6つ以上かつ出席率が75%以上
        passed = True
        grade = "D"

# 結果表示
if passed:
    print(f"合格です。成績: {grade}")
else:
    print("不合格です。再履修が必要です。")
