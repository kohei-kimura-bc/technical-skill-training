import sys


def get_number(message, min_value):
    while True:
        try:
            num = int(input(message))
            if num < min_value:
                raise AssertionError(f"{min_value}以上の値を入力してください")
        except ValueError:
            print("入力された値は数字ではありません")
        # except KeyboardInterrupt:
        #     print("入力が中断されました")
        #     sys.exit()
        except AssertionError as e:
            print(e)
        else:
            return num


height = get_number("身長(cm)を入力してください\n", 100)
weight = get_number("体重(kg)を入力してください\n", 30)
bmi = weight / (height / 100) ** 2
print(bmi)
