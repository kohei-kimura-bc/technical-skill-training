"""
1~100までの数字を出力するプログラムを作成してください
ただし、3の倍数の時はFizz
5の倍数の時はBuzz
15の倍数の時はFizzBuzzと出力するようにしてください
"""

for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print("FizzBuzz")
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)
