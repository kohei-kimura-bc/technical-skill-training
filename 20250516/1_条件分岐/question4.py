"""
月と日から季節を判定するプログラムです。空欄を埋めて完成させてください。
"""

month = int(input("月を入力してください（1-12）: "))
day = int(input("日を入力してください: "))

# 季節の判定
if (
    (month == 3 and day >= 20)
    or (month == 4 or month == 5)
    or (month == 6 and day <= 20)
):
    season = "春"
elif (
    (month == 6 and day >= 21)
    or (month == 7 or month == 8)
    or (month == 9 and day <= 21)
):
    season = "夏"
elif (
    (month == 9 and day >= 22)
    or (month == 10 or month == 11)
    or (month == 12 and day <= 20)
):
    season = "秋"
else:  # 12月21日から3月19日まで
    season = "冬"

print(f"{month}月{day}日の季節は{season}です")
