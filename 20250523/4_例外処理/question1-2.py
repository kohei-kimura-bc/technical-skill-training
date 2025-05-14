"""
発展問題
演習問題①のコードを再利用し、
ユーザに身長と体重を入力させた後、BMIを計算するプログラムを作成してください
"""


def get_number(message="数字を入力してください\n"):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print("入力された値は数字ではありません")
        else:
            return num


height = get_number("身長(cm)を入力してください\n")
weight = get_number("体重(kg)を入力してください\n")
print(weight / (height / 100) ** 2)
