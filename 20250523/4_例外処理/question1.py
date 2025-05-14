"""
ユーザに数字を入力してもらうまで入力を繰り返させるプログラムを作成してください。
数値が入力されたら、その数値を2乗した値を出力してください。
"""

while True:
    try:
        num = int(input("数値を入力してください\n"))
    except ValueError:
        print("数値を入力してください")
    else:
        print(num**2)
        break
