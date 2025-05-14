# 数値を入力
num = int(input("数値を入力してください: "))

# 数値の分類
if num > 0:
    if num % 2 == 0:
        print("正の偶数です")
    else:
        print("正の奇数です")
elif num < 0:
    if num % 2 == 0:
        print("負の偶数です")
    else:
        print("負の奇数です")
else:
    print("ゼロです")
